# CURRENT STATUS — recovery checkpoint

Updated: 2026-10-01

This is the compact recovery point for future chats/agents. The repository contains partial results and exact finite certificates only; there is **no claimed proof of Collatz**.

## 1. Main coordinate and branch split

Use the odd-only Syracuse map

\[
S(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
\]

Assume for contradiction that a least positive counterexample `N` exists. Write

\[
a_j=v_2(3x_j+1),\qquad A_k=\sum_{j<k}a_j,
\]

\[
h_k=\lfloor k\log_2 3\rfloor-A_k,
\]

and

\[
r_k=\lfloor(k+1)\log_2 3\rfloor-\lfloor k\log_2 3\rfloor\in\{1,2\}.
\]

Then exactly

\[
\boxed{h_{k+1}=h_k+r_k-a_k.}
\]

Two branches remain.

### A. First coefficient-contraction branch

Continued-fraction / Denjoy--Koksma analysis isolates the first relevant candidate

\[
(k,A_k)=(72057431991,114208327604).
\]

The clean certified seed window is

\[
\boxed{2075\cdot2^{60}\le N<\frac43\,2^{71}.}
\]

(A sharper numerical ceiling is about `2^71.413083842`.)

The correction-defect budget forces more than `35.3028761%` of the `j<k` times to lie exactly on the critical boundary `h_j=0`.

### B. Escape branch

If the coefficient never contracts, `h_k>=0` for all `k`. For a genuinely divergent orbit, the reciprocal/correction argument gives

\[
\boxed{h_k\to+\infty,\qquad \sum_k2^{-h_k}<\infty.}
\]

The remaining issue is arithmetic realizability of such a path by one positive integer seed.

## 2. Latest exact progress in branch A

### First 46 steps: low-complexity exclusion

The pure 46-step mechanical prefix has `A_46=72` and fixes

\[
N=4697939311072332635131,
\]

which lies above the first-candidate window.

`src/unit_excursion_cert.py` then exhausts the first-46 defect paths with `h in {0,1}` and at most two `0->1` upcrossings:

- exactly one upcrossing: `609` scripts;
- exactly two: `56,405` scripts;
- total nontrivial class: `57,014` scripts;
- exact seed-window survivors: `4,872` integers;
- all descend below themselves, latest at odd-only step `145`.

Thus a survivor must, within the first 46 odd steps, either reach `h>=2` or make at least three unit upcrossings.

Candidate-row digest:

`b9dcfee89ca967a162e9d0e7a18e8ce49ccad111b665d3fa765e714ff8989b05`

### Global boundary-run exclusion

This is the newest and stronger result.

At every boundary time `h_j=0` before the first candidate contraction, the product formula plus the seed window gives

\[
\boxed{x_j<3N<2^{73}.}
\]

If 39 consecutive boundary states occurred, the 38 transitions between them would be a shifted length-38 mechanical word. Such a word has at most `39` possible factors (phase partition of an irrational mechanical word).

`src/boundary_run_cert.py` enumerates all 39 factors, computes every exact local seed lift in

\[
2075\cdot2^{60}\le x_j<2^{73},
\]

and checks all `103,987` concrete local states. Every one falls below the verified frontier; the latest does so after `176` odd-only steps.

Therefore

\[
\boxed{\text{no first-candidate prefix can contain 39 consecutive times with }h_j=0.}
\]

Certificate digest:

`3cc9c7b8230302f1619609530fa635e31b94d87215caa3c479a8b79137da64f5`

Combining this with boundary density > `0.353028761` gives

\[
z=\#\{0\le j<k:h_j=0\}\ge25438345937.
\]

Since each maximal boundary run has length at most `38`, there are at least

\[
669430157
\]

separate boundary runs. Leaving `h=0` upward is possible only via `r_j=2,a_j=1`, so a survivor must contain at least

\[
\boxed{669430156}
\]

unit `0->1` critical-defect excursions before the first contraction.

This converts the former qualitative “a defect must occur” statement into a massive global oscillation requirement.

## 3. Sampled mod-9 / prime-support structure

For consecutive sampled `2 mod 9` returns,

\[
3^{q_j}s_j+\eta_{j+1}=2^{t_{j+1}}s_{j+1},
\qquad \eta_j\in\{3,15,63\}.
\]

Committed exact consequences:

- `gcd(s_j,s_{j+1}) | eta_{j+1}`, so primes `p>7` cannot divide consecutive cofactors;
- two-step recycling forces a discrete-log / multiplicative-order congruence for `3/2 mod p`;
- if sampled odd-run lengths `q_j` are bounded, `P`-smooth cofactors have density zero for every fixed `P` (S-unit finiteness);
- hence an escape tail has a dichotomy: unbounded spikes, or density-one refresh by increasingly large prime factors.

No contradiction has yet been extracted from this structure.

## 4. Important dead ends / cautions

Do not restart these as if untested:

1. A universal local exponential lower bound on endpoint residues is false; global least-counterexample minimality must be included.
2. Pure mechanical/Sturmian shadowing alone is insufficient; positive integers can shadow critical 2-adic scripts for long finite times.
3. Generic multiplicative-order theorems do not automatically control orbit-generated primes, which could concentrate on exceptional small-order sets.
4. Finite computation is useful only when attached to a mathematically complete finite class/certificate.
5. Reciprocal summability in the escape branch is a derived consequence of a quantitative Garcia--Tal orbit-sparsity estimate, not merely of “Banach density zero”; preserve that distinction in future writeups.

## 5. Best next target

The first-candidate branch is now forced to make at least `669,430,156` boundary departures while maintaining a correction ratio high enough to survive.

The next theorem should connect these forced excursions to the sampled arithmetic structure. The desired bridge is roughly:

> hundreds of millions of forced `a=1` boundary departures and compensating returns cannot coexist with the mod-9 prime-turnover / recycling constraints while keeping the first-candidate correction budget.

Promising handles:

- every departure is a forced `r_j=2, a_j=1` event at a definite mechanical phase;
- every return requires compensating excess valuation;
- large primes `p>7` cannot persist across adjacent sampled cofactors;
- recycled primes obey multiplicative-order clocks for `3/2 mod p`;
- the boundary-state bound `x_j<2^73` is uniform throughout the full 72-billion-step first-candidate prefix and may allow additional finite local certificates.

A secondary computational target is to lower the forbidden boundary-run length below 39 states (the length-38 certificate is already exact and fast).

For the escape branch, the missing theorem remains a bad-prime-concentration exclusion compatible with `h_k->infinity` and `sum 2^{-h_k}<infinity`.

## 6. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-09-29-first-contraction-certificate.md`
3. `notes/2026-10-01-critical-defect-budget.md`
4. `notes/2026-10-01-boundary-run-exclusion.md`
5. `notes/2026-10-01-unit-excursion-certificate.md`
6. `notes/2026-10-01-prime-turnover-clock.md`
7. `notes/2026-09-29-critical-defect-coordinate.md`

These reconstruct the current proof state without relying on chat history.
