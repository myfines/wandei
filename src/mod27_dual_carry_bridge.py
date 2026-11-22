#!/usr/bin/env python3
"""Exact 20 mod 27 shortcut-hit gates expressed in odd-only valuations.

Odd-only S(n)=(3n+1)/2^v2(3n+1), shortcut T(n)=(3n+1)/2
for odd n and n/2 for even n. All computations use exact integers
and Fraction. This research module DOES NOT prove Collatz.
"""
from fractions import Fraction
from collections import defaultdict

TARGET = 20
MODULUS = 27
# Index: n % 9; minimal shortcut step i>=1 such that
# 3*n+1 == 20*2**i (mod 27).
THRESHOLDS = (11, 13, 9, 17, 1, 15, 5, 7, 3)


def v2(n):
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


def odd_step(n):
    assert n > 0 and n % 2 == 1
    val = 3*n + 1
    a = v2(val)
    return val >> a, a


def shortcut_step(n):
    assert n > 0
    return (3*n+1)//2 if n % 2 else n//2


def phase_threshold(r):
    r %= 9
    t = THRESHOLDS[r]
    assert 20*pow(2,t,27) % 27 == (3*r+1) % 27
    assert all(20*pow(2,i,27) % 27 != (3*r+1)%27
               for i in range(1,t))
    return t


def target_hit_count(n):
    """Number of T states ==20 mod27 in the shortcut block AFTER odd n.

    The block consists of T(n),...,T^a(n)=S(n), a=v2(3*n+1).
    Does not count its source n; source is counted in its previous block.
    """
    _, a = odd_step(n)
    t = phase_threshold(n%9)
    return 0 if a<t else 1+(a-t)//18


def actual_block_hits(n):
    _, a = odd_step(n)
    hits = []
    x = n
    for i in range(1,a+1):
        x = shortcut_step(x)
        if x%27 == 20:
            hits.append((i,x))
    return hits


def suffix9(a_previous2,a_previous1):
    """Residue S^k(N) mod9 from its last TWO exponents, k>=2."""
    assert a_previous2>=1 and a_previous1>=1
    return (pow(2,-a_previous1,9) *
            (1+3*pow(2,-a_previous2,9))) % 9


def suffix27(a_previous3,a_previous2,a_previous1):
    """Residue S^k(N) mod27 from last THREE exponents, k>=3."""
    assert min(a_previous3,a_previous2,a_previous1)>=1
    return (pow(2,-a_previous1,27)
            +3*pow(2,-(a_previous2+a_previous1),27)
            +9*pow(2,-(a_previous3+a_previous2+a_previous1),27))%27


def next_residue9(r,a):
    return ((3*(r%9)+1)*pow(2,-a,9))%9


def minimum_consecutive_hit_cost(r):
    """Sharp min a+b for two successive target-bearing shortcut blocks.

    Once a >= threshold(r), r'=next_residue9(r,a), and b must be
    at least threshold(r'). The r' value is periodic in a mod6.
    """
    threshold=phase_threshold(r)
    candidates=[(a+phase_threshold(next_residue9(r,a)), a,
                 next_residue9(r,a),
                 phase_threshold(next_residue9(r,a)))
                for a in range(threshold,threshold+6)]
    return min(candidates)


def consecutive_hit_contraction(n):
    """Return the true two-step data if both blocks contain a target hit."""
    y,a=odd_step(n)
    z,b=odd_step(y)
    if target_hit_count(n)==0 or target_hit_count(y)==0:
        return None
    assert a+b>=7
    assert (1<<(a+b))*z == 9*n+3+(1<<a)
    assert 128*z <=9*n+67 and 9*n+67<128*n
    return a,b,y,z


def residue_probability(modulus,r,minimum=1):
    """P(A>=minimum and A==r mod modulus), P(A=a)=2^-a."""
    assert minimum>=1 and modulus>=1
    least=minimum+((r-minimum)%modulus)
    return Fraction(1,2**least)/(1-Fraction(1,2**modulus))


def target_frequency_haar():
    """2-adic Haar distribution of late shortcut-block hits.

    It uses independent geometric odd-only valuation digits. These are
    not time averages of any fixed ordinary positive integer orbit.
    """
    distribution=defaultdict(Fraction)
    for aa in (1,2):
        for bb in range(1,7):
            p=residue_probability(2,aa)*residue_probability(6,bb)
            distribution[phase_threshold(suffix9(aa,bb))]+=p
    return dict(sorted(distribution.items())),sum(
        (p*Fraction(1,2**(t-1)) for t,p in distribution.items()),
        Fraction(0))


def adjacent_joint_frequency_haar():
    """Exact probability that two consecutive late blocks both hit target."""
    joint=Fraction(0)
    for aa in (1,2):
        for bb in range(1,7):
            base=residue_probability(2,aa)*residue_probability(6,bb)
            t=phase_threshold(suffix9(aa,bb))
            for cc in range(1,7):
                joint += (base*residue_probability(6,cc,minimum=t)
                          *Fraction(1,2**(phase_threshold(suffix9(bb,cc))-1)))
    return joint


