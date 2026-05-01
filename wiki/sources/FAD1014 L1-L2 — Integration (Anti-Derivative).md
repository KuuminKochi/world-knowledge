---
title: "FAD1014 L1-L2 — Integration (Anti-Derivative)"
date: 2026-04-28
tags:
  - source/lecture
  - subject/mathematics-ii
  - topic/integration
  - status/seedling
course: "[[FAD1014 - Mathematics II]]"
lecturer: "[[En Jedzry Fadzlin B Jalaluddin]]"
---

# FAD1014 L1-L2 — Integration (Anti-Derivative)

Comprehensive lecture notes covering the fundamentals of integration as the reverse process of differentiation. Lecturer: **En Jedzry Fadzlin B Jalaluddin (BP217)**. Material adapted from J Merrill 2009 and MZMK 2011.

---

## 1.1 — Antiderivatives

### Practical Motivation
Integrals appear in many practical situations. For simple rectangular shapes, we can use basic geometry, but for irregular or curved shapes (e.g., an oval swimming pool with a rounded bottom), **precision engineering** requires exact and rigorous values — these call for integrals.

We have been solving situations dealing with **total amounts** of quantities. **Derivatives** deal with the rate of change of those quantities. Since it is not always possible to find functions that deal with the total amount directly, we need **antidifferentiation**.

### Kinematics Connection
The relationship between distance, velocity, and acceleration illustrates differentiation vs integration:

**Differentiation:**
$$s(t) \xrightarrow{\frac{ds}{dt}} v(t) \xrightarrow{\frac{dv}{dt}} a(t)$$

**Integration (reverse):**
$$a(t) \xleftarrow{\int a(t)\,dt} v(t) \xleftarrow{\int v(t)\,dt} s(t)$$

```mermaid
flowchart LR
    subgraph Diff["Differentiation"]
        D1[s(t)] -->|"d/dt"| D2[v(t)]
        D2 -->|"d/dt"| D3[a(t)]
    end
    subgraph Int["Integration"]
        I3[a(t)] -->|"∫"| I2[v(t)]
        I2 -->|"∫"| I1[s(t)]
    end
    Diff -.->|"Reverse process"| Int
```

### Definition
> **Antiderivative:** If $F'(x) = f(x)$, then $F(x)$ is an **antiderivative** of $f(x)$.

**Examples:**
- If $F(x) = 10x$, then $F'(x) = 10$. So $F(x)$ is the antiderivative of $f(x) = 10$.
- If $F(x) = x^2$, then $F'(x) = 2x$. So $F(x)$ is the antiderivative of $f(x) = 2x$.
- The antiderivative of $f(x) = 5x^4$ is $x^5$ (work backwards from the derivative).

### The Constant of Integration
$F(x) = x^2$ is **not** the only function whose derivative is $f(x) = 2x$:
- $G(x) = x^2 + 2$ has derivative $2x$
- $H(x) = x^2 - 7$ has derivative $2x$

For any real number $C$, the function $F(x) = x^2 + C$ has $f(x) = 2x$ as an antiderivative. There is a whole **family of functions** having $2x$ as a derivative; this family differs only by a constant. Graphically, these are vertical shifts of the same curve with identical tangent slopes at any given $x$.

> **Theorem:** If $F(x)$ and $G(x)$ are both antiderivatives of $f(x)$ on an interval, then there is a constant $C$ such that $F(x) - G(x) = C$. Two antiderivatives of a function can differ only by a constant. The arbitrary real number $C$ is called an **integration constant**.

### Indefinite Integral Notation
The family of all antiderivatives of $f$ is indicated by:
$$\int f(x)\,dx$$

- $\int$ = integral sign
- $f(x)$ = integrand
- $dx$ = indicates integration with respect to $x$

> **Indefinite Integral:** If $F'(x) = f(x)$, then $$\int f(x)\,dx = F(x) + C$$ for any real number $C$. This is the **most general antiderivative** of $f$.

### Variable of Integration
The symbol after $d$ indicates the variable of integration; other letters are treated as constants.

**Example 1.1.1:**
- $\displaystyle\int 2ax\,dx = a(2x)\,\text{? No: } \int 2ax\,dx = ax^2 + C$  
  Here $a$ is treated as a **constant** and $x$ as the **variable**.
