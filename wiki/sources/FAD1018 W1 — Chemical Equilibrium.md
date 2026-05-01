---
title: "FAD1018 W2 — Ionic Equilibria (Part 2)"
date: 2026-04-29
tags:
  - source/lecture
  - course/FAD1018
  - topic/ionic-equilibria
  - status/seedling
week: 2
lecturer: "[[Dr. Fauzani Md. Salleh]]"
---

# FAD1018 W2 — Ionic Equilibria (Part 2)

Week 2 lecture covering the pH scale, ionic product of water, degree of dissociation, and acid–base equilibrium calculations. Lecturer: **Dr. Fauzani Md. Salleh** (Chemistry Division, Centre for Foundation Studies in Science).

## Objectives

- Calculate the pH and read the pH scale
- Explain the acid–base properties of water and the concept of auto-ionisation
- Describe the degree of dissociation ($\alpha$)
- Explain the relationship between $K_a$ and $K_b$

---

## The pH Scale

Introduced by Danish biochemist **Søren Sørensen (1909)**. The pH scale measures the concentration of hydrogen ions in aqueous solution.

- **Neutral**: $[H^+] = 10^{-7}$ mol dm⁻³ and pH = 7
- **Acidic**: $[H^+] > 10^{-7}$ mol dm⁻³ and pH < 7
- **Basic**: $[H^+] < 10^{-7}$ mol dm⁻³ and pH > 7

### Definitions

**Acidic solution:**
$$pH = -\log[H^+] = \log\frac{1}{[H^+]}$$

Or, using the hydronium ion:
$$pH = -\log[H_3O^+] = \log\frac{1}{[H_3O^+]}$$

**Basic solution:**
$$pOH = -\log[OH^-] = \log\frac{1}{[OH^-]}$$

### Relationship between pOH and pH

$$pH + pOH = 14 \quad \text{(at 25 °C)}$$

Or, more generally:
$$pH + pOH = pK_w$$

```smiles
O                  # H2O (water)
[OH3+]             # H3O+ (hydronium)
[OH-]              # OH- (hydroxide)
```

---

## Ionic Product of Water ($K_w$)

The auto-ionisation of water:
$$H_2O(l) + H_2O(l) \rightleftharpoons H_3O^+(aq) + OH^-(aq)$$

From this equilibrium, the dissociation constant for water (the **ionic product**) is:
$$K_w = [H_3O^+][OH^-] = [H^+][OH^-]$$

At **298 K (25 °C)**:
$$K_w = 1.0 \times 10^{-14} \text{ mol}^2 \text{ dm}^{-6}$$

Taking negative logarithms:
$$-\log K_w = -\log[H^+] - \log[OH^-]$$
$$14 = pH + pOH$$

> [!note] Temperature Dependence
> The ionisation of water is an **endothermic** process. The ionic product increases rapidly with temperature.
>
> | Temperature (°C) | $K_w$ (mol² dm⁻⁶) |
> |------------------|-------------------|
> | 0 | $1.1 \times 10^{-15}$ |
> | 20 | $6.8 \times 10^{-15}$ |
> | 50 | $5.5 \times 10^{-14}$ |
> | 100 | $5.1 \times 10^{-13}$ |

---

## Degree of Dissociation ($\alpha$)

The degree of dissociation applies to **weak acids and weak bases**, which only partially dissociate in water.

### Weak Acid

$$\alpha = \frac{[H_3O^+]_{\text{equilibrium}}}{[\text{acid}]_{\text{Initial}}} = \frac{[H^+]_\rightleftharpoons}{[\text{acid}]_0}$$

Or as percentage ionisation:
$$\%\alpha = \frac{[H_3O^+]_\rightleftharpoons}{[\text{acid}]_0} \times 100\%$$

- For weak acids: $\alpha < 1$ or $\%\alpha < 100\%$
- $\alpha$ is **affected by the concentration** of the acid
- $K_a$ is **not affected** by concentration

### Weak Base

