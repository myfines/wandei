from fractions import Fraction
from decimal import Decimal, getcontext

"""Exact rational certificate for the first coefficient-contraction window.

This file uses only integer/rational arithmetic.  The logarithms are enclosed by
an atanh-series interval with an explicit positive tail bound.  It certifies a
clean consequence of the first-contraction route:

    N < (4/3) * 2^71

for the first continued-fraction candidate
(A,k)=(114208327604, 72057431991), under the live verification floor
N >= 2075*2^60 used when isolating the candidate.

It does NOT prove Collatz.  The remaining no-contraction branch is separate.
"""


def log_interval(x: Fraction, terms: int = 220):
    """Rigorous interval for log(x), for the positive rationals used here.

    log x = 2 * sum_{n>=0} z^(2n+1)/(2n+1), z=(x-1)/(x+1).
    The tail is bounded by replacing every denominator by 2M+1.
    """
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

# Live Barina verification floor on 2026-09-29.
N0 = 2075 * (1 << 60)

# Adjacent continued-fraction / Farey data surrounding log_2(3).
pU, qU = 10439860591, 6586818670
pL, qL = 103768467013, 65470613321
pC, qC = pU + pL, qU + qL
pM, qM = pU + pC, qU + qC
pNext, qNext = pC + pL, qC + qL

assert (pC, qC) == (114208327604, 72057431991)
assert (pNext, qNext) == (217976794617, 137528045312)
assert pU * qL - pL * qU == 1
assert pU * qC - pC * qU == 1
assert pC * qL - pL * qC == 1

alpha_lo = ln3_lo / ln2_hi
alpha_hi = ln3_hi / ln2_lo
assert Fraction(pL, qL) < alpha_lo < alpha_hi < Fraction(pC, qC)

# A first coefficient contraction of a least counterexample N>=N0 obeys
# A/k - log_2(3) <= 1/(3*N0*log(2)).
window_hi = Fraction(1, 3 * N0) / ln2_lo
next_upper_gap_lo = Fraction(pM, qM) - alpha_hi
assert next_upper_gap_lo > window_hi

# Candidate linear form D=A log 2-k log 3.
D_lo = pC * ln2_lo - qC * ln3_hi
D_hi = pC * ln2_hi - qC * ln3_lo
assert D_lo > 0

# Mechanical correction envelope.  For f(t)=2^{-t} on R/Z,
# total variation is 1 and integral is 1/(2 log 2).  Since qC=qL+qU,
# split into two convergent-denominator blocks; Denjoy-Koksma gives
# sum_{j<qC} f({j log_2 3}) <= qC/(2 log 2)+2.
I_hi = Fraction(1, 2) / ln2_lo

# e^D-1 >= D gives a fully rational upper bound.
N_upper = (qC * I_hi + 2) / (3 * D_lo)
clean_bound = Fraction(4 * (1 << 71), 3)
assert N_upper < clean_bound
assert Fraction(N0) < clean_bound


if __name__ == "__main__":
    getcontext().prec = 50

    def dec(fr):
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    print("CERTIFIED")
    print("candidate A,k =", pC, qC)
    print("next denominator =", qNext)
    print("window_hi =", dec(window_hi))
    print("next_upper_gap_lo =", dec(next_upper_gap_lo))
    print("D in [", dec(D_lo), ",", dec(D_hi), "]")
    print("N_upper ~=", dec(N_upper))
    print("clean bound (4/3)*2^71 =", dec(clean_bound))
    print("N_upper / 2^71 ~=", dec(N_upper / Fraction(1 << 71)))
    print("live floor / 2^71 =", dec(Fraction(N0, 1 << 71)))
    print("remaining clean/live factor =", dec(clean_bound / Fraction(N0)))
