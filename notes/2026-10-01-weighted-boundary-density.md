# Weighted boundary-density strengthening

Status: exact consequence of the first-candidate correction ratio and Denjoy--Koksma. Not a Collatz proof.

For the first coefficient-contraction candidate, write

S = sum_{j<k} f(theta_j),

where

f(x)=2^{-x},

theta_j={j log_2 3},

and k=qC=72,057,431,991.

The mechanical correction weights are

w_j = 3^{k-1} f(theta_j).

Let Z be the set of boundary times h_j=0, let z=|Z|, and let

T = sum_{j in Z} f(theta_j).

Because every non-boundary time has h_j>=1,

R=d_k/d_k^max <= (T + (S-T)/2)/S = 1/2 + T/(2S).

The exact first-candidate survival condition gives

R > rho := N0/N_upper.

Hence necessarily

T/S > 2rho-1.

## Denjoy--Koksma control of S

The candidate denominator splits as

qC=qL+qU,

where qL and qU are the two convergent-denominator blocks already used in `first_contraction_cert.py`.

For f(x)=2^{-x} on R/Z,

integral f = 1/(2 log 2),

Var(f)=1.

Applying Denjoy--Koksma separately to the two blocks gives

S >= qC/(2 log 2) - 2.

## Threshold bound for the heaviest z phases

Choose the exact rational threshold

u=7391/10000.

Define

g_u(x)=max(2^{-x}-u,0).

For every subset Z of size z, pointwise

T <= z*u + sum_{j<k} g_u(theta_j).

The variation is

Var(g_u)=2(1-u),

and its integral is

J(u)=((1-u)-u log(1/u))/log 2.

Therefore the same two-block Denjoy--Koksma split gives

sum g_u(theta_j) <= qC*J(u)+4(1-u).

Combining this upper bound for T with the necessary inequality

T > (2rho-1) S

yields an explicit lower bound on z.

`src/weighted_boundary_density_cert.py` evaluates every logarithm with rational interval arithmetic and proves

z >= 31,430,911,924.

Thus the boundary density satisfies

z/k >= 0.4361925072201537...,

i.e. at least about 43.61925 percent of the whole first-candidate prefix lies exactly on h=0.

This improves the earlier coarse factor-two bound

z >= 25,438,346,005

by nearly six billion boundary states.

## Consequence for forced excursions

The global boundary-run certificate allows at most 35 boundary states in one run. Hence

number of boundary runs >= ceil(31,430,911,924 / 35) = 898,026,055.

Therefore a first-candidate survivor requires at least

898,026,054

unit departures h=0->1.

Together with the exact cheap-run cap (at most three cheap immediate excursions consecutively), at least

floor(898,026,054 / 4) = 224,506,513

of those excursions are non-cheap. Since heavy immediate two-step returns have already been excluded, at least 224,506,513 excursions have length at least three.

This is the current strongest global excursion count in branch A.