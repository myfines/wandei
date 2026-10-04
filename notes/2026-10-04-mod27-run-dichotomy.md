# At least 27,786,380 target-run cost edges in the first candidate

Status: exact combinatorial consequence of the boundary-to-mod27 hitting bound and the mod27 departure/turnover lemmas. Not a Collatz proof.

The preceding certificate forces at least

`R >= 27,786,381`

distinct **occurrences** of sampled states `n==20 mod27` before or at the first-candidate terminal time.

Order these target occurrences along the existing sampled `2 mod9` return sequence and partition them into maximal consecutive target runs.

Let

- `J` be the number of maximal target runs;
- `E` be the number of sampled edges whose source and target are both `20 mod27`;
- `D` be the number of sampled edges that leave a target state for a non-target sampled state within the observed prefix.

If the run lengths are `l_1,...,l_J`, then

`R=sum l_i`

and every run of length `l_i` contains exactly `l_i-1` internal target-to-target edges. Hence

`E=sum(l_i-1)=R-J`.

Every completed target run ends with one target departure. At most the final run can fail to have its departure inside the observed prefix, so

`D>=J-1`.

Therefore

`E+D >= (R-J)+(J-1)=R-1`.

Using the exact target-hit lower bound gives

`boxed: E+D >= 27,786,380.`

## Arithmetic cost of the two edge types

These are not merely combinatorial edges.

### Departure edge

`notes/2026-10-04-mod27-target-departure-contraction.md` proves that every target departure strictly contracts the normalized sampled state `u=M/9`:

`u'<u`,

with principal coefficient at most `3/4`.

### Internal target edge

`notes/2026-10-04-mod27-normalized-prime-turnover.md` proves that every adjacent target-to-target edge has normalized recurrence

`3^Q c + a = 2^t c'`,

where

`Q>=1`, `a in {1,5,7}`, `3 not|cc'`.

Consequently

`gcd(c,c') | a`.

Thus primes greater than7 cannot persist across an internal target edge; the only possible shared odd primes are5 or7, and the digit `a=1` forces `gcd(c,c')=1`.

## Resulting dichotomy

A first-candidate survivor must therefore realize at least 27,786,380 edges of one of two costly types:

1. strict target-departure contractions, or
2. adjacent target prime-refresh edges.

Equivalently, for every threshold `0<=d<=27,786,380`, either

`D>=d`

or

`E>=27,786,380-d`.

This creates a quantitative bridge suitable for a two-resource optimization: many departures demand compensating positive principal drift elsewhere, while many internal target edges demand rapid normalized prime-support turnover.