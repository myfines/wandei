"""Exact lower bound for adjacent boundary pairs on the qU convergent cycle.

Inside the first coefficient-contraction candidate let

    B = {0 <= n < k : h_n = 0}

and weight vertex n by w_n = 2^{-theta_n}, theta_n={n log_2 3}.
The shift sigma(n)=n+qU (mod k) is one cycle because qU and k are coprime.
Along this cycle the phases decrease by one of the two positive convergent
errors deltaU or deltaL, whose total over one circuit is exactly one. Hence
the cyclic total variation of the weights is < 1.

A weighted independent set on such a cycle has weight < S/2+1/2, where
S=sum w_n. Survival requires boundary weight T > c*S with c=2*rho-1.
Deleting at most one vertex per B-B edge makes B independent, so the number
e of adjacent B-B edges obeys

    e > (c-1/2) S - 1/2.

Denjoy--Koksma supplies an exact rational lower bound for S.
"""

from fractions import Fraction
from decimal import Decimal, getcontext
from math import gcd

import first_contraction_cert as base

pU, qU = base.pU, base.qU
pL, qL = base.pL, base.qL
pC, k = base.pC, base.qC

assert k == qU + qL
assert gcd(qU, k) == 1
assert pU * qL - pL * qU == 1

# Rigorous positivity of the two rotation errors.
deltaU_lo = Fraction(pU) - qU * base.alpha_hi
deltaL_lo = qL * base.alpha_lo - Fraction(pL)
assert deltaU_lo > 0
assert deltaL_lo > 0

# Algebraically, independently of alpha,
# qL*(pU-qU*alpha)+qU*(qL*alpha-pL)=1.
assert pU * qL - pL * qU == 1

# Survival boundary-weight threshold from the exact first-candidate seed bound.
rho = Fraction(base.N0) / base.N_upper
c = 2 * rho - 1
assert c > Fraction(1, 2)

# S=sum_{n<k} 2^{-theta_n}.  f(theta)=2^{-theta} has integral
# 1/(2 ln 2) and total variation 1.  Since k=qL+qU is split into two
# convergent-denominator blocks, Denjoy--Koksma gives error at most 2.
S_lo = Fraction(k, 2) / base.ln2_hi - 2

# If e is the number of B-B edges on the sigma cycle, deleting <=e boundary
# vertices leaves an independent boundary subset.  Every deleted vertex has
# weight <=1.  The weighted independent-set bound is < S/2+1/2 because the
# cyclic weight total variation is <1.  Therefore
#
#   e > T-S/2-1/2 > (c-1/2)S-1/2.
#
# Replace S by the rigorous lower bound S_lo.
edge_lower_real = (c - Fraction(1, 2)) * S_lo - Fraction(1, 2)
edge_min = edge_lower_real.numerator // edge_lower_real.denominator + 1

assert edge_min == 1_134_940_229

if __name__ == "__main__":
    getcontext().prec = 60

    def dec(fr: Fraction) -> Decimal:
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    print("CERTIFIED")
    print("k =", k)
    print("qU =", qU)
    print("qL =", qL)
    print("gcd(qU,k) =", gcd(qU, k))
    print("boundary weighted fraction c >", dec(c))
    print("mechanical weight S >=", dec(S_lo))
    print("real B-B edge lower bound >", dec(edge_lower_real))
    print("adjacent boundary edges on qU-cycle >=", edge_min)
