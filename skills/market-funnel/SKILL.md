---
name: market-funnel
description: "Use when auditing a checkout funnel, diagnosing cart abandonment, benchmarking conversion rates, or mapping the full user journey from first visit to purchase. Identifies drop-off points, quantifies friction, and recommends optimizations with revenue impact estimates."
---

# Sales Funnel Analysis & Optimization

You are the funnel analysis engine for `/market funnel <url>`. Fetch the target site, trace the complete visitor path from landing to conversion, score each step for friction, and output prioritized optimization recommendations to FUNNEL-ANALYSIS.md.

## Fetching the Target Site

Use WebFetch to retrieve the target URL and extract funnel-relevant structure:

```example
WebFetch(
  url: "https://example.com",
  prompt: "Extract the site's conversion funnel structure: identify navigation paths to purchase/signup, list all CTAs with their destinations, note form fields on signup/checkout pages, and flag any trust signals (testimonials, guarantees, security badges)."
)
```

Follow internal links (pricing, signup, checkout, thank-you pages) to map the full funnel. Fetch each page individually if needed.

---

## Phase 1: Funnel Discovery and Mapping

### 1.1 Identify the Funnel Type

Classify the funnel (Lead Gen, SaaS Trial, SaaS Demo, E-commerce, Webinar, Application, Community, or Content) based on the business model and conversion goal detected on the site.

### 1.2 Map Every Funnel Step

For each page in the funnel, document:

```
STEP [#]: [Page Name]
  URL: [url]
  Page Type: [landing/product/pricing/cart/checkout/form/thank-you]
  Primary Action: [what the user should do]
  Next Step: [where the user should go next]
  Exit Points: [where users might leave instead]
  Friction Elements: [anything that slows or confuses]
  Trust Elements: [anything that builds confidence]
  Load Time: [estimated based on page complexity]
```

### 1.3 Visual Funnel Map

Create an ASCII funnel map showing the flow with estimated conversion rates at each step:

```
Traffic Sources
  |
  v
[Homepage] ─── 100% of visitors
  |
  v
[Pricing Page] ─── ~30% click through
  |
  v
[Signup Form] ─── ~15% reach signup
  |
  v
[Paid Plan] ─── ~2% convert to paid
```

Adapt to match the actual funnel discovered.

### Validation Checkpoint 1

Before proceeding, verify:
- [ ] All funnel steps from entry to conversion are mapped
- [ ] Every page has been fetched and analyzed (no gaps)
- [ ] Funnel type is identified with key metric named
- [ ] ASCII map matches the actual site structure (not a generic template)

---

## Phase 2: Page-by-Page Analysis

### 2.1 Scoring Framework

For each page, score these dimensions (0-10):

| Dimension | What to Evaluate |
|-----------|------------------|
| **Clarity** | Is the page purpose immediately obvious? |
| **Continuity** | Does it logically follow from the previous step? |
| **Motivation** | Does it give enough reason to take the next action? |
| **Friction** | How easy is the desired action? (10 = frictionless) |
| **Trust** | Are there adequate trust signals for this stage? |

**Page Score = Average of all 5 dimensions.**

### 2.2 Friction Analysis

For each page, identify specific friction elements. Focus on:

- **CTAs**: Count, clarity, placement (above/below fold), action language
- **Forms**: Field count (target: 3-5 lead gen, 5-8 checkout), progress indicators, inline validation
- **Trust**: Testimonials, guarantees, security badges, social proof near decision points
- **Mobile**: Tap targets, text size, responsive layout
- **Speed**: Heavy images, excessive scripts, render-blocking resources

### 2.3 Lead Magnet Assessment

If the funnel includes a lead magnet, score on: Relevance, Specificity, Perceived Value, Quick Win potential, Product Alignment, and Opt-in Friction (each 0-10).

### Validation Checkpoint 2

Before proceeding, verify:
- [ ] Every funnel page has a 5-dimension score
- [ ] Specific friction elements are identified (not generic observations)
- [ ] Drop-off risk is ranked per step (which step loses the most visitors?)

---

## Phase 3: Funnel Metrics and Revenue Impact

### 3.1 Key Metrics

Estimate or calculate:

```
Conversion Metrics:
  Visitor → Lead:      [X]% (benchmark varies by funnel type)
  Lead → Qualified:    [X]%
  Qualified → Customer:[X]%
  Overall:             [X]%

Revenue Metrics:
  Average Order Value (AOV): $[X]
  Revenue Per Visitor (RPV): $[X]
  LTV:CAC Ratio: [X]:1 (target: 3:1+)
```

### 3.2 Revenue-Per-Visitor Impact Calculation

Quantify every recommendation using RPV:

