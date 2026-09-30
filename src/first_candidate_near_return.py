from fractions import Fraction

"""Exact near-return certificate for the first coefficient-contraction candidate.

Under the least-counterexample hypothesis and the certified first candidate,
if x_k is the odd-only endpoint then

    0 <= x_k - N <= 14259179197 < 2^34.

Only integer/rational arithmetic is used. This is not a Collatz proof.
"""

K = 72057431991
A = 114208327604
N0 = 2075 * (1 << 60)
N_UPPER = Fraction(4 * (1 << 71), 3)


def log_interval(x: Fraction, terms: int = 220):
    assert x > 0
    z = (x - 1) / (x + 1)
    assert 0 <= z < 1
    z2 = z * z
    s = Fraction(0)
    p = z
    for n in range(terms):
        s += 2 * p / Fraction(2 * n + 1)
        p *= z2
    tail = 2 * (z ** (2 * terms + 1)) / (
        Fraction(2 * terms + 1) * (1 - z2)
    )
    return s, s + tail


ln2_lo, ln2_hi = log_interval(Fraction(2))
ln3_lo, ln3_hi = log_interval(Fraction(3))

# D = A log 2 - K log 3 > 0 is the homogeneous logarithmic contraction.
D_lo = A * ln2_lo - K * ln3_hi
D_hi = A * ln2_hi - K * ln3_lo
assert D_lo > 0

# Exact product identity:
# log(x_K/N) = -D + sum_i log(1 + 1/(3 x_i)).
# Least-counterexample minimality gives x_i >= N >= N0, hence
# log(x_K/N) < -D_lo + K/(3 N0) = eps.
eps = Fraction(K, 3 * N0) - D_lo
assert 0 < eps < 1

# For 0 <= z < 1, exp(z) <= 1/(1-z), hence exp(z)-1 <= z/(1-z).
# Also N < N_UPPER. Therefore
#   delta = x_K-N < N_UPPER * eps/(1-eps).
delta_upper_real = N_UPPER * eps / (1 - eps)
DELTA_MAX = delta_upper_real.numerator // delta_upper_real.denominator

assert delta_upper_real < DELTA_MAX + 1
assert DELTA_MAX == 14259179197
assert DELTA_MAX < (1 << 34)

# Both N and x_K are odd, so their difference is even. This slightly sharpens
# the integer maximum, though the clean 2^34 bound is the useful statement.
DELTA_MAX_EVEN = DELTA_MAX if DELTA_MAX % 2 == 0 else DELTA_MAX - 1
assert DELTA_MAX_EVEN == 14259179196

if __name__ == "__main__":
    print("CERTIFIED")
    print("D interval:", D_lo, D_hi)
    print("epsilon:", eps)
    print("delta <", delta_upper_real)
    print("integer delta <=", DELTA_MAX)
    print("even delta <=", DELTA_MAX_EVEN)
    print("delta < 2^34 =", 1 << 34)
