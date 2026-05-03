# textbase.fyi — Agent Guide

## Build & Run

```bash
pip install -r requirements.txt
python build.py          # Builds site/ from wikis/
```

## Project Architecture

- `build.py` — Jinja2-based static site builder. Entry point: `build_site()`
- `templates/` — Two Jinja2 templates:
  - `index.html` — Homepage (wiki directory listing)
  - `page.html` — All other pages (wiki indexes, concepts, sources, tutorials, entities, changelog, AI guide)
- `assets/css/style.css` — Zine/indie web aesthetic: Fraunces (headings) + Inter (body), light multi-color
- `wikis/` — Source markdown files in Obsidian format

## Wiki Structure

Each wiki under `wikis/` is a directory with:
- `index.md` — Required. YAML frontmatter with title, description, author, skills, optional color override
- `log.md` — Optional. Markdown changelog, auto-rendered to `/wiki/changelog/`
- `concepts/` — Atomic knowledge units
- `sources/` — Lecture notes, past papers
- `tutorials/` — Practice problems
- `entities/` — People (lecturers), courses, institutions

## Key Features for AI

### Recommended Skills

Wiki `index.md` frontmatter supports a `skills` array:

```yaml
skills:
  - name: academic-wiki
    purpose: "..."
    auto_offer: true
```

When any AI reads a wiki index page, an HTML comment instructs it to offer these skills to the user. The skill cards are rendered visually for humans too.

### Freshness

- Every page footer has `last edited YYYY-MM-DD` from git log (fallback: frontmatter `date`)
- Every wiki has `/wiki/changelog/` rendered from `log.md`
- Global `/feed.xml` and per-wiki `/wiki/feed.xml` Atom feeds

### Per-Wiki Accent Colors

Colors are hash-derived from wiki slug (MD5 of slug → palette of 8). Can be overridden via `color: '#ff6600'` in `index.md` frontmatter.

## URL Structure

```
/                              → Homepage
/ai/                           → AI Navigation Guide
/feed.xml                      → Global Atom feed
/{wiki}/                       → Wiki index
/{wiki}/concepts/{slug}/       → Concept page
/{wiki}/sources/{slug}/        → Source page
/{wiki}/tutorials/{slug}/      → Tutorial page
/{wiki}/entities/{slug}/       → Entity page
/{wiki}/changelog/             → Change history
/{wiki}/feed.xml               → Per-wiki Atom feed
/sitemap.xml                   → Full sitemap
```

## Markdown Syntax

- `[[wikilinks]]` — Cross-page links (auto-resolved to HTML anchors)
- `![[embed]]` — Obsidian embeds (stripped during build)
- `$...$` / `$$...$$` — LaTeX math (KaTeX + MathJax fallback)
- ```mermaid — Mermaid diagrams
- `smiles` — Chemical structure rendering via smiles-drawer
- YAML frontmatter `---` — Page metadata

## Design Tokens

- **Display font**: Fraunces (variable, opsz 9..144)
- **Body font**: Inter
- **Palette**: Light bg `#f8f5f0`, dark fg `#1e1b17`, per-wiki accent from 8-color palette
- **Layout**: Max-width 740px, single column, generous whitespace
- **Skills card**: Bordered with wiki accent, left-accented entries
