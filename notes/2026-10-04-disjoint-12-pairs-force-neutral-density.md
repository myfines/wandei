# Disjoint mechanical `12` pairs force a stronger neutral-cylinder density

Status: exact unconditional consequence inside the first coefficient-contraction candidate. Not a Collatz proof.

Let

`G = #{j<k : h_{j+1}=h_j+1}`.

Every positive defect increment is exactly `+1` and has local form `r_j=2,a_j=1`. Since `h_0=0` and `h_k=-1`, the total negative defect mass is exactly `G+1`.

Let `C11` denote the number of starts `j` with

- `(r_j,r_{j+1})=(1,2)`,
- `(a_j,a_{j+1})=(1,2)`,
- equivalently `x_j == 11 (mod 16)`.

This is the neutral cylinder isolated in `notes/2026-10-04-unique-neutral-r1-a1-cylinder.md`.

## 1. Exact number of mechanical `12` pairs

For the first candidate

`k=72,057,431,991`,

`floor(k log_2 3)=114,208,327,603`.

Hence the exact number of mechanical letters `r=1` is

`R1 = 29,906,536,379`.

The mechanical word begins with `r_0=1`, ends with `r_{k-1}=1`, and contains no `11` factor. Therefore every `r=1` except the final one starts a `12` pair, so the number of complete mechanical `12` pairs is

`P12 = R1-1 = 29,906,536,378`.

Because the word contains no `11`, these two-transition `12` pairs are pairwise disjoint.

## 2. A `12` pair is neutral iff both defect increments vanish

On a mechanical `12` pair, zero defect increment on both transitions means

`a_j=r_j=1`,

`a_{j+1}=r_{j+1}=2`.

Conversely `(a_j,a_{j+1})=(1,2)` gives zero defect increment twice.

For an odd Syracuse state, the exact valuation prefix `(1,2)` is equivalent to

`x_j == 11 (mod 16)`.

Thus a complete mechanical `12` pair is counted by `C11` iff neither of its two transitions changes the defect.

## 3. Count transitions that can spoil a mechanical `12` pair

There are exactly `G` positive defect-change transitions, each of size `+1`.

Let `Nminus` be the number of negative defect-change transitions. Their total negative mass is `G+1`, and every negative transition contributes at least one unit of negative mass. Hence

`Nminus <= G+1`.

Therefore the total number of transitions with nonzero defect change is at most

`G + Nminus <= 2G+1`.

Since the mechanical `12` pairs are disjoint, one nonzero transition can spoil at most one of them. Consequently

`P12-C11 <= 2G+1`.

Hence

`boxed: C11 >= 29,906,536,377 - 2G.`

This strictly strengthens the previous exponent-count inequality

`C11 >= 29,906,536,377 - 3G`.

## 4. Numerical pressure at the current live lower edge

Using the current unconditional live bound

`G >= 3,191,033,238`,

a hypothetical survivor sitting near that lower edge would require

`C11 >= 29,906,536,377 - 2*3,191,033,238`

so

`boxed: C11 >= 23,524,469,901.`

Thus low-G survival requires an enormous density of one single exact two-transition neutral cylinder.

## 5. Strategic consequence

The main first-candidate problem can now be sharpened further:

> either `G` is substantially larger than its current window lower bound, or the orbit must realize roughly one copy of the same `11 mod16 / 12->12` neutral cylinder every three transitions across a 72-billion-step prefix.

The next useful theorem is an arithmetic/correction-budget upper bound on the realizable density of these neutral mechanical `12` pairs. The natural route is to combine constant-defect 2-adic shadowing depth with the correction penalty `2^{-h}`.
