# GoC Guide Library

A searchable library of step-by-step guides published by
[Generals of Chaos](https://cbgoc-cloud.top/) in the
[Lipford-Dutch](https://github.com/Lipford-Dutch) organization.

**Live site:** <https://lipford-dutch.github.io/goc-guide-library/>

Each guide is converted from a public video or post into a detailed walkthrough:
numbered steps (what, how, why, common mistakes), additions marked *Beyond the
video* or *Beyond the post*, diagrams, tables, checklists, timestamp links, and
cited standards. A PDF of the same guide ships beside the Markdown.

## Browse

- Website search and [tag index](https://lipford-dutch.github.io/goc-guide-library/tags/)
- Machine-readable catalog: [`catalog.json`](catalog.json)
- Source folders: [`guides/`](guides/)

## How a guide is stored

```text
guides/<slug>/
  index.md    # YAML front matter + full guide
  guide.pdf   # printable export
```

Front matter includes title, source URL and type, author/channel, topics, tags,
difficulty, date, standards cited, duration, the original Page URL, and the PDF
path. See [CONTRIBUTING.md](CONTRIBUTING.md) to add one.

## Local preview

```bash
python -m pip install -r requirements-docs.txt
python scripts/build_catalog.py
mkdocs serve
```

The site is rebuilt on every push to `main` by GitHub Actions and published to
GitHub Pages.

## License

Repository tooling is released under the [Unlicense](LICENSE). Guide text and
PDFs are provided for the GoC community; original videos and posts remain the
rights of their authors. Follow each source's license when you reuse third-party
material.
