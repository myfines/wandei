# 2026-11-22 — Collatz / Riemann-zeta bridge: an exactly solvable inverse-ray spectrum

**Status:** elementary theorems, explicit meromorphic continuation and numerical cross-checks. **NOT** a proof of Collatz or the Riemann hypothesis (RH). No claim of originality for Koopman/Dirichlet reformulations or elementary self-similar zeta mathematics.

## 1. Real literature connection, not an RH implication

Berg–Meinardus (1994) recast Collatz as uniqueness of solutions to a holomorphic functional equation. Meinardus, *Some Analytic Aspects Concerning the Collatz Problem* (2001), studies a special Dirichlet-series operator, and the Collatz conjecture is equivalent to the one-dimensional kernel being spanned by the ordinary Riemann zeta function. See https://madoc.bib.uni-mannheim.de/1608/ and https://www.math.uni-rostock.de/math/pub/romako/heft48/berg2.html . Leventides–Poulios, *Koopman operators and the 3x+1-dynamical system* (arXiv:2010.12987), explore an infinite-dimensional linear lift.

This is **different** from the Riemann hypothesis, a conjecture about nontrivial zeros of ordinary ζ(s). In particular, the existence of ζ in an invariant kernel does not say that RH controls that kernel's multiplicity.

## 2. One-step inverse rays and an explicit Dirichlet zeta

Let S(n)=(3n+1)/2^{v₂(3n+1)} on positive odd n. Fix a positive odd target m with 3∤m; let a_m=2 if m≡1 (mod3), otherwise a_m=1, and B_m=2^{a_m}m (so B_m≡1 mod3 and B_m≥4).

All positive odd **direct ancestors** of m are precisely

    R_m(t)=(B_m*4^t−1)/3,   t=0,1,...,

with S(R_m(t))=m and R_m(t+1)=4R_m(t)+1. For Re(s)>0, define

    Z_m(s)=sum_{t≥0} R_m(t)^(−s).

By the binomial series (1−x)^(−s)=Σ_{j≥0}(s)_j x^j/j!, where (s)_j is the rising Pochhammer factorial,

    **Z_m(s)=(3/B_m)^s sum_{j≥0} [(s)_j/(j!*B_m^j)] / [1−4^(−(s+j))].**

The right-hand expression converges locally uniformly on compact sets avoiding its poles, and thus extends Z_m meromorphically to **all** of C. Each j-term decays exponentially like B_m^(−j) times a polynomial in j. The poles are all simple, at

    **s_(j,ell)=−j + 2πi ell/log4, j=0,1,..., ell∈Z.**

The residue at such a pole is

    Res Z_m(s_(j,ell))=
       [(3/B_m)^(s_(j,ell)) (s_(j,ell))_j]/[j!*B_m^j*log4].

Since (s_(j,ell))_j is nonzero, there is no pole cancellation inside one ray.

For m=1 (the stable target), B_m=4 and the formula simplifies to

    **Z_1(s)=3^s Σ_{j≥0} (s)_j / [j! (4^(s+j)−1)].**

This is an exact small spectral model: the affine inverse sibling map R(n)=4n+1 becomes a pure dilation under x=n+1/3, namely x→4x. Its Koopman eigenvalues on x^(−s−j) are 4^(−s−j), which give the resolvent denominators 1−4^(−s−j).

## 3. Universal real-axis residues and exact cancellation

At each nonpositive integer pole s=−j, the residue simplifies to

    **Res_{s=−j} Z_m(s)=(-1)^j/(3^j log4), for ALL allowed targets m.**

Proof: (−j)_j=(-1)^j j!, and (3/B_m)^(−j)*B_m^(−j)=3^(−j).

Thus for any two targets m≠m', **Z_m(s)−Z_(m')(s) is holomorphic at every nonpositive integer**: its entire real-axis pole ladder cancels exactly. This is a precise counterpart to earlier Euler/Walsh cancellation, but over genuine positive integer inverse rays, each of which is known to reach its target after one step.

Numerical: Res(s=0)=1/log4≈0.72134752044; Res(s=−1)=−1/(3log4)≈−0.24044917348.

## 4. First imaginary pole encodes the TARGET as a complex phase

Set ω=2π/log4. At s=iω (j=0,ell=1), the residue is

    **ρ_m=Res_{s=iω}Z_m(s)=(1/log4) exp[−2πi log_4(B_m/3)].**

