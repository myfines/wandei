# 2026-11-22 — Collatz argument audit and adversarial ClaimLab

**Status:** exact finite-state graph and positive-integer finite witnesses, NOT a Collatz proof. This is an optimization corollary of the earlier 15-state mod-27 hit potential on this branch; no mathematical novelty claim.

## Literature comparison

| Direction | What has been proved/verified | What is missing |
| --- | --- | --- |
| Terras and Tao density | Strong descent for almost all seeds in suitable density senses | Exceptional singleton not excluded |
| Krasikov–Lagarias inverse tree | Polynomial lower bounds on the number of seeds reaching 1 (classic exponent around 0.84) | Not a proof that every integer is in the basin |
| Bařina CPU/GPU | All seeds below 2075 × 2^60 checked as of 2026-11-22 | Finite cutoff is not a global bound |
| 2-adic / 3-adic / zeta spectra | Exact inverse rays, cylinders, phases, analytic transforms | Uniform compatibility for a *single fixed positive seed* over unbounded depth |
| Rewriting/Lean | Concrete 11-rule termination encodings and formal certificate checks | Some termination obligations remain open |
| Extreme stopping-time statistics | Helps identify hard finite examples | Regression/Haar averages are not pointwise theorems |

Sources: Tao https://arxiv.org/abs/1909.03562 ; Krasikov–Lagarias https://erdosproblems.ai/wiki/library/number_theory/krasikov_lagarias_2003_bounds_difference_inequalities ; Bařina https://pcbarina.fit.vut.cz/ ; formal-literature initiative https://ccchallenge.org/ ; statistical paper https://doi.org/10.3934/jdg.2026037 . Existing all-purpose CPU/GPU+SQLite platform: https://github.com/cosmintrica/CollatzLab .

## Precise new tool: exact 15-state refutation or potential certificate

Core script: src/collatz_claim_graph_audit.py . Independent regression suite: tests/test_collatz_claim_graph_audit.py .

Let A_k be total valuations of the first k Syracuse steps. H_k counts shortcut blocks that hit 20 mod27, and P_k counts adjacent pairs of such hit-bearing blocks. For user-chosen nonnegative prices λ,μ, test whether some C **independent of seed and horizon** satisfies:

    A_k >= k + λ H_k + μ P_k - C.

Build 15 states (n mod9, previous_hit) and a weighted transition graph with weights a-1-λh-μp. Its 204 representative edges are COMPLETE: once a passes the target threshold, replacing a with a+6 keeps next state/hit status but adds six to the cost.

- If no negative cycle: Bellman-Ford outputs an integer potential satisfying each edge inequality, hence a mathematically valid finite C for all real positive odd trajectories. This does **not** prove global Collatz convergence.
- If a negative cycle exists: return an exact repeated exponent word, its negative total weight, and a CRT-constructed **real positive odd integer finite orbit** witnessing any chosen finite number of repetitions. The positive initial seed may depend on repetition count. This does **not** exhibit an infinite divergent positive orbit.

## Sharp full nonnegative two-price frontier

The universal bounded-error inequality holds for all nonnegative real λ,μ **if and only if**

    λ <= 1 and λ + μ <= 5.

**Sufficiency:** the already-proved 15-state inequality says A_k >= k+H_k+4P_k-1. Since P_k <= H_k, every admissible λ,μ satisfies λH_k+μP_k <= H_k+4P_k, so C=1 works.

**Necessity:** for every finite q positive odd seeds realize (1,2)^q with (k,A,H,P)=(2q,3q,q,0), forcing λ<=1; also (6)^q with (k,A,H,P)=(q,6q,q,q-1), forcing λ+μ<=5. These finite witnesses do not share a fixed positive seed across arbitrarily many q.

The exact graph scan over integer 0<=λ<=3, 0<=μ<=8 yields **11 feasible** and **25 refuted** weight pairs, with fully checkable potential vectors or negative-cycle certificates.

## Why the numerical picture is not close to a global proof

A formal a=1, n≡8 mod9 nonhit cycle has growth multiplier 3/2 and zero local phase cost. On positive integers it can be shadowed for arbitrary finite depths, but its only infinite fixed exponent-1 seed is the negative 2-adic integer -1. Purely bounded finite-state observables cannot rule out this ghost at every depth; a genuinely unbounded Archimedean height or fixed-seed carry compatibility theorem is needed.

## Reproduce

- Run: python src/collatz_claim_graph_audit.py --lambda-price 1 --mu-price 4
- Counterexample: python src/collatz_claim_graph_audit.py --lambda-price 1 --mu-price 5
- Frontier: python src/collatz_claim_graph_audit.py --frontier
- Tests: python -m unittest discover -s tests -p test_collatz_claim_graph_audit.py -v

The downloadable full ClaimLab package adds a self-contained offline HTML dashboard, SQLite steps/claims database, exact JSON certificates, SHA256 digest and 11 passing tests. It sampled 5001 odd seeds <=10001 and 153400 actual odd steps. This finite dataset has no infinite implication.
