# Strong translated 46-step rule and global covering charge

Status: exact finite-certificate consequence inside the first coefficient-contraction branch. Not a Collatz proof.

This note replaces the retracted global cheap/non-cheap frequency argument with a direct window-overlap count that explicitly tolerates boundary waiting.

## 1. Stronger translated finite certificate

`src/translated_noheavy_three_upcross_cert.py` exhausts every length-46 local script satisfying

- start at a boundary state `h=0`;
- all following defect states remain in `{0,1}`;
- at most three upcrossings `0->1` occur;
- no heavy direct return `h=1,r=2,a=3` occurs in the window.

All 47 length-46 mechanical factors are included.

The complete chunked scan gives

- exact scripts: `12,024,283`;
- concrete local candidate rows in `[2075*2^60,2^73)`: `6,112,533`;
- every candidate realizes its prescribed valuation prefix;
- every candidate falls below the verified frontier;
- latest fall: odd step `276`;
- worst local seed: `8171827952796853273339`;
- below-frontier endpoint: `697521228196614030223`.

Therefore, for any boundary time `m` whose next 46 transitions contain no heavy `h=1,r=2,a=3` return, a surviving first-candidate orbit must satisfy at least one of

1. some state in the next 46 steps has `h>=2`; or
2. the window contains at least four upcrossings `0->1`.

This statement is translation-invariant in the mechanical phase.

## 2. Only five heavy-return events can contaminate windows

The sharp repayment phase certificate proves that in the full first-candidate prefix there are at most five odd-height `r=2` direct repayments. In the low-defect class, every heavy return `h=1,r=2,a=3` is one of these events.

A fixed transition can lie in at most 46 length-46 windows indexed by their starting time. Hence five heavy-return events contaminate at most

`5*46 = 230`

possible boundary-started windows.

Also, at most 45 preterminal boundary times lie too close to the terminal index to have a full 46-transition window.

The pair-constrained boundary certificate gives

`z >= 35,251,435,711`

boundary times. Therefore at least

`W >= 35,251,435,711 - 230 - 45`

so

`W >= 35,251,435,436`

boundary-started windows are both complete and free of heavy returns.

Every one of these `W` clean windows must obey the stronger local dichotomy above.

## 3. Direct overlap count

Let

- `H = #{0<=t<k : h_t>=2}` be the number of high-defect occupation times;
- `U = # {0<=j<k : h_j=0, h_{j+1}=1}` be the number of upcrossing transitions.

Partition the `W` clean windows into two classes.

### High windows

A high window contains at least one state with `h>=2`.

One fixed high-defect state can lie in at most 46 length-46 windows. Hence

`W_H <= 46 H`.

### Low windows

A clean window with no `h>=2` state must contain at least four upcrossings.

Counting window/upcrossing incidences, every upcrossing can belong to at most 46 windows, so

`4 W_U <= 46 U`,

hence

`W_U <= (46/4) U`.

Adding the two classes gives

`W <= 46 H + (46/4) U`.

Equivalently,

`92 H + 23 U >= 2 W`,

and therefore

`4 H + U >= ceil(2W/23)`.

Using the certified lower bound on `W`,

`ceil(2*35,251,435,436 / 23) = 3,065,342,212`.

Thus every first-candidate survivor must satisfy the exact global charge inequality

`boxed: 4 H + U >= 3,065,342,212`.

## 4. Why this is safer than the retracted excursion count

This argument never assumes that successive excursions are mechanically adjacent. Boundary waiting transitions are allowed without restriction.

The only overlap fact used is geometric and exact: a fixed state or transition belongs to at most 46 windows of length 46.

So the new inequality is independent of the invalid inference from `(21)^4` to a global non-cheap fraction.

## 5. Next target

The remaining task is to upper-bound the same charge `4H+U` (or a sharper weighted version) from the correction budget and rotation weights.

A promising route is to note that every upcrossing forces a successor state at `h=1`, while every `h>=2` state contributes at most one quarter of the mechanical correction weight. A phase-weighted Lagrange optimization analogous to `pair_constrained_boundary_density_cert.py` may therefore be able to turn the lower charge above into a contradiction.
