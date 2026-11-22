# 2026-11-23 — A no-go for additive adelic height Lyapunov functions

**Not a Collatz proof.** Rigorous elementary barrier to a specific high-dimensional strategy, not a claim of new mathematics.

Odd-only Syracuse: S(n)=(3n+1)/2^v2(3n+1), n positive odd.

## Theorem A: sharp growing shadows with frozen two-prime phase

For any L,r,q >=1 let N=2^(L+r)*3^q−1. For every 0<=j<=L,

    S^j(N)+1=2^(L+r−j)*3^(q+j).

All L odd-only exponents are 1; the real states strictly increase, while every state remains -1 modulo 2^r and modulo 3^q. The Archimedean log-height increases exactly L log(3/2).

Moreover this N is least possible for these properties: the final phase requires 2^(L+r)|(N+1); the initial 3-adic phase requires 3^q|(N+1). The positive seed varies with L; this is NOT an infinite positive escaping trajectory.

## Theorem B: no globally nonincreasing additive adelic potential

Fix any FINITE set of primes P, alpha>0, arbitrary real coefficients c_p and any bounded b(n). Define

    V(n)=alpha*log(n+1)+sum_(p in P)c_p*v_p(n+1)+b(n).

Then V(S(n))<=V(n) cannot hold for ALL positive odd n>1.

Proof. For positive odd y=1 mod3, set n=(4y-1)/3. This is a true exponent-2 step n->y, with n+1=2(2y+1)/3 and 3/4<(y+1)/(n+1)<=1. Thus its log-height increment stays bounded.

1. For each p>=5 in P, choose y by CRT to satisfy y=1(mod4), y=1(mod9), y=0(mod all other primes in P >=5). The independent options y=-1(mod p^h) or y=-1/2(mod p^h) force respectively an arbitrarily large UP or DOWN jump in v_p(n+1), while all other measured valuation increments vanish. With bounded log and b increments, monotonicity forces c_p=0.
2. Choose y=-1(mod2^h), y=1(mod9), forcing v2(n+1)=1, v2(y+1)>=h and equal zero v3 at both ends. Therefore c_2<=0, where c_2=0 if 2 not in P.
3. Choose y=1(mod4), 2y+1=0(mod3^(h+1)), forcing both v2 values 1, v3(n+1)>=h, v3(y+1)=0. Therefore c_3>=0, where c_3=0 if 3 not in P.
4. By Theorem A, the potential change across the L growing steps is

    L*[alpha log(3/2)-c_2+c_3]+b(S^L(N))-b(N).

Its linear coefficient is >= alpha log(3/2)>0, whereas the remaining correction is bounded. Taking L large contradicts global nonincrease. QED.

In particular, no bounded modular/Fourier phase correction works with this fixed linear valuation ansatz. Any continuous real-valued correction on a compact finite p-adic product is also bounded. This does not exclude nonlinear, unbounded, path-history-sensitive or seed-dependent methods.

## Exact integer witnesses

- L=10,r=3,q=2: 73727 -> 4251527 after ten increasing odd steps, all checkpoints -1(mod72).
- 2-adic recharge h=20: 6990505 --a=2--> 5242879, v2(n+1) changes 1 ->20.
- 3-adic discharge h=20: 6973568801 --a=2--> 5230176601, v3(n+1) changes >=20 ->0.

Reproduction: src/archimedean_adelic_nogo.py; tests/test_archimedean_adelic_nogo.py. Seven local unittest methods passed. No Lean proof verification.

Important unproved step: a uniform statement about a SINGLE fixed positive integer and ALL depths. This note neither proves nor disproves Collatz, which is still open as of 2026-11-23: https://mathdb.com/p/315917/collatz-conjecture .
