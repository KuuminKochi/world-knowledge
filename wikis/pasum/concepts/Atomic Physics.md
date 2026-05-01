---
title: Atomic Physics
date: 2026-04-27
tags:
  - concept/physics
  - topic/modern-physics
  - status/sapling
---

# Atomic Physics

Study of atomic structure, electron configurations, and atomic spectra.

## Definition

Atomic physics examines the structure of atoms, the arrangement of electrons around the nucleus, and the interaction of atoms with electromagnetic radiation. It bridges classical and quantum physics.

## Key Concepts

```mermaid
mindmap
  root((Atomic Structure))
    Models
      Thomson Plum Pudding
      Rutherford Nuclear
      Bohr Quantized Orbits
      Quantum Mechanical Orbitals
    Quantum Numbers
      Principal n
      Orbital l
      Magnetic m_l
      Spin m_s
    Electron Configuration
      Shells K L M N
      Pauli Exclusion
      Aufbau Principle
    Spectra
      Emission Lines
      Absorption Lines
      Lyman Balmer Paschen
    Transitions
      Spontaneous Emission
      Stimulated Absorption
      Stimulated Emission
      LASER
```

- Atomic Structure — nucleus (protons, neutrons) + electrons
- Thomson Model — plum pudding model; discovery of the electron
- Rutherford Model — nuclear atom, scattering experiments
- Bohr Model — quantized electron orbits, angular momentum quantization
- Bohr's Postulates — stationary states, $L=n\hbar$, photon emission during transitions
- Energy Levels — discrete allowed energies for electrons
- Quantum Numbers — $n$, $l$, $m_l$, $m_s$ describing electron states
- Electron Shells — K, L, M, N... shells corresponding to $n = 1, 2, 3, 4...$
- Atomic Spectra — emission and absorption line spectra
- Spectral Series — Lyman (UV, $n \to 1$), Balmer (visible, $n \to 2$), Paschen (IR, $n \to 3$)
- Rydberg Formula — wavelengths of spectral lines:
  $$\frac{1}{\lambda} = R_H\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right)$$
- Ionization Energy — energy to remove an electron
- Quantum Mechanical Model — Schrödinger orbitals, probability clouds, wave-particle duality
- Pauli Exclusion Principle — no two electrons same quantum state
- Stimulated Absorption — electron absorbs photon, excites to higher state
- Spontaneous Emission — excited electron emits photon randomly ($\sim 10^{-8}$ s lifetime)
- Stimulated Emission — incident photon triggers emission of an identical photon
- LASER — Light Amplification by Stimulated Emission of Radiation; coherent, monochromatic, directional light

```mermaid
graph TB
    subgraph bohr["Bohr Model Energy Levels"]
        direction TB
        ion["Ionization<br/>E=0 eV"]
        n4["n=4<br/>-0.85 eV"]
        n3["n=3<br/>-1.51 eV"]
        n2["n=2<br/>-3.40 eV"]
        n1["n=1<br/>-13.6 eV<br/>Ground State"]
    end

    n1 -->|Absorb photon| n2
    n2 -->|Absorb photon| n3
    n2 -->|Emit photon<br/>Lyman UV| n1
    n3 -->|Emit photon<br/>Balmer Vis| n2
    n4 -->|Emit photon<br/>Paschen IR| n3
    n1 -->|Absorb photon<br/>Ionize| ion

    style n1 fill:#ffe3e3,stroke:#c92a2a
    style ion fill:#f8f9fa,stroke:#868e96,stroke-dasharray: 5 5
```

## Key Formulas

| Formula | Description |
|---------|-------------|
|$r_n = n^2 a_0 = (5.29 \times 10^{-11} \text{ m})\,n^2$ | Bohr orbit radius |
|$E_n = -\frac{13.6}{n^2}$ eV | Hydrogen energy levels |
|$\frac{1}{\lambda} = R_H\left(\frac{1}{n_f^2} - \frac{1}{n_i^2}\right)$ | Rydberg formula |
|$L = n\hbar = r_n m v_n$ | Quantized angular momentum |
|$\hbar = \frac{h}{2\pi} \approx 1.06 \times 10^{-34} \text{ J}\cdot\text{s}$ | Reduced Planck constant |
|$hf = E_i - E_f$ | Photon energy from transition |
|$E_{\text{ionization}} = 13.6$ eV | Hydrogen ionization energy |
|$\mu = \frac{m_e M}{m_e + M}$ | Reduced mass |

## Related Concepts

- [[Nuclear Physics]] — nuclear structure, extension to nucleus
- [[Modern Physics — Wave-Particle Duality]] — quantum foundations
- [[Electrostatics]] — Coulomb force in atoms

## Course Links

- [[FAD1022 - Basic Physics II]] — main course page
- [[FAD1022 L39-L42 — Atomic & Nuclear Physics]] — lecture source
- [[Hafizul Mat]] — lecturer