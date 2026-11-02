#!/usr/bin/env python3
"""Block PPTX finalization when annotated image prompts lack generated visuals."""

from __future__ import annotations

import hashlib
import json
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import BadZipFile, ZipFile


HEADING = re.compile(r"^##\s*第\s*(\d+)\s*頁.*$", re.M)
NEEDED = re.compile(r"插圖評估\s*[：:]\s*需要")
PROMPT = re.compile(r"插圖\s*Prompt[^：:\n]*[：:]\s*(.+)")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def required_prompts(source: str) -> dict[int, str]:
    headings = list(HEADING.finditer(source))
    required: dict[int, str] = {}
    errors: list[str] = []
    for i, match in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(source)
        block = source[match.end():end]
        if not NEEDED.search(block):
            continue
        page = int(match.group(1))
        prompts = PROMPT.findall(block)
        if len(prompts) != 1:
            errors.append(f"來源第 {page} 頁標為需要插圖，但找到 {len(prompts)} 個插圖 Prompt（預期 1 個）。")
        else:
            required[page] = " ".join(prompts[0].split())
    if errors:
        raise ValueError("\n".join(errors))
    return required


def pptx_slide_media_hashes(z: ZipFile, slide_no: int) -> set[str]:
    slide_xml = f"ppt/slides/slide{slide_no}.xml"
    rels_xml = f"ppt/slides/_rels/slide{slide_no}.xml.rels"
    if slide_xml not in z.namelist() or rels_xml not in z.namelist():
        return set()
    root = ET.fromstring(z.read(rels_xml))
    hashes: set[str] = set()
    for rel in root:
        if not rel.tag.endswith("Relationship") or not rel.attrib.get("Type", "").endswith("/image"):
            continue
        target = rel.attrib.get("Target", "")
        if target.startswith("/"):
            member = target.lstrip("/")
        else:
            member = posixpath.normpath(posixpath.join("ppt/slides", target))
        if member in z.namelist():
            hashes.add(sha(z.read(member)))
    return hashes


def main() -> int:
    if len(sys.argv) != 4:
        print("Usage: check_required_image_assets.py <source.md> <image-plan.json> <candidate.pptx>", file=sys.stderr)
        return 2
    source_path, manifest_path, pptx_path = map(Path, sys.argv[1:])
    try:
        source = source_path.read_text(encoding="utf-8")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"INPUT ERROR: {exc}", file=sys.stderr)
        return 2

    try:
        required = required_prompts(source)
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    assets = manifest.get("required_assets") if isinstance(manifest, dict) else None
    if not isinstance(assets, list):
        print("FAIL: image-plan.json 缺少 required_assets 陣列。", file=sys.stderr)
        return 1

    by_page: dict[int, dict] = {}
    errors: list[str] = []
    for item in assets:
        if not isinstance(item, dict) or not isinstance(item.get("source_page"), int):
            errors.append("required_assets 含無效紀錄或缺少整數 source_page。")
            continue
        page = item["source_page"]
        if page in by_page:
            errors.append(f"manifest 重複列出來源第 {page} 頁。")
        by_page[page] = item

    for page, prompt in required.items():
        item = by_page.get(page)
        if item is None:
            errors.append(f"來源第 {page} 頁沒有 manifest 紀錄。")
            continue
        if " ".join(str(item.get("source_prompt", "")).split()) != prompt:
            errors.append(f"來源第 {page} 頁的 source_prompt 與原稿不一致。")
        if item.get("generation_tool") != "image_gen":
            errors.append(f"來源第 {page} 頁未記錄使用 image_gen。")
        if not str(item.get("generation_prompt", "")).strip():
            errors.append(f"來源第 {page} 頁缺少 generation_prompt。")
        if not str(item.get("id", "")).strip():
            errors.append(f"來源第 {page} 頁缺少 asset id。")
        if not isinstance(item.get("pptx_slide"), int) or item["pptx_slide"] < 1:
            errors.append(f"來源第 {page} 頁缺少有效的 1-based pptx_slide。")
        asset_rels = item.get("asset_paths")
        if not isinstance(asset_rels, list) or not asset_rels or not all(isinstance(x, str) and x for x in asset_rels):
            errors.append(f"來源第 {page} 頁缺少非空 asset_paths 字串陣列。")
            continue
        item["_asset_hashes"] = []
        for asset_rel in asset_rels:
            asset_path = (manifest_path.parent / asset_rel).resolve()
            try:
                item["_asset_hashes"].append((asset_rel, sha(asset_path.read_bytes())))
            except OSError:
                errors.append(f"來源第 {page} 頁的素材檔不存在或無法讀取：{asset_path}")

    extra_pages = sorted(set(by_page) - set(required))
    if extra_pages:
        errors.append(f"manifest 列出原稿未標記為需要插圖的來源頁：{extra_pages}。請移至 optional_assets 或修正來源註記。")

    if not required:
        errors.append("來源 Markdown 沒有可解析的『插圖評估：需要』頁面；確認傳入的是權威簡報逐頁稿。")

    if errors:
        print("FAIL: 必要生成素材未通過檢查：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    try:
        with ZipFile(pptx_path) as z:
            bad = z.testzip()
            if bad:
                raise BadZipFile(f"損壞的 ZIP 成員：{bad}")
            for page in sorted(required):
                item = by_page[page]
                slide_no = item["pptx_slide"]
                slide_hashes = pptx_slide_media_hashes(z, slide_no)
                for asset_rel, asset_hash in item["_asset_hashes"]:
                    if asset_hash not in slide_hashes:
                        errors.append(f"來源第 {page} 頁的生成圖 {asset_rel} 未以原始素材完整嵌入 PPTX 第 {slide_no} 頁。")
    except (OSError, BadZipFile, ET.ParseError) as exc:
        print(f"PPTX ERROR: {exc}", file=sys.stderr)
        return 2

    if errors:
        print("FAIL: 必要生成素材未嵌入投影片：", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(json.dumps({"status": "pass", "required_source_pages": sorted(required), "required_count": len(required), "generated_and_embedded_count": len(required)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
