---
title: "FAD1015 L25-L26 — Hypothesis Testing in R"
date: 2026-04-29
tags:
  - source/lecture
  - course/FAD1015
  - topic/hypothesis-testing
  - topic/r-programming
  - status/evergreen
week: 14
---

# FAD1015 L25-L26 — Hypothesis Testing in R

Lectures 25–26 covering practical implementation of hypothesis testing using R statistical software. Source file: `L25-26 Hypothesis Testing in R - Student.pdf`

## Summary

Hands-on application of hypothesis testing procedures in R: one-sample Z-tests, one-sample t-tests, interpreting output, normality checks, and practical examples.

---

## Overview of Hypothesis Testing Procedure

Statisticians use hypothesis testing to formally check whether a hypothesis is accepted or rejected. The four steps are:

1. **State the Hypotheses** — State the null and alternative hypotheses.
2. **Formulate an Analysis Plan** — Crucial step in deciding the test procedure.
3. **Analyze Sample Data** — Calculation and interpretation of the test statistic.
4. **Interpret Results** — Apply the decision rule described in the analysis plan.

---

## Getting Data into R

### 1. Import a File
- Go to **File >> Import Dataset >> From Text (Base)** in RStudio.

### 2. Manual Data Entry
Use the combine function `c()` to create a numeric vector:

```r
heights <- c(165, 168, 172, 170, 169, 171, 174,
             168, 166, 170, 175, 172, 169, 167, 170)
```

- `heights` is a **variable** (must use `<-` assignment operator).
- `c()` stands for **combine** or **concatenate**; it creates vectors in R.
- A **vector** is a basic data structure that stores multiple values of the same type.

---

## One-Sample Z-Test in R

### When to Apply

| Condition | Explanation |
|-----------|-------------|
| **Population σ known** | Compare a sample mean to a population mean or compare means of two independent samples. |
| **Large sample size** | $n > 30$ is considered large. By the Central Limit Theorem, the sampling distribution of $\bar{x}$ becomes approximately normal, making the Z-test more appropriate. |

### Steps

1. **Define Your Data**
2. **Set Up Hypotheses**
3. **Perform the One-Sample Z-test**
4. **Interpret the Result**

### Syntax

```r
z.test(x, mu = 0, sigma.x = NULL)
```

- **x**: values for the sample / data
- **mu**: mean under the null (or mean difference in two-sample case)
- **sigma.x**: population standard deviation

> **Note:** Use `z.test()` from the **BSDA** package to perform one-sample and two-sample Z-tests in R.

---

### Example 1 — One-Sample Z-Test (Raw Data)

**Problem:** The IQ in a certain population is normally distributed with $\mu = 100$ and $\sigma = 15$. A scientist recruits 20 patients to test a new medication and records their IQ levels.

**Given data:**
```
88, 92, 94, 94, 96, 97, 97, 97, 99, 99,
105, 109, 109, 109, 110, 112, 112, 113, 114, 115
```

**R code:**
```r
library(BSDA)

data <- c(88, 92, 94, 94, 96, 97, 97, 97, 99, 99,
          105, 109, 109, 109, 110, 112, 112, 113, 114, 115)

z.test(data, mu = 100, sigma.x = 15)
```

**Output:**
```
One-sample z-Test

data:  data
z = 0.90933, p-value = 0.3632
alternative hypothesis: true mean is not equal to 100
95 percent confidence interval:
 96.47608 109.62392
sample estimates:
mean of x
 103.05
```

**Interpretation:** Since the p-value (0.3632) is greater than $\alpha = 0.05$, we **fail to reject** $H_0$. There is insufficient evidence that the medication affects IQ levels.

---

### Example 2 — One-Sample Z-Test (Summary Statistics)

**Problem:** A university claims the average GPA of its students is **3.2**. A researcher suspects it might be different. A random sample of **40 students** has a mean GPA of **3.05** with a known population standard deviation of **0.5**. Test at $\alpha = 0.05$.

**R code (manual computation):**
```r
sample_mean    <- 3.05   # Sample mean
population_mean <- 3.2   # Hypothesized population mean
population_std <- 0.5    # Population standard deviation (known)
n              <- 40     # Sample size
alpha          <- 0.05   # Significance level

# Compute z-score
z_score <- (sample_mean - population_mean) / (population_std / sqrt(n))

# Compute p-value for two-tailed test
p_value <- 2 * (1 - pnorm(abs(z_score)))

print(z_score)
print(p_value)
```

---

### Exercise 1 — One-Sample Z-Test

The manager of a large factory believes that the average hourly wage of the employees is below **RM 9.78** per hour. A sample of **40 employees** has a mean hourly wage of **RM 9.60**. The variance of all salaries is **RM 2.20**. Assume the variable is normally distributed. At $\alpha = 0.10$, is there enough evidence to support the manager’s claim?

> **Hint:** Use $\sigma = \sqrt{2.20}$ and a left-tailed test.

---

## One-Sample t-Test in R

### Steps

1. **Define Your Data**
2. **Set Up Hypotheses**
   - $H_0$: The sample mean is equal to the known population mean ($\mu$).
   - $H_a$: The sample mean is **not equal to** the known population mean ($\mu$).
3. **Perform the One-Sample T-test** using `t.test()`
4. **Interpret the Result** — contains t-value, degrees of freedom, and p-value.

### Syntax

```r
t.test(x, mu)
```

- **x**: numeric vector of data
- **mu**: true value of the mean (hypothesized value)

---

### Example 3 — One-Sample t-Test (Raw Data)

**Problem:** A botanist wants to know if the mean height of a certain species of plant is equal to **15 inches**. She collects a simple random sample of **12 plants**.

