---
title: "FAD1015 Week 4 — Discrete Random Variables (PDF & CDF)"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1015
  - topic/random-variables
  - topic/pdf
  - topic/cdf
  - status/seedling
week: 4
lectures: [L7, L8]
---

# FAD1015 Week 4 — Discrete Random Variables (PDF & CDF)

Week 4 covers the foundation of discrete random variables, introducing the probability distribution function (pdf) in Lecture 7 and the cumulative distribution function (CDF) in Lecture 8. Source file: `FAD1015 Week 4 discrete pdf cdf.pdf`

---

## Summary

This lecture introduces discrete random variables and two ways to characterise their distributions: the **probability distribution function** $f(x)=P(X=x)$, which gives the probability of each individual outcome, and the **cumulative distribution function** $F(x)=P(X\leq x)$, which gives the probability of all outcomes up to a given value. The lectures emphasise tabular and functional representations, verification of valid pdfs, and conversion between pdf and CDF.

---

## Key Concepts

- [[Probability Distributions]] — Random variable framework
- [[Discrete Random Variable]] — countable outcomes with associated probabilities
- [[Probability Mass Function]] — $f(x)=P(X=x)$ (lecture calls this the *probability distribution function*)
- [[Cumulative Distribution Function]] — $F(x)=P(X\leq x)$

---

## L7: Probability Distribution Function

### 1. Random Variable

A **variable** is a quantity which may take more than one value.

A **discrete random variable** is a variable which can take individual values each with a given probability. The values are usually the outcome of an experiment.

**Examples:**

| Experiment | Possible values |
|---|---|
| Score on a fair die | $1,2,3,4,5,6$ |
| Number of heads in 3 coin tosses | $0,1,2,3$ |
| Profit (RM) in a game with entry fee RM 10 and prizes RM 50, RM 100 | $-10, 40, 90$ |
| Number of tosses of a coin until a tail occurs | $1,2,3,\dots$ |

### 2. Notation

- Random variables are denoted by **upper-case** letters: $X, Y, R, \dots$
- Particular values are denoted by **lower-case** letters: $x, y, r, \dots$
- The probability that $X$ takes a particular value $x$ is written $P(X=x)$
- For a fair die: $P(X=4)=\dfrac{1}{6}$
- If the values are $x_1, x_2, \dots, x_n$, the probabilities can be summarised as $p_i$ where $i=1,2,\dots,n$:
  $$p_1=P(X=x_1),\quad p_2=P(X=x_2),\quad \dots$$

### 3. Probability Distribution

A **probability distribution** is a list of all possible values of the discrete random variable $X$, together with their associated probabilities. It can be presented as a **table** or a **function**.

**Tabular form (fair die):**

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $P(X=x)$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ | $\dfrac{1}{6}$ |

**Functional form:**
$$P(X=x)=f(x)=\begin{cases}\dfrac{1}{6}, & x=1,2,3,4,5,6 \\[6pt] 0, & \text{otherwise}\end{cases}$$

Here $f(x)$ is called the **probability distribution function** (pdf).

### 4. Properties of a Probability Distribution Function

For $f(x)$ to be a valid pdf, it must satisfy:

1. **Boundedness:** $0\leq P(X=x)\leq 1$ for every value of $x$
2. **Total probability:** $\displaystyle\sum_{\text{all }x} P(X=x)=1$

### 5. Examples

#### Example 1 — Validating a pdf
Determine whether each function is a probability distribution function.

**(a)** $f(x)=\dfrac{x^2}{55},\quad x=1,2,3,4,5$

**(b)** $f(x)=\dfrac{x}{5},\quad x=-1,0,1,2,3$

**(c)** $f(x)=\dfrac{2x-3}{10},\quad x=2,4,6$

*Approach:* Check non-negativity for every $x$ and verify that the probabilities sum to 1.

---

#### Example 2 — Computing probabilities from a pdf
The random variable $X$ has pdf $P(X=x)=\dfrac{x^2}{14}$ for $x=0,1,2,3$.

Construct the probability distribution table and find:
- **(a)** $P(X=2)$
- **(b)** $P(X>1)$
- **(c)** $P(X\leq 2)$

**Distribution table:**

| $x$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| $P(X=x)$ | $0$ | $\dfrac{1}{14}$ | $\dfrac{4}{14}$ | $\dfrac{9}{14}$ |

*Check:* $0+\dfrac{1}{14}+\dfrac{4}{14}+\dfrac{9}{14}=\dfrac{14}{14}=1$.

---

#### Example 3 — Finding a missing constant
Aleeya plays with a biased five-sided spinner marked $1,2,3,4,5$. The pdf of her score $X$ is:

| $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $P(X=x)$ | $0.15$ | $0.24$ | $k$ | $0.25$ | $0.19$ |

Find:
- **(a)** $k$
- **(b)** $P(X\geq 4)$
- **(c)** $P(X<5)$
- **(d)** $P(2<X\leq 4)$

