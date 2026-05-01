---
title: "FAD1015 L20 — Sampling Method & Sampling Distribution of the Mean"
date: 2026-04-29
tags:
  - source/lecture
  - course/FAD1015
  - topic/sampling
  - topic/sampling-distribution
  - status/seedling
week: 11
lecturer:
references:
  - "Levine DM, Stephan DF, Krehbiel TC, Berenson ML (2011). Statistics for Managers, 6th Ed, Pearson Education Limited, Essex, England."
---

# FAD1015 L20 — Sampling Method & Sampling Distribution of the Mean

Lecture 20 (Week 11_2) covering two major topics: (1) types of sampling methods, and (2) sampling distribution of the mean with the Central Limit Theorem. Source file: `(L20) FAD1015 week 11 sampling distribution.pdf`

---

## Part 1: Types of Sampling Method

### 1.1 Introduction

In previous topics, samples were assumed to be randomly and independently chosen. In practice, we take samples because we cannot afford to study every item in a population. Statistical sampling procedures focus on collecting a small, representative group from a larger population.

**Reasons for selecting a sample:**
- Less time consuming
- Less costly
- Less cumbersome and more practical

### 1.2 Types of Samples

Samples are broadly classified into two categories:

**Nonprobability Samples** — items selected without known probabilities of selection. Statistical inference developed for probability sampling (e.g., t-tests) cannot be applied.

**Probability Samples** — items selected based on known probabilities. This allows you to make inferences about the population of interest.

```
Types of Samples Used
├── Nonprobability Samples
│   ├── Judgment Sample
│   └── Convenience Sample
│   └── Quota Sample
│   └── Snowball / Purposive Sample
└── Probability Samples
    ├── Simple Random Sample (SRS)
    ├── Systematic Sample
    ├── Stratified Sample
    └── Cluster Sample
```

#### Probability Sampling Methods

| Method | Description |
|--------|-------------|
| **Simple Random Sampling (SRS)** | Every member of the population has an equal chance of being selected |
| **Systematic Sampling** | Select every $k$-th member from a list or sequence |
| **Stratified Sampling** | Population divided into subgroups (strata); samples taken from each stratum |
| **Cluster Sampling** | Population divided into clusters; entire clusters are randomly selected |

#### Nonprobability Sampling Methods

| Method | Description |
|--------|-------------|
| **Convenience Sampling** | Select items that are easily accessible |
| **Purposive / Judgment Sampling** | Select items that meet specific research criteria (researcher's judgment) |
| **Quota Sampling** | Select samples to match predetermined quotas for certain characteristics |
| **Snowball Sampling** | Existing study subjects recruit future subjects (useful for rare populations) |

#### Probability vs Nonprobability Sampling

| Aspect | Probability Sampling | Non-Probability Sampling |
|--------|---------------------|--------------------------|
| Selection basis | Known probabilities | Unknown probabilities |
| Representativeness | Sample probability known | No probability of selecting any individual |
| Research purpose | Fundamental research; generalization | Action research; no generalization |
| Population reference | Refers from sample and population | No idea of population |

### 1.3 Strengths and Weaknesses of Sampling Methods

| Technique | Strengths | Weaknesses |
|-----------|-----------|------------|
| **Convenience** | Least expensive, least time-consuming, most convenient | Selection bias, sample not representative, not recommended for descriptive or causal research |
| **Judgment** | Low-cost, convenient, ideal for exploratory research | Does not allow generalization, subjective |
| **Quota** | Sample can be controlled for certain characteristics | Selection bias, no assurance of representativeness |
| **Snowball** | Can estimate rare characteristics | Time consuming |
| **Simple Random** | Easily understood, results projectable | Difficult to construct sampling frame, expensive, lower precision, no assurance of representativeness |
| **Systematic** | Can increase representativeness, easier to implement, sampling frame not always necessary | Can decrease representativeness |
| **Stratified** | Includes all important sub-populations, precision | Difficult to select relevant stratification variables, not feasible on many variables, expensive |
| **Cluster** | Easy to implement, cost-effective | Imprecise, difficult to compute and interpret results |

---

## Part 2: Sampling Distribution of the Mean

### 2.1 Introduction

After taking samples that represent the population, the next step is to make **inference about the population from the sample**. The main concern when making statistical inference is drawing conclusions about a **population, not about a sample**.

In practice, you select a single random sample of a predetermined size. Hypothetically, to use the sample **statistic** (note: singular, not "statistics"), you should examine every possible sample of a given size.

- A **sampling distribution** is the distribution of the results if you actually selected all possible samples. The single result obtained in practice is just one of the results in the sampling distribution.
- The **sample mean** ($\bar{x}$) is the most widely used measure of central tendency and is often used to estimate the population mean ($\mu$).
- The **sampling distribution of the mean** is the distribution of all possible sample means if you select all possible samples of a given size.

### 2.2 Sample Mean and Standard Error from Normally Distributed Populations

Let $x_i$ be the $i$-th value of a variable $X$, where $i = 1, 2, \dots, N$ and $N$ is the population size.

**Population parameters:**

$$\mu = \frac{\sum_{i=1}^{N} x_i}{N}, \quad \sigma = \sqrt{\frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}}$$

