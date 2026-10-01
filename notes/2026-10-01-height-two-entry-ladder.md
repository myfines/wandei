# Second translated height ladder: force h>=3, two 1->2 entries, or three 0->1 entries

Status: exact finite certificate in the first coefficient-contraction branch. Not a Collatz proof.

This is the next layer above `translated_noheavy_three_upcross_cert.py`.

## 1. Finite class

Start at an arbitrary boundary time with `h=0`. Consider the next 46 odd-only transitions and impose

- every defect state remains in `{0,1,2}`;
- at most two transitions `0->1` occur;
- at most one transition `1->2` occurs;
- no rare heavy direct return `h=1,r=2,a=3` occurs.

`src/translated_h2_one_entry_cert.cpp` enumerates this class for all 47 length-46 mechanical factors.

The scan uses exact 2-adic seed cylinders and the rigorous local boundary interval

`2075*2^60 <= x < 2^73`.

Exact aggregate result:

- scripts: `59,605,715`;
- concrete candidate rows: `30,702,092`;
- every concrete row realizes its prescribed valuation prefix;
- every candidate falls below the verified frontier;
- latest fall: odd step `262`;
- worst seed: `3345476547508506755675`;
- endpoint: `2003311712042859815183 < 2075*2^60`.

The deterministic full-run stdout obtained during certification has SHA256

`6621a6e003c9845da955e0717f03c7db896e293a6f76632b96464a81177d69b6`.

## 2. Local consequence

Therefore every complete 46-step boundary-started window containing no rare heavy return must satisfy at least one of

1. it reaches `h>=3`;
2. it contains at least two transitions `1->2`;
3. it contains at least three transitions `0->1`.

This conclusion is translation-invariant in the mechanical phase and explicitly permits arbitrary boundary waiting.

## 3. Global covering charge

As in the previous covering note, at least

`W >= 35,251,435,436`

boundary-started length-46 windows are complete and free of the at-most-five heavy-return events.

Define

- `U = # {j : h_j=0, h_{j+1}=1}`;
- `V = # {j : h_j=1, h_{j+1}=2}`;
- `T = # {j : h_j=2, h_{j+1}=3}`.

A clean window reaching `h>=3` contains a first `2->3` entry. A fixed transition belongs to at most 46 length-46 windows. Partitioning clean windows by the three alternatives above gives

`W <= 46 T + (46/2) V + (46/3) U`.

Multiplying by `6/46` gives

`6T + 3V + 2U >= ceil(3W/23)`.

Using the certified lower bound on W,

`boxed: 6T + 3V + 2U >= 4,598,013,318`.

## 4. Common arithmetic form of all three entry events

For every upward unit transition

`h -> h+1`,

the recurrence

`h_{j+1}=h_j+r_j-a_j`

forces

`r_j-a_j=1`.

Since `r_j in {1,2}` and `a_j>=1`, necessarily

`boxed: r_j=2, a_j=1`.

Thus U, V and T are not three unrelated event types. They are the same valuation event `r=2,a=1`, distinguished only by incoming defect height 0, 1 or 2.

This produces a genuine height ladder: the translated local certificates force a large global population of `r=2,a=1` upward defect entries spread across successive defect levels.

## 5. Next target

There are now two independent global structures to combine:

1. the height-entry charge
   `6T+3V+2U >= 4,598,013,318`;
2. the convergent-cycle boundary adjacency lower bound
   `e >= 1,134,940,229`.

The next useful step is to exploit the exact near-unit drift over qU/qL blocks or derive the third height layer without enumerating an uncontrolled `h<=3` state space.
