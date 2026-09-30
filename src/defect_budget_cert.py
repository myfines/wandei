"""Exact rational certificate for the first-candidate defect budget.

Uses the exact rational mechanical correction upper bound N_upper from
first_contraction_cert.py. No decimal/logarithmic approximation is used in the
actual inequalities below.
"""

from __future__ import annotations

from fractions import Fraction

from first_contraction_cert import N0, N_upper, qC

# If d is the actual correction and d_max the mechanical ceiling correction,
# R=d/d_max. Survival with N>=N0 and d_max/(2^A-3^k) <= N_upper forces
# R > N0/N_upper (strictness is harmless; the integer consequences below use
# the exact rational lower bound).
R_LO = Fraction(N0, 1) / N_upper

# If p is the fraction of pre-contraction times with h_j=0, the extremal
# weight argument gives
#
#   R <= (1/4 + 3p/4)/(1/2 + p/2).
#
# Solving for p gives the exact lower bound below.
P_LO = (R_LO / 2 - Fraction(1, 4)) / (Fraction(3, 4) - R_LO / 2)

K = qC
Z_MIN = (P_LO.numerator * K) // P_LO.denominator + 1

# The boundary-run certificate excludes 36 consecutive boundary states, so
# every maximal run has length at most 35.
MAX_BOUNDARY_RUN = 35
RUNS_MIN = (Z_MIN + MAX_BOUNDARY_RUN - 1) // MAX_BOUNDARY_RUN
UPCROSSINGS_MIN = RUNS_MIN - 1

assert Z_MIN == 25_438_346_005
assert RUNS_MIN == 726_809_886
assert UPCROSSINGS_MIN == 726_809_885


if __name__ == "__main__":
    from decimal import Decimal, getcontext

    getcontext().prec = 50

    def dec(x: Fraction) -> Decimal:
        return Decimal(x.numerator) / Decimal(x.denominator)

    print("CERTIFIED")
    print("R >", dec(R_LO))
    print("boundary fraction p >", dec(P_LO))
    print("boundary times z >=", Z_MIN)
    print("boundary runs >=", RUNS_MIN)
    print("unit 0->1 upcrossings >=", UPCROSSINGS_MIN)
