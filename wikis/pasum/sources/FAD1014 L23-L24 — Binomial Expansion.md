---
title: "FAD1014 L23-L24 — Binomial Expansion"
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics-ii
  - topic/binomial-expansion
  - status/sapling
course: "[[FAD1014 - Mathematics II]]"
---

# L23-L24: Binomial Expansion

Lecturer: EN. Hisham Safuan Mohamad Sukri

## Learning Outcomes

By the end of this lecture and the associated tutorial, students should be able to:

- Compute and simplify factorial expressions
- Construct Pascal's triangle to identify binomial coefficients
- Use the standard theorem to expand $(a+b)^n$ for $n \in \mathbb{Z}^+$
- Find a specific term without expanding the entire expression
- Apply the generalized binomial theorem for cases when $n$ is a non-positive integer (negative integer, fraction, etc.) and determine the validity range
- Use the binomial expansion to approximate complex values in decimal form

---

## Factorial

The $n!$ notation:

- We read $n!$ as "$n$ factorial"
- $n!$ is the product of all positive integers from 1 up to a given non-negative integer
- In general, $n!$ is defined as:
  $$n! = n \times (n-1) \times (n-2) \times \cdots \times 3 \times 2 \times 1$$
  with $n \in \mathbb{N}$ and $0! = 1$
- Factorial forms a recursive property:
  $$(n+1)! = (n+1) \times n! = (n+1) \times n \times (n-1)!$$

**Example 1**
Evaluate:
a) $6!$
b) $\dfrac{8!}{6!}$
c) $\dfrac{4!}{(6-4)!}$

**Example 2**
1. Prove that $(n+2) \times n! = n! + (n+1)!$
2. If $(n+1)! = 12 \times (n-1)!$, find the value of $n$

---

## Combinations (Binomial Coefficients)

The notation ${}^nC_r$ or $\displaystyle\binom{n}{r}$ is called the **binomial coefficient** as it is found in binomial expansion.

The binomial coefficient is defined as:
$${}^nC_r = \binom{n}{r} = \frac{n!}{(n-r)! \, r!}$$
where $n$ is a positive integer, $r \in \mathbb{N}$ and $0 \le r \le n$.

**Special cases:**
$${}^nC_0 = \binom{n}{0} = \frac{n!}{n! \, 0!} = 1$$
$${}^nC_1 = \binom{n}{1} = \frac{n!}{(n-1)! \, 1!} = n$$
$${}^nC_2 = \binom{n}{2} = \frac{n(n-1)}{2!}$$

**General form** (useful for computation):
$${}^nC_r = \binom{n}{r} = \frac{n \times (n-1) \times (n-2) \times \cdots \times (n-r+1)}{r!}, \quad n \ge r$$

**Example 3**
Show that:
$$\binom{n}{r-1} + \binom{n}{r} = \binom{n+1}{r}$$

---

## Binomial Expansions — The Binomial Theorem

A **binomial** is a sum of two terms $a+b$, which is usually an algebraic expression. The $a$ and $b$ can also represent specific numbers.

If $n$ is a positive integer, then a general formula for expanding $(a+b)^n$ is given by the **Binomial Theorem**:

$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

Expanded form:
$$(a+b)^n = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{n-1}ab^{n-1} + \binom{n}{n}b^n$$

### Characteristics of the expansion $(a+b)^n$

1. There are a total of $(n+1)$ terms in the series
2. The first term and last term are $a^n$ and $b^n$, respectively
3. The power of $a$ decreases by one from left to right, while the power of $b$ increases by one; the total power adds up to $n$ for each term
4. The coefficients of the terms are symmetrical and follow the pattern in **Pascal's Triangle**

### Pascal's Triangle

```
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
1  5  10  10  5  1
```

**Example 4**
Expand:
a) $(x+2y)^3$
b) $(2x-3y)^4$

**Example 5**
Use the expansion $(a+b)^6$ to approximate $(2.02)^6$ correct to four decimal places.

**Example 6**
a) Find the fifth term in the expansion of $\left(x^3 + \sqrt{y}\right)^{13}$
b) Find the coefficient of $x^2$ in the expansion of $\left(\dfrac{3}{x} - 5x^3\right)^6$
c) Expand $(1+2x-x^2)^5$ in ascending powers of $x$ up to the term in $x^3$

---

## General Binomial Theorem (Non-Positive Integer Powers)

The binomial expansion when $n$ is a **non-positive integer** (or more generally, not a positive integer — including negative integers and fractions) takes the form $(1+x)^n$ where $|x| < 1$.

- The expansion is an **infinite series**
- This series expansion is called the **binomial series** and is only valid for $|x| < 1$:

$$(1+x)^n = 1 + nx + \frac{n(n-1)}{2}x^2 + \frac{n(n-1)(n-2)}{3!}x^3 + \cdots, \qquad |x| < 1$$

### Differences Between the Two Cases

| When $n$ is positive integer | When $n$ is non-positive integer |
|------------------------------|----------------------------------|
| The series $(1+x)^n = 1 + {}^nC_1 x + {}^nC_2 x^2 + {}^nC_3 x^3 + \cdots + x^n$ | The series $(1+x)^n = 1 + nx + \dfrac{n(n-1)}{2}x^2 + \dfrac{n(n-1)(n-2)}{3!}x^3 + \cdots$ |
| The series is **finite**, ending at $x^n$; valid for all $x \in \mathbb{R}$ | The series is **infinite** and converges when $|x| < 1$ (or $-1 < x < 1$); the limit of the sum is $(1+x)^n$ |
| | If $x$ does not satisfy the validity range, the series diverges |

**Example 7**
Expand each of the following functions as an ascending series in $x$, up to and including the term in $x^3$. State the range of $x$ such that the expansion is valid.
a) $\sqrt{1+2x}$
b) $(1+x)^{-4}$

**Example 8**
Expand $(1+x)^{\frac{1}{3}}$ in ascending powers of $x$ up to the term in $x^2$. Hence, evaluate $\sqrt[3]{8.064}$ correct to four decimal places.

**Example 9**
Express $f(x) = \dfrac{17-x}{(2-x)(3+x)}$ in partial fractions.

Hence, expand $f(x)$ as a series in ascending powers of $x$ up to the term in $x^2$. Find the range of values of $x$ for which the expansion is valid.

---

## Links

- [[Binomial Expansion]] — concept page
- [[FAD1014 Tutorial 11 — Binomial Theorem]]
- [[FAD1014 - Mathematics II]] — course
