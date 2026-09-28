# Contracting reverse-tree checkpoint — 2026-09-28

This checkpoint extends the minimum-exponent reverse experiment to **all**
reverse exponent words that can strictly reduce numerical size.

## Exact finite search at fixed depth

For a valid depth-\(k\) reverse word \(a_1,\ldots,a_k\),

\[
y=\frac{2^A x-C}{3^k},
\qquad A=\sum_i a_i,\quad C>0.
\]

If

\[
\frac{3^k}{2^A}>1,
\]

then \(y<x\) for every positive \(x\) in the residue class for which that word
is valid. The condition is equivalent to

\[
A<k\log_2 3.
\]

At a fixed depth \(k\), this bounds \(A\), so there are only finitely many
positive-integer exponent words to inspect. This is important: the enumeration
does **not** need an arbitrary maximum exponent.

Every fixed exponent word has a unique validity class modulo \(3^k\). For

\[
C_0=0,\qquad C_{j+1}=2^{a_{j+1}}C_j+3^j,
\]

the class is

\[
x\equiv C_k\,2^{-A}\pmod{3^k}.
\]

`src/contracting_tree.py` enumerates all such contracting words.

## Results through depth 12

```text
depth,contracting_words,contracting_residues,survivors,survivor_fraction
1,1,1,1,1/2
2,3,3,2,1/3
3,4,4,6,1/3
4,15,11,17,17/54
5,21,16,51,17/54
6,84,57,151,151/486
7,330,206,445,445/1458
8,495,325,1335,445/1458
9,2002,1215,3977,3977/13122
10,3003,1915,11931,3977/13122
11,12376,7317,35669,35669/118098
12,50388,27469,106405,106405/354294
```

Here a **survivor** modulo \(3^k\) is a unit residue class that admits no
strictly size-contracting reverse path of any depth \(j\le k\).

Small positive representatives that still survive through depth 12 begin

```text
1, 7, 16, 19, 25, 28, 34, 37, 43, 46, 52, 55, 61, ...
```

In particular, the reverse-barrier condition alone does not eliminate all
positive-looking residue representatives. This kills the overly optimistic
idea that one might prove Collatz merely by showing that every state has a
smaller reverse ancestor.

## Interpretation

This is a useful negative result.

The minimal-counterexample argument supplies two different kinds of hard
constraints:

1. **Forward floor:** every point \(x_i\) on the orbit must satisfy
   \(x_i\ge N\).
2. **Reverse barrier:** every positive reverse ancestor of every \(x_i\) must
   also satisfy \(y\ge N\).

The second condition alone leaves a large survivor set. Therefore the next
model must couple reverse barriers to the actual **forward height**

\[
h_i=\log(x_i/N)
\]

and the forward exponent sequence

\[
a_i=v_2(3x_{i-1}+1).
\]

A residue can be harmless when \(x_i\) is high above \(N\), but forbidden when
the same residue occurs close to the floor.

## Next proposed state graph

For a modulus depth \(m\), attach to each \(3\)-adic residue a reverse barrier

\[
B_m(r)=\max \frac{3^k}{2^A}
\]

over all valid potentially contracting reverse words visible to depth \(m\).

A minimal-counterexample orbit must then obey

\[
x_i/N \ge B_m(x_i\bmod 3^m)
\]

(up to the stronger exact additive \(C/N\) term).

The forward map updates height by

\[
\log\frac{x_{i+1}}{N}
=
\log\frac{x_i}{N}
+\log 3-a_{i+1}\log2
+\log\left(1+\frac1{3x_i}\right).
\]

The remaining research question is whether the coupled system

\[
(\text{height},\;3\text{-adic residue},\;2\text{-adic forward exponent})
\]

admits an infinite path.

A computational contradiction would only become a proof if it can be turned
into a finite invariant/certificate or a theorem valid at all depths.
