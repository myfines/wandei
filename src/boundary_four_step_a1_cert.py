from fractions import Fraction

"""Exact four-step a=1 forcing certificate for the first contraction candidate.

For every critical-boundary state h_n=0, the repository has the strict altitude
bound

    x_n < HIGH = 6,287,967,883,654,920,544,295.

If four consecutive odd-only exponents satisfy a>=2, then each odd step obeys

    x' <= (3x+1)/4.

Iterating four times gives

    x_{n+4} <= (81*x_n + 175)/256.

Using the current live verified floor LIVE_N0, the exact integer inequality
below shows that the right side is already below LIVE_N0 for every integer
x_n < HIGH. Hence every complete four-transition window starting at h=0 must
contain at least one a=1 transition.
"""

HIGH = 6_287_967_883_654_920_544_295
LIVE_N0 = 2_175_982_616 * (1 << 40)

# Since x < HIGH and x is integral, x <= HIGH-1.
MAX_FOUR_STEP_NUMERATOR = 81 * (HIGH - 1) + 175
assert MAX_FOUR_STEP_NUMERATOR < 256 * LIVE_N0

# Current live boundary-count lower bound propagated in live_frontier_upgrade_cert.py.
Z_MIN = 35_260_917_543

# At most the final three boundary starts fail to support four full transitions.
W4_MIN = Z_MIN - 3
A1_MIN = (W4_MIN + 3) // 4
assert W4_MIN == 35_260_917_540
assert A1_MIN == 8_815_229_385

if __name__ == "__main__":
    print("CERTIFIED")
    print("live floor =", LIVE_N0)
    print("four-step inequality margin =", 256 * LIVE_N0 - MAX_FOUR_STEP_NUMERATOR)
    print("complete boundary-started 4-windows >=", W4_MIN)
    print("forced a=1 transitions >=", A1_MIN)
