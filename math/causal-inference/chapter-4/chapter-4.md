# Effect Modification

A null average causal effect **does not imply a null average causal effect for a subset of the population**. A variable $V$ is an effect modifier if the average causal effect of $A$ on $Y$ differs across levels of $V$.

An effect modifier does need to directly have causal relationship with the different causal effect. If the difference in causal effects can be interpreted causally, the variable is a *causal effect modifier*, otherwise it is a *surrogate effect modifier*.

!!! success "Effects in the treated"
    Notice the treatment variable itself can be regarded as a subgroup. The average causal effect in the treated is measured on subgroup $A = 1$.

    $$
    P(Y^{a = 1} = 1 | A = 1) - P(Y^{a = 0} = 1 | A = 1)
    $$

    1. If the distribution of individual causal effects varies between the treated and untreated, the average causal effect in the treated is not equal to the average causal effect in the population.
    2. $P(Y^{a = 0} = 1 | A = 1)$ is unidentifiable. Estimating $P(Y^{a = 0} = 1 | A = 1)$ requires *partial* exchangeability $Y^{a = 0} \perp A \mid L$.
    3. Following the definition of effects in the treated, we can define effects in the untreated, which is defined on subgroup $a = 0$. Effects in the untreated requires partial exchangeability $Y^{a = 1} \perp A \mid L$.

    The counterfactual $P(Y^{a} = 1 | A = a')$ can be estimated using standardization or IP weighting.

    1. Standardization: $P(Y^{a} = 1 | A = a') = \sum_{l} P(Y = 1 | A = a, L = l) P(L = l | A = a')$
    2. IP weighting: $P(Y^{a} = 1 | A = a') = E\left[\frac{I(A = a)Y}{f(A | L)P(A = a' | L)}\right]/E\left[\frac{I(A = a)}{f(A | L)P(A = a' | L)}\right]$

The extrapolation of computed causal effects across populations are called *transportability*. Transportability is an unverifiable assumption. If the effect modification measure, version of treatment and the in-group interference are similar, we can assume transportability.

From effect modification, we can identify the subgroup that benefits most from the treatment or intervention. Moreover, effect modification helps us to learn underlying mechanisms of the outcome.

## Effect Modification v.s. Prognostic Factor

When marginal randomization does not hold, there exists a prognostic factor $L$ is a variable that affect the treatment assignment, while an effect modifier $V$ affects the effect. To estimate causal effects in such conditions, extra adjustments are required

### Stratification

Stratification can be used to adjust the marginal causal effect of $A$ on $V$. However, it requires to take all the combinations of $V$ and $L$ into account. And stratification requires positivity condition to be met on $L$.

Using stratification, we can yield the conditional causal effect of $A$ on $Y$ for each stratum. The per-stratum causal effect can be further weighted to get a pooled causal effect.

Notice that stratification will introduce sampling variability when the stratification is getting finer.

### Matching

Matching strategy is similar but inversed approach to IP weighting.

The goal of matching is to construct a subset of the population in which the distribution of $L$ is similar between the treated and untreated by sampling in the treated part or untreated part. Stratas with only treated or untreated individuals are excluded.

Usually, the group with more individuals between the treated and untreated is sampled to match the other group. The subgroup being matched is used to calculate the average effect in the treated or untreated.

However, as matching changes the distribution of $L$, the distribution of causal modifier $V$ will also be changed.

## Overview of Adjustment Methods

There are 4 methods to adjust the causal effect of $A$ on $Y$, including standardization, IP weighting, matching and stratification.

1. Standardization and IP weighting can be used to compute marginal or conditional causal effects.
2. Matching and stratification can be used to compute conditional causal effects in subgroups.
3. With effect modification, the causal effect of different adjustment methods may be different.