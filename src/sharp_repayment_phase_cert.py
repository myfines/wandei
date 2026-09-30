from fractions import Fraction
from decimal import Decimal, getcontext

import first_contraction_cert as base

"""Exact sharp phase gate for odd-height r=2 direct repayments.

Inside the fixed first coefficient-contraction candidate, the full affine
correction product is far closer to 1 than the earlier coarse 65/64 bound.
This script turns that into a rigorous phase-window and counting certificate.
"""

k = base.qC
N0 = base.N0

# For every preterminal state x_i >= N >= N0,
#   P_n = prod_{i<n}(1+1/(3x_i)) <= (1+1/(3N0))^n.
# Using log(1+u)<=u and exp(t)<=1/(1-t), for t<1,
#   P_n <= 1/(1-n/(3N0)) <= 1/(1-k/(3N0)).
assert k < 3 * N0
P_bar = Fraction(3 * N0, 3 * N0 - k)

lnP_lo, lnP_hi = base.log_interval(P_bar)
# Rigorous upper bound for eps = log_2(P_bar).
eps_hi = lnP_hi / base.ln2_lo

# The window is tiny.
assert eps_hi < Fraction(1, 60_000_000_000)

# For f=1_I where I=(1-eps_hi,1), Var(f)=2. Splitting
# k=qL+qU into two convergent-denominator blocks gives
# count(I) <= k*|I| + 4.
count_upper_real = k * eps_hi + 4
assert count_upper_real < 6
count_upper_integer = 5

if __name__ == "__main__":
    getcontext().prec = 60

    def dec(fr: Fraction) -> Decimal:
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    print("CERTIFIED")
    print("k =", k)
    print("N0 =", N0)
    print("P_bar - 1 <=", dec(P_bar - 1))
    print("eps = log2(P_bar) <=", dec(eps_hi))
    print("necessary repayment phase theta > 1-eps")
    print("DK real count bound <", dec(count_upper_real))
    print("odd-height r=2 direct repayments <=", count_upper_integer)
