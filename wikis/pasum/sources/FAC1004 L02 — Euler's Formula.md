---
title: FAC1004 L02 — Euler's Formula
date: 2026-04-28
tags:
  - source/lecture
  - subject/mathematics
  - topic/complex-numbers
  - topic/euler-formula
  - topic/exponential-form
  - status/seedling
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L02 — Euler's Formula

This lecture introduces Euler's formula, which connects the exponential function with trigonometric functions in the complex plane. It covers conversion between Cartesian and exponential forms, and efficient multiplication/division of complex numbers in exponential form.

## Key Concepts

- **Euler's Formula** — $re^{i\theta} = r(\cos\theta + i\sin\theta)$
- **Euler's Identity** — $e^{i\pi} + 1 = 0$ (special case when $r=1$, $\theta=\pi$)
- **Exponential Form** — $z = re^{i\theta}$ where $r = |z|$ and $\theta = \arg(z)$
- **Multiplication in Exponential Form** — $z_1 \cdot z_2 = r_1r_2e^{i(\theta_1 + \theta_2)}$
- **Division in Exponential Form** — $\frac{z_1}{z_2} = \frac{r_1}{r_2}e^{i(\theta_1 - \theta_2)}$

## Euler's Formula / Identity

$$re^{i\theta} = r(\cos\theta + i\sin\theta)$$

When $r = 1$ and $\theta = \pi$:

$$e^{i\pi} = \cos\pi + i\sin\pi = -1 + 0$$

$$e^{i\pi} + 1 = 0 \quad \text{(GOAT identity)}$$

## Converting Cartesian to Exponential Form

To express $z = a + bi$ in exponential form $z = re^{i\theta}$:
1. Compute modulus: $r = |z| = \sqrt{a^2 + b^2}$
2. Compute argument: $\theta = \arg(z)$ (consider quadrant)

### Examples

**Example 1:** Express $z = 1 + i$ in exponential form.
- $r = \sqrt{1^2 + 1^2} = \sqrt{2}$
- $\theta = \tan^{-1}(1) = \frac{\pi}{4}$ (first quadrant)
- $z = \sqrt{2}e^{i\pi/4}$

**Example 2:** Write $z = 1 - \sqrt{3}i$ in exponential form.
- $r = \sqrt{1^2 + (\sqrt{3})^2} = \sqrt{1 + 3} = 2$
- $\theta = \tan^{-1}\left(\frac{-\sqrt{3}}{1}\right) = -\frac{\pi}{3}$ (fourth quadrant)
- $z = 2e^{-i\pi/3}$

## Converting Exponential to Cartesian Form

Given $z = re^{i\theta}$, use Euler's formula:
$$z = r(\cos\theta + i\sin\theta) = r\cos\theta + ir\sin\theta$$

So:
- $\text{Re}(z) = r\cos\theta$
- $\text{Im}(z) = r\sin\theta$

### Examples

**Example 3:** Determine $\text{Re}(z)$ and $\text{Im}(z)$ for $z = 3e^{-\frac{5\pi}{6}i}$.
- $\text{Re}(z) = 3\cos\left(-\frac{5\pi}{6}\right) = 3 \cdot \left(-\frac{\sqrt{3}}{2}\right) = -\frac{3\sqrt{3}}{2}$
- $\text{Im}(z) = 3\sin\left(-\frac{5\pi}{6}\right) = 3 \cdot \left(-\frac{1}{2}\right) = -\frac{3}{2}$

## Finding Modulus and Argument from Exponential Form

For $z = re^{i\theta}$:
- Modulus: $|z| = r$
- Argument: $\arg(z) = \theta$

If the exponent has a real component, use $e^{a+bi} = e^a \cdot e^{bi}$, so:
- $z = e^{a+bi} = e^a e^{bi} \implies |z| = e^a$, $\arg(z) = b$

### Examples

**Example 4:** Determine modulus and argument for $z = e^{i}$.
- $|z| = 1$, $\arg(z) = 1$ radian

**Example 5:** Determine modulus and argument for $z = 5e^{0.3i}$.
- $|z| = 5$, $\arg(z) = 0.3$ radians

