---
title: "FAD1018 W16 — Chemical Kinetics Part 2"
date: 2026-04-29
tags:
  - source/lecture
  - subject/chemistry
  - topic/physical-chemistry
  - topic/chemical-kinetics
  - status/seedling
week: 16
course: "[[FAD1018 - Basic Chemistry II]]"
lecturer: "[[Mr. Muhammad Hafiz Husna Bin Hasnan]]"
---

# FAD1018 W16 — Chemical Kinetics Part 2

Week 16 lecture on chemical kinetics (Part 2), continuing from Part 1. This lecture covers the Arrhenius equation, reaction mechanisms, molecularity, rate-determining steps, catalysts, and enzyme kinetics. Delivered by Mr. Muhammad Hafiz Husna Bin Hasnan, Chemistry Division, Centre for Foundation Studies in Sciences, Universiti Malaya.

## 1. Arrhenius Equation

The Arrhenius equation quantitatively describes how the rate constant $k$ depends on temperature and activation energy:

$$k = Ae^{-E_a/RT}$$

Where:
- $k$ = rate constant
- $A$ = Arrhenius constant (frequency factor / pre-exponential factor), related to collision frequency and orientation
- $E_a$ = activation energy (J·mol⁻¹)
- $R$ = gas constant = $8.314$ J·mol⁻¹·K⁻¹
- $T$ = absolute temperature (K)

### Physical Interpretation

- $A$ represents the maximum rate constant at infinite temperature (all collisions are effective)
- $e^{-E_a/RT}$ is the fraction of molecules with energy $\geq E_a$ (from the Maxwell-Boltzmann distribution)
- Higher $T$ → larger $e^{-E_a/RT}$ → larger $k$ → faster reaction
- Higher $E_a$ → smaller $e^{-E_a/RT}$ → smaller $k$ → slower reaction

### Logarithmic Forms

**Natural log form** (for calculation):

$$\ln k = \ln A - \frac{E_a}{RT}$$

**Linearized form** (for graphical determination):

$$\ln k = -\frac{E_a}{R}\left(\frac{1}{T}\right) + \ln A$$

Plotting $\ln k$ vs $1/T$ yields a straight line with:
- **Slope:** $m = -E_a/R$
- **Y-intercept:** $b = \ln A$

### Two-Point Form

For the same reaction at two different temperatures $T_1$ and $T_2$, with corresponding rate constants $k_1$ and $k_2$:

$$\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

Or equivalently:

$$\ln\left(\frac{k_1}{k_2}\right) = \frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$$

### Worked Example 1: Calculating $E_a$ from Two Temperatures

For the decomposition of $\ce{N2O5}$:

```smiles
O=[N+]([O-])O[N+](=O)[O-]
```

Given: $k_1 = 3.46 \times 10^{-5}$ s⁻¹ at $T_1 = 298$ K, $k_2 = 4.87 \times 10^{-3}$ s⁻¹ at $T_2 = 338$ K. Find $E_a$.

**Solution:**

$$\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$

$$\ln\left(\frac{4.87 \times 10^{-3}}{3.46 \times 10^{-5}}\right) = \frac{E_a}{8.314}\left(\frac{1}{298} - \frac{1}{338}\right)$$

$$\ln(140.75) = \frac{E_a}{8.314}\left(\frac{338-298}{298 \times 338}\right)$$

$$4.947 = \frac{E_a}{8.314}\left(\frac{40}{100724}\right)$$

$$E_a = \frac{4.947 \times 8.314 \times 100724}{40} = 103,600\text{ J·mol}^{-1} = 103.6\text{ kJ·mol}^{-1}$$

### Worked Example 2: Finding $k$ at a New Temperature

For the reaction $\ce{2HI(g) -> H2(g) + I2(g)}$:

```smiles
II
```
```smiles
[HH]
```
```smiles
II
```

Given: $E_a = 183$ kJ·mol⁻¹, $k_1 = 3.02 \times 10^{-5}$ M⁻¹·s⁻¹ at $T_1 = 629$ K. Find $k_2$ at $T_2 = 700$ K.

**Solution:**

$$\ln\left(\frac{k_2}{3.02 \times 10^{-5}}\right) = \frac{183,000}{8.314}\left(\frac{1}{629} - \frac{1}{700}\right)$$

