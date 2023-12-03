# Confounding

Confounding is a situation in which the effect of an exposure on an outcome is distorted by the presence of another variable that is associated with both the exposure and the outcome. The confounding effect is a non-causal association that leads to biased estimation of causal effect.

In a causal graph, the confounding effect is caused by an **open backdoor path**. A **backdoor path** is a non-path trail from treatment variable $A$ to outcome variable $Y$ that points to $A$. The simplest structure of confounding contains a variable $L$ pointing to treatment $A$ and outcome $Y$.

{{ latex_image('imgs/7-confounding.tex') }}

Suppose the causal graph is the true causal graph and satisfies faithfulness.

## Exchangeability

Following the definition of backdoor path, the definition of confounding can be alternatively expressed as

!!! success "Alternative definition of confounding"
    Confounding is any systematic bias that can be removed by randomized assignment of treatment $A$ (eliminating the backdoor path).

When backdoor criterion is satisfied, exchangeability stands. The backdoor criterion requires on of the following:

1. **No confounding**: no common cause of treatment $A$ and outcome $Y$.
2. **No unmeasured confounding**: common cause of $A$ and $Y$ exists but a subset $L$ of measured (observed) non-descendants of $A$ blocks all the backdoor paths. The corresponding set $L$ is called a **sufficient set for confounding adjustment**. Variable $L$ is also called a **confounder**.

Unconditional causal effect can be measured when unconditional exchangeability is satisfied. Conditional causal effect can be measured when conditional exchangeability is satisfied. The following table shows causal graph structures holding different exchangeability. The conditioned variable is $L$.

| Causal identifiability table | Unconditional exchangeable | Not unconditional exchangeable |
| :-: | :-: | :-: |
| **Conditional exchangeable** | {{ latex_image('imgs/7-c-u.tex') }} | {{ latex_image('imgs/7-c-nu.tex') }} |
| **Not conditional exchangeable** | {{ latex_image('imgs/7-nc-u.tex') }} | {{ latex_image('imgs/7-nc-nu.tex') }} |

To identify conditional or unconditional causal effect, we can apply standardization on measured variables when conditional or unconditional exchangeability is satisfied. Take the following graph as an example.

{{ latex_image('imgs/7-identification.tex') }}

When either $L_2$ or $L$ is observed, neither unconditional nor conditional exchangeability is satisfied. However, when both $L_2$ and $L$ are observed, both unconditional and conditional exchangeability is satisfied. We can identify the following causal effect based on observation.

1. Conditional causal effect within strata of $L$ and $L_2$: $E[Y | A = a, L = l, L_2 = l_2]$
2. Unconditional causal effect: $E[Y | A = a, L = l, L_2 = l_2]P(L_2 = l_2, L = l)$
3. Conditional causal effect within strata of $L_2$: $E[Y | A = a, L_2 = l_2, L = l]P(L = l | L_2 = l_2)$
4. Conditional causal effect within strata of $L$: $E[Y | A = a, L = l, L_2 = l_2]P(L_2 = l_2 | L = l)$

## Confounders

The sufficient set for identifying confounder depends on variables observed or measured. For a causal graph, there may also exist multiple sufficient sets for confounding adjustment.

### Traditional Confounder

A confounder satisfies the following conditions, which is the definition of a *traditional* confounder.

1. The variable associates with the treatment.
2. Condition on the treatment, the variable associates with the outcome.
3. The variable is not on the causal path from the treatment to the outcome.

However, a variable that satisfies the above conditions is not necessarily a confounder. Variable $L$ in the following graph is a traditional confounder. When $L$ is not adjusted, unconditional causal effect can be directly identified, adjusting for $L$ will introduce extra selection bias.

{{ latex_image('imgs/7-nc-u.tex') }}

<!-- The following conditions fix the definition of traditional confounder:

!!! success "Fixing the traditional definition of confounder"

-->

### Surrogate Confounder

A **surrogate confounder** is a variable that is the result of an unobserved common cause of the treatment and the outcome. The surrogate confounder itself does not lie on a backdoor path. The following graph shows a surrogate confounder $L$.

{{ latex_image('imgs/7-surrogate.tex') }}

Although $L$ does not lie on the backdoor path, observing distribution of $L$ may provide information about the unobserved common cause $U$. In this case, adjusting for $L$ can partially reduce the confounding bias.

## Single-world Intervention Graph

A **single-world intervention graph** (SWIG) is a causal graph that explicitly include the conterfactual variables on the graph. Unlike the causal graph that represents the *real* world, the SWIG represents a *counterfactual* world created by an intervention.

| Causal graph | Single-world intervention graph |
| :-: | :-: |
| {{ latex_image('imgs/7-swig.tex', page=1) }} | {{ latex_image('imgs/7-swig.tex', page=2) }} |

