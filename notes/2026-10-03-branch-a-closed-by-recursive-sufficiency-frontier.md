# RETRACTED: first-candidate closure by recursive-sufficiency frontier

Status: **retracted on 2026-10-04**. This file is retained as a provenance record. The numerical comparison inside it is correct, but the external theorem needed to upgrade the verification frontier is not currently established by the cited paper's proof.

## Retraction

This note previously imported Ansari (2025), Proposition 3.2 / Remark 3.1, to infer that verification below `2^71` extends to

`L=4*3^44+2`.

A later exact audit found that the specific sieve construction used to prove the proposition has a failed induction identity in Lemma 3.1. At the displayed `n=1` step, inside the first block `0<=k<9`, the claimed left side contains

`{3,7,11,15,19,23,27,31}`

while the claimed `F_2` is only

`{3,7,15,19}`.

Thus `11` is an explicit witness that the equality used in the induction is false. The separate omission of `3` in Lemma 3.2 is not the main problem and does not repair this failure.

See `notes/2026-10-04-erratum-ansari-frontier-import.md`.

## What remains true

The repository's internal first-candidate certificate independently proves that a least counterexample realizing

`(A,k)=(114208327604,72057431991)`

must satisfy

`N < (4/3)*2^71`,

with a sharper mechanical ceiling near `2^71.413083842`.

Also, `src/ansari_frontier_bridge_cert.py` correctly checks the purely arithmetic implication

`4*3^44+2 > (4/3)*2^71`.

But this comparison is only conditional: without an independently proved reason that every integer through `4*3^44+2` converges, it does **not** eliminate the candidate.

## Active status

The first coefficient-contraction candidate is OPEN again. Return to the internal proof chain based on the live Barina floor, weighted boundary density, 29-state boundary-run cap, translated finite certificates, exact-four exclusions, and convergent-cycle drift.

No proof of Collatz is claimed.