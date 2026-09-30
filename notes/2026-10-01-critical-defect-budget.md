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

The mechanical/critical ceiling correction is

\[
\boxed{d_k^{\max}=\sum_{j<k}w_j,}
\]

attained exactly when every `e_j=0`.

Since

\[
w_j=3^{k-1}2^{-\{j\log_2 3\}},
\]

every weight lies in

\[
\frac12\,3^{k-1}<w_j\le3^{k-1}.
\]

Thus

\[
R:=\frac{d_k}{d_k^{\max}}
\]

is a weighted average of `2^{-e_j}` with weights varying by less than a factor of two.

## Exact rational lower bound for `R`

For the first continued-fraction candidate

\[
(k,A_k)=(72057431991,114208327604),
\]

`src/first_contraction_cert.py` constructs an **exact rational** upper bound

\[
U_{\rm mech}=N_{\rm upper}
\]

for the seed that could be rescued by the full mechanical correction ceiling. Its decimal size is

\[
N_{\rm upper}
=1.3315289921697844762\ldots\,2^{71},
\]

corresponding to binary logarithm about `71.4130838415...`. The proof itself does not depend on that decimal representation: `N_upper` is a `Fraction` built from rigorous logarithm intervals and Denjoy--Koksma.

Let

\[
N_0=2075\cdot2^{60}
\]

be the verified lower frontier for a hypothetical counterexample. Since the actual correction is `R d_k^max`, survival requires

\[
N_0<N\le R\,U_{\rm mech},
\]

hence exactly

\[
\boxed{R>\frac{N_0}{N_{\rm upper}}.}
\]

`src/defect_budget_cert.py` evaluates this ratio using rational arithmetic only. Numerically,

\[
\boxed{R>0.76091741126790879209\ldots.}
\]

## Boundary-contact density

Let `z` be the number of times `j<k` with `e_j=0`, and write `p=z/k`.
For fixed `p`, the ratio `R` is maximized by assigning maximal possible weights to zero-defect times, minimal possible weights to positive-defect times, and setting every positive defect equal to one. Therefore

\[
R\le
\frac{p+\frac14(1-p)}{p+\frac12(1-p)}
=
\frac{\frac14+\frac34p}{\frac12+\frac12p}.
\]

Solving gives

\[
\boxed{
p\ge
\frac{R/2-1/4}{3/4-R/2}.
}
\]

Using the exact rational lower bound for `R`, the certificate obtains

\[
\boxed{p>0.35302876193514051414\ldots.}
\]

Therefore the integer number of boundary times satisfies

\[
\boxed{z\ge25438346005.}
\]

So if the first contraction occurs at the first continued-fraction candidate and the seed lies above the verified frontier, more than **35.3%** of all preceding odd-step prefix times must lie exactly on the critical ceiling

\[
\boxed{A_j=\lfloor j\log_2 3\rfloor.}
\]

## Combination with the boundary-run certificate

The independent finite certificate `src/boundary_run_cert.py` proves that no maximal boundary run can contain more than 35 consecutive boundary states.

Hence at least

\[
\left\lceil\frac{25438346005}{35}\right\rceil
=
726809886
\]

separate boundary runs are required.

Between consecutive runs the path must leave `h=0`, and the recurrence

\[
h_{j+1}=h_j+r_j-a_j
\]

shows that an upward departure from zero is possible only via

\[
r_j=2,\qquad a_j=1,\qquad 0\to1.
\]

Thus the first-candidate survivor would require at least

\[
\boxed{726809885}
\]

unit critical-defect upcrossings before its first coefficient contraction.

## Interpretation

The deficit from the ideal mechanical correction is paid multiplicatively:

- `e_j=0` contributes full weight;
- `e_j=1` contributes only half;
- `e_j=2` contributes only one quarter;
- and so on.

The combination of the exact correction budget and the local boundary-run certificate therefore forces a hypothetical survivor to oscillate away from and back to the mechanical boundary more than 726 million times.

This is still not a Collatz proof. The next useful target is to combine those forced excursions with an independent arithmetic restriction, most plausibly the sampled mod-9 prime-turnover/recycling structure.
