---
title: "Non-Homogeneous DE (Linearly Independent)"
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics-ii
  - topic/differential-equations
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
lecturer: "[[Dr Ahmad Syafadhli Bin Abu Bakar]]"
---

# Non-Homogeneous Differential Equation (Linearly Independent)

Lecture slides covering non-homogeneous first-order DEs where the linear terms are linearly independent.

## Key Points

- Non-homogeneous DE: $M(x,y)\,dx + N(x,y)\,dy = 0$ with:
  $$
  M(x,y) = a_1 x + b_1 y + c_1, \quad N(x,y) = a_2 x + b_2 y + c_2
  $$
- **Linearly independent** case: $a_1 b_2 - a_2 b_1 \neq 0$ (i.e. $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$)
- Solved by translating coordinates to eliminate constant terms: substitute $x = u + h$, $y = v + k$.

## Examples Covered

1. **Example 1**: $(y - x - 2)\,dx + (4y + x - 3)\,dy = 0$
2. **Example 2**: $(x + y)\,dx + (x - y + 2)\,dy = 0$ — solution is $y - 1 - 2(x+1)(y-1) - (x+1)^2 = A$
3. **Example 3**: $(2x - 5y + 3)\,dx - (2x + 4y - 6)\,dy = 0$ with $y(1) = 2$
4. **Example 4**: $(7y - 3)\,dx + (2x + 1)\,dy = 0$ with $y(1) = 2$

## Links

- [[Differential Equations]] — concept page
- [[FAD1014 - Mathematics II]] — course