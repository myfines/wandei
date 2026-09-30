from fractions import Fraction
from decimal import Decimal, getcontext

import first_contraction_cert as base

"""Exact weighted boundary-density certificate for the first candidate.

The old defect-budget bound used only that the mechanical weights differ by
less than a factor of two. Here we exploit their exact form

    w_j = 3^(k-1) * 2^(-theta_j),  theta_j={j log_2 3},

and Denjoy--Koksma on the two convergent-denominator blocks qL and qU whose
sum is qC. This yields a stronger lower bound on the number of h_j=0 states.
"""

q = base.qC
rho = Fraction(base.N0) / base.N_upper
c = 2 * rho - 1
assert c > 0

# f(x)=2^(-x) on R/Z has integral 1/(2 log 2) and total variation 1.
# Splitting q=qL+qU into two convergent-denominator blocks gives
# S=sum f(theta_j) >= q*I - 2.
I_lo = Fraction(1, 2) / base.ln2_hi
S_lo = q * I_lo - 2

# Rational threshold close to the continuous optimum.
u = Fraction(7391, 10000)
ln1u_lo, ln1u_hi = base.log_interval(1 / u)

# g_u(x)=max(2^(-x)-u,0).
# Its integral is ((1-u)-u log(1/u))/log 2.
# For an upper bound: subtract the lower log(1/u), divide by lower log 2.
J_hi = ((1 - u) - u * ln1u_lo) / base.ln2_lo

# Var(g_u)=2(1-u). Two DK blocks contribute at most 2*Var(g_u).
G_hi = q * J_hi + 4 * (1 - u)

# If Z is the set of z boundary times and T=sum_{j in Z} f(theta_j), then
# pointwise T <= z*u + sum g_u(theta_j).
# Also the correction ratio obeys
#   R <= 1/2 + T/(2S),
# while survival requires R>rho. Therefore T>c*S.
# It follows that
#   z*u + G_hi > c*S_lo.
threshold = (c * S_lo - G_hi) / u
z_min = threshold.numerator // threshold.denominator + 1

runs_min = (z_min + 35 - 1) // 35
departures_min = runs_min - 1

assert z_min == 31_430_911_924
assert runs_min == 898_026_055
assert departures_min == 898_026_054

# The previous integer z=z_min-1 is rigorously impossible.
assert Fraction(z_min - 1) * u + G_hi <= c * S_lo

if __name__ == "__main__":
    getcontext().prec = 50

    def dec(fr: Fraction) -> Decimal:
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    print("CERTIFIED")
    print("rho =", dec(rho))
    print("threshold u =", dec(u))
    print("boundary z >=", z_min)
    print("boundary density >=", dec(Fraction(z_min, q)))
    print("boundary runs >=", runs_min)
    print("0->1 departures >=", departures_min)
