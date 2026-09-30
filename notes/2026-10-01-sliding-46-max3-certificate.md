# Sliding 46-step low-defect exclusion through three upcrossings

Status: exact finite certificate for the first-contraction framework. Not a Collatz proof.

Let a local window start at a critical-boundary state h=0. Suppose that for the next 46 odd-only steps the defect never exceeds one,

h_j in {0,1},

and that the window contains at least one but at most three upcrossings 0->1.

There are exactly 47 possible length-46 factors of the mechanical word

r_j = floor((j+1)log2(3)) - floor(j log2(3)).

The certificate `src/sliding_unit_excursion_cert_max3.cpp` enumerates all valuation scripts compatible with those 47 factors, the defect restriction h in {0,1}, and at most three upcrossings.

For every script it constructs the exact 2-adic seed residue from the affine Syracuse prefix. It then enumerates every lift in the local boundary interval

N0 = 2075*2^60 <= x < 2^73,

and continues the actual odd-only Syracuse orbit until it falls below the verified frontier N0.

Exact output:

- length-46 mechanical factors: 47;
- low-defect scripts with one to three upcrossings: 104,035,682;
- candidate residue classes intersecting the local interval: 47,290,188;
- concrete candidate seed lifts: 47,866,652;
- every candidate falls below N0 within 1000 odd steps;
- the latest such drop occurs at odd step 276;
- worst local seed: 8171827952796853273339;
- its below-frontier endpoint: 697521228196614030223;
- corresponding first factor shift: 31;
- no unsigned-128 overflow occurs.

Therefore a hypothetical first-candidate survivor cannot have a 46-step window beginning at h=0 that both stays in {0,1} and contains only one, two, or three upcrossings.

Equivalently, after any boundary departure sufficiently far from the terminal contraction, survival forces the following local dichotomy within 46 odd steps:

1. the defect reaches h>=2; or
2. at least four distinct 0->1 upcrossings occur.

This is a translation-invariant strengthening of the earlier single-phase 46-step unit-excursion certificate.