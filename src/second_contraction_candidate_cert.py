from fractions import Fraction
from decimal import Decimal, getcontext

"""CONDITIONAL diagnostic for a putative second finite-contraction candidate.

INACTIVE STATUS (2026-10-04): this file assumes the stronger floor

    N >= 4*3^44+2,

which was previously imported from Ansari (2025), Proposition 3.2 / Remark 3.1.
An exact audit found a failed set equality in the Lemma 3.1 sieve induction, so
that frontier upgrade is not accepted as proved in this repository.

Accordingly this file is NOT part of the active unconditional proof chain.
It records what follows *if* the stronger floor is independently established.
See notes/2026-10-04-erratum-ansari-frontier-import.md.
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
    tail = 2 * (z ** (2 * terms + 1)) / (Fraction(2 * terms + 1) * (1 - z2))
    return s, s + tail


ln2_lo, ln2_hi = log_interval(Fraction(2))
ln3_lo, ln3_hi = log_interval(Fraction(3))
alpha_lo = ln3_lo / ln2_hi
alpha_hi = ln3_hi / ln2_lo

pU, qU = 10_439_860_591, 6_586_818_670
pL, qL = 103_768_467_013, 65_470_613_321
pC, qC = pU + pL, qU + qL
pM, qM = pU + pC, qU + qC
p2, q2 = pC + pL, qC + qL

assert (pC, qC) == (114_208_327_604, 72_057_431_991)
assert (p2, q2) == (217_976_794_617, 137_528_045_312)
assert Fraction(pL, qL) < alpha_lo < alpha_hi < Fraction(pC, qC)
assert alpha_hi < Fraction(p2, q2)

# CONDITIONAL stronger floor only.
FRONTIER = 4 * 3**44 + 2
WINDOW_HI = Fraction(1, 3 * FRONTIER) / ln2_lo

pM_gap_lo = Fraction(pM, qM) - alpha_hi
assert pM_gap_lo > WINDOW_HI
p2_gap_hi = Fraction(p2, q2) - alpha_lo
assert p2_gap_hi < WINDOW_HI

D_lo = p2 * ln2_lo - q2 * ln3_hi
D_hi = p2 * ln2_hi - q2 * ln3_lo
assert D_lo > 0

I_hi = Fraction(1, 2) / ln2_lo
N_upper = (q2 * I_hi + 3) / (3 * D_lo)
rho = Fraction(FRONTIER) / N_upper
assert 0 < rho < Fraction(1, 2)

if __name__ == "__main__":
    getcontext().prec = 60
    def dec(fr):
        return Decimal(fr.numerator) / Decimal(fr.denominator)
    print("CONDITIONAL DIAGNOSTIC ONLY")
    print("candidate A,k =", p2, q2)
    print("assumed frontier =", FRONTIER)
    print("log2 N_upper ~=", dec(N_upper).ln() / Decimal(2).ln())
    print("required correction ratio rho ~=", dec(rho))
