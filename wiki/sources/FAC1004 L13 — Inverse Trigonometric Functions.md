---
title: FAC1004 L13 — Inverse Trigonometric Functions
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics
  - topic/inverse-trigonometric-functions
  - status/sprout
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L13 — Inverse Trigonometric Functions

## Learning Objective

To identify the **domains**, **ranges**, and **graphs** of inverse trigonometric functions and calculate their **principal values**.

---

## Core Idea

The six basic trigonometric functions are **not one-to-one** (their values repeat periodically). To define their inverses, we **restrict their domains** to intervals on which they are one-to-one.

---

## Definitions, Domains, and Ranges

### 1. Inverse Sine — $\sin^{-1} x$ or $\arcsin x$

Defined as the inverse of the **restricted sine function**:
$$y = \sin x, \quad -\frac{\pi}{2} \le x \le \frac{\pi}{2}$$

- **Domain:** $[-1, 1]$
- **Range (Principal Value):** $\displaystyle\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$

### 2. Inverse Cosine — $\cos^{-1} x$ or $\arccos x$

Defined as the inverse of the **restricted cosine function**:
$$y = \cos x, \quad 0 \le x \le \pi$$

- **Domain:** $[-1, 1]$
- **Range (Principal Value):** $[0, \pi]$

### 3. Inverse Tangent — $\tan^{-1} x$ or $\arctan x$

Defined as the inverse of the **restricted tangent function**:
$$y = \tan x, \quad -\frac{\pi}{2} < x < \frac{\pi}{2}$$

- **Domain:** $(-\infty, \infty)$ or $\mathbb{R}$
- **Range (Principal Value):** $\displaystyle\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$

### 4. Inverse Secant — $\sec^{-1} x$ or $\text{arcsec } x$

Defined as the inverse of the **restricted secant function**:
$$y = \sec x, \quad 0 \le x < \frac{\pi}{2}, \; \frac{\pi}{2} < x \le \pi$$

- **Domain:** $(-\infty, -1] \cup [1, \infty)$  
  (equivalently: $x \ge 1$ or $x \le -1$)
- **Range (Principal Value):** $\displaystyle\left[0, \frac{\pi}{2}\right) \cup \left(\frac{\pi}{2}, \pi\right]$

### 5. Inverse Cosecant — $\csc^{-1} x$ or $\text{arccsc } x$

Defined as the inverse of the **restricted cosecant function**:
$$y = \csc x, \quad -\frac{\pi}{2} \le x < 0, \; 0 < x \le \frac{\pi}{2}$$

- **Domain:** $(-\infty, -1] \cup [1, \infty)$  
  (equivalently: $x \ge 1$ or $x \le -1$)
- **Range (Principal Value):** $\displaystyle\left[-\frac{\pi}{2}, 0\right) \cup \left(0, \frac{\pi}{2}\right]$

### 6. Inverse Cotangent — $\cot^{-1} x$ or $\text{arccot } x$

Defined as the inverse of the **restricted cotangent function**:
$$y = \cot x, \quad 0 < x < \pi$$

- **Domain:** $(-\infty, \infty)$ or $\mathbb{R}$
- **Range (Principal Value):** $(0, \pi)$

> **Note:** The lecture definition page explicitly gives Range $(0, \pi)$ for $\cot^{-1} x$ (consistent with the asymptotic behaviour of $\cot x$ at $0$ and $\pi$).

---

## Summary Table

| Function | Domain | Range (Principal Value) |
|---|---|---|
| $y = \sin^{-1} x$ | $[-1, 1]$ | $\displaystyle\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| $y = \cos^{-1} x$ | $[-1, 1]$ | $[0, \pi]$ |
| $y = \tan^{-1} x$ | $\mathbb{R}$ | $\displaystyle\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |
| $y = \cot^{-1} x$ | $\mathbb{R}$ | $(0, \pi)$ |
| $y = \sec^{-1} x$ | $(-\infty, -1] \cup [1, \infty)$ | $\displaystyle\left[0, \frac{\pi}{2}\right) \cup \left(\frac{\pi}{2}, \pi\right]$ |
| $y = \csc^{-1} x$ | $(-\infty, -1] \cup [1, \infty)$ | $\displaystyle\left[-\frac{\pi}{2}, 0\right) \cup \left(0, \frac{\pi}{2}\right]$ |

