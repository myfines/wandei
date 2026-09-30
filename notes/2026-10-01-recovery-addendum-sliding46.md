# Recovery addendum: sliding 46-step excursion progress

Read this together with `CURRENT_STATUS.md`. This file records progress made after the current status checkpoint.

## New exact local structure

1. Cheap immediate boundary excursions `0->1->0` of mechanical type `21` and valuation type `12` can occur at most three times consecutively. Exact reason: `(21)^4` is forbidden in the mechanical rotation word, while `(21)^3` is possible.

2. A heavy immediate two-step return of type mechanical `22`, valuation `13`, is impossible. Its second-step phase lies in `[1-beta,beta)`, beta=log2(3)-1, whereas the side-branch repayment gate requires phase `>log2(128/65)`. Therefore every non-cheap excursion has length at least three.

3. A three-symbol mechanical word beginning with a boundary departure is exactly `212` or `221`. The corresponding genuine three-step valuation patterns are exactly:
   - `212 / 113`;
   - `221 / 113`;
   - `221 / 122`.

## Sliding 46-step certificate

`src/sliding_unit_excursion_cert.py` covers all 47 length-46 mechanical factors for paths starting at h=0, staying in h in {0,1}, with one or two upcrossings.

The stronger `src/sliding_unit_excursion_cert_max3.cpp` covers one, two, or three upcrossings.

Exact max-3 counts:

- 47 mechanical factors;
- 104,035,682 low-defect scripts;
- 47,290,188 residue classes intersecting `[2075*2^60,2^73)`;
- 47,866,652 concrete seed lifts;
- every lift falls below the verified frontier;
- latest drop: odd step 276;
- worst local seed: 8171827952796853273339;
- endpoint below frontier: 697521228196614030223;
- factor shift: 31;
- no unsigned-128 overflow.

Therefore any first-candidate survivor, after any boundary departure sufficiently far from the terminal contraction, must within 46 odd steps either

- reach defect height h>=2, or
- contain at least four 0->1 upcrossings.

## Weighted global boundary strengthening

The old defect-budget argument used only that the mechanical correction weights differ by less than a factor two. Two exact Denjoy--Koksma refinements now exploit the true weights `2^{-theta_j}`.

First, `src/weighted_boundary_density_cert.py` gives

- boundary states z >= 31,430,911,924;
- boundary density >= 43.619250722%;
- departures >= 898,026,054.

The stronger pair-constrained argument uses the exact closure rule

`h_j=0 and r_j=1 and j+1<k  =>  h_{j+1}=0`.

Because the mechanical word contains no `11`, these forced pairs are disjoint. The exact Lagrange/Denjoy--Koksma certificate `src/pair_constrained_boundary_density_cert.py` proves

- boundary states z >= 35,251,435,711;
- boundary density >= 48.9213044886%;
- boundary runs >= 1,007,183,878;
- departures >= 1,007,183,877;
- non-cheap excursions >= 251,795,969.

Since heavy immediate returns are impossible, all those non-cheap excursions have length at least three.

This is the current strongest global excursion constraint in branch A.

## Max-4 exploratory scan

A direct max-4 scan has about 1.84 billion scripts. A partial parallel run completed the first 20 of 47 factors with no survivor, but timed out before all factors completed. This is NOT a certificate and must not be cited as a theorem. The correct next move is pruning rather than claiming the partial scan.

## Best next target

Combine the now >1.007 billion forced departures with the sliding max-3 local certificate. For every boundary departure sufficiently far from the terminal time, the next 46 odd steps either hit h>=2 or contain at least four upcrossings. Turn this local dichotomy into a global covering inequality between

- number of departures,
- number of h>=2 states,
- and dense clusters of upcrossings,

then feed the resulting lower defect cost back into the exact weighted correction budget.