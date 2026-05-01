---
title: FAC1004 L21-L22 — Integrals Involving Hyperbolic Functions
date: 2026-04-28
tags:
  - source/lecture
  - subject/mathematics
  - topic/hyperbolic-functions
  - topic/inverse-hyperbolic-functions
  - topic/integrals
  - status/evergreen
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L21-L22 — Integrals Involving Hyperbolic Functions

These lectures cover integration techniques for hyperbolic functions and integrals that lead to inverse hyperbolic functions. L21 focuses on basic hyperbolic integrals and $u$-substitution, while L22 covers standard forms producing inverse hyperbolic results and compares trigonometric versus hyperbolic substitution methods.

## Learning Outcomes

- **L21**: Understand how to integrate hyperbolic functions, apply standard integration formulas, and use basic identities and substitution techniques to solve foundational calculus problems.
- **L22**: Understand how to integrate expressions that lead to inverse hyperbolic functions, using substitution and standard forms to obtain results in calculus problems.

---

## L21 — Integrals of Hyperbolic Functions

### Standard Integration Formulas (Theorem)

$$
\begin{aligned}
\int \sinh u \, du &= \cosh u + C \\
\int \cosh u \, du &= \sinh u + C \\
\int \operatorname{sech}^2 u \, du &= \tanh u + C \\
\int \operatorname{csch}^2 u \, du &= -\coth u + C \\
\int \operatorname{sech} u \tanh u \, du &= -\operatorname{sech} u + C \\
\int \operatorname{csch} u \coth u \, du &= -\operatorname{csch} u + C
\end{aligned}
$$

### Worked Examples

**Example 1** — Power rule with $u$-substitution

$$\int \sinh^5 x \cosh x \, dx$$

Let $u = \sinh x$, then $du = \cosh x \, dx$:

$$
\int u^5 \, du = \frac{1}{6}u^6 + C = \frac{1}{6}\sinh^6 x + C
$$

**Example 2** — Integral of $\tanh x$

$$\int \tanh x \, dx = \int \frac{\sinh x}{\cosh x}\, dx$$

Let $u = \cosh x$, then $du = \sinh x \, dx$:

$$
\int \frac{du}{u} = \ln u + C = \ln(\cosh x) + C
$$

**Example 3** — Radical with $u$-substitution

$$\int \sqrt{\tanh x} \, \operatorname{sech}^2 x \, dx$$

Let $u = \tanh x$, then $du = \operatorname{sech}^2 x \, dx$:

$$
\int \sqrt{u}\, du = \frac{u^{3/2}}{3/2} + C = \frac{2}{3}\tanh^{3/2} x + C
$$

**Example 4** — Negative coefficient from derivative

$$\int \coth^2 x \, \operatorname{csch}^2 x \, dx$$

Let $u = \coth x$, then $du = -\operatorname{csch}^2 x \, dx$:

$$
\int -u^2 \, du = -\frac{u^3}{3} + C = -\frac{1}{3}\coth^3 x + C
$$

---

## L22 — Integrals Involving Inverse Hyperbolic Functions

### Motivation: Two Routes to the Same Result

The integral $\displaystyle\int \frac{dx}{\sqrt{a^2 + x^2}}$ can be evaluated by **trigonometric substitution** or **hyperbolic substitution**.

**Route A — Trigonometric substitution**

Let $x = a\tan\theta$, so $dx = a\sec^2\theta \, d\theta$ and $a^2 + x^2 = a^2\sec^2\theta$.

$$
\int \frac{a\sec^2\theta \, d\theta}{a\sec\theta} = \int \sec\theta \, d\theta = \ln\bigl|\tan\theta + \sec\theta\bigr| + C
$$

Substituting back:

$$
= \ln\left|\frac{x}{a} + \frac{\sqrt{a^2+x^2}}{a}\right| + C = \ln\bigl|x + \sqrt{a^2+x^2}\bigr| + D
$$

where $D = C - \ln|a|$ absorbs the constant.

**Route B — Hyperbolic substitution**

