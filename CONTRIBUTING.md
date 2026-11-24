# Contributing to the GoC Guide Library

This repository is the publishing target for every step-by-step guide the GoC
bot generates. Humans can add or edit a guide the same way.

## Front matter schema

Every `guides/<slug>/index.md` must start with YAML front matter:

```yaml
---
title: "Exact guide title"
source_url: "https://youtu.be/VIDEO_ID"   # or the LinkedIn / article URL
source_type: youtube                      # youtube | linkedin | other
author: "Presenter or writer"
channel: "Channel or publication"
topics: ["short-topic", "another"]
tags: ["searchable", "tags"]
difficulty: beginner                      # beginner | intermediate | advanced | beginner-to-intermediate
date: 2026-11-24                          # ISO date the guide was published to the library
standards_cited: ["NIST SP 800-63B", "CISA 3-2-1"]
duration: "15:37"                         # source runtime, or total course time
page_url: "https://cursor.com/canvas/..." # optional origin Page
pdf: guide.pdf
---
```

`tags` is what MkDocs Material uses for the tag index. `topics` is broader
subject metadata for `catalog.json`. Keep both lowercase and hyphenated.

## Adding a guide

1. Choose a stable kebab-case slug (`home-lab-services`).
2. Create `guides/<slug>/index.md` with the front matter above and the full
   Markdown body (steps, tables, checklists, timestamp links, sources).
3. Put Mermaid diagrams in fenced `mermaid` blocks.
4. Copy the PDF to `guides/<slug>/guide.pdf` and link it from the body
   (`[Download this guide (PDF)](guide.pdf)`).
5. Run the catalog and a strict docs build:

   ```bash
   python scripts/build_catalog.py
   mkdocs build --strict
   ```

   The script writes `catalog.json`, copies `guides/` into `docs/guides/`,
   regenerates the home page, and updates the `mkdocs.yml` nav between the
   `guides-nav` markers. Do not hand-edit those generated files.
6. Open a pull request, or push to `main` if you have write access. GitHub
   Actions will rebuild and publish the site.

## Local preview

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_catalog.py
mkdocs serve
```

## Style

- Mark additions that were not in the source as **Beyond the video** or
  **Beyond the post**.
- Cite standards with a link in the Sources section.
- Keep timestamp links pointing at the original video (`https://youtu.be/ID?t=SECONDS`).
- Follow the GoC dark theme already set in `docs/assets/extra.css`.
