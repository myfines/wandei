# Final boundary repayment is forced into the last 29 odd steps

Status: exact combination of two previously certified results in the first coefficient-contraction branch. Not a Collatz proof.

Let m be the last return to h=0 before the terminal first-contraction state h_k=-1, and let ell=k-m.

The terminal suffix-rigidity result proves that after this last repayment the defect remains exactly on the critical boundary until the terminal step:

h_m=h_{m+1}=...=h_{k-1}=0,

with mechanical valuations on transitions m,...,k-2 and the final exponent one larger than mechanical on transition k-1.

Therefore the suffix contains exactly ell consecutive boundary states

m,m+1,...,k-1.

Independently, the strengthened boundary-run finite certificate proves that no first-candidate orbit can contain 30 consecutive boundary states. Every maximal boundary run has at most 29 states.

Hence the terminal boundary suffix must satisfy

ell <= 29.

Equivalently,

boxed: k-m <= 29,

and with k=72,057,431,991,

boxed: m >= 72,057,431,962.

This strictly strengthens the older terminal-cylinder conclusion k-m<=44. The remaining terminal freedom is now only 29 exact suffix lengths.