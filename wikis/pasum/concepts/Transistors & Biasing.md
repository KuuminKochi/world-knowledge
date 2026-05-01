---
title: Transistors & Biasing
date: 2026-04-27
tags:
  - concept/physics
  - topic/solid-state
  - status/seedling
---

# Transistors & Biasing

Bipolar junction transistors and DC biasing circuits for stable amplification.

## Definition

A transistor is a semiconductor device used to amplify or switch electronic signals. Bipolar Junction Transistors (BJTs) consist of three doped semiconductor regions (emitter, base, collector) forming two p-n junctions. Biasing establishes proper DC operating conditions for amplification.

## Key Concepts

- BJT Structure — NPN and PNP configurations; base acts as a gate controlling current flow
- Operating Regions — cutoff, active (linear), saturation; determined by junction bias states
- Current Relationships — $I_E = I_B + I_C$
- Current Gain — $\beta = \frac{I_C}{I_B}$, typically 50–300; also denoted $h_{FE}$ (AC) or $h_{fe}$ (DC)
- Alpha — $\alpha = \frac{I_C}{I_E}$
- Emitter Current — $I_E = (\beta + 1)I_B$
- Temperature Sensitivity — $\beta$ varies with temperature, causing Q-point drift
- DC Load Line — graphical analysis of operating point bounded by cutoff and saturation
- Q-Point — quiescent operating point $(I_{CQ}, V_{CEQ})$ for distortion-free amplification
- Fixed Bias — simple but thermally unstable; $I_B$ is fixed by $R_B$
- Emitter-Stabilized Bias — adds emitter resistor $R_E$ for negative-feedback stability
- Voltage Divider Bias — most stable, uses base voltage divider (covered in L36)
- Thermal Stability — compensating for temperature and $\beta$ variations
- Saturation — transistor acts as closed switch; $I_C$ reaches maximum
- Cutoff — transistor acts as open switch; all currents ≈ 0

## Operating Regions

| Region | Emitter-Base Junction | Collector-Base Junction | Behavior | Key Condition |
|--------|----------------------|------------------------|----------|---------------|
| Active (Linear) | Forward biased | Reverse biased | Amplifier | $I_C = \beta I_B$ |
| Saturation | Forward biased | Forward biased | Closed switch | $I_C = I_{C(sat)}$, $V_{CE} \approx 0$ |
| Cutoff | Reverse / Open | Reverse / Open | Open switch | $I_C = 0$, $I_B = 0$, $I_E = 0$ |

- **Active region** is the only region suitable for linear amplification.
- **Saturation** occurs when $I_B$ is large enough that $I_C$ can no longer increase with $I_B$.
- **Cutoff** occurs when $V_{BE} < 0.7\,V$ (Si), so no base current flows.

## Fixed-Bias DC Analysis

**Circuit:** $R_B$ from $V_{CC}$ to base; $R_C$ from $V_{CC}$ to collector; emitter grounded.

**Base-Emitter KVL:**
$$V_{CC} - I_B R_B - V_{BE} = 0$$

**Collector-Emitter KVL:**
$$V_{CC} - I_C R_C - V_{CE} = 0$$

**Saturation Current:**
$$I_{C(sat)} = \frac{V_{CC}}{R_C}$$

**Q-Point Instability:**
Because $I_B$ is fixed by $R_B$ alone, $I_C = \beta I_B$ is directly proportional to $\beta$. A doubling of $\beta$ (e.g., from 50 to 100) doubles $I_C$ and shifts the Q-point by ~100%.

## Emitter-Stabilized Bias DC Analysis

**Circuit:** Same as fixed-bias but with $R_E$ added between emitter and ground.

**Base-Emitter KVL:**
$$V_{CC} - I_B R_B - V_{BE} - I_E R_E = 0$$

Substituting $I_E = I_B(\beta + 1)$:
$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E}$$

**Collector-Emitter KVL:**
$$V_{CC} - I_C R_C - V_{CE} - I_E R_E = 0$$

