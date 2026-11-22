#!/usr/bin/env python3
"""Exact one-gate 2-adic Haar moments, NOT orbit-wise time averages."""
from fractions import Fraction
from math import log2
from renewal_gate_fractal import S,gate,v2

def exact_moment(s):
    """E[(3^p/2^A)^s] for integer s>=0 on n in 3+4 Z_2."""
    assert isinstance(s,int) and s>=0
    z=Fraction(1,4)*Fraction(3,4)**s
    return Fraction(3,2)**s/(1-z)*(Fraction(1,2)+z/Fraction(2**(s+1)-1))

def theoretical_exponents():
    """Geometric-series result (E[odd steps], E[2-exponent sum])."""
    return Fraction(5,3),Fraction(3,1)

def finite_block_audit(count):
    """Independent finite integer check, no probabilistic independence."""
    assert count>0
    sum_p=sum_A=0
    sum_M=Fraction(0)
    e_freq={}
    for n in range(3,4*count+3,4):
        kind,end,p,e=gate(n)
        e_freq[e]=e_freq.get(e,0)+1
        x=n
        A=0
        for _ in range(p):
            a=v2(3*x+1)
            A+=a
            x=S(x)
        assert x==end
        sum_p+=p
        sum_A+=A
        sum_M+=Fraction(3**p,2**A)
    return Fraction(sum_p,count),Fraction(sum_A,count),sum_M/count,e_freq

if __name__=='__main__':
    print('Haar E[p],E[A]:',theoretical_exponents())
    for s in (0,1,2,3):print('E[M^%d]='%s,exact_moment(s))
    print('Haar E[log2 M]:',(5/3)*log2(3)-3)
    p,A,M,freq=finite_block_audit(10000)
    print('finite 10k block check:',float(p),float(A),float(M))
