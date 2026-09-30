# Six-lane normal form for the 2 mod 9 induced map

Status: exact reparameterization of the induced first-return map. This is structural simplification, not a proof of Collatz.

For a first return to `2 mod 9`, the earlier induced-map notation has

\[
e\in\{0,2,4\},\qquad
\eta=2^{e+2}-1\in\{3,15,63\},
\]

\[
t=e+r+2,
\]

and the odd-step count is

\[
q\in\{r,r+1\}.
\]

Define

\[
\boxed{d=t-q.}
\]

If the final return step is even (`q=r`), then

\[
d=e+2\in\{2,4,6\}.
\]

If the final return step is odd (`q=r+1`), then

\[
d=e+1\in\{1,3,5\}.
\]

Hence every first-return block lies in exactly one of six lanes

\[
\boxed{d\in\{1,2,3,4,5,6\}.}
\]

The lane determines the additive digit:

\[
\eta_d=
\begin{cases}
3,&d=1,2,\\
15,&d=3,4,\\
63,&d=5,6.
\end{cases}
\]

Equivalently,

\[
\eta_d=2^{2\lfloor(d-1)/2\rfloor+2}-1.
\]

Odd `d` means the final return step is odd; even `d` means it is even.

## Principal coefficient

Since `t=q+d`, every sampled first-return coefficient is

\[
\boxed{
c(q,d)=\frac{3^q}{2^{q+d}}
=\frac{(3/2)^q}{2^d}.
}
\]

Writing

\[
\omega=\log_2(3/2),
\]

the logarithmic increment is

\[
\boxed{\Delta(q,d)=\log_2 c=q\omega-d.}
\]

Thus the complete sampled drift is a lattice walk whose horizontal/odd-run variable `q` may be large but whose correction lane `d` is always one of six integers.

The quantity `d=t-q` is exactly the number of even Terras steps in the return block, so this normal form is the algebraic version of the proved `at most six even steps between 2 mod 9 visits` theorem.

## No trivial same-slope branch surgery

Suppose two sampled return branches had the same principal coefficient. Then

\[
\frac{3^q}{2^{q+d}}=\frac{3^{q'}}{2^{q'+d'}}.
\]

Unique factorization at the primes 2 and 3 forces

\[
q=q',\qquad d=d'.
\]

But `d` already fixes `eta_d` and the parity of the terminal return step. Therefore there is no pair of distinct lanes with the same coefficient but a different additive digit.

So the simplest proposed sampled word surgery — keeping the same slope and endpoint while replacing `eta=3` by `15` or `63` — is impossible. Any useful surgery must change the coefficient/length/count as well.

## Critical-line form

For sampled prefixes define

\[
Q_J=\sum_{j<J}q_j,
\qquad
D_J=\sum_{j<J}d_j,
\qquad
T_J=Q_J+D_J.
\]

Then the cumulative logarithmic principal drift is exactly

\[
\boxed{
H_J=Q_J\log_2 3-T_J
=\omega Q_J-D_J.
}
\]

Hence the critical parity-density condition is the statement that the lattice point `(Q_J,D_J)` repeatedly approaches the irrational line

\[
D=\omega Q.
\]

A hypothetical sampled-noncontracting escape tail must simultaneously have `H_J>=0`, ultimately `H_J -> +infinity` (from correction summability), yet return arbitrarily close to zero relative to scale along critical subsequences. Long odd-run spikes are simply large `q` moves in one of six lanes; compensating contractions are moves with `q*omega<d`.

This six-lane picture is a cleaner base for future finite-state or Diophantine arguments than the original eight-template wording.