# Critical first-contraction defect budget

Status: exact algebraic reduction for the first coefficient-contraction candidate; not a Collatz proof.

Work in the odd-only Syracuse map

\[
S(x)=\frac{3x+1}{2^{a}},\qquad a=v_2(3x+1).
\]

Let a prefix have odd-step length `k`, valuation sum

\[
A_j=\sum_{i<j} a_i,
\]

and suppose `k` is the first coefficient-contraction time:

\[
A_j\le j\log_2 3\quad (j<k),
\qquad
A_k>k\log_2 3.
\]

Define the integer critical defect

\[
e_j=\lfloor j\log_2 3\rfloor-A_j\ge0\qquad(j<k).
\]

The exact affine form is

\[
S^k(N)=\frac{3^kN+d_k}{2^{A_k}},
\]

with

\[
d_k=\sum_{j<k}3^{k-1-j}2^{A_j}.
\]

Substituting `A_j=floor(j log_2 3)-e_j` gives

\[
\boxed{
 d_k=\sum_{j<k} w_j 2^{-e_j},
\qquad
w_j=3^{k-1-j}2^{\lfloor j\log_2 3\rfloor}.
}
\]

The mechanical/critical ceiling correction is therefore

\[
\boxed{
 d_k^{\max}=\sum_{j<k}w_j,
}
\]

attained exactly when every `e_j=0`.

Because

\[
3^j=2^{j\log_2 3},
\]

we also have

\[
w_j=3^{k-1}2^{-\{j\log_2 3\}},
\]

so every weight lies in the fixed interval

\[
\frac12\,3^{k-1}<w_j\le 3^{k-1}.
\]

Thus the ratio

\[
R:=\frac{d_k}{d_k^{\max}}
\]

is a weighted average of `2^{-e_j}` with weights varying by less than a factor of two.

## Consequence from the current verification frontier

For the first continued-fraction candidate

\[
(k,A_k)=(72057431991,114208327604),
\]

our rigorous Denjoy--Koksma mechanical ceiling gives

\[
N<2^{71.413083842}
\]

whenever this first coefficient contraction is still rescued by the `+1` correction.

The current Barina verification frontier is

\[
N>2075\cdot 2^{60},
\]

for any hypothetical counterexample. Hence any surviving first-candidate script must satisfy

\[
R>
\frac{2075\cdot2^{60}}{2^{71.413083842}}
=0.760917411\ldots.
\]

Let `z` be the number of times `j<k` with `e_j=0`, and write `p=z/k`.
For fixed `p`, the ratio `R` is maximized by assigning maximal possible weights to zero-defect times, minimal possible weights to positive-defect times, and setting every positive defect equal to one. Therefore

\[
R\le
\frac{p+\frac14(1-p)}{p+\frac12(1-p)}
=
\frac{\frac14+\frac34p}{\frac12+\frac12p}.
\]

Solving for `p` gives

\[
\boxed{
p\ge
\frac{R/2-1/4}{3/4-R/2}.
}
\]

At `R=0.760917411...`,

\[
\boxed{p>0.353028761.}
\]

So if the first contraction occurs at the first continued-fraction candidate and the seed lies above the current verification frontier, then at least about **35.3%** of all preceding odd-step prefix times must lie exactly on the critical ceiling

\[
\boxed{A_j=\lfloor j\log_2 3\rfloor.}
\]

This is substantially stronger than merely requiring near-critical average density.

## Interpretation

The deficit from the ideal mechanical correction is paid multiplicatively:

- `e_j=0` contributes full weight;
- `e_j=1` contributes only half;
- `e_j=2` contributes only one quarter;
- and so on.

Hence a seed above the verified frontier can survive the first critical contraction only if its valuation walk repeatedly returns exactly to the mechanical boundary.

This does **not** by itself force low factor complexity: short defect excursions can still encode high symbolic complexity. The next useful target is therefore to combine frequent boundary contacts with an independent arithmetic restriction (sampled mod-9 dynamics, seed congruence, or p-adic realizability), rather than treating boundary-contact density alone as a proof.