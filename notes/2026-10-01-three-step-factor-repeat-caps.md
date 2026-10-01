# Repetition caps for the two three-step return factors

Status: exact irrational-rotation lemma inside the first-candidate defect framework. Not a Collatz proof.

Write

- beta = log_2(3)-1,
- b = 1-beta = 2-log_2(3),
- theta_n = {n log_2 3}.

Then r_n=2 iff theta_n >= b. We use only the exact inequalities

1/2 < beta < 3/5,

which follow from

3^2 > 2^3  (9>8)

and

3^5 < 2^8  (243<256).

Equivalently,

2/5 < b < 1/2.

A three-step boundary excursion can have only the mechanical factor 212 or 221.

## 1. The factor 221 cannot repeat immediately

A 221 factor starts exactly when

theta_n in [2b,1).

Indeed, the first two symbols are 2 precisely when theta_n>=2b, while the third symbol is then forced to be 1.

After one complete 221 block, the phase is

theta_{n+3}=theta_n+3 beta-2=theta_n+1-3b.

Since theta_n<1,

theta_{n+3}<2-3b.

For another 221 block to start immediately, we would need theta_{n+3}>=2b. But

2-3b < 2b

is equivalent to b>2/5, which holds because 3^5<2^8.

Therefore

(221)^2 is impossible.

So an immediate sequence of three-step 221 boundary excursions has length at most one.

## 2. The factor 212 can repeat at most twice

A 212 factor starts exactly when

theta_n in [b,2b).

After one complete 212 block the same net phase increment applies:

theta_{n+3}=theta_n+1-3b.

Two consecutive 212 blocks are possible exactly when the second start phase remains at least b, i.e.

theta_n >= 4b-1.

The interval [4b-1,2b) is nonempty because b<1/2, so two consecutive 212 blocks do occur.

For three consecutive blocks we would additionally need

theta_n >= 7b-2.

But

7b-2 >= 2b

is equivalent to b>=2/5, which holds strictly. Hence the required start interval is empty.

Therefore

(212)^3 is impossible,

and the exact maximum number of immediately consecutive 212 blocks is two.

## 3. Consequence for three-step excursions

Every genuine three-step boundary excursion is mechanically 212 or 221. Hence:

- a 221 three-step excursion can never be followed immediately by another 221 three-step excursion;
- at most two 212 three-step excursions can occur immediately back-to-back.

Combined with the sharp repayment certificate, which allows at most five genuine 212/113 excursions in the entire first-candidate prefix, long immediate chains of three-step returns must be broken by either boundary waiting, a longer excursion, or a different local return structure.
