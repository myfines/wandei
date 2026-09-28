# Sparse-Sturmian carry lemma — 2026-09-29

## Status

This note records a rigorous structural consequence of reciprocal summability for a hypothetical divergent positive Collatz orbit. It does **not** prove the conjecture.

Work in the odd-only Syracuse map

\[
x_{k+1}=\frac{3x_k+1}{2^{a_k}},\qquad a_k=v_2(3x_k+1).
\]

Assume a least positive counterexample \(N=x_0\) exists and its odd-only orbit is aperiodic/unbounded. Write

\[
b_k=a_k-1,\qquad B_k=\sum_{i<k} b_i,
\]

and

\[
\omega=\log_2(3/2),\qquad
E_k=\sum_{i<k}\log_2\!\left(1+\frac1{3x_i}\right).
\]

The exact logarithmic identity gives

\[
\log_2\frac{x_k}{N}=k\omega-B_k+E_k.
\]

Define

\[
C_k=\lfloor k\omega+E_k\rfloor,
\qquad
m_k=\left\lfloor\log_2\frac{x_k}{N}\right\rfloor.
\]

Then exactly

\[
\boxed{m_k=C_k-B_k}. 
\]

Since \(x_k\ge N\),

\[
\boxed{B_k\le C_k\quad\text{for every }k}. 
\]

Thus the valuation excess \(b_k\) is a service process that can never consume more than the near-rotation carry budget \(C_k\).

---

## 1. Reciprocal summability produces a limiting phase

Garcia--Tal's uniform orbit-sparsity estimate implies, as a corollary for an aperiodic divergent orbit,

\[
\sum_{k\ge0}\frac1{x_k}<\infty.
\]

Hence

\[
E_k\uparrow E_\infty<\infty.
\]

Define the limiting mechanical cumulative carry

\[
C_k^*=\lfloor k\omega+E_\infty\rfloor.
\]

Set

\[
\delta_k=E_\infty-E_k\downarrow0,
\qquad
 e_k=C_k^*-C_k.
\]

For all sufficiently large \(k\), \(\delta_k<1\), so

\[
e_k\in\{0,1\}.
\]

Moreover,

\[
e_k=1
\]

can occur only when

\[
\{k\omega+E_\infty\}<\delta_k.
\]

Thus the difference between the true cumulative carry and the limiting mechanical carry is controlled by visits of the irrational rotation \(k\omega+E_\infty\) to a shrinking target at zero.

---

## 2. Shrinking-target hits become arbitrarily separated

Because \(\omega=\log_2(3/2)\) is irrational, for every fixed integer \(Q\ge1\),

\[
\eta_Q:=\min_{1\le q\le Q}\|q\omega\|>0.
\]

Suppose \(e_i=e_j=1\) with \(i<j\). Then both phases lie within their shrinking windows around an integer, so

\[
\|(j-i)\omega\|
\le \delta_i+\delta_j
\le 2\delta_i.
\]

Once \(i\) is large enough that

\[
2\delta_i<\eta_Q,
\]

we must have

\[
j-i>Q.
\]

Since \(Q\) is arbitrary:

\[
\boxed{\text{the gaps between sufficiently late indices with }e_k=1\text{ tend to infinity}.}
\]

No quantitative irrationality measure is needed for this qualitative statement.

---

## 3. The actual carry word is a fixed Sturmian word plus sparse defect clusters

Let

\[
c_k=C_{k+1}-C_k,
\qquad
c_k^*=C_{k+1}^*-C_k^*.
\]

The word \((c_k^*)\) is the mechanical/Sturmian word of slope \(\omega\) and intercept \(E_\infty\) (up to the standard lower/upper convention at boundary points).

Because

\[
C_k=C_k^*-e_k,
\]

we have

\[
\boxed{c_k=c_k^*+e_k-e_{k+1}}.
\]

Therefore \(c_k\ne c_k^*\) only next to an index where \(e_k=1\). Since the \(e_k=1\) hits are eventually isolated with gaps tending to infinity, the carry defects occur in clusters of bounded size (at most two adjacent positions) whose mutual gaps tend to infinity.

Hence:

\[
\boxed{
\text{the true carry word is asymptotically a fixed Sturmian word with defect clusters whose spacing }\to\infty.
}
\]

This is stronger than a vague "near-Sturmian" statement: arbitrarily long exact Sturmian stretches must occur.

---

## 4. Critical queue condition for a rational positive counterexample

López--Stoll prove that if a rational 2-adic integer has a non-cyclic Collatz trajectory, then its parity-density lower limit must equal the critical value

\[
\alpha=\frac{\log2}{\log3}.
\]

Translating to odd-only exponents, this forces

\[
\limsup_{k\to\infty}\frac{B_k}{k}=\omega.
\]

Since \(C_k/k\to\omega\), the exact queue identity yields

\[
\boxed{\liminf_{k\to\infty}\frac{m_k}{k}=0}. 
\]

Reciprocal summability also implies \(x_k\to\infty\), hence

\[
\boxed{m_k\to\infty}. 
\]

So any hypothetical least positive divergent orbit must realize the very specific regime

\[
\boxed{
m_k\to\infty,
\qquad
\liminf \frac{m_k}{k}=0,
\qquad
m_k=C_k-B_k,
}
\]

where \(C_k\) is a Sturmian carry process with only asymptotically isolated defect clusters.

This is the new target.

---

## 5. Dead-end audit: adjacent-swap majorization alone

For a first passage to a new dyadic record, the local deficit path gives a prefix-majorization relation between a light valuation word and the carry word. However the adjacent swap direction is the safe one for minimality: moving a `1` earlier (the local `01 -> 10` move in the odd-only \(b=a-1\) word) increases the affine endpoint for a fixed start, equivalently increases the same-endpoint ancestor when reversed in the relevant comparison. Thus majorization monotonicity by itself does not force a smaller counterexample.

Do not treat the first-passage majorization observation as a proof mechanism without an additional arithmetic constraint.

---

## 6. Next concrete bridge

The remaining mismatch is now sharply formulated.

The arrival/carry word is asymptotically fixed Sturmian with sparse defect clusters, while the service word

\[
b_k=v_2(3x_k+1)-1
\]

must keep

\[
m_k=C_k-B_k\ge0,
\]

make \(m_k\to\infty\), yet also satisfy \(\liminf m_k/k=0\).

A useful next theorem would be one of the following:

1. **Sparse-mismatch theorem:** show that the arithmetic realization by a positive integer forces \(b_k\) itself to differ from the limiting mechanical service template only sparsely; then existing finite-defect / mechanical-itinerary exclusions may be extendable.

2. **Dense-mismatch theorem:** show that if \(b_k\) differs from the Sturmian carry process on positive density of sites while maintaining the queue constraints, then the induced affine corrections / 3-adic shadows violate the reverse-barrier restrictions.

This is a cleaner complexity dichotomy than the earlier informal low-complexity/high-complexity split.
