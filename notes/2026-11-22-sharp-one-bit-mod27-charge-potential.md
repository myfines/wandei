# 2026-11-22 — Sharp one-bit mod-27 hit-charge potential

**Status: deterministic single-orbit lemma, not a Collatz proof.** No claim of originality relative to classical finite-state discharging/potential methods.

Let the odd-only map be S(n)=(3n+1)/2^a for positive odd n with a=v2(3n+1). Let h(n) in {0,1} denote whether the following shortcut block T(n),...,S(n) contains **at least one** state 20 mod27. It is an indicator of a hit-bearing block, NOT the count of target states inside a very large valuation block. We have the exact table

    h(n)=1 iff a>=tau(n mod9),
    tau=(11,13,9,17,1,15,5,7,3).

Define the one-bit phase potential

    phi(r)=1 if r=4 (mod9); 0 otherwise.

## Theorem: exact edge charge

For every positive odd n, if n'=S(n), a=v2(3n+1), h=h(n), then

    **a-1-h >= phi(n')-phi(n).**

**Elementary proof by three cases:**

1. If r=n mod9=4 and a=1, then h=1, r'=2, so LHS=-1 and RHS=-1: equality.
2. If r=4 and a>=2, then h=1 and LHS=a-2>=0; RHS is either 0 or -1.
3. If r!=4, then tau(r)>=3 and a-1-h>=0. If r'!=4 then RHS=0 and we are done. If r'=4, note that every a=1 transition sends residues to 2, 5 or 8, NEVER 4. Thus a>=2, and if a=2 then h=0 (since tau(r)>=3), giving LHS=1; if a>=3 then LHS>=1. In both cases RHS=1. QED.

## Corollary: universal cumulative hit budget

For any length-k positive odd Syracuse trajectory n_0,...,n_k, put

    A_k=sum_(j<k) v2(3n_j+1),
    H_k=sum_(j<k) h(n_j).

Summing the exact edge charge telescopes:

    **A_k-k-H_k >= phi(n_k)-phi(n_0) >= -1.**
    Hence **A_k >= k+H_k-1**.

This is a bound on the **same actual integer orbit**, not a Haar expectation and not a finite formal-word ensemble.

The additive loss 1 is optimal: from n_0 mod9=4 choose a first step a=1 to get A=1,k=1,H=1, so equality holds. For arbitrarily long exact saturation, take the exponent word (1,2)^q,1, start at n=4 mod9 via CRT: A=3q+1, k=2q+1, H=q+1, and A=k+H-1. All finite words are realized by positive integer seeds. The repeating pair (1,2)^q also saturates the refined edge-potential inequality with phi(n_k)=phi(n_0)=1.

## Application to a hypothetical least odd counterexample

If N is the least positive odd counterexample, then n_j=S^j(N)>=N. The exact logarithmic identity gives

    0 <= log_2(n_k/N)
      = k log_2 3 - A_k
        +sum_(j<k) log_2(1+1/(3n_j)).

Since n_j>=N and combining the charge lower bound:

    **H_k/k <= (log_2 3-1) + log_2(1+1/(3N)) + 1/k.**

For very large N the asymptotic necessary bound is H_k/k<=0.5849625007... in limsup.

**This does NOT contradict known results.** Monks–Monks–Monks–Monks require infinitely many target hits on a hypothetical divergent orbit, NOT target-hit density >0.5849. The formal Haar density of hit-bearing odd blocks computed in the preceding mod27 bridge is 1079/4096≈0.2634, which is below this upper bound.

Thus the potential gives a true universal orbit-wise accounting law, but its current constant is too weak to prove global descent. A stronger **multi-state potential involving height, dual-adic carry, and correlated target pairs** remains open.

## Verification

- src/mod27_phase_charge.py: exact edge charge, actual-orbit telescoping, and conditional density check.
- tests/test_mod27_phase_charge.py: 5 tests, independently examining 9*600 finite-state edges, 10,000 real odd starting integers for 50 steps, exact sharpness families, and no-descent prefixes. All PASS locally.

External prior result: Monks et al., Discrete Mathematics 313 (2013), arXiv:1204.3904, https://arxiv.org/abs/1204.3904.
