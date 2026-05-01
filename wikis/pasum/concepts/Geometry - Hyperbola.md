---
title: Geometry - Hyperbola
date: 2026-04-27
tags:
  - concept
  - subject/mathematics-ii
  - topic/geometry
  - status/seedling
aliases:
  - Hyperbola
course: "[[FAD1014 - Mathematics II]]"
sources:
  - "[[L31-L32 Hyperbola]]"
---

# Hyperbola

A conic section defined as the set of all points where the absolute difference of distances to two foci is constant.

## Standard Equations

| Orientation | Equation | Transverse axis |
|---|---|---|
| Horizontal | $\frac{(x-h)^2}{a^2} - \frac{(y-k)^2}{b^2} = 1$ | Horizontal ($y = k$) |
| Vertical | $\frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1$ | Vertical ($x = h$) |

## Key Relations

- $a^2 + b^2 = c^2$ (where $c$ is focal distance from centre)
- Vertices are $a$ units from centre along transverse axis
- Foci are $c$ units from centre along transverse axis

## Asymptotes

- Horizontal: $y - k = \pm \frac{b}{a}(x - h)$
- Vertical: $y - k = \pm \frac{a}{b}(x - h)$

## Conic Section Relationships

```mermaid
flowchart LR
    CONICS((Conic Sections))
    CONICS --> ELLIPSE[Ellipse<br/>Sum of distances to foci is constant]
    CONICS --> PARABOLA[Parabola<br/>Equidistant from focus and directrix]
    CONICS --> HYPERBOLA[Hyperbola<br/>Difference of distances to foci is constant]
    ELLIPSE --> CIRCLE[Circle<br/>Special case: a = b]
```

## Identifying Conic Sections

```mermaid
flowchart TD
    A["General Equation: Ax² + Cy² + Dx + Ey + F = 0"] --> B{"Are both A and C present?"}
    B -->|"Yes, same sign"| C[Ellipse family]
    B -->|"Yes, opposite signs"| D[Hyperbola]
    B -->|"Only one present"| E[Parabola]
    C --> F{"A = C?"}
    F -->|"Yes"| G[Circle]
    F -->|"No"| H[Ellipse]
```

## Related Concepts
- [[Geometry - Circle]]
- [[Geometry - Parabola]]
- [[Geometry - Ellipse]]
- [[FAD1014 - Mathematics II]]