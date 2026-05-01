---
title: "FAD1015 Tutorial 6 — Expected Value, Variance, and Continuous Random Variables"
date: 2025-2026
course: FAD1015 Mathematics III
tags:
  - fad1015
  - mathematics
  - expected-value
  - variance
  - continuous-random-variable
  - pdf
  - cdf
---

# FAD1015: Mathematics III — Tutorial 6

**Centre for Foundation Studies in Science**  
**Universiti Malaya**  
**Session 2025/2026**

---

## Topic: Discrete Random Variables — Expected Value, Mode, Median and Variance

### Question 1
Prove that $E(aX + b) = aE(X) + b$.

### Question 2
Prove that $Var(aX + b) = a^2 Var(X)$.

### Question 3
The discrete random variable X has the cumulative distribution function as following:

$$F(x) = \begin{cases} 0, & x < 0.1 \\ 0.05, & 0.1 \leq x < 0.2 \\ 0.3, & 0.2 \leq x < 0.3 \\ 0.6, & 0.3 \leq x < 0.4 \\ 0.75, & 0.4 \leq x < 0.5 \\ 1, & x \geq 0.5 \end{cases}$$

(a) Estimate the median of $X$.

(b) Find the probability distribution of $X$.

(c) Find the mode of $X$.

(d) Calculate $E(X)$.

(e) Calculate $Var(X)$.

(f) Calculate $E(Y)$ and $Var(Y)$ where $Y = 2X - 7$.

### Question 4
A class consists of 7 girls and 5 boys. Three students from the class are chosen at random to represent the class. The number of boys chosen is denoted by the random variable X.

(a) Find the probability distribution function of $X$.

(b) Calculate $E(X)$.

(c) Find $P(X > E(X))$

(d) Calculate the variance of $X$.

### Question 5
The discrete random variable X has the probability distribution given by the following, where $k$ is a constant.

$$P(X = x) = \begin{cases} \frac{kx}{(x^2+1)} & x = 2, 3 \\ \frac{2kx}{(x^2-1)} & x = 4, 5 \end{cases}$$

(a) Show that $k = \frac{20}{33}$.

(b) Find the probability that $X$ is less than 3 or greater than 4.

(c) Find $E(X)$.

(d) Find $Var(X - 2)$.

(e) Find the cumulative distribution function of $X$.

### Question 6
The number of spelling mistakes, X, that Lily makes when writing an essay can be modelled by the following probability distribution.

| $X = x$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $P(X = x)$ | 0.23 | 0.31 | 0.27 | 0.14 | 0.05 |

The mean number of spelling mistakes is $\mu$ and the standard deviation is $\sigma$.

(a) Find the values of $\mu$ and $\sigma$.

(b) Find $P(X > \mu + \sigma)$.

(c) Find the mode and median of $X$.

### Question 7
The discrete random variable $X$ has the cumulative distribution given by the following:

$$F(y) = 1 - (1 - \frac{y}{4})^y, \quad y = 1, 2, 3, 4$$

(a) Estimate the median of $X$.

(b) Find $E(X)$.

(c) Find $Var(3X)$.

---

## Topic: Continuous Random Variables — Probability Distribution Function (pdf)

### Question 1
State differences between discrete and continuous random variables. Give each two examples representing both variables.

### Question 2
Determine if the following functions are density function or otherwise:

(a) $f(x) = \begin{cases} 3(1 - x)^2 & 0 < x < 1 \\ 0 & \text{otherwise} \end{cases}$

(b) $f(x) = \begin{cases} \frac{x(1-x)^2}{16} & 0 \leq x \leq 4 \\ 0 & \text{otherwise} \end{cases}$

### Question 3
The random variable $X$ has probability density function given by:

$$f(x) = \begin{cases} a(b - x) & 0 \leq x \leq b \\ 0 & \text{otherwise} \end{cases}$$

(a) Show that $a = \frac{2}{b^2}$.

(b) Given that $a = \frac{1}{8}$, find $P(\frac{1}{2} \leq x \leq 3)$.

### Question 4
Let $X$ be the weight difference for 2-month-old baby (compared to weight at birth and recorded in kilograms) with probability density function given by:

$$f(x) = \begin{cases} a(x^2 - 10x) & 0 \leq x \leq 3 \\ 0 & \text{otherwise} \end{cases}$$

where $a$ is a constant.

(a) Find the value of $a$.

(b) Find the cumulative distribution function $F(x)$.

(c) Calculate:

&emsp;i. the probability that a randomly selected baby has weight difference of 0 to 1 kg

&emsp;ii. the probability that a randomly selected baby has weight difference more than 1 kg.

---

## Related Concepts

- [[Expected Value]] — long-run average value of a random variable
- [[Variance]] — measure of spread/dispersion
- [[Standard Deviation]] — square root of variance
- [[Mode]] — most frequent value
- [[Median]] — middle value
- [[Continuous Random Variable]] — random variable that can take any value in a range
- [[Probability Density Function]] — pdf for continuous random variables

---

*Source: FAD1015 Questions T1-T6 _20252026.pdf*
