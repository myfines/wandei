# Quantitative prime-support growth along the sampled mod-9 dynamics

Status: a rigorous consequence of the sampled induced-map equation plus standard S-unit solution bounds. This is not a Collatz proof.

For consecutive sampled returns, write

\[
3^{q_j}s_j+\eta_{j+1}=2^{t_{j+1}}s_{j+1},
\qquad
\eta_{j+1}\in\{3,15,63\},
\]

with `s_j,s_{j+1}` odd.

Divide by the right-hand side:

\[
\boxed{
 x_j+y_j=1,
}
\]

where

\[
x_j=\frac{3^{q_j}s_j}{2^{t_{j+1}}s_{j+1}},
\qquad
y_j=\frac{\eta_{j+1}}{2^{t_{j+1}}s_{j+1}}.
\]

Suppose the first `L` sampled transitions use, across all odd cofactors `s_j`, only `P` distinct odd primes.

Then every `x_j,y_j` is an S-unit over the rational field for a finite set of primes consisting of those `P` odd primes together with at most `2,3,5,7`. Thus there are at most `P+4` finite primes in the relevant set S, plus the archimedean place.

Partition the `L` transitions according to `eta in {3,15,63}`. One eta-class contains at least `L/3` transitions. For fixed eta, the pair `(x_j,y_j)` uniquely determines the sampled state: indeed

\[
y_j=\frac{\eta}{M_{j+1}+\eta}
\]

determines `M_{j+1}`. On an unbounded deterministic orbit the sampled states are distinct, since a repeated sampled state would create a bounded periodic tail.

Hence one eta-class supplies at least `L/3` distinct S-unit solutions of `x+y=1`.

For K=Q, Evertse's classical bound for

\[
ax+by=1
\]

in S-units gives at most

\[
3\,7^{d+2s}
\]

solutions, with `d=1` and `s=#S` including the infinite place. Here `s<=P+5`, so each fixed-eta class has at most

\[
3\,7^{2P+11}
\]

solutions.

Therefore

\[
\frac L3\le 3\,7^{2P+11},
\]

and hence

\[
\boxed{
L\le 9\,7^{2P+11}.
}
\]

Equivalently,

\[
\boxed{
P\ge \frac{\log_7(L/9)-11}{2}.
}
\]

In base 2 this is

\[
\boxed{
P\ge 0.1781035935\,\log_2 L-6.0645751.
}
\]

So every genuinely unbounded sampled trajectory must refresh its odd prime support at least logarithmically often in the number of sampled returns.

## Interpretation

This is a true prime-side constraint. It does **not** say that Collatz convergence is multiplicative, nor that checking prime seeds suffices. Rather, the sampled induced map preserves an odd cofactor across each local `2 -> 3` exchange, and the additive digit `eta in {3,15,63}` is the only place where new odd prime support can be created. If too few primes are ever created, the entire return dynamics is trapped in a fixed S-unit equation, which has only finitely many solutions.

The lower bound is quantitatively weak (only logarithmic), but it is unconditional once the standard S-unit theorem is imported. A next target is to convert support growth into a height/radical cost, or to prove stronger support refresh specifically at long-spike times.