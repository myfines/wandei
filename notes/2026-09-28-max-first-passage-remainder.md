# 2026-09-28 — Maximal first-passage remainder barrier

Status: structural lemma + high-precision numerical exploration. No proof of Collatz is claimed. The final decimal threshold should eventually be regenerated with directed interval arithmetic.

## Setup

Use the Terras map

\[
T(n)=\begin{cases}(3n+1)/2,&n\text{ odd},\\ n/2,&n\text{ even}.\end{cases}
\]

Suppose a smallest positive Collatz counterexample \(N\) exists. Let \(j\) be the first time at which the homogeneous coefficient drops below one, and let \(q\) be the number of odd entries among the first \(j\) terms. Put

\[
\alpha=\log_2 3.
\]

First passage implies

\[
j=\lfloor q\alpha\rfloor+1.
\]

Write the odd positions of the parity word, indexed from zero, as

\[
0=s_1<s_2<\cdots<s_q<j.
\]

The standard parity-vector characterization of coefficient first passage gives

\[
s_i\le \lfloor(i-1)\alpha\rfloor,\qquad 1\le i\le q.
\]

This is the same admissibility condition appearing in Terras/Winkler coefficient-stopping-time classes.

## Exact affine numerator

For a parity word with odd positions \(s_1,\ldots,s_q\),

\[
T^j(N)=\frac{3^qN+B}{2^j},
\qquad
B=\sum_{i=1}^{q}3^{q-i}2^{s_i}.
\]

Because \(N\) is the smallest counterexample, no iterate can fall below \(N\). In particular,

\[
T^j(N)\ge N,
\]

so

\[
N\le \frac{B}{2^j-3^q}. \tag{1}
\]

## Maximizing the remainder under first-passage constraints

Rozier–Terracol prove that, for fixed length and Hamming weight, shifting a 1 to the right increases the affine remainder (their unordered-majorization order, Lemma 2.3). Here the same conclusion also follows directly from the explicit formula for \(B\).

The latest simultaneously admissible odd positions are

\[
s_i^{\max}=\lfloor(i-1)\alpha\rfloor.
\]

Hence

\[
B\le B_{\max}(q)
=\sum_{i=1}^{q}3^{q-i}2^{\lfloor(i-1)\alpha\rfloor}.
\]

Letting \(r=i-1\), divide by \(3^q\):

\[
\frac{B_{\max}(q)}{3^q}
=\frac13\sum_{r=0}^{q-1}\frac{2^{\lfloor r\alpha\rfloor}}{3^r}
=\frac13\sum_{r=0}^{q-1}2^{-\{r\alpha\}}.
\]

Also, with

\[
\beta_q=j-q\alpha=1-\{q\alpha\},
\]

we have

\[
2^j-3^q=3^q(2^{\beta_q}-1).
\]

Combining with (1) gives the **maximal first-passage remainder barrier**

\[
\boxed{
N\le M_q:=
\frac{\frac13\sum_{r=0}^{q-1}2^{-\{r\alpha\}}}
{2^{\beta_q}-1}
},
\qquad
\beta_q=1-\{q\alpha\}. \tag{2}
\]

This is stronger than replacing every summand by 1, and it makes the arithmetic structure transparent: a possible huge minimal counterexample requires an exceptionally small one-sided approximation \(\beta_q\), while the numerator is a Birkhoff sum for an irrational rotation.

## Mean and Denjoy–Koksma control

For

\[
f(x)=2^{-x}\quad (0\le x<1)
\]

periodized on the circle,

\[
\mu:=\int_0^1f(x)\,dx=\frac1{2\ln2}.
\]

The periodized function has bounded variation (one may safely take total variation \(\le1\)). At a continued-fraction denominator \(Q\) of \(\alpha\), Denjoy–Koksma gives uniformly in the starting phase

\[
\left|\sum_{r=0}^{Q-1}f(x+r\alpha)-Q\mu\right|\le1.
\]

Therefore an Ostrowski decomposition of \(q\) into a small number of convergent denominators gives a constant-size error in the numerator of (2), rather than an error growing with \(q\).

## First candidate forced by the current verification scale

From the crossing-window note, using the published verification lower bound \(N>2^{71}\), the first upper approximation capable of fitting the necessary paradoxical window is

\[
\frac jq=
\frac{114208327604}{72057431991}.
\]

Its denominator decomposes as two adjacent continued-fraction denominators:

\[
72057431991
=65470613321+6586818670.
\]

Applying Denjoy–Koksma separately to these two blocks gives the convenient rigorous-form bound

\[
\sum_{r=0}^{q-1}2^{-\{r\alpha\}}
\le \frac{q}{2\ln2}+2. \tag{3}
\]

High-precision decimal evaluation of (2)-(3) gives

\[
M_q\lesssim 3.143983941787\times10^{21}
\approx1.331529\,2^{71}. \tag{4}
\]

Barina's live project page currently reports verification below

\[
2075\,2^{60}\approx1.01318\,2^{71}.
\]

Thus the first Diophantine first-passage candidate is numerically only about 31.4% above the live verified frontier. If the verified frontier ever exceeds the certified version of \(M_q\), this entire first candidate order is impossible, and the first crossing is forced to the next much rarer one-sided approximation.

## Why this is more interesting than the raw crossing-window bound

The harmonic-mean inequality only says that \(j/q\) must approximate \(\log_2 3\) extremely closely. Equation (2) additionally uses the **largest affine remainder compatible with first passage**. It therefore incorporates the actual parity-word geometry rather than only the number of odd entries.

There is still a major gap: (2) maximizes over all admissible first-passage words. The maximizing word has a unique residue modulo \(2^j\), and there is no reason its least positive representative should be anywhere near \(M_q\). This suggests the next target:

> Bound the largest remainder among first-passage words whose unique residue representative modulo \(2^j\) is at most \(M_q\).

Because \(j\approx1.14\times10^{11}\) while \(M_q\) is only about \(2^{71.65}\), any hypothetical minimal counterexample must correspond to an extraordinarily small representative inside an astronomically large \(2^j\)-period. This is where the 2-adic residue structure may provide much more leverage than density alone.

## Literature used

- O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349 (2026), 115167. In particular their unordered-majorization/remainder monotonicity and paradoxical-sequence bounds.
- M. Winkler, *Deterministic Structures in the Coefficient Stopping-Time Dynamics of the 3x+1 Problem*, arXiv:1709.03385v8 (2026), for the exact first-passage parity/residue characterization.
- Classical Denjoy–Koksma inequality for irrational rotations and bounded-variation observables.
- D. Barina, *Improved verification limit for the convergence of the Collatz conjecture*, J. Supercomputing 81 (2025), for the peer-reviewed \(2^{71}\) verification frontier.

## Caveat

The symbolic derivation through (3) is the intended rigorous route. The decimal value in (4) is currently generated with high-precision floating-point/Decimal arithmetic, not a formal directed-rounding proof. Before using the number as a theorem-level cutoff, replace it by a certified interval evaluation of \(\log 2\), \(\log 3\), \(2^{\beta_q}\), and the resulting quotient.
