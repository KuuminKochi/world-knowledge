---
title: "Improper Integrals"
date: 2026-04-29
tags:
  - concept/mathematics
  - topic/integration
  - topic/improper-integrals
  - status/seedling
aliases:
  - Improper Integration
sources:
  - "[[FAD1014 L20 — Improper Integrals]]"
---

# Improper Integrals

An improper integral is a definite integral where either the interval of integration is unbounded, or the integrand has an infinite discontinuity within (or at the boundary of) the interval.

## Overview

A proper definite integral $\int_a^b f(x)\,dx$ requires two conditions:
1. The interval $[a, b]$ is **finite**.
2. The integrand $f(x)$ is **continuous** on $[a, b]$.

An **improper integral** arises when at least one of these conditions fails. Such integrals are evaluated by replacing the problematic point with a variable and taking a limit.

---

## Type 1: Infinite Limits of Integration

Occurs when one or both limits of integration are $\pm\infty$.

### Definition

If $\int_a^t f(x)\,dx$ exists for every $t \ge a$:

$$\int_a^\infty f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx$$

If $\int_t^b f(x)\,dx$ exists for every $t \le b$:

$$\int_{-\infty}^b f(x)\,dx = \lim_{t \to -\infty} \int_t^b f(x)\,dx$$

For both limits infinite (choose any $c \in \mathbb{R}$):

$$\int_{-\infty}^\infty f(x)\,dx = \int_{-\infty}^c f(x)\,dx + \int_c^\infty f(x)\,dx$$

The integral **converges** if the limit exists as a finite number; otherwise it **diverges**.

### Type 1 p-Test

For $a > 0$:

$$\int_a^\infty \frac{1}{x^p}\,dx \quad \text{converges} \iff p > 1$$

$$\int_a^\infty \frac{1}{x^p}\,dx \quad \text{diverges if} \quad p \le 1$$

### Key Examples (Type 1)

**Example — Convergent ($p = 2$):**
$$\int_1^\infty \frac{1}{x^2}\,dx = \lim_{t \to \infty} \left[-\frac{1}{x}\right]_1^t = 1$$

**Example — Divergent ($p = 1$):**
$$\int_1^\infty \frac{1}{x}\,dx = \lim_{t \to \infty} \bigl[\ln x\bigr]_1^t = \infty$$

**Example — Exponential Decay:**
$$\int_0^\infty e^{-x}\,dx = \lim_{t \to \infty} \bigl[-e^{-x}\bigr]_0^t = 1$$

---

## Type 2: Discontinuous Integrand

Occurs when $f(x)$ has a vertical asymptote (infinite discontinuity) at a point in the integration interval.

### Definition

**Discontinuity at $a$ (lower limit):**
$$\int_a^b f(x)\,dx = \lim_{t \to a^+} \int_t^b f(x)\,dx$$

**Discontinuity at $b$ (upper limit):**
$$\int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx$$

**Discontinuity at $c \in (a, b)$ (interior):**
$$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$$

The integral converges only if **both** one-sided improper integrals converge independently.

### Type 2 p-Test

For the integral $\int_0^1 \frac{1}{x^p}\,dx$:

$$\text{Converges} \iff p < 1$$

$$\text{Diverges if} \quad p \ge 1$$

### Key Examples (Type 2)

**Example — Convergent ($p = \frac{1}{2} < 1$):**
$$\int_0^1 \frac{1}{\sqrt{x}}\,dx = \lim_{t \to 0^+} \bigl[2\sqrt{x}\bigr]_t^1 = 2$$

**Example — Divergent ($p = 1$):**
$$\int_0^1 \frac{1}{x}\,dx = \lim_{t \to 0^+} \bigl[\ln x\bigr]_t^1 = \infty$$

**Example — Discontinuity in Interior:**
$$\int_{-1}^1 \frac{1}{x^2}\,dx = \int_{-1}^0 \frac{1}{x^2}\,dx + \int_0^1 \frac{1}{x^2}\,dx$$

Both one-sided integrals diverge (each behaves like $\lim_{t \to 0^+} [-\frac{1}{x}]_t^1 = \infty$), so the original integral **diverges**.

---

## The Comparison Test

Used when direct evaluation of an improper integral is difficult. The idea is to compare the integrand with a simpler function whose convergence is already known.

### Theorem Statement

> [!theorem] Comparison Test
> Let $f$ and $g$ be continuous on $[a, \infty)$ with $0 \le g(x) \le f(x)$ for all $x \ge a$.
>
> 1. If $\displaystyle\int_a^\infty f(x)\,dx$ **converges**, then $\displaystyle\int_a^\infty g(x)\,dx$ **converges**.
> 2. If $\displaystyle\int_a^\infty g(x)\,dx$ **diverges**, then $\displaystyle\int_a^\infty f(x)\,dx$ **diverges**.

### Logical Structure

| If... | and... | Then... |
|-------|--------|---------|
| $g(x) \le f(x)$ | $\int f$ converges | $\int g$ converges |
| $g(x) \le f(x)$ | $\int g$ diverges | $\int f$ diverges |

> [!warning] Important
> If $\int f$ diverges, the test gives **no information** about $\int g$.
> If $\int g$ converges, the test gives **no information** about $\int f$.

### Common Comparison Functions

| Function | Behavior at $\infty$ |
|----------|---------------------|
| $\displaystyle\frac{1}{x^p}$ | Converges iff $p > 1$ |
| $e^{-kx}$ ($k > 0$) | Always converges |
| $\displaystyle\frac{1}{x\ln x}$ | Diverges (compare with $1/x$) |

### Worked Example — Comparison Test

**Determine convergence of** $\displaystyle\int_1^\infty \frac{\sin^2 x}{x^2}\,dx$.

**Solution:**

For all $x \ge 1$, $0 \le \sin^2 x \le 1$, so:

$$0 \le \frac{\sin^2 x}{x^2} \le \frac{1}{x^2}$$

From the p-test, $\displaystyle\int_1^\infty \frac{1}{x^2}\,dx$ converges ($p = 2 > 1$). By the comparison test:

$$\int_1^\infty \frac{\sin^2 x}{x^2}\,dx \quad \text{converges}$$

---

## Summary Table

| Criterion | Type 1 $\int_1^\infty \frac{1}{x^p}\,dx$ | Type 2 $\int_0^1 \frac{1}{x^p}\,dx$ |
|-----------|------------------------------------------|-------------------------------------|
| Converges when | $p > 1$ | $p < 1$ |
| Diverges when | $p \le 1$ | $p \ge 1$ |
| Convergent example | $\frac{1}{x^2}$ | $\frac{1}{\sqrt{x}}$ |
| Divergent example | $\frac{1}{x}$ | $\frac{1}{x}$ |

---

## Strategy for Testing Improper Integrals

1. **Identify the type**: infinite limit (Type 1), discontinuity (Type 2), or both.
2. **Rewrite as a limit** of a proper integral.
3. **Evaluate** the proper integral, then **take the limit**.
4. If direct evaluation is impossible, apply the **comparison test** using a known function ($1/x^p$, $e^{-kx}$, etc.).
5. **Declare convergence or divergence** based on the limit result.

---

## Related

- [[FAD1014 L20 — Improper Integrals]] — source lecture
- [[Integration Techniques]] — prerequisite: definite integrals, FTC, limits
- [[FAD1014 - Mathematics II]] — course page
- [[Sequences]] — limits at infinity
- [[Series]] — convergence/divergence for infinite series (analogous concepts)
