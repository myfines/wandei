#!/usr/bin/env python3
"""Exact finite-state audit for odd Collatz mod-27 hit/pair inequalities.

Either a checkable Bellman-Ford potential, or a strictly negative graph
cycle with a genuine positive-integer finite exponent-word witness.
This cannot establish convergence of any unbounded trajectory.
"""
import argparse
import json

TAU=(11,13,9,17,1,15,5,7,3)
STATES=tuple((r,0) for r in range(9))+tuple((r,1) for r in (1,2,4,5,7,8))
INDEX={s:i for i,s in enumerate(STATES)}

def edges():
    result=[]
    for (r,prev),u in INDEX.items():
        for a in range(1,TAU[r]+6):
            h=int(a>=TAU[r])
            rn=((3*r+1)*pow(2,-a,9))%9
            result.append((u,INDEX[(rn,h)],a,h,prev*h))
    assert len(result)==204
    return result

EDGES=edges()

def step(n):
    assert n>0 and n%2
    t=3*n+1
    a=(t&-t).bit_length()-1
    return t>>a,a

def direct_shortcut_hit(n):
    y,a=step(n)
    x=n;flag=False
    for _ in range(a):
        x=(3*x+1)//2 if x%2 else x//2
        flag|=x%27==20
    assert x==y
    return flag

def positive_seed(word,r9):
    """Positive CRT seed, modulo 9*2^(A+1), for an exact finite word."""
    A=C=0
    for a in word:
        assert a>=1
        C=3*C+(1<<A);A+=a
    m=1<<(A+1)
    r2=((1<<A)-C)*pow(3**len(word),-1,m)%m
    n=r2+m*(((r9-r2)*pow(m,-1,9))%9)
    assert n>0 and n%2 and n%9==r9
    x=n
    for a in word:
        x,b=step(x)
        assert a==b
    return n,9*m,x

def check_potential(potential,lam,mu):
    return len(potential)==len(STATES) and all(
        a-1-lam*h-mu*p>=potential[v]-potential[u]
        for u,v,a,h,p in EDGES)

def audit(lam,mu,repeats=3):
    """Bounded correction exists iff there is no negative graph cycle."""
    assert lam>=0 and mu>=0 and repeats>=2
    n=len(STATES);dist=[0]*n;parents=[None]*n
    final=None
    for _ in range(n):
        final=None
        for u,v,a,h,p in EDGES:
            if dist[v]>dist[u]+a-1-lam*h-mu*p:
                dist[v]=dist[u]+a-1-lam*h-mu*p
                parents[v]=(u,v,a,h,p)
                final=v
        if final is None:
            assert check_potential(dist,lam,mu)
            return {'status':'certified_graph_potential','lambda':lam,'mu':mu,
                    'potential':dist,'edges_checked':len(EDGES)}
    x=final
    for _ in range(n):
        x=parents[x][0]
    start=x;back=[]
    while True:
        e=parents[x]
        assert e is not None
        back.append(e);x=e[0]
        if x==start:break
        assert len(back)<=n
    cyc=list(reversed(back))
    assert cyc[0][0]==cyc[-1][1]
    assert all(cyc[j][1]==cyc[j+1][0] for j in range(len(cyc)-1))
    weight=sum(a-1-lam*h-mu*p for u,v,a,h,p in cyc)
    assert weight<0
    word=[e[2] for e in cyc]*repeats
    seed,mod,endpoint=positive_seed(word,STATES[cyc[0][0]][0])
    x=seed;hits=[]
    for a in word:
        hits.append(int(direct_shortcut_hit(x)))
        x,b=step(x);assert b==a
    assert x==endpoint
    return {'status':'refuted_by_formal_negative_cycle','lambda':lam,'mu':mu,
            'cycle_weight':weight,'cycle_start':STATES[cyc[0][0]],
            'cycle_exponents':[e[2] for e in cyc],
            'positive_finite_witness':{'seed':str(seed),'end':str(endpoint),
                'modulus':str(mod),'exponents':word,'hit_bits':hits},
            'edges_checked':len(EDGES)}

def exact_frontier(lam,mu):
    """For NONNEGATIVE real lambda/mu: potential iff both constraints."""
    return lam>=0 and mu>=0 and lam<=1 and lam+mu<=5

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--lambda-price',type=int,default=1)
    p.add_argument('--mu-price',type=int,default=4)
    p.add_argument('--frontier',action='store_true')
    args=p.parse_args()
    if args.frontier:
        report=[{'lambda':lam,'mu':mu,'graph_result':audit(lam,mu)['status'],
                 'theoretical_feasibility':exact_frontier(lam,mu)}
                for lam in range(4) for mu in range(9)]
        print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print(json.dumps(audit(args.lambda_price,args.mu_price),
                         ensure_ascii=False,indent=2))

if __name__=='__main__':main()
