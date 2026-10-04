# Six-step mod-16 target forcing from every boundary

Status: exact unconditional consequence inside the first coefficient-contraction candidate. Not a Collatz proof.

Let

`T16 = {7,11,15} mod16`.

The exact affine-DP certificate

`src/boundary_6_step_mod16_target_cert.py`

proves that every complete six-transition window beginning at a critical-boundary state `h=0` contains a state in `T16`.

## 1. Target-avoiding affine graph

If an odd state avoids `T16`, its residue modulo 16 is in

`{1,3,5,9,13}`.

Using the exact odd-only map and always choosing the smallest possible valuation when a residue admits several valuations gives a safe upper graph:

- `1 mod16`: `a=2`;
- `3 mod16`: `a=1`;
- `5 mod16`: `a>=4`, upper-bounded using `a=4`;
- `9 mod16`: `a=2`;
- `13 mod16`: `a=3`.

All allowed non-target successor residues are retained, so the DP over-approximates every actual target-avoiding orbit.

Starting from the sharp boundary altitude

`x < 6,287,967,883,654,920,544,295`,

the maximal target-avoiding affine envelope is still above the live frontier after five odd steps, but is strictly below it after six.

Therefore every surviving boundary-started six-window must hit `T16`.

## 2. Global target count

The current live boundary lower bound is

`z >= 35,260,917,543`.

At most five terminal boundary starts fail to support six complete transitions, so at least

`35,260,917,538`

complete six-windows remain.

A fixed target state lies in at most six such windows. Hence the number `H16` of distinct target states satisfies

`boxed: H16 >= 5,876,819,590.`

## 3. Why these three residues are useful

All three target residues have first valuation `a=1`.

More precisely:

- `7 mod16` has valuation prefix `(1,1)`;
- `15 mod16` has valuation prefix `(1,1)`;
- `11 mod16` has valuation prefix `(1,2)`.

The mechanical word contains no `11` factor.

Therefore a target state in `7` or `15 mod16` forces at least one exact defect upstep

`G: r=2,a=1`

within its first two odd transitions.

A target state in `11 mod16` also forces such a G unless its mechanical pair is exactly

`r_j r_{j+1}=12`.

In that exceptional case the valuation pair is also `12`, so both defect increments are zero. This is precisely the neutral cylinder isolated independently in

`notes/2026-10-04-unique-neutral-r1-a1-cylinder.md`.

Thus every one of the at least 5.876 billion target states yields either

1. a G event within two transitions, or
2. the single exact neutral exception
   `x_j==11 mod16`, `(r_j,r_{j+1})=(1,2)`, `(a_j,a_{j+1})=(1,2)`.

A single G transition can serve at most two target starts (at times `j` and `j-1`), so if `E11` counts these neutral target exceptions,

`H16 - E11 <= 2G`.

This inequality does not yet improve the current lower bound on G by itself, but it independently identifies the same `11 mod16 / 12->12` cylinder as the unique cheap escape from a dense local forcing theorem.

The coincidence is strategically important: both the global exponent-count decomposition and the six-step altitude argument now reduce low-G survival to controlling the density of the same exact 2-adic cylinder.
