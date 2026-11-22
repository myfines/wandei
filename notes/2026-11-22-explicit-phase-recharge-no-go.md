# 2026-11-22 — Closed-form phase recharge and a one-edge Lyapunov obstruction

**Status:** proved elementary facts. This is an audit/refutation of an overly simple proof candidate, not a Collatz proof.

For the odd-only map S(n)=(3n+1)/2^v2(3n+1), and every integer r>=1, define

    n_r=(2*4^r+1)/3.

This is a positive odd integer congruent to 3 mod 4. Hence v2(3*n_r+1)=1, and there is an *exact* image

    S(n_r)=4^r+1.

Define the 2-adic stable-anchor precision E(n)=v2(n-1) for n>1. Then

    E(n_r)=1, whereas E(S(n_r))=2r.

**Consequently the phase precision can be recharged by an arbitrarily large
amount in a single positive-integer Syracuse step.** This is a closed-form
version of the modular inverse construction in the phase-switch report.
Examples: r=1: 3->5, precision 1->2; r=2: 11->17, 1->4;
r=3: 43->65, 1->6; r=4: 171->257, 1->8.

Moreover there is **no globally nonincreasing function of the form**

    V(n)=log(n)+psi(v2(n-1))

for *any* real-valued function psi on positive integers, even if only required
on n>1. Proof: S(7)=11, and both 7 and 11 have E=1, while log(11)>log(7).
Therefore V(11)>V(7) whatever psi is.

These statements rule out one specific class of naive height + fixed-anchor
phase potentials. They **do not** rule out state-dependent, multitime,
3-adic-coupled, or non-monotone certificate approaches; and they say
nothing about global convergence.

A user asked whether different integers can 'rotate' toward 1. These are
counterexamples to the inference 'one phase coordinate and real log height
always produces a monotone convergence measure.' The genuine next problem is
a cross-scale bound that survives changes of template and phase recharge.

Programmatically checked in src/phase_switch_budget.py by the construction
recharged_seed(2*r); test_arbitrarily_large_recharge_witnesses covers h=2..79.
