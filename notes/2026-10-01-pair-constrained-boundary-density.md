# Pair-constrained weighted boundary density

Status: exact first-candidate consequence. Not a Collatz proof.

This strengthens the weighted boundary-density argument by using a local closure rule that was previously ignored.

## Forced boundary pair at r=1

Before the terminal contraction we have h_j>=0. If h_j=0 and the mechanical letter is r_j=1, then

h_{j+1}=h_j+r_j-a_j=1-a_j.

Since a_j>=1 and h_{j+1}>=0 for j+1<k, necessarily

a_j=1,

h_{j+1}=0.

Therefore every preterminal boundary state at an r=1 phase forces its successor to be a boundary state as well.

Write beta=log_2 3-1 and b=1-beta=2-log_2 3. Then

r_j=1 iff theta_j in [0,b).

Because beta>1/2, the mechanical word contains no `11`: after an r=1 phase, the next phase lies in [beta,1), hence r=2. Thus these forced r=1 -> successor pairs are disjoint.

The successor mechanical weight is exactly

2^{-theta_{j+1}} = (2/3) 2^{-theta_j}.

## Lagrange optimization

Let Z be the set of boundary times, z=|Z|, and let

T=sum_{j in Z} 2^{-theta_j}.

Use the exact multiplier

lambda = 3593/5000.

For one forced pair with start weight w=2^{-theta}, the allowed boundary patterns are only

00, 01, 11.

The maximum of `boundary weight - lambda * boundary count` over those three choices is

max(0, (5/3)w - 2 lambda).

The unpaired r=2 phases are exactly theta in [b,beta), and there the one-site contribution is

max(0,2^{-theta}-lambda).

This yields a phase function H_lambda with two separated positive humps. Its integral and total variation are explicit. The candidate length

qC=qL+qU

splits into two convergent-denominator blocks, so Denjoy--Koksma gives a constant-error upper bound for

sum_{j<qC} H_lambda(theta_j).

There is at most one exceptional r=1 state at j=k-1, because its successor is the terminal h_k=-1 state; a +1 endpoint slack covers it.

Hence one obtains the exact inequality

T - lambda z <= qC * integral(H_lambda) + 2 Var(H_lambda) + 1.

On the other hand, the first-candidate correction ratio still requires

T > (2 rho - 1) S,

where

rho=N0/N_upper

and

S=sum_{j<qC}2^{-theta_j} >= qC/(2 log 2)-2.

`src/pair_constrained_boundary_density_cert.py` evaluates all logarithms with rational intervals and proves

z >= 35,251,435,711.

Therefore the boundary density satisfies

z/k >= 0.4892130448862363...,

so at least about 48.9213 percent of all preterminal times lie exactly on h=0.

## Updated excursion counts

Using the independent boundary-run cap of 35 states per run,

boundary runs >= ceil(35,251,435,711 / 35) = 1,007,183,878.

Hence a first-candidate survivor needs at least

1,007,183,877

unit departures h=0->1.

Because at most three cheap immediate excursions can occur consecutively, at least

floor(1,007,183,877 / 4) = 251,795,969

excursions are non-cheap. Heavy two-step immediate returns are impossible, so all of those 251,795,969 excursions have length at least three.

This is currently the strongest global boundary/excursion constraint in branch A.