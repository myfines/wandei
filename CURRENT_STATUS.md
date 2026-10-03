# CURRENT STATUS — recovery checkpoint

Updated: 2026-10-03

This repository contains partial results and exact finite certificates only. There is **no claimed proof of Collatz**.

## 1. Coordinates

Use the odd-only Syracuse map

S(x)=(3x+1)/2^a,  a=v2(3x+1),

with

A_k=sum_{j<k} a_j,

h_k=floor(k log_2 3)-A_k,

r_k=floor((k+1)log_2 3)-floor(k log_2 3) in {1,2},

so

h_{k+1}=h_k+r_k-a_k.

Assume a least positive counterexample exists.

## 2. Finite-contraction route

### First candidate — CLOSED

The first isolated continued-fraction candidate is

(A,k)=(114208327604,72057431991).

For this candidate `src/first_contraction_cert.py` proves

N < (4/3)*2^71.

Ansari (NNTDM 31(3), 2025, Proposition 3.2 and Remark 3.1) upgrades the verified range below `2^71` to

L=4*3^44+2.

`src/ansari_frontier_bridge_cert.py` checks exactly that

2*3^44+1 < 2^71

and

(4/3)*2^71 < 4*3^44+2.

Therefore the entire first candidate is impossible for a least counterexample.

See `notes/2026-10-03-branch-a-closed-by-recursive-sufficiency-frontier.md` (title retained historically; content corrected to first-candidate closure).

Audit note: Lemma 3.2 in the paper appears to omit the element `3` from its displayed intersection parametrization. Adding `{3}` repairs the statement and does not affect Proposition 3.2 or the interval gap used here.

### Later candidates — OPEN

Eliminating the first candidate does **not** imply coefficient contraction can never occur. A hypothetical counterexample may remain noncontracting at k=72,057,431,991 and first contract later.

The next natural upper convergent candidate is

(A,k)=(217976794617,137528045312).

The finite-contraction machinery should now be restarted using the stronger lower frontier

N >= 4*3^44+2.

Historical first-candidate tools remain reusable templates:

- weighted defect/boundary optimization;
- boundary-run finite certificates;
- sharp repayment phase gates;
- translated local certificates;
- convergent-cycle adjacency/drift;
- terminal suffix rigidity.

Important erratum remains in force: do not infer a global non-cheap-excursion fraction from the local `(21)^4` exclusion.

## 3. Genuine no-contraction escape route — OPEN

If coefficient contraction never occurs, then

h_k>=0 for all k.

For a genuinely divergent orbit the current argument gives

h_k -> +infinity,

sum_k 2^(-h_k) < infinity.

For consecutive sampled `2 mod 9` returns,

3^{q_j}s_j + eta_{j+1} = 2^{t_{j+1}}s_{j+1},

eta_j in {3,15,63}.

Committed consequences:

- primes p>7 cannot divide consecutive sampled cofactors;
- two-step recycling forces a discrete-log / multiplicative-order clock for 3/2 mod p;
- fixed-gap recycling forces recycled p>7 to divide an explicit correction integer D_{j,m};
- bounded sampled odd-run lengths imply fixed-P smooth cofactors have density zero;
- the escape tail faces an unbounded-spike / density-one prime-refresh dichotomy.

`notes/2026-10-02-grh-diagnostic.md` explains why GRH is not currently the missing key: the unresolved issue is deterministic concentration of orbit-generated prime factors, not the generic distribution of multiplicative orders over all primes.

## 4. Current main targets

1. **Second finite-contraction candidate:** rebuild the first-candidate exact machinery at k=137,528,045,312 using the upgraded frontier `4*3^44+2`.
2. **Multi-convergent descent graph:** use more than one continued-fraction shift; if a dense boundary set is forced to contain a directed cycle of strict state-decrease edges, contradiction is immediate.
3. **Weighted correction LP:** optimize the actual correction ratio over a finite-state/path relaxation instead of only counting upsteps. The survival threshold is a direct weighted-average constraint, so a dual LP certificate could close a candidate without eliminating all local pattern classes individually.
4. **Escape branch:** split into unbounded sampled spikes versus bounded-run prime refresh and attack each separately.

## 5. Files to read first after context loss

1. `CURRENT_STATUS.md`
2. `notes/2026-10-03-branch-a-closed-by-recursive-sufficiency-frontier.md`
3. `src/ansari_frontier_bridge_cert.py`
4. `src/first_contraction_cert.py`
5. `notes/2026-10-01-prime-turnover-clock.md`
6. `notes/2026-10-02-grh-diagnostic.md`

These reconstruct the current state without relying on chat history.
