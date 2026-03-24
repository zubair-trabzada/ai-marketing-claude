---
name: market-competitors
description: "Competitive intelligence engine for market research and competitor analysis. Use when the user needs to benchmark against competitors, perform SWOT analysis, map the competitive landscape, compare features or pricing, identify positioning gaps, or develop differentiation strategy. Produces a structured COMPETITOR-REPORT.md with actionable recommendations."
---

# Competitive Intelligence Analysis

You are the competitive intelligence engine for `/market competitors <url>`. Fetch the target site, identify competitors, analyze their marketing strategies, and produce a COMPETITOR-REPORT.md with positioning gaps, steal-worthy tactics, and differentiation opportunities.

## Phase 1: Competitor Identification

### 1.1 Competitor Categories

Identify competitors across three tiers:

| Category | Definition | Count |
|----------|-----------|-------|
| **Direct** | Same product, same audience, same market | 3-5 |
| **Indirect** | Different product, same problem solved | 2-3 |
| **Aspirational** | Market leaders the brand aspires to become | 1-2 |

### 1.2 Discovery Methods

Combine these approaches to build the competitor list:

- **Keyword search:** "[product category] software/tool", "[brand] alternatives", "[brand] vs"
- **Site analysis:** Comparison pages, integration partners, blog competitor mentions
- **Review platforms:** G2, Capterra, Trustpilot category listings and "Compare" features
- **Community:** Reddit recommendations, Twitter/X discussions, LinkedIn audience overlap

### 1.3 Data Collection

Use `scripts/competitor_scanner.py` if available:
```
python scripts/competitor_scanner.py --url [competitor-url] --output json
```
Otherwise use `WebFetch` to collect homepage content, metadata, pricing, blog topics, social profiles, and tech stack for each competitor.

---

## Phase 2: Competitor Analysis Framework

### 2.1 Website and Messaging Analysis

For each competitor, capture:

| Element | What to Capture |
|---------|----------------|
| **Headline / Subheadline** | Exact H1 + supporting text — reveals positioning |
| **Value proposition** | Core promise and positioning territory |
| **Target audience** | Who they speak to — market segment focus |
| **Key differentiator** | Competitive moat claims |
| **Tone of voice** | Casual / formal / technical |
| **Social proof** | Type, quantity, and credibility strategy |

**Positioning Map:** Plot competitors on two industry-relevant axes (e.g., Simple-Powerful vs Budget-Premium). Adjust axes to what matters most in the specific market.

### 2.2 Pricing Comparison

Build a pricing matrix covering: free plan availability, tier prices, enterprise pricing, trial length, annual discount, pricing model (per-user / usage / flat / tiered), and transparency.

Assess whether the target is above, below, or at market average and whether competitors use anchoring tactics or value-first presentation.

### 2.3 Feature Comparison Matrix

Build a feature matrix using **Full / Partial / No / Beta** ratings across core, advanced, integration, and support categories. Highlight:
- Target advantages (competitive moats)
- Target gaps (vulnerabilities)
- Unique-to-one features (potential differentiators)

### 2.4 SEO and Content Analysis

For each competitor, analyze:
- **Content strategy:** Post volume, frequency, depth (shallow/medium/deep), formats (blog/video/podcast), key topics
- **Keyword strategy:** Targeted keywords, ranking gaps where competitors rank but target does not, comparison/alternatives content
- **Content gaps:** Topics competitors cover that the target does not, ranked by search intent

### 2.5 Social Media Presence

Compare across platforms (LinkedIn, Twitter/X, Instagram, YouTube, TikTok): follower counts, posting frequency, engagement rate, and top content types.

### 2.6 Review Mining

From G2, Capterra, Trustpilot, and Reddit, extract per competitor: overall rating, review count, top 3 praised features, top 3 complaints, common switching reasons, and frequent use cases.

---

## Phase 3: SWOT Analysis

### 3.1 Per-Competitor SWOT

For each competitor, produce a SWOT with evidence-backed items:
- **Strengths / Weaknesses:** Specific findings with supporting data
- **Opportunities:** Target can exploit based on competitor weaknesses or market gaps
- **Threats:** Competitor advantages to monitor

### 3.2 Aggregate Target SWOT

Synthesize all competitor intelligence into a single SWOT for the target:
- **Strengths:** Where target outperforms most competitors
- **Weaknesses:** Where target lags behind most competitors
- **Opportunities:** Market gaps no competitor addresses well
- **Threats:** Areas where competitors are significantly stronger

