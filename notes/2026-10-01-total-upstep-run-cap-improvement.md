# Boundary-run cap raises the total-upstep lower bound

Status: exact combinatorial strengthening of the translated two-total-upstep covering argument. Not a Collatz proof.

The translated two-total-upstep certificate proves that every complete heavy-free boundary-started 46-step window contains at least three upward defect transitions

h_j -> h_j+1.

The clean-window count is

W >= 35,251,435,436.

Let

G = #{0<=j<k : h_{j+1}=h_j+1}.

The earlier overlap count used the crude fact that one transition can lie in at most 46 length-46 windows, giving 3W<=46G.

The 29-state boundary-run certificate improves this multiplicity.

For a fixed upward transition at time j, a containing 46-step window can start only at one of the 46 times

j-45,...,j.

Every window under consideration must start at a boundary state h=0. Because no orbit segment contains 30 consecutive boundary states, among any 46 consecutive times at most 45 can be boundary states. Therefore a fixed upward transition belongs to at most 45 boundary-started 46-step windows.

Hence

3W <= 45G,

so

G >= ceil(3W/45).

Using W >= 35,251,435,436 gives

boxed: G >= 2,350,095,696.

Every upward transition has the exact arithmetic form r=2,a=1.

Since h_0=0 and h_k=-1, if D is the total magnitude of all negative defect increments, then

G-D=-1,

hence

boxed: D=G+1 >= 2,350,095,697.

This supersedes the previous total-upstep lower bound 2,299,006,659 by 51,089,037 events.