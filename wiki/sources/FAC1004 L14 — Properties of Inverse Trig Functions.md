---
title: FAC1004 L14 — Properties of Inverse Trig Functions
date: 2026-04-29
tags:
  - source/lecture
  - subject/mathematics
  - topic/inverse-trigonometric-functions
  - status/evergreen
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L14 — Properties of Inverse Trig Functions

This lecture covers the algebraic properties of inverse trigonometric functions, including composition rules, complementary relationships, negative argument properties, sum/difference formulas, double-angle identities, and interconversion between inverse trig functions.

## Learning Objective

To learn the properties of inverse trigonometric functions and perform calculations involving these properties.

## Domain and Range (Principal Values)

| Function | Domain | Range (Principal Value) |
|---|---|---|
| $y = \sin^{-1} x$ | $[-1, 1]$ | $\displaystyle\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ |
| $y = \cos^{-1} x$ | $[-1, 1]$ | $[0, \pi]$ |
| $y = \tan^{-1} x$ | $\mathbb{R}$ | $\displaystyle\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ |
| $y = \cot^{-1} x$ | $\mathbb{R}$ | $[0, \pi]$ |
| $y = \sec^{-1} x$ | $(-\infty, -1] \cup [1, \infty)$ | $\displaystyle\left[0, \frac{\pi}{2}\right) \cup \left(\frac{\pi}{2}, \pi\right]$ |
| $y = \csc^{-1} x$ | $(-\infty, -1] \cup [1, \infty)$ | $\displaystyle\left[-\frac{\pi}{2}, 0\right) \cup \left(0, \frac{\pi}{2}\right]$ |

> [!note] Notation
> This lecture uses $\csc^{-1}$ and $\csc$ notation. The slides also use $\text{cosec}^{-1}$ and $\text{cosec}$ interchangeably.

---

## Property 1: Composition (Cancellation) Equations

These describe when an inverse trig function "cancels" its corresponding trig function, and vice versa.

**Inverse followed by function:**
$$\sin^{-1}(\sin \theta) = \theta, \quad -\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$$
$$\cos^{-1}(\cos \theta) = \theta, \quad 0 \le \theta \le \pi$$
$$\tan^{-1}(\tan \theta) = \theta, \quad -\frac{\pi}{2} < \theta < \frac{\pi}{2}$$

**Function followed by inverse:**
$$\sin(\sin^{-1} x) = x$$
$$\cos(\cos^{-1} x) = x$$
$$\tan(\tan^{-1} x) = x$$

> [!important] Domain restriction
> The identities $\sin^{-1}(\sin \theta) = \theta$, $\cos^{-1}(\cos \theta) = \theta$, and $\tan^{-1}(\tan \theta) = \theta$ **only hold** when $\theta$ is within the principal range of the respective inverse function.

---

## Property 2: Reciprocal Relationships

Inverse cosecant, cotangent, and secant can be expressed in terms of inverse sine, tangent, and cosine:

$$(\text{i}) \quad \csc^{-1} x = \sin^{-1}\left(\frac{1}{x}\right)$$

$$(\text{ii}) \quad \cot^{-1} x = \tan^{-1}\left(\frac{1}{x}\right)$$

$$(\text{iii}) \quad \sec^{-1} x = \cos^{-1}\left(\frac{1}{x}\right)$$

**Proof of (i):** Let $\csc^{-1} x = \theta \Rightarrow x = \csc \theta \Rightarrow \frac{1}{x} = \sin \theta \Rightarrow \theta = \sin^{-1}\left(\frac{1}{x}\right)$.

The other two follow by analogous methods.

---

## Property 3: Negative Argument Properties

$$(\text{i}) \quad \sin^{-1}(-x) = -\sin^{-1} x$$

$$(\text{ii}) \quad \tan^{-1}(-x) = -\tan^{-1} x$$

