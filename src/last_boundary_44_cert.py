from fractions import Fraction

"""Exact certificate: a first-candidate survivor's last return to h=0
must occur within the final 44 odd-only steps.

This uses only integer/rational arithmetic plus an explicit rational interval
for log(2), log(3). It does not prove Collatz.
"""

K = 72057431991
A_K = 114208327604
N0 = 2075 * (1 << 60)
N_UPPER = Fraction(4 * (1 << 71), 3)


def log_interval(x: Fraction, terms: int = 220):
    assert x > 0
    z = (x - 1) / (x + 1)
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
alpha_lo = ln3_lo / ln2_hi
alpha_hi = ln3_hi / ln2_lo

# Certify the exact floors needed for the final 47-step mechanical suffix.
F = {}
for n in range(K - 47, K + 1):
    lo = n * alpha_lo
    hi = n * alpha_hi
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi
    F[n] = flo

assert F[K] == A_K - 1


def mech(n: int) -> int:
    return F[n + 1] - F[n]


# Backward cylinder residues.
# If a suffix beginning at x has first exponent a and the shorter suffix
# requires x_next == R (mod 2^bits), then
#   3*x + 1 = 2^a*x_next
# pins x modulo 2^(bits+a).
# We store B = total suffix exponent, so the modulus is 2^(B+1).
records = {}

a = mech(K - 1) + 1  # terminal first-contraction exponent
B = a
mod = 1 << (B + 1)
num = (1 << a) - 1
q = (-num * pow(mod, -1, 3)) % 3
R = (num + q * mod) // 3
records[1] = (B, q, R)

for ell in range(2, 48):
    a = mech(K - ell)
    B += a
    mod = 1 << (B + 1)
    num = (R << a) - 1
    q = (-num * pow(mod, -1, 3)) % 3
    R = (num + q * mod) // 3
    records[ell] = (B, q, R)

# Very crude but exact correction-product bound.
# z=K/(3*N0) < 1/65 and exp(z) < 1/(1-z) < 65/64.
assert 65 * K < 3 * N0

# Hence any h=0 state before K satisfies
# x/N < 2*(65/64)=65/32.
X_UPPER = Fraction(65, 32) * N_UPPER

B45, q45, R45 = records[45]
B46, q46, R46 = records[46]
B47, q47, R47 = records[47]

# ell=45: modulus 2^73 already exceeds the whole admissible x-band,
# so only the least positive residue could occur, and it is too high.
assert B45 == 72
assert X_UPPER < (1 << 73)
assert Fraction(R45) > X_UPPER

# ell=46: again there is a unique representative in the admissible x-band.
# The phase theta_{K-46} is <1/2.
m46 = K - 46
theta46_hi = m46 * alpha_hi - F[m46]
assert theta46_hi < Fraction(1, 2)

# correction product <65/64, and sqrt(2)*(65/64) < 3/2.
assert 4 * 2 * 65 * 65 < 9 * 64 * 64

# Therefore x_m/N <3/2. But R46>2^72, so
# N > (2/3)R46 > (4/3)2^71, contradicting N_UPPER.
assert B46 == 73
assert X_UPPER < (1 << 74)
assert R46 > (1 << 72)
assert Fraction(2 * R46, 3) > N_UPPER

# ell>=47: extend farther backward through the critical mechanical word.
# Dropping every nonnegative wrap term gives a lower comparison recurrence
# y <- (2^a y - 1)/3.
# Over any contiguous mechanical block of s steps, its multiplicative factor
# lies strictly between 1/2 and 2. Each additive -1 contribution is weighted
# by a later block product <2, so the total subtraction is <2s/3.
# Since s<K, every ell>=47 therefore has
#   R_ell > R47/2 - 2K/3.
GLOBAL_LOWER = Fraction(R47, 2) - Fraction(2 * K, 3)
assert GLOBAL_LOWER > X_UPPER

if __name__ == "__main__":
    print("CERTIFIED")
    print("R45 =", R45)
    print("R46 =", R46)
    print("R47 =", R47)
    print("last h=0 return must have suffix length <= 44")
