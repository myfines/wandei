# Extremal sampled return pair near the critical density

Status: exact consequence of the eight mod-9 first-return families. This is structural infrastructure, not a proof of Collatz.

For a first return from one value congruent to 2 mod 9 to the next, let q be the number of odd Terras steps and t the total number of Terras steps. The main multiplicative coefficient is

c = 3^q / 2^t.

The exact eight-family classification shows:

- the largest contracting coefficient is attained at (q,t)=(5,8):
  c_- = 3^5/2^8 = 243/256;
- the smallest expanding coefficient is attained at (q,t)=(7,11):
  c_+ = 3^7/2^11 = 2187/2048.

Thus

5/8 < alpha < 7/11,

where alpha = log(2)/log(3), and

7*8 - 5*11 = 1.

Hence 5/8 and 7/11 are Farey neighbours bracketing the critical odd-step density alpha.

Equivalently, in logarithmic coefficient coordinates

Delta = q log_2(3) - t,

all contracting sampled returns satisfy

Delta <= Delta_- := 5 log_2(3)-8 < 0,

and all expanding sampled returns satisfy

Delta >= Delta_+ := 7 log_2(3)-11 > 0.

Numerically,

Delta_- = -0.075187496394...,
Delta_+ =  0.094737505048....

Therefore the slowest possible sampled compensation uses these two extremal blocks. If an idealized schedule used only these blocks and had zero mean logarithmic drift, the required expanding-block frequency f would satisfy

f Delta_+ + (1-f) Delta_- = 0,

so

f = (8-5 log_2 3)/(2 log_2 3 - 3)
  = 0.442474596180... .

This frequency is transcendental: it is a nonconstant fractional-linear transformation of log_2(3), which is transcendental by Gelfond-Schneider (since its reciprocal log 2/log 3 is transcendental).

The mediant of the two extremal densities is

(5+7)/(8+11)=12/19,

which lies very close to alpha. The product of one weakest contraction and one weakest expansion is

c_- c_+ = 3^12/2^19 = 531441/524288 > 1.

Interpretation: the sampled dynamics has a canonical two-block near-critical model. Any return using a different family pays a strictly larger absolute logarithmic drift cost. A remaining counterexample may still use other blocks, but this pair gives the extremal envelope for any argument that only uses sampled coefficient drift.

Potential next use: compare any slow-drift sampled tail to the mechanical/Sturmian word over the two symbols {c_-,c_+} having slope f, and quantify the extra drift contributed by non-extremal return blocks.