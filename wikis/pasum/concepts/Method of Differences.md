---
title: Method of Differences
date: 2026-04-28
tags:
  - concept
  - subject/mathematics
  - topic/series
  - topic/summation
  - status/seedling
aliases:
  - Telescoping Series
  - Partial Fractions Method
---

# Method of Differences

A technique for evaluating finite sums where terms cancel in a telescoping pattern. Particularly useful for rational functions that can be decomposed using partial fractions.

## Core Principle

If a general term $a_k$ can be expressed as:

$$a_k = f(k) - f(k-1)$$

Then the sum becomes:

$$\sum_{k=1}^{n} a_k = \sum_{k=1}^{n} [f(k) - f(k-1)]$$

When expanded, most terms cancel:

$$= [f(1) - f(0)] + [f(2) - f(1)] + [f(3) - f(2)] + \ldots + [f(n) - f(n-1)]$$

$$= f(n) - f(0)$$

This is called a **telescoping series** because it collapses like a telescope.

## Partial Fractions Decomposition

The method of differences often requires expressing rational functions as partial fractions.

### Example Decomposition

$$\frac{1}{(k+1)(k+2)} = \frac{1}{k+1} - \frac{1}{k+2}$$

**Verification:**
$$\frac{1}{k+1} - \frac{1}{k+2} = \frac{(k+2) - (k+1)}{(k+1)(k+2)} = \frac{1}{(k+1)(k+2)} \checkmark$$

## Worked Example

### Evaluate $\sum_{k=1}^{n} \frac{1}{(k+1)(k+2)}$

**Step 1:** Decompose using partial fractions
$$\frac{1}{(k+1)(k+2)} = \frac{1}{k+1} - \frac{1}{k+2}$$

**Step 2:** Write out the telescoping sum
$$\sum_{k=1}^{n} \left(\frac{1}{k+1} - \frac{1}{k+2}\right)$$

**Step 3:** Expand to see the cancellation pattern


| $k$ | First Part      | Second Part      |
| --- | --------------- | ---------------- |
| 1   | $\frac{1}{2}$   | $-\frac{1}{3}$   |
| 2   | $\frac{1}{3}$   | $-\frac{1}{4}$   |
| 3   | $\frac{1}{4}$   | $-\frac{1}{5}$   |
| ... | ...             | ...              |
| $n$ | $\frac{1}{n+1}$ | $-\frac{1}{n+2}$ |

**Step 4:** After cancellation, only the first term of the first part and the last term of the second part remain:

$$= \frac{1}{2} - \frac{1}{n+2}$$

**Step 5:** Simplify
$$= \frac{(n+2) - 2}{2(n+2)} = \frac{n}{2(n+2)}$$

## Common Patterns

| Original Term | Partial Fraction Form | Telescopes To |
|---------------|----------------------|---------------|
| $\frac{1}{k(k+1)}$ | $\frac{1}{k} - \frac{1}{k+1}$ | $1 - \frac{1}{n+1}$ |
| $\frac{1}{k(k+2)}$ | $\frac{1}{2}\left(\frac{1}{k} - \frac{1}{k+2}\right)$ | $\frac{1}{2}\left(1 + \frac{1}{2} - \frac{1}{n+1} - \frac{1}{n+2}\right)$ |
| $\frac{1}{(k+1)(k+2)}$ | $\frac{1}{k+1} - \frac{1}{k+2}$ | $\frac{1}{2} - \frac{1}{n+2}$ |

## When to Use Method of Differences

✅ **Use when:**
- Terms can be written as $f(k) - f(k-1)$
- Rational functions that decompose nicely via partial fractions
- Products in the denominator with linear factors

❌ **Don't use when:**
- Polynomial sums (use [[Summation Formulas]] instead)
- Geometric series (use geometric series formula)
- Terms don't telescope

## Related

- [[Summation Formulas]] — for polynomial series
- [[FAD1014 L22 — Finite Series and Summation]] — lecture source
- [[Binomial Expansion]] — related series techniques
