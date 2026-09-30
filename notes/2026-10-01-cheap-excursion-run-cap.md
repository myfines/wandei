# Cheap excursion run cap

Status: exact rotation-combinatorial lemma inside the first-contraction defect framework. Not a Collatz proof.

Let alpha = log2(3)-1 and theta_n = {n alpha}. Let r_n = floor((n+1)log2(3))-floor(n log2(3)) in {1,2}.

A cheapest two-step boundary excursion has h: 0 -> 1 -> 0, mechanical symbols (r_n,r_{n+1})=(2,1), and valuations (a_n,a_{n+1})=(1,2). Its Syracuse map is x -> (3x+1)/2 -> (9x+5)/8.

One 21 pair starts exactly when 1-alpha <= theta_n < 2-2alpha. After a complete 21 pair, phase advances by beta=2alpha-1 > 0.

Thus m consecutive 21 pairs require
1-alpha + (m-1)(2alpha-1) < 2-2alpha.

For m=4 this becomes 7alpha < 4. But alpha > 4/7 because log2(3)>11/7 iff 3^7>2^11, and 2187>2048. Hence (21)^4 cannot occur.

For m=3 the condition becomes 5alpha < 3. This holds because log2(3)<8/5 iff 3^5<2^8, and 243<256.

Therefore the exact maximum number of consecutive 21 pairs is 3.

Consequence: immediate cheap boundary returns 0->1->0 with valuation pair (1,2) can occur at most three times consecutively. A fourth excursion must be longer, reach a higher defect, or use another repayment mechanism.

This uses exact integer inequalities only, not equidistribution.