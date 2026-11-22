#!/usr/bin/env python3
"""Exact mixed renewal ledger and three-symbol CRT cylinders.

Odd-only Collatz. Finite descent certificates, NOT a proof of Collatz.
"""
from fractions import Fraction
from renewal_gate_fractal import S, gate

WEIGHTS = {'A':Fraction(4,5),'B1':Fraction(3,2),
           'B3':Fraction(8,7),'G_even':Fraction(3,5),
           'G_odd':Fraction(23,27)}

# domain residue, modulus, affine numerator, additive, denominator,
# exponent sum of odd steps, number of odd steps
THREE = {'1':(7,8,3,1,2,1,1),
         '3':(27,32,9,5,8,3,2),
         '5':(107,128,27,23,32,5,3)}

def one_renewal(n):
    assert n>1 and n%2==1
    if n%4==1: return 'A',S(n)
    kind,end,_,_=gate(n)
    return kind,end

def verify_weight(n):
    kind,end=one_renewal(n)
    ratio=Fraction(end+1,n+1)
    assert ratio<=WEIGHTS[kind]
    return kind,end,ratio

def ledger(seed,max_gate_steps=500):
    assert seed>1 and seed%2==1
    x=seed
    P=Fraction(1)
    path=[]
    for _ in range(max_gate_steps):
        kind,y,_=verify_weight(x)
        P*=WEIGHTS[kind]
        path.append((kind,x,y,P))
        if P<1: assert y<seed
        if y<seed or y==1: break
        x=y
    return path

def cylinder(word):
    """Single residue mod 2^(A+2) for any finite word in {B1,B3,G5}."""
    assert set(word)<=set('135')
    residue,bits,A,p,y=3,2,0,0,3
    for sym in word:
        r,mod,num,add,den,da,dp=THREE[sym]
        shift=(mod.bit_length()-1)-2
        assert (r-y)%4==0
        t=(((r-y)//4)*pow(3**p,-1,1<<shift))%(1<<shift)
        residue+=(1<<bits)*t
        y+=4*(3**p)*t
        assert y%mod==r
        val=num*y+add
        assert val%den==0
        y=val//den
        bits+=da
        A+=da
        p+=dp
        assert bits==A+2 and y%4==3
    assert 0<residue<1<<bits
    return residue,bits,y,A,p

def word_endpoint(n,word):
    assert n>0 and n%4==3
    x=n
    for sym in word:
        r,mod,num,add,den,da,dp=THREE[sym]
        assert x%mod==r
        expected=(num*x+add)//den
        kind,y,_,e=gate(x)
        if sym=='1':assert kind=='B1'
        elif sym=='3':assert kind=='B3'
        else:assert kind=='G_odd' and e==5
        assert y==expected
        x=y
    return x

def pair_family(q):
    assert q>=1
    w='15'*q
    r,bits,y,A,p=cylinder(w)
    assert (A,p,bits)==(6*q,4*q,6*q+2)
    assert word_endpoint(r,w)==y
    x=r
    for _ in range(q):
        numerator=81*x+73
        assert numerator%64==0
        x=numerator//64
    assert x==y and y>r
    return r,bits,y

def find_first_local_not_global(limit=1000):
    for n in range(3,limit+1,2):
        x=n
        for j in range(100):
            kind,y=one_renewal(x)
            if kind not in ('B1','B3'):
                if y>n:return n,j+1,kind,x,y
                break
            x=y
    return None

if __name__=='__main__':
    for q in range(1,9):
        print('B1-G5 pairs',q,'residue,bits,endpoint',pair_family(q))
    print('first local but not global:',find_first_local_not_global())
    print('ledger n=27:',ledger(27,max_gate_steps=8))
