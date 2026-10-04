from fractions import Fraction

import first_contraction_cert as base

"""Exact propagation of the 2026-10-04 live Barina verification frontier.

The public project status page reports the lowest incomplete work unit at

    2175982616 * 2^40,

with all lower work units verified. Hence a least positive counterexample, if
any, satisfies N >= LIVE_N0 below.

This script keeps the internal first-candidate N_upper and pair-constrained
weighted-boundary argument, substitutes the live floor, and propagates it
through the clean-window machinery and the certified U4/U3V1 exclusions.

The live status is an external changing datum; all arithmetic propagation below
is exact once LIVE_N0 is fixed.
"""

LIVE_N0 = 2_175_982_616 * (1 << 40)
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
assert z_min == 35_260_917_543

# Clean complete 46-step boundary-started windows.
heavy_events_max = 5
heavy_contamination_max = 44 * heavy_events_max
terminal_incomplete_max = 44
W_min = z_min - heavy_contamination_max - terminal_incomplete_max
assert W_min == 35_260_917_279

# After the exact U4 and U3V1 exclusions, every exact-four clean window has at
# least two positive-source upsteps. The exact-q overlap argument in
# notes/2026-10-03-u3v1-exclusion-and-221-charge.md gives
#
#     221 G >= 20 W.

def ceil_fraction(x: Fraction) -> int:
    return x.numerator // x.denominator + (x.numerator % x.denominator != 0)

G_min_int = ceil_fraction(Fraction(20 * W_min, 221))
assert G_min_int == 3_191_033_238

# Endpoint target if every exact-four clean class is eventually excluded.
G_five_target = (W_min + 8) // 9
assert G_five_target == 3_917_879_698

if __name__ == "__main__":
    print("CERTIFIED")
    print("live floor =", LIVE_N0)
    print("boundary z >=", z_min)
    print("clean 46-windows >=", W_min)
    print("current total-upstep G >=", G_min_int)
    print("if exact-four eliminated, G >=", G_five_target)