Let $x = a\sinh u$, so $dx = a\cosh u \, du$ and $a^2 + x^2 = a^2\cosh^2 u$.

$$
\int \frac{a\cosh u \, du}{a\cosh u} = \int du = u + C = \sinh^{-1}\!\left(\frac{x}{a}\right) + C
$$

Both routes agree because:

$$
\int \frac{dx}{\sqrt{a^2 + x^2}} = \ln\bigl|x + \sqrt{a^2+x^2}\bigr| + D = \sinh^{-1}\!\left(\frac{x}{a}\right) + C
$$

### Generalized Integration Theorem (Inverse Hyperbolic Forms)

$$
\begin{aligned}
\int \frac{du}{\sqrt{a^2 + u^2}} &= \sinh^{-1}\!\left(\frac{u}{a}\right) + C \\
\int \frac{du}{\sqrt{u^2 - a^2}} &= \cosh^{-1}\!\left(\frac{u}{a}\right) + C \\
\int \frac{du}{a^2 - u^2} &=
\begin{cases}
\displaystyle\frac{1}{a}\tanh^{-1}\!\left(\frac{u}{a}\right) + C, & |u| < a \\
\displaystyle\frac{1}{a}\coth^{-1}\!\left(\frac{u}{a}\right) + C, & |u| > a
\end{cases} \\
\int \frac{du}{u\sqrt{a^2 + u^2}} &= -\frac{1}{a}\operatorname{csch}^{-1}\!\left(\frac{u}{a}\right) + C \\
\int \frac{du}{u\sqrt{a^2 - u^2}} &= -\frac{1}{a}\operatorname{sech}^{-1}\!\left(\frac{u}{a}\right) + C
\end{aligned}
$$

### Worked Examples

**Example 1** — Form $\displaystyle\int \frac{dx}{\sqrt{a^2+u^2}}$

$$\int \frac{dx}{\sqrt{1 + 9x^2}}$$

Let $u = 3x$, so $du = 3\,dx$ and $dx = \frac{du}{3}$. Then $a = 1$:

$$
\int \frac{du}{3\sqrt{1^2 + u^2}} = \frac{1}{3}\sinh^{-1}\!\left(\frac{u}{1}\right) + C = \frac{1}{3}\sinh^{-1}(3x) + C
$$

**Example 2** — Form $\displaystyle\int \frac{dx}{x\sqrt{a^2+u^2}}$

$$\int \frac{dx}{x\sqrt{9 + 4x^2}}$$

Let $u = 2x$, so $x = \frac{u}{2}$ and $dx = \frac{du}{2}$. Then $a = 3$:

$$
\int \frac{\frac{du}{2}}{\frac{u}{2}\sqrt{3^2 + u^2}} = \int \frac{du}{u\sqrt{3^2 + u^2}} = -\frac{1}{3}\operatorname{csch}^{-1}\!\left(\frac{u}{3}\right) + C = -\frac{1}{3}\operatorname{csch}^{-1}\!\left(\frac{2x}{3}\right) + C
$$

---

## Summary

| Technique | When to Use |
|-----------|-------------|
| Direct hyperbolic integral | Integrand matches standard form exactly |
| $u$-substitution | One hyperbolic factor is the derivative of another |
| Hyperbolic substitution | Radical forms $\sqrt{a^2+x^2}$ or $\sqrt{x^2-a^2}$ |
| Standard inverse forms | After $u$-substitution reduces to $\frac{1}{\sqrt{a^2\pm u^2}}$, $\frac{1}{a^2-u^2}$, etc. |

The piecewise result for $\displaystyle\int \frac{du}{a^2-u^2}$ is essential: use $\tanh^{-1}$ when $|u|<a$ and $\coth^{-1}$ when $|u|>a$.

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Hyperbolic Functions]] — concept page
- [[FAC1004 L19-L20 — Inverse Hyperbolic Functions]] — previous lecture

## Source File

`LECTURE_NOTES_2526/L21 L22 Inverse Hyperbolic function 2 - full version.pdf`