- $\displaystyle\int 2ax\,da = a^2x + C = xa^2 + C$  
  Here $x$ is treated as the **constant**.

---

## Finding the Antiderivative (Power Rule)

Finding the antiderivative is the reverse of finding the derivative. Therefore, the rules for derivatives lead to rules for antiderivatives.

**Example:**
$$\frac{d}{dx}x^5 = 5x^4 \quad\Longrightarrow\quad \int 5x^4\,dx = x^5 + C$$

**Example 1.1.2:**
- $\displaystyle\int x^{-1/2}\,dx$
- $\displaystyle\int 3\,dx = 3x + C$
- $\displaystyle\int \frac{1}{x^3}\,dx$

---

## Sigma Notation, Riemann Sums, and the Definite Integral

### Sigma Notation
The summation symbol $\displaystyle\sum_{k=1}^{n} a_k$ denotes the sum of terms $a_k$ from $k=1$ to $k=n$.

**Examples:**
| Sigma Notation | Expanded | Value |
|---|---|---|
| $\sum_{k=1}^{5} k$ | $1+2+3+4+5$ | $15$ |
| $\sum_{k=1}^{3} (-1)^k k$ | $(-1)^1(1)+(-1)^2(2)+(-1)^3(3)$ | $-1+2-3 = -2$ |
| $\sum_{k=1}^{2} \frac{k}{k+1}$ | $\frac{1}{2}+\frac{2}{3}$ | $\frac{7}{6}$ |
| $\sum_{k=4}^{5} \frac{k^2}{k-1}$ | $\frac{16}{3}+\frac{25}{4}$ | $\frac{139}{12}$ |

### Riemann Sum
If $f$ is continuous, the **left Riemann sum** with $n$ equal subdivisions over $[a,b]$ is:
$$\sum_{k=0}^{n-1} f(x_k)\Delta x = \bigl[f(x_0)+f(x_1)+\dots+f(x_{n-1})\bigr]\Delta x$$
where $a=x_0 < x_1 < \dots < x_n=b$ and $\Delta x = \frac{b-a}{n}$.

### The Definite Integral
$$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{k=0}^{n-1} f(x_k)\Delta x$$

- $f$ = integrand
- $a$, $b$ = limits of integration
- $x$ = variable of integration

**Example:** Approximate $\displaystyle\int_0^2 x^2\,dx$ using $n=10$ (left Riemann sum):
$$\sum_{k=0}^{9} x_k^{\,2}\left(\frac{1}{5}\right) = \Bigl[\left(\tfrac{1}{5}\right)^2 + \left(\tfrac{2}{5}\right)^2 + \dots + \left(\tfrac{9}{5}\right)^2\Bigr]\left(\frac{1}{5}\right) = 2.28$$

---

## 1.2 — Indefinite Integrals and Standard Integrals

### 1.2.1 Rules for Antiderivatives

**Integrating a Constant:**
$$\int a\,dx = ax + c \qquad (a, c \text{ are constants})$$

**Power Rule:**
$$\int x^n\,dx = \frac{x^{n+1}}{n+1} + C \qquad \text{for any real number } n \neq -1$$
*(Add 1 to the exponent and divide by that number.)*

> You can always check your answers by taking the derivative!

**Examples:**
- $\displaystyle\int t^3\,dt = \frac{t^{3+1}}{3+1} = \frac{t^4}{4} + C$
- $\displaystyle\int \frac{1}{t^2}\,dt = \int t^{-2}\,dt = \frac{t^{-1}}{-1} + C = -\frac{1}{t} + C$

**You Do (practice):**
1. $\displaystyle\int \sqrt{u}\,du$
2. $\displaystyle\int dx$

### 1.2.2 Constant Multiple and Sum/Difference

**Basic Rules of Integration:**

(a) **Constant Multiple:** If $k$ is a constant,
$$\int k \cdot f(x)\,dx = k\int f(x)\,dx \qquad \text{for any real number } k$$

(b) **Sum/Difference:** For two functions $f(x)$ and $g(x)$,
$$\int \bigl[f(x) \pm g(x)\bigr]\,dx = \int f(x)\,dx \pm \int g(x)\,dx$$

