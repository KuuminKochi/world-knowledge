---
title: "FAD1018 W16 — Kinetic Chemistry"
date: 2026-04-29
tags:
  - source/lecture
  - course/FAD1018
  - topic/kinetic-chemistry
  - status/seedling
week: 16
lecturer: "[[Mr. Muhammad Hafiz Husna Bin Hasnan]]"
---

# FAD1018 W16 — Kinetic Chemistry

Week 16 lecture on chemical kinetics delivered by Mr. Muhammad Hafiz Husna Bin Hasnan (Chemistry Division, Centre for Foundation Studies in Sciences, Universiti Malaya).
Source pages: `W16-001.png` through `W16-080.png`.

## Learning Objectives

**Part 1:**
- Define reaction rate
- Write differential rate equation
- Determine reaction rate based on differential rate equation of a reaction

**Part 2:**
- Define rate law, order of reaction and half-life
- Write rate law with respect to the order of reaction
- Determine the order of reaction involving single reactant using initial rate method

---

## 1. Thermochemistry vs Kinetic Chemistry

> *"Thermodynamics tell us what can occur during a process, while kinetics tell us what actually occurs"*

| Aspect | Thermochemistry | Kinetic Chemistry |
|--------|----------------|-------------------|
| Focus | Enthalpy (Haba) | Movement and form of matter |
| Question | Can it happen? | How fast does it happen? |

**Example — Graphite vs Diamond:**

```smiles
C
```
$C_{(s, \text{graphite})} \longrightarrow C_{(s, \text{diamond})} \quad \Delta G^\circ_f = +2,900 \text{ kJ mol}^{-1}$
(requires energy, non-spontaneous)

```smiles
C
```
$C_{(s, \text{diamond})} \longrightarrow C_{(s, \text{graphite})} \quad \Delta G^\circ_f = -2,900 \text{ kJ mol}^{-1}$
(releases energy, **spontaneous thermodynamically**, yet kinetically extremely slow — diamonds persist for geological timescales)

---

## 2. Reaction Rate

- Reaction rate is the **change in the concentration of a reactant or product with time**
- Units: $\text{M min}^{-1}$ or $\text{M s}^{-1}$
- Reaction rate is **inversely proportional to time**
- The shorter the time taken, the higher the rate of reaction

Rate can be determined **graphically** from the plot of **concentration against time**.

### 2.1 Types of Rate

| Type | Definition | Graphical Method |
|------|-----------|------------------|
| **Average Rate** (purata / overall) | Rate over a time period | Gradient of a straight line drawn between two points on the curve |
| **Instantaneous Rate** (rate semasa) | Rate at a specific instant | Gradient of the **tangent** to the curve at that point |
| **Initial Rate** (kadar permulaan) | Rate at the very beginning ($t = 0$) | Gradient of the tangent drawn at $t = 0$ |

---

## 3. Differential Rate Equation

The relationship between the rate of **disappearance of reactants** and the rate of **appearance (formation) of products**.

For a general reaction:
$$aA + bB \longrightarrow cC + dD$$

$$\text{Rate} = -\frac{1}{a}\frac{d[A]}{dt} = -\frac{1}{b}\frac{d[B]}{dt} = +\frac{1}{c}\frac{d[C]}{dt} = +\frac{1}{d}\frac{d[D]}{dt}$$

Where $a, b, c, d$ are stoichiometric coefficients.

> The **negative sign** indicates that reactants are disappearing (concentration decreasing).

### 3.1 Example — Formation of Ammonia

```smiles
N#N
```
```smiles
[HH]
```
```smiles
N
```
$$N_2(g) + 3H_2(g) \longrightarrow 2NH_3(g)$$

$$\text{Rate} = -\frac{d[N_2]}{dt} = -\frac{1}{3}\frac{d[H_2]}{dt} = +\frac{1}{2}\frac{d[NH_3]}{dt}$$

Interpretation:
- Rate of disappearance of $N_2$ is $\frac{1}{3}$ of the rate of disappearance of $H_2$
- Rate of disappearance of $N_2$ is $\frac{1}{2}$ of the rate of formation of $NH_3$

### 3.2 Worked Example 1

**Question:** Determine the rate of disappearance of HI when the rate of formation of $I_2$ is $1.8 \times 10^{-6} \text{ M s}^{-1}$.

```smiles
I
```
```smiles
[HH]
```
```smiles
II
```
Given: $2HI \longrightarrow H_2 + I_2$

$$\text{rate} = -\frac{1}{2}\frac{d[HI]}{dt} = \frac{d[H_2]}{dt} = \frac{d[I_2]}{dt}$$

$$-\frac{1}{2}\frac{d[HI]}{dt} = \frac{d[I_2]}{dt}$$

$$-\frac{d[HI]}{dt} = 2 \times (1.8 \times 10^{-6}) = 3.6 \times 10^{-6} \text{ M s}^{-1}$$

> Rate of disappearance of HI = $\mathbf{3.6 \times 10^{-6} \text{ M s}^{-1}}$
> 
> (The negative sign is only an indication of disappearance; the rate value itself is reported as positive.)

