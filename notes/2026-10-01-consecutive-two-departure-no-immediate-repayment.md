# Consecutive-2 departures cannot repay immediately

Status: exact local consequence of irrational-rotation geometry and the odd-height direct-repayment phase gate. Not a Collatz proof.

Let

\[
L=\log_2 3=1+\alpha,\qquad \alpha=L-1,
\]

and

\[
\theta_n=\{nL\}=\{n\alpha\}.
\]

The mechanical increment

\[
r_n=\lfloor(n+1)L\rfloor-\lfloor nL\rfloor
\]

equals 2 exactly when

\[
\theta_n\ge 1-\alpha=2-L.
\]

A boundary departure \(h_n=0\to h_{n+1}=1\) is possible only through

\[
r_n=2,\qquad a_n=1.
\]

Now suppose the next mechanical increment is also 2:

\[
r_n=r_{n+1}=2.
\]

For two consecutive 2s one must have

\[
\theta_n\ge2(1-\alpha)=4-2L.
\]

After the first step,

\[
\theta_{n+1}=\theta_n+\alpha-1=\theta_n-(2-L).
\]

Since \(\theta_n<1\),

\[
2-L\le\theta_{n+1}<L-1.
\]

Numerically this is approximately

\[
0.4150375\le\theta_{n+1}<0.5849625.
\]

But an immediate return from height one at this second \(r=2\) position would require

\[
a_{n+1}=3,
\]

and the committed odd-height direct-repayment phase gate proves that such a step requires

\[
\theta_{n+1}>\log_2(128/65)=0.9776321869\ldots.
\]

The intervals are disjoint. Therefore

\[
\boxed{
h_n=0,\ h_{n+1}=1,\ r_n=r_{n+1}=2
\Longrightarrow h_{n+2}>0.
}
\]

Equivalently, a unit excursion that returns to the critical boundary after exactly one positive-defect state can occur only in the mechanical pattern

\[
(r_n,r_{n+1})=(2,1),
\]

with valuation word

\[
(a_n,a_{n+1})=(1,2).
\]

For reference, that exact valuation word fixes the local odd seed to

\[
x_n\equiv11\pmod{16}.
\]

Thus the cheap one-step repayment channel is completely classified: it is a \(21\) mechanical corner with local 2-adic cylinder \(11\bmod16\). Every \(22\) departure creates an excursion lasting at least two positive-defect times.

This is a local structural restriction. By itself it does not yet bound the total number of excursions, because boundary departures could in principle concentrate on the allowed \(21\) phases.
