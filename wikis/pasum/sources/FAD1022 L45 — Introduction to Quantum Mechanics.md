---
title: FAD1022 L45 — Introduction to Quantum Mechanics
date: 2026-04-29
tags:
  - source/lecture
  - subject/physics
  - topic/quantum-mechanics
  - status/seedling
course: "[[FAD1022 - Basic Physics II]]"
lecturer: "[[Nurul Izzati (NIA)]]"
---

# FAD1022 L45 — Introduction to Quantum Mechanics

This lecture introduces the formal mathematical framework of quantum mechanics, building on the wave-particle duality foundations from previous lectures. Topics span from photon momentum and the Compton effect through de Broglie's matter waves and the Heisenberg uncertainty principle, to the time-independent Schrödinger equation and the particle in a 1D infinite square well.

## Lecture File

- `Lecture 45 - Photon Momentum, Compton Effect, de-Broglie waves and Heisenberg Uncertainty Principle.pdf` (28 slides)
- Lecturer: [[Nurul Izzati (NIA)]]

## 1. Wave-Particle Duality Recap

Wave-particle duality is the cornerstone of quantum mechanics: all matter and radiation exhibit both wave-like and particle-like behaviour depending on the experimental context.

### De Broglie Wavelength

Louis de Broglie (1924) proposed that any particle with momentum $p$ has an associated wavelength:

$$\lambda = \frac{h}{p} = \frac{h}{mv}$$

Where:
- $h = 6.626 \times 10^{-34}$ J·s (Planck's constant)
- $p$ = momentum of the particle
- $m$ = mass, $v$ = velocity

**Key Insight:** For macroscopic objects (e.g., a 0.1 kg baseball at 40 m/s), $\lambda \approx 1.7 \times 10^{-34}$ m — far too small to detect. For electrons ($m_e = 9.11 \times 10^{-31}$ kg) moving at $10^6$ m/s, $\lambda \approx 7.3 \times 10^{-10}$ m — comparable to atomic dimensions.

### Double-Slit Experiment

The double-slit experiment provides direct evidence of wave-particle duality:
- **Classical expectation:** Particles produce two bands (one per slit)
- **Actual result:** Even when electrons pass through one at a time, an **interference pattern** builds up over many detections
- **Interpretation:** Each particle interferes with *itself*, behaving as a wave that passes through both slits simultaneously, then collapsing to a point-like detection

### Complementarity Principle (Niels Bohr)

> The wave and particle aspects of a quantum entity are complementary — both are needed for a complete description, but they cannot be observed simultaneously in a single experiment.

A quantum object exhibits wave behaviour when it is not being "watched" (interference) and particle behaviour when a which-path measurement is made.

## 2. Wave Functions and Probability Density

### The Wave Function $\Psi(x, t)$

In quantum mechanics, the state of a particle is described by a **wave function** $\Psi(x, t)$, a complex-valued function of position and time. The wave function itself has no direct physical interpretation — it is a mathematical tool.

### Probability Density (Born Interpretation)

Max Born (1926) proposed that $|\Psi(x, t)|^2$ gives the **probability density** of finding the particle at position $x$ at time $t$:

$$P(x, t)\,dx = |\Psi(x, t)|^2\,dx = \Psi^*(x, t)\Psi(x, t)\,dx$$

Where $\Psi^*$ is the complex conjugate of $\Psi$.

### Normalization Condition

Since the particle must be found *somewhere* in space, the total probability over all space must equal 1:

$$\int_{-\infty}^{\infty} |\Psi(x, t)|^2\,dx = 1$$

A wave function satisfying this condition is said to be **normalized**. This requirement constrains the mathematical form of $\Psi$ and leads directly to quantized energy levels in bound systems.

### Properties of Valid Wave Functions

A physically admissible wave function must be:
1. **Single-valued** — one value at each point
2. **Continuous** — no jumps or breaks
3. **Finite** — cannot blow up to infinity
4. **Square-integrable** — $\int_{-\infty}^{\infty} |\Psi|^2\,dx$ must be finite

## 3. Heisenberg Uncertainty Principle

Werner Heisenberg (1927) showed that certain pairs of physical quantities cannot be simultaneously known with arbitrary precision.

### Position-Momentum Uncertainty

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

Where:
- $\Delta x$ = uncertainty in position
- $\Delta p$ = uncertainty in momentum
- $\hbar = h/2\pi = 1.0546 \times 10^{-34}$ J·s (reduced Planck constant)

### Energy-Time Uncertainty

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

Where:
- $\Delta E$ = uncertainty in energy
- $\Delta t$ = uncertainty in time / lifetime of a state

### Physical Meaning

The uncertainty principle is **not** a measurement limitation — it is a fundamental property of nature:
- If you confine a particle to a very small region (small $\Delta x$), its momentum becomes highly uncertain (large $\Delta p$)
- Short-lived quantum states have inherently uncertain energies
- This is why electrons in atoms do not spiral into the nucleus: confining an electron to the nuclear volume would give it enormous momentum uncertainty and thus enormous kinetic energy

### Example — Electron Confinement

For an electron confined to $\Delta x = 10^{-10}$ m (atomic size):
$$\Delta p \geq \frac{\hbar}{2\Delta x} = \frac{1.0546 \times 10^{-34}}{2 \times 10^{-10}} \approx 5.27 \times 10^{-25}\text{ kg·m/s}$$

$$\Delta v \geq \frac{\Delta p}{m_e} \approx 5.8 \times 10^5\text{ m/s}$$

This minimum velocity is comparable to the orbital velocity in hydrogen, confirming that quantum uncertainty governs atomic structure.

## 4. Time-Independent Schrödinger Equation (TISE)

### The Wave Equation for Matter

Erwin Schrödinger (1926) proposed a wave equation governing the evolution of the wave function. The full time-dependent Schrödinger equation is:

$$i\hbar\frac{\partial\Psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\Psi(x,t)}{\partial x^2} + V(x)\Psi(x,t)$$

### Separation of Variables

For a time-independent potential $V(x)$, we can separate the wave function:

$$\Psi(x, t) = \psi(x) \cdot e^{-iEt/\hbar}$$

Substituting into the time-dependent equation yields the **Time-Independent Schrödinger Equation (TISE)**:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)$$

