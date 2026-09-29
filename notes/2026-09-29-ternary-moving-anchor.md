# Ternary moving-anchor criterion

Status: rigorous reduction plus finite experiments; not a Collatz proof.

This note sharpens the eventual-monotone critical-defect branch into a concrete 3-adic arithmetic target.

## Setup

For an odd-only Syracuse orbit

\[
x_{n+1}=\frac{3x_n+1}{2^{a_n}},\qquad A_n=\sum_{i<n}a_i,
\]

put

\[
L=\log_2 3,\qquad h_n=\lfloor nL\rfloor-A_n,
\qquad \theta_n=\{nL\}.
\]

The exact height identity is

\[
\log_2(x_n/x_0)=h_n+\theta_n+E_n,
\]

where

\[
E_n=\sum_{i<n}\log_2\left(1+\frac1{3x_i}\right).
\]

For a divergent nonperiodic positive orbit, reciprocal summability makes `E_n` converge to a finite limit `E_infinity`.

Assume the critical-defect coordinate is eventually nondecreasing.  Then eventually `a_n<=r_n`, where

\[
r_n=\lfloor(n+1)L\rfloor-\lfloor nL\rfloor\in\{1,2\},
\]

so the tail has only exponents 1 and 2.

## 1. Critical-density subsequence

López--Stoll's necessary condition for a rational 2-adic integer with a noncyclic trajectory puts the ordinary Terras parity density on the critical lower boundary

\[
\alpha=\frac{\log 2}{\log 3}=\frac1L.
\]

On a tail with `a_n in {1,2}`, arbitrary T-time prefixes differ from odd-step endpoints by at most one parity place.  At the odd endpoints the density is

\[
\frac{n}{A_n}
=
\frac1{L-(h_n+\theta_n)/n}.
\]

Since eventual monotonicity plus divergence gives `h_n>=0` eventually, the critical liminf forces a subsequence `n_j` with

\[
\boxed{h_{n_j}/n_j\to0.}
\]

Along that subsequence the height identity and bounded correction give

\[
x_{n_j}
\le x_0\,2^{1+E_\infty}\,2^{h_{n_j}}
=2^{o(n_j)}.
\]

## 2. The exponent script fixes the endpoint modulo 3^n

The exact affine identity is

\[
2^{A_n}x_n
=3^n x_0+C_n,
\]

with

\[
C_n=\sum_{j=0}^{n-1}3^{n-1-j}2^{A_j}.
\]

Therefore

\[
\boxed{
x_n\equiv
\rho_n:=2^{-A_n}C_n
\pmod{3^n}.
}
\]

The residue `rho_n` depends only on the finite exponent script `(a_0,...,a_{n-1})`, not on the particular seed.

For `n=n_j` large enough, `x_n=2^{o(n)}<3^n`.  Hence the actual endpoint is the least positive representative of this script-determined residue:

\[
\boxed{x_{n_j}=\rho_{n_j}^{(+)}=3^{o(n_j)}.}
\]

Equivalently, when written as an `n_j`-digit ternary residue (allowing leading zeros), `rho_{n_j}` has

\[
n_j-o(n_j)
\]

leading zero trits.

Thus any positive-integer counterexample in the eventual-monotone branch forces infinitely many extremely small 3-adic representatives produced by one-sided sparse perturbations of the fixed critical mechanical exponent word.

## 3. A much weaker sufficient arithmetic theorem

Full equidistribution is unnecessary.  It would suffice to prove:

> There is a constant `c>0` such that every sufficiently long admissible one-sided critical script has least positive endpoint representative
> \[
> \rho_n^{(+)}\ge3^{cn}.
> \]

Even an arbitrarily small fixed exponent `c` contradicts the required critical subsequence `rho_{n_j}=3^{o(n_j)}`.

A weaker variant sufficient for Collatz would only need this bound along every infinite admissible script, not uniformly over all finite scripts.

## 4. Exact 2-adic / 3-adic duality for a finite script

For a fixed exponent prefix, the exact seed class modulo `2^{A_n+1}` and endpoint class modulo `3^n` are two sides of the same affine identity.

If `N_n` is the least positive seed representative realizing the prefix exactly, and `rho_n` is the least positive endpoint representative of the residue above, then reversing the script from `rho_n` by

\[
y\mapsto\frac{2^a y-1}{3},\qquad a\in\{1,2\},
\]

recovers `N_n` exactly in the finite computations.  For exponents 1 and 2 the reverse exponent is determined by `y mod 3`:

- `y=2 mod 3` forces `a=1`;
- `y=1 mod 3` forces `a=2`.

So the endpoint residue encodes the whole bounded-exponent script by repeated reverse decoding.

This explains why the observed near-maximal 2-adic seed residues and near-maximal 3-adic endpoint residues are manifestations of the same arithmetic obstruction.

## 5. Finite experiment

Synthetic admissible scripts were generated with a target

\[
h_n\sim c\log_2 n,\qquad c>1,
\]

raising `h` only at allowed `r_n=2` positions.  These scripts satisfy the principal analytic escape constraints but are not claimed to come from positive integers.

For their endpoint residue modulo `3^n`, the observed normalized ternary logarithm

\[
\frac{\log_3\rho_n}{n}
\]

is close to 1 rather than 0.  Representative samples:

| target c | n | h_n | log_3(rho_n)/n |
|---:|---:|---:|---:|
| 1.1 | 100 | 7 | 0.9979 |
| 1.1 | 400 | 9 | 0.9992 |
| 1.5 | 100 | 9 | 0.9989 |
| 1.5 | 400 | 12 | 0.9999 |
| 2.0 | 200 | 15 | 0.9995 |
| 3.0 | 400 | 25 | 0.9998 |

So the scripts deliberately built to have sublinear critical defect produce residues almost as large as the full modulus `3^n`, whereas a genuine positive integer counterexample in this branch would need an infinite subsequence with exponentially tiny relative representatives.

This is evidence only.

## 6. Relation to known work

Stérin--Woods show that Collatz embeds a base-3/base-2 conversion algorithm, so a direct ternary-digit formulation is structurally natural.  Recent arithmetic-frontier work on Collatz-like exceptional-set methods also arrives at deterministic questions about powers of 2 in powers-of-3 residue windows.  The target here is narrower: one-sided perturbations of one fixed critical mechanical script, and only an exponential lower bound for the least representative is needed.

Potential tools:

- p-adic linear forms / Subspace-Theorem arguments;
- ternary digit complexity of powers of 2;
- Ostrowski/continued-fraction structure of the fixed mechanical word;
- Stérin--Woods base-conversion automata;
- or a direct lower-bound theorem for the exact prefix realizer.
