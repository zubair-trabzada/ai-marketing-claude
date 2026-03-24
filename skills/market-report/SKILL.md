---
name: market-report
description: "Compile marketing audit and analysis data into a client-ready Markdown report with scorecard, category deep-dives, recommendations, and prioritized action plan. Use when the user requests a full marketing report, performance report, client report, marketing analysis summary, or has completed one or more audit skills and wants a compiled assessment document."
---

# Marketing Report Generator (Markdown Format)

## When to Use
- User wants a full marketing report, performance report, or marketing analysis for a client or their own business
- User has completed one or more audit skills and wants a compiled report
- User asks for a marketing assessment, scorecard, or analysis document
- Triggered by `/market report` or `/market report <domain>`

## How to Execute

### Step 1: Collect All Available Data
Before generating the report, check for any existing audit data from previous skill runs. Look for these files in the project directory:

**Possible data sources:**
- `MARKETING-AUDIT.md` -- from `/market audit`
- `LANDING-CRO.md` -- from `/market landing`
- `SEO-AUDIT.md` -- from `/market seo`
- `BRAND-VOICE.md` -- from `/market brand`
- `COMPETITOR-ANALYSIS.md` -- from `/market competitors`
- `FUNNEL-ANALYSIS.md` -- from `/market funnel`
- `CONTENT-AUDIT.md` -- from content analysis
- `AD-AUDIT.md` -- from `/market ads`
- `SOCIAL-AUDIT.md` -- from `/market social`
- `EMAIL-AUDIT.md` -- from `/market emails`

If no previous data exists, inform the user and offer to:
1. Run a quick audit first (recommended)
2. Generate a report based on available information (website URL, user-provided data)
3. Create a report template they can fill in

### Step 2: Calculate the Marketing Scorecard

Score across 6 categories, each worth up to 100 points. The overall score is the weighted average.

#### Category 1: Website & Conversion (Weight: 25%)
Evaluate based on landing page analysis, CRO findings, and UX assessment.

| Factor | Points Available | Criteria |
|---|---|---|
| Page load speed | 15 | Under 2s = 15, Under 3s = 10, Under 5s = 5, Over 5s = 0 |
| Mobile responsiveness | 15 | Fully responsive = 15, Mostly = 10, Partially = 5, Not = 0 |
| Clear value proposition | 20 | Immediately clear = 20, Takes effort = 12, Vague = 5, Missing = 0 |
| CTA effectiveness | 20 | Strong and clear = 20, Present but weak = 12, Unclear = 5, Missing = 0 |
| Social proof | 15 | Multiple types = 15, Some = 10, Minimal = 5, None = 0 |
| Form optimization | 15 | Optimized = 15, Adequate = 10, Needs work = 5, Broken = 0 |

#### Category 2: SEO & Organic (Weight: 20%)
Evaluate based on SEO audit findings.

| Factor | Points Available | Criteria |
|---|---|---|
| Title tags & meta descriptions | 15 | Optimized = 15, Present = 10, Partial = 5, Missing = 0 |
| Header hierarchy (H1-H6) | 10 | Proper = 10, Mostly = 7, Needs work = 3, Missing = 0 |
| Content quality | 25 | Excellent = 25, Good = 17, Average = 10, Poor = 3 |
| Technical SEO | 20 | No issues = 20, Minor issues = 13, Major issues = 7, Critical = 0 |
| Internal linking | 15 | Strategic = 15, Present = 10, Minimal = 5, None = 0 |
| Schema markup | 15 | Comprehensive = 15, Basic = 10, Minimal = 5, None = 0 |

#### Category 3: Content & Messaging (Weight: 15%)
Evaluate based on brand voice analysis and content audit.

| Factor | Points Available | Criteria |
|---|---|---|
| Brand voice consistency | 20 | Consistent = 20, Mostly = 13, Inconsistent = 7, No voice = 0 |
| Content quality | 25 | Expert-level = 25, Good = 17, Generic = 10, Poor = 3 |
| Content variety | 15 | Multiple formats = 15, Some = 10, Limited = 5, Single = 0 |
| Publishing frequency | 15 | Regular cadence = 15, Sporadic = 10, Rare = 5, None = 0 |
| Audience targeting | 25 | Precisely targeted = 25, Somewhat = 17, Broad = 10, Off-target = 3 |

#### Category 4: Social Media & Community (Weight: 15%)
Evaluate based on social media presence and engagement.

| Factor | Points Available | Criteria |
|---|---|---|
| Platform presence | 15 | Right platforms, active = 15, Present but inactive = 8, Missing key = 3 |
| Content quality | 25 | Engaging and on-brand = 25, Adequate = 15, Low quality = 7, Poor = 0 |
| Engagement rate | 25 | Above benchmark = 25, At benchmark = 17, Below = 10, Negligible = 3 |
| Posting consistency | 15 | Regular schedule = 15, Sporadic = 10, Rare = 5, Abandoned = 0 |
| Community building | 20 | Active community = 20, Some engagement = 13, Broadcast only = 7, None = 0 |

