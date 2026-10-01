"""Exact drift certificate for boundary-boundary edges on the qU cycle.

For the first coefficient-contraction candidate, let sigma(n)=n+qU mod k.
If both n and sigma(n) are critical-boundary times h=0, then every such edge
except possibly the single edge with source n=0 strictly decreases the actual
odd Syracuse state in the sigma direction.
"""

from fractions import Fraction
from decimal import Decimal, getcontext

import first_contraction_cert as base

pU, qU = base.pU, base.qU
pL, qL = base.pL, base.qL
k = base.qC
N0 = base.N0

assert k == qU + qL
assert pU * qL - pL * qU == 1

# Positive convergent errors, rigorously bounded from below.
deltaU_lo = Fraction(pU) - qU * base.alpha_hi
deltaL_lo = qL * base.alpha_lo - Fraction(pL)
assert deltaU_lo > 0
assert deltaL_lo > 0

# For a forward qU block whose boundary exponent increment is pU,
# x_{n+qU}/x_n = 2^{-deltaU} P_block.
# Since every preterminal orbit state is >=N0,
# log2(P_block) < qU/(3*N0*ln 2).
corrU_log2_hi = Fraction(qU, 3 * N0) / base.ln2_lo
assert corrU_log2_hi < deltaU_lo

# The qL forward block is simpler: when its exponent increment is pL,
# its coefficient is 2^{deltaL}>1 and P_block>1, so forward qL strictly
# increases x; equivalently the wrapped sigma edge strictly decreases x.

# Useful numerical separation, not used as proof.
if __name__ == "__main__":
    getcontext().prec = 60

    def dec(fr: Fraction) -> Decimal:
        return Decimal(fr.numerator) / Decimal(fr.denominator)

    print("CERTIFIED")
    print("deltaU >", dec(deltaU_lo))
    print("deltaL >", dec(deltaL_lo))
    print("qU correction log2 <", dec(corrU_log2_hi))
    print("correction/deltaU <", dec(corrU_log2_hi / deltaU_lo))