**Example 1.2.1:**
$$\int 2v^3\,dv = 2\int v^3\,dv = 2\left(\frac{v^4}{4}\right) + C = \frac{v^4}{2} + C$$

**You Do (practice):**
- $\displaystyle\int \frac{12}{z^5}\,dz$
- $\displaystyle\int (3z^2 - 4z + 5)\,dz$

**Example 1.2.2:**
$$\int \frac{x^2+1}{\sqrt{x}}\,dx$$

First, rewrite the integrand:
$$= \int \left(\frac{x^2}{\sqrt{x}} + \frac{1}{\sqrt{x}}\right)dx = \int \left(x^{3/2} + x^{-1/2}\right)dx$$

Now integrate:
$$= \frac{x^{5/2}}{\tfrac{5}{2}} + \frac{x^{1/2}}{\tfrac{1}{2}} + C = \frac{2}{5}x^{5/2} + 2x^{1/2} + C$$

---

### 1.2.3 Indefinite Integrals of Exponential Functions

Recall from differentiation:
- If $f(x) = e^x$ then $f'(x) = e^x$
- If $f(x) = a^x$ then $f'(x) = a^x(\ln a)$
- If $f(x) = e^{kx}$ then $f'(x) = ke^{kx}$
- If $f(x) = a^{kx}$ then $f'(x) = k(\ln a)a^{kx}$

This leads to the following integration formulas:

$$\int e^x\,dx = e^x + C$$

$$\int e^{kx}\,dx = \frac{e^{kx}}{k} + C \qquad (k \neq 0)$$

$$\int a^x\,dx = \frac{a^x}{\ln a} + C$$

$$\int a^{kx}\,dx = \frac{a^{kx}}{k(\ln a)} + C \qquad (k \neq 0)$$

**General form:**
$$\int f'(x)e^{f(x)}\,dx = e^{f(x)} + c$$

**Example 1.2.3:**
- $\displaystyle\int 9e^t\,dt = 9\int e^t\,dt = 9e^t + C$
- $\displaystyle\int e^{9t}\,dt = \frac{e^{9t}}{9} + C$
- $\displaystyle\int 3e^{\frac{5}{4}u}\,du = 3\left(\frac{e^{\frac{5}{4}u}}{\tfrac{5}{4}}\right) + C = 3\left(\frac{4}{5}\right)e^{\frac{5}{4}u} + C = \frac{12}{5}e^{\frac{5}{4}u} + C$

**You Do (practice):**
$$\int 2^{-5x}\,dx$$
*(Recall: $\int a^{kx}\,dx = \frac{a^{kx}}{k(\ln a)} + C$, $k \neq 0$)*

---

### 1.2.4 Indefinite Integral of $x^{-1}$

The power rule does not apply when $n = -1$. Instead:

$$\int x^{-1}\,dx = \int \frac{1}{x}\,dx = \ln|x| + C$$

