---
title: "Chemical Equilibrium"
date: 2026-04-27
tags:
  - concept/chemistry
  - topic/physical-chemistry
  - status/seedling
---

# Chemical Equilibrium

A state in which the rate of the forward reaction equals the rate of the reverse reaction, resulting in constant concentrations of reactants and products over time.

## Definition

Dynamic equilibrium occurs in reversible reactions when:
- Forward reaction rate = Reverse reaction rate
- Concentrations of reactants and products remain constant (but not necessarily equal)
- The system is closed (no exchange with surroundings)
- Macroscopic properties are constant

## Key Concepts

### Equilibrium Constant (Kc)
For a general reaction: aA + bB ⇌ cC + dD

$$K_c = \frac{[C]^c[D]^d}{[A]^a[B]^b}$$

- Square brackets denote molar concentrations
- Pure solids and liquids are omitted (activity = 1)
- Kc is temperature-dependent only

### Equilibrium Constant (Kp)
For gaseous reactions:

$$K_p = \frac{(P_C)^c(P_D)^d}{(P_A)^a(P_B)^b}$$

### Relationship between Kc and Kp
$$K_p = K_c(RT)^{\Delta n}$$

Where:
- R = gas constant (0.0821 L·atm/mol·K)
- T = temperature in Kelvin
- Δn = moles of gaseous products - moles of gaseous reactants

### Reaction Quotient (Q)
Used to predict direction of reaction:
- Q < K: Reaction proceeds forward (to the right)
- Q > K: Reaction proceeds backward (to the left)
- Q = K: System at equilibrium

## Le Chatelier's Principle

> If a dynamic equilibrium is disturbed by changing the conditions, the position of equilibrium moves to counteract the disturbance.

### Factors Affecting Equilibrium

| Factor | Change | Effect on Equilibrium |
|--------|--------|----------------------|
| Concentration | Increase reactant | Shifts toward products |
| Pressure | Increase (decrease volume) | Shifts toward fewer moles of gas |
| Temperature | Increase (exothermic) | Shifts toward reactants |
| Temperature | Increase (endothermic) | Shifts toward products |
| Catalyst | Add | No shift; speeds both directions equally |

## Magnitude of K

| K Value | Interpretation |
|---------|---------------|
| K >> 1 | Products favored at equilibrium |
| K ≈ 1 | Significant amounts of both reactants and products |
| K << 1 | Reactants favored at equilibrium |

## Ionic Equilibria (Acid-Base Equilibrium)

Ionic equilibria describe the reversible dissociation of weak acids and bases in aqueous solution, governed by the same equilibrium principles as $K_c$ and $K_p$.

### Auto-Ionisation of Water

Water undergoes auto-ionisation:
$$H_2O(l) + H_2O(l) \rightleftharpoons H_3O^+(aq) + OH^-(aq)$$

The **ionic product of water**:
$$K_w = [H_3O^+][OH^-] = [H^+][OH^-]$$

At **298 K (25 °C)**:
$$K_w = 1.0 \times 10^{-14} \text{ mol}^2 \text{ dm}^{-6}$$

Taking negative logarithms:
$$pH + pOH = 14 \quad \text{where} \quad pH = -\log[H^+], \quad pOH = -\log[OH^-]$$

> [!note] Temperature Dependence
> Water ionisation is **endothermic**, so $K_w$ increases with temperature.
>
> | Temperature (°C) | $K_w$ (mol² dm⁻⁶) |
> |------------------|-------------------|
> | 0 | $1.1 \times 10^{-15}$ |
> | 20 | $6.8 \times 10^{-15}$ |
> | 50 | $5.5 \times 10^{-14}$ |
> | 100 | $5.1 \times 10^{-13}$ |

```smiles
O                  # H2O
[OH3+]             # H3O+
[OH-]              # OH-
```

### Degree of Dissociation ($\alpha$)

For weak acids and weak bases that only partially dissociate:

