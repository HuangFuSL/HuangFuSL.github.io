# Selection bias

Selection bias is caused by extra association caused by only part of the population is selected for analysis. Selection bias is caused by conditioning on a common effect of treatment and outcome, even if the treatment actually has no individual causal effect on the outcome.

On the causal graph, selection bias is caused by either condition on a collider or descendant of a collider. In reality, selection bias can both appear in observational studies or randomized experiments since participants may be removed from the study before the outcome is observed. If participants are removed **not in random**, selection bias is introduced.

{{ latex_image('imgs/8-condition-on-common-effect.tex') }}

$$
\frac{P(Y = 1 | A = 1)}{P(Y = 1 | A = 0)} = \frac{P(Y^{a = 1} = 1)}{P(Y^{a = 0} = 1)} \not = \frac{P(Y = 1 | A = 1, L = 0)}{P(Y = 0 | A = 1, L = 0)}
$$

!!! warning "Selection bias and hazard ratio"
    **Hazards** is defined as the probability of a participant to die at a certain time. Following the definition of risk, the hazard ratio is the same as risk ratio. Consider the following causal graph.

    {{ latex_image('imgs/8-hazard-ratio.tex') }}

    In the graph, treatment $A$ denote the heart transplant. The outcome $Y_1$ and $Y_2$ denote the death of the patient. Unmeasured variable $U$ affect the overall death rate of the patient. For each time, we can define the associational hazard ratio as

    $$
    \begin{aligned}
        aRR_{AY_1} &= \frac{P(Y_1 = 1 | A = 1)}{P(Y_1 = 1 | A = 0)} \\
        aRR_{AY_2} &= \frac{P(Y_2 = 1 | A = 1)}{P(Y_2 = 1 | A = 0)}
    \end{aligned}
    $$

    However, we can only measure the hazard ratio among the patients who are still alive at that time, that is:

    $$
    aRR_{AY_2 \mid Y_1 = 0} = \frac{P(Y_1 = 1 | A = 1, Y_1 = 0)}{P(Y_1 = 1 | A = 0, Y_1 = 0)}
    $$

    However, condition on $Y_1$ opens a trail $A \ra Y_1 \la U\ra Y_2$. Therefore, unless $U$ is measured, from the data collected we cannot distinguish the existence of the path $A \ra Y_2$.

## Selection without Bias

Selection will cause bias within the study, but in some cases such bias can be restricted to some strata of the study. Consider the following causal graph. $Y = 0$ if and only if $Y_A = Y_E = Y_O = 0$.

{{ latex_image('imgs/8-multiplicative-survival-model.tex') }}

1. $Y = 0$ is equivalent to $Y_A = 0$ and $Y_E = 0$. In such case, $A$ is independent of $E$.
2. Consider the case when $Y = 1$ and $Y_O = 0$, then $Y_A = 0$ indicates $Y_E = 1$ and vice versa. In such case, $A$ is dependent of $E$.

## Adjustment for Selection Bias

Assume that positivity holds for $C = 0$ and consistency holds for the analysis. Selection bias arises when the participants are not randomly removed from the study, causing the distribution of remaining participants to be different from the original population, i.e. the joint distribution $P'(A, L) = P(A, L | C = 0)$ is no longer identical to $P(A, L)$.

Selection bias is often unavoidable. IP weighting and standardization can be used to adjust for selection bias. The inverse probability weight $W^C$ is defined as

$$
W^C = \frac{1}{P(C = 0 | \cdot)}
$$

where $\cdot$ denote all the variable that directly affects $C$. Since we can only observed variables for uncensored ($C = 0$) individuals, the IP weight only uses $C = 0$. IP weighting assigns different weight to the probability distribution of each pair of $(A, L)$, so that the distribution of the weighted sample is identical to the original population.

$$
\begin{aligned}
&&& \frac{P(A = a, L = l, C = 0)}{P(C = 0 | A = a, L = l)} \\
&=&& \frac{P(A = a, L = l, C = 0)}{P(A = a, L = l, C = 0) / P(A = a, L = l)} \\
&=&& P(A = a, L = l)
\end{aligned}
$$

!!! warning "Difference in confounding bias and selection bias"
    In confounding bias, IP weighting is applied on the treatment variable $A$, while in selection bias, IP weighting is applied on the censoring variable $C$.

When there are measured variable $L$ on the trail through $C$ that is able to block the trail causing selection bias, we can use stratification to adjust for selection bias by conditioning on $L$.