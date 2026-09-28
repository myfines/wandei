# Final dyadic plateau rigidity — 2026-09-29

## Status

This note records a structural lemma for a hypothetical unbounded least positive counterexample to the accelerated odd-only Collatz map. It is **not** a proof of the conjecture.

Let

\[
T(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1)
\]

on positive odd integers, and suppose \(N\) is the least positive counterexample. Write the odd-only orbit as \(x_0=N,x_1,x_2,\ldots\).

Define

\[
h_i=\log_2(x_i/N),\qquad m_i=\lfloor h_i\rfloor,
\]

\[
b_i=a_i-1,\qquad \omega=\log_2(3/2),
\]

and

\[
\varepsilon_i=\log_2\left(1+\frac1{3x_i}\right)>0.
\]

Then exactly

\[
h_{i+1}=h_i+\omega-b_i+\varepsilon_i.
\]

If

\[
c_i=\lfloor \{h_i\}+\omega+\varepsilon_i\rfloor\in\{0,1\},
\]

then

\[
\boxed{m_{i+1}=m_i+c_i-b_i.}
\]

Because \(b_i\ge0\), every step raises the dyadic height index by at most one.

---

## 1. Final plateau before crossing a dyadic layer

Fix a sufficiently high layer \(r\). Before the orbit first reaches layer \(r+1\), consider the **last** time it enters layer \(r\) from below. From that entry until the first hit of layer \(r+1\), every intermediate state has

\[
m_i=r.
\]

Call this the final \(r\)-plateau.

For every internal step of this plateau,

\[
m_{i+1}-m_i=0,
\]

so the exact state equation gives

\[
\boxed{b_i=c_i.}
\]

Therefore

\[
\boxed{a_i=1+c_i\in\{1,2\}}
\]

at every internal plateau step.

The final crossing step satisfies

\[
m_{i+1}-m_i=1.
\]

Since \(c_i\le1\) and \(b_i\ge0\), this forces

\[
\boxed{c_i=1,\quad b_i=0,\quad a_i=1.}
\]

The entry step from layer \(r-1\) into layer \(r\) is forced to have the same form. Thus every final plateau is bracketed by two identical `up-defects` \((c,b)=(1,0)\), while all internal steps satisfy \(b=c\) exactly.

This removes the earlier need for a majorization argument on the final plateau: there is no freedom in the internal exponent word once the carry sequence is known.

---

## 2. Consequence for residues at upward layer crossings

At every upward layer crossing,

\[
a_i=1,
\]

so

\[
x_{i+1}=\frac{3x_i+1}{2}.
\]

For the predecessor to be integral in the reverse formula

\[
x_i=\frac{2x_{i+1}-1}{3},
\]

we must have

\[
\boxed{x_{i+1}\equiv2\pmod3.}
\]

Hence every dyadic record-entry state of a hypothetical unbounded least counterexample lies in the residue class \(2\bmod3\).

Also, if the current band is \([H,2H)\), the crossing condition

\[
\frac{3x_i+1}{2}\ge2H
\]

forces

\[
x_i\ge\frac{4H-1}{3},
\]

while the new entry state satisfies

\[
2H\le x_{i+1}<3H+\frac12.
\]

After rescaling the new band to \([1,2)\), record entries always land in its lower \(3/2\)-portion.

---

## 3. Plateau valuation word has two-sided bounded critical drift

Let a final plateau start at \(x_s\in[H,2H)\), and define

\[
\theta_0=\log_2(x_s/H)\in[0,1).
\]

For a prefix of \(j\) internal plateau steps, set

\[
E_j=\sum_{q<j}\varepsilon_{s+q}.
\]

Because \(b=c\) internally, the cumulative extra-valuation count satisfies

\[
B_j=\sum_{q<j}b_{s+q}
=\left\lfloor\theta_0+j\omega+E_j\right\rfloor.
\]

The valuation sum is

\[
S_j=j+B_j.
\]

With

\[
\alpha=\log_2 3=1+\omega,
\]

the critical drift becomes

