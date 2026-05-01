---
title: "Kinetic Chemistry"
date: 2026-04-29
tags:
  - concept/chemistry
  - topic/physical-chemistry
  - status/seedling
lecturer: "[[Mr. Muhammad Hafiz Husna Bin Hasnan]]"
course: "[[FAD1018 - Basic Chemistry II]]"
---

# Kinetic Chemistry (Chemical Kinetics)

The study of reaction rates, the factors affecting them, and the mechanisms by which reactions occur.

> *"Thermodynamics tell us what can occur during a process, while kinetics tell us what actually occurs"*

Thermochemistry (enthalpy) tells us **if** a process is spontaneous; kinetic chemistry tells us **how fast** it actually happens. A reaction can be thermodynamically favourable yet kinetically frozen — e.g. diamond converting to graphite ($\Delta G^\circ_f = -2,900 \text{ kJ mol}^{-1}$) is spontaneous but occurs on geological timescales.

## Reaction Rate

The **change in the concentration of a reactant or product with time**.

- Units: $\text{M min}^{-1}$ or $\text{M s}^{-1}$
- Inversely proportional to time; the shorter the time taken, the higher the rate

### Types of Rate (Graphical)

| Type | Definition | Graphical Method |
|------|-----------|------------------|
| **Average Rate** | Rate over a time period | Gradient of a straight line between two points on the concentration–time curve |
| **Instantaneous Rate** | Rate at a specific instant | Gradient of the **tangent** to the curve at that point |
| **Initial Rate** | Rate at the very beginning ($t = 0$) | Gradient of the tangent drawn at $t = 0$ |

### Differential Rate Equation

For a general reaction $aA + bB \longrightarrow cC + dD$:

$$\text{Rate} = -\frac{1}{a}\frac{d[A]}{dt} = -\frac{1}{b}\frac{d[B]}{dt} = +\frac{1}{c}\frac{d[C]}{dt} = +\frac{1}{d}\frac{d[D]}{dt}$$

The negative sign indicates that reactants are disappearing.

#### Example — Ammonia Synthesis

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

#### Example — HI Decomposition

```smiles
I
```
```smiles
[HH]
```
```smiles
II
```

$$2HI \longrightarrow H_2 + I_2$$

If $\frac{d[I_2]}{dt} = 1.8 \times 10^{-6} \text{ M s}^{-1}$, then rate of disappearance of HI:
$$-\frac{d[HI]}{dt} = 2 \times 1.8 \times 10^{-6} = 3.6 \times 10^{-6} \text{ M s}^{-1}$$

## Rate Law (Rate Equation)

An expression relating the rate of a reaction to the rate constant and the concentrations of the reactants raised to some powers:

$$\text{Rate} = k[A]^m[B]^n$$

Where:
- $k$ = rate constant (temperature dependent)
- $m, n$ = reaction orders with respect to each reactant
- Overall order = $m + n$

> **Critical:** $m$ and $n$ are determined **experimentally** and are **not** the stoichiometric coefficients $a$ and $b$. Order $\neq$ stoichiometric coefficient.

### Rate Constant ($k$)

- Constant of proportionality between reaction rate and reactant concentration
- The **unit of $k$ depends on the overall order** of the reaction
- Greater $k$ → faster reaction rate

### Order of Reaction

- The **sum of the powers** to which all reactant concentrations in the rate law are raised
- Defined in terms of **reactant concentration**
- Must be determined **experimentally**

#### Lecture Examples

**Example A — Fluorine and Chlorine Dioxide**

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

Rate law: $\text{Rate} = k[F_2]^1[ClO_2]^1$
- Order wrt $F_2$ = 1, wrt $ClO_2$ = 1
- **Overall order = 2** (second order)

**Example B — Nitric Oxide and Oxygen**

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

Rate law: $\text{rate} = k[NO]^2[O_2]^1$
- Order wrt $NO$ = 2, wrt $O_2$ = 1
- **Overall order = 3** (third order)

**Example C — Hydrogen Peroxide and Iodide**

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

Rate law: $\text{Rate} = k[H_2O_2]^1[I^-]^1$
- Order wrt $H_2O_2$ = 1, wrt $I^-$ = 1, wrt $H^+$ = **0** (does not appear in rate law)
- **Overall order = 2** (second order)

## Determining Reaction Order

### Method of Initial Rates
Compare initial rates at different initial concentrations.

### Integrated Rate Laws