### Hamiltonian Form

The TISE can be written compactly using the **Hamiltonian operator** $\hat{H}$:

$$\hat{H}\psi(x) = E\psi(x)$$

Where $\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$

This is an **eigenvalue equation**: $\psi(x)$ is the eigenfunction and $E$ is the eigenvalue (the allowed energy). Only certain values of $E$ yield physically acceptable solutions — this is the origin of **energy quantization**.

### Terms in the TISE

| Term | Symbol | Meaning |
|------|--------|---------|
| Kinetic energy operator | $-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$ | From de Broglie relation $p = \hbar k$ |
| Potential energy | $V(x)$ | Depends on the physical situation |
| Energy eigenvalue | $E$ | Allowed energy of the state |
| Wave function | $\psi(x)$ | Spatial part of the full wave function |

## Additional Examples from Lecture Slides

### Example — De Broglie Wavelength of an Electron

Calculate the de Broglie wavelength of an electron moving at $2.0 \times 10^6$ m/s.

$$\lambda = \frac{h}{mv} = \frac{6.63 \times 10^{-34}}{(9.11 \times 10^{-31})(2.0 \times 10^6)} = \boxed{3.63 \times 10^{-10} \text{ m}}$$

### Example — De Broglie Wavelength from Kinetic Energy

Calculate the de Broglie wavelength of an electron with kinetic energy of 150 eV.

**Step 1:** Convert eV to joules
$$KE = 150 \text{ eV} = 150 \times 1.602 \times 10^{-19} = 2.403 \times 10^{-17} \text{ J}$$

**Step 2:** Use formula $\lambda = \frac{h}{\sqrt{2mKE}}$

$$\lambda = \frac{6.626 \times 10^{-34}}{\sqrt{2(9.11 \times 10^{-31})(2.403 \times 10^{-17})}} = \frac{6.626 \times 10^{-34}}{6.62 \times 10^{-24}} \approx \boxed{1.00 \times 10^{-10} \text{ m} = 0.1 \text{ nm}}$$

This is within the atomic scale — explaining electron diffraction.

### Example — Heisenberg Uncertainty Principle

**Case 1 (Macroscopic):** A pitcher throws a 0.1-kg baseball at 40 m/s. Momentum is $0.1 \times 40 = 4$ kg·m/s. Suppose the momentum is measured to an accuracy of 1%, i.e., $\Delta p = 0.01p = 4 \times 10^{-2}$ kg·m/s.

$$\Delta x \geq \frac{h}{4\pi \Delta p} = 1.3 \times 10^{-33} \text{ m}$$

*No wonder one does not observe the effects of the uncertainty principle in everyday life!*