**Example 6:** Determine modulus and argument for $z = 3e^{2i}$.
- $|z| = 3$, $\arg(z) = 2$ radians

**Example 7:** Determine modulus and argument for $z = e^{2+\frac{\pi}{3}i}$.
- $z = e^2 \cdot e^{\frac{\pi}{3}i}$
- $|z| = e^2$, $\arg(z) = \frac{\pi}{3}$

**Example 8:** Determine modulus and argument for $z = 3e^{2-\frac{2\pi}{3}i}$.
- $z = 3e^2 \cdot e^{-\frac{2\pi}{3}i}$
- $|z| = 3e^2$, $\arg(z) = -\frac{2\pi}{3}$

## Multiplying and Dividing in Exponential Form

### Multiplication
When multiplying complex numbers in exponential form, **multiply the moduli** and **add the arguments**:

$$z_1 \cdot z_2 = r_1e^{i\theta_1} \cdot r_2e^{i\theta_2} = r_1r_2e^{i(\theta_1 + \theta_2)}$$

**Example 9:** Given $z_1 = 3e^{\frac{2\pi}{3}i}$ and $z_2 = 3e^{-\frac{5\pi}{6}i}$.
$$z_1 \times z_2 = 3 \cdot 3 \cdot e^{i\left(\frac{2\pi}{3} - \frac{5\pi}{6}\right)} = 9e^{i\left(\frac{4\pi - 5\pi}{6}\right)} = 9e^{-\frac{\pi}{6}i}$$

### Division
When dividing complex numbers in exponential form, **divide the moduli** and **subtract the arguments**:

$$\frac{z_1}{z_2} = \frac{r_1e^{i\theta_1}}{r_2e^{i\theta_2}} = \frac{r_1}{r_2}e^{i(\theta_1 - \theta_2)}$$

**Example 10:** Using the same $z_1, z_2$:
$$z_1 \div z_2 = \frac{3}{3} \cdot e^{i\left(\frac{2\pi}{3} - \left(-\frac{5\pi}{6}\right)\right)} = e^{i\left(\frac{4\pi + 5\pi}{6}\right)} = e^{\frac{3\pi}{2}i}$$

## Combined Example

**Example 11:** Show that $e^{1+3i} = -2.707 + 0.3836i$.
$$e^{1+3i} = e^1 \cdot e^{3i} = e(\cos 3 + i\sin 3)$$
$$= e\cos 3 + ie\sin 3$$
$$\approx 2.718(-0.9900) + i(2.718)(0.1411)$$
$$\approx -2.707 + 0.3836i$$

**Example 12:** Let $z_1 = 2e^{-\frac{3\pi}{4}i}$ and $z_2 = \frac{3}{e^{\frac{2\pi}{3}i}} = 3e^{-\frac{2\pi}{3}i}$. Find:
1. $\arg(z_1z_2) = -\frac{3\pi}{4} + \left(-\frac{2\pi}{3}\right) = -\frac{9\pi + 8\pi}{12} = -\frac{17\pi}{12}$
2. $\arg\left(\frac{z_1}{z_2}\right) = -\frac{3\pi}{4} - \left(-\frac{2\pi}{3}\right) = -\frac{9\pi - 8\pi}{12} = -\frac{\pi}{12}$
3. $|z_1 + z_2|$ — convert both to Cartesian form, add, then find modulus

## Summary

Euler's formula provides a powerful connection between exponential functions and trigonometric functions in the complex plane. The exponential form $z = re^{i\theta}$ enables:
- Easy conversion between Cartesian and polar representations
- Efficient multiplication (multiply moduli, add arguments)
- Efficient division (divide moduli, subtract arguments)

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Complex Numbers]] — concept page
- [[FAC1004 L01 — Complex Numbers]] — previous lecture
- [[FAC1004 L5-L6 — Functions of Complex Numbers (n-th Roots)]] — next lecture

## Source File

`LECTURE_NOTES_2526/L02 - Euler_s Formula Student Version .pdf`
