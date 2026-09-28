# 2026-09-28 — Paradoxical crossing window

Status: exploratory but the inequalities below are direct consequences of published results plus the minimal-counterexample assumption. No proof of Collatz is claimed.

## Literature input

Rozier–Terracol, *Paradoxical behavior in Collatz sequences* (Discrete Mathematics 349, 2026; arXiv:2502.00948) use the modified Collatz/Terras map

\[
T(n)=\begin{cases}(3n+1)/2,&n\text{ odd},\\ n/2,&n\text{ even}.\end{cases}
\]

For a length-\(j\) prefix containing \(q\) odd terms, they write

\[
T^j(n)=\frac{3^q}{2^j}n+E_j(n).
\]

Their Theorem 4.2 / Corollary 4.3 imply that if the prefix is paradoxical, i.e.

\[
3^q<2^j,\qquad T^j(n)\ge n,
\]

and \(h\) is the harmonic mean of the odd terms before the endpoint, then

\[
2^j\le (3+h^{-1})^q.
\]

Barina, *Improved verification limit for the convergence of the Collatz conjecture*, J. Supercomputing 81 (2025), verifies every starting value below \(2^{71}\).

## Minimal-counterexample specialization

Assume a smallest positive counterexample \(N\) exists. It is odd. Every odd term on its forward orbit is at least \(N\), otherwise a smaller counterexample exists.

Consider a prefix of the orbit whose Terras-map length is \(j\), with \(q\) odd terms, for which the coefficient first (or later) satisfies \(3^q/2^j<1\). Since the orbit never falls below \(N\), this prefix is paradoxical. Its odd-term harmonic mean satisfies

\[
h\ge N.
\]

Therefore

\[
\boxed{3^q<2^j\le(3+N^{-1})^q.}
\]

Equivalently, with \(\alpha=\log_2 3\),

\[
\boxed{0<\frac jq-\alpha\le \log_2\left(1+\frac1{3N}\right).}
\]

Call this the **crossing-window lemma**.

In odd-only Syracuse notation, if \(a_i=v_2(3x_{i-1}+1)\) and
\(A_q=a_1+\cdots+a_q\), then \(j=A_q\). Thus every positive crossing

\[
A_q-q\log_2 3>0
\]

must lie in the extremely thin window above.

## Consequence from the verified lower bound

Barina gives \(N>2^{71}\) for any counterexample. Hence

\[
0<\frac jq-\log_2 3
\le
\log_2\left(1+\frac1{3\cdot2^{71}}\right)
\approx 2.0366837207889\times10^{-22}.
\]

A continued-fraction / one-sided semiconvergent search for \(\log_2 3\) shows that the first upper rational approximation entering this window is

\[
\boxed{\frac jq=\frac{114208327604}{72057431991}.}
\]

The preceding best upper approximation relevant here is

\[
\frac{10439860591}{6586818670},
\]

whose error is about \(2.21724\times10^{-21}\), too large. The successful semiconvergent has error about

\[
1.10336\times10^{-22}.
\]

Therefore, if the coefficient stopping time of the minimal counterexample is finite, its first coefficient crossing cannot occur before

- \(q=72,057,431,991\) odd terms, and
- \(j=114,208,327,604\) Terras-map iterations.

The script `src/cf_window.py` reproduces this computation.

## Why this may matter

For every earlier odd-prefix length \(q<72,057,431,991\), one must have

\[
A_q\le\lfloor q\log_2 3\rfloor.
\]

So a hypothetical minimal counterexample must follow an extraordinarily long exponent path that never crosses the irrational line \(A= q\log_2 3\). This converts the problem into a constrained lattice-path / 2-adic realization problem.

The next attack is to combine this prefix constraint with the existing reverse \(3\)-adic barriers in this repository. A useful target would be a finite-state or transfer-operator certificate showing that no positive integer residue can realize such a long no-crossing path while also satisfying every reverse-ancestor barrier.

## Caveat

The continued-fraction computation is a numerical certificate generator, not yet a formally verified proof artifact. The one-sided best-approximation statement used to infer minimal denominator is standard continued-fraction theory; a future version should export exact interval bounds for \(\log_2 3\) and a machine-checkable certificate.
