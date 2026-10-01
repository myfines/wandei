# CURRENT STATUS — recovery checkpoint

Updated: 2026-10-01

This repository contains partial results and exact finite certificates only. There is **no claimed proof of Collatz**.

## 1. Coordinate and branch split

Use the odd-only Syracuse map

S(x)=(3x+1)/2^a,  a=v2(3x+1).

Assume a least positive counterexample N exists. Write

A_k=sum_{j<k} a_j,

h_k=floor(k log_2 3)-A_k,

r_k=floor((k+1)log_2 3)-floor(k log_2 3) in {1,2}.

Then

h_{k+1}=h_k+r_k-a_k.

### Branch A: first coefficient contraction

The first relevant candidate is

(k,A_k)=(72057431991,114208327604),

with certified seed window

2075*2^60 <= N < (4/3)*2^71

and sharper ceiling about 2^71.413083842.

### Branch B: escape

If the coefficient never contracts, h_k>=0 for all k. For a genuinely divergent orbit the current argument gives

h_k -> +infinity,

sum_k 2^(-h_k) < infinity.

Arithmetic realizability remains open.

## 2. Strongest exact progress in branch A

### Weighted boundary density

`src/pair_constrained_boundary_density_cert.py` certifies

z=#{0<=j<k:h_j=0} >= 35,251,435,711.

### Boundary-run cap

The chunked length-29 certificate checks all 30 mechanical factors and 1,553,424,384 exact local states in

2075*2^60 <= x < 2^73.

Every candidate falls below the verified frontier. Therefore every maximal boundary run has at most 29 states.

Consequences:

- boundary runs >= 1,215,566,749;
- departures h=0->1 >= 1,215,566,748;
- every such departure has r=2,a=1.

### Important erratum

The local exclusion `(21)^4` does **not** imply that one quarter of all excursions globally are non-cheap, because boundary waiting can occur between excursions. The old global non-cheap lower bounds are retracted. See `notes/2026-10-01-erratum-cheap-excursion-global-count.md`.

### Sharp odd-height repayment gate

Inside the fixed first candidate the correction product is so close to one that

epsilon=log_2(P_bar) < 1/60,000,000,000.

Every positive odd-height direct repayment at r=2 requires

theta_n={n log_2 3}>1-epsilon.

Denjoy--Koksma implies at most five such events in the whole 72,057,431,991-step prefix. In particular there are at most five heavy h=1,r=2,a=3 returns.

### Translation-invariant 46-step certificates

`src/translated_unit_excursion_cert.py` covers all 47 length-46 mechanical factors and excludes every boundary-started local path that stays in h in {0,1} with at most two upcrossings.

Stronger: `src/translated_noheavy_three_upcross_cert.py` covers all 47 factors and excludes every boundary-started length-46 path that

- stays in h in {0,1};
- has at most three upcrossings;
- contains no heavy h=1,r=2,a=3 return.

Exact strong scan:

- scripts: 12,024,283;
- candidate rows: 6,112,533;
- every candidate realizes its exact prefix;
- every candidate falls below the frontier;
- latest drop: odd step 276.

Hence every complete heavy-free boundary-started 46-step window must either

1. reach h>=2, or
2. contain at least four 0->1 upcrossings.

### Clean-window covering charge

At most five heavy returns contaminate at most 230 boundary-started 46-step windows. At most 45 boundary starts are too close to the terminal index. Thus

W >= 35,251,435,436

clean complete boundary windows obey the strong translated rule.

Define

U=#{j:h_j=0,h_{j+1}=1},

V=#{j:h_j=1,h_{j+1}=2}.

Both U and V are the same local valuation event r=2,a=1, distinguished only by incoming defect height.

Using the 29-state boundary-run cap to sharpen overlap multiplicities:

- a fixed U event belongs to at most 45 boundary-started 46-windows;
- a fixed V event belongs to at most 44 such windows.

Therefore

W <= 44V + (45/4)U,

and hence

boxed: 4V+U >= 3,133,460,928.

See `notes/2026-10-01-run-cap-improved-window-charge.md`.

This supersedes the older 3,065,342,212 charge bound.

### Convergent-cycle boundary adjacency

Let qU=6,586,818,670, qL=65,470,613,321 and sigma(n)=n+qU mod k.

`src/convergent_cycle_boundary_edges_cert.py` proves that the boundary set contains at least

1,134,940,229

sigma-edges with both endpoints on h=0.

`src/convergent_boundary_drift_cert.py` then proves that every boundary-boundary sigma edge except possibly the single edge 0->qU strictly decreases the actual Syracuse state in the sigma direction. Thus at least 1,134,940,228 of the forced B-B sigma edges are strict decreases.

See `notes/2026-10-01-convergent-cycle-boundary-edges.md` and `notes/2026-10-01-convergent-boundary-drift.md`.

### Terminal suffix

The older exact terminal-cylinder result gave k-m<=44 for the last return m to h=0 before h_k=-1.

Suffix rigidity says h_m=...=h_{k-1}=0. Combining this with the 29-state boundary-run cap gives the stronger exact result

boxed: k-m <=29,

so

m>=72,057,431,962.

See `notes/2026-10-01-last-boundary-within-29.md`.

## 3. Sampled mod-9 / prime-support structure

For consecutive sampled 2 mod 9 returns,

3^{q_j}s_j + eta_{j+1} = 2^{t_{j+1}}s_{j+1},

eta_j in {3,15,63}.

Committed consequences:

- gcd(s_j,s_{j+1}) divides eta_{j+1}; primes p>7 cannot divide consecutive cofactors;
- two-step recycling forces a discrete-log / multiplicative-order clock for 3/2 mod p;
- bounded sampled odd-run lengths imply fixed-P smooth cofactors have density zero;
- an escape tail faces an unbounded-spike / density-one prime-refresh dichotomy.

No contradiction is yet extracted from this branch.

## 4. Current main target

The cleanest unresolved Branch-A problem is now:

- lower bound: 4V+U >= 3,133,460,928;
- both U,V occur only on r=2,a=1 transitions;
- boundary weight and correction budget are already extremely constrained;
- more than 1.13 billion qU-cycle B-B pairs are forced, with almost all strictly descending in actual state.

The next useful theorem should upper-bound 4V+U from phase/correction structure, or convert the forced convergent-cycle boundary adjacency into an additional local restriction that strengthens the weighted optimization.

Do not return to the retracted global cheap-excursion frequency shortcut.

## 5. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-01-run-cap-improved-window-charge.md`
3. `src/translated_noheavy_three_upcross_cert.py`
4. `notes/2026-10-01-convergent-cycle-boundary-edges.md`
5. `src/convergent_boundary_drift_cert.py`
6. `notes/2026-10-01-convergent-boundary-drift.md`
7. `src/pair_constrained_boundary_density_cert.py`
8. `notes/2026-10-01-boundary-run-29.md`
9. `notes/2026-10-01-sharp-repayment-phase-gate.md`
10. `notes/2026-10-01-last-boundary-within-29.md`

These reconstruct the current state without relying on chat history.