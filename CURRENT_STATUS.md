# CURRENT STATUS — recovery checkpoint

Updated: 2026-10-01

This is the compact recovery point for future chats/agents. The repository contains partial results and exact finite certificates only; there is **no claimed proof of Collatz**.

## 1. Main coordinate and branch split

Use the odd-only Syracuse map

S(x)=(3x+1)/2^a,  a=v2(3x+1).

Assume for contradiction that a least positive counterexample N exists. Write

A_k=sum_{j<k} a_j,

h_k=floor(k log_2 3)-A_k,

r_k=floor((k+1)log_2 3)-floor(k log_2 3) in {1,2}.

Then exactly

h_{k+1}=h_k+r_k-a_k.

Two branches remain.

### A. First coefficient-contraction branch

The first relevant continued-fraction candidate is

(k,A_k)=(72057431991,114208327604).

The certified seed window is

2075*2^60 <= N < (4/3)*2^71,

with a sharper ceiling about 2^71.413083842.

### B. Escape branch

If the coefficient never contracts, h_k>=0 for all k. For a genuinely divergent orbit the current reciprocal/correction argument gives

h_k -> +infinity,

sum_k 2^(-h_k) < infinity.

Arithmetic realizability remains open.

## 2. Strongest exact progress in branch A

### Pair-constrained weighted boundary density

`src/pair_constrained_boundary_density_cert.py` certifies

z=#{0<=j<k : h_j=0} >= 35,251,435,711.

This supersedes the older 25,438,346,005 / 35.3% boundary count.

### Boundary-run cap: 29 states

The chunked length-29 finite certificate checks all 30 mechanical factors and all exact local seed lifts in

2075*2^60 <= x < 2^73.

Aggregate exact scan:

- local candidate states: 1,553,424,384;
- every candidate falls below the verified frontier;
- latest drop: odd step 341;
- worst local seed: 8522726957776383649659.

Therefore no first-candidate prefix can contain 30 consecutive boundary states. Every maximal boundary run has at most 29 states.

Combining with the boundary count gives

- boundary runs >= 1,215,566,749;
- actual departures h=0->1 >= 1,215,566,748.

Every departure is forced to satisfy r=2,a=1.

### IMPORTANT ERRATUM: no global one-quarter non-cheap count

A cheap immediate excursion is

h: 0->1->0,

mechanical letters 21,

valuations 12.

The exact rotation lemma proves `(21)^4` is impossible, so at most three cheap excursions can occur **immediately back-to-back with no boundary waiting transitions**.

It does **not** follow that one out of every four excursions in the global excursion sequence is non-cheap, because after a return the orbit may remain at h=0 for several mechanical transitions before the next departure.

Therefore the previously quoted global lower bounds

- 181,702,471 non-cheap excursions, and
- 303,891,687 non-cheap excursions

are retracted. See `notes/2026-10-01-erratum-cheap-excursion-global-count.md`.

The 29-state run cap and 1,215,566,748 departure lower bound remain valid.

### Three-step local classification

Every length-three mechanical departure word is exactly 212 or 221.

The valuation patterns are:

- 212: only 113;
- 221: either 113 or 122.

The local rotation repetition caps are also adjacency statements only:

- `(221)^2` is impossible;
- `(212)^3` is impossible;
- two immediately consecutive 212 factors are possible.

### Sharp repayment phase gate

Inside the fixed first candidate the full correction product obeys

P_n <= P_bar = 3N0/(3N0-k),

with

epsilon=log_2(P_bar) < 1/60,000,000,000.

If h_n is positive odd, r_n=2, and one step repays the whole defect to zero, then necessarily

theta_n={n log_2 3} > 1-epsilon.

Denjoy--Koksma over the full candidate gives at most five such phases in all 72,057,431,991 steps.

Therefore there are at most five odd-height r=2 direct repayments globally. In particular, genuine 212/113 three-step excursions occur at most five times in the entire first-candidate prefix.

### Translation-invariant 46-step low-complexity exclusion

`src/translated_unit_excursion_cert.py` generalizes the old phase-zero 46-step certificate to **every** boundary phase.

For any boundary time m with h_m=0, suppose the next 46 odd steps stay in h in {0,1} and make at most two upcrossings 0->1. The certificate enumerates the complete finite class:

