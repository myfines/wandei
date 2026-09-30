# First 46 odd steps already exclude the pure mechanical ceiling script

Status: exact finite congruence consequence inside the first coefficient-contraction window. Not a Collatz proof.

Let

\[
L=\log_2 3
\]

and consider the critical mechanical odd-only exponent word

\[
\boxed{
a_j=\lfloor (j+1)L\rfloor-\lfloor jL\rfloor\in\{1,2\}.
}
\]

For `j<=46`, the floors can be computed exactly without floating point via

\[
\lfloor j\log_2 3\rfloor
=\operatorname{bitlength}(3^j)-1.
\]

The first 46 exponents are

`1,2,1,2,1,2,2,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1,2,2,1,2,1,2,1,2,2,1,2,1`

and

\[
\boxed{A_{46}=72.}
\]

## Exact seed congruence

For a fixed odd-only exponent prefix `a_0,...,a_{n-1}`, let

\[
A_m=\sum_{i<m}a_i.
\]

The exact affine identity is

\[
2^{A_n}x_n=3^nN+d_n,
\]

where

\[
d_0=0,
\qquad
d_{m+1}=3d_m+2^{A_m}.
\]

Requiring the endpoint `x_n` to be odd gives

\[
3^nN+d_n\equiv2^{A_n}\pmod{2^{A_n+1}},
\]

so the starting seed is uniquely determined modulo `2^(A_n+1)`:

\[
\boxed{
N\equiv
3^{-n}(2^{A_n}-d_n)
\pmod{2^{A_n+1}}.
}
\]

For the 46-step critical mechanical word above, `A_46=72`, so the prefix fixes `N` modulo `2^73`. The least positive residue is

\[
\boxed{
N_{\rm mech}=4697939311072332635131.
}
\]

Its binary logarithm is

\[
\boxed{
\log_2N_{\rm mech}=71.99251806907955\ldots
}
\]

## Comparison with the first-contraction window

For the first continued-fraction coefficient-contraction candidate

\[
(k,A_k)=(72057431991,114208327604),
\]

the rigorous Denjoy--Koksma correction ceiling derived earlier gives

\[
\boxed{N<2^{71.413083842}.}
\]

But

\[
N_{\rm mech}
>2^{71.9925}
>2^{71.413083842}.
\]

Therefore no seed inside the surviving first-contraction window can begin with the pure critical mechanical exponent prefix for 46 odd-only steps.

Equivalently:

\[
\boxed{
\text{any hypothetical first-candidate survivor must incur a positive critical defect within its first 46 odd steps.}
}
\]

This is a finite-size strengthening of the general fact that an infinite mechanical itinerary cannot come from a nontrivial positive natural seed. It does not control where later defects occur or rule out high-complexity defect patterns.