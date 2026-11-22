#!/usr/bin/env python3
"""Exact one-bit potential charging each 20 mod 27 target-bearing odd block.

Applies to every positive odd Syracuse orbit, without any probability law.
A no-descent implication for a hypothetical least counterexample is included.
It is only a necessary bound; it does not prove Collatz.
"""
from math import log2

TAU = (11,13,9,17,1,15,5,7,3)


def bit_phi(r):
    return int(r % 9 == 4)


def edge_charge(r, a):
    assert 0 <= r < 9 and a >= 1
    h = int(a >= TAU[r])
    rp = (3*r+1)*pow(2,-a,9)%9
    slack = (a-1-h)-(bit_phi(rp)-bit_phi(r))
    assert slack >= 0
    return rp, h, slack


def odd_step(x):
    assert x > 0 and x & 1
    y = 3*x+1
    a = (y & -y).bit_length()-1
    return y >> a, a


def orbital_charge(seed,k):
    assert seed > 0 and seed & 1 and k >= 0
    n = seed
    A = H = slack = 0
    before = bit_phi(n)
    for j in range(k):
        y,a = odd_step(n)
        rp,h,s = edge_charge(n%9,a)
        assert y%9 == rp
        A += a
        H += h
        slack += s
        assert A >= (j+1)+H+bit_phi(y)-before
        n = y
    assert A-k-H == bit_phi(n)-before+slack
    return dict(seed=seed,k=k,terminal=n,A=A,H=H,slack=slack,
                phi_start=before,phi_end=bit_phi(n))


def no_descent_density_ceiling(seed,k):
    """Necessary H/k upper bound if all odd iterates stay >= seed."""
    assert seed >= 1 and seed & 1 and k >= 1
    result = orbital_charge(seed,k)
    if result['terminal'] < seed:
        return None
    x = seed
    for _ in range(k):
        x,_a = odd_step(x)
        if x < seed:
            return None
    bound = (log2(3)-1)+log2(1+1/(3*seed))+1/k
    assert result['H']/k <= bound+1e-10
    return bound


if __name__ == '__main__':
    for n in (7,11,27,139,661,9211,33511):
        print(n,orbital_charge(n,20))
    for k in (2,10,100,1000):
        print('large-seed ceiling at k=',k,':',
              (log2(3)-1)+log2(1+1/(3*10**12))+1/k)
