# Prime-factor / Dirichlet-character bridge — 2026-09-28

## Status

This is a structural bridge, not a proof of Collatz.

A naive reduction "prove Collatz for every prime, therefore every composite follows" is invalid because Collatz convergence is not multiplicative. The useful multiplicative structure is instead carried by Dirichlet characters of the odd state.

## 1. Deep halving is a residue condition

For odd `x`, let

\[
a(x)=v_2(3x+1).
\]

Then

\[
a(x)\ge k
\iff
3x+1\equiv0\pmod{2^k}
\iff
x\equiv -3^{-1}\pmod{2^k}.
\]

If

\[
x=\prod p_i^{e_i},
\]

then this condition is genuinely multiplicative at the residue level:

\[
\prod p_i^{e_i}\equiv -3^{-1}\pmod{2^k}.
\]

For any Dirichlet character `chi` modulo `2^k`,

\[
\chi(x)=\prod_i \chi(p_i)^{e_i}.
\]

So prime factors can encode exactly the finite-state information controlling future halving depth, even though their individual Collatz trajectories do not combine multiplicatively.

## 2. Exact mod-8 character identity

For odd `x`,

\[
a(x)\ge3\iff x\equiv5\pmod8.
\]

Let `chi_-4`, `chi_8`, and `chi_-8=chi_-4 chi_8` be the three nonprincipal real Dirichlet characters modulo 8. Then for odd `x`,

\[
\mathbf 1_{x\equiv5\;(8)}
=
\frac14\left(1+\chi_{-4}(x)-\chi_8(x)-\chi_{-8}(x)\right).
\]

## 3. Low-altitude character-bias lemma

Assume `N` is a least positive counterexample. The side-branch lemma already proved in this repository implies

\[
N\le x\le4N
\Longrightarrow
v_2(3x+1)\le2.
\]

Hence every low-altitude odd orbit state avoids `5 mod 8`.

For a finite set `L` of odd orbit states with `N <= x <= 4N`, summing the exact indicator identity gives

\[
0
=
|L|
+
\sum_{x\in L}\chi_{-4}(x)
-
\sum_{x\in L}\chi_8(x)
-
\sum_{x\in L}\chi_{-8}(x).
\]

Therefore, by the triangle inequality,

\[
\boxed{
\max_{\chi\in\{\chi_{-4},\chi_8,\chi_{-8}\}}
\left|\sum_{x\in L}\chi(x)\right|
\ge \frac{|L|}{3}.
}
\]

So any least-counterexample orbit that spends substantial time below `4N` must exhibit a macroscopic multiplicative-character bias.

This is a rigorous bridge between:

- low-altitude occupation;
- the side-branch obstruction;
- multiplicative prime-factor residue data.

## 4. Quantitative link to the correction identity

For a Terras prefix with `q` odd states and drift debt

\[
D=t\log2-q\log3>0,
\]

exact factorization of the affine correction gives

\[
D
\le
\sum_{\text{odd }i}
\log\left(1+\frac{1}{3x_i}\right).
\]

Let `r` of those `q` odd states lie in `[N,4N]`. Since every orbit state is at least `N`,

\[
D
<
\frac{r}{3N}
+
\frac{q-r}{12N}.
\]

Thus

\[
\boxed{
\frac rq
>
4N\frac{D}{q}-\frac13.
}
\]

At the first continued-fraction candidate currently recorded in this repository,

\[
(q,t)=(72057431991,114208327604),
\]

and using only `N >= 2^71`, the right-hand side is approximately `0.38899`.

So if that earliest candidate were realized by a least counterexample, roughly 39% of its odd states would have to lie in `[N,4N]`. The character-bias lemma would then force at least one nonprincipal mod-8 character sum over those low states to have magnitude at least about 13% of the total odd-state count.

The decimal is only an illustration; the inequality itself is exact.

## 5. Analytic-number-theory target

The next possible bridge is a twisted transfer operator. For a nonprincipal Dirichlet character `chi`, study a backward operator schematically of the form

\[
(\mathcal L_\chi f)(n)
=
\sum_{m:S(m)=n} w(m,n)\chi(m)f(m).
\]

A spectral gap separating nonprincipal character modes from the principal mode could imply cancellation of

\[
\sum_{x_i\in L}\chi(x_i),
\]

contradicting the forced low-altitude bias above.

This is the correct place where zeta/L-function style harmonic machinery may enter.

Important caveat: GRH by itself does not directly control character sums over a deterministic Collatz orbit. It controls characters over classical arithmetic sets such as intervals or primes. A Collatz proof would need a transfer/mixing theorem adapted to the orbit or inverse tree.

## 6. Research target

Try to prove a statement of the form

\[
\left|\sum_{x_i\in L_T}\chi(x_i)\right|
\le c |L_T|
\quad\text{for every nonprincipal }\chi\pmod8,
\]

with some uniform `c < 1/3` for sufficiently long low-altitude blocks or returns.

Combined with the low-altitude character-bias lemma, that would be impossible.

The same construction generalizes from mod 8 to mod `2^k`, where

\[
a(x)\ge k
\iff
x\equiv -3^{-1}\pmod{2^k},
\]

and the forbidden residue class can be expanded in the full character basis modulo `2^k`.
