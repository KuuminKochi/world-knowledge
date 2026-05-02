#!/usr/bin/env python3
"""
World Knowledge — Multi-wiki static site builder
Aggregates multiple Obsidian wikis into a single AI-navigable website.
"""

import html
import os
import re
import shutil
import sys
from pathlib import Path
from datetime import datetime

import yaml
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup
from slugify import slugify
from markdown_it import MarkdownIt

# ── Config ──────────────────────────────────────────────────────────────

WIKIS_DIR = Path(os.environ.get("WIKIS_DIR", "./wikis"))
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "./site"))
TEMPLATE_DIR = Path("./templates")
ASSETS_DIR = Path("./assets")
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")
if not SITE_URL:
    # Auto-detect from Cloudflare Pages or default
    SITE_URL = os.environ.get("CF_PAGES_URL", "").rstrip("/") or "https://example.com"
    if not SITE_URL.startswith("http"):
        SITE_URL = f"https://{SITE_URL}"

if SITE_URL == "https://example.com":
    print("WARNING: Using fallback URL https://example.com. Set SITE_URL or CF_PAGES_URL environment variable.", file=sys.stderr)

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

        # Try qualified key first, then bare key fallback
        qualified_key = f"{wiki_slug}/{page_title}"
        url = slug_map.get(qualified_key)
        if not url:
            url = slug_map.get(page_title)
        else:
            # Check if bare key resolves to a different URL (cross-wiki collision)
            bare_url = slug_map.get(page_title)
            if bare_url and bare_url != url:
                print(f"WARNING: Cross-wiki link collision for '{page_title}'. "
                      f"Qualified: {url}, Bare: {bare_url}", file=sys.stderr)
        if url:
            return f'<a href="{html.escape(url)}">{html.escape(display)}</a>'
        else:
            return f'<span class="broken-link" title="Page not found: {html.escape(page_title)}">{html.escape(display)}</span>'

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
    seen = set()
    for md_file in wiki_dir.rglob("*.md"):
        if md_file.name == "index.md":
            continue
        title = md_file.stem
        slug = slugify(title, allow_unicode=True)
        # Determine section from parent directory
        rel = md_file.relative_to(wiki_dir)
        section = rel.parts[0] if len(rel.parts) > 1 else "pages"
        key = f"{wiki_slug}/{title}"
        if key in seen:
            suffix = 2
            while f"{key}-{suffix}" in seen:
                suffix += 1
            print(f"WARNING: Duplicate slug for '{key}' -> '{key}-{suffix}'", file=sys.stderr)
            key = f"{key}-{suffix}"
        seen.add(key)
        slug_map[key] = f"/{wiki_slug}/{section}/{slug}/"
        slug_map[title] = f"/{wiki_slug}/{section}/{slug}/"
    return slug_map


def build_global_slug_map(wikis_dir: Path) -> dict[str, str]:
    """Build slug map across all wikis for cross-wiki linking."""
    global_map = {}
    for wiki_dir in sorted(wikis_dir.iterdir()):
        if wiki_dir.is_dir() and not wiki_dir.name.startswith("."):
            wiki_slug = wiki_dir.name
            wiki_map = build_slug_map_for_wiki(wiki_dir, wiki_slug)
            # Detect bare-key collisions across wikis
            for key, url in wiki_map.items():
                if "/" not in key and key in global_map and global_map[key] != url:
                    print(f"WARNING: Cross-wiki bare key collision for '{key}': "
                          f"{global_map[key]} vs {url}", file=sys.stderr)
            global_map.update(wiki_map)
    return global_map


def collect_wiki_pages(wiki_dir: Path, slug_map: dict[str, str], wiki_slug: str) -> list[dict]:
    """Collect all pages from a single wiki."""
    pages = []
    seen_paths = set()

    for md_file in wiki_dir.rglob("*.md"):
        if md_file.name == "index.md":
            continue

        title = md_file.stem
        slug = slugify(title, allow_unicode=True)
        raw = md_file.read_text(encoding="utf-8", errors="replace")
        frontmatter, body = strip_frontmatter(raw)
        processed = process_markdown(body, slug_map, wiki_slug)
        html_content = md.render(processed)

        # Determine section from relative path
        rel = md_file.relative_to(wiki_dir)
        section = rel.parts[0] if len(rel.parts) > 1 else "pages"
        url_path = f"{wiki_slug}/{section}/{slug}/"

        if url_path in seen_paths:
            suffix = 2
            while f"{wiki_slug}/{section}/{slug}-{suffix}/" in seen_paths:
                suffix += 1
            new_path = f"{wiki_slug}/{section}/{slug}-{suffix}/"
            print(f"WARNING: Duplicate output path for '{url_path}' -> using '{new_path}'", file=sys.stderr)
            url_path = new_path
        seen_paths.add(url_path)

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
        raw = index_file.read_text(encoding="utf-8", errors="replace")
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

    # Generate wiki index page
    index_file = wiki_dir / "index.md"
    if index_file.exists():
        raw = index_file.read_text(encoding="utf-8", errors="replace")
        frontmatter, body = strip_frontmatter(raw)
        processed = process_markdown(body, slug_map, wiki_slug)
        html_content = md.render(processed)

        index_dir = OUTPUT_DIR / wiki_slug
        index_dir.mkdir(parents=True, exist_ok=True)

        html = page_template.render(
            title=wiki_meta["title"],
            content=Markup(html_content),
            section="index",
            wiki_slug=wiki_slug,
            wiki_title=wiki_meta["title"],
            frontmatter=frontmatter,
            site_url=site_url,
            url_path="",
        )
        (index_dir / "index.html").write_text(html, encoding="utf-8")

    for page in pages:
        page_dir = OUTPUT_DIR / page["url_path"]
        page_dir.mkdir(parents=True, exist_ok=True)

        html = page_template.render(
            title=page["title"],
            content=Markup(page["html_content"]),
            section=page["section"],
            wiki_slug=wiki_slug,
            wiki_title=wiki_meta["title"],
            frontmatter=page["frontmatter"],
            site_url=site_url,
            url_path=page["url_path"],
        )
        (page_dir / "index.html").write_text(html, encoding="utf-8")

    return pages, wiki_meta


