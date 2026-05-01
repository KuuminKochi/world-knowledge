---
title: "FAD1015 Week 2 — Mutually Exclusive & Conditional Probability"
date: 2026-04-27
tags:
  - source/lecture
  - course/FAD1015
  - topic/probability
  - status/seedling
week: 2
lectures:
  - "Lec 3: Mutually Exclusive Events"
  - "Lec 4: Conditional Probability"
---

# FAD1015 Week 2 — Mutually Exclusive & Conditional Probability

Week 2 covers two lectures: Lec 3 on mutually exclusive events and the addition rule, and Lec 4 on conditional probability and the multiplication rule. Source file: `FAD1015 Week 2 Mutually Exc Conditional Prob.pdf`

---

## Lec 3: Mutually Exclusive Events

### Definition
Events are **mutually exclusive** if they **cannot occur at the same time**.

- When $A$ and $B$ are mutually exclusive, there is no overlap between $A$ and $B$:
$$P(A \cap B) = 0$$
i.e. the two events cannot occur at the same time.

**Examples:**
- With one throw of a dice, the events 'scoring a 3' and 'scoring a 5' → mutually exclusive.
- However, the events 'scoring an even number' and 'scoring a prime number' → **not** mutually exclusive.

### Addition Rule for Mutually Exclusive Events

So, the addition rule for mutually exclusive events is:
$$P(A \text{ or } B) = P(A) + P(B)$$
$$P(A \cup B) = P(A) + P(B)$$

The rule can be extended to $n$ mutually exclusive events $A_1, A_2, A_3, \dots, A_n$:
$$P(A_1 \text{ or } A_2 \text{ or } A_3 \text{ or } \dots \text{ or } A_n) = P(A_1) + P(A_2) + P(A_3) + \dots + P(A_n)$$

### Venn Diagram Relationships

