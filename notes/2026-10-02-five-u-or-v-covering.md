# Five-charge covering inequality

Status: exact consequence inside the first coefficient-contraction branch. Not a Collatz proof.

Let a clean 46-step window mean a complete boundary-started window containing no globally rare positive odd-height direct repayment to h=0 at an r=2 step.

The existing sharp phase bound gives at most five such rare events globally, and the pair-constrained boundary certificate gives at least

W >= 35,251,435,436

complete clean boundary-started 46-step windows.

Define

U = #{j : h_j=0, h_{j+1}=1},
V = #{j : h_j=1, h_{j+1}=2}.

## Local dichotomy

The translated no-heavy three-upcross certificate proves that if a clean 46-step window stays in {0,1}, it contains at least four U transitions.

The exact certificate `src/translated_h1_exact_four_u_cert.cpp` excludes the remaining clean low-height class with exactly four U transitions.

Therefore a clean low window contains at least five U transitions.

If a clean window enters h>=2, then before its first V:1->2 transition it must first leave the initial boundary h=0 through a U:0->1 transition. Upward defect jumps have size at most one, so this is unavoidable.

Thus every clean 46-step window satisfies the stronger score inequality

#U(window) + 4 #V(window) >= 5.

Indeed:

- low window: #U>=5;
- high window: #U>=1 and #V>=1.

## Sharpened overlap counts

A fixed U transition has source state h=0. Among the 46 possible starts of length-46 windows containing that transition, at most 45 can be boundary states: 46 boundary starts would give 46 consecutive boundary states, contradicting the certified boundary-run cap of 29 states.

Thus a fixed U belongs to at most 45 boundary-started 46-step windows.

A fixed V transition has source state h=1, so its own source time is not a boundary start. Among the remaining 45 possible starts, at most 44 can be boundary states, because 45 consecutive boundary starts immediately preceding the nonboundary source would again violate the 29-state boundary-run cap.

Thus a fixed V belongs to at most 44 boundary-started 46-step windows.

Summing the local score over all W clean windows therefore gives

5W <= 45 U + 4*44 V
   = 45 U + 176 V.

Using W >= 35,251,435,436,

boxed: 45 U + 176 V >= 176,257,177,180.

Since

45(U+4V) = 45U+180V >= 45U+176V,

we obtain the cleaner global consequence

boxed: U + 4 V >= ceil(5W/45)
                 = ceil(W/9)
                 = 3,916,826,160.

This supersedes the earlier 41-step bound

U+4V >= 3,439,164,436.

For reference, the weaker partition-only argument also gives

44V + 9U >= W,

but the five-charge inequality above is the stronger useful formulation because every high window necessarily contains both its first U and its first V.

Both U and V have the exact local arithmetic form r=2,a=1; only the incoming defect height differs.

The result is independent of the retracted cheap-excursion frequency argument.