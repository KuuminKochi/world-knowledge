---
title: FAC1004 L15-L16 — Derivatives of Inverse Trig Functions
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics
  - topic/inverse-trigonometric-functions
  - topic/derivatives
  - status/evergreen
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L15-L16 — Derivatives of Inverse Trig Functions

Differentiation of inverse trigonometric functions using the inverse rule, implicit differentiation, and the chain rule. The lectures cover derivations of all six inverse trigonometric derivative formulas and apply them in combination with product, quotient, and chain rules.

## Learning Objective

To differentiate inverse trigonometric functions correctly, applying the chain rule and considering domain restrictions and absolute values where necessary.

## The Inverse Rule

For an invertible function $f$ with inverse $f^{-1}$:

$$\frac{d}{dx}\left[f^{-1}(x)\right] = \frac{1}{f'\left(f^{-1}(x)\right)}$$

This is the foundation for all inverse trigonometric derivative formulas.

---

## Derivative of Inverse Sine

Let $y = \sin^{-1} x$, which means $\sin y = x$.

**Step 1 — Implicit differentiation:**
$$\cos(y) \frac{dy}{dx} = 1$$

**Step 2 — Solve for $\frac{dy}{dx}$:**
$$\frac{dy}{dx} = \frac{1}{\cos(y)} = \frac{1}{\cos(\sin^{-1} x)}$$

**Step 3 — Geometric simplification (right triangle):**
Consider a right triangle with angle $y = \sin^{-1} x$:
- Opposite side $= x$
- Hypotenuse $= 1$
- Adjacent side $= \sqrt{1 - x^2}$

Therefore $\cos(y) = \sqrt{1 - x^2}$, giving:

$$\boxed{\frac{d}{dx}\sin^{-1} x = \frac{1}{\sqrt{1-x^2}}}$$

---

## Derivative of Inverse Cosine

Let $f(x) = \cos^{-1} x$, which means $\cos(f(x)) = x$.

**Step 1 — Implicit differentiation:**
$$-\sin(f(x)) \cdot f'(x) = 1$$

**Step 2 — Solve for $f'(x)$:**
$$f'(x) = \frac{1}{-\sin(f(x))} = \frac{-1}{\sin(\cos^{-1} x)}$$

**Step 3 — Geometric simplification (right triangle):**
Consider a right triangle with angle $f(x) = \cos^{-1} x$:
- Adjacent side $= x$
- Hypotenuse $= 1$
- Opposite side $= \sqrt{1 - x^2}$

Therefore $\sin(f(x)) = \sqrt{1 - x^2}$, giving:

$$\boxed{\frac{d}{dx}\cos^{-1} x = \frac{-1}{\sqrt{1-x^2}}}$$

---

## Derivative of Inverse Tangent

Let $f(x) = \tan^{-1} x$, which means $\tan(f(x)) = x$.

**Step 1 — Apply inverse rule:**
$$\frac{d}{dx}\left[\tan^{-1}(x)\right] = \frac{1}{\sec^2(\tan^{-1}(x))}$$

**Step 2 — Geometric simplification (right triangle):**
Consider a right triangle with angle $f(x) = \tan^{-1} x$:
- Opposite side $= x$
- Adjacent side $= 1$
- Hypotenuse $= \sqrt{1 + x^2} = \sec(\tan^{-1} x)$

Therefore:
$$\frac{d}{dx}\left[\tan^{-1}(x)\right] = \frac{1}{(\sec(\tan^{-1} x))^2} = \frac{1}{(\sqrt{1+x^2})^2}$$

$$\boxed{\frac{d}{dx}\tan^{-1} x = \frac{1}{1+x^2}}$$

---

## Derivative of Inverse Cosecant

Let $f(x) = \csc^{-1} x$ (also written $\text{cosec}^{-1} x$), which means $\csc(f(x)) = x$.

**Step 1 — Implicit differentiation:**
$$-\csc(f(x)) \cdot \cot(f(x)) \cdot f'(x) = 1$$

**Step 2 — Solve for $f'(x)$:**
$$f'(x) = \frac{1}{-\csc(f(x)) \cdot \cot(f(x))}$$

**Step 3 — Geometric simplification (right triangle):**
Consider a right triangle with angle $f(x) = \csc^{-1} x$:
- Hypotenuse $= |x|$ (always positive — absolute value required)
- Opposite side $= 1$
- Adjacent side $= \sqrt{x^2 - 1}$

Since $\csc(f(x)) = x$ and $\cot(f(x)) = \sqrt{x^2 - 1}$ (with sign considerations), we get:

$$f'(x) = \frac{-1}{x\sqrt{x^2-1}} = \frac{-1}{|x|\sqrt{x^2-1}}$$

$$\boxed{\frac{d}{dx}\csc^{-1} x = \frac{-1}{|x|\sqrt{x^2-1}}}$$

> **Important:** The hypotenuse is always positive, hence the absolute value $|x|$ in the denominator.

---

## Derivative of Inverse Secant

Following the same method as for inverse cosecant:

$$\boxed{\frac{d}{dx}\sec^{-1} x = \frac{1}{|x|\sqrt{x^2-1}}}$$

---

## Derivative of Inverse Cotangent

Following the same method as for inverse tangent:

$$\boxed{\frac{d}{dx}\cot^{-1} x = \frac{-1}{1+x^2}}$$

---

## Summary Table

### Basic Derivatives

| Function | Derivative |
|----------|------------|
| $\frac{d}{dx}\left[\sin^{-1}(x)\right]$ | $\frac{1}{\sqrt{1-x^2}}$ |
| $\frac{d}{dx}\left[\cos^{-1}(x)\right]$ | $\frac{-1}{\sqrt{1-x^2}}$ |
| $\frac{d}{dx}\left[\tan^{-1}(x)\right]$ | $\frac{1}{1+x^2}$ |
| $\frac{d}{dx}\left[\cot^{-1}(x)\right]$ | $\frac{-1}{1+x^2}$ |
| $\frac{d}{dx}\left[\sec^{-1}(x)\right]$ | $\frac{1}{|x|\sqrt{x^2-1}}$ |
| $\frac{d}{dx}\left[\csc^{-1}(x)\right]$ | $\frac{-1}{|x|\sqrt{x^2-1}}$ |

### Chain Rule Versions

| Function | Derivative |
|----------|------------|
| $\frac{d}{dx}\left[\sin^{-1}(g(x))\right]$ | $\frac{1}{\sqrt{1-(g(x))^2}} \cdot g'(x)$ |
| $\frac{d}{dx}\left[\cos^{-1}(g(x))\right]$ | $\frac{-1}{\sqrt{1-(g(x))^2}} \cdot g'(x)$ |
| $\frac{d}{dx}\left[\tan^{-1}(g(x))\right]$ | $\frac{1}{1+(g(x))^2} \cdot g'(x)$ |
| $\frac{d}{dx}\left[\cot^{-1}(g(x))\right]$ | $\frac{-1}{1+(g(x))^2} \cdot g'(x)$ |
| $\frac{d}{dx}\left[\sec^{-1}(g(x))\right]$ | $\frac{g'(x)}{|g(x)|\sqrt{(g(x))^2-1}}$ |
| $\frac{d}{dx}\left[\csc^{-1}(g(x))\right]$ | $\frac{-g'(x)}{|g(x)|\sqrt{(g(x))^2-1}}$ |

---

## Worked Examples

### Example 1: Power Rule + Chain Rule
Find $\frac{d}{dx}\left[\sqrt{\cos^{-1}(x)}\right]$.

**Solution:**
$$\begin{aligned}
\frac{d}{dx}\left[\sqrt{\cos^{-1}(x)}\right] &= \frac{d}{dx}\left[(\cos^{-1}(x))^{\frac{1}{2}}\right] \\
&= \frac{1}{2}(\cos^{-1}(x))^{-\frac{1}{2}} \cdot \frac{d}{dx}\left[\cos^{-1}(x)\right] \\
&= \frac{1}{2}(\cos^{-1}(x))^{-\frac{1}{2}} \cdot \frac{-1}{\sqrt{1-x^2}} \\
&= \frac{-1}{2\sqrt{\cos^{-1}(x)}\sqrt{1-x^2}}
\end{aligned}$$

---

### Example 2: Chain Rule with Linear Inner Function
Find the derivative of $f(x) = \cos^{-1}(3x)$.

**Solution:**
Let $f(x) = \cos^{-1}(3x)$, so $\cos(f(x)) = 3x$.

$$\begin{aligned}
-\sin(f(x)) \cdot f'(x) &= 3 \\
f'(x) &= \frac{3}{-\sin(f(x))} = \frac{-3}{\sin(\cos^{-1} 3x)} \\
&= \frac{-3}{\sqrt{1-9x^2}}
\end{aligned}$$

Or using the chain rule formula directly:
$$f'(x) = \frac{-1}{\sqrt{1-(3x)^2}} \cdot 3 = \frac{-3}{\sqrt{1-9x^2}}$$

---

### Example 3: Exponential + Chain Rule
Find $\frac{d}{dx}\left[e^{\tan^{-1}(x)}\right]$.

**Solution:**
$$\begin{aligned}
\frac{d}{dx}\left[e^{\tan^{-1}(x)}\right] &= e^{\tan^{-1}(x)} \cdot \frac{d}{dx}\left[\tan^{-1}(x)\right] \\
&= e^{\tan^{-1}(x)} \cdot \frac{1}{1+x^2} \\
&= \frac{e^{\tan^{-1}(x)}}{1+x^2}
\end{aligned}$$

---

### Example 4: Logarithmic + Chain Rule
Find $\frac{d}{dx}\left[\ln(\sin^{-1}(x))\right]$.

**Solution:**
$$\begin{aligned}
\frac{d}{dx}\left[\ln(\sin^{-1}(x))\right] &= \frac{1}{\sin^{-1}(x)} \cdot \frac{d}{dx}\left[\sin^{-1}(x)\right] \\
&= \frac{1}{\sin^{-1}(x)} \cdot \frac{1}{\sqrt{1-x^2}} \\
&= \frac{1}{\sin^{-1}(x)\sqrt{1-x^2}}
\end{aligned}$$

---

### Example 5: Product Rule + Chain Rule
Differentiate $f(x) = x^2 \cos^{-1}\left(e^{3x}\right)$.

**Solution:**
Use the product rule: $(uv)' = uv' + vu'$

Let $g(x) = x^2$ and $h(x) = \cos^{-1}\left(e^{3x}\right)$.

$$\begin{aligned}
g'(x) &= 2x \\
h'(x) &= \frac{-1}{\sqrt{1-(e^{3x})^2}} \cdot 3e^{3x} = \frac{-3e^{3x}}{\sqrt{1-e^{6x}}}
\end{aligned}$$

Therefore:
$$\begin{aligned}
f'(x) &= x^2 \cdot \frac{-3e^{3x}}{\sqrt{1-e^{6x}}} + \cos^{-1}\left(e^{3x}\right) \cdot 2x \\
&= \frac{-3x^2 e^{3x} + 2x\cos^{-1}\left(e^{3x}\right)\sqrt{1-e^{6x}}}{\sqrt{1-e^{6x}}}
\end{aligned}$$

---

### Example 6: Quotient Rule + Chain Rule
Differentiate $y = \frac{\sin^{-1}(3x)}{x^2}$.

**Solution:**
Use the quotient rule (or product rule with $x^{-2}$).

$$\begin{aligned}
\frac{dy}{dx} &= \sin^{-1}(3x) \cdot \frac{-2}{x^3} + \frac{1}{x^2} \cdot \frac{3}{\sqrt{1-9x^2}} \\
&= \frac{-2\sin^{-1}(3x)}{x^3} + \frac{3}{x^2\sqrt{1-9x^2}} \\
&= \frac{-2\sin^{-1}(3x)\sqrt{1-9x^2} + 3x}{x^3\sqrt{1-9x^2}}
\end{aligned}$$

---

## Key Takeaways

1. **All six derivatives can be derived** from the inverse rule $\frac{d}{dx}[f^{-1}(x)] = \frac{1}{f'(f^{-1}(x))}$ using implicit differentiation.

2. **Geometric simplification** using right triangles is essential to convert expressions like $\cos(\sin^{-1} x)$ into algebraic forms.

3. **Absolute values** are required for $\sec^{-1}$ and $\csc^{-1}$ derivatives because hypotenuse lengths are always positive.

4. **Chain rule is ubiquitous** — most problems involve composite functions requiring $\frac{d}{dx}[\text{inverse trig}(g(x))] = \text{formula} \cdot g'(x)$.

5. **Combined techniques** — Product and quotient rules are frequently needed alongside the chain rule.

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Inverse Trigonometric Functions]] — concept page (definitions, domains, ranges, identities)
- [[FAC1004 L14 — Properties of Inverse Trig Functions]] — previous lecture
- [[FAC1004 L17 — Hyperbolic Functions]] — next lecture
- [[FAC1004 Tutorial 6 — Inverse Trigonometric Functions]] — practice problems
- [[FAC1004 Tutorial 7 — Derivatives of Inverse Trig Functions]] — differentiation practice

## Source File

`LECTURE_NOTES_2526/L15 L16 DERIVATIVES OF INVERSE TRIGONOMETRIC FUNCTIONS - full.pdf`
