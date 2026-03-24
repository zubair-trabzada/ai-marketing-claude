---
name: market-landing
description: "Landing page CRO analysis engine. Use when a user shares a landing page URL for conversion optimization, requests a landing page review or conversion audit, or wants to improve conversions on signup, lead capture, or purchase flows. Analyzes headlines, evaluates CTAs, assesses form friction, scores social proof, audits mobile responsiveness, and generates prioritized A/B test recommendations with revenue-impact estimates."
---

# Landing Page CRO Analysis

Use when a user provides a landing page URL and asks for conversion optimization, landing page review, conversion audit, or wants to improve signup, lead capture, or purchase rates. Triggered by `/market landing <url>` or `/market cro <url>`.

## How to Execute

### Step 1: Identify the Page Type
Determine which landing page type to set benchmark expectations and scoring weights.

| Page Type | Primary Goal | Good CR | Great CR |
|---|---|---|---|
| Lead Capture | Email/form submission | 5-10% | 15%+ |
| SaaS Signup | Free trial or freemium signup | 3-7% | 10%+ |
| E-commerce Product | Add to cart / Purchase | 2-4% | 5%+ |
| Webinar Registration | Register for event | 20-30% | 40%+ |
| App Download | Install app | 10-15% | 20%+ |
| Waitlist | Join waitlist | 15-25% | 35%+ |
| Consultation Booking | Schedule a call | 5-10% | 15%+ |
| Nonprofit Donation | Make a donation | 2-5% | 8%+ |

### Step 2: Run the 7-Point CRO Framework
Analyze each section in order. Score each section 1-10 and provide specific findings.

#### Section 1: Hero Section (Weight: 25%)
The first screen a visitor sees. This is where 80% of conversion decisions begin.

**Checklist:**
- [ ] Headline is visible within 2 seconds of page load
- [ ] Headline communicates the primary benefit (not a feature)
- [ ] Headline is under 10 words
- [ ] Subheadline expands on the headline with specificity
- [ ] Primary CTA is above the fold
- [ ] CTA button color contrasts with the background
- [ ] CTA text is action-oriented (not "Submit" or "Click Here")
- [ ] Hero image or video supports the message (not generic stock)
- [ ] Trust badges or social proof visible above the fold
- [ ] Page loads in under 3 seconds
- [ ] No navigation menu competing with the CTA (for dedicated landing pages)

**Scoring guide:** 9-10 = benefit-driven headline + clear contrasting CTA + supporting visual + trust indicators. Deduct points for: generic/feature-focused headline, CTA below fold, missing trust badges, stock imagery, slow load.

#### Section 2: Value Proposition (Weight: 20%)
How clearly the page communicates WHY someone should convert.

**Checklist:**
- [ ] Clear statement of what the product/service does
- [ ] Specific outcomes or results promised
- [ ] Differentiation from alternatives (why THIS solution)
- [ ] Target audience is clear (visitor knows if this is for them)
- [ ] Benefits are quantified where possible (save X hours, increase Y%)
- [ ] Value proposition is scannable (not buried in paragraphs)

**Evaluate Using the 4U Framework:**
1. **Useful** - Does it solve a real problem the visitor has?
2. **Urgent** - Is there a reason to act now?
3. **Unique** - Is it different from competitors?
4. **Ultra-specific** - Are claims concrete, not vague?

#### Section 3: Social Proof (Weight: 15%)
Evidence that others trust and benefit from this product/service.

**Social proof types (strongest first):** Revenue/results metrics > named testimonials with photos > client logos > case studies > star ratings > media mentions > certifications > UGC > follower counts.

**Checklist:**
- [ ] At least 2 types of social proof present
- [ ] Testimonials include real names and photos
- [ ] Testimonials mention specific results or outcomes
- [ ] Social proof is placed near decision points (close to CTAs)
- [ ] Numbers are specific (not rounded - "11,847" beats "10,000+")
- [ ] Logos are recognizable to the target audience
- [ ] Social proof is recent and relevant