**Case 2 (Microscopic):** Same situation, but baseball replaced by an electron ($m = 9.11 \times 10^{-31}$ kg) moving at $4 \times 10^6$ m/s.

$$p = 3.6 \times 10^{-24} \text{ kg·m/s}, \quad \Delta p = 3.6 \times 10^{-26} \text{ kg·m/s}$$

$$\Delta x \geq \frac{h}{4\pi \Delta p} = \boxed{1.4 \times 10^{-4} \text{ m}}$$

This is a macroscopic uncertainty — 0.14 mm — showing that quantum effects are significant for electrons.

## 5. Particle in a 1D Box (Infinite Square Well)

The simplest non-trivial quantum system: a particle of mass $m$ confined to a one-dimensional region $0 < x < L$ by infinitely high potential walls.

### Potential Definition

$$V(x) = \begin{cases} 0 & \text{for } 0 < x < L \\ \infty & \text{for } x \leq 0 \text{ or } x \geq L \end{cases}$$

### Boundary Conditions

Since the potential is infinite outside the box, the wave function must be zero at the walls:

$$\psi(0) = 0, \quad \psi(L) = 0$$

### Solving the TISE Inside the Box

For $0 < x < L$, $V = 0$, so the TISE becomes:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi$$

The general solution is $\psi(x) = A\sin(kx) + B\cos(kx)$ where $k = \sqrt{2mE}/\hbar$.

Applying $\psi(0) = 0$ forces $B = 0$, so $\psi(x) = A\sin(kx)$.

Applying $\psi(L) = 0$ gives $\sin(kL) = 0$, which requires $kL = n\pi$ for $n = 1, 2, 3, \ldots$

### Energy Quantization

From $k_n = n\pi/L$ and $k = \sqrt{2mE}/\hbar$:

$$E_n = \frac{\hbar^2 k_n^2}{2m} = \frac{\hbar^2 \pi^2 n^2}{2mL^2} = \frac{n^2 h^2}{8mL^2}$$

Where $n = 1, 2, 3, \ldots$ is the **quantum number**.

**Key properties:**
- Energy is **quantized** — only discrete values are allowed
- $E_n \propto n^2$ — energy spacing increases with $n$
- **Zero-point energy:** $E_1 = h^2/(8mL^2) > 0$ — the particle can never be at rest ($n=0$ is forbidden by the uncertainty principle)
- As $L$ increases, energy levels become closer together, approaching a classical continuum

### Normalized Wave Functions

Applying the normalization condition $\int_0^L |\psi_n(x)|^2\,dx = 1$:

$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right), \quad n = 1, 2, 3, \ldots$$

### Nodes

Each wave function $\psi_n(x)$ has $(n-1)$ **nodes** — points inside the box where $\psi_n = 0$ (excluding the walls). The probability of finding the particle at a node is zero.

| $n$ | Nodes inside box | Shape description |
|-----|-----------------|-------------------|
| 1   | 0               | Half sine wave (ground state) |
| 2   | 1               | Full sine wave (first excited state) |
| 3   | 2               | 1.5 sine waves |
| 4   | 3               | 2 full sine waves |

### Probability Distributions

The probability density for state $n$ is:

$$|\psi_n(x)|^2 = \frac{2}{L}\sin^2\left(\frac{n\pi x}{L}\right)$$

