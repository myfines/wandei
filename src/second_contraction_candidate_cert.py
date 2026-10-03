from fractions import Fraction
from decimal import Decimal, getcontext

"""Exact arithmetic certificate for the second finite-contraction candidate.

The first candidate
    (A,k)=(114208327604,72057431991)
has already been eliminated by the recursive-sufficiency verification frontier.
This file isolates the next possible upper rational under the stronger floor
    N >= 4*3^44+2
and gives a rigorous mechanical correction ceiling for its seed.
"""


def log_interval(x: Fraction, terms: int = 220):
    assert x > 0
    z = (x - 1) / (x + 1)
    assert 0 <= z < 1
    z2 = z * z
    s = Fraction(0)
    p = z
    for n in range(terms):
        s += 2 * p / Fraction(2 * n + 1)
        p *= z2
    tail = 2 * (z ** (2 * terms + 1)) / (
        Fraction(2 * terms + 1) * (1 - z2)
    )
    return s, s + tail


ln2_lo, ln2_hi = log_interval(Fraction(2))
ln3_lo, ln3_hi = log_interval(Fraction(3))
alpha_lo = ln3_lo / ln2_hi
alpha_hi = ln3_hi / ln2_lo

# Consecutive lower/upper approximants around log_2 3 used by the first-candidate proof.
pU, qU = 10_439_860_591, 6_586_818_670
pL, qL = 103_768_467_013, 65_470_613_321
pC, qC = pU + pL, qU + qL
assert (pC, qC) == (114_208_327_604, 72_057_431_991)

# The nearest upper rational on the outside of pC with denominator above qC.
pM, qM = pU + pC, qU + qC
# The next upper convergent on the alpha side of pC.
p2, q2 = pC + pL, qC + qL
assert (p2, q2) == (217_976_794_617, 137_528_045_312)

assert Fraction(pL, qL) < alpha_lo < alpha_hi < Fraction(pC, qC)
assert alpha_hi < Fraction(p2, q2)
assert pC * qL - pL * qC == 1

# Published recursive-sufficiency frontier imported from the Ansari bridge.
FRONTIER = 4 * 3**44 + 2

# Any first coefficient contraction for a least counterexample N>=FRONTIER obeys
# A/k-alpha <= 1/(3*N*ln 2), hence certainly <= WINDOW_HI.
WINDOW_HI = Fraction(1, 3 * FRONTIER) / ln2_lo

# After the already-eliminated pC/qC candidate, no denominator qC<q<q2
# can yield another upper candidate inside the window.  The closest possible
# upper rational on the exterior side is the Farey mediant pM/qM, and its gap
# is already too large.
pM_gap_lo = Fraction(pM, qM) - alpha_hi
assert pM_gap_lo > WINDOW_HI

# The next upper convergent really does lie inside the allowed Diophantine window.
p2_gap_hi = Fraction(p2, q2) - alpha_lo
assert p2_gap_hi < WINDOW_HI

# Candidate linear form D=A ln2-k ln3.
D_lo = p2 * ln2_lo - q2 * ln3_hi
D_hi = p2 * ln2_hi - q2 * ln3_lo
assert D_lo > 0

# Mechanical correction envelope.  q2 = 2*qL + qU, so split the rotation sum
# into three convergent-denominator blocks.  For f(t)=2^{-t}, integral is
# 1/(2 ln2) and total variation is 1.  Denjoy-Koksma therefore gives
# sum f <= q2/(2 ln2)+3.
I_hi = Fraction(1, 2) / ln2_lo
N_upper = (q2 * I_hi + 3) / (3 * D_lo)

# The survival correction ratio only needs to exceed FRONTIER/N_upper.
rho = Fraction(FRONTIER) / N_upper
assert 0 < rho < Fraction(1, 2)

if __name__ == "__main__":
    getcontext().prec = 60

    def dec(fr):
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    log2_nupper = dec(N_upper).ln() / Decimal(2).ln()
    log2_frontier = Decimal(FRONTIER).ln() / Decimal(2).ln()

    print("CERTIFIED")
    print("candidate A,k =", p2, q2)
    print("frontier =", FRONTIER)
    print("window_hi =", dec(WINDOW_HI))
    print("outside mediant gap_lo =", dec(pM_gap_lo))
    print("candidate gap_hi =", dec(p2_gap_hi))
    print("D in [", dec(D_lo), ",", dec(D_hi), "]")
    print("log2 frontier ~=", log2_frontier)
    print("log2 N_upper ~=", log2_nupper)
    print("required correction ratio rho ~=", dec(rho))