$$\ln\left(\frac{k_2}{3.02 \times 10^{-5}}\right) = 22,011 \times \left(\frac{700-629}{629 \times 700}\right)$$

$$\ln\left(\frac{k_2}{3.02 \times 10^{-5}}\right) = 22,011 \times \frac{71}{440,300} = 3.55$$

$$\frac{k_2}{3.02 \times 10^{-5}} = e^{3.55} = 34.8$$

$$k_2 = 34.8 \times 3.02 \times 10^{-5} = 1.05 \times 10^{-3}\text{ M}^{-1}\text{s}^{-1}$$

A temperature increase of only 71 K (11%) increased the rate constant by a factor of ~35.

### Worked Example 3: Graphical Determination of $E_a$

For the reaction $\ce{2N2O5(g) -> 4NO2(g) + O2(g)}$:

```smiles
O=[N+]([O-])O[N+](=O)[O-]
```
```smiles
N(=O)[O]
```
```smiles
O=O
```

| $T$ (K) | $k$ (s⁻¹) | $1/T$ (K⁻¹) | $\ln k$ |
|---------|-----------|-------------|---------|
| 298 | $3.46 \times 10^{-5}$ | $3.36 \times 10^{-3}$ | $-10.27$ |
| 308 | $1.35 \times 10^{-4}$ | $3.25 \times 10^{-3}$ | $-8.91$ |
| 318 | $4.98 \times 10^{-4}$ | $3.14 \times 10^{-3}$ | $-7.61$ |
| 328 | $1.44 \times 10^{-3}$ | $3.05 \times 10^{-3}$ | $-6.54$ |
| 338 | $4.87 \times 10^{-3}$ | $2.96 \times 10^{-3}$ | $-5.32$ |

The slope of $\ln k$ vs $1/T$ is approximately $-12,400$ K.

$$E_a = -\text{slope} \times R = -(-12,400) \times 8.314 = 103,100\text{ J·mol}^{-1} = 103.1\text{ kJ·mol}^{-1}$$

## 2. Activation Energy

### Definition

**Activation energy ($E_a$)** is the minimum kinetic energy that colliding molecules must possess for a reaction to occur — i.e., the energy barrier that must be overcome for reactants to be converted to products.

### Interpretation on Energy Profile Diagrams

On an energy profile (reaction coordinate) diagram, $E_a$ is the energy difference between the reactants and the **transition state** (activated complex) at the peak of the energy barrier.

For a reaction profile:
- **Forward activation energy ($E_{a,f}$):** Energy from reactants to transition state
- **Reverse activation energy ($E_{a,r}$):** Energy from products to transition state
- **Enthalpy change:** $\Delta H = E_{a,f} - E_{a,r}$

### Exothermic Reaction Energy Profile

```
Energy
  |
  |    /\
  |   /  \  Transition State
  |  /    \
  | / Reactants
  |/        \
  |          \____ Products (lower energy)
  |_________________________
       Reaction Coordinate
```

- $\Delta H < 0$ (heat released)
- $E_{a,\text{reverse}} = E_{a,\text{forward}} + |\Delta H|$
- Example: $\ce{CO(g) + NO2(g) -> CO2(g) + NO(g)}$

### Endothermic Reaction Energy Profile

```
Energy
  |
  |               /\
  |              /  \  Transition State
  |             /    \
  |    Products/      \
  |   ________/        \____ Reactants (lower energy)
  |_________________________
       Reaction Coordinate
```

- $\Delta H > 0$ (heat absorbed)
- $E_{a,\text{reverse}} = E_{a,\text{forward}} - \Delta H$
- Example: $\ce{CO2(g) + NO(g) -> CO(g) + NO2(g)}$

### Relationship to Reaction Rate

- Reactions with **low $E_a$** proceed rapidly (many molecules have sufficient energy)
- Reactions with **high $E_a$** proceed slowly (few molecules have sufficient energy)
- A catalyst provides a pathway with lower $E_a$, increasing the rate

### Effect of Temperature on $E_a$

$E_a$ itself is essentially temperature-independent (it is a property of the reaction pathway). Temperature affects the *fraction of molecules* with energy $\geq E_a$ via the Maxwell-Boltzmann distribution, not $E_a$ itself.