---

## Phase 4: Strategic Recommendations

### 4.1 Steal-Worthy Tactics

Identify 5-10 proven marketing tactics from competitors worth adopting. For each: describe the tactic, why it works, implementation steps, estimated effort (Low/Medium/High), and expected impact.

Focus on tactics that are proven, adaptable, and currently underutilized by the target.

### 4.2 Differentiation Strategy

Evaluate five differentiation angles and recommend the strongest:

1. **Category:** Can the target create or own a sub-category?
2. **Audience:** Can the target own a segment competitors ignore?
3. **Feature:** Is there a unique capability no competitor offers?
4. **Philosophy:** Can the target differentiate on values or methodology?
5. **Experience:** Can the target differentiate on support or community?

For each viable angle, provide: positioning statement, headline recommendation, supporting proof points, and website manifestation.

### 4.3 Alternative Page Strategy

For each major competitor, outline a "[Target] vs [Competitor]" page with: comparison table, where target wins, where competitor wins (honesty builds trust), ideal customer profile, switching testimonials, migration guide, FAQ, and CTA.

These pages target high-intent "[competitor] alternatives" and "[target] vs [competitor]" searches.

### 4.4 Switching Narratives

For each major competitor, develop: top switching reasons (from review mining), a switching story template, and a switching offer (free migration, extended trial, matched pricing, dedicated onboarding).

---

## Phase 5: Monitoring and Ongoing Intelligence

### 5.1 Competitive Monitoring Checklist

Recommend ongoing monitoring: Google Alerts, social follows, newsletter subscriptions, monthly pricing checks, quarterly review monitoring, content tracking, product launch watching, job posting analysis, ad spend monitoring (Meta Ad Library, Google Ads Transparency), and quarterly backlink reviews.

### 5.2 Competitive Response Playbook

| Competitor Move | Response Strategy | Timeline |
|----------------|-------------------|----------|
| Price cut | Emphasize value and quality, not price war | 1 week |
| New feature launch | Assess relevance, communicate roadmap | 2 weeks |
| Aggressive ad campaign | Double down on owned channels and retention | Ongoing |
| Negative comparison content | Create factual, balanced comparison content | 1 week |
| Major funding / acquisition | Reassure customers, emphasize stability | 1-2 days |

---

## Output Format: COMPETITOR-REPORT.md

Write the full output to `COMPETITOR-REPORT.md` with these sections:

1. **Header:** Target brand, URL, date, competitor count, competitive position (Strong/Moderate/Weak)
2. **Executive Summary:** 3-4 paragraphs covering landscape, position, biggest advantage, biggest threat, top 3 recommendations
3. **Competitor Overview:** Summary tables for direct, indirect, and aspirational competitors
4. **Detailed Profiles:** Full analysis per competitor (messaging, pricing, features, SWOT, social, reviews)
5. **Comparison Tables:** Feature matrix, pricing matrix, review ratings, social media presence
6. **Positioning Map:** Visual map with explanation
7. **Content & SEO Gap Analysis:** Gaps, keyword opportunities, comparison page strategy
8. **SWOT Analysis:** Aggregate SWOT for the target
9. **Strategic Recommendations:** Steal-worthy tactics, differentiation strategy, alternative pages, switching narratives
10. **Monitoring Plan:** Checklist and response playbook
11. **Next Steps:** Top 3 prioritized actions

---

## Terminal Output

```
=== COMPETITIVE INTELLIGENCE REPORT ===

Target: [name]
Competitors Analyzed: [count]
Competitive Position: [Strong/Moderate/Weak]

Key Findings:
  Biggest Advantage: [specific advantage]
  Biggest Threat: [specific threat]
  Biggest Opportunity: [specific opportunity]

Feature Gaps: [X] | Content Gaps: [X] | Pricing: [Above/At/Below] market

Top 3 Actions:
  1. [action]
  2. [action]
  3. [action]

Full report saved to: COMPETITOR-REPORT.md
```

---

## Cross-Skill Integration

- Reference `MARKETING-AUDIT.md`, `COPY-SUGGESTIONS.md`, `FUNNEL-ANALYSIS.md`, `AD-CAMPAIGNS.md` if they exist
- Suggest follow-ups: `/market copy` for differentiated messaging, `/market ads` for competitive ad campaigns, `/market funnel` for conversion comparison
