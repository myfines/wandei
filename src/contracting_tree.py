#!/usr/bin/env python3
"""
Enumerate all reverse Collatz exponent words that can strictly contract size.

For a reverse word a_1,...,a_k,
    y = (2^A x - C)/3^k,  A=sum(a_i), C>0.

If 3^k / 2^A > 1, then y < x for every positive x in the corresponding
residue class (whenever the word is valid). Equivalently:
    A < k*log_2(3).

At fixed depth k this leaves only finitely many positive-integer exponent
words, so the search below is exact: there is no arbitrary exponent cutoff.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction
from typing import Iterator, Sequence


LOG2_3 = math.log2(3.0)


def compositions(total: int, length: int) -> Iterator[tuple[int, ...]]:
    """Yield all compositions of total into `length` positive integers."""
    if length < 1 or total < length:
        return
    if length == 1:
        yield (total,)
        return
    for first in range(1, total - length + 2):
        for tail in compositions(total - first, length - 1):
            yield (first,) + tail


def residue_for_word(word: Sequence[int]) -> int:
    """Unique residue mod 3^k on which this reverse exponent word is valid."""
    if not word or any(a < 1 for a in word):
        raise ValueError("word must contain positive exponents")

    C = 0
    A = 0
    for j, a in enumerate(word):
        C = (2**a) * C + 3**j
        A += a

    modulus = 3 ** len(word)
    return (C * pow(pow(2, A, modulus), -1, modulus)) % modulus


def max_contracting_exponent_sum(depth: int) -> int:
    """Largest integer A satisfying A < depth*log2(3)."""
    if depth < 1:
        raise ValueError("depth must be >= 1")
    # log2(3) is irrational, so floor is exact for the strict inequality
    # mathematically. Floating point is harmless at the small depths used here;
    # callers doing very large depths should replace this with certified bounds.
    return math.floor(depth * LOG2_3)


def contracting_words(depth: int) -> Iterator[tuple[int, ...]]:
    """Yield every depth-k exponent word with 3^k/2^A > 1."""
    max_A = max_contracting_exponent_sum(depth)
    for A in range(depth, max_A + 1):
        yield from compositions(A, depth)


def contracting_residues(depth: int) -> dict[int, tuple[int, ...]]:
    """One strongest (minimum-A) contracting word for each residue mod 3^k."""
    best: dict[int, tuple[int, ...]] = {}
    best_sum: dict[int, int] = {}
    for word in contracting_words(depth):
        r = residue_for_word(word)
        A = sum(word)
        if r not in best_sum or A < best_sum[r]:
            best_sum[r] = A
            best[r] = word
    return best


def survivor_layers(max_depth: int) -> list[dict[str, object]]:
    """Residue classes avoiding every contracting reverse path up to each depth.

    The set is built recursively: lift each survivor mod 3^(k-1) to its three
    classes mod 3^k, then remove residues admitting a contracting word of
    exact depth k.
    """
    survivors: set[int] = set()
    records: list[dict[str, object]] = []

    for k in range(1, max_depth + 1):
        bad = set(contracting_residues(k))
        modulus = 3**k

        if k == 1:
            survivors = {1, 2} - bad
        else:
            prev_modulus = 3 ** (k - 1)
            lifted = {
                r + t * prev_modulus
                for r in survivors
                for t in range(3)
            }
            survivors = lifted - bad

        total_units = 2 * 3 ** (k - 1)
        records.append(
            {
                "depth": k,
                "modulus": modulus,
                "contracting_word_count": sum(1 for _ in contracting_words(k)),
                "contracting_residue_count": len(bad),
                "survivor_count": len(survivors),
                "survivor_fraction": Fraction(len(survivors), total_units),
                "survivors": set(survivors),
            }
        )

    return records


def fmt(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-depth", type=int, default=12)
    parser.add_argument(
        "--show-small-survivors",
        type=int,
        default=20,
        help="Print this many smallest survivors at the final depth.",
    )
    args = parser.parse_args()

    layers = survivor_layers(args.max_depth)
    print("depth,contracting_words,contracting_residues,survivors,survivor_fraction")
    for row in layers:
        print(
            f"{row['depth']},{row['contracting_word_count']},"
            f"{row['contracting_residue_count']},{row['survivor_count']},"
            f"{fmt(row['survivor_fraction'])}"
        )

    final = sorted(layers[-1]["survivors"])
    print("smallest_final_survivors:", final[: args.show_small_survivors])


if __name__ == "__main__":
    main()
