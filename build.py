#!/usr/bin/env python3
"""
textbase.fyi — Multi-wiki static site builder
AI-first, human-readable knowledge base. Aggregates Obsidian wikis into a
single website with freshness indicators, recommended LLM skills, and RSS feeds.
"""

import html
import hashlib
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

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
    SITE_URL = os.environ.get("CF_PAGES_URL", "").rstrip("/") or "https://textbase.fyi"
    if not SITE_URL.startswith("http"):
        SITE_URL = f"https://{SITE_URL}"

if SITE_URL == "https://textbase.fyi":
    print("WARNING: Using fallback URL https://textbase.fyi. Set SITE_URL or CF_PAGES_URL.", file=sys.stderr)

# ── Color palette for hash-derived wiki accent colors ───────────────────

COLOR_PALETTE = [
    "#e65c4f",  # red
    "#e8893c",  # orange
    "#d4a02b",  # gold
    "#6ba84d",  # green
    "#3d9b8f",  # teal
    "#4a8dcf",  # blue
    "#8a6fc4",  # purple
    "#c95f96",  # pink
]

def hash_color(slug: str) -> str:
    """Deterministic color from wiki slug."""
    h = hashlib.md5(slug.encode()).hexdigest()
    idx = int(h[:8], 16) % len(COLOR_PALETTE)
    return COLOR_PALETTE[idx]


def compute_root_path(url_path: str) -> str:
    """Compute relative path from a page to the site root.
    e.g. 'pasum/concepts/foo/' -> '../../../' ; 'pasum/' -> '../' ; '' -> './'"""
    if not url_path:
        return "./"
    parts = [p for p in url_path.split("/") if p]
    depth = len(parts)
    if depth <= 1:
        return "../"
    return "../" * depth


# ── Markdown setup ──────────────────────────────────────────────────────

md = MarkdownIt("commonmark", {"html": True})
md.enable("table")
md.enable("strikethrough")


# ── Utilities ───────────────────────────────────────────────────────────

GIT_CACHE: dict[str, str | None] = {}

def get_git_date(filepath: Path, repo_root: Path = None) -> str | None:
    """Get the last commit date of a file from git log."""
    if repo_root is None:
        repo_root = Path.cwd()
    
    abs_path = filepath.resolve()
    if abs_path in GIT_CACHE:
        return GIT_CACHE[abs_path]
    
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "log", "-1", "--format=%aI", "--", str(abs_path)],
            capture_output=True, text=True, timeout=5,
        )
        date = result.stdout.strip() or None
        GIT_CACHE[abs_path] = date
        return date
    except (subprocess.SubprocessError, FileNotFoundError):
        GIT_CACHE[abs_path] = None
        return None

def format_date(date_str: str | None) -> str:
    """Format ISO date to YYYY-MM-DD."""
    if not date_str:
        return ""
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return date_str[:10] if date_str else ""

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

RECOGNIZED_SECTIONS = {"concepts", "sources", "tutorials", "entities"}

def build_slug_map_for_wiki(wiki_dir: Path, wiki_slug: str) -> dict[str, str]:
    """Build slug map for a single wiki."""
    slug_map = {}
    seen = set()
    for md_file in wiki_dir.rglob("*.md"):
        name = md_file.name
        if name in ("index.md", "log.md"):
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
    # Add changelog slug
    slug_map[f"{wiki_slug}/changelog"] = f"/{wiki_slug}/changelog/"
    return slug_map


def build_global_slug_map(wikis_dir: Path) -> dict[str, str]:
    """Build slug map across all wikis for cross-wiki linking."""
    global_map = {}
    for wiki_dir in sorted(wikis_dir.iterdir()):
        if wiki_dir.is_dir() and not wiki_dir.name.startswith("."):
            wiki_slug = wiki_dir.name
            wiki_map = build_slug_map_for_wiki(wiki_dir, wiki_slug)
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
        name = md_file.name
        if name in ("index.md", "log.md"):
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

        # Get last edited date
        git_date = get_git_date(md_file)
        git_date_fmt = format_date(git_date) if git_date else None
        fm_date = frontmatter.get("date", None)
        if fm_date:
            fm_date = format_date(str(fm_date))
        last_edited = git_date_fmt or fm_date or ""

        pages.append({
            "title": frontmatter.get("title", title),
            "section": section,
            "slug": slug,
            "url_path": url_path,
            "frontmatter": frontmatter,
            "html_content": html_content,
            "wiki_slug": wiki_slug,
            "source_file": str(md_file.relative_to(wiki_dir)),
            "last_edited": last_edited,
        })

    return pages


