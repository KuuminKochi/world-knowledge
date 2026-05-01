---
title: "FAD1014 Tutorial 10 — First-Order Linear DEs"
date: 2026-04-27
tags:
  - source/tutorial
  - subject/mathematics-ii
  - topic/differential-equations
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
---

# Tutorial 10: First-Order Linear Differential Equations

Tutorial problems covering first-order linear differential equations and integrating factor method.

## Sections

### Standard Form Linear DEs (Problems 1-4)
- Identifying linear first-order DEs
- Standard form: $\frac{dy}{dx} + P(x)y = Q(x)$
- Finding integrating factors

### Integrating Factor Method (Problems 5-8)
- Compute $\mu(x) = e^{\int P(x)\,dx}$
- Multiply through by integrating factor
- Solve resulting exact equation

### Applications (Problems 9-12)
- Circuit problems
- Mixing with variable rates
- Physics applications

## Integrating Factor Method

For $\frac{dy}{dx} + P(x)y = Q(x)$:

1. **Find integrating factor**: $\mu(x) = e^{\int P(x)\,dx}$
2. **Multiply equation**: $\mu(x)\frac{dy}{dx} + \mu(x)P(x)y = \mu(x)Q(x)$
3. **Left side becomes**: $\frac{d}{dx}[\mu(x)y] = \mu(x)Q(x)$
4. **Integrate**: $\mu(x)y = \int \mu(x)Q(x)\,dx$
5. **Solve for y**: $y = \frac{1}{\mu(x)}\int \mu(x)Q(x)\,dx$

## Links
- [[Differential Equations]] — concept page
- [[FAD1014 Tutorial 7 — Differential Equations]]
- [[FAD1014 - Mathematics II]] — course
