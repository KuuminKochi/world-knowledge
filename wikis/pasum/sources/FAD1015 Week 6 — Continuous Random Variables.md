---
title: "FAD1015 Week 6 — Continuous Random Variables"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1015
  - topic/random-variables
  - status/evergreen
week: 6
lectures:
  - LEC 11: Cumulative Distribution Function of Continuous Random Variable
  - LEC 12: Mean and Variance for Continuous Random Variable
---

# FAD1015 Week 6 — Continuous Random Variables

Week 6 lecture covering the cumulative distribution function (CDF), expectation, and variance for continuous random variables. The lecture consists of two parts: **LEC 11** focuses on the CDF and its properties, while **LEC 12** develops mean and variance for continuous cases. Source file: `FAD1015 Week 6 cont-mean-var.pdf` (28 slides).

## Summary

This lecture extends random variable concepts to the continuous case. LEC 11 defines the cumulative distribution function $F(x)$, establishes its key properties, and demonstrates how to move between the probability density function $f(x)$ and the CDF via integration and differentiation. LEC 12 defines the expected value $E(X)$ and variance $\text{Var}(X)$ for continuous random variables, develops the expectation of a function $E[g(X)]$, and states the fundamental rules for linear transformations of random variables.

## Key Concepts

- [[Probability Distributions]] — Continuous random variables (general theory)
- Cumulative Distribution Function (CDF)
- Probability Density Function (PDF)
- Expected Value / Mean of a Continuous Random Variable
- Variance and Standard Deviation of a Continuous Random Variable
- Expectation of a Function $g(X)$
- Rules for $E[aX + b]$ and $\text{Var}(aX + b)$

---

## LEC 11: Cumulative Distribution Function

### Definition

If $X$ is a continuous random variable with probability density function $f(x)$, the **cumulative distribution function** $F(t)$ is defined as:

$$F(t) = P(X \leq t) = \int_{-\infty}^{t} f(x)\,dx$$

### Properties of the CDF

1. **Boundary values:** If the domain of $X$ is $x_0 \leq x \leq x_1$, then $F(x_0) = 0$ and $F(x_1) = 1$.

2. **Interval probability:** For any $a, b$ in the domain,
   $$P(a \leq X \leq b) = P(a \leq X < b) = P(a < X \leq b) = P(a < X < b) = \int_a^b f(x)\,dx = F(b) - F(a)$$
   *(All inequalities are equivalent because $P(X = x) = 0$ for a continuous random variable.)*

3. **Median:** The median $m$ bisects the distribution such that $X$ is equally likely to be smaller or larger than $m$:
   $$F(m) = \int_{x_0}^{m} f(x)\,dx = \int_{m}^{x_1} f(x)\,dx = \frac{1}{2}$$

4. **PDF from CDF:** Differentiating the CDF recovers the PDF:
   $$\frac{d}{dx}F(x) = f(x)$$

### Worked Examples

The lecture presents six examples progressing in complexity:

- **Example 1:** $f(x) = \dfrac{6 - 2x}{9}$ for $0 \leq x \leq 3$. Find $F(x)$, $P(X \leq 1.3)$, $P(1 \leq X \leq 2)$, and the median.
- **Example 2:** $f(x) = ax - 3x^2$ for $0 \leq x \leq 2$. Find the constant $a$ and $F(x)$.
- **Example 3:** $f(x) = \dfrac{3}{8}(1 + x^2)$ for $-1 \leq x \leq 1$. Find $F(x)$ and the median.
- **Example 4:** Piecewise PDF: $f(x) = \dfrac{x}{25}$ ($0 \leq x < 5$) and $f(x) = \dfrac{2}{5} - \dfrac{x}{25}$ ($5 \leq x \leq 10$). Sketch, find $F(x)$, and compute several interval probabilities.
- **Example 5:** CDF given as $F(x) = \dfrac{x^2}{k}$ ($0 \leq x < 2$). Find $k$, the median, and $f(x)$.
- **Example 6:** Piecewise CDF: $F(x) = \dfrac{x^2}{48}$ ($0 \leq x < 4$) and $F(x) = -\dfrac{1}{2} + \dfrac{x}{4} - \dfrac{x^2}{96}$ ($4 \leq x < 12$). Compute probabilities, find $f(x)$, sketch $f(x)$ to find the mode, and find the median.

