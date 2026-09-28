#!/usr/bin/env python3
"""
Reverse-barrier experiments for the odd-only Collatz/Syracuse map.

Exploratory research code only; this is NOT a proof of the Collatz conjecture.

Odd-only forward map:
    S(x) = (3x + 1) / 2^v2(3x+1)

For an actual positive odd x not divisible by 3, the smallest positive odd
preimage is
    R(x) = (2x - 1)/3   if x == 2 (mod 3)  [reverse exponent a=1]
           (4x - 1)/3   if x == 1 (mod 3)  [reverse exponent a=2]

If 3|x, there is no odd preimage under S.

If N is a hypothetical minimal positive counterexample and x lies on its
odd-only orbit, then every positive reverse ancestor y of x is also a
counterexample, so y >= N.

For a valid reverse exponent word a_1,...,a_k:
    y_k = (2^A x - C_k) / 3^k,  A = sum(a_i), C_k > 0.
Thus y_k >= N implies the necessary barrier
    x/N > 3^k / 2^A.

This file studies the deterministic smallest-exponent reverse chain and
the induced residue classes modulo powers of 3.
"""

from __future__ import annotations

import argparse
import itertools
from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Sequence


@dataclass(frozen=True)
class ReverseProfile:
    residue: int
    modulus_power: int
    exponents: tuple[int, ...]
    barrier: Fraction
    barrier_depth: int
    stopped_on_multiple_of_three: bool

    @property
    def depth(self) -> int:
        return len(self.exponents)


def min_reverse_step(x: int) -> tuple[int, int] | None:
    """Return (preimage, exponent) for an actual positive odd integer x."""
    if x <= 0 or x % 2 == 0:
        raise ValueError("x must be a positive odd integer")
    r = x % 3
    if r == 0:
        return None
    if r == 2:
        return (2 * x - 1) // 3, 1
    return (4 * x - 1) // 3, 2


def reverse_profile_for_residue(residue: int, m: int) -> ReverseProfile:
    """Profile the minimum-exponent reverse chain from a class mod 3^m.

    A residue modulo an odd modulus does NOT encode parity. Therefore we
    evolve residue classes directly rather than pretending the canonical
    representative is itself an odd Collatz state.

    The first m reverse decisions are determined by x mod 3^m, unless the
    reverse chain terminates earlier at a state divisible by 3.
    """
    if m < 1:
        raise ValueError("m must be >= 1")
    modulus = 3**m
    r = residue % modulus
    if gcd(r, 3) != 1:
        raise ValueError("residue must be a unit modulo 3^m")

    cur = r
    current_power = m
    exponents: list[int] = []
    A = 0
    best = Fraction(1, 1)
    best_depth = 0
    stopped = False

    for k in range(1, m + 1):
        if cur % 3 == 0:
            stopped = True
            break

        a = 1 if cur % 3 == 2 else 2
        exponents.append(a)
        A += a

        beta = Fraction(3**k, 2**A)
        if beta > best:
            best = beta
            best_depth = k

        # If x == cur (mod 3^current_power), then
        # y=(2^a x -1)/3 is determined modulo 3^(current_power-1).
        numerator = (2**a) * cur - 1
        quotient = numerator // 3
        current_power -= 1
        if current_power > 0:
            cur = quotient % (3**current_power)
        else:
            cur = quotient

    if len(exponents) < m and cur % 3 == 0:
        stopped = True

    return ReverseProfile(
        residue=r,
        modulus_power=m,
        exponents=tuple(exponents),
        barrier=best,
        barrier_depth=best_depth,
        stopped_on_multiple_of_three=stopped,
    )


def residue_for_surviving_word(word: Sequence[int]) -> int:
    """Return the unique residue mod 3^m realizing a full word in {1,2}^m.

    For
        R^m(x) = (2^A x - C_m)/3^m,
    integrality gives
        2^A x == C_m (mod 3^m).

    Every word over {1,2} of length m has exactly one such residue class.
    The class contains odd integers because 3^m is odd.
    """
    if not word:
        raise ValueError("word must be non-empty")
    if any(a not in (1, 2) for a in word):
        raise ValueError("word entries must be 1 or 2")

    C = 0
    A = 0
    for k, a in enumerate(word):
        C = (2**a) * C + 3**k
        A += a

    modulus = 3 ** len(word)
    twoA = pow(2, A, modulus)
    return (C * pow(twoA, -1, modulus)) % modulus


def surviving_residues(m: int) -> dict[tuple[int, ...], int]:
    """Map each full reverse word of length m to its unique residue mod 3^m."""
    return {
        word: residue_for_surviving_word(word)
        for word in itertools.product((1, 2), repeat=m)
    }


def brute_force_summary(m: int) -> dict[str, object]:
    """Enumerate all units modulo 3^m and summarize reverse-chain depth."""
    modulus = 3**m
    total_units = 2 * 3 ** (m - 1)
    depth_counts = [0] * (m + 1)
    max_barrier = Fraction(1, 1)
    max_barrier_residue = None

    for r in range(1, modulus):
        if r % 3 == 0:
            continue
        p = reverse_profile_for_residue(r, m)
        depth_counts[p.depth] += 1
        if p.barrier > max_barrier:
            max_barrier = p.barrier
            max_barrier_residue = r

    full_depth = depth_counts[m]
    return {
        "m": m,
        "modulus": modulus,
        "total_units": total_units,
        "depth_counts": depth_counts,
        "full_depth_count": full_depth,
        "predicted_full_depth_count": 2**m,
        "full_depth_fraction": Fraction(full_depth, total_units),
        "predicted_fraction": Fraction(2, 3) ** (m - 1),
        "max_barrier": max_barrier,
        "max_barrier_residue": max_barrier_residue,
    }


def verify_word_bijection(m: int) -> bool:
    """Check the exact word <-> surviving-residue correspondence."""
    mapping = surviving_residues(m)
    if len(set(mapping.values())) != 2**m:
        return False
    for word, residue in mapping.items():
        p = reverse_profile_for_residue(residue, m)
        if p.exponents != word:
            return False
    return True


def format_fraction(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=10)
    parser.add_argument(
        "--bruteforce-limit",
        type=int,
        default=12,
        help="Do not brute-force m above this value.",
    )
    args = parser.parse_args()

    print("m,total_units,full_depth,predicted,fraction,max_barrier,max_barrier_residue,bijection")
    for m in range(1, args.max_m + 1):
        bijection = verify_word_bijection(m)
        if m <= args.bruteforce_limit:
            s = brute_force_summary(m)
            print(
                f"{m},{s['total_units']},{s['full_depth_count']},"
                f"{s['predicted_full_depth_count']},"
                f"{format_fraction(s['full_depth_fraction'])},"
                f"{format_fraction(s['max_barrier'])},"
                f"{s['max_barrier_residue']},{bijection}"
            )
        else:
            total = 2 * 3 ** (m - 1)
            full = 2**m
            frac = Fraction(full, total)
            print(f"{m},{total},{full},{full},{format_fraction(frac)},,,{bijection}")


if __name__ == "__main__":
    main()