### 3.3 Worked Example 2

**Question:** Consider the reaction between Zn and $AgNO_3$ to form $Zn(NO_3)_2$ and Ag. When $[Zn^{2+}]$ is increasing at $0.25 \text{ M s}^{-1}$, what is the rate of decrease of $[Ag^+]$?

```smiles
[Zn]
```
```smiles
[N+](=O)([O-])[O-].[Ag+]
```
```smiles
[Zn+2].[N+](=O)([O-])[O-].[N+](=O)([O-])[O-]
```
```smiles
[Ag]
```
Chemical equation: $Zn + 2AgNO_3 \longrightarrow Zn(NO_3)_2 + 2Ag$

$$\text{rate} = -\frac{d[Zn]}{dt} = -\frac{1}{2}\frac{d[Ag^+]}{dt} = \frac{d[Zn^{2+}]}{dt} = \frac{1}{2}\frac{d[Ag]}{dt}$$

Relating $Ag^+$ and $Zn^{2+}$:
$$-\frac{1}{2}\frac{d[Ag^+]}{dt} = \frac{d[Zn^{2+}]}{dt} = 0.25 \text{ M s}^{-1}$$

$$-\frac{d[Ag^+]}{dt} = 2 \times 0.25 = \mathbf{0.50 \text{ M s}^{-1}}$$

### 3.4 Worked Example 3

**Question:** For the reaction below, the rate of depletion of oxygen is $2.25 \times 10^{-3} \text{ mol L}^{-1} \text{ s}^{-1}$. Calculate the rate of:
(a) depletion of ammonia  
(b) formation of water  
(c) formation of nitrogen oxide

```smiles
N
```
```smiles
O=O
```
```smiles
[O-][N+](=O)[O-]
```
```smiles
O
```
$$4NH_3(g) + 5O_2(g) \longrightarrow 4NO(g) + 6H_2O(l)$$

$$\text{Rate} = -\frac{1}{4}\frac{d[NH_3]}{dt} = -\frac{1}{5}\frac{d[O_2]}{dt} = +\frac{1}{4}\frac{d[NO]}{dt} = +\frac{1}{6}\frac{d[H_2O]}{dt}$$

| Part | Quantity | Calculation | Result |
|:--:|:---|:---|:---|
| (a) | Depletion of $NH_3$ | $\frac{4}{5} \times 2.25 \times 10^{-3}$ | $\mathbf{1.8 \times 10^{-3} \text{ M s}^{-1}}$ |
| (b) | Formation of $H_2O$ | $\frac{6}{5} \times 2.25 \times 10^{-3}$ | $\mathbf{2.7 \times 10^{-3} \text{ M s}^{-1}}$ |
| (c) | Formation of $NO$ | $\frac{4}{5} \times 2.25 \times 10^{-3}$ | $\mathbf{1.8 \times 10^{-3} \text{ M s}^{-1}}$ |

---

## 4. Rate Law

An expression relating the **rate of a reaction** to the **rate constant** and the **concentrations of the reactants raised to some powers**. Also known as the **rate equation**.

At constant temperature and pressure, the rate of reaction is **directly proportional** to the concentration of reactants.

For a general reaction $aA + bB \longrightarrow cC + dD$:

> **Takde kaitan dengan coeff.** — The rate law has **no relation** to the stoichiometric coefficients.

$$\boxed{\text{Rate} = k[A]^m[B]^n}$$

Where:
- $[A]$ = concentration of A
- $[B]$ = concentration of B
- $k$ = rate constant
- $m$ = order with respect to A
- $n$ = order with respect to B
- $m + n$ = overall reaction order

> **Critical:** $m$ and $n$ are **not** $a$ and $b$. The order $\neq$ stoichiometric coefficient.

### 4.1 Rate Constant ($k$)

- $k$ is the constant of proportionality between the reaction rate and the concentration of reactants (berkadar terus — directly proportional)
- The **unit of $k$ depends on the overall order** of the reaction
- A greater value of $k$ leads to a faster reaction rate

### 4.2 Order of Reaction

- The **sum of the powers** ($m + n + \dots$) to which all reactant concentrations appearing in the rate law are raised
- Usually defined in terms of **reactant's concentration**
- The values of $m$ and $n$ must be determined **experimentally**
- The order of a reaction is **not related** to the stoichiometric coefficients

#### Example A — Fluorine and Chlorine Dioxide

```smiles
FF
```
```smiles
O=Cl=O
```
```smiles
O=Cl(=O)F
```
$$F_2(g) + 2ClO_2(g) \longrightarrow 2FClO_2(g)$$

Given rate law: $\text{Rate} = k[F_2]^1[ClO_2]^1$

| Species | Order |
|:---|:---:|
| $F_2$ | 1 (first order) |
| $ClO_2$ | 1 (first order) |
| **Overall** | **2 (second order)** |

#### Example B — Nitric Oxide and Oxygen

```smiles
[O]N=O
```
```smiles
O=O
```
```smiles
O=[N+]([O-])[O-]
```
$$2NO(g) + O_2(g) \longrightarrow 2NO_2(g)$$

