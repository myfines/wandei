# Universal 43-overlap cap for exact-four boundary windows

Status: exact combinatorial lemma inside branch A. No finite seed scan is used here. Not a Collatz proof.

Let an **upstep** mean a transition

`h_{j+1}=h_j+1`.

Let an **exact-four window** mean a boundary-started window of 46 transitions containing exactly four total upsteps.

## Lemma

A fixed upstep transition can belong to at most 43 exact-four boundary-started 46-transition windows.

Translate the fixed upstep to transition time `0`. The 46 possible starts of a length-46 window containing it are

`-45,-44,...,0`.

Every qualifying start time is a boundary state.

### Case 1: the fixed upstep has positive source

Then state `0` is nonboundary, so start `0` cannot qualify.

Assume for contradiction that 44 windows qualify.

If start `-45` qualifies, its window contains the fixed upstep at `0` plus three other upsteps at times `<0`. The three target states of those other upsteps are distinct nonboundary states in `[-44,0]`. Even if one target is state `0`, at least two lie in `[-44,-1]`. Hence among the 45 candidate starts `[-45,-1]` at least two are nonboundary, leaving at most 43 qualifying starts, contradiction.

Therefore start `-45` does not qualify. To have 44 qualifying windows, every start `-44,...,-1` must then qualify and hence every state `-44,...,-1` is boundary.

Consider the qualifying window starting at `-44`, whose transitions are `-44,...,1`. Any upstep at a time `j<=-2` would have nonboundary target state `j+1 in [-43,-1]`, impossible. There can be at most one upstep at `-1` (targeting the nonboundary source state `0`) and at most one additional upstep at `1` (whose source is the positive target of the fixed upstep). Together with the fixed upstep this gives at most three upsteps, contradicting exact-four.

So 44 qualifying windows are impossible.

### Case 2: the fixed upstep is a boundary departure `0->1`

Now state `0` is boundary and state `1` is nonboundary.

Again suppose 44 windows qualify.

If start `-45` qualifies, its window contains the fixed upstep at `0` and three other upsteps at times `<0`. None of those three can target state `0`, because state `0` is boundary. Hence all three targets are distinct nonboundary states in `[-44,-1]`. Thus at least three of the candidate starts `[-45,-1]` are nonboundary; even including start `0`, at most 43 starts can qualify, contradiction.

Hence start `-45` does not qualify. Among the remaining 45 possible starts `-44,...,0`, at most one can fail if 44 qualify.

If start `-44` qualifies, then at least 44 of the state times `-44,...,0` are boundary. In that window, any upstep at `j<=-2` creates a nonboundary target in `[-43,-1]`, so at most one such earlier upstep can occur. An upstep at `-1` cannot occur because its target would be the boundary state `0`. After the fixed upstep at `0`, transition `1` can contribute at most one further upstep. Thus the window contains at most three upsteps, contradiction.

Therefore start `-44` must be the unique nonqualifying start, so all starts `-43,...,0` qualify and all corresponding source states are boundary. The window starting at `-43` has transitions `-43,...,2`. No upstep before `0` is possible because its target would be one of the boundary states `-42,...,0`. After the fixed upstep at `0`, only transitions `1` and `2` remain available for additional upsteps. Hence this window again contains at most three upsteps, contradiction.

Thus 44 qualifying windows are impossible in the boundary-source case as well.

Therefore every fixed upstep belongs to at most

`boxed: 43`

exact-four boundary-started 46-transition windows.

## Global consequence

Let

- `W` be the number of clean complete boundary-started 46-step windows;
- `A` be the number of such windows with at least five upsteps;
- `B` be the number with exactly four upsteps;
- `G` be the total number of upstep transitions in the whole first-candidate prefix.

Then

`A+B=W`.

Ordinary boundary-window overlap gives at most 45 windows per upstep, so counting all upstep incidences yields

`5A+4B <= 45G`,

hence

`5W-B <= 45G`.

The universal exact-four overlap lemma gives

`4B <= 43G`,

so

`B <= 43G/4`.

Substituting,

`45G >= 5W-B >= 5W-43G/4`,

therefore

`boxed: 223G >= 20W`.

Using the 2026-10-02 live-frontier clean-window certificate

`W >= 35,260,566,218`,

we obtain

`boxed: G >= ceil(20 W / 223) = 3,162,382,621`.

This strictly strengthens the previous exact-four ladder bound

`G >= 3,152,080,920`.

The lemma is independent of the mechanical word, phase gates, GRH, and the retracted cheap-excursion frequency argument. It uses only the boundary-start condition and the fact that every upstep lands at a nonboundary state.
