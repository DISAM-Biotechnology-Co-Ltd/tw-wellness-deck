# Image Assets And Layered Slides

Read this when the Markdown annotates images, when any product packaging must be shown, or when the deck uses generated images or icons.

The goal is a layered deck: every background, cutout, package, icon, and text block stays a separate object that can be moved or replaced.

## Markdown Annotations

Accept the user's annotation style. These forms are preferred, not required.

Product packaging, at the top of the Markdown:

```md
---
products:
  - id: serum_30ml
    packaging: concept          # final / concept
    form: 30ml 滴管玻璃瓶，霧面白瓶身，香檳金瓶蓋
    source_image: images/serum.png   # required for final; reference only for concept
---
```

Image request, inside the slide section it belongs to:

```md
<!-- image
id: p03_hero
type: cutout   # cutout / background / icon
place: right
prompt: 新鮮靈芝子實體，微距攝影，柔和側光
-->
```

Normalize every annotation into the image plan below. If a type or slide is not stated, infer it from the context and record the inference. Ask only when a wrong guess would change what gets generated. Do not add generated images to slides the user did not annotate unless the user asks, or use them to replace supplied real assets.

If the authoritative slide Markdown marks a page `插圖評估：需要` and provides an `插圖 Prompt`, that prompt is a required generated asset. It is not optional merely because native shapes, charts, or an existing product photo can fill the layout. Generate one final visual for every such prompt with the system `image_gen` tool. Do not silently substitute a shape, stock image, or product packshot. If generation is unavailable or the prompt cannot be made compliant, block final delivery and report the exact slide and reason.

## Image Plan

Before generating anything, write the plan:

| Asset ID | Slide | Type | Source | Layer | User prompt | Final prompt | Status | File |
|---|---|---|---|---|---|---|---|---|

Create a machine-readable `image-plan.json` beside this table. Give every required prompt one record and retain the original prompt verbatim in `source_prompt`:

```json
{
  "required_assets": [
    {
      "id": "p04-lifestyle",
      "source_page": 4,
      "source_prompt": "Exact text copied from the slide Markdown",
      "generation_prompt": "Exact prompt sent to image_gen",
      "generation_tool": "image_gen",
      "asset_paths": ["p04-lifestyle.png"],
      "pptx_slide": 4
    }
  ]
}
```

Each asset path is relative to the JSON manifest. `pptx_slide` is one-based and includes the cover. If there is more than one generated file for a prompt, list every file in `asset_paths`.

- `Type`: `background`, `cutout`, `package`, `icon`, `photo`, or `logo`.
- `Source`: `generated`, `user-provided`, or `icon-library`.
- Save the plan as `image-plan.md` in the deck's asset folder. It is a working record, never slide content.

## Image Style Lock

Derive one style lock from the DM and product images, and record it in the creative brief:

```text
Medium:
Lighting:
Palette:
Materials/texture:
Camera/composition:
Avoid:
```

Apply it to every generated image.

- The user's prompt decides the subject and composition. The style lock fills in only what the prompt leaves open. If they conflict, follow the user's prompt and note the conflict.
- Keep the user's prompt intact in the `Primary request` line of the `imagegen` spec. Do not add objects, ingredients, people, or brand elements the user did not ask for.
- When passing the DM or product image to `image_gen`, label it as a style or subject reference, and forbid copying its text, logos, and layout.
- Every generated image prompt includes `no text, no logo, no watermark, no badge, no certification mark`.

## Image Generation

Use the system `imagegen` skill and its built-in `image_gen` tool. Do not use the CLI fallback or change models unless the user confirms it.

Do not spend generations until the plan and compliance screen are done. Tell the user how many images will be generated when the count is large, because image generation uses plan limits faster than ordinary work.

For each required prompt, call the system `image_gen` tool and save its output as a separate asset. A plan entry alone does not count as generation. Run one representative pilot, inspect it, and then generate the remaining required prompts. Keep the exact source prompt and the prompt actually sent to the tool as separate manifest fields.

### Backgrounds

