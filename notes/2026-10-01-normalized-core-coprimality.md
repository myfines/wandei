# Normalized sampled map and adjacent-core coprimality

Status: exact algebraic consequence of the `2 mod 9` induced map. Not a Collatz proof.

For a sampled state `n = 2 mod 9`, set

\[
M=4n+1,
\qquad
R=\frac M9=\frac{4n+1}{9}.
\]

Since `M = 9 mod 36`,

\[
\boxed{R\equiv1\pmod4.}
\]

The three additive digits `eta=3,15,63` simplify after dividing out the permanent factor 9.

## Three normalized linear forms

### eta = 3 (lanes d=1,2)

\[
M+3=3(3R+1)=2^t s.
\]

Because powers of two do not remove the factor 3, write

\[
s=3u,
\qquad
\boxed{u=\frac{3R+1}{2^t}}
\]

with `u` odd. The next sampled state satisfies

\[
R'=3^{q-1}u.
\]

### eta = 15 (lanes d=3,4)

Similarly

\[
M+15=3(3R+5),
\]

so

\[
\boxed{u=\frac{3R+5}{2^t}},
\qquad
R'=3^{q-1}u.
\]

### eta = 63 (lanes d=5,6)

Here

\[
M+63=9(R+7),
\]

and

\[
\boxed{u=\frac{R+7}{2^t}},
\qquad
R'=3^q u.
\]

Thus every sampled transition has the common form

\[
\boxed{R_{j+1}=3^{a_j}u_j}
\]

for some `a_j>=0`, where the outgoing odd core `u_j` is the odd quotient of exactly one of

\[
\boxed{3R_j+1,\qquad3R_j+5,\qquad R_j+7.}
\]

The apparently ad hoc digits `{3,15,63}` therefore normalize to the much simpler constants `{1,5,7}`.

## Adjacent odd cores are almost coprime

Take two consecutive outgoing cores. Since

\[
R_{j+1}=3^{a_j}u_j,
\]

the next core is the odd quotient of one of the three linear forms.

If the next branch uses `3R+1`, then

\[
\gcd(u_j,3R_{j+1}+1)
=\gcd(u_j,3^{a_j+1}u_j+1)=1.
\]

If it uses `3R+5`, then

\[
\gcd(u_j,3R_{j+1}+5)
=\gcd(u_j,5)\mid5.
\]

If it uses `R+7`, then

\[
\gcd(u_j,R_{j+1}+7)
=\gcd(u_j,7)\mid7.
\]

Dividing the next linear form by a power of two does not change any odd common divisor. Therefore

\[
\boxed{\gcd(u_j,u_{j+1})\mid35.}
\]

More precisely:

- next lane 1/2: `gcd(u_j,u_{j+1})=1`;
- next lane 3/4: the gcd divides 5;
- next lane 5/6: the gcd divides 7.

Hence no odd prime `p>7` can divide two consecutive sampled cores.

## Interpretation

The sampled map is not merely forced to introduce infinitely many odd primes globally. Locally, almost the entire odd prime support must be discarded at every return: primes larger than 7 cannot persist across adjacent cores.

This gives a sharper arithmetic picture for the moving-CRT/S-unit route. A hypothetical escape can recycle an old prime after a gap, but cannot simply carry a large odd prime factor continuously from return to return.

Possible next uses:

1. combine adjacent-core coprimality with S-unit solution counts to improve support-growth estimates;
2. investigate whether long-spike returns force a genuinely new prime rather than merely a prime recycled after one or more gaps;
3. apply abc/S-unit or p-adic-logarithm estimates to the pairwise-coprime linear equations underlying consecutive returns.