| Order | Differential Form | Integrated Form | Half-Life | Linear Plot (Conc vs Time) | Slope |
|-------|-------------------|-----------------|-----------|---------------------------|-------|
| 0 | $-\frac{d[A]}{dt} = k$ | $[A]_t = [A]_0 - kt$ | $t_{1/2} = [A]_0/2k$ | $[A]$ vs $t$ | $-k$ |
| 1 | $-\frac{d[A]}{dt} = k[A]$ | $ln[A]_t = ln[A]_0 - kt$ | $t_{1/2} = 0.693/k$ | $ln[A]$ vs $t$ | $-k$ |
| 2 | $-\frac{d[A]}{dt} = k[A]^2$ | $\frac{1}{[A]_t} = \frac{1}{[A]_0} + kt$ | $t_{1/2} = 1/k[A]_0$ | $\frac{1}{[A]}$ vs $t$ | $+k$ |

**Key points**:
- First-order reactions have **constant half-life**
- Second-order linear plot is the **only one with positive slope** ($+k$)
- Rate constant $k$ is obtained from the magnitude of the gradient

### Rate vs Concentration Plots (p. 36–40)

An alternative way to identify order from the differential rate equation:

| Order | Rate Law | Plot of Rate vs [A] | Appearance |
|-------|----------|---------------------|------------|
| 0 | Rate = k | Rate vs [A] | Horizontal line (independent of [A]) |
| 1 | Rate = k[A] | Rate vs [A] | Straight line through origin (slope = k) |
| 2 | Rate = k[A]² | Rate vs [A] | Parabola (curved) |

> [!note] Lecture emphasis
> For **zero order**, the plot of reaction rate vs concentration is a straight line parallel to the x-axis.
> For **first order**, the plot of reaction rate vs concentration produces a linear line with slope = k.

## Half-Life

**Definition**: Length of time required for the concentration of a reactant to decrease to half of its initial value.

| Order | Half-Life Formula | Graphical Behavior |
|-------|-------------------|-------------------|
| 0 | $t_{1/2} = \frac{[A]_0}{2k}$ | Half-life **decreases** as reaction proceeds |
| 1 | $t_{1/2} = \frac{ln\ 2}{k} = \frac{0.693}{k}$ | Half-life is **constant** (independent of concentration) |
| 2 | $t_{1/2} = \frac{1}{k[A]_0}$ | Half-life **increases** as reaction proceeds |

### Graphical Identification
From a plot of $[A]$ vs time:
- **Zero-order**: Linear decay; successive half-lives get shorter
- **First-order**: Exponential decay; successive half-lives are equal
- **Second-order**: Curved decay; successive half-lives get longer

> [!tip] Lecture memory aids
> - **0th order**: masa ↓ (half-life decreases)
> - **1st order**: Masa sama (half-life stays the same)
> - **2nd order**: Masa ↑ (half-life increases)

## Worked Examples

### Example 1: Zero-Order Decomposition of H₂O₂

```smiles
OO  # H₂O₂ (hydrogen peroxide)
```

Given: $k = 3.66 \times 10^{-3}\ \text{Ms}^{-1}$, $[H_2O_2]_0 = 0.88\ \text{M}$

**(a)** Time when $[H_2O_2] = 0.600\ \text{M}$:
$$t = \frac{0.88 - 0.600}{3.66 \times 10^{-3}} = 77.05\ \text{s}$$

**(b)** $[H_2O_2]$ after $225\ \text{s}$:
$$[H_2O_2]_t = 0.88 - (3.66 \times 10^{-3})(225) = 0.8215\ \text{M}$$

> [!note] Lecture working
> Lecture shows: $0.882 - [H_2O_2]_t = 0.0585$, giving $[H_2O_2]_t = 0.8235\ \text{M}$. Use lecture figures in exams.

### Example 2: First-Order Reaction 2A → B

Given: $k = 2.5 \times 10^{-3}\ \text{s}^{-1}$. Time for 75% consumption of A:

$$t = \frac{ln(100/25)}{2.5 \times 10^{-3}} = \frac{ln(4)}{2.5 \times 10^{-3}} = 554.52\ \text{s}$$

### Example 3: Second-Order Reaction 2A → B

Given: $k = 2.8 \times 10^{-2}\ \text{M}^{-1}\text{min}^{-1}$ at $80\ ^\circ\text{C}$

Time for $[A]$ to decrease from $0.88\ \text{M}$ to $0.14\ \text{M}$:

$$\frac{1}{0.14} - \frac{1}{0.88} = (2.8 \times 10^{-2})t$$
$$t = 214.52\ \text{min}$$

### Example 4: Second-Order Iodine Recombination

```smiles
[I]       # I (iodine atom)
[I][I]    # I₂ (molecular iodine)
```

Reaction: $I(g) + I(g) \longrightarrow I_2(g)$

Given: $k = 7.0 \times 10^{9}\ \text{M}^{-1}\text{s}^{-1}$ at $23\ ^\circ\text{C}$, $[I]_0 = 0.086\ \text{M}$

