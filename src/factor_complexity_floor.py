#!/usr/bin/env python3
"""Exact finite factor-complexity lower bound, odd-only Collatz.

If a nonperiodic positive orbit has distinct states n_0..n_K, the
length-L exponent words at those starts must be different whenever
(seed+1)*3**K <= 2**(L+K+1). All integer arithmetic.
"""
def syracuse(x):
    assert x>0 and x%2==1
    y=3*x+1
    a=(y & -y).bit_length()-1
    return y>>a,a

def guaranteed_distinct_starts(seed,L):
    assert seed>0 and seed%2==1 and L>=1
    lhs=seed+1
    rhs=1<<(L+1)
    if lhs>rhs: return 0
    count=1
    while lhs*3<=rhs*2:
        lhs*=3
        rhs*=2
        count+=1
    return count

def brute_check(seed,L):
    count=guaranteed_distinct_starts(seed,L)
    x=seed
    states=[x]
    symbols=[]
    for _ in range(count+L-1):
        x,a=syracuse(x)
        states.append(x)
        symbols.append(a)
    distinct=len(set(states[:count]))==count
    words=[tuple(symbols[i:i+L]) for i in range(count)]
    words_distinct=len(set(words))==len(words)
    if distinct:
        assert words_distinct
    return count,distinct,words_distinct

if __name__=='__main__':
    for seed in (27,97,871,6171,2**80-1):
        for L in (8,16,32,64,96,128):
            print(seed,L,brute_check(seed,L))
