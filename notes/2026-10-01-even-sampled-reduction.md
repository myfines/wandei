# Even sampled states admit immediate induction certificates

Status: exact strong-induction reduction for the `2 mod 9` sampled map. This is not a proof of Collatz, but it removes all even sampled starting states from the hard branch.

Let `F` be the first-return map on sampled Terras states `n ≡ 2 (mod 9)`, and encode `M=4n+1 ≡ 9 (mod 36)`.

A strong-induction certificate for `n` is either:

1. direct descent: `F(n)<n`; or
2. merge: the endpoint `F(n)` has another sampled predecessor `p<n`.

If either holds, convergence of all smaller sampled seeds implies convergence of `n`.

## Case v2(n)=1

Here the induced branch has `e=0`. Since `n+1` is odd,

`t=v2(M+3)=2`,

so the odd-run parameter is `r=0` and the first-return coefficient is either

`1/4` or `3/4`.

Thus the first return is coefficient-contracting. The known first-return descent theorem gives `F(n)<n` for `n>2` (while `n=2` is the base state).

## Case v2(n)=2 or 3

Here `e=2`, `eta=15`. Write

`M+15 = 2^t s`,
`Y = 3^q s`,

for the sampled endpoint `Y`, with `t=r+4` and `q=r+delta`, `delta in {0,1}`.

Because `M ≡ 9 (mod 36)`, `v3(M+15)=1`, hence `s=3u` with `3∤u`. Then `Y=3^(q+1)u`.

There is an alternate `e=0` sampled predecessor

`P = 3(2^t' u - 1) -> Y`,

with `t' in {q+1,q+2}` chosen by the mod-12 condition.

If `delta=0`, then `t=q+4`, so

`P+3 <= (M+15)/4`, hence `P < M`.

If `delta=1`, then `t=q+3`, so

`P+3 <= (M+15)/2`, hence `P <= (M+9)/2 < M` for non-base sampled states.

Therefore an expanding `e=2` branch merges immediately with a smaller sampled seed. If the branch is contracting, direct descent already certifies it.

## Case v2(n)>=4

Here `e=4`, `eta=63`. Write

`M+63=2^t s`,
`Y=3^q s`,

with `t=r+6`, `q=r+delta`, and `s=3^w u`, where `w>=2` and `3∤u`.

The alternate `e=0` predecessor of `Y` has

`P+3 = 3*2^t' u`,

with `t' <= q+w+1`. Comparing with

`M+63 = 2^(q+6-delta) * 3^w u`,

we get

`(P+3)/(M+63) <= 2^(w+delta-5)/3^(w-1) <= 1/12`.

Hence

`P <= (M+27)/12 < M`.

Again, an expanding `e=4` branch merges with a smaller sampled seed; a contracting branch directly descends.

## Consequence

Every even sampled state `n ≡ 2 (mod 9)` has an immediate strong-induction certificate. Therefore any least sampled counterexample must be odd, and the only genuinely hard sampled starting states lie in

`n ≡ 11 (mod 18)`.

Equivalently, a proof by strong induction only needs a separate argument for odd sampled seeds; all even sampled seeds are discharged by the descent-or-merge mechanism above.