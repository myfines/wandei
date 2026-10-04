from fractions import Fraction

"""Exact affine-DP certificate for the first coefficient-contraction candidate.

Target odd residues modulo 16:
    {11,15}.

Claim: starting from any critical-boundary odd state x < HIGH, if the odd-only
Syracuse orbit avoids the target residues for 28 consecutive odd transitions,
then the resulting state is already below the current live verified frontier.
Hence every complete 28-transition boundary-started window contains a target
state x == 11 or 15 (mod 16).

The DP is an over-approximation: for residue classes whose exact valuation can
vary, we allow every non-target successor and use the smallest possible
valuation, which maximizes the next state. Therefore proving descent for this
larger affine graph is sufficient.
"""

HIGH = 6_287_967_883_654_920_544_295
LIVE_N0 = 2_175_982_616 * (1 << 40)

# Non-target odd residues mod 16.
NODES = (1, 3, 5, 7, 9, 13)

# Edges (next residue, denominator exponent lower bound).
# Exact modular facts:
# 1 mod16: a=2, next in {1,5,9,13}
# 3 mod16: a=1, next in {5,13}
# 5 mod16: a>=4; allowing all non-target successors with a=4 is safe
# 7 mod16: a=1, non-target successor only 3 (the other is target 11)
# 9 mod16: a=2, non-target successors {3,7} (the others are targets 11,15)
# 13 mod16: a=3; allowing all non-target successors is exact/safe
GRAPH = {
    1: ((1, 2), (5, 2), (9, 2), (13, 2)),
    3: ((5, 1), (13, 1)),
    5: ((1, 4), (3, 4), (5, 4), (7, 4), (9, 4), (13, 4)),
    7: ((3, 1),),
    9: ((3, 2), (7, 2)),
    13: ((1, 3), (3, 3), (5, 3), (7, 3), (9, 3), (13, 3)),
}


def propagate(values):
    out = {s: None for s in NODES}
    for r, x in values.items():
        if x is None:
            continue
        for s, a in GRAPH[r]:
            y = (3 * x + 1) / (1 << a)
            if out[s] is None or y > out[s]:
                out[s] = y
    return out


# x is integral and x < HIGH.
values = {r: Fraction(HIGH - 1) for r in NODES}

max27 = None
max28 = None
for step in range(1, 29):
    values = propagate(values)
    mx = max(v for v in values.values() if v is not None)
    if step == 27:
        max27 = mx
    if step == 28:
        max28 = mx

assert max27 is not None and max27 >= LIVE_N0
assert max28 is not None and max28 < LIVE_N0

# Global target count from the current live boundary-count lower bound.
Z_MIN = 35_260_917_543
W28_MIN = Z_MIN - 27
TARGET_MIN = (W28_MIN + 27) // 28
assert W28_MIN == 35_260_917_516
assert TARGET_MIN == 1_259_318_483

if __name__ == "__main__":
    print("CERTIFIED")
    print("live floor =", LIVE_N0)
    print("max target-avoiding state after 27 steps =", max27)
    print("max target-avoiding state after 28 steps =", max28)
    print("complete boundary-started 28-windows >=", W28_MIN)
    print("forced distinct {11,15} mod16 target states >=", TARGET_MIN)
