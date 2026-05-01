---
title: "FAD1014 L3-L4 — Integration by Substitution"
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics-ii
  - topic/integration
  - status/budding
course: "[[FAD1014 - Mathematics II]]"
---

# L3-L4: Integration by Substitution

Lecture notes covering the substitution method (u-substitution) for evaluating integrals. This method is the reverse of the chain rule and depends on the idea of a differential.

---

## 1. Substitution Basics

In finding the antiderivative for some functions, many standard techniques fail. Substitution can sometimes remedy this problem.

**Differential**: If $u = f(x)$, then the differential of $u$, written $du$, is defined as:
$$du = f'(x)\,dx$$

**Example**: If $u = 2x^3 + 1$, then $du = 6x^2\,dx$.

---

## 2. Integration by Substitution (The Method)

Method of integration related to chain rule differentiation. If $u$ is a function of $x$, then we can use the formula:
$$\int f\,dx = \int \left(\frac{f}{du/dx}\right) du$$

More commonly, if $u = g(x)$ and $du = g'(x)\,dx$, then:
$$\int f[g(x)]g'(x)\,dx = \int f(u)\,du = F(u) + C = F(g(x)) + C$$

The core process is: **Pick $u$ → Compute $du$ → Substitute in → Integrate → Back-substitute**.

---

## 3. Choosing $u$

In general, for the types of problems in this course, there are three primary cases for choosing $u$:

1. **The quantity under a root or raised to a power**
2. **The quantity in the denominator**
3. **The exponent on $e$**

Some integrands may need to be rearranged to fit one of these cases. Also, remember that $du$ is the derivative of $u$.

---

## 4. Handling Missing Constant Factors

We haven't always needed to modify $du$ explicitly, because in some problems $du$ (or a constant multiple of it) already appears in the integrand. When it doesn't, we can multiply and divide by the needed constant.

**Key idea**: If $du = k \cdot \text{(something)}\,dx$ but the integrand only has $\text{(something)}\,dx$, multiply inside the integral by $k$ and counteract it by multiplying the entire integral by $1/k$.

```mermaid
flowchart TD
    A([Start: ∫ f(g(x)) g'(x) dx]) --> B{Pick u}
    B -->|"Case 1"| C1["Quantity under a root<br/>or raised to a power"]
    B -->|"Case 2"| C2["Quantity in the denominator"]
    B -->|"Case 3"| C3["Exponent on e"]
    C1 --> D[Compute du = g'(x) dx]
    C2 --> D
    C3 --> D
    D --> E{Does du match<br/>integrand exactly?}
    E -->|Yes| F[Substitute directly]
    E -->|No| G["Multiply / divide<br/>by constant k"]
    F --> H[Integrate ∫ f(u) du]
    G --> H
    H --> I[Back-substitute u = g(x)]
    I --> J([F(g(x)) + C])
```

---

## 5. Worked Examples by Category

### 5.1 Direct Substitution (Perfect $du$ Match)

**Example 2.1.1**: Find $\displaystyle\int (2x^3 + 1)^4 \cdot 6x^2\,dx$
- Let $u = 2x^3 + 1$, then $du = 6x^2\,dx$
- Substitute: $\displaystyle\int u^4\,du = \frac{u^5}{5} + C$
- Back-substitute: $\displaystyle\frac{(2x^3 + 1)^5}{5} + C$

**Example 2.1.6**: Find $\displaystyle\int 3x^2(x^3 - 5)^9\,dx$
- Let $u = x^3 - 5$, then $du = 3x^2\,dx$
- $\displaystyle\int u^9\,du = \frac{u^{10}}{10} + C = \frac{(x^3 - 5)^{10}}{10} + C$

### 5.2 Substitution Requiring Constant Adjustment

**Example 2.1.2 & 2.1.3**: Find $\displaystyle\int x^2\sqrt{x^3 + 1}\,dx$
- Let $u = x^3 + 1$, then $du = 3x^2\,dx$
- We have $x^2\,dx$ but need $3x^2\,dx$:
$$\int x^2\sqrt{x^3 + 1}\,dx = \frac{1}{3}\int \sqrt{u}\,du = \frac{1}{3} \cdot \frac{u^{3/2}}{3/2} + C = \frac{2}{9}(x^3 + 1)^{3/2} + C$$

**Example 2.1.4**: Find $\displaystyle\int \frac{x + 3}{(x^2 + 6x)^2}\,dx$
- Let $u = x^2 + 6x$, then $du = (2x + 6)\,dx = 2(x + 3)\,dx$
- Multiply inside by 2, outside by $1/2$:
$$= \frac{1}{2}\int \frac{du}{u^2} = \frac{1}{2}\int u^{-2}\,du = \frac{1}{2} \cdot \frac{u^{-1}}{-1} + C = \frac{-1}{2(x^2 + 6x)} + C$$

### 5.3 Variable Substitution (Avoiding Bad Choices)

Choosing $u$ poorly leads to an integral still containing the original variable.

**Example 2.2.1**: $\displaystyle\int (x + 8)^{1/7}\,dx$
- **Correct**: Let $u = x + 8$, therefore $du = dx$. Then $\displaystyle\int u^{1/7}\,du$
- **Incorrect**: Let $u = x$, which just gives $\displaystyle\int (u + 8)^{1/7}\,du$ — no simplification.

**Example 2.2.2**: $\displaystyle\int \frac{x + 1}{x^2 + 2x + 3}\,dx$
- **Correct**: Let $u = x^2 + 2x + 3$, then $du = (2x + 2)\,dx = 2(x + 1)\,dx$
- **Incorrect**: Let $u = x + 1$, which leaves $x$ in the denominator.

