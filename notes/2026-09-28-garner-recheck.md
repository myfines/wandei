# 2026-09-28 — Garner bound recheck with the current verification frontier

Status: literature recheck and numerical update. This note does **not** claim a proof of Collatz.

## Garner's criterion

Lynn E. Garner's 1981 coefficient-stopping-time argument introduces, for a cutoff `M`, record measures of how close powers of 2 and 3 approach from below and above. In the notation used by Lionel Laurore (2025), if a start `s` has coefficient stopping time with `r` odd Terras iterates and

\[
r<\min\left\{M,\frac{s}{2}\frac{3^{1-B(M)}}{1-3^{-b(M)}}\right\},
\]

then the ordinary stopping time equals the coefficient stopping time.

Laurore tabulates the record values of `b(M)` and `B(M)` through `M<2e11`. With the older verified range `s<702*2^60`, the paper reports the effective odd-iterate threshold

\[
r<12,289,742,202,
\]

corresponding to about 19.48 billion Terras-map steps.

## Updating only the verified lower bound

David Barina's live verification page currently reports convergence for all

\[
s<2075\,2^{60}.
\]

Using Laurore's tabulated record values, the optimum lies in the interval after the record

\[
M=32,536,519,971,
\]

where, to the six decimals printed in the paper,

\[
b(M)=21.499444,\qquad B(M)=23.043797.
\]

Substituting `s = 2075*2^60` gives

\[
\frac{s}{2}\frac{3^{1-B(M)}}{1-3^{-b(M)}}
\approx36,326,517,190.67.
\]

Thus the direct Garner update gives a uniform coefficient/stopping-time agreement guarantee only through about

\[
\boxed{3.63265\times10^{10}\text{ odd iterates}},
\]

or roughly

\[
\boxed{5.75762\times10^{10}\text{ Terras-map steps}}.
\]

The exact last integer should be recomputed from unrounded `b(M),B(M)` rather than the six-decimal table before being promoted to a theorem-level numerical cutoff.

## Comparison with the crossing-window result in this repository

Our Rozier–Terracol + minimal-counterexample crossing-window argument already forces the first coefficient crossing, if finite, beyond

\[
q=72,057,431,991
\]

odd terms and

\[
j=114,208,327,604
\]

Terras-map steps when using the peer-reviewed `N>2^71` lower bound.

So the currently updated Garner criterion does **not** close the gap. It is weaker here by roughly a factor two in the odd-count variable.

This is useful negative information: simply inserting Barina's newer live verification frontier into the classical Garner theorem will not prove the conjecture or eliminate our first Diophantine crossing candidate.

## Off-by-one correction in a recent table

Laurore's table prints the row

\[
q=72,057,431,991,\qquad n(q)=114,208,327,605.
\]

But high-precision direct evaluation gives

\[
q\log_2 3
=114,208,327,603.9999999999920494\ldots
\]

Hence the first integer exponent above `q log_2 3` is

\[
\boxed{\lceil q\log_2 3\rceil=114,208,327,604}.
\]

This also agrees with the paper's stated formula `n(r)=floor(r log_2 3)+1`. Therefore the `...605` table entry should not be imported into our calculations without an independent reconciliation; it appears to be an off-by-one/table transcription issue.

## Literature links

- L. E. Garner, *On the Collatz 3n+1 Algorithm*, Proc. AMS 82 (1981).
- L. Laurore, *On the Link between Stopping Time and Non-Trivial Cycles in the Collatz Problem*, Advances in Pure Mathematics 15 (2025), 351–389.
- D. Barina, live convergence verification project and 2025 J. Supercomputing paper.

## Next use of Garner

Rather than trying to push the same worst-case Garner sum further, the more promising route is to replace its uniform remainder estimates with the **first-passage-specific remainder geometry** already developed in `notes/2026-09-28-max-first-passage-remainder.md`. That refinement is what produced the much narrower candidate window.
