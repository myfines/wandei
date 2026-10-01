# Boundary-run cap improves the 46-window covering charge

Status: exact combinatorial strengthening inside the first coefficient-contraction branch. Not a Collatz proof.

Use the strong translated 46-step certificate and its clean-window count

W >= 35,251,435,436.

For every clean boundary-started 46-step window, either

1. the window reaches h>=2, or
2. the window contains at least four upcrossings 0->1.

Let

- U = #{j : h_j=0, h_{j+1}=1};
- V = #{j : h_j=1, h_{j+1}=2}.

The length-29 boundary certificate proves that no orbit segment contains 30 consecutive boundary states h=0.

## 1. Multiplicity of a V event

A V event occurs at a transition j with h_j=1, so j itself is not a boundary start.

A length-46 window containing transition j can start only at one of the 46 times j-45,...,j. Among these 46 candidate starts, the last one j is nonboundary. Among the remaining 45 consecutive times, at most 44 can be boundary, because 45 consecutive boundary states would contain 30 consecutive boundary states.

Therefore any fixed V event can witness at most 44 clean boundary-started windows.

Hence

W_V <= 44 V.

## 2. Multiplicity of a U event

A U event occurs at a transition j with h_j=0, so j itself may be a boundary start.

Again the candidate starts are j-45,...,j. Because 30 consecutive boundary states are impossible, among these 46 times at most 45 can be boundary.

Therefore any fixed U event can occur in at most 45 clean boundary-started windows.

Every low clean window contains at least four U events, so incidence counting gives

4 W_U <= 45 U,

hence

W_U <= (45/4) U.

## 3. Improved global charge

Since W = W_V + W_U,

W <= 44 V + (45/4) U.

Multiplying by 4,

4W <= 176 V + 45 U <= 45(4V+U).

Therefore

4V+U >= ceil(4W/45).

With W >= 35,251,435,436,

ceil(4*35,251,435,436/45) = 3,133,460,928.

Thus every first-candidate survivor satisfies

boxed: 4V + U >= 3,133,460,928.

This strengthens the previous bound

4V+U >= 3,065,342,212

by 68,118,716.

The argument explicitly allows boundary waiting and uses only the already certified 29-state boundary-run cap plus the strong translated 46-step rule.