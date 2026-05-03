---
name: academic-wiki
description: Build and maintain an academic wiki from lecture notes, tutorials, and exam papers. Use this skill when the user has academic materials (PDFs, ZIPs, lecture notes, tutorials, past year papers) they want to organize into a structured Obsidian wiki. Triggers on phrases like "build a wiki", "organize my notes", "process lectures", "catalogue academic materials", "create wiki from PDFs", or when the user mentions subjects like Mathematics, Physics, Chemistry, etc. with files to process. Also triggers when the user wants to ingest new sources into an existing academic wiki.
---

# Academic Wiki

Process academic materials (lectures, tutorials, finals) into a structured, interlinked Obsidian wiki. This skill combines the LLM Wiki pattern with academic study workflows.

## Related Skills

- **problem-set-synthesis** — Create interleaved problem sets for exam preparation (use when user wants practice problems, study sets, or mastery materials)

## Core Pattern

**Raw sources** (immutable) → **Wiki** (LLM-generated markdown) → **Schema** (this skill)

The LLM owns the wiki layer — creating source pages, concept explanations, and entity profiles. You curate sources and guide emphasis.

## Directory Structure

```
wiki/
├── inbox/                # New files awaiting processing
├── raw/                  # Original PDFs (immutable, processed)
│   ├── lectures/
│   ├── tutorials/
│   └── finals/
├── wiki/
│   ├── index.md          # Content catalog
│   ├── log.md            # Chronological record
│   ├── sources/          # Source summaries (lectures, tutorials, finals)
│   ├── concepts/         # Topic explanations
│   ├── entities/         # People, courses, institutions
│   └── synthesis/        # Cross-cutting analyses, problem sets, study materials
└── assets/               # Images, diagrams
```

## The Four Layers

### 1. Sources (`wiki/sources/`)
Summaries of individual lectures, tutorials, and exams.
- One page per source
- Links to course entity and concepts covered
- Example: `FAD1014 L21 — Introduction to Series.md`

### 2. Concepts (`wiki/concepts/`)
Topic explanations that may span multiple sources.
- One page per concept
- Links to all sources that mention it
- Example: `Taylor & Maclaurin Series.md`

### 3. Entities (`wiki/entities/`)
People, courses, institutions.
- Course pages list all lectures and concepts
- Lecturer pages list courses taught
- Example: `FAD1014 - Mathematics II.md`

### 4. Synthesis (`wiki/synthesis/`)
Cross-cutting analyses, problem sets, exam prep, comparative studies.
- Combines multiple concepts
- Study materials and practice sets
- Example: `FAD1014 Mastery Set — Interleaved Mathematics II.md`

## Workflow

### Phase 1: Survey

When the user provides academic materials:

1. **List all files** — use `glob` or `bash find` to discover PDFs, ZIPs, Markdown files
2. **Check inbox** — look in `inbox/` folder for new materials
3. **Extract ZIPs** — unzip to a staging area
4. **Sample content** — read first page of key PDFs to identify subjects
5. **Categorize** — sort by subject (Maths, Physics, Chemistry, etc.)
6. **Handle empty files** — remove or flag empty/corrupted files

### Phase 2: Content Extraction (Image-First)

**PRIMARY METHOD: Direct Image Processing**

Read PDFs directly as images using the file read tool. The read tool can process PDF files and return them as visual content.

```
Read: /path/to/lecture.pdf
```

**Why image-first:**
- Preserves mathematical notation, diagrams, and formatting exactly as presented
- Captures lecturer signatures, slide layouts, and visual annotations
- Handles scanned documents and complex layouts better than text extraction
- No loss of structural context (bullet points, tables, equations rendered visually)

**Process:**
1. Read the PDF file directly — the tool will render pages as images
2. Process content visually — transcribe equations, diagrams, and text
3. For multi-page PDFs, read sequentially if needed
4. Capture all visual information including:
   - Slide headers and titles
   - Mathematical equations (transcribe to LaTeX)
   - Diagrams and graphs (describe or note for asset extraction)
   - Lecturer signatures and attributions
   - Important highlights and annotations

