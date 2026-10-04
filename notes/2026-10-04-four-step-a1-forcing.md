# Every boundary forces an `a=1` event within four odd steps

Status: exact unconditional consequence inside the first coefficient-contraction candidate. Not a Collatz proof.

Let `x_n` be an odd-only Syracuse state at a critical boundary time `h_n=0`.
The sharp boundary-altitude certificate gives

`x_n < 6,287,967,883,654,920,544,295 =: H`.

The current independently verified Barina floor used by the repository is

`N_live = 2,175,982,616 * 2^40`.

## 1. Four consecutive non-`a=1` steps are impossible

If an odd-only exponent satisfies `a>=2`, then

`x'=(3x+1)/2^a <= (3x+1)/4`.

Four iterations of the affine upper map `f(x)=(3x+1)/4` give

`f^4(x)=(81x+175)/256`.

Since the boundary state is integral and `x_n<H`, we have `x_n<=H-1`. The exact certificate

`src/boundary_four_step_a1_cert.py`

checks

`81(H-1)+175 < 256 N_live`.

Therefore if four consecutive odd-only exponents after a boundary time all satisfied `a>=2`, then

`x_{n+4}<N_live`,

contradicting least-counterexample survival above the verified frontier.

Hence every complete four-transition window beginning at `h=0` contains at least one exact

`boxed: a=1`

transition.

Equivalently, because `3x+1` has 2-adic valuation one exactly when `x≡3 (mod 4)`, every such boundary-started four-window contains an odd Syracuse state congruent to `3 mod 4`.

## 2. Global charging consequence

The live weighted-boundary argument gives

`z >= 35,260,917,543`

boundary times in the first-candidate prefix.

At most the final three boundary starts are too close to the terminal index to support four complete transitions. Thus there are at least

`W4 >= 35,260,917,540`

complete boundary-started four-windows.

A fixed transition can lie in at most four such windows. Therefore, with

`A1 = #{j<k : a_j=1}`,

we get

`4 A1 >= W4`,

hence

`boxed: A1 >= 8,815,229,385.`

This is a new global arithmetic count independent of the translated 46-step upstep certificates.

## 3. Relation to defect upsteps

Every `a=1` step falls into one of two mechanical cases:

- `r=1,a=1`: defect stays constant;
- `r=2,a=1`: defect rises by one.

The second class is exactly the already studied defect-upstep event `G`.
Thus

`A1 = C + G`,

where `C=#{r=1,a=1}` and the current separate lower bound is

`G >= 3,191,033,238`.

The new `A1` count does not by itself improve `G`, because many forced `a=1` events may occur on `r=1` steps. Its value is that it introduces a second large exact event family tied directly to the actual 2-adic valuation and to the residue class `x≡3 mod4`.

The next useful target is therefore to upper-bound or structurally constrain the `r=1,a=1` constant-defect events. Any such bound converts immediately into a stronger lower bound on `G` via `G=A1-C`.
