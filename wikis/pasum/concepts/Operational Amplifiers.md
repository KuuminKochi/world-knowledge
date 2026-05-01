---
title: Operational Amplifiers
date: 2026-04-28
tags:
  - concept/physics
  - topic/analog-electronics
  - status/seedling
---

# Operational Amplifiers

High-gain voltage amplifiers with differential inputs and single-ended output.

## Definition

An operational amplifier (op-amp) is a DC-coupled high-gain electronic voltage amplifier with a differential input and usually a single-ended output. Op-amps are fundamental building blocks in analog circuits.

## Ideal Op-Amp Rules

With negative feedback, an ideal op-amp obeys two rules:

1. **No current flows into the input pins** — the input impedance is effectively infinite, so input current is diverted through the external feedback network.
2. **The output voltage adjusts to bring the input pins to the same voltage** — the voltage difference between the inverting ($V_-$) and non-inverting ($V_+$) terminals is driven to zero. This is the origin of the **virtual short** (and **virtual ground** when $V_+$ is grounded).

## Inverting Amplifier

In an inverting amplifier, the input signal is applied to the **inverting input (-)** through an input resistor $R_1$, while the **non-inverting input (+)** is connected to ground.

### Virtual Ground
Because the non-inverting input is at 0 V and the ideal op-amp rules force both inputs to the same potential, the inverting input node is held at **0 V**. This point is called **virtual ground** — it is not physically grounded, but sits at ground potential.

### Gain Derivation
Since no current enters the op-amp input (Rule 1), the current through $R_1$ must equal the current through the feedback resistor $R_f$:

$$I = \frac{V_{in}}{R_1} = -\frac{V_{out}}{R_f}$$

Rearranging gives the inverting amplifier output:

$$V_{out} = -\frac{R_f}{R_1} V_{in}$$

The **voltage gain** is:

$$A_v = -\frac{R_f}{R_1}$$

The negative sign indicates a 180° phase inversion between input and output.

### Example
Given $R_1 = 100 \text{ k}\Omega$ and $R_f = 500 \text{ k}\Omega$, find $V_{in}$ required for $V_{out} = -10 \text{ V}$:

$$-10 = -\frac{500}{100} V_{in} \implies V_{in} = 2 \text{ V}$$

## Key Concepts

- Ideal Op-Amp Properties — infinite gain, infinite input impedance, zero output impedance
- Virtual Short — $V_+ = V_-$ due to infinite gain with negative feedback
- Virtual Ground — inverting input held at 0 V when non-inverting input is grounded
- Golden Rules — no current into inputs, inputs at same voltage (with feedback)
- Negative Feedback — output fed back to inverting (-) input for stable linear operation
- Positive Feedback — output fed back to non-inverting (+) input
- Inverting Amplifier — input to (-), (+) grounded, negative gain
- Non-inverting Amplifier — input to (+), feedback to (-), positive gain > 1
- Voltage Follower — unity gain buffer, high input impedance
- Summing Amplifier — multiple inputs added
- Differential Amplifier — amplifies difference between inputs
- Comparator — open-loop, digital output
- Frequency Response — gain-bandwidth product

## Key Formulas

| Formula                                                              | Description            |
| -------------------------------------------------------------------- | ---------------------- |
| $V_{out} = A(V_+ - V_-)$                                             | Open-loop output       |
| $V_{out} = -\frac{R_f}{R_1} V_{in}$                                  | Inverting amplifier    |
| $A = 1 + \frac{R_f}{R_1}$                                            | Non-inverting gain     |
| $V_{out} = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2} + ...\right)$ | Summing amplifier      |
| $V_{out} = \frac{R_2}{R_1}(V_2 - V_1)$                               | Differential amplifier |
| $f_t = A_{CL} \cdot f_{CL}$                                          | Gain-bandwidth product |

## Non-Inverting Amplifier

In a **non-inverting amplifier**, the input signal is applied to the **non-inverting (+)** input terminal. Negative feedback is provided from the output to the **inverting (-)** input through a feedback resistor $R_f$, while a resistor $R_1$ connects the inverting input to ground.

Because of the **virtual short** (ideal op-amp Rule 2), the voltage at the inverting (-) pin equals the voltage at the non-inverting (+) pin:
$$V_- = V_+ = V_{in}$$

Since no current enters the op-amp inputs, the current through $R_1$ is:
$$I = \frac{V_{in}}{R_1}$$

This same current flows through $R_f$. The output voltage is the sum of the voltage at the inverting pin and the voltage drop across $R_f$:

$$V_{out} = V_{in} + I \cdot R_f = V_{in} + V_{in}\frac{R_f}{R_1} = V_{in}\left(1 + \frac{R_f}{R_1}\right) = \left(\frac{R_1 + R_f}{R_1}\right)V_{in}$$

**Characteristics:**
- Amplifies both DC and AC signals.
- Output is **not inverted** — it remains in phase with the input.
- Voltage gain is always greater than 1 (or equal to 1 in the buffer case).

> **Lecture Example (L38):** For $V_{in} = 2\text{ V}$, $R_1 = 100\text{ kΩ}$, and $R_f = 500\text{ kΩ}$:
> $$V_{out} = \left(\frac{100\text{ kΩ} + 500\text{ kΩ}}{100\text{ kΩ}}\right)(2\text{ V}) = \mathbf{+12\text{ V}}$$

## Voltage Follower (Unity-Gain Buffer)

A special case of the non-inverting amplifier occurs when **no feedback resistor** is used ($R_f = 0$) and the inverting input is connected directly to the output, with $R_1$ effectively open (infinite). The gain becomes:

$$A = 1 + \frac{R_f}{R_1} \approx 1$$

In this configuration, called a **voltage follower** or **unity-gain buffer**:
- $V_{out} = V_{in}$ with a gain of exactly 1.
- The output is not inverted.
- The circuit provides very high input impedance and very low output impedance.
- It is used to isolate stages, prevent loading effects, and drive heavy loads without drawing current from the source.

## Related Concepts

- [[Transistors & Biasing]] — internal transistor implementation
- [[Semiconductors & Diodes]] — semiconductor foundation
- [[AC Circuits]] — frequency response analysis

## Course Links

- [[FAD1022 - Basic Physics II]] — main course page
- [[FAD1022 L34-L38 — Semiconductors & Op-Amps]] — lecture source
- [[Zainal Abidin (ZAA)]] — lecturer