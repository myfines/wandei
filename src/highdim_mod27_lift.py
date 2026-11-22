#!/usr/bin/env python3
"""Exact 15-state phase-charge lift of odd-only Collatz mod-27 target hits.

A proof certificate for the finite-state edge inequality. This is NOT
a proof of Collatz convergence; no mathematical novelty is asserted.
"""
from dataclasses import dataclass

TAU = (11,13,9,17,1,15,5,7,3)
UNITS9 = (1,2,4,5,7,8)
STATES = tuple((r,0) for r in range(9)) + tuple((r,1) for r in UNITS9)
PSI = {
 (0,0):0,(1,0):0,(2,0):0,(3,0):0,(4,0):0,
 (5,0):0,(6,0):0,(7,0):0,(8,0):-1,
 (1,1):0,(2,1):-1,(4,1):4,(5,1):1,(7,1):2,(8,1):3,
}

def step(n):
    assert n>0 and n%2
    m=3*n+1
    a=(m & -m).bit_length()-1
    return m>>a,a

def edge(state,a):
    """(next_state, current_hit, adjacent_hit, nonnegative_slack)."""
    assert state in PSI and a>=1
    r,previous=state
    hit=int(a>=TAU[r])
    new_r=((3*r+1)*pow(2,-a,9))%9
    new=(new_r,hit)
    assert new in PSI
    pair=previous*hit
    slack=a-1-hit-4*pair - (PSI[new]-PSI[state])
    return new,hit,pair,slack

def verify_all_edges():
    """204 transitions suffice for all positive exponents:
    above the threshold, a -> a+6 preserves residues/hit and adds 6 slack.
    """
    checked=0
    for state in STATES:
        for a in range(1,TAU[state[0]]+6):
            new,h,p,d=edge(state,a)
            assert d>=0,(state,a,d)
            checked+=1
            if a>=TAU[state[0]]:
                new2,h2,p2,d2=edge(state,a+6)
                assert (new2,h2,p2,d2)==(new,h,p,d+6)
    assert checked==204
    return checked

@dataclass
class Lift:
    n: int
    r: int
    previous_hit: int=0
    k: int=0
    A: int=0
    H: int=0
    P: int=0
    sigma: int=0

    @classmethod
    def start(cls,n):
        assert n>0 and n%2
        return cls(n,n%9)

    def advance(self):
        nxt,a=step(self.n)
        state,h,p,d=edge((self.r,self.previous_hit),a)
        assert d>=0
        self.n=nxt
        self.r,self.previous_hit=state
        self.k+=1;self.A+=a;self.H+=h;self.P+=p;self.sigma+=d
        return a,h,p,d

def lift_orbit(n,k):
    z=Lift.start(n)
    initial=PSI[(n%9,0)]
    for _ in range(k):
        z.advance()
        assert z.A-z.k-z.H-4*z.P==PSI[(z.r,z.previous_hit)]-initial+z.sigma
        assert z.A>=z.k+z.H+4*z.P-1
    return z

def positive_seed(word,residue9):
    """CRT: genuine positive odd seed with chosen valuations and start mod9."""
    word=tuple(word)
    A=C=0
    for a in word:
        assert a>=1
        C=3*C+(1<<A)
        A+=a
    m=1<<(A+1)
    r2=((1<<A)-C)*pow(3**len(word),-1,m)%m
    seed=r2 + m*(((residue9-r2)*pow(m,-1,9))%9)
    assert seed>0 and seed%2 and seed%9==residue9
    return seed

def explicit_minimum_script(bits):
    """Compute exact global minimal valuation cost for a finite hit pattern.

    b_k=0 is a terminal sentinel. Exponent symbols are only 1,2,6.
    """
    bits=tuple(bits)
    assert bits and all(b in (0,1) for b in bits)
    r=4 if bits[0] else 8
    start_r=r
    word=[]
    for j,b in enumerate(bits):
        following=bits[j+1] if j+1<len(bits) else 0
        a=1+(1+4*b)*following
        assert int(a>=TAU[r])==b
        word.append(a)
        r=((3*r+1)*pow(2,-a,9))%9
    H=sum(bits)
    P=sum(bits[i-1]*bits[i] for i in range(1,len(bits)))
    cost=len(bits)+H+4*P-bits[0]
    assert sum(word)==cost
    return cost,start_r,tuple(word),r

if __name__=='__main__':
    print('Proof-certificate finite edges:',verify_all_edges())
    for n in (31,47,661,9211,33511):
        z=lift_orbit(n,40)
        print('seed',n,'A',z.A,'H',z.H,'P',z.P,'sigma',z.sigma)
    for bits in ((1,0,1,1,0,1),(1,1,1,1),(0,1,0,1)):
        A,r,word,_=explicit_minimum_script(bits)
        n=positive_seed(word,r)
        z=lift_orbit(n,len(bits))
        assert z.A==A
        print('bits',bits,'cost',A,'script',word,'seed',n)
