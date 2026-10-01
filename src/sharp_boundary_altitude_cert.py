from fractions import Fraction
from decimal import Decimal, getcontext

import first_contraction_cert as base

"""Exact sharp altitude bound for critical-boundary states in branch A.

For every preterminal orbit state of a least counterexample in the fixed first
coefficient-contraction candidate,

    x_n / N = 2^(h_n + theta_n) P_n,

where theta_n={n log_2 3} and

    P_n = prod_{i<n}(1+1/(3 x_i)).

At h_n=0, theta_n<1.  Using x_i>=N>=N0 and n<=k gives

    P_n <= 1/(1-k/(3N0)) =: P_bar.

Together with N<N_upper this yields the strict local bound

    x_n < 2 P_bar N_upper.

The integer HIGH below is ceil(2 P_bar N_upper), so every boundary state lies
in [N0,HIGH).  This strengthens the older coarse window [N0,2^73).
"""

k = base.qC
N0 = base.N0
N_upper = base.N_upper

assert k < 3 * N0
P_bar = Fraction(3 * N0, 3 * N0 - k)
H = 2 * P_bar * N_upper
HIGH = (H.numerator + H.denominator - 1) // H.denominator

assert H < Fraction(1 << 73)
assert HIGH == 6_287_967_883_654_920_544_295

if __name__ == "__main__":
    getcontext().prec = 60

    def dec(fr: Fraction) -> Decimal:
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    print("CERTIFIED")
    print("P_bar =", dec(P_bar))
    print("N_upper =", dec(N_upper))
    print("2*P_bar*N_upper =", dec(H))
    print("boundary states satisfy x <", HIGH)
    print("old coarse limit =", 1 << 73)
    print("new/old window-top ratio =", dec(Fraction(HIGH, 1 << 73)))
