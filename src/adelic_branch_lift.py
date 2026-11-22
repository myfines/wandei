#!/usr/bin/env python3
"""Exact CRT witnesses for 3-adic discontinuity of odd-only Collatz.

All checks are modular integer computations. Not a Collatz proof.
"""
from inverse_phase_odometer import odd_step, v2


def branch_residue(a: int) -> int:
    """Unique odd r modulo 2^(a+1) with v2(3*r+1)=a."""
    assert a >= 1
    modulus = 1 << (a+1)
    residue = (((1 << a)-1) * pow(3,-1,modulus)) % modulus
    assert residue % 2 and v2(3*residue+1)==a
    return residue


def crt_branch_seed(anchor: int, a: int, k: int) -> int:
    """n>anchor, n==anchor (mod 3^k) and valuation of 3*n+1 equals a."""
    assert anchor >= 1 and anchor % 2 and a >= 1 and k >= 1
    M2, M3 = 1 << (a+1), 3**k
    r = branch_residue(a)
    turns = ((anchor-r) * pow(M2,-1,M3)) % M3
    n = r + M2*turns
    if n <= anchor:
        n += M2*M3 * ((anchor-n)//(M2*M3)+1)
    assert n>anchor and n%2
    assert (n-anchor)%M3==0 and v2(3*n+1)==a
    return n


def image_limit_residue(anchor: int, a: int, k: int) -> int:
    """Fixed-a branch limit (3*anchor+1)/2^a, modulo 3^k."""
    assert anchor>0 and anchor%2 and a>=1 and k>=1
    return ((3*anchor+1)*pow(2,-a,3**k)) % (3**k)


def verify_fiber_limit(anchor: int, a: int, k: int):
    n = crt_branch_seed(anchor,a,k)
    image = odd_step(n)
    limit = image_limit_residue(anchor,a,k)
    assert image%(3**k)==limit
    return n,image,limit


def double_padics_crt(r2: int, r3: int, k2: int, k3: int) -> int:
    """Positive odd diagonal seed matching arbitrary finite 2-,3-adic prefixes."""
    assert k2>=1 and k3>=1 and r2%2
    M2,M3=2**k2,3**k3
    n = (r2%M2) + M2*(((r3-r2)*pow(M2,-1,M3))%M3)
    if n==0:
        n+=M2*M3
    assert n>0 and n%2 and n%M2==r2%M2 and n%M3==r3%M3
    return n


def main():
    print('3-adic cluster limits at anchor n=1 for different exponent branches')
    for a in (1,2,3,4):
        print('a',a,'limit mod 3^7',image_limit_residue(1,a,7))
        for k in (1,2,3,6):
            print('k',k,'(n,S(n),limit mod 3^k)',verify_fiber_limit(1,a,k))
    print('Double-adic CRT examples')
    for x,y in ((1,2),(7,19),(29,17)):
        print(x,y,double_padics_crt(x,y,8,6))


if __name__ == '__main__':
    main()
