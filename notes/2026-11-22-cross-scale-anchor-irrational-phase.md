# 2026-11-22 — 3-adic winding rigidity, anchor shadowing, and cross-metric conservation

**Status:** elementary proofs, exact integer tests, and a transcendence corollary that **imports Mahler's known theorem**. Not a Collatz proof; no claim of mathematical novelty.

This extends the existing odd-only inverse-ray and 3-adic odometer note on this branch. The forward odd-only Syracuse map is
\[
S(n)=\frac{3n+1}{2^{v_2(3n+1)}},\quad n\text{ a positive odd integer}.
\]

## A. Exact phase coordinate and a rationality/transcendence dichotomy

Fix any positive odd target m with 3 not dividing m. Define a=2 if m=1 (mod 3), and a=1 if m=2 (mod 3). All positive odd direct predecessors of m are exactly
\[
R_m(t)=\frac{2^a m\,4^t-1}{3},\qquad t=0,1,2,\dots.
\]

For every positive odd n define its winding coordinate in the 3-adic integers:
\[
\tau_m(n)=\frac{\log_3((3n+1)/(2^a m))}{\log_3 4}\ \in\ \mathbb Z_3.
\]
The logarithms are **3-adic**, not real. Both arguments are in 1+3Z_3, and v_3(log_3 4)=1, so the ratio belongs to Z_3. In this group the exponentiation identity is exactly
\[
4^{\tau_m(n)}=\frac{3n+1}{2^a m}.
\]

**Proposition A1 (elementary).** For positive odd n,
\[
\boxed{\tau_m(n)\in\mathbb Q\iff S(n)=m,}
\]
and in that case \tau_m(n) is actually a nonnegative ordinary integer.

**Proof.** Suppose \tau=p/q in lowest terms with q>0. Write Q=(3n+1)/(2^a m), a positive rational satisfying Q=1 mod 3 in the 3-adic sense. Raising the exponential identity to q gives the ordinary rational equality Q^q=4^p. Comparing ordinary prime-2 valuations shows q|2. If q=2, p is odd. Positivity gives Q=2^p, but that is -1 mod 3, contradiction. (This point needs care: the 3-adic square root 4^(1/2) in 1+3Z_3 is **-2**, not real +2.) Therefore q=1. Write p=t in Z; the equality 3n+1=2^(a+2t)m and oddness of n,m imply a+2t>=1. Since a is 1 or 2, t cannot be negative. Thus t>=0 and n=R_m(t), implying S(n)=m. Converse follows by substitution. QED.

**Corollary A2 (deep external input).** By Mahler's p-adic Gelfond–Schneider theorem, the ratio of p-adic logarithms of algebraic numbers is either rational or transcendental when defined with a nonzero denominator. The arguments above are rational algebraic units, hence
\[
\boxed{S(n)\ne m\implies\tau_m(n)\text{ is transcendental over }\mathbb Q.}
\]
No new transcendence theorem is claimed. Reference: F. Calegari and B. Mazur, *Nearly Ordinary Galois Deformations over Arbitrary Number Fields*, J. Inst. Math. Jussieu 8 (2009), Section 3.5, https://www.math.uchicago.edu/~fcale/papers/ordinary.pdf, which explicitly quotes Mahler's theorem.

## B. Precise finite winding / height gap

The earlier odometer isometry ensures that for every k>=1 there is a unique
\[
0\le t_k(n;m)<3^k,\quad R_m(t_k)\equiv n \pmod{3^k}.
\]
If S(n)=m, then t_k is eventually the fixed nonnegative turn index t.

If S(n)!=m and 3^k>n, the positive integer R_m(t_k) is not n and differs from n by a nonzero multiple of 3^k. It cannot be below n, since n<3^k. Thus
\[
R_m(t_k)\ge n+3^k,
\qquad
t_k\ge \log_4\left(\frac{3(n+3^k)+1}{2^a m}\right).
\]
Consequently
\[
\boxed{
\liminf_{k\to\infty}t_k/k =
0\quad\text{if }S(n)=m,\qquad
\liminf_{k\to\infty}t_k/k \ge\log_4 3
\quad\text{otherwise}.
}
\]
There is a strict **gap** in the normalized least phase-lift growth: no value strictly between 0 and log_4 3. This is purely elementary and is not a theorem of Collatz convergence.

