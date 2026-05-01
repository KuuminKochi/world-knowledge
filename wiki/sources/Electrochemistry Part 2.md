---
title: "Electrochemistry Part 2"
date: 2026-04-30
tags:
  - source/lecture
  - subject/chemistry
  - topic/electrochemistry
  - status/seedling
course: "[[FAD1018 - Basic Chemistry II]]"
lecturer: "[[Mahfuzah Binti Yusoff]]"
weeks: 3
---

# Electrochemistry Part 2

Electrochemistry Part 2 for FAD1018 Basic Chemistry II. Source file: `L3 Stdn Copy.pdf` (34 pages, PowerPoint slides).

> [!note] Direct Image Processing
> Content reconstructed from direct visual processing of all 34 slide images.

## Learning Outcomes
- Explain the driving force behind electrochemical cells
- Relate cell potential to Gibbs free energy and equilibrium
- Use the Nernst equation to calculate cell potential under non-standard conditions
- Solve quantitative problems involving cell potential and pH

---

## 1. The Driving Force Behind Electrochemical Cells

**Cell potential** works like water pressure:
- Electrons flow from higher "eagerness to give" (anode) to lower "eagerness to take" (cathode)
- Just like water flows from high to low, electrons flow from higher to lower reduction potential

$$E = 0 \text{ at equilibrium}$$

At equilibrium:
- There is no more "pressure difference"
- Forward and reverse reactions are perfectly balanced
- No net "push" to drive electrons through the wire
- The voltage reads zero, not because nothing is happening, but because both directions are happening equally

### The Dead Battery Analogy
A dead battery is not out of chemicals — the forward and reverse reactions have reached equilibrium, so there is no longer any net push to drive electrons.

---

## 2. Cell Potential and Spontaneity

$$E°_{cell} = E°_{cathode} - E°_{anode}$$

- **$E°_{cell} > 0$**: spontaneous reaction (galvanic cell)
- **$E°_{cell} < 0$**: non-spontaneous reaction (requires electrolytic cell)
- **$E°_{cell} = 0$**: equilibrium (dead battery)

---

## 3. The Nernst Equation

Relates cell potential to concentration under non-standard conditions:

$$E_{cell} = E°_{cell} - \left(\frac{RT}{nF}\right) \ln Q$$

At $T = 25°C$:

$$E_{cell} = E°_{cell} - \frac{0.0592}{n} \log Q$$

Where:
- $R$ = gas constant (8.314 J·mol⁻¹·K⁻¹)
- $T$ = temperature in Kelvin
- $n$ = number of electrons transferred
- $F$ = Faraday constant (96,485 C·mol⁻¹)
- $Q$ = reaction quotient

---

## 4. Worked Examples from Lecture

### Example 1: Identify Cathode and Anode
Given half-equations, determine cathode/anode using standard reduction potentials:
$$E°_{cell} = E°_{cathode} - E°_{anode}$$

### Example 2: Calculate Cell Potential
Given:
- $E°_{\text{Mg}^{2+}/\text{Mg}} = -2.37$ V
- $E°_{\text{Ca}^{2+}/\text{Ca}} = -2.76$ V

**Solution:**
1. Mg²⁺/Mg is more positive → **cathode**
2. Ca²⁺/Ca is more negative → **anode**
3. $E°_{cell} = (-2.37) - (-2.76) = +0.39$ V

### Practice 4: Calculate [H⁺] and pH from Cell Potential
A galvanic cell consists of a Zn/Zn²⁺ half-cell and the Standard Hydrogen Electrode (SHE).
Given:
- $[\text{Zn}^{2+}] = 0.45$ M
- $P_{\text{H}_2} = 2.0$ atm
- $T = 25°C$
- Voltmeter shows $E_{cell} = 0.65$ V

**Strategy:** Use the Nernst equation to solve for $[\text{H}^+]$, then calculate pH.

---

## 5. Gibbs Free Energy and Cell Potential

$$\Delta G = -nFE_{cell}$$

$$\Delta G° = -nFE°_{cell}$$

- Negative $\Delta G$ → spontaneous reaction
- Positive $\Delta G$ → non-spontaneous reaction
- At equilibrium: $\Delta G = 0$ and $E_{cell} = 0$

### Relationship to Equilibrium Constant
$$\Delta G° = -RT \ln K$$

Combining with $\Delta G° = -nFE°_{cell}$:
$$E°_{cell} = \frac{RT}{nF} \ln K$$

At 25°C:
$$E°_{cell} = \frac{0.0592}{n} \log K$$

---

## Key Concepts

- [[Electrochemistry]] — Concept page
- [[Nernst Equation]] — Cell potential under non-standard conditions
- [[Gibbs Free Energy]] — Thermodynamic spontaneity
- [[Galvanic Cell]] — Spontaneous cells
- [[Equilibrium Constant]] — K and cell potential

## Related

- [[FAD1018 - Basic Chemistry II]] — course page
- [[Mahfuzah Binti Yusoff]] — lecturer
- [[L1 L2 Electrochemistry]] — preceding lecture (fundamentals)
- [[FAD1018 L4-L5 — Electrolytic Cell]] — electrolysis, industrial applications
- [[FAD1018 Tutorial 4 — Electrochemistry]] — tutorial practice
- [[Chemistry Exam Analysis]] — exam weightage analysis
