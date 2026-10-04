# Erratum: Ansari sieve/frontier import is not established

Status: correctness correction. This note retracts the use of Ansari (2025), Proposition 3.2 / Remark 3.1, as a proved verification-frontier upgrade in this repository. It does not affect the internal first-candidate certificates.

## 1. What failed

The paper's Definition 1.3 / Theorem 2.1 strong-induction wrapper for a genuinely recursively sufficient set is useful. However the later construction of the specific sieve sets `F_n` depends on Lemma 3.1.

An independent 2026-09 audit identified an exact failure in the induction step of Lemma 3.1. At the displayed `n=1` step, write `m=4k+3` and restrict to `0<=k<9`. The set called `F'_1` permits all two-digit ternary patterns, while the removed set `A'` removes only the pattern `22`. Thus

`F'_1 \ A' = {3,7,11,15,19,23,27,31}`

inside this block.

But the claimed target `F_2`, whose two ternary digits must lie in `{0,1}`, is only

`F_2 = {3,7,15,19}`

inside the same block.

In particular

`11 in F'_1 \ A'` but `11 notin F_2`.

Therefore the equality `F_{n+1}=F'_n\A'` used to establish recursive sufficiency is false already for `n=1`.

The separate typo in Lemma 3.2 (omission of the element `3` from the displayed infinite intersection) is not the main issue; adding `{3}` does not repair the Lemma 3.1 induction failure.

## 2. Consequence

The repository must not use Proposition 3.2 / Remark 3.1 to claim that verification below `2^71` propagates to

`4*3^44+2`.

Accordingly the previous claim that the first coefficient-contraction candidate

`(A,k)=(114208327604,72057431991)`

is swallowed by an upgraded frontier is retracted.

`src/ansari_frontier_bridge_cert.py` remains only a conditional arithmetic comparison: **if** the external propagation theorem were independently repaired/proved, then its numerical frontier would exceed the first-candidate coarse seed ceiling. It is not an unconditional Collatz verification result.

The files concerning the putative second candidate under the stronger floor `4*3^44+2` are likewise conditional/inactive until such a floor is independently established.

## 3. Active unconditional status

Return to the internally certified first-candidate route using the live Barina floor recorded by the project. The strongest independent tools remain:

- exact first-candidate isolation and seed ceiling;
- pair-constrained weighted boundary density (upgraded with the live floor);
- boundary-run cap of 29 states;
- sharp repayment phase gate;
- translated 39/41/46-step certificates;
- exact-four/U3V1 exclusions and overlap bounds;
- convergent-cycle boundary adjacency and strict state drift;
- terminal suffix rigidity.

No claim of Collatz proof is made.

## 4. External audit source

The exact failed identity was recorded in `Sodelin/Collatz-Conjecture-Work`, `proof-search/sources/Sufficiency_Rank_Audit_2026-09-05.md`, section "Rejected stronger claims in the second paper". The witness above is simple enough to check independently and is the reason for this retraction.