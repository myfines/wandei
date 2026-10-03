#!/usr/bin/env python3
"""Exact arithmetic bridge from the published recursive-sufficiency frontier to Branch A.

External theorem used:
  M. Ansari, "Recursive sufficiency for the Collatz conjecture and computational
  verification", NNTDM 31(3), 2025, Proposition 3.2 + Remark 3.1.

If all starting values below 2^71 are verified, take
    M = 2*3^44 + 1.
Then M < 2^71, and Proposition 3.2 gives convergence for every integer up to
    L = 2M = 4*3^44 + 2.

The Branch-A first-contraction analysis already gives the rigorous coarse seed bound
    N < (4/3)*2^71.
This script checks exactly that L lies above that whole seed window.
"""

from fractions import Fraction

VERIFIED = 2**71
M = 2 * 3**44 + 1
L = 2 * M
BRANCH_A_COARSE_UPPER = Fraction(4 * VERIFIED, 3)

assert M < VERIFIED
assert Fraction(L, 1) > BRANCH_A_COARSE_UPPER

# Integer-only form of the second comparison.
assert 3 * L > 4 * VERIFIED

if __name__ == "__main__":
    print("CERTIFIED")
    print("2^71 =", VERIFIED)
    print("M = 2*3^44+1 =", M)
    print("L = 4*3^44+2 =", L)
    print("3L - 4*2^71 =", 3 * L - 4 * VERIFIED)
    print("Therefore Branch-A seed bound N < (4/3)*2^71 is entirely below L.")
