# 2026-11-22 — A higher-dimensional mod-27 Collatz lift and exact tropical hit-word energy

**Status:** elementary exact integer theorems, verified by independently implemented finite-state methods. **NOT** a proof of Collatz, and mathematical novelty is *not established*. This is a new research checkpoint relative to the project's earlier mod-27 and dual-carry notes.

Let the odd-only Syracuse map be \(S(n)=(3n+1)/2^{a(n)}\), \(a(n)=v_2(3n+1)\), for positive odd \(n\). Define \(h(n)\in\{0,1\}\) by whether the shortcut steps *after* \(n\) and up to \(S(n)\) contain any state \(20\bmod27\). The exact modular threshold from the preceding checkpoint is \(h(n)=1\iff a(n)\ge\tau(n\bmod9)\), with \(\tau=[11,13,9,17,1,15,5,7,3]\).

## 1. Genuine higher-dimensional phase lift

Set \(r_j=n_j\bmod9\), \(b_j=h(n_{j-1})\) for \(j\ge1\), \(b_0=0\), \(h_j=h(n_j)\). Form the state

\[
X_j=(n_j,r_j,b_j,\sigma_j),\quad \sigma_0=0.
\]

For a step with exponent \(a=a(n_j)\), define

\[
 r'= (3r+1)2^{-a}\bmod9,\quad h=\mathbf 1_{a\ge\tau(r)},\quad p=bh.
\]

The potential \(\psi(r,b)\) below is an exact integer certificate. A dash means the state cannot occur after any positive odd step (the image is never a multiple of 3).

| r mod9 | ψ(r,0) | ψ(r,1) |
|---:|---:|---:|
|0|0|–|
|1|0|0|
|2|0|-1|
|3|0|–|
|4|0|4|
|5|0|1|
|6|0|–|
|7|0|2|
|8|-1|3|

Define the *local charge*

