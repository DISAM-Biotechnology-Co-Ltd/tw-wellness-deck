---
name: tw-wellness-deck
description: Turn prepared content and product/brand references into polished PPTX or HTML presentations for Taiwan health, wellness, skincare, and beauty products. Use for visual direction, slide design, and deck production; treat claims as source-dependent and flag wording that needs review.
---

# Taiwan Wellness Deck

Create presentation decks for Taiwan health food, supplement, functional food, skincare, and beauty product contexts. Inputs usually include:

- Markdown content for the deck narrative.
- One or more product DM/reference images.
- Optional product photos, ingredient images, logos, certificates, charts, or old slides.
- Desired output: PPTX, single-file HTML, or both.

The skill's job is to extract the reference material's visual language, convert prepared content into a coherent deck, preserve source traceability, and flag claims that need review. It produces the presentation; it does not treat a visual redesign as evidence research, regulatory approval, or a claims audit.

Important boundary: DM/reference analysis is internal design work. Do not add a "Visual DNA", "design extraction", "creative brief", or process-explanation slide to the final deck unless the user explicitly asks for it. The final deck should present the Markdown's product narrative in the DM-derived visual system.

## Workflow

### 1. Intake

Confirm only what materially affects the work. Ask at most 1-3 questions when missing, grouping related choices where useful:

- Output format: PPTX, HTML, or both.
- Audience and use: sales briefing, distributor training, consumer seminar, investor pitch, product launch, e-commerce livestream, or internal education; clarify whether it will be presented live, read later, or both when that affects density.
- Target slide count or presentation time. If neither is specified, use 8–10 slides including the cover, keep any appendix separate, and state the assumption. Do not add content just to reach the default count.

If the user supplied enough context, proceed and state assumptions.

### 2. Inspect Inputs

Read the Markdown first and identify:

- Product category and hero promise.
- Audience pain points and desired transformation.
- Ingredient/mechanism claims, evidence level, and risky wording.
- Sources attached to claims, figures, comparisons, and product facts; distinguish user-provided facts from independently verified sources.
- Required slides, charts, tables, or before/after material.
- The intended slide/page list. Preserve this content plan unless the user asks for restructuring or it is necessary for compliance/readability.

Read `references/production-workflow.md` before copying assets or creating files. Build an asset inventory that records each user-provided path, whether it is currently readable, and which local working copy will be used. If a prior turn created a local copy of a now-missing reference image, reuse that copy only after noting the fallback in the working notes and final response.

Inspect every DM/reference image. Use visual inspection tools when images are local. Extract:

- Color system: dominant, secondary, accent, background, metallic/gradient usage.
- Typography character: serif/sans, rounded/geometric, high-end/lab/organic/K-beauty/minimal.
- Layout grammar: dense DM, editorial spread, clinical grid, luxury beauty, ingredient story, before/after, certificate wall.
- Visual motifs: botanical extracts, capsules, serum drops, molecular lines, skin texture, leaves, waves, ribbons, badges, seals, QR blocks.
- Photo treatment: cutout product pack, soft shadow, glossy reflection, macro ingredient, model lifestyle, lab scene.
- Brand voice: premium, medical-professional, natural, friendly Taiwanese, youthful, technical, Japanese/Korean influenced.

Read `references/visual-extraction.md` before finalizing the art direction.

Do not treat the DM as deck content by default. Use product cutouts, logos, package photos, and approved product assets when they support the Markdown narrative, but do not place a full DM screenshot or DM analysis table into the final deck unless requested.

### 3. Build The Creative Brief

Before making slides, write a compact creative brief:

```text
Product:
Audience/use:
Output:
Deck length:
Visual DNA:
Palette:
Typography direction:
Layout rules:
Motifs/assets:
Claim risk notes:
Assumptions:
```

Use this brief as the deck contract, but keep it outside the final deck unless requested. It may be saved as a separate notes file when useful. If a DM image and Markdown conflict, preserve product/brand identity from the DM and restructure the Markdown around it.

### 4. Claim and Compliance Pass

Preserve the user's supplied wording unless the user asks for copy editing or claim review. Do not invent efficacy claims or present a suggested rewrite as approved wording. Flag risky or unsupported wording and keep its review status visible in working notes. This skill's wording guidance is not regulatory approval.

Read `references/taiwan-compliance.md` when:

- The deck mentions efficacy, disease, treatment, prevention, clinical effect, immune claims, slimming, whitening, anti-aging, hair growth, hormones, children, pregnancy, or chronic disease.
- The product is a health food, supplement, functional food, skincare, medical beauty, or cosmetic.
- The user asks for sales copy, claims, labeling, advertising, or distributor material.

For claims intended for public-facing use, and whenever the user asks whether wording is allowed, verify current rules against official Taiwan sources before proposing final wording. Treat any alternatives in `references/taiwan-compliance.md` as draft candidates only: confirm they fit the product category, evidence, and intended use. If a claim cannot be verified, flag it for review or omit it from public-facing copy; do not imply that a disclaimer makes it acceptable.

