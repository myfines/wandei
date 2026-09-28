# Low-band balance and weighted-swap direction — 2026-09-28

Status: exact necessary conditions for a hypothetical least positive Collatz counterexample; **not a proof**.

We use the odd-only Syracuse map

\[
S(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1),
\]

and assume a least positive counterexample \(N\) exists.

## 1. Low band forces the alphabet \(\{1,2\}\)

The side-branch lemma proved earlier gives

\[
x\ge 4^{\lfloor(a-1)/2\rfloor}N+
\frac{4^{\lfloor(a-1)/2\rfloor}-1}{3}.
\]

Hence every odd orbit state with

\[
N\le x\le 4N
\]

has

\[
a(x)\in\{1,2\}.
\]

The two branches are

\[
F_1(x)=\frac{3x+1}{2},\qquad
F_2(x)=\frac{3x+1}{4}.
\]

They satisfy

\[
F_1(x)+1=\frac32(x+1),
\qquad
F_2(x)-1=\frac34(x-1).
\]

Consequently a fully low-band block cannot contain four consecutive 1's or five consecutive 2's.

## 2. Every low subblock has almost critical density

Take any contiguous block

\[
N\le x_0,x_1,\ldots,x_k\le4N
\]

and let \(r\) be the number of indices with exponent \(a_i=1\). Since all exponents are 1 or 2,

\[
A=\sum_{i=0}^{k-1}a_i=2k-r.
\]

The exact product formula is

\[
\frac{x_k}{x_0}
=\frac{3^k}{2^A}
\prod_{i=0}^{k-1}\left(1+\frac1{3x_i}\right).
\]

Because \(x_i\ge N\) and both endpoints lie in \([N,4N]\),

\[
\frac14\le\frac{x_k}{x_0}\le4.
\]

Using the lower estimate obtained by dropping the correction product gives

\[
\frac{3^k}{2^A}<4,
\]

hence

\[
r<(2-\log_2 3)k+2.
\]

Using

\[
\prod_i\left(1+\frac1{3x_i}\right)
\le
\left(1+\frac1{3N}\right)^k
\]

and \(x_k/x_0\ge1/4\) gives

\[
2^A\le 4(3+1/N)^k,
\]

and therefore

\[
r\ge
\bigl(2-\log_2(3+1/N)\bigr)k-2.
\]

Thus every contiguous low-band subblock obeys

\[
\boxed{
\bigl(2-\log_2(3+1/N)\bigr)k-2
\le r<
(2-\log_2 3)k+2.
}
\]

Let

\[
p=2-\log_2 3=0.415037499\ldots.
\]

For the known lower bound \(N>2^{71}\), the two slopes differ by only \(O(1/N)\). For any subblock length \(k\le N\), two equal-length low factors differ in the number of 1's by at most 4. So a long low excursion is a uniformly finite-balanced binary word pinned to the irrational slope \(p\).

## 3. A sharpened mod-8 character bias

Inside the low band, \(a=2\) occurs exactly when

\[
x\equiv1\pmod8,
\]

while \(a=1\) occurs for \(x\equiv3,7\pmod8\); the forbidden class \(5\pmod8\) would have \(a\ge3\).

Therefore, on a long low block, the frequency of residue \(1\pmod8\) is approximately

\[
1-p=\log_2 3-1=0.584962500\ldots.
\]

For the three nontrivial real Dirichlet characters modulo 8,

\[
1_{x\equiv1(8)}
=\frac14\bigl(1+\chi_{-4}(x)+\chi_8(x)+\chi_{-8}(x)\bigr).
\]

Hence if a low block has length \(k\) and \(r_2\) states with \(a=2\), then

\[
\sum_{\chi\in\{\chi_{-4},\chi_8,\chi_{-8}\}}
\sum_{i<k}\chi(x_i)=4r_2-k.
\]

The density estimate above gives, up to the explicit \(O(1/k)+O(k/N)\) endpoint error,

\[
\max_\chi\frac1k\left|\sum_{i<k}\chi(x_i)\right|
\gtrsim
\frac{4(\log_2 3-1)-1}{3}
=0.4466166\ldots.
\]

Thus a long low-band counterexample segment carries a very large multiplicative-character bias. This is much stronger than merely observing that the residue class 5 mod 8 is absent.

## 4. Important warning from combinatorics on words

Finite balance is **not** enough to conclude that a word is Sturmian or mechanical. The classical equivalence is for binary **1-balanced** aperiodic words. Our bound is roughly 4-balanced.

Bounded abelian complexity / finite letter-balance still allows substantially richer symbolic dynamics. So the implication

\[
\text{low band}\Rightarrow\text{mechanical word}
\]

would be unjustified.

This matches the current formal Collatz proof programs: globally mechanical itineraries and finite-defect near-periodic words can be excluded, but the missing step is a genuine coverage theorem forcing ordinary integer trajectories into one of those classes.

## 5. Weighted adjacent swaps

The next useful structure is that order changes the affine correction even when the counts of 1 and 2 are fixed:

\[
F_2(F_1(x))=\frac{9x+5}{8},
\qquad
F_1(F_2(x))=\frac{9x+7}{8}.
\]

Therefore swapping a local word \(12\) to \(21\) increases the state after those two steps by exactly \(1/4\).

If a suffix \(S\) of length \(m\) and total exponent \(A_S\) follows the swapped pair, then the final endpoint difference is exactly

\[
\boxed{
\Delta_S=\frac14\frac{3^m}{2^{A_S}}.
}
\]

So deviations from an ordered/mechanical template carry **weighted affine costs**. The weight is the multiplicative drift of the suffix.

This suggests the next target:

> prove a complexity-vs-defect dichotomy for low-band words. Either the word has few weighted swaps and is close enough to a mechanical/finite-defect template to invoke an existing return certificate, or it has many weighted swaps and the accumulated affine correction forces it out of the low band.

This is more specific than the earlier generic "show low-band frequency is small" target and directly addresses the known coverage gap.

## 6. Relation to existing work

Applegate--Lagarias found that modified 3x+1 semigroup descent certificates cover every class mod 4096 except \(-1\bmod4096\), with the nested \(-1\bmod2^j\) classes being the persistent 2-adic obstruction. Their semigroup moves are not actual Collatz orbit steps, so this does not by itself contradict a least counterexample, but it reinforces that the hard exceptional structure is strongly 2-adic.

Recent formal proof experiments have independently established exact adjacent-swap identities and finite-defect return certificates, while explicitly listing "ordinary integer coverage" / a complexity-versus-defect dichotomy as still missing. The low-band balance lemma above is a candidate new input for that missing bridge.