#### Category 5: Email & Automation (Weight: 15%)
Evaluate based on email marketing assessment.

| Factor | Points Available | Criteria |
|---|---|---|
| List building mechanism | 20 | Multiple opt-ins = 20, One opt-in = 13, No visible opt-in = 5 |
| Email design & content | 20 | Professional and engaging = 20, Adequate = 13, Needs work = 7 |
| Automation sequences | 25 | Comprehensive = 25, Basic = 15, Minimal = 8, None = 0 |
| Segmentation | 20 | Advanced = 20, Basic = 13, None = 5 |
| Deliverability signals | 15 | Strong = 15, Adequate = 10, Concerning = 5, Problems = 0 |

#### Category 6: Paid Advertising (Weight: 10%)
Evaluate based on ad account audit (if applicable).

| Factor | Points Available | Criteria |
|---|---|---|
| Campaign structure | 20 | Well-organized = 20, Adequate = 13, Messy = 7, None = 0 |
| Targeting quality | 25 | Precise and layered = 25, Good = 17, Broad = 10, Wasteful = 3 |
| Ad creative quality | 25 | Compelling and varied = 25, Adequate = 17, Weak = 10, Poor = 3 |
| Landing page alignment | 15 | Perfect match = 15, Good = 10, Misaligned = 5, Broken = 0 |
| Tracking & attribution | 15 | Comprehensive = 15, Basic = 10, Minimal = 5, Missing = 0 |

#### Overall Score Calculation
```
Overall Score = (Website * 0.25) + (SEO * 0.20) + (Content * 0.15) + (Social * 0.15) + (Email * 0.15) + (Paid * 0.10)
```

**Score Interpretation:** 85-100 Excellent, 70-84 Good, 55-69 Average, 40-54 Below Average, 0-39 Critical.

### Step 3: Write Category Deep-Dives

For each of the 6 categories, provide:

1. **Score and Rating** -- X/100 with interpretation
2. **Key Findings** -- 3-5 specific observations with evidence
3. **What's Working** -- Positive elements to preserve and build on
4. **Gaps and Issues** -- Problems identified with severity ratings
5. **Recommendations** -- Specific, actionable improvements ranked by impact
6. **Revenue Impact Estimate** -- Estimated financial impact of implementing recommendations

**Revenue Impact Estimation:** Calculate as `(Estimated traffic change * Conversion rate change * Average deal value) * Confidence factor`. Apply a conservative confidence factor (0.5) for all estimates.

### Step 4: Competitor Comparison Summary
If competitor data is available from `/market competitors`, include:

**Competitive Positioning Matrix:**
| Factor | Client | Competitor 1 | Competitor 2 | Competitor 3 |
|---|---|---|---|---|
| Website Quality | X/10 | X/10 | X/10 | X/10 |
| SEO Visibility | X/10 | X/10 | X/10 | X/10 |
| Content Quality | X/10 | X/10 | X/10 | X/10 |
| Social Presence | X/10 | X/10 | X/10 | X/10 |
| Overall Position | Xth/4 | Xth/4 | Xth/4 | Xth/4 |

**Competitive Advantages:** What the client does better
**Competitive Gaps:** Where competitors outperform the client
**Opportunities:** Spaces competitors are not addressing

### Step 5: Content Quality Assessment
Summarize content findings across all channels:

- **Website copy** -- Clarity, persuasiveness, brand alignment
- **Blog content** -- Depth, expertise, SEO optimization, publishing cadence
- **Social media content** -- Engagement quality, brand consistency, platform optimization
- **Email content** -- Subject line effectiveness, body copy quality, CTA strength
- **Ad creative** -- Messaging clarity, visual quality, offer presentation

### Step 6: Conversion Optimization Summary
Compile all conversion-related findings:

- **Primary conversion paths** -- How visitors become customers
- **Funnel leaks** -- Where potential customers drop off
- **CRO quick wins** -- Changes that can be implemented immediately
- **Testing opportunities** -- A/B tests recommended with hypotheses
- **Benchmark comparison** -- Current rates vs industry standards

### Step 7: SEO Snapshot
Summarize SEO health in a scannable format:

```
SEO Health Snapshot:
- Title Tags: [Optimized / Needs Work / Missing]
- Meta Descriptions: [Optimized / Needs Work / Missing]
- H1 Tags: [Proper / Issues / Missing]
- Image Alt Text: [Complete / Partial / Missing]
- Page Speed: [Fast / Moderate / Slow]
- Mobile-Friendly: [Yes / Partially / No]
- Schema Markup: [Present / Partial / Missing]
- Robots.txt: [Configured / Issues / Missing]
- Sitemap: [Present / Issues / Missing]
- HTTPS: [Yes / No]
- Core Web Vitals: [Pass / Needs Work / Fail]
```

