---
name: llm-wiki
description: Build and maintain a persistent Obsidian wiki knowledge base using LLMs. Use this skill whenever the user wants to create, ingest, query, or maintain a personal wiki powered by an LLM — whether they mention "LLM wiki," "Karpathy wiki," "knowledge base," "personal wiki," "Obsidian wiki," "ingest sources," "build a knowledge base," "wiki from articles," or want to organize research notes, book notes, project docs, meeting notes, or any collection of documents into an interlinked markdown wiki. Also triggers when the user mentions "Memex," "Zettelkasten," "evergreen notes," or wants to accumulate knowledge over time rather than doing one-shot RAG queries. Make sure to trigger on implicit requests too — e.g., "I want to save what I learn about topic X" or "help me organize my research on Y."
---

# LLM Wiki Pattern

Build and maintain a persistent, interlinked Obsidian wiki using an LLM. The wiki is a directory of markdown files that the LLM owns — it creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You (the human) curate sources, ask questions, and guide the analysis. The LLM does the bookkeeping.

**The core idea**: Instead of RAG (re-discovering knowledge from raw docs on every query), the LLM **incrementally builds a persistent wiki** that compounds over time. Cross-references are already there. Contradictions are flagged. The synthesis reflects everything you've read. The wiki gets richer with every source ingested and every question asked.

Think of it like this: Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase.

---

## Three Layers

1. **Raw sources** — your curated collection of source documents (articles, papers, notes). Immutable — the LLM reads but never modifies them.
2. **The wiki** — a directory of LLM-generated markdown files. The LLM owns this layer entirely.
3. **The schema** — conventions for how the wiki is structured (AGENTS.md / CLAUDE.md). Co-evolved with the LLM.

## Directory Structure Convention

```
wiki/
├── raw/                  # Source documents (immutable)
│   ├── articles/
│   ├── papers/
│   └── notes/
├── wiki/                 # The wiki itself
│   ├── index.md          # Content-oriented catalog of all pages
│   ├── log.md            # Chronological, append-only record of operations
│   ├── entities/         # Pages for people, places, organizations
│   ├── concepts/         # Pages for ideas, theories, terms
│   ├── sources/          # Summaries of ingested sources
│   └── synthesis/        # Cross-cutting analyses, comparisons, syntheses
└── assets/               # Images, diagrams, etc.
```

## Operations Workflow

When the user asks you to do something with their wiki, follow the pattern below. Use surgical changes (touch only what must change). Define verifiable success criteria for each operation.

### Ingest

When the user provides a new source (article, paper, note, podcast transcript, etc.):

1. **Read the source** thoroughly
2. **Discuss key takeaways** with the user — ask what to emphasize
3. **Write a summary page** in `wiki/sources/` with:
   - YAML frontmatter (title, date, source type, tags)
   - Summary of key points
   - Links to relevant entity and concept pages (created or updated as needed)
4. **Update or create entity/concept pages** that the source touches
5. **Update `wiki/index.md`** — add the new source and any new pages
6. **Append to `wiki/log.md`** with a consistent date-prefixed entry

Format for log entries:
```markdown
## [YYYY-MM-DD] ingest | Source Title
- Created/updated: [list of pages touched]
```

**Karpathy guideline**: State your plan before starting:
```
1. Read source → verify: summarized key points with user
2. Create/update wiki pages → verify: index.md updated, log.md appended, cross-references added
```

### Query

When the user asks a question:

1. **Read `wiki/index.md`** to find relevant pages
2. **Drill into specific pages** as needed
3. **Synthesize an answer** with citations to specific wiki pages
4. **File good answers back** into the wiki as new synthesis pages (in `wiki/synthesis/`)

Good answers don't disappear into chat history — they compound in the knowledge base.

### Lint / Health Check

Periodically run a health check:

- **Contradictions** between pages that newer sources superseded
- **Orphan pages** with no inbound links
- **Missing pages** — important concepts mentioned but lacking their own page
- **Stale claims** — assertions contradicted by newer sources
- **Cross-reference gaps** — pages that should link to each other but don't
- **Data gaps** — questions the wiki can't answer that a web search might fill

### Create

When starting a new wiki from scratch:

1. Ask the user: what domain/topic? What's the scope?
2. Create the directory structure
3. Create `wiki/index.md` and `wiki/log.md` with initial entries
4. Create initial entity/concept pages based on what the user knows so far
5. Ask the user for their first sources to ingest

## Obsidian Markdown Conventions

Use Obsidian Flavored Markdown for all wiki pages:

### Frontmatter (Properties)

```yaml
---
title: Page Title
date: 2026-04-27
tags:
  - topic
  - status/active
aliases:
  - Alternative Name
sources:
  - "[[Source Page]]"
---
```

### Links

- **Wikilinks** for internal pages: `[[Entity Name]]`, `[[Entity Name|Display Text]]`
- **External links** for URLs: `[text](url)`
- **Heading links**: `[[Page#Heading]]`

### Callouts

Use callouts for structure:
- `> [!note]` — General information
- `> [!warning]` — Contradictions or unresolved questions
- `> [!quote]` — Direct quotes from sources
- `> [!example]` — Examples
- `> [!info]` — Additional context
- `> [!question]` — Open questions for future investigation

### Tags

```yaml
tags:
  - topic/subtopic
  - status/evergreen
```

Tags allow Obsidian Dataview queries. Include status tags like:
- `status/seedling` — newly created, needs more content
- `status/evergreen` — well-developed, stable
- `status/draft` — in progress, likely to change

### Embeds

Use `![[image.png]]` for embedded images. Images go in `assets/`.

### Synthesis Pages Format

```markdown
---
title: Comparison of X and Y
date: 2026-04-27
tags:
  - synthesis
  - topic/comparison
---

# Comparison of X and Y

Key differences between [[Entity X]] and [[Entity Y]].

> [!note]
> This synthesis was generated in response to: [user's question]
```