In a SWIG, the original treatment variable $A$ is now regarded as two distinct nodes $A$ and $a$. $A$ encodes the possible value of $A$ under no intervention, $a$ is the value of intervened treatment variable. Any descendant $X$ of $A$ is replaced by $X^a$, which is the value of $X$ under intervention $A = a$. From the SWIG, we can see that after conditioning on $L$, the trail $A\leftarrow L\leftarrow U\rightarrow Y^a$ is blocked, indicating that exchangeability $A \perp Y^a | L$ holds.

!!! success "Confounder cannot be descendants of treatment"
    A confounder cannot be a descendant of the treatment variable. Suppose $L$ is a descendant of $A$, and $L$ connects to $Y$ through some trail. If the trail is a path from $L$ to $Y$, then the whole path through $L$ is a causal path, adjustment on $L$ will block such path. Otherwise, there should be a collider on the path. If the collider is $L$, adjustment on $L$ will open the non-causal trail, introducing extra selection bias. If the collider is not $L$, adjustment on $L$ have no effect.

## Confounding Adjustment

Methods adjust for confounder $L$ can be classified into two categories:

1. **G-methods**: methods that adjust for $L$ by conditioning on $L$ - IP weighting, G-estimation, standardization.
2. **Stratification methods**: methods that adjust for $L$ by stratifying on $L$ - stratification, matching.
3. Other methods: difference-in-difference, instrumental variable, front-door adjustment. These methods does not rely on conditional exchangeability.

### Difference-in-Difference

Consider the following causal graph. We want to measure causal effect on treated $E(Y^1 | A = 1) - E(Y^0 | A = 1)$. But there exists some unknown factors $U$ that affects both treatment $A$ and outcome $Y$. For example, $U$ can be the severity of disease, which affects both the treatment decision and the outcome.

{{ latex_image('imgs/7-did.tex') }}

Notice that

$$
\begin{aligned}
&&& \underbrace{E(Y | A = 1) - E(Y | A = 0)}_{\text{Measured association}} \\
&=&& E(Y^1 | A = 1) - E(Y^0 | A = 0) \\
&=&& \underbrace{(E(Y^1 | A = 1) - E(Y^0 | A = 1))}_{\text{Causal effect on treated}} + \underbrace{(E(Y^0 | A = 1) - E(Y^0 | A = 0))}_{\text{Confounding effect}}
\end{aligned}
$$

To estimate confounding effect $E(Y^0 | A = 1) - E(Y^0 | A = 0)$ we can measure a pre-treatment outcome $C$ before the treatment is applied. There is no direct causal relationship between pre-treatment outcome $C$ and treatment $A$, but $C$ and $A$ show some association since backdoor $C\leftarrow U\rightarrow A$ presents, that is, $E(C | A = 1) - E(C | A = 0) \neq 0$. The metric $E(C | A = 1) - E(C | A = 0) \neq 0$ measures the strength of confounding effect of $A$ on $C$. If the confounding effect of $A$ on $Y$ caused by $Y\leftarrow U\rightarrow A$ is the same as the confounding effect of $A$ on $C$ (additive equi-confounding assumption), then the confounding effect of $A$ on $Y$ can be removed by difference-in-difference.

$$
E(Y^0 | A = 1) - E(Y^0 | A = 0) = E(C | A = 1) - E(C | A = 0)
$$

The causal effect can be measured in

$$
\begin{aligned}
&&& E(Y^1 | A = 1) - E(Y^0 | A = 1) \\
&=&& (E(Y | A = 1) - E(Y | A = 0)) - (E(C | A = 1) - E(C | A = 0))
\end{aligned}
$$

### Front-door Criterion

Consider a causal graph with a treatment $A$, a mediator $M$ and an outcome $Y$. The causal effect of $A$ on $Y$ is confounded by an unobserved variable $U$. The mediator fully mediates the effect of $A$ on $Y$, i.e. all the causal path from $A$ to $Y$ passes through $M$.

{{ latex_image('imgs/7-front-door.tex') }}

First we have

$$
P(Y^a = 1) = \sum_{m} P(Y^a = 1 | M^a = m) P(M^a = m)
$$

$M$ is not confounded, so

$$
P(M^a = m) = P(M = m | A = a)
$$

Notice that

$$
P(Y^a = 1 | M^a = m) = P(Y^m = 1) = P(Y = 1 | M = m)
$$

and

$$
P(Y = 1 | M = m) = \sum_{a'} P(Y^m = 1 | M = m, A = a')P(A = a')
$$

by conditional exchangeability $Y^m \perp M \mid A$. Under this case, $P(Y^a)$ can be identified by

$$
P(Y^a = 1) = \sum_{m} P(M = m | A = a)\sum_{a'} P(Y = 1 | M = m, A = a')P(A = a')
$$