### Step 8: Build the Prioritized Action Plan

Organize all recommendations into three tiers:

#### Quick Wins (Implement This Week)
High impact, low effort changes. These should be implementable within 1-5 business days.

Format each item as:
```
- [ ] [Action item]: [Specific description]
  - Impact: [HIGH/MEDIUM/LOW]
  - Effort: [1-5 hours]
  - Expected Result: [Specific outcome]
  - Revenue Impact: [$X/month estimated]
```

#### Medium-Term (Implement This Month)
Moderate impact, moderate effort. These require 1-4 weeks.

#### Strategic (Implement This Quarter)
High impact, high effort. These are foundational changes that require planning and sustained effort.

### Step 9: Build the 30-60-90 Day Roadmap

**Days 1-30: Foundation & Quick Wins**
- Week 1: Implement all quick wins from the action plan
- Week 2: Set up tracking and analytics baseline
- Week 3: Begin medium-term improvements
- Week 4: First performance review and adjustment

**Days 31-60: Growth & Optimization**
- Week 5-6: Launch core campaign improvements
- Week 7: A/B testing program begins
- Week 8: Content strategy implementation

**Days 61-90: Scale & Expand**
- Week 9-10: Scale what's working, cut what isn't
- Week 11: Expand to new channels or campaigns
- Week 12: Comprehensive review, update strategy for next quarter

### Step 10: Appendix

Include methodology notes so the client understands how scores were derived:

**Scoring Methodology:**
- How each category was evaluated
- Data sources used
- Benchmarks referenced
- Limitations and assumptions
- Date of analysis

**Tools Used:**
- List any tools or scripts used in the analysis
- Reference to scripts/analyze_page.py if used

## Output Format

Generate a file called `MARKETING-REPORT.md` with:

```markdown
# Marketing Report
## [Company/Domain Name]
### Prepared by: [Agent/Agency Name]
### Date: [Date]

---

## Executive Summary

### Overall Marketing Score: [X/100] -- [Rating]

[2-3 paragraph summary covering: current state assessment, top 3 findings, estimated revenue impact of implementing recommendations, and recommended first steps]

### Score Breakdown
| Category | Score | Rating |
|---|---|---|
| Website & Conversion | X/100 | [Rating] |
| SEO & Organic | X/100 | [Rating] |
| Content & Messaging | X/100 | [Rating] |
| Social Media | X/100 | [Rating] |
| Email & Automation | X/100 | [Rating] |
| Paid Advertising | X/100 | [Rating] |
| **Overall** | **X/100** | **[Rating]** |

### Top 3 Priority Actions
1. [Most impactful recommendation with revenue estimate]
2. [Second most impactful recommendation]
3. [Third most impactful recommendation]

---

## Detailed Findings

### 1. Website & Conversion [X/100]
[Deep-dive analysis with findings, what's working, gaps, recommendations]

### 2. SEO & Organic [X/100]
[Deep-dive analysis]

### 3. Content & Messaging [X/100]
[Deep-dive analysis]

### 4. Social Media [X/100]
[Deep-dive analysis]

### 5. Email & Automation [X/100]
[Deep-dive analysis]

### 6. Paid Advertising [X/100]
[Deep-dive analysis]

---

## Competitor Comparison
[Matrix and analysis]

---

## SEO Snapshot
[Health checklist]

---

## Conversion Optimization Summary
[Funnel analysis and CRO recommendations]

---

## Revenue Impact Summary
| Recommendation | Estimated Monthly Impact | Confidence | Priority |
|---|---|---|---|
| [Rec 1] | $X,XXX | High/Medium/Low | 1 |
| [Rec 2] | $X,XXX | High/Medium/Low | 2 |
| ... | ... | ... | ... |
| **Total Estimated Impact** | **$XX,XXX/month** | | |

---

## Prioritized Action Plan

### Quick Wins (This Week)
- [ ] [Action items with impact and effort]

### Medium-Term (This Month)
- [ ] [Action items]

### Strategic (This Quarter)
- [ ] [Action items]

---

## 30-60-90 Day Roadmap
[Week-by-week plan]

---

## Appendix
### Methodology
### Tools Used
### Data Sources
```

## Key Principles
- This report should be impressive enough to use as a sales tool. A well-crafted marketing report can open the door to a client engagement.
- Always lead with insights and opportunities, not criticism. Frame everything through the lens of growth potential.
- Quantify everything possible. "$32,000/month in unrealized revenue" is more compelling than "you're leaving money on the table."
- Make the action plan so specific that someone could hand it to a junior marketer and they could execute it.
- Use professional formatting: consistent headers, tables for data, checkboxes for action items, clear visual hierarchy.
- If data from previous skills is available, reference specific findings. If not, be transparent about what's based on analysis vs estimation.
- The report should tell a story: Here's where you are, here's where you could be, here's how to get there, and here's what it's worth.
