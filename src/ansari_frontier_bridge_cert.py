#!/usr/bin/env python3
"""Conditional arithmetic bridge for the Ansari frontier claim.

IMPORTANT STATUS (2026-10-04):
The numerical comparisons in this file are exact, but the external propagation
claim from Ansari (2025), Proposition 3.2 / Remark 3.1, is NOT imported as a
proved theorem in this repository.  An exact audit found a failed set equality
in Lemma 3.1, the sieve induction used later in the paper.

Therefore this file proves only the conditional statement:

    IF every integer through L = 4*3^44+2 is independently known to converge,
    THEN the first-candidate coarse seed window N < (4/3)*2^71 lies below L.

See notes/2026-10-04-erratum-ansari-frontier-import.md.
"""

from fractions import Fraction

VERIFIED = 2**71
M = 2 * 3**44 + 1
L = 2 * M
FIRST_CANDIDATE_COARSE_UPPER = Fraction(4 * VERIFIED, 3)

# Pure arithmetic comparisons only.
assert M < VERIFIED
assert Fraction(L, 1) > FIRST_CANDIDATE_COARSE_UPPER
assert 3 * L > 4 * VERIFIED

if __name__ == "__main__":
    print("CONDITIONAL ARITHMETIC COMPARISON CERTIFIED")
    print("2^71 =", VERIFIED)
    print("M = 2*3^44+1 =", M)
    print("L = 4*3^44+2 =", L)
    print("3L - 4*2^71 =", 3 * L - 4 * VERIFIED)
    print("No unconditional verification-frontier extension is asserted here.")