After $t = 2.0\ \text{min} = 120\ \text{s}$:

$$[I]_t = 1.19 \times 10^{-12}\ \text{M}$$

### Example 5: Half-Life of N₂O₅

```smiles
O=[N+]([O-])O[N+](=O)[O-]  # N₂O₅ (dinitrogen pentoxide)
```

Given: first-order decomposition, $k = 5.7 \times 10^{-4}\ \text{s}^{-1}$

$$t_{1/2} = \frac{ln\ 2}{5.7 \times 10^{-4}} = 1216.05\ \text{s}$$

### Example 6: Radioactive Element K (First-Order)

Given: $[K]_0 = 3.5 \times 10^{-6}\ \text{M}$, $t_{1/2} = 0.22\ \text{years}$

$$k = \frac{ln\ 2}{0.22} = 3.15\ \text{years}^{-1}$$

**(a)** $[K]$ after 6 months ($0.5$ year):
$$[K]_t = 7.2 \times 10^{-7}\ \text{M}$$

**(b)** Time to reduce to $1.75 \times 10^{-6}\ \text{M}$ (half of initial):
$$t = 0.22\ \text{years}$$

### Example 7: Graphical Order Determination

For $S \rightarrow T + V$:

| Time (min) | 0 | 10 | 20 | 30 | 40 | 50 | 60 |
|------------|---|----|----|----|----|----|-----|
| [S] (mol dm⁻³) | 4.5 | 3.10 | 2.38 | 1.92 | 1.60 | 1.40 | 1.22 |

Since $\frac{1}{[S]}$ vs $t$ is linear → **second order**

- $k = 0.01\ \text{M}^{-1}\text{min}^{-1}$
- $t_{1/2} = 22.2\ \text{min}$
- At $1500\ \text{s} = 25\ \text{min}$: $[S] = 2.13\ \text{M}$

### Example 8: Method of Initial Rates — S₂O₈²⁻ + I⁻ (p. 21)

```smiles
O=S(=O)([O-])OOS(=O)(=O)[O-]  # S2O8^2- (peroxodisulfate)
[I-]                           # I- (iodide)
[O-]S(=O)(=O)[O-]             # SO4^2- (sulfate)
I[I-]I                         # I3- (triiodide)
```

Reaction: S₂O₈²⁻(aq) + 3I⁻(aq) → 2SO₄²⁻(aq) + I₃⁻(aq)

| Exp | [S₂O₈²⁻] | [I⁻] | Initial Rate (M s⁻¹) |
|-----|----------|------|----------------------|
| 1   | 0.08     | 0.034| 2.2 × 10⁻⁴           |
| 2   | 0.08     | 0.017| 1.1 × 10⁻⁴           |
| 3   | 0.16     | 0.017| 2.2 × 10⁻⁴           |

- Comparing Exp 1 and 2: [I⁻] halved → rate halves → **order w.r.t [I⁻] = 1**
- Comparing Exp 2 and 3: [S₂O₈²⁻] doubled → rate doubles → **order w.r.t [S₂O₈²⁻] = 1**

**Rate law: Rate = k[S₂O₈²⁻][I⁻]** (overall order = 2)

### Example 9: Determining Order from Rate Change (p. 31)

For A → Product, rate increases 8-fold when [A] doubles:

$$Rate = k[A]^x \Rightarrow 8 = 2^x \Rightarrow x = 3$$

**Third order reaction.**

### Example 10: Multi-Reactant System (p. 33)

For aA + bB → cC:

| Exp | [A]/M | [B]/M | Initial Rate (M min⁻¹) |
|-----|-------|-------|------------------------|
| 1   | 1.0   | 1.0   | 2.20 × 10⁻⁴            |
| 2   | 2.0   | 2.0   | 1.70 × 10⁻³            |
| 3   | 1.0   | 3.0   | 6.60 × 10⁻⁴            |
| 4   | 3.0   | 2.0   | 3.96 × 10⁻³            |

- Order w.r.t [B] = 1, order w.r.t [A] = 2
- **Rate law: Rate = k[A]²[B]** (overall order = 3)

## Factors Affecting Reaction Rate

The rate of a reaction can be speed up or slowed down by four factors:

### 1. Concentration

Raising the concentration makes the reaction happen at a faster rate.

**Mechanism:**
1. Higher concentration → more particles per unit volume
2. More particles → frequency of collision increases
3. More collisions → frequency of effective collision increases
4. Therefore, rate of reaction increases

**Rate Law:** $Rate = k[A]^m$

> [!important] Exception
> Rate of reaction for **zero-order reaction** is **not affected** by concentration.

### 2. Pressure (for gaseous reactions)

