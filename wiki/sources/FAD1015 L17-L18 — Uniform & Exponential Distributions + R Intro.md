---
title: "FAD1015 L17-L18 — Uniform & Exponential Distributions + R Intro"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1015
  - topic/uniform-distribution
  - topic/exponential-distribution
  - topic/r-programming
  - status/seedling
week: 10
---

# FAD1015 L17-L18 — Uniform & Exponential Distributions + R Intro

Lectures 17–18 covering continuous uniform and exponential distributions with an introduction to R programming. Source file: `(L17 L18) FAD1015 w10 24-25.pdf` (49 pages)

## Summary

Lecture 17 introduces two fundamental continuous distributions: the **uniform distribution** (constant probability over an interval) and the **exponential distribution** (waiting times between events in a Poisson process). Key properties — probability density functions, cumulative distribution functions, means, standard deviations, and variances — are developed with worked examples. Lecture 18 provides a first introduction to the **R** statistical computing environment: installation, basic syntax, vectors, simple calculations, standard mathematical functions, summary statistics, and built-in probability functions for the binomial distribution.

## Key Concepts

- [[Probability Distributions]] — Uniform and Exponential
- Uniform Distribution — constant PDF over an interval $[a, b]$
- Exponential Distribution — waiting times, memoryless property
- R Programming — statistical computing environment
- Memoryless Property — $P(X > s+t \mid X > s) = P(X > t)$
- Poisson–Exponential Link — shared rate parameter $\lambda$

## Lecture 17: Uniform & Exponential Distributions

### 1. The Uniform Distribution

**Definition:** A continuous random variable $X$ follows a **uniform distribution** on the interval $[a, b]$, denoted $X \sim U(a, b)$, if every value in the interval is equally likely.

**Probability Density Function (PDF):**
$$f(x) = \begin{cases} \dfrac{1}{b-a} & \text{for } a \leq x \leq b \\[6pt] 0 & \text{otherwise} \end{cases}$$

**Cumulative Distribution Function (CDF):**
$$F(x) = \begin{cases} 0 & \text{for } x < a \\[6pt] \dfrac{x-a}{b-a} & \text{for } a \leq x \leq b \\[6pt] 1 & \text{for } x > b \end{cases}$$

**Mean, Variance, and Standard Deviation:**
- **Mean:** $E[X] = \dfrac{a + b}{2}$
- **Variance:** $\text{Var}(X) = \dfrac{(b - a)^2}{12}$
- **Standard Deviation:** $\sigma = \dfrac{b - a}{\sqrt{12}} = \dfrac{b - a}{2\sqrt{3}}$

**Application — Random Numbers:**
One of the most common uses of the uniform distribution is in the selection of random numbers. When you use simple random sampling, you assume that each random number comes from a uniform distribution that has a minimum value of $0$ and a maximum value of $1$, i.e. $U(0, 1)$.

#### Example 1
(Figure-based problem on uniform distribution over an interval)

#### Example 2
(Figure-based problem on uniform distribution)

#### Example 3
The time between arrivals of customers at a bank during the noon to 2 pm period has a uniform distribution between $0$ to $110$ seconds.

a. What is the probability that the time between the arrival of two customers will be
   i. less than $25$ seconds?
   ii. between $10$ and $40$ seconds?
   iii. more than $55$ seconds?

b. What are the mean and standard deviation of the time between arrivals?

---

### 2. The Exponential Distribution

**Definition:** The **exponential distribution** models the time between events in a Poisson process. If events occur at a constant rate $\lambda$, the waiting time until the next event follows an exponential distribution with parameter $\lambda$.

**Probability Density Function (PDF):**
$$f(x) = \lambda e^{-\lambda x}, \quad x \geq 0$$

**Cumulative Distribution Function (CDF):**
$$F(x) = P(X \leq x) = 1 - e^{-\lambda x}, \quad x \geq 0$$

**Mean and Standard Deviation:**
- **Mean:** $E[X] = \dfrac{1}{\lambda}$
- **Standard Deviation:** $\sigma = \dfrac{1}{\lambda}$
- **Variance:** $\text{Var}(X) = \dfrac{1}{\lambda^2}$

Note: For the exponential distribution, the **mean equals the standard deviation**.

**Memoryless Property:**
$$P(X > s + t \mid X > s) = P(X > t) = e^{-\lambda t}$$

The memoryless property means that the probability of waiting an additional time $t$ is independent of how much time $s$ has already elapsed.

