# CURRENT STATUS — recovery checkpoint

Updated: 2026-10-02

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

2075*2^60 <= N < (4/3)*2^71.

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

The chunked length-29 certificate checks all 30 mechanical factors and 1,553,424,384 exact local states in the certified local state interval. Every candidate falls below the verified frontier.

Therefore every maximal boundary run has at most 29 states.

Consequences:

- boundary runs >= 1,215,566,749;
- departures h=0->1 >= 1,215,566,748;
- every such departure has r=2,a=1.

### Sharp odd-height repayment gate

Inside the fixed first candidate,

epsilon=log_2(P_bar) < 1/60,000,000,000.

Every positive odd-height direct repayment at r=2 requires theta_n>1-epsilon. Denjoy--Koksma implies at most five such events in the whole first-candidate prefix.

### Translated finite certificates

The 46-step translated certificates cover all 47 mechanical factors. In particular:

- `src/translated_noheavy_three_upcross_cert.py` excludes the clean low-height class with at most three U=0->1 upcrossings;
- the targeted height-2/height-3 certificates exclude all clean windows with only three total upsteps;
- `src/translated_h1_exact_four_u_cert.cpp` excludes the remaining clean low-height class with exactly four U transitions.

Hence every clean complete boundary-started 46-step window satisfies:

1. if it stays in h<=1, it contains at least five U transitions;
2. if it reaches h>=2, it necessarily contains at least one U followed later by at least one V=1->2 transition.

At most five rare heavy returns contaminate at most 230 starts, and at most 45 starts are terminally incomplete. Therefore

W >= 35,251,435,436

clean 46-step boundary windows remain.

Using the 29-state boundary-run cap:

- a fixed U can lie in at most 45 boundary-started 46-windows;
- a fixed V can lie in at most 44 such windows.

Charging each low window by five U's and each high window by one U plus one V gives

5W <= 45U + 176V <= 45(U+4V).

Therefore

boxed: U + 4V >= 3,916,826,160.

See `notes/2026-10-02-five-u-or-v-covering.md`.

This supersedes the older 4V+U >= 3,133,460,928 bound as the strongest simple U/V charge currently recorded.

### Total upstep count

Independent targeted certificates also imply every clean 46-step window contains at least four total defect upsteps. Thus, with overlap control,

G=#{j:h_{j+1}=h_j+1} >= 3,133,460,928.

Every upstep has exact local form r=2,a=1. Since h_0=0 and h_k=-1, total repayment mass is G+1.

### Convergent-cycle boundary adjacency and drift

Let qU=6,586,818,670, qL=65,470,613,321 and sigma(n)=n+qU mod k.

The exact cycle certificate forces at least

1,134,940,229

sigma-edges with both endpoints on h=0.

The exact drift certificate proves every such B-B edge except possibly 0->qU strictly decreases the actual Syracuse state in the sigma direction. Hence at least 1,134,940,228 forced B-B sigma edges are strict decreases.

### Terminal suffix

Combining terminal rigidity with the 29-state boundary-run cap gives

boxed: k-m <=29,

so the final return to h=0 occurs within the last 29 odd steps.

### Important erratum

Do **not** infer a global non-cheap-excursion fraction from the local `(21)^4` exclusion. Boundary waiting breaks that inference. The old global non-cheap counts are retracted.

## 3. Branch B prime-turnover structure

For consecutive sampled 2 mod 9 returns,

3^{q_j}s_j + eta_{j+1} = 2^{t_{j+1}}s_{j+1},

eta_j in {3,15,63}.

Committed consequences:

- primes p>7 cannot divide consecutive sampled cofactors;
- two-step recycling forces a discrete-log clock for 3/2 mod p;
- bounded sampled odd-run lengths imply fixed-P smooth cofactors have density zero;
- the escape tail faces an unbounded-spike / density-one prime-refresh dichotomy.

`notes/2026-10-02-grh-diagnostic.md` records why GRH is not presently the missing key: Artin/GRH can control multiplicative orders over all primes, but the unresolved issue is deterministic concentration of orbit-generated prime factors. Short-gap recycling is already finitely constrained without GRH.

## 4. Current main target

The best unconditional Branch-A targets are now:

1. upper-bound the realizable density of the exact upstep event r=2,a=1 strongly enough to contradict G>=3,133,460,928 or U+4V>=3,916,826,160;
2. convert the >1.13 billion strictly descending qU-cycle B-B edges into an additional global restriction;
3. continue targeted exclusion of exact-four-upstep pattern classes rather than brute-force the full four-upstep state space.

Do not return to the retracted cheap-excursion shortcut. Do not make GRH a prerequisite unless a genuinely orbit-sensitive prime concentration theorem is found.

## 5. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-02-five-u-or-v-covering.md`
3. `notes/2026-10-01-four-total-upsteps-covering.md`
4. `src/translated_h1_exact_four_u_cert.cpp`
5. `notes/2026-10-01-convergent-cycle-boundary-edges.md`
6. `notes/2026-10-01-convergent-boundary-drift.md`
7. `src/pair_constrained_boundary_density_cert.py`
8. `notes/2026-10-01-boundary-run-29.md`
9. `notes/2026-10-01-sharp-repayment-phase-gate.md`
10. `notes/2026-10-02-grh-diagnostic.md`

These reconstruct the current state without relying on chat history.
