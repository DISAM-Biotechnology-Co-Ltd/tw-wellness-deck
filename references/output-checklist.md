# Output Checklist

Run this before delivery.

## Input Integrity

- Markdown content has been fully reviewed.
- Final slide/section list maps to the Markdown content unless the user requested restructuring or compliance required changes.
- Every DM/reference image was inspected or noted as unavailable.
- Asset inventory is complete: original paths, readability, local working copies, and fallback substitutions are recorded.
- Product name, ingredient names, dosage/use, and audience are consistent.
- Each material claim, figure, comparison, certification, and product fact has a traceable source, or is clearly identified in working notes as user-provided or unverified.
- Sources about an ingredient are not presented as finished-product evidence; key study conditions and comparison bases are retained where relevant.
- User-provided brand assets are preserved and not redrawn without permission.
- Internal notes such as visual extraction tables, creative briefs, and process explanations are not inserted into the final deck unless explicitly requested.

## Visual Fit

- Palette visibly comes from the DM/reference, with clear color roles.
- Typography direction matches the brand personality.
- Slide layouts adapt the DM structure but are readable as presentation slides.
- Product image appears prominently in cover and relevant selling slides.
- Motifs are repeated consistently and do not clutter content.
- No generic template look remains.
- Product photos, badges, callout cards, and decorative arcs/patterns do not cover title, body, labels, dosage text, CTA chips, or each other.

## Taiwan Compliance

- Disease, treatment, cure, and prevention claims are removed or explicitly marked for qualified review; a source or disclaimer alone does not establish approval.
- Ingredient evidence is not overstated as finished-product proof.
- Cosmetic wording stays within appearance, moisture, texture, comfort, and routine support unless approved.
- Before/after or efficacy visuals include conservative framing.
- Distributor/sales talking points include safe phrases and do-not-say guidance when needed.
- Suggested wording from the compliance reference has not been treated as pre-approved; current official requirements were checked when the material is intended for public-facing use.

## PPTX Quality

- Text remains editable where practical.
- Artifact-tool was used through the `presentations:Presentations` workflow when available; `python-pptx` was not used for new decks.
- Body text is projection-readable.
- Margins are consistent.
- Images are not blurry, stretched, or accidentally cropped.
- Charts/tables are simplified for presentation.
- File opens successfully.
- Source notes appear on slides containing material claims, figures, or comparisons; full citation details are included on-slide or in a delivered `references.md` keyed to the slide notes.
- One PNG per slide was rendered.
- A clean contact sheet was built from slide PNGs only and visually inspected.
- Overflow/slide bounds testing passed, or the limitation is reported.
- Inspect/search confirms no internal process pages or terms remain in the final deck.

## HTML Quality

- `index.html` opens locally.
- Asset paths are relative and correct.
- Mobile and desktop framing are acceptable if sharing online.
- No external dependency is required unless disclosed.
- Text does not overlap at common viewport sizes.
- Hero sections use normal flow/grid/flex for adjacent callouts whenever possible; any absolute-positioned overlays have been checked for overlap at wide desktop, laptop, tablet, and phone widths.
- If automated browser inspection is blocked for a `file://` URL, note that limitation and perform static CSS review plus user-supplied screenshot iteration instead of claiming visual verification.

## Final Response

Tell the user:

- Created file path(s).
- Extracted visual DNA.
- Deck structure used.
- Claim-sensitive wording changed or flagged.
- Any missing assets that would improve the next iteration.