$$\alpha = \frac{[OH^-]_{\text{equilibrium}}}{[\text{base}]_{\text{Initial}}}$$

Or as percentage ionisation:
$$\%\alpha = \frac{[OH^-]_\rightleftharpoons}{[\text{base}]_0} \times 100\%$$

- For strong bases: $\alpha = 1$ or $\%\alpha = 100\%$
- For weak bases: $\alpha < 1$ or $\%\alpha < 100\%$
- $\alpha$ is affected by the concentration of the base

---

## Acid Dissociation Constant ($K_a$) and Weak Acids

For a generic weak acid HA:
$$HA(aq) + H_2O(l) \rightleftharpoons H_3O^+(aq) + A^-(aq)$$

$$K_a = \frac{[H_3O^+][A^-]}{[HA]}$$

### pKa

$$pK_a = -\log K_a$$

### Assumption Method

For weak acids where $K_a$ is small, the change in concentration $x$ is very small compared to the initial concentration $C_0$:

$$(C_0 - x) \approx C_0$$

> [!warning] When is the assumption valid?
> The assumption is typically valid when the resulting degree of dissociation is small ($\%\alpha < 10\%$). If $K_a$ or $K_b$ is given and is very small, the lecture explicitly applies $(C - x) \approx C$.

### Example: Nitrous Acid ($HNO_2$)

```smiles
O=NO              # HNO2 (nitrous acid)
```

Calculate the molarity of $H_3O^+$ in **0.1 M $HNO_2$** ($K_a = 5 \times 10^{-4}$):

| | $HNO_2$ | $H_3O^+$ | $NO_2^-$ |
|---|---|---|---|
| Initial | 0.1 | 0 | 0 |
| Change | $-x$ | $+x$ | $+x$ |
| Equilibrium | $0.1 - x$ | $x$ | $x$ |

$$K_a = \frac{x^2}{0.1 - x} \approx \frac{x^2}{0.1}$$

$$x = 7.07 \times 10^{-3} \text{ mol dm}^{-3}$$

$$pH = -\log(7.07 \times 10^{-3}) = 2.15$$

### Example: Ethanoic Acid ($CH_3COOH$)

```smiles
CC(=O)O           # CH3COOH (ethanoic / acetic acid)
CC(=O)[O-]        # CH3COO- (acetate)
```

Given **1.0 M $CH_3COOH$** with $K_a = 1.8 \times 10^{-5}$:

- $pK_a = -\log(1.8 \times 10^{-5}) = 4.74$
- Using ICE table and assumption: $x = 4.24 \times 10^{-3}$ M
- $pH = -\log(4.24 \times 10^{-3}) = 2.37$
- Degree of dissociation: $\alpha = \dfrac{4.24 \times 10^{-3}}{1.0} = 4.24 \times 10^{-3}$

---

## Base Dissociation Constant ($K_b$) and Weak Bases

For a generic weak base B:
$$B(aq) + H_2O(l) \rightleftharpoons BH^+(aq) + OH^-(aq)$$

$$K_b = \frac{[BH^+][OH^-]}{[B]}$$

### pKb

$$pK_b = -\log K_b$$

### Example: Ammonia ($NH_3$)

```smiles
N                  # NH3 (ammonia)
[NH4+]             # NH4+ (ammonium)
```

What is the pH of **0.40 M ammonia**? ($K_b = 1.8 \times 10^{-5}$)

| | $NH_3$ | $NH_4^+$ | $OH^-$ |
|---|---|---|---|
| Initial | 0.4 | 0 | 0 |
| Change | $-x$ | $+x$ | $+x$ |
| Equilibrium | $0.4 - x$ | $x$ | $x$ |

$$K_b = \frac{x^2}{0.4 - x} \approx \frac{x^2}{0.4}$$

$$x = 2.68 \times 10^{-3} \text{ mol dm}^{-3}$$

$$pOH = -\log(2.68 \times 10^{-3}) = 2.57$$
$$pH = 14 - 2.57 = 11.43$$

