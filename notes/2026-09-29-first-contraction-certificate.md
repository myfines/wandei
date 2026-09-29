# First coefficient-contraction certificate

Status: partial result / research note only. This does **not** prove the Collatz conjecture.

We work with the odd-only map

\[
S(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1).
\]

For a fixed prefix of `k` odd-only steps, let

\[
A_j=\sum_{i<j}a_i,
\]

and write

\[
x_k=\frac{3^kN+C_k}{2^{A_k}},\qquad
C_k=\sum_{j=0}^{k-1}3^{k-1-j}2^{A_j}.
\]

Assume `N` is a least positive counterexample and `k` is the **first** time the multiplicative coefficient contracts:

\[
3^k<2^{A_k},
\]

while for every `j<k`,

\[
3^j\ge2^{A_j}.
\]

Since every orbit state of a least counterexample is at least `N`,

\[
2^{A_k}N\le 3^kN+C_k,
\]

hence

\[
N\le \frac{C_k}{2^{A_k}-3^k}.
\]

## Diophantine window

Before the first contraction,

\[
A_j\le\lfloor j\log_2 3\rfloor.
\]

The crude bound `C_k <= k 3^{k-1}` gives

\[
\frac{A_k}{k}-\log_2 3
\le \frac{1}{3N\log 2}.
\]

Using the live Barina verification floor

\[
N\ge 2075\cdot 2^{60},
\]

this window has width less than

\[
2.010182294061\times10^{-22}.
\]

Continued-fraction/Farey data around `log_2 3` isolate the first candidate

\[
(A,k)=(114208327604,72057431991).
\]

The next relevant upper Farey point below the next convergent-denominator threshold is farther from `log_2 3` than the certified window. The next convergent denominator is

\[
137528045312.
\]

The exact inequalities are checked in `src/first_contraction_cert.py` using rational logarithm intervals.

## Mechanical correction envelope

For the candidate prefix, first-contraction minimality gives

\[
C_k
\le
3^{k-1}\sum_{j=0}^{k-1}2^{-\{j\log_2 3\}}.
\]

Let

\[
f(t)=2^{-t}\quad (t\in\mathbb R/\mathbb Z).
\]

Its circle variation is `1` and

\[
\int_0^1f(t)\,dt=\frac{1}{2\log2}.
\]

Here

\[
k=65470613321+6586818670,
\]

a sum of two adjacent convergent denominators. Splitting the orbit sum into these two blocks and applying Denjoy--Koksma to each gives

\[
\sum_{j<k}f(\{j\log_2 3\})
\le
\frac{k}{2\log2}+2.
\]

Write

\[
D=A\log2-k\log3>0.
\]

Then

\[
2^A-3^k=3^k(e^D-1),
\]

so, using `e^D-1 >= D`,

\[
N
\le
\frac{k/(2\log2)+2}{3D}.
\]

The rational certificate proves the clean bound

\[
\boxed{N<\frac43\,2^{71}}.
\]

A high-precision evaluation of the sharper expression is about

\[
\log_2N<71.413083842,
\]

but the committed certificate deliberately uses the cleaner rational inequality above.

## Consequence / current dichotomy

With the live verified floor, any hypothetical least counterexample whose first coefficient contraction lies in this early Diophantine window must lie in the narrow interval

\[
2075\cdot2^{60}
\le N
<\frac43\,2^{71}.
\]

The ratio between the clean upper endpoint and the live lower endpoint is

\[
\frac{8192}{6225}\approx1.315984.
\]

If this early candidate is excluded, the next continued-fraction scale begins at odd-only length

\[
137528045312.
\]

The separate branch in which the multiplicative coefficient never contracts is **not** addressed by this certificate. That branch remains a 2-adic/rationality and moving-anchor problem.
