---
title: "FAD1018 W3 — Buffer Solutions"
date: 2026-04-29
tags:
  - source/lecture
  - course/FAD1018
  - topic/ionic-equilibria
  - topic/buffers
  - status/seedling
week: 3
lecturer: "[[Dr Fauzani Md Salleh]]"
---

# FAD1018 W3 — Buffer Solutions

Part 4 of Ionic Equilibria. Source file: `W3 (2).pdf` (60 slides).

## Objectives
- Define buffer solution
- Calculate pH for acidic & basic buffer solutions
- Calculate pH after addition of acid or base into the buffer solution

## Common Ion Effect

The shift in equilibrium caused by the addition of a compound having an ion in common with the dissolved substances.

- Plays an important role in determining the pH of a solution
- A special case of Le Chatelier's principle
- Applies to weak acids, weak bases, and solubility of salts

**Example:**

$$HF(aq) + H_2O(l) \rightleftharpoons H_3O^+(aq) + F^-(aq) \quad K_a = 7.2 \times 10^{-4}$$

When NaF is added, $F^-$ increases; by Le Chatelier's principle, $[H^+]$ decreases and pH increases.

## Buffer Solution

A solution that maintains its pH when a small amount of an acid or a base is added to it.

### Types
- **Acidic buffer solution** (pH < 7)
- **Basic buffer solution** (pH > 7)

### Composition

| Buffer Type | Components | Example |
|-------------|-----------|---------|
| Acidic | Weak acid + its salt (conjugate base) | CH₃COOH + CH₃COONa |
| Basic | Weak base + its salt (conjugate acid) | NH₃ + NH₄Cl |

**Common buffer systems:**

```smiles
CC(=O)O
```
```smiles
CC(=O)[O-]
```
```smiles
N
```
```smiles
[NH4+]
```
```smiles
O=CO
```
```smiles
O=C[O-]
```
```smiles
F
```
```smiles
[F-]
```
```smiles
CN
```
```smiles
C[NH3+]
```
```smiles
S
```
```smiles
[SH-]
```
```smiles
C(=O)([O-])[O-]
```
```smiles
O=C(O)[O-]
```
```smiles
O=P([O-])(O)O
```
```smiles
O=P([O-])([O-])O
```
### Buffer Action

**Acidic buffer (CH₃COOH / CH₃COO⁻):**
- Acid added: $H^+ + CH_3COO^- \rightarrow CH_3COOH$
- Base added: $OH^- + CH_3COOH \rightarrow CH_3COO^- + H_2O$

**Basic buffer (NH₃ / NH₄⁺):**
- Acid added: $H^+ + NH_3 \rightarrow NH_4^+$
- Base added: $OH^- + NH_4^+ \rightarrow NH_4OH$

## Henderson-Hasselbalch Equation

### Acidic Buffer

$$pH = pK_a + \log\frac{[\text{conjugate base}]}{[\text{weak acid}]}$$

$$pH = pK_a + \log\frac{[A^-]}{[HA]}$$

### Basic Buffer

$$pOH = pK_b + \log\frac{[\text{conjugate acid}]}{[\text{weak base}]}$$

$$pH + pOH = 14$$

> [!important] Lecture note
> The Henderson-Hasselbalch equation is derived from the Ka expression by taking negative logs. It is valid when the assumption $x \ll [HA]_0$ and $x \ll [A^-]_0$ holds.

## Worked Examples

### Example 1: Common Ion Effect (Acidic)

Calculate the pH of a solution containing 0.20 M CH₃COOH and 0.30 M CH₃COONa. ($K_a = 1.8 \times 10^{-5}$)

**Method 1: Ka expression**
$$K_a = \frac{[H_3O^+][CH_3COO^-]}{[CH_3COOH]}$$
$$1.8 \times 10^{-5} = \frac{x(0.30)}{0.20}$$
$$x = 1.2 \times 10^{-5} \text{ mol dm}^{-3}$$
$$pH = -\log(1.2 \times 10^{-5}) = 4.92$$

**Method 2: Henderson-Hasselbalch**
$$pH = -\log(1.8 \times 10^{-5}) + \log\frac{0.30}{0.20} = 4.74 + 0.176 = 4.92$$

**Comparison:** Without salt, pH of 0.20 M CH₃COOH alone = 2.72. The common ion effect reduces ionisation and raises pH.

### Example 2: Acidic Buffer — Addition of Acid

Buffer: 0.025 mol CH₃COONa in 250.00 cm³ of 0.10 M CH₃COOH.

