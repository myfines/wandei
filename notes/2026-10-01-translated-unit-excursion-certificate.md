# Translation-invariant 46-step low-complexity excursion exclusion

Status: exact finite certificate in the first coefficient-contraction branch. Not a Collatz proof.

The older `src/unit_excursion_cert.py` covered only the length-46 mechanical factor beginning at phase zero. The new `src/translated_unit_excursion_cert.py` removes that phase restriction.

## Statement

Let `m<k` be any preterminal time in the first coefficient-contraction candidate such that

h_m=0.

Suppose that during the next 46 odd-only transitions the critical defect stays in

h in {0,1}

and makes at most two upcrossings

0 -> 1.

Then the corresponding local orbit state `x_m` is impossible for a least counterexample.

Equivalently, from every boundary time of a surviving first-candidate orbit, within the next 46 odd steps one must either

1. reach defect `h>=2`, or
2. make at least three unit upcrossings `0->1`.

This conclusion is now valid at every rotation phase, not only at the initial seed.

## Why the class is finite

A length-46 factor of the irrational mechanical word

r_j=floor((j+1)log_2 3)-floor(j log_2 3)

has only 47 possible factors. The certificate exhibits all 47 exactly using integer powers of 3.

For each factor it enumerates every valuation script consistent with

- start height `h=0`;
- all intermediate heights in `{0,1}`;
- at most two `0->1` upcrossings.

The pure mechanical zero-upcrossing scripts are included as well.

The total number of scripts is

2,896,739.

For each exact script, the odd-only affine formula determines one residue class modulo `2^(A+1)` for the local seed.

Every boundary state in the first candidate satisfies

2075*2^60 <= x_m < 3N < 2^73.

Intersecting all script residue classes with this rigorous local interval gives exactly

1,289,079

candidate rows, containing

1,141,211

distinct odd local seeds.

Every candidate row is checked to realize its prescribed 46-step valuation word exactly.

## Exhaustive continuation

Every one of the 1,141,211 distinct local seeds is then continued under the exact odd-only Syracuse map until it falls below the verified frontier

N0=2075*2^60.

All candidates do so.

The latest such fall occurs after 237 odd steps, for

x = 4810798976564215475307,

which reaches

1869158857707769661911 < N0.

A state on the orbit of a least counterexample cannot later fall below `N0<=N`, so every enumerated local script is excluded.

## Reproducibility digests

Candidate-row SHA256:

`bef8f2e5b0dd6f6881a648f52cbe14f991648ba9586100bfd438c9f48b688982`

Distinct-seed descent SHA256:

`24eaa38073ec1139faf01b2cfa741b9de1ef1a7413fd035ed2634963347a6159`

## Interpretation

The old 46-step result was an initial-prefix obstruction. The new result is a local rule that can be applied after every boundary contact:

boundary contact -> within 46 steps, either h>=2 or at least three new upcrossings.

This gives a direct bridge from the global lower bound on boundary contacts/runs to repeated forced local complexity, and is therefore a stronger input for the excursion-density argument than the original phase-zero certificate.
