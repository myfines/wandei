# 2026-11-22 — Nowhere 3-adically continuous odd Syracuse map, and its continuous adelic lift

**Status:** rigorous elementary CRT/topology statements, standard-library exact tests. NOT a Collatz proof, and no claim of mathematical novelty. This is complementary to the 3-adic winding and phase-transcendence note on this research branch.

Write S(n)=(3n+1)/2^v2(3n+1) for positive odd integers n.

## 1. S is nowhere continuous in the 3-adic topology

**Lemma.** Fix any positive odd anchor n0 and a positive integer a. For each k>=1 there exists a positive odd n_(a,k)>n0 such that
\[
n_{a,k}\equiv n_0\pmod{3^k},
\qquad v_2(3n_{a,k}+1)=a.
\]

**Proof:** The congruence 3n+1=2^a (mod 2^(a+1)) has one and only one solution r_a modulo 2^(a+1), since 3 is invertible. This solution is odd and imposes v2 exactly a. The Chinese remainder theorem gives a simultaneous solution to n=n0 mod3^k and n=r_a mod2^(a+1); add a sufficiently large multiple of 3^k*2^(a+1) to make n>n0.

Then, for each fixed a, as k increases:
\[
S(n_{a,k})\equiv (3n_0+1)2^{-a}\pmod{3^k}.
\]
Therefore n_(a,k) approaches n0 in Z_3 but its image approaches the **a-dependent** element (3n0+1)/2^a of Z_3. In particular a=1 and a=2 produce distinct limits (already distinguishable mod 3 because 3n0+1=1 mod3). Thus S fails continuity at every positive odd n0 in the induced 3-adic topology, and has no continuous extension to all Z_3 that agrees with these positive odd values.

For anchor n0=1 there are easy explicit witnesses:
- n_k=1+2*3^k approaches 1, always has v2(3n_k+1)=1, and S(n_k)=2+3^(k+1) approaches **2** in Z_3.
- n'_k=1+8*3^k approaches 1, always has v2(3n'_k+1)=2, and S(n'_k)=1+6*3^k approaches **1** in Z_3.

This is a precise no-go for modeling the original Syracuse transformation as a single continuous map of *only* the 3-adic state.

## 2. Continuous three-coordinate skew-product (partial dynamical map)

Take ordinary r>0, 2-adic x in Z_2^odd except x=-1/3, and 3-adic y in Z_3. Define a(x)=v2(3x+1), a finite integer >=1, and
\[
\boxed{
\mathcal F(r,x,y)=
\left(
\frac{3r+1}{2^{a(x)}},
\frac{3x+1}{2^{a(x)}},
\frac{3y+1}{2^{a(x)}}
\right).
}
\]
This is a **partial map**: some noninteger 2-adic points may eventually land on the singular point -1/3. To iterate indefinitely, restrict to points whose forward 2-adic orbit avoids the singularity. Every positive odd integer diagonal belongs to this infinite-iteration domain.

The exponent a(x) is locally constant on a suitable 2-adic cylinder x+2^(a+1)Z_2, so F is continuous in the product topology wherever defined. It sends each diagonal positive odd integer (n,n,n) to (S(n),S(n),S(n)). It is therefore an exact continuous high-dimensional realization of the original integer dynamics on its diagonal.

In a fixed-a branch the real slope is 3/2^a, the 2-adic separation factor is 2^a and the 3-adic separation factor is 1/3. These three factors multiply to **1**. On any specified k-step exponent word the 3-adic fiber contracts by 3^(-k), but this does **not** force the real height to shrink, since the 2-adic branch can change or expand.

## 3. Even two p-adic coordinates alone cannot distinguish ordinary positive integers

For any odd r2 modulo 2^h and arbitrary r3 modulo 3^k, CRT produces a positive odd n with
\[
n=r_2\pmod{2^h},\qquad n=r_3\pmod{3^k}.
\]
Consequently the positive odd diagonal {(n,n)} is dense in Z_2^odd x Z_3. Its membership in ordinary positive integers cannot be captured by a closed p-adic set that distinguishes it from all artificial p-adic pairs. A quantitative **Archimedean height** condition must accompany the p-adic phase coordinates.

**Analytic caveat:** do not insert an arbitrary 3-adic turn number t into an ordinary complex exponential exp(2*pi*i*t); there is no canonical continuous complex evaluation of all Z_3 turns. The legitimate finite-frequency probes are the roots of unity exp(2*pi*i*t_k/3^k).

## 4. Next target — open

Find a **seed-uniform, along-one-orbit** incompatibility between (a) real height, (b) the 2-adic exponent/branch-change itinerary, and (c) precision of 3-adic matching to inverse ancestors of 1. No such inequality follows from these lemmas. Existing static Fourier and coefficient-cancellation results do not solve it. This note closes a tempting but invalid pure 3-adic-contraction approach and exhibits a mathematically sound joint extension instead.

## 5. Independent verification

Run:
- python src/adelic_branch_lift.py
- python -m unittest discover -s tests -p 'test_adelic_branch_lift.py' -v

Five exact integer tests pass locally, checking all-anchors CRT witnesses, incompatible cluster limits of images, valuation residue uniqueness, and diagonal density at finite precisions. No Lean formalization is claimed.