### Example: Aniline ($C_6H_5NH_2$)

```smiles
Nc1ccccc1          # C6H5NH2 (aniline)
```

Given **0.1 M aniline** with $K_b = 3.8 \times 10^{-10}$:

- $pK_b = -\log(3.8 \times 10^{-10}) = 9.42$
- Using assumption: $x = 6.164 \times 10^{-6}$ M
- $pOH = -\log(6.164 \times 10^{-6}) = 5.21$
- $pH = 14 - 5.21 = 8.79$
- $\alpha = \dfrac{6.164 \times 10^{-6}}{0.1} = 6.164 \times 10^{-5}$

---

## Relationship between $\alpha$, $K_a$ and $K_b$

When the degree of dissociation is small ($\%\alpha < 10\%$), the following approximations are valid:

**For weak acids:**
$$\alpha = \sqrt{\frac{K_a}{c}}$$

**For weak bases:**
$$\alpha = \sqrt{\frac{K_b}{c}}$$

> [!important] Validity Condition
> These formulae are **only valid when $\%\alpha < 10\%$**.

The degree of dissociation is **inversely proportional** to the square root of the molarity / concentration.

---

## Worked Exercises from Lecture

### Strong Acid pH Calculations

1. **0.001 mol dm⁻³ nitric acid ($HNO_3$)** — strong acid, fully dissociates:
   $$pH = -\log(0.001) = 3$$

2. **$[H^+] = 3.5 \times 10^{-3}$ mol dm⁻³**:
   $$pH = -\log(3.5 \times 10^{-3}) = 2.5$$

3. **0.01 M hydrochloric acid ($HCl$)**:
   $$pH = -\log(0.01) = 2$$

```smiles
O=[N+]([O-])O      # HNO3 (nitric acid)
Cl                 # HCl (hydrochloric acid)
```

### Strong Base pH Calculations

1. **0.05 M potassium hydroxide ($KOH$)**:
   $$pOH = -\log(0.05) = 1.3$$
   $$pH = 14 - 1.3 = 12.7$$

2. **NaOH solution with pH = 13.5**:
   $$pOH = 0.5$$
   $$[OH^-] = 10^{-0.5} = 0.32 \text{ M}$$

```smiles
[K+].[OH-]         # KOH (potassium hydroxide)
[Na+].[OH-]        # NaOH (sodium hydroxide)
```

### Mixed Calculations

1. **Coffee with $[OH^-] = 2.5 \times 10^{-9}$ mol dm⁻³**:
   - Method 1: $pOH = 8.6$, $pH = 5.4$, $[H^+] = 10^{-5.4} = 3.98 \times 10^{-6}$ M
   - Method 2: $[H^+] = \dfrac{K_w}{[OH^-]} = \dfrac{1.0 \times 10^{-14}}{2.5 \times 10^{-9}} = 4.00 \times 10^{-6}$ M

2. **$2.0 \times 10^{-3}$ M HCl at 25 °C**:
   - $[H^+] = 2.0 \times 10^{-3}$ M
   - $pH = 2.70$
   - $pOH = 11.30$
   - $[OH^-] = 5.01 \times 10^{-12}$ M

### Weak Acid Calculations

1. **0.1 M $HNO_2$ ($K_a = 5 \times 10^{-4}$)**:
   - $[H_3O^+] = 7.07 \times 10^{-3}$ M, $pH = 2.15$

2. **1.0 M $CH_3COOH$ ($K_a = 1.8 \times 10^{-5}$)**:
   - $pK_a = 4.74$, $pH = 2.37$, $\alpha = 4.24 \times 10^{-3}$

3. **0.1 M $CH_3COOH$, % ionisation = 1.34 %**:
   - $[H^+] = 1.34 \times 10^{-3}$ M

4. **0.10 M HCOOH, pH = 2.39**:
   - $[H^+] = 10^{-2.39} = 4.07 \times 10^{-3}$ M
   - $K_a = \dfrac{(4.07 \times 10^{-3})^2}{0.10 - 4.07 \times 10^{-3}} = 1.73 \times 10^{-4}$

