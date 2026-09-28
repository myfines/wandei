# Critical-density certificate — 2026-09-28

## Status

This is a **necessary-condition result**, not a proof of the Collatz conjecture.

It sharpens the current least-counterexample program by combining:

1. the least-counterexample condition;
2. the exact affine form of a Collatz/Terras prefix;
3. the Rozier--Terracol harmonic-mean bound for paradoxical prefixes;
4. a rigorous continued-fraction certificate using exact rational bounds for logarithms.

The output is a very large lower bound on the first time at which a hypothetical least counterexample could even have multiplicative coefficient below one.

## 1. Prefix-density floor

Use the Terras map

\[
T(n)=\begin{cases}(3n+1)/2,&n\text{ odd},\\n/2,&n\text{ even}.\end{cases}
\]

For a length-\(j\) prefix starting at \(N\), let \(q_j\) be the number of odd terms among the first \(j\) iterates. The affine prefix has multiplicative coefficient

\[
C_j=\frac{3^{q_j}}{2^j}.
\]

Assume \(N\) has infinite stopping time, so \(T^j(N)\ge N\) for every \(j\ge1\). Set

\[
\alpha=\frac{\log2}{\log3},\qquad
\alpha_N=\frac{\log2}{\log(3+1/N)}.
\]

Then

\[
\boxed{\frac{q_j}{j}\ge\alpha_N\quad\text{for every }j.}
\]

If \(C_j\ge1\), this follows immediately from \(3^{q_j}\ge2^j\). If \(C_j<1\), the prefix is paradoxical because the actual orbit has not descended. Every odd term is at least \(N\), so its harmonic mean \(h\ge N\). Rozier--Terracol Corollary 4.3 gives

\[
\frac{q_j}{j}\ge\frac{\log2}{\log(3+h^{-1})}\ge\frac{\log2}{\log(3+N^{-1})}=\alpha_N.
\]

## 2. Critical window for a coefficient drop

For \(C_j<1\), we additionally need \(q_j/j<\alpha\). Thus every possible first coefficient drop must contain a rational number in

\[
\boxed{\alpha_N\le\frac{q_j}{j}<\alpha.}
\]

Taking only the conservative verified-size input \(N\ge2^{71}\), it suffices to study

\[
\frac{\log2}{\log(3+2^{-71})}\le\frac{q_j}{j}<\frac{\log2}{\log3}.
\]

The width is about \(8.10747\times10^{-23}\), but the certificate below does not rely on floating point.

## 3. Exact logarithm enclosure

For rational \(x>1\), put \(z=(x-1)/(x+1)\). Then

\[
\log x=2\sum_{n=0}^{\infty}\frac{z^{2n+1}}{2n+1}.
\]

After \(M\) terms, all omitted terms are positive and

\[
0<R_M\le\frac{2z^{2M+1}}{(2M+1)(1-z^2)}.
\]

For \(x=2\), \(x=3\), and \(x=3+2^{-71}\), both \(z\) and this remainder bound are rational. Therefore `src/critical_window.py` encloses all three logarithms, and hence both endpoints of the critical window, with exact `Fraction` arithmetic.

## 4. Continued-fraction certificate

The certified outer enclosure for the critical window has endpoint continued fractions sharing 23 partial quotients. Their first differing partial quotients are 10 and 9.

The standard continued-fraction interval theorem then gives the minimum-denominator rational in the enclosing interval by appending

\[
\min(10,9)+1=10
\]

to the common prefix. It is

\[
\boxed{\frac{72057431991}{114208327604}.}
\]

The program separately verifies, using the inner rigorous endpoint bounds, that this rational lies in the true critical window. Consequently no rational with denominator below

\[
\boxed{114208327604}
\]

can lie in the true window.

Hence, subject to \(N\ge2^{71}\),

\[
\boxed{j<114208327604\implies\frac{3^{q_j}}{2^j}\ge1.}
\]

Equivalently, a hypothetical least counterexample cannot have a coefficient-stopping-time before 114,208,327,604 Terras steps.

This does **not** say its actual value has not fluctuated upward; the positive affine correction is still present. It only excludes a multiplicative coefficient below one during that range.

## 5. Why this still does not prove Collatz

A hypothetical unbounded orbit might keep

\[
\frac{3^{q_j}}{2^j}\ge1
\]

for arbitrarily long, or forever, while its parity density approaches the critical slope from above. Therefore paradoxical-prefix arguments alone do not cover every possible counterexample.

The useful change of viewpoint is: do not search all parity words; search only ordinary-positive-integer parity words that remain above the least-counterexample floor and stay extremely close to the critical line.

## 6. Next bridge to attack

Let

\[
e_j=q_j-\alpha j.
\]

An unbounded counterexample is forced into a narrow regime in which the average excess \(e_j/j\) is small, but \(e_j\) need not be bounded.

Purely mechanical/Sturmian itineraries are not enough: recent formal experiments already exclude broad mechanical families without obtaining ordinary-integer coverage.

The next target is therefore

\[
\boxed{\text{critical-density integer orbit}+\text{fixed }2^t\text{-residue reconstruction}+\text{reverse }3\text{-adic barriers}\Longrightarrow\text{finite defect / return / descent}.}
\]

A concrete route is to compare a long critical-density parity prefix with the nearest mechanical word. If the number of defects is small, finite-defect return certificates may apply. If the number of defects is large, try to show that the resulting displacement forces either a reverse ancestor below the least counterexample or enough multiplicative drift to leave the critical window.

The missing theorem is a **coverage dichotomy** between those two regimes.
