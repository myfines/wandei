# At least 2.299 billion total defect upsteps in branch A

Status: exact consequence of the translated two-upstep finite certificate, the sharp heavy-return count, and the pair-constrained boundary lower bound. Not a Collatz proof.

## 1. Local certificate

`src/translated_two_total_upsteps_cert.py` covers every length-46 mechanical factor and every exact local valuation script satisfying

- the window starts at `h=0`;
- the next 46 transitions contain at most two total upward defect transitions `h -> h+1`;
- the rare heavy direct return `h=1,r=2,a=3` does not occur.

Because a defect increase is at most one per odd step and the path starts at zero, at most two total upsteps imply `h<=2` throughout the window. The certificate therefore enumerates all possible stay/down transitions from `h=0,1,2`, not merely the unit-defect class.

Using the sharp local boundary altitude interval

`2075*2^60 <= x < 6,287,967,883,654,920,544,295`,

the exact complete scan gives

- 47 mechanical factors;
- 2,184,132 exact scripts;
- 587,410 concrete local candidate rows;
- every row realizes its prescribed valuation prefix;
- every row falls below the verified frontier;
- latest fall: odd step 237;
- worst local seed: `4,810,798,976,564,215,475,307`;
- corresponding below-frontier endpoint: `1,869,158,857,707,769,661,911`;
- summary SHA256: `2fda262c322cbf4b179d50607cdda9e8d99444088d7ae906528f04af37f54c38`.

Hence, any surviving boundary-started 46-step window with no rare heavy return must contain at least **three** total defect upsteps.

## 2. Clean boundary-started windows

The sharp repayment phase certificate proves that the full first-candidate prefix contains at most five odd-height `r=2` direct repayments. In the present local class the only excluded heavy event is `h=1,r=2,a=3`, so at most five such transitions exist globally.

Each transition contaminates at most 46 length-46 windows. Thus at most

`5*46 = 230`

boundary-started windows are contaminated by a heavy event.

At most 45 preterminal boundary times are too close to the terminal index to support a complete 46-transition window.

The pair-constrained boundary certificate gives

`z >= 35,251,435,711`.

Therefore the number `W` of complete, heavy-free, boundary-started windows satisfies

`W >= 35,251,435,711 - 230 - 45`

and hence

`W >= 35,251,435,436`.

## 3. Global overlap count

Let

`G = #{0<=j<k : h_{j+1}=h_j+1}`

be the total number of upward defect transitions at every height.

Every clean window contains at least three such transitions. Counting incidences between clean windows and upward transitions gives

`3W <= 46G`,

because a fixed transition belongs to at most 46 length-46 windows.

Therefore

`G >= ceil(3W/46)`.

With the certified lower bound for `W`,

`ceil(3*35,251,435,436/46) = 2,299,006,659`.

Thus

`boxed: G >= 2,299,006,659`.

## 4. Arithmetic form of every charged event

The defect recurrence is

`h_{j+1}=h_j+r_j-a_j`,

where `r_j in {1,2}` and `a_j>=1`.

An upward transition requires

`r_j-a_j=1`.

Therefore every one of the at least 2,299,006,659 charged transitions has exactly

`boxed: r_j=2, a_j=1`.

This is stronger and cleaner than the earlier split charge `4V+U`: it counts the same local arithmetic event at every incoming defect height.

## 5. Immediate conservation consequence

Since `h_0=0` and the first contraction ends at `h_k=-1`, the total signed defect increment is `-1`.

Every upward transition contributes `+1`. Hence if `D` denotes the total magnitude of all negative defect increments, then

`G-D=-1`,

so

`boxed: D=G+1 >= 2,299,006,660`.

Thus a first-candidate survivor must contain at least 2.299 billion unit-or-larger repayment mass in addition to at least 2.299 billion exact `r=2,a=1` upward events.

The next target is to upper-bound the realizable density of these `r=2,a=1` events, or to show that the required repayment mass forces too many side-branch / high-altitude events.