**Proof of (i):** Let $-x = \sin \theta$, so $x = -\sin \theta = \sin(-\theta)$. Then $-\theta = \sin^{-1} x$, giving $\theta = -\sin^{-1} x$. Therefore $\sin^{-1}(-x) = -\sin^{-1} x$.

> [!note]
> This lecture covers only $\sin^{-1}(-x)$ and $\tan^{-1}(-x)$. The property $\cos^{-1}(-x) = \pi - \cos^{-1} x$ is **not covered** in L14.

---

## Property 4: Complementary Relationships

$$(\text{i}) \quad \sin^{-1} x + \cos^{-1} x = \frac{\pi}{2}$$

$$(\text{ii}) \quad \tan^{-1} x + \cot^{-1} x = \frac{\pi}{2}$$

$$(\text{iii}) \quad \csc^{-1} x + \sec^{-1} x = \frac{\pi}{2}$$

**Proof of (i):** Let $\sin^{-1} x = \theta \Rightarrow x = \sin \theta = \cos\left(\frac{\pi}{2} - \theta\right)$. Then $\cos^{-1} x = \frac{\pi}{2} - \theta$, so $\theta + \cos^{-1} x = \frac{\pi}{2}$, giving $\sin^{-1} x + \cos^{-1} x = \frac{\pi}{2}$.

The others follow similarly using cofunction identities.

---

## Property 5: Sum and Difference Formulas

For inverse tangent:

$$(\text{i}) \quad \tan^{-1} x + \tan^{-1} y = \tan^{-1}\left(\frac{x + y}{1 - xy}\right)$$

$$(\text{ii}) \quad \tan^{-1} x - \tan^{-1} y = \tan^{-1}\left(\frac{x - y}{1 + xy}\right)$$

**Proof of (i):** Let $\tan^{-1} x = \theta$ and $\tan^{-1} y = \phi$, so $x = \tan \theta$ and $y = \tan \phi$.

$$\text{L.H.S.} = \theta + \phi$$
$$\text{R.H.S.} = \tan^{-1}\left(\frac{\tan \theta + \tan \phi}{1 - \tan \theta \tan \phi}\right) = \tan^{-1}[\tan(\theta + \phi)] = \theta + \phi = \text{L.H.S.}$$

$\therefore$ The result holds.

---

## Property 6: Double Angle Formula

$$2\tan^{-1} x = \sin^{-1}\left(\frac{2x}{1 + x^2}\right) = \cos^{-1}\left(\frac{1 - x^2}{1 + x^2}\right) = \tan^{-1}\left(\frac{2x}{1 - x^2}\right)$$

**Proof:** Let $x = \tan \theta$.

$$2\tan^{-1} x = 2\tan^{-1}(\tan \theta) = 2\theta \quad \text{......(i)}$$

$$\sin^{-1}\left(\frac{2x}{1 + x^2}\right) = \sin^{-1}\left(\frac{2\tan \theta}{1 + \tan^2 \theta}\right) = \sin^{-1}(2\sin\theta\cos\theta) = \sin^{-1}(\sin 2\theta) = 2\theta \quad \text{......(ii)}$$

$$\cos^{-1}\left(\frac{1 - x^2}{1 + x^2}\right) = \cos^{-1}\left(\frac{1 - \tan^2 \theta}{1 + \tan^2 \theta}\right) = \cos^{-1}(\cos^2\theta - \sin^2\theta) = \cos^{-1}(\cos 2\theta) = 2\theta \quad \text{......(iii)}$$

$$\tan^{-1}\left(\frac{2x}{1 - x^2}\right) = \tan^{-1}\left(\frac{2\tan \theta}{1 - \tan^2 \theta}\right) = \tan^{-1}(\tan 2\theta) = 2\theta \quad \text{......(iv)}$$

From (i), (ii), (iii), and (iv):
$$2\tan^{-1} x = \sin^{-1}\left(\frac{2x}{1 + x^2}\right) = \cos^{-1}\left(\frac{1 - x^2}{1 + x^2}\right) = \tan^{-1}\left(\frac{2x}{1 - x^2}\right)$$

