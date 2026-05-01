---
title: "FAD1015 Tutorial 10 — Estimation of Population Mean"
date: 2026-04-27
tags:
  - source/tutorial
  - course/FAD1015
  - topic/estimation
  - status/seedling
---

# FAD1015 Tutorial 10 — Estimation of Population Mean

Tutorial questions on confidence intervals for population mean with known and unknown population standard deviation. Source file: `FAD1015 25-26 Tutorial 10 Questions.pdf`

## Summary

Problem set covering point estimation, confidence interval construction, interpretation, and sample size determination for estimating population mean.

## Topics Covered

### 1. Point Estimation
- Sample mean as point estimator
- Properties: unbiasedness, consistency

### 2. Confidence Intervals (σ Known)
- Formula: x̄ ± z_(α/2) × σ/√n
- Critical values from standard normal
- Margin of error calculation

### 3. Confidence Intervals (σ Unknown)
- Using t-distribution
- Degrees of freedom: n - 1
- Formula: x̄ ± t_(α/2,n-1) × s/√n
- t-table usage

### 4. Sample Size Determination
- n = (z_(α/2) × σ / E)²
- Balancing confidence level and precision

### 5. Interpretation
- Correct vs incorrect interpretations
- Confidence level meaning

## Key Formulas

**σ Known:**
$$\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

**σ Unknown:**
$$\bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}$$

**Sample Size:**
$$n = \left(\frac{z_{\alpha/2} \cdot \sigma}{E}\right)^2$$

**Margin of Error:**
$$E = \text{critical value} \times \text{standard error}$$

## Problem Types

1. **CI with σ known**: Given x̄, σ, n, construct interval
2. **CI with σ unknown**: Given sample data, use t-distribution
3. **Sample size**: Determine n for desired margin of error
4. **Interpretation**: Explain meaning of confidence level

## Related Lectures

- [[FAD1015 L21-L22 — Estimation of Population Mean]]
- [[FAD1015 L20 — Sampling Distribution of the Mean]] — prerequisite
- [[FAD1015 L19 — Input Data & Descriptive Statistics in R]] — R implementation

## Related Concepts

- [[Probability Distributions]]
- [[Hypothesis Testing]] — uses similar test statistic concepts

## Related Course Page

- [[FAD1015 - Mathematics III]]
