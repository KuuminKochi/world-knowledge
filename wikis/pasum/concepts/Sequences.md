---
title: "Sequences"
date: 2026-04-28
tags:
  - concept/mathematics
  - topic/sequences
  - topic/calculus
  - status/seedling
---

# Sequences

A **sequence** is an ordered list of numbers where each number is called a **term** of the sequence.

## Definition

A sequence is a function whose domain is the set of positive integers (or non-negative integers). It is typically denoted as:

$$\{a_k\}_{k=1}^{\infty} = a_1, a_2, a_3, \ldots, a_k, \ldots$$

Where $a_k$ is the $k$th term (or general term) of the sequence.

---

## Types of Sequences

### Convergent Sequences

> [!success] Definition
> A sequence $\{a_k\}$ is **convergent** if:
> $$\lim_{k \to \infty} a_k = L$$
> where $L$ is a finite real number.

The sequence **converges to L** as $k$ approaches infinity.

#### Examples of Convergent Sequences

| Sequence | General Term | Limit | Behavior |
|----------|-------------|-------|----------|
| $1.1, 1.01, 1.001, \ldots$ | $a_k = 1 + (0.1)^k$ | $1$ | Converges to 1 |
| $1, \frac{1}{2}, \frac{1}{3}, \ldots$ | $a_k = \frac{1}{k}$ | $0$ | Converges to 0 |
| $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \ldots$ | $a_k = \frac{k}{k+1}$ | $1$ | Converges to 1 |

---

### Divergent Sequences

> [!warning] Definition
> A sequence $\{a_k\}$ is **divergent** if:
> $$\lim_{k \to \infty} a_k \text{ does not exist}$$

This includes sequences that:
- Grow without bound ($\to \infty$ or $\to -\infty$)
- Oscillate without approaching any value

#### Examples of Divergent Sequences

| Sequence | General Term | Limit | Behavior |
|----------|-------------|-------|----------|
| $1, 3, 5, 7, \ldots$ | $a_k = 2k - 1$ | $\infty$ | Diverges to $+\infty$ |
| $2, 4, 8, 16, \ldots$ | $a_k = 2^k$ | $\infty$ | Diverges (exponential growth) |
| $-1, 1, -1, 1, \ldots$ | $a_k = (-1)^k$ | DNE | Diverges (oscillates) |

---

## Convergence Tests for Sequences

### Basic Limit Approach

The primary method to determine convergence:

1. Identify the general term $a_k$
2. Evaluate $\lim_{k \to \infty} a_k$
3. If the limit exists and is finite → **convergent**
4. If the limit is infinite or doesn't exist → **divergent**

### Useful Limits

$$\lim_{k \to \infty} \frac{1}{k^p} = 0 \quad \text{for } p > 0$$

$$\lim_{k \to \infty} r^k = 0 \quad \text{for } |r| < 1$$

$$\lim_{k \to \infty} \left(1 + \frac{1}{k}\right)^k = e$$

---

## Common Sequence Types

### Arithmetic Sequences

$$a_k = a_1 + (k-1)d$$

where $d$ is the common difference.

> **Note:** Arithmetic sequences with $d \neq 0$ are always **divergent**.

### Geometric Sequences

$$a_k = a_1 \cdot r^{k-1}$$

where $r$ is the common ratio.

| Condition | Behavior |
|-----------|----------|
| $\|r\| < 1$ | Converges to 0 |
| $r = 1$ | Converges to $a_1$ |
| $r = -1$ | Diverges (oscillates) |
| $\|r\| > 1$ | Diverges (unbounded) |

---

## Related Concepts

- [[Series]] — the sum of sequence terms
- [[Binomial Expansion]] — series expansion
- [[Power Series — Taylor & Maclaurin]] — infinite series representations
- [[FAD1014 L21 — Introduction to Series]] — lecture source
