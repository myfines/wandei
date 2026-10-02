# Exact-q overlap spectrum for boundary-started windows

Status: exact combinatorial theorem plus a branch-A diagnostic. Not a Collatz proof.

## 1. Universal overlap theorem

Fix a length `L` and a defect upstep at transition time `0`.

Consider boundary-started length-`L` windows containing that transition. Their possible start times are

`-(L-1), ..., 0`,

so there are exactly `L` possible starts.

Suppose a qualifying window contains exactly `q` total upsteps.

Let `s*=-(L-1)+r` be the earliest qualifying start, so the first `r` possible starts do not qualify.

The window beginning at `s*` ends at transition time `r`. Besides the fixed upstep at time `0`, at most `r` of its other upsteps can occur after time `0`, because only transitions `1,...,r` lie after the fixed transition inside this window.

Hence at least

`q-1-r`

of the other upsteps occur before time `0`.

Every upstep lands at a positive-defect, hence nonboundary, state. The target states of those `q-1-r` earlier upsteps lie strictly after `s*` and at or before time `0`, so they give `q-1-r` additional distinct possible start times that cannot qualify. They are disjoint from the first `r` nonqualifying starts by the definition of `s*`.

Therefore at least

`r + (q-1-r) = q-1`

of the `L` possible starts cannot qualify.

Thus any fixed upstep belongs to at most

`boxed: L-q+1`

boundary-started length-`L` windows containing exactly `q` upsteps.

For `L=46`, the exact-q overlap spectrum is therefore

- exact 4: at most 43 windows per upstep;
- exact 5: at most 42;
- exact 6: at most 41;
- ...;
- exact 46: at most 1.

The earlier exact-four `43` lemma is the case `q=4` of this theorem.

## 2. Fractional packing consequence

Inside branch A, the 29-state boundary-run certificate also gives the coarser total bound that one upstep belongs to at most 45 boundary-started 46-windows of all complexities combined.

Let `I_q` be the number of upstep/window incidences contributed by clean windows containing exactly `q` upsteps. Then

`sum_q I_q <= 45 G`,

while the exact-q overlap theorem gives

`I_q <= (47-q) G`.

The number of clean windows is

`W = sum_q I_q/q`.

For fixed `G`, maximizing `W` is a fractional knapsack problem: spend the total incidence budget first on the smallest allowed `q`, subject to each layer cap `(47-q)G`.

`src/exact_q_overlap_spectrum.py` performs this optimization with exact rational arithmetic.

With the current minimum local count `q>=4`, it recovers

`G/W >= 20/223`,

and with the 2026-10-02 live-frontier value

`W >= 35,260,566,218`

this gives

`boxed: G >= 3,162,382,621`.

## 3. Why pure local-window escalation is not enough

Every upstep has local arithmetic form

`r=2, a=1`.

In the first candidate,

`sum_{j<k} r_j = floor(k log_2 3) = 114,208,327,603`.

Since each `r_j` is 1 or 2, the exact number of `r=2` positions is

`114,208,327,603 - 72,057,431,991`

so

`boxed: # {r=2} = 42,150,895,612`.

Therefore always

`G <= 42,150,895,612`.

The exact overlap packing shows:

- if every clean 46-window had at least 39 upsteps, one would only get
  `G >= 40,394,462,617`, still compatible with the `r=2` supply;
- if every clean 46-window had at least 40 upsteps, then
  `G >= 52,802,848,259`, impossible.

Thus a strategy based **only** on successively proving `4,5,6,...` minimum upsteps per 46-window would need to reach the absurdly high threshold `40` before it could close branch A by simple event supply.

This is a strategic diagnostic: targeted exact-four/five certificates remain useful as auxiliary constraints, but they should not be the sole main line. A second global restriction on the same `r=2,a=1` events, or a coupling to repayment/correction/convergent-cycle structure, is necessary for a realistic closure.
