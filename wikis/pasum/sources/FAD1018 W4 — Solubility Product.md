---
title: "FAD1018 W4 — Solubility Product"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1018
  - topic/solubility-product
  - status/evergreen
week: 4
lecturer: "[[ChM Wan Nurhidayah Binti A Karim]]"
---

# FAD1018 W4 — Solubility Product

Week 4 lecture on solubility equilibria, covering dissolution/precipitation of ionic compounds, solubility product constant ($K_{sp}$), molar solubility, the ion product $Q$, selective precipitation, and the common-ion effect.

## Learning Outcomes

At the end of this topic, students should be able to:
- Identify soluble and insoluble compounds
- Write solubility equilibrium equations
- Define saturated solution, solubility, and molar solubility
- Write solubility product expressions ($K_{sp}$)
- Calculate $K_{sp}$ from solubility data and vice versa
- Write and apply the solubility quotient $Q$ to predict precipitation
- Understand separation of ions by fractional precipitation
- Define and describe the common-ion effect using Le Chatelier's principle
- Perform calculations involving common ions

---

## 1. Introduction to Solubility Equilibria

Dissolution and precipitation of ionic compounds are **heterogeneous reactions** — they involve equilibria between a solid phase and an aqueous phase.

### Solubility Equilibrium Equation

**Dissolving (ionization/dissociation):**

```smiles
[Ag+].[Cl-]
```
$$\text{AgCl}(s) \rightleftharpoons \text{Ag}^+(aq) + \text{Cl}^-(aq)$$

```smiles
[Ca+2].[S-2]
```
$$\text{CaS}(s) \rightleftharpoons \text{Ca}^{2+}(aq) + \text{S}^{2-}(aq)$$

```smiles
[Ca+2].[F-].[F-]
```
$$\text{CaF}_2(s) \rightleftharpoons \text{Ca}^{2+}(aq) + 2\text{F}^-(aq)$$

**Precipitating (reverse):**
$$\text{Ag}^+(aq) + \text{Cl}^-(aq) \rightleftharpoons \text{AgCl}(s)$$

---

## 2. Saturated Solutions

| Type | Definition |
|------|------------|
| **Unsaturated** | Dissolves less solute than needed to form a saturated solution; contains less solute than it has the capacity to dissolve |
| **Saturated** | Solution that contains the **maximum possible quantity** of dissolved solute at a given temperature; in equilibrium with undissolved solute |
| **Supersaturated** | Contains more solute than is present in a saturated solution (metastable) |

For the dissolution of an ionic solid, the saturated solution is one in which the solution is in contact with undissolved solute. The equilibrium constant for this dissolution is called the **solubility-product constant** ($K_{sp}$).

**Example:**

```smiles
[Ba+2].[O-]S(=O)(=O)[O-]
```
$$\text{BaSO}_4(s) \rightleftharpoons \text{Ba}^{2+}(aq) + \text{SO}_4^{2-}(aq)$$

$$K_{sp} = [\text{Ba}^{2+}][\text{SO}_4^{2-}]$$

---

## 3. Soluble and Insoluble Compounds (Recap)

| Soluble Compounds | Insoluble Exceptions |
|-------------------|----------------------|
| All nitrate salts | None |
| All sulfate salts | $\text{PbSO}_4$, $\text{BaSO}_4$, $\text{CaSO}_4$ |
| All chloride, bromide, iodide salts | $\text{Hg}_2\text{Cl}_2$, $\text{PbCl}_2$, $\text{AgCl}$ (and corresponding bromides/iodides) |
| $\text{Na}_2\text{CO}_3$, $\text{K}_2\text{CO}_3$, $(\text{NH}_4)_2\text{CO}_3$ | Other carbonate salts |
| All ammonium, sodium, potassium salts | None |
| All Group 1 salts + $\text{NH}_4^+$ | None |
| Acetates, chlorates, perchlorates | Most sulfides ($\text{S}^{2-}$) |
| Group 1 hydroxides and carbonates | Most hydroxides and carbonates |
| $\text{Ca(OH)}_2$ slightly soluble; Group 2 Sr and Ba hydroxides soluble | |

---

## 4. Solubility Product Constant, $K_{sp}$

$K_{sp}$ is the product of the molar concentrations of the constituent ions, each raised to the power of its stoichiometric coefficient.

**General form:**

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
- The **smaller** the $K_{sp}$ value, the **less soluble** the compound in water
- $K_{sp}$ is **temperature-dependent**

