---
title: "FAD1015 L29-L30 — Matrices (Inverse & Systems of Equations)"
date: 2026-04-29
tags:
  - source/lecture
  - course/FAD1015
  - topic/matrices
  - status/seedling
week: 17
---

# FAD1015 L29-L30 — Matrices (Inverse & Systems of Equations)

Lectures 29–30 covering matrix inverses, determinants, and solving systems of linear equations using matrix methods. Source file: `(L29L30) - WEEK 17_MATRICES.pdf` (35 slides)

## Summary

This lecture covers inverse matrices (definition, 2×2 formula, adjoint method, elementary row operations) and three methods for solving systems of linear equations with three variables: inverse matrix method, Gauss-Jordan elimination, and Cramer's Rule.

---

## L29: Inverse Matrices

### 1. Definition of Inverse Matrices

Let $A$ be any square matrix of order $n \times n$. If there exists a matrix $B$ such that:

$$AB = BA = I$$

Then $B$ is called the **inverse** of $A$ and vice-versa. The inverse of $A$ is denoted by $A^{-1}$.

Also:

$$A \cdot A^{-1} = A^{-1} \cdot A = I$$

**Example 1:** If $A = \begin{pmatrix} 2 & 5 \\ 1 & 3 \end{pmatrix}$, $B = \begin{pmatrix} 3 & -5 \\ -1 & 2 \end{pmatrix}$, show that $A$ is the inverse matrix of $B$.

*(Solution: verify $AB = BA = I$)*

---

### 2. Inverse of a 2 × 2 Matrix

Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ and $B = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$

Then $BA = (ad - bc)\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$

Hence, if $ad - bc \neq 0$:

$$A^{-1} = \frac{1}{|A|} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} \quad \text{where } |A| = ad - bc$$

**Singular vs Non-Singular:**
- If $A^{-1}$ exists, $A$ is called a **non-singular matrix**
- When $|A| = 0$, $A^{-1}$ does not exist and $A$ is called a **singular matrix**

**Steps to find inverse of 2×2:**
1. **Interchange** the elements of the leading diagonal
2. **Reverse the sign** of the other elements
3. **Divide** the matrix by the determinant

**Example 2:** Find the inverse of $A = \begin{pmatrix} 3 & 1 \\ 4 & 2 \end{pmatrix}$

**Example 3:** If $A = \begin{pmatrix} 1 & 0 \\ 4 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix}$, find $AB$ and show that $(AB)^{-1} = B^{-1}A^{-1}$

**Example 4:** Given $A = \begin{pmatrix} -2 & 1 & 1 \\ 3 & -2 & 1 \\ -1 & 2 & -1 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 3 & 3 \\ 2 & 3 & 5 \\ 4 & 3 & 1 \end{pmatrix}$. Find $AB$. Hence deduce the inverse of $A$.

---

### 3. Adjoint Matrix

If $A$ is a $n \times n$ matrix and $C_{ij}$ is the cofactor for element $a_{ij}$, then the **cofactor matrix** of $A$ is:

$$C = \begin{bmatrix} C_{11} & C_{12} & \cdots & C_{1n} \\ C_{21} & C_{22} & \cdots & C_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ C_{n1} & C_{n2} & \cdots & C_{nn} \end{bmatrix}$$

The **adjoint** of matrix $A$ is:

$$\text{adj}(A) = C^T$$

**Example 5:** Find adjoint of $A$ if $A = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 3 & 1 \\ 1 & 0 & 2 \end{pmatrix}$

---

### 4. Finding Inverse Using Matrix Adjoint

Given a non-singular square matrix $A$ of any size:

$$A^{-1} = \frac{1}{|A|} \text{adj}(A)$$

**Example 6:** Find the inverse of $A = \begin{pmatrix} 2 & 3 & 0 \\ -5 & 0 & 4 \\ 0 & 2 & 1 \end{pmatrix}$

---

### 5. Elementary Row Operations (ERO)

There are three elementary row operations:

1. **Interchange** any two rows ($R_i \leftrightarrow R_j$)
2. **Multiply** all elements of a row by a scalar ($R_i \rightarrow kR_i$)
3. **Multiply** all elements of a row by a scalar and add to another row ($R_j \rightarrow kR_i + R_j$)

When a matrix $A$ is changed into another matrix $B$ after using ERO, $A$ and $B$ are said to be **equivalent**.

---

### 6. Finding Inverse Using ERO

To find the inverse of matrix $A$, start by writing the matrix in the form $(A|I)$ and change it by ERO into $(I|B)$. The resulting matrix $B$ is $A^{-1}$.

$$(A|I) \text{ reduce to } (I|A^{-1})$$

**5-step process for 3×3:**
- **Step 1:** Obtain a 1 in the first position on the leading diagonal
- **Step 2:** Obtain zeros under the 1 in the first column
- **Step 3:** Obtain a 1 in the second position on the leading diagonal
- **Step 4:** Obtain zeros under the 1 in the second column
- **Step 5:** Obtain a 1 in the third position on the leading diagonal. Finally obtain zeros above all the 1's

