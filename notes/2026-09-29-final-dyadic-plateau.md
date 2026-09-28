# Final dyadic plateau rigidity — corrected 2026-09-29

## Status

Structural lemma for a hypothetical unbounded least positive counterexample to the accelerated odd-only Collatz map. This is **not** a proof of the conjecture.

Let

\[
T(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1),
\]

and suppose \(N\) is the least positive counterexample. Write its odd-only orbit as \(x_i\), and define

\[
h_i=\log_2(x_i/N),\qquad m_i=\lfloor h_i\rfloor,
\]

\[
b_i=a_i-1,\qquad \omega=\log_2(3/2),
\]

\[
\varepsilon_i=\log_2\left(1+\frac1{3x_i}\right)>0.
\]

Then exactly

\[
h_{i+1}=h_i+\omega-b_i+\varepsilon_i.
\]

With

\[
c_i=\lfloor\{h_i\}+\omega+\varepsilon_i\rfloor\in\{0,1\},
\]

we get the exact integer-height equation

\[
\boxed{m_{i+1}=m_i+c_i-b_i.}
\]

Since \(b_i\ge0\), a single step can raise the dyadic layer index by at most one.

---

## 1. The final contiguous plateau in one dyadic layer

Fix a sufficiently high layer \(r\), with band

\[
H\le x<2H,\qquad H=2^rN.
\]

Because a nonperiodic divergent orbit eventually leaves every bounded set, layer \(r\) has a **last visit**. Let the final \(r\)-plateau be the maximal contiguous block of states in layer \(r\) ending at that last visit. Its last step exits upward to layer \(r+1\); otherwise, if it exited downward, the orbit would later have to revisit layer \(r\) before escaping above it, contradicting finality.

For every internal plateau step,

\[
m_{i+1}-m_i=0,
\]

so

\[
\boxed{b_i=c_i.}
\]

Hence internally

\[
\boxed{a_i=1+c_i\in\{1,2\}.}
\]

For the final crossing,

\[
m_{i+1}-m_i=1.
\]

Since \(c_i\le1\) and \(b_i\ge0\), this forces

\[
\boxed{c_i=1,\quad b_i=0,\quad a_i=1.}
\]

Thus the **exit** of every final plateau is rigid.

---

## 2. Correct entry dichotomy

The earlier version of this note incorrectly claimed that the plateau entry must also come from below. That is not always true: the orbit may have visited a higher layer and later dropped back into layer \(r\) before its final escape.

The correct entry classification is:

### Light entry: from below

If the state immediately before the plateau lies in a lower layer, then the layer index must increase by exactly one (upward jumps larger than one are impossible), so

\[
\boxed{c=1,\ b=0,\ a=1.}
\]

This is the same up-defect as the final exit.

### Heavy entry: from above

If the plateau is entered from a higher layer, then the entering step has

\[
m_{i+1}-m_i\le-1.
\]

From \(m_{i+1}-m_i=c-b\) and \(c\le1\), this requires a positive excess valuation \(b\), often large when several layers are crossed downward.

Such a step is exactly where the earlier side-branch lemma becomes useful. If \(a=b+1\) and

\[
r'=\left\lfloor\frac{a-1}{2}\right\rfloor,
\]

then the existence of lowered reverse exponents gives

\[
\boxed{x\ge4^{r'}N+\frac{4^{r'}-1}{3}.}
\]

So entry from above carries an explicit altitude/side-branch cost.

This yields a clean local coverage split:

\[
\boxed{
\text{final plateau entry}
=\text{light up-defect from below}
\quad\text{or}\quad
\text{heavy side-branch event from above}.
}
\]

---

## 3. Residue and geometry of the rigid upward exit

At every upward dyadic crossing we have \(a_i=1\), hence

\[
x_{i+1}=\frac{3x_i+1}{2}.
\]

The reverse formula

\[
x_i=\frac{2x_{i+1}-1}{3}
\]

forces

\[
\boxed{x_{i+1}\equiv2\pmod3.}
\]

If the current band is \([H,2H)\), crossing upward also forces

\[
x_i\ge\frac{4H-1}{3}
\]

and

\[
2H\le x_{i+1}<3H+\frac12.
\]

So every rigid upward exit occurs from the top third of the current dyadic band, and its target lies in the lower \(3/2\)-portion of the next band.

---

## 4. Two-sided bounded drift on the plateau

Let the plateau begin at \(x_s\in[H,2H)\), and put

\[
\theta_0=\log_2(x_s/H)\in[0,1).
\]

For an internal prefix of length \(j\), define

\[
E_j=\sum_{q<j}\varepsilon_{s+q}.
\]

Because \(b=c\) internally,

\[
B_j:=\sum_{q<j}b_{s+q}
=\left\lfloor\theta_0+j\omega+E_j\right\rfloor.
\]

The total valuation is \(S_j=j+B_j\). With

\[
\alpha=\log_2 3=1+\omega,
\]

we obtain

\[
R_j:=S_j-\alpha j
=\theta_0+E_j-\{\theta_0+j\omega+E_j\}.
\]

Hence every proper internal prefix satisfies

\[
\boxed{-1<R_j<1+E_j.}
\]

Including the final forced crossing removes one expected extra-valuation unit, yielding

\[
\boxed{-2<R_L<E_L.}
\]

So every final plateau is a finite two-sided bounded-drift valuation word.

---

## 5. Correction bound and short-plateau rigidity

Every plateau state is at least \(H\), hence

\[
0<E_L<\frac{L}{3H\ln2}.
\]

If \(L=O(\log H)\), this perturbation is exponentially small as a function of \(L\). Comparing

\[
C_j=\lfloor\theta_0+j\omega+E_j\rfloor
\]

with the fixed-intercept mechanical carries

\[
D_j=\lfloor\theta_0+j\omega\rfloor
\]

shows that two distinct sensitive indices would imply

\[
\|(j-k)\omega\|<2E_L.
\]

Any effective lower bound for nonzero integer linear forms in \(\log2\) and \(\log3\) is polynomial in \(|j-k|\), while \(E_L\) is exponentially small. Thus sufficiently high short plateaus have at most one carry-sensitive index.

Consequently their internal valuation word is a fixed-intercept critical mechanical word plus at most one local adjacent carry transposition `01 -> 10`, while the final upward crossing contributes one additional forced defect.

---

## 6. Exact-realizer reduction for long plateaus

For a length-\(L\) valuation word \(a_0,\ldots,a_{L-1}\), with

\[
A=\sum a_i,
\]

the affine identity is

\[
3^Lx+C=2^Ay.
\]

Requiring the terminal accelerated state \(y\) to be odd pins the starting odd integer to one residue class modulo

\[
2^{A+1}.
\]

For plateau words, \(A=\alpha L+O(1)\). Hence once

\[
2^{A+1}>2H,
\]

or roughly

\[
L>\frac{\log_2H+O(1)}{\log_2 3},
\]

there is at most one positive representative of that exact-realizer class inside \([H,2H)\).

Thus the plateau problem splits into:

- **long plateaus:** a moving-anchor small-realizer problem for two-sided bounded-drift words;
- **short plateaus:** a constant-defect critical mechanical/Sturmian problem;
- **entry from above:** a heavy side-branch event with an explicit altitude cost.

This corrected trichotomy is the current useful structural reduction.