*Solution for (a):* $0.15+0.24+k+0.25+0.19=1\implies k=0.17$.

---

#### Example 4 — Hypergeometric-type setting
A basket contains 12 peppers: 3 red, 4 green, 5 yellow. Three peppers are taken at random **without replacement**.

- **(a)** Find the probability that the three peppers are all different colours.
- **(b)** Show that the probability exactly 2 peppers are green is $\dfrac{12}{55}$.
- **(c)** Let $X$ be the number of green peppers taken. Draw up the probability distribution table for $X$.

*Values of $X$:* $0,1,2,3$.

---

#### Example 5 — Piecewise pdf with unknown constant
The pdf of $X$ is
$$f(x)=\begin{cases}kx^2, & x=0,1,2,3 \\ k, & x=4,5\end{cases}$$

Find:
- **(a)** the value of $k$
- **(b)** $P(0<X\leq 3)$
- **(c)** $P(|X-2|<1)$
- **(d)** $P(X\text{ is even})$

*Approach for (a):* Sum all probabilities and set equal to 1:
$$k(0^2+1^2+2^2+3^2)+k+k = k(0+1+4+9)+2k = 15k+2k = 17k = 1 \implies k=\frac{1}{17}$$

---

## L8: Cumulative Distribution Function

### 1. Definition

For a discrete random variable $X$ with pdf $P(X=x)$ where $x=x_1,x_2,\dots,x_n$, the **cumulative distribution function** $F(t)$ is defined as

$$F(t)=P(X\leq t)=\sum_{x_1}^{t} P(X=x)$$

**Fair die example:**

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $F(x)$ | $\dfrac{1}{6}$ | $\dfrac{2}{6}$ | $\dfrac{3}{6}$ | $\dfrac{4}{6}$ | $\dfrac{5}{6}$ | $1$ |

Written as a piecewise function:
$$F(x)=\begin{cases}0, & x<1 \\ \dfrac{1}{6}, & 1\leq x<2 \\ \dfrac{2}{6}, & 2\leq x<3 \\ \dfrac{3}{6}, & 3\leq x<4 \\ \dfrac{4}{6}, & 4\leq x<5 \\ \dfrac{5}{6}, & 5\leq x<6 \\ 1, & x\geq 6\end{cases}$$

### 2. Key Relationships

For any discrete random variable with CDF $F$:

$$P(a<X\leq b)=P(X\leq b)-P(X\leq a)=F(b)-F(a)$$

$$P(X=b)=F(b)-F(a)$$

*(Lecture notation: the second formula uses $a$ to denote the value immediately preceding $b$ in the support of $X$.)*

### 3. Examples

#### Example 6 — CDF from a table (spinner revisited)
Using the spinner from Example 3 with $k=0.17$:

| $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $P(X=x)$ | $0.15$ | $0.24$ | $0.17$ | $0.25$ | $0.19$ |

- **(b)** Find the cumulative distribution of $X$.
- **(c)** Find:
  - **i.** $P(X<3)$
  - **ii.** $P(2<X\leq 5)$
  - **iii.** $P(2\leq X<5)$

---

#### Example 7 — Recovering the pdf from the CDF
$X$ takes values $0,1,2,3$ with CDF:
$$F(x)=\begin{cases}0, & x<0 \\ 0.2, & 0\leq x<1 \\ 0.6, & 1\leq x<2 \\ 0.9, & 2\leq x<3 \\ 1, & x\geq 3\end{cases}$$

- **(a)** Find:
  - **i.** $P(X\leq 1)$
  - **ii.** $P(X>1)$
  - **iii.** $P(X=1)$
  - **iv.** $P(0<X\leq 2)$
  - **v.** $P(1<X<3)$
- **(b)** Find the pdf $f(x)$.

*Key idea:* $P(X=x_i)=F(x_i)-F(x_{i-1})$.

---

#### Example 8 — Car sales
A car dealer records the number of cars sold per day. The relative frequencies give:

| Number of cars, $x$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| $P(X=x)$ | $0.1$ | $0.1$ | $0.2$ | $0.3$ | $0.2$ | $0.1$ |

- **(a)** Find the probability that 2 cars or less will be sold the next day.
- **(b)** Find the cumulative distribution function.

---

#### Example 9 — Peppers (full pdf and CDF)
Same setting as Example 4 (12 peppers: 3 red, 4 green, 5 yellow; 3 drawn without replacement).

- **(a)** Let $X$ be the number of green peppers taken. Draw up the probability distribution table for $X$.
- **(b)** Find the cumulative frequency distribution of green peppers taken.

---

## Related Topics

- [[FAD1015 Week 3 — Independent Events & Bayes' Theorem]] — prerequisite probability
- [[FAD1015 Week 5 — Mean & Variance (Discrete & Continuous)]] — extends to moments
- [[FAD1015 Tutorial 1-6 — Counting & Probability Fundamentals]] — practice problems

## Related Course Page

- [[FAD1015 - Mathematics III]]