---

## Worked Examples

### Example 1 — Principal Values

Find the principal value of each of the following:

**(i)** $\displaystyle\sin^{-1}\left(\frac{1}{\sqrt{2}}\right)$

Let $\displaystyle\sin^{-1}\left(\frac{1}{\sqrt{2}}\right) = \theta$. Then:
$$\sin \theta = \frac{1}{\sqrt{2}} = \sin\left(\frac{\pi}{4}\right)$$
$$\boxed{\theta = \frac{\pi}{4}}$$

**(ii)** $\displaystyle\cos^{-1}\left(-\frac{1}{2}\right)$

Let $\displaystyle\cos^{-1}\left(-\frac{1}{2}\right) = \theta$. Then:
$$\cos \theta = -\frac{1}{2} = \cos\left(\pi - \frac{\pi}{3}\right) = \cos\left(\frac{2\pi}{3}\right)$$
$$\boxed{\theta = \frac{2\pi}{3}}$$

**(iii)** $\displaystyle\tan^{-1}\left(-\frac{1}{\sqrt{3}}\right)$

Let $\displaystyle\tan^{-1}\left(-\frac{1}{\sqrt{3}}\right) = \theta$. Then:
$$\tan \theta = -\frac{1}{\sqrt{3}} = \tan\left(-\frac{\pi}{6}\right)$$
$$\boxed{\theta = -\frac{\pi}{6}}$$

### Example 2 — Composition of Functions

Find the value of $\displaystyle\sec\left[\cos^{-1}\frac{\sqrt{3}}{2}\right]$.

Let $\displaystyle\cos^{-1}\left(\frac{\sqrt{3}}{2}\right) = \theta$. Then:
$$\cos \theta = \frac{\sqrt{3}}{2} = \cos\left(\frac{\pi}{6}\right) \quad\Longrightarrow\quad \theta = \frac{\pi}{6}$$

Therefore:
$$\sec\left[\cos^{-1}\frac{\sqrt{3}}{2}\right] = \sec \theta = \sec\left(\frac{\pi}{6}\right) = \frac{2}{\sqrt{3}}$$

### Example 3 — Algebraic Simplification

**Simplify $\cos\left(\sin^{-1} x\right)$.**

Let $\sin^{-1} x = \theta \;\Rightarrow\; x = \sin \theta$.

$$\cos\left(\sin^{-1} x\right) = \cos \theta = \sqrt{1 - \sin^{2}\theta} = \sqrt{1 - x^{2}}$$

$$\boxed{\cos\left(\sin^{-1} x\right) = \sqrt{1 - x^{2}}}$$

**Simplify $\cot\left(\csc^{-1} x\right)$.**

Let $\csc^{-1} x = \theta \;\Rightarrow\; x = \csc \theta$.

$$\cot\left(\csc^{-1} x\right) = \cot \theta = \sqrt{\csc^{2}\theta - 1} = \sqrt{x^{2} - 1}$$

$$\boxed{\cot\left(\csc^{-1} x\right) = \sqrt{x^{2} - 1}}$$

---

## Key Takeaways

1. Inverse trig functions require **domain restriction** on the original trig function to ensure it is one-to-one.
2. The **principal value** is the unique angle in the restricted range that satisfies the equation.
3. For negative inputs, use the corresponding reference angle and adjust according to the range of the inverse function.
4. Compositions can be simplified using Pythagorean identities.

---

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Inverse Trigonometric Functions]] — concept page
- [[FAC1004 L14 — Properties of Inverse Trig Functions]] — next lecture
- [[FAC1004 L15-L16 — Derivatives of Inverse Trig Functions]] — derivatives lecture
- [[FAC1004 Tutorial 6 — Inverse Trigonometric Functions]] — practice problems

## Source File

`LECTURE_NOTES_2526/L13 Inverse Trigonometric Function Full Version.pdf`
