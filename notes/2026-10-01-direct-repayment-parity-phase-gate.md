# Odd-height direct repayments at r=2 require the extreme phase window

Status: exact consequence of the side-branch altitude lemma and the certified first-candidate correction-product bound. Not a Collatz proof.

Assume the first coefficient-contraction candidate. Write

\[
h_n=\lfloor n\log_2 3\rfloor-A_n,\qquad
\theta_n=\{n\log_2 3\},\qquad
r_n\in\{1,2\}.
\]

Before the terminal contraction,

\[
\frac{x_n}{N}
=2^{h_n+\theta_n}
\prod_{i<n}\left(1+\frac1{3x_i}\right)
<2^{h_n+\theta_n}\frac{65}{64}.
\]

Suppose a single step repays the entire current defect height, so

\[
h_{n+1}=0.
\]

Since \(h_{n+1}=h_n+r_n-a_n\), this requires

\[
a_n=h_n+r_n.
\]

The side-branch altitude lemma says that if

\[
s=\left\lfloor\frac{a_n-1}{2}\right\rfloor,
\]

then

\[
x_n\ge4^sN+\frac{4^s-1}{3}>4^sN.
\]

Combining the two inequalities gives the necessary phase condition

\[
2^{h_n+\theta_n}\frac{65}{64}>2^{2s},
\]

hence

\[
\boxed{\theta_n>2s-h_n+\log_2(64/65).}
\]

Now specialize to an odd positive height \(h_n=2m+1\) and a mechanical \(r_n=2\) location. Direct repayment requires

\[
a_n=h_n+2=2m+3,
\]

so \(s=m+1\). Therefore

\[
2s-h_n=1
\]

and every such direct repayment must satisfy

\[
\boxed{
\theta_n>1+\log_2(64/65)
=\log_2(128/65)
=0.9776321869\ldots
}.
\]

Thus the earlier height-one phase gate is not special to height one:

\[
\boxed{
h_n\text{ odd},\ r_n=2,\ h_{n+1}=0
\Longrightarrow
\theta_n>\log_2(128/65).
}
\]

So every odd-height one-step return to the critical boundary occurring at an \(r=2\) phase is confined to the same top roughly 2.24% of the rotation circle.

For comparison, the elementary side-branch bound alone gives no nontrivial phase restriction for even-height direct repayments or for odd-height direct repayments at \(r=1\); their resulting threshold is nonpositive. Therefore the next counting argument must distinguish repayment parity and cannot simply multiply the 2.24% phase measure by the total excursion count.

This parity classification prevents an invalid overcount and identifies the exact class of boundary returns on which the phase gate can be used.