Given rate law: $\text{rate} = k[NO]^2[O_2]^1$

| Species | Order |
|:---|:---:|
| $NO$ | 2 (second order) |
| $O_2$ | 1 (first order) |
| **Overall** | **3 (third order)** |

#### Example C — Hydrogen Peroxide and Iodide

```smiles
OO
```
```smiles
[I-]
```
```smiles
[O-][I+2][O-]
```
```smiles
O
```
$$H_2O_2(aq) + 3I^-(aq) + 2H^+(aq) \longrightarrow I_3^-(aq) + 2H_2O(l)$$

Given rate law: $\text{Rate} = k[H_2O_2]^1[I^-]^1$

| Species | Order |
|:---|:---:|
| $H_2O_2$ | 1 (first order) |
| $I^-$ | 1 (first order) |
| $H^+$ | 0 (zero order — does not appear in rate law) |
| **Overall** | **2 (second order)** |

> Even though $H^+$ has a stoichiometric coefficient of 2, its reaction order is **zero** because it does not appear in the experimentally determined rate law.

---

## 5. Worked Examples — Method of Initial Rates

### Example 1: Determining Order from Experimental Data (p. 21)
Reaction: S₂O₈²⁻(aq) + 3I⁻(aq) → 2SO₄²⁻(aq) + I₃⁻(aq)

```smiles
O=S(=O)([O-])OOS(=O)(=O)[O-]
```
```smiles
[I-]
```
```smiles
[O-]S(=O)(=O)[O-]
```
```smiles
I[I-]I
```
Experimental data:
| Exp | [S₂O₈²⁻] | [I⁻] | Initial Rate (M s⁻¹) |
|-----|----------|------|----------------------|
| 1   | 0.08     | 0.034| 2.2 × 10⁻⁴           |
| 2   | 0.08     | 0.017| 1.1 × 10⁻⁴           |
| 3   | 0.16     | 0.017| 2.2 × 10⁻⁴           |

Comparing Exp 1 and 2: [S₂O₈²⁻] constant, [I⁻] halved → rate halves → **order w.r.t [I⁻] = 1**
Comparing Exp 2 and 3: [I⁻] constant, [S₂O₈²⁻] doubled → rate doubles → **order w.r.t [S₂O₈²⁻] = 1**

Rate law: **Rate = k[S₂O₈²⁻][I⁻]**
Overall order = 2

### Example 2: Determining Order from Rate Change (p. 31)
For A → Product, rate increases 8-fold when [A] doubles.

$$Rate = k[A]^x$$
$$8 = 2^x$$
$$x = 3$$

**Third order reaction.**

### Example 3: Calculating Rate Constant (p. 32)
Decomposition of N₂O₅ at 45°C (first order):

```smiles
O=[N+]([O-])O[N+](=O)[O-]
```
```smiles
O=[N]O
```
```smiles
O=O
```
$$2N_2O_5(g) \longrightarrow 4NO_2(g) + O_2(g)$$

Rate = k[N₂O₅]

Given: [N₂O₅]₀ = 1.5 × 10⁻³ M, rate = 8.6 × 10⁻⁷ M s⁻¹

$$k = \frac{8.6 \times 10^{-7}}{1.5 \times 10^{-3}} = 5.73 \times 10^{-4}\ s^{-1}$$

### Example 4: Multiple Reactants (p. 33)
For aA + bB → cC

| Exp | [A]/M | [B]/M | Initial Rate (M min⁻¹) |
|-----|-------|-------|------------------------|
| 1   | 1.0   | 1.0   | 2.20 × 10⁻⁴            |
| 2   | 2.0   | 2.0   | 1.70 × 10⁻³            |
| 3   | 1.0   | 3.0   | 6.60 × 10⁻⁴            |
| 4   | 3.0   | 2.0   | 3.96 × 10⁻³            |

Using method of initial rates:
- Comparing Exp 1 and 3: [A] constant, [B] tripled → rate triples → **order w.r.t [B] = 1**
- Comparing Exp 2 and 4: [B] constant, [A] increased 1.5× → rate increased ~2.33× → **order w.r.t [A] = 2**

Rate law: **Rate = k[A]²[B]**
Overall order = 3

---

## 6. Effect of Order on Reaction Rate (p. 22–25)

For A → Products with Rate = k[A]ⁿ:

| Order (n) | Rate Law | Effect of Doubling [A] |
|-----------|----------|------------------------|
| 0         | Rate = k | No change              |
| 1         | Rate = k[A] | Rate doubles        |
| 2         | Rate = k[A]² | Rate quadruples    |

General rule: If [A] is multiplied by factor f, rate changes by factor **fⁿ**.

> [!tip] Memory aid from lecture
> **0th order**: Rate is flat — doubling [A] does nothing.
> **1st order**: Rate is proportional — doubling [A] doubles rate.
> **2nd order**: Rate is squared — doubling [A] gives 4× rate.

---

## 7. Unit of Rate Constant (p. 26–30)

The unit of k depends on overall order.

