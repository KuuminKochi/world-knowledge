---
title: "Non-Homogeneous DE (Linearly Dependent)"
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics-ii
  - topic/differential-equations
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
lecturer: "[[Dr Ahmad Syafadhli Bin Abu Bakar]]"
---

# Non-Homogeneous Differential Equation (Linearly Dependent)

Lecture slides covering non-homogeneous first-order DEs where the linear terms are linearly dependent.

## Key Points

- Non-homogeneous DE: $M(x,y)\,dx + N(x,y)\,dy = 0$ with:
  $$
  M(x,y) = a_1 x + b_1 y + c_1, \quad N(x,y) = a_2 x + b_2 y + c_2
  $$
- **Linearly dependent** case: $a_1 b_2 - a_2 b_1 = 0$ (i.e. $\frac{a_1}{a_2} = \frac{b_1}{b_2}$)
- Solved by substituting $u = a_1 x + b_1 y$ to reduce to a separable equation.

## Examples Covered

1. **Example 1**: $(x + y)\,dx + (3x + 3y - 4)\,dy = 0$
2. **Example 2**: $(x + y - 2)\,dx + (x + y + 2)\,dy = 0$ — simplifies to $(x + y + 2)^2\,dx = 8x + A$
3. **Example 3**: $(x - 2y + 3)\,dx - (4y - 2x + 1)\,dy = 0$ with $x = 0, y = 1$
4. **Example 4**: $(x + y)\,dx + (x + y + 1)\,dy = 0$ with $y(2) = 1$

## Links

- [[Differential Equations]] — concept page
- [[FAD1014 - Mathematics II]] — course