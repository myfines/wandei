"""Translated 46-step low-complexity excursion certificate.

This is an integer-only finite certificate for the first coefficient-contraction
branch.  It covers *every* length-46 mechanical factor, not only the factor at
phase zero.

Starting from an arbitrary critical-boundary state h=0, enumerate every
46-step defect path that stays in {0,1} and makes at most two upcrossings
0->1.  For each exact valuation script, intersect its 2-adic seed congruence
with the rigorous local boundary window

    2075*2^60 <= x < 2^73.

Every concrete local seed is checked to realize its script, and every distinct
seed is then continued until it drops below the verified frontier.

The result is a translation-invariant local exclusion: at any boundary time,
a surviving first-candidate orbit must, within the next 46 odd steps, either
reach defect h>=2 or make at least three upcrossings.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

STEPS = 46
LOW = 2075 * (1 << 60)
LOCAL_LIMIT = 1 << 73
MAX_UPCROSSINGS = 2


def exact_mechanical_letters(count: int) -> list[int]:
    p = 1
    floors: list[int] = []
    for _ in range(count + 1):
        floors.append(p.bit_length() - 1)
        p *= 3
    return [floors[j + 1] - floors[j] for j in range(count)]


def all_factors() -> dict[tuple[int, ...], int]:
    # The coding of an irrational rotation by one cut has factor complexity
    # n+1.  Thus a length-n factor has at most n+1 possibilities.  It is enough
    # to exhibit n+1 distinct exact factors.
    mech = exact_mechanical_letters(400)
    factors: dict[tuple[int, ...], int] = {}
    for shift in range(len(mech) - STEPS + 1):
        word = tuple(mech[shift : shift + STEPS])
        factors.setdefault(word, shift)
        if len(factors) == STEPS + 1:
            break
    assert len(factors) == STEPS + 1
    return factors


@dataclass(frozen=True)
class Script:
    h: int
    upcrossings: int
    A: int
    d: int
    packed_word: int


def extend_scripts(mechanical: tuple[int, ...]) -> list[Script]:
    states = [Script(0, 0, 0, 0, 0)]
    for j, r in enumerate(mechanical):
        nxt: list[Script] = []
        for s in states:
            # Stay at the same defect height: a_j=r_j.
            nxt.append(
                Script(
                    s.h,
                    s.upcrossings,
                    s.A + r,
                    3 * s.d + (1 << s.A),
                    s.packed_word | (r << (2 * j)),
                )
            )

            # Unit upcrossing 0->1: only r=2,a=1.
            if s.h == 0 and r == 2 and s.upcrossings < MAX_UPCROSSINGS:
                nxt.append(
                    Script(
                        1,
                        s.upcrossings + 1,
                        s.A + 1,
                        3 * s.d + (1 << s.A),
                        s.packed_word | (1 << (2 * j)),
                    )
                )

            # Unit return 1->0: a_j=r_j+1.
            if s.h == 1:
                a = r + 1
                nxt.append(
                    Script(
                        0,
                        s.upcrossings,
                        s.A + a,
                        3 * s.d + (1 << s.A),
                        s.packed_word | (a << (2 * j)),
                    )
                )
        states = nxt
    return states


def seed_residue(script: Script) -> tuple[int, int]:
    modulus = 1 << (script.A + 1)
    inv = pow(pow(3, STEPS, modulus), -1, modulus)
    residue = (inv * ((1 << script.A) - script.d)) % modulus
    assert residue & 1
    return residue, modulus


def lifts_in_window(residue: int, modulus: int):
    q = max(0, (LOW - residue + modulus - 1) // modulus)
    while True:
        x = residue + q * modulus
        if x >= LOCAL_LIMIT:
            return
        if x >= LOW:
            yield x
        q += 1


def odd_step(x: int) -> tuple[int, int]:
    y = 3 * x + 1
    a = (y & -y).bit_length() - 1
    return y >> a, a


def verify_script(seed: int, packed_word: int) -> None:
    x = seed
    for j in range(STEPS):
        x, a = odd_step(x)
        expected = (packed_word >> (2 * j)) & 3
        assert a == expected


def first_below_frontier(seed: int, limit: int = 2000) -> tuple[int, int]:
    x = seed
    for k in range(1, limit + 1):
        x, _ = odd_step(x)
        if x < LOW:
            return k, x
    raise AssertionError(f"no drop below frontier within {limit} odd steps: {seed}")


def main() -> None:
    factors = all_factors()
    assert len(factors) == 47

    script_count = 0
    rows: list[tuple[int, int, int, int, int, int]] = []
    # row = (shift, A, upcrossings, final_h, seed, packed_word)

    for mechanical, shift in sorted(factors.items(), key=lambda item: item[1]):
        scripts = extend_scripts(mechanical)
        script_count += len(scripts)
        for s in scripts:
            residue, modulus = seed_residue(s)
            for seed in lifts_in_window(residue, modulus):
                verify_script(seed, s.packed_word)
                rows.append(
                    (shift, s.A, s.upcrossings, s.h, seed, s.packed_word)
                )

    assert script_count == 2_896_739
    assert len(rows) == 1_289_079

    row_digest = hashlib.sha256()
    for shift, A, up, h, seed, _ in sorted(
        rows, key=lambda row: (row[0], row[1], row[2], row[3], row[4])
    ):
        row_digest.update(f"{shift},{A},{up},{h},{seed}\n".encode())
    assert (
        row_digest.hexdigest()
        == "bef8f2e5b0dd6f6881a648f52cbe14f991648ba9586100bfd438c9f48b688982"
    )

    seeds = sorted({row[4] for row in rows})
    assert len(seeds) == 1_141_211

    descent_digest = hashlib.sha256()
    worst = (0, 0, 0)  # step, seed, endpoint
    for seed in seeds:
        k, endpoint = first_below_frontier(seed)
        if k > worst[0]:
            worst = (k, seed, endpoint)
        descent_digest.update(f"{seed},{k},{endpoint}\n".encode())

    assert worst == (
        237,
        4810798976564215475307,
        1869158857707769661911,
    )
    assert (
        descent_digest.hexdigest()
        == "24eaa38073ec1139faf01b2cfa741b9de1ef1a7413fd035ed2634963347a6159"
    )

    print("CERTIFIED")
    print("length-46 mechanical factors =", len(factors))
    print("low-complexity scripts =", script_count)
    print("candidate rows =", len(rows))
    print("distinct local seeds =", len(seeds))
    print("latest drop below frontier = odd step", worst[0])
    print("worst local seed =", worst[1])
    print("worst endpoint =", worst[2])
    print("row sha256 =", row_digest.hexdigest())
    print("descent sha256 =", descent_digest.hexdigest())


if __name__ == "__main__":
    main()
