# Exact logarithmic rotation cocycle — 2026-09-28

## Status

This note records an exact structural reduction for the odd-only Syracuse map.
It is **not** a proof of the Collatz conjecture.

The useful point is that the fractional part of logarithmic height follows an
irrational circle rotation plus a tiny positive correction, globally — not only
inside a low-altitude block.

---

## 1. Setup

Let

\[
S(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1)
\]

on positive odd integers.  Assume a least positive counterexample \(N\) exists,
and write its odd-only orbit as

\[
x_0=N,\qquad x_{i+1}=S(x_i).
\]

Minimality gives \(x_i\ge N\) for all \(i\).

Define logarithmic height

\[
h_i=\log_2(x_i/N)=H_i+\theta_i,
\]

where

\[
H_i=\lfloor h_i\rfloor\in\mathbb Z_{\ge0},
\qquad
\theta_i=\{h_i\}\in[0,1).
\]

Also define

\[
\omega=\log_2(3/2)=\log_2 3-1
\]

and the positive correction

\[
\varepsilon_i
=\log_2\!\left(1+\frac1{3x_i}\right).
\]

Since \(x_i\ge N\),

\[
0<\varepsilon_i\le
\delta_N:=\log_2\!\left(1+\frac1{3N}\right).
\]

---

## 2. Exact circle-rotation identity

From

\[
x_{i+1}=\frac{3x_i+1}{2^{a_i}}
\]

we get

\[
h_{i+1}
=h_i+\log_2 3-a_i+\varepsilon_i
=h_i+1+\omega-a_i+\varepsilon_i.
\]

Because \(a_i\) is an integer, taking fractional parts gives the exact identity

\[
\boxed{
\theta_{i+1}
=
\{\theta_i+\omega+\varepsilon_i\}.
}
\]

Thus the phase of every least-counterexample orbit is a rigid irrational
rotation by \(\omega\), perturbed by a positive error of size \(O(1/N)\) per
odd step.

This is global: no low-altitude hypothesis is used.

Let

\[
E_k=\sum_{i=0}^{k-1}\varepsilon_i.
\]

Since \(\theta_0=0\), iteration gives

\[
\boxed{
\theta_k=\{k\omega+E_k\}.
}
\]

and

\[
0<E_k\le k\delta_N.
\]

---

## 3. Wrap cocycle and the vertical height

Define the wrap bit

\[
b_i=\lfloor\theta_i+\omega+\varepsilon_i\rfloor\in\{0,1\}.
\]

The integer part satisfies

\[
\boxed{
H_{i+1}=H_i+1+b_i-a_i.
}
\]

If

\[
A_k=\sum_{i=0}^{k-1}a_i,
\qquad
B_k=\sum_{i=0}^{k-1}b_i,
\]

then, since \(H_0=0\),

\[
\boxed{
A_k=k+B_k-H_k.
}
\]

Also

\[
\boxed{
B_k=\lfloor k\omega+E_k\rfloor.
}
\]

For comparison, the rigid mechanical word of slope \(\omega\) has prefix wrap
count

\[
B_k^{(0)}=\lfloor k\omega\rfloor.
\]

Therefore

\[
\boxed{
B_k-B_k^{(0)}
=\lfloor k\omega+E_k\rfloor-\lfloor k\omega\rfloor.
}
\]

In particular, whenever \(E_k<1\),

\[
\boxed{
B_k-B_k^{(0)}\in\{0,1\}.
}
\]

So through every horizon satisfying \(k\delta_N<1\), the cumulative wrap word
lies pointwise between a rigid mechanical word and that word plus one extra
wrap.

For \(N>2^{71}\), this shadowing horizon is vastly longer than the current
\(10^{11}\)-scale critical Diophantine candidates.

---

## 4. Exact characterization of a coefficient contraction

The multiplicative coefficient after \(k\) odd-only steps is

\[
\frac{3^k}{2^{A_k}}.
\]

A coefficient contraction means

\[
A_k>k\log_2 3.
\]

Using \(A_k=k+B_k-H_k\) and \(\log_2 3=1+\omega\), define

\[
d_k=A_k-k\log_2 3.
\]

Then

\[
d_k=B_k-H_k-k\omega.
\]

Assume \(E_k<1\).  Write

\[
k\omega=m+\phi,
\qquad m\in\mathbb Z,
\quad 0<\phi<1.
\]

Since \(B_k=\lfloor k\omega+E_k\rfloor\), there are only two possibilities:

\[
B_k=m
\quad\text{or}\quad
B_k=m+1.
\]

If \(B_k=m\), then

\[
d_k=-H_k-\phi<0.
\]

Therefore a coefficient contraction is possible only in the second case.  If
\(B_k=m+1\), then

\[
d_k=1-H_k-\phi.
\]

Since \(H_k\ge0\), positivity forces

\[
\boxed{H_k=0.}
\]

Hence, under \(E_k<1\),

\[
\boxed{
A_k>k\log_2 3
\Longrightarrow
N\le x_k<2N.
}
\]

Moreover in that case

\[
\boxed{
A_k-k\log_2 3
=1-\{k\omega\}.
}
\]

Equivalently,

\[
\boxed{
A_k=\lceil k\log_2 3\rceil.
}
\]

Finally, for the extra wrap to occur we need

\[
\boxed{
E_k\ge1-\{k\omega\}.
}
\]

Since \(E_k\le k\delta_N\), every such contraction time must satisfy the
one-sided Diophantine condition

\[
\boxed{
1-\{k\log_2(3/2)\}
\le
k\log_2\!\left(1+\frac1{3N}\right).
}
\]

This is the clean rotation form of the very narrow continued-fraction window
encountered earlier.

---

## 5. Interpretation

A coefficient contraction before the accumulated correction reaches one is
not an arbitrary event.  It occurs exactly when all three things happen:

1. the rigid rotation \(k\omega\) lies just below the next integer;
2. the accumulated positive Collatz correction \(E_k\) is large enough to
   push the phase across that integer;
3. the actual orbit is back in the bottom dyadic altitude band
   \([N,2N)\).

Thus continued-fraction candidates are precisely possible *phase-crossing
returns to the ground band*.

This provides a cleaner bridge between:

- Diophantine approximation of \(\log_2 3\);
- mechanical/Sturmian words;
- low-altitude occupation;
- the exact additive Collatz correction.

---

## 6. Important limitation

This does not exclude an escaping divergent orbit.  A hypothetical unbounded
orbit may eventually satisfy

\[
A_k<k\log_2 3
\]

persistently, so that its multiplicative coefficient is expanding rather than
contracting.  The rotation-cocycle lemma therefore clarifies the paradoxical
prefix branch but does not by itself close the global coverage problem.

The next target is to combine the global near-rotation with the existing
side-branch altitude restriction and reverse 3-adic constraints to attack the
supercritical escape branch.
