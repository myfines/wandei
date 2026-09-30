# Last-boundary suffix rigidity in the first contraction candidate

Status: exact structural consequence of the first-candidate hypothesis. Not a Collatz proof.

Let

\[
L=\log_2 3,\qquad A_n=\sum_{i<n}a_i,\qquad h_n=\lfloor nL\rfloor-A_n,
\]

and assume the first coefficient contraction of a least counterexample occurs at

\[
(k,A_k)=(72057431991,114208327604).
\]

Then

\[
h_n\ge0\quad(n<k),\qquad h_k=-1.
\]

By the 46-step exclusion, a survivor must have a positive defect before time 46. Let

\[
m=1+\max\{n<k:h_n>0\}
\]

be the first time after the last positive defect. Then

\[
\boxed{h_m=h_{m+1}=\cdots=h_{k-1}=0,\qquad h_k=-1.}
\]

## 1. The entire terminal exponent word is fixed

Put

\[
r_n=\lfloor(n+1)L\rfloor-\lfloor nL\rfloor\in\{1,2\}.
\]

Since

\[
h_{n+1}-h_n=r_n-a_n,
\]

we get for every internal suffix step

\[
\boxed{a_n=r_n\qquad(m\le n\le k-2).}
\]

At the terminal first-contraction step,

\[
-1=h_k-h_{k-1}=r_{k-1}-a_{k-1},
\]

so

\[
\boxed{a_{k-1}=r_{k-1}+1.}
\]

Thus once the last boundary-return time `m` is specified, there is no remaining symbolic freedom in the suffix.

Its total exponent is

\[
B_{m,k}:=A_k-A_m
=\lfloor kL\rfloor-\lfloor mL\rfloor+1.
\]

## 2. Every last boundary-return state lies in a fixed low band

For odd-only states,

\[
\log_2\frac{x_m}{N}
=mL-A_m+\sum_{i<m}\log_2\left(1+\frac1{3x_i}\right).
\]

Because `h_m=0`, we have `A_m=floor(mL)`, hence

\[
\log_2\frac{x_m}{N}
=\{mL\}+E_m,
\qquad
E_m:=\sum_{i<m}\log_2\left(1+\frac1{3x_i}\right).
\]

Minimality gives `x_i>=N`, so with the live verified floor

\[
N_0=2075\,2^{60}
\]

and `m<k`,

\[
0<E_m<\frac{k}{3N_0\log 2}<1.45\times10^{-11}.
\]

Therefore

\[
\boxed{x_m<2^{1+1.45\times10^{-11}}N.}
\]

Using the clean first-candidate bound

\[
N<\frac43\,2^{71},
\]

we obtain the uniform low-band bound

\[
\boxed{x_m<2^{1+1.45\times10^{-11}}\frac43\,2^{71}.}
\]

So every possible last boundary return occurs below essentially

\[
\frac83\,2^{71},
\]

independently of how late `m` is.

## 3. Exact cylinder consequence

For any chosen `m`, the fixed suffix word determines one residue class for `x_m` modulo

\[
\boxed{2^{B_{m,k}+1}.}
\]

Indeed if the suffix length is `ell=k-m` and

\[
2^{B_{m,k}}x_k=3^{\ell}x_m+d_{m,k},
\]

then oddness of `x_k` gives

\[
3^{\ell}x_m+d_{m,k}\equiv2^{B_{m,k}}\pmod{2^{B_{m,k}+1}},
\]

hence

\[
\boxed{x_m\equiv3^{-\ell}(2^{B_{m,k}}-d_{m,k})\pmod{2^{B_{m,k}+1}}.}
\]

The first-candidate problem is therefore reduced to the following exact arithmetic question:

> For which last-return times `m` does the unique suffix cylinder contain an odd integer in the narrow admissible band `[N_0, (8/3+o(1))2^71)` that can also be reached from an earlier positive-defect prefix without descending below `N`?

This is the next finite-certificate target.