def positive_shadow(q):
    """Genuine positive 2q-step shadow of negative (1,2)-cycle.

    Includes exactly q-1 shortcut 20 mod27 hits; every pair of odd
    steps increases the state, but the fixed seed changes with q.
    """
    assert q>=1
    seed=(1<<(3*q+1))-5
    x=seed
    hit_count=0
    odd_steps=[]
    for j in range(2*q):
        hit_count+=target_hit_count(x)
        y,a=odd_step(x)
        assert a==(1 if j%2==0 else 2)
        odd_steps.append((x,a,y))
        if j%2==1:
            assert y>odd_steps[j-1][0]
        x=y
    assert x==2*9**q-5
    assert hit_count==q-1
    # Exact dual-carry signature of the canonical (1,2)^q cylinder.
    k=2*q
    A=3*q
    C=5*(9**q-8**q)
    mod2=1<<(A+1)
    assert (9**q*seed+C)==(1<<A)*x
    assert seed==(C*pow((1<<A)-9**q,-1,mod2))%mod2
    end_residue=9**q-5
    assert x==end_residue+9**q
    assert end_residue==(C*pow(2,-A,9**q))%(9**q)
    return {'q':q,'seed':seed,'endpoint':x,'hits':hit_count,
            'dual_carry':1,'endpoint_mod_3power':end_residue}


def run_checks():
    assert [phase_threshold(r) for r in range(9)]==list(THRESHOLDS)
    for n in range(1,500001,2):
        hits=actual_block_hits(n)
        assert target_hit_count(n)==len(hits)
        if hits:
            assert hits[0][0]==phase_threshold(n%9)
        y,a=odd_step(n)
        if target_hit_count(n) and target_hit_count(y):
            consecutive_hit_contraction(n)
    for n in range(1,100001,2):
        x=n; exps=[]
        for k in range(8):
            x,a=odd_step(x);exps.append(a)
            if k>=1:
                assert x%9 == suffix9(exps[-2],exps[-1])
            if k>=2:
                assert x%27 == suffix27(exps[-3],exps[-2],exps[-1])
    d,p=target_frequency_haar()
    assert p==Fraction(1079,4096)
    assert d=={1:Fraction(11,63),3:Fraction(22,63),
               7:Fraction(2,63),9:Fraction(16,63),
               13:Fraction(8,63),15:Fraction(4,63)}
    assert adjacent_joint_frequency_haar()==Fraction(59345,8388608)
    assert min(minimum_consecutive_hit_cost(r)[0] for r in range(9))==7
    for q in range(1,41): positive_shadow(q)
    print('PASS: 250k exact blocks; 50k x 8 suffixes; moments; 40 shadows')


if __name__=='__main__':
    print('r mod 9 -> trigger threshold:',THRESHOLDS)
    print('min adjacent-hit exponent cost:',
          {r:minimum_consecutive_hit_cost(r)[0] for r in range(9)})
    print('one-shot Haar probability:',target_frequency_haar())
    print('adjacent pair probability:',adjacent_joint_frequency_haar())
    print('q=2,4,12,40 shadow samples:')
    for q in (2,4,12,40): print(positive_shadow(q))
    run_checks()


def greedy_disjoint_target_pairs(source, steps):
    """Return (terminal, pairs, ever_dipped_below_source, block_hits).

    Greedily partitions the first `steps` odd moves into hit-hit pairs
    and remaining single moves. Every pair is two adjacent odd blocks.
    """
    assert source>0 and source%2 and steps>=0
    x=source
    hits=[]
    endpoints=[x]
    for _ in range(steps):
        hits.append(target_hit_count(x)>0)
        x,_=odd_step(x)
        endpoints.append(x)
    pair_count=0
    j=0
    while j<steps:
        if j+1<steps and hits[j] and hits[j+1]:
            pair_count+=1
            j+=2
        else:
            j+=1
    dipped=any(x<source for x in endpoints)
    return x,pair_count,dipped,hits


def no_descent_pair_budget(seed,steps):
    """Exact multiplicative upper bound for endpoint in an undescended run.

    If every intermediate odd endpoint is >=seed, then
       (endpoint+1)/(seed+1) <= ledger_bound.
    Even without that hypothesis, ledger_bound may be too small, because
    the pair factor uses seed as a lower bound on intermediate states.
    """
    terminal,pairs,dipped,hits=greedy_disjoint_target_pairs(seed,steps)
    beta=Fraction(9*(seed+1)+186,128*(seed+1))
    bound=Fraction(3,2)**(steps-2*pairs)*beta**pairs
    if not dipped:
        assert Fraction(terminal+1,seed+1)<=bound
        assert bound>=1
    return terminal,pairs,dipped,bound