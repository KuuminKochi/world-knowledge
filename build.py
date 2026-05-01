#!/usr/bin/env python3
"""
World Knowledge — Multi-wiki static site builder
Aggregates multiple Obsidian wikis into a single AI-navigable website.
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

import yaml
from jinja2 import Environment, FileSystemLoader
from slugify import slugify
from markdown_it import MarkdownIt

# ── Config ──────────────────────────────────────────────────────────────

WIKIS_DIR = Path(os.environ.get("WIKIS_DIR", "./wikis"))
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "./site"))
TEMPLATE_DIR = Path("./templates")
ASSETS_DIR = Path("./assets")
SITE_URL = os.environ.get("SITE_URL", "https://example.com")

# ── Markdown setup ──────────────────────────────────────────────────────

md = MarkdownIt("commonmark", {"html": True})
md.enable("table")
md.enable("strikethrough")


# ── Utilities ───────────────────────────────────────────────────────────

def strip_frontmatter(text: str) -> tuple[dict, str]:
    """Extract and remove YAML frontmatter from markdown."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return frontmatter, body
            except yaml.YAMLError:
                pass
    return {}, text


def strip_embeds(text: str) -> str:
    """Remove Obsidian embed lines ![[...]]."""
    return re.sub(r'^!\[\[.*?\]\]\s*$', '', text, flags=re.MULTILINE)


def convert_wikilinks(text: str, slug_map: dict[str, str], wiki_slug: str) -> str:
    """Convert [[wikilinks]] to HTML anchor tags."""
    def replace_link(match):
        content = match.group(1)
        if "|" in content:
            page_title, display = content.split("|", 1)
        else:
            page_title = content
            display = content

        page_title = page_title.strip()
        display = display.strip()

        # Try same-wiki link first, then cross-wiki
        url = slug_map.get(f"{wiki_slug}/{page_title}")
        if not url:
            url = slug_map.get(page_title)
        if url:
            return f'<a href="{url}">{display}</a>'
        else:
            return f'<span class="broken-link" title="Page not found: {page_title}">{display}</span>'

    return re.sub(r'\[\[([^\]]+?)\]\]', replace_link, text)


def process_markdown(text: str, slug_map: dict[str, str], wiki_slug: str) -> str:
    """Full processing pipeline for a markdown file."""
    text = strip_embeds(text)
    text = convert_wikilinks(text, slug_map, wiki_slug)
    return text


# ── Wiki processing ─────────────────────────────────────────────────────

def build_slug_map_for_wiki(wiki_dir: Path, wiki_slug: str) -> dict[str, str]:
    """Build slug map for a single wiki."""
    slug_map = {}
    for md_file in wiki_dir.rglob("*.md"):
        if md_file.name == "index.md":
            continue
        title = md_file.stem
        slug = slugify(title, allow_unicode=True)
        # Determine section from parent directory
        rel = md_file.relative_to(wiki_dir)
        section = rel.parts[0] if len(rel.parts) > 1 else "pages"
        slug_map[f"{wiki_slug}/{title}"] = f"/{wiki_slug}/{section}/{slug}/"
        slug_map[title] = f"/{wiki_slug}/{section}/{slug}/"
    return slug_map


def build_global_slug_map(wikis_dir: Path) -> dict[str, str]:
    """Build slug map across all wikis for cross-wiki linking."""
    global_map = {}
    for wiki_dir in sorted(wikis_dir.iterdir()):
        if wiki_dir.is_dir() and not wiki_dir.name.startswith("."):
            wiki_slug = wiki_dir.name
            global_map.update(build_slug_map_for_wiki(wiki_dir, wiki_slug))
    return global_map


def collect_wiki_pages(wiki_dir: Path, slug_map: dict[str, str], wiki_slug: str) -> list[dict]:
    """Collect all pages from a single wiki."""
    pages = []

    for md_file in wiki_dir.rglob("*.md"):
        if md_file.name == "index.md":
            continue

        title = md_file.stem
        slug = slugify(title, allow_unicode=True)
        raw = md_file.read_text(encoding="utf-8")
        frontmatter, body = strip_frontmatter(raw)
        processed = process_markdown(body, slug_map, wiki_slug)
        html_content = md.render(processed)

        # Determine section from relative path
        rel = md_file.relative_to(wiki_dir)
        section = rel.parts[0] if len(rel.parts) > 1 else "pages"
        url_path = f"{wiki_slug}/{section}/{slug}/"

        pages.append({
            "title": frontmatter.get("title", title),
            "section": section,
            "slug": slug,
            "url_path": url_path,
            "frontmatter": frontmatter,
            "html_content": html_content,
            "wiki_slug": wiki_slug,
            "source_file": str(md_file.relative_to(wiki_dir)),
        })

    return pages


