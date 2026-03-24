Hey @zubair-trabzada 👋

I ran your skills through `tessl skill review` at work and found some targeted improvements. Here's the full before/after:

![Score Card](score_card.png)

| Skill | Before | After | Change |
|-------|--------|-------|--------|
| market-seo | 46% | 89% | +43 |
| market-proposal | 46% | 89% | +43 |
| market-funnel | 48% | 89% | +41 |
| market-brand | 43% | 84% | +41 |
| market | 45% | 85% | +40 |
| market-audit | 55% | 89% | +34 |
| market-landing | 59% | 89% | +30 |
| market-social | 59% | 89% | +30 |
| market-ads | 60% | 89% | +29 |
| market-launch | 61% | 89% | +28 |
| market-report-pdf | 64% | 89% | +25 |
| market-competitors | 60% | 81% | +21 |
| market-copy | 69% | 89% | +20 |
| market-report | 69% | 89% | +20 |
| market-emails | 73% | 89% | +16 |

**Average: 57% → 88% (+31)**

<details>
<summary>Changes made</summary>

### All 15 skills
- **Added YAML frontmatter** — none of the skills had frontmatter (`name`, `description`), which caused them to fail validation entirely (scoring 0% without it). After adding frontmatter with proper kebab-case names and quoted descriptions, the LLM judge could actually evaluate the content.
- **Added "Use when..." clauses** — every description now includes explicit trigger guidance so agents know when to select each skill, which was the single biggest scoring improvement across the board.
- **Expanded trigger terms** — added natural user language variations (e.g., "GTM" for market-launch, "cart abandonment" for market-funnel, platform names for market-ads/market-social).

### High-impact content improvements
- **market-brand** (43→84): Reduced from 477 to 180 lines (62%). Removed verbose tone signal tables and archetype descriptions Claude already knows. Added validation checkpoint for source material sufficiency.
- **market-seo** (46→89): Reduced from 488 to 128 lines (74%). Removed basic SEO concept explanations. Added script execution validation steps.
- **market-proposal** (46→89): Reduced from 387 to 158 lines (59%). Removed pricing psychology tips, follow-up sequences, and formatting guidance. Added input validation checkpoint.
- **market-funnel** (48→89): Reduced from 449 to 291 lines (35%). Removed funnel type reference tables and drop-off cause matrices. Added WebFetch example and validation checkpoints.
- **market** (45→85): Added concrete WebFetch example, replaced Business Context Detection section with Subagent Validation Checkpoints.

### Moderate content improvements
- **market-ads** (60→89): Removed ROAS/CPA benchmark tables, condensed ad copy angle templates.
- **market-copy** (69→89): Removed CTA Color Psychology section, condensed page-specific copy structures.
- **market-launch** (61→89): Removed Common Launch Mistakes and Key Principles sections.
- **market-social** (59→89): Removed platform demographics tables, added brand voice validation checkpoint.
- **market-landing** (59→89): Condensed benchmark tables, hero scoring rubrics, and A/B test examples.
- **market-competitors** (60→81): Condensed discovery methods and template tables.
- **market-audit** (55→89): Condensed business type detection to bullet list format.

### Lighter touch (description-only improvements)
- **market-emails** (73→89): Removed basic concept explanations and "Why It Matters" column.
- **market-report** (69→89): Removed E-E-A-T explanation and glossary section.
- **market-report-pdf** (64→89): Removed PDF vs Markdown comparison table and color scheme tables.

</details>

> **Note:** All skills originally scored 0% because they lacked YAML frontmatter. I added frontmatter with proper names and descriptions to unblock the LLM judge, then re-scored to get meaningful baselines. The "before" scores in the table above reflect those post-frontmatter baselines — the true starting point was 0% across the board.

Honest disclosure — I work at @tesslio where we build tooling around skills like these. Not a pitch - just saw room for improvement and wanted to contribute.

Want to self-improve your skills? Just point your agent (Claude Code, Codex, etc.) at [this Tessl guide](https://docs.tessl.io/evaluate/optimize-a-skill-using-best-practices) and ask it to optimize your skill. Ping me - [@rohan-tessl](https://github.com/rohan-tessl) - if you hit any snags.

Thanks in advance 🙏
