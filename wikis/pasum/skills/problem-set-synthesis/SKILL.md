---
name: problem-set-synthesis
description: Create interleaved problem sets that combine multiple mathematical topics for deeper learning. Use when the user wants to study for exams, create practice problems, or build mastery through mixed practice. Triggers on phrases like "create problem set", "practice problems", "interleaved practice", "mastery problems", "study plan", or when the user wants to combine multiple topics into exercises.
---

# Problem Set Synthesis

Create interleaved problem sets that weave together multiple mathematical topics. This skill produces synthesis-level study materials that force the brain to recognize which techniques to apply, building stronger neural connections than siloed practice.

## When to Use

- Student preparing for comprehensive exams
- Creating mastery-level practice materials
- Building study plans that span multiple days
- Combining topics that are usually taught separately

## Workflow

### Phase 1: Gather Context

1. **Read existing tutorials** — understand question formats and difficulty levels
2. **Review concept pages** — identify key formulas and techniques
3. **Check lecture sources** — align with course content
4. **Identify target topics** — list all areas to interleave

### Phase 2: Design Interleaved Problems

Each problem should require **2-4 different techniques** from different topics.

**Good interleaving:**
- Geometry + Series + Integration (Problem uses circle equation, requires series expansion of sqrt, integrates using trig sub)
- Taylor series + Trigonometric identities + Definite integrals

**Bad interleaving:**
- 10 geometry problems, then 10 series problems (not interleaved—just sequential)

### Phase 3: Create Problem Structure

Each problem should have:

1. **Context/Story** — real-world application (physics, engineering, architecture)
2. **Progressive parts (a), (b), (c)...** — each part uses different technique
3. **Verification steps** — compare approximate (series) to exact (integration) answers
4. **Difficulty ramp** — start accessible, build to challenging

### Phase 4: Write Problem Set

Create file in `wiki/synthesis/`:

```markdown
---
title: "[Course] Mastery Set — Interleaved [Topics]"
date: YYYY-MM-DD
course: [Course Code] [Subject]
tags: [mathematics, interleaved-practice, topic1, topic2, mastery]
---

# [Course]: [Subject] — Interleaved Mastery Problem Set

**[X]-Day Intensive Study Plan**
**Topics:** [List all topics]

## How to Use This Set

Each problem intentionally **mixes multiple concepts**...

## The Mastery Problems

### Problem 1: [Descriptive Name] [Topic1 + Topic2 + Topic3]

[Context/setup]

**(a)** [Geometry part]

**(b)** [Series part]

**(c)** [Integration part]

**(d)** [Connection/verification part]
```

### Phase 5: Add Supporting Materials

1. **Techniques summary table** — show which problems use which techniques
2. **Formula reference** — key equations for all topics
3. **Study schedule** — day-by-day breakdown
4. **Related resources** — wikilinks to concept pages

## Problem Templates

### Template 1: The Physical Object

```
A [parabolic mirror/cooling tower/elliptical orbit] has equation [conic section equation].

(a) Find [geometric property]
(b) A [physical phenomenon] occurs at [condition]. Calculate [value].
(c) Expand [function] as [series type] to approximate [quantity].
(d) The exact answer requires [integral]. Evaluate using [technique] and compare.
```

### Template 2: The Parametric Motion

```
A particle moves along [parametric equations involving trig functions].

(a) Show the path lies on [conic section].
(b) Find the Maclaurin/Taylor series for [component] up to [term].
(c) Find slope/area/arc length using parametric derivatives.
(d) Evaluate the resulting integral using [trig technique].
```

### Template 3: The Approximation Verification

```
Consider [function with integral].

(a) Find the [series expansion] up to [term].
(b) Approximate [definite integral] by integrating series term-by-term.
(c) Evaluate the integral exactly using [substitution/technique].
(d) Calculate percentage error. How many terms needed for [accuracy]?
```

## Quality Checklist

- [ ] Each problem uses ≥2 distinct topics
- [ ] Problems increase in difficulty
- [ ] Real-world contexts where possible
- [ ] Verification steps (approximate vs exact)
- [ ] Formula reference included
- [ ] Study schedule provided
- [ ] All wikilinks resolve to concept pages
- [ ] Matches tutorial question style

## Example Execution

**User**: "I want to study Mathematics II for 5 days, covering Geometry, Series, Taylor-Maclaurin, and Trigonometric Integration. Create interleaved problems."

**Agent**:
1. Read Tutorial 12 (Power Series + Circle Geometry) — see how questions combine topics
2. Read Tutorial 3 (Trigonometric Integrals) — understand integration techniques
3. Read concept pages for all four topics
4. Design 15 problems, each mixing 2-4 topics:
   - Problem 1: Circle + Maclaurin + Trig integration (area formula)
   - Problem 2: Parabola + Binomial series + Trig substitution (arc length)
   - ...etc
5. Create file: `wiki/synthesis/FAD1014 Mastery Set — Interleaved Mathematics II.md`
6. Update index.md synthesis section
7. Append to log.md

## Integration with Academic Wiki

Problem sets are **synthesis documents** — they live in `wiki/synthesis/` and link together concepts from multiple sources.

Update academic-wiki skill:
- Add synthesis folder to directory structure
- Add problem-set-synthesis as related skill
- Reference in tips section

## Tips

- **Interleave, don't batch** — never group all problems of one type together
- **Verification builds confidence** — always include "check your answer" steps
- **Physical contexts help** — mirrors, orbits, pendulums, arches
- **Progressive difficulty** — parts (a)→(d) should build complexity
- **Formula overload** — provide reference sheet; problems should test application, not memorization
- **Time estimates** — consider adding suggested time per problem for exam practice
