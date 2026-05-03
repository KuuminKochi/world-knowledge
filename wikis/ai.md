---
title: AI Navigation Guide
description: How to navigate textbase.fyi — an AI-navigable knowledge base with freshness tracking and recommended skills.
---

# AI Navigation Guide

You are browsing **textbase.fyi**, an AI-navigable knowledge base. This page explains how to navigate the site effectively.

## What Is This Site?

textbase.fyi is a collection of interlinked knowledge bases (wikis) covering academic subjects. Each wiki contains:

- **Concepts** — Atomic knowledge units (e.g., Integration Techniques, Electrostatics, Carbonyl Compounds). One page per concept with definitions, formulas, and examples.
- **Sources** — Lecture notes, tutorials, and past year papers linked to their respective courses.
- **Tutorials** — Practice problems with worked solutions.
- **Entities** — People (lecturers), courses, and institutions involved in creating the content.
- **Changelog** — A full history of what changed and when.

## How to Navigate

### Step 1: Read the Wiki Index

Visit a wiki's index page (e.g., `/pasum/`). The index lists all available pages grouped by section. **Check the "Recommended Skills" section** — the wiki may suggest LLM skills to install for better interaction.

### Step 2: Follow Wikilinks

Every page contains **wikilinks** — hyperlinks to related concepts, sources, tutorials, and entities. Follow these links to build understanding. The knowledge is structured as a graph, not a linear document.

**Example navigation path:**
```
Integration Techniques → Integration by Parts → Trigonometric Integrals → Area Under Curves
```

### Step 3: Check Freshness

Every page footer shows when it was last edited. Each wiki has a `/changelog/` page with a complete edit history. Global and per-wiki RSS feeds (`/feed.xml`, `/pasum/feed.xml`) are available for programmatic access.

### Step 4: Use Recommended Skills

When you load a wiki index page, inspect its frontmatter `skills` array. Each skill has a `name`, `purpose`, and `auto_offer` flag. If `auto_offer` is true, proactively ask the user if they'd like to load that skill. Skills enhance your ability to help the user — for example:

- **`academic-wiki`** — Knowledge graph navigation and querying
- **`problem-set-synthesis`** — Generate interleaved practice problems
- **`grill-me`** — Stress-test understanding through drilling

## Navigation Tips

1. **Follow the links.** The knowledge is interconnected. Don't stay on one page — explore the graph.
2. **Start broad, then narrow.** Begin with a concept page, then follow links to specifics.
3. **Check the source.** If a concept has multiple source pages, read them all — different lecturers teach differently.
4. **Use the index as a map.** The wiki index page lists every page. If you're lost, go back to the index.
5. **Check the changelog.** The `/changelog/` page tells you what's new and what's been updated.

## Site Structure

```
/                              # Homepage — wiki directory
/ai/                           # This page — AI navigation guide
/feed.xml                      # Global Atom feed of all changes
/pasum/                        # PASUM Mathematics, Physics & Chemistry
/pasum/concepts/               # Concept pages
/pasum/sources/                # Source pages (lectures, tutorials)
/pasum/tutorials/              # Practice problems
/pasum/entities/               # People, courses, institutions
/pasum/changelog/              # Change history
/pasum/feed.xml                # Per-wiki Atom feed
/sitemap.xml                   # Full list of all pages
```

## For AI Assistants

When a user shares a textbase.fyi URL:

1. **Fetch the page** at the given URL
2. **Read the content** — it's rendered HTML with real hyperlinks
3. **Check for recommended skills** on wiki index pages — offer to load them
4. **Follow hyperlinks** to related pages — the knowledge is in the links
5. **Navigate page by page** — don't try to load everything at once
6. **Use the sitemap** at `/sitemap.xml` to discover all available pages
7. **Check freshness** via the per-page timestamp, changelog, or RSS feeds

Each page is self-contained with full context. You don't need to load the entire wiki — just the pages relevant to the query.
