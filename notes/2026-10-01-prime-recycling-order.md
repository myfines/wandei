# Prime recycling reduces to multiplicative-order residue classes

Status: exact refinement of the two-step recycling congruence. Not a Collatz proof.

From the six-lane sampled normal form, every first-return block has

\[
t=q+d,
\qquad d\in\{1,2,3,4,5,6\}.
\]

In the normalized variable `R`, the next state is

\[
R'=3^a u,
\]

with

\[
a=q-1\quad\text{for lanes }d=1,2,3,4,
\]

and

\[
a=q\quad\text{for lanes }d=5,6.
\]

Therefore

\[
\boxed{\lambda:=t-a\in\{2,3,4,5,6\}.}
\]

More explicitly:

\[
d=1,2,3,4,5,6
\quad\Longrightarrow\quad
\lambda=2,3,4,5,5,6.
\]

Now suppose a prime `p>7` divides `u_j` and is recycled after one gap so that `p | u_{j+2}`. The previous note gives

\[
A_{j+2}B_{j+1}3^{a_{j+1}}
+B_{j+2}2^{t_{j+1}}
\equiv0\pmod p,
\]

where each normalized branch pair is one of

\[
(A,B)\in\{(3,1),(3,5),(1,7)\}.
\]

Substitute

\[
t_{j+1}=a_{j+1}+\lambda_{j+1}.
\]

Since `p>7`, all small constants and 2,3 are invertible modulo p. Dividing by `2^{a_{j+1}}` gives

\[
\boxed{
\left(\frac32\right)^{a_{j+1}}
\equiv
-\frac{B_{j+2}2^{\lambda_{j+1}}}
       {A_{j+2}B_{j+1}}
\pmod p.
}
\]

Thus the apparently two-dimensional exponential condition in `(a,t)` collapses to a one-dimensional discrete-log condition for the base `3/2 mod p`.

Let

\[
h_p=\operatorname{ord}_p(3\cdot2^{-1}).
\]

For any fixed prime `p>7` and fixed pair of local lane types, either the recycling congruence has no solution at all, or every allowed exponent lies in one residue class

\[
\boxed{a\equiv a_0\pmod{h_p}.}
\]

There are only finitely many local constants: the middle block has six lanes (fixing `B_{j+1}` and `lambda`), while the next normalized linear form has three types `(A,B)`, so at most eighteen discrete-log targets occur.

## Interpretation

A large odd prime cannot persist on adjacent sampled cores. If it is recycled two returns later, the length/exponent of the intervening return is arithmetically synchronized with the multiplicative order of `3/2 modulo p`.

So finite prime recycling has an additional hidden clock:

\[
\boxed{\operatorname{ord}_p(3/2).}
\]

This suggests two future branches:

1. **large-order primes:** recycling exponents lie in sparse arithmetic progressions;
2. **small-order primes:** such primes divide numbers `(3/2)^h-1`, so their supply is constrained by divisors of `3^h-2^h` for relatively small h.

A complete argument would need to connect these order restrictions to the critical sampled schedule; the present lemma only exposes the arithmetic clock.