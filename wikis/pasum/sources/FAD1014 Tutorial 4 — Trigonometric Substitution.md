---
title: "FAD1014 Tutorial 4 — Trigonometric Substitution"
date: 2026-04-27
tags:
  - source/tutorial
  - subject/mathematics-ii
  - topic/integration
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
---

# Tutorial 4: Trigonometric Substitution

Tutorial problems focused on trigonometric substitution for integrals containing radicals.

## Sections

### Basic Substitutions (Problems 1-4)
- $\sqrt{a^2 - x^2}$: $x = a\sin\theta$
- $\sqrt{a^2 + x^2}$: $x = a\tan\theta$
- $\sqrt{x^2 - a^2}$: $x = a\sec\theta$

### More Complex Integrals (Problems 5-8)
- Completing the square first
- Multiple substitutions
- Integrals requiring back-substitution

### Definite Integrals (Problems 9-12)
- Changing limits with substitution
- Evaluating without back-substitution

## Substitution Summary

| Radical | Substitution | Identity | Triangle |
|---------|--------------|----------|----------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $\cos^2\theta = 1 - \sin^2\theta$ | sin = opp/hyp |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $\sec^2\theta = 1 + \tan^2\theta$ | tan = opp/adj |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $\tan^2\theta = \sec^2\theta - 1$ | sec = hyp/adj |

## Common Results

- $\int \frac{dx}{\sqrt{a^2 - x^2}} = \arcsin\frac{x}{a} + C$
- $\int \frac{dx}{a^2 + x^2} = \frac{1}{a}\arctan\frac{x}{a} + C$

## Links
- [[FAD1014 L9-L10 — Trigonometric Substitution]]
- [[Integration Techniques]] — concept page
- [[FAD1014 - Mathematics II]] — course
