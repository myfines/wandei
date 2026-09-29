# Exact critical-defect coordinate

Status: exploratory lemma / reduction, not a Collatz proof.

Work with the odd-only Syracuse map

\[
x_{k+1}=\frac{3x_k+1}{2^{a_k}},\qquad a_k=v_2(3x_k+1),\qquad A_k=\sum_{i<k}a_i.
\]

Put

\[
L=\log_2 3,\qquad g_k=kL-A_k.
\]

Since `A_k` is an integer,

\[
g_k=h_k+\{kL\},\qquad h_k:=\lfloor kL\rfloor-A_k\in\mathbb Z.
\]

Define the fixed mechanical reference word

\[
r_k:=\lfloor (k+1)L\rfloor-\lfloor kL\rfloor\in\{1,2\}.
\]

Then, exactly,

\[
\boxed{h_{k+1}=h_k+r_k-a_k.}
\]

There is no correction/error term in this recurrence.  All orbit dependence has been moved into the realized valuation `a_k`; `r_k` is a fixed irrational mechanical word determined only by `log_2 3`.

Consequences of `a_k>=1`:

- if `r_k=1`, then `h_{k+1}<=h_k`;
- if `r_k=2`, then `h_{k+1}<=h_k+1`;
- therefore `h` can rise only at `r_k=2`, and by at most one per step.

The exact logarithmic orbit identity is

\[
\log_2(x_k/x_0)=g_k+E_k
=h_k+\{kL\}+E_k,
\]

where

\[
E_k=\sum_{i<k}\log_2\left(1+\frac1{3x_i}\right).
\]

Hence `h_k` is the integer critical-drift coordinate; it differs from the true log-height only by the rigid fractional rotation `{kL}` and the positive correction `E_k`.

## Divergent-orbit summability

For a nonperiodic divergent positive orbit, the Garcia--Tal orbit sparsity estimate implies reciprocal summability (see the provenance notes in the literature review):

\[
\sum_k \frac1{x_k}<\infty.
\]

The standard exact prefix identity gives

\[
\frac{2^{A_k}}{3^k}=2^{-g_k}=2^{-h_k-\{kL\}}.
\]

The same correction identity yields

\[
\sum_k \frac{2^{A_k}}{3^k}<\infty,
\]

so, since `2^{-1} <= 2^{-\{kL\}} <= 1`,

\[
\boxed{\sum_k2^{-h_k}<\infty.}
\]

In particular `h_k -> +infinity` along a divergent orbit.

Thus a hypothetical divergent integer orbit must realize an integer path `h_k` satisfying all of:

1. `h_0=0`;
2. `h_{k+1}=h_k+r_k-a_k` with the fixed mechanical `r_k in {1,2}`;
3. `a_k=v_2(3x_k+1)` is an actually realizable valuation sequence of one positive integer seed;
4. `h_k -> infinity`;
5. `sum 2^{-h_k}<infinity`.

The easy symbolic paths are not automatically realizable.  For example choosing `a_k=1` for every k makes `h_k` grow linearly and satisfies summability, but the all-ones valuation/parity shadow is the 2-adic fixed point `-1`, not a positive integer seed.

This isolates the remaining arithmetic problem as **realizability of a sparse-defect path relative to one fixed critical mechanical word**.

## Bernstein-series interpretation

At the odd-step positions `A_k`, Bernstein's inverse-conjugacy series has terms

\[
\frac{2^{A_k}}{3^{k+1}}=\frac13\,2^{-h_k-\{kL\}}.
\]

For a divergent orbit this series converges in the real absolute value (because `sum 2^{-h_k}<infinity`) while its 2-adic sum represents the positive integer seed.  This is a clean adelic formulation of the surviving case, but by itself is not a contradiction: the real and 2-adic completions can have different limits.

## Research target

Prove that no positive integer can realize a valuation sequence whose critical-defect coordinate satisfies the five conditions above, perhaps by combining:

- finite-defect / word-complexity exclusions;
- 2-adic attainability;
- 3-adic reverse barriers;
- or an adelic / transcendence argument for the Bernstein series.
