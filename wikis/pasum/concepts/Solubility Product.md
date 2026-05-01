---
title: "Solubility Product"
date: 2026-04-27
tags:
  - concept/chemistry
  - topic/physical-chemistry
  - status/evergreen
---

# Solubility Product ($K_{sp}$)

The equilibrium constant for the dissolution of a sparingly soluble ionic compound in water. $K_{sp}$ indicates how soluble the solid is in water.

## Definition

For a general dissolution:

```smiles
[A].[B]
```
$$\text{A}_a\text{B}_b(s) \rightleftharpoons a\text{A}^{m+}(aq) + b\text{B}^{n-}(aq)$$

| | Molar Solubility |
|---|---|
| | $s$ | $as$ | $bs$ |

$$K_{sp} = [\text{A}^{m+}]^a[\text{B}^{n-}]^b = (as)^a(bs)^b$$

$$\text{unit } K_{sp} = (\text{concentration})^{a+b}$$

- Pure solid is omitted (activity = 1)
- $K_{sp}$ is temperature-dependent
- The **smaller** the $K_{sp}$ value, the **less soluble** the compound in water
- $K_{sp} \downarrow$, solubility $\downarrow$; $T \uparrow$, solubility $\uparrow$, $K_{sp} \uparrow$

## Solubility vs Molar Solubility

| | Solubility | Molar Solubility |
|---|---|---|
| **Definition** | Maximum amount of solute (g) that dissolves in a known volume of solvent (L) to form a saturated solution | Number of moles of solute in 1 L (or 1 dm³) of saturated solution |
| **Unit** | g L⁻¹ or g dm⁻³ | mol L⁻¹ or mol dm⁻³ |
| **Conversion** | $\div$ Molar mass | $\times$ Molar mass |

> [!important] $K_{sp}$ is **not** the same as solubility
> $K_{sp}$ is an equilibrium constant; solubility is a concentration.

## Molar Solubility Calculations

### 1:1 Ratio (e.g., AgCl)

```smiles
[Ag+].[Cl-]
```
$$\text{AgCl}(s) \rightleftharpoons \text{Ag}^+(aq) + \text{Cl}^-(aq)$$
$$K_{sp} = s^2 \quad \Rightarrow \quad s = \sqrt{K_{sp}}$$

### 1:2 or 2:1 Ratio (e.g., CaF₂)

```smiles
[Ca+2].[F-].[F-]
```
$$\text{CaF}_2(s) \rightleftharpoons \text{Ca}^{2+}(aq) + 2\text{F}^-(aq)$$
$$K_{sp} = 4s^3 \quad \Rightarrow \quad s = \sqrt[3]{\frac{K_{sp}}{4}}$$

### 1:3 or 3:1 Ratio (e.g., LaF₃)

```smiles
[La+3].[F-].[F-].[F-]
```
$$\text{LaF}_3(s) \rightleftharpoons \text{La}^{3+}(aq) + 3\text{F}^-(aq)$$
$$s = \sqrt[4]{\frac{K_{sp}}{27}}$$

## Common Ion Effect

