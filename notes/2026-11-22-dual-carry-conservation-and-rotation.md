# 2026-11-22 — exact 2-/3-adic carry conservation and irrational-rotation obstruction

**Status: elementary proven identities, integer-only finite checks, no Collatz proof. No independent novelty claim.** The underlying dual radix representation is related to Stérin–Woods (2020) and to existing endpoint-residue carry results in Sodelin, Collatz-Conjecture-Work. The contribution of this experiment is a transparent binary-overlap convention and exact bidirectional lift audit.

## 1. Two canonical representations for one odd-only exponent word

Use S(n)=(3n+1)/2^v2(3n+1) on positive odd integers. For any finite word a_0,...,a_(k-1) with a_j>=1, set A_0=C_0=0 and
A_(j+1)=A_j+a_j, C_(j+1)=3*C_j+2^A_j.
Then 2^A_k*S^k(n)=3^k*n+C_k for any seed realizing the word.

Let r_k be the unique odd integer in [1,2^(A_k+1)) satisfying
    r_k = (2^A_k-C_k)*3^(-k) (mod 2^(A_k+1)).
Let M_k be the unique integer in [1,3^k) satisfying
    M_k = C_k*2^(-A_k) (mod 3^k).
The powers with negative exponents are modular inverses. For k=0 define r_0=1, M_0=0.

The "minimal positive seed" r_k genuinely realizes the word. This follows either from the 2-adic parity-cylinder theorem or, independently, by reversing the proposed exponents from the minimal positive odd terminal residue. Its endpoint is
    Y_k=(3^k*r_k+C_k)/2^A_k.

## 2. Binary overlap and the EXACT two-carry law

The endpoint Y_k is the **least positive odd** integer congruent to M_k modulo 3^k. As 3^k is odd, it must be either M_k or M_k+3^k, giving

    Y_k=M_k+q_k*3^k,  q_k in {0,1},
    q_k=1-(M_k modulo 2).

**Proof of minimality:** the least positive odd representative Y of the endpoint residue is between 1 and 2*3^k-1. Every prescribed reverse step x -> (2^a*x-1)/3 is integral (the terminal 3^k congruence is exactly the nested divisibility condition); since x and a are positive it is also a positive odd integer. The resulting seed is (2^A*Y-C)/3^k, strictly between 0 and 2^(A+1), so it equals r_k.

On appending exponent a=a_k, write the 2-adic seed lift as
    r_(k+1)=r_k+2^(A_k+1)*u_k,  0<=u_k<2^a,
and the 3-adic endpoint lift as
    2^a*M_(k+1)=3*M_k+1+3^(k+1)*v_k, 0<=v_k<2^a.
Substituting Y_k=M_k+q_k*3^k into the exact affine step gives the conservation identity

    **2^a*q_(k+1)+v_k=q_k+2*u_k.**

This is exact finite-word arithmetic, with no random-orbit or independence assumption. Its connection to known base-2/base-3 conversion should be credited; it is not a new solution to 3x+1.

## 3. Uniform deterministic 'dual lock' for a genuine positive seed

For every positive odd N with its *actual* infinite valuation sequence, for every
    k >= bit_length(N)
we have
    r_k=N,  M_k=S^k(N),  q_k=0.
Consequently u_k=v_k=0 for all sufficiently large k.

Proof: A_k>=k, so the odd residue modulo 2^(A_k+1) identifies N exactly once 2^k>=N+1. On the other end, S(x)+1 <= (3/2)(x+1) for x>0, so S^k(N)+1 <= (3/2)^k(N+1) <= 3^k. The actual terminal value is already the least positive representative modulo 3^k.

Furthermore, for an arbitrary infinite positive-exponent word the following are equivalent:
(a) it is realized by some fixed positive odd N;
(b) its seed-lift digits u_k vanish eventually;
(c) its endpoint-lift digits v_k vanish eventually.

(a)->(b),(c) by the previous paragraph; (b)->(a) because the canonical r_k stabilizes to an actual seed realizing all its prefixes; (c)->(b) because v_k=0 on a tail implies M_k odd on that tail, hence q_k=0, then the carry law forces u_k=0. This is an exact **positive-integer realizability test**, NOT a test of whether the resulting positive orbit reaches 1.

## 4. Pure critical irrational rotation cannot be a positive orbit

Consider the exact mechanical word
    a_j=floor((j+1)*log_2(3))-floor(j*log_2(3))  in {1,2}.
As log_2(3) is irrational, it is a nonperiodic Sturmian word with precisely L+1 different factors of length L.

Suppose a positive odd seed N follows this infinite word. Its odd states x_j are pairwise distinct (a repeated state would make the tail periodic). Among L+2 starting positions j=0,...,L+1, two length-L factors coincide. The corresponding states x_i!=x_j must satisfy
    |x_i-x_j| >= 2^(A+1),
where A is the sum of those L exponents. For the mechanical word A>=floor(L log_2 3), so 2^(A+1)>3^L.

But the real growth bound yields
    |x_i-x_j| < (N+1)*(3/2)^(L+1),
hence
    N+1 > (2/3)*2^L
for **every** L>=1. Contradiction. Therefore no fixed positive odd integer has exactly the critical mechanical valuation word forever.

Likewise any nonperiodic Sturmian word over positive integers is excluded by the weaker inequality N+1>(4/3)^(L+1). This is a specialization of the earlier factor-complexity obstruction; other higher-complexity aperiodic words, which could still code divergent positive orbits, are NOT excluded.

## 5. Deterministic experiment and tests

A 4096-symbol critical mechanical word is produced using only exact integers: floor(j log_2 3)=bit_length(3^j)-1. The least positive canonical seed after 4096 symbols has **6493 bits**. Over its 4096 finite lifts we see **2617 nonzero u digits** and **2616 nonzero v digits**. Both facts are *finite* observations; the preceding factor-complexity proof, not the finite table, establishes the infinite exclusion.

Companion files:
- src/dual_carry_arithmetic.py — exact cylinder reconstruction, independent fast/small modulus carry computation, finite checks.
- tests/test_dual_carry_arithmetic.py — five deterministic regression tests.
- notes/2026-11-22-mechanical-bicarries.csv — machine-readable checkpoints k=8,...,4096.

No Lean verification is claimed. The genuine next open issue is **after** positive-seed realizability: an eventual-zero carry sequence is satisfied by EVERY genuine positive odd orbit, including any hypothetical divergent one. Additional along-orbit global descent constraints are needed.

## Prior art

- Stérin and Woods (2020), *The Collatz Process Embeds a Base Conversion Algorithm*, https://mural.maynoothuniversity.ie/id/eprint/15714/
- Sodelin, *Collatz-Conjecture-Work*, route F endpoint residue gate, https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/routes/F_bounded_alphabet_endpoint_residue_gate.md
- Existing wandei note: notes/2026-11-22-no-mean-factor-complexity-floor.md (on this research branch).
