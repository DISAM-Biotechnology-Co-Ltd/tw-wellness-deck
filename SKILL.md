---
name: tw-wellness-deck
description: Turn prepared content and product/brand references into polished PPTX or HTML presentations for Taiwan health, wellness, skincare, and beauty products. Use for visual direction, slide design, deck production, and layered slides with generated images, simulated packaging, and vector icons; treat claims as source-dependent and flag wording that needs review.
---

# Taiwan Wellness Deck

Create presentation decks for Taiwan health food, supplement, functional food, skincare, and beauty product contexts. Inputs usually include:

- Markdown content for the deck narrative.
- One or more product DM/reference images.
- Optional product photos, ingredient images, logos, certificates, charts, or old slides.
- Optional image annotations in the Markdown (slide, type, prompt) and each product's packaging status.
- Desired output: PPTX, single-file HTML, or both.

The skill's job is to extract the reference material's visual language, convert prepared content into a coherent deck, preserve source traceability, and flag claims that need review. It produces the presentation; it does not treat a visual redesign as evidence research, regulatory approval, or a claims audit.

Important boundary: DM/reference analysis is internal design work. Do not add a "Visual DNA", "design extraction", "creative brief", or process-explanation slide to the final deck unless the user explicitly asks for it. The final deck should present the Markdown's product narrative in the DM-derived visual system.

## Workflow

### 1. Intake

Confirm only what materially affects the work. Ask at most 1-3 questions when missing, grouping related choices where useful:

- Output format: PPTX, HTML, or both.
- Audience and use: sales briefing, distributor training, consumer seminar, investor pitch, product launch, e-commerce livestream, or internal education; clarify whether it will be presented live, read later, or both when that affects density.
- Target slide count or presentation time. If neither is specified, use 8–10 slides including the cover, keep any appendix separate, and state the assumption. Do not add content just to reach the default count.
- Packaging status for each product shown, when the Markdown does not state it: `final` or `concept`. Never infer it.

If the user supplied enough context, proceed and state assumptions.

### 2. Inspect Inputs

Read the Markdown first and identify:

- Product category and hero promise.
- Audience pain points and desired transformation.
- Ingredient/mechanism claims, evidence level, and risky wording.
- Sources attached to claims, figures, comparisons, and product facts; distinguish user-provided facts from independently verified sources.
- Required slides, charts, tables, or before/after material.
- Image annotations and packaging status. Read `references/image-assets.md` when either is present, or when the deck uses generated images or icons.
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
Image style lock:
Packaging status:
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

Screen image prompts with the same care: follow the compliance limits in `references/image-assets.md` before generating anything.

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

### 6. Image Assets

#### Mandatory image-generation gate for annotated decks

When the authoritative slide Markdown contains a slide marked `插圖評估：需要` with an associated `插圖 Prompt`, treat that prompt as a required generated visual. This is a production requirement, not an optional suggestion. Native charts, text, shapes, product packshots, stock images, or a note saying “no generated images” do not satisfy it.

Before building slides:

1. Count every required slide prompt and add one entry per required source page to `image-plan.json`. Preserve the source prompt verbatim as `source_prompt`; put DM style-lock additions in a separate `generation_prompt` field.
2. Screen every prompt against compliance and packaging rules. For a final package, generate a product-free scene or background and layer the user's untouched package photo separately. Never ask the model to create, repair, or redraw final package artwork.
3. Run one representative image-and-slide pilot and inspect it. Then call the system `image_gen` tool for every remaining required prompt. Record `generation_tool: "image_gen"`, each saved asset path, and the PPTX slide where it is used.
4. Keep a one-to-one mapping between required source prompts and manifest entries. If one prompt requires multiple generated files, list every file under that entry's `asset_paths` array.

Do not silently replace an annotated generated visual with editable shapes, a stock image, or an existing product photo. If image generation is unavailable or a prompt cannot be made compliant, stop before final export and report the exact slide and blocker. Ask the user only for a decision needed to resolve that blocker.

Slides marked `插圖評估：不需要` remain eligible for native, editable charts and diagrams and do not trigger image generation.

For PPTX delivery, validate the candidate deck before finalization with `scripts/check_required_image_assets.py`. Every required page must have a matching manifest entry, a generated asset file, and that exact image embedded on the mapped slide. Any missing item blocks finalization. Report required, generated, and embedded counts in private QA notes; do not call the deck complete while the counts differ.

