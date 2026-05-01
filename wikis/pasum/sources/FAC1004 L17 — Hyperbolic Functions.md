---
title: FAC1004 L17 — Hyperbolic Functions
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics
  - topic/hyperbolic-functions
  - status/evergreen
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L17 — Hyperbolic Functions

## Learning Outcomes

1. To understand hyperbolic functions.
2. To understand basic hyperbolic identities.

---

## Motivation: From Trigonometry to Hyperbolics

```mermaid
graph LR
    subgraph trig["Trigonometric"]
        T1["Unit Circle<br/>x^2 + y^2 = 1"]
        T2["x = cos t"]
        T3["y = sin t"]
    end
    subgraph hyp["Hyperbolic"]
        H1["Hyperbola<br/>x^2 - y^2 = 1"]
        H2["x = cosh t"]
        H3["y = sinh t"]
    end

    T1 --> T2
    T1 --> T3
    H1 --> H2
    H1 --> H3

    style trig fill:#e7f5ff,stroke:#1971c2
    style hyp fill:#ffe8cc,stroke:#d9480f
```

In trigonometry, for any angle $t$, the intersection of the terminal side and the unit circle has coordinates:
- $x = \cos t$
- $y = \sin t$

Hyperbolic functions are analogs defined using the **hyperbola** instead of the unit circle. They arise as combinations of the exponential functions $e^x$ and $e^{-x}$.

---

## Even and Odd Decomposition of $e^x$

Any function $f(x)$ can be expressed as the sum of an **even function** and an **odd function**:

$$f(x) = \underbrace{\frac{f(x) + f(-x)}{2}}_{\text{even}} + \underbrace{\frac{f(x) - f(-x)}{2}}_{\text{odd}}$$

Applying this to $f(x) = e^x$:

$$e^x = \underbrace{\frac{e^x + e^{-x}}{2}}_{\text{hyperbolic cosine}} + \underbrace{\frac{e^x - e^{-x}}{2}}_{\text{hyperbolic sine}}$$

This decomposition is the foundation of all hyperbolic functions.

---

## Definitions

```mermaid
graph TD
    EXP["e^x"] --> EVEN["Even Part<br/>(e^x + e^-x) / 2<br/>= cosh x"]
    EXP --> ODD["Odd Part<br/>(e^x - e^-x) / 2<br/>= sinh x"]
    EVEN --> TANH["tanh x = sinh x / cosh x"]
    ODD --> TANH
    EVEN --> SECH["sech x = 1 / cosh x"]
    ODD --> CSCH["csch x = 1 / sinh x"]
    TANH --> COTH["coth x = 1 / tanh x"]

    style EXP fill:#e7f5ff,stroke:#1971c2
    style EVEN fill:#ffe8cc,stroke:#d9480f
    style ODD fill:#e5dbff,stroke:#5f3dc4
    style TANH fill:#d3f9d8,stroke:#2f9e44
    style SECH fill:#c5f6fa,stroke:#0c8599
    style CSCH fill:#c5f6fa,stroke:#0c8599
    style COTH fill:#c5f6fa,stroke:#0c8599
```

### Hyperbolic Sine ($\sinh x$)

$$\sinh x = \frac{e^x - e^{-x}}{2} = \frac{1}{2}e^x - \frac{1}{2}e^{-x}$$

- **Domain:** $(-\infty, \infty)$
- **Range:** $(-\infty, \infty)$
- **Parity:** Odd function ($\sinh(-x) = -\sinh x$)
- **Graph:** Passes through the origin, increasing monotonically. Can be visualized as the difference of $y = \frac{1}{2}e^x$ and $y = \frac{1}{2}e^{-x}$.

### Hyperbolic Cosine ($\cosh x$)

$$\cosh x = \frac{e^x + e^{-x}}{2} = \frac{1}{2}e^x + \frac{1}{2}e^{-x}$$

- **Domain:** $(-\infty, \infty)$
- **Range:** $[1, \infty)$
- **Parity:** Even function ($\cosh(-x) = \cosh x$)
- **Graph:** U-shaped curve with minimum at $(0, 1)$. Can be visualized as the sum of $y = \frac{1}{2}e^x$ and $y = \frac{1}{2}e^{-x}$.

### Hyperbolic Tangent ($\tanh x$)

$$\tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

