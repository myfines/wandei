# 2026-11-22 — Exact mod-27 target gates, two-hit descent, and dual-carry countermodels

**Status:** proved elementary arithmetic lemmas and finite exact regression tests. **Not a proof of Collatz; no independent originality claim.** The external 20 mod 27 recurrence theorem is due to Monks–Monks–Monks–Monks (2013). This note carefully translates their *shortcut* map to the repository's *odd-only* exponent scripts.

## 1. Correct bridge between the two maps

Use the shortcut map `T(n)=n/2` (even), `(3n+1)/2` (odd), and odd-only map `S(n)=(3n+1)/2^a`, `a=v2(3n+1)` for positive odd n. The shortcut **block following** odd n consists of

    T(n),...,T^a(n) = (3n+1)/2,...,(3n+1)/2^a = S(n).

The block includes its endpoint but not its starting odd n; consecutive odd blocks thus partition the shortcut states after the starting odd seed, without double-counting.

**Theorem 1 (exact 20 mod 27 trigger).** Define τ(r) as the smallest positive integer t with `20*2^t = 3r+1 (mod 27)`. The nine values are:

| r=n mod 9 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| τ(r) | 11 | 13 | 9 | 17 | 1 | 15 | 5 | 7 | 3 |

The shortcut block after odd n hits 20 modulo 27 **iff** `a(n)>=τ(n mod 9)`. In fact its exact number of hits is

    h(n)=max(0, 1+floor((a(n)-τ(n mod9))/18)).

Proof: `2` has multiplicative order 18 modulo 27 and every `3r+1` is a unit. The i-th shortcut state is `2^-i(3n+1) mod27`. Its first matching exponent is τ, and further matches occur every 18 steps. This is not a statement that S(n) itself must be 20 mod27; the target can be an intermediate even shortcut state.

**Theorem 2 (finite memory in the exponent word).** For k>=2 and actual exponents a_(k-2),a_(k-1),

    S^k(n) = 2^-a_(k-1) [1+3*2^-a_(k-2)] (mod 9),

and for k>=3,

    S^k(n) = 2^-a_(k-1)+3*2^[-a_(k-1)-a_(k-2)]
             +9*2^[-a_(k-1)-a_(k-2)-a_(k-3)] (mod 27).

The inverses are mod 9/27. These follow by iterating `2^a*S(n)=3n+1` modulo powers of 3. In the prior *dual-carry* notation, `M_k=S^k(n) (mod 3^k)` fixes the `mod 9` trigger for k>=2; the additional binary overlap/carry `q_k` plays no part in the local test. A hypothetical divergent positive shortcut orbit must trigger this gate infinitely often, by the Monks et al. strong sufficiency result; no density claim follows.

## 2. Two consecutive target-bearing odd blocks guarantee strict descent

