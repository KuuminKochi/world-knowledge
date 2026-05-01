---
title: "FAD1014 L11-L12 — Area Under Curves"
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics-ii
  - topic/integration
  - status/evergreen
course: "[[FAD1014 - Mathematics II]]"
---

# FAD1014 L11-L12: Area Under Curves

Lecture notes from **Week 6** covering the definite integral, Riemann sums, and their applications to calculating areas under and between curves.

---

## 1. From Riemann Sums to the Definite Integral

### 1.1 Approximating Area with Rectangles

To find the area under a curve $y = f(x)$, we approximate it by adding up the areas of rectangles:

- **Riemann sum**: the result of adding rectangles to approximate area under a curve.
- **Subinterval**: the width of one rectangle.
- **Partition**: the entire interval $[a, b]$ divided into subintervals.
- Subintervals do not all have to be the same size.

If the partition is denoted by $P$, the length of the longest subinterval is called the **norm** of $P$, denoted $\|P\|$.

> As $\|P\|$ gets smaller, the approximation for the area gets better.

### 1.2 The Limit Definition

For a partition $P$ of $[a, b]$:

$$\text{Area} = \lim_{\|P\| \to 0} \sum_{k=1}^{n} f(c_k)\,\Delta x_k$$

This limit is called the **definite integral** of $f$ over $[a, b]$.

### 1.3 Equal Subintervals

If we use $n$ subintervals of equal length:

$$\Delta x = \frac{b - a}{n}$$

The definite integral is then:

$$\lim_{n \to \infty} \sum_{k=1}^{n} f(c_k)\,\Delta x = \int_a^b f(x)\,dx$$

Leibnitz introduced the integral symbol $\int$ as a stylized "S" for sum. Note that the very small change in $x$ becomes $dx$.

### 1.4 Anatomy of the Definite Integral

$$\int_a^b f(x)\,dx$$

| Part | Meaning |
|------|---------|
| $\int$ | Integration symbol |
| $a$ | Lower limit of integration |
| $b$ | Upper limit of integration |
| $f(x)$ | Integrand |
| $dx$ | Variable of integration (dummy variable) |

> The variable of integration is called a **dummy variable** because the answer does not depend on the variable chosen.

### 1.5 The Area Function and FTC

Let $A_a(x)$ = area under the curve from $a$ to $x$ (where $a$ is constant).

Then $A_a(x+h) - A_a(x)$ is the area of a thin strip from $x$ to $x+h$.

By the squeeze theorem using min and max heights:

$$h \cdot \min f \le A_a(x+h) - A_a(x) \le h \cdot \max f$$

Dividing by $h$ and taking the limit as $h \to 0$:

$$\frac{d}{dx} A_a(x) = f(x)$$

Since $A_a(x) = F(x) + c$ and $A_a(a) = 0$:

$$A_a(x) = F(x) - F(a)$$

> **Area under curve from $a$ to $x$ = antiderivative at $x$ minus antiderivative at $a$.**

---

## 2. Summary Chain

$$\text{Area} = \lim_{\|P\| \to 0} \sum_{k=1}^{n} f(c_k)\,\Delta x_k = \int_a^b f(x)\,dx = F(x) - F(a)$$

---

## 3. Area Under a Single Curve

### 3.1 Fundamental Theorem of Calculus (Evaluation Form)

If $f$ is continuous on $[a, b]$ and $F$ is an antiderivative of $f$:

$$\int_a^b f(x)\,dx = F(b) - F(a) = \bigl[F(x)\bigr]_a^b$$

**Example:** Find the area under $y = x^2$ from $x = 1$ to $x = 2$.

$$\int_1^2 x^2\,dx = \left[\frac{x^3}{3}\right]_1^2 = \frac{8}{3} - \frac{1}{3} = \frac{7}{3}$$

### 3.2 Four-Step Procedure for Area Under a Curve

1. **Sketch a graph** of $f(x)$ over $[a, b]$.
2. **Find any $x$-intercepts** of $f(x)$ in $[a, b]$. These divide the total region into subregions.
3. **The definite integral will be positive** for subregions above the $x$-axis and **negative** for subregions below the $x$-axis. Use separate integrals to find the (positive) areas of the subregions.
4. **The total area is the sum** of the areas of all of the subregions.

