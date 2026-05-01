---
title: FAC1004 L5-L6 — Functions of Complex Numbers (n-th Roots)
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics
  - topic/complex-numbers
  - topic/de-moivre
  - topic/n-th-roots
  - topic/complex-exponential
  - topic/complex-trigonometric-functions
  - topic/complex-logarithm
  - status/sapling
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[Hisham Safuan bin Mohamad Sukri]]"
---

# FAC1004 L5-L6 — Functions of Complex Numbers (n-th Roots)

> **Note:** The lecture slides display the course code **FAC1001** Advanced Mathematics II. This source is catalogued under FAC1004 to match the computing-stream wiki structure.

This lecture covers advanced functions of complex numbers: De Moivre's theorem, n-th roots, the complex exponential function, complex trigonometric functions, and the complex logarithm.

## Review of Complex Number Forms

For a complex number $z = a + bi$:

1. **Cartesian form:** $z = a + bi$
2. **Polar form:** $z = r(\cos\theta + i\sin\theta)$, where $r = |z|$ is the magnitude and $\theta = \arg(z)$ is the argument
3. **Euler form:** $z = re^{i\theta}$

Key points from the lecture:
- The **principal argument** is restricted to $\theta \in (-\pi, \pi]$
- The magnitude $r$ is always positive (it is the distance from the origin in the Argand diagram)

## De Moivre's Theorem

For $z = r(\cos\theta + i\sin\theta)$ and integer $n$:

$$z^n = [r(\cos\theta + i\sin\theta)]^n = r^n(\cos n\theta + i\sin n\theta)$$

By its Euler form:
$$z^n = (re^{i\theta})^n = r^n e^{in\theta}$$

This shows that $f : \mathbb{C} \to \mathbb{C}$, or simply $z^n = w$ where $z, w \in \mathbb{C}$.

## Coterminal Angles

- **Coterminal angles** are angles that share the same terminal side.
- For a complex number $z = a + bi = r(\cos\theta + i\sin\theta)$, the principal angle is $\theta \in (-\pi, \pi]$.
- Coterminal angles are $\theta + 2\pi k$ where $k \in \mathbb{Z}$.
- A complex number can be written in Euler form using its principal angle: $z = re^{i\theta}$
- Considering its coterminal aspect: $z = re^{i(\theta + 2\pi k)}$
- When raised to the power of integer $n$: $z = re^{i(\theta + 2\pi k)} \implies z^n = \big(re^{i(\theta + 2\pi k)}\big)^n$

## n-th Roots of a Complex Number

Since powers of a complex number yield another complex number ($z^n = w$), we can find the original complex number by taking the n-th root: $z = w^{1/n}$.

Consider the Euler form of $w$ with its coterminal angle:

$$z = \big(re^{(\theta + 2\pi k)i}\big)^{1/n}$$

$$z = r^{1/n} e^{\frac{\theta + 2\pi k}{n}i} = \sqrt[n]{r}\left(\cos\frac{\theta + 2\pi k}{n} + i\sin\frac{\theta + 2\pi k}{n}\right)$$

for $k = 0, 1, 2, \ldots, n-1$.

Every non-zero complex number has exactly $n$ distinct n-th roots, equally spaced around a circle of radius $\sqrt[n]{r}$ in the complex plane.

## Complex Exponential Function

What is the outcome when evaluating $e^z$?

Using the Cartesian form $z = a + bi$:
$$e^z = e^{a+bi} = e^a \cdot e^{bi}$$

The form $e^a \cdot e^{bi}$ is similar to the Euler form $re^{i\theta}$. Comparing both:
- $|e^z| = e^a$
- $\arg(e^z) = b$ rad

Further simplified in polar and Cartesian form:
$$e^a \cdot e^{bi} = e^a(\cos b + i\sin b) = e^a\cos b + i\,(e^a\sin b)$$

**Conclusion:** $e^z$ is a **periodic function**.

## Complex Cosines and Sines Function

Let $z = a + bi = r(\cos\theta + i\sin\theta) = re^{i\theta}$.

Using the polar and Euler form:
$$e^{xi} = \cos x + i\sin x \quad \text{...(1)}$$
$$e^{-xi} = \cos x - i\sin x \quad \text{...(2)}$$

### Complex Cosine

From (1) + (2):
$$e^{xi} + e^{-xi} = 2\cos x \implies \cos x = \frac{1}{2}\{e^{xi} + e^{-xi}\}$$

Evaluate the cosine of a complex number $z = a + bi$:
$$\cos z = \frac{1}{2}\{e^{zi} + e^{-zi}\}$$