**General form (produces log function):**
$$\int \frac{f'(x)}{f(x)}\,dx = \ln\bigl|f(x)\bigr| + c$$

> **Note:** If $x$ takes on a negative value, then $\ln x$ is undefined. The **absolute value sign** keeps that from happening.

**Example 1.2.4:**
$$\int \frac{4}{x}\,dx = 4\int \frac{1}{x}\,dx = 4\ln|x| + C$$

**You Do (practice):**
$$\int \left(\frac{-5}{x} + e^{-2x}\right)dx$$

---

### 1.2.5 Indefinite Integrals of Trigonometric Functions

$$\int \sin x\,dx = -\cos x + c$$

$$\int \cos x\,dx = \sin x + c$$

$$\int \tan x\,dx = \ln|\sec x| + c$$

$$\int \sec x\,dx = \ln|\sec x + \tan x| + c$$

$$\int \cot x\,dx = \ln|\sin x| + c$$

$$\int \sec^2 x\,dx = \tan x + c$$

$$\int \csc x\,dx = \ln|\csc x - \cot x| + c$$

$$\int \csc^2 x\,dx = -\cot x + c$$

$$\int \sec x \tan x\,dx = \sec x + c$$

$$\int \csc x \cot x\,dx = -\csc x + c$$

**Example 1.2.5:**
$$\int \left(3\cos x - 4\sin x + \frac{1}{x^2}\right)dx$$

$$= 3\int \cos x\,dx - 4\int \sin x\,dx + \int \frac{1}{x^2}\,dx$$

$$= 3\sin x + 4\cos x - \frac{1}{x} + C$$

**Example 1.2.6:**
$$\int \left(3^x - 4e^x + \frac{7}{4x}\right)dx$$

$$= \int 3^x\,dx - 4\int e^x\,dx + \frac{7}{4}\int \frac{1}{x}\,dx$$

$$= \frac{3^x}{\ln 3} - 4e^x + \frac{7}{4}\ln|x| + C$$

**Example 1.2.7:**
$$\int \frac{3x^2+4x+1}{x-1}\,dx$$

First, perform polynomial division / rewrite the integrand:
$$= \int \left(3x + 7 + \frac{8}{x-1}\right)dx$$

$$= 3\int x\,dx + 7\int dx + 8\int \frac{1}{x-1}\,dx$$

For the last term, let $u = x-1$, therefore $du = dx$:
$$= 3\cdot\frac{x^2}{2} + 7x + 8\int \frac{1}{u}\,du$$

$$= \frac{3x^2}{2} + 7x + 8\ln(u) + C$$

$$= \frac{3x^2}{2} + 7x + 8\ln(x-1) + C$$

---

## Key Equations Summary

| Rule / Function | Integral |
|---|---|
| Constant | $\displaystyle\int a\,dx = ax + C$ |
| Power Rule ($n \neq -1$) | $\displaystyle\int x^n\,dx = \frac{x^{n+1}}{n+1} + C$ |
| $x^{-1}$ | $\displaystyle\int \frac{1}{x}\,dx = \ln\|x\| + C$ |
| $e^x$ | $\displaystyle\int e^x\,dx = e^x + C$ |
| $e^{kx}$ | $\displaystyle\int e^{kx}\,dx = \frac{e^{kx}}{k} + C$ |
| $a^x$ | $\displaystyle\int a^x\,dx = \frac{a^x}{\ln a} + C$ |
| $a^{kx}$ | $\displaystyle\int a^{kx}\,dx = \frac{a^{kx}}{k(\ln a)} + C$ |
| General log | $\displaystyle\int \frac{f'(x)}{f(x)}\,dx = \ln\|f(x)\| + C$ |
| General exp | $\displaystyle\int f'(x)e^{f(x)}\,dx = e^{f(x)} + C$ |
| $\sin x$ | $\displaystyle\int \sin x\,dx = -\cos x + C$ |
| $\cos x$ | $\displaystyle\int \cos x\,dx = \sin x + C$ |
| $\tan x$ | $\displaystyle\int \tan x\,dx = \ln\|\sec x\| + C$ |
| $\sec x$ | $\displaystyle\int \sec x\,dx = \ln\|\sec x + \tan x\| + C$ |
| $\cot x$ | $\displaystyle\int \cot x\,dx = \ln\|\sin x\| + C$ |
| $\sec^2 x$ | $\displaystyle\int \sec^2 x\,dx = \tan x + C$ |
| $\csc x$ | $\displaystyle\int \csc x\,dx = \ln\|\csc x - \cot x\| + C$ |
| $\csc^2 x$ | $\displaystyle\int \csc^2 x\,dx = -\cot x + C$ |
| $\sec x \tan x$ | $\displaystyle\int \sec x \tan x\,dx = \sec x + C$ |
| $\csc x \cot x$ | $\displaystyle\int \csc x \cot x\,dx = -\csc x + C$ |

---

## Properties of Indefinite Integrals

- **Constant Multiple:** $\displaystyle\int k \cdot f(x)\,dx = k\int f(x)\,dx$
- **Sum/Difference:** $\displaystyle\int \bigl[f(x) \pm g(x)\bigr]\,dx = \int f(x)\,dx \pm \int g(x)\,dx$

---

## Links
- [[Integration Techniques]] — concept page
- [[FAD1014 Tutorial 1 — Indefinite Integrals]]
- [[FAD1014 - Mathematics II]] — course
