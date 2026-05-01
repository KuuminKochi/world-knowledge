---
title: Quantum Mechanics
date: 2026-04-29
tags:
  - concept/physics
  - topic/quantum-mechanics
  - status/seedling
aliases:
  - Wave Mechanics
  - Quantum Physics
---

# Quantum Mechanics

The theoretical framework describing physical systems at atomic and subatomic scales, where classical mechanics breaks down. Quantum mechanics replaces deterministic trajectories with probabilistic wave functions and introduces fundamental limits on measurement precision.

## Definition

Quantum mechanics is the branch of physics dealing with matter and energy at the smallest scales, where energy, momentum, angular momentum, and other quantities are restricted to discrete values (quantization). It is governed by the Schrödinger equation and characterized by wave-particle duality, the uncertainty principle, and probabilistic predictions.

## Key Concepts

### Wave-Particle Duality

All quantum entities exhibit both wave and particle properties. The de Broglie relation connects a particle's momentum to its wavelength:

$$\lambda = \frac{h}{p}$$

- **Wave evidence:** Interference (double-slit experiment), diffraction
- **Particle evidence:** Photoelectric effect, Compton scattering
- **Complementarity principle:** Wave and particle aspects are complementary — both describe reality, but only one is manifested per experiment

This is fully described in [[Modern Physics — Wave-Particle Duality]].

### The Wave Function $\Psi(x, t)$

Every quantum system is described by a complex-valued wave function. The wave function itself is not directly observable.

**Born Rule:** The probability density of finding a particle at position $x$ at time $t$ is:

$$P(x, t) = |\Psi(x, t)|^2 = \Psi^*(x, t)\Psi(x, t)$$

**Normalization:** The total probability of finding the particle somewhere in space must be 1:

$$\int_{-\infty}^{\infty} |\Psi(x, t)|^2\,dx = 1$$

**Physical requirements for $\Psi$:**
- Single-valued, continuous, and finite everywhere
- First derivative continuous (except at infinite potential boundaries)
- Square-integrable over all space

### Heisenberg Uncertainty Principle

Fundamental limits on simultaneous knowledge of conjugate variables:

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

Where $\hbar = h/2\pi = 1.0546 \times 10^{-34}$ J·s.

**Key implications:**
- The more precisely position is known, the less precisely momentum can be known (and vice versa)
- Short-lived states have inherently uncertain energies
- Confining a particle increases its minimum kinetic energy
- This is why electrons do not spiral into atomic nuclei
- The uncertainty principle is **not** a measurement defect — it is a fundamental property of quantum systems

### The Schrödinger Equation

The fundamental equation of non-relativistic quantum mechanics, analogous to Newton's $F = ma$ in classical mechanics.

**Time-Dependent Schrödinger Equation:**

$$i\hbar\frac{\partial\Psi(x,t)}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\Psi(x,t)}{\partial x^2} + V(x)\Psi(x,t)$$

**Time-Independent Schrödinger Equation (TISE):**

For time-independent potentials, separating $\Psi(x,t) = \psi(x)e^{-iEt/\hbar}$ yields:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)$$

In **operator form** using the Hamiltonian $\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$:

$$\hat{H}\psi = E\psi$$

This is an **eigenvalue equation**: only certain values of $E$ (energy eigenvalues) yield physically acceptable solutions $\psi(x)$ (eigenfunctions). This is the mathematical origin of **energy quantization**.

### Particle in a 1D Box (Infinite Square Well)

The simplest exactly solvable quantum system: a particle confined between impenetrable walls at $x=0$ and $x=L$.

**Potential:** $V(x) = 0$ for $0 < x < L$, $V(x) = \infty$ elsewhere

**Quantized energies:**

$$E_n = \frac{n^2\pi^2\hbar^2}{2mL^2} = \frac{n^2h^2}{8mL^2}, \quad n = 1, 2, 3, \ldots$$

**Normalized wave functions:**

$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right), \quad 0 < x < L$$

**Probability density:**

$$|\psi_n(x)|^2 = \frac{2}{L}\sin^2\left(\frac{n\pi x}{L}\right)$$