#### Example 4
Suppose that customers arrive at a bank's ATM at a rate of $20$ per hour. If a customer has just arrived, what is the probability that the next customer will arrive
a. within $3$ minutes?
b. within $12$ minutes?

#### Example 5
(Exponential distribution waiting-time problem)

#### Example 6
Cars arrive at a toll plaza located at the entrance to a bridge at a rate of $45$ per minute during the 5:00-to-6:00 pm period. If a car has just arrived, what is the probability that the next car will arrive within $6$ seconds?

a. What is the probability that the next car will arrive within
   i. $1$ second?
   ii. $5$ seconds?

b. What are your answers to (a) if the rate of arrival of cars is
   i. $20$ per minute?
   ii. $40$ per minute?

#### Example 7
A checkout counter at a supermarket completes the process according to an exponential distribution with a service rate of $10$ per hour. A customer arrives at the checkout counter. Find the probability of the following events.
a. The service is completed in fewer than $4$ minutes.
b. The customer leaves the checkout counter more than $11$ minutes after arriving.
c. The service is completed in a time between $4$ and $9$ minutes.

#### Example 8
On average, a pair of running shoes can last $16$ months if used every day. The length of time running shoes last is exponentially distributed. What is the probability that a pair of running shoes last more than $15$ months? On average, how long would $5$ pairs of running shoes last if they are used one after the other? Eighty percent of running shoes last at most how long if used every day?

---

### 3. Relationship Between Poisson and Exponential

| Distribution | Type | Models | Parameter |
|-------------|------|--------|-----------|
| Poisson | Discrete | Number of events in a fixed time interval | $\lambda$ (rate) |
| Exponential | Continuous | Time until the next event | $\lambda$ (rate) |

The Poisson and exponential distributions are two views of the same **Poisson process**:
- **Poisson**: counts how many events occur in a fixed interval
- **Exponential**: measures how long you wait between consecutive events

Both share the same rate parameter $\lambda$.

## Lecture 18: Introduction to R

### 1. Why R?

R is a powerful open-source statistical computing environment widely used in academia and industry for data analysis, statistical modelling, and graphical visualisation.

### 2. Installation

**Windows:**
- Download the binary file from: https://cran.r-project.org/bin/windows/base/
- Run the downloaded installer.

**Mac:**
- Download the binary file from: https://cran.r-project.org/bin/macosx/
- Run the downloaded installer.

Or simply search "Download R" in a web browser.

### 3. R and RStudio

- **R** is the name of the programming language itself.
- **RStudio** is a convenient integrated development environment (IDE) for R.

To install RStudio, search "Download RStudio" or visit: https://www.rstudio.com/products/rstudio/download/

R can be used without RStudio (via the basic GUI or command line), but RStudio provides a much more user-friendly interface.

### 4. Assignment and Basics

Assignment to an object name may be done using:
1. An equals sign `=`, or
2. A "left arrow" `<-` (less than, hyphen)

You can type the name of any object to look at that object. Variables must start with a letter, but may also contain numbers and periods. **R is case sensitive.**

```r
> n <- 15
> n
[1] 15

> a = 12
> a
[1] 12

> N = 26.42
> N
[1] 26.42

> n
[1] 15
```

To see a list of your objects, look at the workspace. Use `rm()` to delete objects you no longer need. Anything after a hash sign `#` is a comment and has no effect on execution.

### 5. Simple Calculations

R uses standard arithmetic symbols `+`, `-`, `*`, `/`, as well as parentheses and `^` (exponentiation).

```r
> a <- 12 + 14
> a
[1] 26

> 3 * 5
[1] 15

> (20 - 4) / 2
[1] 8

> 7^2
[1] 49
```

### 6. Standard Mathematical Functions

```r
> exp(2)
[1] 7.389056

> log(10)        # Natural log
[1] 2.302585

> log10(10)      # Base 10
[1] 1

> log2(64)       # Base 2
[1] 6

> pi
[1] 3.141593

> cos(pi)
[1] -1

> sqrt(100)
[1] 10

> set.seed(13)   # Specify generator seed
> rnorm(n = 3)
```

### 7. Vectors

Vectors may be created using the `c()` command (**c** stands for concatenate), separating elements with commas.

```r
> a <- c(1, 7, 32, 16)
> a
[1]  1  7 32 16
```

Sequences of integers may be created using a colon `:`.

```r
> b <- 1:10
> b
[1]  1  2  3  4  5  6  7  8  9 10

> c <- 20:15
> c
[1] 20 19 18 17 16 15
```

Other regular vectors may be created using `seq()` (sequence) and `rep()` (repeat).

