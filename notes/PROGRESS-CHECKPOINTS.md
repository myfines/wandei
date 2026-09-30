# Progress checkpoint discipline

Purpose: make the research recoverable after chat/context loss.

## Current hard checkpoint

The latest exact local result is the **46 odd-only step mechanical-prefix exclusion** in the first coefficient-contraction window:

- the critical mechanical prefix for the first 46 odd-only steps has total exponent `A_46 = 72`;
- it forces the seed into one residue class modulo `2^73`;
- the least positive seed in that cylinder is `4697939311072332635131` with `log2 N ≈ 71.992518069...`;
- the first-contraction certificate gives the sharper surviving-window ceiling `log2 N < 71.413083842...`;
- therefore the pure critical mechanical prefix is impossible for all 46 initial odd-only steps.

A subsequent reduction shows that any first-candidate survivor must create a positive critical defect within those first 46 steps and later repay it to `h=0`; after the **last** repayment, the suffix up to the first contraction is forced to be purely mechanical.

## Commit rule from now on

Every mathematically reusable action should be persisted immediately as its own small commit, for example:

1. a new lemma or exact algebraic identity;
2. a computational certificate or counterexample;
3. a failed route that rules out a proposed lemma;
4. a new reduction of the search space;
5. a corrected numerical bound or proof dependency;
6. code that verifies any of the above.

Do not leave substantive progress only in chat. Prefer one logical result per note/commit so the proof state can be reconstructed from Git history alone.

## Recovery rule

When resuming after context loss, read this checkpoint first, then inspect the newest commits/notes before doing new mathematics.
