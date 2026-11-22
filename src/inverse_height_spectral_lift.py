#!/usr/bin/env python3
"""Exact height-sieved 3-adic inverse Collatz tree and Fourier-Mellin lift.
Standard-library-only arithmetic research. NOT a proof of Collatz or RH.
"""
from fractions import Fraction
from math import pi, log
from cmath import exp


def S(n):
    assert n > 0 and n % 2
    x = 3*n+1
    return x >> ((x & -x).bit_length()-1)


def a0(m):
    assert m>0 and m%2 and m%3
    return 2 if m%3 == 1 else 1


def parent_preimage(m,t):
    assert t>=0 and m>0 and m%2 and m%3
    n=((1 << (a0(m)+2*t))*m-1)//3
    assert S(n)==m
    return n


def first_turn(m):
    return 1 if m==1 else 0


def ancestor_count(m,X):
    if m%3==0 or X<1:return 0
    t=first_turn(m)
    start=t
    while parent_preimage(m,t)<=X:t+=1
    return t-start


def envelope(X,d):
    assert X>=1 and d>=0
    return max(X,3**d*(X+1)//2**d-1)


def inverse_levels(X,d):
    """Safe search: include nodes above X during traversal."""
    B=envelope(X,d)
    rows=[[1]]
    seen={1}
    for _ in range(d):
        next_row=[]
        for m in rows[-1]:
            if m%3==0:continue
            t=first_turn(m)
            while True:
                n=parent_preimage(m,t)
                if n>B:break
                assert n not in seen
                seen.add(n);next_row.append(n);t+=1
        rows.append(next_row)
    return rows


def forward_first_hits(X,d):
    out=[]
    for n in range(1,X+1,2):
        x=n
        for j in range(d+1):
            if x==1:
                out.append((n,j));break
            x=S(x)
    return out


def residues(X,d,q):
    M=3**q
    c=[0]*M
    for row in inverse_levels(X,d):
        for n in row:
            if n<=X:c[n%M]+=1
    return c


def phase_energy(c):
    M=len(c)
    return M*sum(v*v for v in c)-sum(c)**2


def sparse_energy_floor(c):
    N=sum(c);M=len(c)
    return max(0,N*(M-N))


def ray_residues(m,q):
    M=3**q
    t0=first_turn(m)
    values=[parent_preimage(m,t)%M for t in range(t0,t0+M)]
    assert sorted(values)==list(range(M))
    return values


def full_phase_height(m,q):
    """Exact least height where ONE inverse ray covers Z/(3^q)."""
    return parent_preimage(m,first_turn(m)+3**q-1)


def ray_phase_energy(m,q,turns):
    """For 0<=turns<=3^q, exact nonzero unweighted Fourier energy."""
    M=3**q
    assert 0<=turns<=M
    t0=first_turn(m)
    c=[0]*M
    for t in range(t0,t0+turns):
        c[parent_preimage(m,t)%M]+=1
    E=phase_energy(c)
    assert E==turns*(M-turns)
    return E


def full_ray_weighted_energy(m,q,s=2):
    """Strictly positive real-Mellin Fourier leakage, exact Fraction."""
    assert s>0
    M=3**q
    t0=first_turn(m)
    w=[Fraction(1,parent_preimage(m,t)**s)
       for t in range(t0,t0+M)]
    W=sum(w,Fraction(0))
    E=M*sum((v*v for v in w),Fraction(0))-W*W
    assert E>0
    return W,E


def exact_zeta_moment(X,d,s=2):
    assert s>=2
    return sum((Fraction(1,n**s)
                for row in inverse_levels(X,d) for n in row if n<=X),
               Fraction(0))


def branch_bound(X,d):
    """Uniform bound on # inverse children below safe envelope."""
    B=envelope(X,d)
    t=0
    while 2*4**(t+1)<=3*B+1:t+=1
    return t+1


def total_node_bound(X,d):
    L=branch_bound(X,d)
    return sum(L**j for j in range(d+1))


def numeric_fourier(c):
    M=len(c)
    return [sum(count*exp(2j*pi*h*r/M)
                for r,count in enumerate(c))
            for h in range(M)]


def benchmark(X=5000,d=8,q=3):
    c=residues(X,d,q)
    rows=inverse_levels(X,d)
    count=sum(c)
    return {
      'X':X,'d':d,'q':q,'rooted_count':count,
      'odd_candidates':(X+1)//2,
      'occupied_residues':sum(v>0 for v in c),
      'unweighted_fourier_energy':phase_energy(c),
      'depth_counts':[sum(n<=X for n in r) for r in rows],
      'safe_envelope':envelope(X,d)
    }


if __name__=='__main__':
    for q in range(1,6):
        X=full_phase_height(1,q)
        print('q',q,'mod',3**q,'minimum_height_bits',X.bit_length())
    print(benchmark())
    print('exact root full-ray s=2 phase leakage:',
          float(full_ray_weighted_energy(1,3,2)[1]))
