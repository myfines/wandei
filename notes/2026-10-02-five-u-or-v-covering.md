# Five-U-or-V covering inequality

Status: exact consequence inside the first coefficient-contraction branch. Not a Collatz proof.

Let a clean 46-step window mean a complete boundary-started window containing no globally rare positive odd-height direct repayment to h=0 at an r=2 step.

The existing sharp phase bound gives at most five such rare events globally, and the pair-constrained boundary certificate gives at least

W >= 35,251,435,436

complete clean boundary-started 46-step windows.

Define

U = #{j : h_j=0, h_{j+1}=1},
V = #{j : h_j=1, h_{j+1}=2}.

## Local dichotomy

The translated no-heavy three-upcross certificate already proves that if a clean 46-step window stays in {0,1}, it must contain at least four U transitions.

The newer exact certificate `src/translated_h1_exact_four_u_cert.cpp` excludes the remaining clean low-height class with exactly four U transitions.

Therefore every clean 46-step boundary-started window satisfies one of:

1. it enters h>=2, hence contains at least one V transition; or
2. it stays in {0,1}, in which case it contains at least five U transitions.

## Sharpened overlap counts

A fixed U transition has source state h=0. Among the 46 possible starts of length-46 windows containing that transition, at most 45 can be boundary states: 46 boundary starts would give 46 consecutive boundary states, contradicting the certified boundary-run cap of 29 states.

Thus a fixed U belongs to at most 45 boundary-started 46-step windows.

A fixed V transition has source state h=1, so its own source time is not a boundary start. Among the remaining 45 possible starts, at most 44 can be boundary states, because 45 consecutive boundary starts immediately preceding the nonboundary source would again violate the 29-state boundary-run cap.

Thus a fixed V belongs to at most 44 boundary-started 46-step windows.

Partition the W clean windows into high windows and low windows. Then

W_high <= 44 V,
5 W_low <= 45 U,

so

W = W_high + W_low <= 44 V + 9 U.

Using W >= 35,251,435,436 gives the exact global charge

boxed: 44 V + 9 U >= 35,251,435,436.

A simpler consequence follows because

44V+9U <= 9(5V+U):

boxed: 5 V + U >= ceil(35,251,435,436/9) = 3,916,826,160.

Both U and V have the exact local arithmetic form r=2,a=1; only the incoming defect height differs.

This strengthens the previous low-height covering information and is independent of the retracted cheap-excursion frequency argument.