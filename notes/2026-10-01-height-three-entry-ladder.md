# Third translated height ladder: force h>=4 or repeat an upward entry level

Status: exact finite certificate in the first coefficient-contraction branch. Not a Collatz proof.

## 1. Finite class

Start at an arbitrary boundary time `h=0`. Over the next 46 odd-only transitions impose

- every defect state stays in `{0,1,2,3}`;
- each upward entry `0->1`, `1->2`, `2->3` occurs at most once;
- no positive odd-height direct repayment to `h=0` at an `r=2` step occurs.

The excluded odd-height direct repayments are exactly the rare class controlled by `src/sharp_repayment_phase_cert.py`, which allows at most five such events in the entire first-candidate prefix.

`src/translated_h3_single_entry_cert.cpp` covers all 47 length-46 mechanical factors and intersects every exact valuation script with

`2075*2^60 <= x < 2^73`.

Exact aggregate scan:

- scripts: `67,075,614`;
- concrete candidate rows: `35,382,699`;
- every row realizes its exact prescribed valuation prefix;
- every candidate falls below the verified frontier;
- latest fall: odd step `259`;
- worst seed: `4780127247684938901371`;
- endpoint: `848117883565327063261`.

The deterministic certification stdout has SHA256

`74ace83af13df9e889c755e975d4c5a02d53535f096f13375cce932f873354fd`.

## 2. Local consequence

Every complete 46-step boundary-started window containing no rare odd-height `r=2` direct repayment must satisfy at least one of

1. it reaches `h>=4`;
2. it contains at least two `0->1` entries;
3. it contains at least two `1->2` entries;
4. it contains at least two `2->3` entries.

This is translation-invariant in mechanical phase and permits arbitrary boundary waiting.

## 3. Global charge

As before, at least

`W >= 35,251,435,436`

boundary-started length-46 windows are complete and uncontaminated by the globally at-most-five rare odd-height direct repayments.

Define

- `U=#(0->1)`;
- `V=#(1->2)`;
- `T=#(2->3)`;
- `Q=#(3->4)`.

A clean window reaching `h>=4` contains a `3->4` entry. Each transition belongs to at most 46 length-46 windows. Partitioning windows by the alternatives above gives

`W <= 46 Q + 23(U+V+T)`.

Therefore

`boxed: 2Q + T + V + U >= ceil(W/23)`.

With the certified W,

`boxed: 2Q + T + V + U >= 1,532,671,106`.

Every upward entry `h->h+1` again has the same exact arithmetic form

`r=2, a=1`.

## 4. Combined lower bound on upward defect jumps

The independent committed inequalities now include

1. `U >= 1,215,566,748` from the 29-state boundary-run cap;
2. `4V+U >= 3,065,342,212` from the first translated covering layer;
3. `6T+3V+2U >= 4,598,013,318` from the height-two layer;
4. `2Q+T+V+U >= 1,532,671,106` from this height-three layer.

A continuous linear-program relaxation already implies

`U+V+T+Q >= 1,807,935,318`.

Since all variables are integers, the exact integer lower bound is at least this ceiling. This means a first-candidate survivor must contain more than 1.8 billion upward unit defect transitions among the first four levels alone, and every one is an `r=2,a=1` valuation event.

The LP number is a derived summary rather than a new finite scan; future work should encode its exact rational dual certificate if it becomes important downstream.

## 5. Next target

Blindly extending to unrestricted `h<=4` will grow the script class rapidly. Better next steps are

- derive a rational dual certificate for the combined ladder inequalities;
- exploit the fact that every upward entry is `r=2,a=1` against phase/continued-fraction structure;
- combine the ladder with the convergent-cycle result forcing at least `1,134,940,229` adjacent boundary pairs under the qU shift.
