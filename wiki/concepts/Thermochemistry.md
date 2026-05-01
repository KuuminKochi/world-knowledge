---
title: "Thermochemistry"
date: 2026-04-27
tags:
  - concept/chemistry
  - topic/physical-chemistry
  - status/seedling
---

# Thermochemistry

The study of heat energy associated with chemical reactions and physical transformations.

## Basic Concepts

### System and Surroundings
- **System**: Part of universe under study
- **Surroundings**: Everything else
- **Universe**: System + Surroundings

### Types of Systems
| Type | Energy Exchange | Matter Exchange |
|------|-----------------|-----------------|
| Open | Yes | Yes |
| Closed | Yes | No |
| Isolated | No | No |

### State Functions
Properties depending only on initial and final states:
- Enthalpy (H)
- Internal energy (U)
- Entropy (S)
- Gibbs free energy (G)

### First Law of Thermodynamics
$$ΔU = q + w$$

Where:
- ΔU = change in internal energy
- q = heat absorbed by system
- w = work done on system

## Enthalpy (H)

Heat content at constant pressure: **H = U + PV**

### Types of Enthalpy Changes

| Symbol | Name | Definition |
|--------|------|------------|
| ΔH°f | Standard enthalpy of formation | One mole from elements in standard states |
| ΔH°c | Standard enthalpy of combustion | One mole burns in O₂ |
| ΔH°neut | Enthalpy of neutralization | Acid + base → salt + water |
| ΔH°sol | Enthalpy of solution | One mole dissolves |
| ΔH°vap | Enthalpy of vaporization | Liquid → gas |
| ΔH°fus | Enthalpy of fusion | Solid → liquid |
| ΔH°sub | Enthalpy of sublimation | Solid → gas |
| ΔH°at | Enthalpy of atomization | One mole to gaseous atoms |

### Standard Conditions
- 1 bar pressure
- 298 K (25°C) temperature
- 1 M concentration for solutions
- Specified physical state

## Calorimetry

### Coffee-Cup Calorimeter (Constant Pressure)
$$q = mcΔT$$

Where:
- m = mass (g)
- c = specific heat capacity (J/g·K)
- ΔT = temperature change

At constant pressure: **q = ΔH**

### Bomb Calorimeter (Constant Volume)
- Measures ΔU directly
- qv = Cv × ΔT

## Hess's Law

> The total enthalpy change for a reaction is the same, regardless of the pathway taken.

### Applications

#### Using Formation Enthalpies
$$ΔH°_{rxn} = ΣΔH°_f(products) - ΣΔH°_f(reactants)$$

#### Using Bond Enthalpies
$$ΔH°_{rxn} = Σ(Bonds\ broken) - Σ(Bonds\ formed)$$
- Breaking bonds: Endothermic (+)
- Forming bonds: Exothermic (-)

### Born-Haber Cycle
Hess's law application for ionic compounds:
- Atomization of metal
- Ionization of metal
- Atomization of non-metal
- Electron affinity of non-metal
- Lattice energy
- Formation enthalpy

### Enthalpy of Hydration (ΔH°hyd)
Energy released when one mole of gaseous ions is surrounded by water molecules:
- **Cations**: ΔH°hyd is negative (exothermic); smaller ions and higher charges → more negative
- **Anions**: ΔH°hyd is negative; smaller ions → more negative
- **Overall**: ΔH°hyd(total) = ΔH°hyd(cation) + ΔH°hyd(anion)

### Relationship: Enthalpy of Solution
$ΔH°_{sol} = ΔH°_{lattice} + ΔH°_{hyd}$

- If |ΔH°hyd| > |ΔH°lattice|: ΔH°sol is negative (exothermic dissolution)
- If |ΔH°hyd| < |ΔH°lattice|: ΔH°sol is positive (endothermic dissolution)

## Lattice Energy

Energy required to separate one mole of solid ionic compound into gaseous ions.

**Factors affecting lattice energy**:
1. Ionic charge: Higher charge → Higher LE
2. Ionic radius: Smaller ions → Higher LE

## Spontaneity and Gibbs Free Energy

$$ΔG = ΔH - TΔS$$

| ΔG | Spontaneity |
|----|-------------|
| < 0 | Spontaneous |
| = 0 | Equilibrium |
| > 0 | Non-spontaneous |

### Temperature Dependence
| ΔH | ΔS | Spontaneity |
|----|----|-------------|
| - | + | Always spontaneous |
| - | - | Spontaneous at low T |
| + | + | Spontaneous at high T |
| + | - | Never spontaneous |

## Related Topics
- [[Chemical Equilibrium]] — ΔG° = -RT ln K
- [[Phase Equilibria]] — Enthalpy of phase transitions
- [[Kinetic Chemistry]] — Activation energy

## Sources
- [[FAD1018 W15 — Thermochemistry]]
- [[FAD1018 - Basic Chemistry II]]
