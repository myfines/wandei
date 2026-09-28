# Short dyadic plateaus reduce to finitely many mechanical defects — 2026-09-29

## Status

Structural reduction for a hypothetical unbounded least positive counterexample. This is **not** a proof of Collatz.

Continue the notation of `2026-09-29-final-dyadic-plateau.md`.

Let a final dyadic plateau lie in

\[
H\le x_i<2H
\]

and have accelerated length \(L\). Internally, the exact plateau rigidity gives

\[
a_i=1+c_i,\qquad c_i\in\{0,1\}.
\]

Write

\[
\omega=\log_2(3/2),
\qquad
\theta_0=\log_2(x_0/H),
\]

and

\[
E_j=\sum_{i<j}\log_2\left(1+\frac1{3x_i}\right).
\]

Then the cumulative true carry is

\[
C_j=\lfloor\theta_0+j\omega+E_j\rfloor,
\]

while the fixed-intercept mechanical carry is

\[
D_j=\lfloor\theta_0+j\omega\rfloor.
\]

---

## 1. The perturbation is exponentially small when `L = O(log H)`

Since every plateau state is at least \(H\),

\[
0<E_L
\le
L\log_2\left(1+\frac1{3H}\right)
<
\frac{L}{3H\ln2}.
\]

Hence if

\[
L\le C_0\log H,
\]

then \(E_L\) is exponentially small as a function of \(L\).

---

## 2. Sensitive carry indices

Because \(0\le E_j\le E_L<1\) for high enough \(H\),

\[
C_j-D_j\in\{0,1\}.
\]

The two cumulative carries can differ only if

\[
\{\theta_0+j\omega\}\in[1-E_L,1).
\]

Call such a \(j\) sensitive.

If two distinct indices \(j,k\le L\) are sensitive, then subtraction gives

\[
\boxed{\|(j-k)\omega\|<2E_L.}
\]

Now

\[
\omega=\frac{\log3}{\log2}-1.
\]

Standard effective lower bounds for nonzero integer linear forms in \(\log2\) and \(\log3\) imply the existence of constants \(c,B>0\) such that, for all sufficiently large integers \(q\),

\[
\|q\omega\|\ge c q^{-B}.
\]

(Strong explicit irrationality-measure results for combinations of \(\log2\) and \(\log3\) are known; only the existence of some effective polynomial bound is needed here.)

Since \(E_L\) is exponentially small in \(L\) while the lower bound above is only polynomially small, for every fixed \(C_0\) there is a height threshold after which a plateau with

\[
L\le C_0\log H
\]

has **at most one sensitive cumulative-carry index**.

---

## 3. Digit-level consequence

Set

\[
d_i=D_{i+1}-D_i,
\qquad
c_i=C_{i+1}-C_i.
\]

Let

\[
q_j=C_j-D_j\in\{0,1\}.
\]

Then

\[
c_i-d_i=q_{i+1}-q_i.
\]

If at most one cumulative index has \(q_j=1\), the digit words can differ only locally.

For an interior sensitive index, the only possible change is

\[
\boxed{01\longrightarrow10,}
\]

that is, the positive correction advances one mechanical carry by one position.

If the sole sensitivity occurs at an endpoint, there is only one one-bit boundary change.

Therefore, on every sufficiently high short plateau,

\[
\boxed{
\text{true carry word}
=
\text{fixed-intercept mechanical word}
+
\text{at most one adjacent }01\to10\text{ transposition}.
}
\]

Because the internal accelerated valuation digit is \(a_i=1+c_i\), the same statement holds for the internal valuation word after the obvious relabeling \(0\mapsto1\), \(1\mapsto2\).

The final dyadic crossing contributes one additional forced defect:

\[
(c,b)=(1,0),
\]

so the actual extra-valuation word differs from the carry template by one final `1 -> 0` deletion at the crossing.

---

## 4. Relation to ordinary Terras parity

An accelerated valuation digit maps to the ordinary shortcut/Terras parity block as

\[
a=1\mapsto 1,
\qquad
a=2\mapsto10.
\]

Thus the morphism on carry digits is

\[
0\mapsto1,
\qquad
1\mapsto10.
\]

Its incidence matrix has determinant \(-1\), and it is a standard Sturmian morphism. Hence a pure fixed-intercept critical mechanical carry word maps to a Sturmian ordinary parity word of density

\[
\frac1{1+\omega}
=
\frac1{\log_2 3}
=
\frac{\log2}{\log3},
\]

exactly the classical critical odd-density threshold.

A single carry transposition produces only a constant number of ordinary-parity bit edits inside the corresponding local block.

So high short plateaus lie in a **constant-defect critical Sturmian family**.

---

## 5. Why the existing generic finite-defect return theorem does not immediately close the problem

There are formal finite-defect theorems showing that sufficiently few `q`-shift parity disagreements over a sufficiently long interval force an exact return. However, their generic checkpoint horizon grows exponentially in the permitted defect count, while a Sturmian word has a small but nonzero density of `q`-shift disagreements unless one works on a carefully chosen convergent scale.

A first attempt to combine those bounds does not automatically yield a uniform `L <= C log H` theorem for all continued-fraction geometries. In particular, for bounded partial quotients the available near-periodic window and the generic checkpoint horizon can be of comparable size in the wrong direction.

So the reduction is useful, but the final step needs either:

1. a sharper return theorem specialized to Sturmian/mechanical templates; or
2. a direct moving-anchor realizer lower bound; or
3. a continued-fraction-scale argument that exploits the exact plateau boundary conditions, not merely generic shift disagreements.

This negative check is important: the plateau reduction is stronger than generic finite-defect control, but current generic defect certificates do not yet finish the short-plateau branch.
