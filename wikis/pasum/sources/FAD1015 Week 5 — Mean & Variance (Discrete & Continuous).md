---
title: "FAD1015 Week 5 — Mean & Variance (Discrete) & Continuous PDF Introduction"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1015
  - topic/random-variables
  - status/seedling
week: 5
lectures:
  - LEC 9: Discrete Random Variable — Expectation, Variance, Mode, Median
  - LEC 10: Continuous Random Variable — Probability Density Function
---

# FAD1015 Week 5 — Mean & Variance (Discrete) & Continuous PDF Introduction

Week 5 lecture covering moments of discrete random variables (mean, variance, mode, median) and introducing the probability density function for continuous random variables. Source file: `FAD1015 Week 5 mean-var discrete-continuous pdf.pdf` (35 pages, 19 examples).

> **Note on scope:** This lecture develops **mean and variance only for discrete** random variables. The continuous portion (LEC 10) defines the probability density function (PDF) and its properties but does **not** extend expectation or variance to the continuous case — those are covered in [[FAD1015 Week 6 — Continuous Random Variables|Week 6 (LEC 12)]].

---

## LEC 9: Discrete Random Variable

### 1. Expectation of $X$ ($E[X]$ or $\mu$)

The **expectation** (or **expected value** / **expected mean**) of a discrete random variable $X$ is the long-run mean you would expect from a very large number of observations.

**Definition:**
$$\mu = E(X) = \sum_{i=1}^{n} x_i \, p_i = \sum x \, P(X = x)$$

**Example — Fair die:**
$$E(X) = 1\left(\frac{1}{6}\right) + 2\left(\frac{1}{6}\right) + 3\left(\frac{1}{6}\right) + 4\left(\frac{1}{6}\right) + 5\left(\frac{1}{6}\right) + 6\left(\frac{1}{6}\right) = 3.5$$

---

### 2. Expectation of a Function $g(X)$

If $g(X)$ is a function of the random variable $X$:

$$E[g(X)] = \sum g(x) \, P(X = x)$$

A frequently used case is $g(X) = X^2$:

$$E(X^2) = \sum x^2 \, P(X = x)$$

---

### 3. Rules for Expectation

For constants $a$ and $b$:

1. $E(a) = a$
2. $E(aX) = a \, E(X)$
3. $E(aX + b) = a \, E(X) + b$

---

### 4. Variance of $X$ ($\text{Var}(X)$ or $\sigma^2$)

**Definition:**
$$\text{Var}(X) = \sigma^2 = \sum (x_i - \mu)^2 \, p_i = \sum (x - \mu)^2 \, P(X = x)$$

**Computational form (used in practice):**
$$\text{Var}(X) = E(X^2) - [E(X)]^2 = E(X^2) - \mu^2$$

where $E(X^2) = \sum x^2 \, P(X = x)$.

**Standard deviation:**
$$\sigma = \sqrt{\text{Var}(X)}$$

---

### 5. Rules for Variance

For constants $a$ and $b$:

1. $\text{Var}(a) = 0$
2. $\text{Var}(aX) = a^2 \, \text{Var}(X)$
3. $\text{Var}(aX + b) = a^2 \, \text{Var}(X)$

*(Adding a constant shifts the distribution but does not change its spread.)*

---

### 6. Mode and Median

- **Mode:** The value of $x$ with the **greatest probability**.
- **Median ($m$):** The value such that $P(X \leq m) = 0.5$, i.e. $F(m) = 0.5$.

---

### Worked Examples (Discrete)

| Example | Problem Statement |
|---------|-------------------|
| **Example 1** | Given $f(x) = \dfrac{x^2}{30}$ for $x = 0, 1, 2, 3, 4$. Find $E(X)$. |
| **Example 2** | Azie and Ratna play a dice game: win RM 6 on a '6', lose RM 1 otherwise. Find Azie’s expected gain/loss. |
| **Example 3** | Prove $E(aX + b) = aE(X) + b$ from the definition. |
| **Example 4** | Bicycle sales per week with given relative frequencies. Find $E(X)$ and the expected weekly profit $g(X) = 160X - 50$. |
| **Example 5** | Prove $\text{Var}(X) = E(X^2) - \mu^2$ from the definition. |
| **Example 6** | Prove $\text{Var}(aX + b) = a^2\,\text{Var}(X)$. |
| **Example 7** | $f(x) = \dfrac{x}{8}$ for $x = 1, 2, 5$; $0$ otherwise. Find $F(x)$, median, mode, $E(X)$, $E(Y)$, $\text{Var}(X)$, $\text{Var}(Y)$ for $Y = 3X + 5$. |
| **Example 8** | Distribution: $P(X=0)=0.1, P(X=1)=0.2, P(X=2)=0.4, P(X=3)=0.2, P(X=4)=0.1$. Find $F(x)$, median, mode, $E(Y)$ for $Y = X - 3$, and $P(X > E(X))$. |
| **Example 9** | $P(X=1)=0.3, P(X=2)=0.4, P(X=3)=0.3$. If $Y = 10X + 5$, find $E(Y)$, $\text{Var}(Y)$, $\sigma_X$, $\sigma_Y$. |
| **Example 10** | $P(Y=y) = \dfrac{ay}{8}$ for $y = 1, 2, 3, 4$. Find $a$, $E(Y)$, $\text{Var}(Y)$. |
| **Example 11** | Box of 10 dry cells (3 defective). Sample of 2 tested. Find distribution of $X$ (defectives), then $\mu$, $\sigma$, and $P(X < \mu + \sigma)$. |
| **Example 12** | Distribution: $P(X=0)=0.26, P(X=1)=k, P(X=2)=3k, P(X=3)=0.05, P(X=4)=0.09$. Find $k$, $E(X)$, $\text{Var}(X)$, $E(Y)$ and $\text{Var}(Y)$ for $Y = 2X - 7$. |
| **Example 13** | $P(X=x) = \dfrac{1}{6}$ for $x = 1, 5, 9$ and $\dfrac{1}{4}$ for $x = 3, 7$; $0$ otherwise. Find $E(X)$, $\text{Var}(X)$, $E(Y)$ and $\text{Var}(Y)$ for $Y = 3X - 2$. |