Using $I_E \approx I_C$ (valid when $\beta \gg 1$):
$$V_{CE} = V_{CC} - I_C(R_C + R_E)$$

**Saturation Current:**
$$I_{C(sat)} = \frac{V_{CC}}{R_C + R_E}$$

**Stability Mechanism:**
The term $(\beta + 1)R_E$ in the denominator of $I_B$ provides negative feedback:
- If $\beta$ increases → $I_B$ decreases → partially cancels the $\beta$ increase → $I_C$ stays more stable.

**Approximation Condition (Strong Stability):**
When $(\beta + 1)R_E \gg R_B$, commonly designed as:
$$(\beta + 1)R_E \geq 10 R_B$$
Under this condition:
$$I_C \approx \frac{V_{CC} - V_{BE}}{R_E}$$
The collector current becomes **largely independent of $\beta$**, giving excellent Q-point stability.

**Individual Node Voltages:**
- $V_E = I_E R_E$
- $V_C = V_{CE} + V_E = V_{CC} - I_C R_C$
- $V_B = V_{BE} + V_E = V_{CC} - I_B R_B$

## Stability Comparison: Fixed-Bias vs Emitter-Stabilized

For a circuit with $V_{CC} = 20\,V$, $R_B = 430\,k\Omega$, $R_C = 2\,k\Omega$:

| Configuration | $\beta = 50$ | $\beta = 100$ | $I_C$ Change |
|---------------|-------------|---------------|--------------|
| Fixed-bias | $I_C = 2.24\,mA$ | $I_C = 4.49\,mA$ | **+100%** |
| Emitter-stabilized ($R_E = 1\,k\Omega$) | $I_C = 2.01\,mA$ | $I_C = 3.63\,mA$ | **+80.6%** |

Adding $R_E$ significantly reduces Q-point drift caused by $\beta$ variation.

## Key Formulas

| Formula | Description |
|---------|-------------|
| $I_E = I_B + I_C$ | KCL at transistor node |
| $\beta = \frac{I_C}{I_B}$ | DC current gain |
| $I_C = \beta I_B$ | Collector current (active region) |
| $\alpha = \frac{I_C}{I_E}$ | Common-base current gain |
| $I_E = (\beta + 1)I_B$ | Emitter current in terms of base current |
| $V_{BE} \approx 0.7\,V$ | Silicon forward base-emitter voltage |
| $I_B = \frac{V_{CC} - V_{BE}}{R_B}$ | Fixed-bias base current |
| $V_{CE} = V_{CC} - I_C R_C$ | Fixed-bias collector-emitter voltage |
| $I_{C(sat)} = \frac{V_{CC}}{R_C}$ | Fixed-bias saturation current |
| $I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E}$ | Emitter-stabilized base current |
| $V_{CE} = V_{CC} - I_C(R_C + R_E)$ | Emitter-stabilized $V_{CE}$ ($I_E \approx I_C$) |
| $I_{C(sat)} = \frac{V_{CC}}{R_C + R_E}$ | Emitter-stabilized saturation current |
| $I_C \approx \frac{V_{CC} - V_{BE}}{R_E}$ | Emitter-stabilized approximation when $(\beta + 1)R_E \gg R_B$ |
| $V_E = I_E R_E$ | Emitter voltage |
| $V_C = V_{CC} - I_C R_C$ | Collector voltage |
| $V_B = V_{BE} + V_E$ | Base voltage |
| $I_C = \frac{V_{TH} - V_{BE}}{R_E + R_{TH}/\beta}$ | Voltage divider exact analysis (L36) |

## Related Concepts

- [[Semiconductors & Diodes]] — p-n junction foundation
- [[Operational Amplifiers]] — integrated circuit amplifiers
- [[AC Circuits]] — AC signal analysis

## Course Links

- [[FAD1022 - Basic Physics II]] — main course page
- [[FAD1022 L34-L38 — Semiconductors & Op-Amps]] — lecture source
- [[Zainal Abidin (ZAA)]] — lecturer
