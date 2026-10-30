# Production Workflow

Use this reference before creating HTML or PPTX output.

## Asset Inventory

Create a short working inventory before authoring:

| Asset | Original path | Readable now? | Working copy | Role |
|---|---|---|---|---|

Rules:

- Copy readable user assets into the output or scratch `images/` / `assets/` folder before authoring. Run directory creation before copy operations; do not parallelize dependent `mkdir` and `cp`.
- If an original path is unavailable, search only the current workspace and prior output folders for an existing local copy. Do not silently substitute an unrelated image.
- Preserve product packshots and logos as concrete assets. Use DM screenshots as style references by default, not slide content.
- Record fallback copies in the final response when an original asset was unavailable.

## Content Boundary

- Map final slides/sections from the user's Markdown first.
- Keep creative briefs, visual extraction tables, QA notes, and implementation notes outside the final deck unless requested.
- If creating both HTML and PPTX, derive both from the same slide list and content boundary.
- Put a concise source note on the slide with each material claim, figure, or comparison. If the full citation will clutter the slide, use a short citation key there and deliver a matching `references.md` beside the deck; do not rely on working notes or source files the audience will not receive.

## PPTX Production

When the `presentations:Presentations` workflow is available:

- Use `@oai/artifact-tool` through JavaScript ES modules; do not use `python-pptx`.
- Set up the artifact-tool workspace before running generated modules.
- Put generated source and temporary QA files under a scratch `tmp/` folder. Export only the final `.pptx` to `outputs/` unless the user asks otherwise.
- Keep visible text editable wherever practical. Use native text boxes, shapes, tables, and simple diagrams; use product images only for real raster assets.
- Use at least 50 px for cover titles, 35 px for slide titles, 24 px for subheads/callout headings, and 16 px for body/table text unless a supplied template dictates otherwise.
- Avoid absolute-positioned badges over product photos unless a rendered preview proves they do not cover text, dosage labels, or callout copy.

If that workflow or its artifact tools are unavailable, use the best available method that produces the requested PPTX. Keep text and shapes editable where practical. Do not let unavailable tooling silently lower the deliverable standard: run the checks that remain possible and state exactly which visual or structural checks could not be performed. Never report a render, open, overflow, or visual-inspection check as passed unless it actually ran.

Minimum PPTX QA:

1. Export one PNG per slide.
2. Export layout JSON or inspect NDJSON.
3. Run the presentation skill's overflow test when available.
4. Generate a clean contact sheet from slide PNGs only; do not include previous montage/contact-sheet files in the contact sheet input folder.
5. Search the inspect output for forbidden internal-process terms such as `Visual DNA`, `creative brief`, `extraction table`, `設計語言`, and `視覺 DNA`.
6. Inspect the contact sheet visually for text overlap, clipped text, product-image collisions, inconsistent slide count, and accidental internal-analysis pages.

## HTML Production

- Use a single `index.html` plus local `images/` folder unless the user asks for a full app.
- Keep all asset paths relative.
- Prefer normal document flow, CSS grid, and flexbox for hero images and callouts. Avoid absolute overlays unless tested at common desktop and mobile widths.
- If browser automation blocks a `file://` page, say so plainly. Perform static asset/anchor checks and iterate from user screenshots instead of claiming visual verification.

## Validation Fallbacks

- If automated PPTX rendering or overflow inspection is unavailable, verify that the exported file exists and is non-empty, inspect its structure with available tools, and report that rendered visual QA remains incomplete. Do not claim that the slides were visually inspected.
- If a browser preview is unavailable for HTML, complete the available static checks and report that visual browser QA remains incomplete.

- If `quick_validate.py` cannot run because the Python environment lacks `yaml`, run a manual frontmatter check for `name` and `description`, confirm required files exist, and report the dependency limitation.
- If the workspace is not a Git repository, do not rely on `git diff` or `git status`; summarize changed files from the known edit list.
