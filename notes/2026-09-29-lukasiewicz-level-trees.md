# Dyadic first-passage blocks as decorated Lukasiewicz trees — 2026-09-29

## Status

Exploratory structural lemma for a hypothetical least positive Collatz counterexample. This is not a proof of the Collatz conjecture.

Use the odd-only Syracuse map

\[
S(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1),
\]

and assume a least positive odd counterexample \(N\) with odd orbit \(x_0=N,x_1,\ldots\).

Define

\[
h_i=\log_2(x_i/N),\qquad m_i=\lfloor h_i\rfloor,
\]

\[
b_i=a(x_i)-1\ge0,
\]

and

\[
\omega=\log_2(3/2),\qquad
\varepsilon_i=\log_2\!\left(1+\frac1{3x_i}\right).
\]

The exact logarithmic increment is

\[
h_{i+1}-h_i=\omega-b_i+\varepsilon_i.
\]

Let

\[
C_n=\left\lfloor n\omega+\sum_{j<n}\varepsilon_j\right\rfloor,
\qquad
c_i=C_{i+1}-C_i.
\]

For a least counterexample \(N\gg1\), \(0<\omega+\varepsilon_i<1\), hence \(c_i\in\{0,1\}\). The exact integer-height equation is

\[
\boxed{m_{i+1}=m_i+c_i-b_i.}
\]

Because \(2\omega>1\), two consecutive zeros in \(c\) are impossible. For the verified-size regime the correction is tiny enough that \(3\omega+\varepsilon_i+\varepsilon_{i+1}+\varepsilon_{i+2}<2\), so three consecutive ones are also impossible. Thus the carry process is a small run-length-limited perturbation of the mechanical word of slope \(\omega\).

## 1. First passage through dyadic height levels

Suppose the orbit is unbounded. Let

\[
\tau_r=\min\{i:m_i=r\}
\]

for every reached level \(r\). Since the height can increase by at most one per step, \(\tau_r\) is well-defined for all sufficiently large \(r\), and the final transition into level \(r+1\) must have

\[
c_i=1,\qquad b_i=0,
\]

so its Syracuse exponent is \(a_i=1\).

For the block of transitions

\[
i=\tau_r,\ldots,\tau_{r+1}-1,
\]

first-passage means

\[
m_i\le r\quad(i<\tau_{r+1}),
\qquad
m_{\tau_{r+1}}=r+1.
\]

If the block has \(k\) odd-only steps and total exponent

\[
A=\sum a_i,
\]

then

\[
1<\frac{x_{\tau_{r+1}}}{x_{\tau_r}}<4,
\]

hence

\[
\boxed{0<k\log_2 3-A+E_r<2,}
\]

where

\[
E_r=\sum_{i=\tau_r}^{\tau_{r+1}-1}\varepsilon_i.
\]

So every dyadic level-up block is automatically near the critical line with error less than two. For an unbounded orbit, known reciprocal-summability results imply the tail correction tends to zero, so \(E_r\to0\).

## 2. Compression at carry times

List the indices inside the block where \(c_i=1\):

\[
i_1<i_2<\cdots<i_M=\tau_{r+1}-1.
\]

Group each carry together with the zero-carry transitions immediately preceding it. Since \(c\) has no consecutive zeros, every group contains one or two odd-only transitions.

Let

\[
S_j=\sum b_i
\]

within the \(j\)-th group. Define the height deficit from the current record level

\[
Q_j=r-m_{i_j+1}
\]

at group boundaries. The first-passage condition gives the exact partial-sum rule

\[
\sum_{j=1}^{s}(S_j-1)\ge0\qquad(1\le s<M),
\]

while the final crossing gives

\[
\sum_{j=1}^{M}(S_j-1)=-1.
\]

Therefore

\[
\boxed{(S_1,\ldots,S_M)\text{ is a Lukasiewicz word / rooted plane-tree degree sequence}.}
\]

Equivalently, every dyadic level-up excursion of an unbounded least counterexample canonically encodes a rooted ordered tree with vertex outdegrees \(S_j\).

The tree identity

\[
\sum_{j=1}^{M}S_j=M-1
\]

is just the first-passage identity

\[
\sum b_i=\sum c_i-1.
\]

Thus the near-critical drift is built directly into the tree: the average tree outdegree is exactly \(1-1/M\).

## 3. Light versus heavy vertices

This tree gives an intrinsic dichotomy.

### Light regime

If every original step in the block has

\[
b_i\in\{0,1\}
\]

(i.e. all Syracuse exponents are \(a_i\in\{1,2\}\)), define the binary carry word \(c\) on the block and replace its final forced crossing bit by zero, obtaining \(d\). Then

\[
|b|_1=|d|_1,
\]

and first passage implies for every proper prefix

\[
\sum b_i\ge\sum d_i.
\]

Hence \(b\) is obtained from \(d\) by repeatedly moving 1s to the left. In dominance/majorization language, \(b\) prefix-dominates \(d\).

Under the morphism from odd-only exponents to the ordinary Terras parity word,

\[
0\mapsto 1,\qquad 1\mapsto10,
\]

moving a 1 left in \(b\) delays later odd Terras steps. The elementary two-step identity

\[
F_1(F_2(x))=\frac{9x+7}{8},\qquad
F_2(F_1(x))=\frac{9x+5}{8}
\]

shows the resulting affine correction changes monotonically. This is the same ordering phenomenon captured by the unordered-majorization machinery of Rozier--Terracol and by the verified adjacent-swap identities in recent Lean work.

Ignoring the tiny \(+1\) correction, the carry word is mechanical with slope

\[
\omega=\log_2(3/2).
\]

The morphism \(0\mapsto1,1\mapsto10\) transforms its frequency to

\[
\frac1{1+\omega}=\frac1{\log_2 3}=\frac{\log2}{\log3},
\]

exactly the critical Collatz parity density. Thus the light first-passage block is an ordered perturbation of a critical-slope mechanical/Sturmian template.

### Heavy regime

If some step has

\[
b_i\ge2\qquad(a_i\ge3),
\]

then the side-branch lemma applies. With

\[
r_i=\left\lfloor\frac{a_i-1}{2}\right\rfloor,
\]

lowering the reverse exponent by \(2r_i\) produces another positive predecessor and least-counterexample minimality forces

\[
x_i\ge4^{r_i}N+\frac{4^{r_i}-1}{3}.
\]

So every heavy step carries a definite archimedean altitude cost and creates extra inverse-tree structure.

## 4. Proposed coverage program

The original vague dichotomy

- low word complexity versus high word complexity

can now be replaced by a more local and arithmetic dichotomy on every first-passage tree:

1. **light tree:** all \(b_i\le1\). Then the block is a majorized perturbation of a critical mechanical template; attack with adjacent-swap, Sturmian, finite-defect and correction-attainability tools;
2. **heavy tree:** some \(b_i\ge2\). Then use side-branch predecessors and altitude budgets; if heavy steps are frequent, try to force too many inverse ancestors or excessive height; if heavy steps are sparse, reduce back toward the light/finite-defect regime.

A successful theorem would show that neither type can occur for infinitely many successive dyadic first-passage blocks.

## 5. Current gap

The tree encoding itself is exact, but it does not yet bound the number of light majorization moves or prove that heavy side branches contradict minimality. The next useful target is quantitative:

\[
\boxed{\text{large light-majorization distance}\ \text{or many heavy vertices}\ \Longrightarrow\ \text{forbidden height / reverse ancestor}.}
\]

This is the concrete bridge still missing.
