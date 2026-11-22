#!/usr/bin/env python3
"""Exact two-/three-adic bidirectional carries for odd-only Collatz.
Standard-library integers; neither code nor observations prove Collatz.
"""
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class Node:
    word: tuple
    k: int
    A: int
    C: int
    seed: int
    endpoint_residue: int
    endpoint: int
    overlap: int


def cylinder(word):
    word=tuple(word)
    assert all(isinstance(a,int) and a>=1 for a in word)
    A=C=0
    for a in word:
        C=3*C+(1<<A)
        A+=a
    k=len(word)
    modulus=1<<(A+1)
    r=((1<<A)-C)*pow(3**k,-1,modulus)%modulus
    assert 0<r<modulus and r%2
    y=(3**k*r+C)//(1<<A)
    assert 3**k*r+C==(1<<A)*y and y%2
    M=(C*pow(2,-A,3**k))%(3**k) if k else 0
    if k: assert 0<M<3**k
    q=(y-M)//(3**k)
    assert q in (0,1) and y==M+q*3**k and q==1-M%2
    return Node(word,k,A,C,r,M,y,q)


def extend_slow(d,a):
    nxt=cylinder(d.word+(a,))
    u=(nxt.seed-d.seed)//(1<<(d.A+1))
    assert nxt.seed==d.seed+(1<<(d.A+1))*u and 0<=u<2**a
    numer=(1<<a)*nxt.endpoint_residue-3*d.endpoint_residue-1
    assert numer%3**(d.k+1)==0
    v=numer//3**(d.k+1)
    assert 0<=v<2**a
    assert (1<<a)*nxt.overlap+v==d.overlap+2*u
    return nxt,u,v


def extend_fast(d,a):
    """Independent lifting algorithm requiring an inverse only modulo 2^a."""
    assert a>=1
    pow3=3**d.k
    u=((1<<(a-1))-(3*d.endpoint+1)//2)*pow(3*pow3,-1,1<<a)%(1<<a)
    r=d.seed+(u<<(d.A+1))
    y=(3*(d.endpoint+2*u*pow3)+1)//(1<<a)
    A=d.A+a
    C=3*d.C+(1<<d.A)
    k=d.k+1
    M=y%(3**k)
    q=(y-M)//(3**k)
    v=((1<<a)*M-3*d.endpoint_residue-1)//3**k
    assert q in (0,1) and v>=0 and v<2**a
    assert v==d.overlap+2*u-(1<<a)*q
    assert 3**k*r+C==(1<<A)*y
    return Node(d.word+(a,),k,A,C,r,M,y,q),u,v


def syracuse(n):
    assert n>0 and n%2
    y=3*n+1
    a=(y&-y).bit_length()-1
    return y>>a,a


def critical_rotation_word(k):
    """Exact floor(j log2 3) differences; no floating-point arithmetic."""
    power=1
    previous=0
    for _ in range(k):
        power*=3
        current=power.bit_length()-1
        yield current-previous
        previous=current


def log_lock_depth(n):
    """Guaranteed depth at which both canonical residues identify real orbit."""
    assert n>0 and n%2
    return n.bit_length()


def self_check():
    root=cylinder(())
    for depth in range(5):
        for word in product((1,2,3,4),repeat=depth):
            d=cylinder(word)
            x=d.seed
            for a in word:
                x,b=syracuse(x)
                assert b==a
            assert x==d.endpoint
            for a in (1,2,3,4,5):
                assert extend_slow(d,a)==extend_fast(d,a)
    for N in range(1,1500,2):
        d=root
        x=N
        for k in range(1,log_lock_depth(N)+6):
            x,a=syracuse(x)
            d,u,v=extend_fast(d,a)
            if k>=log_lock_depth(N):
                assert d.seed==N and d.endpoint_residue==x and d.overlap==0
            if k>log_lock_depth(N):
                assert u==v==0
    print("PASS: exact cylinders, dual-carry balance, positive-seed log lock")


if __name__=="__main__":
    self_check()
    d=cylinder(())
    for j,a in enumerate(critical_rotation_word(4096),1):
        d,u,v=extend_fast(d,a)
        if j in (16,64,256,1024,4096):
            print(j,d.A,d.seed.bit_length(),d.endpoint_residue.bit_length(),d.overlap)
