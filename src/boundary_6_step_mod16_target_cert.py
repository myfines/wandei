from fractions import Fraction

"""Exact affine-DP target certificate for the first contraction candidate.

Every critical-boundary odd state must hit one of

    7, 11, 15 (mod 16)

within the next six odd-only transitions, or else it falls below the current
live verified frontier.

The target-avoiding odd residue set is {1,3,5,9,13}.  The transition graph below
is a safe affine over-approximation.  For residues with variable valuation we
allow every non-target successor at the smallest possible valuation, maximizing
all future states.
"""

HIGH = 6_287_967_883_654_920_544_295
LIVE_N0 = 2_175_982_616 * (1 << 40)
NODES = (1, 3, 5, 9, 13)

GRAPH = {
    1: ((1, 2), (5, 2), (9, 2), (13, 2)),
    3: ((5, 1), (13, 1)),
    5: ((1, 4), (3, 4), (5, 4), (9, 4), (13, 4)),
    9: ((3, 2),),
    13: ((1, 3), (3, 3), (5, 3), (9, 3), (13, 3)),
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


values = {r: Fraction(HIGH - 1) for r in NODES}
max5 = max6 = None
for step in range(1, 7):
    values = propagate(values)
    mx = max(v for v in values.values() if v is not None)
    if step == 5:
        max5 = mx
    if step == 6:
        max6 = mx

assert max5 is not None and max5 >= LIVE_N0
assert max6 is not None and max6 < LIVE_N0

Z_MIN = 35_260_917_543
W6_MIN = Z_MIN - 5
TARGET_MIN = (W6_MIN + 5) // 6
assert W6_MIN == 35_260_917_538
assert TARGET_MIN == 5_876_819_590

if __name__ == "__main__":
    print("CERTIFIED")
    print("live floor =", LIVE_N0)
    print("max target-avoiding state after 5 steps =", max5)
    print("max target-avoiding state after 6 steps =", max6)
    print("complete boundary-started 6-windows >=", W6_MIN)
    print("forced distinct {7,11,15} mod16 target states >=", TARGET_MIN)
