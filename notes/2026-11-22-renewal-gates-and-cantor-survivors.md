# 2026-11-22 — Two exact Syracuse renewal gates and a 2-adic Cantor survivor set

**Status:** rigorous elementary identities and reproducible exact integer experiments. **Not a Collatz proof; no originality claim.** This is a new *representation* of a narrow growth-only subproblem, not a theorem excluding all positive escaping orbits. Keep the original \`main\` proof status and errata unchanged.

Let \(S(n)=(3n+1)/2^{v_2(3n+1)}\) for positive odd integers.

## 1. Complete local classification from \(n\equiv3\pmod4\)

If \(n\equiv1\pmod4\) and \(n>1\), then \(S(n)<n\). Otherwise \(n\equiv3\pmod4\), \(v_2(3n+1)=1\), and
\[
y=S(n)=1+2^e u,\quad e\ge1,\ u\ge1\text{ odd},\qquad n=(1+2^{e+1}u)/3.
\]

**Odd \(e=2r+1\):** after \(r\) more forced valuation-2 odd steps,
\[
S^{r+1}(n)=1+2\cdot3^r u.
\]
For \(r=0\) or 1 the endpoint is greater than \(n\), still 3 modulo 4; these are precisely
\[
B_1(n)=\frac{3n+1}{2}\quad(n\equiv7\pmod8),\qquad
B_3(n)=\frac{9n+5}{8}\quad(n\equiv27\pmod{32}).
\]
For \(r\ge2\) it is below \(n\), since \(4^{r+1}-6\cdot3^r\ge10\).

**Even \(e=2r\), \(r\ge1\):** after \(r-1\) valuation-2 steps the state is \(1+4\cdot3^{r-1}u\); the following step is
\[
S^{r+1}(n)=\frac{1+3^r u}{2^{v_2(1+3^ru)}}\le\frac{1+3^r u}{2}<n.
\]
Last inequality follows from \(1+3^{r+1}u<4^{r+1}u\).

Thus every \(n\equiv3\pmod4\) makes either an **expanding renewal gate** \(B_1\) or \(B_3\), returning to 3 mod4, or a finite excursion ending **below that gate's own entry value**. Such a local descent after preceding growth need *not* fall below the original initial seed.

## 2. Exact 2-adic inverse IFS

Let \(X=3+4\mathbb Z_2\). The growing domains \(D_1=7+8\mathbb Z_2\), \(D_3=27+32\mathbb Z_2\) are disjoint and each gate maps bijectively onto \(X\) under 2-adic extension. Their inverse similarities are
\[
g_1(x)=(2x-1)/3,\quad |g_1(x)-g_1(y)|_2=\tfrac12|x-y|_2;
\qquad
g_3(x)=(8x-5)/9,\quad |g_3(x)-g_3(y)|_2=\tfrac18|x-y|_2.
\]
The compact invariant Cantor set \(K=g_1(K)\cup g_3(K)\subset X\) describes exactly infinite **2-adic** scripts taking *only* growing gates. For a finite word of \(r\) symbols, containing \(u\) gates \(B_1\) and \(v\) gates \(B_3\), its initial seeds form **one residue class** mod \(2^{2+u+3v}\), of relative Haar measure \(2^{-u-3v}\).

Hence the proportion of \(X\) still on a growing gate after \(r\) renewals is exactly
\[
\sum_{u+v=r}{r\choose v}2^{-u-3v}=(\tfrac12+\tfrac18)^r=(\tfrac58)^r.
\]
Equivalently, in **each complete integer block of length \(2^{3r+2}\)**, exactly \(5^r\) of the \(8^r\) integers congruent to 3 mod4 follow \(r\) growing gates. This is a deterministic count, not a random simulation.

By the standard disjoint-self-similar-IFS dimension argument,
\[
\dim_H(K)=d,\quad 2^{-d}+8^{-d}=1,\qquad d\approx0.5514630897455954.
\]
Haar measure of K is zero, yet K is nonempty and uncountable. **Whether K contains any positive integer is *not* decided**: a positive integer in K would generate an indefinitely expanding renewal trajectory, but proving \(K\cap\mathbb Z_{>0}=\varnothing\) would still not prove all Collatz orbits converge.

## 3. Exact transfer pressure, not a pointwise drift

A \(B_1\) gate has linear real multiplier \(3/2\) and conditional 2-adic mass \(1/2\); a \(B_3\) gate has \(9/8\) and mass \(1/8\). Thus for real s the full-word weighted partition function is
\[
Z_r(s)=\left[\tfrac12(3/2)^s+\tfrac18(9/8)^s\right]^r.
\]
In particular \(Z_r(0)=(5/8)^r,\ Z_r(1)=(57/64)^r,\ Z_r(2)=(657/512)^r\).
The multiplier is the **linear coefficient** in the affine return map, not the actual endpoint ratio. These are weighted ensemble identities; they do not prove any individual orbit loses height.

## 4. Exact finite tests and frontier

Python standard library only: \`src/renewal_gate_fractal.py\` enumerates exact residue cylinders; \`src/renewal_interval_frontier.py\` scans bounded positive odd seeds; \`src/export_interval_data.py\` independently checks all 2,500,000 n≡3 mod4 in 3<=n<=10,000,000 and creates \`notes/renewal_interval_10m.csv\`.

- Exact complete-modulus formula \(5^r\) independently brute-checked through r=4.
- Cylinder/forward-gate identity independently checked to r=6; all gate cases checked for 25,000 positive inputs.
- Bounded integer frontier: longest initial string of growing gates is **32**, attained by n=6,416,623; **all checked seeds** hit a *local descent gate* by the 33rd renewal decision.
- Minimal seeds by growing-gate prefix: r=12→4591; r=20→65307; r=23→159487; r=28→3041127; r=29→6416623.
- Seven new local unit tests pass. Lean proof checking not attempted.

Crucial distinction: this finite check does **not** establish eventual arrival at 1 for the checked seeds, only a first gate that descends relative to its *current* entry.

## 5. Open obstruction

The sole remaining question *within this simplified gate subsystem* is whether any fixed positive odd integer belongs to K. The complete Collatz problem is still harder, because trajectories can make arbitrarily long expanding runs, encounter a locally contracting gate, and then resume growth while remaining above their ORIGINAL starting minimum. Proving only Haar-nullity or Hausdorff dimension <1 does not eliminate isolated positive integers. A theorem coupling cumulative height with successive gate renewals is still missing.

Related background (not novelty claims): Bernstein–Lagarias 1996 2-adic conjugacy; Weitzer 2020 p-adic systems; Bell–Lagarias 2015 inverse orbit generating functions (DOI:10.4064/aa170-2-1). See prior wandei notes \`2026-09-29-static-2adic-fourier-barrier.md\` and \`2026-11-22-phase-switch-recharge-audit.md\`.
