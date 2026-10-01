# Boundary-run cap strengthened to 29 states

Status: exact finite certificate in the first-candidate branch. Not a Collatz proof.

All 30 possible length-29 mechanical factors were checked. For every factor, every exact 2-adic seed lift in

2075*2^60 <= x < 2^73

was continued under the odd-only Syracuse map until it fell below the verified frontier.

The full scan was executed in six disjoint chunks covering factor indices

0:5, 5:10, 10:15, 15:20, 20:25, 25:30.

Exact aggregate result:

- mechanical factors: 30;
- local candidate states: 1,553,424,384;
- every candidate falls below the verified frontier;
- latest drop: odd step 341;
- worst local seed: 8522726957776383649659;
- below-frontier endpoint: 1477878697162943367103;
- worst factor first occurs at shift 26.

Therefore no first-candidate prefix can contain 29 consecutive mechanical transitions while staying on h=0.

Equivalently, no boundary run can contain 30 consecutive boundary states, so every maximal boundary run contains at most 29 boundary states.

Combining with the pair-constrained weighted boundary count

z >= 35,251,435,711,

the number of boundary runs is at least

ceil(35,251,435,711 / 29) = 1,215,566,749.

Hence the number of unit departures h=0->1 is at least

1,215,566,748.

Every such departure is forced by the defect recurrence to have

r=2, a=1.

These boundary-run and departure counts are exact consequences of the certificate.

An earlier version of this note additionally claimed that at least one quarter of all excursions are non-cheap by using the local `(21)^4` exclusion. That global inference is retracted: boundary waiting transitions may occur between successive excursions, so excursion adjacency does not imply adjacent `21` factors. See `notes/2026-10-01-erratum-cheap-excursion-global-count.md`.