If you are sampling from a population that is **normally distributed** with mean $\mu$ and standard deviation $\sigma$, then regardless of the sample size $n$, the sampling distribution of the sample mean $\bar{X}$ is normally distributed with:

**Mean of sample means:**
$$\mu_{\bar{X}} = \mu$$

**Standard error of the mean:**
$$\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}$$

**Distribution notation:**
$$\bar{X} \sim N\left(\mu, \frac{\sigma}{\sqrt{n}}\right)$$

> **Note:** For most practical applications, $\sigma$ (and $\mu$) is unknown. When $\sigma$ is unknown, the **sample standard deviation** $S$ can be used:
> $$S = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}}, \quad \text{where } \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$
> This will be revisited in later topics on estimation.

### 2.3 Finding Probability of a Sample Mean

Recall from the normal distribution topic: to find the area (probability) below any random variable $X$, convert to standardized $Z$ values:

$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

To find the probability of a random sample mean $\bar{X}$, substitute $\bar{X}$ for $X$, $\mu_{\bar{X}}$ for $\mu$, and $\sigma_{\bar{X}}$ for $\sigma$:

$$Z = \frac{\bar{X} - \mu_{\bar{X}}}{\sigma_{\bar{X}}} = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)$$

#### Worked Example

Given a normal distribution with $\mu = 100$ and $\sigma = 10$. If you select a random sample of $n = 25$, what is the probability that the sample mean $\bar{X}$ is:

**a. Less than 95?**

$$Z = \frac{95 - 100}{10/\sqrt{25}} = \frac{-5}{2} = -2.50$$

$$P(\bar{X} < 95) = P(Z < -2.50) = 0.0062$$

**b. Between 95 and 97.5?**

For $\bar{X} = 95$: $Z = -2.50$

For $\bar{X} = 97.5$: $Z = \frac{97.5 - 100}{2} = -1.25$

$$P(95 < \bar{X} < 97.5) = P(-2.50 < Z < -1.25) = 0.1056 - 0.0062 = 0.0994$$

**c. Above 102.2?**

$$Z = \frac{102.2 - 100}{2} = 1.10$$

$$P(\bar{X} > 102.2) = P(Z > 1.10) = 1 - 0.8643 = 0.1357$$

### 2.4 Sampling from Non-Normally Distributed Populations: Central Limit Theorem

The sampling distribution of the mean for a normally distributed population is straightforward, but assuming normality is often unrealistic in real applications. The **Central Limit Theorem (CLT)** addresses this.

> **Central Limit Theorem:** As the sample size gets large enough, the sampling distribution of the mean is **approximately normally distributed**. This is true **regardless of the shape** of the distribution of the individual values in the population.

**Practical Rules for CLT:**

| Population Shape | Minimum Sample Size for Approximate Normality |
|-----------------|-----------------------------------------------|
| Most distributions (regardless of shape) | $n \geq 30$ |
| Fairly symmetric distributions | $n \geq 5$ (can be smaller) |
| Normally distributed population | Any $n$ (exactly normal) |

The diagrams in the lecture illustrate this: for uniform, bimodal, and right-skewed population distributions, the sampling distribution of $\bar{X}$ with $n=5$ begins to look more normal, and with $n=30$ it is approximately normal in all cases.

### 2.5 Key Takeaways (Recap)

1. Different types of sampling methods exist, classified as probability and nonprobability sampling
2. The sampling distribution of the mean for a normally distributed population is $\bar{X} \sim N(\mu, \sigma/\sqrt{n})$
3. The sampling distribution of the mean can be used to find probabilities of sample means via Z-standardization
4. The Central Limit Theorem allows us to use normal distribution methods even when the population is not normal, provided $n$ is large enough

---

## Related Topics

- [[FAD1015 L15-L16 — Normal Distribution & Approximation]] — prerequisite: normal distribution properties and Z-scores
- [[FAD1015 L21-L22 — Estimation of Population Mean]] — application of sampling distributions
- [[FAD1015 Tutorial 9 — Sampling Methods]] — practice problems on sampling methods
- [[Probability Distributions]] — concept page linking all distribution topics

## Related Course Page

- [[FAD1015 - Mathematics III]]
