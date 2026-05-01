---
title: "Electrochemistry"
date: 2026-04-27
tags:
  - concept
  - subject/chemistry
  - status/seedling
---

# Electrochemistry

The study of chemical processes that involve the transfer of electrons, encompassing both spontaneous redox reactions (galvanic cells) and non-spontaneous reactions driven by electrical energy (electrolysis).

## Redox Reactions

Oxidation and reduction always occur together in redox reactions:
- **Oxidation**: Loss of electrons, increase in oxidation number
- **Reduction**: Gain of electrons, decrease in oxidation number
- **Oxidising agent**: Species that is reduced (gains electrons)
- **Reducing agent**: Species that is oxidised (loses electrons)

## Electrochemical Cells

### Galvanic (Voltaic) Cells
Spontaneous cells that produce electrical energy from chemical reactions:
- **Anode**: Site of oxidation (negative electrode, electrons flow out)
- **Cathode**: Site of reduction (positive electrode, electrons flow in)
- Electrons flow from anode to cathode through external circuit
- Current flows from cathode to anode (opposite direction)
- **Salt bridge**: Maintains electrical neutrality by allowing ion flow between half-cells

### Electrolytic Cells
Non-spontaneous cells that use electrical energy to drive chemical reactions:
- External power source forces electron flow
- Anode: positive terminal (oxidation)
- Cathode: negative terminal (reduction)

## Cell Notation (Cell Diagram)

Standard notation for representing electrochemical cells:

$$ \text{Anode} \mid \text{Anode electrolyte} \parallel \text{Cathode electrolyte} \mid \text{Cathode} $$

- Single vertical line (|) represents phase boundary
- Double vertical line (||) represents salt bridge
- Inert electrodes (Pt, graphite) used when no solid metal participates

**Examples:**
- $\text{Zn}(s) \mid \text{Zn}^{2+}(aq) \parallel \text{Cu}^{2+}(aq) \mid \text{Cu}(s)$
- $\text{Pt}(s) \mid \text{Br}^-(aq), \text{Br}_2(l) \parallel \text{Cl}_2(g), \text{Cl}^-(aq) \mid \text{Pt}(s)$

```smiles
BrBr
```

```smiles
ClCl
```

## Standard Electrode Potential (E°)

The potential of a half-cell under standard conditions (1 M solutions, 1 atm gases, 25°C).

### Standard Hydrogen Electrode (SHE)
Reference electrode with $E° = 0.00$ V: $2\text{H}^+(aq) + 2e^- \rightarrow \text{H}_2(g)$

```smiles
[H][H]
```

### Standard Cell Potential (E°cell)

$$ E°_{cell} = E°_{cathode} - E°_{anode} $$

- Positive $E°_{cell}$ indicates spontaneous reaction
- More positive cathode: stronger oxidising agent
- More negative anode: stronger reducing agent

## Electromotive Force (EMF) and Gibbs Free Energy

$$ \Delta G° = -nFE°_{cell} $$

Where:
- $n$ = number of electrons transferred
- $F$ = Faraday constant (96,485 C/mol)
- Negative $\Delta G°$ = spontaneous reaction

## Nernst Equation

Relates cell potential to concentration:

$$ E_{cell} = E°_{cell} - \frac{RT}{nF} \ln Q $$

At 25°C:

$$ E_{cell} = E°_{cell} - \frac{0.0592}{n} \log Q $$

## Electrolysis and Faraday's Laws

**Faraday's First Law**: Mass of substance produced is proportional to quantity of electricity passed.

**Faraday's Second Law**: Masses of different substances produced by the same quantity of electricity are proportional to their equivalent weights.

$$ m = \frac{Q \times M}{n \times F} $$

Where:
- $m$ = mass of substance produced
- $Q$ = charge passed (current × time)
- $M$ = molar mass
- $n$ = number of electrons per ion
- $F$ = Faraday constant

## Applications

- **Batteries**: Lead-acid, alkaline, lithium-ion
- **Fuel cells**: Hydrogen-oxygen fuel cells
- **Corrosion**: Rusting as electrochemical process
- **Electroplating**: Coating metals using electrolysis

## Related Pages

- [[FAD1018 - Basic Chemistry II]] — course page
- [[Redox Reactions]] — oxidation-reduction fundamentals
- [[Thermodynamics]] — Gibbs free energy relationships

## Sources

- [[L1 L2 Electrochemistry]] — Lectures 1-2 on electrochemical cells (redox, cell notation, standard potential)
- [[Electrochemistry Part 2]] — Lecture part 2 on driving force, Nernst equation, equilibrium
- [[FAD1018 L4-L5 — Electrolytic Cell]] — Electrolysis, selective discharge, overpotential, industrial cells
- [[FAD1018 Tutorial 4 — Electrochemistry]] — tutorial practice