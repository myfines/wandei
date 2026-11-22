# 2026-11-22 — Real height × 3-adic phase × inverse-tree spectral lift

**Status:** elementary exact mathematics, independently tested finite computations. **Not a Collatz proof.** No originality claim relative to classical 3-adic inverse rays or existing Collatz transfer-operator literature. Human mathematical review and Lean formalization remain open.

## 0. Riemann hypothesis status, corrected
On 2026-11-20 Levent Alpöge announced a Claude-assisted formal RH proof; on 2026-11-21 the Lean and Mathlib communities issued an explicit certification of the theorem statement and its Lean proof (https://leanprover-community.github.io/blog/posts/riemann-hypothesis/). The following arguments **do not depend on RH**.

## 1. Inverse odd-Collatz tree and a genuine joint state
Define S(n)=(3n+1)/2^v2(3n+1) for positive odd n. For positive odd m with 3∤m define

    a0(m)=2 if m=1(mod3), otherwise 1
    R_m(t)=(2^(a0(m)+2t)*m−1)/3, t=0,1,2,...

These are **all** positive odd one-step predecessors of m, with S(R_m(t))=m. Targets divisible by 3 have no odd predecessors. When m=1, suppress the self-loop t=0, R_1(0)=1. Because S is deterministic, the resulting rooted inverse graph is a tree: each positive n eventually reaching 1 has one unique earliest hitting depth.

Lift each genuine inverse node to the higher-dimensional state

    X=(n, depth d, last turn t, r_q=n mod3^q,
       real height h=log(3n+1), complex character exp(2πi n/3^q),
       Mellin weight n^(−s)).

The finite inverse adjacency transfer P_B acts on test functions by

    (P_B f)(m)= sum_{t>=t0(m), R_m(t)<=B} f(R_m(t)),

where t0(1)=1, and t0(m)=0 for other allowed m; targets divisible by 3 contribute 0. For X>=1, d>=0 let

    B(X,d)=max(X, floor((3/2)^d*(X+1))-1).

The bound S(n)+1 <= (3/2)(n+1) ensures EVERY intermediate odd state from a seed <=X whose first hitting depth is <=d is <=B(X,d), including paths overshooting the initial height X. Thus with f(n)=1_{n<=X} n^(−s) exp(2πiℓ n/3^q),

    Z_{d,X,q}(s,ℓ)
      =sum_{j=0}^d (P_{B(X,d)}^j f)(1)
      =sum_{n<=X, first_hit(n)<=d} n^(−s) exp(2πiℓn/3^q).

This is an EXACT distinct-positive-integer finite spectral transfer, not a stochastic or formal parity-word average. It is a Dirichlet polynomial for fixed X,d, hence does not automatically inherit any RH-like zero theorem.

## 2. Sharp 3-adic/Archimedean phase-height uncertainty

The LTE identity yields v3(R_m(t)−R_m(u))=v3(t−u). Thus every 3^q consecutive turns visit ALL residue classes mod 3^q once, and fewer turns cannot. The exact minimum height needed to cover the full residue space on the real positive odd ONE-STEP inverse ray is

    X_{m,q}=R_m(t0(m)+3^q−1).

For the root m=1, t0=1:

    X_{1,q}=(4^(3^q+1)−1)/3,
    bit_length(X_{1,q})=2*3^q+1.

For q=1,2,3,4,5, the minimum heights require 7,19,55,163,487 binary bits. This is a strict DOUBLE-EXPONENTIAL height price for full 3-adic phase precision q. It is a theorem for a **single parent ray**, not the full unlimited-depth inverse tree.

## 3. Exact Fourier-energy / Mellin-weight no-go

Let M=3^q, and let c_r be the nonnegative integer number of finite-height inverse-tree nodes in residue class r (mod M), N=sum c_r. Then by Parseval

    sum_{ℓ=1}^{M−1} |sum_r c_r exp(2πiℓr/M)|²
       =M*sum_r c_r²−N²
       >=N(M−N)  when N<=M.

For the FIRST N<=M distinct turns of ONE inverse ray, equality holds exactly: nontrivial energy=N(M−N). At N=M all unweighted nonzero Fourier modes vanish.

However if the M distinct turns are given their real Mellin weights w_t=R_m(t)^(−s), s>0, their nonzero Fourier energy is

    E_{m,q,s} = M sum_t w_t² − (sum_t w_t)² > 0,

with strictness because the real heights increase and weights are unequal. **Perfect 3-adic residue cancellation NEVER implies complete real-height-weighted Mellin cancellation** on these rays.

This is the exact spectral reason that p-adic equidistribution alone cannot prove an ordinary positive-integer convergence theorem. It does not rule out more sophisticated joint potential/spectral estimates.

## 4. Fixed-depth height sparsity

With B=B(X,d), put L=1+floor(log_4((3B+1)/2)), computable by integer comparisons. Every inverse parent under height B has <=L children under B. Consequently

    # {positive odd n<=X: first_hit(n)<=d} <= sum_{j=0}^d L^j.

For fixed d, this is O_d((log X)^d), thus each FIXED finite-depth 1-basin has natural density zero among positive odd integers. If 3^q exceeds this upper bound, some residue classes mod 3^q are unrepresented by depth d and height X. To capture most seeds, depth MUST grow with height. This is not an upper or lower bound on arbitrary orbit escape.

## 5. Reproducible finite certificate

Source: src/inverse_height_spectral_lift.py
Tests: tests/test_inverse_height_spectral_lift.py
Data: notes/2026-11-22-height-phase-spectral-data.csv

Exact benchmark X=5000, maximum odd depth d=8:
- 2500 positive odd candidate seeds, **287** have first hit of 1 by depth 8.
- Every residue mod 27 is already occupied, but multiplicities differ.
- Unweighted nonzero Fourier energy (all 26 modes) is **4706**, exact by integer Parseval.
- Reverse enumeration uses the safe B(X,d) to allow temporary overshoot and was independently checked against forward iteration.
- For one complete non-self inverse ray of root 1 modulo 27, unweighted energy=0, but **s=2 weighted energy ≈0.04154030496574466 >0**, with exact rational positive certificate.
- **Nine** independent standard-library tests passed locally.

## 6. Actual missing step and related work

No positive-orbit convergence conclusion follows from these theorems. The missing result is a **uniform depth-growing, height-sensitive, coefficient-wise** lower bound for the entire 1-basin, one that would disallow even a single omitted positive odd integer. RH proof methods may inspire formalization but RH itself is not shown to imply such a bound.

Related: Bernstein–Lagarias (1996) 2-adic conjugacy; Stérin–Woods (2020) base conversion; contemporary inverse-tree/spectral preprints including https://hexagonmath.org/2610.00681v1. These results should not be claimed original without deeper literature review.


## 7. Exact three-space phase-return cocycle

Fix a target m (positive odd, 3∤m), q>=1, M=3^q, and any non-self inverse turn t>=t0(m). Let n=R_m(t), n'=R_m(t+M). Then all three identities hold **exactly**:

    n' == n (mod 3^q),  v3(n'-n)=q,
    v2(3n'+1)-v2(3n+1)=2*3^q,
    (3n'+1)/(3n+1)=4^(3^q).

The first identity follows from the LTE/isometry identity v3(R_m(t)-R_m(u))=v3(t-u); importantly the next 3-adic digit does **not** agree. The second and third follow from 3R_m(t)+1=2^(a0(m)+2t)m. A single q-digit 3-adic phase 'full rotation' has an exact 2-adic exponent jump and an exponential Archimedean height cost. This is the main real/2-adic/3-adic arithmetic cocycle of this checkpoint.

This does not impose a global decreasing potential on an arbitrary forward orbit, and no direct implication from the formally verified RH theorem is claimed.
