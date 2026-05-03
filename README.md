# textbase.fyi

An AI-first, human-readable knowledge aggregator. Aggregates multiple Obsidian wikis into a single static website with freshness tracking, recommended LLM skills, RSS feeds, wikilink navigation, KaTeX math rendering, Mermaid diagrams, and SMILES chemical structures.

**Previously:** World Knowledge

## Architecture

```
wikis/          → Source .md files (Obsidian format)
  pasum/        → PASUM wiki (mathematics, physics, chemistry)
    index.md    → Wiki metadata + recommended LLM skills
    log.md      → Change history (auto-rendered as /changelog/)
    concepts/   → Atomic knowledge units
    sources/    → Lecture notes and chapter content
    tutorials/  → Practice problems and worked solutions
    entities/   → People, courses, institutions
templates/      → Jinja2 HTML templates
assets/         → Static assets (CSS, JS)
build.py        → Multi-wiki static site builder
site/           → Build output (gitignored, deployed)
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Build
python build.py

# Output in site/
```

## Features

- **Freshness tracking** — Per-page "last edited" dates, per-wiki changelog pages, global and per-wiki Atom RSS feeds
- **Recommended LLM skills** — Wiki indexes can suggest AI skills (academic-wiki, problem-set-synthesis, grill-me, etc.) that an LLM agent can auto-offer to the user
- **Entity pages** — Structured pages for people (lecturers), courses, and institutions
- **Wikilinks** — Obsidian-style `[[links]]` resolve across all wikis
- **Math rendering** — KaTeX (primary) + MathJax (fallback) for LaTeX math
- **Diagrams** — Mermaid for flowcharts, decision trees, and concept maps
- **Chemical structures** — SMILES rendering via smiles-drawer
- **Responsive** — Works on desktop, tablet, and mobile
- **Dark mode** — Automatic via `prefers-color-scheme`

## Wiki Index Format

Each wiki's `index.md` supports YAML frontmatter with:

```yaml
---
title: Wiki Title
description: A description of the wiki
author: YourName
skills:
  - name: academic-wiki
    purpose: "Navigate the knowledge graph interactively"
    auto_offer: true
  - name: problem-set-synthesis
    purpose: "Generate interleaved practice problems"
    auto_offer: true
---
```

The `skills` array tells AI assistants which skills to proactively offer. Each skill needs:
- `name` — The skill name (must match an installed skill)
- `purpose` — A human-readable explanation of what the skill does
- `auto_offer` — Whether the AI should proactively offer to load it

## Environment Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `WIKIS_DIR` | Path to wiki source .md files | `./wikis` |
| `OUTPUT_DIR` | Build output directory | `./site` |
| `SITE_URL` | Production URL for absolute links | Auto-detected |
| `CF_PAGES_URL` | Cloudflare Pages deployment URL | Auto-detected |

## Deployment

Deployed to Cloudflare Pages. Build settings:
- **Build command:** `python build.py`
- **Output directory:** `site`
- **Python version:** 3.11+

### Required Cloudflare Pages environment variables:
- `CF_PAGES_URL` — set automatically by Cloudflare
- `SITE_URL` — set to your custom domain

## License

MIT
