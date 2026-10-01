# More than 1.13 billion adjacent boundary pairs on the convergent cycle

Status: exact consequence of the first-candidate correction budget, continued-fraction geometry, and a weighted cycle argument. Not a Collatz proof.

Let

- `alpha=log_2 3`;
- `k=qC=72,057,431,991`;
- `(pU,qU)=(10,439,860,591, 6,586,818,670)`;
- `(pL,qL)=(103,768,467,013, 65,470,613,321)`;
- `k=qU+qL`;
- `B={0<=n<k:h_n=0}`.

Give vertex `n` mechanical weight

`w_n = 2^{-theta_n}`,  `theta_n={n alpha}`.

Let `S=sum_{n<k} w_n` and `T=sum_{n in B} w_n`.

The first-candidate survival inequality gives

`T > c S`,

where

`c=2*(N0/N_upper)-1 = 0.5218348225... > 1/2`.

## 1. The qU shift orders all phases around one cycle

Define

`sigma(n)=n+qU (mod k)`.

Because `gcd(qU,k)=1`, sigma is a single cycle through all `k` indices.

Write the positive continued-fraction errors

`deltaU = pU-qU alpha >0`,

`deltaL = qL alpha-pL >0`.

If `n+qU<k`, then along the sigma edge the phase changes by `-deltaU mod 1`. If `n+qU>=k`, equivalently sigma subtracts qL, and the phase changes by `-deltaL mod 1`.

There are exactly `qL` edges of the first type and `qU` of the second. The determinant identity

`pU*qL-pL*qU=1`

gives exactly

`qL*deltaU + qU*deltaL = 1`.

Therefore one full sigma circuit decreases the lifted phase by exactly one. Modulo one, the cycle has exactly one wrap through phase zero. Away from that single wrap the phases are strictly decreasing.

Consequently the weights `2^{-theta}` are strictly increasing around the cycle except at one jump. Since every weight lies in `(1/2,1]`, their cyclic total variation is

`TV_sigma(w)=2(max w-min w) < 1`.

## 2. Weighted independent-set bound

Let `I` be any independent vertex set on the sigma cycle. For each selected vertex `i`, pair it with its successor `sigma(i)`. Independence makes these pairs vertex-disjoint.

For each pair,

`w_i <= (w_i+w_sigma(i)+|w_i-w_sigma(i)|)/2`.

Summing over selected vertices gives

`weight(I) <= (S+TV_sigma(w))/2 < S/2+1/2`.

## 3. Apply to the boundary set

Let `e` be the number of sigma edges whose two endpoints both belong to `B`.

If `B` is not already independent, delete at most one boundary vertex for each B-B edge; run by run this leaves an independent subset and deletes at most `e` vertices. Since each deleted weight is at most 1, the surviving independent subset has weight at least

`T-e`.

Hence

`T-e < S/2+1/2`.

Using `T>cS`,

`e > (c-1/2)S - 1/2`.

Denjoy--Koksma on `w(theta)=2^{-theta}` and the split `k=qL+qU` gives the exact lower bound

`S >= k/(2 ln 2)-2`.

`src/convergent_cycle_boundary_edges_cert.py` evaluates the resulting rational inequality and certifies

`boxed: e >= 1,134,940,229`.

Thus a first-candidate survivor must contain more than 1.13 billion pairs of boundary times that are adjacent under the convergent shift `n -> n+qU mod k`.

## 4. Why this is useful

These are not ordinary neighboring times. Each sigma edge corresponds to one of two huge continued-fraction blocks:

- an ordinary forward block of length `qU=6,586,818,670`, or
- a wrapped reverse edge corresponding chronologically to a block of length `qL=65,470,613,321`.

Both block coefficients are extraordinarily close to one because qU and qL are convergent denominators. The next target is to combine the billion forced B-B edges with the sign of the exact affine drift on these two block types.

Unlike the retracted cheap-excursion count, this argument is global from the start and does not assume that excursions are adjacent in ordinary time.
