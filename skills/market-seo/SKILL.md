---
name: market-seo
description: "Comprehensive SEO audit combining automated page analysis with expert review of on-page SEO, E-E-A-T content quality, keyword strategy, and technical SEO. Use when a user provides a URL for search engine optimization analysis, wants to improve rankings, needs meta tags reviewed, or requests content gap and featured snippet recommendations. Triggered by /market seo with a target URL."
---

# SEO Content Audit

Perform a comprehensive SEO audit combining automated analysis via `scripts/analyze_page.py` with expert manual review. Produces an actionable audit covering on-page SEO, E-E-A-T, keyword analysis, technical SEO, and content strategy.

## Workflow

### Step 1: Run Automated Analysis

```bash
python3 scripts/analyze_page.py <url>
```

**Validation after execution:**
- If the script exits with a non-zero code, report the error and attempt diagnosis (missing dependencies, network issues)
- If the URL returns a 4xx/5xx status or the page is behind authentication, inform the user and skip to manual recommendations
- If the JSON output is empty or malformed, re-run once; if it still fails, proceed with manual-only analysis
- Confirm the JSON contains expected fields (title, meta_description, headings, links, images, schema) before proceeding

Use the JSON output as the foundation for all subsequent analysis.

### Step 2: On-Page SEO Checklist

Score each element as **Pass**, **Needs Work**, or **Fail**.

**Title Tag** — Check: exists, 50-60 chars, contains primary keyword near front, includes brand name, unique across site, compelling for clicks.

**Meta Description** — Check: exists, 150-160 chars, includes target keyword naturally, has call-to-action, unique, compelling as ad copy.

**Heading Hierarchy** — Check: exactly one H1 with primary keyword, H1 differs from title, logical H2>H3 nesting (no skipped levels), secondary keywords in subheadings.

**Image Optimization** — Check: all images have descriptive alt text with natural keywords, descriptive filenames, optimized file sizes (WebP preferred), lazy loading on below-fold images, responsive srcset/picture usage, decorative images use `alt=""`.

**Internal Linking** — Check: descriptive anchor text, deep links (not just homepage), contextually relevant, 3-10 links per 1,000 words, no broken links.

**URL Structure** — Check: human-readable, contains keywords, under 75 chars, hyphen-separated, lowercase, clean (no unnecessary query params), consistent trailing slashes.

### Step 3: E-E-A-T Content Quality Assessment

Evaluate each dimension as **Strong / Present / Weak / Missing** with specific evidence:

| Dimension | What to Look For |
|---|---|
| Experience | First-hand anecdotes, case studies, screenshots, specific hands-on details |
| Expertise | Author credentials, content depth, accurate data, proper terminology, authoritative sources |
| Authoritativeness | Author bylines with bios, about page, industry recognition, backlink profile |
| Trustworthiness | HTTPS, privacy policy, contact info, reviews/testimonials, sourced claims, up-to-date info |

### Step 4: Keyword Analysis

**Primary keyword assessment:** Identify the target keyword, then check placement in title, H1, first 100 words, subheadings, meta description, and URL. Target 1-2% density (over 3% is stuffing).

**Search intent alignment:** Determine if the content type matches the keyword intent (informational=guide, commercial=comparison, transactional=product page, navigational=specific destination). Misalignment is a ranking killer — users bounce and Google notices.

**Secondary keywords:** Identify 5-10 related terms including synonyms, long-tail variations, People Also Ask queries, and LSI keywords that should appear naturally.

### Step 5: Technical SEO Quick Check

- [ ] **robots.txt** — Accessible, not blocking important pages/resources, points to sitemap
- [ ] **XML Sitemap** — Exists, contains important pages, no broken URLs, accurate dates
- [ ] **Canonical tags** — Present, self-referencing or pointing to correct canonical version
- [ ] **Core Web Vitals** — LCP under 2.5s, FID under 100ms, CLS under 0.1, TTFB under 200ms
- [ ] **Mobile-friendliness** — Viewport meta tag, readable text (16px+), adequate tap targets (48px+), no horizontal scroll

### Step 6: Content Gap & Snippet Opportunities

**Content gaps:** Map the topic cluster, identify subtopics competitors cover that this site doesn't, check People Also Ask and related searches. Present as:

| Missing Topic | Volume Potential | Competition | Content Type Needed | Priority |
|---|---|---|---|---|
| [Topic] | High/Med/Low | High/Med/Low | Blog/Guide/Tool | 1-5 |

**Featured snippet optimization:** Target question-based queries, place concise answers (40-60 words) immediately after question headings, use structured lists/tables where appropriate.

### Step 7: Schema Markup Audit

Check for JSON-LD structured data: Organization, LocalBusiness, Product, Article, FAQ, HowTo, Review/AggregateRating, BreadcrumbList, WebSite/SearchAction — as applicable to the page type. Flag missing schemas that could earn rich results. Validate with Google's Rich Results Test.

### Step 8: Content Strategy Recommendations

Based on findings, recommend publishing cadence, content types, keyword targeting balance (high-volume vs long-tail), content length benchmarks, refresh schedule, and distribution plan. Prioritize by: high volume + low competition + high business value.

## Output Format

Generate `SEO-AUDIT.md` with this structure:

```markdown
# SEO Content Audit: [URL]
### Date: [Date] | SEO Health Score: [X/100]

## On-Page SEO Checklist
[For each element: Status, Current value, Recommended value, Issues]

## Content Quality (E-E-A-T)
| Dimension | Score | Evidence |
|---|---|---|
| Experience / Expertise / Authoritativeness / Trustworthiness | [rating] | [details] |

## Keyword Analysis
[Primary keyword, search intent, placement checklist, secondary keywords]

## Technical SEO
[Quick check results]

## Content Gaps & Snippet Opportunities
[Tables and specific recommendations]

## Schema Markup
[Current vs recommended]

## Prioritized Recommendations
### Critical (Fix Immediately)
### High Priority (This Month)
### Medium Priority (This Quarter)
### Low Priority (When Resources Allow)
```

## Key Principles

- Tie every recommendation to business outcomes — not "optimize your title tag" but "this could increase CTR by 20-35%, bringing ~500 more visitors/month."
- Always show before (current state) and after (recommended change).
- Prioritize by effort-to-impact ratio: a title tag fix takes 5 minutes but affects every impression.
- Cross-reference with prior `/market audit` or `/market landing` findings if available.
