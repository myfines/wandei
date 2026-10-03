# Strong-induction reduction to the expanding eta=3 sampled core

Status: exact reduction theorem for the `2 mod 9` induced map. Not a proof of Collatz; it isolates the only first-return branches that still need a nontrivial merge/descent certificate.

Let `F` be the exact first-return map on sampled Terras states `n == 2 (mod 9)`, and encode sampled states by

`M=4n+1 == 9 (mod 36)`.

Recall the induced branch data

- `e in {0,2,4}`;
- `eta=2^(e+2)-1 in {3,15,63}`;
- `M+eta = 2^t w`, with `w` odd;
- `q in {t-e-2,t-e-1}` chosen by the final mod-4 condition;
- `M' = 3^q w`.

Also write `d=t-q in {1,...,6}`. The principal coefficient is

`c=3^q/2^t=(3/2)^q/2^d`.

The merge-or-descend induction says it is enough, for every sampled source above the base state, to obtain either a direct sampled descent or a future state having a smaller sampled predecessor.

## 1. Contracting branches are immediate descent certificates

The existing sampled-return contraction theorem proves that whenever `c<1`, the first-return endpoint is strictly smaller than the source for every sampled seed above the base case.

Hence every coefficient-contracting first-return branch is already certified by direct descent.

This includes the `e=0`, `v2(n)=1` branch: its first-return word is `EO` with coefficient `3/4`.

## 2. Every expanding e=2 branch has a smaller e=0 predecessor

Take an expanding `e=2` source. The exact branch classification gives `q>=6`. Write

`M+15 = 2^t * 3u`, `3 not divide u`,

so

`M' = 3^(q+1) u`.

The same target has an `e=0` sampled predecessor

`M_tilde = 3(2^s u - 1)`,

where the parity choice `s in {q+1,q+2}` is the unique one making `M_tilde == 9 (mod 36)` and giving the correct final mod-4 branch.

For an `e=2` branch, `d=t-q` is either 3 or 4, so

`t >= q+3`.

Therefore

`M_tilde <= 3*2^(q+2)u - 3`

while

`M = 3*2^t u - 15 >= 3*2^(q+3)u - 15`.

Since `q>=6` and `u>=1`,

`3*2^(q+2)u - 3 < 3*2^(q+3)u - 15`,

hence

`boxed: M_tilde < M.`

Thus every expanding `e=2` branch has a one-step merge certificate through a smaller sampled source.

## 3. Every expanding e=4 branch has a smaller e=0 predecessor

Take an expanding `e=4` source. Write

`M+63 = 2^t * 3^a u`,

with `a>=2` and `3 not divide u`, so the endpoint is a power of 3 times `u`.

The exact predecessor construction gives an `e=0` sampled predecessor of the same endpoint

`M_tilde = 3(2^s u - 1)`

with

`s <= q+a+1`.

For `e=4`, `d=t-q` is 5 or 6, hence `t>=q+5`. Therefore

`M_tilde < 3*2^(q+a+1)u`

and

`M = 2^t 3^a u - 63 >= 2^(q+5)3^a u -63`.

For every `a>=2`,

`3*2^(q+a+1)u < 2^(q+5)3^a u`,

because this is equivalent to

`2^(a-4) < 3^(a-1)`,

which holds for all `a>=2`. The finite additive slack is already dominated in every expanding `e=4` branch (equivalently by the exact branch lower bounds used in the minimal-sampled-counterexample proof).

Hence

`boxed: M_tilde < M.`

So every expanding `e=4` branch also has a one-step merge certificate through a smaller sampled source.

## 4. The only unresolved first-return core

After Sections 1--3, a sampled source can fail to receive an immediate descent/merge certificate only if

- `e=0`;
- the source `n` is odd (the `v2(n)=1` case is the contracting `EO` branch);
- the first-return coefficient is expanding.

For `e=0`, the shift is always

`eta=3`,

and the lane is only

`d in {1,2}`.

Thus the entire sampled strong-induction problem reduces to the expanding `eta=3` core:

`boxed: e=0, eta=3, d=1 or 2, c>1.`

Equivalently, with

`M+3=2^t w`, `w` odd,

one has

`M'=3^(t-d) w`, `d in {1,2}`,

subject to the deterministic mod-4 branch choice and the inequality `3^(t-d)>2^t`.

Because `n` is odd in this core,

`M == 45 (mod 72)`

and `t=v2(M+3)>=3`.

More explicitly:

- lane `d=1` has `q=t-1` and is expanding for every allowed `t>=3`;
- lane `d=2` has `q=t-2` and is expanding only for `t>=6`.

## 5. Research consequence

To prove the sampled merge-or-descend property, it is enough to solve the expanding `eta=3` core. There is no need to treat `eta=15` and `eta=63` expanding branches as independent hard cases: they already merge into smaller sampled seeds in one return.

This reduction should be used as the base state space for future symbolic/finite-state searches. In particular, bounded-run or residue-cylinder arguments can focus entirely on the two expanding lanes `d=1,2`, while every departure from this core is an immediate induction certificate.
