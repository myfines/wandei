# Sampled contraction density on a hypothetical unbounded Collatz tail

Status: derived necessary condition, not a proof of Collatz.

Work with the Terras map and sample an unbounded positive orbit at successive visits to residue 2 modulo 9. Existing formal results give a tail with no cumulative sampled coefficient contraction: if `T_j` is the elapsed Terras time and `Q_j` the number of odd steps from the chosen sampled-tail start to the j-th sampled return, then

\[
C_j:=\frac{3^{Q_j}}{2^{T_j}}\ge 1
\]

for every j. The same project also proves bounded ideal correction / reciprocal summability for unbounded positive orbits.

## 1. Bounded correction forces reciprocal sampled coefficients to be summable

For the direct sampled map, with `u_j=n_j+1/4`, each return satisfies

\[
u_{j+1}=c_j(u_j+d_j),\qquad d_j\in\{3/4,15/4,63/4\},
\]

where `c_j=C_{j+1}/C_j`. Hence

\[
\frac{u_J}{C_J}=u_0+\sum_{j<J}\frac{d_j}{C_j}.
\]

The ordinary Collatz correction bound implies `u_J/C_J` is bounded. Since every `d_j>=3/4`,

\[
\boxed{\sum_{j\ge0}\frac1{C_j}<\infty.}
\]

In particular `C_j -> infinity`.

## 2. Sampled criticality

López--Stoll prove that if a rational 2-adic integer has a non-cyclic trajectory, its parity density has lower limit exactly

\[
\alpha=\frac{\log 2}{\log 3}.
\]

At successive visits to 2 modulo 9, at most six even steps occur between samples. Since the sampled-noncontracting tail already has `Q_j/T_j >= alpha`, the global critical liminf forces a sampled subsequence with

\[
\frac{Q_j}{T_j}\to\alpha.
\]

On that subsequence, because `T_j-Q_j<=6j`,

\[
\frac{T_j}{j}\le \frac{6}{1-Q_j/T_j}\to \frac{6\log_2 3}{\log_2 3-1}.
\]

Define the sampled logarithmic excess

\[
H_j:=\log_2 C_j=Q_j\log_2 3-T_j.
\]

Then along the same subsequence

\[
\boxed{\frac{H_j}{j}\to0.}
\]

## 3. First-return coefficient gap

Every first-return block has at most six even steps. Exact finite classification gives

\[
c<1\implies \frac1{64}\le c\le\frac{243}{256},
\]

while

\[
c>1\implies c\ge\frac{2187}{2048}.
\]

Set

\[
\delta:=\log_2\frac{2187}{2048}=7\log_2 3-11
\approx0.0947375050481.
\]

If among the first j sampled blocks there are `K_j` contracting blocks, then every expanding block contributes at least `delta` to `H`, and every contracting block contributes at least `-6`. Thus

\[
H_j\ge \delta(j-K_j)-6K_j
=\delta j-(6+\delta)K_j.
\]

Therefore

\[
\frac{K_j}{j}\ge
\frac{\delta-H_j/j}{6+\delta}.
\]

Along the critical sampled subsequence,

\[
\boxed{
\limsup_{j\to\infty}\frac{K_j}{j}
\ge
\frac{\delta}{6+\delta}
=\frac{7\log_2 3-11}{7\log_2 3-5}
\approx0.01554414853.
}
\]

So any hypothetical unbounded rational orbit must have arbitrarily long sampled prefixes in which at least about 1.55% of all first-return blocks are coefficient-contracting.

Every coefficient-contracting first return from a seed above 2 is independently known to be an actual strict descent. Hence an unbounded counterexample tail must exhibit infinitely many strict sampled descents, with positive upper density along critical sampled prefixes, even though its cumulative sampled coefficient tends to infinity.

## 4. Exact finite list

A contracting first return has length at most 16. The script `src/sampled_return_contracting.py` exhausts all starts `n == 2 (mod 9)` modulo `2^16`; because 9 is invertible modulo `2^16`, this exactly covers every possible length-16 parity prefix. It finds exactly 34 contracting first-return words. Their coefficient range is exactly

\[
\frac1{64}\le c\le\frac{243}{256}.
\]

Consequently at least one fixed contracting first-return word must occur with positive upper frequency at least

\[
\frac{0.01554414853}{34}\approx4.57\times10^{-4}
\]

along some infinite subsequence of sampled prefixes.

## Next target

Exploit repeated occurrence of one fixed contracting affine return map. Each of the 34 maps has a fixed parity word, a fixed coefficient `3^q/2^t`, and one of the three sampled correction shifts. Repetition at positive upper density may be combined with:

- minimal sampled-counterexample altitude constraints;
- the three-digit sampled S-unit series;
- prime-support growth;
- or residue restrictions on the starting cylinders of the repeated contracting word.
