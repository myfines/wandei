# Mod-27 target hits give a sharper normalized prime-turnover law

Status: exact arithmetic lemma for the sampled `2 mod 9` return map, combined with a published strongly-sufficient residue theorem. Not a Collatz proof.

## 1. External hitting theorem

Monks, Monks, Monks and Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, Discrete Mathematics 313(4) (2013), prove that every divergent positive Terras orbit and every nontrivial positive cycle contains an integer congruent to

`20 mod 27`.

Because every tail of a divergent orbit is again divergent, a hypothetical divergent orbit must in fact hit `20 mod 27` arbitrarily late, hence infinitely often.

This note only uses that theorem as a hitting statement. The algebra below is internal and exact.

## 2. Translation to the existing sampled M-coordinate

The repository samples Terras states

`n == 2 mod 9`

and writes

`M=4n+1`, so `M==9 mod36`.

For the stronger target

`n==20 mod27`,

we have

`M=4n+1 ==81 mod108`.

Hence every target hit satisfies

`27 | M`.

The induced `2 mod9` map uses

`M+eta = 2^t s`,

`M' = 3^q s`,

with

`eta in {3,15,63}`

and `s` odd.

## 3. Exact 3-adic normalization at a target hit

Write `M=27u`.

For the three digits:

- `M+3 = 3(9u+1)`, so `v3(M+3)=1`;
- `M+15 = 3(9u+5)`, so `v3(M+15)=1`;
- `M+63 = 9(3u+7)`, so `v3(M+63)=2`.

Thus define

`b(3)=1`, `b(15)=1`, `b(63)=2`,

and write

`s=3^b c`, with `3 not| c`.

The normalized additive digit is

`a=eta/3^b`,

so exactly

`boxed: a in {1,5,7}.`

This removes the unavoidable factor of 3 from the old digit set `{3,15,63}`.

## 4. Criterion for an immediate target-to-target sampled return

The next sampled state is

`M' = 3^(q+b) c`.

Every sampled state satisfies `M'==9 mod36`. Among the three possible residues modulo108,

`9,45,81`,

only `81` is divisible by27. Therefore

`boxed: M'==81 mod108  iff  q+b>=3.}`

Equivalently:

- for `eta=3` or `15` (`b=1`), the next sampled return is again a `20 mod27` hit iff `q>=2`;
- for `eta=63` (`b=2`), it is again a target hit iff `q>=1`.

## 5. Normalized adjacent target-return recurrence

Suppose two consecutive `2 mod9` sampled states are both `20 mod27` targets. Write

`s_j=3^{b_j}c_j`, `s_{j+1}=3^{b_{j+1}}c_{j+1}`,

with `3 not| c_j c_{j+1}`.

The ordinary sampled transition gives

`3^{q_j+b_j} c_j + eta_{j+1} = 2^{t_{j+1}} 3^{b_{j+1}} c_{j+1}`.

Since the target-to-target condition gives `q_j+b_j>=3` while `b_{j+1}<=2`, division by `3^{b_{j+1}}` is exact and yields

`boxed: 3^{Q_j} c_j + a_{j+1} = 2^{t_{j+1}} c_{j+1},`

where

`Q_j=q_j+b_j-b_{j+1}>=1`,

`a_{j+1} in {1,5,7}`,

and

`3 not| c_j c_{j+1}`.

## 6. Sharpened adjacent prime turnover

Let an odd prime `p` divide both normalized cofactors `c_j` and `c_{j+1}`. Reducing the normalized recurrence modulo `p` gives

`p | a_{j+1}`.

Therefore

`boxed: gcd(c_j,c_{j+1}) | a_{j+1}.}`

Since `a_{j+1} in {1,5,7}`:

- if `a_{j+1}=1`, then `gcd(c_j,c_{j+1})=1`;
- if `a_{j+1}=5`, any shared odd prime is only `5`;
- if `a_{j+1}=7`, any shared odd prime is only `7`.

Thus on adjacent target hits the old exceptional support set

`{3,5,7}`

shrinks to

`boxed: {5,7},`

and one of the three normalized lanes forces complete coprimality.

## 7. Two-step recycling inside a target run

For three consecutive target hits, compose two normalized transitions:

`2^{t_{j+1}+t_{j+2}} c_{j+2}`

`=3^{Q_j+Q_{j+1}}c_j + 3^{Q_{j+1}}a_{j+1} + 2^{t_{j+1}}a_{j+2}`.

Hence every prime `p>7` appearing in both endpoint cofactors must divide the smaller normalized correction

`D_j^(2)=3^{Q_{j+1}}a_{j+1}+2^{t_{j+1}}a_{j+2}`,

with digits only in `{1,5,7}`.

This is the mod-27 version of the existing prime-recycling clock and is strictly cleaner than the mod-9 `{3,15,63}` form.

## 8. Limitation and next target

The Monks theorem forces infinitely many `20 mod27` hits on a divergent orbit, but it does not by itself bound the number of intervening `2 mod9` returns. Therefore this note does **not** claim that adjacent target hits occur with positive density.

The next useful target is to control departures from `81 mod108` (the low-q cases `q+b<3`) and determine whether a divergent sampled orbit can separate almost all target hits by non-target returns. If not, the normalized `{1,5,7}` recurrence becomes a positive-density prime-refresh constraint.