```
RPV = Monthly Revenue / Monthly Visitors

Example: 10,000 visitors × 2% conversion × $100 AOV = $20,000/month
If conversion improves to 2.5%: $25,000/month → $60,000/year lift
```

Use this framework for every recommendation's revenue impact estimate.

---

## Phase 4: Optimization Recommendations

### 4.1 Prioritization Matrix

Rank every recommendation:

| Priority | Criteria | Timeline |
|----------|----------|----------|
| **P1 — Do Now** | High impact (>10% lift), low effort (<1 day) | This week |
| **P2 — Plan** | High impact, medium effort (1-5 days) | This month |
| **P3 — Schedule** | Medium impact (5-10% lift), low effort | This month |
| **P4 — Backlog** | Medium impact, high effort (5+ days) | This quarter |

### 4.2 Stage-Specific Guidance

Apply optimizations appropriate to the funnel stage:

- **Top of Funnel**: Headline clarity, social proof, page speed, exit-intent capture
- **Mid-Funnel**: Case studies, feature comparisons, interactive demos, retargeting sequences
- **Bottom of Funnel**: Pricing page design, checkout friction, risk reversal (guarantees/trials), urgency elements, cart abandonment recovery
- **Post-Purchase**: Onboarding sequences, upsell on thank-you page, referral program

For each recommendation, include: specific action, expected lift range, and implementation effort.

### 4.3 Pricing Page Audit

If a pricing page exists, check:
- Value-framing headline (not just "Pricing")
- 3 plans max with one highlighted as recommended
- Annual pricing shown first with savings
- Social proof near pricing
- FAQ addressing top objections
- Money-back guarantee or free trial prominently displayed
- Action-oriented CTA language

---

## Phase 5: Nurture Sequence Integration

Map each funnel stage to its recommended email sequence:

```
Visitor (anonymous)   → Retargeting ads (no email)
Lead (opted in)       → Welcome sequence (5-7 emails)
Trial User            → Onboarding sequence (5-7 emails)
Inactive Trial        → Re-engagement sequence (3-4 emails)
Customer              → Post-purchase / loyalty sequence
Churned Customer      → Win-back sequence (3-4 emails)
```

Align entry points to traffic source intent: branded search → short funnel (direct to trial/buy); paid social → long funnel (capture, nurture, convert).

---

## Output Format: FUNNEL-ANALYSIS.md

Write the full output to `FUNNEL-ANALYSIS.md`:

```markdown
# Funnel Analysis: [Business Name]
**URL:** [url]
**Date:** [current date]
**Business Type:** [type]
**Funnel Type:** [type]
**Overall Funnel Health: [X]/100**

---

## Executive Summary
[3-4 paragraphs: funnel type, performance assessment,
biggest bottleneck, top 3 recommendations with revenue impact]

---

## Funnel Map
[ASCII funnel visualization with conversion rates per step]

## Page-by-Page Analysis
### Step 1: [Page Name]
[Scores, friction points, trust elements, recommendations]

## Funnel Metrics
[Current metrics vs benchmarks with gaps highlighted]

## Revenue Impact Analysis
[RPV calculations, improvement scenarios]

## Optimization Recommendations
### Priority 1 — Do Now (This Week)
### Priority 2 — Plan (This Month)
### Priority 3 — Strategic (This Quarter)

## Pricing Page Assessment
## Lead Magnet Assessment
## Email Nurture Integration
## Next Steps
1. [Most critical action]
2. [Second priority]
3. [Third priority]
```

---

## Terminal Output

```
=== FUNNEL ANALYSIS COMPLETE ===

Business: [name]
Funnel Type: [type]
Steps: [count]
Funnel Health: [X]/100

Conversion Flow:
  Visitors → Leads:   [X]% (benchmark: [X]%)
  Leads    → Trial:   [X]% (benchmark: [X]%)
  Trial    → Paid:    [X]% (benchmark: [X]%)
  Overall:            [X]% (benchmark: [X]%)

Biggest Bottleneck: [stage] — [X]% drop-off
Revenue Opportunity: $[X,XXX]/month with recommended fixes

Top 3 Fixes:
  1. [fix] — est. [X]% lift
  2. [fix] — est. [X]% lift
  3. [fix] — est. [X]% lift

Full analysis saved to: FUNNEL-ANALYSIS.md
```

---

## Cross-Skill Integration

- If `MARKETING-AUDIT.md` exists, reference conversion scores
- If `COPY-SUGGESTIONS.md` exists, apply copy improvements to funnel pages
- If `EMAIL-SEQUENCES.md` exists, verify alignment with funnel stages
- If `COMPETITOR-REPORT.md` exists, compare funnel effectiveness
- Suggest follow-up: `/market copy` for page-specific copy, `/market emails` for nurture sequences, `/market landing` for CRO deep dive
