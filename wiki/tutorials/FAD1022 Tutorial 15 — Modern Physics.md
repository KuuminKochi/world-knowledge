---
title: FAD1022 Tutorial 15 — Modern Physics
date: 2026-04-13
course: "[[FAD1022 Physics II]]"
tags:
  - physics
  - modern-physics
  - tutorial
  - FAD1022
  - blackbody-radiation
  - photoelectric-effect
  - de-Broglie
  - uncertainty-principle
  - quantum-mechanics
---

# Tutorial 15 — Modern Physics

**Course:** FAD1022 Basic Physics 2  
**Session:** 2024/2025 (with solutions)

---

## 1. Blackbody Radiation

### Concept Summary

[[Blackbody Radiation|Blackbody radiation]] refers to the electromagnetic radiation emitted by a body in thermal equilibrium. [[Planck's Law|Planck's law]] describes the spectral density of this radiation, solving the ultraviolet catastrophe predicted by classical physics.

### Question 1.1

**Calculate the peak wavelength of radiation emitted by a blackbody at temperature 3000 K.**

**Solution:**
Use [[Wien's Displacement Law]]:

$$\lambda_{max} = \frac{2.90 \times 10^{-3} \text{ m K}}{T}$$

$$\lambda_{max} = \frac{2.90 \times 10^{-3} \text{ m K}}{3000 \text{ K}} = 9.67 \times 10^{-7} \text{ m} = 967 \text{ nm}$$

### Question 1.2

**The maximum wavelength emitted from the blackbody is on the blue spectrum. Determine the temperature of the blackbody.**

**Solution:**

Wavelengths in blue spectrum range: 450 nm - 485 nm

Consider any wavelengths in the range, e.g., 470 nm:

$$T = \frac{2.90 \times 10^{-3}}{\lambda_{max}} = \frac{2.90 \times 10^{-3}}{470 \times 10^{-9}} = 6170.2 \text{ K}$$

---

## 2. Photon Momentum

### Concept Summary

[[Photon|Photons]], although massless, carry momentum given by $p = E/c$ or $p = h/\lambda$. This concept is crucial in understanding phenomena like radiation pressure and the [[Photoelectric Effect|photoelectric effect]].

### Question 2.1

An excited nucleus emits a gamma ray photon with an energy of 2.45 MeV.

**a) Calculate the photon frequency**

**Solution:**
$$E = 2.45 \text{ MeV} = 2.45 \times 10^6 \text{ eV} \times 1.602 \times 10^{-19} \text{ J} = 3.92 \times 10^{-13} \text{ J}$$

$$f = \frac{E}{h} = \frac{3.92 \times 10^{-13} \text{ J}}{6.63 \times 10^{-34}} = 5.91 \times 10^{20} \text{ Hz}$$

**b) Calculate the photon wavelength**

$$\lambda = \frac{hc}{E} = \frac{6.63 \times 10^{-34} \times 3.0 \times 10^8}{3.92 \times 10^{-13}} = 5.07 \times 10^{-13} \text{ m}$$

### Question 2.2

A laser emits a monochromatic beam of light with a wavelength of 500 nm in vacuum. The beam is directed onto a metal surface and causes photoelectric emission.

**a) Determine the energy of a single photon.**

$$E = \frac{hc}{\lambda} = \frac{6.63 \times 10^{-34} \times 3.0 \times 10^8}{500 \times 10^{-9}} = 3.98 \times 10^{-19} \text{ J} = 2.48 \text{ eV}$$

**b) Calculate the corresponding momentum of the photon.**

$$p = \frac{h}{\lambda} = \frac{6.63 \times 10^{-34}}{500 \times 10^{-9}} = 1.33 \times 10^{-27} \text{ kg m/s}$$

**c) Comment on the consistency of the relationship $E = pc$ for massless particles.**

$$E = pc = 1.33 \times 10^{-27} \times 3.0 \times 10^8 = 3.99 \times 10^{-19} \text{ J}$$

Matches the value of energy calculated in Step 1 (within rounding error).

---

## 3. de Broglie Waves

