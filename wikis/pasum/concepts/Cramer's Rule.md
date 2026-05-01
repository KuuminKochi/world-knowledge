---
title: Cramer's Rule
date: 2026-04-29
tags:
  - concept
  - subject/mathematics
  - topic/linear-algebra
  - status/seedling
aliases:
  - Cramer's Rule
  - Determinant Method for Linear Systems
sources:
  - "[[FAD1015 L29-L30 — Matrices (Inverse & Systems of Equations)]]"
  - "[[FAD1015 Tutorial 13 — Matrices]]"
parent:
  - "[[Matrices]]"
  - "[[Systems of Linear Equations]]"
---

# Cramer's Rule

A method for solving a system of $n$ linear equations in $n$ variables using determinants. Named after Swiss mathematician **Gabriel Cramer** (1704–1752), who published it in 1750.

---

## General Statement

For a system $AX = B$ where $A$ is an $n \times n$ non-singular coefficient matrix ($|A| \neq 0$), the unique solution is:

$$x_i = \frac{|A_i|}{|A|} \quad \text{for } i = 1, 2, \ldots, n$$

where $A_i$ is the matrix formed by **replacing the $i$-th column of $A$ with the constants column $B$**.

$$A_i = \begin{bmatrix} a_{11} & \cdots & b_1 & \cdots & a_{1n} \\ a_{21} & \cdots & b_2 & \cdots & a_{2n} \\ \vdots & & \vdots & & \vdots \\ a_{n1} & \cdots & b_n & \cdots & a_{nn} \end{bmatrix} \quad \text{(column $i$ replaced by $B$)}$$

---

## Why Cramer's Rule Works

Cramer's Rule follows directly from the matrix inverse formula $X = A^{-1}B$ and the adjoint method:

$$A^{-1} = \frac{1}{|A|} \text{adj}(A) = \frac{1}{|A|} C^T$$

where $C$ is the cofactor matrix. Multiplying both sides by $B$:

$$X = \frac{1}{|A|} C^T B$$

For the $i$-th component $x_i$, this equals $\frac{1}{|A|}$ times the dot product of the $i$-th row of $C^T$ (i.e., the $i$-th column of $C$) with $B$. But by the **cofactor expansion of a determinant**, this is exactly $|A_i|$ — the determinant of $A$ with the $i$-th column replaced by $B$.

In short: $x_i = \frac{\sum b_j C_{ji}}{|A|} = \frac{|A_i|}{|A|}$.

---

## 2×2 Cramer's Rule

For the system:
$$\begin{aligned} a_1 x + b_1 y &= c_1 \\ a_2 x + b_2 y &= c_2 \end{aligned}$$

**Step 1:** Form coefficient matrix $A = \begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix}$, constant matrix $B = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$

**Step 2:** Compute $|A| = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1$

**Step 3:** Compute $|A_x|$ (column 1 replaced by $B$):
$$|A_x| = \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix} = c_1 b_2 - c_2 b_1$$

**Step 4:** Compute $|A_y|$ (column 2 replaced by $B$):
$$|A_y| = \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix} = a_1 c_2 - a_2 c_1$$

**Step 5:** Solve:
$$x = \frac{|A_x|}{|A|}, \quad y = \frac{|A_y|}{|A|}$$

### Worked Example (2×2)

Solve: $2x + 3y = 8$, $x - y = -1$

$$\begin{aligned} |A| &= \begin{vmatrix} 2 & 3 \\ 1 & -1 \end{vmatrix} = 2(-1) - 1(3) = -2 - 3 = -5 \\ |A_x| &= \begin{vmatrix} 8 & 3 \\ -1 & -1 \end{vmatrix} = 8(-1) - (-1)(3) = -8 + 3 = -5 \\ |A_y| &= \begin{vmatrix} 2 & 8 \\ 1 & -1 \end{vmatrix} = 2(-1) - 1(8) = -2 - 8 = -10 \end{aligned}$$

