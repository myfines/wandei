# Every departure from the `20 mod 27` target strictly contracts the sampled normalized state

Status: exact arithmetic lemma for the sampled `2 mod 9` map. Not a Collatz proof.

This strengthens `notes/2026-10-04-mod27-normalized-prime-turnover.md`.

## 1. Target coordinate

For the sampled section `n==2 mod9`, write

`M=4n+1=9u`.

Then `M==9 mod36`, so `u==1 mod4`.

The stronger target

`n==20 mod27`

is equivalent to

`M==81 mod108`,

hence

`boxed: u==9 mod12.`

In particular every target has `u>=9` and `3|u`.

## 2. Exact departure condition

At a target hit the old sampled map has

`M+eta = 2^t 3^b c`,

`M' = 3^(q+b)c`,

where `3 not|c` and

- `eta=3` gives `b=1`;
- `eta=15` gives `b=1`;
- `eta=63` gives `b=2`.

Every sampled output satisfies `M'==9 mod36`, so `v3(M')>=2`. Since `3 not|c`,

`q+b>=2`.

Among sampled residues modulo108, the target residue `81` is exactly the one divisible by27. Therefore

`M' is again a target iff q+b>=3`.

Thus

`boxed: a target departure occurs iff q+b=2.}`

## 3. Three departure lanes

### Digit eta=3

Here `e=0`, `b=1`, so departure forces `q=1`.

The ordinary first-return rule has

`q in {t-e-2,t-e-1}={t-2,t-1}`,

therefore

`t in {2,3}`.

Since

`9u+3=3(3u+1)`,

the output `M'=9u'` has

`boxed: u'=(3u+1)/2^t,  t in {2,3}.}`

Hence

`u' <= (3u+1)/4 < u`

for every target `u>=9`.

### Digit eta=15

Here `e=2`, `b=1`, so again departure forces `q=1`.

Now

`q in {t-4,t-3}`,

so

`t in {4,5}`.

Since

`9u+15=3(3u+5)`,

`boxed: u'=(3u+5)/2^t,  t in {4,5}.}`

Therefore

`u' <= (3u+5)/16 < u`

for every target `u>=9`.

### Digit eta=63

Here `e=4`, `b=2`, so departure forces `q=0`.

The condition `e=4` means `v2(n)>=4`. Since

`n=(9u-1)/4`,

we obtain

`9u==1 mod64`,

hence

`u==57 mod64`.

Thus `u+7` is divisible by64. Since

`9u+63=9(u+7)`,

we have `t>=6`. But `q` is one of `{t-6,t-5}` and departure requires `q=0`, so necessarily

`t=6`.

Therefore

`boxed: u'=(u+7)/64 < u.}`

## 4. Uniform consequence

Every sampled transition that leaves the `20 mod27` target section satisfies

`boxed: u'<u.}`

Moreover the weakest departure lane is the `eta=3,t=2` lane, giving the uniform affine bound

`boxed: u' <= (3u+1)/4.}`

Thus every target departure has principal coefficient at most `3/4`.

`src/mod27_target_departure_cert.py` records the exact modular identities and inequalities.

## 5. Why this matters

The Monks--Monks--Monks--Monks strongly-sufficient residue theorem forces every divergent positive orbit to hit `20 mod27` arbitrarily late. Therefore a divergent sampled orbit has only two ways to interact with those infinitely many hits:

1. remain in the target section for one or more consecutive sampled returns; or
2. depart, in which case the normalized sampled state `u=M/9` strictly decreases at that departure.

So any hypothetical divergent orbit must repeatedly compensate these target-departure contractions by expansion elsewhere, or eventually spend long stretches in consecutive target-to-target transitions.

This gives a new structural split for the escape branch. The next useful question is whether bounded sampled odd-run length can supply enough expansion between the forced target departures, or whether target runs themselves admit a separate descent/prime-turnover obstruction.