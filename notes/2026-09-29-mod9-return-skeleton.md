# Exact mod-9 first-return language for the Terras map

Status: exact finite-state reduction. This supersedes the earlier 36-state / 82-skeleton presentation in the first version of this note. That larger state space was valid as an over-refinement but obscured a much simpler direct mod-9 classification.

Use the Terras map

\[
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

Write `E` for an even step and `O` for an odd step. Modulo 9, division by 2 is multiplication by 5, so the two symbolic transitions are

\[
E(r)=5r\pmod 9,
\qquad
O(r)=5(3r+1)\pmod 9.
\]

Starting from residue 2, and stopping at the first positive return to residue 2, only the residues

\[
2,1,5,7,8,4
\]

are reachable. Their transitions are

\[
\begin{array}{c|cc}
r&E&O\\\hline
2&1&8\\
1&5&2\\
5&7&8\\
7&8&2\\
8&4&8\\
4&2&2
\end{array}
\]

Thus the only non-return cycle is the odd self-loop

\[
8\xrightarrow{O}8.
\]

## Complete first-return language

Every first-return parity word from `2 mod 9` to `2 mod 9`, with no intermediate return, is exactly one of the following eight template types:

\[
\boxed{EO},
\]

\[
\boxed{EEEO},
\]

and, for `m\ge0`,

\[
\boxed{O^{m+1}EE},\qquad
\boxed{O^{m+1}EO},
\]

\[
\boxed{EE\,O^{m+1}EE},\qquad
\boxed{EE\,O^{m+1}EO},
\]

\[
\boxed{EEEE\,O^mEE},\qquad
\boxed{EEEE\,O^mEO}.
\]

So an arbitrarily long first return has only one source of unbounded length: one consecutive odd run while the mod-9 state is trapped at 8.

Every finite parity word is realized by one residue class modulo the relevant power of 2; since powers of 2 are coprime to 9, the Chinese remainder theorem is compatible with the initial condition `n=2 mod 9`. Thus these symbolic templates genuinely occur for suitable integers.

## Unified affine form

The six parametric families can be written

\[
E^e O^r E Q,
\]

with

\[
e\in\{0,2,4\},\qquad Q\in\{E,O\},
\]

where `r\ge1` for `e=0,2` and `r\ge0` for `e=4`.

Let

\[
q=\begin{cases}
r,&Q=E,\\
r+1,&Q=O,
\end{cases}
\qquad
t=e+r+2.
\]

Then the exact affine identity is

\[
\boxed{
T^t(n)=
\frac{3^q n+2^e(3^q-2^r)}{2^t}.
}
\]

Because the `O^r` run is followed by an even step, there is an odd integer `s` such that

\[
\boxed{n+2^e=2^{e+r}s.}
\]

In this parameter the endpoint collapses to

\[
\boxed{
T^t(n)=\frac{3^q s-1}{4}.
}
\]

Equivalently, with the principal multiplicative coefficient

\[
c=\frac{3^q}{2^t},
\]

one has the shifted multiplicative identity

\[
\boxed{
T^t(n)+\frac14
=
c\,(n+2^e).
}
\]

This finite-shift form is useful: all six infinite first-return families use only the three input shifts `1,4,16`, while the output shift is always `1/4`.

## Contracting versus noncontracting first returns

The two exceptional fixed words are always coefficient-contracting:

\[
EO:\quad \frac34<1,
\qquad
EEEO:\quad \frac3{16}<1.
\]

For the six parametric families, coefficient noncontraction `3^q>2^t` is equivalent to the following sharp integer thresholds:

\[
\begin{array}{c|cc}
e&Q=E&Q=O\\\hline
0&r\ge4&r\ge1\\
2&r\ge7&r\ge5\\
4&r\ge11&r\ge8
\end{array}
\]

There is no equality case because powers of 2 and 3 cannot agree nontrivially.

Combined with the independently Lean-verified theorem `contracting_two_mod_nine_segment_descends`, this means any coefficient-contracting first return from a seed above 2 strictly descends, while every noncontracting first return lies in one of the six explicit threshold families above.

## Long odd-run transfer

The odd self-loop occurs at residue 8. If a loop-state value `y=8 mod 9` remains odd for `m` successive Terras steps, then

\[
2^m\mid y+1,
\qquad
T^m(y)+1=\left(\frac32\right)^m(y+1).
\]

Since also `9\mid y+1`,

\[
\boxed{9\cdot2^m\mid y+1}
\]

and consequently

\[
\boxed{T^m(y)\equiv-1\pmod{3^{m+2}}.}
\]

Thus a long first-return excursion transfers high 2-adic divisibility of `y+1` into high 3-adic divisibility of a later state plus one.

## Current use

The sampled-noncontracting-tail theorem reduces any hypothetical unbounded positive orbit to a tail based at `2 mod 9` whose cumulative sampled coefficients never contract. The classification above says that every first-return block on such a tail comes from only eight templates, with all unbounded combinatorial freedom concentrated in one integer run-length parameter.

The next useful target is therefore not another large residue automaton. It is the induced affine dynamics of the six noncontracting parametric families, especially how sparse long odd runs interact with the critical-density condition and with the 2-adic/3-adic divisibility transfer.