def read_wiki_index(wiki_dir: Path) -> dict:
    """Read the index.md frontmatter for a wiki."""
    index_file = wiki_dir / "index.md"
    if index_file.exists():
        raw = index_file.read_text(encoding="utf-8", errors="replace")
        frontmatter, body = strip_frontmatter(raw)
        skills = frontmatter.get("skills", [])
        # Parse skills from frontmatter
        parsed_skills = []
        for skill in skills:
            if isinstance(skill, dict):
                parsed_skills.append({
                    "name": skill.get("name", ""),
                    "purpose": skill.get("purpose", ""),
                    "auto_offer": skill.get("auto_offer", False),
                })
        
        color_override = frontmatter.get("color", None)
        
        return {
            "title": frontmatter.get("title", wiki_dir.name),
            "description": frontmatter.get("description", ""),
            "tags": frontmatter.get("tags", []),
            "author": frontmatter.get("author", ""),
            "slug": wiki_dir.name,
            "skills": parsed_skills,
            "color_override": color_override,
        }
    return {
        "title": wiki_dir.name,
        "description": "",
        "tags": [],
        "author": "",
        "slug": wiki_dir.name,
        "skills": [],
        "color_override": None,
    }


def read_wiki_log(wiki_dir: Path, slug_map: dict, wiki_slug: str) -> str | None:
    """Read and render the wiki log.md as HTML, if it exists."""
    log_file = wiki_dir / "log.md"
    if log_file.exists():
        raw = log_file.read_text(encoding="utf-8", errors="replace")
        _, body = strip_frontmatter(raw)
        processed = process_markdown(body, slug_map, wiki_slug)
        return md.render(processed)
    return None


# ── RSS Feed Generation ──────────────────────────────────────────────