**FALLBACK METHOD: Text Extraction**

Only use text extraction when direct image processing is unavailable or fails:

```bash
# Fallback 1: pdftotext
pdftotext "/path/to/lecture.pdf" -

# Fallback 2: Python
python3 -c "
from pypdf import PdfReader
reader = PdfReader('/path/to/lecture.pdf')
for page in reader.pages:
    print(page.extract_text())
"
```

**Tips for image processing:**
- Read all pages — academic content often spans multiple pages
- Transcribe math symbols carefully to LaTeX ($...$ inline, $...$ display)
- Look for lecturer signatures at end of slides
- Note any diagrams that should be extracted to assets/
- Handle complex layouts by describing structure

### Phase 3: Parallel Ingestion

**For multiple files in inbox:** Process concurrently using subagents.

Spawn one subagent per file (or per subject group):

```
Task per lecture:
- Read existing wiki/index.md for structure
- Create source page for the lecture
- Create/update concept pages for key topics
- Create/update entity pages (lecturers, courses)
- Update course entity with links
```

Each subagent should:
- Use Obsidian Flavored Markdown
- Include YAML frontmatter with title, date, tags, course
- Add wikilinks to related pages
- Follow existing wiki conventions
- Use LaTeX for mathematical formulas ($...$ for inline, $$...$$ for display)

### Phase 4: Index & Log

After subagents complete:

1. **Update index.md** — add new sources, concepts, entities
2. **Append to log.md** — record what was ingested with format: `[date] ingest | description`
3. **Verify links** — ensure all wikilinks resolve
4. **Archive sources** — move processed PDFs from `inbox/` to `raw/lectures/`

## Page Templates

### Source Page (Lecture)

```markdown
---
title: FAD1014 L1-L2 — Integration
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
lecturer: "[[Dr Name]]"
---

# FAD1014 L1-L2 — Integration

Brief summary of lecture content.

## Key Points
- Point 1
- Point 2

## Key Equations (for math lectures)
$$E = hf = \frac{hc}{\lambda}$$

## Links
- [[Integration Techniques]]
- [[FAD1014 - Mathematics II]]
```

### Concept Page

```markdown
---
title: Integration Techniques
date: 2026-04-27
tags:
  - concept
  - subject/mathematics
  - status/seedling
aliases:
  - Integration
---

# Integration Techniques

Explanation of the concept.

## Methods
1. Substitution
2. By Parts

## Related
- [[FAD1014 - Mathematics II]]
```

### Entity Page (Course)

```markdown
---
title: FAD1014 - Mathematics II
date: 2026-04-27
tags:
  - entity/course
  - subject/mathematics
institution: "[[University Name]]"
---

# FAD1014 — Mathematics II

Course description.

## Lectures
- [[FAD1014 L1-L2 — Integration]]

## Concepts
- [[Integration Techniques]]
```

### Synthesis Page (Problem Set)

```markdown
---
title: "FAD1014 Mastery Set — Interleaved Topics"
date: 2026-04-28
course: FAD1014 Mathematics II
tags: [mathematics, interleaved-practice, synthesis, mastery]
---

# [Course]: Interleaved Mastery Problem Set

Cross-cutting practice problems combining multiple topics.

## Problem 1: [Name]

(a) [Part using concept A]
(b) [Part using concept B]
(c) [Part connecting A and B]

## Related
- [[Concept A]]
- [[Concept B]]
- [[Source Lecture]]
```

## Karpathy Guidelines Applied

1. **Surgical changes** — each subagent touches only their subject area
2. **Simplicity first** — minimal viable wiki structure, expand as needed
3. **Goal-driven** — define success: all sources catalogued, all links resolve
4. **Surface assumptions** — if a PDF's subject is unclear, ask the user
5. **Concurrent processing** — use parallel subagents for multiple files