For any residue r modulo9 let `r'=(3r+1)*2^-a mod9` if the current valuation is a. If both the current and the following odd blocks hit 20 mod27, we require

    a>=τ(r), b>=τ(r'), r'= (3r+1)*2^-a (mod 9).

Because r' depends only on a modulo6, searching a in `{τ(r),...,τ(r)+5}` is an **exhaustive finite modular proof** of the minimum of a+b. For r=0,...,8 these exact minima are

    (17,19,15,23,7,21,11,13,9).

Thus `a+b>=7` universally, with equality attainable for r=4, a=6, b=1. The exact affine two-step identity is

    S^2(n)=(9n+3+2^a)/2^(a+b).

Therefore for every such positive n,

    **S^2(n) <= (9n+67)/128 < n.**

The bound is sharp: `661 --a=6--> 31 --b=1--> 47`, and the first block contains 992≡20 mod27, the second ends at 47≡20 mod27; `128*47=9*661+67`.

## 3. Conditional global height budget for a smallest counterexample

For arbitrary positive odd x, `S(x)+1 <= (3/2)(x+1)`. For adjacent two-hit blocks,

    S^2(x)+1 <= [9(x+1)+186]/128.

Let N be a *hypothetical least positive odd counterexample*: its entire odd-only orbit stays >=N. Define

    beta_N=[9+186/(N+1)]/128 <1.

Take any first k odd steps and partition them into p disjoint adjacent pairs of target-bearing blocks, with the other k-2p steps treated singly. Telescoping the **true** height gives

    1 <= (S^k(N)+1)/(N+1)
      <= (3/2)^(k-2p) * beta_N^p.

Hence every such prefix must obey the rigorous conditional density upper bound

    **p/k <= log(3/2) / log((9/4)/beta_N).**

For very large N this upper limit tends to `log(3/2)/log(32)≈0.1169925001` disjoint two-hit pairs per odd step. This is a *necessary* condition for a smallest counterexample, **not** a contradiction. The older first-candidate `~27.786 million` shortcut target hits among `~72.057 billion` odd steps do not force anywhere near enough adjacent target-bearing pairs to violate it. Further density or local adjacency evidence would be required.

## 4. Exact Haar cylinder statistics, NOT a deterministic orbit claim

Under Haar-uniform positive odd 2-adic starting states, finite odd valuation words have exact cylinder weights `2^-sum(a_j)`, i.e. the formal valuation digits are independent with `P(a_j=t)=2^-t`. For k>=2 the mod-9 residue gate is determined by the preceding two valuations, so its threshold distribution is

| τ | 1 | 3 | 7 | 9 | 13 | 15 |
|---:|---:|---:|---:|---:|---:|---:|
| Probability | 11/63 | 22/63 | 2/63 | 16/63 | 8/63 | 4/63 |

The exact probability that the current *shortcut block* contains at least one 20 mod27 target is therefore

    **P(hit)=Σ_t P(τ=t)*2^(1-t)=1079/4096≈0.263427734375.**

For two adjacent late blocks, exact geometric-residue sums give

    **P(hit now & hit next)=59345/8388608≈0.0070744752884**,

strictly smaller than `P(hit)^2`. Thus these finite-cylinder events have strong negative lag-one correlation under Haar; no assumption of temporal independence along an individual ordinary integer trajectory is justified. The event depends on three consecutive valuation symbols; formally it is 2-dependent under the Haar script law.

## 5. Countermodel: arbitrarily frequent target hits alongside real growth

For every q>=1 set

    n_q=2^(3q+1)-5.

Its next 2q odd-only valuations are precisely `(1,2)^q`; each completed pair expands under `S^2(x)=(9x+5)/8`, and

    **S^(2q)(n_q)=2*9^q-5>n_q.**

Exactly **q-1** of the 2q *shortcut blocks* contain a state congruent to 20 mod27 (at odd-block indices 2,4,...,2q-2 when counted from zero). There are **no adjacent hit-bearing blocks** in this family. It realizes arbitrarily many visits with every completed pair gaining height, but **the positive starting seed changes with q**.

The associated formal infinite exponent word `(1,2)^infinity` corresponds to the *negative* odd-only period `-5 -> -7 -> -5`; in shortcut form it is `-5 -> -7 -> -10 -> -5`, and `-7≡20 mod27`. Therefore *modular targets plus expanding symbolic drift* do not alone exclude phantom negative 2-adic cycles.

The dual-carry data of the finite positive witness are explicitly

    A_(2q)=3q,
    C_(2q)=5*(9^q-8^q),
    r_(2q)=2^(3q+1)-5,
    Y_(2q)=2*9^q-5,
    M_(2q)=9^q-5,
    q_(2q)=1.

Thus these special finite prefix realizers keep the binary **overlap carry equal to 1** at the period endpoints, unlike any fixed positive seed, whose carries eventually vanish. This precisely identifies the extra Archimedean/dual-carry information discarded by an argument using only mod27 hits and log drift.

## 6. Reproduction and open problem

- `src/mod27_dual_carry_bridge.py` — modular threshold automaton, exact suffix residues, consecutive-hit descent, rational Haar statistics, dual-carry shadow family, and real-height pair budget.
- `tests/test_mod27_dual_carry_bridge.py` — independent shortcut trajectory vs threshold comparisons; 6 deterministic tests pass locally, including 50k odd starting integers over 8 odd steps, six residue cases, 250k blocks in the script's own check, q<=59 growing shadows, and height budget checks.

The missing result is **a uniform same-orbit theorem** forcing sufficient adjacent target-bearing odd blocks, or otherwise constraining separated target visits and the cross-carry height, on a hypothetical counterexample. The present finite target count does not yield such a theorem.

### External reference

K. Monks, K. G. Monks, K. Monks, M. Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, Discrete Mathematics 313(4), 468–489 (2013), arXiv:1204.3904, https://arxiv.org/abs/1204.3904.