**Weak acid:**
$$\alpha = \frac{[H_3O^+]_{\text{eq}}}{[HA]_0} \quad \text{or} \quad \%\alpha = \frac{[H_3O^+]_{\text{eq}}}{[HA]_0} \times 100\%$$

**Weak base:**
$$\alpha = \frac{[OH^-]_{\text{eq}}}{[B]_0} \quad \text{or} \quad \%\alpha = \frac{[OH^-]_{\text{eq}}}{[B]_0} \times 100\%$$

> [!important] Key Properties
> - For weak acids/bases: $\alpha < 1$ (or $\%\alpha < 100\%$)
> - For strong acids/bases: $\alpha = 1$ (or $\%\alpha = 100\%$)
> - $\alpha$ is affected by concentration (dilution increases $\alpha$)
> - $K_a$ and $K_b$ are **not** affected by concentration

### Acid and Base Dissociation Constants

**Weak acid ($K_a$):**
$$HA(aq) + H_2O(l) \rightleftharpoons H_3O^+(aq) + A^-(aq)$$

$$K_a = \frac{[H_3O^+][A^-]}{[HA]} \qquad pK_a = -\log K_a$$

**Weak base ($K_b$):**
$$B(aq) + H_2O(l) \rightleftharpoons BH^+(aq) + OH^-(aq)$$

$$K_b = \frac{[BH^+][OH^-]}{[B]} \qquad pK_b = -\log K_b$$

### Relationship between $K_a$ and $K_b$

For a conjugate acid-base pair:
$$K_a \times K_b = K_w = 1.0 \times 10^{-14} \text{ (at 25 °C)}$$

$$pK_a + pK_b = 14$$

### Relationship between $\alpha$, $K_a$, and $K_b$

When $\%\alpha < 10\%$ (small dissociation):

**Weak acids:**
$$\alpha = \sqrt{\frac{K_a}{c}}$$

**Weak bases:**
$$\alpha = \sqrt{\frac{K_b}{c}}$$

The degree of dissociation is **inversely proportional** to the square root of concentration.

> [!important] Validity
> These formulae are **only valid when $\%\alpha < 10\%$**.

### ICE Table Method and the Assumption

For weak acid/base equilibrium calculations, use an ICE (Initial, Change, Equilibrium) table:

| | Acid/Base | Conjugate | $H_3O^+$ / $OH^-$ |
|---|---|---|---|
| Initial | $C_0$ | 0 | 0 |
| Change | $-x$ | $+x$ | $+x$ |
| Equilibrium | $C_0 - x$ | $x$ | $x$ |

> [!tip] The "x is small" Assumption
> When $K_a$ or $K_b$ is very small, assume $x \ll C_0$, so:
> $$C_0 - x \approx C_0$$
> This avoids solving a quadratic equation. **Always verify** by checking if $\%\alpha < 10\%$.

### Example Species

```smiles
CC(=O)O           # CH3COOH (ethanoic acid)
CC(=O)[O-]        # CH3COO- (acetate)
N                  # NH3 (ammonia)
[NH4+]             # NH4+ (ammonium)
F                  # HF (hydrofluoric acid)
[F-]               # F- (fluoride)
O=CO               # HCOOH (formic acid)
Oc1ccccc1          # C6H5OH (phenol)
Nc1ccccc1          # C6H5NH2 (aniline)
CNC                # (CH3)2NH (dimethylamine)
CN                 # CH3NH2 (methylamine)
c1ccncc1           # C5H5N (pyridine)
```

## Related Topics
- [[Ionic Equilibria]] — Extended ionic equilibrium concepts (buffers, salt hydrolysis)
- [[Solubility Product]] — Equilibrium of sparingly soluble salts
- [[Phase Equilibria]] — Equilibrium between phases

## Sources
- [[FAD1018 W1 — Chemical Equilibrium]]
- [[FAD1018 - Basic Chemistry II]]
