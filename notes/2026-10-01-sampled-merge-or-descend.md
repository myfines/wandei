# Merge-or-descend induction on the 2 mod 9 sampled map

Status: rigorous reduction principle plus finite exact experiments. This is not a proof of Collatz.

Let `F` denote the exact first-return map on sampled Terras states `n ≡ 2 (mod 9)` (equivalently on `M=4n+1 ≡ 9 (mod 36)`).

## Strong-induction reduction

To prove convergence of every sampled state it is enough to prove the following certificate property:

For every sampled `n>2`, there exist integers `k,l>=0` and a sampled `p<n` such that

`F^k(n) = F^l(p)`.

Indeed, by strong induction on `n`, the smaller sampled seed `p` converges to 2 (hence to 1 under Terras). Therefore the common state `F^k(n)=F^l(p)` also converges, so `n` converges.

A particularly convenient sufficient certificate is one of:

1. direct descent: for some `k`, `F^k(n)<n`;
2. one-step merge: for some `k`, the future state `y=F^k(n)` has a sampled predecessor `p<n` with `F(p)=y`.

Thus the problem can be weakened from "every sampled orbit descends" to

`every sampled orbit eventually descends or merges with a smaller sampled orbit`.

This criterion is equivalent to Collatz if no finite horizon is imposed, since a convergent orbit eventually reaches the base sampled state 2. Its potential value is that a bounded or structurally classifiable certificate horizon would give a finite proof mechanism.

## Exact predecessor enumeration

For a sampled target encoded by `Y ≡ 9 (mod 36)`, let `V=v_3(Y)`. Every one-step sampled predecessor can be enumerated from the induced branch parameters

`e ∈ {0,2,4}`, `delta ∈ {0,1}`, `q <= V`,

with

`r=q-delta >=0`,
`t=e+r+2`,
`eta=2^(e+2)-1`,
`s=Y/3^q`,
`X=2^t*s-eta`.

Keeping only positive `X ≡ 9 (mod 36)` whose forward induced map really returns `Y` gives the complete finite predecessor set of `Y`.

Hence a merge certificate is mechanically and exactly checkable with integer arithmetic.

## Exploratory exact scan

A direct integer scan was run over all sampled `M ≡ 9 (mod 36)` with

`M < 20,000,000`.

For each starting state, future sampled returns were followed and at each future state both tests were applied:

- has the orbit fallen below the original starting state?;
- does the current future state have a sampled predecessor below the original starting state?

Apart from the base state `M=9`, every tested state received a certificate within at most 51 sampled returns.

This is evidence only. It does not establish a universal horizon, and the maximum certificate depth can grow with the search range.

## Why this reduction may help

The induced map has only three additive shifts, `eta in {3,15,63}`, and every predecessor set is finite and explicit. This allows a CEGAR-style proof search over finite branch patterns:

- contracting branches give immediate direct descent;
- expanding `e=2` and `e=4` branches often admit an alternate smaller `e=0` predecessor;
- long `e=0` stretches are the main hard branch and can be combined with the sampled spike-altitude and critical-drift restrictions.

A successful proof could therefore take the form of a finite family of symbolic merge certificates rather than a monotone ranking function.