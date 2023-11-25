# Observational Studies

In an **observational** study, the variables are neither assigned nor controlled by the researcher. The researcher only observes the values of the variables. Compared with randomized experiments, observational studies are more limited to the researchers.

## Identifiability Conditions

If the following **identifiability** conditions are met, the observational study can be regarded as a conditionally randomized experiment.

!!! success "Identifiability condition"

    1. **Consistency**: The values of treatment under comparison correspond to well-defined interventions that, in turn, correspond to the versions of treatment in the data.
    2. **Exchangeability**: The conditional probability of receiving any value of treatment depends only on **observed** covariates $L$.
    3. **Positivity**: The probability of receiving any value of treatment is strictly positive for all combinations of covariates $L$.

If the identifiability conditions are not met, we can use other methods including instrumental variable to establish another group of identifiability condition.

### Exchangeability

In observational studies, the exchangeablitiy condition may or may not hold, as the observed $L$ may not be the only predictor of the treatment. The true predictor may even be unobserved or unobservable.

Exchangeability is given by

$$
Y^a \perp A \mid L \Longleftrightarrow \forall a, P(Y^a  = 1 \mid A = a, L = l) = P(Y^a = 1\mid A \not = a, L = l)
$$

However, in observational studies, $P(Y^a = 1\mid A\not = a, L = l)$ is unidentifiable. Thus, **the exchangeablitiy cannot be empirically verified**.

### Positivity

To measure causal effects, we need to measure the distribution of outcome under treatment and under no treatment. That is, in the whole sample or any observed subgroup, the probability of receiving any value of treatment should be strictly positive, which is called **positivity**. Notice that positivity is only required for these observed covariates that requires exchangeability.

Standardization and IP weighting are meaningful only if positivity holds.

!!! warning "IP weighting without positivity"
    If positivity does not hold, *IP weighting* is undefined since the denominator in

    $$
    E\left[\frac{I(A = a)Y}{P(A = a | L)}\right]
    $$

    is zero. However, the *IP weighted mean* is still defined.

    $$
    E\left[\frac{I(A = a)Y}{N(A = a, L) / N(L)}\right]
    $$

    Notice that $N(A = a, L) / N(L)$ is defined on observed data. Let $Q(a) = \{l | N(A = a, L) / N(L) > 0\}$. Now, $E\left[\frac{I(A = a)Y}{N(a, L) / N(L)}\right] = E[Y^a | L \in Q(a)]P(L\in Q(a))$ is a **biased** estimator of $E[Y^a]$.

    When positivity does not hold, then $Q(0) \not = Q(1)$, under this condition, the difference between IP weighted means ($E\left[\frac{I(A = 1)Y}{N(A = 1, L) / N(L)}\right] - E\left[\frac{I(A = 0)Y}{N(A = 0, L) / N(L)}\right]$) cannot be interpreted causally.

### Consistency

Consider the following examples in heart transplant studies:

> 1. Two patients received heart transplants performed by different surgeons.
> 2. Two patients received heart transplants performed under different procedures.

Due to the complexity of real-world situations, we always need to aggregate the different treatments into a single treatment value. The map between discrete values of the treatment variable and real-world intervention is called treatment protocol. The first step for investigating the causal effect is to precisely specify the treatment protocol, so that any variation regarded as treatment will lead to the same outcome, or **treatment variation irrelevance**. Under this condition can we define the potential outcome under the specified treatment value. In addition, the treatment protocol of interest and the treatment protocol of the observed data should be the same.

Under the treatment variation irrelevance, we can define the potential outcome $Y^a$.

!!! warning "Treatment variation irrelevance"

    Suppose that receiving heart transplant is denoted as $a$, the heart transplant is performed by Alex and Bob. But the treatment protocol is observed as the heart transplant is performed by Alex. Then, the treatment variation irrelevance is violated and consistency assumption $Y = Y^{a = 1}$ does not hold.

## Target Trial

Under the identifiability conditions, we can regard the observational study as a conditionally randomized experiment. The equivalent hypothetical, randomized experiment is called **target trial**.