- **Domain:** $(-\infty, \infty)$
- **Range:** $(-1, 1)$
- **Parity:** Odd function
- **Horizontal Asymptotes:** $y = -1$ and $y = 1$
- **Graph:** S-shaped curve passing through the origin, bounded between the asymptotes.

### Reciprocal Hyperbolic Functions

By analogy with trigonometric functions:

| Function | Definition | Exponential Form |
|---|---|---|
| Hyperbolic cosecant | $\operatorname{cosech} x = \dfrac{1}{\sinh x}$ | $\dfrac{2}{e^x - e^{-x}}$ |
| Hyperbolic secant | $\operatorname{sech} x = \dfrac{1}{\cosh x}$ | $\dfrac{2}{e^x + e^{-x}}$ |
| Hyperbolic cotangent | $\coth x = \dfrac{1}{\tanh x}$ | $\dfrac{e^x + e^{-x}}{e^x - e^{-x}}$ |

> **Note:** $\operatorname{cosech} x$ is also commonly written as $\operatorname{csch} x$.

---

## Fundamental Hyperbolic Identities

```mermaid
graph TD
    FUND["cosh^2 x - sinh^2 x = 1"] --> DIV1["Divide by cosh^2 x"]
    FUND --> DIV2["Divide by sinh^2 x"]
    DIV1 --> ID1["1 - tanh^2 x = sech^2 x"]
    DIV2 --> ID2["coth^2 x - 1 = csch^2 x"]
    FUND --> ADD["Addition Formulas"]
    ADD --> A1["sinh(x +/- y) =<br/>sinh x cosh y +/- cosh x sinh y"]
    ADD --> A2["cosh(x +/- y) =<br/>cosh x cosh y +/- sinh x sinh y"]
    ADD --> A3["tanh(x +/- y) =<br/>(tanh x +/- tanh y) /<br/>(1 +/- tanh x tanh y)"]

    style FUND fill:#fff4e6,stroke:#e67700
    style ID1 fill:#d3f9d8,stroke:#2f9e44
    style ID2 fill:#d3f9d8,stroke:#2f9e44
    style A1 fill:#e7f5ff,stroke:#1971c2
    style A2 fill:#e7f5ff,stroke:#1971c2
    style A3 fill:#e7f5ff,stroke:#1971c2
```

### Pythagorean-Type Identities

$$\cosh^2 x - \sinh^2 x = 1$$

Dividing by $\cosh^2 x$ and $\sinh^2 x$ respectively:

$$1 - \tanh^2 x = \operatorname{sech}^2 x$$
$$\coth^2 x - 1 = \operatorname{cosech}^2 x$$

### Addition Formulas

$$\sinh(x \pm y) = \sinh x \cosh y \pm \cosh x \sinh y$$
$$\cosh(x \pm y) = \cosh x \cosh y \pm \sinh x \sinh y$$
$$\tanh(x \pm y) = \frac{\tanh x \pm \tanh y}{1 \pm \tanh x \tanh y}$$

### Double Angle Formulas

$$\sinh 2x = 2\sinh x \cosh x$$
$$\cosh 2x = \cosh^2 x + \sinh^2 x$$

### Half-Angle (Power-Reduction) Formulas

From $\cosh 2x = 2\cosh^2 x - 1$ and $\cosh 2x = 2\sinh^2 x + 1$:

$$\cosh^2 x = \frac{\cosh 2x + 1}{2}$$
$$\sinh^2 x = \frac{\cosh 2x - 1}{2}$$

---

## Summary

This lecture introduces hyperbolic functions as combinations of exponential functions. The key takeaways are:

- Hyperbolic functions are built from $e^x$ and $e^{-x}$ via even/odd decomposition.
- $\sinh x$ is odd and unbounded; $\cosh x$ is even with minimum value 1; $\tanh x$ is bounded between $-1$ and $1$.
- The fundamental identity $\cosh^2 x - \sinh^2 x = 1$ mirrors the trigonometric identity $\cos^2 x + \sin^2 x = 1$, but with a crucial sign difference.
- Basic identities (addition, double-angle, Pythagorean-type) are essential tools for manipulating hyperbolic expressions.

---

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Hyperbolic Functions]] — concept page
- [[FAC1004 L15-L16 — Derivatives of Inverse Trig Functions]] — previous lecture
- [[FAC1004 L18 — Hyperbolic Functions (Derivatives & Integrals)]] — next lecture

## Source File

`LECTURE_NOTES_2526/L17 Hyperbolic Function - full.pdf`