### 3.3 Area When the Curve Crosses the x-axis

If the curve dips below the $x$-axis, the definite integral gives a negative value for that portion. Since **area is always positive**, take the absolute value or negate the integral for regions below the axis.

**Example 6.2.3:** Find the area bounded by $f(x) = x^2 - 4$, the $x$-axis, and $x = 0, x = 2$.

$$\int_0^2 (x^2 - 4)\,dx = \left[\frac{x^3}{3} - 4x\right]_0^2 = \left(\frac{8}{3} - 8\right) - 0 = -\frac{16}{3}$$

The answer is negative because the area is below the $x$-axis. Since area must be positive:

$$\text{Area} = \left|-\frac{16}{3}\right| = \frac{16}{3}$$

**Example 6.2.4:** Find the area between the $x$-axis and $f(x) = x^2 - 4$ from $x = 0$ to $x = 4$.

The curve crosses the $x$-axis at $x = 2$. Split into two integrals:

$$\text{Area} = \left|\int_0^2 (x^2 - 4)\,dx\right| + \left|\int_2^4 (x^2 - 4)\,dx\right|$$

$$= \left|-\frac{16}{3}\right| + \left|\frac{16}{3}\right| = \frac{16}{3} + \frac{32}{3} = 16$$

**Example 6.2.2:** Find the area between the $x$-axis and $y = \cos x$ from $x = 0$ to $x = \frac{3\pi}{2}$.

$$\int_0^{\pi/2} \cos x\,dx - \int_{\pi/2}^{3\pi/2} \cos x\,dx = \bigl[\sin x\bigr]_0^{\pi/2} - \bigl[\sin x\bigr]_{\pi/2}^{3\pi/2}$$

$$= (1 - 0) - (-1 - 1) = 1 + 2 = 3$$

### 3.4 Key Notes on Sign

- An **area is always positive**.
- The **definite integral is positive** for areas above the $x$-axis but **negative** for areas below the axis.
- To find an area, we need to know whether the curve crosses the $x$-axis between the boundaries.
- For areas above the axis, the definite integral gives the area directly.
- For areas below the axis, we need to change the sign of the definite integral to find the area.

---

## 4. Area Between Two Curves

### 4.1 Vertical Strips

The area $A$ of the region bounded by $y = f(x)$ (top), $y = g(x)$ (bottom), and the lines $x = a, x = b$, where $f(x) \ge g(x)$ on $[a, b]$:

$$A = \int_a^b \bigl[f(x) - g(x)\bigr]\,dx$$

Or using the lecture notation:

$$\text{Area} = \int_a^b \bigl[f_1(x) - f_2(x)\bigr]\,dx$$

**Example:** Find the area between $y_1 = 2 - x^2$ and $y_2 = -x$.

Intersections: $2 - x^2 = -x \Rightarrow x^2 - x - 2 = 0 \Rightarrow x = -1, 2$.

$$\text{Area} = \int_{-1}^{2} \bigl[(2 - x^2) - (-x)\bigr]\,dx = \int_{-1}^{2} (2 - x^2 + x)\,dx$$

$$= \left[2x - \frac{x^3}{3} + \frac{x^2}{2}\right]_{-1}^{2} = \left(4 - \frac{8}{3} + 2\right) - \left(-2 + \frac{1}{3} + \frac{1}{2}\right) = \frac{10}{3} - \left(-\frac{7}{6}\right) = \frac{27}{6} = \frac{9}{2}$$

### 4.2 Horizontal Strips

When vertical strips would require splitting the integral into multiple parts, it may be easier to use **horizontal strips** (integrate with respect to $y$).

- Solve both curves for $x$ in terms of $y$.
- The width of the strip is $dy$.
- The length of the strip is $(\text{right curve} - \text{left curve})$.

**Example:** Area between $y = \sqrt{x}$ and $y = x - 2$.

With vertical strips:
$$\int_0^2 \sqrt{x}\,dx + \int_2^4 \bigl[\sqrt{x} - (x - 2)\bigr]\,dx \quad \text{(two integrals)}$$

With horizontal strips: rewrite as $x = y^2$ and $x = y + 2$.

