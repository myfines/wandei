"""Sliding length-46 certificate for low-complexity critical-defect excursions.

Integer-only. Enumerates all 47 length-46 mechanical factors and all scripts
that start at h=0, remain in h in {0,1}, and make one or two 0->1 upcrossings.
Every exact 2-adic lift in [N0,2^73) is continued under the odd-only Syracuse
map and must fall below N0 within 1000 odd steps.
"""
from __future__ import annotations
import hashlib
STEPS=46
LOW=2075*(1<<60)
LOCAL_LIMIT=1<<73
MAX_UPCROSSINGS=2

def exact_mechanical_letters(count:int)->list[int]:
    p=1; floors=[]
    for _ in range(count+1): floors.append(p.bit_length()-1); p*=3
    return [floors[j+1]-floors[j] for j in range(count)]

def all_factors()->dict[tuple[int,...],int]:
    mech=exact_mechanical_letters(1000); factors={}
    for shift in range(len(mech)-STEPS+1):
        w=tuple(mech[shift:shift+STEPS]); factors.setdefault(w,shift)
        if len(factors)==STEPS+1: break
    assert len(factors)==STEPS+1
    return factors

def generate(word):
    # state=(h,upcrossings,A,d), where x_46=(3^46 x_0+d)/2^A
    states=[(0,0,0,0)]
    for r in word:
        nxt=[]; app=nxt.append
        for h,u,A,d in states:
            app((h,u,A+r,3*d+(1<<A)))
            if h==0 and r==2 and u<MAX_UPCROSSINGS:
                app((1,u+1,A+1,3*d+(1<<A)))
            if h==1:
                app((0,u,A+r+1,3*d+(1<<A)))
        states=nxt
    return [s for s in states if s[1]>0]

def odd_step(x):
    y=3*x+1; a=(y&-y).bit_length()-1
    return y>>a

def first_below_frontier(seed,limit=1000):
    x=seed
    for k in range(1,limit+1):
        x=odd_step(x)
        if x<LOW: return k,x
    raise AssertionError(f'no drop below frontier within {limit} odd steps: {seed}')

def main():
    factors=all_factors(); pow3=3**STEPS; inv_cache={}
    total_scripts=candidate_scripts=row_count=0
    worst=(0,0,0,0); digest=hashlib.sha256()
    for word,shift in factors.items():
        scripts=generate(word); total_scripts+=len(scripts)
        for h,u,A,d in scripts:
            if A not in inv_cache:
                modulus=1<<(A+1); inv_cache[A]=(modulus,pow(pow3,-1,modulus))
            modulus,inv=inv_cache[A]
            residue=(inv*((1<<A)-d))%modulus
            assert residue&1
            q=max(0,(LOW-residue+modulus-1)//modulus)
            first=True
            while True:
                seed=residue+q*modulus
                if seed>=LOCAL_LIMIT: break
                if first: candidate_scripts+=1; first=False
                k,x=first_below_frontier(seed)
                if k>worst[0]: worst=(k,seed,x,shift)
                digest.update(f'{shift},{h},{u},{A},{residue},{modulus},{q},{seed},{k},{x}\n'.encode())
                row_count+=1; q+=1
    assert total_scripts==2_896_692
    assert candidate_scripts==1_277_488
    assert row_count==1_289_063
    assert worst==(237,4810798976564215475307,1869158857707769661911,16)
    hexdigest=digest.hexdigest()
    assert hexdigest=='346bfef946c44eb608738a278aa31a0d16a1ad3497d8852a92fcaaa144304156'
    print('mechanical factors =',len(factors))
    print('low-complexity scripts =',total_scripts)
    print('candidate residue classes =',candidate_scripts)
    print('candidate seed lifts =',row_count)
    print('latest drop below frontier = odd step',worst[0])
    print('worst local seed =',worst[1])
    print('candidate-row sha256 =',hexdigest)
if __name__=='__main__': main()
