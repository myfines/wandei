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

The current external Barina project status used by the repository (checked 2026-10-04) has lowest incomplete work unit

`2,175,982,616 * 2^40`.

`src/live_frontier_upgrade_cert.py` propagates this datum through the first-candidate weighted correction argument and gives

- boundary times `z >= 35,260,917,543`;
- clean complete 46-step boundary windows `W >= 35,260,917,279`.

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

Every such upstep has exact local form

`r_j=2, a_j=1`.

After the `U3V1` exclusion and exact overlap accounting, the current live floor gives

`boxed: G >= 3,191,033,238`.

The governing exact charge is `221G>=20W`.

### Convergent-cycle structure

For the first candidate, with

`qU=6,586,818,670`, `qL=65,470,613,321`,

there are at least 1,134,940,229 boundary-boundary edges under the `qU` shift, and all but at most one are strict decreases of the actual Syracuse state in the certified direction.

Multiple continued-fraction shifts can be encoded as chords in the qU-cycle via their Farey determinants. This is structurally interesting, but the induced descent directions largely follow the rotation phase potential, so a direct multi-shift cycle contradiction has not yet been obtained.

### Important old erratum

Do **not** infer a global non-cheap-excursion fraction from the local `(21)^4` exclusion. Boundary waiting breaks that inference.

## 4. New mod-27 bridge from first-candidate boundary density

Monks--Monks--Monks--Monks (Discrete Mathematics 313(4), 2013) prove that every divergent positive shortcut-T orbit and every nontrivial positive cycle hits `20 mod27`. An independently reconstructed exact rank gives the stopped statement: every positive input reaches `1`, `2`, or `20 mod27`.

### Normalized target recurrence

At a target hit `n==20 mod27`, write sampled `M=4n+1=9u`; then `u==9 mod12` and `27|M`.

Removing the exact 3-adic factor from the old digits `{3,15,63}` normalizes them to

`a in {1,5,7}`.

For adjacent target-to-target sampled returns the normalized cofactors satisfy

`3^Q c + a = 2^t c'`,

with `Q>=1`, `3 not|cc'`, and

`gcd(c,c') | a`.

Thus the old adjacent shared-prime exceptional set `{3,5,7}` shrinks to `{5,7}`; the digit `a=1` forces complete coprimality.

See `notes/2026-10-04-mod27-normalized-prime-turnover.md`.

### Every target departure strictly contracts

A sampled target departure occurs exactly when `q+b=2`. The only lanes are

- `eta=3`: `u'=(3u+1)/2^t`, `t in {2,3}`;
- `eta=15`: `u'=(3u+5)/2^t`, `t in {4,5}`;
- `eta=63`: `u'=(u+7)/64`.

Hence every target departure satisfies

`u'<u`,

with principal coefficient at most `3/4`.

See `src/mod27_target_departure_cert.py` and `notes/2026-10-04-mod27-target-departure-contraction.md`.

### Boundary contacts force millions of target hits

Every first-candidate boundary state satisfies

`x < 6,287,967,883,654,920,544,295 < 2^73`.

Combining this altitude with the exact Monks rank gives a uniform shortcut hitting bound

`H=1268`:

- divisible-by-3 phase: at most 73 steps;
- core phase: at most 1117 steps, using exact contraction `20/21`;
- residue26/13 phase: at most 78 steps.

A least counterexample cannot hit1 or2, so every eligible boundary state must hit `20 mod27` within1268 shortcut steps.

Charging the live boundary count yields

`boxed: at least 27,786,381 distinct target occurrences`

before or at the first-candidate terminal time.

See `src/boundary_to_mod27_hit_cert.py` and `notes/2026-10-04-boundary-forces-27m-mod27-hits.md`.

### Target-run dichotomy

Let

- `E` = adjacent target-to-target sampled edges;
- `D` = target-to-nontarget departures.

Partitioning the forced target occurrences into maximal target runs gives

`boxed: E+D >= 27,786,380`.

Every D is a strict normalized-state contraction; every E is a normalized `{1,5,7}` prime-turnover edge.

See `notes/2026-10-04-mod27-run-dichotomy.md`.

This is currently the strongest quantitative bridge between the first-candidate boundary machinery and sampled arithmetic structure.

## 5. Conditional/inactive second-candidate files

The files

- `src/second_contraction_candidate_cert.py`;
- `notes/2026-10-03-second-contraction-candidate-regime-change.md`

were derived under the stronger floor `N>=4*3^44+2`. Since that floor came from the retracted Ansari sieve import, these files are **conditional diagnostics only** and are not part of the active unconditional proof chain.

## 6. Genuine no-contraction escape route — OPEN

If coefficient contraction never occurs, then

`h_k>=0` for all k.

For a genuinely divergent orbit the current internal argument gives

`h_k -> +infinity`,

`sum_k 2^(-h_k) < infinity`.

For consecutive sampled `2 mod9` returns,

`3^{q_j}s_j + eta_{j+1} = 2^{t_{j+1}}s_{j+1}`,

`eta_j in {3,15,63}`.

Committed consequences include:

- primes `p>7` cannot divide consecutive sampled cofactors;
- two-step recycling forces a discrete-log / multiplicative-order clock for `3/2 mod p`;
- fixed-gap recycling forces recycled `p>7` to divide an explicit correction integer `D_{j,m}`;
- bounded sampled odd-run lengths imply fixed-P smooth cofactors have density zero;
- the escape tail faces an unbounded-spike / density-one prime-refresh dichotomy;
- every divergent orbit hits `20 mod27` infinitely often, and each departure from that target section is a strict sampled contraction.

GRH is not currently the missing key; the unresolved issue is deterministic concentration of orbit-generated prime factors.

## 7. Current main targets

1. **Exploit the 27.786M target-run cost:** turn `E+D>=27,786,380` into a contradiction by coupling departure drift with target-run prime refresh/recycling.
2. **First-candidate global upper bound:** convert the forced `G>=3,191,033,238` exact `r=2,a=1` events into a conflicting upper bound using phase/correction structure.
3. **Weighted correction optimization:** optimize the full defect-weight distribution instead of only boundary density; a dual finite-state/LP certificate remains a preferred conceptual target.
4. **Escape route:** combine infinitely many mod27 target hits and strict target departures with the unbounded-spike versus bounded-run prime-refresh split.
5. **External frontier:** only use verification-frontier extensions after independent proof/audit; do not reuse the retracted Ansari sieve propagation.

## 8. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-04-erratum-ansari-frontier-import.md`
3. `src/first_contraction_cert.py`
4. `src/live_frontier_upgrade_cert.py`
5. `notes/2026-10-03-u3v1-exclusion-and-221-charge.md`
6. `notes/2026-10-04-boundary-forces-27m-mod27-hits.md`
7. `notes/2026-10-04-mod27-normalized-prime-turnover.md`
8. `notes/2026-10-04-mod27-target-departure-contraction.md`
9. `notes/2026-10-04-mod27-run-dichotomy.md`
10. `notes/2026-10-01-prime-turnover-clock.md`

These reconstruct the active unconditional state without relying on chat history.