---
title: Summation Formulas
date: 2026-04-28
tags:
  - concept
  - subject/mathematics
  - topic/series
  - topic/summation
  - status/seedling
aliases:
  - Finite Series
  - Sigma Notation
---

# Summation Formulas

Standard formulas for evaluating finite sums of polynomial sequences. These formulas are essential for calculating sums efficiently without computing each term individually.

## Sigma Notation

Summation notation provides a compact way to represent the sum of a sequence:

$$\sum_{r=1}^{n} a_r = a_1 + a_2 + a_3 + \ldots + a_n$$

Where:
- $r$ is the index of summation
- $1$ is the lower limit
- $n$ is the upper limit
- $a_r$ is the general term

## Standard Formulas

### Sum of First n Natural Numbers (Arithmetic Series)

$$\sum_{r=1}^{n} r = 1 + 2 + 3 + \ldots + n = \frac{n(n+1)}{2}$$

**Proof by induction** or by pairing terms (Gauss's method): 
$1 + n = 2 + (n-1) = 3 + (n-2) = \ldots = n+1$, with $n/2$ such pairs.

### Sum of Squares

$$\sum_{r=1}^{n} r^2 = 1^2 + 2^2 + 3^2 + \ldots + n^2 = \frac{n(n+1)(2n+1)}{6}$$

### Sum of Cubes

$$\sum_{r=1}^{n} r^3 = 1^3 + 2^3 + 3^3 + \ldots + n^3 = \frac{n^2(n+1)^2}{4}$$

> [!important] Special Property
> The sum of cubes equals the **square** of the sum of the first $n$ natural numbers:
> $$\sum_{r=1}^{n} r^3 = \left(\sum_{r=1}^{n} r\right)^2 = \left[\frac{n(n+1)}{2}\right]^2$$

## Properties of Summation

### Linearity

$$\sum_{r=1}^{n} (ca_r + db_r) = c\sum_{r=1}^{n} a_r + d\sum_{r=1}^{n} b_r$$

### Change of Index

$$\sum_{r=m}^{n} a_r = \sum_{r=1}^{n} a_r - \sum_{r=1}^{m-1} a_r$$

## Worked Examples

### Example 1: Basic Application

Find $\sum_{r=1}^{10} r$:
$$\sum_{r=1}^{10} r = \frac{10(11)}{2} = 55$$

### Example 2: Expanded Polynomial

Find $\sum_{r=1}^{10} (r+7)(r-1)$:

First expand: $(r+7)(r-1) = r^2 + 6r - 7$

Then apply linearity:
$$\sum_{r=1}^{10} (r^2 + 6r - 7) = \sum r^2 + 6\sum r - \sum 7$$
$$= \frac{10(11)(21)}{6} + 6 \cdot \frac{10(11)}{2} - 7(10)$$
$$= 385 + 330 - 70 = 645$$

### Example 3: Sum of Odd Squares

Find $1^2 + 3^2 + 5^2 + \ldots$ to 20 terms.

The $r$-th odd number is $2r-1$, so we need:
$$\sum_{r=1}^{20} (2r-1)^2 = \sum_{r=1}^{20} (4r^2 - 4r + 1)$$
$$= 4\sum r^2 - 4\sum r + \sum 1$$
$$= 4 \cdot \frac{20(21)(41)}{6} - 4 \cdot \frac{20(21)}{2} + 20$$

## Related

- [[Method of Differences]] — for non-polynomial series
- [[Power Series — Taylor & Maclaurin]] — infinite series expansions
- [[Binomial Expansion]] — another type of series expansion
- [[FAD1014 L22 — Finite Series and Summation]] — lecture source
