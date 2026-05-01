---
title: "FAD1015 Tutorial 8 — Uniform & Exponential Distributions"
date: 2026-04-27
tags:
  - source/tutorial
  - course/FAD1015
  - topic/uniform-distribution
  - topic/exponential-distribution
  - status/seedling
---

# FAD1015 Tutorial 8 — Uniform & Exponential Distributions

Tutorial questions on continuous uniform and exponential distributions. Source file: `FAD1015 25-26 Tutorial 8 Questions.pdf`

## Summary

Problem set covering uniform distribution (constant probability) and exponential distribution (waiting times, memoryless property) with practical applications.

## Topics Covered

### 1. Uniform Distribution
- PDF and CDF calculations
- Expected value and variance
- Probability over intervals

### 2. Exponential Distribution
- PDF: f(x) = λe^(-λx)
- CDF: F(x) = 1 - e^(-λx)
- Mean and standard deviation: 1/λ
- Memoryless property applications

### 3. Relationship to Poisson
- Poisson: events per unit time
- Exponential: time between events
- λ parameter connection

## Key Formulas

**Uniform Distribution [a, b]:**
- PDF: f(x) = 1/(b-a)
- E[X] = (a + b)/2
- Var(X) = (b-a)²/12

**Exponential Distribution:**
- PDF: f(x) = λe^(-λx), x ≥ 0
- CDF: F(x) = 1 - e^(-λx)
- E[X] = 1/λ
- Var(X) = 1/λ²

**Memoryless Property:**
$$P(X > s + t \mid X > s) = P(X > t) = e^{-\lambda t}$$

## Problem Types

1. **Uniform**: Finding probabilities over intervals, expected values
2. **Exponential**: Waiting time problems, reliability, survival analysis
3. **Memoryless**: Conditional probability problems
4. **Poisson-Exponential Link**: Converting between event counts and waiting times

## Related Lectures

- [[FAD1015 L17-L18 — Uniform & Exponential Distributions + R Intro]]
- [[FAD1015 L14 — Poisson Distribution]] — related distribution
- [[FAD1015 L15-L16 — Normal Distribution & Approximation]] — other continuous distributions

## Related Concepts

- [[Probability Distributions]]

## Related Course Page

- [[FAD1015 - Mathematics III]]