If one of the ions in a solution equilibrium is already dissolved in the solution, the equilibrium shifts to the **left** (Le Chatelier's principle) and the solubility of the salt **decreases**.

In general, the solubility of a slightly soluble salt decreases in the presence of a second solute that provides a common ion.

> [!important] $K_{sp}$ remains constant
> At a given temperature, only the **solubility** is altered by the common-ion effect. The **solubility product** ($K_{sp}$), being an equilibrium constant, remains the same whether or not other substances are present.

**Example — AgI in NaI:**

```smiles
[Ag+].[I-]
```
- In pure water: $s = 9.23 \times 10^{-9}$ M
- In 0.274 M NaI: $s = 3.11 \times 10^{-16}$ M

The molar solubility of AgI is **much smaller** in NaI solution due to the common ion $\text{I}^-$.

**Example — CaF₂:**
- In pure water: $s = 2.1 \times 10^{-4}$ M
- In 0.010 M $\text{Ca}^{2+}$: $s = 3.1 \times 10^{-5}$ M
- In 0.010 M $\text{F}^-$: $s = 3.9 \times 10^{-7}$ M

The effect of $\text{F}^-$ is **more pronounced** than $\text{Ca}^{2+}$ because $[\text{F}^-]$ appears to the **second power** in the $K_{sp}$ expression for $\text{CaF}_2$, whereas $\text{Ca}^{2+}$ appears to the **first power**.

## Solubility Quotient ($Q$)

The **ion product** $Q$ (also called the solubility quotient) uses **initial concentrations** (not equilibrium concentrations). Its expression has the same form as $K_{sp}$:

$$Q = [\text{A}^+]_0[\text{B}^-]_0$$

The subscript 0 reminds us that these are initial concentrations.

### Precipitation Prediction

| Condition | Meaning |
|-----------|---------|
| $Q < K_{sp}$ | Unsaturated solution; no precipitate forms |
| $Q = K_{sp}$ | Saturated solution; at equilibrium (point of precipitation) |
| $Q > K_{sp}$ | Supersaturated solution; precipitate will form |

A precipitate will form **only when $Q > K_{sp}$**.

**Procedure for mixed solutions:**
1. Calculate moles of each ion before mixing
2. Find total volume after mixing
3. Calculate new concentrations
4. Compute $Q$ and compare to $K_{sp}$

## Selective Precipitation

Separating ions by controlled precipitation based on different $K_{sp}$ values. Separation by using a reagent that forms a precipitate with one or more (but not all) ions is called **selective precipitation**.

**Example — separating Ag⁺ and Pb²⁺ by adding Cl⁻:**

Solution contains $1.0 \times 10^{-2}$ M $\text{Ag}^+$ and $2.0 \times 10^{-2}$ M $\text{Pb}^{2+}$.
- $\text{AgCl}$ ($K_{sp} = 1.8 \times 10^{-10}$)
- $\text{PbCl}_2$ ($K_{sp} = 1.7 \times 10^{-5}$)
  ```smiles
  [Pb+2].[Cl-].[Cl-]
  ```

$[\text{Cl}^-]$ to begin $\text{AgCl}$ precipitation:
$$[\text{Cl}^-] = \frac{K_{sp}}{[\text{Ag}^+]} = \frac{1.8 \times 10^{-10}}{1.0 \times 10^{-2}} = 1.8 \times 10^{-8} \text{ M}$$

$[\text{Cl}^-]$ to begin $\text{PbCl}_2$ precipitation:
$$[\text{Cl}^-] = \sqrt{\frac{K_{sp}}{[\text{Pb}^{2+}]}} = \sqrt{\frac{1.7 \times 10^{-5}}{2.0 \times 10^{-2}}} = 2.9 \times 10^{-2} \text{ M}$$

**Separation window:** Keep $[\text{Cl}^-]$ between $1.8 \times 10^{-8}$ M and $2.9 \times 10^{-2}$ M to selectively precipitate $\text{Ag}^+$ while $\text{Pb}^{2+}$ remains in solution.

> [!tip] Which salt precipitates first?
> The salt with the **smaller $K_{sp}$** precipitates first **only if the stoichiometry is the same**. For different stoichiometries, calculate the required reagent concentration for each.

## Common $K_{sp}$ Values (at 25°C)

| Compound | $K_{sp}$ |
|----------|----------|
| $\text{Al(OH)}_3$ | $1.8 \times 10^{-33}$ |
| $\text{BaCO}_3$ | $8.1 \times 10^{-9}$ |
| $\text{BaSO}_4$ | $1.1 \times 10^{-10}$ |
| $\text{CaCO}_3$ | $8.7 \times 10^{-9}$ |
| $\text{CaF}_2$ | $4.0 \times 10^{-11}$ |
| $\text{Ca(OH)}_2$ | $8.0 \times 10^{-6}$ |
| $\text{Ca}_3(\text{PO}_4)_2$ | $1.2 \times 10^{-26}$ |
| $\text{Fe(OH)}_3$ | $1.1 \times 10^{-36}$ |
| $\text{Mg(OH)}_2$ | $1.2 \times 10^{-11}$ |
| AgCl | $1.6 \times 10^{-10}$ |
| AgBr | $7.7 \times 10^{-13}$ |
| AgI | $8.3 \times 10^{-17}$ |
| $\text{Ag}_2\text{CrO}_4$ | $1.4 \times 10^{-5}$ |
| $\text{Ag}_2\text{S}$ | $6.0 \times 10^{-51}$ |
| $\text{PbCl}_2$ | $2.4 \times 10^{-4}$ |
| $\text{PbCrO}_4$ | $2.0 \times 10^{-14}$ |
| $\text{PbS}$ | $3.4 \times 10^{-28}$ |
| $\text{Zn(OH)}_2$ | $1.8 \times 10^{-14}$ |

## Related Topics
- [[Ionic Equilibria]] — Acid-base equilibria
- [[Chemical Equilibrium]] — General equilibrium concepts
- [[Le Chatelier's Principle]] — Equilibrium shifts
- [[Solubility Rules]] — Predicting precipitation

## Sources
- [[FAD1018 W4 — Solubility Product]] — Primary lecture source (ChM Wan Nurhidayah)
- [[FAD1018 - Basic Chemistry II]]
