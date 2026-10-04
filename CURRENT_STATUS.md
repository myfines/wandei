# CURRENT STATUS — recovery checkpoint

Updated: 2026-10-04

This repository contains partial results and exact finite certificates only. There is **no claimed proof of Collatz**.

## 1. Coordinates

Use the odd-only Syracuse map

`S(x)=(3x+1)/2^a`, `a=v2(3x+1)`.

Write

`A_k=sum_{j<k} a_j`,

`h_k=floor(k log_2 3)-A_k`,

`r_k=floor((k+1)log_2 3)-floor(k log_2 3) in {1,2}`,

so

`h_{k+1}=h_k+r_k-a_k`.

Assume a least positive counterexample exists.

## 2. Important external-theorem erratum

The previously imported Ansari (2025) Proposition 3.2 / Remark 3.1 frontier extension is **not currently accepted as proved** in this repository.

A 2026-09 independent audit gives an exact failure in the Lemma 3.1 sieve induction: already at `n=1`, inside `0<=k<9`, the claimed equality `F_{n+1}=F'_n\A'` fails because `11` lies in the displayed left side but not in `F_2`.

Therefore the claim that verification below `2^71` automatically extends to `4*3^44+2` is retracted. See

`notes/2026-10-04-erratum-ansari-frontier-import.md`.

`src/ansari_frontier_bridge_cert.py` is only a conditional arithmetic comparison. The files based on the stronger floor `4*3^44+2` are conditional/inactive until that floor is independently established.

## 3. Active finite-contraction route: first candidate OPEN

The first isolated continued-fraction candidate remains

`(A,k)=(114208327604,72057431991)`.

`src/first_contraction_cert.py` gives the rigorous seed ceiling

`N < (4/3)*2^71`,

with a sharper mechanical ceiling near `2^71.413083842`.

The last independently recorded live Barina floor used by the repository is

`N >= 2,175,975,677 * 2^40`.

`src/live_frontier_upgrade_cert.py` propagates that floor through the first-candidate weighted correction argument and gives

- boundary times `z >= 35,260,566,482`;
- clean complete 46-step boundary windows `W >= 35,260,566,218`.

### Local exact structure

Independent exact certificates establish:

- maximal boundary run: at most 29 states;
- positive odd-height direct repayment at `r=2`: at most five events globally;
- translated 39/41/46-step local exclusions across every Sturmian factor;
- every clean 46-step boundary window contains at least four total defect upsteps;
- exact-four class `U4` is excluded;
- exact-four class `U3V1` is excluded by `src/translated_h2_three_u_one_v_cert.cpp` after scanning 832,402,470 scripts and 247,899,900 concrete seed rows.

Let

`G = #{j : h_{j+1}=h_j+1}`.

Every such upstep has the exact local arithmetic form

`r_j=2, a_j=1`.

After the `U3V1` exclusion and exact overlap accounting,

`boxed: G >= 3,191,001,468`.

See `notes/2026-10-03-u3v1-exclusion-and-221-charge.md`.

### Convergent-cycle structure

For the first candidate, with

`qU=6,586,818,670`, `qL=65,470,613,321`,

there are at least 1,134,940,229 boundary-boundary edges under the `qU` shift, and all but at most one are strict decreases of the actual Syracuse state in the certified direction.

This has not yet been converted into a contradiction.

### Important old erratum

Do **not** infer a global non-cheap-excursion fraction from the local `(21)^4` exclusion. Boundary waiting breaks that inference.

## 4. Conditional/inactive second-candidate files

The files

- `src/second_contraction_candidate_cert.py`;
- `notes/2026-10-03-second-contraction-candidate-regime-change.md`

were derived under the stronger floor `N>=4*3^44+2`. Since that floor came from the now-retracted Ansari sieve import, these files are **conditional diagnostics only** and are not part of the active unconditional proof chain.

Their arithmetic may still be useful if an independent proof of that stronger frontier is found.

## 5. Genuine no-contraction escape route — OPEN

If coefficient contraction never occurs, then

`h_k>=0` for all k.

For a genuinely divergent orbit the current internal argument gives

`h_k -> +infinity`,

`sum_k 2^(-h_k) < infinity`.

For consecutive sampled `2 mod 9` returns,

`3^{q_j}s_j + eta_{j+1} = 2^{t_{j+1}}s_{j+1}`,

`eta_j in {3,15,63}`.

Committed consequences include:

- primes `p>7` cannot divide consecutive sampled cofactors;
- two-step recycling forces a discrete-log / multiplicative-order clock for `3/2 mod p`;
- fixed-gap recycling forces recycled `p>7` to divide an explicit correction integer `D_{j,m}`;
- bounded sampled odd-run lengths imply fixed-P smooth cofactors have density zero;
- the escape tail faces an unbounded-spike / density-one prime-refresh dichotomy.

GRH is not currently the missing key; the unresolved issue is deterministic concentration of orbit-generated prime factors.

## 6. Current main targets

1. **First-candidate global upper bound:** convert the forced `G>=3,191,001,468` exact `r=2,a=1` events into a conflicting upper bound using phase/correction structure.
2. **Multi-convergent descent graph:** combine more than one continued-fraction shift and seek a density-forced directed cycle of strict state-decrease edges.
3. **Weighted correction optimization:** optimize the full defect-weight distribution instead of only boundary density; a dual finite-state/LP certificate is the preferred conceptual target.
4. **Escape route:** continue the unbounded-spike versus bounded-run prime-refresh split.
5. **External frontier:** only use new verification-frontier extensions after independent proof/audit; do not reuse the retracted Ansari sieve propagation.

## 7. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-04-erratum-ansari-frontier-import.md`
3. `src/first_contraction_cert.py`
4. `src/live_frontier_upgrade_cert.py`
5. `notes/2026-10-03-u3v1-exclusion-and-221-charge.md`
6. `notes/2026-10-01-convergent-cycle-boundary-edges.md`
7. `notes/2026-10-01-convergent-boundary-drift.md`
8. `notes/2026-10-01-prime-turnover-clock.md`
9. `notes/2026-10-02-grh-diagnostic.md`

These reconstruct the active unconditional state without relying on chat history.