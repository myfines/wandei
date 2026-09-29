# Mod-9 first-return skeleton for the Terras map

Status: exact finite-state reduction + exhaustive 36-state enumeration. This is structural infrastructure, not a Collatz proof.

Use the Terras map

\[
T(n)=\begin{cases}n/2,&n\text{ even},\\(3n+1)/2,&n\text{ odd}.\end{cases}
\]

Suppose a parity prefix has already contained at least two odd steps. Let `p<q<t` be the positions of its last two odd steps. In the standard affine identity

\[
2^tT^t(n)=3^j n+d,
\]

all contributions to `d` except those from the last two odd positions vanish modulo 9, because they contain a factor `3^2`. Therefore

\[
T^t(n)\equiv 2^{-t}\bigl(2^q+3\,2^p\bigr)\pmod9.
\]

Set

\[
u=t-q,\qquad v=q-p.
\]

Then

\[
\boxed{T^t(n)\equiv 2^{-u}\bigl(1+3\,2^{-v}\bigr)\pmod9.}
\]

Because `2^6=1 (mod 9)`, only `(u,v) mod 6` matters: 36 states.

Appending one even parity bit gives

\[
E(u,v)=(u+1,v)\pmod6,
\]

while appending one odd parity bit gives

\[
O(u,v)=(1,u)\pmod6.
\]

The residue is 2 modulo 9 exactly for

\[
R=\{(1,0),(1,2),(1,4),(3,1),(3,3),(3,5)\}\pmod6.
\]

Indeed, when `v` is even the bracket is `4 mod 9`, forcing `u=1 mod 6`; when `v` is odd the bracket is `7 mod 9`, forcing `u=3 mod 6`.

Exhaustive enumeration of the directed 36-state graph gives:

* after removing the six return states `R`, the only directed cycle reachable inside a first-return excursion is the odd self-loop
  \[
  (1,1)\xrightarrow{O}(1,1);
  \]
* suppressing this self-loop leaves exactly 82 first-return skeleton paths;
* the longest skeleton has length 8;
* every skeleton uses at most 6 even steps (consistent with the independently Lean-proved theorem `even_steps_between_two_mod_nine`).

Consequently every sufficiently described first-return parity word belongs to one of finitely many families

\[
\boxed{u\,1^m\,v,\qquad m\ge0,}
\]

plus fixed short families not passing through `(1,1)`.

The self-loop state `(1,1)` corresponds to residue `8 mod 9`. Thus the variable part is a consecutive odd run while the orbit remains 8 modulo 9.

If the run starts at `y` and lasts at least `m` odd steps, then

\[
2^m\mid y+1,
\qquad
T^m(y)+1=\left(\frac32\right)^m(y+1).
\]

Since the loop state also has `y=8 mod 9`, actually

\[
9\cdot2^m\mid y+1
\]

and therefore

\[
T^m(y)\equiv-1\pmod{3^{m+2}}.
\]

So long mod-9 first returns are not combinatorially arbitrary: almost all of their length is one odd run which transfers high 2-adic divisibility of `y+1` into high 3-adic divisibility of the later value plus one.

Next target: combine this finite skeleton with the sampled-noncontracting-tail theorem. At critical density, long `m` excursions must be sparse; the remaining return dynamics is then a finite-family affine system with sparse long-loop defects.
