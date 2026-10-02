from fractions import Fraction

import first_contraction_cert as base

"""Exact propagation of the 2026-10-02 live Barina verification frontier.

The project status page reports the lowest incomplete work unit at
2175975677 * 2^40, with all lower work units verified.  Hence a least positive
counterexample, if any, satisfies N >= LIVE_N0 below.

This script keeps the existing first-candidate N_upper and pair-constrained
weighted-boundary argument, substitutes the stronger live floor, and propagates
it through the clean-window / exact-four overlap ladder.
"""

LIVE_N0 = 2_175_975_677 * (1 << 40)
assert LIVE_N0 > base.N0

q = base.qC
rho = Fraction(LIVE_N0) / base.N_upper
c = 2 * rho - 1
assert c > 0

# Mechanical total-weight lower bound.
S_lo = q * (Fraction(1, 2) / base.ln2_hi) - 2

# Same rigorous Lagrange choice used by the pair-constrained certificate.
lam = Fraction(3593, 5000)
P0 = Fraction(5, 3) - 2 * lam
Ub = Fraction(3, 4) - lam
log_pair_lo, _ = base.log_interval(Fraction(5, 1) / (6 * lam))
log_unpaired_lo, _ = base.log_interval(Fraction(3, 1) / (4 * lam))
num_hi = P0 - 2 * lam * log_pair_lo + Ub - lam * log_unpaired_lo
H_integral_hi = num_hi / base.ln2_lo
VarH = 2 * (P0 + Ub)
H_sum_hi = q * H_integral_hi + 2 * VarH
terminal_slack = 1

threshold = (c * S_lo - H_sum_hi - terminal_slack) / lam
z_min = threshold.numerator // threshold.denominator + 1
assert z_min == 35_260_566_482

# Sharpen the clean-window losses using the 29-state boundary-run cap.
# A heavy transition has nonboundary source, so among its 46 possible starts
# at most 44 can be boundary starts.  Likewise among the final 45 start times
# that cannot support a complete 46-transition window, at most 44 are boundary.
heavy_events_max = 5
heavy_contamination_max = 44 * heavy_events_max
terminal_incomplete_max = 44
W_min = z_min - heavy_contamination_max - terminal_incomplete_max
assert W_min == 35_260_566_218

# Existing exact-four certificate excludes U4.  Therefore every exact-four
# clean window has at least one positive-height upstep.  The overlap-ladder
# bound for s=1 is ceil(((4+1/44)/45) W).
num = Fraction(4, 1) + Fraction(1, 44)
G_min = (num * W_min / 45)
G_min_int = G_min.numerator // G_min.denominator + (G_min.denominator != 1)
assert G_min_int == 3_152_080_920

# If all exact-four clean windows are eventually excluded, every clean window
# has at least five upsteps, so 5 W <= 45 G.
G_five_target = (W_min + 8) // 9
assert G_five_target == 3_917_840_691

if __name__ == "__main__":
    print("CERTIFIED")
    print("live floor =", LIVE_N0)
    print("boundary z >=", z_min)
    print("clean 46-windows >=", W_min)
    print("current total-upstep G >=", G_min_int)
    print("if exact-four eliminated, G >=", G_five_target)
