# Deterministic mod-8 character bias — 2026-09-28

## Status

This is a rigorous necessary condition for a hypothetical least positive
counterexample.  It does **not** prove Collatz.

The point is that a least counterexample cannot look even approximately uniform
modulo 8 along its odd-only orbit: every prefix must exhibit a large
multiplicative-character bias.

---

## 1. Odd-only setup

Let

\[
x_{i+1}=\frac{3x_i+1}{2^{a_i}},
\qquad
 a_i=v_2(3x_i+1),
\]

with \(x_0=N\), where \(N\) is assumed to be the least positive
counterexample.

Then \(x_i\ge N\) for all \(i\).

Let

\[
A_n=\sum_{i=0}^{n-1}a_i
\]

and

\[
E_n=\sum_{i=0}^{n-1}
\log_2\!\left(1+\frac1{3x_i}\right).
\]

The exact logarithmic-height identity is

\[
\log_2(x_n/N)
=n\log_2 3-A_n+E_n.
\]

Since \(x_n\ge N\),

\[
A_n\le n\log_2 3+E_n.
\]

Also, because \(x_i\ge N\),

\[
E_n\le n\delta_N,
\qquad
\delta_N:=\log_2\!\left(1+\frac1{3N}\right).
\]

Hence every prefix satisfies

\[
\boxed{
\frac{A_n}{n}
\le
\log_2 3+\delta_N.
}
\]

---

## 2. Valuation tails as residue frequencies

For any positive integer-valued random variable \(a\),

\[
a=1+\mathbf 1_{a\ge2}+\mathbf 1_{a\ge3}+\cdots.
\]

Apply this to the finite empirical distribution of \(a_0,\ldots,a_{n-1}\).
Let

\[
f_2=\frac1n\#\{i<n:a_i\ge2\},
\qquad
f_3=\frac1n\#\{i<n:a_i\ge3\}.
\]

Then

\[
\frac{A_n}{n}
\ge1+f_2+f_3.
\]

For odd \(x\), direct congruence calculation gives

\[
a(x)\ge2
\iff
x\equiv1\pmod4,
\]

and

\[
a(x)\ge3
\iff
x\equiv5\pmod8.
\]

Write \(p_r\) for the empirical frequency of \(x_i\equiv r\pmod8\),
for \(r\in\{1,3,5,7\}\).  Then

\[
f_2=p_1+p_5,
\qquad
f_3=p_5.
\]

Therefore

\[
\boxed{
p_1+2p_5
\le
\omega+\delta_N,
\qquad
\omega:=\log_2(3/2).
}
\]

This holds for **every** prefix length \(n\ge1\).

Under uniform distribution on the four odd residue classes mod 8, the left
side would equal

\[
\frac14+2\cdot\frac14=\frac34.
\]

Since

\[
\frac34-\omega
=0.165037499\ldots,
\]

a least counterexample must sustain a large residue bias at every scale.

---

## 3. Convert the residue deficit into Dirichlet-character bias

Use the three nontrivial real Dirichlet characters modulo 8, with values on
\(1,3,5,7\):

\[
\chi_{-4}=(1,-1,1,-1),
\]

\[
\chi_{8}=(1,-1,-1,1),
\]

\[
\chi_{-8}=(1,1,-1,-1).
\]

Let their empirical orbit averages be

\[
c_{-4}=\frac1n\sum_{i<n}\chi_{-4}(x_i),
\]

\[
c_8=\frac1n\sum_{i<n}\chi_8(x_i),
\]

\[
c_{-8}=\frac1n\sum_{i<n}\chi_{-8}(x_i).
\]

Fourier inversion on the four odd residue classes gives

\[
p_1=\frac{1+c_{-4}+c_8+c_{-8}}4,
\]

\[
p_5=\frac{1+c_{-4}-c_8-c_{-8}}4.
\]

Thus

\[
p_1+2p_5
=
\frac{3+3c_{-4}-c_8-c_{-8}}4.
\]

Combining with the least-counterexample inequality,

\[
3c_{-4}-c_8-c_{-8}
\le
4(\omega+\delta_N)-3.
\]

Set

\[
K_N:=3-4(\omega+\delta_N).
\]

For the currently relevant enormous \(N\), \(K_N>0\).  Therefore

\[
|3c_{-4}-c_8-c_{-8}|
\ge K_N.
\]

By the triangle inequality,

\[
5\max\{|c_{-4}|,|c_8|,|c_{-8}|\}
\ge K_N.
\]

Hence every prefix of a hypothetical least counterexample satisfies

\[
\boxed{
\max_{\chi\in\{\chi_{-4},\chi_8,\chi_{-8}\}}
\left|
\frac1n\sum_{i=0}^{n-1}\chi(x_i)
\right|
\ge
\frac{3-4\omega-4\delta_N}{5}.
}
\]

Since \(\omega=\log_2 3-1\), this is

\[
\boxed{
\max_\chi
\left|
\frac1n\sum_{i<n}\chi(x_i)
\right|
\ge
\frac{7-4\log_2 3-4\delta_N}{5}.
}
\]

As \(N\to\infty\), the right-hand side tends to

\[
\boxed{
\frac{7-4\log_2 3}{5}
=0.1320299994\ldots
}
\]

So a least counterexample would force at least one nontrivial mod-8
multiplicative character to have roughly **13.2% or larger average bias on every
prefix**.

The winning character may vary with the prefix, but among infinitely many
prefixes at least one of the three characters must carry such a bias infinitely
often.

---

## 4. Why this is useful

This turns the global convergence problem into a concrete spectral/mixing
subproblem:

> Prove that no positive odd Syracuse orbit which stays forever above its
> starting minimum can sustain a nontrivial mod-8 character average of this
> magnitude.

A theorem of the schematic form

\[
\limsup_{n\to\infty}
\max_{\chi\ne1\bmod8}
\left|
\frac1n\sum_{i<n}\chi(x_i)
\right|
<c
\]

for any universal

\[
c<\frac{7-4\log_2 3}{5}
\]

would immediately contradict the least-counterexample condition.

This is the cleanest current point of contact with Dirichlet-character,
transfer-operator, and spectral-gap ideas.

---

## 5. Limitation

Ordinary Dirichlet-character cancellation over intervals or over primes does
not automatically apply to a single deterministic Collatz orbit.  The missing
step is an **orbitwise** mixing/spectral estimate.

So the result above should be viewed as a sharp target, not as an invocation of
GRH or of standard prime-distribution theorems.
