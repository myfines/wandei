# RS carry automaton and exact binary transition balance
2026-11-25. Elementary lemmas and obstruction results, NOT a proof of Collatz. Originality not established.

## 1. Exact full-adder / latch representation

For a positive odd n, write its binary digits b_j, padded with zeros above the most significant digit, and put b_{-1}=0. Incorporate the added 1 into the initial carry c_0=1 (unlike the alternative convention c_0=0 and an explicit +1 at position 0). Then for every j>=0,
\[
b_j+b_{j-1}+c_j=d_j+2c_{j+1},
\]
where d_j are the digits of 3n+1. All carries are Boolean. Define t_j=b_j XOR b_{j-1}, u_j=c_{j+1} XOR c_j. Then
\[
d_j=t_j\oplus c_j,\qquad
c_{j+1}=\begin{cases} b_j&t_j=0,\\c_j&t_j=1.\end{cases}
\]
Consequently \(t_j u_j=0\). The state transition behaves like an RS latch: 00 resets, 11 sets, 01/10 holds. This is a logical analogy, not a claim that the circuit requires only two gates.

For \(q_j=b_j\oplus c_j\), one also has
\[
d_j=b_{j-1}\oplus q_j,\qquad
q_{j+1}=t_{j+1}\oplus(t_jq_j).
\]
An input alternating run therefore transmits the same carry and produces constant output digits.

## 2. Exact transition-block theorem

Define \(J(n)=\sum_{j\ge0}(b_j\oplus b_{j-1})\), counting both zero-padded boundaries; it is twice the number of runs of 1 digits in n. Let the finite 1-blocks of the transition word t, in low-to-high order, have lengths \(l_1,\ldots,l_B\). Each is followed by a zero gap of length \(z_i\ge1\), with \(z_B=\infty\) for the final padded gap. Set
\[
e_1=1-(l_1\bmod2),\qquad e_i=l_i\bmod2\ (i>1),
\quad \eta_i=\begin{cases}-1&z_i=1,\\1&z_i\ge2.\end{cases}
\]
Here \(e_i\) indicates whether the carry flips at the first zero of gap i.

**Theorem.** For \(U(n)=(3n+1)/2^{v_2(3n+1)}\),
\[
\boxed{v_2(3n+1)=l_1,\qquad J(U(n))=2B-1+\sum_{i=1}^B e_i\eta_i.}
\]

**Proof.** Since n is odd, t_0=1 and c_0=1. Throughout the first 1-block the carry remains 1 and all output bits are 0. At its following first zero the output bit is 1, proving the valuation formula. After any zero in t, the carry equals the input bit at that position. Thus before each subsequent 1-block, the carry equals the bit preceding that block. The input bit flips at each position of the block, so a carry flip in its following gap occurs exactly when its length is odd. For the first block the carry starts opposite to b_{-1}=0, so the parity criterion is reversed.

At each 1->0 boundary of t, the output d flips, contributing B. At a 0->1 boundary it normally flips, contributing B-1 across all finite gaps, except when the gap has length 1 and its carry flips, in which case the output does not flip. A carry flip in a gap of length at least 2 adds one internal output transition. There are no other output transitions: inside a 1-block the carry is constant, and after the first position of a zero gap it is constant. Since d_0=0, no lower boundary transition is omitted; upper padding is included. Division by a power of 2 preserves J. This proves the formula.

## 3. Local balance and a conditional descent rule

Because \(J(n)=\sum_i l_i\), the exact balance is
\[
J(U(n))-J(n)=(1-l_1+e_1\eta_1)+
\sum_{i=2}^B(2-l_i+e_i\eta_i).
\]

The initial contribution is at most \(-2\lfloor(l_1-1)/2\rfloor\). Every later contribution is nonpositive except for \(l_i=1,z_i\ge2\), in which case it is +2. In particular \(l_i=2\) contributes zero, and \(l_i=3\) contributes zero or -2. Let \(I(n)=\#\{i\ge2:l_i=1,z_i\ge2\}\). Then
\[
\boxed{\frac{J(U(n))-J(n)}2\le I(n)-\left\lfloor\frac{v_2(3n+1)-1}{2}\right\rfloor.}
\]
If \(I(n)=0\) and the valuation is at least 3, the number of runs of 1 strictly decreases. This is only a conditional descent: \(I(n)\) may be positive, e.g. n=7 -> 11 increases the run count. The alternating word n=21 -> 1 decreases it from 3 to 1.

For any finite orbit, summing gives a necessary budget inequality
\[
\sum_{j<k}\left\lfloor\frac{a_j-1}{2}\right\rfloor
\le \frac{J(n_0)-J(n_k)}2+\sum_{j<k}I(n_j).
\]
In a cycle the endpoint term disappears. The inequality does not alone exclude cycles or escape.

Exact integer test: the block theorem was checked on all 100,000 positive odd integers below 200,000; zero mismatches. This supplements, rather than replaces, the proof.

## 4. No-go theorem for translation-invariant quadratic Fourier potentials

Let w be a nonzero nonnegative integrable weight (nonzero in L1), \(r_j=(2\pi)^{-1}\int w(\theta)\cos(j\theta)d\theta\), and
\[
E_w(n)=(2\pi)^{-1}\int w(\theta)|P_n(e^{i\theta})|^2d\theta.
\]
Let L(n) be binary length. No real lambda makes \(V=E_w+\lambda L\) strictly decrease under U on every odd n>1.

Indeed, for n=2^k-1, k>=3, U(n)=3*2^(k-1)-1, the energy difference is \(2(r_k-r_1)\) and length increases by 1. For n=2^k+1, U(n)=3*2^(k-2)+1, the difference is \(r_0+2r_1+2r_{k-2}+2r_{k-1}-2r_k\), and length decreases by 1. Taking k->infinity using Riemann-Lebesgue forces
\(r_0+2r_1\le\lambda\le2r_1\), contrary to \(r_0>0\).
This does not rule out multistep, nonlinear, boundary-sensitive or carry-dependent potentials.

Also, for the cycle ratio G(X) in the preceding derivative note, every summand is strictly decreasing on X>0 because all a_j>=1 and P has nonnegative coefficients. Searching for a second positive root is therefore not a viable strategy.

## 5. Next target

Track how isolated transition blocks with long zero gaps are created or annihilated by the next latch iteration. Seek an independent amortized bound on their total creation, or a proper well-founded potential based on transition blocks, their lengths, and carry state. The exact balance localizes all positive run-count contributions but does not control them across time. Do not confuse finite transducer state with a finite global state space: the binary word can grow without bound.
