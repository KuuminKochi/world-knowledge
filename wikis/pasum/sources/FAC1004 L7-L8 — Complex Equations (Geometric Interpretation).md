---
title: FAC1004 L7-L8 — Complex Equations (Geometric Interpretation)
date: 2026-04-27
tags:
  - source/lecture
  - subject/mathematics
  - topic/complex-numbers
  - topic/geometry
  - status/evergreen
course: "[[FAC1004 - Advanced Mathematics II (Computing)]]"
lecturer: "[[En Hisham Safuan Mohamad Sukri]]"
---

# FAC1004 L7-L8 — Complex Equations (Geometric Interpretation)

Geometric interpretation of complex equations in the Argand plane. This lecture translates complex numbers into coordinate geometry, solves systems of geometric loci, and interprets solutions geometrically and algebraically.

## Learning Outcomes

- Understanding the geometric interpretation of complex equations
- Translating complex numbers into coordinate geometry
- Solving systems of geometric loci
- Interpreting solutions geometrically and algebraically

## Complex Equation I: Circle

The complex equation:

$$|z - z_1| = r$$

where:
- $z$ : variable point in the complex plane (Argand)
- $z_1$ : fixed complex number (fixed point / centre)
- $r$ : radius

### Interpretation

- $z - z_1$ is the resultant between two complex numbers (segment connecting $z$ and $z_1$)
- $|z - z_1|$ means the distance between two complex points in the Argand plane
- $|z - z_1| = r$ interprets as: distance between a free complex point and a fixed complex point is a constant
- **Locus obtained is a circle with centre $z_1$ and radius $r$**

### Cartesian Equation: Circle

Consider $z_1 = a + bi$, the derivation of Cartesian equation:

$$|z - (a + bi)| = r$$

Squaring both sides and substituting $z = x + yi$ yields:

$$(x - a)^2 + (y - b)^2 = r^2$$

### Example 1: Circle Loci

Find the locus of point $z$ satisfying the complex equation below. Hence, sketch the locus.

a) $|z - (1 + i)| = 1$ — Circle centre $1 + i$, radius $1$
b) $|z + 1 + i| = 2$ — Circle centre $-1 - i$, radius $2$
c) $|z - 2 + 3i| = 3$ — Circle centre $2 - 3i$, radius $3$
d) $|2z - 6 + 4i| = 4$ — Rewrite as $|z - (3 - 2i)| = 2$; circle centre $3 - 2i$, radius $2$
e) $|5 - z - i| = 5$ — Rewrite as $|z - (5 - i)| = 5$; circle centre $5 - i$, radius $5$

### Example 2: Special Circle Forms

1. Find and sketch the locus satisfying $z\overline{z} = 9$.
   - Since $z\overline{z} = |z|^2$, we have $|z|^2 = 9$, so $|z| = 3$.
   - This is a circle centred at the origin with radius $3$.

2. What is the locus of point $z$, if the complex equation is $\left|\frac{z - 2 + i}{z + 2 - i}\right| = 3$?
   - This represents an Apollonius circle (a circle of Apollonius) where the ratio of distances from $z$ to two fixed points is constant.

### Example 3: Circle with Max/Min Modulus and Argument

Suppose we have a circle of radius $3$ units with centre at point $4 + 4i$.

a) Complex equation: $|z - (4 + 4i)| = 3$

b) Find $|z|_{\min}$ and $|z|_{\max}$:
   - Distance from origin to centre: $|4 + 4i| = \sqrt{4^2 + 4^2} = 4\sqrt{2} \approx 5.66$
   - $|z|_{\min} = 4\sqrt{2} - 3$
   - $|z|_{\max} = 4\sqrt{2} + 3$

c) Find $\min[\arg(z)]$ and $\max[\arg(z)]$:
   - These occur at the tangent lines from the origin to the circle.
   - The angle is found using geometry: $\arg(4 + 4i) = \frac{\pi}{4}$ and $\sin\alpha = \frac{3}{4\sqrt{2}}$
   - $\min[\arg(z)] = \frac{\pi}{4} - \alpha$
   - $\max[\arg(z)] = \frac{\pi}{4} + \alpha$

---

## Complex Equation II: Perpendicular Bisector

The complex equation:

$$|z - z_1| = |z - z_2|$$

where:
- $z$ : variable point in the complex plane (Argand)
- $z_1$ : fixed complex number (fixed point)
- $z_2$ : another fixed complex number (fixed point)

### Interpretation

- $|z - z_1|$ means distance between free point and complex number $z_1$
- $|z - z_2|$ means distance between free point and complex number $z_2$
- $|z - z_1| = |z - z_2|$ means the point $z$ is equidistant from the fixed points $z_1$ and $z_2$
- **Locus obtained is a straight line** (the perpendicular bisector of the line segment joining $z_1$ and $z_2$)

### Cartesian Equation: Perpendicular Bisector

Consider $z_1 = a + bi$ and $z_2 = c + di$, the derivation of Cartesian equation:

$$|z - (a + bi)| = |z - (c + di)|$$

Squaring both sides and expanding yields a linear equation in $x$ and $y$ representing the perpendicular bisector.

### Example 4: Perpendicular Bisector Loci

Find the locus of point $z$ satisfying the complex equation below. Hence, sketch the locus.

