# Current proof state — 2026-10-01

Recovery checkpoint for the first coefficient-contraction branch. This is research progress, not a Collatz proof.

## Fixed candidate

The first surviving coefficient-contraction candidate is

\[
(k,A_k)=(72057431991,114208327604),
\]

with

\[
N_0=2075\cdot2^{60}\le N<\frac43\,2^{71},
\]

and critical defect

\[
h_n=\lfloor n\log_2 3\rfloor-A_n,
\qquad h_n\ge0\ (n<k),\quad h_k=-1.
\]

## Hard exact results now available

1. **Initial 46-step exclusion.** The pure critical mechanical exponent word cannot occupy the first 46 odd-only steps. Therefore a positive defect is created within the first 46 steps.

2. **Last repayment rigidity.** After the final return to `h=0`, the exponent suffix is completely fixed: mechanical until the terminal step, whose exponent is mechanical plus one.

3. **Final repayment is very late.** Exact cylinder arithmetic proves the last return to `h=0` occurs within the final 44 odd-only steps:

\[
\boxed{k-m\le44.}
\]

4. **No long boundary plateau.** Exact exhaustive enumeration of all 36 length-35 critical mechanical factors, comprising 1,527,532 integer realizers in an over-approximating admissible band, shows every realizer falls below the verified floor `N0` within at most 252 odd-only steps. Hence

\[
\boxed{\text{there are no 35 consecutive preterminal states with }h=0.}
\]

5. **Height-one heavy repayment gate.** If `h_n=1` and `a_n>=3`, then the side-branch altitude bound forces

\[
\boxed{\{n\log_2 3\}>\log_2(128/65)=0.9776321869\ldots.}
\]

Thus heavy repayment from defect height one is restricted to a tiny rotation-phase window.

6. **External floor rechecked.** The live Barina verification page still supports `N0=2075*2^60` as the current complete floor.

## Current obstacle

The first candidate is not eliminated. The surviving regime must contain positive defects throughout the roughly 72-billion-step prefix, but these defects may occur as frequent short low-height excursions. The crude density consequence of the no-35-boundary-run theorem is far too weak to reduce the affine correction enough by itself.

The next target is therefore the **low-height excursion language**, especially paths with `h in {0,1}`. These admit an exact weighted-subset-sum normal form and may be attacked by finite-state / modular dynamic programming rather than exponential word enumeration.

## Persistence rule

Every reusable lemma, exact computational certificate, failed route, corrected bound, or verifier code is committed separately. On context recovery, read this file and the newest commits before continuing.