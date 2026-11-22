# 2026-11-22 — Every finite 20-mod-27 hit word is realized by positive integers

**Status:** elementary exact modular theorem, a no-go result for finite target-bit restrictions. **NOT** a proof or disproof of Collatz; no novelty claim relative to the classical full 2-adic valuation-language property.

Use the odd-only Syracuse map S(n)=(3n+1)/2^a, a=v2(3n+1), for positive odd n. Define a **hit bit** h(n)=1 iff the following shortcut block T(n),...,T^a(n)=S(n) contains a state congruent to 20 modulo 27. The source n is not included in its own block. Our preceding note proved

    h(n)=1  <=>  a >= tau(n mod 9),
    tau=(11,13,9,17,1,15,5,7,3) at residues 0,...,8.

## Theorem 1: The finite target-hit language is the full binary language

For **every finite binary word** b=(b_0,...,b_(L-1)), there are infinitely many positive odd seeds n such that

    (h(n),h(S(n)),...,h(S^(L-1)(n))) = b.

**Constructive proof.** Start from the modulus-9 state r=8. The transition formula

    r'=(3r+1)*2^(-a) (mod 9)

fixes r=8 for BOTH a=1 and a=7, because 2^7=2 modulo 9 and 7*2^(-1)=8 modulo 9. The threshold tau(8)=3, so a=1 gives h=0 and a=7 gives h=1. Assign exponent a_j=1+6*b_j.

For any positive-exponent word a_j, standard exact Syracuse parity-cylinder arithmetic produces a unique odd initial residue modulo 2^(A+1), A=sum a_j. This residue can be combined with n=8 mod9 using CRT, giving one nonempty arithmetic progression of positive odd seeds modulo 9*2^(A+1). Every seed on that progression follows the exact exponent script, stays in residue class 8 modulo 9 at odd checkpoints, and realizes b. QED.

This uses **genuine positive integer trajectories** for each *finite* b. It emphatically does **not** assert one fixed positive integer realizes an arbitrarily prescribed **infinite** target sequence. The seed may grow with L.

**Consequence:** The hit-bit projection has NO finite forbidden blocks. A purported global proof relying solely on banning some finite pattern of hits/nonhits, without additional real-height or fixed-seed compatibility hypotheses, cannot work.

## Theorem 2: Any finite target pattern can occur inside a prefix with NO first descent

Let H be the number of ones in b. Prepend 10H zero bits, producing c=0^(10H)b, and use exactly the preceding exponent coding (a=1 for 0, a=7 for 1) with n=8 mod9.

For any prefix of c containing h hit blocks and ell nonhit blocks **after** the initial padding, the affine *linear coefficient* of the entire odd-only composition is

    (3/2)^(10H+ell)*(3/128)^h
    = [(3/2)^10*(3/128)]^h * (3/2)^[10(H-h)+ell].

Since (3/2)^10*(3/128)=177147/131072 >1, every nonempty prefix has linear coefficient >1 (unless no steps were taken). Every additive Collatz correction is positive, so every intermediate odd state satisfies S^j(n)>n for all j=1,...,10H+L.

Thus arbitrary long adjacent hit runs, or any prescribed finite binary target word, can be preceded by sufficient legitimate growth credit while remaining above the ORIGINAL seed throughout. **This even holds at every intermediate shortcut T-step**, not just odd-only checkpoints: inside each odd block, successive shortcut states (3x+1)/2^j decrease with j and are therefore all at least the final odd endpoint S(x)>n. The construction is finite and seed-dependent, not a divergent orbit.

## Theorem 3: Arbitrarily long target-free growth

For every integer q>=1 the explicit positive odd seed

    n_q=9*2^(q+1)-1

satisfies, for all 0<=j<=q,

    S^j(n_q)=9*3^j*2^(q+1-j)-1.

For j<q, the true exponent a_j=1, the state is 8 mod9, and therefore no shortcut block hits 20 mod27. All q odd steps are strictly increasing. It follows that no target-recurrence gap cap **uniform in positive seed height** exists; any quantitative gap theorem must incorporate Archimedean height or equivalent information.

## Reproduction, limitations, and sources

Implementation: src/mod27_gap_language.py.
Independent direct-orbit and exact-DP tests: tests/test_mod27_gap_language.py.

Local exact check: 8190 nonempty finite target words of lengths <=12, and all 2^1+...+2^9=1022 binary words embedded as no-first-descent suffixes; independent shortcut target scans also agree. These are software regression checks, not formal Lean proofs. All-depth assertions above have independent algebraic proofs.

The strongly sufficient target 20 mod27 for divergent positive shortcut orbits is due to Monks–Monks–Monks–Monks (2013), arXiv:1204.3904, https://arxiv.org/abs/1204.3904. The finite residue-class word realization is classical 2-adic cylinder theory, not an originality claim.

**Open problem:** show an infinite fixed positive integer trajectory cannot simultaneously satisfy the necessary target recurrence AND its global real-height/2-/3-adic compatibility; no such theorem is proved here.
