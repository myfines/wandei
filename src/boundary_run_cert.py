"""Finite certificate excluding long critical-boundary runs.

For the first coefficient-contraction candidate, every boundary state h_j=0
satisfies x_j < 2^73.  A run of 38 mechanical odd-only transitions therefore
reduces to finitely many local seed congruence classes below 2^73.

This script enumerates all 39 possible length-38 mechanical factors and every
lift of their exact seed residues in [2075*2^60, 2^73).  Every such concrete
state is checked to realize the factor and then to fall below the verified
frontier.
"""

from __future__ import annotations

import hashlib

STEPS = 38
LOW = 2075 * (1 << 60)
LOCAL_LIMIT = 1 << 73


def exact_mechanical_letters(count: int) -> list[int]:
    """Return r_j=floor((j+1)log2(3))-floor(j log2(3)) exactly."""
    p = 1
    floors: list[int] = []
    for _ in range(count + 1):
        floors.append(p.bit_length() - 1)
        p *= 3
    return [floors[j + 1] - floors[j] for j in range(count)]


def all_factors() -> dict[tuple[int, ...], int]:
    # A length-n mechanical factor changes only when the rotation phase crosses
    # one of n+1 points {-m alpha}, m=0,...,n.  Hence there are at most n+1
    # distinct factors.  It is therefore enough to exhibit n+1 distinct ones.
    mech = exact_mechanical_letters(200)
    factors: dict[tuple[int, ...], int] = {}
    for shift in range(len(mech) - STEPS + 1):
        word = tuple(mech[shift : shift + STEPS])
        factors.setdefault(word, shift)
        if len(factors) == STEPS + 1:
            break
    assert len(factors) == STEPS + 1
    return factors


def seed_residue(word: tuple[int, ...]) -> tuple[int, int, int]:
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


def odd_step(x: int) -> tuple[int, int]:
    y = 3 * x + 1
    a = (y & -y).bit_length() - 1
    return y >> a, a


def verify_prefix(seed: int, word: tuple[int, ...]) -> None:
    x = seed
    vals = []
    for _ in range(len(word)):
        x, a = odd_step(x)
        vals.append(a)
    assert tuple(vals) == word


def first_below_frontier(seed: int, limit: int = 1000) -> tuple[int, int]:
    x = seed
    for k in range(1, limit + 1):
        x, _ = odd_step(x)
        if x < LOW:
            return k, x
    raise AssertionError(f"no drop below frontier within {limit} odd steps: {seed}")


def main() -> None:
    factors = all_factors()
    assert len(factors) == 39

    rows = []
    worst = (0, 0, 0, 0)  # step, seed, endpoint, first shift

    for word, shift in factors.items():
        residue, A, modulus = seed_residue(word)
        q = max(0, (LOW - residue + modulus - 1) // modulus)
        while True:
            seed = residue + q * modulus
            if seed >= LOCAL_LIMIT:
                break

            verify_prefix(seed, word)
            k, endpoint = first_below_frontier(seed)
            if k > worst[0]:
                worst = (k, seed, endpoint, shift)
            rows.append((shift, A, residue, modulus, q, seed, k, endpoint))
            q += 1

    assert len(rows) == 103_987
    assert worst == (
        176,
        6801297196994201447531,
        1646280377576769250213,
        4,
    )

    lines = [
        f"{shift},{A},{residue},{modulus},{q},{seed},{k},{endpoint}"
        for shift, A, residue, modulus, q, seed, k, endpoint in sorted(
            rows, key=lambda row: (row[0], row[5])
        )
    ]
    digest = hashlib.sha256(("\n".join(lines) + "\n").encode()).hexdigest()
    assert digest == "3cc9c7b8230302f1619609530fa635e31b94d87215caa3c479a8b79137da64f5"

    print(f"length-{STEPS} mechanical factors = {len(factors)}")
    print(f"local candidate states = {len(rows)}")
    print(f"latest drop below verified frontier = odd step {worst[0]}")
    print(f"worst local seed = {worst[1]}")
    print(f"candidate-row sha256 = {digest}")


if __name__ == "__main__":
    main()