### Writing $K_{sp}$ Expressions — Lecture Examples

```smiles
[Pb+2].[Cl-].[Cl-]
```
$$\text{PbCl}_2(s) \rightleftharpoons \text{Pb}^{2+}(aq) + 2\text{Cl}^-(aq)$$
$$K_{sp} = [\text{Pb}^{2+}][\text{Cl}^-]^2$$

```smiles
[Fe+3].[OH-].[OH-].[OH-]
```
$$\text{Fe(OH)}_3(s) \rightleftharpoons \text{Fe}^{3+}(aq) + 3\text{OH}^-(aq)$$
$$K_{sp} = [\text{Fe}^{3+}][\text{OH}^-]^3$$

```smiles
[Ag+].[Ag+].[O-][Cr](=O)(=O)[O-]
```
$$\text{Ag}_2\text{CrO}_4(s) \rightleftharpoons 2\text{Ag}^+(aq) + \text{CrO}_4^{2-}(aq)$$
$$K_{sp} = [\text{Ag}^+]^2[\text{CrO}_4^{2-}]$$

```smiles
[As+3].[As+3].[S-2].[S-2].[S-2]
```
$$\text{As}_2\text{S}_3(s) \rightleftharpoons 2\text{As}^{3+}(aq) + 3\text{S}^{2-}(aq)$$
$$K_{sp} = [\text{As}^{3+}]^2[\text{S}^{2-}]^3$$

```smiles
[Ca+2].[Ca+2].[Ca+2].[O-]P(=O)([O-])[O-].[O-]P(=O)([O-])[O-]
```
$$\text{Ca}_3(\text{PO}_4)_2(s) \rightleftharpoons 3\text{Ca}^{2+}(aq) + 2\text{PO}_4^{3-}(aq)$$
$$K_{sp} = [\text{Ca}^{2+}]^3[\text{PO}_4^{3-}]^2$$

---

## 5. Solubility vs Molar Solubility

| | Solubility | Molar Solubility |
|---|---|---|
| **Definition** | Maximum amount of solute (g) that dissolves in a known volume of solvent (L) to form a saturated solution | Number of moles of solute in 1 L (or 1 dm³) of saturated solution |
| **Unit** | g L⁻¹ or g dm⁻³ | mol L⁻¹ or mol dm⁻³ |
| **Conversion** | $\div$ Molar mass | $\times$ Molar mass |

**Key distinction:** $K_{sp}$ is **not** the same as solubility. $K_{sp}$ is an equilibrium constant; solubility is a concentration.

---

## 6. Calculating $K_{sp}$ from Solubility

**Sample:** The solubility of PbS is $8.36 \times 10^{-14}$ mol L⁻¹. Calculate $K_{sp}$.

```smiles
[Pb+2].[S-2]
```
$$\text{PbS}(s) \rightleftharpoons \text{Pb}^{2+}(aq) + \text{S}^{2-}(aq)$$

$$K_{sp} = (s)(s) = (8.36 \times 10^{-14})^2 = 6.99 \times 10^{-27} \text{ mol}^2\text{ L}^{-2}$$

**Sample:** Molar solubility of $\text{Pb(IO}_3)_2$ is $4.0 \times 10^{-5}$ mol L⁻¹. Calculate $K_{sp}$.

```smiles
[Pb+2].[O-]I(=O)=O.[O-]I(=O)=O
```
$$\text{Pb(IO}_3)_2(s) \rightleftharpoons \text{Pb}^{2+}(aq) + 2\text{IO}_3^-(aq)$$

$$K_{sp} = (s)(2s)^2 = 4s^3 = 4(4.0 \times 10^{-5})^3 = 2.56 \times 10^{-13} \text{ mol}^3\text{ L}^{-3}$$

---

## 7. Calculating Solubility from $K_{sp}$

**Sample:** What are $[\text{Ag}^+]$ and $[\text{CrO}_4^{2-}]$ in a saturated solution of $\text{Ag}_2\text{CrO}_4$? Given $K_{sp} = 1.9 \times 10^{-12}$.

```smiles
[Ag+].[Ag+].[O-][Cr](=O)(=O)[O-]
```
$$\text{Ag}_2\text{CrO}_4(s) \rightleftharpoons 2\text{Ag}^+(aq) + \text{CrO}_4^{2-}(aq)$$

$$K_{sp} = (2s)^2(s) = 4s^3 = 1.9 \times 10^{-12}$$