## 3. Reaction Mechanisms (Elementary Steps)

### Elementary Reaction vs Overall Reaction

- An **elementary reaction** is a single-step process where reactants directly form products in one collision or unimolecular event — it cannot be broken down into simpler steps
- An **overall reaction** represents the net chemical change but may occur through a **sequence of elementary steps** called a **reaction mechanism**

### Writing Reaction Mechanisms

A reaction mechanism is a proposed sequence of elementary steps that:
1. Sum to the overall balanced equation
2. Are consistent with the experimentally determined rate law
3. Involve reasonable intermediates

### Intermediates

**Reaction intermediates** are species that are:
- Formed in one elementary step
- Consumed in a subsequent elementary step
- Do **not** appear in the overall balanced equation
- Often highly reactive (radicals, carbocations, unstable complexes)

### Example Mechanism: $\ce{2NO(g) + O2(g) -> 2NO2(g)}$

```smiles
[O]N=O
```
```smiles
O=O
```
```smiles
O=[N+]([O-])[O-]
```

**Proposed two-step mechanism:**

| Step | Elementary Reaction | Molecularity |
|------|-------------------|-------------|
| Step 1 | $\ce{2NO(g) <=> N2O2(g)}$ (fast, equilibrium) | Bimolecular |
| Step 2 | $\ce{N2O2(g) + O2(g) -> 2NO2(g)}$ (slow) | Bimolecular |
| **Overall** | $\ce{2NO(g) + O2(g) -> 2NO2(g)}$ | — |

The intermediate is $\ce{N2O2}$, which is formed in Step 1 and consumed in Step 2.

```smiles
O=NN=O
```

## 4. Rate-Determining Step

### Definition

The **rate-determining step (RDS)** is the slowest elementary step in a reaction mechanism. It acts as a "bottleneck" — the overall reaction cannot proceed faster than this step.

### Determining Rate Law from Mechanism

The rate law of the overall reaction is determined by the **rate-determining step**:

1. Identify the slowest elementary step
2. Write its rate law based on its molecularity
3. If the RDS involves intermediates, express their concentrations in terms of reactants using the fast equilibrium steps

### Example: Validating a Mechanism

**Overall reaction:** $\ce{2NO(g) + 2H2(g) -> N2(g) + 2H2O(g)}$

```smiles
[O]N=O
```
```smiles
[HH]
```
```smiles
N#N
```
```smiles
O
```

**Experimentally determined rate law:** Rate $= k[\ce{NO}]^2[\ce{H2}]$

**Proposed Mechanism A:**

| Step | Reaction | Rate Law |
|------|----------|----------|
| Step 1 (slow) | $\ce{2NO(g) + H2(g) -> N2O(g) + H2O(g)}$ | Rate $= k_1[\ce{NO}]^2[\ce{H2}]$ |
| Step 2 (fast) | $\ce{N2O(g) + H2(g) -> N2(g) + H2O(g)}$ | Rate $= k_2[\ce{N2O}][\ce{H2}]$ |

**Verdict:** Mechanism A is **valid** — Step 1 is rate-determining and its rate law matches the experimental rate law.

**Proposed Mechanism B:**

| Step | Reaction | Rate Law |
|------|----------|----------|
| Step 1 (fast, eq) | $\ce{2NO(g) <=> N2O2(g)}$ | — |
| Step 2 (slow) | $\ce{N2O2(g) + H2(g) -> N2O(g) + H2O(g)}$ | Rate $= k_2[\ce{N2O2}][\ce{H2}]$ |
| Step 3 (fast) | $\ce{N2O(g) + H2(g) -> N2(g) + H2O(g)}$ | — |

From Step 1 equilibrium: $K = [\ce{N2O2}]/[\ce{NO}]^2$, so $[\ce{N2O2}] = K[\ce{NO}]^2$

Substituting into Step 2 rate law: Rate $= k_2 K [\ce{NO}]^2 [\ce{H2}] = k_{\text{obs}}[\ce{NO}]^2[\ce{H2}]$

**Verdict:** Mechanism B is also **valid** — after substitution, the derived rate law matches experiment. This demonstrates that more than one mechanism can be consistent with the same rate law.

## 5. Molecularity