For A → Product, Rate = k[A]ˣ:

| Order | Derivation | Unit of k |
|-------|------------|-----------|
| 0     | Rate = k | M s⁻¹     |
| 1     | k = Rate/[A] | s⁻¹     |
| 2     | k = Rate/[A]² | M⁻¹ s⁻¹ |

General formula: **M^(1−n) s⁻¹**

---

## 8. Integrated Rate Equations — Introduction (p. 34–35)

An equation representing the dependence of the rate of reaction on the concentration of reacting species.

- Instantaneous rate of reaction is expressed as the slope of the tangent at any instant of time in the concentration vs time graph
- It is very difficult to determine the rate of reaction from the concentration vs time graph directly
- Therefore, we integrate the differential rate equation to obtain a relation between the concentration at different points and the rate constant
- Different orders of reaction have different integrated rate equations

---

## 9. Integrated Rate Equations — Zero and First Order Derivations (p. 36–40)

### 9.1 Zero Order

Differential form:
$$-\frac{d[A]}{dt} = k$$

Integrated form:
$$[A]_0 - [A]_t = kt$$

Rearranged:
$$[A]_t = -kt + [A]_0$$

Graphical analysis:
- Plot of **[A] vs t**: linear with **slope = −k**
- Plot of **rate vs [A]**: horizontal line (rate independent of concentration)

> [!note] Key insight from lecture
> Only the plot of concentration vs time for zero-order reaction will give a linear plot of [A] vs t.

### 9.2 First Order

Differential form:
$$-\frac{d[A]}{dt} = k[A]$$

Integrated form:
$$\ln[A]_0 - \ln[A]_t = kt$$

Graphical analysis:
- Plot of **rate vs [A]**: linear with **slope = k**
- Plot of **ln[A] vs t**: linear with **slope = −k**

---

### 10. Integrated Rate Equations — Graphical Methods

#### First Order (Recap)
$$ln[A]_t = -kt + ln[A]_0$$

From the integrated rate equation $ln[A]_0 - ln[A]_t = kt$:
- Plot of $ln[A]$ vs $t$ gives a straight line with **negative slope** $-k$
- Rate constant obtained from gradient: $k = -(\text{slope})$

#### Second Order
For $A \rightarrow \text{Product}$ with Rate $= k[A]^2$:

Differential form:
$$-\frac{d[A]}{dt} = k[A]^2$$

Integrated form:
$$\frac{1}{[A]_t} - \frac{1}{[A]_0} = kt$$

Rearranged:
$$\frac{1}{[A]_t} = kt + \frac{1}{[A]_0}$$

- Plot of $\frac{1}{[A]}$ vs $t$ gives a straight line with **positive slope** $+k$
- **Important**: This is the only linear plot with a positive slope among the three orders

### 11. Worked Examples — Integrated Rate Laws

#### Example 1: Zero-Order Decomposition of H₂O₂

```smiles
OO
```
For the zero-order decomposition of H₂O₂ (aq):
- $k = 3.66 \times 10^{-3}\ \text{Ms}^{-1}$
- $[H_2O_2]_0 = 0.88\ \text{M}$

**(a)** Time when $[H_2O_2] = 0.600\ \text{M}$:
$$[A]_0 - [A]_t = kt$$
$$0.88 - 0.600 = (3.66 \times 10^{-3})t$$
$$t = 77.05\ \text{s}$$

**(b)** $[H_2O_2]$ after $225\ \text{s}$:
$$[H_2O_2]_0 - [H_2O_2]_t = kt$$
$$0.88 - [H_2O_2]_t = (3.66 \times 10^{-3})(225) = 0.0585$$
$$[H_2O_2]_t = 0.8215\ \text{M}$$

> [!note] Lecturer note
> Part (b) calculation shown in lecture: $0.882 - [H_2O_2]_t = 0.0585\ \text{M}$, giving $[H_2O_2]_t = 0.8235\ \text{M}$. Follow lecture working for exams.

#### Example 2: First-Order Reaction 2A → B

The reaction $2A \longrightarrow B$ has $k = 2.5 \times 10^{-3}\ \text{s}^{-1}$.

Determine the time taken for $[A]$ to decrease by 75%.

- $[A]_0 = 100$ (arbitrary units)
- $[A]_t = 25$ (remaining after 75% used)
- $k = 2.5 \times 10^{-3}\ \text{s}^{-1}$

$$ln[A]_0 - ln[A]_t = kt$$
$$t = \frac{ln(100) - ln(25)}{2.5 \times 10^{-3}} = \frac{ln(4)}{2.5 \times 10^{-3}}$$
$$t = 554.52\ \text{s}$$

#### Example 3: Second-Order Reaction 2A → B

The reaction $2A \longrightarrow B$ has $k = 2.8 \times 10^{-2}\ \text{M}^{-1}\text{min}^{-1}$ at $80\ ^\circ\text{C}$.

How long for $[A]$ to decrease from $0.88\ \text{M}$ to $0.14\ \text{M}$?