$$\text{Area} = \int_0^2 \bigl[(y + 2) - y^2\bigr]\,dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_0^2 = 2 + 4 - \frac{8}{3} = \frac{10}{3}$$

### 4.3 General Strategy for Area Between Curves

1. **Sketch the curves.**
2. **Decide on vertical or horizontal strips.** Pick whichever is easier to write formulas for the length of the strip, and/or whichever will let you integrate fewer times.
3. **Write an expression for the area of the strip.** If the width is $dx$, the length must be in terms of $x$. If the width is $dy$, the length must be in terms of $y$.
4. **Find the limits of integration.** If using $dx$, the limits are $x$ values; if using $dy$, the limits are $y$ values.
5. **Integrate to find area.**

---

## 5. Area with Respect to the y-axis

The area bounded by a curve, the $y$-axis, and the lines $y = c$ and $y = d$ is found by switching the $x$s and $y$s in the formula:

$$\int_a^b y\,dx \quad \text{becomes} \quad \int_c^d x\,dy$$

**Example:** Find the area between $y = \sqrt{x}$, the $y$-axis, and $y = 1$ to $y = 2$.

Rewrite $y = \sqrt{x}$ as $x = y^2$:

$$\int_1^2 y^2\,dy = \left[\frac{y^3}{3}\right]_1^2 = \frac{8}{3} - \frac{1}{3} = \frac{7}{3}$$

---

## 6. Harder Areas: Two Methods

### Method 1: Subtract Areas Separately

Find the area under the upper curve, subtract the area under the lower curve (or geometric shape).

**Example:** Area enclosed by $y = 2x - x^2$ and $y = x$.

Intersections: $x = 2x - x^2 \Rightarrow x^2 - x = 0 \Rightarrow x = 0, 1$.

$$\text{Area under curve} = \int_0^1 (2x - x^2)\,dx = \left[x^2 - \frac{x^3}{3}\right]_0^1 = \frac{2}{3}$$

$$\text{Area of triangle} = \frac{1}{2}(1)(1) = \frac{1}{2}$$

$$\text{Required area} = \frac{2}{3} - \frac{1}{2} = \frac{1}{6}$$

### Method 2: Integrate the Difference

Subtract the functions first, then integrate:

$$(2x - x^2) - x = x - x^2$$

$$\text{Area} = \int_0^1 (x - x^2)\,dx = \left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$$

**Example (a):** $y = x^2 + 2$ and $y = 6$.

Intersections: $x^2 + 2 = 6 \Rightarrow x = \pm 2$.

$$\text{Area under curve} = \int_{-2}^{2} (x^2 + 2)\,dx = \left[\frac{x^3}{3} + 2x\right]_{-2}^{2} = \frac{16}{3}$$

$$\text{Shaded area} = \text{area of rectangle} - \text{area under curve} = 24 - \frac{16}{3} = 18\frac{2}{3}$$

**Example (b):** $y = 4 - x^2$ and $y = x + 2$.

Intersections: $4 - x^2 = x + 2 \Rightarrow x^2 + x - 2 = 0 \Rightarrow x = -2, 1$.

Points: $(-2, 0)$ and $(1, 3)$.

---

## 7. Area of a Symmetrical Curve

If a curve crosses the $x$-axis between the limits of integration, part of the area will be above the axis and part below.

**Example:** $y = x^3$ between $-1$ and $+1$.

The symmetry of the curve means that the **integral** from $-1$ to $+1$ is $0$.

To find the **area**, we could integrate from $0$ to $1$ and, because of the symmetry, double the answer.

For a curve which wasn't symmetrical, we could find the two areas separately and then add.

---

## Properties of Definite Integrals

1. $\displaystyle\int_a^a f(x)\,dx = 0$
2. $\displaystyle\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$
3. $\displaystyle\int_a^b \bigl[f(x) + g(x)\bigr]\,dx = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx$
4. $\displaystyle\int_a^b c \cdot f(x)\,dx = c\int_a^b f(x)\,dx$
5. $\displaystyle\int_a^b f(x)\,dx + \int_b^c f(x)\,dx = \int_a^c f(x)\,dx$

---

## Links
- [[Integration Techniques]] — concept page for antiderivative methods
- [[FAD1014 Tutorial 5 — Area Enclosed by Curves]]
- [[FAD1014 - Mathematics II]] — course page