## Subagent Prompt Template

```
You are building the [SUBJECT] section of the academic wiki at [WIKI_PATH]

READ FIRST:
1. Read wiki/index.md to understand structure
2. Read existing source pages for format
3. Check for existing course/concept pages

LECTURE CONTENT:
Read the PDF file(s) directly to process them as images. Do NOT extract text via pdftotext or Python scripts. Process the visual content directly, transcribing equations to LaTeX and noting diagrams.

YOUR TASK:
Create pages for [COURSE CODE] [LECTURE TITLE]:

**Source Pages** (in wiki/sources/):
- Create: [[Course L## — Topic]]
- YAML frontmatter with title, date, tags, course link, lecturer
- Brief summary of lecture
- Key points with wikilinks to concepts
- Key equations in LaTeX
- Example problems if present
- Lecturer attribution (identify from signature)

**Concept Pages** (in wiki/concepts/):
- Create/update concept pages for key topics covered
- Include definitions, formulas, examples
- Link back to source page

**Entity Pages** (in wiki/entities/):
- Update course page to add lecture link
- Create/update lecturer entity if new

**Log Update**:
- Append to wiki/log.md with ingestion record

Return summary of pages created/modified.
```

## Example Execution

### Scenario 1: Processing Inbox with Multiple Files

**User**: "Do the same for the current inbox. Do it concurrently"

**Agent**:
1. List inbox contents — find 3 files (2 PDFs, 1 MD)
2. Check MD file — empty, remove it
3. Extract text from both PDFs concurrently
4. Spawn 2 subagents in parallel (one per PDF)
5. Each subagent creates source page + concept pages
6. Update index.md with all new pages
7. Archive PDFs to raw/lectures/
8. Append to log.md: "[date] ingest | 2 lecture PDFs → 2 source pages, 4 concept pages"

### Scenario 2: Bulk Import from Downloads

**User**: "I have a bunch of lecture PDFs in ~/Downloads/lectures/ for my PASUM courses"

**Agent**:
1. Survey ~/Downloads/lectures/ — find 50 PDFs across Maths, Physics, Chemistry
2. Spawn 3 subagents (one per subject) to process in parallel
3. Each subagent creates ~15 source pages + 5 concept pages + 2 entity pages
4. Update index.md with all new pages
5. Append to log.md: "[date] ingest | 50 lecture PDFs → 45 source pages, 12 concept pages"

### Scenario 3: Creating Synthesis Materials

**User**: "I want to study Mathematics II for 5 days. Create interleaved problems covering Geometry, Series, Taylor-Maclaurin, and Trigonometric Integration."

**Agent**:
1. Load problem-set-synthesis skill
2. Read relevant tutorials to understand question formats
3. Read concept pages for formulas
4. Design 15 interleaved problems
5. Create file in `wiki/synthesis/`
6. Update index.md synthesis section
7. Append to log.md: "[date] create | Interleaved mastery problem set"

## Tips

- **Lecture Note Method**: If the user's lecturer emphasizes a specific note-taking method, follow it strictly
- **Tutorials are gold**: Transcribe tutorial questions fully — they're primary study material
- **Cross-reference**: Link concept pages to multiple courses when topics overlap
- **Status tags**: Use `status/seedling` for new pages, `status/evergreen` for mature pages
- **Parallelize**: Always use subagents for multi-file ingestion — it's much faster
- **Math Formulas**: Use LaTeX ($...$ for inline, $$...$$ for display) for all mathematical expressions
- **Lecturer Identification**: Look for signatures at end of slides (e.g., "Dr Name", "Thank you, Dr X")
- **Empty Files**: Remove empty or corrupted files from inbox after noting them
- **Archive After Processing**: Always move processed files from inbox to raw/ to maintain clean workflow
- **Wiki Health**: Update the health stats in index.md after each ingestion
- **Synthesis Layer**: Use synthesis/ for cross-cutting materials like problem sets, exam prep, comparative analyses
