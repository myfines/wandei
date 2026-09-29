# First-contraction branch versus escape branch

Status: exploratory mathematics; no proof of Collatz is claimed.

Work with the odd-only Syracuse map

\[
S(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1).
\]

For a least odd counterexample seed \(N\), let

\[
A_k=\sum_{i<k} a_i,\qquad L=\log_2 3,
\]

and define the coefficient defect

\[
D_k=A_k\log 2-k\log 3.
\]

The exact logarithmic identity is

\[
\log\frac{x_k}{N}
= -D_k + \sum_{i<k}\log\left(1+\frac1{3x_i}\right).
\]

Since every state of a least counterexample satisfies \(x_i\ge N\), any prefix with \(D_k>0\) but \(x_k\ge N\) must satisfy

\[
D_k
\le \sum_{i<k}\log\left(1+\frac1{3x_i}\right)
< \frac{k}{3N}.
\]

Hence every coefficient-contracting non-descending prefix obeys the explicit upper bound

\[
\boxed{N<\frac{k}{3D_k}}.
\]

This gives a useful split:

1. **First-contraction branch.** Some prefix has \(D_k>0\). Then Diophantine approximations of \(\log_2 3\) determine the possible first lengths, and the above inequality gives an upper bound on \(N\).
2. **Escape branch.** No prefix has \(D_k>0\). In the critical-defect coordinate
   \[
   h_k=\lfloor k\log_2 3\rfloor-A_k,
   \]
   this means \(h_k\ge0\) for all \(k\). For a genuinely divergent orbit, the reciprocal/correction formulation instead drives \(h_k\to+\infty\). This is the moving-anchor / slow-escape branch.

## Mechanical correction upper envelope

Before the first coefficient contraction we have

\[
A_j\le \lfloor jL\rfloor.
\]

For a fixed terminal length \(k\), the odd-only affine correction is

\[
C_k=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}.
\]

Therefore it is termwise bounded by the critical mechanical envelope

\[
C_k\le C_{\rm mech}(k)
:=\sum_{j=0}^{k-1}3^{k-1-j}2^{\lfloor jL\rfloor}.
\]

If the first contraction has terminal exponent \(A\), then endpoint non-descent implies

\[
(2^A-3^k)N\le C_k\le C_{\rm mech}(k),
\]

so

\[
\boxed{
N\le \frac{C_{\rm mech}(k)}{2^A-3^k}.
}
\]

Writing \(\theta_j=\{jL\}\),

\[
C_{\rm mech}(k)=3^{k-1}\sum_{j<k}2^{-\theta_j}.
\]

Thus the bound is controlled by a Birkhoff sum for irrational rotation. Since

\[
\int_0^1 2^{-x}\,dx=\frac1{2\log 2},
\]

continued-fraction/Denjoy--Koksma bounds give an essentially exact finite estimate along convergent and semiconvergent lengths.

## First currently relevant Diophantine candidate

Using the conservative computational floor \(N\ge2^{71}\), the first upper approximation in the critical window is

\[
\frac{114208327604}{72057431991}>\log_2 3.
\]

For

\[
k=72057431991,\qquad A=114208327604,
\]

we have

\[
D=A\log2-k\log3
\approx 5.51089009576957\times10^{-12}.
\]

The crude correction bound gives

\[
N<\frac{k}{3D}\approx 2^{71.88431747}.
\]

Using the mechanical correction envelope and the rotation average tightens this to about

\[
\boxed{N\lesssim2^{71.41308384}}.
\]

For this semiconvergent, its denominator is the sum of two consecutive convergent denominators, so Denjoy--Koksma can make the rotation-sum estimate rigorous with only an \(O(1)\) additive error.

The current public computation frontier is about \(2^{71}\), so the first-contraction candidate is confined to a narrow factor of roughly \(1.33\) above the verified range. This does **not** handle the escape branch where the main coefficient never contracts.

## Local record-block experiment: an important negative result

Enumerating local defect-record blocks showed that a proposed lower bound of the form

\[
\rho_k\ge 3^{ck}
\]

for every local endpoint residue is false. Small residues can persist through longer local blocks. A concrete nested example is

\[
897\to673\to505\to379\to569\to427\to641\to481\to361\to271\to407\to611\to917.
\]

The same small endpoint residue can therefore occur for increasingly long local scripts. The reason this does not threaten least-counterexample arguments is that the chain passes through the much smaller state 271. Hence any future moving-anchor estimate must include the **global non-descent/minimality constraint**, not just local realizability modulo powers of 2 and 3.