> [!tip] Skema exam — This is the exam marking scheme format

The effect of changing pressure is like changing the concentration.

**Relationship:** $\uparrow P = \downarrow V$ (inverse relationship)

**Mechanism:**
1. Increase in pressure decreases the volume of container
2. Gas particles are pushed closer to each other
3. More gas per unit volume → frequency of collision increases
4. Frequency of effective collision increases
5. Thus, rate of reaction increases

### 3. Particle Size / Surface Area

> [!note] Key concept: "tak boleh bergerak" (cannot move)

Solid particles are **immobile** but rely on liquid or gas particles colliding with solid's surface to react.

**Key Points:**
- In a solid-liquid reaction, the surface area of the solid impacts how fast the reaction occurs
- Liquid and solid can only bump into each other at the liquid-solid interface (surface of the solid)
- Solid molecules trapped within the body of the solid cannot react

**Mechanism:**
1. Breaking solid into smaller pieces → larger total surface area
2. Greater total area exposed → more solid molecules exposed
3. Frequency of collision increases
4. Frequency of effective collision increases
5. Rate of reaction increases

### 4. Temperature

- Higher T → more molecules with E ≥ Ea → faster rate
- Illustrated using Maxwell-Boltzmann distribution curve

**Mechanism:**
1. When temperature increases, kinetic energy of molecules increases
2. More collisions occur at a given time
3. Higher kinetic energy → higher energy of collisions
4. More collisions achieve the activation energy, $E_a$
5. Frequency of effective collision increases
6. Rate of reaction increases

### 5. Catalyst

**Definition:** A substance that increases the rate of reaction by providing an **alternative pathway with lower activation energy**.

**Key Properties:**
- Catalyst will **not affect** the enthalpy of reactant or product
- It **only decreases** the activation energy, $E_a$
- Types: Homogeneous, Heterogeneous, Enzymes

**Mechanism:**
$$\downarrow E_a \rightarrow \uparrow \text{particles with } E \geq E_a \rightarrow \uparrow \text{frequency of effective collision} \rightarrow \uparrow \text{rate}$$

### Effect of Concentration Change by Order (p. 22–25)

For A → Products with Rate = k[A]ⁿ, the effect of doubling [A]:

| Order (n) | Rate Law | Effect of Doubling [A] | Factor |
|-----------|----------|------------------------|--------|
| 0 | Rate = k | No change | 2⁰ = 1 |
| 1 | Rate = k[A] | Rate doubles | 2¹ = 2 |
| 2 | Rate = k[A]² | Rate quadruples | 2² = 4 |

**General rule**: If [A] is multiplied by factor f, rate changes by factor **fⁿ**.

> [!tip] Memory aid from lecture
> **0th order**: Rate is flat — doubling [A] does nothing.
> **1st order**: Rate is proportional — doubling [A] doubles rate.
> **2nd order**: Rate is squared — doubling [A] gives 4× rate.

## Arrhenius Equation

$k = Ae^{-E_a/RT}$

Where:
- k = rate constant
- A = Arrhenius constant (collision frequency factor)
- Eₐ = activation energy (J/mol)
- R = gas constant (8.314 J mol⁻¹ K⁻¹)
- T = absolute temperature (K)

### Logarithmic Forms

Natural logarithm form:
$\ln k = \ln A - \frac{E_a}{RT}$

Linear (straight-line) form — plot ln k vs 1/T:
$\ln k = \frac{-E_a}{R}\left(\frac{1}{T}\right) + \ln A$

- Slope, m = -Eₐ/R
- Y-intercept = ln A

### Two-Point Form
For the same reaction at two temperatures:
$\ln\frac{k_1}{k_2} = \frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$

**Factors affecting $k$:**
- Higher temperature → greater rate constant
- Catalyst present → lowers $E_a$ → greater rate constant

### Worked Example: Graphical Determination of $E_a$

For the decomposition of $\ce{N2O5}$:

```smiles
O=[N+]([O-])O[N+](=O)[O-]
```

| $T$ (K) | $k$ (s⁻¹) | $1/T$ (K⁻¹) | $\ln k$ |
|---------|-----------|-------------|---------|
| 298 | $3.46 \times 10^{-5}$ | $3.36 \times 10^{-3}$ | $-10.27$ |
| 308 | $1.35 \times 10^{-4}$ | $3.25 \times 10^{-3}$ | $-8.91$ |
| 318 | $4.98 \times 10^{-4}$ | $3.14 \times 10^{-3}$ | $-7.61$ |
| 328 | $1.44 \times 10^{-3}$ | $3.05 \times 10^{-3}$ | $-6.54$ |
| 338 | $4.87 \times 10^{-3}$ | $2.96 \times 10^{-3}$ | $-5.32$ |

