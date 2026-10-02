from fractions import Fraction

"""Pure combinatorial overlap spectrum for boundary-started windows.

For a window of L transitions with exactly q defect upsteps, any fixed upstep
can belong to at most L-q+1 such boundary-started windows.  Combined with the
existing 29-state run cap, an upstep belongs to at most 45 boundary-started
46-windows in total.

This script solves the resulting fractional packing problem exactly and records
how large a minimum local upstep count would have to be before window counting
alone contradicts the finite supply of r=2 positions in the first candidate.
"""

L = 46
TOTAL_OVERLAP = 45
W = 35_260_566_218  # live-frontier clean-window lower bound
k = 72_057_431_991
floor_k_alpha = 114_208_327_603
R2_TOTAL = floor_k_alpha - k
assert R2_TOTAL == 42_150_895_612


def ceil_fraction(x: Fraction) -> int:
    return x.numerator // x.denominator + (x.numerator % x.denominator != 0)


def g_per_w_lower(min_upsteps: int) -> Fraction:
    """Exact LP optimum G/W using only overlap capacities.

    Let I_q be total incidences contributed by exact-q windows.  Then
      sum I_q <= 45 G,
      I_q <= (47-q) G,
      W = sum I_q/q.
    For fixed G, maximize W by filling incidence capacity from smallest q up.
    """
    remaining = Fraction(TOTAL_OVERLAP)
    w_per_g = Fraction(0)
    for q in range(min_upsteps, L + 1):
        cap = Fraction(L - q + 1)
        use = min(remaining, cap)
        w_per_g += use / q
        remaining -= use
        if remaining == 0:
            break
    assert w_per_g > 0
    return 1 / w_per_g


# Current minimum is four upsteps.
assert g_per_w_lower(4) == Fraction(20, 223)
G4 = ceil_fraction(g_per_w_lower(4) * W)
assert G4 == 3_162_382_621

# Pure local-window counting still cannot close at min=39.
G39 = ceil_fraction(g_per_w_lower(39) * W)
assert G39 == 40_394_462_617
assert G39 < R2_TOTAL

# But min=40 would exceed the exact number of r=2 positions.
G40 = ceil_fraction(g_per_w_lower(40) * W)
assert G40 == 52_802_848_259
assert G40 > R2_TOTAL

if __name__ == "__main__":
    print("CERTIFIED")
    print("r=2 supply =", R2_TOTAL)
    for m in (4, 5, 6, 10, 20, 30, 39, 40):
        c = g_per_w_lower(m)
        print(m, c, ceil_fraction(c * W))
    print("pure-window contradiction threshold = 40")