$$\frac{1}{[A]_t} - \frac{1}{[A]_0} = kt$$
$$\frac{1}{0.14} - \frac{1}{0.88} = (2.8 \times 10^{-2})t$$
$$t = 214.52\ \text{min}$$

#### Example 4: Second-Order Iodine Atom Recombination

```smiles
[I]
```
```smiles
[I][I]
```
Iodine atoms combine in the gas phase:
$$I(g) + I(g) \longrightarrow I_2(g)$$

- Rate constant: $k = 7.0 \times 10^{9}\ \text{M}^{-1}\text{s}^{-1}$ at $23\ ^\circ\text{C}$
- $[I]_0 = 0.086\ \text{M}$
- Time: $t = 2.0\ \text{min} = 120\ \text{s}$

$$\frac{1}{[I]_t} - \frac{1}{[I]_0} = kt$$
$$\frac{1}{[I]_t} - \frac{1}{0.086} = (7.0 \times 10^{9})(120)$$
$$[I]_t = 1.19 \times 10^{-12}\ \text{M}$$

### 12. Half-Life — Detailed Analysis

**Definition**: Length of time required for the concentration of a reactant to decrease to half of its initial value.

Different reaction orders have different half-life formulas and graphical behaviors.

#### Zero-Order Half-Life

From $[A]_0 - [A]_t = kt$, at $t = t_{1/2}$, $[A]_t = \frac{[A]_0}{2}$:

$$[A]_0 - \frac{[A]_0}{2} = kt_{1/2}$$

$$t_{1/2} = \frac{[A]_0}{2k}$$

**Graphical behavior**:
- Plot of $[A]$ vs time is **linear**
- Half-life **decreases** as the reaction proceeds
- Each successive half-life is shorter than the previous

> [!tip] Memory aid from lecture
> **0th order**: masa ↓ (half-life decreases)

#### First-Order Half-Life

From $ln[A]_0 - ln[A]_t = kt$, at $t = t_{1/2}$, $[A]_t = \frac{[A]_0}{2}$:

$$ln[A]_0 - ln\frac{[A]_0}{2} = kt_{1/2}$$
$$ln(2) = kt_{1/2}$$

$$t_{1/2} = \frac{ln\ 2}{k} = \frac{0.693}{k}$$

**Graphical behavior**:
- Plot of $[A]$ vs time is a **curve** (exponential decay)
- Half-life is **constant** and independent of initial concentration
- Each successive half-life is the same length

> [!tip] Memory aid from lecture
> **1st order**: Masa sama (half-life stays the same)

#### Second-Order Half-Life

From $\frac{1}{[A]_t} - \frac{1}{[A]_0} = kt$, at $t = t_{1/2}$, $[A]_t = \frac{[A]_0}{2}$:

$$\frac{1}{\frac{[A]_0}{2}} - \frac{1}{[A]_0} = kt_{1/2}$$
$$\frac{2}{[A]_0} - \frac{1}{[A]_0} = kt_{1/2}$$

$$t_{1/2} = \frac{1}{k[A]_0}$$

**Graphical behavior**:
- Plot of $[A]$ vs time is a **curve**
- Half-life **increases** as the reaction proceeds
- Each successive half-life is longer than the previous

> [!tip] Memory aid from lecture
> **2nd order**: Masa ↑ (half-life increases)

### 13. Worked Examples — Half-Life

#### Example 1: Half-Life of N₂O₅

```smiles
O=[N+]([O-])O[N+](=O)[O-]
```
What is the half-life of N₂O₅ if it decomposes with $k = 5.7 \times 10^{-4}\ \text{s}^{-1}$?

First-order reaction:
$$t_{1/2} = \frac{ln\ 2}{k} = \frac{ln\ 2}{5.7 \times 10^{-4}}$$
$$t_{1/2} = 1216.05\ \text{s}$$

#### Example 2: Radioactive Element K

A radioactive element K (always first order):
- $[K]_0 = 3.5 \times 10^{-6}\ \text{mol\ L}^{-1}$
- $t_{1/2} = 0.22\ \text{years}$

First calculate $k$:
$$k = \frac{ln\ 2}{t_{1/2}} = \frac{ln\ 2}{0.22} = 3.15\ \text{years}^{-1}$$

**(a)** Concentration after 6 months ($t = 0.5$ year):
$$ln[K]_0 - ln[K]_t = kt$$
$$ln(3.5 \times 10^{-6}) - ln[K]_t = 3.15(0.5)$$
$$[K]_t = 7.2 \times 10^{-7}\ \text{M}$$

**(b)** Time to reduce to $1.75 \times 10^{-6}\ \text{M}$:

Since $1.75 \times 10^{-6} = \frac{3.5 \times 10^{-6}}{2}$, this is exactly one half-life:
$$t = 0.22\ \text{years}$$

#### Example 3: Graphical Determination of Order

For the reaction $S \rightarrow T + V$:

| Time (min) | 0 | 10 | 20 | 30 | 40 | 50 | 60 |
|------------|---|----|----|----|----|----|-----|
| [S] (mol dm⁻³) | 4.5 | 3.10 | 2.38 | 1.92 | 1.60 | 1.40 | 1.22 |

