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

## 3. Stronger overlap count using entries into h>=2

Define

- `U = # {0<=j<k : h_j=0, h_{j+1}=1}`;
- `V = # {0<=j<k : h_j=1, h_{j+1}=2}`.

A clean 46-step window begins at `h=0`. If it reaches any state with `h>=2`, then before its first such state it must contain a transition `1->2`. Therefore high windows can be charged to **entry transitions** rather than all high-defect occupation times.

A fixed transition belongs to at most 46 length-46 windows. Hence, if `W_V` denotes clean windows that reach `h>=2`,

`W_V <= 46 V`.

If a clean window never reaches `h>=2`, the finite certificate forces at least four `0->1` upcrossings. If `W_U` denotes these low windows, incidence counting gives

`4 W_U <= 46 U`,

so

`W_U <= (46/4) U`.

Since `W=W_V+W_U`,

`W <= 46V + (46/4)U`.

Equivalently,

`92V + 23U >= 2W`,

and therefore

`boxed: 4V + U >= ceil(2W/23)`.

Using `W>=35,251,435,436`,

`boxed: 4V + U >= 3,065,342,212`.

This strictly strengthens the earlier occupation-count version `4H+U>=3,065,342,212`, because every `1->2` entry contributes a high state but a long high excursion may contribute many high states.

## 4. Mechanical form of both charged events

The recurrence is

`h_{j+1}=h_j+r_j-a_j`,

with `r_j in {1,2}` and every valuation `a_j>=1`.

For a `0->1` upcrossing, `r_j-a_j=1`, hence necessarily

`r_j=2, a_j=1`.

For a `1->2` entry, the same increment `+1` is required, so again necessarily

`r_j=2, a_j=1`.

Thus **every event counted by either U or V is the same local valuation event `r=2,a=1`; only the incoming defect height differs.** This makes the strengthened charge particularly suitable for a phase/continued-fraction counting argument.

## 5. Why this is safe with boundary waiting

This argument never assumes that successive excursions are mechanically adjacent. Boundary waiting transitions are allowed without restriction.

The only overlap fact used is exact: a fixed transition belongs to at most 46 length-46 windows.

So the new inequality is independent of the retracted inference from `(21)^4` to a global non-cheap fraction.

## 6. Next target

The remaining task is to upper-bound the same charge `4V+U` from arithmetic/rotation structure.

Both U and V occur only on `r=2,a=1` transitions. Candidate routes are:

1. combine their required density with the exact irrational-rotation positions of `r=2`;
2. use the fact that U has incoming height 0 and V incoming height 1 to charge their correction-weight losses differently;
3. exploit continued-fraction shifts `q_U=6,586,818,670` and `q_L=65,470,613,321`, whose rotation errors are of order `10^-11`, to force close boundary pairs or repeated contracting blocks.
