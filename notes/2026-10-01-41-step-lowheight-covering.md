# 41-step low-height certificate raises the global covering charge

Status: exact finite-certificate consequence inside the first coefficient-contraction branch. Not a Collatz proof.

This strengthens the earlier 46-step no-heavy low-height covering rule.

## 1. Local class

`src/translated_lowheight_three_upcross_41_chunk_cert.cpp` covers all 42 length-41 mechanical factors. Starting from an arbitrary critical-boundary state `h=0`, it enumerates every exact 41-transition script satisfying

- all defect states remain in `{0,1}`;
- at most three `0->1` upcrossings occur;
- the rare heavy direct return `h=1,r=2,a=3` is absent.

Every exact 2-adic seed cylinder is intersected with the sharp boundary-state window

`2075*2^60 <= x < 6,287,967,883,654,920,544,295`.

The scan was completed in disjoint chunks `0:4, 4:8, 8:11, 11:22, 22:32, 32:42`.

Exact aggregate:

- factors: `42`;
- scripts: `5,596,528`;
- concrete local seeds: `379,556,603`;
- every seed falls below the verified frontier;
- latest drop: odd step `297`;
- worst local seed: `6,114,300,038,360,557,642,401`;
- below-frontier endpoint: `635,537,898,295,088,599,553`.

Therefore any surviving, complete, heavy-free, boundary-started 41-step window must either

1. enter `h>=2`, hence contain a transition `V: 1->2`; or
2. contain at least four transitions `U: 0->1`.

## 2. Clean-window count

The sharp phase certificate bounds the globally rare odd-height `r=2` direct repayments by at most five. A fixed heavy transition contaminates at most 41 length-41 windows, so at most

`5*41 = 205`

boundary starts are lost to heavy contamination.

At most 40 preterminal boundary starts are too close to the terminal index to have a complete 41-transition window.

The pair-constrained weighted boundary certificate gives

`z >= 35,251,435,711`.

Hence the number `W_41` of complete, heavy-free, boundary-started windows satisfies

`W_41 >= 35,251,435,711 - 205 - 40`

so

`boxed: W_41 >= 35,251,435,466`.

## 3. Global covering charge

Let

- `U = #{j : h_j=0, h_{j+1}=1}`;
- `V = #{j : h_j=1, h_{j+1}=2}`.

Partition clean windows according to whether they enter `h>=2`.

A high window contains at least one `V`; one fixed transition lies in at most 41 windows. Thus

`W_V <= 41 V`.

A low window contains at least four `U`; incidence counting gives

`4 W_U <= 41 U`,

so

`W_U <= (41/4) U`.

Since `W_41=W_V+W_U`,

`W_41 <= 41V + (41/4)U`.

Therefore

`4V+U >= ceil(4 W_41 / 41)`.

Using the exact clean-window lower bound,

`ceil(4*35,251,435,466/41) = 3,439,164,436`.

Hence

`boxed: 4V + U >= 3,439,164,436`.

Both charged transitions require the same local valuation event `r=2,a=1`; only the incoming defect height differs.

This supersedes the older 46-step charge `4V+U>=3,065,342,212`.

## 4. Search status

The same low-height class has also been completely certified at lengths 45, 44, 43, and 42. The 41-step scan is the current shortest fully completed result. A 40-step scan has not yet been completed; no mathematical failure at length 40 is claimed.