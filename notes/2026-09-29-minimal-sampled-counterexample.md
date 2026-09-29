# Necessary residue classes for a minimal sampled counterexample

Status: conditional reduction. Assume the Collatz conjecture is false. This note derives restrictions on the least counterexample lying in the sampled section `n = 2 mod 9`.

Use the Terras map and the exact induced first-return map from the companion note.

A known residue-coverage theorem implies that every positive orbit visits `2 mod 9` arbitrarily late. Hence, if any counterexample exists, then there exists a counterexample `n = 2 mod 9`. By well-ordering choose the smallest such sampled counterexample and call it

\[
\boxed{n_*}.
\]

Set

\[
\boxed{M_*=4n_*+1.}
\]

Then

\[
M_*\equiv9\pmod{36}.
\]

## 1. The minimal sampled counterexample is odd

The first return of `n_*` to `2 mod 9` cannot have contracting principal coefficient. The independently verified theorem `contracting_two_mod_nine_segment_descends` says that a coefficient-contracting segment before the next residue-two visit strictly descends for every seed above two. Its endpoint would therefore be a smaller sampled counterexample, contradicting minimality.

Thus the first return from `n_*` is coefficient-expanding.

Recall the three-shift induced classification. Let

\[
e\in\{0,2,4\}
\]

be the branch type, with shifts

\[
\eta_e=2^{e+2}-1\in\{3,15,63\}.
\]

For `e=2`, every expanding branch has at least `q>=6` odd steps in the first-return block. Write

\[
M_*+15=2^t\,3u,
\qquad 3\nmid u,
\]

so the target is

\[
M'=3^{q+1}u.
\]

The target has an alternative `e=0` sampled predecessor of the form

\[
\widetilde M=3(2^{\widetilde t}u-1),
\qquad
\widetilde t\in\{q+1,q+2\},
\]

where the parity of `\widetilde t` is chosen so that `\widetilde M=9 mod 36`. This predecessor maps to the same `M'`.

Since the original `e=2` branch has

\[
t\ge q+3,
\]

we have

\[
\widetilde M
\le 3\cdot2^{q+2}u-3
<3\cdot2^{q+3}u-15
\le M_*.
\]

Thus an expanding `e=2` first return contradicts the minimality of `M_*`.

For `e=4`, write

\[
M_*+63=2^t3^d u,
\qquad d\ge2,
\qquad 3\nmid u.
\]

Every expanding branch has large `q` and

\[
t\ge q+5.
\]

The same target again has an alternative `e=0` sampled predecessor

\[
\widetilde M=3(2^{\widetilde t}u-1),
\qquad
\widetilde t\le q+d+1.
\]

The inequality

\[
3\cdot2^{q+d+1}u
<2^{q+5}3^d u
\]

holds already for `d>=2`, and the additive constants do not close the gap. Hence again

\[
\widetilde M<M_*.
\]

So `e=4` is also impossible for the first return of the minimal sampled counterexample.

Only `e=0` remains. If `v_2(n_*)=1`, the first-return word is the fixed word `EO`, whose coefficient is `3/4<1`, already excluded. Therefore

\[
\boxed{v_2(n_*)=0.}
\]

Thus

\[
\boxed{n_*\text{ is odd}.}
\]

Since also `n_*=2 mod 9`,

\[
\boxed{n_*\equiv11\pmod{18}.}
\]

Equivalently,

\[
\boxed{M_*\equiv45\pmod{72}.}
\]

## 2. A high 3-adic valuation gives a smaller sampled predecessor

Write

\[
M_*=3^V u,
\qquad 3\nmid u.
\]

Because `M_*=9 mod 36`, we have `V>=2`.

Choose the unique

\[
\widetilde t\in\{V,V+1\}
\]

such that

\[
2^{\widetilde t}u\equiv4\pmod{12}.
\]

Then

\[
\boxed{\widetilde M=3(2^{\widetilde t}u-1)}
\]

satisfies

\[
\widetilde M\equiv9\pmod{36}
\]

and its `e=0` induced branch maps exactly to `M_*`.

If `V>=5`, then

\[
\widetilde M
\le3\cdot2^{V+1}u-3
<3^V u
=M_*,
\]

because

\[
2^{V+1}<3^{V-1}
\]

for every `V>=5`.

This would be a smaller sampled counterexample. Hence

\[
\boxed{v_3(M_*)\le4.}
\]

So only `V=2,3,4` remain.

## 3. Refinement at V=3 and V=4

For `V=3`, if `u=2 mod 3`, the chosen exponent is `\widetilde t=3`, giving a strictly smaller predecessor. Thus the minimal sampled counterexample can survive at `V=3` only when

\[
u\equiv1\pmod3.
\]

Equivalently,

\[
M_*\equiv27\pmod{81}.
\]

For `V=4`, if `u=1 mod 3`, the chosen exponent is `\widetilde t=4`, again producing a smaller predecessor. Hence survival at `V=4` requires

\[
u\equiv2\pmod3,
\]

or

\[
M_*\equiv162\pmod{243}.
\]

At `V=2`, both nonzero classes of `u mod 3` remain possible.

## 4. Four explicit residue cylinders

Combining the oddness condition

\[
M_*\equiv45\pmod{72}
\]

with the allowed 3-adic cases gives the following complete necessary residue alternatives:

### V=2

\[
M_*\equiv45\text{ or }117\pmod{216},
\]

which translates to

\[
\boxed{n_*\equiv11\text{ or }29\pmod{54}.}
\]

### V=3

\[
M_*\equiv189\pmod{648},
\]

so

\[
\boxed{n_*\equiv47\pmod{162}.}
\]

### V=4

\[
M_*\equiv405\pmod{1944},
\]

so

\[
\boxed{n_*\equiv101\pmod{486}.}
\]

Therefore any least sampled counterexample must lie in the union

\[
\boxed{
n_*\equiv11,29\pmod{54}
\quad\text{or}\quad
n_*\equiv47\pmod{162}
\quad\text{or}\quad
n_*\equiv101\pmod{486}.
}
\]

This is only a necessary condition, not an exclusion theorem.

## 5. Sampled side-branch interpretation

The alternative-predecessor construction also gives altitude penalties away from the sampled minimum. For example, an expanding `e=2` branch has an alternative predecessor roughly at most half as large as its source; an expanding `e=4` branch has an alternative predecessor roughly at most one twelfth as large. Thus on a hypothetical counterexample orbit, these branch types cannot occur too close to the least sampled counterexample.

This is a sampled analogue of the earlier odd-only side-branch altitude lemma.

Next target: combine these low-altitude sampled restrictions with the critical-density/correction lower bounds, or iterate the induced reverse-predecessor argument to further shrink the four surviving residue cylinders.