# Sharp odd-height repayment phase gate inside the first candidate

Status: exact consequence of the fixed first-candidate length, the verified frontier, the side-branch altitude lemma, and Denjoy--Koksma. Not a Collatz proof.

The earlier repayment gate used the coarse global estimate

P_n = product_{i<n}(1+1/(3x_i)) < 65/64.

Inside the fixed first coefficient-contraction candidate this is vastly weaker than necessary.

For every preterminal state of a least counterexample,

x_i >= N >= N0,

where

N0 = 2075*2^60,

and the candidate length is

k = 72,057,431,991.

Therefore

P_n <= (1+1/(3N0))^n.

Using

log(1+u) <= u

and

exp(t) <= 1/(1-t) for 0<=t<1,

we obtain uniformly for n<=k

P_n <= P_bar := 1/(1-k/(3N0))
     = 3N0/(3N0-k).

`src/sharp_repayment_phase_cert.py` evaluates

epsilon = log_2(P_bar)

with rational logarithm intervals and proves

epsilon < 1/60,000,000,000,

numerically about

1.448485739445... * 10^(-11).

## Odd-height direct repayment at r=2

Suppose h_n=2m+1 is positive and odd, r_n=2, and one step repays the entire defect:

h_{n+1}=0.

Then

a_n=h_n+2=2m+3.

The side-branch altitude lemma gives

x_n > 4^(m+1) N = 2^(h_n+1) N.

On the other hand the exact height/product identity gives

x_n/N = 2^(h_n+theta_n) P_n
      <= 2^(h_n+theta_n) P_bar,

where

theta_n={n log_2 3}.

Hence necessarily

2^(h_n+theta_n) P_bar > 2^(h_n+1),

so

theta_n > 1-log_2(P_bar).

Thus every odd-height r=2 direct repayment is confined to the extreme top phase window

(1-epsilon,1),

whose width is less than 1/60,000,000,000.

This replaces the old width

log_2(65/64) = 0.0223678...

by a window roughly 1.5 billion times narrower.

## Global count inside the first candidate

The indicator of this top phase interval has total variation 2. Since

k=qL+qU

is the sum of the same two convergent denominators used by the first-candidate certificate, Denjoy--Koksma applied to the two blocks gives

# {0<=n<k : theta_n > 1-epsilon}
<= k*epsilon + 4
< 6.

Therefore the integer count is at most

5.

So throughout the entire 72-billion-step first-candidate prefix,

there can be at most five odd-height direct repayments occurring at r=2.

In particular every `212 / 113` three-step boundary excursion is one of at most five such events.

This is currently much stronger than the earlier 2.24-percent phase-gate statement and should replace it in subsequent branch-A arguments.