# CURRENT STATUS — recovery checkpoint

Updated: 2026-10-01

This file is the compact recovery point for future chats/agents. The repository contains partial results and exact finite certificates only; there is **no claimed proof of Collatz**.

## 1. Main coordinate and branch split

Use the odd-only Syracuse map

\[
S(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
\]

Assume for contradiction that a least positive counterexample `N` exists. Write

\[
a_j=v_2(3x_j+1),\qquad A_k=\sum_{j<k}a_j,
\]

and

\[
h_k=\lfloor k\log_2 3\rfloor-A_k.
\]

Let

\[
r_k=\lfloor(k+1)\log_2 3\rfloor-\lfloor k\log_2 3\rfloor\in\{1,2\}.
\]

Then the exact defect recurrence is

\[
\boxed{h_{k+1}=h_k+r_k-a_k.}
\]

Two main branches remain.

### A. First coefficient-contraction branch

Before the first contraction, `h_k>=0`. Continued-fraction / Denjoy--Koksma analysis isolates the first relevant candidate

\[
(k,A_k)=(72057431991,114208327604).
\]

Combining the live computational lower frontier with the correction ceiling gives the narrow seed interval

\[
\boxed{2075\cdot2^{60}\le N<\frac43\,2^{71}.}
\]

A sharper numerical ceiling is about `2^71.413083842`, but the clean rational certificate above is the committed rigorous bound.

The critical-defect budget shows that any survivor at this first candidate must spend more than about 35.3% of the pre-contraction times exactly on the boundary `h_j=0`.

### B. Escape branch

If the multiplicative coefficient never contracts, then `h_k>=0` for all `k`. For a genuinely divergent orbit, reciprocal/correction summability gives

\[
\boxed{h_k\to+\infty,\qquad \sum_k2^{-h_k}<\infty.}
\]

The remaining problem is arithmetic realizability of such a sparse-defect path by one positive integer seed.

## 2. Latest exact finite progress in branch A

### Pure mechanical prefix

For the first 46 odd-only steps, the mechanical word has

\[
A_{46}=72.
\]

The exact seed congruence for this word gives

\[
N_{\rm mech}=4697939311072332635131,
\]

which lies above the first-candidate upper window. Therefore a first-candidate survivor cannot remain on `h=0` for all first 46 steps.

### Unit-excursion certificate

`src/unit_excursion_cert.py` exhausts the first 46-step defect paths satisfying

- `h_j in {0,1}`;
- at most two upcrossings `0->1`;
- between state changes the valuation equals the fixed mechanical letter.

Exact counts:

- exactly one upcrossing: `609` scripts;
- exactly two upcrossings: `56,405` scripts;
- total nontrivial class: `57,014` scripts.

Intersecting their exact seed residue classes with

\[
2075\cdot2^{60}\le N<\frac43\,2^{71}
\]

leaves only `4,872` concrete integer seeds. Every one is checked directly and falls below itself; the latest first descent is odd-only step `145`.

Therefore any first-candidate survivor must satisfy

\[
\boxed{
\text{within the first 46 odd steps, either }h\ge2
\text{ or there are at least three unit upcrossings.}
}
\]

Candidate-row digest:

`b9dcfee89ca967a162e9d0e7a18e8ce49ccad111b665d3fa765e714ff8989b05`

## 3. Sampled mod-9 / prime-support structure

For consecutive sampled `2 mod 9` returns, the normalized transition can be written

\[
3^{q_j}s_j+\eta_{j+1}=2^{t_{j+1}}s_{j+1},
\qquad \eta_j\in\{3,15,63\}.
\]

Exact consequences already committed:

- adjacent large-prime support turns over:
  \[
  \gcd(s_j,s_{j+1})\mid\eta_{j+1},
  \]
  so primes `p>7` cannot divide consecutive cofactors;
- two-step recycling forces a discrete-log / multiplicative-order congruence for `3/2 mod p`;
- for bounded sampled odd-run lengths `q_j`, `P`-smooth cofactors have density zero for every fixed `P` (S-unit finiteness argument);
- hence a hypothetical sampled escape tail has a dichotomy: unbounded spike lengths, or density-one refresh by increasingly large prime factors.

This is structural progress, not yet a contradiction.

## 4. Important dead ends / cautions

Do not restart these as if they were untested:

1. A universal local exponential lower bound on endpoint residues is false. Small residues can survive long local scripts because the path may pass through a smaller intermediate value; global least-counterexample minimality must be included.
2. Pure mechanical / Sturmian shadowing alone is insufficient. Positive integer seeds can shadow critical 2-adic scripts for long finite times.
3. Multiplicative-order results for generic primes do not immediately apply because orbit-generated primes could concentrate on exceptional small-order sets.
4. Finite computation alone is not a Collatz proof unless converted into a finite certificate covering a mathematically complete class.

## 5. Best next targets

### Immediate finite extension

Extend `unit_excursion_cert.py` to exactly three upcrossings while keeping `h in {0,1}`. There are about 1.9 million such first-46 scripts, so this is still computationally realistic, but it is secondary to the theoretical bridge below.

### Main theoretical bridge: boundary-return compression

The first-candidate defect budget forces >35.3% boundary contacts `h_j=0`. A useful next lemma should exploit **returns to the boundary**, not just their density.

At a boundary return of length `m`,

\[
A_m=\lfloor m\log_2 3\rfloor,
\]

and the exact odd-prefix congruence fixes the seed modulo

\[
2^{A_m+1}.
\]

For `m>=46`, this modulus is already larger than the entire first-candidate seed window. Thus each realized boundary-return word determines at most one seed in that window.

The desired compression theorem is roughly:

> repeated boundary returns of a least-counterexample prefix cannot keep producing admissible unique seeds while simultaneously satisfying the sampled mod-9 prime-turnover constraints and the correction budget.

A successful version of this lemma would convert the 35.3% boundary-density statement into a global contradiction and could close the first coefficient-contraction branch without enumerating arbitrary high-defect paths.

### Escape branch target

For the no-contraction branch, combine

\[
h_k\to\infty,\quad \sum2^{-h_k}<\infty
\]

with the sampled prime-refresh dichotomy. The missing theorem is a bad-prime-concentration exclusion: an orbit should not be able to refresh almost all large prime support from primes with anomalously small `ord_p(3/2)` while also satisfying the critical-drift/correction constraints.

## 6. Files to read first after context loss

1. `CURRENT_STATUS.md` (this file)
2. `notes/2026-09-29-first-contraction-certificate.md`
3. `notes/2026-10-01-critical-defect-budget.md`
4. `notes/2026-10-01-first-46-mechanical-exclusion.md`
5. `notes/2026-10-01-unit-excursion-certificate.md`
6. `notes/2026-10-01-prime-turnover-clock.md`
7. `notes/2026-09-29-critical-defect-coordinate.md`

These reconstruct the current proof state without relying on chat history.
