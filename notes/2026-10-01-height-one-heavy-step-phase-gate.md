# Height-one heavy steps require an extreme rotation phase

Status: exact consequence of the side-branch altitude lemma plus the first-candidate correction bound. Not a Collatz proof.

Assume the first coefficient-contraction candidate and write

\[
h_n=\lfloor n\log_2 3\rfloor-A_n,
\qquad
\theta_n=\{n\log_2 3\}.
\]

For every preterminal state,

\[
\frac{x_n}{N}
=2^{h_n+\theta_n}
\prod_{i<n}\left(1+\frac1{3x_i}\right).
\]

Using `N>=2075*2^60` and `n<k=72057431991`, the correction product satisfies the already certified bound

\[
\prod_{i<n}\left(1+\frac1{3x_i}\right)<\frac{65}{64}.
\]

Now suppose

\[
h_n=1
\]

and the Syracuse exponent at this step is heavy,

\[
a_n\ge3.
\]

The side-branch altitude lemma forces

\[
x_n\ge4N+1>4N.
\]

But the critical-defect formula gives

\[
\frac{x_n}{N}
<2^{1+\theta_n}\frac{65}{64}.
\]

Therefore a necessary condition for any heavy step at height one is

\[
2^{1+\theta_n}\frac{65}{64}>4,
\]

or equivalently

\[
\boxed{
\theta_n>\log_2\frac{128}{65}
=0.9776321869\ldots
}.
\]

Thus a height-one repayment using `a>=3` can occur only in the top roughly `2.24%` of the irrational-rotation phase circle.

In particular, outside this very small phase window every `h=1` step is light:

\[
\boxed{h_n=1,\ \theta_n\le\log_2(128/65)\Longrightarrow a_n\in\{1,2\}.}
\]

For defect bookkeeping this means that a drop `h=1 -> 0` at a mechanical `r_n=2` location, which requires `a_n=3`, is forbidden except in this extreme phase window. Away from it, height-one defect units can only be repaid at an `r_n=1` location via `a_n=2`.

This gives an exact arithmetic gate on one of the two repayment mechanisms and is intended for the finite-state defect-excursion analysis.