**Key features:**
- **Zero-point energy:** $E_1 > 0$ — the particle can never be at rest (a consequence of the uncertainty principle)
- **Nodes:** $\psi_n$ has $(n-1)$ nodes inside the box (excluding walls)
- **Energy spacing:** $E_n \propto n^2$; spacing increases with $n$
- **Correspondence principle:** As $n \to \infty$, the quantum probability distribution approaches the classical uniform distribution

### Energy Quantization

In bound quantum systems, energy can only take discrete values. This arises mathematically from boundary conditions applied to the Schrödinger equation.

| System | Quantization Condition | Energy Levels |
|--------|----------------------|---------------|
| Particle in 1D box | $\psi(0) = \psi(L) = 0$ | $E_n = n^2h^2/(8mL^2)$ |
| Harmonic oscillator | $\psi(\pm\infty) = 0$ | $E_n = (n + \frac{1}{2})\hbar\omega$ |
| Hydrogen atom | $\psi(r\to\infty) = 0$ | $E_n = -13.6/n^2$ eV |

**Contrast with classical physics:** In classical mechanics, a particle in a box could have any kinetic energy. In quantum mechanics, only discrete energies are allowed. The two descriptions agree only in the limit of large quantum numbers (**Bohr's Correspondence Principle**):

$$\lim_{n\to\infty} \frac{\Delta E_n}{E_n} = \lim_{n\to\infty} \frac{2}{n} = 0$$

### Operators and Observables

In quantum mechanics, every measurable quantity (observable) is represented by a Hermitian operator:

| Observable | Classical Variable | Quantum Operator |
|------------|-------------------|-----------------|
| Position | $x$ | $\hat{x} = x$ |
| Momentum | $p$ | $\hat{p} = -i\hbar\frac{d}{dx}$ |
| Kinetic energy | $\frac{p^2}{2m}$ | $\hat{T} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$ |
| Total energy | $E$ | $\hat{H} = \hat{T} + V(x)$ |

The expectation value (average of many measurements) of an observable $\hat{A}$ in state $\psi$ is:

$$\langle A \rangle = \int_{-\infty}^{\infty} \psi^*(x)\,\hat{A}\,\psi(x)\,dx$$

## Key Formulas

| Formula | Description |
|---------|-------------|
| $\lambda = h/p$ | De Broglie wavelength |
| $P(x) = |\Psi|^2$ | Probability density (Born rule) |
| $\int |\Psi|^2\,dx = 1$ | Normalization condition |
| $\Delta x \cdot \Delta p \geq \hbar/2$ | Position-momentum uncertainty |
| $\Delta E \cdot \Delta t \geq \hbar/2$ | Energy-time uncertainty |
| $\hat{H}\psi = E\psi$ | Time-Independent Schrödinger Equation |
| $E_n = n^2h^2/(8mL^2)$ | Energy — particle in 1D box |
| $\psi_n = \sqrt{2/L}\sin(n\pi x/L)$ | Wave function — particle in 1D box |
| $\hbar = h/2\pi = 1.0546 \times 10^{-34}$ J·s | Reduced Planck constant |

## Constants

| Symbol | Value | Name |
|--------|-------|------|
| $h$ | $6.626 \times 10^{-34}$ J·s | Planck constant |
| $\hbar$ | $1.0546 \times 10^{-34}$ J·s | Reduced Planck constant |
| $m_e$ | $9.109 \times 10^{-31}$ kg | Electron mass |
| $m_p$ | $1.673 \times 10^{-27}$ kg | Proton mass |
| $c$ | $2.998 \times 10^{8}$ m/s | Speed of light |

## Related Concepts

- [[Modern Physics — Wave-Particle Duality]] — foundational principle underlying quantum mechanics
- [[Atomic Physics]] — application of quantum mechanics to atomic structure and spectra
- [[Photoelectric Effect]] — experimental evidence for quantization of light
- [[Photons]] — quantum of electromagnetic radiation
- [[Nuclear Physics]] — quantum effects in nuclear structure

## Sources

- [[FAD1022 L45 — Introduction to Quantum Mechanics]] — primary lecture source covering wave functions, TISE, particle in a box, and energy quantization
- [[FAD1022 L43 — Modern Physics]] — wave-particle duality foundations

## Course Links

- [[FAD1022 - Basic Physics II]] — main course page
- [[Nurul Izzati (NIA)]] — lecturer
