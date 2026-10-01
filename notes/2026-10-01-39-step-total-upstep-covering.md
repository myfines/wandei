# 39-step translated certificate forces 2.711 billion defect upsteps

Status: exact finite-certificate consequence inside the first coefficient-contraction branch. Not a Collatz proof.

This strengthens `notes/2026-10-01-total-upstep-covering.md` by shortening the translated local window from 46 transitions to 39.

## 1. Exact finite scan

`src/translated_two_upsteps_39_chunk_cert.cpp` covers all 40 length-39 mechanical factors.

For each factor it enumerates every exact defect/valuation script satisfying

- start at `h=0`;
- at most two total upward defect transitions `h->h+1` in the next 39 odd-only transitions;
- no rare heavy direct return `h=1,r=2,a=3`.

At most two total upward transitions imply `h<=2`, so the enumeration includes every possible stay/down transition from the reachable heights `0,1,2`.

Every exact 2-adic cylinder is intersected with the sharp boundary-state interval

`2075*2^60 <= x < 6,287,967,883,654,920,544,295`.

The scan was executed in five disjoint factor chunks `0:8, 8:16, 16:24, 24:32, 32:40`.

Exact aggregate:

- mechanical factors: `40`;
- valuation/defect scripts: `992,954`;
- concrete local seed rows: `594,900,016`;
- every row drops below the verified frontier;
- latest drop: odd step `301`;
- worst local seed: `3,922,996,901,307,644,258,171`;
- below-frontier endpoint: `2,064,323,270,781,959,543,497`;
- worst factor first shift: `26`.

Therefore any surviving, heavy-free, boundary-started 39-transition window must contain at least three total upward defect transitions.

## 2. Clean 39-step windows

The sharp phase certificate bounds the globally rare odd-height `r=2` direct repayments by at most five events. A single transition can contaminate at most 39 length-39 windows, so heavy contamination removes at most

`5*39 = 195`

boundary starts.

At most `38` preterminal boundary times are too close to the terminal index to support a full 39-transition window.

The pair-constrained weighted boundary certificate gives

`z >= 35,251,435,711`.

Hence the number `W_39` of complete, heavy-free, boundary-started 39-step windows obeys

`W_39 >= 35,251,435,711 - 195 - 38`

and therefore

`boxed: W_39 >= 35,251,435,478`.

## 3. Global upward-event count

Let

`G = #{0<=j<k : h_{j+1}=h_j+1}`.

Every clean 39-step window contains at least three such transitions, while a fixed transition belongs to at most 39 windows. Therefore

`3 W_39 <= 39 G`,

so

`G >= ceil(W_39/13)`.

Using the exact lower bound above,

`ceil(35,251,435,478 / 13) = 2,711,648,883`.

Thus

`boxed: G >= 2,711,648,883`.

Every upward transition satisfies `r_j-a_j=1`, hence necessarily

`boxed: r_j=2, a_j=1`.

So a first-candidate survivor must realize at least 2.711 billion exact `r=2,a=1` transitions.

Since `h_0=0` and `h_k=-1`, the total magnitude `D` of negative defect increments satisfies `D=G+1`. Hence

`boxed: D >= 2,711,648,884`.

## 4. Search boundary

The same finite class was also certified at window lengths 45, 44, 43, 42, 41, and 40 before the 39-step scan. The 39-step scan is the current shortest fully completed certificate.

A 38-step scan is substantially larger and has not yet been completed; no mathematical failure at 38 is claimed.

The next conceptual target is to combine the forced density of `r=2,a=1` events with the correction-weight budget or continued-fraction cycle structure, rather than relying only on further brute-force shortening.