**Given data:**
```
14, 14, 16, 13, 12, 17, 15, 14, 15, 13, 15, 14
```

**R code:**
```r
my_data <- c(14, 14, 16, 13, 12, 17, 15, 14, 15, 13, 15, 14)

t.test(my_data, mu = 15)
```

**Output:**
```
One Sample t-test

data:  my_data
t = -1.6848, df = 11, p-value = 0.1201
alternative hypothesis: true mean is not equal to 15
95 percent confidence interval:
 13.46244 15.20423
sample estimates:
mean of x
 14.33333
```

**Interpretation of output:**

| Field | Meaning |
|-------|---------|
| **data** | Name of the vector used (`my_data`). |
| **t** | The t test-statistic, calculated as $\displaystyle \frac{\bar{x} - \mu}{s/\sqrt{n}}$. |
| **df** | Degrees of freedom, calculated as $n - 1$. |
| **p-value** | The two-tailed p-value corresponding to the t-statistic and df. Here, $p = 0.1201$. |
| **95% CI** | The 95% confidence interval for the true population mean: $[13.46244,\; 15.20423]$. |

**Hypotheses:**
- $H_0: \mu = 15$
- $H_A: \mu \neq 15$

**Conclusion:** Since $p = 0.1201 > 0.05$, we **fail to reject** $H_0$. There is insufficient evidence that the mean height differs from 15 inches.

---

### Changing the Alternative Hypothesis in R

You can change the `alternative` argument to specify the type of test:

| Test type | Syntax |
|-----------|--------|
| Two-tailed (default) | `t.test(x, mu)` |
| Left-tailed | `t.test(x, mu, alternative = "less")` |
| Right-tailed | `t.test(x, mu, alternative = "greater")` |

---

### Exercise 2 — One-Sample t-Test

You are conducting research on the heights of individuals. You want to determine if the sample mean height you’ve collected from **15 individuals** significantly differs from the known population mean height of **170 cm**.

**Sample heights:**
```
165, 172, 168, 174, 169, 171, 175, 167, 170,
173, 166, 168, 172, 169, 171
```

Write the code in R.

---

### Example 4 — One-Sample t-Test (Summary Statistics)

**Problem:** The mean height of all female college basketball players is **69.5 inches**. A random sample of **25** such players produced a mean height of **70.2 inches** with a **variance of 4.41 inches**. Assuming normality, test at the **1% significance level** if their mean height is different from 69.5 inches.

**R code (manual computation):**
```r
mu_0  <- 69.5        # Claimed population mean
x_bar <- 70.2        # Sample mean
s     <- sqrt(4.41)  # Sample standard deviation
n     <- 25          # Sample size
df    <- n - 1       # Degrees of freedom

# Compute t-score
t_score <- (x_bar - mu_0) / (s / sqrt(n))

# Compute p-value (two-tailed test)
p_value <- 2 * (1 - pt(abs(t_score), df))

print(t_score)
print(p_value)
```

### Understanding `pt(x, df)`

- `pt()` gives the area under the t-distribution to the **left** of value `x` for a given `df`.
- Example: `pt(-1.83, 12)` gives the area to the left of $-1.83$ with 12 degrees of freedom.
- `abs(t_score)` takes the absolute value (two-tailed test considers both signs).
- `pt(abs(t_score), df)` computes the left-tailed probability.
- `1 - pt(...)` gives the right-tailed probability.
- Multiply by **2** because it is a two-tailed test.

---

## Test for Normality in R

Normality testing is important in statistics since it ensures the validity of various analytical procedures. Understanding whether data follows a normal distribution is critical for drawing appropriate conclusions.

### Types of Normality Tests in R

1. **Shapiro-Wilk test**
2. **Kolmogorov-Smirnov test**
3. **Anderson-Darling test**

### Shapiro-Wilk Test

Use the built-in function:

```r
shapiro.test(x)
```

- **x**: a numeric vector of data values.
- Produces a test statistic (W) along with a corresponding p-value.
- If the **p-value < 0.05**, there is sufficient evidence to say that the sample does **not** come from a population that is normally distributed.

> **Note:** The sample size must be between **3 and 5,000** to use `shapiro.test()`.

### Example 5 — Shapiro-Wilk Test

```r
set.seed(0)

data <- rnorm(100)   # 100 random values from a normal distribution

shapiro.test(data)
```

The p-value of the test turns out to be **0.6303**. Since this value is greater than 0.05, we can assume the sample data comes from a population that is normally distributed. This result is expected because we generated the data using `rnorm()`, which draws from $N(0, 1)$.

### Another Way to Check Normality

1. **Histogram** — using the `hist()` function. A graphical representation of the distribution of your data; shows how frequently different values occur within bins.
2. **QQ plot** — using the `qqnorm()` function. A graphical representation of how well your data matches a theoretical normal distribution.

---

## Key Concepts

- [[Hypothesis Testing]] — theoretical framework
- [[One-Sample Z-Test]] — when $\sigma$ is known or $n > 30$
- [[One-Sample t-Test]] — when $\sigma$ is unknown
- [[Normality Test]] — Shapiro-Wilk, histograms, QQ plots
- [[R Programming for Statistics]] — data input, vectors, built-in functions

## Related Topics

- [[FAD1015 L23-L24 — Hypothesis Testing About the Mean]] — theoretical foundation
- [[FAD1015 L19 — Input Data & Descriptive Statistics in R]] — prerequisite R skills
- [[FAD1015 Tutorial 12 — Hypothesis Testing in R]] — practice problems

## Related Course Page

- [[FAD1015 - Mathematics III]]
