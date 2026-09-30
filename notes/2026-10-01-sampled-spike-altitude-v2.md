# Sampled spike-altitude lemma

Status: exact necessary condition for a hypothetical minimal counterexample on the `2 mod 9` sampled section. This is not a proof of Collatz.

Work with sampled states `M=4n+1 ≡ 9 (mod 36)`. Let `M_*` be the least sampled state whose forward Terras orbit does not reach 1, assuming such a state exists.

Let `M = 3^V u`, with `3 ∤ u` and `V ≥ 3`, be any sampled counterexample state. Choose `t ∈ {V,V+1}` so that `2^t u ≡ 4 (mod 12)` and set

`M_tilde = 3(2^t u - 1)`.

Then `M_tilde ≡ 9 (mod 36)`, and because `t≥3` its induced branch uses the shift `eta=3`. Also

`M_tilde + 3 = 3*2^t*u`.

After stripping the power of two, the odd cofactor is `3u`. The induced exponent is `q=V-1` because `q` is one of `t-2,t-1` and `3^q(3u)=3^V u=M≡1 (mod 4)`. Hence `M_tilde -> M` in one sampled return.

Since `M` is a counterexample, every positive sampled predecessor reaching it is also a counterexample. Therefore `M_* ≤ M_tilde`. But `t≤V+1`, so

`M_tilde < 3*2^(V+1)*u = 6*(2/3)^V*M`.

Thus

`M > (M_*/6)*(3/2)^V`.

This converts high 3-adic valuation into a real-height lower bound.

For a first-return word `E^e O^r E Q`, where `r` is the consecutive odd-run length and `Q∈{E,O}`, the endpoint has the form `M_{j+1}=3^q s` with `q∈{r,r+1}`. Therefore `v_3(M_{j+1})≥r`, and for `r≥3`,

`M_{j+1} > (M_*/6)*(3/2)^r`.

In particular `(1/6)*(3/2)^8 = 4.271484375 > 4`, so

`M_{j+1} ≤ 4 M_*  =>  r ≤ 7`.

Similarly `M_{j+1} ≤ 2 M_* => r ≤ 6`.

Hence long odd-run spikes cannot end in the low sampled band. Inside `[M_*,4M_*]`, every sampled return belongs to the finite subfamily with `r≤7`.

This creates a direct bridge between the earlier low-altitude program and the bounded-run finite-alphabet program. The remaining missing bridge is quantitative: transfer sufficiently many low ordinary/odd-only orbit visits into sufficiently many low sampled visits.