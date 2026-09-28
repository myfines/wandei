#!/usr/bin/env python3
"""Exact rational certificate for the critical Collatz density window.

No floating point is used in the certificate path.

For a hypothetical least counterexample N whose trajectory never descends
below N, Rozier--Terracol's paradoxical-prefix inequality implies that every
prefix with q odd terms in j Terras steps satisfies

    q/j >= alpha_N := log(2) / log(3 + 1/N).

A prefix can have multiplicative coefficient 3^q / 2^j < 1 only if

    alpha_N <= q/j < alpha := log(2) / log(3).

For N >= 2^71 this interval is extremely narrow. This script constructs
rigorous rational intervals for alpha_N and alpha using the atanh series for
logarithms, then certifies the first rational in that window with the smallest
possible denominator.

All certificate quantities are fractions.Fraction objects.
"""

from __future__ import annotations

from fractions import Fraction
from typing import List, Tuple, NamedTuple


class Interval(NamedTuple):
    lo: Fraction
    hi: Fraction


def log_bounds(x: Fraction, terms: int = 220) -> Interval:
    """Rigorous rational bounds for log(x), for x > 1."""
    if x <= 1:
        raise ValueError("x must be > 1")
    z = (x - 1) / (x + 1)
    z2 = z * z

    s = Fraction(0)
    p = z
    for n in range(terms):
        s += p / (2 * n + 1)
        p *= z2

    lo = 2 * s
    # log x = 2 sum z^(2n+1)/(2n+1).  The omitted terms are
    # positive.  Replacing every later denominator by the first omitted
    # denominator gives this geometric upper bound on the tail.
    tail = 2 * z ** (2 * terms + 1) / (
        (2 * terms + 1) * (1 - z2)
    )
    return Interval(lo, lo + tail)


def positive_ratio_bounds(num: Interval, den: Interval) -> Interval:
    """Bounds for A/B when A,B are positive intervals."""
    if num.lo <= 0 or den.lo <= 0:
        raise ValueError("intervals must be positive")
    return Interval(num.lo / den.hi, num.hi / den.lo)


def continued_fraction(x: Fraction) -> List[int]:
    """Canonical finite simple continued fraction of a nonnegative rational."""
    if x < 0:
        raise ValueError("expected nonnegative fraction")
    out: List[int] = []
    n, d = x.numerator, x.denominator
    while d:
        a, r = divmod(n, d)
        out.append(a)
        n, d = d, r
    return out


def from_continued_fraction(coeffs: List[int]) -> Fraction:
    if not coeffs:
        raise ValueError("empty continued fraction")
    value = Fraction(coeffs[-1], 1)
    for a in reversed(coeffs[:-1]):
        value = a + 1 / value
    return value


def simplest_fraction_between_positive_rationals(
    left: Fraction, right: Fraction
) -> Tuple[Fraction, List[int], int, int]:
    """Return the minimum-denominator rational strictly between two endpoints.

    We use the standard continued-fraction interval theorem.  In the generic
    case needed here, when the endpoint continued fractions share a prefix and
    first differ at partial quotients a and b, the simplest interior rational
    is the common prefix followed by min(a,b)+1.
    """
    if not (0 <= left < right):
        raise ValueError("need 0 <= left < right")

    a = continued_fraction(left)
    b = continued_fraction(right)
    k = 0
    while k < min(len(a), len(b)) and a[k] == b[k]:
        k += 1
    if k == min(len(a), len(b)):
        raise ValueError("endpoint-prefix case not implemented")

    candidate_cf = a[:k] + [min(a[k], b[k]) + 1]
    candidate = from_continued_fraction(candidate_cf)
    if not left < candidate < right:
        raise AssertionError("continued-fraction candidate is not interior")
    return candidate, a[:k], a[k], b[k]


def critical_window_certificate(
    n_floor: int = 2**71, log_terms: int = 220
) -> dict:
    """Build the exact certificate for N >= n_floor."""
    if n_floor <= 1:
        raise ValueError("n_floor must exceed 1")

    ln2 = log_bounds(Fraction(2), log_terms)
    ln3 = log_bounds(Fraction(3), log_terms)
    x = Fraction(3 * n_floor + 1, n_floor)
    ln3plus = log_bounds(x, log_terms)

    alpha = positive_ratio_bounds(ln2, ln3)
    alpha_n = positive_ratio_bounds(ln2, ln3plus)

    # Search the larger certified enclosure [alpha_N.lo, alpha.hi]. If its
    # simplest interior rational has denominator Q, the true narrower window
    # has no rational with denominator < Q. Then separately prove that the
    # candidate itself is in the true window using the opposite strict bounds.
    candidate, common, left_next, right_next = (
        simplest_fraction_between_positive_rationals(alpha_n.lo, alpha.hi)
    )

    if not alpha_n.hi < candidate < alpha.lo:
        raise AssertionError("candidate not certified inside true window")

    return {
        "n_floor": n_floor,
        "alpha": alpha,
        "alpha_n": alpha_n,
        "candidate": candidate,
        "common_cf": common,
        "left_next": left_next,
        "right_next": right_next,
        "denominator_lower_bound": candidate.denominator,
    }


def main() -> None:
    cert = critical_window_certificate()
    c = cert["candidate"]
    print(f"N floor: {cert['n_floor']}")
    print(f"common CF prefix length: {len(cert['common_cf'])}")
    print(
        "first differing partial quotients: "
        f"{cert['left_next']} and {cert['right_next']}"
    )
    print(
        "first certified rational in critical window: "
        f"{c.numerator}/{c.denominator}"
    )
    print(f"minimum possible denominator: {c.denominator}")
    print("certificate: exact rational arithmetic only")


if __name__ == "__main__":
    main()
