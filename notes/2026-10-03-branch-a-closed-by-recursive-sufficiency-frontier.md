# Branch A is swallowed by the recursive-sufficiency verification frontier

Status: closes the first coefficient-contraction branch, assuming the published 2025 recursive-sufficiency theorem (Ansari, Proposition 3.2) is accepted. This is not a proof of the Collatz conjecture because Branch B (escape) remains open.

## 1. Published external theorem

Mohammad Ansari, *Recursive sufficiency for the Collatz conjecture and computational verification*, Notes on Number Theory and Discrete Mathematics 31(3) (2025), 471–480, Proposition 3.2, proves the following special propagation rule.

If

`M = 2*3^n + 1`

and all positive integers up to `M` satisfy Collatz, then all integers in `(M,2M]` satisfy Collatz as well.

The proof constructs a recursively sufficient set `F` whose next element after `M` is `4*3^n+3 = 2M+1`, so `F` has no point in `(M,2M]`; Corollary 2.2 then fills the whole gap.

Remark 3.1 applies this with the computational verification below `2^71`. Taking `n=44`,

`M = 2*3^44 + 1 < 2^71`,

hence every integer up to

`L = 2M = 4*3^44 + 2`

satisfies the Collatz conjecture.

### Audit note

Lemma 3.2 as printed omits the element `3` from the displayed parametrization of the infinite intersection of the recursively sufficient sets: `3` belongs to every `F_n`. The corrected intersection is `{3} union E`. This does not affect Proposition 3.2, because `3 < M` and the claimed empty interval `(M,2M]` is unchanged. The recursive-set closure steps used in Lemma 3.1 were checked separately and no obstruction to the proposition was found.

## 2. Existing Branch-A seed upper bound

The first coefficient-contraction branch fixes

`k = 72,057,431,991`

and the repository already proves the rigorous coarse bound

`N < (4/3)*2^71`

for any least counterexample entering this branch. A sharper bound near `2^71.413083842` also exists but is unnecessary here.

## 3. Exact comparison

`src/ansari_frontier_bridge_cert.py` checks using integer/rational arithmetic that

`2*3^44 + 1 < 2^71`

and

`4*3^44 + 2 > (4/3)*2^71`.

Equivalently,

`3(4*3^44+2) > 4*2^71`.

Therefore every possible Branch-A seed lies strictly below the published upgraded verification frontier `L=4*3^44+2`.

Hence no least counterexample can lie in Branch A.

## 4. Consequence

The first coefficient-contraction branch is closed:

`boxed: Branch A impossible.`

All remaining work is concentrated in Branch B, where the coefficient never contracts:

`h_n >= 0 for all n`,

and for a genuinely divergent orbit the existing argument gives

`h_n -> infinity`,

`sum_n 2^{-h_n} < infinity`.

The mod-9 sampled recurrence, prime turnover, S-unit dichotomy, and multiplicative-order clock now become the main line rather than a side branch.

This closure depends on a published external theorem rather than solely on certificates internal to this repository, so future formalization should either import Proposition 3.2 as a literature dependency or reprove its specialized `n=44` instance internally.