For events where $A$ and $B$, $B$ and $C$ are **not** mutually exclusive, but $A$ and $C$ **are** mutually exclusive:
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- $P(A \cup C) = P(A) + P(C)$ *(since $P(A \cap C) = 0$)*
- $P(A' \cap C) = P(C)$
- $P(B' \cap C) = P(C) - P(B \cap C)$
- $P(A' \cap B') = 1 - P(A \cup B)$

### Examples

**Example 1**
A pair of dice is thrown, find the probability that the sum of the numbers on the dice is 10 or sum is divisible by 6.

**Example 2**
In a race where there can be only one winner, the probability that Iskandar will win is 0.3 and the probability that Habib will win is 0.2. Find the probability that:
(a) Iskandar or Habib wins,
(b) someone else wins.

**Example 3**
The probability of the events $A, B$ and $C$ is given below:
$P(A) = 0.44$, $P(B) = 0.37$, $P(C) = 0.41$, $P(A \cup B) = 0.67$,
$P(B \cap C) = 0.15$ and $A$ and $C$ are mutually exclusive. Using the Venn diagram, evaluate:
(a) $P(A \cap B)$   (a) $P(B' \cap C)$
(b) $P(A \cap C)$   (b) $P(A' \cap B')$
(c) $P(A \cup C)$   (c) $P(A \cup B \cup C)$
(d) $P(B \cup C)$   (d) $P(A \cup B \cup C)'$
(e) $P(A' \cap C)$

**Example 4**
A card is dealt from an ordinary pack of 52 playing cards. Find the probability that the card is:
(a) a spade or a club,
(b) a spade or a Queen.

**Example 5**
All the students in a class of 30 study at least one of the subject, Geography and Science. Of these, 20 study Geography and 21 study Science. Find the probability that a student chosen at random:
(a) studies both Geography and Science,
(b) studies only Geography.

**Example 6**
The students in a class of 50 either take Biology or Physics. There are 20 students who take Physics, 15 male students who take Biology and there are 23 female students in the class. Find the probability that a student chosen at random is a:
(a) female and takes Physics,
(b) male or takes Biology.

**Example 7**
Events $A$ and $B$ are such that $P(A \text{ occurs}) = 0.6$, $P(B \text{ occurs}) = 0.7$, $P(\text{at least one of } A \text{ and } B \text{ occur}) = 0.9$. Find:
(a) $P(\text{both } A \text{ and } B \text{ occur})$,
(b) $P(\text{neither } A \text{ nor } B \text{ occurs})$,
(c) $P(A \text{ occurs or } B \text{ occurs but not both } A \text{ and } B \text{ occur})$.

---

## Lec 4: Conditional Probability

### Definition
Conditional Probability is used when the probability that an event will occur depends on whether another event has occurred.

For events $A$ and $B$, the **conditional probability** that event $B$ occurs, given that the event $A$ has already occurred:
$$P(B \text{ given } A) \text{ is written } P(B \mid A)$$

Since $A$ has already occurred, the sample space is reduced to just $A$.

### Formulas

**Using counts:**
$$P(B \mid A) = \frac{n(A \text{ and } B)}{n(A)}$$

**Using probabilities:**
$$P(B \mid A) = \frac{P(A \text{ and } B)}{P(A)} = \frac{P(A \cap B)}{P(A)}$$
*provided that $P(A) \neq 0$.*

### Multiplication Rule
This gives the multiplication rule:
$$P(A \text{ and } B) = P(A) \times P(B \mid A)$$

### Dependent vs Independent Events
- The events $A$ and $B$ are **dependent** if the first event, $B$, affects the outcome or occurrence of the second event, namely $A$.
- On the other hand, the events $A$ and $B$ are **independent** if the first event, say $A$, does not affect the outcome or occurrence of the second event, say $B$.

### Examples

**Example 8**
Given $A$ and $B$ be events such that $P(A) = 0.25$, $P(B) = 0.2$ and $P(A \cup B) = 0.55$. Evaluate:
(a) $P(A \mid B)$
(b) $P(B \mid A)$
(c) $P(A \mid B')$

**Example 9**
A number is chosen at random from the numbers $1, 2, 3, \dots, 20$. If it is known that the number is even, what is the probability that it is greater than 15?

**Example 10**
The probability that Ali will do well in his written Japanese language test is 0.7 and the probability that he will do well in the oral test is 0.5. The probability that he will do well in both tests is 0.25.
(a) If he did well in his oral test, what is the probability that he will do well in the written test?
(b) If he did well in his written test, what is the probability that he will do well in the oral test?

**Example 11**
Show that for any two events $A$ and $B$, with $P(B) > 0$ that:
$$P(A \mid B) + P(A' \mid B) = 1$$

**Example 12** *(From Example 5)*
All the students in a class of 30 study at least one of the subject, Geography and Science. Of these, 20 study Geography and 21 study Science. Find the probability that a student chosen at random:
(a) studies both Geography and Science,
(b) studies only Geography,
(c) studies Geography, given that the student studies Science,
(d) studies Science, given that the student studies Geography.

**Example 13 — Two-way table**
A machine shop has an experience machinist and an apprentice. The experienced machinist who is faster and more skilful, produced 10 items of which only one is defective while the apprentice produced 8 items of which 2 are defective. Unaware of this, a buyer randomly select one of this items. What is the probability that the item is machined by the apprentice?

If the item is found to be defective, what is the probability that it is machine by the apprentice?

**Example 14 — Tree diagram**
There are 5 red marbles and 7 blue marbles in a bag. Delisa takes a marble from the bag, puts it on the table and then takes another marble from the bag. Find the probability that she takes out:
(a) a red marble then a blue marble,
(b) two marbles that are the same colour,
(c) at least one red marble.

**Example 15**
The probability that Marya goes swimming on any day is 0.2. On a day that she goes swimming, the probability that Marya has chocolate pancake for breakfast is 0.75. On a day when she does not go swimming, the probability that she has chocolate pancake for her breakfast is $x$. The probability that Marya has chocolate pancake for breakfast on any day is 0.5.
(a) Find $x$,
(b) Given that Marya has chocolate pancake for breakfast, find the probability that she went swimming that day.

---

## Key Equations

| Concept | Formula |
|---------|---------|
| Mutually exclusive | $P(A \cap B) = 0$ |
| Addition rule (mutually exclusive) | $P(A \cup B) = P(A) + P(B)$ |
| Addition rule (general) | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| Conditional probability | $P(B \mid A) = \dfrac{P(A \cap B)}{P(A)}$ |
| Multiplication rule | $P(A \cap B) = P(A) \cdot P(B \mid A)$ |
| Complement under conditioning | $P(A \mid B) + P(A' \mid B) = 1$ |

---

## Related Topics

- [[FAD1015 Week 1 — Counting Rules & Permutation]] — prerequisite counting
- [[FAD1015 Week 3 — Independent Events & Bayes' Theorem]] — extends conditional probability to independence and Bayes' theorem
- [[FAD1015 Tutorial 1-6 — Counting & Probability Fundamentals]] — practice problems

## Related Course Page

- [[FAD1015 - Mathematics III]]
