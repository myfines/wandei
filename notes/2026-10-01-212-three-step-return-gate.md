# Exact phase window for a three-step `212 / 113` boundary return

Status: exact local consequence of the mechanical rotation and the previously proved heavy-repayment phase gate. Not a Collatz proof.

Write

- beta = log_2(3)-1,
- b = 1-beta = 2-log_2(3),
- theta_n = {n log_2(3)},
- g = log_2(128/65).

A genuine three-step boundary excursion of mechanical type `212` has the unique valuation pattern `113`:

h: 0 -> 1 -> 1 -> 0.

Let theta_0 be the phase at the departure step. The condition that the first three mechanical letters are `212` is

b <= theta_0 < 2b.

After the first `r=2` step,

theta_1 = theta_0 - b,

so 0 <= theta_1 < b. After the following `r=1` step,

theta_2 = theta_1 + beta = theta_0 + 2beta - 1.

The terminal step has h=1, r=2, a=3, so the exact heavy-repayment phase gate requires

theta_2 > g = log_2(128/65).

Hence the following equivalent necessary conditions hold:

1. departure phase:

   theta_0 > g - (2beta-1);

2. intermediate `r=1` phase:

   theta_1 > g-beta;

3. terminal phase:

   theta_2 > g.

Because theta_1 is already restricted to [0,b), the admissible intermediate interval is exactly

(g-beta, b).

Its width simplifies to

b-(g-beta) = 1-g = log_2(65/64).

Therefore every genuine `212 / 113` three-step boundary return must pass through the top slice of the `r=1` phase interval having exact width

log_2(65/64) = 0.0223678130284544... .

Equivalently,

boxed: 212/113 return => theta_1 in (log_2(128/65)-beta, 1-beta).

This is stronger and more directly usable than merely saying that the terminal repayment lies in the top 2.24 percent of the full phase circle: it identifies the precise narrow subinterval of the intermediate `r=1` phase that can mediate a three-step return.

This local gate is a natural next input for the pair-constrained weighted boundary optimization.