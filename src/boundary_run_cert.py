"""Finite certificate excluding long critical-boundary runs.

For the first coefficient-contraction candidate, every boundary state h_j=0
satisfies x_j < 2^73. A run of 35 mechanical odd-only transitions therefore
reduces to finitely many local seed congruence classes below 2^73.

This script enumerates all 36 possible length-35 mechanical factors and every
lift of their exact seed residues in [2075*2^60, 2^73). Every such concrete
state is checked to fall below the verified frontier. One representative of
each residue class is also checked to realize the exact factor; every lift has
the same first-35 valuation word because it is congruent modulo 2^(A+1).
"""

from __future__ import annotations

import hashlib

STEPS = 35
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
    # one of n+1 points {-m alpha}, m=0,...,n. Hence there are at most n+1
    # distinct factors. It is enough to exhibit n+1 distinct ones.
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
    assert len(factors) == 36

    digest = hashlib.sha256()
    row_count = 0
    worst = (0, 0, 0, 0)  # step, seed, endpoint, first shift

    for word, shift in sorted(factors.items(), key=lambda item: item[1]):
        residue, A, modulus = seed_residue(word)

        # The residue class itself realizes the exact valuation word; every
        # lift by the modulus has the same first STEPS valuations.
        representative = residue if residue else modulus
        verify_prefix(representative, word)

        q = max(0, (LOW - residue + modulus - 1) // modulus)
        while True:
            seed = residue + q * modulus
            if seed >= LOCAL_LIMIT:
                break

            k, endpoint = first_below_frontier(seed)
            if k > worst[0]:
                worst = (k, seed, endpoint, shift)
            digest.update(
                f"{shift},{A},{residue},{modulus},{q},{seed},{k},{endpoint}\n".encode()
            )
            row_count += 1
            q += 1

    assert row_count == 2_691_480
    assert worst == (
        252,
        4683730498974184172651,
        1556394996594058312685,
        28,
    )

    hexdigest = digest.hexdigest()
    assert hexdigest == "a8f4322128bd42e4db3111c8073b7fed59a8b0cf28102988372fb9d08f8cc86b"

    print(f"length-{STEPS} mechanical factors = {len(factors)}")
    print(f"local candidate states = {row_count}")
    print(f"latest drop below verified frontier = odd step {worst[0]}")
    print(f"worst local seed = {worst[1]}")
    print(f"candidate-row sha256 = {hexdigest}")


if __name__ == "__main__":
    main()