When the deck uses generated images, packaging, or icons, follow `references/image-assets.md`:

- Parse every `插圖評估：需要` / `插圖 Prompt` pair in the authoritative slide Markdown and treat each pair as mandatory. Populate `image-plan.json` and `image-plan.md`; never omit a required entry because a native diagram seems sufficient.
- For `concept` packaging, stop for the user to approve one package master before building slides that show it. Reuse that one file throughout the deck.
- Build and check one pilot slide before generating the full set, unless the user says to skip it.
- Generate through the system `imagegen` skill, verify each result, and copy approved files into the deck's asset folder.

### 7. Output Selection

For PPTX:

- Use the `presentations:Presentations` workflow and its supported artifact tools when available, and request an explicit local `.pptx` file so it does not route to another destination. If unavailable, use another available PPTX method that can produce the requested file; preserve editability where practical and state any QA limitation. Never claim a check passed unless it was actually run.
- Build a real `.pptx`, not only an outline.
- Use extracted palette, typography direction, and motifs consistently.
- Prefer editable shapes/text over flattened screenshots.
- Keep backgrounds, cutouts, packages, icons, and text as separate layers, in the order set by `references/image-assets.md`.
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

### 8. Visual System Rules

Convert the DM into a small design system:

- 3-5 core colors with roles, not a random palette.
- 2 font directions: display and body. Use locally available or common fallback fonts.
- 4-8 repeatable slide layouts.
- 2-4 motifs/patterns derived from the DM.
- 1 product hero treatment.
- 1 image style lock for all generated images.
- 1 icon set and stroke style.
- 1 evidence/ingredient treatment.
- 1 CTA/closing treatment.

Do not copy the DM pixel-for-pixel. Adapt its visual identity into a presentation system.
Do not add the design-system description itself to the deck unless explicitly requested.

### 9. Review Before Delivery

Read `references/output-checklist.md` and run the checklist before final response.

Minimum checks:

- Potentially medicalized or unsupported claims are removed or flagged; do not describe wording as approved based only on a source or disclaimer.
- Each material claim, number, comparison, certification, and product fact has a traceable source or is clearly marked as user-provided / unverified in working notes; public-facing slides do not present unsupported claims as established fact.
- Product/ingredient names are consistent.
- Visual style visibly matches the DM reference.
- Final deck contains product/marketing content only; internal analysis pages such as Visual DNA, creative brief, extraction table, or process notes are absent unless requested.
- Chinese text is readable on projection.
- Product images, callout cards, badges, and decorative motifs do not overlap or obscure text at common desktop and mobile viewports. A `background` layer may sit behind text when the rendered contrast is readable.
- Slides are layered: no flattened slide images, all text is native, and icons are vector.
- Required image-generation audit passed: every source slide marked `插圖評估：需要` has its source prompt, `image_gen` asset, existing file, and embedded slide placement recorded in the manifest and checked by the validator. A missing asset is a release blocker.
- Packaging matches its status: `final` uses only user files; `concept` uses one approved master throughout, with the visible notice on each slide.
- Layout does not feel like a generic template.
- PPTX/HTML file opens successfully.
- A clean rendered preview or contact sheet was inspected for the final deck. If automated preview is blocked, state the limitation and use the strongest available static checks plus user screenshot iteration.

## Reference Routing

- `references/visual-extraction.md`: read when DM/reference images are provided.
- `references/taiwan-compliance.md`: read for all health food, supplement, functional food, skincare, cosmetic, medical beauty, or claims-sensitive decks.
- `references/deck-patterns.md`: read when deciding slide sequence or layout families.
- `references/production-workflow.md`: read before creating HTML/PPTX files, copying assets, or running QA.
- `references/image-assets.md`: read when the Markdown annotates images or packaging, or when the deck uses generated images or icons.
- `references/output-checklist.md`: read before final delivery.

## Output Notes

Always tell the user:

- What files were created.
- Which visual DNA was applied from the DM, summarized briefly in the response rather than inserted as a deck page.
- Any compliance-sensitive wording that was softened.
- Any unavailable original assets and the fallback copies used.
- Which images were generated, where they and `image-plan.md` are saved, and which products use simulated packaging.
- Which QA checks passed, and any check that could not run because of environment/tool limitations.
- What could be refined if they provide brand fonts, logo files, approved claims, or higher-resolution product photos.