Since a plot of $\frac{1}{[S]}$ vs $t$ produces a linear plot, the reaction is **second order**.

Results from graph:
- **Rate constant**: $k = 0.01\ \text{M}^{-1}\text{min}^{-1}$
- **Half-life**: $t_{1/2} = 22.2\ \text{min}$
- **At 1500 s (25 min)**: $[S] = 2.13\ \text{M}$

> [!important] Exam technique
> To determine order graphically: test which transformation gives a straight line — $[A]$ vs $t$ (zero), $ln[A]$ vs $t$ (first), or $\frac{1}{[A]}$ vs $t$ (second).

### 14. Learning Objectives Summary

**Part 4** (Pages 49–59):
- Explain the concept of half-life
- Determine reaction order from concentration-time graphs using half-life gaps
- Perform calculations using integrated rate equations and half-life formulas

**Part 5** (Pages 60–70):
- Explain collision theory
- Define activation energy
- Explain transition state theory
- Draw energy profile diagrams

**Part 6** (Pages 71–80):
- Explain effect of concentration/pressure, temperature, catalyst, and particle size on reaction rate
- Illustrate temperature effect using Maxwell-Boltzmann distribution curve
- Compare energy profile diagrams with and without catalyst

---

## Part 5: Collision Theory and Energy Profile Diagrams (Pages 61–70)

> [!info] Learning Objectives (Part 5)
> - Explain collision theory
> - Define activation energy
> - Explain transition state theory
> - Draw energy profile diagrams

### 15. Collision Theory (Page 61)

Collision Theory is the theory to explain the rate of chemical reaction.

**Key Ideas:**
1. Molecules must collide to react
2. The collision involved must be an **effective collision**

$$Rate \propto \frac{\text{Number of effective collisions}}{\text{time}}$$

### 16. Effective Collision (Pages 62–63)

**Definition:** A collision that leads to the formation of product.

**Requirements for Effective Collision:**

| Requirement | Explanation |
|-------------|-------------|
| **Minimum Kinetic Energy** | Colliding molecules must possess a certain minimum kinetic energy (activation energy, $E_a$) to initiate the chemical reaction |
| **Proper Orientation** | Molecules must collide in the right orientation |

**Diagram Analysis:**

| Type | Condition | Result |
|------|-----------|--------|
| (a) **Effective collision** | Proper orientation | Product formed |
| (b) **Ineffective collision** | Wrong orientation | No reaction ("Takde tindak balas") |

### 17. Activation Energy (Page 64)

**Definition:** The minimum energy required to initiate a chemical reaction.

