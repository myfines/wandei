# CURRENT STATUS — recovery checkpoint

Updated: 2026-10-03

This repository contains partial results and exact finite certificates only. There is **no claimed proof of Collatz**.

## 1. Coordinate and branch split

Use the odd-only Syracuse map

S(x)=(3x+1)/2^a,  a=v2(3x+1).

Assume a least positive counterexample N exists. Write

A_k=sum_{j<k} a_j,

h_k=floor(k log_2 3)-A_k,

r_k=floor((k+1)log_2 3)-floor(k log_2 3) in {1,2},

so

h_{k+1}=h_k+r_k-a_k.

Two branches arise.

### Branch A: first coefficient contraction — CLOSED

The first relevant candidate is

(k,A_k)=(72057431991,114208327604),

and the internal first-contraction analysis gives the rigorous coarse seed bound

N < (4/3)*2^71.

A 2025 published theorem of Mohammad Ansari (*Recursive sufficiency for the Collatz conjecture and computational verification*, NNTDM 31(3), Proposition 3.2 and Remark 3.1) upgrades the verified frontier 2^71 to

L = 4*3^44 + 2.

`src/ansari_frontier_bridge_cert.py` checks exactly that

2*3^44+1 < 2^71

and

(4/3)*2^71 < 4*3^44+2.

Therefore every possible Branch-A seed lies below a published verified frontier, so no least counterexample can enter Branch A.

See `notes/2026-10-03-branch-a-closed-by-recursive-sufficiency-frontier.md`.

Audit note: Lemma 3.2 in the paper appears to omit the element 3 from the displayed parametrization of the infinite intersection; adding `{3}` repairs the statement and does not affect Proposition 3.2 or the gap `(N,2N]` used here. The recursive-set closure steps in Lemma 3.1 were checked and no obstruction to Proposition 3.2 was found.

### Branch B: escape — OPEN

If the coefficient never contracts, then

h_k>=0 for all k.

For a genuinely divergent orbit the current argument gives

h_k -> +infinity,

sum_k 2^(-h_k) < infinity.

Arithmetic realizability remains open. This is now the sole main branch.

## 2. Historical Branch-A work retained in the repository

The following exact results remain useful as techniques and consistency checks, but they are no longer needed to close Branch A:

- pair-constrained weighted boundary density;
- boundary-run cap of 29 states;
- sharp odd-height repayment phase gate;
- translated 39/41/46-step finite certificates;
- exact-four upstep pattern classifications;
- convergent-cycle boundary adjacency and strict state drift;
- terminal suffix rigidity.

Important erratum remains in force: do **not** infer a global non-cheap-excursion fraction from the local `(21)^4` exclusion, because boundary waiting breaks that inference.

## 3. Branch B prime-turnover structure

For consecutive sampled 2 mod 9 returns,

3^{q_j}s_j + eta_{j+1} = 2^{t_{j+1}}s_{j+1},

eta_j in {3,15,63}.

Committed consequences:

- primes p>7 cannot divide consecutive sampled cofactors;
- two-step recycling forces a discrete-log / multiplicative-order clock for 3/2 mod p;
- for any fixed recycle gap m, a recycled prime p>7 must divide an explicit correction integer D_{j,m};
- bounded sampled odd-run lengths imply fixed-P smooth cofactors have density zero;
- the escape tail faces an unbounded-spike / density-one prime-refresh dichotomy.

`notes/2026-10-02-grh-diagnostic.md` records why GRH is not presently the missing key: Artin/GRH can control multiplicative orders over all primes, but the unresolved issue is deterministic concentration of orbit-generated prime factors. Short-gap recycling is already finitely constrained without GRH.

## 4. Current main target

With Branch A closed, all effort should move to Branch B.

The best current split is:

1. **unbounded-spike branch:** q_j is unbounded. Exploit the resulting increasingly long odd runs and the forced simultaneous 2-adic / 3-adic alignment;
2. **bounded-run prime-refresh branch:** q_j is eventually bounded. Then large prime factors must refresh on a density-one set of sampled times. Combine this with the multiplicative-order clock, S-unit finiteness, and correction summability to rule out indefinite escape.

The desired next theorem is an orbit-sensitive prime-refresh obstruction, or a direct contradiction between `h_k -> infinity`, `sum 2^(-h_k)<infinity`, and the sampled recurrence.

Do not spend more computation on exact-four Branch-A windows unless independently auditing the historical certificate machinery.

## 5. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-03-branch-a-closed-by-recursive-sufficiency-frontier.md`
3. `src/ansari_frontier_bridge_cert.py`
4. `notes/2026-10-01-prime-turnover-clock.md`
5. `notes/2026-10-02-grh-diagnostic.md`
6. the Branch-B escape/summability notes and sampled mod-9 recurrence notes.

These reconstruct the current state without relying on chat history.