def generate_sitemap(wiki_dirs: list[dict], site_url: str, extra_urls: list[str] | None = None,
                     lastmod: str | None = None) -> str:
    """Generate sitemap.xml for all wikis."""
    if lastmod is None:
        lastmod = datetime.now().strftime("%Y-%m-%d")
    if extra_urls is None:
        extra_urls = []

    urls = [f"""  <url>
    <loc>{html.escape(site_url)}/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
  </url>"""]

    for wiki in wiki_dirs:
        urls.append(f"""  <url>
    <loc>{html.escape(site_url)}/{html.escape(wiki['meta']['slug'])}/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>monthly</changefreq>
  </url>""")
        for page in wiki["pages"]:
            urls.append(f"""  <url>
    <loc>{html.escape(site_url)}/{html.escape(page['url_path'])}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>monthly</changefreq>
  </url>""")

    for url in extra_urls:
        urls.append(f"""  <url>
    <loc>{html.escape(url)}</loc>
    <lastmod>{lastmod}</lastmod>
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
    try:
        wiki_dirs = sorted([
            d for d in WIKIS_DIR.iterdir()
            if d.is_dir() and not d.name.startswith(".")
        ])
    except FileNotFoundError:
        print(f"ERROR: WIKIS_DIR not found: {WIKIS_DIR}", file=sys.stderr)
        sys.exit(1)
    print(f"  Found {len(wiki_dirs)} wikis: {[d.name for d in wiki_dirs]}")

    # Build global slug map
    slug_map = build_global_slug_map(WIKIS_DIR)
    print(f"  Mapped {len(slug_map)} page slugs across all wikis")

    # Setup templates
    try:
        env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)), autoescape=True)
        index_template = env.get_template("index.html")
    except Exception as e:
        print(f"ERROR: Failed to load templates from {TEMPLATE_DIR}: {e}", file=sys.stderr)
        sys.exit(1)

    # Build each wiki
    all_wikis = []
    all_pages = []
    for wiki_dir in wiki_dirs:
        pages, meta = build_wiki(wiki_dir, slug_map, env, SITE_URL)
        all_wikis.append({"meta": meta, "pages": pages})
        all_pages.extend(pages)
        print(f"  Built {wiki_dir.name}: {len(pages)} pages")

    # Build AI navigation guide if exists
    ai_file = WIKIS_DIR / "ai.md"
    if ai_file.exists():
        raw = ai_file.read_text(encoding="utf-8", errors="replace")
        frontmatter, body = strip_frontmatter(raw)
        processed = process_markdown(body, slug_map, "")
        html_content = md.render(processed)
        
        page_template = env.get_template("page.html")
        html = page_template.render(
            title=frontmatter.get("title", "AI Navigation Guide"),
            content=Markup(html_content),
            section="guide",
            wiki_slug="",
            wiki_title="World Knowledge",
            frontmatter=frontmatter,
            site_url=SITE_URL,
            url_path="ai/",
        )
        ai_dir = OUTPUT_DIR / "ai"
        ai_dir.mkdir(parents=True, exist_ok=True)
        (ai_dir / "index.html").write_text(html, encoding="utf-8")
        print("  Built /ai/ navigation guide")

    # Generate homepage
    index_html = index_template.render(
        wikis=[w["meta"] for w in all_wikis],
        site_url=SITE_URL,
        last_updated=datetime.now().strftime("%Y-%m-%d"),
        total_pages=len(all_pages),
    )
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Generate sitemap
    extra_urls = []
    if ai_file.exists():
        extra_urls.append(f"{SITE_URL}/ai/")
    sitemap = generate_sitemap(all_wikis, SITE_URL, extra_urls=extra_urls)
    (OUTPUT_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print(f"  Generated sitemap.xml with {len(all_pages) + 1 + len(extra_urls)} URLs")

    # Generate robots.txt
    robots_txt = f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
"""
    (OUTPUT_DIR / "robots.txt").write_text(robots_txt, encoding="utf-8")
    print("  Generated robots.txt")

    # Copy assets
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, OUTPUT_DIR / "assets", dirs_exist_ok=True)
        print("  Copied assets/")

    print(f"\nBuild complete: {OUTPUT_DIR}")
    print(f"  {len(all_wikis)} wikis, {len(all_pages)} total pages")


if __name__ == "__main__":
    build_site()
