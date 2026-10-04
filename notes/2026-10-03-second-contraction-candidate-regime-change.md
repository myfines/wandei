# CONDITIONAL / INACTIVE: second finite-contraction candidate regime change

Status updated 2026-10-04: this note depends on the stronger floor

`F=4*3^44+2`,

which was previously imported from Ansari (2025), Proposition 3.2 / Remark 3.1. An exact audit found a failed set equality in the Lemma 3.1 sieve induction, so that frontier upgrade is not accepted as proved in this repository. See `notes/2026-10-04-erratum-ansari-frontier-import.md`.

Therefore the material below is a **conditional diagnostic only**. It is not part of the active unconditional proof chain.

## Conditional statement

If one independently establishes the floor

`N>=4*3^44+2`,

then the same Farey/continued-fraction geometry isolates the next upper candidate after the first as

`(A,k)=(217976794617,137528045312)`.

`src/second_contraction_candidate_cert.py` conditionally certifies this and gives a mechanical seed ceiling with

`log_2 N_upper ~= 74.962036844899...`.

Under the same assumed floor, the survival correction ratio would only need

`R > F/N_upper ~= 0.107046771248413... < 1/2`,

showing a qualitative regime change: the first-candidate high-boundary-density relaxation would no longer force positive boundary density.

This conditional observation may become useful if the stronger frontier is independently proved in the future.

## Active route

Until then, return to the first finite-contraction candidate

`(A,k)=(114208327604,72057431991)`

using the independently recorded live Barina floor and the repository's internal exact certificates.