\[
R_j=S_j-\alpha j
=B_j-\omega j
=\theta_0+E_j-\{\theta_0+j\omega+E_j\}.
\]

Therefore every proper plateau prefix satisfies

\[
\boxed{-1<R_j<1+E_j.}
\]

The final crossing prefix differs by one missing \(b\)-unit and satisfies

\[
\boxed{-2<R_L<E_L.}
\]

Thus every final dyadic plateau is automatically a finite **two-sided bounded-drift valuation word**.

---

## 4. Elementary uniform correction bound inside one band

A divergent orbit cannot repeat a positive state, so the odd states visited in a single band are distinct. After the first accelerated step, odd Syracuse outputs are not divisible by 3. Hence the number of possible odd orbit states in \([H,2H)\) is at most about \(H/3+O(1)\).

Since each plateau state satisfies \(x\ge H\),

\[
\varepsilon_i
=\log_2\left(1+\frac1{3x_i}\right)
<\frac1{3H\ln2}.
\]

Consequently the total correction accumulated during any single-band plateau obeys the elementary uniform bound

\[
E_{\rm band}
\lesssim \frac1{9\ln2}
\approx0.1603,
\]

up to the obvious endpoint \(O(1/H)\) term.

So, even without any probabilistic input, a final plateau is a near-critical word with a uniformly small Archimedean correction.

A stronger external input is available for divergent trajectories: García–Tal prove Banach-density zero for an aperiodic orbit, and a 2026 quantitative refinement by Curry claims a window bound of the form

\[
\#(\mathcal O\cap[a,a+X))\le C_\beta X^\beta\log(2X),\qquad \beta>\beta_*\approx0.9653844.
\]

If that refinement is used, the correction mass of a high dyadic band tends to zero like \(H^{\beta-1}\log H\). This is useful context, but the present structural lemma does not depend on it.

---

## 5. Exact-realizer reduction

For a length-\(L\) accelerated valuation word \(a_0,\ldots,a_{L-1}\) with total valuation

\[
A=\sum_{i<L}a_i,
\]

standard parity/valuation arithmetic determines the starting odd integer in one residue class modulo a power of two (in the exact realizer formalism, modulo \(2^{A+1}\) when terminal oddness is included).

Hence, if a final plateau lies in \([H,2H)\) and

\[
2^{A+1}>2H,
\]

then there is at most one positive representative of that realizer class inside the band. The actual plateau start is therefore the unique small positive realizer of its valuation word.

Since on the plateau

\[
A=\alpha L+O(1),
\]

a sufficient rough threshold is

\[
\boxed{L>\frac{\log_2 H+O(1)}{\log_2 3}.}
\]

Thus a final plateau only modestly longer than \(0.63093\log_2 H\) already turns into an exact **small-realizer problem for a bounded-drift, near-mechanical valuation word**.

This is precisely the arithmetic-placement / moving-anchor frontier emphasized in current exact-realizer approaches: abstract critical mechanical words are easy to write down, but proving that no fixed natural integer can keep realizing the required moving finite prefixes is the hard part.

---

## 6. Current reduction

A hypothetical unbounded least counterexample must therefore supply infinitely many dyadic layers whose final escape segment has all of the following properties:

1. it stays in one band \([H,2H)\) until the last step;
2. internally \(a_i=1+c_i\in\{1,2\}\) exactly;
3. the critical drift is uniformly two-sided bounded;
4. the final crossing is the forced defect \((c,b)=(1,0)\);
5. the next-layer entry is \(2\bmod3\);
6. if the segment length exceeds \(\approx(\log_2 H)/\log_2 3\), its start is an anomalously small exact realizer of that moving near-mechanical word.

So the proof problem can be sharpened to a dichotomy:

- **long final plateaus:** exclude anomalously small realizers of bounded-drift moving-anchor words;
- **short final plateaus:** exploit the forced repeated up-defects / record-entry residue structure.

The first branch matches the currently known moving-anchor obstruction. The second branch appears less developed and may be worth attacking separately.
