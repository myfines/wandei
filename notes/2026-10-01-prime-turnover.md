# Prime turnover in the sampled mod-9 Collatz map

Status: exact elementary consequence of the induced map; not a Collatz proof.

On sampled states `n = 2 (mod 9)`, set

\[
M=4n+1\equiv 9\pmod{36}.
\]

The exact induced map derived earlier has the form

\[
M' = 3^q\frac{M+\eta}{2^t},
\qquad
\eta\in\{3,15,63\},
\qquad
t=v_2(M+\eta).
\]

For every prime `p>3`, the factors `2^t` and `3^q` are p-adic units, hence

\[
\boxed{v_p(M')=v_p(M+\eta).}
\]

Thus the prime-to-6 part of the next sampled state is exactly the prime-to-6 part of `M+eta`.

## Consecutive-prime turnover

Suppose a prime `p>3` divides both `M` and `M'`. Then the valuation identity implies `p | M+eta`; together with `p|M`,

\[
p\mid \eta.
\]

Since

\[
\eta\in\{3,15,63\},
\]

the only possibilities above 3 are `p=5` (on the eta=15 branch) or `p=7` (on the eta=63 branch). Therefore

\[
\boxed{p\ge 11 \Longrightarrow \neg(p\mid M\ \text{and}\ p\mid M').}
\]

More precisely, after removing powers of 3,

\[
\boxed{
\gcd\!\left(
\frac{M}{3^{v_3(M)}},
\frac{M'}{3^{v_3(M')}}
\right)\in\{1,5,7\}.
}
\]

The exponent of a common factor 5 or 7 is at most one, since `v_5(15)=v_7(63)=1`.

Interpretation: apart from powers of 3 and the exceptional small primes 5 and 7, the large-prime support of two consecutive sampled states is disjoint. A hypothetical divergent sampled orbit must continually refresh its large prime factors.

## Two-step recurrence constraint

There is also a useful refinement. Write one induced branch as

\[
M_{j+1}=\frac{3^{q_j}}{2^{t_j}}(M_j+\eta_j).
\]

If a prime `p>=11` divides both `M_j` and `M_{j+2}`, then, modulo `p`,

\[
M_{j+1}\equiv \frac{3^{q_j}}{2^{t_j}}\eta_j,
\]

while `M_{j+2}=0 (mod p)` implies `M_{j+1}+eta_{j+1}=0 (mod p)`. Clearing the power of 2 gives

\[
\boxed{
p\mid 3^{q_j}\eta_j+2^{t_j}\eta_{j+1}.
}
\]

Hence recurrence of a large prime after one gap is possible only if that prime divides an explicit two-step S-unit correction integer. For any bounded-run subsystem there are only finitely many such two-step correction integers.

This does not by itself exclude an orbit, because new primes may continue to appear and old primes may recur after longer gaps. But it gives a concrete prime-turnover constraint that can be combined with bounded-run/finite-alphabet arguments or S-unit methods.