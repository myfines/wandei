# 2026-11-22 — Unconditional factor-complexity floor for any nonperiodic positive odd Collatz orbit

**Status:** exact elementary conditional statement about hypothetical infinite nonperiodic positive orbits; does not exclude such an orbit and is NOT a Collatz proof. Related stronger bounds assuming an existing valuation mean are independently documented in Sodelin/Collatz-Conjecture-Work (2026-09-05). No originality claim.

Let S(n)=(3n+1)/2^v2(3n+1) and let n_j=S^j(n_0) with n_0 positive odd. Write a_j=v2(3n_j+1). If the orbit is not eventually periodic, the states n_j are all distinct. Define p(L) to be the number of distinct length-L subwords (a_j,...,a_(j+L-1)) over the infinite sequence, without restricting the alphabet.

**Finite deterministic bound.** For L>=1 define K_L to be the largest nonnegative integer K satisfying

    (n_0+1)*3^K <= 2^(L+K+1),

or K_L=-1 if none exists. If the first K_L+1 orbit states n_0,...,n_(K_L) are distinct, then the valuation words starting at indices 0,...,K_L and of length L are pairwise distinct.

**Proof.** Each step S(n)+1 <= (3/2)(n+1), so each 0<=j<=K_L has
n_j+1 <= (3/2)^j(n_0+1) <= 2^(L+1).
Two distinct positive odd starts whose next L exponents agree must be congruent modulo 2^(A+1), where A is their shared exponent sum, and A>=L. Consequently their nonzero difference has absolute value >=2^(L+1). But both starts belong to (0,2^(L+1)), contradiction. QED.

For a hypothetical nonperiodic infinite orbit this holds for all L, so

    p(L) >= max(0,K_L+1).

As L tends to infinity, K_L/L tends to 1/log_2(3/2). Hence

    liminf_(L -> infinity) p(L)/L >= 1/log_2(3/2)
                                  = 1.70951129135...

This requires **no existence of a limiting mean valuation**. It is stronger than the generic Morse-Hedlund lower bound p(L)>=L+1, but far too weak to exclude arbitrary high-complexity words.

It only rules out a restricted class of low-complexity symbolic escape scenarios. The step that would prove Collatz is a theorem showing every actual positive orbit must have some forbidden repetition or subword-complexity cap; no such result has been established.

Note on finite code: Python computes K_L by checking the inequality with exact integers, not floating-point logs.

Related prior work, including stronger conditional complexity barriers:
https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/research/blind-2026-09-05/SymbolicNotes.md

Underlying 2-adic parity cylinder structure is classical: Bernstein--Lagarias, 1996:
https://websites.umich.edu/~lagarias/doc/bernstein.pdf
