# Early-defect repayment inside the first contraction candidate

Status: exact consequence of the first-candidate window and the 46-step mechanical-prefix exclusion. Not a Collatz proof.

Let

\[
L=\log_2 3,\qquad
h_n=\lfloor nL\rfloor-A_n,
\]

for the odd-only exponent sums \(A_n=\sum_{i<n}a_i\).

Assume a least counterexample lies in the first coefficient-contraction candidate

\[
(k,A_k)=(72057431991,114208327604).
\]

Before the first contraction,

\[
h_n\ge0\qquad(0\le n<k),
\]

while for this candidate

\[
A_k=\lfloor kL\rfloor+1,
\qquad
\boxed{h_k=-1}.
\]

## 1. A defect must already exist by time 46

The exact 46-step cylinder computation in
`2026-10-01-first-window-mechanical-prefix.md` excludes the pure mechanical
prefix

\[
a_j=\lfloor(j+1)L\rfloor-\lfloor jL\rfloor
\quad(0\le j<46).
\]

For a path satisfying \(h_n\ge0\), starting from \(h_0=0\), equality
\(h_n=0\) for every \(n\le46\) forces exactly that mechanical prefix.
Therefore every first-candidate survivor satisfies

\[
\boxed{\max_{1\le n\le46}h_n\ge1.}
\]

Equivalently, at least one positive critical defect is created in the first
46 odd steps.

## 2. Every early defect must later be repaid

Since \(h_k=-1\) but \(h_n\ge0\) for every \(n<k\), define

\[
\tau=\max\{n<k:h_n>0\}.
\]

This set is nonempty by the previous section. Necessarily

\[
h_{\tau}>0,\qquad h_{\tau+1}=0.
\]

Thus the first-candidate path contains an exact positive-to-zero repayment
before the terminal crossing. After that last repayment,

\[
h_n=0\qquad(\tau+1\le n<k),
\]

because \(\tau\) was the last positive time and negative values are forbidden
before the first contraction.

Hence the suffix from \(\tau+1\) through \(k-1\) is forced to be the
critical mechanical word:

\[
\boxed{
a_n=\lfloor(n+1)L\rfloor-\lfloor nL\rfloor
\quad(\tau+1\le n<k-1).
}
\]

At the terminal step the candidate crosses from \(h_{k-1}=0\) to \(h_k=-1\).

So every survivor has the structural form

\[
\boxed{
\text{early defect creation}
\;\longrightarrow\;
\text{last repayment to }h=0
\;\longrightarrow\;
\text{pure mechanical suffix}
\;\longrightarrow\;
\text{first contraction}.
}
\]

## 3. Why this is useful

The previous 46-step calculation only excluded a mechanical prefix. The lemma
above converts that local exclusion into a global obligation: a survivor must
leave the critical boundary and later hit it again.

The next exact target is therefore not to enumerate all length-(k) exponent
words. It is enough to study possible **last returns to the boundary**
\(h=0\). For each candidate return time \(m=\tau+1\), the entire suffix
from \(m\) to the first-contraction endpoint is fixed by irrational rotation.
The remaining freedom is confined to the prefix ending at \(m\).

A future certificate can attack these return cylinders by combining:

1. the unique 2-adic seed class determined by the fixed mechanical suffix;
2. the narrow first-candidate height interval;
3. minimal-counterexample non-descent along the prefix.

This is a substantial reduction of the symbolic search space, but it does not
yet exclude all possible return times \(m\).
