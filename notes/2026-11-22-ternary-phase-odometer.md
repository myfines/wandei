# 2026-11-22: Exact inverse-phase / 3-adic odometer for the odd-only map

**Status:** rigorous elementary inverse-ray identities, exact finite tests and explicit *no-go* for a purely static 3-adic phase proof. **Not** a proof of Collatz; much of the inverse-tree and p-adic mathematics is classical. The contribution here is an auditable synthesis connecting the user's suggested "complex phase / winding count" to actual positive-integer ancestors, their real heights, and the 2- and 3-adic geometries.

This complements (rather than supersedes) \`notes/2026-09-28-rotation-cocycle.md\`, \`notes/2026-09-29-ternary-moving-anchor.md\` and the phase/cylinder finite-horizon branch notes. Unlike the forward symbolic phase sums, the finite character cancellation below occurs on **genuine positive integers known to reach the chosen target**.

## 1. Every odd integer has a unique (target, turns) coordinate

For a positive odd integer n define
\[
S(n)=\frac{3n+1}{2^{v_2(3n+1)}}.
\]
Its image m=S(n) is positive, odd, and never divisible by 3.

For every positive odd m with 3 not dividing m define
\[
a_0(m)=\begin{cases}2&m\equiv1\pmod3,\\1&m\equiv2\pmod3.\end{cases}
\]
All **positive odd one-step inverse ancestors** of m, with no omissions, are
\[
R_m(t)=\frac{2^{a_0(m)+2t}m-1}{3},
\qquad t=0,1,\dots.
\]
They obey
\[
S(R_m(t))=m,\quad R_m(t+1)=4R_m(t)+1,\quad
3R_m(t)+1=2^{a_0(m)+2t}m.
\]

Conversely given any positive odd n, the pair
\[
m=S(n),\qquad
t=\frac{v_2(3n+1)-a_0(m)}2
\]
is a uniquely determined element of \((\mathbb N_{odd}\setminus3\mathbb N)\times\mathbb N_0\), with n=R_m(t). This is a true bijective coordinate change, **not** yet a map that sends every n to 1.

For m=1, \(a_0=2\):
\[
R_1(t)=\frac{4^{t+1}-1}{3}=1,5,21,85,341,\ldots.
\]
Under the shortcut odd-only map, \(S(1)=1\), so these are actual, not formal, convergent seeds.

## 2. Complex-phase lock (fixed target)

Define, for positive odd n and fixed m above,
\[
\mathcal P_m(n)=
\exp\left(2\pi i\log_4\frac{3n+1}{2^{a_0(m)}m}\right).
\]
Then
\[
\boxed{\mathcal P_m(n)=1\iff S(n)=m.}
\]

Proof: the exponential is 1 exactly when the **real logarithm** in the exponent is an integer t. The equation \(3n+1=2^{a_0(m)+2t}m\) and parity/integrality rule out t<0 (for t=-1, the RHS is either nonintegral or odd; for smaller t it is also impossible), hence t>=0 and n=R_m(t). The converse is immediate.

For stable target 1 this simplifies to
\[
\mathcal P_1(n)=\exp(2\pi i\log_4(3n+1))
\quad\text{and}\quad
\mathcal P_1(n)=1\iff S(n)=1.
\]
The local nonnegative phase energy \(V(n)=2-2\cos(2\pi\log_4(3n+1))\) has zeros at all direct ancestors of 1, but is **not** a globally decreasing Lyapunov function. E.g. under S, 7->11 and V(11)>V(7).

This phase lock is an exact detection of **one step to a specified target**, not proof of finite-time reachability for all n.

## 3. The new exact winding-number identity is a 3-adic isometry

For t≠u, using \(4=1+3\) and the lifting-the-exponent lemma
\(v_3(4^r-1)=1+v_3(r)\), obtain
\[
\boxed{v_3(R_m(t)-R_m(u))=v_3(t-u).}
\]
Therefore, for every integer k>=1,
\[
\boxed{R_m(t)\equiv R_m(u)\pmod{3^k}
\iff t\equiv u\pmod{3^k}.}
\]
Moreover \(t=0,\dots,3^k-1\) visits **every** residue class mod \(3^k\) exactly once, since the 3^k classes are distinct.

Because the nonnegative integers are dense in \(\mathbb Z_3\), this isometry extends uniquely to an isometric homeomorphism
\[
R_m:\mathbb Z_3\stackrel{\sim}{\to}\mathbb Z_3,
\qquad R_m(t+1)=4R_m(t)+1.
\]
Thus the affine "sibling" map \(y\mapsto4y+1\) is conjugate to the 3-adic adding machine \(t\mapsto t+1\).

More explicitly,
\[
R_m(t)=\frac{2^{a_0(m)}m\,4^t-1}{3},\qquad
t=\frac{\log_{3\text{-adic}}((3y+1)/(2^{a_0(m)}m))}
           {\log_{3\text{-adic}}4}.
\]
The 3-adic logarithm here is **not** the real base-3 logarithm. Both numerator and denominator are in \(3\mathbb Z_3\), and the denominator has valuation exactly 1.

**Critical caveat:** a general 3-adic t is not a nonnegative ordinary integer. Its corresponding 3-adic y need not be an actual finite inverse ancestor. This is precisely why completing the phase circle does not automatically establish Collatz.

## 4. Exact root-of-unity cancellation over real convergent integers

Let \(M=3^k\), \(\zeta=e^{2\pi i/M}\), and m be fixed. Because the actual integers \(R_m(0),\ldots,R_m(M-1)\) cover all residues mod M:
\[
\boxed{
\sum_{t=0}^{M-1}\zeta^{jR_m(t)}
=\begin{cases}M&M\mid j,\\0&M\nmid j.\end{cases}}
\]
For m=1, **every summand comes from a positive integer that really reaches 1 in one odd step**. Hence the phase cancellation no longer relies on summing "fictional" parity words. The limitation remains: this is an ensemble sum of a very sparse set, not a pointwise constraint on arbitrary n.

## 5. Real / 2-adic size conservation and sparse-height cutoff

For any fixed m:
\[
(3R_m(t)+1)|3R_m(t)+1|_2=m.
\]
In particular for m=1:
\[
|3R_1(t)+1|_\infty\,|3R_1(t)+1|_2=1,
\quad R_1(t)\to+\infty\text{ in }\mathbb R,
\quad R_1(t)\to-1/3\text{ in }\mathbb Q_2.
\]
But the sequence \(R_1(t)\) does not converge in \(\mathbb Z_3\); it visits all 3-adic residues modulo every fixed power.

The exact height cutoff is
\[
R_m(t)\le X\iff 2^{a_0(m)+2t}m\le3X+1.
\]
If \(t_{\max}(m,X)\) is the largest nonnegative feasible turn (or -1), the number of distinct residues mod \(3^k\) occupied by these true direct ancestors below X is
\[
\boxed{\min(3^k,\ t_{\max}(m,X)+1).}
\]
Thus density in \(\mathbb Z_3\) is **not** density among bounded positive integers.

Example m=1, X=10^6: feasible turns t=0,...,9, so only 10 of the 6561 residue classes mod \(3^8\) are occupied at that height. The next turn already yields 1,398,101 > 10^6.

More generally, for each fixed odd-only depth d the number of positive odd integers n<=X reaching 1 within d odd-only steps is \(O_d((\log X)^d)\) as X grows. Proof: S(n)<2n, so every intermediate of such a path is <=2^d X; each inverse node has at most \(1+O(\log(2^d X))\) ancestors under this common bound; sum the resulting finite tree to depth d. Fixed-depth inverse coverage has natural density zero, even though a single inverse ray is 3-adically dense.

## 6. Reproducible exact tests

\`src/inverse_phase_odometer.py\` implements forward/inverse coordinates, exact modulo \(3^k\) evaluation, base-3 Hensel-style turn lifting (without building huge \(4^t\)), residue coverage, and a capped inverse tree.

\`tests/test_inverse_phase_odometer.py\` independently checks:
- all positive odd n<10000 reconstruct from their unique (m,t);
- 3-adic isometry and permutation mod \(3^k\) for multiple targets and k<=6;
- the stable-target phase lock through 10k integers;
- phase lifting for r=7 and k<=10;
- exact X<=10^6 inverse tree counts against direct forward iteration.

Sample exact turn lifts for target m=1, desired residue r=7:

| k | 3^k | t_k (mod 3^k) |
|---:|---:|---:|
| 1 | 3 | 0 |
| 2 | 9 | 6 |
| 3 | 27 | 6 |
| 4 | 81 | 60 |
| 5 | 243 | 141 |
| 6 | 729 | 384 |
| 7 | 2187 | 1842 |
| 8 | 6561 | 1842 |
| 9 | 19683 | 8403 |
| 10 | 59049 | 47769 |

For X=1,000,000, the numbers of positive odd seeds reaching 1 in at most d odd-only steps for d=1,...,5 are **10, 44, 122, 298, 580**, independently checked by reverse generation and by direct forward trajectories.

## 7. No-go, and the next worthwhile question

The one-step inverse ray of m is dense in \(\mathbb Z_3\). Therefore any continuous real-valued function on \(\mathbb Z_3\) which vanishes on all one-step inverse ancestors must vanish everywhere. **A purely 3-adic continuous phase energy cannot separate genuine one-step convergence from nonmembers of that ray.**

The arithmetic distinction is the *diagonal consistency* of the turn count:
- in \(\mathbb R\), t is a nonnegative integer connected to exponential height \(R_m(t)\asymp4^t\);
- in \(\mathbb Z_3\), t controls residue phases and can be an arbitrary 3-adic integer;
- in \(\mathbb Q_2\), increasing ordinary t contracts the distance to \(-1/3\).

A potentially useful research target is a **cross-scale phase-height incompatibility lemma** for an *infinite sequence of compatible inverse turns* (with the true orbit constraints), not a claim about single inverse rays, single moduli, or cancellation averaged over a family. It would need to exclude an infinite positive-integer orbit that forever avoids the actual inverse tree of 1. No such lemma is established here.

## Background

- Bernstein and Lagarias, *The 3x+1 Conjugacy Map*, Canadian J. Math. (1996): https://websites.umich.edu/~lagarias/doc/bernstein.pdf
- Standard p-adic logarithm on \(1+3\mathbb Z_3\), e.g. Blomer and Milićević, *p-adic analytic twists and strong subconvexity*: https://pure.mpg.de/pubman/item/item_3120099_3/component/file_3276511/Blomer-Milicevic_p-adic%2Banalytic%2Btwists%2Band%2Bstrong%2Bsubconvexity_Preprint.pdf
- Prior wandei studies already handle inverse exponent rays and logarithmic rotations; no novelty is presumed.
