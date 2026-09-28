#!/usr/bin/env python3
"""One-sided continued-fraction search for the Collatz crossing window.

Given a lower bound N for a hypothetical smallest counterexample, the
Rozier–Terracol harmonic-mean inequality gives the necessary condition

    log_2(3) < j/q <= log_2(3 + 1/N)

for any paradoxical prefix of that minimal counterexample.

This script searches the continued-fraction semiconvergents of log_2(3) and
returns the first upper rational approximation in that interval.

The Decimal computation is deliberately high precision, but this is not a formal
interval-arithmetic proof. It is intended as a reproducible certificate generator.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from typing import Iterable, Iterator, List, Optional, Tuple


DEFAULT_PREC = 140


def alpha_and_upper(N: int, prec: int = DEFAULT_PREC) -> Tuple[Decimal, Decimal]:
    if N <= 0:
        raise ValueError("N must be positive")
    with localcontext() as ctx:
        ctx.prec = prec
        ln2 = Decimal(2).ln()
        alpha = Decimal(3).ln() / ln2
        upper = (Decimal(3) + Decimal(1) / Decimal(N)).ln() / ln2
        return +alpha, +upper


def continued_fraction(x: Decimal, terms: int = 80, prec: int = DEFAULT_PREC) -> List[int]:
    if terms <= 0:
        return []
    out: List[int] = []
    with localcontext() as ctx:
        ctx.prec = prec
        y = +x
        for _ in range(terms):
            a = int(y)
            out.append(a)
            frac = y - Decimal(a)
            if not frac:
                break
            y = Decimal(1) / frac
    return out


def semiconvergents(cf: Iterable[int]) -> Iterator[Tuple[int, int, int, int]]:
    """Yield (index, t, numerator, denominator) intermediate convergents.

    At continued-fraction index n with partial quotient a_n, t runs from 1 to
    a_n. t=a_n is the ordinary convergent; smaller t are intermediates.
    """

    p_nm2, p_nm1 = 0, 1
    q_nm2, q_nm1 = 1, 0

    for n, a in enumerate(cf):
        for t in range(1, a + 1):
            p = t * p_nm1 + p_nm2
            q = t * q_nm1 + q_nm2
            yield n, t, p, q

        p = a * p_nm1 + p_nm2
        q = a * q_nm1 + q_nm2
        p_nm2, p_nm1 = p_nm1, p
        q_nm2, q_nm1 = q_nm1, q


def first_upper_semiconvergent(
    N: int,
    *,
    terms: int = 80,
    prec: int = DEFAULT_PREC,
) -> Optional[Tuple[int, int, Decimal, Decimal, int, int]]:
    """Return the least-denominator upper semiconvergent inside the window.

    Return tuple:
        (j, q, j/q-alpha, upper-j/q, cf_index, intermediate_t)
    """

    alpha, upper = alpha_and_upper(N, prec)
    cf = continued_fraction(alpha, terms=terms, prec=prec)

    best = None
    with localcontext() as ctx:
        ctx.prec = prec
        for n, t, p, q in semiconvergents(cf):
            ratio = Decimal(p) / Decimal(q)
            if alpha < ratio <= upper:
                candidate = (p, q, ratio - alpha, upper - ratio, n, t)
                if best is None or q < best[1]:
                    best = candidate
    return best


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--N",
        type=int,
        default=2**71,
        help="lower bound for a hypothetical smallest counterexample (default: 2^71)",
    )
    parser.add_argument("--terms", type=int, default=80)
    parser.add_argument("--prec", type=int, default=DEFAULT_PREC)
    args = parser.parse_args()

    alpha, upper = alpha_and_upper(args.N, args.prec)
    hit = first_upper_semiconvergent(args.N, terms=args.terms, prec=args.prec)

    print(f"N lower bound: {args.N}")
    print(f"alpha = log_2(3) = {alpha}")
    print(f"window width = {upper - alpha}")
    if hit is None:
        print("No upper semiconvergent found; increase --terms/--prec.")
        raise SystemExit(2)

    j, q, err, slack, idx, t = hit
    print(f"first hit: j/q = {j}/{q}")
    print(f"odd terms q = {q}")
    print(f"Terras-map steps j = {j}")
    print(f"j/q - alpha = {err}")
    print(f"upper - j/q = {slack}")
    print(f"continued-fraction index = {idx}, intermediate t = {t}")


if __name__ == "__main__":
    main()
