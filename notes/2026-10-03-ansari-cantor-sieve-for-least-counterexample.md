# Ansari recursive sufficiency forces a ternary-Cantor least counterexample

Status: exact consequence of the published recursive-sufficiency construction, with the small Lemma 3.2 correction noted below. Not a Collatz proof.

Let `C` be the set of positive integers that do not satisfy Collatz, and suppose `C` is nonempty. Let

`N_* = min C`.

Mohammad Ansari's recursively sufficient sieves `F_n` are nested, and their intersection `F` is recursively sufficient. The printed formula for the intersection omits the element `3`; the corrected set is

`F = {3} union E`,

where

`E = { 3 + 4*sum_{i=0}^m a_i 3^i : m>=0, a_i in {0,1}, a_m=1 }`.

(The equivalent printed parametrization uses an explicit leading `4*3^m` term.)

## 1. The least counterexample must lie in F

By recursive sufficiency, every integer `n>1` outside `F` merges with some smaller positive integer `m<n`.

If the least counterexample `N_*` were outside `F`, there would be an `m<N_*` with `m <-> N_*`. By minimality, `m` satisfies Collatz, so `N_*` would satisfy it as well, contradiction.

Therefore

`boxed: N_* in F.`

Since `3` itself satisfies Collatz, a hypothetical least counterexample must in fact lie in `E`.

## 2. Explicit ternary digit restriction

Write

`S=(N_*-3)/4`.

Then

`boxed: S = sum a_i 3^i,  a_i in {0,1}.`

So the ordinary base-3 expansion of `(N_*-3)/4` contains no digit `2`.

This is a genuine deterministic sieve, not a density heuristic.

Immediate congruence consequences include:

- `N_* == 3 (mod 4)`;
- hence for the odd-only Syracuse map, `v2(3N_*+1)=1` at the first odd step;
- modulo 9, using `(a_0,a_1) in {0,1}^2`, one gets
  `N_* mod 9 in {1,3,6,7}`;
- in particular the global least counterexample itself is never `2 mod 9`.

## 3. Sparsity

The number of elements of `E` up to scale `X` grows on the order of

`X^(log_3 2)`

(up to constant-factor/end-point effects), because each ternary digit position has only two choices instead of three.

Thus the least-counterexample search is confined to a Cantor-type zero-density set with exponent

`log_3 2 ~= 0.6309297535`.

This does not by itself make brute-force verification to the second finite-contraction ceiling practical: near `2^75` the raw number of such candidates is still enormous. Its value is structural.

## 4. New bridge to the internal ternary machinery

The repository's earlier `ternary-moving-anchor` and base-2/base-3 duality work derived ternary restrictions on endpoints from a hypothetical critical escape script, but lacked a theorem forcing the actual least seed itself into a sparse ternary class.

Recursive sufficiency supplies exactly such a seed-side coverage theorem.

A promising combined target is now:

> intersect the Ansari seed Cantor condition
> `N=3+4 sum a_i 3^i`, `a_i in {0,1}`
> with the dyadic cylinder / moving-anchor conditions forced by long Syracuse prefixes.

Any exponential loss in the allowed intersection beyond the raw `X^(log_3 2)` count could materially strengthen both finite-contraction candidate searches and the escape branch.

## 5. Verification-frontier interpretation

The same set explains Proposition 3.2. For

`M_n=2*3^n+1`,

`M_n` is a member of `F`, and the next member of `F` is `4*3^n+3=2M_n+1`; hence the interval `(M_n,2M_n]` is empty of `F`. Once all integers up to `M_n` are verified, recursive sufficiency fills that entire gap automatically.

The deeper lesson for this project is that future verification-frontier improvements need only control the sparse `F` points, not every intervening integer.
