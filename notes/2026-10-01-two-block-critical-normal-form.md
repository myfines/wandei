# Two-block critical normal form for sampled Collatz returns

Status: exact reduction for the two sampled first-return blocks closest to coefficient 1. This does **not** prove Collatz; it isolates a canonical hardest-looking two-letter subsystem.

Let

\[
c_- = \frac{3^5}{2^8}=\frac{243}{256}<1,
\qquad
c_+ = \frac{3^7}{2^{11}}=\frac{2187}{2048}>1.
\]

Both arise from the same sampled induced branch with shift \(\eta=15\), so the corresponding sampled map is

\[
M_{j+1}=c_{\pm}(M_j+15),
\qquad M_j=4n_j+1.
\]

Suppose the first \(j\) sampled blocks use the expanding block \(c_+\) exactly \(P_j\) times. Then

\[
C_j:=\prod_{i<j}c_i
=\left(\frac{243}{256}\right)^j\left(\frac98\right)^{P_j}.
\]

Set \(L=\log_2 3\) and

\[
\lambda:=\log_2\frac98=2L-3>0.
\]

The zero-drift expanding-block frequency is

\[
p=\frac{8-5L}{2L-3}=0.4424745961808629\ldots
\]

because

\[
(1-p)(5L-8)+p(7L-11)=0.
\]

Hence there is an exact identity

\[
\boxed{\log_2 C_j=\lambda(P_j-pj).}
\]

Therefore a sampled-noncontracting tail (all cumulative coefficients \(C_j\ge1\)) satisfies

\[
\boxed{P_j\ge \lceil pj\rceil\quad\text{for every }j.}
\]

Thus the minimal admissible two-letter schedule is the upper mechanical/Sturmian word of slope \(p\).

Now write

\[
D_j:=P_j-\lceil pj\rceil\ge0.
\]

Then

\[
\log_2 C_j
=\lambda\bigl(D_j+\lceil pj\rceil-pj\bigr),
\]

so

\[
\left(\frac89\right)^{D_j+1}
\le \frac1{C_j}
\le \left(\frac89\right)^{D_j}.
\]

Consequently

\[
\boxed{\sum_j\frac1{C_j}<\infty
\iff
\sum_j\left(\frac89\right)^{D_j}<\infty.}
\]

If critical density is retained along the tail, then \(D_j=o(j)\). Thus any surviving two-block escape script must be a sparse but unbounded upward perturbation of the critical mechanical word: \(D_j\ge0\), sublinear, yet large enough for \(\sum(8/9)^{D_j}\) to converge.

The sampled affine recurrence telescopes exactly:

\[
\frac{M_J}{C_J}=M_0+15\sum_{j<J}\frac1{C_j}.
\]

In \(\mathbb Q_2\), the left side tends to zero because its 2-adic valuation tends to infinity. Hence

\[
\boxed{
-\frac{M_0}{15}
=
\sum_{j\ge0}
\left(\frac{256}{243}\right)^j
\left(\frac89\right)^{P_j}
\quad(\mathbb Q_2).
}
\]

Substituting \(P_j=\lceil pj\rceil+D_j\) gives a concrete sparse-defect Hecke--Mahler-type rationality problem:

\[
\boxed{
-\frac{M_0}{15}
=
\sum_{j\ge0}
\left(\frac{256}{243}\right)^j
\left(\frac89\right)^{\lceil pj\rceil+D_j}.
}
\]

The same series also converges in \(\mathbb R\) exactly when \(\sum (8/9)^{D_j}<\infty\). The unresolved arithmetic question is whether such a sparse, sublinear defect perturbation can make this 2-adic value rational (indeed a negative rational with numerator tied to a positive integer sampled seed).

This is a candidate boundary object: the unperturbed mechanical schedule has bounded cumulative drift and cannot satisfy the required sampled correction summability; a true escape script must add infinitely many defects, but only at zero density if it remains critical.
