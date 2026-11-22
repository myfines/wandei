# 2026-11-22 — Exact phase switching, recharge, and an obstruction to naive Collatz Lyapunov arguments

**Status: elementary exact deductions and integer tests, NOT a proof of Collatz.**
Odd-only map S(n)=(3n+1)/2^v2(3n+1). The fixed-word budget result is already treated in other work (see sources), so it is **not claimed new**.

## 1. Exact template phase budget
For a word w=(a_0,...,a_(p-1)) of positive 2-adic exponents, let
A=sum_i a_i, A_j=sum_(i<j) a_i,
C_w=sum_(j=0..p-1) 3^(p-1-j) 2^A_j,
D_w=2^A-3^p, H_w(n)=D_w*n-C_w.

All C_w,D_w are odd, D_w!=0. The rational 2-adic fixed point of the formal return map F_w(x)=(3^p*x+C_w)/2^A is c_w=C_w/D_w. Its 2-adic orbit genuinely has exponent pattern w repeated indefinitely.

For every positive odd integer n and q>=1:

    n follows exactly the first q copies of w
      iff 2^(qA+1) divides H_w(n).

Therefore if H_w(n)!=0, the maximal number of complete repeated copies is
floor((v2(H_w(n))-1)/A); if H_w(n)=0, n is a genuine positive cycle point.
The equality is a parity-cylinder identity, not a proof of global convergence.

Euler phase encoding: exp(2*pi*i*H_w(n)/2^(qA+1))=1 iff this q-copy match holds. The statement is **exact modular arithmetic**, not a floating-point trigonometric test.

## 2. Height barrier and sharp positive expanding shadows
If 3^p>2^A, then D_w<0 and the 2-adic fixed point c_w is negative in the real numbers. A positive integer n following q copies necessarily obeys

    2^(qA+1) <= abs(D_w)*n + C_w.

The expanding word (1,2) has A=3, C=5, D=-1 and c_w=-5. Define n_q=2^(3q+1)-5. For q>=1, n_q follows (1,2)^q, S^(2q)(n_q)=2*9^q-5, and its NEXT exponent is precisely 3 instead of the periodic template's 1. This sharp exact family can exhibit arbitrarily long finite growth without proving infinite divergence.

## 3. Cross-template phase holonomy
For another word v with parameters p_v,A_v,C_v,D_v, define

    K_(w,v)=D_w*C_v-D_v*C_w.

If the positive seed n really follows v once, direct affine calculation gives:

    H_w(S^(p_v)(n)) = (3^(p_v)*H_w(n)+K_(w,v))/2^(A_v).

This is an exact switching / recharge identity. **But K is no independent miracle invariant.** Since both denominators D are odd,

    v2(K_(w,v))=v2(c_v-c_w).

Let the two periodic exponent scripts first differ at index j, after the common prefix exponent sum A_<j, where their next exponents are a_j and b_j. Then

    v2(K_(w,v))=A_<j+min(a_j,b_j).

If the infinite scripts coincide, K=0. This follows from first-differing valuation and exact 2-adic distance scaling on the shared prefix. Our tests confirm the identity for all pairs of words of lengths <=3 and exponent values <=4. The determinant only repackages common symbolic prefixes; it has not yielded an independent constraint on infinite positive orbits.

## 4. Arbitrary one-step recharge close to stable point 1
Let E(n)=v2(n-1), a 2-adic closeness measure to the fixed point 1. For ANY integer h>=2 choose the least positive n_h with

    3*n_h == 1 (mod 2^(h+1)).

Then n_h==3 (mod 4), so E(n_h)=1 and v2(3n_h+1)=1, while

    S(n_h)-1=(3*n_h-1)/2 is divisible by 2^h.

Thus

    E(n_h)=1,    E(S(n_h))>=h.

For h=4, n_h=11 and S(11)=17: the 2-adic defect jumps from 1 to 4. Arbitrarily large *legitimate* recharge in one step disproves global monotone descent of this fixed-anchor phase budget. This says **nothing about the existence of more sophisticated multi-coordinate Lyapunov functions**.

## 5. Conclusion and next missing theorem
A fixed periodic word consumes 2-adic phase budget at an exactly determined rate. Once the script changes, the phase may be replenished by an arbitrary amount. The cross-template determinant only measures how many initial exponent symbols match. Consequently these elementary tools **do not imply a universal decrease along a single aperiodic infinite orbit**.

The real target remains a seed-uniform coupling between (i) Archimedean height, (ii) 2-adic phase recharges and switches, and (iii) the 3-adic inverse ancestor constraints, able to control a changing, potentially nonperiodic word. This is OPEN.

### Reproduction
Run:
    python src/phase_switch_budget.py
    python -m unittest discover -s tests -p 'test_phase_switch_budget.py' -v

7 local tests pass, including independent trajectory iteration, all word pairs length<=3 / exponents<=4, exact rational fixed points, and one-step recharge witnesses through h=79.

### Prior sources
- Independent earlier fixed-word repetition budget: https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/research/blind-2026-09-05/SymbolicNotes.md
- 2-adic periodic points: https://aue.repo.nii.ac.jp/record/704/files/kenshi52511.pdf
- Bernstein--Lagarias conjugacy: https://websites.umich.edu/~lagarias/doc/bernstein.pdf
