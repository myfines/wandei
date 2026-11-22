#!/usr/bin/env python3
"""Exact 3-adic turn coordinates for one-step odd Collatz ancestors.

Odd Syracuse map S(n)=(3*n+1)/2**v2(3*n+1). All finite computations
use integer arithmetic. No claim of solving the Collatz conjecture.
"""


def v2(x: int) -> int:
    assert x > 0
    return (x & -x).bit_length() - 1


def v3(x: int) -> int:
    assert x != 0
    x, count = abs(x), 0
    while x % 3 == 0:
        x //= 3
        count += 1
    return count


def odd_step(n: int) -> int:
    assert n > 0 and n % 2 == 1
    return (3*n + 1) >> v2(3*n + 1)


def first_exponent(m: int) -> int:
    """Smallest a>=1 with 2**a*m == 1 (mod 3)."""
    assert m > 0 and m % 2 == 1 and m % 3 != 0
    return 2 if m % 3 == 1 else 1


def ancestor(m: int, turn: int) -> int:
    """The (turn)-th positive odd direct preimage of target m."""
    assert isinstance(turn, int) and turn >= 0
    a = first_exponent(m) + 2*turn
    numerator = (1 << a) * m - 1
    assert numerator % 3 == 0
    return numerator // 3


def turn_coordinates(n: int):
    """Bijection odd n <-> (odd 3-unit target m, turn t>=0)."""
    m = odd_step(n)
    a = v2(3*n+1)
    assert (a - first_exponent(m)) % 2 == 0
    t = (a - first_exponent(m)) // 2
    assert ancestor(m, t) == n
    return m, t


def ancestor_mod(m: int, turn: int, k: int) -> int:
    """Compute ancestor mod 3^k without forming astronomically large 4^t."""
    assert k >= 1 and turn >= 0
    modulus = 3**k
    exponent = first_exponent(m) + 2*turn
    numerator = (m * pow(2, exponent, 3*modulus) - 1) % (3*modulus)
    assert numerator % 3 == 0
    return (numerator // 3) % modulus


def phase_lift(m: int, residue: int, k: int) -> int:
    """Unique t in [0,3^k) with ancestor(m,t) == residue mod 3^k.

    Base-3 phase lifting, with 3 candidates per digit.
    """
    assert k >= 1
    t = 0
    for j in range(1, k + 1):
        base = 3**(j - 1)
        hits = [t + digit*base for digit in (0, 1, 2)
                if ancestor_mod(m, t+digit*base, j) == residue % 3**j]
        assert len(hits) == 1
        t = hits[0]
    return t


def largest_turn_under(m: int, upper: int) -> int:
    """Largest t>=0 with ancestor(m,t)<=upper, or -1."""
    if upper < ancestor(m, 0):
        return -1
    t = 0
    while ancestor(m, t+1) <= upper:
        t += 1
    return t


def represented_residue_count(m: int, upper: int, k: int) -> int:
    """Residue classes mod 3^k visited by one-step ancestors <=upper."""
    return min(3**k, largest_turn_under(m, upper) + 1)


def inverse_tree_counts(upper: int, depth: int):
    """Exact number of odd n<=upper reaching 1 within 1..depth odd steps.

    Seeds <=upper have all of their first 'depth' intermediates <=2^depth*upper.
    The enlarged bound prevents accidentally pruning paths that first rise.
    """
    bound = (1 << depth) * upper
    seen, new, counts = {1}, {1}, []
    for _ in range(depth):
        nxt = set()
        for m in new:
            if m % 3 == 0:
                continue
            t = 0
            while True:
                y = ancestor(m, t)
                if y > bound:
                    break
                if y not in seen:
                    nxt.add(y)
                t += 1
        seen.update(nxt)
        new = nxt
        counts.append(sum(n <= upper for n in seen))
    return counts


if __name__ == "__main__":
    print("Direct odd predecessors of stable 1:",
          [ancestor(1, t) for t in range(10)])
    print("Exact 3-adic turn lifts for target 1 and residue 7:")
    for k in range(1, 11):
        print(k, 3**k, phase_lift(1, 7, k))
    print("Actual seeds <=10^6 that reach 1 in <=1,...,5 odd steps:",
          inverse_tree_counts(10**6, 5))