For m=1, n=7 (not a direct predecessor), exact values include:
k=3: t=6 (lower bound 3); k=6: t=384 (bound 5); k=10: t=47769 (bound 8); k=16: t=21777801 (bound 13). Values are computed by modular 3-adic digit lifting, not approximations.

Effective p-adic linear-form estimates (Yu/Bugeaud–Laurent) may give stronger fixed-(m,n) lower bounds on t_k. However their constants depend on the numbers; no uniform pathwise inequality is established here.

## C. Stable fixed point can be shadowed for arbitrarily long *exact* intervals

For any integer k>=1 and positive odd q, define
\[
N_{k,q}=1+2q\,4^k.
\]
Then for every 0<=j<=k,
\[
\boxed{S^j(N_{k,q})=1+2q\,3^j4^{k-j}.}
\]
For j<k the 2-adic valuation v_2(3S^j(N)+1) is **exactly 2**, just like the stable fixed point S(1)=1. At j=k it becomes **exactly 1**. Therefore the exponent script agrees for exactly k steps and *must separate* on the next step.

Proof: for j<k the displayed state is 1 mod 8, yielding v_2(3x+1)=2, hence the next formula. At j=k the state is 3 mod 4, yielding v_2(3x+1)=1. QED.

Special case q=1: (k, initial n, state at k) equals
(1, 9, 7), (2, 33, 19), (3, 129, 55), (4, 513, 163), (5, 2049, 487), (10, 2097153, 118099).

**No-go consequence:** finite symbolic proximity to the stable orbit, even for arbitrarily many initial steps, cannot by itself establish eventual capture or a global Lyapunov function.

## D. Cross-metric separation conservation for a common exponent script

Let two distinct positive odd initial states x,y have the same exponent sequence a_0,...,a_(k-1) under the odd-only map, with A=sum a_j. Their affine correction terms cancel in the subtraction:
\[
S^k(x)-S^k(y)=\frac{3^k}{2^A}(x-y).
\]
Therefore the ratios of their distances are exactly:
- ordinary absolute value: 3^k / 2^A;
- 2-adic distance: 2^A;
- 3-adic distance: 3^(-k).

**The product of these three scale factors equals 1.** It is a special case of the rational product formula, not a newly proved invariant. This relation applies only on a **shared exponent-script cylinder**; after branch separation it does not give a global invariant for two arbitrary orbits.

For x=1, y=N_(k,1), the common script has A=2k. The initial real separation 2*4^k becomes 2*3^k after k steps, while the 3-adic distance shrinks by 3^(-k).

## E. Actual obstruction and next mathematical target

1. The transcendental/ordinary-integer phase dichotomy identifies **one-step** inverse-ray membership exactly. Iterating it naively merely rewrites the Collatz problem.
2. Arbitrary finite 2-adic shadowing of the stable cycle exists, so a finite phase lock does not force eventual reachability.
3. A multiplicative product of real/2-adic/3-adic distances is constant on shared scripts, so the easiest proposed global strict-contraction potential is **ruled out**.
4. The genuinely open task is a **uniform cross-scale branch-change constraint**: control along one *actual infinite orbit*, not just finite cylinders or sums over many paths, the interplay of real height, 3-adic target-match precision and the times where the 2-adic exponent script changes. The project's earlier static Fourier barrier remains applicable.

## F. Reproduction and epistemic status

Run:
- python src/cross_scale_anchor.py
- python -m unittest discover -s tests -p 'test_cross_scale_anchor.py' -v

Six independent standard-library regression tests locally pass: exact forced departure for k<=29 and odd multipliers; normalized lift bounds k<=16 across several targets/seeds; stabilized direct lifts; and real/2-/3-adic scaling. Tests support elementary formulas but cannot computationally verify Mahler's transcendence theorem or an infinite statement. No Lean compilation or full Collatz proof is claimed.

Additional background for possible future estimates: Kunrui Yu, *Linear forms in p-adic logarithms. III*, Compositio Mathematica 91 (1994), https://www.numdam.org/article/CM_1994__91_3_241_0.pdf .
