# Sampled branch-type altitude stratification above the least counterexample

Status: exact necessary conditions along the orbit of a hypothetical least sampled counterexample. Not a Collatz proof.

Let `M_*` be the least sampled counterexample in the induced section `M == 9 (mod 36)`. Every sampled state on its forward orbit is also a counterexample and hence is at least `M_*`.

Combine this minimality with the direct-descent and alternative-predecessor certificates.

## 1. Contracting first returns cannot start too low

For any coefficient-contracting sampled return,

`M' = c(M+eta)`

with

`c <= 243/256`, `eta in {3,15,63}`.

Since the endpoint `M'` is still a counterexample,

`M' >= M_*`.

Therefore

`M+eta >= (256/243) M_*`,

and using `eta<=63`,

`boxed: M >= (256/243) M_* - 63.`

Consequently no sampled source in

`[M_*, (256/243)M_* -63)`

can take a contracting first return.

## 2. Expanding e=2 sources lie above essentially 2 M_*

For an expanding `e=2` branch write

`M+15 = 2^t * 3u`,

with endpoint `M' = 3^(q+1)u` and `t>=q+3`.

The same endpoint has the smaller `e=0` sampled predecessor

`P = 3(2^s u -1)`, `s in {q+1,q+2}`.

Hence

`P <= B := 3*2^(q+2)u -3`.

Because `P` shares the divergent future, it is itself a counterexample, so

`P >= M_*` and therefore `B>=M_*`.

On the other hand,

`M >= 3*2^(q+3)u -15 = 2B-9`.

Thus

`boxed: M >= 2 M_* -9.`

So below `2M_*-9`, no expanding `e=2` branch can occur on the least-counterexample orbit.

## 3. Expanding e=4 sources lie above essentially 12 M_*

For an expanding `e=4` branch write

`M+63 = 2^t 3^a u`,

where `a>=2`, `3 not divide u`, and `t>=q+5`.

The same endpoint has an `e=0` sampled predecessor

`P=3(2^s u-1)`

with

`s<=q+a+1`.

Therefore

`P <= B := 3*2^(q+a+1)u -3`.

Again `P` is a counterexample, so `B>=P>=M_*`.

Meanwhile

`M >= 2^(q+5)3^a u -63`.

For every `a>=2`,

`2^(q+5)3^a u >= 12 * 3*2^(q+a+1)u`,

because the ratio is

`2^(4-a) 3^(a-1) >= 12`

(the minimum occurs at `a=2`, after which the ratio grows by `3/2`). Hence

`M >= 12(B+3)-63 = 12B-27`.

Thus

`boxed: M >= 12 M_* -27.`

So expanding `e=4` branches are forbidden throughout the much larger low band below `12M_*-27`.

## 4. Low-altitude branch hierarchy

Along the orbit of the least sampled counterexample:

- below `(256/243)M_*-63`, contracting branches are impossible;
- below `2M_*-9`, expanding `e=2` is impossible;
- below `12M_*-27`, expanding `e=4` is impossible.

Together with `notes/2026-10-03-sampled-expanding-core-reduction.md`, the very lowest sampled band is therefore forced entirely into the expanding `e=0`, `eta=3`, `d in {1,2}` hard core.

This is a quantitative bridge between sampled altitude and branch type. Future low-band density or return arguments can use branch exclusions at explicit multiplicative thresholds rather than only qualitative minimality.
