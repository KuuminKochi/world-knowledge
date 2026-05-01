---
title: "Binomial Expansion"
date: 2026-04-27
tags:
  - concept/mathematics
  - topic/binomial
  - status/sapling
---

# Binomial Expansion

The binomial theorem and its generalization for expanding powers of binomials.

## Overview

The binomial theorem provides a formula for expanding expressions of the form $(a + b)^n$ without performing repeated multiplication.

## Factorial

**Definition:**
$$n! = n \times (n-1) \times (n-2) \times \cdots \times 3 \times 2 \times 1$$
with $n \in \mathbb{N}$ and $0! = 1$.

**Recursive property:**
$$(n+1)! = (n+1) \times n!$$

## Binomial Coefficients

The binomial coefficient is defined as:
$$\binom{n}{r} = {}^nC_r = \frac{n!}{(n-r)! \, r!}$$
where $n$ is a positive integer, $r \in \mathbb{N}$ and $0 \le r \le n$.

**Computational form:**
$$\binom{n}{r} = \frac{n(n-1)(n-2)\cdots(n-r+1)}{r!}, \qquad n \ge r$$

**Properties**:
- Symmetry: $\binom{n}{r} = \binom{n}{n-r}$
- Pascal's identity: $\binom{n}{r-1} + \binom{n}{r} = \binom{n+1}{r}$
- Special values: $\binom{n}{0} = 1$, $\binom{n}{1} = n$, $\binom{n}{2} = \dfrac{n(n-1)}{2}$

## Pascal's Triangle

Triangular array where each number is the sum of the two above it:
```
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
1  5 10 10  5  1
```

## Binomial Theorem (Positive Integer Powers)

For positive integer $n$:
$$(a + b)^n = \sum_{r=0}^{n} \binom{n}{r} a^{n-r} b^r$$

Expanded form:
$$(a + b)^n = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{n}b^n$$

### Characteristics
1. There are $(n+1)$ terms in total
2. The first term is $a^n$ and the last term is $b^n$
3. The power of $a$ decreases by 1 from left to right, while the power of $b$ increases by 1; the sum of the powers in each term equals $n$
4. The coefficients are symmetrical

## General Term

The $(r+1)$th term in $(a + b)^n$:
$$T_{r+1} = \binom{n}{r} a^{n-r} b^r$$

This allows finding a specific term without expanding the entire expression.

## General Binomial Theorem (Infinite Series)

For any real number $n$ that is **not a positive integer** (e.g., negative integers, fractions), the expansion of $(1+x)^n$ is an infinite series valid only when $|x| < 1$:

$$(1 + x)^n = 1 + nx + \frac{n(n-1)}{2!}x^2 + \frac{n(n-1)(n-2)}{3!}x^3 + \cdots, \qquad |x| < 1$$

This is called the **binomial series**. If $|x| \ge 1$, the series diverges.

### Finite vs Infinite Expansions

| | $n$ positive integer | $n$ not a positive integer |
|---|---|---|
| **Form** | $(1+x)^n = 1 + {}^nC_1 x + {}^nC_2 x^2 + \cdots + x^n$ | $(1+x)^n = 1 + nx + \dfrac{n(n-1)}{2}x^2 + \cdots$ |
| **Series length** | Finite ($n+1$ terms) | Infinite |
| **Validity** | Valid for all $x \in \mathbb{R}$ | Converges only for $\|x\| < 1$ |

## Approximations Using Binomial Expansion

### Case 1: Positive integer powers
For small $b$ relative to $a$, expand $(a+b)^n$ directly and truncate to obtain a decimal approximation.
- Example: $(2.02)^6 = (2 + 0.02)^6$

### Case 2: Non-integer or negative powers
Rewrite the expression in the form $k(1+x)^n$ where $|x| < 1$, apply the binomial series, and truncate.
- Example: $\sqrt[3]{8.064} = \sqrt[3]{8(1+0.008)} = 2(1+0.008)^{1/3}$

Always check that $x$ satisfies the validity condition $|x| < 1$.

## Applications

- Approximation of expressions and numerical values
- Finding specific coefficients or terms
- Probability (binomial distribution)
- Series expansions in calculus

## PASUM Course Links

- [[FAD1014 L23-L24 — Binomial Expansion]]
- [[FAD1014 Tutorial 11 — Binomial Theorem]]
- [[FAD1014 - Mathematics II]] — course
