---
title: Revision Faraday and Lenz Law
date: 2026-04-29
tags:
  - source/lecture
  - subject/physics
  - topic/electromagnetism
  - status/seedling
course: "[[FAD1022 - Basic Physics II]]"
lecturer: "[[Amirul Hakimi Bin Baderus (AHB)]]"
---

# Revision Faraday and Lenz Law

Revision lecture on electromagnetic induction, covering Faraday's law of induction, magnetic flux, and Lenz's law. Delivered by Amirul Hakimi Bin Baderus (AHB) as part of the FAD1022 Basic Physics II course.

## Lecture Structure

- **20.1** Induce EMF (revision)
- **20.2** Self Induction and Energy
- **20.3** Mutual Induction and Application (Transformers)

This revision focuses on sections 20.1 (Faraday's Law and Lenz's Law).

---

## 20.1 Induced EMF (Revision)

### Faraday's Discovery

- Michael Faraday is credited with the discovery of electromagnetic induction on **August 29, 1831**
- Current is induced when a magnet moves through a loop of wire, or when the loop moves over a stationary magnet
- The current is produced due to **change of the magnetic field**

### Faraday's Experiment Conclusions

1. The **current induced** is due to the relative motion between the magnet and the coil
2. The deflection is more if the magnet is moved faster, and less if moved slowly
3. The **deflection is reversed** when the magnet is moved in the opposite direction, indicating reversed current direction
4. The deflection changes with the **change in number of turns** of the coil (greater deflection for larger number of turns)

### 20.1.1 Magnetic Flux

Magnetic flux is proportional to both the strength of the magnetic field passing through the plane of a loop of wire and the area of the loop.

**Formula:**
$$\Phi_B = BA\cos\theta = B_\perp A$$

where:
- $B$ = magnetic field
- $A$ = area of the current loop
- $\theta$ = angle between direction of $\vec{B}$ and the normal to the loop area

**Unit of magnetic flux:** weber (Wb)

Only the **perpendicular component** of the loop area with the magnetic field contributes to the flux:
- $\theta = 90^\circ \rightarrow \Phi = 0$ (loop edge-on to field)
- $\theta = 45^\circ \rightarrow \Phi_B > 0$
- $\theta = 0^\circ \rightarrow \Phi_B = \text{max}$ (loop perpendicular to field)

### 20.1.2 Induced Current

A current can be produced by a **change in magnetic flux** passing through the coil.

$$\Phi = \vec{B} \cdot \vec{A}$$

- **Increasing magnetic flux** → current induced in one direction
- **Decreasing magnetic flux** → current induced in the opposite direction
- **No movement / constant flux** → $I = 0$

### 20.1.3 Faraday's Law

The induced emf may be increased by having $N$ tightly wound loops.

**Faraday's Law:**
$$\mathcal{E} = N\left(\frac{\Delta\Phi_B}{\Delta t}\right)$$

The bar magnet may be replaced by a **solenoid** to provide the magnetic field ($B = \mu_0 n I$). The change in flux can be achieved by changing (increasing/decreasing) the current flow in the solenoid:

$$\mathcal{E} = \frac{\Delta\Phi_B}{\Delta t} = \mu_0 n\left(\frac{\Delta I}{\Delta t}\right)$$

### 20.1.4 Lenz's Law

> Lenz's law states that the direction of the induced e.m.f. is such that it always tends to **oppose the cause which produces it**.

The induced emf resulting from a **changing magnetic flux** has a polarity that leads to an induced current whose direction is such that the induced magnetic field **opposes** the original flux change.

When applying Lenz's Law, there are **two magnetic fields** to consider:
1. The **external changing magnetic field** that induces the current in the loop
2. The **magnetic field produced by the current** in the loop

These two fields must oppose each other.

| Situation | External Flux | Induced Field Direction |
|-----------|---------------|------------------------|
| Increasing flux | Into the loop | **Opposite** (out of loop) |
| Decreasing flux | Into the loop | **Same** (into loop) |

- **Inserting magnet into solenoid:** a North pole is induced on the near side to **oppose the incoming North pole**
- **Withdrawing magnet from solenoid:** a South pole is induced on the near side to **oppose the outgoing North pole**

Use the **Right Hand Grip Rule** to determine the direction of induced current once the induced pole direction is known.

---

## Permeability vs Permittivity

| Aspect | Permittivity ($\varepsilon$) | Permeability ($\mu$) |
|--------|------------------------------|----------------------|
| Definition | Ability of a material to polarize in response to an external electric field | Ability of a material to magnetize in response to an external magnetic field |
| Denoted by | $\varepsilon$ | $\mu$ |
| SI unit | Fm$^{-1}$ | Hm$^{-1}$ (kg$\cdot$m$\cdot$s$^{-2}\cdot$A$^{-2}$) |
| Free-space value | $8.85 \times 10^{-12}$ | $1.26 \times 10^{-6}$ Hm$^{-1}$ |
| Related to | Electric fields | Magnetic fields |
| Application | Dielectric materials in capacitors | Transformer cores and inductors |

---

## Links
- [[FAD1022 - Basic Physics II]]
- [[FAD1022 L31-L33 — Inductance & Transformers]]
- [[Inductance & Transformers]]
- [[Magnetism]]
- [[Amirul Hakimi Bin Baderus (AHB)]]
