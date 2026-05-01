---
title: "FAD1015 Tutorial 12 — Hypothesis Testing in R"
date: 2024-2025
course: FAD1015 Mathematics III
tags:
  - fad1015
  - mathematics
  - hypothesis-testing
  - r-programming
  - t-test
  - normality-test
  - shapiro-wilk
---

# FAD1015: Mathematics III — Tutorial 12

**Centre for Foundation Studies in Science**  
**Universiti Malaya**  
**Session 2024/2025**

---

## Topic: Hypothesis Testing in R

It is important to remember that the hypothesis testing for sample mean assumes that the X follows a normal distribution. This may be true if X follows a normal distribution or if the sample size is large enough (in practice, n>30, thanks to the [[Central Limit Theorem]]).

---

## Case Study: Octopus Weight Analysis

We examine the weight of adult female octopuses fished off the coast of Mauritania. The data can be found here: http://tinyurl.com/yhyetsuw

We would like to obtain an estimation of the mean of the weight and a confidence interval for this mean with a threshold of 95%.

---

## Steps

### Step 1: Read the data (given as OctopusF.txt)

```r
# Read the octopus data
octopus <- read.table("OctopusF.txt", header = TRUE)
```

### Step 2: Select the female octopus only / remove male octopus

```r
octF <- subset(octopus, Sexe == "F")
```

### Step 3: Find the summary statistics

```r
summary(octF)
```

### Step 4: Assess normality

From the summary statistics, can you tell if the data is normally distributed or not?

### Step 5: Construct a histogram

```r
hist(octF$weight)
```

### Step 6: Check for normality

Do you think this is necessary? Name a few normality tests:
- [[Shapiro-Wilk Test]]
- [[Q-Q Plot]] (Quantile-Quantile plot)

```r
# Q-Q Plot
qqnorm(octF$weight)
qqline(octF$weight)

# Shapiro-Wilk test
shapiro.test(octF$weight)
```

### Step 7: State hypotheses

Assuming normality assumption holds, test if the mean weight for female octopus is equal or greater than 640.

State the null and alternative hypothesis:
- **H₀:** μ = 640 (or μ ≤ 640)
- **H₁:** μ > 640

### Step 8: Read about t.test function

Use `help(t.test)` and read up about the details of the function `t.test`

```r
help(t.test)
```

### Step 9: Perform t-tests

Perform the following t.test (in practice σ is unknown) and observe their output. Discuss the differences of each command.

```r
# Default two-tailed t-test
weightF <- octF$weight
t.test(weightF)

# One-sample t-test with specified mean
t.test(weightF, mu = 640)

# One-tailed test (greater)
t.test(weightF, mu = 640, alternative = "greater")

# One-tailed test (less)
t.test(weightF, mu = 640, alternative = "less")
```

**Discussion Points:**
- What does each variant test?
- How do the p-values differ?
- When would you use each alternative hypothesis?

### Step 10: Draw conclusions

Referring to Step 7, what conclusion can you reach based on the t-test results?

### Step 11: Confidence interval

Find the confidence interval of the sample mean (σ is unknown). Observe the result.

From Step 6, it is shown that the data is not following normal distribution. 

**Questions to consider:**
- Do you think the results from the t-test is valid when normality is violated?
- What is the alternative to t-test when data is not normally distributed?

---

## Additional Notes

### When to use t-test vs alternatives:

| Condition | Test to Use |
|-----------|-------------|
| Normal distribution, σ unknown | One-sample t-test |
| Non-normal, large sample (n > 30) | t-test (CLT applies) |
| Non-normal, small sample | [[Mann-Whitney U Test]] or [[Wilcoxon Signed-Rank Test]] |
| Paired data | Paired t-test |
| Two independent groups | Two-sample t-test |

### R Functions Reference

| Function | Purpose |
|----------|---------|
| `t.test()` | Performs one/two sample t-tests |
| `shapiro.test()` | Shapiro-Wilk normality test |
| `qqnorm()` | Creates Q-Q plot |
| `qqline()` | Adds reference line to Q-Q plot |
| `hist()` | Creates histogram |
| `summary()` | Summary statistics |
| `subset()` | Select subset of data |

---

## Related Concepts

- [[Hypothesis Testing]] — overview of statistical hypothesis testing framework
- [[T-Test]] — statistical test for mean with unknown variance
- [[Null Hypothesis]] — default assumption to be tested
- [[Alternative Hypothesis]] — claim to be tested against null
- [[P-Value]] — probability of test statistic under null
- [[Confidence Interval]] — range of plausible values for parameter
- [[Shapiro-Wilk Test]] — test for normality
- [[Q-Q Plot]] — graphical check for normality
- [[Central Limit Theorem]] — basis for large-sample inference
- [[Non-Parametric Tests]] — tests without normality assumption
- [[Probability Distributions]] — t-distribution and normality

## Related Lectures

- [[FAD1015 L25-L26 — Hypothesis Testing in R]]
- [[FAD1015 L23-L24 — Hypothesis Testing About the Mean]] — theoretical foundation
- [[FAD1015 L19 — Input Data & Descriptive Statistics in R]] — R basics

## Related Course Page

- [[FAD1015 - Mathematics III]]

---

*Source: FAD1015 25-26 Tutorial 12 Questions.pdf*
