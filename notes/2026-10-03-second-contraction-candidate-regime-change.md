# Second finite-contraction candidate: exact isolation and regime change

Status: exact arithmetic consequence of the upgraded verification frontier and continued-fraction geometry. Not a Collatz proof.

The first finite-contraction candidate

`(A,k)=(114208327604,72057431991)`

is already excluded by the published recursive-sufficiency frontier. The next question is the earliest later time at which a least counterexample could first have coefficient contraction.

## 1. Next candidate

Using the same Farey/continued-fraction geometry as `src/first_contraction_cert.py`, but with the stronger lower frontier

`F = 4*3^44+2`,

`src/second_contraction_candidate_cert.py` certifies that the next upper candidate is

`boxed: (A,k)=(217976794617,137528045312).`

The reason is quantitative. Any first contraction above the frontier obeys

`A/k - log_2 3 <= 1/(3 F log 2)`.

The closest exterior upper mediant after the eliminated first candidate is

`124648188195 / 78644250661`,

and its gap from `log_2 3` is already strictly larger than the allowed window. The next upper convergent

`217976794617 / 137528045312`

lies inside the window.

## 2. Mechanical seed ceiling

Write

`D = A log 2 - k log 3 > 0`.

For this candidate the exact log intervals give

`D ~= 8.9865487086179247e-13`.

Since

`k = 2*65470613321 + 6586818670`,

the mechanical correction sum splits into three convergent-denominator blocks. Denjoy-Koksma gives

`sum_{j<k} 2^{-theta_j} <= k/(2 log 2)+3`.

Using `e^D-1 >= D`, the same affine rescue argument as for the first candidate yields the rigorous upper bound

`N < N_upper`,

with

`log_2 N_upper ~= 74.962036844899...`.

By comparison, the imported verification frontier is

`log_2 F ~= 71.738350031731...`.

So this candidate is not swallowed by the present frontier.

## 3. Regime change in the correction budget

Survival only requires

`R > F/N_upper`.

The exact certificate gives

`boxed: F/N_upper ~= 0.107046771248413... < 1/2.`

This is qualitatively different from the first candidate, where the required correction ratio was above `0.76` and therefore forced a very large density of exact boundary states `h=0`.

When the survival threshold falls below `1/2`, the old worst-case weighted-average argument no longer forces any positive density of boundary contacts: an orbit could, at the level of that relaxation, spend essentially all of its time at defect one and still exceed the required correction ratio.

Therefore the historical first-candidate strategy

`high correction ratio -> huge boundary density -> many translated boundary windows`

cannot simply be transplanted to the second candidate.

## 4. Consequence for the research strategy

The second candidate requires a different global resource. The strongest current possibilities are:

1. optimize the full weighted defect distribution rather than only `h=0` density;
2. use several continued-fraction shifts simultaneously and seek a forced directed cycle of strict state-decrease edges;
3. exploit arithmetic realizability of long low-defect paths, not merely their correction weight;
4. strengthen the external verified frontier enough to swallow more finite-contraction candidates.

This note is specifically a warning against reusing first-candidate boundary-density constants outside their valid regime.
