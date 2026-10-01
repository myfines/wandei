# Exact-four overlap ladder for total defect upsteps

Status: exact combinatorial consequence of the clean-window certificates and the 29-state boundary-run cap. Not a Collatz proof.

Let W be the number of complete clean boundary-started 46-step windows. The existing global count gives

W >= 35,251,435,436.

Let

G = #{j : h_{j+1}=h_j+1}

be the total number of defect upsteps, and let H be the number of upsteps whose source has positive defect h_j>=1. Thus G-H is the number of boundary upsteps U:0->1.

Every clean 46-step window contains at least four total upsteps. The exact certificate `src/translated_h1_exact_four_u_cert.cpp` excludes the only exact-four class whose four upsteps are all U transitions. Therefore every clean window with exactly four total upsteps contains at least one positive-height upstep.

Write A for the number of clean windows with at least five upsteps and B for the number with exactly four. Then

A+B=W.

Counting total upstep incidences gives

I >= 5A+4B = 5W-B.

A boundary upstep U can belong to at most 45 boundary-started 46-windows, while a positive-height upstep can belong to at most 44 because its source time is not a boundary start. Hence

I <= 45(G-H)+44H = 45G-H.

Every exact-four window contains at least one positive-height upstep, so incidence counting also gives

B <= 44H,

hence

H >= B/44.

Combining,

5W-B <= 45G-H <= 45G-B/44,

so

45G >= 5W - 43B/44.

The weakest bound occurs at B=W. Therefore

G >= ceil((177/1980) W).

Using W>=35,251,435,436 gives

boxed: G >= 3,151,264,683.

This strictly improves the previous exact lower bound

G >= 3,133,460,928.

## Ladder principle

More generally, suppose future targeted certificates prove that every exact-four clean window contains at least s positive-height upsteps. Then B<=44H/s, so H>=sB/44 and the same calculation yields

G >= ceil(((4+s/44)/45) W).

Thus every additional forced positive-height upstep inside the surviving exact-four classes immediately strengthens the global G lower bound.

At the endpoint, if all exact-four clean windows are excluded, then every clean window has at least five upsteps and

5W <= 45G,

so

G >= ceil(W/9) = 3,916,826,160.

This gives a quantitative reason to continue targeted elimination of the seven remaining exact-four height-pattern classes instead of attempting one unrestricted four-upstep scan.
