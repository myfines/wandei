"""Translated 46-step certificate with at most two total defect upsteps.

First-candidate local class:
- start at a critical-boundary state h=0;
- consider the next 46 odd-only transitions;
- allow at most two total upward defect transitions h -> h+1;
- exclude the rare heavy direct return h=1,r=2,a=3.

Because every upward transition raises h by exactly one and the path starts at
h=0, at most two total upsteps imply h<=2 throughout the window.  All allowed
stay/down transitions from h=0,1,2 are enumerated exactly.

All 47 length-46 mechanical factors are covered.  Every valuation script is
intersected with the sharp local boundary window certified by
sharp_boundary_altitude_cert.py.  Every concrete local seed is checked to
realize its script and is then continued until it falls below the verified
frontier.

A successful full run proves: away from the globally rare heavy-return events,
any surviving boundary-started 46-step window must contain at least three total
defect upsteps.
"""

from __future__ import annotations

import hashlib
import sys

import sharp_boundary_altitude_cert as alt

STEPS = 46
LOW = alt.N0
LOCAL_LIMIT = alt.HIGH
MAX_UPSTEPS = 2
POW3 = 3**STEPS

EXPECTED_SCRIPTS = 2_184_132
EXPECTED_ROWS = 587_410
EXPECTED_WORST = (
    237,
    4_810_798_976_564_215_475_307,
    1_869_158_857_707_769_661_911,
)
EXPECTED_SUMMARY_SHA256 = (
    "2fda262c322cbf4b179d50607cdda9e8d99444088d7ae906528f04af37f54c38"
)


def exact_mechanical_letters(count: int) -> list[int]:
    p = 1
    floors: list[int] = []
    for _ in range(count + 1):
        floors.append(p.bit_length() - 1)
        p *= 3
    return [floors[j + 1] - floors[j] for j in range(count)]


def all_factors() -> list[tuple[int, tuple[int, ...]]]:
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
    # State = (h, total_upsteps, A, affine_d, packed_3bit_valuation_word).
    states = [(0, 0, 0, 0, 0)]

    for j, r in enumerate(mechanical):
        nxt = []
        bit = 3 * j

        for h, up, A, d, code in states:
            # Since a>=1, h' <= h+r-1.  Starting from h=0 with at most two
            # total upsteps means no reachable state can exceed h=2.
            max_h_next = h + r - 1
            for h_next in range(max_h_next + 1):
                a = h + r - h_next
                assert a >= 1

                # h=1,r=2,h'=0 means a=3: the rare odd-height heavy direct
                # repayment.  It is excluded from this local certificate and
                # handled globally by the sharp phase-count certificate.
                if h == 1 and r == 2 and h_next == 0:
                    continue

                up_next = up + (h_next == h + 1)
                if up_next > MAX_UPSTEPS:
                    continue

                # Any h_next>2 would require at least three total upsteps from
                # the initial h=0, so it cannot survive the previous test.
                assert h_next <= 2

                nxt.append(
                    (
                        h_next,
                        up_next,
                        A + a,
                        3 * d + (1 << A),
                        code | (a << bit),
                    )
                )

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
                    expected = (code >> (3 * (k - 1))) & 7
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
        assert summary.hexdigest() == EXPECTED_SUMMARY_SHA256
        print("CERTIFIED")


if __name__ == "__main__":
    main()
