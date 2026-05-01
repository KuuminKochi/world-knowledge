---
type: tutorial
created: 2026-04-25
updated: 2026-04-25
sources: [raw/st13-student.pdf]
status: draft
tags: [mathematics, fad1015, statistics, tutorial]
---

# ST13 — Student Version
![[Advanced Math thing ST13.excalidraw]]
![[Drawing 2026-04-26 17.10.46.excalidraw]]
## Overview
This tutorial covers Bernoulli differential equations, including identification, transformation to linear form, and solution methods. It also includes problems requiring multiple solution approaches for the same differential equation.

## How to Solve a Bernoulli Differential Equation

### What is a Bernoulli DE?
A **Bernoulli differential equation** is any first-order ODE that can be written in the standard form:

$\frac{dy}{dx} + P(x)y = Q(x)y^n$

where $P(x)$ and $Q(x)$ are functions of $x$ only, and $n$ is any real number **except 0 and 1**.

- If $n = 0$: It's just a linear first-order ODE.
- If $n = 1$: It's a separable equation.
- If $n \neq 0, 1$: It's Bernoulli and requires a substitution.

### The General Method

**Step 1: Rewrite in standard form**
Get the equation into the form:
$\frac{dy}{dx} + P(x)y = Q(x)y^n$

**Step 2: Identify $n$**
Find the exponent $n$ on the right-hand side.

**Step 3: Divide by $y^n$**
Divide every term by $y^n$ (assuming $y \neq 0$):
$y^{-n}\frac{dy}{dx} + P(x)y^{1-n} = Q(x)$

**Step 4: Make the substitution**
Let $v = y^{1-n}$.

Then differentiate $v$ with respect to $x$:
$\frac{dv}{dx} = (1-n)y^{-n}\frac{dy}{dx}$

So:
$y^{-n}\frac{dy}{dx} = \frac{1}{1-n}\frac{dv}{dx}$

**Step 5: Transform to linear form**
Substitute into the equation from Step 3:
$\frac{1}{1-n}\frac{dv}{dx} + P(x)v = Q(x)$

Multiply by $(1-n)$:
$\frac{dv}{dx} + (1-n)P(x)v = (1-n)Q(x)$

This is now a **linear first-order ODE in $v$**.

**Step 6: Solve the linear equation**
Use the integrating factor method:
- Find $\mu(x) = e^{\int (1-n)P(x)\,dx}$
- Multiply through by $\mu(x)$
- Left side becomes $\frac{d}{dx}[\mu(x) v]$
- Integrate both sides: $\mu(x) v = \int \mu(x)(1-n)Q(x)\,dx + C$
- Solve for $v$

**Step 7: Back-substitute**
Replace $v = y^{1-n}$ to get the solution in terms of $y$.

### Worked Example

**Problem:** Solve $\frac{dy}{dx} - y = e^x y^2$

**Step 1:** Already in standard form with $P(x) = -1$ and $Q(x) = e^x$.

**Step 2:** The exponent on the right is $n = 2$.

**Step 3:** Divide by $y^2$:
$y^{-2}\frac{dy}{dx} - y^{-1} = e^x$

**Step 4:** Substitute $v = y^{1-2} = y^{-1} = \frac{1}{y}$

Differentiate: $\frac{dv}{dx} = -y^{-2}\frac{dy}{dx}$

So: $y^{-2}\frac{dy}{dx} = -\frac{dv}{dx}$

**Step 5:** Substitute:
$-\frac{dv}{dx} - v = e^x$

Multiply by $-1$:
$\frac{dv}{dx} + v = -e^x$

**Step 6:** Integrating factor:
$\mu(x) = e^{\int 1\,dx} = e^x$

Multiply through:
$e^x\frac{dv}{dx} + e^x v = -e^{2x}$

Left side is $\frac{d}{dx}[e^x v]$:
$\frac{d}{dx}[e^x v] = -e^{2x}$

Integrate:
$e^x v = -\frac{1}{2}e^{2x} + C$

Solve for $v$:
$v = -\frac{1}{2}e^x + Ce^{-x}$

**Step 7:** Back-substitute $v = \frac{1}{y}$:
$\frac{1}{y} = -\frac{1}{2}e^x + Ce^{-x}$

Or:
$y = \frac{1}{Ce^{-x} - \frac{1}{2}e^x}$

---

## Questions Summary

1. **Bernoulli Equations**: Show that each differential equation is Bernoulli and solve it.
   - (a) $x\frac{dy}{dx} + y = \frac{1}{y^2}$
   - (b) $\frac{dy}{dx} - y = e^x y^2$
   - (c) $xe^y y' = 2e^y + x^3 e^{2y}$
   - (d) $x^2 y' + 2xy = 5y^3$
   - (e) $x^2 \frac{dy}{dx} + y^2 \cos x = 3xy$
   - (f) $3(1 + x^2)y' = 2xy(y^3 - 1)$

2. **Particular Solutions**: Obtain particular solutions for Bernoulli equations with initial conditions.
   - (a) $xdy + ydx = x^3y^6$; $y(1) = 1$
   - (b) $2xyy' = y^2 - 2x^3$; $y(2) = 1$
   - (c) $(y^4 - 2xy)dx + 3x^2 dy = 0$; $y(2) = 1$
   - (d) $(x^2 + 2y^2)dx - ydy = 0$; $y(0) = 1$

3. **Multiple Methods**: Solve using two distinct methods.
   - (a) $x^2 \frac{dy}{dx} - y^2 = xy$
   - (b) $xe^y dy + (e^y + x^3 e^{2x})dx = 0$; $y(1) = 2$
   - (c) $(x^2 + 6y^2)dx - 4xydy = 0$; $y(1) = 1$

4. **Combined Methods**: The equation $(x^4 + y^4)dx + 4xy^3 dy = 0$ is homogeneous, exact, and Bernoulli. Using all three methods, show the solution is $x^5 + 5xy^4 = A$.

## Key Concepts Tested
- Identification of Bernoulli differential equations
- Transformation: $v = y^{1-n}$ to convert to linear form
- Solving linear first-order differential equations
- Particular solutions with initial conditions
- Homogeneous differential equations
- Exact differential equations
- Multiple solution methods for verification

## Important Formulas
- Bernoulli form: $\frac{dy}{dx} + P(x)y = Q(x)y^n$
- Substitution: $v = y^{1-n}$, $\frac{dv}{dx} = (1-n)y^{-n}\frac{dy}{dx}$
- Linear form after substitution: $\frac{dv}{dx} + (1-n)P(x)v = (1-n)Q(x)$
- Integrating factor: $\mu(x) = e^{\int P(x)dx}$

## Related Topics
[[differential-equations]] [[bernoulli-equations]] [[linear-differential-equations]] [[integrating-factors]] [[homogeneous-equations]] [[exact-equations]] [[first-order-odes]]