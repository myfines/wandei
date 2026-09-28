#!/usr/bin/env python3
"""Exact side-branch identities for the odd-only Collatz/Syracuse map.

If
    z = (3*x + 1) / 2**a
with odd x,z and a >= 1, then any exponent a-2r >= 1 of the same parity
also gives an odd positive predecessor of z:

    y_r = (2**(a-2r) * z - 1) / 3.

The key exact identity is

    x = 4**r * y_r + (4**r - 1)/3.

For a hypothetical least positive counterexample N, every positive predecessor
of a counterexample state is again a counterexample, so y_r >= N. Hence

    x >= 4**r * N + (4**r - 1)/3.

This yields a pointwise altitude bound on large 2-adic valuations.
"""

from __future__ import annotations


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    a = 0
    while n % 2 == 0:
        n //= 2
        a += 1
    return a


def syracuse_step(x: int) -> tuple[int, int]:
    if x <= 0 or x % 2 == 0:
        raise ValueError("x must be a positive odd integer")
    a = v2(3 * x + 1)
    return (3 * x + 1) // (2**a), a


def lowered_predecessor(z: int, a: int, r: int) -> int:
    """Predecessor obtained by lowering a by 2r."""
    if z <= 0 or z % 2 == 0:
        raise ValueError("z must be positive odd")
    if r < 1 or a - 2 * r < 1:
        raise ValueError("need r >= 1 and a-2r >= 1")
    num = (2 ** (a - 2 * r)) * z - 1
    if num % 3:
        raise AssertionError("lowered exponent should preserve divisibility by 3")
    y = num // 3
    if y <= 0 or y % 2 == 0:
        raise AssertionError("expected positive odd predecessor")
    return y


def side_branch_identity(x: int, r: int) -> int:
    """Recover y_r directly from x using x = 4^r y_r + (4^r-1)/3."""
    p = 4**r
    num = x - (p - 1) // 3
    if num % p:
        raise ValueError("x is not compatible with this side-branch depth")
    return num // p


def max_lowering_depth(a: int) -> int:
    """Maximum r for which a-2r >= 1."""
    if a < 1:
        raise ValueError("a must be positive")
    return (a - 1) // 2


def altitude_floor_for_exponent(a: int, N: int) -> int:
    """Least-counterexample lower bound on predecessor x for exponent a."""
    if N <= 0:
        raise ValueError("N must be positive")
    r = max_lowering_depth(a)
    p = 4**r
    return p * N + (p - 1) // 3


def exponent_cap_below_height_multiplier(M: int) -> int:
    """Conservative exponent cap below height M*N."""
    if M < 1:
        raise ValueError("M must be >= 1")
    r = 0
    p = 1
    while p * 4 <= M:
        p *= 4
        r += 1
    return 2 * r + 2


if __name__ == "__main__":
    for a in range(1, 11):
        print(a, max_lowering_depth(a), exponent_cap_below_height_multiplier(4 ** max_lowering_depth(a)))
