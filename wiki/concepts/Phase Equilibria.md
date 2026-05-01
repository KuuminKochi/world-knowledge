---
title: "Phase Equilibria"
date: 2026-04-27
tags:
  - concept/chemistry
  - topic/physical-chemistry
  - status/seedling
---

# Phase Equilibria

Study of the equilibrium between different phases of matter and the transitions between them.

## Phase

A homogeneous part of a system that is physically distinct and mechanically separable.

| System | Phase | Component | Description |
|--------|-------|-----------|-------------|
| Mixture of O₂, N₂, H₂ gases | 1 | 3 | Gases well mixed; no visible boundary |
| Oil + water (unmixed) | 2 | 2 | Boundary between two liquids |
| Alcohol + water (mixed) | 1 | 2 | No boundary; miscible |
| Salt solution | 1 | 2 | Salt + water |
| Saturated CuSO₄ in closed bottle | 3 | 2 | Solid, liquid, gas (water vapour) |
| Steel | 1 | 2 | Fe + C |

```smiles
O
O=C=O
[Cu+2].[O-]S(=O)(=O)[O-]
```

## Phase Rule (Gibbs Phase Rule)

$$F = C - P + 2$$

Where:
- F = degrees of freedom
- C = number of components
- P = number of phases

## One-Component Phase Diagrams

### Water Phase Diagram
- **Triple point**: All three phases coexist (0.01°C, 0.006 atm)
- **Critical point**: 374°C, 218 atm (above: supercritical fluid)
- **Normal boiling point**: 100°C at 1 atm
- **Normal freezing point**: 0°C at 1 atm

### CO₂ Phase Diagram
- **Triple point**: 5.11 atm, −56.6°C
- **Critical point**: 31.1°C, 73 atm
- Sublimes at 1 atm (dry ice)
- Solid-liquid line has **positive slope** (solid denser than liquid)

```smiles
O=C=O
O
```

## Phase Transitions

| Transition | Name | ΔH |
|------------|------|-----|
| Solid → Liquid | Fusion (melting) | ΔHfus > 0 |
| Liquid → Solid | Freezing | ΔHfus < 0 |
| Liquid → Gas | Vaporization | ΔHvap > 0 |
| Gas → Liquid | Condensation | ΔHvap < 0 |
| Solid → Gas | Sublimation | ΔHsub > 0 |
| Gas → Solid | Deposition | ΔHsub < 0 |

## Clausius-Clapeyron Equation

Describes the temperature dependence of vapor pressure:

$$\ln\frac{P_2}{P_1} = -\frac{\Delta H_{vap}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$$

## Raoult's Law

For a component A in solution:
$$P_A = X_A P_A^o$$

Where:
- $X_A$ = mole fraction of component A
- $P_A^o$ = vapor pressure of pure component A

For a two-component system (A + B), by **Dalton's law**:
$$P_{total} = P_A + P_B = X_A P_A^o + X_B P_B^o$$

Where $X_A + X_B = 1$.

### Ideal Solutions
- A–A ≈ B–B ≈ A–B interactions
- $ΔH_{soln} = 0$ (thermoneutral)
- $ΔV = 0$
- Obeys Raoult's law exactly
- Example: benzene–toluene

```smiles
c1ccccc1
Cc1ccccc1
```

### Deviations from Raoult's Law

| Deviation | Condition | $ΔH_{soln}$ | $ΔV$ | Vapor Pressure | Boiling Point |
|-----------|-----------|-------------|------|----------------|---------------|
| **Positive** | A–A, B–B > A–B | +ve (endothermic) | +ve (expansion) | $P_{actual} > P_{calc}$ | Azeotrope has **minimum** bp |
| **Negative** | A–B > A–A, B–B | −ve (exothermic) | −ve (shrinkage) | $P_{actual} < P_{calc}$ | Azeotrope has **maximum** bp |

- **Positive deviation examples**: ethanol–water, ethanol–benzene, NaCl–H₂O (ionic)
- **Negative deviation examples**: HCl–water, HNO₃–water, acetone–chloroform

```smiles
CCO
c1ccccc1
Cl
O
CC(=O)C
C(Cl)(Cl)Cl
O=[N+]([O-])O
```

## Colligative Properties

Properties that depend on the number of solute particles, not their identity.

### 1. Vapor Pressure Lowering
$$ΔP = X_{solute} × P°_{solvent}$$

### 2. Boiling Point Elevation
$$ΔT_b = K_b × m$$

### 3. Freezing Point Depression
$$ΔT_f = K_f × m$$

### 4. Osmotic Pressure
$$π = MRT$$

> [!example] Worked Examples
>
> **Vapor pressure lowering:** 218 g glucose (RMM 180.2) in 460 mL water at 30°C. $P°_{water} = 31.82$ mmHg.
> $X_{glucose} = 0.0453$ → $ΔP = 1.44$ mmHg → $P_{solution} = 30.38$ mmHg.
>
> **Freezing point depression:** 1.60 g naphthalene (C₁₀H₈) in 20.0 g benzene. $K_f = 4.3$ °C m⁻¹. Pure benzene fp = 5.5°C.
> $m = 0.624$ mol/kg → $ΔT_f = 2.68$°C → fp = 2.82°C.
>
> **Boiling point elevation:** 651 g ethylene glycol in 2505 g water. RMM = 62. $K_b = 0.52$ °C/m.
> $m = 4.19$ mol/kg → $ΔT_b = 2.18$°C → bp = 102.18°C.
>
> **Osmotic pressure:** 46.0 g glycerin (C₃H₈O₃, RMM 92) per liter at 0°C.
> $Π = (0.5 / 1.0) × 0.0821 × 273 = 11.21$ atm.

```smiles
C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O
c1ccc2ccccc2c1
OCCO
OCC(O)CO
```

## Fractional Distillation & Azeotropes

### Fractional Distillation
Procedure for separating liquid components based on different boiling points.
- **Distillate** (receiving flask): lower boiling point component
- **Residue** (distilling flask): higher boiling point component

### Azeotrope
A mixture that distills at constant composition; cannot be separated by simple fractional distillation.

#### Positive Deviation Azeotropes (Minimum Boiling Point)
| System | Azeotrope Composition | Boiling Point |
|--------|----------------------|---------------|
| Ethanol–Benzene | 32.4% ethanol | Lower than both pure components |
| Ethanol–Water | 95.6% ethanol, 4.4% water | 78.2°C |

- Starting < azeotrope % → distillate = azeotrope, residue = higher bp component
- Starting > azeotrope % → distillate = azeotrope, residue = higher bp component
- Starting = azeotrope → only azeotrope distills over

#### Negative Deviation Azeotropes (Maximum Boiling Point)
| System | Azeotrope Composition | Boiling Point |
|--------|----------------------|---------------|
| HCl–Water | 20.2% HCl | Higher than both pure components |
| HNO₃–Water | 68% HNO₃, 32% water | 120.5°C |

- Starting < azeotrope % → distillate = lower bp pure component, residue = azeotrope
- Starting > azeotrope % → distillate = higher bp pure component, residue = azeotrope

```smiles
CCO
CCCCO
Cl
O=[N+]([O-])O
```

## Related Topics
- [[Thermochemistry]] — Enthalpy of phase transitions
- [[Chemical Equilibrium]] — Phase equilibrium as dynamic process

## Sources
- [[FAD1018 W5-W6 — Phase Equilibria]]
- [[FAD1018 - Basic Chemistry II]]