### 5.4 Trigonometric Function Substitution

**Example 2.3.1**: Find $\displaystyle\int x\cos(3x^2)\,dx$
- Let $u = 3x^2$, then $du = 6x\,dx$ so $\frac{du}{6} = x\,dx$
- $\displaystyle\frac{1}{6}\int \cos u\,du = \frac{1}{6}\sin u + C = \frac{1}{6}\sin(3x^2) + C$

**Example 2.3.2**: Find $\displaystyle\int (\sin x + 1)^7 \cos x\,dx$
- Let $u = \sin x + 1$, then $du = \cos x\,dx$
- $\displaystyle\int u^7\,du = \frac{u^8}{8} + C = \frac{1}{8}(\sin x + 1)^8 + C$

### 5.5 Exponential Function Substitution

**Example 2.4.1**: Find $\displaystyle\int e^{3x}\,dx$
- Let $u = 3x$, then $\frac{du}{3} = dx$
- $\displaystyle\frac{1}{3}\int e^u\,du = \frac{1}{3}e^{3x} + C$

**Example 2.4.2**: Find $\displaystyle\int 5^{x^2} x\,dx$
- Let $u = x^2$, then $\frac{du}{2} = x\,dx$
- $\displaystyle\frac{1}{2}\int 5^u\,du = \frac{5^u}{2\ln 5} + C = \frac{5^{x^2}}{2\ln 5} + C$

**Example 2.4.3**: Find $\displaystyle\int \frac{e^{\sqrt{x}}}{\sqrt{x}}\,dx$
- Let $u = \sqrt{x}$, then $2\,du = \frac{1}{\sqrt{x}}\,dx$
- $\displaystyle 2\int e^u\,du = 2e^{\sqrt{x}} + C$

### 5.6 Resulting Logarithmic Function

When substitution produces $\displaystyle\int \frac{du}{u}$, the result is $\ln|u| + C$.

**Example 2.1.5**: Find $\displaystyle\int \frac{x^2 + 1}{x^3 + 3x}\,dx$
- Let $u = x^3 + 3x$, then $du = (3x^2 + 3)\,dx = 3(x^2 + 1)\,dx$
- $\displaystyle\frac{1}{3}\int \frac{du}{u} = \frac{1}{3}\ln|x^3 + 3x| + C$

**Example 2.1.9**: Find $\displaystyle\int \frac{e^{3t}}{e^{3t} + 2}\,dt$
- Let $u = e^{3t} + 2$, then $\frac{du}{3e^{3t}} = dt$
- $\displaystyle\frac{1}{3}\int \frac{du}{u} = \frac{1}{3}\ln(e^{3t} + 2) + C$

**Example 2.5.3**: Find $\displaystyle\int \frac{24x + 9}{8x^2 + 6x + 2}\,dx$
- Factor numerator: $3(8x + 3)$
- Let $u = 8x^2 + 6x + 2$, then $du = (16x + 6)\,dx = 2(8x + 3)\,dx$
- $\displaystyle\frac{3}{2}\int \frac{du}{u} = \frac{3}{2}\ln|8x^2 + 6x + 2| + C$

### 5.7 Resulting Inverse Trigonometric Function

Two fundamental integration formulas arise frequently:
$$\int \frac{1}{\sqrt{1 - x^2}}\,dx = \sin^{-1} x + C$$
$$\int \frac{1}{x^2 + 1}\,dx = \tan^{-1} x + C$$

Generalized forms via substitution:
$$\int \frac{dx}{\sqrt{a^2 - x^2}} = \sin^{-1}\frac{x}{a} + C \quad (a > 0)$$
$$\int \frac{dx}{a^2 + x^2} = \frac{1}{a}\tan^{-1}\frac{x}{a} + C \quad (a \neq 0)$$

**Example 2.6.1**: Find $\displaystyle\int \frac{dx}{\sqrt{9 - x^2}}$
- Rewrite: $\displaystyle\int \frac{dx}{3\sqrt{1 - (x/3)^2}}$
- Let $u = x/3$, then $du = \frac{1}{3}\,dx$
- $\displaystyle\int \frac{du}{\sqrt{1 - u^2}} = \sin^{-1}\frac{x}{3} + C$

**Example 2.6.3**: Find $\displaystyle\int \frac{x}{x^4 + 9}\,dx$
- Let $u = x^2$, then $du = 2x\,dx$
- $\displaystyle\frac{1}{2}\int \frac{du}{u^2 + 9} = \frac{1}{2} \cdot \frac{1}{3}\tan^{-1}\frac{u}{3} + C = \frac{1}{6}\tan^{-1}\frac{x^2}{3} + C$

---

## 6. Summary of Key Patterns

| Pattern | Choice of $u$ | Notes |
|---------|--------------|-------|
| Power/Root | Quantity inside power or under root | Often requires constant adjustment |
| Rational | Quantity in denominator | Check if numerator is derivative of denominator |
| Exponential | Exponent on $e$ or base $a$ | Remember $\int a^x\,dx = \frac{a^x}{\ln a} + C$ |
| Logarithmic | Quantity in denominator | Result is $\ln|u|$ when $\int du/u$ |
| Inverse Trig | Forms matching $\sqrt{a^2 - x^2}$ or $a^2 + x^2$ | May need substitution to match standard form |

---

## Links
- [[Integration Techniques]] — concept page
- [[FAD1014 Tutorial 1 — Indefinite Integrals]]
- [[FAD1014 - Mathematics II]] — course
