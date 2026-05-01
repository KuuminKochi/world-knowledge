---
title: "FAD1014 L20 — Improper Integrals"
date: 2026-04-29
tags:
  - source/lecture
  - subject/mathematics
  - topic/integration
  - topic/improper-integrals
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
---

# FAD1014 L20 — Improper Integrals

Lecture covering improper integrals: types, convergence/divergence criteria, the comparison test, and worked examples.

## Summary

This lecture extends the definite integral to cases where either (1) the interval of integration is infinite, or (2) the integrand has a vertical asymptote (infinite discontinuity) within or at the boundary of the integration interval. Both situations produce an **improper integral**, which is evaluated as a limit of proper integrals. The lecture introduces the **p-test** for both types, the **comparison test** for determining convergence/divergence, and multiple worked examples.

---

## Key Concepts

### 1. Type 1: Infinite Limits of Integration

An integral is **improper of Type 1** when at least one limit of integration is infinite.

#### Definition (Infinite Upper Limit)

If $\int_a^t f(x)\,dx$ exists for every $t \ge a$, then:

$$\int_a^\infty f(x)\,dx = \lim_{t \to \infty} \int_a^t f(x)\,dx$$

provided this limit exists (as a finite number).

#### Definition (Infinite Lower Limit)

If $\int_t^b f(x)\,dx$ exists for every $t \le b$, then:

$$\int_{-\infty}^b f(x)\,dx = \lim_{t \to -\infty} \int_t^b f(x)\,dx$$

#### Definition (Both Limits Infinite)

$$\int_{-\infty}^\infty f(x)\,dx = \int_{-\infty}^c f(x)\,dx + \int_c^\infty f(x)\,dx$$

where $c$ is any real number. The integral converges only if **both** integrals on the right converge independently.

> [!important] Convergence Terminology
> If the limit exists (is finite), the improper integral **converges**. If the limit does not exist or is infinite, the improper integral **diverges**.

### 2. Type 2: Discontinuous Integrand

An integral is **improper of Type 2** when the integrand $f(x)$ has an infinite discontinuity (vertical asymptote) at a point within or at the boundary of $[a, b]$.

#### Definition (Discontinuity at Lower Limit)

If $f$ is continuous on $(a, b]$ and discontinuous at $a$:

$$\int_a^b f(x)\,dx = \lim_{t \to a^+} \int_t^b f(x)\,dx$$

#### Definition (Discontinuity at Upper Limit)

If $f$ is continuous on $[a, b)$ and discontinuous at $b$:

$$\int_a^b f(x)\,dx = \lim_{t \to b^-} \int_a^t f(x)\,dx$$

#### Definition (Discontinuity in the Interior)

If $f$ has a discontinuity at $c \in (a, b)$:

$$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$$

The integral converges only if **both** improper integrals on the right converge independently.

### 3. The p-Test

#### Type 1 (p-Test for Infinite Limits)

$$\int_1^\infty \frac{1}{x^p}\,dx \quad \text{is} \quad \begin{cases} \displaystyle\text{convergent,} & p > 1 \\[8pt] \displaystyle\text{divergent,} & p \le 1 \end{cases}$$

#### Type 2 (p-Test for Discontinuity at Zero)

$$\int_0^1 \frac{1}{x^p}\,dx \quad \text{is} \quad \begin{cases} \displaystyle\text{convergent,} & p < 1 \\[8pt] \displaystyle\text{divergent,} & p \ge 1 \end{cases}$$

> [!note] Notice the Reversal
> The conditions for convergence are reversed between the two types. For Type 1, the integral converges only when $p$ is *large enough* ($p > 1$). For Type 2, it converges only when $p$ is *small enough* ($p < 1$).

---

## Worked Examples

### Example 1 (Type 1 — Convergent)

**Evaluate** $\displaystyle \int_1^\infty \frac{1}{x^2}\,dx$.

**Solution:**

The integral is improper because the upper limit is infinite.

$$\int_1^\infty \frac{1}{x^2}\,dx = \lim_{t \to \infty} \int_1^t \frac{1}{x^2}\,dx = \lim_{t \to \infty} \left[ -\frac{1}{x} \right]_1^t = \lim_{t \to \infty} \left( -\frac{1}{t} + 1 \right) = 0 + 1 = 1$$

Since the limit exists and equals $1$, the integral **converges to 1**.

> Geometrically: the region under $y = 1/x^2$ from $x = 1$ to $\infty$ has finite area, exactly $1$.

---

### Example 2 (Type 1 — Divergent)

**Evaluate** $\displaystyle \int_1^\infty \frac{1}{x}\,dx$.

**Solution:**

$$\int_1^\infty \frac{1}{x}\,dx = \lim_{t \to \infty} \int_1^t \frac{1}{x}\,dx = \lim_{t \to \infty} \bigl[ \ln|x| \bigr]_1^t = \lim_{t \to \infty} (\ln t - 0) = \infty$$

The limit does not exist (tends to infinity), so the integral **diverges**.

> This is the $p = 1$ case of the p-test. Contrast with Example 1 ($p = 2$), which converged. The borderline $p = 1$ diverges for Type 1.

---

### Example 3 (Type 2 — Convergent)

**Evaluate** $\displaystyle \int_0^1 \frac{1}{\sqrt{x}}\,dx$.