- Request a 16:9 full-bleed image, and state where the low-detail text area must be.
- The built-in tool does not accept a size setting, so check the actual dimensions. Keep important details away from the edges, and place it with `fit: "cover"` so any small mismatch crops without stretching.
- Report the final resolution. Do not upscale silently.
- Keep readability treatment such as a tint or overlay as a separate native shape, not baked into the image.
- A background may repeat across slides. Any other generated image is used once unless this file says otherwise.

### Cutouts

1. Ask `image_gen` for a real transparent background and keep its alpha channel.
2. Verify the alpha from pixel data, for example with Pillow: the file must have an alpha channel, the minimum alpha must be below 255, and the corners must be transparent. A checkerboard or white background seen by eye does not count.
3. If the alpha fails, regenerate once on a flat key color that does not appear in the subject (magenta for green botanicals, green otherwise), then run:

   ```bash
   python "${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/scripts/remove_chroma_key.py" --input <input> --out <output.png> --auto-key border --soft-matte --despill
   ```

4. Inspect the result on both a light and a dark background for halos, color spill, and missing fine edges. If it still fails, tell the user. Do not hide the edge with a box or pass it off as a cutout.

## Product Packaging

Every product shown must have a packaging status. If it is missing, ask the user. Never infer it from an image, because a supplied image may be a draft, a competitor, or a reference.

| Status | Image source | Generate packaging? | On the slide |
|---|---|---|---|
| `final` | User's product photo or design file | Never | No notice |
| `concept` | One generated package master per product | Once per product | Visible notice |

### Final Packaging

- Use only the user's files. Preserve proportions and all label content.
- Do not run generative edits on a final package, including background removal, without the user's approval. If approved, compare the label text with the original and reject any change.
- If no clean cutout exists, ask for the designer's transparent file, or frame the supplied photo cleanly.

### Concept Packaging

1. **Options:** generate 2-3 directions from the `form` description and the style lock. Stop until the user picks one. Do not build slides with an unapproved package.
2. **Master:** save the approved direction as a transparent master named `pack_<product id>_v1.png`. Each product gets its own master; a range shares materials, lighting, and label layout.
3. **Reuse:** use the same master file everywhere, changing only size and position. Never regenerate the package per slide. This is an explicit user requirement and overrides the `Presentations` default against reusing images.
4. **Scenes:** generate scene images without the product, then layer the master on top. Do not generate a scene that contains the package.
5. **Other angles:** only when a slide needs one. Generate from the master as a reference, compare bottle shape, proportions, and color with the master, and redo on any mismatch. Record it as `pack_<product id>_v1_<angle>.png`, and ask the user to approve it.

Label rules:

- The master has a blank label area. Never let the model write label text.
- Add the product name as a native text box, or composite the user's real logo file. Keep them within the label area and sized to the package.
- Do not put volume, ingredients, dosage, or certification marks on a concept package unless the user supplies that exact information for it.

Notice:

- Every slide showing a concept package has a small visible native text box named `pack_notice`, reading `包裝設計示意，實際以上市版本為準` unless the user supplies other wording.
- Never put the notice inside an image.
- For consumer-facing or advertising use, tell the user in the final response that the deck contains simulated packaging, and leave the decision to use it with them.

### Replacing A Concept Package

When packaging is final:

1. Change the status to `final` and record the real image.
2. Find each placed master by name with `await presentation.inspect({ kind: "image", search: "<asset id>" })`, then get it with `presentation.resolve(id)`.
3. Call `image.replace({ blob, contentType: "image/png", alt, fit: "contain" })`, and set `image.name` to the new asset ID. Keep its frame, then correct the frame if the real image has different proportions.
4. Remove every `pack_notice` for that product and re-render the affected slides.

## Icons

Icons are vector, never generated with `image_gen`, and never rasterized to PNG. This is an explicit user requirement and overrides the `Presentations` default against programmatic vector shapes.

