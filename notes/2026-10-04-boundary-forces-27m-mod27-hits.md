# First-candidate boundary density forces at least 27,786,381 distinct `20 mod 27` hits

Status: exact combination of internal first-candidate certificates with the known Monks--Monks--Monks--Monks residue-hitting rank. Not a Collatz proof.

## 1. External rank input

For the shortcut Terras map

`T(n)=n/2` for even n, `(3n+1)/2` for odd n,

Monks--Monks--Monks--Monks (Discrete Mathematics 313(4), 2013) prove that every divergent positive orbit and every nontrivial positive cycle hits `20 mod27`. An exact finite-rank reconstruction gives the stronger stopped statement: every positive input reaches `1`, `2`, or `20 mod27`.

The reconstruction uses the lexicographic phases recorded in the source audit:

- if `3|n`, repeated even halvings lower n and the first odd step exits the divisible-by-3 phase;
- on the fifteen core residues, `Q(n)=w_h n` with weights `(16,28,49)` and every core-to-core step satisfies `Q(Tn)/Q(n)<=20/21`;
- on residue26, `v2(n+1)` decreases exactly along the odd self-loop; residue13 enters the target in one step.

This note only uses those exact inequalities.

## 2. Boundary altitude gives a uniform hitting time

For the first coefficient-contraction candidate the repository already proves that every critical-boundary odd state satisfies

`x < HIGH = 6,287,967,883,654,920,544,295 < 2^73`.

### Divisible-by-3 phase

Starting below `2^73`, at most 72 even halvings can occur before the odd part is reached, followed by at most one odd step to leave the phase. Hence this phase costs at most

`73`

shortcut steps.

Using the exact `HIGH`, the odd exit is still below `2^73`:

`(3(HIGH-1)+1)/2 < 2^73`.

### Core phase

On entry,

`Q < 49*2^73`.

Every core-to-core step multiplies Q by at most `20/21`. Exact integer arithmetic gives

`49*2^73 * 20^1117 < 21^1117`,

while 1117 is the first exponent with this property. Therefore 1117 consecutive actual core steps are an absolute upper bound: after at most 1116 core-to-core stays, one more step must leave the core or hit the target.

While in the core, the smallest weight is16, so

`n < (49/16)*2^73 < 2^75`.

An odd exit satisfies `T(n)/n<=5/3`, hence enters the last phase below `2^76`.

### Residue26/13 phase

For `n<2^76`,

`v2(n+1)<=76`.

The residue26 rank `v2(n+1)+2` therefore gives at most78 further steps; residue13 is even cheaper.

Combining the three worst-case phases gives the uniform bound

`boxed: H=73+1117+78=1268.`

Thus every first-candidate boundary state hits `1`, `2`, or `20 mod27` within at most1268 shortcut steps.

## 3. Least-counterexample consequence

Along a least positive counterexample orbit, a hit of1 or2 is impossible because it would imply convergence. Therefore every eligible boundary state must hit

`20 mod27`

within1268 shortcut steps.

The live first-candidate boundary certificate currently gives

`z >= 35,260,917,543`.

Discard at most1268 boundary starts too close to the odd-only terminal index k to guarantee the whole shortcut hitting window lies before or at that terminal time. This leaves at least

`35,260,916,275`

eligible boundary starts.

Distinct odd-only boundary states occur at distinct shortcut times, separated by at least one shortcut step. Therefore one fixed target hit can lie within the next1268 shortcut steps of at most1269 boundary starts.

Hence the number R of distinct `20 mod27` hits before or at the terminal time satisfies

`R >= ceil((z-1268)/1269)`

and exact integer arithmetic gives

`boxed: R >= 27,786,381.`

`src/boundary_to_mod27_hit_cert.py` certifies all numerical inequalities.

## 4. New bridge created

This is the first direct quantitative bridge from the first-candidate weighted boundary machinery to the mod-27 arithmetic section:

`35.26 billion boundary contacts`

force

`at least 27.786 million distinct 20 mod27 hits`.

At those hits the normalized prime-turnover lemma uses digits `{1,5,7}`, and every departure from the target section strictly contracts the sampled normalized state `u=M/9` with principal coefficient at most `3/4`.

Thus the remaining first-candidate problem now has a new target-run dichotomy:

- many target runs imply many strict target-departure contractions;
- few target runs imply many adjacent target-to-target edges, hence many normalized prime-turnover constraints.

The next useful theorem should quantify this dichotomy strongly enough to conflict with first-candidate principal drift or prime-support recycling.