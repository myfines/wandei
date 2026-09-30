# Finite exclusion of the first two unit critical-defect excursions

Status: exact finite certificate inside the first coefficient-contraction window. This is not a proof of the Collatz conjecture.

Work with the odd-only Syracuse map

\[
x_{j+1}=\frac{3x_j+1}{2^{a_j}},\qquad a_j=v_2(3x_j+1),
\]

and the critical-defect coordinate

\[
h_j=\lfloor j\log_2 3\rfloor-A_j,
\qquad
A_j=\sum_{i<j}a_i.
\]

Let

\[
r_j=\lfloor (j+1)\log_2 3\rfloor-\lfloor j\log_2 3\rfloor\in\{1,2\}.
\]

Then exactly

\[
h_{j+1}=h_j+r_j-a_j.
\]

The earlier 46-step mechanical exclusion handled the path `h_j=0` throughout the first 46 odd-only steps. Here we enlarge the finite class to low-complexity unit excursions with

\[
h_j\in\{0,1\}
\]

and at most two upcrossings `0 -> 1` in the first 46 steps.

For this restricted class the valuation at each step is forced by the transition of `h`:

- stay at the same height: `a_j=r_j`;
- rise `0 -> 1`: necessarily `r_j=2` and `a_j=1`;
- return `1 -> 0`: `a_j=r_j+1`.

Thus this is a complete enumeration of the stated defect class, not a sample.

## One-excursion count

Among the first 46 mechanical letters there are exactly 26 positions with `r_j=2`.

A single unit excursion can either remain open through step 46, giving 26 scripts, or return at a later step. Summing the possible return positions gives 583 closed scripts. Hence there are exactly

\[
\boxed{26+583=609}
\]

nontrivial one-upcrossing scripts.

## Two-excursion count

Running the same finite two-state automaton while allowing a second `0 -> 1` upcrossing gives exactly

\[
\boxed{56,405}
\]

scripts with exactly two upcrossings.

Together with the one-upcrossing class, this gives

\[
\boxed{57,014}
\]

nontrivial prefixes.

The enumeration is reproduced by `src/unit_excursion_cert.py` using exact integer arithmetic only.

## Exact seed congruence

For any fixed valuation word of length `n`, define

\[
d_0=0,\qquad d_{m+1}=3d_m+2^{A_m}.
\]

Then

\[
2^{A_n}x_n=3^nN+d_n.
\]

Requiring the endpoint to be odd fixes the starting seed modulo `2^(A_n+1)`:

\[
\boxed{
N\equiv 3^{-n}(2^{A_n}-d_n)\pmod{2^{A_n+1}}.
}
\]

We intersect each exact residue class with the first-contraction candidate interval

\[
2075\cdot2^{60}\le N<\frac43\,2^{71}.
\]

For the 609 one-upcrossing scripts, only

\[
\boxed{49}
\]

concrete integer seeds survive this intersection.

For the 56,405 exactly-two-upcrossing scripts, only

\[
\boxed{4,823}
\]

concrete integer seeds survive.

Hence the complete low-complexity class contains only

\[
\boxed{4,872}
\]

candidate seeds inside the narrow first-contraction interval.

## Direct minimality check

For every one of these 4,872 concrete seeds, the script recomputes the actual odd-only Syracuse trajectory, verifies that its first 46 valuations equal the enumerated word, and then searches for the first state below the starting seed.

Every candidate descends below itself.

The latest first descent occurs at odd-only step

\[
\boxed{145}.
\]

The corresponding seed is

\[
\boxed{2671106144283589295099}.
\]

Therefore none of these 57,014 defect scripts can be the prefix of a least counterexample in the first-contraction candidate window.

Equivalently,

\[
\boxed{
\text{any surviving first-candidate prefix must either reach defect height }\ge2
\text{ within 46 steps, or make at least three unit upcrossings.}
}
\]

For reproducibility, the sorted candidate/descent rows have SHA-256

`b9dcfee89ca967a162e9d0e7a18e8ce49ccad111b665d3fa765e714ff8989b05`.

## What remains

This is a genuine strengthening of the pure mechanical exclusion, but it is still a finite low-complexity certificate rather than a proof of Collatz.

The next natural finite target is the three-upcrossing `h in {0,1}` class. More importantly, a general argument must also control prefixes that reach `h>=2`, where the number of symbolic defect paths grows quickly. The existing defect-budget lemma says a first-candidate survivor must spend a positive proportion of its enormous pre-contraction lifetime exactly on the boundary `h=0`; the useful next bridge is therefore to combine repeated boundary returns with exact seed congruences rather than enumerate unrestricted paths blindly.
