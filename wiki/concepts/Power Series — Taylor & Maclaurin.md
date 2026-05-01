---
title: "Power Series — Taylor & Maclaurin"
date: 2026-04-27
tags:
  - concept/mathematics
  - topic/power-series
  - status/seedling
---

# Power Series — Taylor & Maclaurin

Representation of functions as infinite series and their applications.

## Overview

A power series is an infinite series of the form $\sum_{n=0}^{\infty} c_n (x-a)^n$. Taylor and Maclaurin series allow us to represent smooth functions as power series, approximating them near a specific point using the function's derivatives.

## Power Series

**General Form**:
$$\sum_{n=0}^{\infty} c_n (x-a)^n = c_0 + c_1(x-a) + c_2(x-a)^2 + \cdots$$

where $x$ is a variable, $c_n$ are coefficients, and $a$ is the center.

**Radius of Convergence**: The distance $R$ from the center $a$ within which the series converges. The series represents, approximates and defines functions converging within this radius.

## Taylor Series

A Taylor series is an infinite series that represents a smooth function as a polynomial, approximating it near a specific point using the function's derivatives.

The Taylor series of $f(x)$ about center $x = a$:
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

$$= f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$

**Conditions**: $f$ must be infinitely differentiable at $a$.

## Maclaurin Series

A Maclaurin series is a special case of the Taylor series in the region near $x = 0$. It provides polynomial approximations of functions like $\sin x$, $e^x$ and $\ln(1+x)$ using their derivatives at $x = 0$. Also called **"Taylor at zero"**.

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$$

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$$

## Constructing Series from Standard Forms

By applying algebra to standard Maclaurin or Taylor series, we can derive series for related functions:
- **Substitution**: replace $x$ with $x^2$, $-3x^2$, etc. (e.g. $e^{-3x^2}$)
- **Multiplication**: multiply two known series (e.g. $x^4 e^{-3x^2}$ or $(\sin 3x^2)e^{2x}$)
- **Term-by-term integration**: integrate a known series to approximate integrals like $\int \frac{\sin x}{x}\,dx$

## Common Maclaurin Series

| Function    | Series                                                                                               | Valid For          |
| ----------- | ---------------------------------------------------------------------------------------------------- | ------------------ |
| $e^x$       | $\sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$              | all $x$            |
| $\sin x$    | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ | all $x$            |
| $\cos x$    | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$     | all $x$            |
| $\ln(1+x)$  | $\sum_{n=1}^{\infty} \frac{(-1)^{n+1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$          | $-1 < x \leq 1$    |
| $\arctan x$ | $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{2n+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots$      | $-1 \leq x \leq 1$ |
| $(1+x)^n$   | $\sum_{r=0}^{\infty} \binom{n}{r} x^r$                                                               | $|x| < 1$          |

## Applications

### Function Approximation
- Taylor polynomials approximate functions near a point; the center $a$ is the anchor point of highest accuracy
- More terms give better approximations

### Numerical Calculations
- Computing $e$, $\pi$, logarithms, trigonometric values
- Error estimation using remainder term

### Calculus Operations
- Differentiating and integrating power series term by term
- Solving differential equations
- Evaluating limits

### Error Estimation
**Taylor's Remainder Theorem**:
$$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}$$
for some $c$ between $a$ and $x$.

## PASUM Course Links

- [[FAD1014 L25-L26 — Power Series, Taylor & Maclaurin]]
- [[FAD1014 Tutorial 12 — Taylor & Maclaurin Series]]
- [[Binomial Expansion]] — related concept
- [[FAD1014 - Mathematics II]] — course