def generate_atom_feed(
    site_url: str,
    title: str,
    entries: list[dict],
    feed_path: str,
    updated: str | None = None,
) -> str:
    """Generate an Atom 1.0 feed."""
    if updated is None:
        updated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    
    feed_id = f"{site_url}/{feed_path}"
    entries_xml = []
    
    for entry in entries[:50]:  # max 50 entries per feed
        entry_id = f"{site_url}/{entry['url_path']}"
        entry_updated = entry.get("last_edited", "") or updated
        if entry_updated and len(entry_updated) == 10:
            entry_updated += "T00:00:00Z"
        elif entry_updated:
            try:
                dt = datetime.fromisoformat(entry_updated)
                entry_updated = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            except (ValueError, TypeError):
                entry_updated = updated
        
        title_escaped = html.escape(entry.get("title", ""))
        summary = entry.get("summary", "")
        
        entries_xml.append(f"""  <entry>
    <id>{html.escape(entry_id)}</id>
    <title>{title_escaped}</title>
    <updated>{entry_updated}</updated>
    <link rel="alternate" href="{html.escape(entry_id)}"/>
    <summary>{html.escape(summary)}</summary>
  </entry>""")
    
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <id>{html.escape(feed_id)}</id>
  <title>{html.escape(title)}</title>
  <updated>{updated}</updated>
  <link rel="alternate" href="{html.escape(site_url)}/"/>
  <link rel="self" href="{html.escape(site_url)}/{html.escape(feed_path)}"/>
{chr(10).join(entries_xml)}
</feed>"""


# ── Build ──────────────────────────────────────────────────────────────

def build_wiki(wiki_dir: Path, slug_map: dict[str, str], templates: Environment, site_url: str) -> tuple[list[dict], dict]:
    """Build all pages for a single wiki. Returns (pages, metadata)."""
    wiki_slug = wiki_dir.name
    wiki_meta = read_wiki_index(wiki_dir)
    wiki_color = wiki_meta.get("color_override") or hash_color(wiki_slug)
    pages = collect_wiki_pages(wiki_dir, slug_map, wiki_slug)

    page_template = templates.get_template("page.html")
    repo_root = Path.cwd()

    # Determine overall wiki last-updated date
    wiki_last_updated = ""
    all_dates = [p["last_edited"] for p in pages if p["last_edited"]]
    if all_dates:
        all_dates.sort(reverse=True)
        wiki_last_updated = all_dates[0]
    # Also check log.md date
    log_file = wiki_dir / "log.md"
    if log_file.exists():
        git_log_date = get_git_date(log_file)
        if git_log_date:
            fm = format_date(git_log_date)
            if fm and (not wiki_last_updated or fm > wiki_last_updated):
                wiki_last_updated = fm

    # Generate wiki index page
    index_file = wiki_dir / "index.md"
    if index_file.exists():
        raw = index_file.read_text(encoding="utf-8", errors="replace")
        frontmatter, body = strip_frontmatter(raw)
        processed = process_markdown(body, slug_map, wiki_slug)
        html_content = md.render(processed)

        index_dir = OUTPUT_DIR / wiki_slug
        index_dir.mkdir(parents=True, exist_ok=True)

        root_path = compute_root_path(f"{wiki_slug}/")

        html = page_template.render(
            title=wiki_meta["title"],
            content=Markup(html_content),
            section="index",
            wiki_slug=wiki_slug,
            wiki_title=wiki_meta["title"],
            wiki_description=wiki_meta["description"],
            wiki_author=wiki_meta["author"],
            frontmatter=frontmatter,
            site_url=site_url,
            url_path="",
            skills=wiki_meta["skills"],
            last_updated=wiki_last_updated,
            wiki_color=wiki_color,
            root_path=root_path,
        )
        (index_dir / "index.html").write_text(html, encoding="utf-8")

    for page in pages:
        page_dir = OUTPUT_DIR / page["url_path"]
        page_dir.mkdir(parents=True, exist_ok=True)
        root_path = compute_root_path(page["url_path"])

        html = page_template.render(
            title=page["title"],
            content=Markup(page["html_content"]),
            section=page["section"],
            wiki_slug=wiki_slug,
            wiki_title=wiki_meta["title"],
            wiki_description=wiki_meta["description"],
            wiki_author=wiki_meta["author"],
            frontmatter=page["frontmatter"],
            site_url=site_url,
            url_path=page["url_path"],
            skills=[],
            last_updated=page["last_edited"],
            wiki_color=wiki_color,
            root_path=root_path,
        )
        (page_dir / "index.html").write_text(html, encoding="utf-8")

    # Build changelog page from log.md
    log_html_content = read_wiki_log(wiki_dir, slug_map, wiki_slug)
    if log_html_content:
        changelog_dir = OUTPUT_DIR / wiki_slug / "changelog"
        changelog_dir.mkdir(parents=True, exist_ok=True)
        
        log_git_date = get_git_date(log_file)
        log_last_updated = format_date(log_git_date) if log_git_date else wiki_last_updated
        root_path = compute_root_path(f"{wiki_slug}/changelog/")
        
        html = page_template.render(
            title="Changelog",
            content=Markup(log_html_content),
            section="changelog",
            wiki_slug=wiki_slug,
            wiki_title=wiki_meta["title"],
            wiki_description=wiki_meta["description"],
            wiki_author=wiki_meta["author"],
            frontmatter={"title": "Changelog"},
            site_url=site_url,
            url_path=f"{wiki_slug}/changelog/",
            skills=[],
            last_updated=log_last_updated,
            wiki_color=wiki_color,
            root_path=root_path,
        )
        (changelog_dir / "index.html").write_text(html, encoding="utf-8")

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
        wiki_slug = wiki["meta"]["slug"]
        urls.append(f"""  <url>
    <loc>{html.escape(site_url)}/{html.escape(wiki_slug)}/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
  </url>""")
        # Add changelog
        urls.append(f"""  <url>
    <loc>{html.escape(site_url)}/{html.escape(wiki_slug)}/changelog/</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
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
    print(f"Building textbase.fyi from {WIKIS_DIR} → {OUTPUT_DIR}")

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
            wiki_title="textbase.fyi",
            wiki_description="AI-navigable knowledge base",
            wiki_author="",
            frontmatter=frontmatter,
            site_url=SITE_URL,
            url_path="ai/",
            skills=[],
            last_updated="",
            wiki_color=COLOR_PALETTE[0],
            root_path="../",
        )
        ai_dir = OUTPUT_DIR / "ai"
        ai_dir.mkdir(parents=True, exist_ok=True)
        (ai_dir / "index.html").write_text(html, encoding="utf-8")
        print("  Built /ai/ navigation guide")

    # Compute site-wide last updated
    site_last_updated = datetime.now().strftime("%Y-%m-%d")

    # Generate homepage
    index_html = index_template.render(
        wikis=[w["meta"] for w in all_wikis],
        site_url=SITE_URL,
        last_updated=site_last_updated,
        total_pages=len(all_pages),
        total_wikis=len(all_wikis),
        root_path="./",
    )
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")

    # Generate sitemap
    extra_urls = []
    if ai_file.exists():
        extra_urls.append(f"{SITE_URL}/ai/")
    for w in all_wikis:
        extra_urls.append(f"{SITE_URL}/{w['meta']['slug']}/changelog/")
    sitemap = generate_sitemap(all_wikis, SITE_URL, extra_urls=extra_urls, lastmod=site_last_updated)
    (OUTPUT_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print(f"  Generated sitemap.xml with URLs")

    # Generate robots.txt
    robots_txt = f"""User-agent: *
Allow: /
Sitemap: {SITE_URL}/sitemap.xml
"""
    (OUTPUT_DIR / "robots.txt").write_text(robots_txt, encoding="utf-8")
    print("  Generated robots.txt")

    # Generate Atom feeds
    all_feed_entries = []
    for w in all_wikis:
        wiki_slug = w["meta"]["slug"]
        per_wiki_entries = []
        for page in w["pages"]:
            entry = {
                "title": page["title"],
                "url_path": page["url_path"],
                "last_edited": page["last_edited"],
                "summary": f"Updated in {wiki_slug}/{page['section']}",
            }
            per_wiki_entries.append(entry)
            all_feed_entries.append(entry)
        
        # Sort by date
        per_wiki_entries.sort(key=lambda e: e["last_edited"] or "", reverse=True)
        
        if per_wiki_entries:
            wiki_feed = generate_atom_feed(
                SITE_URL,
                f"{w['meta']['title']} — textbase.fyi",
                per_wiki_entries,
                f"{wiki_slug}/feed.xml",
            )
            feed_dir = OUTPUT_DIR / wiki_slug
            feed_dir.mkdir(parents=True, exist_ok=True)
            (feed_dir / "feed.xml").write_text(wiki_feed, encoding="utf-8")
            print(f"  Generated /{wiki_slug}/feed.xml ({len(per_wiki_entries)} entries)")

    # Global feed
    all_feed_entries.sort(key=lambda e: e["last_edited"] or "", reverse=True)
    global_feed = generate_atom_feed(
        SITE_URL,
        "textbase.fyi — All Updates",
        all_feed_entries,
        "feed.xml",
    )
    (OUTPUT_DIR / "feed.xml").write_text(global_feed, encoding="utf-8")
    print(f"  Generated /feed.xml ({len(all_feed_entries)} entries)")

    # Copy assets
    if ASSETS_DIR.exists():
        shutil.copytree(ASSETS_DIR, OUTPUT_DIR / "assets", dirs_exist_ok=True)
        print("  Copied assets/")

    print(f"\nBuild complete: {OUTPUT_DIR}")
    print(f"  {len(all_wikis)} wikis, {len(all_pages)} total pages")


if __name__ == "__main__":
    build_site()