Expanding and grouping real and imaginary parts:
$$\text{Re}(\cos z) = \frac{1}{2}\cos a\left(e^{-b} + e^b\right)$$
$$\text{Im}(\cos z) = \frac{1}{2}\sin a\left(e^{-b} - e^b\right)$$

### Complex Sine

From (1) − (2):
$$e^{xi} - e^{-xi} = 2i\sin x \implies \sin x = \frac{1}{2i}\{e^{xi} - e^{-xi}\}$$

Evaluate the sine of a complex number $z = a + bi$:
$$\sin z = \frac{1}{2i}\{e^{zi} - e^{-zi}\}$$

After rationalising (multiplying by $\frac{i}{i}$) to ensure a standard complex number form:
$$\text{Re}(\sin z) = \frac{1}{2}\sin a\left(e^{-b} - e^b\right)$$
$$\text{Im}(\sin z) = -\frac{1}{2}\cos a\left(e^{-b} + e^b\right)$$

## Complex Logarithm Function

The logarithm function is the inverse of the exponential function.

Due to $e^z$ being a periodic function:
$$e^z = e^{z + 2\pi ki} \quad ; \; k \in \mathbb{Z}$$

An equation $f(z) = e^z$ has infinitely many solutions, so the complex logarithm $\ln(z)$ is a **multi-valued function**.

Let the Euler form of a complex number be $z = |z|e^{\arg(z)\,i}$. Then:
$$\ln(z) = \ln|z| + \big((\arg(z) + 2\pi k)i\big) \quad ; \; k \in \mathbb{Z}$$

### Principal Complex Logarithm

If $k = 0$:
$$\text{Ln}(z) = \ln|z| + (\arg(z))i$$

### Summary
1. **General complex logarithm:** $\ln(z) = \ln|z| + \big((\arg(z) + 2\pi k)i\big)$ ; $k \in \mathbb{Z}$
2. **Principal complex logarithm:** $\text{Ln}(z) = \ln|z| + (\arg(z))i$

## Examples from Lecture

### n-th Roots
**Example 1.0**
- a) Find the square roots of $1 + i$
- b) Find the cube roots of $-\sqrt{3} - i$
- c) Find the fourth roots of $-8i$

**Example 2.0**  
Suppose $1 + i$ is a root of $z^5 + 12(1-i)z^4 + a + bi = 0$ for $z \in \mathbb{C}$ where $a$ and $b$ are constants. Find $a$ and $b$.

**Example 3.0**  
Find the Cartesian form of $(1 - \sqrt{3}\,i)^7 + (-1 - i)^5$.

**Example 4.0**  
Let $w_1, w_2, w_3, \ldots, w_n$ be all the $n$-th roots of a non-zero complex number $z$. Determine $w_1 w_2 w_3 \cdots w_n$.

### Complex Exponential
**Example 5.0**
1. Determine the Cartesian form of:
   - a) $e^{2+3i}$
   - b) $e^{i}$
2. Find the exact Cartesian form of $e^{-1 + \frac{\pi}{3}i}$.

**Example 6.0**  
Find the complex number $z$ satisfying:
- a) $e^z = 2i$
- b) $e^z = 1 + i$
- c) $e^z = -2$
- d) $e^z = -\sqrt{3} - \sqrt{3}\,i$

### Complex Trigonometric
**Example 7.0**  
Evaluate:
- a) $\cos(2 - 2i)$
- b) $\sin\big(e^{\frac{\pi}{3}i}\big)$

### Complex Logarithm
**Example 8.0**  
Find $\ln(z)$ and $\text{Ln}(z)$ when:
- a) $z = 2e^{-\frac{\pi}{3}i}$
- b) $z = 5 + 5i$
- c) $z = -\sqrt{3} - i$

**Example 9.0**  
Find the complex number $z$ satisfying $\ln(z^2 - 4) = \ln 2 + \pi i$.

## Summary

This lecture extends complex number operations to:
- Finding n-th roots using De Moivre's theorem and coterminal angles
- Evaluating the complex exponential function $e^z$ and understanding its periodic nature
- Defining complex sine and cosine functions via exponential forms
- Understanding the multi-valued complex logarithm $\ln(z)$ and its principal value $\text{Ln}(z)$

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Complex Numbers]] — concept page
- [[FAC1004 L02 — Euler's Formula]] — previous lecture
- [[FAC1004 L7-L8 — Complex Equations (Geometric Interpretation)]] — next lecture

## Source File

`LECTURE_NOTES_2526/[L5 L6] FUNCTIONS OF COMPLEX NUMBERS.pdf`
