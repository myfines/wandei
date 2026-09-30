# Sharper uniform altitude bound on critical-boundary states

Status: exact consequence of the critical-defect product identity and the certified first-candidate seed bound. Not a Collatz proof.

For a preterminal state in the first coefficient-contraction branch,

\[
\frac{x_j}{N}
=2^{h_j+\theta_j}
\prod_{i<j}\left(1+\frac1{3x_i}\right).
\]

At a critical-boundary time \(h_j=0\), the certified correction-product estimate gives

\[
\frac{x_j}{N}
<2^{\theta_j}\frac{65}{64}
<2\frac{65}{64}
=\frac{65}{32}.
\]

The clean first-candidate seed ceiling is

\[
N<\frac43\,2^{71}.
\]

Therefore every preterminal boundary state satisfies

\[
\boxed{
x_j<\frac{65}{32}\frac43\,2^{71}
=\frac{65}{24}\,2^{71}.
}
\]

Equivalently,

\[
x_j<\frac{65}{48}\,2^{72}
\approx 2^{72.438\ldots}.
\]

This strictly improves the earlier coarse local certificate bound \(x_j<2^{73}\).

The finite boundary-run certificate should therefore enumerate local seed lifts only in

\[
2075\cdot2^{60}\le x_j<\frac{65}{24}2^{71}.
\]

This smaller exact interval may reduce the shortest mechanical-run length needed for a complete local descent certificate.