Energy profile diagram labels:
- $E_{a\ (forward)}$ — activation energy for forward reaction
- $E_{a\ (backward)}$ — activation energy for reverse reaction  
- $\Delta H$ — enthalpy change
- $AB^{\#}$ — activated complex at the peak

```smiles
[C-]#[O+]
```
```smiles
N(=O)[O]
```
```smiles
O=C=O
```
```smiles
[N]=O
```
### 18. Transition State Theory (Pages 65–67)

**Transition State:** The configuration of atoms of the colliding species at the time of the collision.

**Activation Complex ($AB^{\#}$):** Species formed at the transition state.

#### Characteristics of Activated Complex

| Characteristic | Description |
|----------------|-------------|
| **Stability** | Very unstable and has a short half-life (sangat cepat) |
| **Potential Energy** | Greater than reactants or products |
| **Equilibrium** | The activated complex and the reactants are in chemical equilibrium |
| **Decomposition** | Decomposes to form products or reactants (boleh berlaku tindak balas berbalik / reversible) |

**Example Reaction with Molecular View:**

Hydroxide + Bromomethane → **Transition State (imaginary)** → Methanol + Bromide

```smiles
[OH-]
```
```smiles
CBr
```
```smiles
CO
```
```smiles
[Br-]
```
### 19. Energy Profile Diagrams (Pages 68–69)

> [!warning] Selalu keluar exam — Always appears in exams

#### 19.1 Exothermic Reaction

- Reactant energy > Product energy
- $\Delta H$ is negative (heat released)
- Example: $\text{CO (g)} + \text{NO}_2 \text{ (g)} \longrightarrow \text{CO}_2 \text{ (g)} + \text{NO (g)}$

$$E_{a\ \text{reverse}} = E_a + \Delta H$$

#### 19.2 Endothermic Reaction

- Reactant energy < Product energy
- $\Delta H$ is positive (heat absorbed)
- Example: $\text{CO}_2 \text{ (g)} + \text{NO (g)} \longrightarrow \text{CO (g)} + \text{NO}_2 \text{ (g)}$

$$E_{a\ \text{reverse}} = E_a - \Delta H$$

### 20. Worked Example: Free-Radical Substitution (Page 70)

**Problem:** A free-radical substitution reaction:
$$\text{P}\bullet + \text{Q}_2 \longrightarrow \text{PQ} + \text{Q}\bullet$$

Given:
- $E_{a\ \text{forward}} = 127\ \text{kJ mol}^{-1}$
- $E_{a\ \text{reverse}} = 15\ \text{kJ mol}^{-1}$

**Analysis:**
- Forward $E_a$ > Reverse $E_a$ → **Endothermic**
- $\Delta H = E_{a\ \text{forward}} - E_{a\ \text{reverse}} = 127 - 15 = \mathbf{112\ \text{kJ mol}^{-1}}$

Energy profile diagram shows activated complex at peak with $E_a = 127\ \text{kJ mol}^{-1}$ and $\Delta H = 112\ \text{kJ mol}^{-1}$.

---

## Part 6: Factors Affecting Reaction Rate (Pages 71–80)

> [!info] Learning Objectives (Part 6)
> - Explain effect of concentration/pressure, temperature, catalyst, and particle size on reaction rate
> - Illustrate temperature effect using Maxwell-Boltzmann distribution curve
> - Compare energy profile diagrams with and without catalyst

The rate of a reaction can be speed up or slowed down by four factors:

### 21. Overview of Factors (Page 72)

| Factor | Effect on Rate |
|--------|----------------|
| **Concentration or Pressure** | Higher → Faster rate |
| **Size of Particles** | Smaller → Faster rate |
| **Temperature** | Higher → Faster rate |
| **Catalyst** | Present → Faster rate |

### 22. Effect of Concentration on Reaction Rate (Pages 73–74)

Raising the concentration of reactant makes the reaction happen at a faster rate.

**Mechanism:**
1. Higher concentration → more particles per unit volume
2. More particles → frequency of collision increases
3. More collisions → frequency of effective collision increases
4. Therefore, rate of reaction increases

**Rate Law Relationship:**
$$Rate = k[A]^m$$

> [!important] Exception
> Rate of reaction for **zero-order reaction** is **not affected** by the concentration of the reactant.

### 23. Effect of Pressure on Reaction Rate (Pages 75–76)

> [!tip] Skema exam — This is the exam marking scheme format

The effect of changing pressure is like changing the concentration of reactant.

**Relationship:** $\uparrow P = \downarrow V$ (inverse relationship)

**Mechanism:**
1. Increase in pressure decreases the volume of container
2. Gas particles are pushed closer to each other
3. More gas per unit volume → frequency of collision increases
4. Frequency of effective collision increases
5. Thus, rate of reaction increases

### 24. Effect of Particle Size on Reaction Rate (Pages 77–79)

> [!note] Key concept: "tak boleh bergerak" (cannot move)

Solid particles are **immobile** but rely on liquid or gas particles colliding with solid's surface to react.

**Key Points:**
- In a reaction between solid and liquid, the surface area of the solid impacts how fast the reaction occurs
- Liquid and solid can only bump into each other at the liquid-solid interface (surface of the solid)
- Solid molecules trapped within the body of the solid cannot react

**Mechanism:**
1. If a solid is broken into smaller pieces, its total surface area gets larger
2. Greater total area exposed for reaction
3. Frequency of collision increases
4. Frequency of effective collision increases
5. Rate of reaction increases

### 25. Effect of Catalyst on Reaction Rate (Page 80)

**Definition:** A substance that increases the rate of reaction by providing an **alternative pathway with lower activation energy**.

**Key Properties:**
- Catalyst will **not affect** the enthalpy of reactant or product
- It **only decreases** the activation energy, $E_a$
- Types: Homogeneous, Heterogeneous, Enzymes

**Mechanism:**
$$\downarrow E_a \rightarrow \uparrow \text{particles with } E \geq E_a \rightarrow \uparrow \text{frequency of effective collision} \rightarrow \uparrow \text{rate}$$

---

## Pages 81–100: Catalysts, Temperature, and Arrhenius Equation

### Effect of Catalyst on Reaction Rate (p. 81–82)

**Energy Profile Diagram**
- Catalyst provides an alternative reaction pathway with lower activation energy
- Eₐ(with catalyst) < Eₐ(without catalyst)
- ΔH remains unchanged (reactants and products energy levels unaffected)
- Rate increases because more particles possess kinetic energy ≥ Eₐ

**Mechanism**
When catalyst is added:
1. Eₐ is lowered
2. Number of particles with energy > Eₐ increases
3. Frequency of effective collision increases
4. Rate of reaction increases

### Effect of Temperature on Reaction Rate (p. 83–88)

**Principles**
- Temperature affects the kinetic energy of reacting molecules (supplies energy)
- Increase in kinetic energy increases the speed of reacting molecules

**Chain of Events**
1. When temperature increases, kinetic energy of molecules increases
2. More collisions occur at a given time
3. The higher the kinetic energy, the higher the energy of the collisions
4. More collisions achieve the activation energy, Eₐ
5. Frequency of collision increases
6. Number of effective collisions increases
7. Rate of reaction increases

**Maxwell-Boltzmann Distribution Curve (p. 85–88)**
- Explains the effect of temperature on reaction rate
- Plot of variation of kinetic energy for a given temperature
- Different temperatures produce different curve shapes
- Area under the graph represents the total number of molecules in the reaction
- Only collisions with energy greater than Eₐ can react
- At T₂ > T₁:
  - T₁ curve has smaller area above Eₐ
  - T₂ curve has larger area above Eₐ
  - More particles at T₂ possess kinetic energy greater than activation energy
  - Therefore rate increases at higher temperature

### Arrhenius Equation — Detailed (p. 91–97)

**Learning Objectives**
- State the Arrhenius equation
- Explain the relationship between temperature and activation energy to the rate constant
- Determine k, Eₐ, T and A by calculation and graph

**Equation**
$k = Ae^{-E_a/RT}$

Where:
- k = rate constant
- A = Arrhenius constant (collision frequency factor)
- Eₐ = activation energy for reaction
- R = universal gas constant (8.314 J mol⁻¹ K⁻¹)
- T = absolute temperature in K

**Linear Form**
Taking natural logarithm:
$\ln k = \ln A - \frac{E_a}{RT}$

Rearranged to straight-line form (y = mx + c):
$\ln k = \frac{-E_a}{R}\left(\frac{1}{T}\right) + \ln A$

**Graph Representation**
- Plotting ln k vs 1/T gives a straight line
- Slope, m = -Eₐ/R
- Y-intercept = ln A

**Two-Point Form**
For the same reaction at two different temperatures T₁ and T₂:
$\ln\frac{k_1}{k_2} = \frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$

**Factors Affecting Rate Constant**
- **Temperature**: The higher the temperature, the greater the rate constant
- **Catalyst**: Lowers Eₐ → greater rate constant

### Worked Examples (p. 89–90, 98–100)

**Example 1: Temperature Effect (p. 89)**
Explain how temperature would influence the rate of reaction:
1. Kinetic energy is directly proportional to the temperature
2. When temperature increases, kinetic energy also increases
3. More molecules will have equal or greater energy than activation energy
4. Effective collision increases, therefore reaction increases

**Example 2: Iodination of Acetone (p. 90)**
Reaction:

```smiles
CC(=O)C.II>>CC(=O)CI.I
```
(CH₃COCH₃(aq) + I₂(aq) → ICH₂COCH₃(aq) + HI(aq))

Rate constant = 1.8 × 10⁻³ M s⁻¹ (zero order overall — concentration not a factor)

Suggest 2 ways to increase the rate:
1. **Increase Temperature**: kinetic energy increases → frequency of collision and effective collision increases → rate increases
2. **Add Catalyst**: lowers activation energy → more molecules possess kinetic energy > Eₐ → frequency of effective collision increases → rate increases

**Example 3: Arrhenius — Find k₂ (p. 98)**
The rate constant of a first-order reaction is 3.46 × 10⁻² s⁻¹ at 298 K. What is the rate constant at 350 K if Eₐ = 50.2 J/mol?

Given:
- k₁ = 3.46 × 10⁻² s⁻¹
- T₁ = 298 K
- T₂ = 350 K
- Eₐ = 50.2 J/mol

Using:
$\ln\frac{k_1}{k_2} = \frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$

Solution: k₂ = 3.47 × 10⁻² s⁻¹

**Example 4: Arrhenius — Find T₂ (p. 99)**
Eₐ = 50.2 kJ mol⁻¹, k₁ = 3.46 × 10⁻² s⁻¹ at 298 K. Calculate T₂ if k₂ = 6.30 × 10⁻⁴ s⁻¹.

Given:
- Eₐ = 50.2 × 10³ J/mol
- k₁ = 3.46 × 10⁻² s⁻¹
- T₁ = 298 K
- k₂ = 6.30 × 10⁻⁴ s⁻¹

Solution: T₂ = 248.81 K

**Example 5: Arrhenius Graph — Determine Eₐ (p. 100)**
Decomposition of hydrogen iodide:

```smiles
I.I>>[H][H].[I][I]
```
(2HI(g) → H₂(g) + I₂(g))

Data for plotting ln k vs 1/T:

| k (M⁻¹ s⁻¹) | T (K) | ln k | 1/T (K⁻¹) |
|-------------|-------|------|-----------|
| 3.52 × 10⁻⁷ | 555 | -14.860 | 1.80 × 10⁻³ |
| 3.02 × 10⁻⁵ | 629 | -10.408 | 1.59 × 10⁻³ |
| 2.19 × 10⁻⁴ | 666 | -8.426 | 1.50 × 10⁻³ |
| 1.16 × 10⁻³ | 699 | -6.759 | 1.43 × 10⁻³ |
| 3.95 × 10⁻² | 781 | -3.231 | 1.28 × 10⁻³ |

Method: Plot ln k vs 1/T, determine slope = -Eₐ/R, then calculate Eₐ in kJ/mol.

## Related Topics

- [[Chemical Equilibrium]] — Kinetics and thermodynamics
- [[Thermochemistry]] — Activation energy and enthalpy

## Study Notes

> [!important] Exam Weight
> Kinetic Chemistry has high mark weight (10–18%) and appears consistently. Master integrated rate laws and Arrhenius calculations.

## Related Course Page

- [[FAD1018 - Basic Chemistry II]]
