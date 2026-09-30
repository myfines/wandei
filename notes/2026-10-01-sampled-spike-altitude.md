# Sampled spike altitude lemma

Status: exact necessary condition for any hypothetical unbounded Collatz orbit, using the mod-9 sampled map. Not a proof of the Collatz conjecture.

Let `n_*` be the least counterexample among sampled states `n ≡ 2 (mod 9)`, and write

\[
M_*=4n_*+1.
\]

For any sampled counterexample state `n` write `M=4n+1` and

\[
M=3^V u,\qquad 3\nmid u.
\]

For `V>=5`, one can choose `t in {V,V+1}` so that

\[
\widetilde M=3(2^t u-1)\equiv9\pmod{36}.
\]

Then `\widetilde n=(\widetilde M-1)/4` is another sampled state whose first sampled return is `n`. Hence if `n` lies on a counterexample orbit, then `\widetilde n` is also a counterexample, so by minimality

\[
\widetilde M\ge M_*.
\]

Since `t<=V+1`,

\[
M_*\le\widetilde M<3\,2^{V+1}u.
\]

Using `M=3^V u` gives the altitude bound

\[
\boxed{
M>\frac{1}{6}\left(\frac32\right)^V M_*.
}
\]

Equivalently, a sampled counterexample with large `v_3(4n+1)` must lie exponentially high above the least sampled counterexample.

Now consider a first-return block containing a consecutive odd loop of length `m` at residue `8 mod 9`. If the loop starts at `y`, then exact exit from the loop gives

\[
y+1=9\,2^m a
\]

with odd `a`, and after the loop

\[
T^m(y)+1=3^{m+2}a.
\]

The only two loop-exit suffixes are `00` and `01`. Therefore the next sampled state `n'` satisfies respectively

\[
4n'+1=3^{m+2}a
\]

or

\[
4n'+1=3^{m+3}a.
\]

Hence always

\[
V'=v_3(4n'+1)\ge m+2.
\]

Combining with the sampled altitude bound yields, for `m` large enough that `V'>=5`,

\[
\boxed{
4n'+1>
\frac38\left(\frac32\right)^m M_*.
}
\]

Thus a long odd-run spike has an unavoidable exponential altitude cost. In particular, if a sampled counterexample state lies below a fixed multiplicative height `K M_*`, then the immediately preceding odd-loop length satisfies

\[
m\le \log_{3/2}(8K/3)
\]

up to the small `V'<5` edge cases.

This is a sampled analogue of the earlier side-branch altitude lemma: high local divisibility (here 3-adic divisibility produced by a long mod-9 odd loop) cannot occur near the minimal counterexample floor.

Next target: combine this with the sampled correction identity and reciprocal-summability to bound the frequency of long odd-loop spikes inside low sampled altitude bands.