Slope of $\ln k$ vs $1/T$ ≈ $-12,400$ K. Therefore:
$$E_a = -\text{slope} \times R = 12,400 \times 8.314 = 103,100\text{ J·mol}^{-1} = 103.1\text{ kJ·mol}^{-1}$$

### Worked Example: Finding $k$ at a New Temperature

For $\ce{2HI(g) -> H2(g) + I2(g)}$, $E_a = 183$ kJ·mol⁻¹, $k_1 = 3.02 \times 10^{-5}$ M⁻¹·s⁻¹ at $T_1 = 629$ K. Find $k_2$ at $T_2 = 700$ K.

$$\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

$$k_2 = 1.05 \times 10^{-3}\text{ M}^{-1}\text{s}^{-1}$$

A temperature increase of 71 K (~11%) increased $k$ by a factor of ~35 — demonstrating the exponential sensitivity of rate to temperature.

## Collision Theory

$$Rate \propto \frac{\text{Number of effective collisions}}{time}$$

Collision Theory explains the rate of chemical reaction based on two key ideas:
1. Molecules must collide to react
2. The collision must be an **effective collision**

### Effective Collision

**Definition:** A collision that leads to the formation of product.

**Requirements:**

| Requirement | Explanation |
|-------------|-------------|
| **Minimum Kinetic Energy** | Colliding molecules must possess a certain minimum kinetic energy (activation energy, $E_a$) to initiate the chemical reaction |
| **Proper Orientation** | Molecules must collide in the right orientation |

**Collision Outcomes:**

| Type | Condition | Result |
|------|-----------|--------|
| **Effective collision** | Proper orientation + sufficient energy | Product formed |
| **Ineffective collision** | Wrong orientation or insufficient energy | No reaction ("Takde tindak balas") |

**Rate Constant Equation:**
$$k = p·Z·e^{-E_a/RT}$$

Where:
- p = steric factor (orientation)
- Z = collision frequency

## Maxwell-Boltzmann Distribution

The Maxwell-Boltzmann distribution curve explains why temperature affects reaction rate:

- Plot of the fraction of molecules having a certain kinetic energy vs kinetic energy
- Different temperatures produce different curve shapes (T₂ > T₁ produces a broader, flatter curve shifted to higher energies)
- The area under the graph represents the total number of molecules in the reaction
- Only collisions with energy greater than Eₐ can react
- At higher temperature (T₂), the area above Eₐ is larger → more particles possess sufficient energy to react → rate increases

```smiles
I.I>>[H][H].[I][I]
```

(This illustrates that raising temperature increases the fraction of HI molecules with enough energy to decompose.)

## Transition State Theory

**Transition State:** The configuration of atoms of the colliding species at the time of the collision.