### Concept Summary

Louis [[de Broglie]] proposed that particles exhibit wave-like behavior, with wavelength $\lambda = \frac{h}{p}$. This [[Wave-Particle Duality|wave-particle duality]] is fundamental in quantum mechanics.

### Question 3.1

If the [[de Broglie Wavelength|de Broglie wavelength]] of an electron is 1.0 Å, determine its velocity and its kinetic energy.

**Solution:**

$$v = \frac{h}{m\lambda} = \frac{6.63 \times 10^{-34}}{(9.11 \times 10^{-31})(10^{-10})} = 7.28 \times 10^6 \text{ m/s}$$

$$KE = \frac{1}{2}mv^2 = \frac{1}{2}(9.11 \times 10^{-31})(7.28 \times 10^6)^2 = 2.41 \times 10^{-17} \text{ J} = 151 \text{ eV}$$

### Question 3.2

An electron and a proton are each accelerated from rest through the same potential difference, 5000 V.

**a) Derive an expression for the de Broglie wavelength in terms of the accelerating voltage V and the particle's mass m.**

**Solution:**
$$KE = eV = \frac{1}{2}mv^2 \Rightarrow v = \sqrt{\frac{2eV}{m}}$$

$$\lambda = \frac{h}{mv} = \frac{h}{m\sqrt{\frac{2eV}{m}}} = \frac{h}{\sqrt{2meV}}$$

**b) Calculate the ratio of the de Broglie wavelengths of the proton to that of the electron.**

$$\frac{\lambda_p}{\lambda_e} = \sqrt{\frac{m_e}{m_p}} = \sqrt{\frac{9.11 \times 10^{-31}}{1.67 \times 10^{-27}}} = 0.02335$$

$$\lambda_e = 42.8\lambda_p$$

**c) Evaluate which particle exhibits more pronounced wave-like behaviour and justify your answer based on your result.**

The electron has a much larger de Broglie wavelength than the proton when accelerated through the same voltage.

Since wave-like behavior is more pronounced at larger wavelengths, the electron exhibits more observable wave behavior (e.g., diffraction, interference).

This result is consistent with experimental observations in electron diffraction and supports de Broglie's hypothesis.

### Question 3.3

An electron has a rest mass, $9.11 \times 10^{-31} \text{ kg}$. If the electron has a kinetic energy of $1.14 \times 10^{-27} \text{ J}$, determine its de Broglie wavelength.

$$\lambda = \frac{h}{m\sqrt{\frac{2E}{m}}} = \frac{6.63 \times 10^{-34}}{(9.11 \times 10^{-31})\sqrt{\frac{2(1.14 \times 10^{-27})}{(9.11 \times 10^{-31})}}} = 1.45 \times 10^{-5} \text{ m}$$

---

## 4. Heisenberg Uncertainty Principle

### Concept Summary

The [[Heisenberg Uncertainty Principle]] states that it is impossible to simultaneously know the exact position and momentum of a particle. Mathematically: $\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$.

### Question 4.1

If the uncertainty in position of an electron is $1.0 \times 10^{-10} \text{ m}$, calculate the minimum uncertainty in its momentum.

$$\Delta p = \frac{h}{4\pi\Delta x} = \frac{6.63 \times 10^{-34}}{4\pi(1.0 \times 10^{-10})} = 5.28 \times 10^{-25} \text{ kg m/s}$$

### Question 4.2

An electron is confined within a region of width $1.0 \times 10^{-10} \text{ m}$.

**a) Estimate the minimum uncertainty in the x-component of the electron's momentum.**

$$(\Delta p_x)_{min} = \frac{\hbar}{2\Delta x} = \frac{1.055 \times 10^{-34} \text{ J s}}{2(1.0 \times 10^{-10} \text{ m})} = 5.28 \times 10^{-25} \text{ kg m/s}$$

**b) If the electron has momentum with magnitude equal to the uncertainty found in part (a), determine its kinetic energy.**

