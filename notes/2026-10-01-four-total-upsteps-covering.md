# Every clean boundary-started 46-step window has at least four total upsteps

Status: exact combination of four translated finite certificates plus the global sharp-repayment bound. Not a Collatz proof.

Let a **clean** 46-step window mean a complete boundary-started window containing no positive odd-height direct repayment to h=0 at an r=2 step. The sharp repayment phase certificate proves that at most five such rare events occur in the entire first-candidate prefix, so the same clean-window count as before applies:

W >= 35,251,435,436.

We prove that every clean window contains at least four total upward defect transitions h->h+1.

## 1. Existing exact certificates

Several complete translated certificates already exclude the following local classes over all 47 length-46 mechanical factors.

1. `src/translated_noheavy_three_upcross_cert.py`:
   if all states remain in {0,1}, then at most three 0->1 entries are impossible.

2. `src/translated_h2_one_entry_cert.cpp`:
   if all states remain in {0,1,2}, then the class with at most two 0->1 entries and at most one 1->2 entry is impossible.

3. `src/translated_h3_single_entry_cert.cpp`:
   if all states remain in {0,1,2,3}, then the class in which each of 0->1, 1->2, 2->3 occurs at most once is impossible.

These certificates all use exact 2-adic seed cylinders and verify every concrete lift in the certified local boundary-state interval.

## 2. Classify a hypothetical window with exactly three total upsteps

Suppose a clean window had exactly three upward transitions in total.

Because every upstep raises h by exactly one and the window starts at h=0, its maximum defect height is at most 3.

### Case A: max h <= 1

Then every upstep is 0->1, so there are exactly three such entries. This is excluded by certificate 1.

### Case B: max h = 2

Write

U=#(0->1),  V=#(1->2)

inside the window. Since there are exactly three total upsteps,

U+V=3,

and reaching height 2 forces U>=1, V>=1.

The possibilities are therefore

(U,V)=(2,1) or (1,2).

The first is excluded by certificate 2.

The second is the only previously uncovered three-upstep pattern. It is now covered by

`src/translated_h2_one_u_two_v_cert.cpp`.

That exact scan covers all 47 length-46 mechanical factors with the constraints

- start at h=0;
- stay in {0,1,2};
- exactly U=1;
- exactly V=2;
- no rare h=1,r=2 direct repayment to h=0.

Exact aggregate result:

- scripts: 61,175,686;
- concrete candidate rows: 17,737,070;
- every row realizes its prescribed valuation prefix;
- every row falls below the verified frontier;
- latest drop: odd step 283;
- worst seed: 4,942,811,925,495,116,845,049;
- below-frontier endpoint: 1,802,150,773,986,880,577,533;
- factor-summary SHA256: `bcf647bedc1f46565e577e148b2cd157f9ca6be31de9aa47bbb721b2d942632b`.

Thus the second pattern is also impossible.

### Case C: max h = 3

Reaching height 3 with only three total upsteps forces exactly one entry at each level:

U=V=T=1,

where T=#(2->3).

This is excluded by certificate 3.

No height >=4 can be reached with only three upsteps.

Therefore every clean boundary-started 46-step window contains at least four total upsteps.

## 3. Global overlap count

Let

G = #{0<=j<k : h_{j+1}=h_j+1}

be the total number of upward defect transitions at all heights.

Every clean window contains at least four such transitions.

A fixed transition belongs to at most 45 boundary-started length-46 windows: among its 46 possible window starts, the 29-state boundary-run certificate forbids all 46 starts from being boundary times.

Hence

4W <= 45G.

Using

W >= 35,251,435,436

gives

G >= ceil(4W/45)
  = 3,133,460,928.

Thus

boxed: G >= 3,133,460,928.

Every upstep has the exact arithmetic form

r=2, a=1.

## 4. Repayment mass

Since h_0=0 and h_k=-1, the total signed defect increment over the first-candidate prefix is -1.

If D denotes the total magnitude of all negative defect increments, then

G-D=-1,

hence

boxed: D=G+1 >= 3,133,460,929.

This supersedes the earlier total-upstep lower bounds 2,299,006,659 and 2,350,095,696.

The next target is to classify the exact-four-upstep windows in the same targeted way, rather than attempting the prohibitively large unrestricted cap-four state space.