**Molecularity** is the number of reactant molecules (or species) involved in an **elementary step**. It applies only to elementary reactions, not overall reactions.

| Molecularity | Rate Law | Description | Example |
|-------------|----------|-------------|---------|
| **Unimolecular** | Rate $= k[A]$ | A single molecule rearranges or decomposes | $\ce{CH3NC -> CH3CN}$ |
| **Bimolecular** | Rate $= k[A][B]$ or $k[A]^2$ | Two molecules collide and react | $\ce{NO + O3 -> NO2 + O2}$ |
| **Termolecular** | Rate $= k[A][B][C]$ or $k[A]^2[B]$ | Three molecules collide simultaneously | Very rare |

> **Critical distinction:** Molecularity vs Reaction Order
> - **Molecularity** is theoretical — determined from the mechanism (integer: 1, 2, or rarely 3)
> - **Reaction order** is experimental — determined from rate data (can be fractional, zero, or integer)
> - Molecularity applies only to elementary steps; order applies to overall reactions

### Unimolecular Reactions

**Rate law for elementary step:** Rate $= k[A]$

First-order kinetics. Examples:
- Isomerization: $\ce{CH3NC(g) -> CH3CN(g)}$
- Decomposition: $\ce{N2O5(g) -> NO2(g) + NO3(g)}$

### Bimolecular Reactions

**Rate law for elementary step:** Rate $= k[A][B]$ or Rate $= k[A]^2$

Second-order kinetics. Most common type. Examples:
- $\ce{NO(g) + O3(g) -> NO2(g) + O2(g)}$
- $\ce{2NO2(g) -> 2NO(g) + O2(g)}$

```smiles
N(=O)[O]
```
```smiles
O=O[O-]
```
```smiles
O=O
```

### Termolecular Reactions

**Rate law for elementary step:** Rate $= k[A][B][C]$ or $k[A]^2[B]$ or $k[A]^3$

Third-order kinetics. Extremely rare — the probability of three molecules colliding simultaneously with correct orientation and sufficient energy is very low. Examples:
- $\ce{2NO(g) + O2(g) -> 2NO2(g)}$
- $\ce{2NO(g) + Cl2(g) -> 2NOCl(g)}$

> In practice, many reactions that appear termolecular actually proceed through two consecutive bimolecular steps.

## 6. Catalysts and How They Lower Activation Energy

### Definition

A **catalyst** is a substance that increases the rate of a chemical reaction by providing an **alternative reaction pathway** with a lower activation energy. The catalyst is **not consumed** in the overall reaction — it is regenerated.

### How Catalysts Lower $E_a$

A catalyst changes the mechanism to one with a lower energy barrier:
- Forms an intermediate complex with reactants (an alternative, lower-energy transition state)
- The alternative pathway has a lower $E_a$ than the uncatalyzed pathway
- Since $k = Ae^{-E_a/RT}$, a lower $E_a$ means a larger rate constant and faster reaction

**Energy profile comparison (catalyzed vs uncatalyzed):**

| Feature | Uncatalyzed | Catalyzed |
|---------|------------|-----------|
| $E_{a,\text{forward}}$ | Higher | Lower |
| $E_{a,\text{reverse}}$ | Higher (same $\Delta H$ maintained) | Lower |
| $\Delta H$ | Same (reactants and products unchanged) | Same |
| Reactant energy | Same | Same |
| Product energy | Same | Same |
| Transition state energy | Higher peak | Lower peak(s) |

**Critical point:** A catalyst does **not** affect:
- $\Delta H$ of the reaction (enthalpy of reactants and products unchanged)
- Equilibrium position or equilibrium constant
- Thermodynamic spontaneity ($\Delta G$)

A catalyst only affects **kinetics** (rate), not **thermodynamics**.

### Homogeneous Catalysis

- The catalyst is in the **same phase** as the reactants
- Example: $\ce{2H2O2(aq) ->[I-(aq)] 2H2O(l) + O2(g)}$
  - Iodide ions catalyze the decomposition of hydrogen peroxide
  - Both catalyst and reactants are in the aqueous phase

```smiles
OO
```
```smiles
[I-]
```

