# Denjoy–Koksma bound for the first coefficient-contraction candidate

Status: rigorous reduction/formula; decimal evaluation is high-precision numerical unless separately interval-certified.

Let the odd-only Collatz/Syracuse orbit be

\[
x_{i+1}=\frac{3x_i+1}{2^{a_i}},\qquad A_j=\sum_{i<j}a_i.
\]

Assume a smallest positive odd counterexample `N`, and suppose the first prefix whose multiplicative coefficient contracts occurs at length `k`, with total exponent `A`:

\[
3^k<2^A,
\]

while for every `i<k`,

\[
3^i\ge 2^{A_i}.
\]

The exact affine identity is

\[
2^A x_k=3^kN+C_k,
\qquad
C_k=\sum_{i=0}^{k-1}3^{k-1-i}2^{A_i}.
\]

Since minimality gives `x_k>=N`,

\[
N\le \frac{C_k}{2^A-3^k}.
\]

Write `L=log_2 3`. Before the first contraction, `A_i<=floor(iL)`, hence

\[
C_k\le C_{\max}(k):=
\sum_{i<k}3^{k-1-i}2^{\lfloor iL\rfloor}
=3^{k-1}\sum_{i<k}2^{-\{iL\}}.
\]

For the first critical candidate

\[
(k,A)=(72057431991,114208327604),
\]

`A/k` is the intermediate convergent obtained by adding two consecutive convergents of `L`:

\[
(k,A)=(q_{22}+q_{21},p_{22}+p_{21}).
\]

Set `alpha={L}` and `f(x)=2^{-x}` on the circle. Its integral is

\[
\int_0^1f(x)\,dx=\frac1{2\ln2}.
\]

Using Denjoy–Koksma separately on the `q_22` and `q_21` blocks gives the safe bound

\[
\sum_{i<k}2^{-\{iL\}}
\le \frac{k}{2\ln2}+2,
\]

where `+2` is a conservative two-block bounded-variation error.

Therefore

\[
\boxed{
N\le
\frac{\frac{k}{2\ln2}+2}
{3\bigl(2^{A-k\log_2 3}-1\bigr)}
}.
\]

High-precision evaluation gives

\[
\log_2 N<71.4130838416\ldots
\]

for this first contraction candidate.

As of 2026-09-29, Barina's public verification page reports all starts below

\[
2075\cdot2^{60}\approx2^{71.0188956211}
\]

verified. Thus, if a least counterexample has its first coefficient contraction at this candidate, it is confined to approximately

\[
2^{71.0189}<N<2^{71.4131}.
\]

This does not resolve Collatz. It only sharpens the first-contraction branch. If this candidate is eliminated, the next positive continued-fraction candidate is much weaker numerically, so the no-contraction / slow-escape branch remains the main theoretical obstacle.
