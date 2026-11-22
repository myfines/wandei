#!/usr/bin/env python3
"""Exact integer witnesses obstructing linear adelic Collatz Lyapunov proofs.

No general Collatz proof/disproof. Standard-library only.
"""
from math import gcd, log

def v_p(n,p):
    assert n>0 and p>=2
    k=0
    while n%p==0:
        n//=p;k+=1
    return k

def syracuse(n):
    assert n>0 and n%2
    a=3*n+1
    k=v_p(a,2)
    return a>>k,k

def crt(residues):
    """Pairwise coprime Chinese remaindering; returns positive integer."""
    x=0;M=1
    for m,a in residues:
        assert m>1 and gcd(m,M)==1
        x+=M*(((a-x)*pow(M,-1,m))%m)
        M*=m
    return x%M or M

def frozen_shadow(L,r=2,q=1):
    assert L>=1 and r>=1 and q>=1
    n=(1<<(L+r))*3**q-1
    x=n;states=[]
    for j in range(L+1):
        assert x+1==(1<<(L+r-j))*3**(q+j)
        assert (x+1)%((1<<r)*3**q)==0
        states.append(x)
        if j<L:
            y,a=syracuse(x)
            assert a==1 and y>x
            x=y
    return n,states

def two_recharge(h):
    assert h>=2
    y=crt(((1<<h,-1),(9,1)))
    n=(4*y-1)//3
    assert syracuse(n)==(y,2)
    assert v_p(n+1,2)==1 and v_p(y+1,2)>=h
    assert v_p(n+1,3)==v_p(y+1,3)==0
    return n,y

def three_discharge(h):
    assert h>=1
    m=3**(h+1)
    y=crt(((m,-pow(2,-1,m)),(4,1)))
    n=(4*y-1)//3
    assert syracuse(n)==(y,2)
    assert v_p(n+1,2)==v_p(y+1,2)==1
    assert v_p(n+1,3)>=h and v_p(y+1,3)==0
    return n,y

def odd_prime_excursion(p,h,kind,other_odd_primes=()):
    assert p>=5 and h>=1 and kind in ('up','down')
    mod=p**h
    option=-1 if kind=='up' else -pow(2,-1,mod)
    constraints=[(4,1),(9,1),(mod,option)]
    for q in other_odd_primes:
        assert q>=5 and q!=p and gcd(q,p)==1
        constraints.append((q,0))
    y=crt(constraints)
    n=(4*y-1)//3
    assert syracuse(n)==(y,2)
    assert (v_p(n+1,2),v_p(y+1,2))==(1,1)
    assert (v_p(n+1,3),v_p(y+1,3))==(0,0)
    for q in other_odd_primes:
        assert (v_p(n+1,q),v_p(y+1,q))==(0,0)
    if kind=='up':
        assert v_p(n+1,p)==0 and v_p(y+1,p)>=h
    else:
        assert v_p(n+1,p)>=h and v_p(y+1,p)==0
    return n,y

def potential_change(start,end,coeff,alpha=1.):
    """Variation in alpha log(n+1)+sum c_p v_p(n+1)."""
    return alpha*(log(end+1)-log(start+1))+sum(
        c*(v_p(end+1,p)-v_p(start+1,p)) for p,c in coeff.items())

def witness_against_linear_height(coeff,alpha=1.,bounded_error=1.):
    """Find a finite positive integer orbit that defeats ANY |b|<=B.

    By theorem in notes, the increase before b exceeds 2*B.
    Double arithmetic is a check; the proof itself uses exact integer CRT.
    """
    assert alpha>0 and bounded_error>=0
    assert all(p>=2 for p in coeff)
    eps=2*bounded_error+1
    c2=coeff.get(2,0);c3=coeff.get(3,0)
    high=sorted((p,c) for p,c in coeff.items() if p>=5 and c!=0)
    if high:
        p,c=high[0]
        h=max(2,int((eps+alpha*log(4/3))/abs(c))+3)
        other=tuple(q for q in coeff if q>=5 and q!=p)
        n,y=odd_prime_excursion(p,h,'up' if c>0 else 'down',other)
        kind='odd-prime-'+str(p);steps=1
    elif c2>0:
        h=max(2,int((eps+alpha*log(4/3))/c2)+3)
        n,y=two_recharge(h);kind='2-adic recharge';steps=1
    elif c3<0:
        h=max(2,int((eps+alpha*log(4/3))/(-c3))+3)
        n,y=three_discharge(h);kind='3-adic discharge';steps=1
    else:
        rate=alpha*log(3/2)-c2+c3
        assert rate>0
        steps=max(1,int(eps/rate)+2)
        n,states=frozen_shadow(steps,2,1)
        y=states[-1];kind='frozen growing shadow'
    increment=potential_change(n,y,coeff,alpha)
    assert increment>2*bounded_error
    return {'kind':kind,'seed':n,'terminal':y,'odd_steps':steps,
            'height_plus_valuations_increase':increment,
            'guaranteed_increase_for_any_bounded_correction':
                increment-2*bounded_error}

if __name__=='__main__':
    for L in (1,10,100):
        n,seq=frozen_shadow(L,3,2)
        print('frozen',L,'seed',n,'end',seq[-1])
    for coeff in ({},{2:0.3},{3:-0.7},{2:-.9,3:.4},{5:.25},{7:-.12}):
        print('candidate',coeff,witness_against_linear_height(coeff))
