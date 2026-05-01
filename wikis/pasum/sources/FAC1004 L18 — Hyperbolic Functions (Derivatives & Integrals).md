---
title: FAC1004 L18 — Hyperbolic Functions (Derivatives & Integrals)
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics
  - topic/hyperbolic-functions
  - topic/derivatives
  - topic/integrals
  - status/seedling
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L18 — Hyperbolic Functions (Derivatives & Integrals)

## Learning Outcome

To find and apply derivatives and integrals of hyperbolic functions.

---

## Definitions (Recap)

The function $e^x$ can be expressed as the sum of an even function and an odd function:

$$e^x = \frac{e^x + e^{-x}}{2} + \frac{e^x - e^{-x}}{2}$$

- **Even function**: hyperbolic cosine of $x$
  $$\cosh x = \frac{e^x + e^{-x}}{2}$$

- **Odd function**: hyperbolic sine of $x$
  $$\sinh x = \frac{e^x - e^{-x}}{2}$$

---

## Derivatives of Hyperbolic Functions

Derivatives for hyperbolic functions can be obtained by expressing the function in terms of $e^x$ and $e^{-x}$.

### Derivation of $\frac{d}{dx}\sinh x$

$$\frac{d}{dx}[\sinh x] = \frac{d}{dx}\left[\frac{e^x - e^{-x}}{2}\right] = \frac{e^x + e^{-x}}{2} = \cosh x$$

### Derivation of $\frac{d}{dx}\cosh x$

$$\frac{d}{dx}[\cosh x] = \frac{d}{dx}\left[\frac{e^x + e^{-x}}{2}\right] = \frac{e^x - e^{-x}}{2} = \sinh x$$

### General Derivative Formulas (Chain Rule)

Let $u$ be a differentiable function of $x$:

| Function | Derivative |
|----------|------------|
| $\sinh u$ | $\cosh u \cdot \frac{du}{dx}$ |
| $\cosh u$ | $\sinh u \cdot \frac{du}{dx}$ |
| $\tanh u$ | $\text{sech}^2 u \cdot \frac{du}{dx}$ |
| $\coth u$ | $-\text{csch}^2 u \cdot \frac{du}{dx}$ |
| $\text{sech } u$ | $-\text{sech } u \tanh u \cdot \frac{du}{dx}$ |
| $\text{csch } u$ | $-\text{csch } u \coth u \cdot \frac{du}{dx}$ |

### Worked Examples

**Example 1**: Find $\frac{d}{dx}[\cosh(x^3)]$

$$\frac{d}{dx}[\cosh(x^3)] = \sinh(x^3) \cdot \frac{d}{dx}[x^3] = 3x^2 \sinh(x^3)$$

**Example 2**: Find $\frac{d}{dx}[\ln(\tanh x)]$

$$\frac{d}{dx}[\ln(\tanh x)] = \frac{1}{\tanh x} \cdot \frac{d}{dx}[\tanh x] = \frac{\text{sech}^2 x}{\tanh x}$$

---

## Integrals of Hyperbolic Functions

The following theorem provides a complete list of the generalized integration formulas for hyperbolic functions.

### Basic Integration Formulas

| Integral | Result |
|----------|--------|
| $\int \sinh u \, du$ | $\cosh u + C$ |
| $\int \cosh u \, du$ | $\sinh u + C$ |
| $\int \text{sech}^2 u \, du$ | $\tanh u + C$ |
| $\int \text{csch}^2 u \, du$ | $-\coth u + C$ |
| $\int \text{sech } u \tanh u \, du$ | $-\text{sech } u + C$ |
| $\int \text{csch } u \coth u \, du$ | $-\text{csch } u + C$ |

### Worked Examples

**Example 1**: Evaluate $\int \sinh^5 x \cosh x \, dx$

Let $u = \sinh x$, then $du = \cosh x \, dx$.

$$\int \sinh^5 x \cosh x \, dx = \int u^5 \, du = \frac{1}{6}u^6 + C = \frac{1}{6}\sinh^6 x + C$$

**Example 2**: Evaluate $\int \tanh x \, dx$

Rewrite $\tanh x = \frac{\sinh x}{\cosh x}$.

Let $u = \cosh x$, then $du = \sinh x \, dx$.

$$\int \tanh x \, dx = \int \frac{\sinh x}{\cosh x} \, dx = \int \frac{1}{u} \, du = \ln u + C = \ln(\cosh x) + C$$

---

## Summary

This lecture develops the calculus of hyperbolic functions. Key takeaways:

1. Derivatives of hyperbolic functions follow patterns similar to trigonometric functions but with sign differences (no alternating sign for $\cosh x$).
2. The chain rule applies to hyperbolic functions exactly as it does to trigonometric functions.
3. Integration formulas are the reverse of differentiation formulas.
4. Substitution techniques (u-substitution) are essential for evaluating hyperbolic integrals.

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Hyperbolic Functions]] — concept page
- [[FAC1004 L17 — Hyperbolic Functions]] — introduction lecture
- [[FAC1004 L19-L20 — Inverse Hyperbolic Functions]] — next lecture

## Source File

`LECTURE_NOTES_2526/L18 Hyperbolic Function full version.pdf`
