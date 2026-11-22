# 2026-11-22 — Sharp target-gap cost: adjacent hits contract, all positive gaps permit growth

**Status:** exact finite-state theorem and real positive integer witnesses. **NOT** a Collatz proof; no general novelty claim.

Use the exact target-hit indicator for each odd-only shortcut block after n, defined in notes/2026-11-22-full-mod27-hit-language-and-growth-credit.md. Let H mean a target hit (a>=tau(n mod9)), N a nonhit. For g>=0, consider a window with pattern H N^g H, of total odd-only length L=g+2.

## Theorem: exact minimum 2-exponent sum

Among all positive odd trajectories realizing this window,

    A_min(g) = 7 if g=0;  g+3 if g>=1.

**Case g=0:** for initial residue r=0,...,8, any hit requires a>=tau(r), and the next residue r'=(3r+1)2^-a mod9 depends only on a mod6. The cheapest subsequent hit costs tau(r'). Checking only a=tau(r),...,tau(r)+5 is therefore exhaustive. The nine exact minima for r=0,...,8 are

    (17,19,15,23,7,21,11,13,9),

with overall minimum 7, witnessed by residue r=4 and a,b=(6,1), e.g. n=661 ->31 ->47, as shown in the previous bridge note.

**Case g>=1:** if all L exponents equaled 1, the first hit could occur ONLY at residue r=4 (tau(4)=1). Under a=1, this residue is sent to 2, then 8, and residue 8 is fixed by further a=1 steps. Since tau(2)=9 and tau(8)=3, a second hit cannot occur. Thus at least one exponent must be >=2, whence A>=L+1=g+3.

Sharpness: take the exponent word

    w=(1 repeated g times, 2, 1)

and initial n=4 mod9. The first a=1 gives a hit (4->2); the intermediate g nonhit steps go through residue 2 and possibly 8, with the final a=2 returning to residue 4; the last a=1 gives a hit. The total A is g+3. Exact 2-adic cylinder arithmetic plus CRT produces infinitely many positive odd n realizing the word and n=4 mod9. QED.

For g>=1, the minimal linear coefficient across this length-L window is attainable and exceeds 1:

    M_g=3^(g+2)/2^(g+3)=(9/8)*(3/2)^g>1.

For g=0 the cost-7 witness has coefficient 9/128<1. The "coefficient" is not equal to the actual endpoint/input ratio because there is also a strictly positive additive correction.

## Arbitrarily many regularly spaced hits with NO first descent

For any integers g>=1 and q>=1, repeat the odd exponent period

    p_g=(1 repeated g times,2)

exactly q times, starting at n=4 mod9. Each period begins with a hit; the remaining g blocks in that period are nonhits, and the mod9 residue returns to 4. Thus the q hits occur at positions 0,g+1,2(g+1),..., (q-1)(g+1).

The exact return map for a single period is

    F_g(x)=[3^(g+1)*x + 3^(g+1)-2^(g+1)]/2^(g+2).

For g>=1 we have 3^(g+1)>2^(g+2), so F_g(x)>x for every positive x. Inside a period the initial g steps all have a=1 and strictly increase; the terminal a=2 step returns to a value STILL ABOVE the period's start. Consequently every intermediate odd checkpoint of these q periods is strictly larger than the original positive seed.

Every finite q has infinitely many genuine positive integer witnesses by CRT. Their initial seeds DEPEND on q; no fixed positive integer is asserted to realize the infinite periodic script.

Numerical examples with exactly 3 target hits:
- g=1: 9211 ->13117 (hits at odd-block indices 0,2,4);
- g=2: 33511 ->161041 (indices 0,3,6);
- g=3: 553711 ->8980267 (indices 0,4,8);
- g=4: 2240671 ->122647081 (indices 0,5,10).

The formal infinite fixed point of this expanding word is

    c_g=[3^(g+1)-2^(g+1)]/[2^(g+2)-3^(g+1)] < 0,

which explains why finite positive shadows do NOT furnish a positive periodic escaping orbit.

## Main consequence

A guarantee of infinitely many shortcut hits at 20 mod27, even with bounded **finite** gaps and positive hit density in a finite horizon, is not enough to derive a seed-independent finite-time descent theorem by counting or local return costs alone. Arbitrary finite no-descent growth shadows exist.

To attack a hypothetical *fixed* exceptional positive integer one needs a global compatibility theorem across the growing sequence of 2-adic cylinders and real height; the known Monks theorem supplies recurrence but not its needed long-time correlation.

## Verification

Exact dynamic program on all nine residue states proves g=0 and checks the closed form for 1<=g<=150. Tested genuine CRT positive seeds for many (g,q), all intermediate odd states, hit positions, and affine period formulas. Implementation/test files: src/mod27_gap_language.py and tests/test_mod27_gap_language.py. Tests verify finite computations and do not substitute for the algebraic proof.