**Activation Complex ($AB^{\#}$):** Species formed at the transition state — at the peak of the energy barrier.

### Key Relationships

$$\Delta H = E_{a\ \text{forward}} - E_{a\ \text{reverse}}$$

### Activated Complex Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Stability** | Very unstable and has a short half-life (sangat cepat / very fast) |
| **Potential Energy** | Greater than reactants or products |
| **Equilibrium** | The activated complex and reactants are in chemical equilibrium |
| **Decomposition** | Decomposes to form products or reactants (boleh berlaku tindak balas berbalik / reversible) |

### Example: Nucleophilic Substitution

Hydroxide + Bromomethane → **Transition State (imaginary)** → Methanol + Bromide

```smiles
[OH-]              # Hydroxide ion
CBr                # Bromomethane (CH3Br)
CO                 # Methanol (CH3OH)
[Br-]              # Bromide ion
```

## Energy Profile Diagrams

> [!warning] Selalu keluar exam — Always appears in exams

Energy profile diagrams show the energy changes during a chemical reaction, including activation energies and enthalpy change.

### Exothermic Reaction

- Reactant energy > Product energy
- $\Delta H$ is negative (heat released)
- Example: $\text{CO (g)} + \text{NO}_2 \text{ (g)} \longrightarrow \text{CO}_2 \text{ (g)} + \text{NO (g)}$

$$E_{a\ \text{reverse}} = E_a + \Delta H$$

### Endothermic Reaction

- Reactant energy < Product energy
- $\Delta H$ is positive (heat absorbed)
- Example: $\text{CO}_2 \text{ (g)} + \text{NO (g)} \longrightarrow \text{CO (g)} + \text{NO}_2 \text{ (g)}$

$$E_{a\ \text{reverse}} = E_a - \Delta H$$

```smiles
[C-]#[O+]          # CO (carbon monoxide)
N(=O)[O]           # NO2 (nitrogen dioxide)
O=C=O              # CO2 (carbon dioxide)
[N]=O              # NO (nitric oxide)
```

### Worked Example: Free-Radical Substitution

**Problem:** For the reaction $\text{P}\bullet + \text{Q}_2 \longrightarrow \text{PQ} + \text{Q}\bullet$

Given:
- $E_{a\ \text{forward}} = 127\ \text{kJ mol}^{-1}$
- $E_{a\ \text{reverse}} = 15\ \text{kJ mol}^{-1}$

**Analysis:**
- Forward $E_a$ > Reverse $E_a$ → **Endothermic**
- $\Delta H = E_{a\ \text{forward}} - E_{a\ \text{reverse}} = 127 - 15 = \mathbf{112\ \text{kJ mol}^{-1}}$

**Energy Profile Diagram Labels:**
- $E_{a\ (forward)}$ — activation energy for forward reaction
- $E_{a\ (backward)}$ — activation energy for reverse reaction
- $\Delta H$ — enthalpy change
- $AB^{\#}$ — activated complex at the peak

## Reaction Mechanisms

The step-by-step sequence of elementary reactions by which an overall reaction occurs.

### Elementary Reaction vs Overall Reaction

- An **elementary reaction** is a single-step process where reactants directly form products in one molecular event — it cannot be broken down further
- An **overall reaction** represents the net change but may proceed through multiple elementary steps (the **reaction mechanism**)
- Reaction intermediates are formed and consumed within the mechanism, not appearing in the overall equation

### Molecularity

**Molecularity** is the number of reactant species in an **elementary step** (theoretical, integer values only):

| Molecularity | Rate Law (from mechanism) | Description | Example |
|-------------|--------------------------|-------------|---------|
| **Unimolecular** | Rate $= k[A]$ | Single molecule rearranges or decomposes; first order | $\ce{CH3NC -> CH3CN}$, $\ce{N2O5 -> NO2 + NO3}$ |
| **Bimolecular** | Rate $= k[A][B]$ or $k[A]^2$ | Two molecules collide; second order; most common | $\ce{NO + O3 -> NO2 + O2}$ |
| **Termolecular** | Rate $= k[A][B][C]$ or $k[A]^2[B]$ or $k[A]^3$ | Three molecules collide simultaneously; third order; extremely rare | $\ce{2NO + O2 -> 2NO2}$ |

> **Critical distinction:** Molecularity ≠ Reaction Order
> - Molecularity is **theoretical** (from proposed mechanism), always integer (1, 2, 3)
> - Reaction order is **experimental** (from rate data), can be fractional, zero, or integer
> - Molecularity applies only to elementary steps; order applies to overall reactions

### Rate-Determining Step (RDS)

The **slowest elementary step** in the mechanism. It acts as a bottleneck — the overall rate cannot exceed the rate of this step. The rate law of the overall reaction is derived from the rate-determining step.

### Determining Rate Law from Mechanism

**Procedure:**
1. Identify the slowest step (RDS)
2. Write its rate law based on molecularity
3. If the RDS involves intermediates, express their concentrations in terms of reactants using preceding fast equilibrium steps

### Mechanism Validation Example: $\ce{2NO(g) + 2H2(g) -> N2(g) + 2H2O(g)}$

```smiles
[O]N=O
```
```smiles
[HH]
```
```smiles
N#N
```

Experimentally determined rate law: Rate $= k[\ce{NO}]^2[\ce{H2}]$

**Mechanism A (valid):**
| Step | Reaction | Rate Law |
|------|----------|----------|
| Step 1 (**slow**) | $\ce{2NO + H2 -> N2O + H2O}$ | Rate $= k_1[\ce{NO}]^2[\ce{H2}]$ |
| Step 2 (fast) | $\ce{N2O + H2 -> N2 + H2O}$ | — |

Step 1 is RDS; its rate law matches experiment directly. ✓

**Mechanism B (also valid):**
| Step | Reaction |
|------|----------|
| Step 1 (fast, eq) | $\ce{2NO <=> N2O2}$ |
| Step 2 (**slow**) | $\ce{N2O2 + H2 -> N2O + H2O}$ |
| Step 3 (fast) | $\ce{N2O + H2 -> N2 + H2O}$ |

From Step 1 equilibrium: $K = [\ce{N2O2}]/[\ce{NO}]^2$ → $[\ce{N2O2}] = K[\ce{NO}]^2$

RDS rate law: Rate $= k_2[\ce{N2O2}][\ce{H2}] = k_2K[\ce{NO}]^2[\ce{H2}] = k_{\text{obs}}[\ce{NO}]^2[\ce{H2}]$ ✓

> Multiple mechanisms can be consistent with the same experimental rate law. Additional evidence (detection of intermediates, isotopic labelling) is needed to distinguish between them.

### Reaction Intermediates
- Formed in one elementary step, consumed in a subsequent step
- Do **not** appear in the overall balanced equation
- Often radicals, carbocations, or unstable complexes
- Their concentration is typically low and they are hard to detect directly

## Catalysts

- Increase reaction rate without being consumed (regenerated in the mechanism)
- Provide **alternative reaction pathway** with lower activation energy
- Do **not** affect $\Delta H$, equilibrium position, or thermodynamic spontaneity ($\Delta G$ unchanged)
- Reactants and products energy levels remain unchanged — only the barrier height changes

**Energy Profile Comparison:**
- $E_a$(with catalyst) < $E_a$(without catalyst)
- Transition state energy is lower for the catalyzed pathway
- More particles possess kinetic energy $\geq E_a$ → frequency of effective collisions increases → rate increases

### Homogeneous Catalysis

Catalyst is in the **same phase** as the reactants:
- Example: Iodide-catalyzed decomposition of $\ce{H2O2}$
  - $\ce{H2O2 + I- -> H2O + IO-}$ (slow)
  - $\ce{H2O2 + IO- -> H2O + O2 + I-}$ (fast)
  - $\ce{I-}$ consumed in Step 1, regenerated in Step 2
- Example: Acid-catalyzed esterification

```smiles
OO       # H2O2
[I-]     # Iodide catalyst
```

### Heterogeneous Catalysis

Catalyst is in a **different phase** from the reactants (typically solid catalyst, gaseous/liquid reactants):
- Reaction occurs at the catalyst **surface**
- **Mechanism:** Adsorption → Surface reaction → Desorption
- Examples:
  - **Haber process:** $\ce{N2 + 3H2 ->[Fe(s)] 2NH3}$
  - **Catalytic converters:** Pt/Pd/Rh convert $\ce{CO}$, $\ce{NO_x}$, hydrocarbons
  - **Hydrogenation:** $\ce{C2H4 + H2 ->[Ni(s)] C2H6}$

### Comparison: Homogeneous vs Heterogeneous

| Feature | Homogeneous | Heterogeneous |
|---------|------------|---------------|
| Phase (catalyst vs reactants) | Same phase | Different phase |
| Active site | Individual molecules/ions | Solid surface sites |
| Separation after reaction | Difficult (distillation, extraction) | Easy (filtration) |
| Selectivity | Typically high | Moderate |
| Temperature tolerance | Limited (thermal decomposition) | High |

## Enzyme Kinetics

Enzymes are biological catalysts — typically proteins — that dramatically accelerate biochemical reactions with extraordinary specificity.

### Key Terminology

| Term | Definition |
|------|------------|
| **Substrate (S)** | The reactant molecule that binds to the enzyme |
| **Active site** | The specific region of the enzyme where substrate binds and reaction occurs |
| **Enzyme-substrate complex (ES)** | The intermediate formed when substrate binds to the enzyme active site |
| **Product (P)** | The molecule released after the reaction |
| **Turnover number ($k_{\text{cat}}$)** | Maximum number of substrate molecules converted per enzyme molecule per second |

### General Enzyme-Catalyzed Reaction

$$\ce{E + S <=>[k_1][k_{-1}] ES ->[k_2] E + P}$$

### Michaelis-Menten Kinetics

Leonor Michaelis and Maud Menten (1913) developed the fundamental model of enzyme kinetics.

**Key assumptions:**
1. Enzyme and substrate form an ES complex
2. ES formation is in rapid equilibrium (or steady state)
3. Breakdown of ES to product is the rate-determining step
4. $[\ce{S}] \gg [\ce{E}]$ (substrate in large excess)

### The Michaelis-Menten Equation

$$v = \frac{V_{\text{max}}[S]}{K_m + [S]}$$

Where:
- $v$ = initial reaction velocity
- $V_{\text{max}}$ = maximum velocity (all enzyme active sites saturated)
- $[S]$ = substrate concentration
- $K_m$ = Michaelis constant = $[S]$ at which $v = V_{\text{max}}/2$

### Interpreting $K_m$

$$K_m = \frac{k_{-1} + k_2}{k_1}$$

$K_m$ measures enzyme-substrate **affinity**:
- **Low $K_m$** → high affinity (tight binding; reaches half-maximum velocity at low $[S]$)
- **High $K_m$** → low affinity (weak binding; needs high $[S]$ to reach half-maximum velocity)

When $k_2 \ll k_{-1}$ (product formation is slow compared to ES dissociation), $K_m \approx k_{-1}/k_1 = K_d$ (the dissociation constant of the ES complex).

### Kinetic Regimes

| Condition | Velocity | Kinetic Order |
|-----------|----------|---------------|
| $[S] \ll K_m$ | $v \approx \frac{V_{\text{max}}}{K_m}[S]$ | First-order in $[S]$ |
| $[S] = K_m$ | $v = V_{\text{max}}/2$ | — |
| $[S] \gg K_m$ | $v \approx V_{\text{max}}$ | Zero-order in $[S]$ (saturated) |

### $V_{\text{max}}$ and Turnover Number

$$V_{\text{max}} = k_2[E]_{\text{total}}$$

$$k_{\text{cat}} = \frac{V_{\text{max}}}{[E]_{\text{total}}}$$

$k_{\text{cat}}$ (turnover number) ranges from $10^{-1}$ to $10^7$ s⁻¹. Carbonic anhydrase: ~$10^6$ s⁻¹ — one of the fastest known enzymes.

### Lineweaver-Burk Plot (Double Reciprocal)

Taking reciprocals of the Michaelis-Menten equation:

$$\frac{1}{v} = \frac{K_m}{V_{\text{max}}}\frac{1}{[S]} + \frac{1}{V_{\text{max}}}$$

A plot of $1/v$ vs $1/[S]$ yields a straight line:
- **Slope** = $K_m/V_{\text{max}}$
- **Y-intercept** = $1/V_{\text{max}}$
- **X-intercept** = $-1/K_m$

Used experimentally to determine $K_m$ and $V_{\text{max}}$ from initial rate measurements.

### Enzyme Inhibition

| Type | Binding Site | Effect on $V_{\text{max}}$ | Effect on $K_m$ |
|------|-------------|--------------------------|----------------|
| **Competitive** | Active site (competes with S) | Unchanged | Increases |
| **Non-competitive** | Allosteric site (not active site) | Decreases | Unchanged |
| **Uncompetitive** | ES complex only | Decreases | Decreases |

### Biological Significance

- **Specificity:** Lock-and-key and induced-fit models
- **Efficiency:** Accelerate reactions by factors of $10^6$ to $10^{17}$
- **Mild conditions:** Operate at physiological temperature (37°C) and pH (~7.4)
- **Regulation:** Feedback inhibition, allosteric regulation, covalent modification

## Worked Examples

**Example: Temperature Effect on Rate**
Explain how temperature influences rate:
1. Kinetic energy is directly proportional to temperature
2. When temperature increases, kinetic energy increases
3. More molecules have energy ≥ activation energy
4. Effective collisions increase → rate increases

**Example: Iodination of Acetone**
Reaction:

```smiles
CC(=O)C.II>>CC(=O)CI.I
```

(CH₃COCH₃ + I₂ → ICH₂COCH₃ + HI)

Given rate constant = 1.8 × 10⁻³ M s⁻¹ (zero order). Ways to increase rate:
- Increase temperature (increases collision frequency and effective collisions)
- Add catalyst (lowers Eₐ)

**Example: Arrhenius Calculation — Find k₂**
k₁ = 3.46 × 10⁻² s⁻¹ at 298 K. Find k₂ at 350 K if Eₐ = 50.2 J/mol.

$\ln\frac{k_1}{k_2} = \frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$

Solution: k₂ = 3.47 × 10⁻² s⁻¹

**Example: Arrhenius Calculation — Find T₂**
Eₐ = 50.2 kJ mol⁻¹, k₁ = 3.46 × 10⁻² s⁻¹ at 298 K. Find T₂ for k₂ = 6.30 × 10⁻⁴ s⁻¹.

Solution: T₂ = 248.81 K

**Example: Arrhenius Graph — Determine Eₐ**
For 2HI(g) → H₂(g) + I₂(g), plot ln k vs 1/T. Slope = -Eₐ/R → calculate Eₐ in kJ/mol.

```smiles
I.I>>[H][H].[I][I]
```

## Related Topics
- [[Chemical Equilibrium]] — Kinetics relates to approach to equilibrium
- [[Thermochemistry]] — Activation energy and enthalpy

## Sources
- [[FAD1018 W16 — Kinetic Chemistry]] — Part 1 (pages 1–80): reaction rates, rate laws, integrated rate laws, half-life, collision theory, transition state theory, energy profile diagrams, factors affecting reaction rate
- [[FAD1018 W16 — Chemical Kinetics Part 2]] — Part 2: Arrhenius equation (detailed with worked examples), reaction mechanisms and molecularity, rate-determining step, mechanism validation, homogeneous vs heterogeneous catalysis, enzyme kinetics (Michaelis-Menten, $V_{\text{max}}$, $K_m$, turnover number, Lineweaver-Burk)
- [[FAD1018 - Basic Chemistry II]]
