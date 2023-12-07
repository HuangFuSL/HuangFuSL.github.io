# Measurement bias and "noncausal" diagrams

## Measurement Bias

Measurement bias is caused by errors in measuring values of variables, i.e. $A^* \not = A$. **Measurement error** is defined as the difference between the measured value and the true value of a variable, $e_A = A^* - A$. Taken measurement error into consideration, the causal diagram is modified as follows:

{{ latex_image('imgs/9-measurement-bias.tex') }}

Measurement error follow two properties:

1. **Indepedence**: $e_A \perp e_Y$.
    {{ latex_image('imgs/9-independence.tex') }}
2. **Nondifferentiality**: $e_A \perp Y$ and $e_Y \perp A$.
    {{ latex_image('imgs/9-nondifferentiality.tex') }}

Lack of either property will bring extra association and lead to bias.

* Edge $Y\ra U_A$ will introduce **recall bias**.
* Edge $A\ra U_Y$ will introduce **reverse causation bias**.
* Edge $U_A\la U_{AY}\ra U_Y$ will introduce **independent measurement error**.

Correcting for measurement error usually requires additional validated non-biased samples.

## "Noncausal" Diagrams

A causal graph requires that *all* of the edges in the graph can be interpreted causally, together with well-defined intervention. For graphs with non-causal edges, adjustments might fail to remove bias, as the adjusted variable is not on the true causal path.

{{ latex_image('imgs/9-noncausal.tex') }}
