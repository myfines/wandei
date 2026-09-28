# Side-branch altitude lemma — 2026-09-28

## Status

Exact elementary lemma for a hypothetical least positive Collatz counterexample.
It does **not** prove the conjecture.

Use the odd-only Syracuse map

\[
S(x)=\frac{3x+1}{2^{a}},\qquad a=v_2(3x+1),
\]

on positive odd integers.

Assume \(N\) is the least positive counterexample, and let \(x\) be any odd
state on its orbit. Write \(z=S(x)\).

## 1. Lowering a reverse exponent by two

The actual predecessor relation is

\[
x=\frac{2^a z-1}{3}.
\]

If \(a-2r\ge1\), then \(a-2r\) has the same parity as \(a\), hence

\[
y_r=\frac{2^{a-2r}z-1}{3}
\]

is also an odd positive predecessor of \(z\).

Because \(z\) is a counterexample state, every positive predecessor of \(z\)
is also a counterexample. Minimality therefore gives

\[
y_r\ge N.
\]

A direct calculation gives

\[
\boxed{x=4^r y_r+\frac{4^r-1}{3}.}
\]

Therefore

\[
\boxed{x\ge4^rN+\frac{4^r-1}{3}}
\qquad(a-2r\ge1).
\]

Taking

\[
r=\left\lfloor\frac{a-1}{2}\right\rfloor
\]

gives

\[
\boxed{x\ge4^{\lfloor(a-1)/2\rfloor}N+\frac{4^{\lfloor(a-1)/2\rfloor}-1}{3}.}
\]

## 2. Immediate consequences

For \(a\ge3\),

\[
x\ge4N+1.
\]

Hence every odd orbit point with

\[
N\le x\le4N
\]

must satisfy

\[
\boxed{v_2(3x+1)\in\{1,2\}.}
\]

More generally:

- \(a\ge5\) forces \(x\ge16N+5\);
- \(a\ge7\) forces \(x\ge64N+21\);
- each extra two powers of 2 in the Syracuse exponent require roughly another
  factor 4 of altitude above the least counterexample.

This is stronger than the earlier observation restricted to \([N,2N]\).

## 3. Why this matters for the low-altitude program

The current critical-density route says that when a multiplicative coefficient
\(3^q/2^t\) tries to dip below one, the positive affine correction must keep the
actual orbit above \(N\). That forces reciprocal mass

\[
\sum \frac1{x_i}
\]

to come from comparatively low states.

The side-branch lemma now says those low states have a sharply restricted
2-adic exponent alphabet. In the entire band \([N,4N]\) only exponents 1 and 2
are permitted.

Thus the next bridge is a two-symbol process whenever the orbit is low:

\[
a_i\in\{1,2\}.
\]

The target is a quantitative statement of the form

\[
\text{too much time below }MN
\Longrightarrow
\text{a forbidden lowered side branch }<N,
\]

or equivalently a uniform upper bound on low-altitude occupation compatible
with the critical-density lower bound.

## 4. Branching version

Every occurrence of an exponent \(a\) supplies

\[
\left\lfloor\frac{a-1}{2}\right\rfloor
\]

lowered side predecessors \(y_r\). All are counterexamples and all are at least
\(N\).

This suggests counting the full side-branch tree rather than using only the
deepest branch. A useful future lemma would show that a critical-density orbit
with too many large exponents creates too many distinct counterexample
predecessors inside a bounded height interval.

That would connect the forward 2-adic exponent sequence directly to the inverse
tree without requiring an equidistribution assumption.