**Mechanism of iodide-catalyzed $\ce{H2O2}$ decomposition:**
1. $\ce{H2O2 + I- -> H2O + IO-}$ (slow)
2. $\ce{H2O2 + IO- -> H2O + O2 + I-}$ (fast)

The iodide ion is consumed in Step 1 and regenerated in Step 2.

### Heterogeneous Catalysis

- The catalyst is in a **different phase** from the reactants (typically solid catalyst with gaseous or liquid reactants)
- Reaction occurs at the catalyst **surface**
- Examples:
  - **Haber process:** $\ce{N2(g) + 3H2(g) ->[Fe(s)] 2NH3(g)}$ — iron catalyst
  - **Catalytic converters:** Platinum/palladium/rhodium catalysts convert $\ce{CO}$, $\ce{NO_x}$, and hydrocarbons to $\ce{CO2}$, $\ce{N2}$, and $\ce{H2O}$
  - **Hydrogenation:** $\ce{C2H4(g) + H2(g) ->[Ni(s)] C2H6(g)}$ — nickel catalyst

**Mechanism of heterogeneous catalysis:**
1. **Adsorption:** Reactants bind to active sites on the catalyst surface
2. **Reaction:** Bonds break and form on the surface (weakened bonds, lower $E_a$)
3. **Desorption:** Products leave the surface, freeing active sites

### Comparison: Homogeneous vs Heterogeneous

| Feature | Homogeneous | Heterogeneous |
|---------|------------|---------------|
| Phase | Same as reactants | Different from reactants |
| Active site | Individual molecules/ions | Solid surface sites |
| Separation | Difficult (distillation, extraction) | Easy (filtration) |
| Selectivity | High | Moderate |
| Example | Acid-catalyzed esterification | Haber process (Fe catalyst) |

## 7. Enzyme Kinetics Basics

### What Are Enzymes?

Enzymes are biological catalysts — typically proteins — that dramatically accelerate biochemical reactions with high specificity. They are homogeneous catalysts operating in aqueous biological environments.

### Key Terminology

| Term | Definition |
|------|------------|
| **Substrate (S)** | The reactant molecule that binds to the enzyme |
| **Active site** | The specific region of the enzyme where the substrate binds and the reaction occurs |
| **Enzyme-substrate complex (ES)** | The intermediate formed when substrate binds to the active site |
| **Product (P)** | The molecule released after the reaction |
| **Turnover number ($k_{\text{cat}}$)** | Maximum number of substrate molecules converted to product per enzyme molecule per second |

### General Enzyme-Catalyzed Reaction

$$\ce{E + S <=>[k_1][k_{-1}] ES ->[k_2] E + P}$$

```smiles
CC(=O)OCC  # Ethyl acetate (example substrate)
```
```smiles
O       # Water
```

### Michaelis-Menten Kinetics

Leonor Michaelis and Maud Menten (1913) developed a model describing the rate of enzyme-catalyzed reactions.

**Key Assumptions:**
1. The enzyme and substrate form an enzyme-substrate complex (ES)
2. The ES complex formation is in rapid equilibrium (or steady state)
3. The rate-determining step is the breakdown of ES to product
4. $[\ce{S}] \gg [\ce{E}]$ (substrate in large excess)

### The Michaelis-Menten Equation

$$v = \frac{V_{\text{max}}[S]}{K_m + [S]}$$

Where:
- $v$ = initial reaction rate (velocity)
- $V_{\text{max}}$ = maximum reaction rate (when all enzyme active sites are saturated with substrate)
- $[S]$ = substrate concentration
- $K_m$ = Michaelis constant (the substrate concentration at which $v = V_{\text{max}}/2$)

### Interpreting $K_m$

$K_m$ is a measure of the **affinity** of the enzyme for its substrate:
- **Low $K_m$** → high affinity (enzyme binds substrate tightly; reaches $V_{\text{max}}/2$ at low $[S]$)
- **High $K_m$** → low affinity (enzyme binds substrate weakly; needs high $[S]$ to reach $V_{\text{max}}/2$)

$$K_m = \frac{k_{-1} + k_2}{k_1}$$

When $k_2 \ll k_{-1}$ (dissociation of ES is much faster than product formation), $K_m \approx k_{-1}/k_1 = K_d$ (the dissociation constant of ES).

