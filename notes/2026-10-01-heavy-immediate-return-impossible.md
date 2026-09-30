# Heavy immediate return is impossible

Status: exact combination of the rotation geometry and the direct-repayment phase gate. Not a Collatz proof.

Consider a non-cheap boundary excursion that tries to return in two steps. Departure is forced to have r_n=2, a_n=1, taking h:0->1. An immediate non-cheap return would require r_{n+1}=2, a_{n+1}=3, taking h:1->0.

Let beta=log2(3)-1 and theta_j={j log2(3)}. We have r_j=2 iff theta_j >= 1-beta.

If r_n=r_{n+1}=2, then after the first r=2 step

theta_{n+1}=theta_n+beta-1.

Since theta_n<1, this gives theta_{n+1}<beta. Together with r_{n+1}=2,

1-beta <= theta_{n+1} < beta.

Numerically this is approximately [0.4150374993, 0.5849625007).

But the odd-height direct-repayment phase gate, applied to h_{n+1}=1, r_{n+1}=2, a_{n+1}=3, requires

theta_{n+1} > log2(128/65) = 0.9776321869...

The intervals are disjoint. Therefore a heavy immediate 22 / a=13 return is impossible.

Consequently every non-cheap boundary excursion has length at least 3.

Combining with the cheap-run cap and the certified total excursion lower bound E>=726809885, at least

floor(E/4)=181702471

boundary excursions have length at least 3.

Thus a first-candidate survivor must contain at least 181702471 genuinely extended excursions away from h=0.