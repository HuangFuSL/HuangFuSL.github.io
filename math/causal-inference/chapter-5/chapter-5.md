# Interaction

This chapter considers a system that consists multiple treatment variables.

## From Joint Intervention to Interaction

**Intervention** is to manually set the value of **treatment** variable ignoring the original distribution of the variable. Intervention on multiple variables are called **joint intervention**.

Let the treatment variable be $A$ and $B$. If the causal effect (measured in *risk difference*) of treatment $A$ is different with different values of $B$, then $B$ has an *additive* interaction on $A$. Notice that $B$ has an interaction on $A$ is equivalent to $A$ has an interaction on $B$.

$$
P(Y^{a = 1, b = 1} = 1) - P(Y^{a = 0, b = 1} = 1) \not = P(Y^{a = 1, b = 0} = 1) - P(Y^{a = 0, b = 0} = 1)
$$

!!! success "Superadditive and subadditive"
    Rewrite the above inequality as

    $$
    \begin{aligned}
        P(Y^{a = 1, b = 1} = 1) - P(Y^{a = 0, b = 0} = 1) &\not = [P(Y^{a = 1, b = 1} = 1) - P(Y^{a = 0, b = 1} = 1)] \\
        &+ [P(Y^{a = 1, b = 0} = 1) - P(Y^{a = 0, b = 0} = 1)]
    \end{aligned}
    $$

    If the $\not =$ can be replaced by $>$ or $<$, then the interaction is called **superadditive** or **subadditive**, respectively.

    Similarly, if the causal effect (measured in *risk ratio*) of treatment $A$ is different with different values of $B$, or vice versa, then there is a *multiplicative* interaction between $A$ and $B$. If the $\not =$ can be replaced by $>$ or $<$, then the interaction is called **supermultiplicative** or **submultiplicative**, respectively.

    $$
    \frac{P(Y^{a = 1, b = 1} = 1)}{P(Y^{a = 0, b = 0} = 1)} \not = \frac{P(Y^{a = 1, b = 0} = 1)}{P(Y^{a = 0, b = 0} = 1)} \times \frac{P(Y^{a = 1, b = 1} = 1)}{P(Y^{a = 0, b = 1} = 1)}
    $$

### Idenfication of Interactions

To identify the interaction between $A$ and $B$, we need make sure that **consistency, exchangeability, positivity** for $A$ is satisfied for all values of both $A$ and $B$.

Notice the difference between effect modification and interaction. If $B$ is randomly assigned, then $B$ interacts with $A$ is equivalent to that $B$ serves as an effect modifier for $A$.

!!! warning "Effect modification v.s. interaction"
    In an interaction, the two variables are of **equal status**, we can intervene on either or both of them. In effect modification, one variable is the treatment and the other is the modifier, we can **only intervene on the treatment variable**.

    For treatment variables, we need consistency, exchangeability, positivity. But such conditions are not required for modifier variables.

### Response Type

For each individual, the potential outcome pattern for receiving different levels of treatment is called **response type**.

{{ latex_image('imgs/5-response-type.tex') }}

For binary outcome and one binary treatment, there are $2^{2^1} = 4$ response types. For binary outcome and two binary treatments, there are $2^{2 ^ 2} = 16$ response types.

!!! success "Monotonicity"
    For a response type, when treatment variables except $A$ are fixed, if $Y^{a = 1} \geq Y^{a = 0}$, then the causal effect of $A$ on $Y$ is monotonic.

## Sufficient Cause Interaction

Consider the mechanism of yielding certain outcome by controlling one binary treatment variable $A$. There are three types of mechanisms to *inevitably* yield the outcome.

1. With treatment $A$.
2. Without treatment $A$.
3. $A$ is irrelevant to the outcome.

Since the outcome is stochastic, there exists some unknown factors $U_1, U_2, U_0$ that leads to the outcome, respectively. For example, we can say $\{A = 1, U_1 = 1\}, \{A = 0, U_2 = 1\}$ or $\{U_3 = 1\}$ are **sufficient-component causes** for the outcome.

For models with $k$ binary treatment variables, there are $3^k$ possible mechanisms. If any individual $U_i = 1$ corresponds to multiple variables exists, then there exists **sufficient cause interaction** among these variables.

Let $k = 2$ and the treatment variables be $A, B$, respectively. The sufficient cause interaction is **synergistic** if $A = 1, B = 1$ is a sufficient-component cause for the outcome. The sufficient cause interaction is **antagonistic** if $A = 1, B = 0$ or $A = 0, B = 1$ are sufficient-component causes for the outcome.

When monotonicity holds, some sufficient causes are not possible.

## Summary

Sufficient-component-cause framework and the counterfactual framework focus on different interaction questions:

1. Sufficient-component-cause framework focuses on the causal mechanism (reason) of the outcome.
2. Counterfactual framework focuses on the causal effect of the treatment.