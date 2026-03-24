---
name: market-proposal
description: "Generate professional marketing services proposals with anchored pricing, tiered options, ROI projections, and competitive positioning. Use when creating a quote, bid, sales proposal, or client pitch after a discovery call or audit."
---

# Client Proposal Generator for Marketing Services

Generate a complete, client-ready marketing services proposal that positions the agency as the clear choice, frames pricing with anchoring and tiered options, and includes ROI projections to justify the investment.

## When to Use
- Creating a proposal, quote, or bid for a prospective marketing client
- Formalizing engagement after a discovery call
- Triggered by `/market proposal` or `/market proposal <client name>`

## How to Execute

### Step 1: Gather Proposal Inputs

Collect from the user (ask if not provided):

**Client Details:**
1. Client name, company, industry, and business model
2. Current marketing situation and primary pain points
3. Goals (revenue, growth, leads, brand awareness)
4. Budget range, decision timeline, and key stakeholders

**Services:**
1. Services proposed (SEO, paid ads, content, social, email, full-stack)
2. Engagement model (retainer, project, performance-based, hybrid)
3. Proposed timeline and relevant case studies

**If audit data exists:** Incorporate any previous `/market audit` findings into the Situation Analysis.

> **Validation checkpoint:** Before proceeding, confirm you have at minimum: client name, industry, at least one pain point, at least one goal, and proposed services. If any are missing, ask the user before continuing.

### Step 2: Discovery Call Questions (If Needed)

If the user hasn't had the discovery call yet, provide these essential questions:

1. "Walk me through your business model. How do you make money?"
2. "Who is your ideal customer?"
3. "What marketing are you doing today, and what's working or not?"
4. "What's your current monthly marketing spend and ROI?"
5. "If we're wildly successful, what does that look like in 6-12 months?"
6. "What specific numbers are you trying to hit?"
7. "What's the lifetime value of a customer?"
8. "Who else is involved in this decision, and what's your timeline?"
9. "Have you worked with agencies before? What went well or poorly?"
10. "Is there anything that would make you say 'no' to working together?"

### Step 3: Build the Proposal Document

#### Section 1: Cover Page
Include: company logo, proposal title, client name, preparer name, date, validity period (date + 30 days), and CONFIDENTIAL marking.

#### Section 2: Executive Summary (1 page max)
- Acknowledge the client's situation and goals
- State the core problem you will solve
- Preview recommended approach and expected outcome
- Create urgency to act

Use the client's own language from the discovery call. Mirror their words back.

#### Section 3: Situation Analysis (2-3 pages)
1. **Current State Overview** -- performance of existing marketing
2. **Opportunities Identified** -- specific improvement areas
3. **Competitive Landscape** -- comparison to competitors (from `/market competitors` if available)
4. **Key Challenges** -- obstacles to address
5. **Market Context** -- industry trends and benchmarks

Frame everything as opportunities, not failures.

#### Section 4: Strategy and Approach (2-3 pages)
1. **Phase 1: Foundation** (Month 1-2) -- Setup, audits, baselines, quick wins
2. **Phase 2: Growth** (Month 3-4) -- Core campaign execution, optimization
3. **Phase 3: Scale** (Month 5-6) -- Expand winners, cut underperformers

For each phase include: specific activities, expected outcomes, and success metrics.

#### Section 5: Scope of Work (1-2 pages)

**Include:** Specific deliverables with quantities, meeting cadence, response time commitments, tools/platforms, reporting format and frequency.

**Explicitly Exclude:** Out-of-scope items, additional costs (ad spend, software), assumptions about client responsibilities.

**Client Responsibilities:** Timely feedback/approvals (specify SLA), account access, designated point of contact, content approval timeline, ad budget (separate from management fees).

#### Section 6: Timeline
Visual timeline showing phases, milestones, and deliverables across the engagement period.

#### Section 7: Investment

Present pricing using Good-Better-Best tier structure:

| Component | Growth | Accelerate | Dominate |
|---|---|---|---|
| Strategy & Planning | Quarterly review | Monthly strategy | Weekly strategy |
| Content Creation | 4 pieces/month | 8 pieces/month | 16 pieces/month |
| Paid Ads Management | Up to $5K spend | Up to $15K spend | Up to $50K spend |
| SEO | Basic on-page | Full SEO program | Full SEO + link building |
| Reporting | Monthly report | Bi-weekly report | Weekly dashboard |
| **Monthly Investment** | **$X,XXX** | **$X,XXX** | **$X,XXX** |

Mark the middle tier as "Recommended." Anchor the highest tier first so the middle feels reasonable. Always show the ROI math alongside cost.

#### Section 8: ROI Projection
```
Current State:
- Monthly traffic: [X] | Conversion rate: [X%] | Leads/month: [X]
- Close rate: [X%] | Average deal value: $[X] | Monthly revenue: $[X]

Projected State (6 months):
- Traffic increase: [X%] | New conversion rate: [X%]
- Projected leads increase: [X%] | Revenue increase: $[X]/month

Investment: $[total 6-month cost]
Projected Return: $[projected revenue increase]
ROI: [X]x return
```

Use conservative projections with ranges. Add disclaimer that results depend on multiple factors.

#### Section 9: Team
For each team member: name, title, relevant experience, role on this engagement (2-3 sentences max each).

#### Section 10: Case Studies (2-3 relevant examples)
Format: Client (anonymized if needed) → Challenge → Solution → Results (with specific metrics).

#### Section 11: Next Steps
Clear, friction-free action sequence: sign proposal → kickoff call within 48 hours → onboarding questionnaire → begin Foundation phase. Include contact info and proposal expiration date.

### Step 4: Objection Handling Reference

| Objection | Response Framework |
|---|---|
| "Too expensive" | Reframe as investment, show ROI math, offer smaller starting scope |
| "We can do this in-house" | Highlight opportunity cost, specialized expertise, fully-loaded in-house cost |
| "Tried before, didn't work" | Ask what failed, differentiate approach, offer pilot with success criteria |
| "Need to think about it" | Set specific follow-up date, address specific concerns |
| "Can you guarantee results?" | Share historical results, offer performance-based component |
| "Talking to other agencies" | Differentiate on methodology not price, emphasize culture fit |

### Step 5: Terms and Conditions
Include in appendix: payment terms, contract duration, cancellation policy (30-day notice), scope change process, IP ownership, confidentiality, liability limitations, third-party costs, results disclaimer.

## Output Format

Generate `CLIENT-PROPOSAL.md` with all sections populated based on client details, including Table of Contents and Appendix with Terms & Conditions.

## Key Principles
- The proposal is a sales document -- it should SELL, not just describe.
- Lead with the client's problems and goals, not your services.
- Every price should be anchored to the ROI it will generate.
- Use the client's own language from discovery. Mirror their words.
- If audit data is available, use it extensively -- data-backed proposals close at 2-3x the rate.
- Keep it concise and scannable: bold key numbers, use headers and tables.
- Always include a specific, time-bound next step.
