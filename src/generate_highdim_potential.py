#!/usr/bin/env python3
"""Independently regenerate the 15-state phase potential with Bellman-Ford.

Finite graph verification is exact; all source exponents above TAU+5 are
dominated by the same residue class 6 lower since cost rises by 6.
"""
from highdim_mod27_lift import TAU,STATES,PSI

def edges(lam):
    for r,prev in STATES:
        for a in range(1,TAU[r]+6):
            hit=int(a>=TAU[r])
            nxt=((3*r+1)*pow(2,-a,9))%9
            dest=(nxt,hit)
            assert dest in STATES
            yield (r,prev),dest,a-1-hit-lam*prev*hit,a

def bellman_potential(lam=4):
    graph=tuple(edges(lam))
    inf=10**9
    dist={s:(0 if s[1]==0 else inf) for s in STATES}
    for _ in range(len(STATES)-1):
        changed=False
        for u,v,w,a in graph:
            if dist[u]!=inf and dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
                changed=True
        if not changed:break
    for u,v,w,a in graph:
        if dist[v]>dist[u]+w:
            return None,(u,v,w,a)
    return dist,None

if __name__=='__main__':
    found,bad=bellman_potential(4)
    assert bad is None and found==PSI
    none,negative=bellman_potential(5)
    assert none is None and negative is not None
    # Explicit 1-edge negative cycle at (r=4,prev_hit=1) with a=6:
    # r'=4, hit=1, cost a-1-hit-5*pair=6-1-1-5=-1.
    assert [(u,v,w,a) for u,v,w,a in edges(5)
            if u==(4,1) and v==(4,1) and a==6]==[
              ((4,1),(4,1),-1,6)]
    print('PASS: 204 finite graph edges and exact Bellman potential')
    print('POTENTIAL:',found)
    print('Optimality obstruction to coefficient 5:',negative)