**(a) Initial pH:**
$$[CH_3COO^-] = \frac{0.025}{0.250} = 0.10 \text{ M}$$
$$pH = pK_a + \log\frac{0.10}{0.10} = 4.74 + 0 = 4.75$$

**(b) After adding 1.0 cm³ H₂SO₄ (0.1 M):**
$$n_{H^+} = 2 \times (0.1)(0.001) = 2.0 \times 10^{-4} \text{ mol}$$
$$V_{total} = 0.251 \text{ dm}^3$$

$$[CH_3COO^-] = \frac{0.025 - 2.0 \times 10^{-4}}{0.251} = 0.0988 \text{ M}$$
$$[CH_3COOH] = \frac{0.025 + 2.0 \times 10^{-4}}{0.251} = 0.1004 \text{ M}$$

$$pH = 4.74 + \log\frac{0.0988}{0.1004} = 4.73$$

$$\Delta pH = 4.75 - 4.73 = 0.02$$

**(c) After adding 1.0 cm³ NaOH (0.1 M):**
$$n_{OH^-} = 1.0 \times 10^{-4} \text{ mol}$$

$$[CH_3COO^-] = \frac{0.025 + 1.0 \times 10^{-4}}{0.251} = 0.1000 \text{ M}$$
$$[CH_3COOH] = \frac{0.025 - 1.0 \times 10^{-4}}{0.251} = 0.0992 \text{ M}$$

$$pH = 4.74 + \log\frac{0.1000}{0.0992} = 4.74$$

$$\Delta pH = 4.75 - 4.74 = 0.01$$

### Example 3: Basic Buffer

Mixture: 100 cm³ NH₃ (0.1 M) + 100 cm³ NH₄Cl (1.0 M). ($K_b = 1.8 \times 10^{-5}$)

**(a) Initial pH:**
$$[NH_3] = \frac{0.01}{0.2} = 0.05 \text{ M}$$
$$[NH_4^+] = \frac{0.1}{0.2} = 0.5 \text{ M}$$

$$pOH = -\log(1.8 \times 10^{-5}) + \log\frac{0.5}{0.05} = 4.744 + 1 = 5.744$$
$$pH = 14 - 5.744 = 8.26$$

**(b) After adding 1 cm³ HCl (0.1 M):**
$$n_{H^+} = 1.0 \times 10^{-4} \text{ mol}; \quad V_{total} = 0.201 \text{ dm}^3$$

$$[NH_3] = \frac{0.01 - 1.0 \times 10^{-4}}{0.201} = 0.0493 \text{ M}$$
$$[NH_4^+] = \frac{0.1 + 1.0 \times 10^{-4}}{0.201} = 0.498 \text{ M}$$

$$pOH = 4.744 + \log\frac{0.498}{0.0493} = 5.748$$
$$pH = 14 - 5.748 = 8.25$$

$$\Delta pH = 8.26 - 8.25 = 0.01$$

The solution is a buffer — pH changes only slightly upon addition of acid.

## Exercises (from lecture)

1. Calculate the pH of a buffer containing 0.30 M HCOOH and 0.52 M HCOOK. ($K_a = 1.7 \times 10^{-4}$)
2. Calculate the pH of a buffer containing 0.1 M HF and 0.3 M NaF. ($K_a = 7.1 \times 10^{-4}$)
3. A buffer is prepared by mixing 400 mL of 1.50 M NH₄Cl with 600 mL of 0.10 M NH₃. Calculate pH and the new pH after adding 2.0 mL of 0.1 M HCl. ($K_b = 1.8 \times 10^{-5}$)
4. Which of the following are buffer systems?
   - (a) KH₂PO₄ / H₃PO₄
   - (b) NaClO₄ / HClO₄
   - (c) C₅H₅N / C₅H₅NHCl
   - (d) KF / HF
   - (e) KBr / HBr
   - (f) Na₂CO₃ / NaHCO₃

## Biological Applications

- Buffer solutions are essential in biological systems (e.g., blood buffer, amino acid charge states)
- The pH of blood is maintained ~7.4 by the carbonic acid–bicarbonate buffer system
- Amino acids act as buffers depending on their pKa values

## Key Equations

$$pH = pK_a + \log\frac{[A^-]}{[HA]}$$

$$pOH = pK_b + \log\frac{[BH^+]}{[B]}$$

$$pH + pOH = 14 \text{ (at 25°C)}$$

## Links
- [[Ionic Equilibria]]
- [[FAD1018 - Basic Chemistry II]]
- [[FAD1018 Tutorial 3 — Buffer Solutions]]
- [[FAD1018 W2-W3 — Ionic Equilibria]]
