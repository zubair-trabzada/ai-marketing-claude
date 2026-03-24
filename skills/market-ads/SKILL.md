---
name: market-ads
description: "Advertising engine that generates complete ad campaigns for Facebook Ads, Google Ads, LinkedIn Ads, TikTok Ads, and Twitter/X Ads. Use when creating ad campaigns, writing ad copy, planning audience targeting, setting ad budgets, building retargeting funnels, or generating creative briefs for any paid advertising platform."
---

# Ad Creative & Copy Generation

You are the advertising engine for `/market ads <url>`. Generate production-ready ad campaigns across Google, Meta, LinkedIn, TikTok, and Twitter/X with copy variations, audience targeting, budget allocation, and creative specs. Output everything to AD-CAMPAIGNS.md.

Fetch the target URL first to extract: product/service, price point, target audience, USP, conversion action, social proof, objections, and competitors. These inform all campaign messaging.

## Phase 1: Campaign Foundation

Map the business goal to campaign objectives:

| Business Goal | Campaign Objective | Primary Platforms | Ad Format |
|--------------|-------------------|-----------------|-----------|
| Brand awareness | Reach / Impressions | Meta, YouTube, TikTok | Video, Display |
| Lead generation | Lead Gen / Conversions | Meta, LinkedIn, Google | Lead forms, Landing pages |
| Trial signups | Conversions | Google, Meta, LinkedIn | Search, Landing pages |
| E-commerce sales | Sales / ROAS | Google Shopping, Meta, TikTok | Shopping, Carousel |
| App installs | App Install | Meta, Google, TikTok | App install ads |
| Content promotion | Engagement / Traffic | Meta, Twitter, LinkedIn | Boosted posts, Video |

---

## Phase 2: Platform-Specific Ad Generation

### 2.1 Google Ads

**Search Ads (Responsive Search Ads):**

Character limits:
- Headlines: Up to 15 headlines, 30 characters each
- Descriptions: Up to 4 descriptions, 90 characters each
- Display URL path: 2 fields, 15 characters each

Generate at least:
- 10 headlines covering these angles:
  - Brand name + value prop
  - Pain point + solution
  - Specific benefit + number
  - Social proof headline
  - Urgency / offer headline
  - Question headline
  - How-to headline
  - Comparison headline
  - Feature-focused headline
  - Action-oriented headline
- 4 descriptions covering:
  - Value proposition + CTA
  - Features + benefits
  - Social proof + trust
  - Urgency + offer details

**Keyword Strategy:**
- 10-15 high-intent keywords per ad group
- Match types: mix of exact, phrase, and broad match modified
- Negative keywords list (10-20 irrelevant terms to exclude)
- Organize into 3-5 ad groups by theme

**Performance Max Campaigns:**
- Asset groups organized by audience segment
- Headline variations (15 short + 5 long)
- Description variations (5)
- Image specs: 1200x1200 (square), 1200x628 (landscape), 960x1200 (portrait)
- Video assets: 10-30 seconds recommended
- Audience signals: custom segments, in-market, affinity

### 2.2 Meta Ads (Facebook + Instagram)

**Ad Formats and Specs:**

| Format | Placement | Image Spec | Video Spec | Text Limits |
|--------|-----------|-----------|-----------|-------------|
| Single Image | Feed, Stories, Reels | 1080x1080 (feed), 1080x1920 (stories) | N/A | Primary: 125 chars, Headline: 40, Description: 30 |
| Video | Feed, Stories, Reels | N/A | 1080x1080 or 1080x1920, <240 min | Same as image |
| Carousel | Feed, Stories | 1080x1080 per card, 2-10 cards | 1080x1080, <240 min | Same as image |
| Collection | Feed | 1200x628 cover | 1200x628 cover | Same as image |

**Generate for each ad concept:**
- Primary text (3 variations: short, medium, long)
- Headline (5 variations)
- Description (3 variations)
- CTA button (select from: Learn More, Sign Up, Shop Now, Get Offer, Book Now, Download, Contact Us)

**Ad Copy Angles (generate 5-10 per campaign):**

Use these angle categories, adapting tone and length per placement:
- **Pain point** — Lead with frustration, resolve with product
- **Social proof** — Numbers, customer quotes, trust signals
- **Before/after** — Contrast painful state vs desired outcome
- **Objection handling** — Name the objection, counter with evidence + risk-free offer
- **Urgency/scarcity** — Limited availability, deadline, locked-in pricing
- **Curiosity** — Tease a secret or counterintuitive insight
- **Direct benefit** — Specific outcome + timeframe, no fluff
- **Comparison** — Old way vs product advantage
- **Testimonial** — Verbatim customer quote with attribution
- **How-to** — 3-step format showing product in action

### 2.3 LinkedIn Ads

**Ad Formats:**
- Sponsored Content (single image, video, carousel)
- Message Ads (InMail)
- Text Ads
- Conversation Ads
- Document Ads (PDF carousel)

