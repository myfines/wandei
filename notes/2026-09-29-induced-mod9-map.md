# Exact induced map on the 2 mod 9 section

Status: exact reformulation of the next-return map. This is not a proof of Collatz.

Let

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}\end{cases}
\]

and restrict to sampled states

\[
n\equiv2\pmod9.
\]

Set

\[
\boxed{M=4n+1.}
\]

Then

\[
\boxed{M\equiv9\pmod{36}.}
\]

The next visit of the Terras orbit to `2 mod 9` can be computed directly from `M`, without simulating the intermediate steps.

## Step 1: choose one of three shifts

Let

\[
v=v_2(n).
\]

Define

\[
e=2\min\!\left(\left\lfloor\frac v2\right\rfloor,2\right)
\in\{0,2,4\}.
\]

Equivalently,

* `e=0` if `v_2(n)=0 or 1`;
* `e=2` if `v_2(n)=2 or 3`;
* `e=4` if `v_2(n)>=4`.

Set

\[
\boxed{\eta=2^{e+2}-1\in\{3,15,63\}.}
\]

These are exactly the three correction digits arising from the complete mod-9 first-return classification.

## Step 2: strip all powers of two

Set

\[
\boxed{t=v_2(M+\eta),}
\]

and

\[
\boxed{w=\frac{M+\eta}{2^t},}
\]

so `w` is odd.

The corresponding first-return word has the form

\[
E^e O^r E Q,
\qquad
r=t-e-2\ge0,
\qquad
Q\in\{E,O\}.
\]

## Step 3: determine the final odd/even branch

The number of odd steps is one of two adjacent integers:

\[
q\in\{t-e-2,\ t-e-1\}.
\]

Choose the unique one satisfying

\[
\boxed{3^q w\equiv1\pmod4.}
\]

Since multiplying by 3 flips an odd residue modulo 4, exactly one of the two candidates works.

## Step 4: the induced return map

The next sampled value is encoded by

\[
\boxed{
M'=3^q w
=3^q\frac{M+\eta}{2^{v_2(M+\eta)}}.
}
\]

Then

\[
\boxed{n'=\frac{M'-1}{4}.}
\]

By construction

\[
M'\equiv9\pmod{36},
\qquad
n'\equiv2\pmod9.
\]

Thus the first-return dynamics is a deterministic self-map of

\[
\mathcal M=\{M>0:M\equiv9\pmod{36}\}.
\]

In words:

> add one of `3,15,63`, divide by every available factor of 2, then multiply by a power of 3 determined by the resulting odd residue modulo 4.

This is an accelerated generalized-Collatz map with only three additive constants.

## Check on small examples

For `n=11`,

\[
M=45,
\quad e=0,
\quad \eta=3,
\quad M+\eta=48=2^4\cdot3.
\]

Thus `t=4`, `w=3`, and `q` is chosen from `{2,3}`. Since

\[
3^3\cdot3=81\equiv1\pmod4,
\]

we get

\[
M'=81,
\qquad
n'=20.
\]

Indeed the actual first-return word is `OOEO` and `11 -> 20` at the next `2 mod 9` visit.

For `n=20`,

\[
M=81,
\quad e=2,
\quad\eta=15,
\quad M+\eta=96=2^5\cdot3.
\]

Then `t=5`, `w=3`, the candidates are `{1,2}`, and `q=1`, giving

\[
M'=9,
\qquad n'=2.
\]

The actual first-return word is `EEOEE`.

## Relation to Collatz

A known residue-coverage theorem says every positive Terras orbit visits `2 mod 9` arbitrarily late. Therefore proving that every orbit of this induced map on `M=9 mod 36` eventually reaches

\[
M=9
\]

would imply the Collatz conjecture; conversely Collatz immediately implies this induced convergence.

So the original problem can be studied on one arithmetic progression with the three-shift map above.

## Exact coefficient gap

Let

\[
c=\frac{3^q}{2^t}
\]

be the principal coefficient of one first-return block. The eight-template classification gives a genuine gap around 1:

\[
\boxed{c<1\Longrightarrow c\le\frac{243}{256},}
\]

while

\[
\boxed{c>1\Longrightarrow c\ge\frac{2187}{2048}.}
\]

The closest contracting block is the family `e=2,r=4,Q=O`, with coefficient `243/256`. The closest expanding block is `e=2,r=7,Q=E`, with coefficient `2187/2048`.

Hence no first-return coefficient lies in

\[
\left(\frac{243}{256},\frac{2187}{2048}\right),
\]

an interval containing 1.

This turns the sampled principal drift into a discrete walk with nonzero jumps bounded away from zero. Long odd-run spikes are the only source of unbounded positive jump size.

## Next target

The natural split is now:

1. **bounded run lengths:** the induced map uses a finite collection of affine branch types with a uniform coefficient gap;
2. **unbounded run lengths:** the long `O^r` blocks force the previously identified transfer from high 2-adic divisibility to high 3-adic divisibility.

A useful next question is whether every bounded-run induced subsystem admits a finite descent/ranking certificate, which would reduce any hypothetical counterexample to the unbounded-spike branch.