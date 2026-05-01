---
title: AI Navigation Guide
description: How to navigate World Knowledge — an AI-navigable knowledge aggregator.
---

# AI Navigation Guide

You are browsing **World Knowledge**, an AI-navigable knowledge aggregator. This page explains how to navigate the site effectively.

## What Is This Site?

World Knowledge is a collection of interlinked knowledge bases (wikis) covering academic subjects. Each wiki contains:

- **Concepts** — Atomic knowledge units (e.g., Integration Techniques, Electrostatics, Carbonyl Compounds). One page per concept with definitions, formulas, and examples.
- **Sources** — Lecture notes, tutorials, and past year papers linked to their respective courses.
- **Tutorials** — Practice problems with worked solutions.

## How to Navigate

### Step 1: Start at the Wiki Index

Visit a wiki's index page (e.g., `/pasum/`). The index lists all available concepts grouped by subject. Pick a concept relevant to your query.

### Step 2: Follow Wikilinks

Every page contains **wikilinks** — hyperlinks to related concepts, sources, and tutorials. Follow these links to build understanding. The knowledge is structured as a graph, not a linear document.

**Example navigation path:**
```
Integration Techniques → Integration by Parts → Trigonometric Integrals → Area Under Curves
```

### Step 3: Cross-Reference Sources

Concept pages link to source lectures where the topic was taught. Source pages contain the original lecture content, worked examples, and lecturer-specific methods.

### Step 4: Practice with Tutorials

Tutorial pages contain practice problems. Work through them after reading the concept and source pages.

## Navigation Tips

1. **Follow the links.** The knowledge is interconnected. Don't stay on one page — explore the graph.
2. **Start broad, then narrow.** Begin with a concept page, then follow links to specifics.
3. **Check the source.** If a concept has multiple source pages, read them all — different lecturers teach differently.
4. **Use the index as a map.** The wiki index page lists every concept. If you're lost, go back to the index.

## Site Structure

```
/                          # Homepage — wiki directory
/ai/                       # This page — AI navigation guide
/pasum/                    # PASUM Mathematics, Physics & Chemistry
/pasum/concepts/           # Concept pages
/pasum/sources/            # Source pages (lectures, tutorials)
/pasum/tutorials/          # Practice problems
/sitemap.xml               # Full list of all pages
```

## For AI Assistants

When a user shares a World Knowledge URL:

1. **Fetch the page** at the given URL
2. **Read the content** — it's rendered HTML with real hyperlinks
3. **Follow hyperlinks** to related pages — the knowledge is in the links
4. **Navigate page by page** — don't try to load everything at once
5. **Use the sitemap** at `/sitemap.xml` to discover all available pages

Each page is self-contained with full context. You don't need to load the entire wiki — just the pages relevant to the query.