---

## LEC 12: Mean and Variance for Continuous Random Variables

### Expectation of $X$

For a continuous random variable $X$ with PDF $f(x)$, the **mean** (or **expectation**) is:

$$\mu = E(X) = \int_{\text{all }x} x\,f(x)\,dx$$

### Expectation of a Function $g(X)$

If $g(X)$ is a function of the random variable, then:

$$E[g(X)] = \int_{-\infty}^{\infty} g(x)\,f(x)\,dx$$

A frequently used case is $g(X) = X^2$:

$$E(X^2) = \int_{-\infty}^{\infty} x^2\,f(x)\,dx$$

### Rules for the Expectation of $g(X)$

For constants $a$ and $b$:

1. $E(a) = a$
2. $E(aX) = a\,E(X)$
3. $E(aX + b) = a\,E(X) + b$

### Variance of $X$

$$\text{Var}(X) = \sigma^2 = \int_{\text{all }x} (x - \mu)^2\,f(x)\,dx$$

**Computational forms:**

$$\text{Var}(X) = \int_{\text{all }x} x^2\,f(x)\,dx - \mu^2$$

$$\text{Var}(X) = E(X^2) - [E(X)]^2$$

**Standard deviation:**

$$\sigma = \sqrt{\text{Var}(X)}$$

### Rules for the Variance of $g(X)$

For constants $a$ and $b$:

1. $\text{Var}(a) = 0$
2. $\text{Var}(aX) = a^2\,\text{Var}(X)$
3. $\text{Var}(aX + b) = a^2\,\text{Var}(X)$ *(adding a constant does not affect spread)*

### Worked Examples

- **Example 7:** $f(x) = \dfrac{1}{18}(6 - x)$ for $0 \leq x \leq 6$. Find $E(X)$.
- **Example 8:** Car-park stay time with $f(x) = kx^{-3/2}$ for $1 \leq x \leq 9$. Interpret the domain, show $k = \dfrac{3}{4}$, and calculate the mean stay.
- **Example 9:** Prove $E(aX + b) = aE(X) + b$ from the definition.
- **Example 10:** $f(x) = 3(1 - x)^2$ for $0 \leq x \leq 1$. Find the mean, variance, standard deviation, $E(3X + 2)$, and $\text{Var}(3X + 2)$.
- **Example 11:** Piecewise PDF: $f(x) = \dfrac{1}{4}$ ($0 \leq x < 2$) and $f(x) = \dfrac{x}{2} - \dfrac{3}{4}$ ($2 \leq x < 3$). Find $E(X)$, $\text{Var}(X)$, $\sigma$, $E(5X - 2)$, and $\text{Var}(5X - 2)$.
- **Example 12:** Re-uses the CDF from Example 6. Find $E(X)$, $\text{Var}(X)$, $\sigma_X$, $E(Y)$ if $Y = 2X - 1$, $\text{Var}(Y)$ if $Y = 4X + 1$, and the standard deviation of $Y$, $\sigma_Y$.

---

## Past Exam Questions (Tutorial / Revision)

The final slides list past-year examination titles only; the actual question text is not shown in the lecture slides:

- **Question 4 (2016/2017)**
- **Question 5 (2016/2017)**
- **Question 6.a (2016/2017)**
- **Question 1.b (2015/2016)**
- **Question 2 (2015/2016)**

---

## Related Topics

- [[FAD1015 Week 5 — Mean & Variance (Discrete & Continuous)]] — prerequisite moments and introduction to continuous mean/variance
- [[FAD1015 Week 4 — Discrete Random Variables (PDF & CDF)]] — discrete counterparts
- [[FAD1015 L15-L16 — Normal Distribution & Approximation]] — specific continuous distribution
- [[FAD1015 L17-L18 — Uniform & Exponential Distributions + R Intro]] — specific continuous distributions
- [[FAD1015 Tutorial 1-6 — Counting & Probability Fundamentals]] — practice problems

## Related Course Page

- [[FAD1015 - Mathematics III]]