\[
 d(r,b,a)=a-1-h-4bh-[\psi(r',h)-\psi(r,b)].
\]

**Theorem A (pointwise nonnegative lifted charge).** For every allowed state and positive exponent, \(d\ge0\). Hence

\[
 X_{j+1}=\left(\frac{3n_j+1}{2^a},r',h,\sigma_j+d\right)
\]

is an exact map on positive-integer diagonal states with a globally nondecreasing \(\sigma\)-coordinate. For an arbitrary finite actual orbit, with \(A_k=\sum_{j<k}a_j\), \(H_k=\sum_{j<k}h_j\), and \(P_k=\sum_{1\le j<k}h_{j-1}h_j\), telescoping gives

\[
 A_k-k-H_k-4P_k=\psi(r_k,b_k)-\psi(r_0,0)+\sigma_k.
\]

Since \(\psi(r_0,0)\in\{-1,0\}\) and \(\psi(r_k,b_k)\ge-1\):

\[
 \boxed{A_k\ge k+H_k+4P_k-1.}
\]

The constant -1 is best possible: \(31\to47\) has \(a=1,h=1,k=1\). The coefficient **4** is best possible among estimates with a fixed additive constant: for any L there is a positive integer whose first L odd valuations are all 6, staying at residue 4 mod9; each block is a hit. Then \(A=6L, H=L,P=L-1\), making an attempted coefficient \(4+\varepsilon\) impossible as \(L\to\infty\).

**Finite proof certificate:** r lies in 0..8, b is 0 or 1, but b=1 only if r is a unit modulo 9, leaving 15 states. For h=0, a<tau(r); for h=1, residue transitions depend only on a mod6 and taking a to a+6 increases d by exactly 6. Hence checking the 204 representative edges with a in 1..tau(r)+5 is an exhaustive finite proof, which the code performs in exact integers.

## 2. Exact minimum cost of *every* finite hit/nonhit word

Let a prescribed binary word be \(b_0\dots b_{k-1}\), k>=1. Define its count H=sum b_j and its adjacent-hit count P=sum_(j=1..k-1) b_(j-1)b_j. Let U be the number of adjacent **0→1** transitions. Then \(H=b_0+P+U\).

**Theorem B (exact tropical hit-language energy):** among *all positive odd seeds* whose first k odd-only shortcut blocks have hit word b, the MINIMUM total 2-exponent sum is exactly

\[
 \boxed{A_{\min}(b)=k+H+4P-b_0=k+5P+U.}
\]

This is an exact arithmetic optimum, not an expectation. It has a surprisingly simple proof by a finite-state lower-bound certificate and a positive-integer construction.

**Lower bound.** For b0=1, Theorem A immediately yields the displayed expression. For b0=0, Theorem A gives at worst one unit less. That extra loss is impossible: if initial r=8, ψ(initial)=-1 and all terminal potentials are ≥-1; otherwise ψ(initial)=0, and the only first **nonhit** steps with zero local charge go to states (r,b)=(2,0) or (5,0), neither of which has a zero-charge outgoing edge. So a path starting with a nonhit cannot achieve total surplus -1. This is a finite check in the same 204-edge table.

**Upper bound and explicit constructive witness.** Append a sentinel bit b_k=0. Choose

\[
 \boxed{a_j=1+(1+4b_j)b_{j+1}\qquad(0\le j<k).}
\]

Thus a_j is 6 for hit→hit, 2 for nonhit→hit, and 1 otherwise. Start at residue r=4 mod9 when b0=1, or r=8 mod9 when b0=0. The transitions of residues 2,4,8 close exactly:

- r=4 and a=6: hit, next r=4; r=4 and a=1: hit, next r=2.
- r=2 and a=2: nonhit, next r=4; r=2 and a=1: nonhit, next r=8.
- r=8 and a=2: nonhit, next r=4; r=8 and a=1: nonhit, next r=8.

Hence every b is realized by this exponent word on one **genuine positive integer arithmetic progression** obtained by CRT between its standard odd 2-adic valuation cylinder and the prescribed initial residue mod9. The total cost is k+5P+U. Combined with the lower certificate, this is exact.

**Independent verification:** a 9×9 min-plus weighted adjacency matrix for hit=0 and another for hit=1 computes the minimum a over all genuine positive seeds. It agrees with the explicit three-symbol construction for **all 8190 nonempty bit words of lengths 1..12**, and direct shortcut iteration on each explicit witness independently reproduces each hit symbol.

## 3. Two-dimensional Euler-phase transfer and exact cancellation

The minimum cost is equivalent to a one-dimensional nearest-neighbour lattice energy, with transition surcharge

| previous hit | next hit | extra cost beyond 1 next step |
|---:|---:|---:|
|0|0|0|
|0|1|1|
|1|0|0|
|1|1|5|

Introduce a generating polynomial counting *each binary hit word once*, weighted by its **minimum** total exponent:

\[
 Z_k(z)=\sum_{b\in\{0,1\}^k}z^{A_{\min}(b)}
 = z(1,1)\begin{pmatrix}z&z^2\\z&z^6\end{pmatrix}^{k-1}\binom11.
\]

At Euler phase z=-1 the 2×2 transfer matrix becomes

\[
 M(-1)=\begin{pmatrix}-1&1\\-1&1\end{pmatrix},\quad M(-1)^2=0,\quad M(-1)\binom11=0.
\]

Therefore

\[
 \boxed{Z_k(-1)=0\quad\text{for every }k\ge2.}
\]

This is an *exact algebraic cancellation*, but crucially **each binary pattern is counted with weight 1**, not each actual positive integer, and all exponents are replaced by their minimum legal costs. This identity therefore provides **no pointwise descent theorem**.

## 4. Exact real-height coupling and why this is still not Collatz

With \(\epsilon_j=\log_2(1+1/(3n_j))>0\), the real height obeys

\[
 \log_2(n_k/n_0)=k(\log_2 3-1)-H_k-4P_k-\sigma_k
 -[\psi(r_k,b_k)-\psi(r_0,0)]+\sum_{j<k}\epsilon_j.
\]

Thus if N were a least positive odd counterexample, all n_j>=N and \(\epsilon_j\le\delta_N=\log_2(1+1/(3N))\) would force

\[
 \boxed{H_k+4P_k+\sigma_k\le k(\log_2 3-1+\delta_N)+1.}
\]

This is a **joint deterministic necessary condition on one actual orbit**, with a nonnegative monotone charge and explicit adjacent-hit penalty. It is not contradictory with the known 20 mod27 recurrence theorem, which forces infinitely many hits but no large lower hit density.

**Essential phantom-cycle test:** the legal infinite symbolic exponent script (1,2)^infinity at residues 4→2→4 realizes hit pattern (1,0)^infinity, has σ=0, P=0, and formal real multiplier 9/8>1 every two steps. Its unique infinite 2-adic fixed seed is -5, **not a positive integer**. Arbitrarily long finite positive-integer shadows exist by CRT. Therefore a purely finite-state/phase-charge proof cannot exclude all symbolic expanding paths: an additional **fixed-positive-seed, cross-scale** compatibility theorem is still missing.

## 5. Reproduction and source context

Standard-library Python:

```
python src/highdim_mod27_lift.py
python src/mod27_tropical_transfer.py
python -m unittest discover -s tests -p 'test_highdim_mod27_lift.py' -v
```

Mathematical input and prior art: Monks et al. (2013), *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, https://arxiv.org/abs/1204.3904; Bernstein–Lagarias, *The 3x+1 Conjugacy Map*, https://websites.umich.edu/~lagarias/doc/bernstein.pdf. Tropical/min-plus weighted automata are standard; this is a specific Collatz-mod27 application and is not asserted to be an original published result.