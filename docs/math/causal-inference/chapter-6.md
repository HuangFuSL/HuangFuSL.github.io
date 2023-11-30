# Graphical Representation of Causal Effects

A causal graph consists the following elements:

* **Nodes** in causal graphs represent random variables.
* **Edges** in causal graphs represent *direct* causal effects.
    * A **trail** is a sequence of edges that does not meet the same node twice.
    * A **path** is a trail that all the edges are pointing in the same direction.
* Conventionally, time flows from left to right in causal graphs.
* Causal graphs follow the properties of Bayesian networks (acyclic, markov factorization).

!!! success "Markov Factorization"
    The joint distribution of a set of random variables can be factorized into a product of conditional distributions of each variable **given its parents** in the graph.

    $$
    P(X_1, \dots, X_n) = \prod_{i=1}^n P(X_i \mid \text{Pa}(X_i))
    $$

    where $\text{Pa}(X_i)$ is the set of parents of $X_i$.

    Markov factorization is equivalent to the following **local independence property**:

    $$
    X_i \perp \text{ND}(X_i) \mid \text{Pa}(X_i)
    $$

    where $\text{ND}(X_i)$ is the set of non-descendants of $X_i$.


A causal graph contains the following building blocks: fork, chain, collider.

{{ latex_image('imgs/6-building-blocks.tex') }}

## D-seperation and Independence

Conditional independence relations are encoded in the graph structure.

### Blocked Trails and D-seperation

Trails in causal graphs are regarded as blocked or open according to the following rules:

1. If there are no nodes being observed, a path is blocked if and only if there exists one or more colliders on the path.
2. If the trail contains a non-collider that is observed, the trail is blocked.
3. A collider which is observed does not block the trail.
4. A collider which any of its descendants is observed does not block the trail.

A trail is blocked if it satisfies any of the following conditions:

1. There exists a collider on the trail that itself or all of its descendants are not observed.
2. There exists a non-collider on the trail that is observed.

If all possible trails between two nodes $X, Y$ are blocked $Z$, the two nodes are **d-separated**. D-separated nodes are conditionally independent given the observed nodes, i.e., $X \perp Y \mid Z$.

!!! success "Faithfulness assumption"
    Faithfulness assumptions states that the observed conditional independence relations are consistent with the graph structure. That is: observed conditional independence $X \perp Y \mid Z$ implies that $X$ and $Y$ are d-separated given $Z$ in the graph.

### Flows of Association and Causation

If two nodes are not d-separated, there exists at least one open trail between the nodes.

* Association flows along open trails.
* Causation flows along open paths.

There may be multiple trails and paths between two nodes, each trail provides a *flow* of association or causation. The overall observed association is affected by all the flows of association and causation. Existence of undesired flows of association may lead to lack of exchangeability and **biased** estimation of causal effects. If there are no flow of association between two nodes, the association is causal.

There two types of flows of association:

1. **Common cause**: two nodes are associated because they are both affected by a common cause.

    {{ latex_image('imgs/6-common-cause.tex') }}

2. **Condition on common effect**: two nodes are associated because they are both affecting an observed common effect.

    {{ latex_image('imgs/6-condition-on-common-effect.tex') }}

Blocking a trail can be regarded as blocking the flow of association or causation on the graph.

## Hidden Properties

Causal graphs only encode conditional independence relations and flows of causation or association. Some properties or assumptions cannot be represent in causal graphs.

* **Positivity**: Positivity in causal graphs can be represented that all of the edges in the graph are **not deterministic**.
* **Consistency**: Consistency is implicitly assumed in causal graphs.

In a causal graph, the treatment node should lead to *well-defined* treatment.\
