# World Knowledge

An open, public, AI-navigable knowledge aggregator. Aggregates multiple Obsidian wikis into a single elegant static website with full wikilink navigation, KaTeX math rendering, Mermaid diagrams, and SMILES chemical structures.

## Architecture

```
wikis/          → Source .md files (Obsidian format)
templates/      → Jinja2 HTML templates
assets/         → Static assets (CSS, JS)
build.py        → Multi-wiki static site builder
site/           → Build output (gitignored, deployed to Cloudflare Pages)
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Build
python build.py

# Output in site/
```

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
- `SITE_URL` — set to your custom domain (optional, overrides CF_PAGES_URL)

## Wiki Format

Each wiki is a directory under `wikis/` containing:
- `index.md` — Wiki metadata (title, description, author, tags)
- `concepts/` — Atomic knowledge units
- `sources/` — Lecture notes and chapter content
- `tutorials/` — Practice problems and worked solutions

Markdown files use Obsidian-flavored syntax with `[[wikilinks]]`, YAML frontmatter, and `$LaTeX$` math.

## License

MIT
