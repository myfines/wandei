# Boundary-run cap strengthened to 31 states

Status: exact finite certificate in the first-candidate branch. Not a Collatz proof.

At a critical-boundary time h_j=0, the local state satisfies

N0 <= x_j < 2^73.

A run of L mechanical transitions on the boundary fixes the exact valuation word to the corresponding length-L mechanical factor. For each factor, the exact 2-adic seed residue is therefore determined.

`src/boundary_run_31_cert.cpp` enumerates every length-31 mechanical factor and every lift of its exact residue in

[2075*2^60, 2^73).

Exact result:

- mechanical factors: 32;
- local candidate states: 184,782,336;
- every candidate falls below the verified frontier;
- latest such drop: odd step 330;
- worst local seed: 8355649853805505174523;
- below-frontier endpoint: 1072053775599191922857;
- first occurrence shift of the worst factor: 36.

Therefore no first-candidate prefix can contain 31 consecutive mechanical transitions while remaining on h=0.

Equivalently,

no boundary run can contain 32 consecutive boundary states,

so every maximal boundary run has at most

31 boundary states.

This improves the previous cap of 35 states.

Combining with the current pair-constrained weighted boundary count

z >= 35,251,435,711,

the number of boundary runs is at least

ceil(35,251,435,711 / 31) = 1,137,143,088.

Hence the number of unit departures h=0->1 is at least

1,137,143,087.

Using the exact cheap-excursion run cap (at most three consecutive cheap immediate excursions), at least

floor(1,137,143,087 / 4) = 284,285,771

excursions are non-cheap, and because heavy immediate returns are impossible, all of those have length at least three.

A scan of 30 transitions has not yet been completed and must not be cited as a certificate.