---

## Property 7: Interconversion Formulas

### Part (i): Expressing $\sin^{-1} x$ in terms of other inverse functions

$$\sin^{-1} x = \cos^{-1}\left(\sqrt{1 - x^2}\right) = \tan^{-1}\left(\frac{x}{\sqrt{1 - x^2}}\right) = \sec^{-1}\left(\frac{1}{\sqrt{1 - x^2}}\right) = \cot^{-1}\left(\frac{\sqrt{1 - x^2}}{x}\right) = \csc^{-1}\left(\frac{1}{x}\right)$$

**Proof:** Let $\sin^{-1} x = \theta \Rightarrow \sin \theta = x$. By right-triangle or Pythagorean identity:
$$\cos \theta = \sqrt{1 - x^2}, \quad \tan \theta = \frac{x}{\sqrt{1 - x^2}}, \quad \sec \theta = \frac{1}{\sqrt{1 - x^2}}, \quad \cot \theta = \frac{\sqrt{1 - x^2}}{x}, \quad \csc \theta = \frac{1}{x}$$

Therefore $\theta$ equals each of the inverse expressions above.

### Part (ii): Expressing $\cos^{-1} x$ in terms of other inverse functions

$$\cos^{-1} x = \sin^{-1}\left(\sqrt{1 - x^2}\right) = \tan^{-1}\left(\frac{\sqrt{1 - x^2}}{x}\right) = \csc^{-1}\left(\frac{1}{\sqrt{1 - x^2}}\right) = \cot^{-1}\left(\frac{x}{\sqrt{1 - x^2}}\right) = \sec^{-1}\left(\frac{1}{x}\right)$$

**Proof:** Let $\cos^{-1} x = \theta \Rightarrow \cos \theta = x$. Then:
$$\sin \theta = \sqrt{1 - x^2}, \quad \tan \theta = \frac{\sqrt{1 - x^2}}{x}, \quad \csc \theta = \frac{1}{\sqrt{1 - x^2}}, \quad \cot \theta = \frac{x}{\sqrt{1 - x^2}}, \quad \sec \theta = \frac{1}{x}$$

---

## Worked Examples

### Example 1: Evaluating a Composite Expression

Find the exact value of:
$$\cos\left(\sin^{-1}\left(\frac{3}{5}\right) + \frac{\pi}{2}\right)$$

**Solution:**
Using the cosine addition formula:
$$\cos\left(\sin^{-1}\left(\frac{3}{5}\right) + \frac{\pi}{2}\right) = \cos\left(\sin^{-1}\left(\frac{3}{5}\right)\right)\cos\left(\frac{\pi}{2}\right) - \sin\left(\sin^{-1}\left(\frac{3}{5}\right)\right)\sin\left(\frac{\pi}{2}\right)$$

From Property 7(i), $\cos\left(\sin^{-1}\left(\frac{3}{5}\right)\right) = \sqrt{1 - \left(\frac{3}{5}\right)^2} = \sqrt{\frac{16}{25}} = \frac{4}{5}$.

Also, $\sin\left(\sin^{-1}\left(\frac{3}{5}\right)\right) = \frac{3}{5}$, $\cos\left(\frac{\pi}{2}\right) = 0$, and $\sin\left(\frac{\pi}{2}\right) = 1$.

$$= \left(\frac{4}{5}\right)(0) - \left(\frac{3}{5}\right)(1) = \boxed{-\frac{3}{5}}$$

### Example 2: Proving an Inverse Tangent Identity

Prove that:
$$\tan^{-1}\left(\frac{1}{7}\right) + \tan^{-1}\left(\frac{1}{13}\right) = \tan^{-1}\left(\frac{2}{9}\right)$$

**Solution:**
Applying Property 5(i):
$$\tan^{-1}\left(\frac{1}{7}\right) + \tan^{-1}\left(\frac{1}{13}\right) = \tan^{-1}\left(\frac{\frac{1}{7} + \frac{1}{13}}{1 - \frac{1}{7} \cdot \frac{1}{13}}\right)$$

