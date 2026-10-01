# Boundary-boundary edges on the convergent cycle are almost all strictly descending

Status: exact consequence of the first-candidate product bound and continued-fraction best approximation. Not a Collatz proof.

Let

- alpha = log_2 3;
- k=qU+qL=72,057,431,991;
- qU=6,586,818,670 with pU-qU*alpha = deltaU >0;
- qL=65,470,613,321 with qL*alpha-pL = deltaL >0;
- sigma(n)=n+qU mod k;
- B={n:h_n=0}.

The previous convergent-cycle lemma proves that a surviving first-candidate orbit has at least 1,134,940,229 sigma-edges whose two endpoints lie in B.

This note determines the sign of the actual Syracuse-state drift on such edges.

## 1. Nonwrapped qU edge

Suppose n<qL, so sigma(n)=n+qU chronologically forward.

Because both endpoints are boundary times,

A_{n+qU}-A_n = floor((n+qU)alpha)-floor(n alpha).

Since qU*alpha=pU-deltaU, this increment is

- pU-1 if theta_n={n alpha}<deltaU;
- pU if theta_n>=deltaU.

For the pU case,

x_{n+qU}/x_n = 2^{-deltaU} P,

where P is the correction product over the qU-step block.

Every preterminal state is at least N0=2075*2^60, hence

log_2 P < qU/(3 N0 ln 2).

`src/convergent_boundary_drift_cert.py` proves exactly

qU/(3 N0 ln 2) < deltaU.

Therefore

boxed: theta_n>=deltaU and n<qL imply x_{sigma(n)}<x_n.

Now use the best-approximation property of consecutive convergents qU<qL. For every integer 0<n<qL,

||n alpha|| >= ||qU alpha|| = deltaU.

Thus no positive n<qL can satisfy theta_n<deltaU. The only nonwrapped source in the exceptional phase interval is n=0.

So every nonwrapped B-B sigma edge except possibly 0->qU strictly decreases the actual odd state.

## 2. Wrapped edge

Suppose n>=qL, so sigma(n)=n-qL. Put m=n-qL; then m<n and n=m+qL.

Since qL*alpha=pL+deltaL, the forward qL exponent increment is

- pL if theta_m<1-deltaL;
- pL+1 if theta_m>=1-deltaL.

In the pL case,

x_n/x_m = 2^{deltaL} P >1,

so in the sigma direction

x_{sigma(n)}=x_m<x_n.

Could the exceptional pL+1 case occur? It would require theta_m>1-deltaL, equivalently ||m alpha||<deltaL. But 0<=m<qU<qL, and qU,qL are consecutive convergent denominators with deltaL smaller than every ||m alpha|| for 0<m<qL. Therefore it is impossible. For m=0, theta_m=0 and the ordinary pL case holds.

Hence every wrapped B-B sigma edge strictly decreases the actual odd state.

## 3. Global conclusion

Therefore

boxed: for every n in B with sigma(n) in B and n!=0,
       x_{sigma(n)} < x_n.

The single edge 0->qU is the only possible exception; if qU is also a boundary time, its exponent increment is pU-1 and the block is expanding rather than contracting.

Combining with the certified adjacency count, at least 1,134,940,228 boundary-boundary sigma edges are strict decreases in the sigma direction.

This does not by itself close branch A, because the boundary subset can break the sigma cycle into descending runs. Its value is structural: any future argument that forces a closed or sufficiently long boundary chain on the qU cycle immediately acquires a strict monotonicity obstruction.