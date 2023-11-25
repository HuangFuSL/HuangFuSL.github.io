# A Definition of Causal Effect

Key concepts: **treatment**, **outcome**, **average causal effect**, **potential outcome**, **consistency**, **causation-association difference**, **identifiability**

## Treatment and Outcome

We want to compare the result when a specified action is or is not applied to an individual. The action is called a **treatment**, and the result is called an **outcome**, which are denoted by $A$ and $Y$ respectively. Usually we take $A$ and $Y$ to be both binary.

The outcome under a specified treatment $A = a$ is denoted by $Y^{A = a}$. In reality, we can only observe one value of $Y^{A = 1}$ or $Y^{A = 0}$ for each individual. Each $Y^{A = a}$ is called a **potential outcome**. If $A = a$ is observed, $Y^{A = a}$ is **factual**, and $Y^{A = 1 - a}$ is **counterfactual**. The probability of potential outcome $Y = 1$ is called **risk**.

!!! success "Consistency assumption"
    If $A = a$ is observed, then $Y = Y^{A = a}$.

## Causal Effects

!!! success "Identifiability"
    A quantity is **identifiable** if it can be expressed (unbiasedly) as a function of the distribution of the observed data.

Before we clarify the definition of causal effect, we need to make some assumptions on individual outcome.

!!! success "No interference assumption"
    The potential outcome under $A = a$ **does not depend** on the treatment of other individuals (i.e. **no interference**).

### Individual Causal Effect

If for individual $i$, $Y_i^{A = 1} \not = Y_i^{A = 0}$, then we say that the treatment has a **causal effect for individual $i$**.

### Average Causal Effect

The **average causal effect** is defined as

$$
P(Y^{A = 1} = 1) - P(Y^{A = 0} = 1)
$$

or

$$
E(Y^{A = 1}) - E(Y^{A = 0})
$$

The two forms of average causal effect are equivalent. We can test average causal effect by testing the **causal null hypothesis** $H_0: P(Y^{A = 1} = 1) = P(Y^{A = 0} = 1)$. However, the absence of average causal effect does not imply the absence of individual causal effect. We call the null hypothesis $H_0: \forall i, Y_i^{a = 1} = Y_i^{a = 0}$ as **sharp causal null hypothesis**.

### Functional Causal Effect

We can measure the outcome $Y$ over a function $f(y)$. For example $V(Y^{a = 1}) - V(Y^{a = 0})$ as the causal effect on sample variance. Notice that $V(Y^{a = 1}) - V(Y^{a = 0})$ usually does not equal to $V(Y^{a = 1} - Y^{a = 0})$.

### Measuring Causal Effects

The causal null hypothesis can be written as

1. Difference: $H_0: P(Y^{a = 1} = 1) - P(Y^{a = 0} = 1) = 0$
2. Ratio: $H_0: \frac{P(Y^{a = 1} = 1)}{P(Y^{a = 0} = 1)} = 1$
3. Odds ratio: $H_0: \frac{P(Y^{a = 1} = 1) / P(Y^{a = 1} = 0)}{P(Y^{a = 0} = 1) / P(Y^{a = 0} = 0)} = 1$

When $H_0$ is rejected, we can use **number needed to treat** (NNT) to measure the strength of causal effect. NNT is defined as the number of individuals needed to be treated to prevent one additional bad outcome. NNT is given by:

$$
\text{NNT} = \frac{-1}{P(Y^{a = 1} = 1) - P(Y^{a = 0} = 1)}
$$

## Random Variability

In reality, we can only collect a sample of individuals in the population, and our estimate on causal effect suffers from random variability.

1. Sampling variablility: We use $\hat P(Y^{a = 1} = 1) = N(Y^{a = 1}) / N(Y)$ as an estimator of $P(Y^{a = 1} = 1)$. The estimator suffers from random variability.
2. Potential outcomes are usually not deterministic, which makes another source of random variability.


## Causation and Association

In the real world, we can only observe one potential outcome for each individual. Therefore, we cannot directly measure the outcome $P(Y^{a = 1} = 1)$ and $P(Y^{a = 0} = 1)$. Instead, we can only use $P(Y = 1 | A = 1)$ and $P(Y = 1 | A = 0)$ as estimators.

Like the causal null hypothesis, we can also define the independent ($A\perp Y$) null hypothesis in three forms:

1. Risk difference: $H_0: P(Y = 1 | A = 1) - P(Y = 1 | A = 0) = 0$
2. Risk ratio: $H_0: \frac{P(Y = 1 | A = 1)}{P(Y = 1 | A = 0)} = 1$
3. Odds ratio: $H_0: \frac{P(Y = 1 | A = 1) / P(Y = 0 | A = 1)}{P(Y = 1 | A = 0) / P(Y = 0 | A = 0)} = 1$

Notice that any terms in the form of conditional probability or expectation are associations. Only marginal probability or expectation can be causal effects, since the marginal probability takes all other factors into consideration.

{{ latex_image('imgs/1-causation-association-difference.tex') }}