$$= \tan^{-1}\left(\frac{\frac{13 + 7}{91}}{1 - \frac{1}{91}}\right) = \tan^{-1}\left(\frac{\frac{20}{91}}{\frac{90}{91}}\right) = \tan^{-1}\left(\frac{20}{90}\right) = \boxed{\tan^{-1}\left(\frac{2}{9}\right)}$$

---

## Summary of All Properties

| Property | Identity |
|---|---|
| **1(i)** | $\sin^{-1}(\sin \theta) = \theta$, $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$ |
| **1(ii)** | $\cos^{-1}(\cos \theta) = \theta$, $0 \le \theta \le \pi$ |
| **1(iii)** | $\tan^{-1}(\tan \theta) = \theta$, $-\frac{\pi}{2} < \theta < \frac{\pi}{2}$ |
| **2(i)** | $\csc^{-1} x = \sin^{-1}\left(\frac{1}{x}\right)$ |
| **2(ii)** | $\cot^{-1} x = \tan^{-1}\left(\frac{1}{x}\right)$ |
| **2(iii)** | $\sec^{-1} x = \cos^{-1}\left(\frac{1}{x}\right)$ |
| **3(i)** | $\sin^{-1}(-x) = -\sin^{-1} x$ |
| **3(ii)** | $\tan^{-1}(-x) = -\tan^{-1} x$ |
| **4(i)** | $\sin^{-1} x + \cos^{-1} x = \frac{\pi}{2}$ |
| **4(ii)** | $\tan^{-1} x + \cot^{-1} x = \frac{\pi}{2}$ |
| **4(iii)** | $\csc^{-1} x + \sec^{-1} x = \frac{\pi}{2}$ |
| **5(i)** | $\tan^{-1} x + \tan^{-1} y = \tan^{-1}\left(\frac{x + y}{1 - xy}\right)$ |
| **5(ii)** | $\tan^{-1} x - \tan^{-1} y = \tan^{-1}\left(\frac{x - y}{1 + xy}\right)$ |
| **6** | $2\tan^{-1} x = \sin^{-1}\left(\frac{2x}{1 + x^2}\right) = \cos^{-1}\left(\frac{1 - x^2}{1 + x^2}\right) = \tan^{-1}\left(\frac{2x}{1 - x^2}\right)$ |
| **7(i)** | $\sin^{-1} x = \cos^{-1}(\sqrt{1-x^2}) = \tan^{-1}\left(\frac{x}{\sqrt{1-x^2}}\right) = \sec^{-1}\left(\frac{1}{\sqrt{1-x^2}}\right) = \cot^{-1}\left(\frac{\sqrt{1-x^2}}{x}\right) = \csc^{-1}\left(\frac{1}{x}\right)$ |
| **7(ii)** | $\cos^{-1} x = \sin^{-1}(\sqrt{1-x^2}) = \tan^{-1}\left(\frac{\sqrt{1-x^2}}{x}\right) = \csc^{-1}\left(\frac{1}{\sqrt{1-x^2}}\right) = \cot^{-1}\left(\frac{x}{\sqrt{1-x^2}}\right) = \sec^{-1}\left(\frac{1}{x}\right)$ |

---

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Inverse Trigonometric Functions]] — comprehensive concept page
- [[FAC1004 L13 — Inverse Trigonometric Functions]] — introduction lecture (definitions, principal values)
- [[FAC1004 L15-L16 — Derivatives of Inverse Trig Functions]] — next lecture
- [[FAC1004 Tutorial 6 — Inverse Trigonometric Functions]] — practice problems
- [[FAC1004 Tutorial 7 — Derivatives of Inverse Trig Functions]] — differentiation practice

## Source File

`LECTURE_NOTES_2526/L14 Properties of Inverse Trigonometric Functions Full Version.pdf`