$$s = 7.8 \times 10^{-5} \text{ mol L}^{-1}$$

$$[\text{Ag}^+] = 2s = 1.6 \times 10^{-4} \text{ M}; \quad [\text{CrO}_4^{2-}] = s = 7.8 \times 10^{-5} \text{ M}$$

**Sample:** Calculate molar solubility of AgCl given $K_{sp} = 1.56 \times 10^{-10}$.

$$s = \sqrt{K_{sp}} = \sqrt{1.56 \times 10^{-10}} = 1.25 \times 10^{-5} \text{ M}$$

Solubility in g L⁻¹: $1.25 \times 10^{-5} \times 143.5 = 1.79 \times 10^{-3}$ g L⁻¹

---

## 8. Solubility Quotient, $Q$

The **ion product** $Q$ uses **initial concentrations** (not equilibrium concentrations):

$$Q = [\text{A}^+]_0[\text{B}^-]_0$$

The expression for $Q$ is the same form as $K_{sp}$.

| Condition | Meaning |
|-----------|---------|
| $Q < K_{sp}$ | Unsaturated solution — no precipitate forms |
| $Q = K_{sp}$ | Solution at saturation point (point of precipitation) |
| $Q > K_{sp}$ | Supersaturated solution — precipitate forms |

### Predicting Precipitation — Lecture Examples

**Example 1:** $[\text{Mg}^{2+}] = 1.5 \times 10^{-6}$ M, $[\text{OH}^-] = 1.0 \times 10^{-4}$ M. Will $\text{Mg(OH)}_2$ precipitate? ($K_{sp} = 5.6 \times 10^{-12}$)

```smiles
[Mg+2].[OH-].[OH-]
```
$$\text{Mg(OH)}_2(s) \rightleftharpoons \text{Mg}^{2+}(aq) + 2\text{OH}^-(aq)$$

$$Q = (1.5 \times 10^{-6})(1.0 \times 10^{-4})^2 = 1.5 \times 10^{-14}$$

$Q < K_{sp}$ → **No precipitate forms** (unsaturated)

**Example 2:** 200 mL of 0.004 M $\text{BaCl}_2$ + 600 mL of 0.008 M $\text{K}_2\text{SO}_4$. Will $\text{BaSO}_4$ precipitate? ($K_{sp} = 1.1 \times 10^{-10}$)

After mixing (total volume = 0.8 L):
- $[\text{Ba}^{2+}] = 0.001$ M
- $[\text{SO}_4^{2-}] = 0.006$ M

$$Q = (0.001)(0.006) = 6 \times 10^{-6}$$

$Q > K_{sp}$ → **Precipitate forms** (supersaturated)

**Example 3:** What $[\text{SO}_4^{2-}]$ is required to just begin precipitating $\text{BaSO}_4$ when $[\text{Ba}^{2+}] = 0.01$ M?

$$K_{sp} = [\text{Ba}^{2+}][\text{SO}_4^{2-}]$$
$$1.1 \times 10^{-10} = (0.01)[\text{SO}_4^{2-}]$$
$$[\text{SO}_4^{2-}] = 1.1 \times 10^{-8} \text{ M}$$

Precipitation begins when $[\text{SO}_4^{2-}] > 1.1 \times 10^{-8}$ M.

---

## 9. Selective Precipitation of Ions

Ions can be separated based on the different solubilities of their salts. Separation by using a reagent that forms a precipitate with one or more (but not all) ions is called **selective precipitation**.

**Lecture example:** Solution contains $1.0 \times 10^{-2}$ M $\text{Ag}^+$ and $2.0 \times 10^{-2}$ M $\text{Pb}^{2+}$. When $\text{Cl}^-$ is added:
- $\text{AgCl}$ ($K_{sp} = 1.8 \times 10^{-10}$)
- $\text{PbCl}_2$ ($K_{sp} = 1.7 \times 10^{-5}$)

**Which precipitates first?** $\text{AgCl}$ (smaller $K_{sp}$)

$[\text{Cl}^-]$ to begin $\text{AgCl}$ precipitation:
$$[\text{Cl}^-] = \frac{1.8 \times 10^{-10}}{1.0 \times 10^{-2}} = 1.8 \times 10^{-8} \text{ M}$$

$[\text{Cl}^-]$ to begin $\text{PbCl}_2$ precipitation:
$$[\text{Cl}^-] = \sqrt{\frac{1.7 \times 10^{-5}}{2.0 \times 10^{-2}}} = 2.9 \times 10^{-2} \text{ M}$$

