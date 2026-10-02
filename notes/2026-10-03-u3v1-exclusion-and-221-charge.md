# Excluding the U3V1 exact-four class and strengthening the global charge

Status: exact finite-certificate consequence inside branch A. Not a Collatz proof.

Let a clean 46-step window be a complete boundary-started window containing no globally rare positive odd-height direct repayment at an r=2 step.

Write the upstep counts by incoming height as

- U = #(0->1),
- V = #(1->2),
- T = #(2->3),
- Q = #(3->4), etc.

The exact-four height-pattern classification has eight possibilities:

U4, U3V1, U2V2, U1V3, U2V1T1, U1V2T1, U1V1T2, U1V1T1Q1.

The U4 class was already excluded by `src/translated_h1_exact_four_u_cert.cpp`.

## 1. Exact U3V1 certificate

`src/translated_h2_three_u_one_v_cert.cpp` exhausts every length-46 mechanical factor and every exact valuation/defect script satisfying

- start at h=0;
- stay in {0,1,2};
- exactly three U entries 0->1;
- exactly one V entry 1->2;
- no rare clean-excluded h=1,r=2 direct repayment to h=0.

The scan uses the conservative local interval

`2075*2^60 <= x < 6,287,967,883,654,920,544,295`,

so it remains valid after the later live-frontier upgrade.

Exact aggregate over all 47 Sturmian factors:

- defect/valuation scripts: `832,402,470`;
- concrete local seed rows: `247,899,900`;
- every row realizes its prescribed prefix;
- every row falls below the old verified frontier `2075*2^60`;
- latest fall: odd step `304`;
- worst seed: `5,727,473,727,383,584,829,487`;
- below-frontier endpoint: `1,271,471,526,915,619,774,637`.

Therefore no surviving clean 46-step boundary window can have exact-four pattern U3V1.

## 2. Consequence for positive-height upsteps

After excluding U4 and U3V1, every remaining exact-four pattern contains at least two upsteps whose source has positive defect:

- U2V2: 2;
- U1V3: 3;
- U2V1T1: 2;
- U1V2T1: 3;
- U1V1T2: 3;
- U1V1T1Q1: 3.

Let

- W be the number of clean complete boundary-started 46-step windows;
- B be the number of exact-four clean windows;
- G be the total number of defect upsteps in the whole first-candidate prefix;
- H be the number of those upsteps whose source has positive defect.

The live-frontier certificate gives

`W >= 35,260,566,218`.

Every clean window has at least four upsteps. Hence total upstep/window incidences I satisfy

`I >= 5(W-B)+4B = 5W-B`.

A boundary-source upstep belongs to at most 45 boundary-started 46-windows, while a positive-source upstep belongs to at most 44. Therefore

`I <= 45(G-H)+44H = 45G-H`.

The exact-q overlap theorem gives at most 43 exact-four windows per fixed upstep. Since each exact-four window now contains at least two positive-source upsteps,

`2B <= 43H`,

so

`H >= 2B/43`.

Also, counting all four incidences in exact-four windows and using the same universal 43-overlap cap gives

`4B <= 43G`,

hence

`B <= 43G/4`.

Combine the inequalities:

`5W-B <= 45G-H <= 45G-2B/43`,

so

`45G >= 5W-(41/43)B`.

Using `B <= 43G/4`,

`45G >= 5W-41G/4`,

therefore

`boxed: 221 G >= 20 W`.

With `W >= 35,260,566,218`,

`boxed: G >= ceil(20W/221) = 3,191,001,468`.

Every counted upstep has the exact arithmetic form `r=2,a=1`.

This strengthens the previous exact-q packing bound

`G >= 3,162,382,621`.

## 3. Strategic implication

The next useful exact-four targets are not equal in value. To force every surviving exact-four window to contain at least three positive-source upsteps, it is enough to eliminate the two remaining two-positive classes

- U2V2,
- U2V1T1.

If that is achieved, the same argument replaces 221 by 220 in the denominator and immediately strengthens the global upstep charge again.

More importantly, the exact-q overlap diagnostic shows that local-window escalation alone cannot close branch A: a second global upper restriction on the same `r=2,a=1` events is still required. The targeted certificates are now best viewed as a way to sharpen that coupled global optimization rather than as a standalone path to 40 upsteps per window.