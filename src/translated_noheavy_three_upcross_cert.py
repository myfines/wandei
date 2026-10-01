"""Chunkable translated 46-step certificate with at most three upcrossings.

First-candidate local class:
- start at critical boundary h=0;
- next 46 defect states stay in {0,1};
- at most three 0->1 upcrossings;
- forbid the rare direct return h=1,r=2,a=3.

All 47 length-46 mechanical factors are supported.  For every exact valuation
script, intersect its 2-adic seed cylinder with

    2075*2^60 <= x < 2^73,

verify the prescribed prefix, and continue the exact odd-only Syracuse orbit
until it drops below the verified frontier.

The script accepts optional first-occurrence shifts as positional arguments so
the complete scan can be reproduced in independent chunks.  With no arguments
it runs all 47 factors and checks the aggregate constants recorded below.
"""

from __future__ import annotations

import hashlib
import sys

STEPS = 46
LOW = 2075 * (1 << 60)
LOCAL_LIMIT = 1 << 73
MAX_UPCROSSINGS = 3
POW3 = 3**STEPS

EXPECTED_SCRIPTS = 12_024_283
EXPECTED_ROWS = 6_112_533
EXPECTED_WORST = (
    276,
    8171827952796853273339,
    697521228196614030223,
)


def exact_mechanical_letters(count: int) -> list[int]:
    p = 1
    floors: list[int] = []
    for _ in range(count + 1):
        floors.append(p.bit_length() - 1)
        p *= 3
    return [floors[j + 1] - floors[j] for j in range(count)]


def all_factors() -> list[tuple[int, tuple[int, ...]]]:
    # Sturmian complexity is n+1; exhibit all 47 length-46 factors exactly.
    mech = exact_mechanical_letters(400)
    factors: dict[tuple[int, ...], int] = {}
    for shift in range(len(mech) - STEPS + 1):
        word = tuple(mech[shift : shift + STEPS])
        factors.setdefault(word, shift)
        if len(factors) == STEPS + 1:
            break
    assert len(factors) == 47
    return sorted((shift, word) for word, shift in factors.items())


def odd_step(x: int) -> tuple[int, int]:
    y = 3 * x + 1
    a = (y & -y).bit_length() - 1
    return y >> a, a


def check_factor(shift: int, mechanical: tuple[int, ...]):
    # State = (h, upcrossings, A, affine_d, packed_2bit_valuation_word).
    states = [(0, 0, 0, 0, 0)]

    for j, r in enumerate(mechanical):
        nxt = []
        bit = 2 * j
        for h, up, A, d, code in states:
            # Stay at same defect height: a=r.
            nxt.append((h, up, A + r, 3 * d + (1 << A), code | (r << bit)))

            # Unit upcrossing 0->1: necessarily r=2,a=1.
            if h == 0 and r == 2 and up < MAX_UPCROSSINGS:
                nxt.append(
                    (1, up + 1, A + 1, 3 * d + (1 << A), code | (1 << bit))
                )

            # Unit return 1->0 through r=1,a=2.
            # The alternative r=2,a=3 is intentionally excluded here; the
            # sharp phase certificate bounds such heavy returns globally.
            if h == 1 and r == 1:
                nxt.append((0, up, A + 2, 3 * d + (1 << A), code | (2 << bit)))
        states = nxt

    rows = 0
    worst = (0, 0, 0)
    digest = hashlib.sha256()
    inv_cache: dict[int, int] = {}

    for h, up, A, d, code in states:
        modulus = 1 << (A + 1)
        inv = inv_cache.get(A)
        if inv is None:
            inv = pow(POW3, -1, modulus)
            inv_cache[A] = inv
        residue = (inv * ((1 << A) - d)) % modulus
        assert residue & 1

        q = max(0, (LOW - residue + modulus - 1) // modulus)
        while True:
            seed = residue + q * modulus
            if seed >= LOCAL_LIMIT:
                break

            x = seed
            fell = None
            for k in range(1, 2001):
                x, a = odd_step(x)
                if k <= STEPS:
                    expected = (code >> (2 * (k - 1))) & 3
                    assert a == expected
                if x < LOW:
                    fell = (k, x)
                    break
            assert fell is not None, (shift, seed)

            k, endpoint = fell
            if k > worst[0]:
                worst = (k, seed, endpoint)
            digest.update(f"{A},{up},{h},{seed},{k},{endpoint}\n".encode())
            rows += 1
            q += 1

    return len(states), rows, worst, digest.hexdigest()


def main() -> None:
    factors = all_factors()
    wanted = set(map(int, sys.argv[1:])) if len(sys.argv) > 1 else None
    selected = [(s, w) for s, w in factors if wanted is None or s in wanted]
    if wanted is not None:
        assert {s for s, _ in selected} == wanted

    total_scripts = 0
    total_rows = 0
    global_worst = (0, 0, 0)
    summary = hashlib.sha256()

    for shift, word in selected:
        scripts, rows, worst, digest = check_factor(shift, word)
        print("FACTOR", shift, scripts, rows, worst, digest)
        total_scripts += scripts
        total_rows += rows
        if worst[0] > global_worst[0]:
            global_worst = worst
        summary.update(
            f"{shift},{scripts},{rows},{worst[0]},{worst[1]},{worst[2]},{digest}\n".encode()
        )

    print("SELECTED_FACTORS", len(selected))
    print("TOTAL_SCRIPTS", total_scripts)
    print("TOTAL_ROWS", total_rows)
    print("WORST", global_worst)
    print("SUMMARY_SHA256", summary.hexdigest())

    if wanted is None:
        assert len(selected) == 47
        assert total_scripts == EXPECTED_SCRIPTS
        assert total_rows == EXPECTED_ROWS
        assert global_worst == EXPECTED_WORST
        print("CERTIFIED")


if __name__ == "__main__":
    main()