**Character Limits:**
- Sponsored Content: Intro text 600 chars, Headline 200 chars
- Message Ads: Subject 60 chars, Body 1,500 chars
- Text Ads: Headline 25 chars, Description 75 chars

**LinkedIn-Specific Copy Angles:**
- Professional development: "Level up your [skill]"
- Industry insight: "[Industry] is changing. Here's how to stay ahead."
- ROI-focused: "Companies using [product] see [X]% improvement in [metric]"
- Peer comparison: "Your competitors are already using [approach]. Are you?"
- Thought leadership: "[Report/whitepaper] reveals [surprising finding]"

**Targeting Options to Recommend:**
- Job title targeting (decision makers)
- Company size
- Industry
- Seniority level
- Skills and interests
- Matched audiences (website retargeting, email lists)
- Lookalike audiences

### 2.4 TikTok Ads

**Ad Formats:**
- In-Feed Ads (video)
- TopView (full-screen takeover)
- Branded Hashtag Challenge
- Spark Ads (boosted organic content)

**Specs:**
- Video: 9:16 vertical, 5-60 seconds (9-15 seconds optimal)
- Resolution: 720x1280 minimum
- File size: Up to 500 MB
- Ad text: 100 characters
- CTA buttons: Learn More, Shop Now, Sign Up, Download, Contact Us

**TikTok Creative Principles:**
- First 3 seconds determine watch rate (hook immediately)
- Native aesthetic outperforms polished ads (look organic)
- Use trending sounds and music
- Text overlays for sound-off viewing
- Face-to-camera content outperforms product-only
- Keep it fast-paced with jump cuts

**TikTok Script Template:**
```
[0-3 sec] HOOK: "Wait — you're still doing [old way]?"
[3-10 sec] PROBLEM: Show the frustration / pain point visually
[10-20 sec] SOLUTION: Introduce product with quick demo
[20-25 sec] PROOF: Flash testimonial, number, or result
[25-30 sec] CTA: "Link in bio" or "Click to try free"
```

### 2.5 Twitter/X Ads

**Ad Formats:**
- Promoted Tweets (text, image, video, carousel)
- Follower Ads
- Amplify (video pre-roll)

**Character Limits:**
- Tweet text: 280 characters (but 100-150 performs best)
- Image: 1200x675 or 1080x1080
- Video: up to 2:20, but 6-15 seconds optimal

**Twitter Ad Copy Style:**
- Conversational, not corporate
- Hot take + solution format
- Thread-style ads (first tweet is the hook, rest is the story)
- Engage in trending conversations with brand angle

---

## Phase 3: Retargeting Sequences

### 3.1 Three-Stage Retargeting Funnel

```
STAGE 1: AWARENESS (Cold Audience)
  Audience: Lookalikes, interest-based, broad targeting
  Goal: Introduce the brand and value proposition
  Ad Type: Educational content, how-to videos, thought leadership
  Budget: 40% of total ad spend
  Metrics: CPM, reach, video view rate, landing page views

STAGE 2: CONSIDERATION (Warm Audience)
  Audience: Website visitors (7-30 days), video viewers (50%+),
            social engagers, email list
  Goal: Build trust and handle objections
  Ad Type: Case studies, testimonials, demos, comparison content
  Budget: 35% of total ad spend
  Metrics: CPC, CTR, landing page conversion rate

STAGE 3: CONVERSION (Hot Audience)
  Audience: Cart abandoners, pricing page visitors, trial users,
            high-intent page visitors
  Goal: Drive the final conversion action
  Ad Type: Direct offer, urgency, guarantee, limited-time discount
  Budget: 25% of total ad spend
  Metrics: CPA, ROAS, conversion rate
```

### 3.2 Retargeting Ad Sequences

For each stage, generate 3-5 ad variations:

```
Stage 1 Ads (Awareness):
  Ad 1A: Educational — "[Topic] explained in 60 seconds"
  Ad 1B: Pain point — "If [frustration], you need to see this"
  Ad 1C: Social proof — "[Number] [audience] trust [product]"

Stage 2 Ads (Consideration):
  Ad 2A: Case study — "How [customer] achieved [result]"
  Ad 2B: Demo — "See [product] in action (2-min walkthrough)"
  Ad 2C: Comparison — "[Product] vs [alternative]: honest breakdown"
  Ad 2D: FAQ — "Your top 3 questions about [product], answered"

Stage 3 Ads (Conversion):
  Ad 3A: Offer — "[Discount/trial] — limited to [number/time]"
  Ad 3B: Urgency — "Your free trial starts now (no credit card)"
  Ad 3C: Guarantee — "Try [product] risk-free for [period]"
  Ad 3D: Testimonial — "'[Quote about specific result]' — Start yours"
```

---

## Phase 4: Budget and Performance

### 4.1 Budget Allocation Recommendations

