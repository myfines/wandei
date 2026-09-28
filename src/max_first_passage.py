#!/usr/bin/env python3
"""Maximal first-passage remainder bound for a hypothetical minimal counterexample.

For a coefficient first-passage word with q odd entries and total Terras-map
length j=floor(q*log_2(3))+1, the largest affine remainder compatible with first
passage is attained when the i-th odd entry is placed at

    s_i = floor((i-1)*log_2(3)).

Writing beta = j-q*log_2(3), this gives

    N <= [ (1/3) sum_{r<q} 2^{-frac(r alpha)} ] / (2^beta-1).

At special q which decompose into a few continued-fraction denominators of alpha,
Denjoy-Koksma bounds the Birkhoff sum by

    q/(2 ln 2) + dk_error,

where dk_error can be taken as the number of denominator blocks if one uses the
safe total-variation bound Var(f)<=1 for periodized f(x)=2^{-x}.

This module evaluates the resulting bound with high-precision Decimal arithmetic.
It is NOT interval arithmetic and therefore is an exploratory certificate generator,
not a formal numerical proof artifact.
"""

from __future__ import annotations

import argparse
from decimal import Decimal, localcontext
from typing import Tuple


DEFAULT_PREC = 140


def dk_maximal_remainder_bound(
    q: int,
    j: int,
    *,
    dk_error: int = 2,
    prec: int = DEFAULT_PREC,
) -> Tuple[Decimal, Decimal, Decimal]:
    """Return (alpha, beta, M_upper) using a supplied DK block error.

    ``dk_error`` is an additive upper bound for the Birkhoff-sum discrepancy
    from q/(2 ln 2). For q written as b convergent-denominator blocks, the safe
    choice b follows from Denjoy-Koksma with Var(f)<=1.
    """

    if q <= 0 or j <= 0:
        raise ValueError("q and j must be positive")
    if dk_error < 0:
        raise ValueError("dk_error must be nonnegative")

    with localcontext() as ctx:
        ctx.prec = prec
        two = Decimal(2)
        three = Decimal(3)
        ln2 = two.ln()
        alpha = three.ln() / ln2
        beta = Decimal(j) - Decimal(q) * alpha
        if beta <= 0:
            raise ValueError("j/q must lie strictly above log_2(3)")

        mean = Decimal(1) / (two * ln2)
        s_upper = Decimal(q) * mean + Decimal(dk_error)
        denominator = three * (two**beta - Decimal(1))
        m_upper = s_upper / denominator
        return +alpha, +beta, +m_upper


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", type=int, default=72_057_431_991)
    parser.add_argument("--j", type=int, default=114_208_327_604)
    parser.add_argument(
        "--dk-error",
        type=int,
        default=2,
        help="safe sum of Denjoy-Koksma variation errors over denominator blocks",
    )
    parser.add_argument("--prec", type=int, default=DEFAULT_PREC)
    args = parser.parse_args()

    alpha, beta, m_upper = dk_maximal_remainder_bound(
        args.q, args.j, dk_error=args.dk_error, prec=args.prec
    )

    with localcontext() as ctx:
        ctx.prec = args.prec
        two71 = Decimal(2) ** 71
        live = Decimal(2075) * (Decimal(2) ** 60)
        print(f"alpha = {alpha}")
        print(f"beta = j-q*alpha = {beta}")
        print(f"M_q upper estimate = {m_upper}")
        print(f"M_q / 2^71 = {m_upper / two71}")
        print(f"M_q / (2075*2^60) = {m_upper / live}")


if __name__ == "__main__":
    main()
