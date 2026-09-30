# Three-step extended excursion valuation classification

Status: exact defect-recurrence classification inside the first-contraction framework. Not a Collatz proof.

A boundary excursion starts at h=0 and must leave by r=2, a=1, hence h: 0 -> 1.

From the exact three-symbol mechanical classification, the first three mechanical symbols after such a departure are either 212 or 221.

For a genuine length-three excursion, the path must stay positive after the first two steps and return to h=0 exactly after the third.

## Mechanical word 212

The first valuation is a0=1. At the second step, r=1 and h=1. To avoid an immediate return, we need

h2 = 1 + 1 - a1 > 0,

so a1=1 and h2=1. The third mechanical symbol is r=2, and return to zero requires

a2 = h2 + r = 3.

Thus the only length-three valuation pattern over 212 is

(r0,r1,r2) = (2,1,2),
(a0,a1,a2) = (1,1,3).

The terminal step is an odd-height direct repayment with r=2, so it is subject to the previously proved extreme phase gate.

## Mechanical word 221

Again a0=1 and h1=1. At the second step r=2, so

h2 = 1 + 2 - a1 = 3-a1.

To remain positive until the third step, a1 can be only 1 or 2.

- If a1=1, then h2=2. The final symbol is r=1, and return requires a2=3. This gives valuation pattern 113.
- If a1=2, then h2=1. The final symbol is r=1, and return requires a2=2. This gives valuation pattern 122.

Hence the only length-three valuation patterns over 221 are

(a0,a1,a2) = (1,1,3) or (1,2,2).

Therefore every genuine three-step boundary excursion is one of exactly three local cylinders:

1. mechanical 212 with valuations 113;
2. mechanical 221 with valuations 113;
3. mechanical 221 with valuations 122.

This finite classification is the correct input for the next local certificate / automaton search.