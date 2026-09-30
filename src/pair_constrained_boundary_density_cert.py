from fractions import Fraction
from decimal import Decimal, getcontext

import first_contraction_cert as base

"""Exact pair-constrained boundary-density certificate.

At a preterminal boundary time h_j=0 with mechanical letter r_j=1, positivity
of the defect before the first contraction forces h_{j+1}=0 as well. Since the
mechanical word has no 11 factor, these forced r=1 -> successor pairs are
disjoint. This local closure constraint is combined with the exact rotation
weights and Denjoy--Koksma to strengthen the global boundary-density bound.
"""

q = base.qC
rho = Fraction(base.N0) / base.N_upper
c = 2 * rho - 1
assert c > 0

# Mechanical weight total S=sum 2^{-theta_j}. Split q=qL+qU into two
# convergent-denominator blocks. f(x)=2^{-x} has integral 1/(2 log 2)
# and total variation 1.
I_lo = Fraction(1, 2) / base.ln2_hi
S_lo = q * I_lo - 2

# Lagrange multiplier chosen close to the continuous optimum.
lam = Fraction(3593, 5000)
assert Fraction(2, 3) < lam < Fraction(3, 4)
assert 6 * lam < 5

# Let beta=log_2 3 - 1 and b=1-beta=2-log_2 3.
# If r_j=1, theta_j in [0,b), and the successor weight is exactly 2/3
# times the start weight. For an allowed pair (00,01,11), the maximum of
# weight-lam*count is
#   max(0, (5/3)2^{-theta} - 2 lam).
# The unpaired r=2 phases are theta in [b,beta), where the single-site
# contribution is max(0,2^{-theta}-lam).
# For our lambda, both supports terminate strictly inside those intervals.
P0 = Fraction(5, 3) - 2 * lam
Ub = Fraction(3, 4) - lam
assert P0 > 0 and Ub > 0

# Pair support ends when 2^{-theta}=6 lam/5.
log_pair_lo, _ = base.log_interval(Fraction(5, 1) / (6 * lam))
# Unpaired support ends when 2^{-theta}=lam; at theta=b the weight is 3/4.
log_unpaired_lo, _ = base.log_interval(Fraction(3, 1) / (4 * lam))

# Integral of the two positive humps. Logs are subtracted, so their lower
# bounds and the lower bound for log 2 give a rigorous upper bound.
num_hi = (
    P0
    - 2 * lam * log_pair_lo
    + Ub
    - lam * log_unpaired_lo
)
assert num_hi > 0
H_integral_hi = num_hi / base.ln2_lo

# The total variation of the two separated humps is 2(P0+Ub).
VarH = 2 * (P0 + Ub)
# Two convergent-denominator blocks: total DK error <= 2*VarH.
H_sum_hi = q * H_integral_hi + 2 * VarH

# There can be one exceptional r=1 boundary at j=k-1, whose successor is the
# terminal h_k=-1 state outside the preterminal boundary set. A +1 slack
# covers that single endpoint exactly.
terminal_slack = 1

# If Z is the boundary set with size z and T its total mechanical weight,
# the pair closure gives
#   T - lam*z <= H_sum_hi + terminal_slack.
# Survival still requires T > (2*rho-1) S, and S>=S_lo.
threshold = (
    c * S_lo - H_sum_hi - terminal_slack
) / lam
z_min = threshold.numerator // threshold.denominator + 1

runs_min = (z_min + 35 - 1) // 35
departures_min = runs_min - 1
noncheap_min = departures_min // 4

assert z_min == 35_251_435_711
assert runs_min == 1_007_183_878
assert departures_min == 1_007_183_877
assert noncheap_min == 251_795_969

# The previous integer is rigorously impossible.
assert (
    Fraction(z_min - 1) * lam + H_sum_hi + terminal_slack
    <= c * S_lo
)

if __name__ == "__main__":
    getcontext().prec = 50

    def dec(fr: Fraction) -> Decimal:
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    print("CERTIFIED")
    print("lambda =", dec(lam))
    print("boundary z >=", z_min)
    print("boundary density >=", dec(Fraction(z_min, q)))
    print("boundary runs >=", runs_min)
    print("0->1 departures >=", departures_min)
    print("non-cheap excursions >=", noncheap_min)