#### Section 4: Features and Benefits (Weight: 15%)
How the page presents what the product/service includes.

**Checklist:**
- [ ] Features are translated into benefits (what the feature DOES for the user)
- [ ] Content is scannable (icons, bullet points, short paragraphs)
- [ ] Visual hierarchy guides the eye through features
- [ ] Most important features/benefits are listed first
- [ ] Each feature section has a clear mini-headline
- [ ] Screenshots, demos, or visuals accompany feature descriptions
- [ ] Feature list is comprehensive but not overwhelming (3-7 key features)

**Feature-to-Benefit Translation Check:**
Bad: "AI-powered analytics dashboard"
Good: "See exactly which campaigns drive revenue -- AI analyzes your data so you don't have to"

#### Section 5: Objection Handling (Weight: 10%)
How the page addresses reasons a visitor might NOT convert.

**Common Objections by Page Type:**

| Objection | How to Address |
|---|---|
| "Too expensive" | ROI calculator, price comparison, money-back guarantee |
| "Not sure it works" | Case studies, free trial, demo video |
| "Too complicated" | Setup wizard, onboarding support, "get started in 5 minutes" |
| "Not sure I need it" | Problem agitation, cost of inaction |
| "What if I don't like it?" | Free trial, money-back guarantee, cancel anytime |
| "Is my data safe?" | Security badges, compliance logos, privacy policy link |
| "I need to ask my team" | Shareable comparison page, team trial, ROI one-pager |

**Checklist:**
- [ ] FAQ section addresses top 3-5 objections
- [ ] Risk reversals present (guarantee, free trial, cancel anytime)
- [ ] Pricing transparency (no hidden fees or surprise costs)
- [ ] Security and privacy indicators where relevant
- [ ] Comparison with alternatives (if applicable)

#### Section 6: Call-to-Action (Weight: 10%)
The conversion mechanism itself.

**CTA Button Checklist:**
- [ ] CTA text describes the VALUE, not the action ("Get My Free Report" vs "Submit")
- [ ] CTA button is visually dominant (size, color, whitespace)
- [ ] CTA appears multiple times on long pages
- [ ] Secondary CTA exists for visitors not ready to commit
- [ ] CTA has supporting microcopy (e.g., "No credit card required")
- [ ] Button text uses first person ("Start MY trial" vs "Start YOUR trial")
- [ ] CTA is specific to the offer (not generic)

**CTA copy strength:** Weak = "Submit", "Click Here" | Medium = "Sign Up", "Get Started" | Strong = "Start My Free Trial", "Get My Custom Report"

#### Section 7: Footer and Secondary Elements (Weight: 5%)
The bottom of the page and supporting elements.

**Checklist:**
- [ ] Final CTA present at bottom of page
- [ ] Contact information or support options visible
- [ ] Privacy policy and terms of service linked
- [ ] Trust badges repeated near final CTA
- [ ] No competing links that lead away from conversion
- [ ] Copyright and legal information present
- [ ] Social media links (only if they support conversion, not distract)

### Step 3: Copy Scoring
Score the overall page copy on 5 dimensions (1-10 each):

1. **Clarity** - Can a visitor understand the offer in 5 seconds?
2. **Urgency** - Is there a reason to act NOW vs later?
3. **Specificity** - Are claims concrete with numbers, timeframes, outcomes?
4. **Proof** - Are claims backed by evidence, data, or testimonials?
5. **Action Orientation** - Does the copy drive toward a specific next step?

Calculate the Copy Score: average of all 5 dimensions, multiplied by 10 for a score out of 100.

### Step 4: Form Optimization Audit
If the page has a form, evaluate:

| Element | Best Practice |
|---|---|
| Field count | Every additional field reduces conversion ~7%. Lead capture: 3-5 fields max. |
| Labels | Use inline labels or floating labels. Avoid placeholder-only labels. |
| Button text | Match the value proposition. "Get My Free Guide" > "Submit". |
| Error handling | Inline validation. Specific error messages. Don't clear the entire form on error. |
| Multi-step | Break long forms into steps with progress indicator. |
| Required vs optional | Mark optional fields, not required ones. |
| Auto-fill | Enable browser auto-fill for standard fields. |
| Field types | Use appropriate input types (email, tel, url) for mobile keyboards. |