So all target rays share the same pole LOCATIONS, and share every real-axis pole residue, but their non-real pole **phases** are target-specific. The first non-real pole residue determines m uniquely among allowed positive odd targets:

If ρ_m=ρ_n, then log_4(B_m/B_n)∈Z, so B_m/B_n=4^k. Yet B_m=2^{a_m}m with a_m∈{1,2} and m odd, implying by ordinary 2-adic valuation that a_m−a_n=2k. The left side is in {−1,0,1}, hence k=0, a_m=a_n, and m=n.

This exact phase fingerprint supports the user's intuition that winding phases can encode target identity. **It detects the one-step target, not eventual convergence from an arbitrary seed.**

## 5. Another exact ζ(s) link that identifies the remaining logical gap

Define the positive odd basin of 1:

    B={n∈positive odd integers : S^k(n)=1 for some k≥0}.

For Re(s)>1, the basin Dirichlet series is

    Z_B(s)=Σ_{n∈B} n^(−s).

The full odd-integer Dirichlet series is

    Z_odd(s)=(1−2^(−s)) ζ(s).

Because Z_odd(s)−Z_B(s)=Σ_{odd n not in B} n^(−s) has **nonnegative coefficients**, the Collatz conjecture is equivalent to the single real equality

    **Z_B(2)=Σ_{n∈B}1/n²=π²/8.**

Any exceptional positive odd integer n would force a deficit of at least 1/n². This is an exact scalar reformulation, not a new analytic proof; bounding the deficit by zero is exactly the original hard problem in disguise.

The same distinction appears in a bounded-coefficient Koopman lift. Let A be the vector space of holomorphic Dirichlet series F_u(s)=Σ_{odd n} u(n)n^(−s), with bounded coefficients u. Define (K F_u)(s)=F_{u◦S}(s). Because bounded Dirichlet series have unique coefficients,

    **ker(I−K)=span{(1−2^(−s)) ζ(s)} iff Collatz holds.**

Proof: if every n reaches 1, any bounded u satisfying u=u◦S must be constant. If a counterexample exists, the nonconstant bounded indicator u(n)=1{n reaches 1} is invariant, giving a second linearly independent kernel element. This is an especially simple illustrative Koopman-kernel equivalence (different functional setting from Meinardus's cited work), not a shortcut to solve Collatz.

## 6. Rigorous anti-shortcut: pole information alone cannot see a lone exception

The analytic functions (1−2^(−s))ζ(s) and (1−2^(−s))ζ(s)−m^(−s) have **identical pole sets and identical pole principal parts**, since m^(−s) is entire. Yet the latter is missing the coefficient at m. The modified series is only a toy counterexample to the inference "matching ζ singularities proves matching all integer trajectories"; it is not asserted to arise from any genuine Collatz-invariant basin.

Likewise, the inverse-ray Z_1(s) is meromorphic on all C and has beautifully organized pole lines even though the ray {1,5,21,...} is extremely sparse among positive integers. Analytic continuation or tidy spectra alone do not imply full basin coverage.

## 7. Verified numbers and next step

Direct high-precision complex series and independent meromorphic expansion agree to >50 decimal digits at sample s. The residue formula has been checked for m=1,5,7,11 and several j,ell. A standard-library Python version also independently verifies the statements (see tests).

- Z_1(1)=1.26329305810027133188797...
- Z_1(2)=1.0424151543286642...
- first RH zero near s=0.5+14.1347251417347i: Z_1(s)≈0.934655223+0.417459524i, *not* zero. Numerical illustration only.
- Σ_{odd n≤1001} 1/n² over odd seeds verified to reach 1 within 150 odd steps is 1.2332015483..., versus π²/8=1.2337005501...; the finite difference includes the obvious size tail and does not bear on Collatz at infinity.

**Research next step (OPEN):** rather than proving that a local ray spectrum is regular, construct an operator on the **full distinct-ancestor tree**, preserving both the real height and the 2-/3-adic compatible integer diagonal. Seek a spectral/positivity estimate strong enough to annihilate *every positive coefficient* of the exceptional-basin defect, not only bound its average mass or pole data. Riemann-hypothesis-style zero bounds do not currently supply such an estimate.

Reproduce from repo: `python src/inverse_ray_zeta.py` and `python -m unittest discover -s tests -p 'test_inverse_ray_zeta.py' -v`. Six tests pass locally; no Lean formalization claimed.