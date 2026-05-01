---
title: "FAD1014 L22 — Finite Series and Summation"
date: 2026-04-28
tags:
  - source/lecture
  - subject/mathematics
  - topic/series
  - topic/summation
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
lecturer: "[[Dr Norshahirah]]"
---

# FAD1014 L22 — Finite Series and Summation

Lecture covering standard summation formulas for finite series and the method of differences for telescoping series.

## Key Points

- Standard formulas for summing arithmetic sequences, squares, and cubes
- Method of differences for series that telescope
- Partial fractions technique for setting up telescoping series

## Standard Summation Formulas

### Sum of First n Natural Numbers

$$\sum_{r=1}^{n} r = 1 + 2 + 3 + \ldots + (n-1) + n = \frac{1}{2}n(n+1)$$

### Sum of Squares

$$\sum_{r=1}^{n} r^2 = 1^2 + 2^2 + 3^2 + \ldots + n^2 = \frac{1}{6}n(n+1)(2n+1)$$

### Sum of Cubes

$$\sum_{r=1}^{n} r^3 = 1^3 + 2^3 + 3^3 + \ldots + n^3 = \frac{1}{4}n^2(n+1)^2$$

> [!note] Relationship
> The sum of cubes equals the square of the sum of first $n$ natural numbers: $\sum r^3 = \left(\sum r\right)^2$

## Examples

### Example 1: Basic Summation

a) $$\sum_{i=1}^{10} i = \frac{1}{2}(10)(11) = 55$$

b) $$\sum_{r=1}^{10} (r+7)(r-1) = \sum_{r=1}^{10} (r^2 + 6r - 7) = 385 + 330 - 70 = 645$$

### Example 2: Special Series

a) Sum of $1^2 + 3^2 + 5^2 + \ldots$ to 20 terms (odd squares)

b) Sum of $1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 + \ldots$ to $n$ terms

### Example 3: Variable Limits

Evaluate:
a) $\sum_{r=1}^{n+1} (2r+1)$
b) $\sum_{r=0}^{n+1} (2r+1)$
c) $\sum_{r=n}^{2n} (2r+1)$

## Method of Differences

If $a_k$ can be expressed as $f(k) - f(k-1)$, then:

$$\sum_{k=1}^{n} a_k = \sum_{k=1}^{n} [f(k) - f(k-1)] = f(n) - f(0)$$

This creates a **telescoping series** where intermediate terms cancel out.

### Example Using Partial Fractions

$$\frac{1}{(k+1)(k+2)} = \frac{1}{k+1} - \frac{1}{k+2}$$

Therefore:
$$\sum_{k=1}^{n} \frac{1}{(k+1)(k+2)} = \frac{n}{2(n+2)}$$

## Links

- [[Summation Formulas]] — detailed formulas and derivations
- [[Method of Differences]] — telescoping series technique
- [[FAD1014 - Mathematics II]]
