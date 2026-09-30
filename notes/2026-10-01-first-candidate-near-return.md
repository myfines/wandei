# The first contraction candidate is a sub-2^34 near-return

Status: exact necessary condition inside the first coefficient-contraction candidate. Not a Collatz proof.

Let

\[
(k,A)=(72057431991,114208327604)
\]

be the certified first candidate, and let `x_k` be the odd-only Syracuse state after `k` odd steps from a least counterexample `N`.

The exact logarithmic identity is

\[
\log\frac{x_k}{N}
=-(A\log2-k\log3)
+\sum_{i<k}\log\left(1+\frac1{3x_i}\right).
\]

Write

\[
D=A\log2-k\log3>0.
\]

Least-counterexample minimality gives `x_i>=N>=N0`, with

\[
N_0=2075\,2^{60}.
\]

Therefore

\[
0\le\log\frac{x_k}{N}
<\frac{k}{3N_0}-D.
\]

Using the rigorous rational logarithm enclosure already employed by the first-contraction certificate, together with

\[
N<\frac43\,2^{71},
\]

and the elementary bound

\[
e^z-1\le\frac{z}{1-z}\qquad(0\le z<1),
\]

`src/first_candidate_near_return.py` certifies

\[
\boxed{0\le x_k-N\le14,259,179,197<2^{34}.}
\]

Since both `N` and `x_k` are odd, the displacement is even, so in fact

\[
\boxed{x_k-N\le14,259,179,196.}
\]

Thus the enormous first-passage prefix is not merely non-descending: after roughly 72 billion odd-only Syracuse steps it must return to within fewer than `2^34` integers of its starting value near `10^21`.

This reframes the first-candidate branch as a **positive near-return problem**. The next target is to combine the small gap

\[
\delta=x_k-N
\]

with congruence/valuation information. In particular, any independent mechanism forcing `N` and `x_k` into the same residue class modulo `2^34` would imply `delta=0`, converting the candidate into an exact nontrivial cycle.