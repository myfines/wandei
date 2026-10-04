#!/usr/bin/env python3
"""Exact arithmetic constants for charging first-candidate boundary states to
20 mod 27 target hits.

External theorem/rank input (Monks--Monks--Monks--Monks 2013, with the exact
rank reconstruction recorded in the 2026-09 sufficiency audit): shortcut-T
iteration stopped on A={1,2} union {20 mod27} admits these phases:

* divisible-by-3 phase: at most v2(n)+1 actual steps before exit;
* core phase: Q=w_h*n, w_h in {16,28,49}, and every core-to-core step
  multiplies Q by at most 20/21;
* residue-26/13 phase: rank score at most v2(n+1)+2.

This file combines that rank with the repository's exact first-candidate
boundary altitude and live boundary count. The universal proof is the rank
argument; this script certifies all numerical inequalities and the final
charging count.
"""

import sharp_boundary_altitude_cert as alt
import live_frontier_upgrade_cert as live

HIGH = alt.HIGH
assert HIGH < (1 << 73)

# If a boundary state begins in the 3|n phase, after removing all factors of 2
# the final odd step exits that phase. Starting below HIGH gives <=72 halvings
# plus one odd step. Moreover the state entering the next phase is still <2^73.
PHASE3_STEPS = 73
phase3_exit_top = (3 * (HIGH - 1) + 1) // 2
assert phase3_exit_top < (1 << 73)

# Core phase. Initially Q < 49*2^73. Every core-to-core step contracts Q by
# <=20/21. Find the first m for which m consecutive core-to-core transitions
# would force Q<1 and hence be impossible.
CORE_INPUT_Q_TOP = 49 * (1 << 73)
m = 0
p20 = 1
p21 = 1
while CORE_INPUT_Q_TOP * p20 >= p21:
    m += 1
    p20 *= 20
    p21 *= 21
CORE_STEPS = m  # at most m-1 core-to-core stays, then at most one exit step
assert CORE_STEPS == 1117
assert CORE_INPUT_Q_TOP * 20**CORE_STEPS < 21**CORE_STEPS

# While still in the core, weight >=16, hence n < (49/16)*2^73 <2^75.
assert 49 * (1 << 73) < 16 * (1 << 75)
# An odd exit obeys T(n)/n <=5/3 for n>=3, so the phase-1 input is <2^76.
assert 5 * (1 << 75) < 3 * (1 << 76)

# Residue 26 has rank score v2(n+1)+2; for n<2^76 this is at most 78.
PHASE1_STEPS = 78

H = PHASE3_STEPS + CORE_STEPS + PHASE1_STEPS
assert H == 1268

# A least counterexample cannot hit 1 or2, so each eligible boundary state must
# encounter 20 mod27 within H shortcut steps. Boundary odd states occur at
# distinct shortcut times, separated by at least one step. Thus one target hit
# can serve at most H+1 boundary starts. Discard at most H boundary starts too
# close to the odd-only terminal index k.
z = live.z_min
eligible = z - H
TARGET_HITS_MIN = (eligible + H) // (H + 1)
assert TARGET_HITS_MIN == 27_786_381

if __name__ == "__main__":
    print("CERTIFIED")
    print("boundary HIGH =", HIGH)
    print("phase-3 steps <=", PHASE3_STEPS)
    print("core steps <=", CORE_STEPS)
    print("phase-1 steps <=", PHASE1_STEPS)
    print("total shortcut hitting bound H =", H)
    print("live boundary states z >=", z)
    print("eligible boundary starts >=", eligible)
    print("distinct 20 mod27 hits forced >=", TARGET_HITS_MIN)
