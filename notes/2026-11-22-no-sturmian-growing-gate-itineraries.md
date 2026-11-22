# 2026-11-22 — Growing-renewal survivors cannot have periodic or Sturmian scripts

**Status: rigorous conditional exclusion, not a Collatz proof.** This is an adaptation of the earlier valuation-word complexity argument in \`notes/2026-11-22-no-mean-factor-complexity-floor.md\`, not a claim of a new general technique. Only the *restricted all-growing B1/B3 renewal subsystem* is under discussion.

Let a positive odd integer N take exclusively the two growing gates forever:
\[
B_1(n)=(3n+1)/2 \ (n\equiv7\bmod8),\qquad
B_3(n)=(9n+5)/8 \ (n\equiv27\bmod32).
\]
Let \(x_j\) denote the strictly increasing positive renewal checkpoints, and \(b_j\in\{1,3\}\) the gate symbols. For a word \(w\) of L gate symbols, let its binary precision cost \(A(w)\) be the sum of 1 for every B1 and 3 for every B3; thus \(A(w)\ge L\).

**Cylinder-collision lemma.** If two positive states x,y have the same next L gate symbols w, then
\[
x\equiv y\pmod {2^{A(w)+2}}.
\]
Proof: the L-macro composition has an affine difference coefficient \(3^{p(w)}/2^{A(w)}\). Both endpoint states are 3 mod4, hence their difference is divisible by 4. Multiplying by 2^A and using invertibility of \(3^p\) modulo powers of 2 gives the congruence.

**Archimedean size envelope.** Every growing gate obeys
\[
B_i(n)+1\le\tfrac32(n+1).
\]
So \(x_j+1\le(3/2)^j(N+1)\).

For L≥1 let \(K(L,N)\) be the greatest integer K≥0 with
\[
(3/2)^K(N+1)\le2^{L+2}
\]
(or -1 if no such integer exists). The distinct states \(x_0,\ldots,x_K\) all lie in \([1,2^{L+2}-1]\). If any two of their starting length-L gate words coincided, the collision lemma would force their nonzero difference to be at least \(2^{L+2}\), impossible. Hence the factor complexity of the infinite gate word satisfies
\[
p_b(L)\ge K(L,N)+1,
\qquad
\boxed{\liminf_{L\to\infty}p_b(L)/L\ge1/\log_2(3/2)\approx1.70951129135}.
\]

**Consequences:** no positive integer can remain in B1/B3 forever with an ultimately periodic or **Sturmian** renewal word (Sturmian words have exactly L+1 factors of length L). More generally any sublinear or sufficiently low-slope (<1.709511...) complexity word is excluded.

**Crucial limitations:** non-Sturmian high-complexity 2-adic itineraries still exist; the statement does NOT show that the bad-only Cantor survivor set contains no positive integers. And even empty positive-integer intersection of the bad-only set would not prove Collatz, since general trajectories can have good/local-descent gates that do not return below the original starting value. This exclusion is a clean restriction on the simple 'irrational rotation' interpretation, not the missing global convergence theorem.
