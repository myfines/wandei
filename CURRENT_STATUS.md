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

A sharper numerical ceiling is about `2^71.413083842`.

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

`src/unit_excursion_cert.py` exhausts the first-46 defect paths with `h in {0,1}` and at most two `0->1` upcrossings:

- exactly one upcrossing: `609` scripts;
- exactly two: `56,405` scripts;
- total nontrivial class: `57,014` scripts;
- exact seed-window survivors: `4,872` integers;
- all descend below themselves, latest at odd-only step `145`.

Thus a survivor must, within the first 46 odd steps, either reach `h>=2` or make at least three unit upcrossings.

Candidate-row digest:

`b9dcfee89ca967a162e9d0e7a18e8ce49ccad111b665d3fa765e714ff8989b05`

### Final boundary repayment lies in the last 44 odd steps

Let `m` be the last return to `h=0` before the terminal crossing `h_k=-1` and put `ell=k-m`.

`src/last_boundary_44_cert.py` plus the exact terminal-cylinder analysis excludes every `ell>=45`. Therefore

\[
\boxed{k-m\le44},
\qquad
\boxed{m\ge72057431947}.
\]

So any first-candidate survivor creates positive defect near the beginning but makes its final repayment to the critical boundary only in the last 44 odd-only steps.

### Global boundary-run exclusion: current strongest finite certificate

At every boundary time `h_j=0`, the exact product identity gives

\[
\frac{x_j}{N}
=
\frac{3^j}{2^{A_j}}
\prod_{i<j}\left(1+\frac1{3x_i}\right),
\]

hence throughout the first candidate

\[
\boxed{x_j<3N<2^{73}.}
\]

The current `src/boundary_run_cert.py` excludes a run of 35 consecutive mechanical transitions on the boundary, equivalently it excludes 36 consecutive boundary states.

It enumerates all `36` length-35 mechanical factors and all exact local seed lifts in

\[
2075\cdot2^{60}\le x_j<2^{73}.
\]

Exact counts/results:

- local candidate states: `2,691,480`;
- all fall below the verified frontier;
- latest drop: odd-only step `252`;
- worst local seed: `4683730498974184172651`;
- certificate digest: `a8f4322128bd42e4db3111c8073b7fed59a8b0cf28102988372fb9d08f8cc86b`.

Therefore

\[
\boxed{\text{no first-candidate prefix contains 36 consecutive boundary states}.}
\]

Every maximal boundary run has at most `35` states.

The boundary-density lower bound gives

\[
z=\#\{0\le j<k:h_j=0\}\ge25438346005.
\]

Therefore there are at least

\[
\left\lceil\frac z{35}\right\rceil=726809886
\]

separate boundary runs, and at least

\[
\boxed{726809885}
\]

unit departures `h=0 -> 1`. Every such departure is forced to satisfy

\[
\boxed{r_j=2,\qquad a_j=1.}
\]

### Height-one heavy-return phase gate

If `h_n=1` and `a_n>=3`, the side-branch altitude lemma gives `x_n>4N`, while the correction product satisfies `<65/64`. Hence

\[
\boxed{\theta_n=\{n\log_2 3\}>\log_2(128/65)=0.9776321869\ldots}
\]

is necessary.

Thus a drop `h=1 -> 0` at an `r_n=2` location (which requires `a_n=3`) is possible only in the top roughly `2.24%` of the rotation phase circle. Outside that window, a height-one repayment can occur only at `r_n=1` via `a_n=2`.

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
5. Reciprocal summability in the escape branch is a derived consequence of a quantitative Garcia--Tal orbit-sparsity estimate, not merely of “Banach density zero”; preserve that distinction.

## 5. Best next targets

### Main first-candidate target: excursion-return automaton

A survivor now requires more than `7.26e8` boundary departures. The next target is to classify the compensating returns by height and mechanical phase.

The immediate quantitative question is whether the rotation supplies enough admissible repayment phases once heavy repayments are restricted by altitude. A useful finite-state model should track at least

- defect height `h`;
- mechanical letter `r in {1,2}`;
- phase window membership for heavy repayment;
- exact valuation excess `a-r`.

The goal is to turn the huge excursion count into a contradiction with the available phase/altitude budget, before invoking the more complicated sampled prime-turnover machinery.

### Secondary arithmetic bridge

If the phase/altitude budget alone is insufficient, combine forced excursions with sampled mod-9 turnover:

- departures force `a=1` at definite phases;
- returns require compensating excess valuation;
- primes `p>7` cannot persist in adjacent sampled cofactors;
- recycled primes obey multiplicative-order clocks for `3/2 mod p`.

### Escape branch

The missing theorem remains a bad-prime-concentration exclusion compatible with `h_k->infinity` and `sum 2^{-h_k}<infinity`.

## 6. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-01-boundary-run-exclusion.md`
3. `notes/2026-10-01-last-boundary-within-44.md`
4. `notes/2026-10-01-height-one-heavy-step-phase-gate.md`
5. `notes/2026-10-01-critical-defect-budget.md`
6. `notes/2026-10-01-unit-excursion-certificate.md`
7. `notes/2026-10-01-prime-turnover-clock.md`
8. `notes/2026-09-29-first-contraction-certificate.md`
9. `notes/2026-09-29-critical-defect-coordinate.md`

These reconstruct the current proof state without relying on chat history.