### Step 5: Mobile Responsiveness Audit
Mobile accounts for 60%+ of web traffic. Check:

- [ ] CTA is thumb-reachable (bottom half of screen)
- [ ] Text is readable without zooming (16px minimum body text)
- [ ] Forms are usable on mobile (large tap targets, appropriate keyboards)
- [ ] Images resize properly and don't break layout
- [ ] No horizontal scrolling required
- [ ] Page loads under 3 seconds on 4G
- [ ] Click-to-call for phone numbers
- [ ] Sticky CTA bar on scroll (if applicable)

### Step 6: Page Speed Impact Assessment
Conversion drops roughly 7% at 2-3s, 20% at 3-5s, 35% at 5-8s, and 50%+ beyond 8s. Flag these common issues:
- Unoptimized images (recommend WebP, lazy loading)
- Render-blocking JS, unminified CSS/JS
- Missing browser caching or CDN
- Excessive third-party scripts

### Step 7: Generate A/B Test Recommendations
Format each test as a hypothesis:

**Template:**
"If we [CHANGE], then [METRIC] will [IMPROVE/INCREASE] because [REASON]."

**Common test areas:** headline wording, CTA color/text, social proof placement, form field count, hero image vs video, page length, urgency elements, price anchoring, testimonial format, live chat widget.

### Step 8: Heat Map Interpretation Guidance
Even without actual heat map data, provide guidance on:

- **Expected attention zones** based on page layout
- **F-pattern vs Z-pattern** reading based on content density
- **Scroll depth predictions** based on page length and content breaks
- **Click probability zones** based on visual hierarchy
- **Rage click indicators** (elements that look clickable but aren't)
- **Dead zones** where content may be ignored

## Output Format

Generate a file called `LANDING-CRO.md` in the project root or output directory with:

```markdown
# Landing Page CRO Analysis
## [Page URL]
### Analysis Date: [date]

---

## Overall CRO Score: [X/100]

## Page Type: [identified type]
## Current Estimated Conversion Rate: [estimate based on findings]
## Target Conversion Rate: [realistic improvement target]

---

## Section-by-Section Analysis

### 1. Hero Section [Score: X/10]
**Findings:**
- [specific observations]

**Fixes (Priority: HIGH/MEDIUM/LOW):**
- [specific, actionable recommendations]

[Repeat for all 7 sections]

---

## Copy Score: [X/100]
| Dimension | Score | Notes |
|---|---|---|
| Clarity | X/10 | [notes] |
| Urgency | X/10 | [notes] |
| Specificity | X/10 | [notes] |
| Proof | X/10 | [notes] |
| Action Orientation | X/10 | [notes] |

---

## Form Audit
[findings and recommendations]

---

## Mobile Audit
[findings and recommendations]

---

## A/B Test Recommendations
1. [Hypothesis format test]
2. [Hypothesis format test]
3. [Hypothesis format test]

---

## Prioritized Fix List

### Quick Wins (implement this week)
1. [fix with expected impact]

### Medium-Term (implement this month)
1. [fix with expected impact]

### Strategic (implement this quarter)
1. [fix with expected impact]

---

## Before/After Wireframe Suggestions
[Text-based wireframe descriptions of current vs recommended layout]
```

## Key Principles
- **Tie every recommendation to revenue impact** -- e.g., "contrasting CTA color typically lifts clicks 15-30%, meaning ~X more conversions/month at your traffic."
- **Prioritize by effort-to-impact ratio.** Quick wins first.
- **Be specific and actionable** -- rewrite the actual headline, don't just say "improve it."
- **Reference industry benchmarks** so the client sees where they stand.
- If browser access is available, reference specific page elements. If `/market audit` was run previously, incorporate those findings.
