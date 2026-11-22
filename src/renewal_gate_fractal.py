#!/usr/bin/env python3
"""Exact growing/descending renewal gates in odd Collatz (Syracuse).

No proof of the Collatz conjecture. Python standard library only.
"""

def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def S(n):
    assert n > 0 and n & 1
    y=3*n+1
    return y >> v2(y)


def gate(n):
    """n≡3 mod4 -> (kind, endpoint, odd_steps, e).

    B1 and B3 are strictly expanding returns to n≡3 mod4.
    All other cases end below the current n in finite odd steps.
    """
    assert n >= 3 and n % 4 == 3
    y=S(n)
    assert y > 1 and v2(3*n+1)==1
    e=v2(y-1)
    if e==1:
        assert y>n and y%4==3
        return 'B1',y,1,e
    if e==3:
        z=S(y)
        assert v2(3*y+1)==2 and z%4==3 and z>n
        assert z==(9*n+5)//8
        return 'B3',z,2,e
    if e%2:
        r=(e-1)//2
        for _ in range(r):
            assert v2(3*y+1)==2
            y=S(y)
        assert y<n and y%4==3
        return 'G_odd',y,r+1,e
    r=e//2
    for _ in range(r-1):
        assert v2(3*y+1)==2
        y=S(y)
    assert v2(y-1)==2
    y=S(y)
    assert y<n
    return 'G_even',y,r+1,e


def survive_word(n, depth):
    assert n>0 and n%4==3 and depth>=0
    word=[]
    for _ in range(depth):
        kind,n,_,_=gate(n)
        if kind not in ('B1','B3'): break
        word.append(kind)
    return tuple(word)


def next_cylinders(state):
    """(residue,bits,A,p,image_at_residue,word); refine to B1 and B3."""
    residue,bits,A,p,y0,word=state
    assert bits==A+2 and y0%4==3
    # For n=r+2^(A+2)*t, endpoint after prefix is y0+4*3^p*t.
    t1=((7-y0)//4)%2
    r1=residue+(1<<bits)*t1
    y1=y0+4*(3**p)*t1
    assert y1%8==7
    out1=(3*y1+1)//2
    assert out1%4==3
    inv3p_mod8=3 if p%2 else 1
    t3=(((27-y0)//4)*inv3p_mod8)%8
    r3=residue+(1<<bits)*t3
    y3=y0+4*(3**p)*t3
    assert y3%32==27
    out3=(9*y3+5)//8
    assert out3%4==3
    return ((r1,bits+1,A+1,p+1,out1,word+'1'),
            (r3,bits+3,A+3,p+2,out3,word+'3'))


def cylinders(depth):
    assert depth>=0
    nodes=[(3,2,0,0,3,'')]
    for _ in range(depth):
        nodes=[child for state in nodes for child in next_cylinders(state)]
    return nodes


def min_seed_per_depth(max_depth):
    nodes=[(3,2,0,0,3,'')]
    rows=[]
    for depth in range(max_depth+1):
        best=min(nodes,key=lambda state:state[0])
        rows.append((depth,len(nodes),best[0],best[-1],5**depth,8**depth))
        if depth<max_depth:
            nodes=[child for state in nodes for child in next_cylinders(state)]
    return rows


def dimension(iterations=100):
    lo,hi=0.,1.
    for _ in range(iterations):
        mid=(lo+hi)/2
        if 2**(-mid)+8**(-mid)>1:lo=mid
        else:hi=mid
    return (lo+hi)/2


if __name__=='__main__':
    print('depth,cylinders,min_positive_seed,word,numerator,denominator')
    for record in min_seed_per_depth(17):
        print(*record,sep=',')
    print('2-adic Hausdorff dimension:',dimension())