For the ground state ($n=1$), the particle is most likely found near the centre of the box. For higher $n$, the probability distribution shows multiple peaks, approaching the classical uniform distribution as $n \to \infty$ (**Bohr's correspondence principle**).

### Worked Example 1 — Electron in a Box

An electron is confined in a 1D box of length $L = 1.0 \times 10^{-10}$ m (approximately atomic size). Find:
(a) The ground state energy $E_1$
(b) The wavelength of a photon emitted when the electron transitions from $n=3$ to $n=1$

**Solution (a):**
$$E_1 = \frac{h^2}{8mL^2} = \frac{(6.626 \times 10^{-34})^2}{8(9.11 \times 10^{-31})(1.0 \times 10^{-10})^2}$$
$$E_1 = \frac{4.39 \times 10^{-67}}{7.29 \times 10^{-50}} = 6.02 \times 10^{-18}\text{ J} = 37.6\text{ eV}$$

**Solution (b):**
$$E_3 = 9E_1 = 9(6.02 \times 10^{-18}) = 5.42 \times 10^{-17}\text{ J}$$
$$\Delta E = E_3 - E_1 = 5.42 \times 10^{-17} - 6.02 \times 10^{-18} = 4.82 \times 10^{-17}\text{ J}$$
$$\lambda = \frac{hc}{\Delta E} = \frac{(6.626 \times 10^{-34})(3.0 \times 10^8)}{4.82 \times 10^{-17}} = 4.12 \times 10^{-9}\text{ m} = 4.12\text{ nm}$$

This wavelength is in the X-ray region of the electromagnetic spectrum.

### Worked Example 2 — Proton in a Box

A proton ($m_p = 1.67 \times 10^{-27}$ kg) is confined in a 1D box of length $L = 1.0 \times 10^{-15}$ m (nuclear dimensions). Find the ground state energy.

$$E_1 = \frac{h^2}{8mL^2} = \frac{(6.626 \times 10^{-34})^2}{8(1.67 \times 10^{-27})(1.0 \times 10^{-15})^2}$$
$$E_1 = \frac{4.39 \times 10^{-67}}{1.34 \times 10^{-56}} = 3.28 \times 10^{-11}\text{ J} \approx 205\text{ MeV}$$

This enormous energy scale (MeV range) is why nuclear processes involve such high energies.

## 6. Energy Quantization — Classical vs Quantum

### Why is Energy Discrete at Quantum Scales?

The TISE is a differential equation with boundary conditions, similar to a standing wave on a string. Only specific wavelengths — and therefore specific energies — can satisfy the boundary conditions. This is the mathematical origin of quantization.

### Contrast Between Classical and Quantum

| Property | Classical Physics | Quantum Mechanics |
|----------|-------------------|-------------------|
| Energy | Continuous (any value) | Discrete (quantized) at small scales |
| Position | Definite trajectory $x(t)$ | Probability distribution $|\psi(x)|^2$ |
| Momentum | Definite $p = mv$ | Uncertain; $\Delta x\Delta p \geq \hbar/2$ |
| State | Determined by $x$ and $p$ | Determined by wave function $\psi$ |
| Measurement | Passive observation | Affects the system (wave function collapse) |
| Causality | Deterministic | Probabilistic |

### When Does Classical Physics Recover?

As the quantum number $n$ becomes large, the energy spacing relative to the energy becomes small:

$$\frac{E_{n+1} - E_n}{E_n} = \frac{(n+1)^2 - n^2}{n^2} = \frac{2n+1}{n^2} \approx \frac{2}{n} \to 0 \text{ as } n \to \infty$$

This is **Bohr's Correspondence Principle**: quantum mechanics approaches classical mechanics in the limit of large quantum numbers.

### Zero-Point Energy

Even in the lowest energy state ($n=1$), the particle has non-zero energy ($E_1 > 0$). This is a direct consequence of the uncertainty principle:
- Confining the particle to the box gives it a minimum $\Delta x \approx L$
- The uncertainty principle then requires a minimum $\Delta p \approx \hbar/L$
- This minimum momentum implies a minimum kinetic energy

Classically, a particle could be at rest ($E=0$) inside the box. Quantum mechanically, this is impossible.

## Key Equations Summary

| Equation | Description |
|----------|-------------|
| $\lambda = h/p$ | De Broglie wavelength |
| $P(x) = |\Psi(x,t)|^2$ | Probability density (Born rule) |
| $\int_{-\infty}^{\infty} |\Psi|^2\,dx = 1$ | Normalization condition |
| $\Delta x \cdot \Delta p \geq \hbar/2$ | Heisenberg uncertainty (position-momentum) |
| $\Delta E \cdot \Delta t \geq \hbar/2$ | Heisenberg uncertainty (energy-time) |
| $-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi = E\psi$ | Time-Independent Schrödinger Equation |
| $\hat{H}\psi = E\psi$ | TISE in operator form |
| $E_n = \frac{n^2 h^2}{8mL^2}$ | Particle in 1D box energy |
| $\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$ | Particle in 1D box wave function |

## Related Concepts

- [[Modern Physics — Wave-Particle Duality]] — foundational principle
- [[Quantum Mechanics]] — concept page
- [[Atomic Physics]] — quantum mechanics applied to atoms
- [[Photoelectric Effect]] — experimental evidence for quantum nature
- [[Photons]] — quantum of electromagnetic radiation

## Previous Lecture

- [[FAD1022 L44 — Photons and Photoelectric Effect]] — photon properties, photoelectric equation

## Lecturer

[[Nurul Izzati (NIA)]] — PASUM Physics Lecturer

## Related

- [[FAD1022 - Basic Physics II]] — main course page
