---
title: "FAD1015 Tutorial 9 — Sampling Methods"
date: 2026-04-27
tags:
  - source/tutorial
  - course/FAD1015
  - topic/sampling
  - status/seedling
---

# FAD1015 Tutorial 9 — Sampling Methods

Tutorial questions on sampling distributions, Central Limit Theorem applications, and sampling methodology. Source file: `FAD1015 25-26 Tutorial 9 Questions.pdf`

## Summary

Problem set focused on sampling distributions of the mean, Central Limit Theorem applications, and calculations involving standard error.

## Topics Covered

### 1. Sampling Distribution Concepts
- Sample mean as random variable
- Distribution of x̄
- Standard error: σ/√n

### 2. Central Limit Theorem Applications
- When CLT applies (n ≥ 30 rule of thumb)
- Finding probabilities about sample means
- Non-normal populations → normal sampling distribution

### 3. Sampling Distribution Properties
- E[x̄] = μ
- Var(x̄) = σ²/n
- Shape approaches normal as n increases

### 4. Finite Population Correction
- When n/N > 0.05
- Correction factor: √((N-n)/(N-1))

## Key Formulas

**Sampling Distribution of Mean:**
$$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) \text{ for large } n$$

**Standard Error:**
$$SE = \frac{\sigma}{\sqrt{n}}$$

**Z-Score for Sample Mean:**
$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}$$

**Finite Population Correction:**
$$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \cdot \sqrt{\frac{N-n}{N-1}}$$

## Problem Types

1. **Probability about x̄**: Find P(x̄ < a), P(x̄ > b), given μ, σ, n
2. **Finding sample mean values**: Given probability, find cutoff
3. **CLT verification**: Checking conditions, applying theorem
4. **Finite population**: Applying correction factor

## Related Lectures

- [[FAD1015 L20 — Sampling Distribution of the Mean]]
- [[FAD1015 L21-L22 — Estimation of Population Mean]] — builds on sampling concepts

## Related Concepts

- [[Probability Distributions]]
- [[Hypothesis Testing]] — sampling distributions form foundation

## Related Course Page

- [[FAD1015 - Mathematics III]]
