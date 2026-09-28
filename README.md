# wandei — Collatz reverse-barrier experiments

Exploratory work on the Collatz / Syracuse conjecture.

**Status:** research notes and computational experiments only. There is no claimed proof.

## Current attack

Use the odd-only Syracuse map

\[
S(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
\]

Assume, for contradiction, that a smallest positive counterexample \(N\) exists.
If \(x\) is any point on the odd-only orbit of \(N\), then every positive odd
reverse ancestor \(y\) with \(S^k(y)=x\) is also a counterexample. Therefore

\[
y\ge N.
\]

For a valid reverse exponent word \(a_1,\ldots,a_k\),

\[
y_k=\frac{2^A x-C_k}{3^k},
\qquad
A=\sum_{j=1}^k a_j,\quad C_k>0.
\]

Hence a necessary condition for a point \(x\) on the orbit of a minimal
counterexample is

\[
\frac{x}{N}>\frac{3^k}{2^A}.
\]

The project studies whether the collection of these reverse barriers, combined
with forward \(2\)-adic constraints, can make an infinite counterexample orbit
impossible.

## First exact result: minimum-exponent reverse chain

For an actual positive odd \(x\not\equiv0\pmod3\), the smallest odd reverse step is

\[
R_{\min}(x)=
\begin{cases}
(2x-1)/3,&x\equiv2\pmod3,\\
(4x-1)/3,&x\equiv1\pmod3.
\end{cases}
\]

The corresponding reverse exponent is \(a=1\) or \(a=2\).
If a reverse state becomes \(0\pmod3\), the chain terminates because that state
has no odd preimage under \(S\).

For residue classes modulo \(3^m\):

- every word in \(\{1,2\}^m\) occurs for exactly one residue class modulo \(3^m\);
- therefore exactly \(2^m\) unit residue classes survive \(m\) minimum-exponent
  reverse steps;
- there are \(2\cdot3^{m-1}\) units modulo \(3^m\), so the surviving fraction is

\[
\frac{2^m}{2\cdot3^{m-1}}=
\left(\frac23\right)^{m-1}.
\]

A short proof is in [`notes/2026-09-28.md`](notes/2026-09-28.md).

The extremal word \(1,1,\ldots,1\) corresponds to

\[
x\equiv -1\pmod{3^m}
\]

and yields the barrier

\[
\frac{x}{N}>\left(\frac32\right)^m.
\]

## Code

Run:

```bash
python src/reverse_barrier.py --max-m 10
```

Tests:

```bash
python -m pytest -q
```

The current test suite checks the residue/word bijection, termination at a
multiple of 3, and the exact \(2^m\) count for small \(m\).

## Next target

The minimum-exponent branch is only a baseline. A state has infinitely many
reverse preimages because a valid exponent can be increased by any even amount.

However, a reverse path of depth \(k\) can only produce a barrier greater than
1 if

\[
A<k\log_2 3.
\]

Since \(A\) is an integer, the set of potentially contracting reverse exponent
words at any fixed depth \(k\) is finite. This gives an exact search strategy
with no arbitrary exponent cutoff:

1. enumerate all valid reverse words with total exponent
   \(A<k\log_2 3\);
2. solve their congruence classes modulo \(3^k\);
3. compute the strongest reverse barrier for each residue/state;
4. combine that barrier with the forward Syracuse transition and its
   \(2\)-adic exponent constraints;
5. search for an infinite admissible state path.

The hoped-for contradiction would be: every infinite forward path eventually
enters a state whose reverse barrier exceeds its available height above \(N\).

## Important caveat

Finite computation by itself will not prove Collatz unless the computation is
turned into a finite certificate or a general theorem covering all depths.
The repository is intended to make that distinction explicit.
