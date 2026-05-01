---
title: FAC1004 L19-L20 — Inverse Hyperbolic Functions
date: 2026-04-28
tags:
  - source/lecture
  - subject/mathematics
  - topic/hyperbolic-functions
  - topic/inverse-hyperbolic-functions
  - status/evergreen
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L19-L20 — Inverse Hyperbolic Functions

These lectures cover the definitions, domains, ranges, logarithmic forms, and derivatives of the six inverse hyperbolic functions. **L19** focuses on establishing the functions and their logarithmic representations; **L20** focuses on differentiation.

---

## L19 — Domain, Range, and Logarithmic Forms

### Learning Objective

To understand the domain, range, principal values, and conversion of hyperbolic functions to their inverse forms.

### Definitions

Inverse hyperbolic functions are established by reflecting the graphs of the hyperbolic functions (with appropriate restrictions) about the line $y = x$.

| Function | Definition | Restriction |
|----------|-----------|-------------|
| $\sinh^{-1} x$ | Inverse of $\sinh x$ | None (sinh is one-to-one) |
| $\cosh^{-1} x$ | Inverse of $\cosh x$ | $x \geq 0$ (restrict to principal branch) |
| $\tanh^{-1} x$ | Inverse of $\tanh x$ | None (tanh is one-to-one) |
| $\coth^{-1} x$ | Inverse of $\coth x$ | None (coth is one-to-one on each branch) |
| $\text{sech}^{-1} x$ | Inverse of $\text{sech } x$ | $x \geq 0$ (restrict to principal branch) |
| $\text{csch}^{-1} x$ | Inverse of $\text{csch } x$ | None (csch is one-to-one) |

> **Note**: For $\cosh^{-1} x$ and $\text{sech}^{-1} x$, restricting $x$ to be non-negative makes the function invertible by selecting the principal branch.

### Domain and Range

| Function | Domain | Range |
|----------|--------|-------|
| $\sinh^{-1} x$ | $(-\infty, \infty)$ | $(-\infty, \infty)$ |
| $\cosh^{-1} x$ | $(1, \infty)$ | $[0, \infty)$ |
| $\tanh^{-1} x$ | $(-1, 1)$ | $(-\infty, \infty)$ |
| $\coth^{-1} x$ | $(-\infty, -1) \cup (1, \infty)$ | $(-\infty, 0) \cup (0, \infty)$ |
| $\text{sech}^{-1} x$ | $(0, 1)$ | $[0, \infty)$ |
| $\text{csch}^{-1} x$ | $(-\infty, 0) \cup (0, \infty)$ | $(-\infty, 0) \cup (0, \infty)$ |

> **Lecture convention**: The domain of $\cosh^{-1} x$ is taken as $(1, \infty)$ (open at 1) and $\text{sech}^{-1} x$ as $(0, 1)$ (open at both ends).

### Logarithmic Forms

The inverse hyperbolic functions can be expressed in terms of natural logarithms.

#### Derivation of $\sinh^{-1} x$

Let $x = \sinh y = \frac{1}{2}(e^y - e^{-y})$.

$$x = \frac{1}{2}(e^y - e^{-y})$$
$$e^y - e^{-y} - 2x = 0$$
$$e^{2y} - 2xe^y - 1 = 0$$

Treating this as a quadratic in $e^y$:
$$e^y = \frac{2x \pm \sqrt{4x^2 + 4}}{2} = x \pm \sqrt{x^2 + 1}$$

Since $e^y > 0$ and $x - \sqrt{x^2+1} < 0$, we take the positive root:
$$e^y = x + \sqrt{x^2 + 1}$$

Therefore:
$$\boxed{\sinh^{-1} x = \ln(x + \sqrt{x^2 + 1})}$$

#### Summary of All Logarithmic Forms

$$\sinh^{-1} x = \ln(x + \sqrt{x^2 + 1})$$

$$\cosh^{-1} x = \ln(x + \sqrt{x^2 - 1})$$

$$\tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right)$$

$$\coth^{-1} x = \frac{1}{2}\ln\left(\frac{x+1}{x-1}\right)$$

$$\text{sech}^{-1} x = \ln\left(\frac{1 + \sqrt{1-x^2}}{x}\right)$$

$$\text{csch}^{-1} x = \ln\left(\frac{1}{x} + \frac{\sqrt{1+x^2}}{|x|}\right)$$

### Worked Examples (L19)

#### Example 1: Exact Value of $\sinh^{-1}(\pi/3)$

$$\sinh^{-1}\left(\frac{\pi}{3}\right) = \ln\left(\frac{\pi}{3} + \sqrt{\left(\frac{\pi}{3}\right)^2 + 1}\right)$$

---