- all 47 length-46 mechanical factors;
- 2,896,739 exact low-complexity scripts (including pure mechanical scripts);
- 1,289,079 concrete candidate rows in [2075*2^60,2^73);
- 1,141,211 distinct local seeds.

Every candidate row realizes its prescribed valuation prefix, and every distinct local seed falls below the verified frontier. Latest fall: odd step 237, from

4810798976564215475307

to

1869158857707769661911 < 2075*2^60.

Digests:

- row SHA256: `bef8f2e5b0dd6f6881a648f52cbe14f991648ba9586100bfd438c9f48b688982`;
- descent SHA256: `24eaa38073ec1139faf01b2cfa741b9de1ef1a7413fd035ed2634963347a6159`.

Thus from every boundary contact of a surviving first-candidate orbit, within the next 46 odd steps one must either

1. reach h>=2, or
2. make at least three new 0->1 upcrossings.

This result is independent of the retracted non-cheap counting argument.

### Final repayment near the endpoint

Let m be the last return to h=0 before terminal h_k=-1. The exact terminal-cylinder certificate gives

k-m <= 44,

so

m >= 72057431947.

Thus a survivor must continue returning to the critical boundary until the final 44 odd steps.

## 3. Current computation in progress

A stronger translated 46-step class has now been exhaustively checked in chunks locally:

- defect restricted to h in {0,1};
- at most three upcrossings;
- no `h=1,r=2,a=3` heavy return inside the window.

All 47 mechanical factors were checked with no counterexample among 12,024,283 scripts and 6,112,533 concrete candidate rows. The worst observed candidate falls below the frontier at odd step 276.

This result is not yet the primary committed certificate until its chunkable source and aggregate note are added to the repository. If committed, it will imply that every 46-step boundary window containing no rare heavy return must either reach h>=2 or contain at least four upcrossings.

Because the sharp phase gate allows at most five heavy-return events globally, only finitely many boundary windows can be contaminated by them.

## 4. Sampled mod-9 / prime-support structure

For consecutive sampled 2 mod 9 returns,

3^{q_j}s_j + eta_{j+1} = 2^{t_{j+1}} s_{j+1},

eta_j in {3,15,63}.

Committed consequences include:

- gcd(s_j,s_{j+1}) divides eta_{j+1}; primes p>7 cannot divide consecutive cofactors;
- two-step recycling forces a discrete-log / multiplicative-order clock for 3/2 mod p;
- bounded sampled odd-run lengths imply fixed-P smooth cofactors have density zero;
- an escape tail therefore faces an unbounded-spike / density-one prime-refresh dichotomy.

No contradiction has yet been extracted from this branch.

## 5. Important cautions

1. Do not claim a Collatz proof from these certificates.
2. Do not promote a local factor adjacency cap to a global excursion-frequency bound unless boundary waiting is explicitly modeled.
3. Pure mechanical/Sturmian shadowing alone is insufficient; integer seeds can shadow finite critical scripts.
4. Finite computation is useful only for a mathematically complete finite class.
5. Generic multiplicative-order results do not automatically control orbit-generated primes.
6. Keep exact certificate claims separate from heuristic density intuition.

## 6. Best next target

First commit and independently reproducibly package the stronger no-heavy/three-upcrossing translated 46-step certificate.

Then exploit it globally with a correct covering/charging argument that includes boundary waiting. The sharp phase gate gives at most five heavy returns, so almost every boundary-started 46-step window should obey the stronger local rule.

The desired bridge is a rigorous lower bound on either

- occupation times with h>=2, or
- upcrossing events,

with overlap counted explicitly rather than through excursion adjacency.

## 7. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-01-erratum-cheap-excursion-global-count.md`
3. `notes/2026-10-01-translated-unit-excursion-certificate.md`
4. `src/translated_unit_excursion_cert.py`
5. `notes/2026-10-01-sharp-repayment-phase-gate.md`
6. `src/pair_constrained_boundary_density_cert.py`
7. `notes/2026-10-01-boundary-run-29.md`
8. `notes/2026-10-01-last-boundary-within-44.md`
9. `notes/2026-10-01-prime-turnover-clock.md`

These reconstruct the current proof state without relying on chat history.