```r
> d <- seq(1, 5, by = 0.5)
> d
[1] 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0

> e <- seq(0, 10, length = 5)
> e
[1]  0.0  2.5  5.0  7.5 10.0

> f <- rep(0, 5)
> f
[1] 0 0 0 0 0

> g <- rep(1:3, 4)
> g
[1] 1 2 3 1 2 3 1 2 3 1 2 3
```

If a vector is passed to an arithmetic calculation, it is computed **element-by-element**.

```r
> c(1, 2, 3) + c(4, 5, 6)
[1] 5 7 9

> sqrt(c(100, 225, 400))
[1] 10 15 20
```

**Subsetting vectors** with square brackets `[ ]`:

```r
> d[3]
[1] 2

> d[5:7]
[1] 3.0 3.5 4.0

> d[d > 2.8]
[1] 3.0 3.5 4.0 4.5 5.0
```

The number of elements in a vector is found with `length()`.

```r
> length(d)
[1] 9

> length(d[d > 2.8])
[1] 5
```

To remove elements, use negative indices:

```r
> d[-(1:3)]    # d without its first three elements
```

**Random vectors** can be created with functions that start with `r`, such as `rnorm()` (normal) or `runif()` (uniform).

```r
> x <- rnorm(5)           # Standard normal random variables
> y <- rnorm(7, 10, 3)    # Normal r.v. with mu = 10, sigma = 3
> z <- runif(10)          # Uniform(0, 1) random variables
```

#### Example 1 (R)
(Vector creation and manipulation example)

#### Example 2 (R)
Create the following vectors in R.
- $a = (5, 10, 15, 20, \dots, 160)$
- $b = (87, 86, 85, \dots, 56)$

Use vector arithmetic to multiply these vectors and call the result $D$. Select subsets of $D$ to identify the following:
a. What are the 19th, 20th, and 21st elements of $D$?
b. What are all of the elements of $D$ which are less than $2000$?
c. How many elements of $D$ are greater than $6000$?

### 8. Simple Statistics

A variety of mathematical and statistical summaries can be computed from a vector.

```r
> Y <- rnorm(10)
> mean(Y)
[1] -0.3191486

> sort(Y)
[1] -1.1783715 -1.1337012 -0.9507774 -0.9095197 -0.8321391 -0.7406619
[7]  0.2993040  0.4288495  0.7052832  1.1202479

> median(Y)
[1] -0.7864005

> var(Y)
[1] 0.739266

> sd(Y)
[1] 0.8598058
```

#### Example 3 (R)
Using $D$ from Example 2, use R to compute the following statistics of $D$:
a. sum
b. median
c. standard deviation
d. Try using the function `summary()`. What will you get? Explain.

### 9. Arrangements, Permutations, and Combinations

(Slide content covering formulas for counting arrangements, permutations of $r$ distinct objects, and combinations.)

### 10. Binomial Distribution Functions in R

R has built-in functions for the binomial distribution. They are described below.

**`pbinom(x, size, prob)`** — Cumulative probability:
```r
# Probability of getting 26 or less heads from 51 tosses of a coin
> x <- pbinom(26, 51, 0.5)
> x
[1] 0.610116
```

**`qbinom(p, size, prob)`** — Quantile function:
```r
# How many heads will have a probability of 0.25 when a coin is tossed 51 times
> x <- qbinom(0.25, 51, 1/2)
> x
[1] 23
```

**`rbinom(n, size, prob)`** — Random generation:
```r
# Find 8 random values from a sample of 150 with probability of 0.4
> x <- rbinom(8, 150, 0.4)
> x
[1] 56 60 59 61 51 61 65 48
```

#### Example 4 (R)
Using R, evaluate the following (Example from Week 6):

Ten percent of all iPhones manufactured by APPLE are defective. A quality control inspector randomly selects five iPhones from the production line. Is this experiment a binomial experiment? What is the probability that
a. exactly three of these iPhones are defective?
b. more than one of these iPhones is defective?
c. less than two of these iPhones are defective?
d. at least two of these iPhones are defective?
e. at most two of these iPhones are defective?

## Related Topics

- [[FAD1015 L14 — Poisson Distribution]] — related to exponential via Poisson process
- [[FAD1015 Tutorial 8 — Uniform & Exponential Distributions]] — practice problems
- [[FAD1015 L19 — Input Data & Descriptive Statistics in R]] — continues R programming
- [[Probability Distributions]]

## Related Course Page

- [[FAD1015 - Mathematics III]]
