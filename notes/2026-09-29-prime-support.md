# Prime support and S-unit obstruction

Status: rigorous auxiliary lemma / research note, not a Collatz proof.

Consider a nonperiodic odd-only Syracuse orbit

\[
x_{i+1}=\frac{3x_i+1}{2^{a_i}},\qquad a_i=v_2(3x_i+1).
\]

Suppose, for contradiction, that every odd iterate `x_i` has all of its prime factors in one fixed finite set `P`.

Let

\[
S=P\cup\{2,3\}.
\]

Each transition gives

\[
3x_i+1=2^{a_i}x_{i+1},
\]

or

\[
(-3x_i)+(2^{a_i}x_{i+1})=1.
\]

Both terms are `S`-units.  The classical S-unit theorem says that, for a fixed finite-rank multiplicative group, the equation

\[
u+v=1
\]

has only finitely many solutions.  Therefore there are only finitely many possible transition pairs

\[
(-3x_i,\;2^{a_i}x_{i+1}).
\]

A nonperiodic deterministic orbit has infinitely many distinct transitions, contradiction.

Hence:

\[
\boxed{\text{Every genuinely divergent/nonperiodic Collatz orbit uses infinitely many distinct prime divisors.}}
\]

This is a real prime-theoretic constraint, unlike the false idea that convergence is multiplicative over prime factors.

## Quantitative version

Beukers--Schlickewei (1996) prove that if `Gamma` is a subgroup of `(K^*)^2` of rank `r`, then `u+v=1` has at most

\[
2^{8(r+1)}
\]

solutions in `Gamma`.

If `s=|S|`, then the group of rational `S`-units has rank `s`, so the product group has rank at most `2s`.  Consequently the number of distinct Syracuse transitions supported on the same finite prime set `S` is at most

\[
2^{8(2s+1)}=2^{16s+8}.
\]

Thus if the first `L` transitions of an aperiodic orbit use only `s` primes (including 2 and 3), necessarily

\[
L\le 2^{16s+8},
\]

or equivalently

\[
\boxed{s\ge \frac{\log_2 L-8}{16}.}
\]

The numerical constant is weak, but the conclusion is qualitative and unconditional: **prime support must grow at least logarithmically with the number of distinct transitions.**

## Relation to the critical-word route

López--Stoll show that a rational 2-adic integer with a noncyclic Collatz trajectory must lie on the critical parity-density boundary `log 2 / log 3`.  That number is transcendental: it is irrational, and if it were algebraic irrational then Gelfond--Schneider applied to `3^alpha=2` would be impossible.

Therefore any hypothetical counterexample simultaneously needs:

- infinitely growing prime support;
- a parity itinerary pinned to a transcendental critical frequency (when the limiting frequency exists);
- and nonperiodic / nonautomatic structure.

Potential future use: combine prime-support growth with repeated-block/low-complexity certificates.  Repeated affine blocks restrict the orbit to finitely generated multiplicative data; high block complexity forces many distinct corrections.  A useful theorem would quantify a tradeoff between word complexity and new-prime creation.
