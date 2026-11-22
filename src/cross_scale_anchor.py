#!/usr/bin/env python3
"""Odd Collatz: exact fixed-point shadows and 3-adic phase-lift height bounds.

Finite computations only, with standard-library integer arithmetic.
None of the tests purports to prove the Collatz conjecture.
"""
from inverse_phase_odometer import (
    ancestor, first_exponent, odd_step, phase_lift, v2, v3
)


def anchor_shadow_seed(k: int, q: int = 1) -> int:
    """Seed that follows stable 1's a=2 branch for exactly k odd steps."""
    assert k >= 1 and q > 0 and q % 2 == 1
    return 1 + 2*q*4**k


def anchor_shadow_at(k: int, j: int, q: int = 1) -> int:
    """Exact shadow state at j (0 <= j <= k)."""
    assert k >= 1 and 0 <= j <= k and q > 0 and q % 2 == 1
    return 1 + 2*q*3**j*4**(k-j)


def first_departure_certificate(k: int, q: int = 1):
    """Check exactly k a=2 exponents, then forced departure with a=1."""
    n = anchor_shadow_seed(k, q)
    x = n
    for j in range(k):
        assert x == anchor_shadow_at(k, j, q)
        assert v2(3*x + 1) == 2
        x = odd_step(x)
    assert x == anchor_shadow_at(k, k, q)
    assert v2(3*x + 1) == 1
    return n, x, 1


def min_turn_for_height(m: int, n: int, k: int) -> int:
    """Smallest t with 2^(a0+2t)*m >= 3*(n+3^k)+1."""
    assert m > 0 and m % 2 and m % 3 and n > 0 and k >= 1
    current = (1 << first_exponent(m))*m
    target = 3*(n + 3**k)+1
    t = 0
    while current < target:
        current *= 4
        t += 1
    return t


def phase_height_certificate(m: int, n: int, k: int):
    """Return (finite turn lift, exact lower bound, true direct-member flag).

    For n not a direct ancestor of m, 3^k>n implies
    R_m(t_k) >= n+3^k, hence t_k >= min_turn_for_height.
    Never materializes huge R_m(t_k).
    """
    assert m > 0 and m % 2 and m % 3 and n > 0 and n % 2 and k >= 1
    t = phase_lift(m, n, k)
    direct = odd_step(n) == m
    if direct:
        a = v2(3*n + 1)
        t_true = (a - first_exponent(m))//2
        assert t == t_true % (3**k)
        return t, 0, True
    if 3**k <= n:
        return t, 0, False
    lower = min_turn_for_height(m, n, k)
    assert t >= lower, (m,n,k,t,lower)
    return t, lower, False


def adelic_pair_certificate(n: int, m: int, k: int):
    """For common exponent script, differences scale by 3^k/2^A.

    Real * 2-adic * 3-adic separation factors multiply to exactly 1.
    """
    assert n > 0 and m > 0 and n % 2 and m % 2 and n != m and k >= 0
    x, y, A = n, m, 0
    for _ in range(k):
        ax, ay = v2(3*x+1), v2(3*y+1)
        assert ax == ay, 'exponent scripts differ'
        A += ax
        x, y = odd_step(x), odd_step(y)
    d0, dk = n-m, x-y
    assert (1 << A)*dk == (3**k)*d0
    assert v2(abs(dk)) == v2(abs(d0))-A
    assert v3(abs(dk)) == v3(abs(d0))+k
    return {'steps':k, 'A':A,
            'real_ratio':(3**k, 2**A),
            'two_adic_ratio':2**A,
            'three_adic_ratio':(1,3**k),
            'initial_difference':d0,
            'terminal_difference':dk}


def main():
    print('k, shadow seed, state after k, next exponent')
    for k in range(1, 11):
        print(k, *first_departure_certificate(k))
    print('m=1, n=7: k, t_k, lower turn bound')
    for k in range(3, 17):
        t, lower, _ = phase_height_certificate(1,7,k)
        print(k,t,lower)
    print('Exact triple-metric separation (k=10):')
    print(adelic_pair_certificate(1,anchor_shadow_seed(10),10))


if __name__ == '__main__':
    main()
