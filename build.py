#!/usr/bin/env python3
"""
World Knowledge — Static site builder
Converts Obsidian wiki markdown → clean HTML for AI-navigable knowledge base.
"""

import os
import re
import shutil
import json
from pathlib import Path
from datetime import datetime

import yaml
from jinja2 import Environment, FileSystemLoader
from slugify import slugify
from markdown_it import MarkdownIt

# ── Config ──────────────────────────────────────────────────────────────

WIKI_DIR = Path(os.environ.get("WIKI_DIR", "../nothingburger/wiki"))
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "./site"))
TEMPLATE_DIR = Path("./templates")
ASSETS_DIR = Path("./assets")
SITE_URL = os.environ.get("SITE_URL", "https://example.com")

# Sections to process (directory names in wiki/)
SECTIONS = ["concepts", "sources", "tutorials"]

# ── Markdown setup ──────────────────────────────────────────────────────

md = MarkdownIt("commonmark", {"html": True})
md.enable("table")
md.enable("strikethrough")


# ── Wikilink conversion ────────────────────────────────────────────────

def build_slug_map(wiki_dir: Path) -> dict[str, str]:
    """Build a mapping from page titles to their slugified URL paths."""
    slug_map = {}
    for section in SECTIONS:
        section_dir = wiki_dir / section
        if not section_dir.exists():
            continue
        for md_file in section_dir.rglob("*.md"):
            title = md_file.stem
            slug = slugify(title, allow_unicode=True)
            slug_map[title] = f"/{section}/{slug}/"
    return slug_map


def convert_wikilinks(text: str, slug_map: dict[str, str]) -> str:
    """Convert [[wikilinks]] to HTML anchor tags."""
    def replace_link(match):
        content = match.group(1)
        # Handle [[Page|display text]] and [[Page]]
        if "|" in content:
            page_title, display = content.split("|", 1)
        else:
            page_title = content
            display = content

        page_title = page_title.strip()
        display = display.strip()

        # Find the slug
        url = slug_map.get(page_title)
        if url:
            return f'<a href="{url}">{display}</a>'
        else:
            # Link target not found — keep as text with a note
            return f'<span class="broken-link" title="Page not found: {page_title}">{display}</span>'

    # Match [[...]] but not [[[...]]] (Obsidian aliases)
    return re.sub(r'\[\[([^\]]+?)\]\]', replace_link, text)


def strip_embeds(text: str) -> str:
    """Remove Obsidian embed lines ![[...]] (images, excalidraw, etc.)."""
    return re.sub(r'^!\[\[.*?\]\]\s*$', '', text, flags=re.MULTILINE)


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


def process_markdown(text: str, slug_map: dict[str, str]) -> str:
    """Full processing pipeline for a markdown file."""
    text = strip_embeds(text)
    text = convert_wikilinks(text, slug_map)
    return text


# ── Build ──────────────────────────────────────────────────────────────

def collect_pages(wiki_dir: Path, slug_map: dict[str, str]) -> list[dict]:
    """Collect all markdown pages with metadata."""
    pages = []

    for section in SECTIONS:
        section_dir = wiki_dir / section
        if not section_dir.exists():
            continue
        for md_file in section_dir.rglob("*.md"):
            title = md_file.stem
            slug = slugify(title, allow_unicode=True)
            raw = md_file.read_text(encoding="utf-8")
            frontmatter, body = strip_frontmatter(raw)
            processed = process_markdown(body, slug_map)
            html_content = md.render(processed)

            url_path = f"/{section}/{slug}/"

            pages.append({
                "title": frontmatter.get("title", title),
                "section": section,
                "slug": slug,
                "url_path": url_path,
                "frontmatter": frontmatter,
                "html_content": html_content,
                "source_file": str(md_file.relative_to(wiki_dir)),
            })

    return pages


def build_index(wiki_dir: Path, pages: list[dict]) -> dict:
    """Build the homepage data from wiki/index.md."""
    index_file = wiki_dir / "index.md"
    if index_file.exists():
        raw = index_file.read_text(encoding="utf-8")
        frontmatter, body = strip_frontmatter(raw)
        processed = process_markdown(body, slug_map)
        html_content = md.render(processed)
    else:
        frontmatter = {}
        html_content = "<p>No index found.</p>"

    # Count stats
    concept_count = len([p for p in pages if p["section"] == "concepts"])
    source_count = len([p for p in pages if p["section"] == "sources"])
    entity_count = len([p for p in pages if p["section"] == "entities"])
    total_count = len(pages)

    return {
        "frontmatter": frontmatter,
        "html_content": html_content,
        "stats": {
            "concept_count": concept_count,
            "source_count": source_count,
            "entity_count": entity_count,
            "total_count": total_count,
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
        }
    }


def generate_sitemap(pages: list[dict], site_url: str) -> str:
    """Generate sitemap.xml."""
    urls = []
    for page in pages:
        urls.append(f"""  <url>
    <loc>{site_url}{page['url_path']}</loc>
    <changefreq>monthly</changefreq>
  </url>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{site_url}/</loc>
    <changefreq>weekly</changefreq>
  </url>
{chr(10).join(urls)}
</urlset>"""


def build_site():
    """Main build function."""
    print(f"Building site from {WIKI_DIR} → {OUTPUT_DIR}")

    # Clean output
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    # Build slug map
    global slug_map
    slug_map = build_slug_map(WIKI_DIR)
    print(f"  Mapped {len(slug_map)} page titles to slugs")

    # Collect pages
    pages = collect_pages(WIKI_DIR, slug_map)
    print(f"  Collected {len(pages)} pages")

    # Setup Jinja2
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    page_template = env.get_template("page.html")
    index_template = env.get_template("index.html")

    # Build index
    index_data = build_index(WIKI_DIR, pages)
    print(f"  Index: {index_data['stats']}")

    # Render index
    index_html = index_template.render(
        content=index_data["html_content"],
        stats=index_data["stats"],
        site_url=SITE_URL,
    )
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Render pages
    for page in pages:
        page_dir = OUTPUT_DIR / page["url_path"]
        page_dir.mkdir(parents=True, exist_ok=True)

        html = page_template.render(
            title=page["title"],
            content=page["html_content"],
            section=page["section"],
            frontmatter=page["frontmatter"],
            site_url=SITE_URL,
        )
        (page_dir / "index.html").write_text(html, encoding="utf-8")

    # Generate sitemap
    sitemap = generate_sitemap(pages, SITE_URL)
    (OUTPUT_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print(f"  Generated sitemap.xml with {len(pages) + 1} URLs")

    # Copy assets
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, OUTPUT_DIR / "assets", dirs_exist_ok=True)
        print("  Copied assets/")

    # Copy wiki log if exists
    log_file = WIKI_DIR / "log.md"
    if log_file.exists():
        log_dir = OUTPUT_DIR / "meta"
        log_dir.mkdir(exist_ok=True)
        raw = log_file.read_text(encoding="utf-8")
        frontmatter, body = strip_frontmatter(raw)
        processed = process_markdown(body, slug_map)
        html_content = md.render(processed)
        html = page_template.render(
            title="Wiki Log",
            content=html_content,
            section="meta",
            frontmatter=frontmatter,
            site_url=SITE_URL,
        )
        (log_dir / "index.html").write_text(html, encoding="utf-8")

    print(f"\nBuild complete: {OUTPUT_DIR}")
    print(f"  {len(pages)} pages + index + sitemap")


if __name__ == "__main__":
    build_site()