$$KE = \frac{p^2}{2m} = \frac{(5.28 \times 10^{-25})^2}{2 \times 9.11 \times 10^{-31}} = 1.53 \times 10^{-19} \text{ J}$$

---

## 5. Photoelectric Effect

### Concept Summary

The [[Photoelectric Effect|photoelectric effect]] is the emission of electrons from a metal surface when exposed to light of sufficient frequency. This phenomenon supports the particle nature of light. The energy of the incident photon must exceed the [[Work Function|work function]] ($\phi$) of the material.

**Einstein's equation:** $KE_{max} = hf - \phi$

### Question 5.1

Light of frequency $1.0 \times 10^{15} \text{ Hz}$ is incident on a metal with work function 2.0 eV. Find the kinetic energy of the emitted electrons.

$$E = hf = (6.626 \times 10^{-34})(1.0 \times 10^{15}) = 6.63 \times 10^{-19} \text{ J} = 4.14 \text{ eV}$$

$$KE_{max} = 4.14 \text{ eV} - 2.0 \text{ eV} = 2.14 \text{ eV}$$

### Question 5.2

The graph shows how the maximum kinetic energy, $KE_{max}$, of electrons emitted from the surface of metal A varies with the frequency, $f$, of the incident electromagnetic radiation.

**Given:**
- Threshold frequency: $5.25 \times 10^{14} \text{ Hz}$

**a) Explain threshold frequency.**

The threshold frequency is the minimum frequency (of radiation) required to eject photoelectrons.

**b) Calculate the work function of metal A in J and eV.**

$$\phi = hf_0 = 6.63 \times 10^{-34} \text{ J s} \times 5.25 \times 10^{14} \text{ s}^{-1} = 3.48 \times 10^{-19} \text{ J}$$

$$\phi = \frac{3.48 \times 10^{-19} \text{ J}}{1.602 \times 10^{-19} \text{ J/eV}} = 2.17 \text{ eV}$$

**c) Metal A is exchanged for metal B. The work function of metal B is half that of metal A. Add a line to the graph to show how the maximum kinetic energy of electrons emitted from metal B varies with frequency.**

*(Graph sketch: line with same slope but lower x-intercept)*

**d) At a fixed frequency of the radiation incident, the emitted electrons are collected, and a current is recorded. Explain a change that may be made to increase this current.**

Increase the intensity (brightness).

*OR*

One photon interacts with one electron and the increase in number of photons incidents on the surface will result in more emitted electrons per second — therefore a greater rate of flow of charge.

### Question 5.3

An ultraviolet light with a wavelength of 254 nm falls upon a clean metal surface, the stopping potential necessary to stop emission of photoelectron is 0.181 V.

**a) Determine photoelectric threshold wavelength for this copper surface.**

$$eV_0 = \frac{hc}{\lambda} - \frac{hc}{\lambda_0}$$

$$\lambda_0 = \frac{hc}{\frac{hc}{\lambda} - eV_0} = 2.64 \times 10^{-7} \text{ m} = 264 \text{ nm}$$

**b) Determine the work function for this surface.**

$$\phi = \frac{hc}{\lambda_0} = \frac{6.63 \times 10^{-34} \times 3.0 \times 10^8}{2.64 \times 10^{-7}} = 7.53 \times 10^{-19} \text{ J} = 4.70 \text{ eV}$$

---

## Related Concepts

- [[Modern Physics — Wave-Particle Duality]]
- [[Atomic Physics]]
- [[Blackbody Radiation]]
- [[Wien's Displacement Law]]
- [[Planck's Law]]
- [[Photon]]
- [[Photon Energy]] ($E = hf$)
- [[Photon Momentum]] ($p = \frac{h}{\lambda}$)
- [[de Broglie Wavelength]] ($\lambda = \frac{h}{p}$)
- [[Wave-Particle Duality]]
- [[Heisenberg Uncertainty Principle]]
- [[Photoelectric Effect]]
- [[Work Function]]
- [[Threshold Frequency]]
- [[Stopping Potential]]
- [[Einstein's Photoelectric Equation]]

## Related Lectures

- [[FAD1022 L43 — Modern Physics]]