**By Platform (adjust based on business type):**

| Business Type | Google | Meta | LinkedIn | TikTok | Other |
|--------------|--------|------|----------|--------|-------|
| SaaS (B2B) | 30% | 25% | 30% | 5% | 10% |
| SaaS (B2C) | 25% | 40% | 5% | 20% | 10% |
| E-commerce | 30% | 40% | 0% | 20% | 10% |
| Agency | 20% | 30% | 35% | 5% | 10% |
| Local Business | 50% | 35% | 0% | 5% | 10% |
| Creator/Course | 10% | 40% | 10% | 30% | 10% |

Split by funnel stage: ~40% awareness, ~35% consideration, ~25% conversion.

### 4.2 Performance Benchmarks

Provide ROAS and CPA targets appropriate to the business type, industry, and platform mix. Factor in typical ranges for each platform (e.g., LinkedIn tends higher CPA than Meta/TikTok for B2B leads). Include acceptable, good, and excellent tiers so the user can gauge campaign health.

### 4.3 Landing Page Alignment

For each ad campaign, verify landing page alignment:

**Alignment Checklist:**
- Does the landing page headline match the ad headline?
- Does the landing page deliver on the ad's promise?
- Is the CTA on the landing page consistent with the ad's CTA?
- Is the visual style consistent between ad and page?
- Is the landing page mobile-optimized (critical for social ads)?
- Does the landing page load in under 3 seconds?
- Is there one clear conversion action (not multiple competing CTAs)?

**Message Match Score:**
Rate the alignment between each ad and its destination page 1-10. Flag any score below 7.

---

## Phase 5: Ad Variations and Testing

### 5.1 Variation Generation

For each ad concept, generate:
- 5 headline variations (different angles, lengths, emotions)
- 3 primary text variations (short: 1-2 sentences, medium: 3-4 sentences, long: 5-7 sentences)
- 3 CTA variations
- 3 visual concept descriptions (for designer handoff)

### 5.2 Testing Framework

**Test Priority Order:**
1. Audience (who you target matters most)
2. Offer (what you offer: free trial vs demo vs discount)
3. Creative concept (the big idea and visual approach)
4. Headline (specific wording of the hook)
5. Body copy (supporting text)
6. CTA (button text and color)

**Testing Rules:**
- Test one variable at a time
- Run tests for at least 3-5 days or 1,000 impressions per variant
- Statistical significance threshold: 95%
- Kill underperformers at 2x the CPA target
- Scale winners by 20% budget increments (not 2x overnight)

---

## Output Format: AD-CAMPAIGNS.md

Write the full output to `AD-CAMPAIGNS.md`:

```markdown
# Ad Campaigns: [Business Name]
**URL:** [url]
**Date:** [current date]
**Business Type:** [type]
**Primary Objective:** [objective]
**Recommended Platforms:** [platforms]

---

## Campaign Strategy Overview
[2-3 paragraph overview of the ad strategy]

## Audience Targeting
[Detailed audience definitions for each platform]

## Campaign 1: [Platform Name]
### Ad Group 1: [Theme]
**Targeting:** [audience parameters]
**Budget:** [recommended daily/monthly]
**Objective:** [campaign objective]

#### Ad Variation 1
- **Headline:** [text]
- **Primary Text:** [text]
- **Description:** [text]
- **CTA:** [button text]
- **Visual:** [creative description]
- **Landing Page:** [URL/page]

[Repeat for each variation]

[Repeat for each ad group and platform]

## Retargeting Strategy
[Three-stage funnel with ad variations]

## Budget Allocation
[Platform and funnel stage breakdown]

## Testing Plan
[Prioritized A/B tests]

## Performance Benchmarks
[ROAS and CPA targets by platform]

## Landing Page Alignment
[Message match assessment and recommendations]

## Creative Brief for Designers
[Visual specifications, brand guidelines, image/video requirements]
```

---

## Terminal Output

```
=== AD CAMPAIGNS GENERATED ===

Business: [name]
Platforms: [list]
Total Ad Variations: [count]

Campaign Structure:
  Google Ads: [X] ad groups, [X] variations
  Meta Ads: [X] ad sets, [X] variations
  LinkedIn: [X] campaigns, [X] variations

Budget Recommendation: $[X,XXX]/month
Expected CPA: $[XX]-$[XX]
Target ROAS: [X]:1

Full campaigns saved to: AD-CAMPAIGNS.md
```

---

## Cross-Skill Integration

- If `COPY-SUGGESTIONS.md` exists, reuse value propositions and messaging angles
- If `COMPETITOR-REPORT.md` exists, use competitor positioning for comparison ads
- If `FUNNEL-ANALYSIS.md` exists, align ad funnel stages to conversion path
- If `SOCIAL-CALENDAR.md` exists, promote top organic content as Spark/boosted ads
- Suggest follow-up: `/market funnel` for conversion path, `/market landing` for page optimization
