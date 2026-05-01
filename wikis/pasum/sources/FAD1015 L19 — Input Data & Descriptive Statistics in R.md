---
title: "FAD1015 L19 — Input Data & Descriptive Statistics in R"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1015
  - topic/r-programming
  - topic/descriptive-statistics
  - status/seedling
week: 11
---

# FAD1015 L19 — Input Data & Descriptive Statistics in R

Lecture 19 introducing R programming for data input, descriptive statistics, and data visualization. Source file: `(L19) FAD1015 w11 input data R.pdf`

## Summary

Introduction to R for statistical computing: computing simple statistics from vectors, importing data into RStudio, exploring built-in datasets, and basic visualization with the `Nile` dataset example.

## Key Concepts

- R Programming — statistical computing environment
- Data Input — importing via RStudio interface, built-in datasets
- Descriptive Statistics — `mean`, `median`, `sd`, `var`, `range`, `sum`, `sort`
- Data Visualization — `plot`, `hist`, `boxplot`
- Built-in Datasets — `data()`, `help()`
- Time Series — `Nile` dataset example

## Lecture Coverage

### 1. Simple Statistics

Mathematical and statistical summaries computed from a vector:

```r
1:4          # Sequence 1 to 4
sum(1:4)     # 10
max(1:10)    # 10
min(1:10)    # 1
range(1:10)  # Returns min and max: 1  10
```

Descriptive statistics on random data:
```r
X <- rnorm(10)
mean(X)      # Arithmetic mean
sd(X)        # Standard deviation
median(X)    # Median
var(X)       # Variance
sort(X)      # Sorted values
```

### 2. Importing Data into RStudio

**Via the Environment Pane:**
- Use the **Import Dataset** dropdown in the **Environment** pane.
- Supports: Text (base), Text (readr), Excel, SPSS, SAS, Stata.

**Data Preparation Notes:**
- Avoid spaces and special characters in column names (use underscores or periods).
- Handle missing data appropriately before import.

### 3. Built-in Datasets

List and load available datasets:
```r
data()          # View all built-in datasets
data("Nile")    # Load the Nile dataset
help(Nile)      # View dataset description
```

### 4. Working with the Nile Dataset

The `Nile` dataset contains annual flow of the river Nile at Aswan from 1871–1970.

**Descriptive Statistics:**
```r
mean(Nile)
sd(Nile)
summary(Nile)   # Min, 1st Qu, Median, Mean, 3rd Qu, Max
```

**Visualization:**
```r
plot(Nile)      # Time series plot
hist(Nile)      # Histogram
```

### 5. Practice Activities

**Activity 1 — Dahlia.csv:**
Load `Dahlia.csv` and perform:
1. Summarize the dataset (`summary()`)
2. Display rows and columns (`dim()`)
3. Display column names (`names()`)
4. Create a histogram of sepal length with labeled axes
5. Create a scatter plot of sepal length vs sepal width
6. Create a boxplot of sepal length by species
7. Extract `sepal.length` and calculate its standard deviation

**Activity 2:**
Using any available dataset in R, calculate summary statistics and plot histograms/scatterplots.

> **Advanced Visualization Reference:** [Top 50 Ggplot2 Visualizations](http://r-statistics.co/Top50-Ggplot2-Visualizations-MasterList-R-Code.html)

## Related Topics

- [[FAD1015 L17-L18 — Uniform & Exponential Distributions + R Intro]] — prerequisite R concepts
- [[FAD1015 L25-L26 — Hypothesis Testing in R]] — extends R programming
- [[FAD1015 Tutorial 12 — Hypothesis Testing in R]] — practice problems

## Related Course Page

- [[FAD1015 - Mathematics III]]
