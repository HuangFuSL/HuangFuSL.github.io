# Randomized Experiments

Key concepts: **random experiment**, **exchangeability**, **effect modification**

## Randomized Experiments

Consider the following treatment assignment:

{{ latex_image('imgs/1-causation-association-difference.tex') }}

Assume that the treatment assignment is determined by a random procedure, the experiment is called a **random experiment**. Then exchanging the individual in treated group with those in control group will not affect the association measure.

If a random experiment satisfies the following conditions, it is called an **ideal randomized experiment**:

1. Full adherence: All individuals follow the treatment assignment.
2. No loss to follow-up: All individuals are followed up and their outcomes are observed.
3. Single treatment: Each individual is assigned to one treatment only.
4. Double-blind assignment: The treatment assignment is unknown to both the individuals and the researchers.

If all the possible values of treatment variable $A = a$ are sequentially assigned to individuals, the experiment is called **crossover experiment**. Individual causal effects can be estimated using crossover experiments if the following conditions are met:

1. No carryover effect: The treatment effect of $a$ does not depend on the previous treatments.
2. The individual causal effect $\alpha_i = Y^{a_t = 1}_{it} - Y^{a_t = 0}_{it}$ does not depend on time.
3. The potential outcome under no treatment does not depend on time.

By assigning the treatment value sequence randomly, we can remove the required conditiona 3. In such case:

$$
(Y_{i1} - Y_{i0})A_{i1} - (Y_{i0} - Y_{i1})A_{i0}
$$

estimates the individual causal effect $E(\alpha_i)$ under condition 2. If condition 2 is not met, the estimator estimates $E(\alpha_{i0} + \alpha_{i1}) / 2$.

### Exchangeability

!!! success "Exchangeability"
    * **(Full) exchangeability** indicates that swapping the treatment assignment of two individuals does not affect the association measure, or $Y^a \perp A$.
    * **Mean exchangeability** indicates that $\forall a', E(Y^a | A = a') = E(Y^a)$, or the **expectation** of switched potential outcome is the same as the original one.

    When $Y$ and $A$ are binary, full exchangeability is equivalent to mean exchangeability. Mean exchangeability is sufficient for deriving $E(Y^a) = E(Y | A = a)$.

Exchangeability indicates that all the potential outcome and the treatment assignment are independent, i.e. $\forall a, Y^{A = a} \perp A$, or the treatment assignment is exogenous. Under exchangeability, $P(Y = 1 | A = a)$ is an unbiased estimator of $P(Y^{a} = 1)$.

!!! danger "$Y^a\perp A$ and $Y\perp A$"
    Notice that $Y^a \perp A$ is not equivalent to $Y \perp A$. The latter indicates that treatment $A$ does not have any causal effect on the outcome $Y$. If $\forall a, E(Y^a) = E(Y)$, then $Y\perp A$.

Notice that a randomized experiment could be unexchangeable even if infinite samples are collected.

### Conditional Randomization

Consider an additional factor $L$ affects the assignment of treatments, i.e., when $L$ takes different values, the distribution of $A$ is different. Such a randomized experiment is called **conditional randomized experiment**. In a conditional randomized experiment, the corresponding randomized experiment using the overall distribution of $A$ is called **marginally randomized experiment**.

Although the marginally randomized experiment is exchangeable, the conditional randomized experiment is not exchangeable in general. Only conditional exchangeability holds in such randomized experiments, i.e. $\forall a, Y^a \perp A | L$.

We can measure the causal effects on sub-groups $P(Y^{a = 1} = 1 | L = l) - P(Y^{a = 0} = 1 | L = l)$ using conditional exchangeability (**stratification**) or directly measure the overall causal effect $P(Y^{a = 1} = 1) - P(Y^{a = 0} = 1)$ on the population using marginal exchangeability. For different sub-groups, the causal effects may be different, which is called **effect modification** or **treatment effect heterogeneity**.

!!! success "Stratification"
    Stratification is to split the population into mutually exclusive sub-groups in which the treatment assignment is exchangeable. The causal effect can be estimated in each sub-group.

## Standardization

We can view the marginal risk as a weighted average of the conditional risks:

$$
P(Y^a = 1) = \sum_{l\in \calL} P(Y^a = 1 | L = l) P(L = l)
$$

With conditional exchangeability holds, we can derive that $P(Y^a = 1) = \sum_{l\in \calL} P(Y = 1 | A = a, L = l) P(L = l)$, which is called **standardization**, making the unobserved potential outcome $P(Y^a = 1)$ to be identifiable.

### Inverse Probability Weighting

Notice that

$$
P(A = a | L = l) = \frac{P(A = a, L = l)}{P(L = l)}
$$

We can assign the weight $w_l = \frac{1}{P(A = a | L = l)}$ to each individual with $L = l$ to construct a **pseudo-population**. The pseudo-population satisfies exchangeability, and we can use the pseudo-population to estimate the causal effect. The IP weighted mean of outcome $Y$ is $E\left( I(A = a) Y / P(A = a | L)\right)$, where $I(A = a)$ is the indicator function.

Assuming that $\forall l, P(A = a | L = l) > 0$, we can derive that

$$
\begin{aligned}
    & E\left( \frac{I(A = a) Y}{P(A = a | L)}\right) \\
    =& \sum_{l} \frac{E\left( I(A = a) Y | L = l\right) P(L = l)}{P(A = a | L = l)} \\
    =& \sum_{l} \frac{E\left( Y | A = a, L = l\right) P(A = a | L = l)P(L = l)}{P(A = a | L = l)} \\
    =& \sum_{l} E\left( Y | A = a, L = l\right) P(L = l) \\
    =& \sum_{l} E(Y^a | L = l) P(L = l) \\
    =& E(Y^a)
\end{aligned}
$$

Therefore, under positivity assumption, IP weighting is equivalent to standardization.

!!! success "Positivity"
    For any individual in any sub-group $l$ has a non-zero probability of receiving treatment $a$, i.e. $\forall l, \forall a, P(A = a | L = l) > 0$.
