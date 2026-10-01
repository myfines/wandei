# Erratum: the `(21)^4` cap does not imply a global non-cheap excursion fraction

Status: correction of an earlier overreach. The local rotation lemma itself remains valid.

## Valid local lemma

A cheap immediate boundary excursion has mechanical letters `21` and valuations `12`:

h: 0 -> 1 -> 0.

The exact rotation argument proves that the mechanical factor

(21)^4

cannot occur. Equivalently, at most three **immediately back-to-back** cheap excursions can occur with no intervening boundary waiting transitions.

This local factor statement is correct.

## Invalid global inference

Earlier notes treated the excursion sequence as though consecutive excursions were always represented by adjacent `21` blocks. That is false.

After a cheap return to `h=0`, the orbit may remain on the boundary for one or more mechanical transitions (`a_j=r_j`) before the next departure `0->1`. Those waiting transitions change the rotation phase. Hence two successive excursions in the excursion sequence need not correspond to adjacent mechanical factors.

Therefore

(21)^4 impossible

does **not** imply

"among every four boundary excursions, at least one is non-cheap."

The previously quoted global lower bounds

- 181,702,471 non-cheap excursions (from the older 35-state run count), and
- 303,891,687 non-cheap excursions (after the 29-state run improvement)

are retracted.

Any later conclusion that uses only those global non-cheap counts must also be treated as unsupported until rederived with boundary waiting explicitly included.

## Results unaffected by this erratum

The following remain independent exact results:

1. pair-constrained boundary count `z >= 35,251,435,711`;
2. boundary-run cap: at most 29 boundary states per maximal run;
3. at least 1,215,566,748 actual departures `h=0 -> 1`;
4. every departure has `r=2, a=1`;
5. the local `(21)^4` factor exclusion itself;
6. heavy two-step `22/13` immediate return exclusion;
7. three-step mechanical classification (`212` or `221`);
8. sharp odd-height `r=2` direct-repayment phase gate and global count at most five;
9. translated 46-step low-complexity finite certificate;
10. last boundary repayment occurs within the final 44 odd steps.

## Correct replacement target

Future counting must treat a boundary run plus its following excursion as one block, or otherwise include the number and mechanical content of boundary waiting transitions explicitly. Local factor repetition caps may not be promoted to excursion-sequence frequency bounds without that bridge.