def read_wiki_index(wiki_dir: Path) -> dict:
    """Read the index.md frontmatter for a wiki."""
    index_file = wiki_dir / "index.md"
    if index_file.exists():
        raw = index_file.read_text(encoding="utf-8")
        frontmatter, body = strip_frontmatter(raw)
        return {
            "title": frontmatter.get("title", wiki_dir.name),
            "description": frontmatter.get("description", ""),
            "tags": frontmatter.get("tags", []),
            "author": frontmatter.get("author", ""),
            "slug": wiki_dir.name,
        }
    return {
        "title": wiki_dir.name,
        "description": "",
        "tags": [],
        "author": "",
        "slug": wiki_dir.name,
    }


# ── Build ──────────────────────────────────────────────────────────────

def build_wiki(wiki_dir: Path, slug_map: dict[str, str], templates: Environment, site_url: str) -> tuple[list[dict], dict]:
    """Build all pages for a single wiki. Returns (pages, metadata)."""
    wiki_slug = wiki_dir.name
    wiki_meta = read_wiki_index(wiki_dir)
    pages = collect_wiki_pages(wiki_dir, slug_map, wiki_slug)

    page_template = templates.get_template("page.html")

    for page in pages:
        page_dir = OUTPUT_DIR / page["url_path"]
        page_dir.mkdir(parents=True, exist_ok=True)

        html = page_template.render(
            title=page["title"],
            content=page["html_content"],
            section=page["section"],
            wiki_slug=wiki_slug,
            wiki_title=wiki_meta["title"],
            frontmatter=page["frontmatter"],
            site_url=site_url,
        )
        (page_dir / "index.html").write_text(html, encoding="utf-8")

    return pages, wiki_meta


def generate_sitemap(wiki_dirs: list[dict], site_url: str) -> str:
    """Generate sitemap.xml for all wikis."""
    urls = [f"""  <url>
    <loc>{site_url}/</loc>
    <changefreq>weekly</changefreq>
  </url>"""]

    for wiki in wiki_dirs:
        for page in wiki["pages"]:
            urls.append(f"""  <url>
    <loc>{site_url}/{page['url_path']}</loc>
    <changefreq>monthly</changefreq>
  </url>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""


def build_site():
    """Main build function."""
    print(f"Building World Knowledge from {WIKIS_DIR} → {OUTPUT_DIR}")

    # Clean output
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    # Discover wikis
    wiki_dirs = sorted([
        d for d in WIKIS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    ])
    print(f"  Found {len(wiki_dirs)} wikis: {[d.name for d in wiki_dirs]}")

    # Build global slug map
    slug_map = build_global_slug_map(WIKIS_DIR)
    print(f"  Mapped {len(slug_map)} page slugs across all wikis")

    # Setup templates
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    index_template = env.get_template("index.html")

    # Build each wiki
    all_wikis = []
    all_pages = []
    for wiki_dir in wiki_dirs:
        pages, meta = build_wiki(wiki_dir, slug_map, env, SITE_URL)
        all_wikis.append({"meta": meta, "pages": pages})
        all_pages.extend(pages)
        print(f"  Built {wiki_dir.name}: {len(pages)} pages")

    # Generate homepage
    index_html = index_template.render(
        wikis=[w["meta"] for w in all_wikis],
        site_url=SITE_URL,
        last_updated=datetime.now().strftime("%Y-%m-%d"),
        total_pages=len(all_pages),
    )
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Generate sitemap
    sitemap = generate_sitemap(all_wikis, SITE_URL)
    (OUTPUT_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print(f"  Generated sitemap.xml with {len(all_pages) + 1} URLs")

    # Copy assets
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, OUTPUT_DIR / "assets", dirs_exist_ok=True)
        print("  Copied assets/")

    print(f"\nBuild complete: {OUTPUT_DIR}")
    print(f"  {len(all_wikis)} wikis, {len(all_pages)} total pages")


if __name__ == "__main__":
    build_site()
