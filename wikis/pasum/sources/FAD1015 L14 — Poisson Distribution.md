---
title: "FAD1015 L14 — Poisson Distribution"
date: 2026-04-29
tags:
  - source/lecture
  - course/FAD1015
  - topic/poisson-distribution
  - status/evergreen
week: 7
---

# FAD1015 L14 — Poisson Distribution

Lecture 14 covering the Poisson distribution for modeling rare events. Source file: `Week 7 L14 Poisson Distribution.pdf`

## Summary

Study of the Poisson distribution: setting/characteristics, probability mass function, Poisson distribution tables, mean, variance, and use as an approximation to the binomial distribution.

## Key Concepts

- [[Probability Distributions]] — Poisson distribution
- Poisson Process — events occurring at constant rate over an interval
- Rate Parameter (λ) — average occurrences per interval
- Poisson Probability Formula
- Mean = Variance = λ
- Poisson Approximation to Binomial

## Lecture Coverage

### 1. Poisson Setting / Characteristics

The following conditions must be satisfied to apply the Poisson probability distribution:

1. **X is a discrete random variable**
2. **X is the number of occurrences of an event over some interval** (time, distance, area, volume)
3. **The occurrences must be random** — occurrences do not follow any pattern; they are unpredictable
4. **The occurrences must be independent of each other** — one occurrence (or non-occurrence) does not influence successive occurrences

**Examples:**
- Number of patients arriving at the emergency ward during a one-hour interval
- Number of defective items in the next 100 items manufactured
- Number of accidents on a highway during a one-week period
- Number of customers coming to a grocery store during a one-hour interval
- Number of television sets sold during a given week

### 2. Differences from Binomial Distribution

| Feature | Binomial | Poisson |
|---|---|---|
| Parameters | Sample size $n$ and probability $p$ | Mean $\lambda$ only |
| Possible values | $0, 1, 2, \ldots, n$ | $0, 1, 2, \ldots$ (no upper limit) |

### 3. Probability Mass Function

If a random variable $X$ has a Poisson probability distribution with parameter $\lambda$, then:

$$X \sim P_o(\lambda)$$

$$P(X = x) = \frac{\lambda^x e^{-\lambda}}{x!}$$

where:
- $x =$ number of occurrences $= 0, 1, 2, \ldots$
- $\lambda =$ mean number of occurrences in an interval; $\lambda > 0$
- $e \approx 2.71828$

**Key properties:**
- The Poisson distribution deals with the frequency of an event in a specific interval
- The probability of an event occurring is proportional to the size of the interval
- No upper limit on the number of events

### 4. Using the Poisson Table

Cumulative probabilities are calculated as:

$$P(X \geq r) = P(X = r) + P(X = r+1) + P(X = r+2) + \ldots + P(X = n)$$

Tables provide cumulative upper-tail probabilities for given $m = \lambda$ and $r$ values.

### 5. Mean and Variance

If $X \sim P_o(\lambda)$, then:

- **Mean:** $\mu = \lambda$
- **Variance:** $\sigma^2 = \lambda$
- **Standard Deviation:** $\sigma = \sqrt{\lambda}$

The mean and variance of the Poisson distribution are both equal to the parameter $\lambda$ itself.

### 6. Poisson Approximation to the Binomial Distribution

The binomial distribution tends toward the Poisson distribution when $n \to \infty$, $p \to 0$, and $\lambda = np$ stays constant.

When $n$ is large and $p$ is very small, the binomial distribution can be approximated by a Poisson distribution.

**Rule of thumb:**
- If $n > 20$ and $np < 5$ **OR** $nq < 5$, then Poisson is a good approximation

**New parameter:** $\lambda = np$

### 7. Worked Examples

**Example 1 — Using the Formula**
A car breaks down an average of three times per month. Find the probability that during the next month, this car will have:
a) Exactly two breakdowns
b) At most one breakdown

**Example 2 — Using the Poisson Table**
For $X \sim P_o(3)$:
a) $P(X = 2)$
b) $P(X \leq 1)$

**Example 3 — Mean and Variance**
A car breaks down an average of three times per month. Find the mean and variance of the distribution.

**Example 4 — LAZADA Returns**
LAZADA provides free examination for seven days. On average, 2 of every 10 products sold are returned. Find the probability that:
a) Exactly 6 of 40 products sold are returned
b) Exactly 3 of 25 products sold are returned
c) Less than 5 of 60 products sold are returned
d) More than 1 of 5 products sold are returned

**Example 5 — Rate Adjustment**
The number of calls arriving at a switchboard each hour is 180. Determine the probability that in a randomly chosen minute, the number of calls is:
a) Less than 6
b) More than 2
c) More than 2, given less than 6 arrivals

**Example 6 — Poisson Approximation**
The probability of any one letter being delivered to the wrong house is 0.03. On a random day Mr Postman delivers 100 letters. Using a Poisson approximation, find the probability that at least 4 letters are delivered to the wrong house.

**Example 7 — Poisson Approximation (Large n, small q)**
Let $X \sim B(60, 0.95)$. Use the Poisson approximation to find:
a) $P(X = 50)$
b) $P(X \geq 44)$

### 8. Exercises

**Exercise 1**
If $X \sim P_o(1.8)$, find the following probabilities by using the formula and the Poisson distribution table (round to four decimal places):
a) $P(X = 1)$
b) $P(X \geq 2)$
c) $P(X < 1)$
d) $P(X \leq 1)$
e) $P(X > 3)$
f) $P(0 < X < 3)$
g) $P(2 \leq X \leq 4)$
h) $P(0 \leq X < 2)$

**Exercise 2**
Yummy expected to receive 4 emails in a week. Find the probability of receiving:
a) No emails this week
b) 3 emails at most this week
c) 8 emails for the next 2 weeks
Use the formula and the Poisson distribution table. Round to four significant figures.

**Exercise 3**
A rental car service company has 5 cars available each day. The number of cars rented out each day is randomly distributed with a mean of 2. Find the probability that the company cannot meet the demand for cars on any one day. Round to four decimal places.

**Exercise 4**
The number of accidents at a junction in Jalan Duta, Kuala Lumpur averages four per week. Calculate the probability that the number of accidents is:
a) At most one over a period of one week
b) Exactly three over a fortnight
c) Zero over a period of three weeks
d) Exactly five in a month
Round to four decimal places.

**Exercise 5**
If $X \sim P_o(\beta)$ and $P(X = 0) = 0.0005$, find:
a) The value of $\beta$
b) $P(X = 7)$

**Exercise 6**
If $X$ is a discrete random variable with mean $\lambda$ and $P(X = 0) = 0.0302$, find:
a) The value of $\lambda$
b) $P(X = 4)$

**Exercise 7**
$X$ is a discrete Poisson random variable with parameter $\lambda = 3.5$. Find the probabilities:
a) $P(X = 2)$
b) $P(X < 3)$
c) $P(X = 2 \mid X < 3)$
Round to four decimal places.

## Related Topics

- [[FAD1015 L13 — Binomial Distribution]] — related distribution and approximation source
- [[FAD1015 L15-L16 — Normal Distribution & Approximation]] — another approximation
- [[FAD1015 Tutorial 1-6 — Counting & Probability Fundamentals]] — practice problems

## Related Course Page

- [[FAD1015 - Mathematics III]]