**Example 7:** Given $A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$. Find $A^{-1}$ using ERO.

**Example 8:** If $A = \begin{pmatrix} 2 & -1 & 1 \\ 1 & -1 & -1 \\ 2 & -2 & -1 \end{pmatrix}$, find $A^{-1}$ using ERO.

---

## L30: Systems of Linear Equations with Three Variables

### 1. System of Linear Equations in Matrix Notation

The system:
$$\begin{aligned} a_{11}x + a_{12}y + a_{13}z &= b_1 \\ a_{21}x + a_{22}y + a_{23}z &= b_2 \\ a_{31}x + a_{32}y + a_{33}z &= b_3 \end{aligned}$$

Can be represented as $AX = B$:

$$\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}$$

Where $A$ is the **coefficients matrix**, $X$ is the **matrix of variables**, and $B$ is the **constants matrix**.

**Example 9:** The equations $2x - y + 3z = 4$, $x + 2y - z = 1$ and $3x + y - 2z = 2$ can be written as $AX = B$.

---

### 2. Method Using the Inverse Matrix

$$AX = B$$
$$A^{-1}(AX) = A^{-1}B$$
$$(A^{-1}A)X = A^{-1}B$$
$$IX = A^{-1}B$$
$$X = A^{-1}B$$

> **Note:** This method **cannot be used** if $A$ is a singular matrix ($|A| = 0$).

**Example 10:** Solve the system:
$$\begin{aligned} x + 2y + 7z &= 1 \\ x + 3y &= 2 \\ -y + 8z &= 3 \end{aligned}$$

---

### 3. Gauss-Jordan Elimination Method

Steps for solving $AX = B$:

1. Write the system in the form $AX = B$
2. Form an **augmented matrix** $(A|B)$
3. Use ERO to reduce $(A|B)$ to $(I|X)$

**Possible Solutions:**

1. If $|A| \neq 0$: **unique solution** given by $X = A^{-1}B$
2. If $|A| = 0$ and $(\text{adj } A)B = 0$: **infinitely many solutions** (e.g., row reduces to $(0 \quad 0 \quad 0 \;|\; 0)$)
3. If $|A| = 0$ and $(\text{adj } A)B \neq 0$: **no solution** (e.g., row reduces to $(0 \quad 0 \quad 0 \;|\; c)$ where $c$ is a constant)

**Example 11:** Solve by Gauss-Jordan elimination:
$$\begin{aligned} x + z &= 5 \\ 3x + y + 2z &= 11 \\ 3x + 2y + 2z &= 10 \end{aligned}$$

---

### 4. Cramer's Rule

Cramer's Rule uses determinants to solve systems with the same number of equations as variables.

**For 2×2:**
$$x = \frac{\begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}}, \quad y = \frac{\begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}}$$

**For 3×3:**
$$x = \frac{\begin{vmatrix} d_1 & b_1 & c_1 \\ d_2 & b_2 & c_2 \\ d_3 & b_3 & c_3 \end{vmatrix}}{|A|}, \quad y = \frac{\begin{vmatrix} a_1 & d_1 & c_1 \\ a_2 & d_2 & c_2 \\ a_3 & d_3 & c_3 \end{vmatrix}}{|A|}, \quad z = \frac{\begin{vmatrix} a_1 & b_1 & d_1 \\ a_2 & b_2 & d_2 \\ a_3 & b_3 & d_3 \end{vmatrix}}{|A|}$$

**Example 12:** Solve using Cramer's Rule:
$$\begin{aligned} x + y - z &= 0 \\ 2x - 3y + z &= 1 \\ 2x + y + 2z &= 7 \end{aligned}$$

**Example 13 (Word Problem):** Aishah bought a marker pen, two examination pads and a file for RM36. Balqis bought three marker pens, two examination pads and a file for RM43 while Camelia bought three marker pens, an examination pad and four files for RM74. Let $x, y, z$ represent prices. Write the system, express as matrix, and solve using Cramer's Rule.

---

## Key Concepts

- [[Matrices]] — Matrix algebra, types, and operations
- [[Matrix Inverse]] — $A^{-1}$ such that $AA^{-1} = I$
- [[Determinant]] — Scalar value $|A|$ for square matrices
- [[Adjoint Matrix]] — Transpose of cofactor matrix
- [[Elementary Row Operations]] — ERO for matrix reduction
- [[Gauss-Jordan Elimination]] — Solving systems via augmented matrix
- [[Cramer's Rule]] — Determinant-based solution method
- [[Systems of Linear Equations]] — $AX = B$ representation

## Related Topics

- [[FAD1015 L27-L28 — Matrices (Types & Operations)]] — prerequisite basics
- [[FAD1015 Tutorial 1-6 — Counting & Probability Fundamentals]]

## Related Course Page

- [[FAD1015 - Mathematics III]]
