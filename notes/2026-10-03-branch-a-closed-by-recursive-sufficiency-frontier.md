# First coefficient-contraction candidate is swallowed by the recursive-sufficiency frontier

Status: closes the **first** coefficient-contraction candidate, assuming the published 2025 recursive-sufficiency theorem (Ansari, Proposition 3.2) is accepted. It does **not** eliminate later possible first-contraction candidates, and it is not a proof of Collatz.

## 1. Published external theorem

Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3) (2025), 471–480, Proposition 3.2, proves the following propagation rule.

If

`M = 2*3^n + 1`

and all positive integers up to `M` satisfy Collatz, then all integers in `(M,2M]` satisfy Collatz as well.

Remark 3.1 applies this with the verified range below `2^71`. Taking `n=44`,

`M = 2*3^44 + 1 < 2^71`,

hence every integer up to

`L = 2M = 4*3^44 + 2`

satisfies Collatz.

### Audit note

Lemma 3.2 as printed omits the element `3` from the displayed parametrization of the infinite intersection of the recursively sufficient sets: `3` belongs to every `F_n`. The corrected intersection is `{3} union E`. This does not affect Proposition 3.2, because `3 < M` and the gap `(M,2M]` is unchanged. The recursive-set closure steps used in Lemma 3.1 were checked separately and no obstruction to Proposition 3.2 was found.

## 2. First finite-contraction candidate

The repository isolates the first continued-fraction candidate

`(A,k)=(114208327604,72057431991)`

for the first coefficient contraction of a least counterexample above the old live frontier. For this candidate the exact first-contraction certificate proves the rigorous coarse seed bound

`N < (4/3)*2^71`.

A sharper bound near `2^71.413083842` also exists but is unnecessary here.

## 3. Exact frontier comparison

`src/ansari_frontier_bridge_cert.py` checks exactly that

`2*3^44 + 1 < 2^71`

and

`4*3^44 + 2 > (4/3)*2^71`.

Therefore every seed capable of realizing this **first candidate** is already below the published upgraded verification frontier.

Hence

`boxed: the k=72,057,431,991 first-contraction candidate is impossible.}`

## 4. What remains

This does **not** imply that coefficient contraction can never occur. A hypothetical least counterexample could remain noncontracting at the first candidate and first contract at a later sufficiently good upper approximation to `log_2 3`.

The next natural upper convergent after the eliminated candidate is

`(A,k)=(217976794617,137528045312)`.

Thus the finite-contraction route should now be restarted with the upgraded lower frontier

`N >= 4*3^44+2`

and the next candidate `k=137,528,045,312`.

Separately, the genuine no-contraction escape route remains open:

`h_n>=0 for all n`,

and for a divergent orbit the existing argument gives

`h_n -> infinity`,

`sum_n 2^{-h_n} < infinity`.

The main value of the recursive-sufficiency theorem here is therefore a free elimination of the entire first 72-billion-step contraction candidate, not a closure of every finite-contraction possibility.
