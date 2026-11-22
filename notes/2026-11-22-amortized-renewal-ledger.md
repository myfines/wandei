# 2026-11-22 — Sharp mixed-gate height ledger, exact Haar moments and finite-pattern no-go

**Status: exact elementary deductions and independent tests, NOT a proof of Collatz. No novelty claimed.** This extends the prior renewal-gate note in this branch; main and its existing errata remain unchanged.

## A. A sharp, universal height ledger

Let S(n)=(3n+1)/2^v2(3n+1) for positive odd n. Let R(n) denote the endpoint of one renewal gate (for n=1 mod4, a single odd step, called A; for n=3 mod4 use the previous B1/B3/G_even/G_odd classification). For every positive odd n>1,

    (R(n)+1)/(n+1) <= w(type).

All five bounds are globally sharp, with explicit equality seeds:

| Gate | w | sharp actual transition |
| --- | --- | --- |
| B1 | 3/2 | 7 -> 11 |
| B3 | 8/7 | 27 -> 31 |
| G_odd | 23/27 | 107 -> 91 |
| G_even | 3/5 | 19 -> 11 |
| A | 4/5 | 9 -> 7 |

**Proof.** B1 satisfies (R+1)/(n+1)=3/2. For B3, the ratio is 9/8+1/[2(n+1)] <=8/7 as n>=27. For n=1 mod4, n>1, n=5 is special with S(5)=1; otherwise n>=9, a=v2(3n+1)>=2 and the ratio <=(3n+5)/[4(n+1)]<=4/5.

For G_odd, put e=v2(S(n)-1)=2r+1 with r>=2, n=(1+4^(r+1)u)/3, u positive odd, and R=1+2*3^r*u. The ratio is (6+6*3^r*u)/(4+4^(r+1)*u), strictly decreasing in u. For r=2, 3-divisibility forces u=2 mod3; the first positive odd possibility u=5 gives maximum 23/27. For r>=3 the ratio is <=6/4^(r+1)+(3/2)*(3/4)^r<=21/32<23/27.

For G_even, e=2r, r>=1, write n=(1+2^(2r+1)u)/3. The endpoint R=(1+3^r*u)/2^v for v>=1, hence ratio <=(9+3^(r+1)*u)/(8+2^(2r+2)*u). If r>=2, this is <=9/64+(3/4)^3=9/16<3/5. If r=1, integrality requires u=1 mod3: u=1 gives n=3->1, ratio1/2; otherwise odd u>=7 and the preceding decreasing bound is at most 3/5 at u=7, n=19->11. QED.

**Across-gate consequence.** For any actual successive gate word t_0,...,t_(q-1),

    (n_q+1)/(n_0+1) <= product_j w(t_j).

A product <1 is a sufficient, exact certificate that the endpoint is below the *original* n_0. A hypothetical least odd Collatz counterexample N must satisfy product>=1 at **every** prefix of its gate itinerary. This condition alone does not require any prefix product<1.

## B. Exact one-gate 2-adic Haar moments, with NO mixing assumption

Sample the starting 2-adic integer uniformly from X=3+4Z_2. Let e=v2(S(n)-1). Then P(e=j)=2^-j for j>=1. When e=2r, the conditional v=v2(1+3^r*u), where u=(3n-1)/2^(2r+1) is odd, has geometric P(v=j|e)=2^-j for j>=1.

Let p be the number of odd-only steps in the gate and A the sum of the corresponding 2-exponents. If e=2r+1 (r>=0), then (p,A)=(r+1,2r+1). If e=2r (r>=1), then (p,A)=(r+1,2r+1+v). The exact *linear* affine multiplier is M=3^p/2^A. Geometric sums give

    E[p]=5/3, E[A]=3, E[log2(M)]=(5/3)log2(3)-3<0.

For integer s>=0 and z=(3/4)^s/4, the exact moment is

    E[M^s]=(3/2)^s/(1-z) * (1/2+z/(2^(s+1)-1)).

Especially **E[M]=27/26>1**, **E[M^2]=2097/1540**, despite the negative mean *logarithmic* multiplier. This is a one-time arithmetic-residue average, NOT a time average for any single deterministic integer orbit and NOT a claim that the gate map preserves Haar measure.

The coarse sharp type-wise majorants lose too much information even in this one-shot model:
    E[log w]=1/2 log(3/2)+1/8 log(8/7)+1/3 log(3/5)+1/24 log(23/27)>0.
Thus further work should preserve valuation subtypes and inter-gate dependence instead of assuming all good gates are represented by one contraction constant.

## C. Every finite three-symbol gate word is realizable

The e=5 good gate, denoted G5, satisfies

    G5(n)=(27n+23)/32, domain n=107 mod128.

Together with B1 (n=7 mod8) and B3 (n=27 mod32), these are full branches mapping their 2-adic domains bijectively onto X. Their inverse maps on X are (2x-1)/3, (8x-5)/9, (32x-23)/27 and respectively contract 2-adic distances by 1/2, 1/8, 1/32.

Every finite word over {B1,B3,G5} is realized by infinitely many **positive odd integers**, in exactly one congruence class modulo 2^(A_word+2). Thus no such finite word is ruled out by 2-adic congruence constraints alone.

In particular, for B1 followed by G5, the return composition is

    G5(B1(n))=(81n+73)/64 > n

whenever the pair is legal. For every finite q there is a positive seed following (B1,G5)^q and increasing after EVERY pair, despite one G5 local descent per two gates. The starts depend on q; an infinite repeating pattern would have the 2-adic fixed point n=-73/17 (not a positive integer).

Examples (q, least positive cylinder representative, 2q-gate endpoint, modulus):
1,71,91,2^8
2,2887,4627,2^14
3,740167,1500535,2^20
4,55266119,141800959,2^26

Local descent is not global: the true trajectory 27 ->31 ->47 ->71 ->107 ->91 has a good final gate 107->91, but 91>27.

## D. Reproduction / limitations

Programs in src/renewal_ledger.py and src/renewal_moments.py; eight independent tests in tests/test_renewal_ledger.py and tests/test_renewal_moments.py (local run PASSED). Standard-library integers and Fractions; no Lean kernel certification. Related earlier branch research includes phase recharges and the 2-adic Cantor survivor. A seed-uniform *single-orbit* cross-gate frequency/correlation inequality remains open.

Related probabilistic block discussion (NOT used as an assumption here): https://ai.vixra.org/pdf/2512.0068v1.pdf .