---

## LEC 10: Continuous Random Variable — Probability Density Function

### Definition and Properties

A **continuous random variable** cannot take precise values but can be defined only within a specified interval. It is associated with measurements such as time, mass, or length.

**Examples:** life-span of insects, weights of newborn babies, heights of 12-year-olds, distance from home to school.

The **probability density function** $f(x)$ has the following properties:

1. $f(x) \geq 0$ for all $x$.
2. The total area under the graph of $y = f(x)$ is $1$:
   $$\int_{-\infty}^{\infty} f(x)\,dx = 1$$
3. The probability that $X$ lies between $a$ and $b$ equals the area under $f(x)$ between $a$ and $b$:
   $$P(a \leq X \leq b) = \int_a^b f(x)\,dx$$

### Important Notes for Continuous Variables

$$P(a \leq X \leq b) = P(a \leq X < b) = P(a < X \leq b) = P(a < X < b)$$

and

$$P(X = a) = 0 = P(X = b)$$

For a continuous random variable $X$ with PDF $f(x)$ on $a \leq X \leq b$:

$$P(x_1 \leq X \leq x_2) = \int_{x_1}^{x_2} f(x)\,dx$$

$$\int_a^b f(x)\,dx = 1$$

*(Mean and variance for continuous random variables are **not** covered in this lecture; see [[FAD1015 Week 6 — Continuous Random Variables|Week 6]].)*

---

### Worked Examples (Continuous PDF)

| Example | Problem Statement |
|---------|-------------------|
| **Example 14** | Verify that the following are PDFs: (a) $f(x) = \dfrac{3}{4}(x^2 - x)$, $x \in [0,2]$; (b) $f(x) = 2e^{-2x}$, $x \in [0, \infty)$. |
| **Example 15** | $f(x) = \dfrac{1}{36}x(6 - x)$ for $0 \leq x \leq 6$. Calculate $P(2 \leq X \leq 3.5)$, $P(X < 3)$, $P(X = 3)$, $P(X > 5)$. |
| **Example 16** | $f(t) = \dfrac{k}{t^4}$ for $t \geq 1$; $0$ otherwise. Find $k$, then calculate $P(2.5 \leq T \leq 3.5)$, $P(T \leq 5)$, $P(3 < T \leq 7)$, $P(T = 4)$. |
| **Example 17** | Piecewise PDF: $f(x) = tx$ ($0 \leq x < 2$), $f(x) = 2t$ ($2 \leq x \leq 3$), $0$ otherwise. Find $t$, sketch $f(x)$, then compute several interval probabilities. |
| **Example 18** | Visibility hours at Mount Kinabalu: $f(x) = kx^2$ for $0 \leq x \leq 5$. Find $k$ and $P(2 \leq X \leq 3)$. |
| **Example 19** | Piecewise PDF: $f(x) = ax + 1$ ($0 \leq x < 1$), $f(x) = x + b$ ($1 \leq x < 2$), $0$ otherwise. Given $P(0 \leq X < 1) = \frac{1}{2}$, find $a$, $b$, and various probabilities. |

---

## Key Concepts

- [[Probability Distributions]] — Distribution moments and PDF properties
- Expected Value (Mean) — $E[X]$ or $\mu$
- Variance — $\text{Var}(X)$ or $\sigma^2$
- Standard Deviation — $\sigma$
- Properties of Expectation and Variance
- Linear transformations of random variables
- Mode and Median of a discrete distribution
- Probability Density Function (PDF) — continuous case

## Related Topics

- [[FAD1015 Week 4 — Discrete Random Variables (PDF & CDF)]] — prerequisite (discrete PDF/CDF)
- [[FAD1015 Week 6 — Continuous Random Variables]] — continuous CDF, mean, and variance (LEC 11–12)
- [[FAD1015 Tutorial 1-6 — Counting & Probability Fundamentals]] — practice problems

## Related Course Page

- [[FAD1015 - Mathematics III]]