- Source order: SVG files supplied by the user, then one openly licensed icon set chosen for the deck. Record the set and license in the image plan. Do not mix sets or invent icon paths by hand.
- Match the style to the DM: stroke weight, corners, and accent color.
- In PPTX, convert each SVG path to a native shape with `slide.shapes.add({ geometry: "custom", customPaths, fill, line })`, using one custom path per SVG path. `customPaths` supports `moveTo`, `lineTo`, `quadBezTo`, `cubicBezTo`, and `close`, so convert SVG arcs and transforms into these commands first. Map stroke icons to `fill: "none"` plus `line`.
- Do not use `slide.images.add({ svg })` for icons. It exports as a picture with a 1 x 1 PNG fallback, so it is not a native shape and may display incorrectly in apps that use the fallback.
- In HTML, use inline SVG.
- The icon checker may warn about icons on the cover or repeated icons. These warnings do not block delivery. Judge them from the rendered slide, and report any you keep.

## Layer Order

Build each PPTX slide from bottom to top, in this order:

1. `background`: full-bleed image with `position: { left: 0, top: 0, width: 1280, height: 720 }` on a 1280 x 720 slide.
2. Tint or overlay shapes, when needed.
3. `cutout`, `package`, and `photo` images.
4. `icon` shapes.
5. Text and `pack_notice`.

Rules:

- For local PPTX authoring, add images with `blob` bytes and `contentType`, for example `blob: new Uint8Array(await fs.readFile(file))`. Do not use `path`: in the standalone tool it exports an empty image file.
- Set every object's `name` to its asset ID, including images with `image.name = "pack_serum_30ml_v1"`. The name survives export and reopening. `alt` does not, so it cannot be used to find an image later. Still set `alt` to a short description.
- Text sits only in native text boxes. Never bake titles, body copy, numbers, or claims into an image. Sources and charts stay native too.
- A full-slide image is allowed only as the `background` layer, and every slide must keep its text as separate objects.
- Text may sit on the background on purpose. Check its contrast in the rendered slide. Text must not sit on cutouts, packages, or photos unless the render proves it stays readable and hides nothing.

## Compliance Limits For Generated Images

Screen every prompt before generating it, and every result after. Do not generate these unless the user has qualified approval for that exact use, and flag the request instead:

- Before/after comparisons, or skin, body, or health changes that imply a result.
- Doctors, lab scenes, or clinical settings that imply endorsement or evidence the source material does not support.
- Disease, wounds, organs, or medical treatment imagery tied to the product.
- Certification marks, government marks, award badges, or test seals.
- Ingredients absent from the product.
- A package presented as real when its status is `concept`.

A generated image is illustration, not evidence. Do not use one to support a claim or as a chart, test result, or mechanism proof.

## Pilot And QA

Before generating the whole set, build one representative slide with the layers it needs, and check it. If a concept package is needed, get the master approved first. Skip the pilot only if the user says so.

Check every generated or placed asset:

- Subject, style lock, and composition match the plan.
- No text, logos, badges, or artifacts appeared unexpectedly.
- Cutouts pass the alpha check and the light/dark inspection.
- Final files are in the deck's asset folder, not only under `$CODEX_HOME/generated_images`.

Check the finished PPTX with the inspect output or the package XML:

- Every file in `ppt/media/` is non-empty, and cutouts still have their alpha channel. A rendered image-placeholder icon means the image was not embedded.
- No slide is a single flattened image, and no text was replaced by an image.
- The only full-slide pictures are `background` assets.
- Each icon is a native custom shape (`a:custGeom`), not a picture.
- Each product uses one master file, apart from approved angles, and `final` products use no generated package.
- Every slide showing a concept package has `pack_notice`.

Before finalizing a PPTX, run the deterministic required-image gate against the authoritative Markdown, `image-plan.json`, and candidate PPTX:

```bash
python3 "<skill folder>/scripts/check_required_image_assets.py" \
  "<source slide Markdown>" "<asset folder>/image-plan.json" "<candidate PPTX>"
```

The gate fails if a source page marked `需要` lacks its prompt, manifest row, `image_gen` entry, file, or image placement. It also verifies that each asset's exact bytes are embedded on the declared slide. A failing gate blocks finalization; never remove a source requirement or alter its prompt just to pass the check.

Report any check that could not run. Do not report it as passed.