5. **0.30 M HA, % dissociation = 2.0 %**:
   - $[H_3O^+] = \dfrac{2.0}{100} \times 0.30 = 6.00 \times 10^{-3}$ M
   - $K_a = \dfrac{(6.00 \times 10^{-3})^2}{0.30 - 6.00 \times 10^{-3}} = 1.22 \times 10^{-4}$
   - $pH = -\log(6.00 \times 10^{-3}) = 2.22$

6. **0.025 M HF ($K_a = 7.1 \times 10^{-4}$)** — solved **without** assumption (quadratic equation):
   - $[H_3O^+] = 3.85 \times 10^{-3}$ M
   - $pH = 2.41$

```smiles
F                  # HF (hydrofluoric acid)
[F-]               # F- (fluoride)
O=CO               # HCOOH (formic acid)
Oc1ccccc1          # C6H5OH (phenol)
[O-]c1ccccc1       # C6H5O- (phenoxide)
```

7. **0.5 M phenol ($C_6H_5OH$, $K_a = 1.3 \times 10^{-10}$)**:
   - $[H_3O^+] = 8.06 \times 10^{-6}$ M
   - $pH = 5.09$

### Weak Base Calculations

1. **0.40 M $NH_3$ ($K_b = 1.8 \times 10^{-5}$)**:
   - $[OH^-] = 2.68 \times 10^{-3}$ M
   - $pOH = 2.57$, $pH = 11.43$

2. **0.1 M aniline ($K_b = 3.8 \times 10^{-10}$)**:
   - $pK_b = 9.42$, $pH = 8.79$, $\alpha = 6.164 \times 10^{-5}$

3. **1.0 M dimethylamine ($(CH_3)_2NH$, $K_b = 5.4 \times 10^{-4}$)**:
   - $[OH^-] = 2.30 \times 10^{-2}$ M
   - $pOH = 1.64$, $pH = 12.36$

```smiles
CNC                # (CH3)2NH (dimethylamine)
CN                 # CH3NH2 (methylamine)
c1ccncc1           # C5H5N (pyridine)
```

4. **0.26 M methylamine ($CH_3NH_2$, $K_b = 4.4 \times 10^{-4}$)**:
   - $[OH^-] = 1.05 \times 10^{-2}$ M
   - $pOH = 1.98$, $pH = 12.02$

5. **0.062 M pyridine ($C_5H_5N$, $K_b = 1.7 \times 10^{-9}$)**:
   - $[OH^-] = 1.02 \times 10^{-5}$ M
   - $pOH = 4.99$, $pH = 9.01$

### Degree of Dissociation Applications

1. **0.4 M acetic acid, $K_a = 1.8 \times 10^{-5}$**:
   $$\alpha = \sqrt{\frac{1.8 \times 10^{-5}}{0.4}} = 6.71 \times 10^{-3}$$

2. **0.50 M $NH_3$, % dissociation = 6.3 %**:
   - $[OH^-] = \dfrac{6.3}{100} \times 0.5 = 3.15 \times 10^{-2}$ M
   - $pOH = 1.5$, $pH = 12.5$

---

## Key Takeaways

- **Strong acids/bases**: Completely dissociate; no need for ICE tables or $K_a$/$K_b$
- **Weak acids/bases**: Partially dissociate; use ICE tables with $K_a$ or $K_b$
- **Assumption**: For weak acids/bases with small $K$ values, $(C - x) \approx C$
- **Temperature matters**: $K_w$ changes with temperature; $pH + pOH = 14$ only at 25 °C
- **Degree of dissociation**: Inversely proportional to concentration; use $\alpha = \sqrt{K/c}$ when $\%\alpha < 10\%$

---

## Links

- [[Chemical Equilibrium]] — Foundation concepts
- [[Ionic Equilibria]] — Extended ionic equilibrium topics
- [[FAD1018 - Basic Chemistry II]] — Course page
