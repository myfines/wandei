#!/usr/bin/env python3
"""Meromorphic Dirichlet zeta of odd-Collatz one-step inverse rays.

Fully elementary formulas with stdlib complex arithmetic. The code is a
numerical regression aid; notes contain the exact proofs. Not Collatz/RH proof.
"""
from cmath import exp
from math import log, pi
from fractions import Fraction

LN4 = log(4.0)


def syracuse(n):
    assert n > 0 and n % 2
    v = 3*n + 1
    a = (v & -v).bit_length() - 1
    return v >> a


def target_base(m):
    assert m > 0 and m % 2 and m % 3
    return (4 if m % 3 == 1 else 2) * m


def ancestor(m, t):
    assert t >= 0
    B = target_base(m)
    n = (B * 4**t - 1) // 3
    assert syracuse(n) == m
    return n


def ray_sum(m, s, terms=120):
    """Direct series for Re(s)>0 only."""
    s = complex(s)
    assert s.real > 0
    return sum(exp(-s * log(ancestor(m, t))) for t in range(terms))


def ray_continuation(m, s, terms=80):
    """Continuation away from s=-j + 2*pi*i*ell/log(4), j>=0."""
    s = complex(s)
    B = target_base(m)
    prefactor = exp(s * log(3/B))
    coeff = 1+0j  # (s)_j/j!
    ans = 0j
    for j in range(terms):
        denominator = 1-exp(-(s+j)*LN4)
        if abs(denominator) < 1e-14:
            raise ValueError('at or too close to a pole')
        ans += coeff * (B**(-j)) / denominator
        coeff *= (s+j) / (j+1)
    return prefactor * ans


def lattice_pole(j, ell):
    assert isinstance(j,int) and j >= 0 and isinstance(ell,int)
    return complex(-j, 2*pi*ell/LN4)


def pole_residue(m,j,ell):
    """Exact formula (evaluated as float) for residues of ray_continuation."""
    s = lattice_pole(j,ell)
    B = target_base(m)
    poch = 1+0j
    for h in range(j):
        poch *= (s+h)/(h+1)
    return exp(s*log(3/B)) * poch * (B**(-j)) / LN4


def target_spectral_phase(m):
    """Logarithmic target fingerprint modulo one; one-step inverse ray."""
    B = target_base(m)
    return (log(B/3.0) / LN4) % 1.0


def first_harmonic_residue(m):
    """At s=2*pi*i/log4, a unit-circle phase divided by log4."""
    return pole_residue(m, 0, 1)


def universal_real_residue(j):
    """Independent of odd target m (provided 3 does not divide m)."""
    assert j>=0
    return (-1)**j / (3**j * LN4)


def finite_basin_square_sum(limit, max_odd_steps):
    """A finite lower bound for the odd 1-basin zeta at s=2."""
    total = Fraction(0)
    reached = 0
    for n in range(1,limit+1,2):
        x = n
        for _ in range(max_odd_steps+1):
            if x == 1:
                total += Fraction(1,n*n)
                reached += 1
                break
            x = syracuse(x)
    return total,reached


def run_checks():
    for m in (1,5,7,11,17):
        for t in range(30):
            assert syracuse(ancestor(m,t)) == m
        for s in (0.5, 1.3, 2.5, complex(.7,1.1), complex(1.4,14.1347)):
            direct = ray_sum(m,s,140)
            continued = ray_continuation(m,s,110)
            assert abs(direct-continued) < 5e-11 * max(1,abs(direct)),(m,s,direct,continued)
        for j in range(5):
            assert abs(pole_residue(m,j,0)-universal_real_residue(j)) < 1e-12
            s0 = lattice_pole(j,0)
            delta = 1e-7
            estimated = delta*ray_continuation(m,s0+delta,80)
            assert abs(estimated-universal_real_residue(j)) < 5e-6,(m,j,estimated)
    for j in range(5):
        assert abs(pole_residue(1,j,0)-pole_residue(7,j,0))<1e-12
    assert abs(pole_residue(1,0,1)-pole_residue(7,0,1))>0.1
    for m in (1,5,7,11,17):
        expected = exp(-2j*pi*target_spectral_phase(m))/LN4
        assert abs(first_harmonic_residue(m)-expected)<1e-12
    b,count=finite_basin_square_sum(1001,150)
    assert count == 501
    print('target pole phases:', {m:round(target_spectral_phase(m),8) for m in (1,5,7,11,17)})
    print('Z_1(1) =',ray_sum(1,1).real)
    print('Z_1(2) =',ray_sum(1,2).real)
    print('Odd basin square sum <=1001 =',float(b),'n=',count)
    print('Riemann odd zeta at s=2 =',pi*pi/8)
    print('Z_1(0.5+14.134725i) =',ray_sum(1,complex(.5,14.1347251417347)))
    print('PASS exact inverse rays, target real-pole residues, complex non-RH behavior, basin finite check')


if __name__ == '__main__':run_checks()
