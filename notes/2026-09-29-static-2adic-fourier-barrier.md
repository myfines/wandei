# Static 2-adic Fourier barrier — 2026-09-29

## Status

This note records an **optimality / obstruction result**, not a proof of the
Collatz conjecture.

The current least-counterexample program gives a simple drift restriction.  If
`N` is a least positive counterexample and

\[
x_{i+1}=\frac{3x_i+1}{2^{a_i}},\qquad a_i=v_2(3x_i+1),
\]

then every prefix satisfies

\[
\frac1n\sum_{i<n}a_i\le \lambda+\delta_N,
\qquad
\lambda:=\log_2 3,
\qquad
\delta_N:=\log_2\left(1+\frac1{3N}\right).
\]

The question studied here is:

> how much multiplicative-character bias can be forced **using only this one-time residue-distribution constraint**?

The answer is that modulus 16 already reaches the exact static limit.

---

## 1. Mod-16 truncated valuation

For odd residues modulo 16 define

\[
\tau(r)=\min(v_2(3r+1),4).
\]

On

\[
r=1,3,5,7,9,11,13,15
\]

we get

\[
\tau=(2,1,4,1,2,1,3,1).
\]

The uniform mean is

\[
\mathbb E_{\mathrm{unif}}\tau=\frac{15}{8}.
\]

Let `p` be any probability distribution on the odd residue classes mod 16
coming from an orbit prefix. Since `tau <= a`, the least-counterexample drift
restriction gives

\[
\mathbb E_p\tau\le \lambda+\delta_N.
\]

Expanding `tau` in the character basis of

\[
(\mathbb Z/16\mathbb Z)^\times\cong C_2\times C_4,
\]

the absolute values of its seven nontrivial Fourier coefficients are

\[
\frac78,\frac38,\frac38,\frac18,\frac18,\frac18,\frac18,
\]

whose sum is

\[
\frac{17}{8}.
\]

Therefore

\[
\frac{15}{8}-(\lambda+\delta_N)
\le
\frac{17}{8}
\max_{\chi\ne1}|\mathbb E_p\chi|.
\]

Hence some nontrivial Dirichlet character modulo 16 satisfies

\[
\boxed{
|\mathbb E_p\chi|
\ge
\frac{15-8\lambda-8\delta_N}{17}.
}
\]

For large `N`, this tends to

\[
\boxed{0.13648823495475\ldots}.
\]

---

## 2. The bound is exactly sharp at modulus 16

Ignore the negligible `delta_N` for the extremal static model and impose

\[
\mathbb E\tau=\lambda.
\]

Set

\[
c=\frac{4-\lambda}{17},\qquad
b=\frac{7\lambda-11}{17}.
\]

Assign probability `b` to the class `5 mod 16`, and probability `c` to each of
the other seven odd residue classes. Then

\[
7c+b=1,
\]

and because the seven non-5 classes have total `tau`-weight 11,

\[
11c+4b=\lambda.
\]

For every nontrivial character `chi mod 16`, the sum of `chi` over all eight
units is zero. Thus

\[
\mathbb E\chi
=b\chi(5)+c\sum_{r\ne5}\chi(r)
=(b-c)\chi(5),
\]

so every nontrivial character has the **same absolute bias**

\[
\boxed{
|\mathbb E\chi|
=c-b
=\frac{15-8\lambda}{17}.
}
\]

Therefore the Fourier lower bound above is not merely convenient: it is the
exact optimum for the static mod-16 problem.

---

## 3. Lifting to the full 2-adic unit group

The same obstruction persists even if one allows **all finite-conductor
characters on** `Z_2^×`.

Construct a probability measure as follows.

- For each mod-16 class other than `5`, place total mass `c` and distribute it
  Haar-uniformly inside that entire mod-16 coset.
- Place the exceptional mass `b` Haar-uniformly on the smaller coset
  `5 mod 32`.

For every `x = 5 mod 32`,

\[
3x+1=16(1+6k),
\]

so

\[
v_2(3x+1)=4
\]

exactly.  For the other seven mod-16 classes the valuation is also already
fixed by the residue modulo 16. Hence the full, uncapped valuation has mean

\[
\mathbb E a=11c+4b=\lambda.
\]

Now consider any nontrivial finite-conductor character on `Z_2^×`.

1. If it factors modulo 16, its bias has magnitude exactly `c-b`.
2. If it factors modulo 32 but not modulo 16, the Haar-uniform parts on the
   seven full mod-16 cosets cancel; only the exceptional `5 mod 32` coset
   survives, so the bias magnitude is at most `b`.
3. If its conductor exceeds 32, it integrates to zero on every coset used
   above because the measure is Haar-uniform inside those mod-32 cosets.

Since

\[
b < c-b,
\]

we obtain

\[
\boxed{
\sup_{\chi\ne1}|\mathbb E\chi|
=\frac{15-8\log_2 3}{17}.
}
\]

Thus **no argument that uses only a static 2-adic residue distribution plus the
mean-drift constraint can force a larger universal character bias**, no matter
how high the modulus is taken.

---

## 4. Consequence for the proof program

This kills a tempting but insufficient strategy:

> keep increasing the modulus `8 -> 16 -> 32 -> 64 -> ...` and hope that the
> static Fourier contradiction eventually becomes arbitrarily strong.

It does not.

The next progress must exploit information that the extremal static measure
ignores, for example:

- **temporal correlations** between successive residues;
- the global archimedean phase
  `frac(log_2(x_i/N))`, which follows a near irrational rotation;
- the 3-adic reverse-tree constraints from minimality;
- or the fact that a hypothetical exceptional 2-adic itinerary must correspond
  to an actual positive integer, not merely an arbitrary point of `Z_2`.

This is consistent with the classical Bernstein--Lagarias fact that the
standard Collatz map on `Z_2` is Bernoulli / shift-conjugate: purely 2-adic
measure mixing cannot exclude a single exceptional positive integer orbit.

The useful target is therefore no longer a static character bound, but a
**space-time / adelic incompatibility theorem**.