### $V_{\text{max}}$ and Turnover Number

$$V_{\text{max}} = k_2 [E]_{\text{total}}$$

The **turnover number** ($k_{\text{cat}}$) is the maximum number of substrate molecules one enzyme molecule converts per second:

$$k_{\text{cat}} = \frac{V_{\text{max}}}{[E]_{\text{total}}}$$

Typical values: $k_{\text{cat}}$ ranges from $10^{-1}$ to $10^7$ s⁻¹ (carbonic anhydrase: ~$10^6$ s⁻¹).

### Analysis of Michaelis-Menten Kinetics

| Condition | Rate | Interpretation |
|-----------|------|----------------|
| $[S] \ll K_m$ | $v \approx \frac{V_{\text{max}}}{K_m}[S]$ | First-order in $[S]$ |
| $[S] = K_m$ | $v = \frac{V_{\text{max}}}{2}$ | Half-maximum velocity |
| $[S] \gg K_m$ | $v \approx V_{\text{max}}$ | Zero-order in $[S]$ (saturated) |

### Lineweaver-Burk Plot (Double Reciprocal)

Taking the reciprocal of the Michaelis-Menten equation:

$$\frac{1}{v} = \frac{K_m}{V_{\text{max}}}\frac{1}{[S]} + \frac{1}{V_{\text{max}}}$$

A plot of $1/v$ vs $1/[S]$ yields a straight line:
- **Slope:** $K_m/V_{\text{max}}$
- **Y-intercept:** $1/V_{\text{max}}$
- **X-intercept:** $-1/K_m$

This linearized form is used experimentally to determine $K_m$ and $V_{\text{max}}$ from initial rate measurements at various substrate concentrations.

### Enzyme Inhibition

Inhibitors reduce enzyme activity:

| Type | Binding Site | Effect on $V_{\text{max}}$ | Effect on $K_m$ |
|------|-------------|--------------------------|----------------|
| **Competitive** | Active site (competes with S) | Unchanged | Increases |
| **Non-competitive** | Allosteric site (not active site) | Decreases | Unchanged |
| **Uncompetitive** | ES complex only | Decreases | Decreases |

### Biological Significance

Enzymes are essential for life:
- **Specificity:** Each enzyme catalyzes a specific reaction (lock-and-key model, induced fit model)
- **Regulation:** Enzyme activity can be controlled (feedback inhibition, allosteric regulation)
- **Efficiency:** Enzymes can accelerate reactions by factors of $10^6$ to $10^{17}$
- **Mild conditions:** Operate at physiological temperature (~37°C) and pH (~7.4)

## Key Equations Summary

| Equation | Description |
|----------|-------------|
| $k = Ae^{-E_a/RT}$ | Arrhenius equation |
| $\ln k = \ln A - E_a/RT$ | Logarithmic Arrhenius form |
| $\ln\left(\frac{k_2}{k_1}\right) = \frac{E_a}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$ | Two-point Arrhenius form |
| Rate $= k[A]^m[B]^n$ | Rate law (elementary steps: $m,n$ = molecularity) |
| $v = \frac{V_{\text{max}}[S]}{K_m + [S]}$ | Michaelis-Menten equation |
| $\frac{1}{v} = \frac{K_m}{V_{\text{max}}}\frac{1}{[S]} + \frac{1}{V_{\text{max}}}$ | Lineweaver-Burk equation |
| $k_{\text{cat}} = V_{\text{max}}/[E]_{\text{total}}$ | Turnover number |
| $\Delta H = E_{a,f} - E_{a,r}$ | Enthalpy from activation energies |

## Related Concepts

- [[Kinetic Chemistry]] — Part 1 of this lecture series (reaction rates, rate laws, integrated rate laws, collision theory)
- [[Thermochemistry]] — activation energy connects kinetics to thermodynamics
- [[Chemical Equilibrium]] — kinetics determines how fast equilibrium is approached

## Previous Lecture

- [[FAD1018 W16 — Kinetic Chemistry]] — Part 1: reaction rates, rate laws, half-life, collision theory, transition state theory

## Lecturer

[[Mr. Muhammad Hafiz Husna Bin Hasnan]] — Chemistry Division, UM

## Related

- [[FAD1018 - Basic Chemistry II]] — main course page