**Separation window:** $\text{Ag}^+$ can be separated from $\text{Pb}^{2+}$ by keeping $[\text{Cl}^-]$ between $1.8 \times 10^{-8}$ M and $2.9 \times 10^{-2}$ M.

---

## 10. Common-Ion Effect

If one of the ions in a solution equilibrium is already dissolved in the solution, the equilibrium shifts to the **left** (Le Chatelier's principle) and the solubility of the salt **decreases**.

**General statement:** The solubility of a slightly soluble salt decreases in the presence of a second solute that provides a common ion.

**Key point:** At a given temperature, only the **solubility** is altered by the common-ion effect. The **solubility product** ($K_{sp}$), being an equilibrium constant, remains the same.

### Lecture Examples

**Example 1:** Molar solubility of $\text{Mg(OH)}_2$ in 0.1 M NaOH? ($K_{sp} = 1.2 \times 10^{-11}$)

```smiles
[Mg+2].[OH-].[OH-]
```
$$\text{Mg(OH)}_2(s) \rightleftharpoons \text{Mg}^{2+}(aq) + 2\text{OH}^-(aq)$$

| | $\text{Mg(OH)}_2(s)$ | $\rightleftharpoons$ | $\text{Mg}^{2+}(aq)$ | $2\text{OH}^-(aq)$ |
|---|---|---|---|---|
| Initial (M) | — | | 0.0 | 0.1 (from NaOH) |
| Change (M) | $-s$ | | $+s$ | $+2s$ |
| Equilibrium (M) | — | | $s$ | $0.1 + 2s \approx 0.1$ |

$$K_{sp} = (s)(0.1)^2 = 1.2 \times 10^{-11}$$
$$s = 1.2 \times 10^{-9} \text{ M}$$

**Example 2:** Molar solubility of AgI in 0.274 M NaI? ($K_{sp} = 8.52 \times 10^{-17}$)

```smiles
[Ag+].[I-]
```
$$\text{AgI}(s) \rightleftharpoons \text{Ag}^+(aq) + \text{I}^-(aq)$$

$$s = \frac{8.52 \times 10^{-17}}{0.274} = 3.11 \times 10^{-16} \text{ M}$$

In pure water: $s = \sqrt{8.52 \times 10^{-17}} = 9.23 \times 10^{-9}$ M

**Molar solubility of AgI is much smaller in NaI** due to the common ion $\text{I}^-$.

**Example 3:** $\text{CaF}_2$ ($K_{sp} = 3.9 \times 10^{-11}$)
- In pure water: $s = 2.1 \times 10^{-4}$ M
- In 0.010 M $\text{Ca}^{2+}$: $s = 3.1 \times 10^{-5}$ M
- In 0.010 M $\text{F}^-$: $s = 3.9 \times 10^{-7}$ M

The effect of $\text{F}^-$ is more pronounced than $\text{Ca}^{2+}$ because $[\text{F}^-]$ appears to the **second power** in the $K_{sp}$ expression, whereas $\text{Ca}^{2+}$ appears to the **first power**.

---

## Key Lecture Data: $K_{sp}$ Values at 25°C

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
| $\text{PbCl}_2$ | $2.4 \times 10^{-4}$ |
| $\text{PbCrO}_4$ | $2.0 \times 10^{-14}$ |
| $\text{PbS}$ | $3.4 \times 10^{-28}$ |
| AgCl | $1.6 \times 10^{-10}$ |
| AgBr | $7.7 \times 10^{-13}$ |
| AgI | $8.3 \times 10^{-17}$ |
| $\text{Ag}_2\text{CrO}_4$ | $1.4 \times 10^{-5}$ |
| $\text{Ag}_2\text{S}$ | $6.0 \times 10^{-51}$ |
| $\text{Zn(OH)}_2$ | $1.8 \times 10^{-14}$ |

---

## Related Topics

- [[Chemical Equilibrium]] — General equilibrium principles
- [[Ionic Equilibria]] — Acid-base equilibria foundation
- [[Le Chatelier's Principle]] — Equilibrium shifts
- [[Solubility Rules]] — Predicting precipitation from ionic equations

## Related Course Page

- [[FAD1018 - Basic Chemistry II]]

---

> [!warning] Variable exam presence
> Solubility Product has ~5–11% mark weight but was absent in 2023/24 and 2024/25 papers. May return this year.
