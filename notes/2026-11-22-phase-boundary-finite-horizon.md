# 2026-11-22: Exact arithmetic cylinders and Euler-phase cancellation (finite horizon)

**Status:** exact elementary finite-horizon results + standard-library regression tests. **Not** a Collatz proof, not a proof of Terras's coefficient-stopping-time conjecture, and no claim of mathematical novelty. This uses the *shortcut* map T(n)=n/2 if even and (3n+1)/2 if odd, rather than the odd-only Syracuse map elsewhere in this repository.

## 1. Exact residue/correction formula

For a binary parity word b=(b_0,...,b_{k-1}), define S_j=Σ_{i<j} b_i and C_0=0, C_{j+1}=3^{b_j}C_j+2^j b_j. Any initial integer n realizing b satisfies

    2^j T^j(n)=3^{S_j}n+C_j      (1<=j<=k).

Each word is realized on exactly one residue class mod 2^k, explicitly

    r(b)= -3^{-S_k} C_k  (mod 2^k).

These are classical parity/residue facts.

## 2. Exact *real trajectory* first-descent condition for each word

Define D_j=2^j-3^{S_j}. Then

    T^j(n)>=n  <=>  C_j>=D_j*n.

If D_j<=0 this is automatic for n>0. If D_j>0 it is exactly n<=floor(C_j/D_j). Let

    U_k(b)=min_{1<=j<=k, D_j>0} floor(C_j/D_j),

taking U_k(b)=infinity when there are no such j. Consequently the positive integer seeds which realize b *and* never dip below their initial value through step k are exactly

    {n>=1 : n==r(b) (mod 2^k) and n<=U_k(b)}.

The code counts these genuine seeds in arbitrary finite intervals by exact arithmetic progressions; no floating point, Monte Carlo, or replacement of one orbit by an average over all formal words.

## 3. Explicit large-seed equivalence, for every fixed finite k

Induction on the correction recurrence gives 0<=C_j<=3^j-2^j. If 3^{S_j}<2^j, the positive integer D_j=2^j-3^{S_j} is at least 1. Thus whenever

    n>=N_k:=3^k-2^k+1,

we have D_j*n>=n>3^k-2^k>=C_j, and T^j(n)<n. The converse T^j(n)<n => 3^{S_j}<2^j follows from C_j>=0. Equality 3^{S_j}=2^j is impossible for j>=1.

Therefore for each fixed k and EVERY n>=N_k:

    [T^j(n)>=n for all 1<=j<=k]
      <=>
    [3^{S_j}>2^j for all 1<=j<=k].

N_k is not sharp and increases with k; this **does not establish** coefficient-stopping-time equality for all k or Collatz convergence.

## 4. Exact phase cancellation for large blocks of *genuine* integers

Let B_k be the allowed words on the right side above, and P_k(z)=Σ_{b∈B_k} z^{S_k(b)}. Define q_0=0 and q_j=min{s:3^s>2^j} (j>=1); let delta_j=q_{j+1}-q_j in {0,1} and A_j count B_j words with S_j=q_j. Pairing an old word's odd/even children gives

    P_{j+1}(z)=(1+z)P_j(z)-delta_j*A_j*z^{q_j}.

At Euler's phase z=-1=e^{i*pi},

    P_{j+1}(-1)=-delta_j*A_j*(-1)^{q_j}.

In particular P_k(-1)=0 if q_k=q_{k-1}. Any interval [N,N+2^k-1] with N>=N_k contains each parity residue exactly once, and section 3 identifies the true first-descent-avoiding integers with B_k. Hence the exact phase identity on positive integer orbits is

    Σ_{n=N}^{N+2^k-1} 1{T^j(n)>=n for all j<=k}*(-1)^{S_k(n)}
       = P_k(-1).

This is an exact ensemble identity; it says **nothing pointwise** about any fixed initial integer.

## 5. Small-seed correction and obstruction

For a finite interval, word b contributes only members of its arithmetic progression n==r(b) mod 2^k that also satisfy n<=U_k(b). Thus the additive +1 corrections can be isolated exactly, with no assumption of coefficient/actual stopping-time equality.

For [1,2^k], finite exact cylinder counts for 1<=k<=16 find coefficient-survivor count plus exactly one extra positive seed (n=1). At k=12: 226 coefficient-survivor words, 227 actual no-descent seeds, signed phases 30 versus 31. **This is a finite computation, NOT a proof for all k.** The general question of equality of Terras coefficient stopping time and actual first descent for n>=2 is open.

The root-of-unity projector for a fixed n selects one b from 2^k words. Thus cancellation among different words cannot alone bound a specified orbit; additional cross-scale arithmetic constraints are essential.

## 6. Reproduction, prior work, and references

Run:

    python src/phase_exact_finite_horizon.py
    python -m unittest discover -s tests -p 'test_phase_exact_finite_horizon.py' -v

Companion CSV: notes/2026-11-22-phase-finite-results.csv (all exact counts k=1..16). Related local work: notes/2026-09-29-static-2adic-fourier-barrier.md; notes/2026-10-01-algebraic-frequency-obstruction.md. This time-dependent phase path experiment does not evade that earlier *static* Fourier barrier.

External context: Terras (1976), Mike Winkler (2026 preprint) https://doi.org/10.13140/RG.2.2.20089.94563 and *Paradoxical behavior in Collatz sequences* (2026) https://www.sciencedirect.com/science/article/abs/pii/S0012365X26001913. Literature already studies the coefficient stopping-time structure; avoid claiming this reformulation is novel.
