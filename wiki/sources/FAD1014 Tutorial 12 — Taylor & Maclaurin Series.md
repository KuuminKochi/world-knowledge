---
title: "FAD1014 Tutorial 12 — Taylor & Maclaurin Series"
date: 2026-04-27
tags:
  - source/tutorial
  - subject/mathematics-ii
  - topic/power-series
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
---

# Tutorial 12: Taylor & Maclaurin Series

Tutorial problems covering power series expansions and approximations.

## Sections

### Maclaurin Series (Problems 1-4)
- Finding Maclaurin series from definition
- Using known series
- Radius of convergence

### Taylor Series (Problems 5-8)
- Series about specific points
- Taylor polynomials
- Remainder estimation

### Applications (Problems 9-12)
- Function approximation
- Numerical calculations
- Limit evaluation using series

## Standard Maclaurin Series

| Function | Series |
|----------|--------|
| $e^x$ | $\sum_{n=0}^{\infty} \frac{x^n}{n!}$ |
| $\sin x$ | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!}$ |
| $\cos x$ | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$ |
| $\ln(1+x)$ | $\sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n}$ |
| $(1+x)^n$ | $\sum_{r=0}^{\infty} \binom{n}{r} x^r$ |

## Taylor Series Formula

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

## Applications

- Approximating function values
- Evaluating limits
- Integration of non-elementary functions
- Solving differential equations

## Links
- [[FAD1014 L25-L26 — Power Series, Taylor & Maclaurin]]
- [[Power Series — Taylor & Maclaurin]] — concept page
- [[FAD1014 - Mathematics II]] — course