## L20 — Derivatives of Inverse Hyperbolic Functions

### Learning Objective

To understand the derivatives of inverse hyperbolic functions, explore how they are derived, and apply these rules to solve a variety of differentiation problems.

### Derivation of $\frac{d}{dx}[\sinh^{-1} x]$

Using the logarithmic form:
$$\frac{d}{dx}[\sinh^{-1} x] = \frac{d}{dx}\left[\ln(x + \sqrt{x^2+1})\right]$$

$$= \frac{1}{x + \sqrt{x^2+1}} \cdot \left(1 + \frac{x}{\sqrt{x^2+1}}\right)$$

$$= \frac{1}{x + \sqrt{x^2+1}} \cdot \frac{\sqrt{x^2+1} + x}{\sqrt{x^2+1}}$$

$$= \frac{1}{\sqrt{x^2+1}}$$

### Complete Derivative Table

| $f(x)$ | $\frac{d}{dx}f(x)$ |
|--------|-------------------|
| $\sinh^{-1} x$ | $\dfrac{1}{\sqrt{1+x^2}}$ |
| $\cosh^{-1} x$ | $\dfrac{1}{\sqrt{x^2-1}}$ |
| $\tanh^{-1} x$ | $\dfrac{1}{1-x^2}$ |
| $\coth^{-1} x$ | $\dfrac{1}{1-x^2}$ |
| $\text{sech}^{-1} x$ | $\dfrac{-1}{x\sqrt{1-x^2}}$ |
| $\text{csch}^{-1} x$ | $\dfrac{-1}{|x|\sqrt{1+x^2}}$ |

### Domain Restrictions for Derivatives

- $\frac{d}{dx}\cosh^{-1} x = \frac{1}{\sqrt{x^2-1}}$ for $x > 1$
- $\frac{d}{dx}\tanh^{-1} x = \frac{1}{1-x^2}$ for $|x| < 1$
- $\frac{d}{dx}\coth^{-1} x = \frac{1}{1-x^2}$ for $|x| > 1$
- $\frac{d}{dx}\text{sech}^{-1} x = \frac{-1}{x\sqrt{1-x^2}}$ for $0 < x < 1$
- $\frac{d}{dx}\text{csch}^{-1} x = \frac{-1}{|x|\sqrt{1+x^2}}$ for $x \neq 0$

### Worked Examples (L20)

#### Example 2: Chain Rule with $\sinh^{-1}$

$$\frac{d}{dx}\left[\sinh^{-1}\left(\frac{x}{3}\right)\right] = \frac{\frac{1}{3}}{\sqrt{1 + \left(\frac{x}{3}\right)^2}} = \frac{1}{\sqrt{9+x^2}}$$

#### Example 3: Chain Rule with $\cosh^{-1}$

$$\frac{d}{dx}\left[\cosh^{-1}(\tan x)\right] = \frac{1}{\sqrt{\tan^2 x - 1}} \cdot \sec^2 x = \frac{\sec^2 x}{\sqrt{\tan^2 x - 1}}$$

#### Example 4: Logarithm of Inverse Hyperbolic Function

Using the chain rule directly:
$$\frac{d}{dx}\left[\ln(\tanh^{-1} x)\right] = \frac{1}{\tanh^{-1} x} \cdot \frac{1}{1-x^2} = \frac{1}{(1-x^2)\tanh^{-1} x}$$

Alternatively, substituting the logarithmic form of $\tanh^{-1} x$:
$$= \frac{1}{\frac{1}{2}\ln\left(\frac{1+x}{1-x}\right)} \cdot \frac{1}{1-x^2} = \frac{2}{\ln\left(\frac{1+x}{1-x}\right)(1-x^2)}$$

---

## Summary

These lectures establish the six inverse hyperbolic functions through graphical reflection, derive their logarithmic representations via algebraic manipulation of exponential definitions, and develop their derivatives using both the logarithmic forms and implicit differentiation. Key skills include:

1. Identifying domains and ranges from restricted hyperbolic graphs
2. Converting between inverse hyperbolic and logarithmic notation
3. Applying the chain rule to differentiate composite inverse hyperbolic functions

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Hyperbolic Functions]] — concept page
- [[FAC1004 L17 — Hyperbolic Functions]] — introduction lecture
- [[FAC1004 L18 — Hyperbolic Functions (Derivatives & Integrals)]] — derivatives lecture
- [[FAC1004 L21-L22 — Integrals Involving Hyperbolic Functions]] — next lecture
- [[FAC1004 Tutorial 9 — Inverse Hyperbolic Functions]] — practice problems

## Source File

`LECTURE_NOTES_2526/L19 L20 Inverse Hyperbolic Function 1 - full version.pdf`
