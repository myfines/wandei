# No 39 consecutive critical-boundary states in the first candidate

Status: exact finite consequence inside the first coefficient-contraction branch. Not a proof of Collatz.

Let

\[
h_j=\lfloor j\log_2 3\rfloor-A_j,
\qquad
r_j=\lfloor(j+1)\log_2 3\rfloor-\lfloor j\log_2 3\rfloor.
\]

Before the first coefficient contraction, `h_j>=0`. At a boundary time `h_j=0`,

\[
A_j=\lfloor j\log_2 3\rfloor.
\]

For the first continued-fraction candidate

\[
k=72057431991,
\qquad
2075\cdot2^{60}\le N<\frac43\,2^{71}.
\]

## 1. Every boundary state is below `2^73`

The exact product form gives

\[
\frac{x_j}{N}
=
\frac{3^j}{2^{A_j}}
\prod_{i<j}\left(1+\frac1{3x_i}\right).
\]

At a boundary time,

\[
\frac{3^j}{2^{A_j}}=2^{\{j\log_2 3\}}<2.
\]

Because `N` is least and every orbit state satisfies `x_i>=N`,

\[
\prod_{i<j}\left(1+\frac1{3x_i}\right)
<
\exp\left(\frac{j}{3N}\right)
<
\exp(1/3)
<\frac32.
\]

(The middle inequality is extremely loose: `j<k<<N`; and `log(3/2)>1/3` follows from integrating `1/t` on `[1,3/2]`.)

Therefore

\[
\boxed{x_j<3N<2^{73}.}
\]

This uniform bound is the key finite-compression step.

## 2. A long boundary run becomes a local mechanical word

If

\[
h_j=h_{j+1}=\cdots=h_{j+38}=0,
\]

then the next 38 realized valuations are exactly the shifted mechanical word

\[
a_{j+i}=r_{j+i}\qquad(0\le i<38).
\]

For any fixed length-38 mechanical factor `w`, the exact prefix identity fixes the local starting state `x_j` modulo

\[
2^{A(w)+1}.
\]

The length-38 factors of an irrational mechanical word number at most `38+1=39`: as the rotation phase varies, the factor can change only when the phase crosses one of the 39 points `{-m alpha}`, `m=0,...,38`, where `alpha=log_2 3-1`.

The exact mechanical sequence exhibits 39 distinct factors, so these are all possible factors.

## 3. Complete local certificate

`src/boundary_run_cert.py` enumerates all 39 factors using integer `bit_length(3^j)` floors.

For each factor it computes the exact local seed residue and every lift in

\[
2075\cdot2^{60}\le x_j<2^{73}.
\]

There are exactly

\[
\boxed{103,987}
\]

such local candidate states.

For every candidate, the script verifies the exact 38-step valuation word and then iterates the odd-only Syracuse map until the state falls below the verified frontier `2075*2^60`.

All candidates do so. The latest such drop occurs after

\[
\boxed{176}
\]

odd-only steps, from the local state

\[
6801297196994201447531.
\]

The sorted certificate rows have SHA-256

`3cc9c7b8230302f1619609530fa635e31b94d87215caa3c479a8b79137da64f5`.

Hence

\[
\boxed{
\text{a first-candidate least-counterexample prefix cannot contain 39 consecutive times with }h_j=0.
}
\]

Equivalently, there is no run of 38 consecutive mechanical transitions while staying on the critical boundary.

## 4. Global consequence: hundreds of millions of required excursions

The earlier correction-budget lemma gives, for a first-candidate survivor,

\[
\frac{1}{k}\#\{0\le j<k:h_j=0\}>0.353028761.
\]

Thus the number `z` of boundary times obeys

\[
z\ge25438345937.
\]

Since every maximal boundary run has length at most 38, there must be at least

\[
\left\lceil\frac{z}{38}\right\rceil
=
669430157
\]

separate boundary runs.

Between two consecutive boundary runs the defect path must leave `h=0`. From

\[
h_{j+1}=h_j+r_j-a_j
\]

and `a_j>=1`, leaving zero upward is possible only by the unit move

\[
r_j=2,\qquad a_j=1,\qquad h_j=0\to h_{j+1}=1.
\]

Therefore any surviving first-candidate prefix must contain at least

\[
\boxed{669430156}
\]

unit upcrossings `0->1` before the first coefficient contraction.

This is a substantial strengthening of the earlier statement that at least one defect must occur in the first 46 steps. A hypothetical survivor is forced to oscillate away from and back to the critical boundary hundreds of millions of times.

## 5. Next bridge

The remaining task is to turn this massive excursion count into an arithmetic contradiction. The most promising combination is with the sampled mod-9 / prime-turnover structure:

- each boundary departure is a forced `a=1` event at a fixed mechanical phase;
- each return requires compensating excess valuation;
- sampled cofactors cannot retain any prime `p>7` across consecutive returns;
- recycled large primes obey multiplicative-order congruences for `3/2 mod p`.

A useful next theorem would show that more than `6.69e8` critical-boundary excursions cannot be realized while the correction ratio remains high enough for the first candidate and the sampled prime support keeps satisfying the turnover/recycling constraints.
