#!/usr/bin/env python3
"""Nine-dimensional exact min-plus transfer for finite mod-27 hit words.

Independently minimizes the 2-adic valuation sum over all positive odd
integer seeds realizing a hit/nonhit word. The output is not a Collatz proof.
"""
from itertools import product

TAU=(11,13,9,17,1,15,5,7,3)
INF=10**18

def transfer_matrices():
    matrix=[[[INF]*9 for _ in range(9)] for _ in range(2)]
    args=[[[None]*9 for _ in range(9)] for _ in range(2)]
    for r in range(9):
        # Finite complete set: for hits a>=TAU[r], a+6 is more expensive
        # but reaches the same residue, and is still a hit.
        for a in range(1,TAU[r]+6):
            h=int(a>=TAU[r])
            nxt=((3*r+1)*pow(2,-a,9))%9
            if a<matrix[h][r][nxt]:
                matrix[h][r][nxt]=a
                args[h][r][nxt]=a
    return matrix,args

MATRIX,ARG=transfer_matrices()

def exact_min_cost(bits):
    """Returns (minimum A, initial residue mod9, script, terminal residue)."""
    bits=tuple(bits)
    cost=[0]*9
    paths=[(r,()) for r in range(9)]
    for h in bits:
        assert h in (0,1)
        updated=[INF]*9
        fresh=[None]*9
        for r in range(9):
            if cost[r]>=INF:continue
            for nxt in range(9):
                a=MATRIX[h][r][nxt]
                value=cost[r]+a
                if value<updated[nxt]:
                    updated[nxt]=value
                    fresh[nxt]=(paths[r][0],paths[r][1]+(a,))
        cost,paths=updated,fresh
    end=min(range(9),key=lambda r:cost[r])
    return cost[end],paths[end][0],paths[end][1],end

def explicit_cost(bits):
    bits=tuple(bits)
    return len(bits)+sum(bits)+4*sum(bits[i-1]*bits[i]
           for i in range(1,len(bits)))-(bits[0] if bits else 0)

def canonical_word(bits):
    """Local 3-symbol construction, independent of the 9x9 shortest path."""
    bits=tuple(bits)
    word=tuple(1+(1+4*bits[i])*(bits[i+1] if i+1<len(bits) else 0)
               for i in range(len(bits)))
    return word, (4 if bits and bits[0] else 8)

def signed_partition(k):
    """Z_k(-1) = sum of (-1)^A_min over ALL 2^k hit words."""
    assert k>=1
    return sum((-1)**explicit_cost(b)
               for b in product((0,1),repeat=k))

def partition_at(k,z):
    """2x2 Ising-style transfer Z_k(z), exact when z is int/Fraction."""
    assert k>=1
    vector=(z,z)
    for _ in range(k-1):
        old0,old1=vector
        vector=(old0*z+old1*z,old0*z*z+old1*z**6)
    return sum(vector)

def verify_every_pattern(max_k=12):
    total=0
    for k in range(1,max_k+1):
        for bits in product((0,1),repeat=k):
            A,r,w,end=exact_min_cost(bits)
            construction,init=canonical_word(bits)
            assert A==explicit_cost(bits)==sum(construction)
            assert end in range(9)
            total+=1
        assert partition_at(k,-1)==(-2 if k==1 else 0)
    return total

if __name__=='__main__':
    print('Exhaustive finite words:',verify_every_pattern(12))
    for bits in ((1,0,1,1,0,1),(1,)*8,(0,1)*5):
        print('pattern',bits,'min-plus',exact_min_cost(bits),
              'explicit',canonical_word(bits))
    print('Euler phase partition:',[partition_at(k,-1) for k in range(1,9)])
