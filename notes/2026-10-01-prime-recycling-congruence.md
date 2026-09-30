# Two-step prime recycling in the normalized sampled map

Status: exact congruence consequence of the normalized mod-9 induced map. Not a Collatz proof.

Use the normalized sampled variables

\[
R_{j+1}=3^{a_j}u_j,
\]

where each outgoing odd core is defined by

\[
2^{t_j}u_j=A_jR_j+B_j,
\qquad
(A_j,B_j)\in\{(3,1),(3,5),(1,7)\}.
\]

The previous note proves

\[
\gcd(u_j,u_{j+1})\mid35,
\]

so any prime `p>7` cannot divide two consecutive odd cores.

Suppose nevertheless that a prime `p>7` is recycled after one gap:

\[
p\mid u_j,
\qquad
p\mid u_{j+2}.
\]

Since

\[
R_{j+1}=3^{a_j}u_j,
\]

we have

\[
R_{j+1}\equiv0\pmod p.
\]

The next-core relation gives

\[
2^{t_{j+1}}u_{j+1}
=A_{j+1}R_{j+1}+B_{j+1}
\equiv B_{j+1}\pmod p.
\]

Thus

\[
2^{t_{j+1}}u_{j+1}\equiv B_{j+1}\pmod p.
\]

Now

\[
R_{j+2}=3^{a_{j+1}}u_{j+1}.
\]

Because `p | u_{j+2}`, the following linear form vanishes modulo p:

\[
A_{j+2}R_{j+2}+B_{j+2}\equiv0\pmod p.
\]

Substituting and multiplying by `2^{t_{j+1}}` yields

\[
\boxed{
A_{j+2}B_{j+1}3^{a_{j+1}}
+B_{j+2}2^{t_{j+1}}
\equiv0\pmod p.
}
\]

Therefore every recycled prime `p>7` occurring at positions `j` and `j+2` must divide one member of the finite family of exponential binomials

\[
\boxed{c\,3^a+d\,2^t}
\]

with constants drawn from the nine combinations induced by

\[
(A,B)\in\{(3,1),(3,5),(1,7)\}.
\]

## Interpretation

The prime-support alternatives are now sharper:

1. a large odd prime disappears permanently, forcing continued introduction of new prime support; or
2. it is recycled after a gap, but then its reappearance is authorized by a rigid congruence between a power of 3 and a power of 2 with small coefficients.

Thus prime recycling itself is not free. Repeated recycling of the same finite prime set converts the sampled Collatz dynamics into a system of exponential congruences modulo those primes, involving the multiplicative order of 2 and 3 modulo p.

Possible next targets:

- quantify how many `(a,t)` pairs can recycle a fixed prime p in the critical corridor;
- combine several recycle events for the same p to obtain order constraints on `2*3^{-1} mod p`;
- use large-order / S-unit / p-adic logarithm tools to separate frequent prime recycling from genuine prime-support growth.
