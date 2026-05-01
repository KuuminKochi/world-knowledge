---
title: "FAD1015 Tutorial 8 — Uniform and Exponential Distributions"
date: 2024-2025
course: FAD1015 Mathematics III
tags:
  - fad1015
  - mathematics
  - uniform-distribution
  - exponential-distribution
  - continuous-probability
  - r-programming
---

# FAD1015: Mathematics III — Tutorial 8

**Centre for Foundation Studies in Science**  
**Universiti Malaya**  
**Session 2024/2025**

---

## Topic: The Uniform and Exponential Distributions

### Question 1
Consider uniform distribution with $a = 0$ and $b = 10$.

(a) What is the probability that the value will be:

&emsp;i. less than 5.

&emsp;ii. between 2 and 7?

&emsp;iii. between 3 and 6?

(b) What are the mean and standard deviation?

### Question 2
A study of the time spent shopping in a supermarket for a market basket of 20 specific items showed an approximately uniform distribution between 20 minutes and 40 minutes.

(a) What is the probability that the shopping time will be:

&emsp;i. between 25 and 30 minutes?

&emsp;ii. less than 35 minutes?

(b) What are the mean and standard deviation of the shopping time?

### Question 3
A computer components manufacturer in Kuala Lumpur has scheduled the normal build time for a complex motherboard to be 65 minutes. Assuming that the actual manufacturing time is uniformly distributed between 50 and 74 minutes:

(a) What is the probability that the manufacturing time will be:

&emsp;i. less than 70 minutes?

&emsp;ii. between 65 and 70 minutes?

&emsp;iii. more than 65 minutes?

(b) What are the mean and standard deviation of the manufacturing time?

### Question 4
The total duration of football games in the major league in the 2013 season is uniformly distributed between 445 hours and 523 hours inclusive.

(a) Find $a$ and $b$ and describe what they represent.

(b) Write the distribution.

(c) Find the mean and the standard deviation.

(d) What is the probability that the duration of games for a team for the 2013 season is between 487 and 502 hours?

(e) What is the 55th percentile for the duration of games for a team for the 2013 season?

### Question 5
Given an exponential distribution with $\lambda = 25$, what is the probability that the arrival time is:

(a) less than $X = 0.2$?

(b) greater than $X = 0.2$?

(c) between $X = 0.1$ and $X = 0.3$?

(d) less than $X = 0.15$ or greater than $X = 0.25$?

### Question 6
Customers arrive at the drive-through window of a fast-food restaurant at a rate of 3 per minute during the lunch hour.

(a) What is the probability that the next customer will arrive:

&emsp;i. within 2 minutes?

&emsp;ii. within 4 minutes?

(b) During the dinner time period, the arrival rate is 2 per minute. What are your answers to (a) for this?

### Question 7
Telephone calls are received at the information desk of a computer software company at a rate of 12 per hour.

(a) What is the probability that the next call will arrive within:

&emsp;i. 5 minutes?

&emsp;ii. 12 minutes?

(b) Suppose the company has just introduced an updated version of one of its software programs, and telephone calls are now received at a rate of 20 per hour. Given this information, what are your answers to (a)?

### Question 8
The number of days ahead travelers purchase their airline tickets can be modeled by an exponential distribution with the average amount of time equal to 18 days. Find the probability that a traveler will purchase a ticket fewer than 9 days in advance. How many days do half of all travelers wait?

### Question 9
On the average, a certain computer part lasts 8 years. The length of time the computer part lasts is exponentially distributed.

(a) What is the probability that a computer part lasts more than 5 years?

(b) On the average, how long would five computer parts last if they are used one after another?

(c) Eighty percent of computer parts last at most how long?

(d) What is the probability that a computer part lasts between nine and 11 years?

---

## Topic: Introduction to R

### Question 1
Use R as a calculator to compute the following values.

(a) $28(121 - 79)$

(b) $\ln(13^2) + 27$

(c) $\sqrt{\frac{354}{29}}$

(d) $\frac{3}{5}e^{-7}$

### Question 2
Create the following vectors in R.

$p = (3, 6, 9, 12, …, 120)$ and $q = (97, 96, 95, …, 58)$

Use vector arithmetic to multiply these vectors and call the result T. Select subsets of T to identify the following.

(a) What are the 13th, 24th, and 35th elements of T?

(b) What are all of the elements of T which are less than 3000?

(c) How many elements of T are greater than 6000?

### Question 3
Using T from Question 2, use R to compute the following statistics of T.

(a) sum

(b) mean

(c) standard deviation

(d) try using function `summary()`. What will you get?

### Question 4
Using R, evaluate the following.

(a) How many ways are there to choose a book and a magazine from 5 different books and 7 different magazines?

(b) In how many ways can five alphabets K, L, M, N, P and T be arranged?

(c) Four letters are arranged from the word MRTKLIA. In how many way can the letters be arranged if repetitions:

&emsp;(i) are not allowed

&emsp;(ii) are allowed

(d) Seven girls and five boys sit in a row. How many possible arrangements are there if:

&emsp;(i) all the girls must sit next to each other?

&emsp;(ii) all the boys are separated?

(e) How many different ways are there to select 5 different students from a class of 9 students?

(f) Three digits are chosen at random from the set {2, 3, 4,…, 9}.

&emsp;(i) How many different combinations are there?

&emsp;(ii) How many ways are there if only odd numbers are chosen?

### Question 5
Aqil sells a magazine that is produced to raise money for homeless people. The probability of making a sale is, independently, 0.09 for each person he approaches. Given that he approaches 20 people, use R to find the probability that he will make:

(a) exactly four sales

(b) two or fewer sales

(c) more than three sales

(d) less than four sales

---

## Related Concepts

- [[Uniform Distribution]] — continuous distribution with constant probability
- [[Exponential Distribution]] — distribution modeling time between events
- [[R Programming]] — statistical computing language
- [[Poisson Process]] — counting process related to exponential
- [[Rate Parameter]] — lambda (λ) in exponential distribution
- [[Memoryless Property]] — characteristic of exponential distribution

---

*Source: FAD1015 25-26 Tutorial 8 Questions.pdf*
