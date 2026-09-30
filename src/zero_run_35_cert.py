from fractions import Fraction

"""Exact exhaustive certificate excluding 35 consecutive h=0 steps
inside the first coefficient-contraction candidate.

The proof over-approximates the allowed starting-state band and checks every
integer realizer of every length-35 critical mechanical factor. Each such
integer falls below the live verification floor N0 under exact odd-only
Syracuse iteration. Therefore it cannot lie on the orbit of a least
counterexample.

This is a finite integer/rational certificate, not a proof of Collatz.
"""

N0 = 2075 * (1 << 60)
N_UPPER = Fraction(4 * (1 << 71), 3)
X_UPPER = Fraction(65, 32) * N_UPPER
LENGTH = 35


def log_interval(x: Fraction, terms: int = 220):
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
omega_lo = alpha_lo - 1
omega_hi = alpha_hi - 1


def mechanical_factors(n: int):
    """Return all n+1 length-n exponent factors in {1,2}, rigorously."""
    endpoints = [(Fraction(0), Fraction(0), 0)]
    for j in range(1, n + 1):
        lo = j * omega_lo
        hi = j * omega_hi
        flo = lo.numerator // lo.denominator
        fhi = hi.numerator // hi.denominator
        assert flo == fhi
        c = flo + 1
        e_lo = Fraction(c) - hi
        e_hi = Fraction(c) - lo
        assert 0 < e_lo < e_hi < 1
        endpoints.append((e_lo, e_hi, j))

    endpoints.sort(key=lambda z: (z[0] + z[1]) / 2)
    for left, right in zip(endpoints, endpoints[1:]):
        assert left[1] < right[0]

    words = set()
    for i, (_, e_hi, _) in enumerate(endpoints):
        next_lo = endpoints[i + 1][0] if i + 1 < len(endpoints) else Fraction(1)
        theta = (e_hi + next_lo) / 2

        word = []
        for j in range(n):
            xlo = theta + j * omega_lo
            xhi = theta + j * omega_hi
            ylo = theta + (j + 1) * omega_lo
            yhi = theta + (j + 1) * omega_hi
            fxlo = xlo.numerator // xlo.denominator
            fxhi = xhi.numerator // xhi.denominator
            fylo = ylo.numerator // ylo.denominator
            fyhi = yhi.numerator // yhi.denominator
            assert fxlo == fxhi and fylo == fyhi
            bit = fylo - fxlo
            assert bit in (0, 1)
            word.append(1 + bit)

        words.add(tuple(word))

    assert len(words) == n + 1
    return sorted(words)


def cylinder(word):
    """Least residue R mod 2^(A+1) realizing exactly this exponent word."""
    d = 0
    A = 0
    for a in word:
        d = 3 * d + (1 << A)
        A += a
    mod = 1 << (A + 1)
    R = (pow(pow(3, len(word), mod), -1, mod) * ((1 << A) - d)) % mod
    return R, A, mod


def ceil_fraction(x: Fraction):
    return -((-x.numerator) // x.denominator)


def floor_fraction(x: Fraction):
    return x.numerator // x.denominator


def first_below_floor(x: int, max_steps=1000):
    for step in range(max_steps + 1):
        if x < N0:
            return step, x
        y = 3 * x + 1
        a = (y & -y).bit_length() - 1
        x = y >> a
    raise AssertionError(("candidate did not fall below N0", x))


words = mechanical_factors(LENGTH)
assert len(words) == 36

checked = 0
max_descent_steps = 0
max_descent_seed = None

for word in words:
    R, A, mod = cylinder(word)

    # Deliberately ignore the phase theta and use the larger uniform h=0 band
    # N0 <= x < X_UPPER. This is an over-approximation.
    tmin = max(0, ceil_fraction(Fraction(N0 - R, mod)))
    # Strict x < X_UPPER:
    tmax = floor_fraction((X_UPPER - 1 - R) / mod)

    if tmax < tmin:
        continue

    for t in range(tmin, tmax + 1):
        x = R + t * mod
        assert N0 <= x < X_UPPER
        steps, y = first_below_floor(x)
        checked += 1
        if steps > max_descent_steps:
            max_descent_steps = steps
            max_descent_seed = x

assert checked == 1527532
assert max_descent_steps <= 252

if __name__ == "__main__":
    print("CERTIFIED")
    print("mechanical factors:", len(words))
    print("integer realizers checked:", checked)
    print("maximum odd-only steps to fall below N0:", max_descent_steps)
    print("seed attaining maximum:", max_descent_seed)
    print("there is no 35-step h=0 mechanical block in a first-candidate survivor")
