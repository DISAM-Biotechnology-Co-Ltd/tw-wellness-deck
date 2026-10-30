# Visual Extraction From Taiwan Product DM

Use this guide when the user provides product DM images, package photos, or reference designs.

## Extraction Table

Create a concise table before designing. This table is an internal working note, not a final deck slide, unless the user explicitly asks to show visual analysis.

| Element | Observed From DM | Deck Translation |
|---|---|---|
| Palette | dominant/background/accent | CSS/PPT theme color roles |
| Typography | display/body/labels | title/body/caption font direction |
| Layout | grid, density, section rhythm | repeatable slide layouts |
| Motifs | botanicals, molecules, waves, capsules | background marks, dividers, icons |
| Imagery | product pack, ingredients, model, lab | hero treatment and image slots |
| Tone | premium, clinical, natural, youthful | copy tone and hierarchy |

## Palette Heuristics

Extract color roles, not just swatches:

- **Base**: page background or product packaging field.
- **Ink**: main text color.
- **Accent**: CTA, badge, ingredient highlight, or claim marker.
- **Soft field**: tint for cards, tables, or ingredient blocks.
- **Premium effect**: gold, silver, pearl, translucent white, gloss, gradient.

For Taiwan wellness/beauty decks, common but distinct directions:

- Clinical trust: white, navy, cyan, cool gray, thin lines.
- Botanical/natural: ivory, forest green, sage, kraft, warm neutral.
- Premium beauty: off-white, champagne gold, blush, deep brown/black.
- Functional ingredient: white, cobalt/teal, molecular accent, clean charts.
- Youth/social commerce: bright accent, large numbers, sticker-like badges.

Keep dominant colors restrained; use accent color for navigation, ingredient tags, KPI numbers, and CTA.

## Typography Heuristics

Infer font personality:

- High-end beauty: elegant serif or high-contrast display + light sans body.
- Clinical/professional: geometric sans, tight grid, small labels.
- Natural/herbal: soft serif, rounded sans, warm spacing.
- Youthful: rounded sans, bold badges, playful hierarchy.
- Japanese/Korean influenced skincare: airy sans, generous whitespace, fine rules.

Use safe fallbacks if brand fonts are unavailable:

- Chinese sans: `Noto Sans TC`, `PingFang TC`, `Microsoft JhengHei`.
- Chinese serif: `Noto Serif TC`, `Songti TC`, `PMingLiU`.
- English sans: `Inter`, `Helvetica Neue`, `Arial`.
- English serif: `Cormorant Garamond`, `Playfair Display`, `Georgia`.

Do not use tiny DM-style text on slides. Presentation body text should usually be 18 pt or larger in PPT, and visually equivalent in HTML.

## Layout Translation

Turn DM composition into deck layouts:

- Product packshot + headline -> cover and section openers.
- Ingredient blocks -> formula rationale slides.
- Dense DM feature list -> 3-5 benefit cards.
- Certificate rows -> proof/evidence wall.
- Before/after visuals -> controlled comparison layout with disclaimers.
- Icons around product -> radial or orbit diagram.
- Timeline/steps -> usage routine or mechanism flow.
- QR/CTA area -> closing slide or contact slide.

Avoid adding a deck section that explains this translation. The final audience should see the resulting visual style and product story, not the design process.

## Motif Adaptation

Use motifs lightly and consistently:

- Botanical line art as corner marks or section dividers.
- Molecular network as low-opacity background, not fake science clutter.
- Serum drops/capsules as icon shapes for product formats.
- Gold foil as thin rules, small labels, or key numbers.
- Soft gradients only if the DM uses luminous skincare language.
- Ingredient photography should support claims; do not invent ingredients absent from the product.

## Image Handling

- Preserve product package proportions.
- Avoid cropping away brand, dosage, key ingredient, or certification marks.
- Use cutout product images when available; otherwise frame DM/product photo cleanly.
- If screenshot or DM text is low-resolution, recreate the information as editable deck text instead of enlarging blur.
- Do not fabricate official badges, certifications, clinical logos, or government marks.
- Do not use a full DM screenshot as a content slide when the user supplied Markdown deck copy. Treat the DM as a style/reference source unless the Markdown asks for a DM audit, before/after comparison, or reference appendix.
- Keep product images and callout cards in separate grid/flex areas when possible. If using absolute-positioned badges or cards, test that they do not cover labels, dosage, CTA chips, or body copy.
