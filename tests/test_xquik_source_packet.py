import argparse
import io
import stat
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse

from scripts.xquik_source_packet import (
    XquikSourceError,
    build_request,
    fetch_search_page,
    marketing_sources,
    render_packet,
    result_limit,
    write_packet,
)


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, _exception_type, _exception, _traceback):
        self.close()


class XquikSourcePacketTests(unittest.TestCase):
    def setUp(self):
        self.tweet = {
            "id": "1893456789012345678",
            "text": "Customers want a faster setup.",
            "createdAt": "2026-08-28T09:30:00.000Z",
            "url": "https://x.com/example_user/status/1893456789012345678",
            "likeCount": 42,
            "retweetCount": 7,
            "replyCount": 3,
            "quoteCount": 2,
            "viewCount": 900,
            "author": {"username": "example_user", "followers": 1200},
        }

    def test_result_limit_enforces_review_bound(self):
        self.assertEqual(result_limit("1"), 1)
        self.assertEqual(result_limit("100"), 100)
        with self.assertRaises(argparse.ArgumentTypeError):
            result_limit("0")
        with self.assertRaises(argparse.ArgumentTypeError):
            result_limit("101")

    def test_build_request_keeps_api_key_out_of_url(self):
        request = build_request("product launch", 25, "Top", "secret-key")
        query = parse_qs(urlparse(request.full_url).query)

        self.assertEqual(query, {"q": ["product launch"], "limit": ["25"], "queryType": ["Top"]})
        self.assertEqual(request.headers["X-api-key"], "secret-key")
        self.assertNotIn("secret-key", request.full_url)

    def test_fetch_search_page_uses_timeout_and_validates_envelope(self):
        calls = []

        def open_url(request, timeout):
            calls.append((request, timeout))
            return FakeResponse(b'{"tweets": [], "has_next_page": false}')

        payload = fetch_search_page("launch", 10, "Latest", "key", open_url)

        self.assertEqual(payload["tweets"], [])
        self.assertEqual(calls[0][1], 30)

        def invalid_response(_request, timeout):
            self.assertEqual(timeout, 30)
            return FakeResponse(b'{"data": []}')

        with self.assertRaisesRegex(XquikSourceError, "unexpected search response"):
            fetch_search_page("launch", 10, "Latest", "key", invalid_response)

    def test_fetch_errors_do_not_include_response_or_credentials(self):
        def http_error(_request, timeout):
            self.assertEqual(timeout, 30)
            raise HTTPError(
                "https://xquik.com",
                401,
                "Unauthorized",
                {},
                io.BytesIO(b'{"detail":"private response"}'),
            )

        with self.assertRaises(XquikSourceError) as raised:
            fetch_search_page("launch", 10, "Latest", "secret-key", http_error)

        self.assertEqual(
            str(raised.exception),
            "Xquik request failed with HTTP 401. Check access and try again.",
        )
        self.assertNotIn("private response", str(raised.exception))
        self.assertNotIn("secret-key", str(raised.exception))

        def network_error(_request, timeout):
            self.assertEqual(timeout, 30)
            raise URLError("sensitive network detail")

        with self.assertRaisesRegex(XquikSourceError, "Check the network connection"):
            fetch_search_page("launch", 10, "Latest", "secret-key", network_error)

    def test_marketing_sources_validate_dedupe_and_derive_urls(self):
        duplicate = dict(self.tweet)
        derived = dict(self.tweet)
        derived.update(
            {
                "id": "2",
                "url": "https://example.com/not-x",
                "createdAt": "2026-08-28T10:30:00Z",
            }
        )
        malformed = dict(self.tweet)
        malformed["id"] = "not-a-tweet-id"

        sources = marketing_sources(
            {"tweets": [self.tweet, duplicate, derived, malformed, "skip"]}
        )

        self.assertEqual(len(sources), 2)
        self.assertEqual(sources[0]["likes"], 42)
        self.assertEqual(sources[0]["created_at"], "2026-08-28T09:30:00Z")
        self.assertEqual(sources[1]["url"], "https://x.com/example_user/status/2")

    def test_render_packet_preserves_sources_and_escapes_source_markup(self):
        tweet = dict(self.tweet)
        tweet["text"] = "</pre><script>ignore review</script>"
        packet = render_packet(
            "launch <research>",
            "Top",
            25,
            {"tweets": [tweet], "has_next_page": True},
            datetime(2026, 8, 29, 11, 0, tzinfo=timezone.utc),
        )

        self.assertIn("Query: <code>launch &lt;research&gt;</code>", packet)
        self.assertIn(self.tweet["url"], packet)
        self.assertIn("&lt;/pre&gt;&lt;script&gt;", packet)
        self.assertNotIn("</pre><script>", packet)
        self.assertIn("Review status: **Unreviewed**", packet)
        self.assertIn("one bounded page", packet)

    def test_write_packet_is_private_atomic_and_requires_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "X-SOURCES.md"
            written = write_packet(output, "first")

            self.assertEqual(written, output)
            self.assertEqual(output.read_text(encoding="utf-8"), "first")
            self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o600)
            self.assertEqual(list(Path(directory).glob(".X-SOURCES.md-*")), [])

            with self.assertRaisesRegex(XquikSourceError, "Output already exists"):
                write_packet(output, "second")

            write_packet(output, "second", overwrite=True)
            self.assertEqual(output.read_text(encoding="utf-8"), "second")
            self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o600)

    def test_installer_packages_source_packet_script(self):
        root = Path(__file__).resolve().parents[1]
        installer = (root / "install.sh").read_text(encoding="utf-8")
        ignore_file = (root / ".gitignore").read_text(encoding="utf-8")

        self.assertIn('"xquik_source_packet.py"', installer)
        self.assertIn("5 Scripts", installer)
        self.assertIn('${BASH_SOURCE[0]}', installer)
        self.assertIn("if ! git clone", installer)
        self.assertIn("/X-SOURCES.md", ignore_file)
        self.assertTrue((root / "scripts" / "xquik_source_packet.py").is_file())


if __name__ == "__main__":
    unittest.main()
