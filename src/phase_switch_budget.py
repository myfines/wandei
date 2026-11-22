#!/usr/bin/env python3
"""Exact 2-adic phase budgets and switching audits for the odd Syracuse map.
Research experiment only. Standard library; no Collatz proof.
"""
from dataclasses import dataclass
from fractions import Fraction
from math import lcm

def v2(n):
    if n==0: return None
    n=abs(n)
    return (n & -n).bit_length()-1

def syracuse(n):
    assert n>0 and n%2==1
    y=3*n+1
    a=v2(y)
    return y>>a,a

@dataclass(frozen=True)
class Template:
    exponents: tuple
    A: int
    C: int
    D: int

    @property
    def fixed_point(self):
        return Fraction(self.C,self.D)
    def defect(self,n):
        return self.D*n-self.C
    def phase_budget(self,n):
        return v2(self.defect(n))
    def repeats(self,n):
        s=self.phase_budget(n)
        return None if s is None else max(0,(s-1)//self.A)
    def matching(self,n,q):
        assert q>=1
        s=self.phase_budget(n)
        return s is None or s>=q*self.A+1

def template(exponents):
    exponents=tuple(exponents)
    assert exponents and all(isinstance(a,int) and a>=1 for a in exponents)
    C=A=0
    for a in exponents:
        C=3*C+(1<<A)
        A+=a
    D=(1<<A)-3**len(exponents)
    assert C%2 and D%2 and D!=0
    return Template(exponents,A,C,D)

def direct_matches(n,w,q):
    assert n>0 and n%2==1
    x=n
    for _ in range(q):
        for a in w.exponents:
            x,b=syracuse(x)
            if b!=a: return False
    return True

def minimum_seed(w,q):
    modulus=1<<(q*w.A+1)
    n=w.C*pow(w.D,-1,modulus)%modulus
    assert n>0 and n%2==1
    return n

def common_phase_budget(w,z):
    return v2(w.D*z.C-z.D*w.C)

def common_prefix_divergence(w,z):
    total=0
    for j in range(lcm(len(w.exponents),len(z.exponents))):
        a=w.exponents[j%len(w.exponents)]
        b=z.exponents[j%len(z.exponents)]
        if a!=b: return total+min(a,b)
        total+=a
    return None

def sync_transition(w,z,n):
    assert direct_matches(n,z,1)
    x=n
    for _ in z.exponents: x,_=syracuse(x)
    K=w.D*z.C-z.D*w.C
    numerator=3**len(z.exponents)*w.defect(n)+K
    assert numerator%(1<<z.A)==0
    assert w.defect(x)==numerator//(1<<z.A)
    return v2(w.defect(n)),v2(w.defect(x)),v2(K)

def recharged_seed(h):
    assert h>=2
    n=pow(3,-1,1<<(h+1))
    x,a=syracuse(n)
    assert v2(n-1)==1 and a==1 and v2(x-1)>=h
    return n,x,v2(x-1)

if __name__=='__main__':
    w=template((1,2))
    print('Word (1,2):', 'fixed 2-adic point',w.fixed_point)
    for q in range(1,11):
        n=minimum_seed(w,q)
        assert n==2**(3*q+1)-5
        assert direct_matches(n,w,q)
        x=n
        for _ in range(2*q): x,_=syracuse(x)
        assert x==2*9**q-5 and syracuse(x)[1]==3
        print(q,n,x,'forced next exponent 3')
    for h in (2,4,8,16,32,64,128):
        print('phase recharge target',h,':',recharged_seed(h))