Before layout, create a compact internal claim/source map for every material efficacy claim, number, comparison, certification, and product fact. Record the exact wording or value, source, source type, whether it concerns an ingredient or finished product, and any relevant population, dose, conditions, or limitations. Do not invent missing details. Keep this map outside the final deck unless requested, and put a concise source note on the relevant slide or chart whenever a factual claim or figure is presented.

### 5. Deck Architecture

Choose the deck structure from `references/deck-patterns.md`.

Common structures:

- **Sales deck**: Hook -> product pain point -> ingredient logic -> evidence -> product superiority -> SKU/use -> closing.
- **Training deck**: Market context -> product principles -> ingredient education -> customer Q&A -> compliant talking points.
- **Launch deck**: Brand mood -> product hero -> problem -> formulation -> proof -> campaign assets -> call to action.
- **Scientific-commercial deck**: Mechanism -> evidence hierarchy -> formula rationale -> target audience -> claim-safe copy.
- **HTML showcase**: product-first, DM-inspired, swipeable or scrollable presentation for live demo or sharing.

Keep Taiwan audiences in mind: readable Traditional Chinese by default, clean hierarchy, concrete product information, clear product images, and evidence cues that can be traced to their sources.

When the Markdown already contains explicit slide headings, map each heading to a slide/section first. Add, remove, or merge slides only for compliance, readability, or a user-requested format shift. Do not add standalone methodology pages.

### 6. Output Selection

For PPTX:

- Use the `presentations:Presentations` workflow and its supported artifact tools when available. If unavailable, use another available PPTX method that can produce the requested file; preserve editability where practical and state any QA limitation. Never claim a check passed unless it was actually run.
- Build a real `.pptx`, not only an outline.
- Use extracted palette, typography direction, and motifs consistently.
- Prefer editable shapes/text over flattened screenshots.
- Follow `references/production-workflow.md` for workspace setup, asset copying, render/inspect QA, and final deliverable checks.

For HTML:

- Use a single-file HTML deck unless the user asks for a web app.
- Make it openable locally without a build step.
- Keep assets in an `images/` folder next to `index.html` when needed.
- Use CSS variables for palette and motif rules.
- Verify in a browser when possible.
- Prefer ordinary document flow and CSS grid/flex for hero layouts. Avoid absolute-positioned product callouts unless overlap is intentionally designed and tested at desktop, tablet, and mobile widths.
- For product hero sections, constrain product images with both width and max-height, and ensure nearby badges/cards remain in normal flow or in a non-overlapping grid area.
- Follow `references/production-workflow.md` for local asset paths, file-url/browser limitations, and screenshot or static-review fallback.

If both are requested, create HTML first only when it helps visual prototyping; otherwise create PPTX first and derive HTML from the approved structure.

### 7. Visual System Rules

Convert the DM into a small design system:

- 3-5 core colors with roles, not a random palette.
- 2 font directions: display and body. Use locally available or common fallback fonts.
- 4-8 repeatable slide layouts.
- 2-4 motifs/patterns derived from the DM.
- 1 product hero treatment.
- 1 evidence/ingredient treatment.
- 1 CTA/closing treatment.

Do not copy the DM pixel-for-pixel. Adapt its visual identity into a presentation system.
Do not add the design-system description itself to the deck unless explicitly requested.

### 8. Review Before Delivery

Read `references/output-checklist.md` and run the checklist before final response.

Minimum checks:

- Potentially medicalized or unsupported claims are removed or flagged; do not describe wording as approved based only on a source or disclaimer.
- Each material claim, number, comparison, certification, and product fact has a traceable source or is clearly marked as user-provided / unverified in working notes; public-facing slides do not present unsupported claims as established fact.
- Product/ingredient names are consistent.
- Visual style visibly matches the DM reference.
- Final deck contains product/marketing content only; internal analysis pages such as Visual DNA, creative brief, extraction table, or process notes are absent unless requested.
- Chinese text is readable on projection.
- Product images, callout cards, badges, and decorative motifs do not overlap or obscure text at common desktop and mobile viewports.
- Layout does not feel like a generic template.
- PPTX/HTML file opens successfully.
- A clean rendered preview or contact sheet was inspected for the final deck. If automated preview is blocked, state the limitation and use the strongest available static checks plus user screenshot iteration.

## Reference Routing

- `references/visual-extraction.md`: read when DM/reference images are provided.
- `references/taiwan-compliance.md`: read for all health food, supplement, functional food, skincare, cosmetic, medical beauty, or claims-sensitive decks.
- `references/deck-patterns.md`: read when deciding slide sequence or layout families.
- `references/production-workflow.md`: read before creating HTML/PPTX files, copying assets, or running QA.
- `references/output-checklist.md`: read before final delivery.

## Output Notes

Always tell the user:

- What files were created.
- Which visual DNA was applied from the DM, summarized briefly in the response rather than inserted as a deck page.
- Any compliance-sensitive wording that was softened.
- Any unavailable original assets and the fallback copies used.
- Which QA checks passed, and any check that could not run because of environment/tool limitations.
- What could be refined if they provide brand fonts, logo files, approved claims, or higher-resolution product photos.
