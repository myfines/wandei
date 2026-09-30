# Boundary-run cap strengthened to 30 states

Status: exact finite certificate in the first-candidate branch. Not a Collatz proof.

A length-30 pure mechanical boundary segment was checked over all 31 possible mechanical factors. For each factor, every exact 2-adic seed lift in the local boundary interval

2075*2^60 <= x < 2^73

was continued under the odd-only Syracuse map until it fell below the verified frontier.

Because the full scan exceeded one tool-call runtime, the 31 factors were verified in four disjoint exact chunks: indices 0:8, 8:16, 16:24, and 24:31. Together these ranges cover all factors exactly once.

Exact aggregate result:

- mechanical factors: 31;
- local candidate states: 563,742,720;
- every candidate falls below the verified frontier;
- latest drop: odd step 330;
- worst local seed: 8355649853805505174523;
- below-frontier endpoint: 1072053775599191922857;
- worst factor first occurs at shift 36.

Therefore no first-candidate prefix can contain 30 consecutive mechanical transitions while staying on h=0.

Equivalently, no boundary run can contain 31 consecutive boundary states, so every maximal boundary run contains at most 30 boundary states.

Combining with the current pair-constrained weighted boundary count

z >= 35,251,435,711,

the number of boundary runs is at least

ceil(35,251,435,711 / 30) = 1,175,047,858.

Hence the number of unit departures h=0->1 is at least

1,175,047,857.

With the exact cheap-excursion run cap, at least

floor(1,175,047,857 / 4) = 293,761,964

excursions are non-cheap. Since heavy immediate two-step returns are impossible, all of these non-cheap excursions have length at least three.

This improves the previous 31-state boundary-run cap.