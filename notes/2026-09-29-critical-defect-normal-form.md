# Critical-defect normal form

Let the odd-only Collatz/Syracuse orbit be

\[
x_{n+1}=\frac{3x_n+1}{2^{a_n}},\qquad a_n=v_2(3x_n+1),
\]

with \(x_0=N\), and define

\[
A_n=\sum_{i<n}a_i,
\qquad
L=\log_2 3,
\qquad
\theta_n=\{nL\},
\qquad
h_n=\lfloor nL\rfloor-A_n.
\]

Then the standard affine expansion

\[
2^{A_n}x_n
=
3^nN+
\sum_{j=0}^{n-1}3^{n-1-j}2^{A_j}
\]

can be rewritten exactly as

\[
\boxed{
 x_n=2^{h_n+\theta_n}
 \left(
 N+\frac13\sum_{j<n}2^{-h_j-\theta_j}
 \right)
 }.
\]

Define

\[
B_n=N+\frac13\sum_{j<n}2^{-h_j-\theta_j}.
\]

Then

\[
x_n=2^{h_n+\theta_n}B_n,
\qquad
B_{n+1}=B_n\left(1+\frac1{3x_n}\right).
\]

Consequences:

1. Since \(1\le 2^{\theta_n}<2\), the series \(\sum 2^{-h_n-\theta_n}\) converges iff \(\sum 2^{-h_n}\) converges.

2. \(B_n\) converges iff \(\sum 2^{-h_n}\) converges.

3. Because
   \[
   \frac1{x_n}=\frac{2^{-h_n-\theta_n}}{B_n},
   \]
   and \(B_n\ge N>0\), while convergence of \(\sum 1/x_n\) implies convergence of the product \(\prod(1+1/(3x_n))\) and hence bounded \(B_n\), one obtains
   \[
   \boxed{
   \sum_{n\ge0}\frac1{x_n}<\infty
   \iff
   \sum_{n\ge0}2^{-h_n}<\infty.
   }
   \]

4. Therefore reciprocal-summability forces
   \[
   \boxed{h_n\to+\infty.}
   \]
   In this coordinate, a genuinely escaping orbit is a critical mechanical drift plus a defect backlog that tends permanently to \(+\infty\).

5. If \(h_n\) is eventually nondecreasing, then \(2^{-h_n}\) is eventually nonincreasing and summable, hence
   \[
   n2^{-h_n}\to0,
   \]
   so
   \[
   \boxed{h_n-\log_2 n\to+\infty.}
   \]

6. Since
   \[
   h_{n+1}-h_n=r_n-a_n,
   \qquad
   r_n=\lfloor(n+1)L\rfloor-\lfloor nL\rfloor\in\{1,2\},
   \]
   every upward jump of \(h\) is exactly \(+1\) and must occur at
   \[
   \boxed{r_n=2,\ a_n=1.}
   \]

This note does not prove Collatz. It packages the affine correction, reciprocal summability, and critical defect into a single exact normal form for later use in the moving-anchor / 2-adic–3-adic analysis.
