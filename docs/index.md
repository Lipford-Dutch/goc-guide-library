# GoC Guide Library

Step-by-step guides from [Generals of Chaos](https://cbgoc-cloud.top/),
each built from a public video or post, expanded with industry standards,
and tagged so you can search by metadata.

**5 guides** in the library. Use the search box, browse
[by tag](tags.md), or filter the table below.

| Guide | Date | Source | Author | Difficulty | Duration | Tags | PDF |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Full Stack’s Featured Repos, Nov 10–24, 2026: Step-by-Step Try-It Guide](guides/full-stack-featured-repos-nov-2026/index.md) | 2026-11-24 | [youtube](https://www.youtube.com/channel/UC_GBIzXUzVTV9r7GKpu6IWw/videos) | Full Stack | intermediate | 1h 36m (7 videos) | `github`, `ai-agents`, `browser-automation`, `web-scraping`, `self-hosting`, `llm-training` | [PDF](guides/full-stack-featured-repos-nov-2026/guide.pdf) |
| [Free DevOps Roadmap: Step-by-Step Study Guide](guides/free-devops-roadmap/index.md) | 2026-11-23 | [linkedin](https://www.linkedin.com/posts/david-popoola-op_devops-sre-cloudcomputing-share-7530280973574238208-WZg9/) | David Popoola | beginner-to-intermediate | 60h 48m | `devops`, `linux`, `docker`, `kubernetes`, `terraform`, `cicd` | [PDF](guides/free-devops-roadmap/guide.pdf) |
| [This Week’s Top 10 GitHub Repos: Step-by-Step Try-It Guide](guides/top-10-github-repos/index.md) | 2026-11-19 | [youtube](https://youtu.be/Blo_TXR-S-4) | Full Stack | intermediate | 24:17 | `github`, `ai-agents`, `security`, `open-source`, `supply-chain` | [PDF](guides/top-10-github-repos/guide.pdf) |
| [Uncensored AI in 3 Levels: Step-by-Step Guide](guides/uncensored-ai-in-3-levels/index.md) | 2026-11-19 | [youtube](https://youtu.be/bc7QaDmLmoA) | Jack Roberts | intermediate | 22:42 | `ai`, `llm`, `ollama`, `tailscale`, `privacy`, `uncensored-models` | [PDF](guides/uncensored-ai-in-3-levels/guide.pdf) |
| [Home Lab Services: Step-by-Step Build Guide](guides/home-lab-services/index.md) | 2026-11-12 | [youtube](https://youtu.be/Pp-OuIpXF90) | WunderTech | intermediate | 15:37 | `home-lab`, `self-hosting`, `docker`, `proxmox`, `backups`, `networking` | [PDF](guides/home-lab-services/guide.pdf) |

## How this library works

- Each guide lives in `guides/<slug>/` with Markdown, YAML front matter, and a PDF.
- `catalog.json` is generated from that front matter on every docs build.
- The site is built with MkDocs Material (search, tags, Mermaid diagrams).

To add a guide, follow [CONTRIBUTING.md](https://github.com/Lipford-Dutch/goc-guide-library/blob/main/CONTRIBUTING.md).
