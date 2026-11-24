# Collatz research: binary carry polynomials
2026-11-25 — exploratory note, NOT a proof.

## Motivation
Instead of suppressing the +1 term as a small real perturbation, study the exact binary carries it produces. Seek a simple elementary termination certificate, possibly via polynomial or Fourier methods. Earlier directions (Möbius inversion, complex rotation, 2-adic series, Hankel rank, affine rewriting) generated conditional reductions but no complete proof. Do not treat these as independently verified novel results.

## Exact identity
For a positive odd integer n, let U(n)=(3n+1)/2^a, a=v_2(3n+1), and P_n(X)=sum_j b_j X^j, where b_j are its binary digits. Let C_n(X)=sum_j c_{j+1} X^j, with c_0=0, b_{-1}=0 and
b_j+b_{j-1}+1_{j=0}+c_j=d_j+2c_{j+1},
where d_j are the binary digits of 3n+1. Carries are nonnegative integers; all sequences have finite support. Summing gives
(1+X)P_n(X)+1-X^a P_{U(n)}(X)=(2-X)C_n(X).
At X=2 this is Collatz; at X=1 it gives s_2(U(n))=2s_2(n)+1-C_n(1); at X=-1 it gives (-1)^a P_U(-1)+3C_n(-1)=1.
On the unit circle, multiplication by X^a is unitary, and Parseval gives ||P_n||_2^2=s_2(n) with normalized angular measure.

## Proposed energy and immediate obstruction
Consider E_w(n)=integral w(theta)|P_n(exp(i theta))|^2 dtheta/(2pi), w>=0 integrable. Seek a strict decrease, or a more general carry-based potential with finite sublevel sets. The naive single-step translation-invariant quadratic energy cannot work: n=9 (P=1+X^3), U(n)=7 (P=1+X+X^2) alone does not rule out all weights, but the family n=2^k+1, k>=3, does. For these n, a=2 and U(n)=3*2^(k-2)+1, so P_U=1+X^(k-2)+X^(k-1). The energy difference tends to integral w |1+e^(i theta)|^2 minus integral w, i.e. integral w (1+2cos theta); this particular family is only a necessary constraint, not a universal impossibility proof. More decisively n=2^k-1, k>=3, has U(n)=3*2^(k-1)-1=2^k+2^(k-1)-1, with digits at positions 0,...,k-2 and k. This imposes additional constraints. Do not assert a no-go theorem without checking all weights. Also E_w(2^k+1) stays bounded by 4 integral w, so E_w alone is never proper on odd integers. Properness is sufficient, not necessary for termination; a discrete well-founded range could substitute.

## A concrete alternative
Track a potential that includes the length of the string and a correction for carries, or use a finite set of derived legal rewrite rules with a well-founded order. A successful certificate must decrease on all n>1 (or on a rigorously specified finite/variable block), not just typical trajectories. A correction H with integer nonnegative total V(n)=s_2(n)+H(n) would suffice if
C_n(1)=s_2(n)+1+H(U(n))-H(n)+D(n), D(n)>=1 for n>1.
This is a target, not a proved inequality.

## Gemini handoff
Act as an independent mathematical collaborator and adversarial reviewer. Prioritize deriving new unconditional identities or inequalities from the carry recurrence; test proposed potentials against long runs, sparse binary strings and arbitrary legal finite parity prefixes. Examine finite-state transducers, weighted automata, string rewriting, and q-analog literature; distinguish published results from speculation. Try a different representation if quadratic energy fails. Seek an elementary global descent or a proof that every odd n>1 shares its forward orbit with a smaller positive integer. Treat cycles and divergent trajectories separately unless a certificate handles both. Never infer a universal statement from density or finite experiments. Report exact lemmas, counterexamples, remaining gaps, and source references. Do not claim the Collatz conjecture or a connection implying it from RH has been proved.
