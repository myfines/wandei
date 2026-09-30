"""Finite certificate for low-complexity critical-defect excursions.

This script is integer-only. It enumerates the first 46 odd-only valuation
prefixes whose critical-defect coordinate h_j stays in {0,1}, starts at 0,
and makes at most two upcrossings 0->1. Between state changes the valuation
is the mechanical reference value.

It then intersects the exact 2-adic seed congruence with the current first-
contraction candidate interval and checks that every surviving concrete seed
falls below itself under the odd-only Syracuse map.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

STEPS = 46
LOW = 2075 * (1 << 60)
# Clean first-contraction certificate: N < (4/3) * 2^71.
MAX_N = (4 * (1 << 71) - 1) // 3
MAX_UPCROSSINGS = 2


def floor_log2_3_power(j: int) -> int:
    # 3**j is never a power of two for j>0, so bit_length-1 is exact floor.
    return (3**j).bit_length() - 1


FLOORS = [floor_log2_3_power(j) for j in range(STEPS + 1)]
MECHANICAL = tuple(FLOORS[j + 1] - FLOORS[j] for j in range(STEPS))
assert set(MECHANICAL) <= {1, 2}
assert sum(MECHANICAL) == 72


@dataclass(frozen=True)
class Prefix:
    h: int
    upcrossings: int
    word: tuple[int, ...]
    events: tuple[tuple[str, int], ...]


def generate_prefixes() -> list[Prefix]:
    states = [Prefix(0, 0, (), ())]
    for j, r in enumerate(MECHANICAL):
        nxt: list[Prefix] = []
        for s in states:
            # Stay at the same defect height: a_j = r_j.
            nxt.append(Prefix(s.h, s.upcrossings, s.word + (r,), s.events))

            # Unit upcrossing 0->1 is possible only when r_j=2, using a_j=1.
            if s.h == 0 and r == 2 and s.upcrossings < MAX_UPCROSSINGS:
                nxt.append(
                    Prefix(
                        1,
                        s.upcrossings + 1,
                        s.word + (1,),
                        s.events + (("U", j),),
                    )
                )

            # Unit return 1->0 uses a_j=r_j+1.
            if s.h == 1:
                nxt.append(
                    Prefix(
                        0,
                        s.upcrossings,
                        s.word + (r + 1,),
                        s.events + (("D", j),),
                    )
                )
        states = nxt

    # Drop the pure mechanical path (zero upcrossings).
    return [s for s in states if s.upcrossings > 0]


def seed_residue(word: tuple[int, ...]) -> tuple[int, int, int]:
    """Return (least residue, A, modulus) for this exact odd-only word."""
    A = 0
    d = 0
    for a in word:
        d = 3 * d + (1 << A)
        A += a

    modulus = 1 << (A + 1)
    inv = pow(pow(3, len(word), modulus), -1, modulus)
    residue = (inv * ((1 << A) - d)) % modulus
    assert residue & 1
    return residue, A, modulus


def lifts_in_window(residue: int, modulus: int):
    q = max(0, (LOW - residue + modulus - 1) // modulus)
    while True:
        n = residue + q * modulus
        if n > MAX_N:
            return
        if n >= LOW:
            yield n
        q += 1


def odd_step(x: int) -> tuple[int, int]:
    y = 3 * x + 1
    a = (y & -y).bit_length() - 1
    return y >> a, a


def first_descent(seed: int, limit: int = 1000):
    x = seed
    valuations: list[int] = []
    for k in range(1, limit + 1):
        x, a = odd_step(x)
        valuations.append(a)
        if x < seed:
            return k, x, tuple(valuations)
    raise AssertionError(f"no descent within {limit} odd steps for {seed}")


def main() -> None:
    prefixes = generate_prefixes()
    exact1 = sum(s.upcrossings == 1 for s in prefixes)
    exact2 = sum(s.upcrossings == 2 for s in prefixes)
    assert exact1 == 609
    assert exact2 == 56_405

    rows = []
    for s in prefixes:
        residue, A, modulus = seed_residue(s.word)
        for seed in lifts_in_window(residue, modulus):
            k, x, valuations = first_descent(seed)
            # Verify that the concrete seed really realizes the enumerated prefix.
            assert valuations[:STEPS] == s.word
            rows.append((s.upcrossings, s.h, A, s.events, seed, k, x))

    c1 = sum(row[0] == 1 for row in rows)
    c2 = sum(row[0] == 2 for row in rows)
    assert c1 == 49
    assert c2 == 4_823
    assert len(rows) == 4_872

    worst = max(rows, key=lambda row: row[5])
    assert worst[5] == 145

    digest_lines = []
    for up, h, A, events, seed, k, x in sorted(
        rows, key=lambda row: (row[0], row[3], row[4])
    ):
        event_text = ";".join(f"{kind}{j + 1}" for kind, j in events)
        digest_lines.append(f"{up},{h},{A},{event_text},{seed},{k},{x}")
    digest = hashlib.sha256(("\n".join(digest_lines) + "\n").encode()).hexdigest()
    assert digest == "b9dcfee89ca967a162e9d0e7a18e8ce49ccad111b665d3fa765e714ff8989b05"

    print(f"mechanical A_46 = {sum(MECHANICAL)}")
    print(f"exactly one upcrossing scripts = {exact1}")
    print(f"exactly two upcrossing scripts = {exact2}")
    print(f"candidate seeds, one upcrossing = {c1}")
    print(f"candidate seeds, two upcrossings = {c2}")
    print(f"candidate seeds total = {len(rows)}")
    print(f"latest first descent = odd step {worst[5]}")
    print(f"worst seed = {worst[4]}")
    print(f"candidate-row sha256 = {digest}")


if __name__ == "__main__":
    main()