$$x = \frac{-5}{-5} = 1, \quad y = \frac{-10}{-5} = 2$$

> **Check:** $2(1) + 3(2) = 8$ ✓, $1 - 2 = -1$ ✓

---

## 3×3 Cramer's Rule

For the system:
$$\begin{aligned} a_1 x + b_1 y + c_1 z &= d_1 \\ a_2 x + b_2 y + c_2 z &= d_2 \\ a_3 x + b_3 y + c_3 z &= d_3 \end{aligned}$$

**Components:**

$$|A| = \begin{vmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{vmatrix}$$

$$|A_x| = \begin{vmatrix} d_1 & b_1 & c_1 \\ d_2 & b_2 & c_2 \\ d_3 & b_3 & c_3 \end{vmatrix}, \quad |A_y| = \begin{vmatrix} a_1 & d_1 & c_1 \\ a_2 & d_2 & c_2 \\ a_3 & d_3 & c_3 \end{vmatrix}, \quad |A_z| = \begin{vmatrix} a_1 & b_1 & d_1 \\ a_2 & b_2 & d_2 \\ a_3 & b_3 & d_3 \end{vmatrix}$$

**Solution:**
$$x = \frac{|A_x|}{|A|}, \quad y = \frac{|A_y|}{|A|}, \quad z = \frac{|A_z|}{|A|}$$

### Worked Example (3×3)

Solve:
$$\begin{aligned} x + y - z &= 0 \\ 2x - 3y + z &= 1 \\ 2x + y + 2z &= 7 \end{aligned}$$

**Step 1:** $|A|$ — compute by cofactor expansion along row 1:
$$\begin{aligned} |A| &= 1 \cdot \begin{vmatrix} -3 & 1 \\ 1 & 2 \end{vmatrix} - 1 \cdot \begin{vmatrix} 2 & 1 \\ 2 & 2 \end{vmatrix} + (-1) \cdot \begin{vmatrix} 2 & -3 \\ 2 & 1 \end{vmatrix} \\ &= 1(-6 - 1) - 1(4 - 2) - 1(2 + 6) \\ &= 1(-7) - 1(2) - 1(8) \\ &= -7 - 2 - 8 = -17 \end{aligned}$$

**Step 2:** $|A_x|$ (column 1 replaced by $d$):
$$\begin{aligned} |A_x| &= \begin{vmatrix} 0 & 1 & -1 \\ 1 & -3 & 1 \\ 7 & 1 & 2 \end{vmatrix} \\ &= 0 \cdot \begin{vmatrix} -3 & 1 \\ 1 & 2 \end{vmatrix} - 1 \cdot \begin{vmatrix} 1 & 1 \\ 7 & 2 \end{vmatrix} + (-1) \cdot \begin{vmatrix} 1 & -3 \\ 7 & 1 \end{vmatrix} \\ &= 0 - 1(2 - 7) - 1(1 + 21) \\ &= 0 - 1(-5) - 1(22) \\ &= 5 - 22 = -17 \end{aligned}$$

**Step 3:** $|A_y|$ (column 2 replaced by $d$):
$$\begin{aligned} |A_y| &= \begin{vmatrix} 1 & 0 & -1 \\ 2 & 1 & 1 \\ 2 & 7 & 2 \end{vmatrix} \\ &= 1 \cdot \begin{vmatrix} 1 & 1 \\ 7 & 2 \end{vmatrix} - 0 \cdot \begin{vmatrix} 2 & 1 \\ 2 & 2 \end{vmatrix} + (-1) \cdot \begin{vmatrix} 2 & 1 \\ 2 & 7 \end{vmatrix} \\ &= 1(2 - 7) - 0 - 1(14 - 2) \\ &= -5 - 12 = -17 \end{aligned}$$

**Step 4:** $|A_z|$ (column 3 replaced by $d$):
$$\begin{aligned} |A_z| &= \begin{vmatrix} 1 & 1 & 0 \\ 2 & -3 & 1 \\ 2 & 1 & 7 \end{vmatrix} \\ &= 1 \cdot \begin{vmatrix} -3 & 1 \\ 1 & 7 \end{vmatrix} - 1 \cdot \begin{vmatrix} 2 & 1 \\ 2 & 7 \end{vmatrix} + 0 \cdot \begin{vmatrix} 2 & -3 \\ 2 & 1 \end{vmatrix} \\ &= 1(-21 - 1) - 1(14 - 2) + 0 \\ &= -22 - 12 = -34 \end{aligned}$$

**Step 5:** Final answers:
$$x = \frac{-17}{-17} = 1, \quad y = \frac{-17}{-17} = 1, \quad z = \frac{-34}{-17} = 2$$

> **Check all 3 equations:**
> - $1 + 1 - 2 = 0$ ✓
> - $2(1) - 3(1) + 2 = 1$ ✓
> - $2(1) + 1 + 2(2) = 7$ ✓

---

## Cramer's Rule for $n \times n$ Systems (General Case)

For a system of $n$ equations in $n$ unknowns:

$$\begin{aligned} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n &= b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n &= b_2 \\ &\ \vdots \\ a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n &= b_n \end{aligned}$$

Each variable $x_i$ is given by:

$$x_i = \frac{|A_i|}{|A|} \quad \text{for } i = 1, 2, \ldots, n$$

where $A_i$ is the $n \times n$ matrix formed by replacing column $i$ of $A$ with the constants column $B = (b_1, b_2, \ldots, b_n)^T$.

---

## Procedure Summary

1. **Write the system in matrix form:** $AX = B$
2. **Compute $|A|$** — if $|A| = 0$, stop (Cramer's Rule cannot be used; the system has either no solution or infinitely many)
3. **For each variable $x_i$:** form $A_i$ by replacing column $i$ of $A$ with $B$, compute $|A_i|$
4. **Read off the solution:** $x_i = |A_i| / |A|$

---

## Solvability and Solution Types

| Condition | Result | Interpretation |
|-----------|--------|----------------|
| $|A| \neq 0$ | Unique solution via Cramer's Rule | System is **consistent and independent** |
| $|A| = 0$ and $(\text{adj } A)B = 0$ | Infinitely many solutions | System is **consistent and dependent** |
| $|A| = 0$ and $(\text{adj } A)B \neq 0$ | No solution | System is **inconsistent** |

> **Important:** Cramer's Rule only applies to **square systems** ($n$ equations, $n$ unknowns) with $|A| \neq 0$.

---

## Word Problem (3×3 Application)

> Aishah bought a marker pen, two examination pads and a file for RM36. Balqis bought three marker pens, two examination pads and a file for RM43. Camelia bought three marker pens, an examination pad and four files for RM74.

**Step 1 — Define variables:** Let $x =$ price of marker pen, $y =$ price of exam pad, $z =$ price of file.

**Step 2 — Write equations:**
$$\begin{aligned} x + 2y + z &= 36 \\ 3x + 2y + z &= 43 \\ 3x + y + 4z &= 74 \end{aligned}$$

**Step 3 — Matrix form:**
$$\begin{pmatrix} 1 & 2 & 1 \\ 3 & 2 & 1 \\ 3 & 1 & 4 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 36 \\ 43 \\ 74 \end{pmatrix}$$

**Step 4 — Compute $|A|$:**
$$\begin{aligned} |A| &= 1(2 \cdot 4 - 1 \cdot 1) - 2(3 \cdot 4 - 1 \cdot 3) + 1(3 \cdot 1 - 2 \cdot 3) \\ &= 1(8 - 1) - 2(12 - 3) + 1(3 - 6) \\ &= 7 - 18 - 3 = -14 \end{aligned}$$

$|A| \neq 0$, so a unique solution exists.

**Step 5 — Compute $|A_x|, |A_y|, |A_z|$:**
$$\begin{aligned} |A_x| &= \begin{vmatrix} 36 & 2 & 1 \\ 43 & 2 & 1 \\ 74 & 1 & 4 \end{vmatrix} = 36(8-1) - 2(172-74) + 1(43-148) \\ &= 36(7) - 2(98) + 1(-105) = 252 - 196 - 105 = -49 \\[4pt] |A_y| &= \begin{vmatrix} 1 & 36 & 1 \\ 3 & 43 & 1 \\ 3 & 74 & 4 \end{vmatrix} = 1(172-74) - 36(12-3) + 1(222-129) \\ &= 98 - 36(9) + 93 = 98 - 324 + 93 = -133 \\[4pt] |A_z| &= \begin{vmatrix} 1 & 2 & 36 \\ 3 & 2 & 43 \\ 3 & 1 & 74 \end{vmatrix} = 1(148-43) - 2(222-129) + 36(3-6) \\ &= 105 - 2(93) + 36(-3) = 105 - 186 - 108 = -189 \end{aligned}$$

**Step 6 — Solutions:**
$$x = \frac{-49}{-14} = 3.5, \quad y = \frac{-133}{-14} = 9.5, \quad z = \frac{-189}{-14} = 13.5$$

**Answer:** Marker pen = RM 3.50, Exam pad = RM 9.50, File = RM 13.50.

---

## Comparison with Other Methods

| Method | Used When | Advantages | Disadvantages |
|--------|-----------|------------|---------------|
| **Cramer's Rule** | $|A| \neq 0$, small $n$ | Direct formula, shows structure | Computationally expensive for large $n$ |
| **Inverse Matrix** | $|A| \neq 0$ | Elegant one-step $X = A^{-1}B$ | Need to compute inverse first |
| **Gauss-Jordan Elimination** | Any size | Efficient, handles all solution types | More steps, row operations |

For **$n \le 3$**, Cramer's Rule is competitive with other methods. For **$n > 3$**, Gaussian elimination is preferred because computing determinants becomes expensive: an $n \times n$ determinant requires $\sim n!$ operations if computed naively (though cofactor expansion reduces this).

---

## Computational Note

The number of operations to compute an $n \times n$ determinant by cofactor expansion is $O(n!)$. For Cramer's Rule, you need $n+1$ such determinants, making the total $O((n+1)!)$ ≈ $O(n!)$ — impractical for large $n$.

In practice:
- $n = 2$: very fast (2 multiplications, 1 subtraction per determinant)
- $n = 3$: manageable (~9 terms per determinant)
- $n \ge 4$: use Gaussian elimination or inverse matrix method instead

---

## Key Formulas to Memorize

**2×2 Determinant:**
$$\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

**3×3 Determinant (diagonal expansion for checking):**
$$|A| = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}$$

**3×3 Cofactor Sign Pattern:**
$$\begin{pmatrix} + & - & + \\ - & + & - \\ + & - & + \end{pmatrix}$$

---

## Related Sources

- [[FAD1015 L29-L30 — Matrices (Inverse & Systems of Equations)]] — lecture covering Cramer's Rule
- [[FAD1015 Tutorial 13 — Matrices]] — practice problems

## Related Concepts

- [[Matrices]] — matrix algebra fundamentals
- [[Systems of Linear Equations]] — $AX = B$ formulation and solution types
- [[Determinant]] — |A| computation and properties
- [[Gauss-Jordan Elimination]] — alternative row-reduction method
- [[Matrix Inverse]] — $A^{-1}$ method for solving systems
- [[Adjoint Matrix]] — $\text{adj}(A) = C^T$, used in deriving Cramer's Rule

## Related Courses

- [[FAD1015 - Mathematics III]]
- [[FAC1001 - Advanced Mathematics II]]
