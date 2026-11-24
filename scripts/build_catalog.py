#!/usr/bin/env python3
"""Generate catalog.json, the library home page, and sync guides into docs/."""
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / "guides"
DOCS = ROOT / "docs"
CATALOG = ROOT / "catalog.json"
MKDOCS = ROOT / "mkdocs.yml"

NAV_START = "# guides-nav:start"
NAV_END = "# guides-nav:end"


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    data = yaml.safe_load(raw) or {}
    return data, body


def slug_title(slug: str, meta: dict) -> str:
    return meta.get("title") or slug.replace("-", " ").title()


def load_guides() -> list[dict]:
    entries = []
    if not GUIDES.exists():
        return entries
    for path in sorted(GUIDES.glob("*/index.md")):
        meta, _ = parse_front_matter(path.read_text(encoding="utf-8"))
        slug = path.parent.name
        entry = {
            "slug": slug,
            "path": f"guides/{slug}/index.md",
            "pdf": f"guides/{slug}/guide.pdf",
            "title": slug_title(slug, meta),
            "source_url": meta.get("source_url"),
            "source_type": meta.get("source_type"),
            "author": meta.get("author"),
            "channel": meta.get("channel"),
            "topics": meta.get("topics") or [],
            "tags": meta.get("tags") or [],
            "difficulty": meta.get("difficulty"),
            "date": str(meta.get("date") or ""),
            "standards_cited": meta.get("standards_cited") or [],
            "duration": meta.get("duration"),
            "page_url": meta.get("page_url"),
        }
        entries.append(entry)
    entries.sort(key=lambda e: e["date"] or "", reverse=True)
    return entries


def sync_docs(entries: list[dict]) -> None:
    dest_root = DOCS / "guides"
    if dest_root.exists():
        shutil.rmtree(dest_root)
    dest_root.mkdir(parents=True)
    for entry in entries:
        src = GUIDES / entry["slug"]
        dst = dest_root / entry["slug"]
        shutil.copytree(src, dst)


def write_home(entries: list[dict]) -> None:
    lines = [
        "# GoC Guide Library",
        "",
        "Step-by-step guides from [Generals of Chaos](https://cbgoc-cloud.top/),",
        "each built from a public video or post, expanded with industry standards,",
        "and tagged so you can search by metadata.",
        "",
        f"**{len(entries)} guides** in the library. Use the search box, browse",
        "[by tag](tags.md), or filter the table below.",
        "",
        "| Guide | Date | Source | Author | Difficulty | Duration | Tags | PDF |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for e in entries:
        link = f"[{e['title']}]({e['path']})"
        src = e.get("source_type") or ""
        if e.get("source_url"):
            src = f"[{src}]({e['source_url']})"
        tags = ", ".join(f"`{t}`" for t in (e.get("tags") or [])[:6])
        pdf = f"[PDF]({e['pdf']})"
        lines.append(
            f"| {link} | {e.get('date') or ''} | {src} | {e.get('author') or ''} | "
            f"{e.get('difficulty') or ''} | {e.get('duration') or ''} | {tags} | {pdf} |"
        )
    lines += [
        "",
        "## How this library works",
        "",
        "- Each guide lives in `guides/<slug>/` with Markdown, YAML front matter, and a PDF.",
        "- `catalog.json` is generated from that front matter on every docs build.",
        "- The site is built with MkDocs Material (search, tags, Mermaid diagrams).",
        "",
        "To add a guide, follow [CONTRIBUTING.md](https://github.com/Lipford-Dutch/goc-guide-library/blob/main/CONTRIBUTING.md).",
        "",
    ]
    (DOCS / "index.md").write_text("\n".join(lines), encoding="utf-8")


def update_nav(entries: list[dict]) -> None:
    text = MKDOCS.read_text(encoding="utf-8")
    start = text.find(NAV_START)
    end = text.find(NAV_END)
    if start == -1 or end == -1 or end < start:
        raise SystemExit("mkdocs.yml is missing guides-nav markers")
    nav_lines = [
        NAV_START,
        "nav:",
        "  - Home: index.md",
        "  - Guides:",
    ]
    # chronological already; show oldest-first in nav for a stable reading order
    for e in sorted(entries, key=lambda x: x["date"] or ""):
        nav_lines.append(f"      - {json.dumps(e['title'], ensure_ascii=False)}: {e['path']}")
    nav_lines += [
        "  - Tags: tags.md",
        NAV_END,
    ]
    new = text[:start] + "\n".join(nav_lines) + text[end + len(NAV_END) :]
    MKDOCS.write_text(new, encoding="utf-8")


def main() -> None:
    entries = load_guides()
    CATALOG.write_text(json.dumps({"guides": entries}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    sync_docs(entries)
    write_home(entries)
    update_nav(entries)
    print(f"catalog: {len(entries)} guides")


if __name__ == "__main__":
    main()
