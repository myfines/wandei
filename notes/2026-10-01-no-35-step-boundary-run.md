# No 35 consecutive critical-boundary steps in a first-candidate survivor

Status: finite exact certificate inside the first coefficient-contraction candidate. Not a proof of Collatz.

Let

\[
h_n=\lfloor n\log_2 3\rfloor-A_n.
\]

Whenever `h_n=0` for a consecutive block, the Syracuse exponents on that block are exactly a finite factor of the critical mechanical word

\[
a_j=\lfloor(j+1)\log_2 3+\rho\rfloor-\lfloor j\log_2 3+\rho\rfloor
\in\{1,2\}
\]

for an appropriate intercept `rho`.

The script `src/zero_run_35_cert.py` gives a complete finite certificate for length 35.

## 1. There are only 36 mechanical factors

A Sturmian/mechanical word has factor complexity `n+1`. Using rigorous rational intervals for `log 2` and `log 3`, the script constructs all endpoints of the intercept partition and certifies exactly

\[
\boxed{36}
\]

distinct exponent words of length 35.

## 2. The starting state lies in a uniform finite band

For every `h=0` state in the first candidate,

\[
N_0\le x<\frac{65}{32}N
<\frac{65}{24}2^{71},
\]

where

\[
N_0=2075\,2^{60}.
\]

For each of the 36 exponent factors, oddness of the terminal Syracuse state fixes the starting integer to one residue class modulo `2^(A+1)`. Enumerating every representative of those residue classes in the larger phase-independent band above produces exactly

\[
\boxed{1,527,532}
\]

integer candidates.

This deliberately over-counts the actual candidate set because it ignores the precise rotation phase.

## 3. Every candidate descends below the verified floor

Each of the 1,527,532 integers is then iterated with exact integer odd-only Syracuse arithmetic. Every one falls below

\[
N_0=2075\,2^{60}.
\]

The longest such descent takes at most

\[
\boxed{252}
\]

odd-only steps. The certificate records the seed attaining the maximum checked descent time as

`4683730498974184172651`.

But every state on the orbit of a least counterexample `N>=N0` is itself a counterexample and therefore can never fall below `N`, hence certainly never below `N0`.

Therefore none of these realizers can occur on a first-candidate counterexample orbit.

## Conclusion

\[
\boxed{\text{A first-candidate survivor cannot have }35\text{ consecutive states with }h=0.}
\]

Thus every block of 35 preterminal odd-only steps contains at least one strictly positive critical defect:

\[
\boxed{\max(h_j)>0\text{ in every length-35 window before the terminal crossing}.}
\]

Combined with the separate result that the final repayment occurs within the last 44 steps, this forces positive-defect events throughout the entire roughly 72-billion-step candidate prefix rather than only near its two ends.

The immediate quantitative consequence is a positive lower density of defect times. By itself that density is not yet large enough to eliminate the first candidate through the affine-correction bound; further local exclusion of low-height defect excursions is still needed.