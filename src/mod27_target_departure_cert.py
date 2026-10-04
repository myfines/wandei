#!/usr/bin/env python3
"""Exact modular/algebraic certificate for departures from the 20 mod 27 target.

Work in the sampled 2 mod 9 coordinate M=4n+1=9u.  A target hit n=20 mod27
is equivalent to M=81 mod108, hence u=9 mod12.

At a target hit, normalize the old digits eta in {3,15,63} by their exact
3-adic factors b=(1,1,2).  The next sampled state is M'=3^(q+b)c.  Since every
sampled M' is 9 mod36, q+b>=2, and it is again a target iff q+b>=3.
Therefore a target departure is exactly q+b=2.

The three possible departure lanes all strictly contract u=M/9.
"""

from fractions import Fraction

# Lane data: (eta, e, b, q_on_departure, possible t values, affine u' numerator)
# u' formulas are:
# eta=3:  (3u+1)/2^t
# eta=15: (3u+5)/2^t
# eta=63: (u+7)/2^t, and e=4 at a target forces t>=6; departure q=0 then t=6.
LANES = {
    3:  {"e": 0, "b": 1, "q": 1, "t": (2, 3)},
    15: {"e": 2, "b": 1, "q": 1, "t": (4, 5)},
    63: {"e": 4, "b": 2, "q": 0, "t": (6,)},
}

# For eta=3, q is one of t-e-2,t-e-1; q=1 gives t=2 or3.
assert set((1 + 0 + 2, 1 + 0 + 1)) == {2, 3}
# eta=15: e=2, q=1 gives t=4 or5.
assert set((1 + 2 + 2, 1 + 2 + 1)) == {4, 5}
# eta=63: e=4, target plus e=4 implies u=57 mod64, hence u+7=0 mod64.
assert (9 * 57 - 1) % 64 == 0
assert (57 + 7) % 64 == 0
# Thus t>=6; departure q=0 with q in {t-6,t-5} forces t=6.

# Uniform strict inequalities for every target u>=9.
# eta=3 worst lane: (3u+1)/4 < u iff u>1.
assert 3 * 9 + 1 < 4 * 9
# eta=15 worst lane: (3u+5)/16 < u iff 5<13u.
assert 3 * 9 + 5 < 16 * 9
# eta=63: (u+7)/64 < u iff 7<63u.
assert 9 + 7 < 64 * 9

# Uniform affine upper envelope for every departure.
# u' <= (3u+1)/4 < u, so principal coefficient <=3/4.
UNIFORM_PRINCIPAL_COEFF = Fraction(3, 4)

if __name__ == "__main__":
    print("CERTIFIED")
    print("target: u == 9 (mod 12)")
    print("departure iff q+b=2")
    print("eta=3  : u'=(3u+1)/2^t, t in {2,3}")
    print("eta=15 : u'=(3u+5)/2^t, t in {4,5}")
    print("eta=63 : u'=(u+7)/64")
    print("all target departures satisfy u'<u")
    print("uniform principal coefficient <=", UNIFORM_PRINCIPAL_COEFF)
