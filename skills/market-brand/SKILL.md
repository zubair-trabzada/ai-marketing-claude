---
name: market-brand
description: "Analyze a brand's voice from existing content and generate comprehensive brand voice guidelines. Use when building a style guide, writing guidelines, brand voice documentation, or auditing tone consistency across channels."
---

# Brand Voice Analysis and Guidelines Generation

Analyze a brand's voice, tone, and messaging across channels. Extract patterns, score voice dimensions, and produce actionable brand voice guidelines any writer can follow.

Triggered by `/market brand <url>` or `/market brand`.

## Validation Checkpoint

Before proceeding, confirm sufficient source material exists. You need **at minimum**:
- Homepage content accessible and substantive
- At least 2 additional pages (about, product, blog, or social)

If fewer than 3 content sources are available, warn the user that analysis will be limited and ask whether to proceed or gather more material first.

## Step 1: Gather Source Material

Prioritize sources in this order:

1. **Primary (required):** Homepage, About page, Product/service pages
2. **Secondary:** Blog posts (3-5 recent), social media profiles, email newsletters, customer-facing copy (error messages, onboarding, help docs)
3. **Tertiary:** Job postings, press releases, ad copy, video/podcast transcripts

Use browser tools or analyze_page.py to access web content. Check the website for social links.

## Step 2: Voice Dimension Analysis

Score each dimension 1-10 with 3-5 quoted examples as evidence:

- **Formal (1) <-----> Casual (10):** Contraction usage, sentence complexity, pronoun person, humor frequency
- **Serious (1) <-----> Playful (10):** Levity, metaphor creativity, emoji/exclamation use, wordplay
- **Technical (1) <-----> Simple (10):** Jargon density, acronym handling, assumed expertise level
- **Reserved (1) <-----> Bold (10):** Claim strength, opinion directness, competitive references, personality distinctiveness

## Step 3: Tone Spectrum Mapping

Map how tone shifts across contexts. For each channel analyzed, document:

| Context | Typical Tone | Example Quote |
|---|---|---|
| Homepage | [e.g., Confident] | "[quote]" |
| Product pages | [e.g., Informative] | "[quote]" |
| Blog | [e.g., Educational] | "[quote]" |
| Social media | [e.g., Casual] | "[quote]" |
| Error/404 | [e.g., Humorous] | "[quote]" |
| Email subjects | [e.g., Direct] | "[quote]" |
| CTAs | [e.g., Action-oriented] | "[quote]" |
| Support | [e.g., Empathetic] | "[quote]" |

## Step 4: Brand Personality Archetype

Assign 1-2 archetypes from: **Authority** (expert, data-driven — e.g., McKinsey, IBM), **Innovator** (forward-thinking, disruptive — e.g., Tesla, Stripe), **Friend** (warm, approachable — e.g., Mailchimp, Slack), **Rebel** (bold, convention-challenging — e.g., Nike, Oatly), **Guide** (wise, instructional — e.g., HubSpot, Khan Academy).

Document: primary archetype, secondary archetype (if applicable), archetype fit (Strong/Moderate/Weak) with evidence.

## Step 5: Vocabulary Analysis

Identify 15-20 characteristic words organized as:
- **Action words:** Favored verbs
- **Descriptive words:** Characteristic adjectives
- **Value words:** Words reflecting brand values
- **Industry terms:** Domain-specific vocabulary
- **Words they avoid:** Terms notably absent or off-brand
- **Signature phrases:** Tagline, recurring patterns, linguistic habits

## Step 6: Competitor Voice Comparison

Compare against 2-3 competitors using a voice comparison matrix:

| Dimension | [Brand] | Competitor 1 | Competitor 2 | Competitor 3 |
|---|---|---|---|---|
| Formal <> Casual | X/10 | X/10 | X/10 | X/10 |
| Serious <> Playful | X/10 | X/10 | X/10 | X/10 |
| Technical <> Simple | X/10 | X/10 | X/10 | X/10 |
| Reserved <> Bold | X/10 | X/10 | X/10 | X/10 |
| Primary Archetype | [type] | [type] | [type] | [type] |

Assess: voice distinctiveness, overlap areas, unoccupied voice territory, differentiation recommendations. If `/market competitors` was run previously, use that data.

## Step 7: Consistency Audit

Score each channel as Consistent/Mostly/Inconsistent with specific observations. Provide an overall consistency score (X/10). Frame inconsistencies as improvement opportunities, not failures.

## Step 8: Brand Messaging Hierarchy

Document messaging at five levels:
1. **Tagline** (under 10 words)
2. **Value Propositions** (3-5, one sentence each)
3. **Elevator Pitch** (75 words)
4. **Boilerplate** (100-150 words)
5. **Full Brand Story** assessment (exists/partial/missing, with recommendations)

## Step 9: Voice Documentation

Generate a voice chart and writing guidelines:

**Voice Chart:** 4+ rows of "Our Voice IS / Our Voice IS NOT" pairs (e.g., Confident / Arrogant, Helpful / Condescending).

**Do's and Don'ts:** 5+ specific, evidence-based writing instructions per category drawn from the analysis.

## Step 10: Copy Samples

Write 5-8 sample pieces in the identified brand voice covering: homepage headline, product description, blog opening, social post, email subject line, CTA button, error message, thank-you message.

These samples are the most valuable deliverable — writers learn voice by example.

## Output Format

Generate `BRAND-VOICE.md` with these sections:

```markdown
# Brand Voice Guidelines — [Brand Name]
### Analysis Date: [Date]

## Voice Summary
[2-3 sentence summary]

## Voice Dimensions
### Formal <-----> Casual: [X/10]
[Evidence]
### Serious <-----> Playful: [X/10]
[Evidence]
### Technical <-----> Simple: [X/10]
[Evidence]
### Reserved <-----> Bold: [X/10]
[Evidence]

### Visual Voice Map
Formal    |----[X]----------------------------------| Casual
Serious   |--------[X]------------------------------| Playful
Technical |------------------[X]--------------------| Simple
Reserved  |------------[X]--------------------------| Bold

## Brand Personality
Primary/Secondary Archetype with evidence

## Tone by Context
[Table with context, tone, example quotes]

## Vocabulary
Words We Use | Words We Avoid | Signature Phrases

## Voice Chart
| Our Voice IS | Our Voice IS NOT |
|---|---|

## Writing Guidelines
### Do's
### Don'ts

## Brand Messaging Hierarchy
Tagline → Value Props → Elevator Pitch → Boilerplate

## Copy Samples
[5-8 diverse examples]

## Competitor Voice Comparison
[Matrix and differentiation analysis]

## Consistency Audit
[Channel assessment, Overall Score: X/10]

## Recommendations
### Immediate Actions
### Voice Evolution Opportunities
### Consistency Improvements
```

## Key Principles

- Provide **evidence** (quoted examples) for every assessment — never make unsupported claims about voice.
- The guide must be usable by someone who has never worked with the brand. A new copywriter should write on-brand content after reading it.
- Voice is the consistent personality; tone shifts by context. Both must be documented.
- Copy samples are the highest-value deliverable — make them diverse across contexts.
- Plot voice dimensions visually so stakeholders grasp positioning at a glance.