a) $|z - 1| = |z - 4|$ — Perpendicular bisector of segment joining $1$ and $4$ on real axis
c) $|z + 3i| = |z + 4|$ — Perpendicular bisector of segment joining $-3i$ and $-4$
d) $|i - 5 - z| = |z - (3 - 3i)|$ — Rewrite as $|z - (-5 + i)| = |z - (3 - 3i)|$; perpendicular bisector of segment joining $-5 + i$ and $3 - 3i$

### Example 5: Perpendicular Bisector with Min Distance

1. Determine the locus of point $z$ that is equidistant to $-2 + 3i$ and $4 - i$. Hence, find the complex number satisfying $|z - 2|_{\min}$.
   - Locus is the perpendicular bisector of the segment joining $-2 + 3i$ and $4 - i$.
   - The point on this line closest to $2$ gives the minimum $|z - 2|$.

2. Find the locus of point $z$ satisfying $\text{Im}(z - 2i) = 4$.
   - Let $z = x + yi$. Then $\text{Im}(x + yi - 2i) = \text{Im}(x + (y-2)i) = y - 2 = 4$.
   - So $y = 6$, which is a horizontal line.

---

## Complex Equation III: Half-line

The complex equation:

$$\arg(z - z_1) = \theta$$

where:
- $z$ : variable point in the complex plane (Argand)
- $z_1$ : fixed complex number (fixed point)
- $\theta$ : principal argument formed by initial and terminal side satisfying $(-\pi, \pi]$

### Interpretation

- Resultant $z - z_1$ is the segment connecting the two complex points ($z$ and $z_1$)
- Interpretation: principal value of angle measured from initial side (positive real axis) to the terminal side (formed from $z - z_1$), lying in the range of $(-\pi, \pi]$
- **IMPORTANT: The complex number $z_1$ is excluded from the locus**, hence the open/hollow circle in diagrams
- **Locus obtained is a half-line (ray) from $z_1$ at angle $\theta$**

### Cartesian Equation: Half-line

Consider $z_1 = a + bi$, the derivation of Cartesian equation:

$$\arg(z - (a + bi)) = \theta$$

This gives a line through $(a, b)$ with slope $\tan\theta$, but only the half extending from $(a, b)$ in the direction of angle $\theta$.

### Example 6: Half-line Cartesian Equations

Find the Cartesian equation of the following complex equations:

a) $\arg(z) = \frac{\pi}{3}$ — Half-line from origin at angle $\frac{\pi}{3}$; Cartesian: $y = \sqrt{3}x$, $x > 0$
b) $\arg(z - i) = -\frac{2\pi}{3}$ — Half-line from $i$ (point $(0,1)$) at angle $-\frac{2\pi}{3}$
c) $\arg(z + 1) = \frac{\pi}{2}$ — Half-line from $-1$ (point $(-1,0)$) vertically upward; $x = -1$, $y > 0$
d) $\arg(z + 2 + 3i) = -\frac{\pi}{6}$ — Half-line from $-2 - 3i$ at angle $-\frac{\pi}{6}$
e) $\arg(z - 2 - 2i) = -\frac{3\pi}{4}$ — Half-line from $2 + 2i$ at angle $-\frac{3\pi}{4}$

---

## Extended Questions: Systems of Loci

Determine the complex number $z$ satisfying both complex equations for each of the following:

a) $|z - (-1 + i)| = |z - 5 - i|$ and $|z - 3i| = 2$
   - Perpendicular bisector intersecting a circle

b) $|z + 2 - i| = 3$ and $\arg(z - 1) = \frac{3\pi}{4}$
   - Circle intersecting a half-line

c) $|z - 2 + 3i)| = |z + 4 - i|$ and $\arg(z + 1) = \frac{\pi}{4}$
   - Perpendicular bisector intersecting a half-line

d) $\text{Re}(z + \overline{z}) = 2$ and $\text{Im}(-3\overline{z}) = -2$
   - Since $z + \overline{z} = 2\text{Re}(z) = 2x$, we get $2x = 2 \Rightarrow x = 1$
   - Let $z = x + yi$. Then $\overline{z} = x - yi$, so $-3\overline{z} = -3x + 3yi$, giving $\text{Im}(-3\overline{z}) = 3y = -2 \Rightarrow y = -\frac{2}{3}$
   - Intersection point: $z = 1 - \frac{2}{3}i$

## Summary

This lecture develops the geometric interpretation of complex equations. Students learn to translate between complex equations and their geometric representations in the Argand plane:

| Complex Equation | Geometric Locus |
|---|---|
| $\|z - z_1\| = r$ | Circle with centre $z_1$ and radius $r$ |
| $\|z - z_1\| = \|z - z_2\|$ | Perpendicular bisector of segment joining $z_1$ and $z_2$ |
| $\arg(z - z_1) = \theta$ | Half-line (ray) from $z_1$ at angle $\theta$ (excluding $z_1$) |

Key skills include finding Cartesian equivalents, sketching loci, and determining max/min modulus and argument for circle loci.

## Related

- [[FAC1004 - Advanced Mathematics II (Computing)]] — main course page
- [[Complex Numbers]] — concept page
- [[FAC1004 L5-L6 — Functions of Complex Numbers (n-th Roots)]] — previous lecture

## Source File

`LECTURE_NOTES_2526/[L7 L8] COMPLEX EQUATIONS.pdf`
