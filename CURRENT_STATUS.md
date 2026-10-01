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

### Boundary-run cap: 29 states

The chunked length-29 finite certificate checks all 30 mechanical factors and 1,553,424,384 exact local candidate states in

2075*2^60 <= x < 2^73.

Every candidate falls below the verified frontier; latest drop is odd step 341.

Therefore every maximal boundary run has at most 29 states. Hence

- boundary runs >= 1,215,566,749;
- departures h=0->1 >= 1,215,566,748;
- every departure has r=2,a=1.

### IMPORTANT ERRATUM

The local factor `(21)^4` is impossible, so at most three cheap `21 / a=12` excursions can occur **immediately back-to-back with no boundary waiting**.

This does not imply that one quarter of all excursions globally are non-cheap. Boundary waiting can occur between excursions. Therefore the old global lower bounds 181,702,471 and 303,891,687 non-cheap excursions are retracted.

See `notes/2026-10-01-erratum-cheap-excursion-global-count.md`.

### Three-step local structure

Every length-three mechanical departure word is 212 or 221.

- 212 has valuation pattern 113;
- 221 has valuation pattern 113 or 122.

Adjacency-only rotation caps:

- `(221)^2` impossible;
- `(212)^3` impossible;
- two adjacent 212 factors possible.

### Sharp repayment phase gate

Inside the fixed first candidate,

epsilon=log_2(P_bar) < 1/60,000,000,000.

Every positive odd-height direct repayment at r=2 requires

theta_n={n log_2 3} > 1-epsilon.

Denjoy--Koksma gives at most five such events in the whole 72,057,431,991-step prefix.

Thus there are at most five heavy `h=1,r=2,a=3` returns globally.

### Translation-invariant 46-step certificate: <=2 upcrossings

`src/translated_unit_excursion_cert.py` covers every length-46 mechanical factor. Starting from any boundary time h=0, the class

- h remains in {0,1};
- at most two upcrossings;

is completely excluded.

Exact scan:

- 47 factors;
- 2,896,739 scripts;
- 1,289,079 candidate rows;
- 1,141,211 distinct local seeds;
- latest drop below the frontier: odd step 237.

Therefore every surviving boundary-started 46-step window must reach h>=2 or contain at least three upcrossings.

### Strong translated 46-step certificate: <=3 upcrossings with no heavy return

`src/translated_noheavy_three_upcross_cert.py` strengthens the local class by allowing up to three upcrossings while excluding the rare heavy return `h=1,r=2,a=3`.

All 47 factors were exhaustively checked in chunks:

- scripts: 12,024,283;
- concrete candidate rows: 6,112,533;
- every candidate realizes its exact prefix;
- every candidate falls below the verified frontier;
- latest drop: odd step 276;
- worst local seed: 8171827952796853273339;
- endpoint: 697521228196614030223.

Hence every complete 46-step boundary window containing no heavy return must either

1. reach h>=2, or
2. contain at least four upcrossings.

### Global covering charge

At most five heavy returns contaminate at most 5*46=230 boundary-started 46-step windows. At most 45 additional boundary times are too close to the terminal index to start a complete window.

Thus at least

W >= 35,251,435,711 - 230 - 45 = 35,251,435,436

clean complete boundary windows obey the strong translated rule.

Let

H=#{0<=t<k : h_t>=2},

U=# {0<=j<k : h_j=0,h_{j+1}=1}.

A fixed high state belongs to at most 46 windows; a fixed upcrossing belongs to at most 46 windows. Therefore

W <= 46H + (46/4)U.

Equivalently,

boxed: 4H + U >= 3,065,342,212.

See `notes/2026-10-01-noheavy-three-upcross-covering.md`.

This bound explicitly allows boundary waiting and is independent of the retracted non-cheap frequency argument.

### Final repayment near the endpoint

Let m be the last return to h=0 before terminal h_k=-1. The exact terminal-cylinder certificate gives

k-m <=44,

so m>=72057431947.

## 3. Sampled mod-9 / prime-support structure

For consecutive sampled 2 mod 9 returns,

3^{q_j}s_j + eta_{j+1} = 2^{t_{j+1}} s_{j+1},

eta_j in {3,15,63}.

Committed consequences include:

- gcd(s_j,s_{j+1}) divides eta_{j+1}; primes p>7 cannot divide consecutive cofactors;
- two-step recycling forces a discrete-log / multiplicative-order clock for 3/2 mod p;
- bounded sampled odd-run lengths imply fixed-P smooth cofactors have density zero;
- an escape tail faces an unbounded-spike / density-one prime-refresh dichotomy.

No contradiction has yet been extracted from this branch.

## 4. Important cautions

1. Do not claim a Collatz proof from these certificates.
2. Do not promote local factor adjacency caps to global excursion-frequency bounds without explicitly modeling boundary waiting.
3. Pure mechanical/Sturmian shadowing alone is insufficient.
4. Finite computation is useful only for a mathematically complete finite class.
5. Generic multiplicative-order results do not automatically control orbit-generated primes.
6. Keep exact certificate claims separate from heuristic density intuition.

## 5. Best next target

Attack the new exact lower charge

4H+U >= 3,065,342,212

from the other side using the correction budget and rotation weights.

Every upcrossing forces a successor h=1 state, while every h>=2 state contributes at most one quarter of its mechanical correction weight. The next useful object is a phase-weighted Lagrange/finite-state optimization that gives an upper bound on 4H+U compatible with survival.

If that is too weak, enrich the charge with local phase classes rather than returning to the invalid cheap-excursion counting shortcut.

## 6. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-01-erratum-cheap-excursion-global-count.md`
3. `notes/2026-10-01-noheavy-three-upcross-covering.md`
4. `src/translated_noheavy_three_upcross_cert.py`
5. `notes/2026-10-01-translated-unit-excursion-certificate.md`
6. `src/translated_unit_excursion_cert.py`
7. `notes/2026-10-01-sharp-repayment-phase-gate.md`
8. `src/pair_constrained_boundary_density_cert.py`
9. `notes/2026-10-01-boundary-run-29.md`
10. `notes/2026-10-01-last-boundary-within-44.md`

These reconstruct the current proof state without relying on chat history.