**Solution:**

The integrand $1/\sqrt{x}$ is discontinuous at $x = 0$ (vertical asymptote). This is a Type 2 improper integral.

$$\int_0^1 \frac{1}{\sqrt{x}}\,dx = \lim_{t \to 0^+} \int_t^1 x^{-1/2}\,dx = \lim_{t \to 0^+} \bigl[ 2x^{1/2} \bigr]_t^1 = \lim_{t \to 0^+} (2 - 2\sqrt{t}) = 2$$

The limit exists, so the integral **converges to 2**.

---

### Example 4 (Type 2 — Divergent)

**Evaluate** $\displaystyle \int_0^1 \frac{1}{x}\,dx$.

**Solution:**

The integrand $1/x$ is discontinuous at $x = 0$.

$$\int_0^1 \frac{1}{x}\,dx = \lim_{t \to 0^+} \int_t^1 \frac{1}{x}\,dx = \lim_{t \to 0^+} \bigl[ \ln|x| \bigr]_t^1 = \lim_{t \to 0^+} (0 - \ln t) = -(-\infty) = \infty$$

The integral **diverges**.

---

### Example 5 (Comparison Test for Convergence)

**Determine the convergence of** $\displaystyle \int_1^\infty \frac{1}{x^2 + 1}\,dx$.

**Solution (using comparison):**

For $x \ge 1$, we have $x^2 + 1 \ge x^2$, so:

$$\frac{1}{x^2 + 1} \le \frac{1}{x^2}$$

From Example 1, $\displaystyle \int_1^\infty \frac{1}{x^2}\,dx$ converges. By the comparison test, since $0 \le \frac{1}{x^2 + 1} \le \frac{1}{x^2}$ for all $x \ge 1$ and the larger integral converges:

$$\int_1^\infty \frac{1}{x^2 + 1}\,dx \quad \text{converges}$$

**Solution (direct evaluation):**

$$\int_1^\infty \frac{1}{x^2 + 1}\,dx = \lim_{t \to \infty} \int_1^t \frac{1}{x^2 + 1}\,dx = \lim_{t \to \infty} \bigl[ \tan^{-1} x \bigr]_1^t = \lim_{t \to \infty} (\tan^{-1} t - \tan^{-1} 1) = \frac{\pi}{2} - \frac{\pi}{4} = \frac{\pi}{4}$$

The direct evaluation confirms convergence; the integral converges to $\pi/4$.

---

### Example 6 (Comparison Test for Divergence)

**Determine the convergence of** $\displaystyle \int_1^\infty \frac{1}{\sqrt{x} + 1}\,dx$.

**Solution:**

For $x \ge 1$, $\sqrt{x} \ge 1$, so $\sqrt{x} + 1 \le \sqrt{x} + \sqrt{x} = 2\sqrt{x}$. Therefore:

$$\frac{1}{\sqrt{x} + 1} \ge \frac{1}{2\sqrt{x}}$$

Now, $\displaystyle \int_1^\infty \frac{1}{2\sqrt{x}}\,dx = \frac{1}{2}\int_1^\infty \frac{1}{x^{1/2}}\,dx$ has $p = \frac{1}{2} \le 1$, so it **diverges** (by the p-test).

Since $\frac{1}{\sqrt{x} + 1} \ge \frac{1}{2\sqrt{x}} > 0$ and the smaller integral diverges, by the comparison test:

$$\int_1^\infty \frac{1}{\sqrt{x} + 1}\,dx \quad \text{diverges}$$

---

## The Comparison Test (Formal Statement)

> [!theorem] Comparison Test for Improper Integrals
> Suppose $f$ and $g$ are continuous functions with $0 \le g(x) \le f(x)$ for all $x \ge a$.
>
> 1. If $\displaystyle\int_a^\infty f(x)\,dx$ **converges**, then $\displaystyle\int_a^\infty g(x)\,dx$ also **converges**.
> 2. If $\displaystyle\int_a^\infty g(x)\,dx$ **diverges**, then $\displaystyle\int_a^\infty f(x)\,dx$ also **diverges**.

> [!tip] Memory Aid
> - A smaller positive function under a convergent integral must also converge.
> - A larger positive function over a divergent integral must also diverge.

---

## Key Equations

| Type | Form | Convergence Condition |
|------|------|----------------------|
| Type 1 | $\displaystyle\int_1^\infty \frac{1}{x^p}\,dx$ | Converges iff $p > 1$ |
| Type 2 | $\displaystyle\int_0^1 \frac{1}{x^p}\,dx$ | Converges iff $p < 1$ |
| Type 1 | $\displaystyle\int_a^\infty e^{-kx}\,dx$ ($k > 0$) | Always converges to $\dfrac{e^{-ka}}{k}$ |
| Type 1 | $\displaystyle\int_1^\infty \frac{\ln x}{x^p}\,dx$ | Converges iff $p > 1$ |

---

## Links

- [[Improper Integrals]] — concept page with full theory and additional examples
- [[Integration Techniques]] — prerequisite: evaluating proper definite integrals
- [[Sequences]] — related: limits at infinity
- [[Series]] — related: convergence/divergence for infinite series
- [[FAD1014 - Mathematics II]] — course page
