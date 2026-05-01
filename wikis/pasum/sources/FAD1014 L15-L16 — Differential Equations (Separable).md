---
title: "FAD1014 L15-L16 — Differential Equations (Separable)"
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics-ii
  - topic/differential-equations
  - status/sapling
course: "[[FAD1014 - Mathematics II]]"
lecturer: "Norsiah Hashim"
---

# L15-L16: Differential Equations (Separable)

Lecture notes covering the definition and classification of differential equations, and the solution of first-order differential equations with separable variables.

---

## 1. Introduction to Differential Equations

> **Differential equation (DE)** is an equation that contains variables $x$ and $y$, with at least one derivative of $y$ with respect to $x$.

### Order and Degree

| Term | Definition |
|------|------------|
| **Order of DE** | The highest derivative present in the equation |
| **Degree of DE** | The power of the highest derivative |

**Examples:**
- $\displaystyle \frac{dy}{dx} + 3y = x$ → **1st order, 1st degree**
- $\displaystyle \frac{d^2y}{dx^2} + x^2 = 5\frac{dy}{dx}$ → **2nd order, 1st degree**
- $\displaystyle \left(\frac{d^2y}{dx^2}\right)^3 - \frac{dy}{dx} = 3y$ → **2nd order, 3rd degree**

### Solutions of a DE

> A **solution** to a differential equation is any function that satisfies the given equation.

**Example verification:**
$y = \sin x$ is a solution to $y'' + y = 0$ because:
- $y' = \cos x$
- $y'' = -\sin x$
- Substituting: $(-\sin x) + (\sin x) = 0 \quad \checkmark$

### General Solution

Differentiating $y = x^3 + C$ with respect to $x$ gives:
$$\frac{dy}{dx} = 3x^2$$

The equation $\displaystyle \frac{dy}{dx} = 3x^2$ is a 1st order and 1st degree differential equation, and:
$$y = x^3 + C$$
is the **general solution** because it contains an arbitrary constant $C$.

### Particular Solution

If further information (an **initial condition**) is given so that the constant can be determined, then the **particular solution** of the differential equation can be obtained.

---

## 2. Differential Equations of Separable Variable Type

A first-order differential equation whose variables $x$ and $y$ are separable is of the general form:

$$\frac{dy}{dx} = \frac{f(x)}{g(y)} \quad \text{or} \quad g(y)\frac{dy}{dx} = f(x)$$

### Solution Method

1. **Separate variables**: group all $y$ terms with $dy$ and all $x$ terms with $dx$
2. **Integrate both sides**
3. **Solve for $y$** (if possible) to obtain the **general solution**
4. **Apply initial condition** (if given) to find the **particular solution**

```mermaid
flowchart TD
    A(["Separable DE<br/>dy/dx = f(x)/g(y)"]) --> B[Separate Variables<br/>g(y) dy = f(x) dx]
    B --> C[Integrate Both Sides<br/>∫ g(y) dy = ∫ f(x) dx]
    C --> D([General Solution<br/>with constant C])
    D --> E{Initial Condition<br/>Given?}
    E -->|Yes| F[Substitute x₀, y₀<br/>to find C]
    F --> G([Particular Solution])
    E -->|No| H[Leave as<br/>General Solution]
```

---

## 3. Worked Examples

### Example 1 — General Solution

Solve:
$$y\frac{dy}{dx} = 3x^2$$

**Solution:**
Separate variables:
$$y\,dy = 3x^2\,dx$$

Integrate both sides:
$$\int y\,dy = \int 3x^2\,dx$$

$$\frac{y^2}{2} = \frac{3x^3}{3} + C = x^3 + C$$

$$y^2 = 2x^3 + 2C$$

Let $A = 2C$:
$$\boxed{y^2 = 2x^3 + A}$$

This is the **general solution**.

---

### Example 2 — General Solution with Logarithms

Solve:
$$x\frac{dy}{dx} = 2y$$

**Solution:**
Separate variables:
$$\frac{1}{2y}\,dy = \frac{1}{x}\,dx$$

Integrate both sides:
$$\frac{1}{2}\int \frac{1}{y}\,dy = \int \frac{1}{x}\,dx$$

$$\frac{1}{2}\ln y = \ln x + C$$

$$\ln y = 2\ln x + 2C = \ln x^2 + 2C$$

Exponentiate:
$$y = e^{\ln x^2 + 2C} = x^2 \cdot e^{2C}$$

Let $A = e^{2C}$:
$$\boxed{y = Ax^2}$$

This is the **general solution**.

---

### Example 3 — Particular Solution

Solve the differential equation:
$$\frac{dy}{dx} = \frac{2y}{x^2 - 1}, \quad \text{given that } y = 1 \text{ when } x = 2$$

**Solution:**
Separate variables:
$$\frac{dy}{2y} = \frac{dx}{x^2 - 1}$$

Integrate both sides:
$$\int \frac{dy}{2y} = \int \frac{dx}{x^2 - 1}$$

$$\frac{1}{2}\ln y = \int \frac{dx}{(x-1)(x+1)}$$

Use **partial fractions** on the RHS:
$$\frac{1}{(x-1)(x+1)} = \frac{1}{2}\left(\frac{1}{x-1} - \frac{1}{x+1}\right)$$

So:
$$\frac{1}{2}\ln y = \frac{1}{2}\left[\ln(x-1) - \ln(x+1)\right] + C$$

Multiply by 2:
$$\ln y = \ln(x-1) - \ln(x+1) + 2C = \ln\left(\frac{x-1}{x+1}\right) + 2C$$

Exponentiate:
$$y = \frac{x-1}{x+1} \cdot e^{2C}$$

Let $A = e^{2C}$:
$$\boxed{y = \frac{A(x-1)}{x+1}} \quad \text{(General solution)}$$

Apply initial condition $y = 1$ when $x = 2$:
$$1 = \frac{A(2-1)}{2+1} = \frac{A}{3} \quad \Rightarrow \quad A = 3$$

$$\boxed{y = \frac{3(x-1)}{x+1}} \quad \text{(Particular solution)}$$

---

## Summary

| Concept | Description |
|---------|-------------|
| **DE** | Equation involving derivatives of $y$ w.r.t. $x$ |
| **Order** | Highest derivative present |
| **Degree** | Power of the highest derivative |
| **General solution** | Contains an arbitrary constant |
| **Particular solution** | Constant determined by initial conditions |
| **Separable DE** | Can be written as $g(y)\,dy = f(x)\,dx$ |

## Links
- [[Differential Equations]] — concept page
- [[Application of DE - Mixing Problems]]
- [[FAD1014 Tutorial 7 — Differential Equations]]
- [[FAD1014 - Mathematics II]] — course
