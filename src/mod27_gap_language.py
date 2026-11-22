#!/usr/bin/env python3
"""Exact mod-27 target-gap costs, complete finite hit language, CRT witnesses.

Odd-only Syracuse S(n)=(3n+1)/2**v2(3n+1). A hit refers to any
20 mod 27 state in the shortcut block AFTER an odd state.
All calculations are exact. No proof of the Collatz conjecture.
"""
from itertools import product

TAU = (11, 13, 9, 17, 1, 15, 5, 7, 3)


def odd_step(n):
    assert n > 0 and n & 1
    y = 3 * n + 1
    a = (y & -y).bit_length() - 1
    return y >> a, a


def target_hit(n):
    _, a = odd_step(n)
    return a >= TAU[n % 9]


def actual_shortcut_hit(n):
    """Independent, direct shortcut scan (also used by tests)."""
    y, a = odd_step(n)
    x = n
    found = False
    for _ in range(a):
        x = (3 * x + 1) // 2 if x & 1 else x // 2
        found |= x % 27 == 20
    assert x == y
    return found


def seed_for_word(word, residue9):
    """Least positive odd seed matching exponent word AND n % 9 = residue9.

    All seeds in the resulting class modulo 9*2**(A+1) work.
    """
    assert all(isinstance(a, int) and a >= 1 for a in word)
    A = C = 0
    for a in word:
        C = 3 * C + (1 << A)
        A += a
    modulus = 1 << (A + 1)
    r2 = (((1 << A) - C) * pow(pow(3, len(word), modulus), -1, modulus)) % modulus
    lift = ((residue9 - r2) * pow(modulus, -1, 9)) % 9
    n = r2 + modulus * lift
    assert n > 0 and n & 1 and n % 9 == residue9
    return n, 9 * modulus


def word_trace(seed, word):
    x = seed
    states = [x]
    hits = []
    for a in word:
        hits.append(target_hit(x))
        y, actual = odd_step(x)
        assert a == actual
        x = y
        states.append(x)
    return states, tuple(hits)


def finite_hit_word(bits):
    """Arbitrary finite 0/1 target word -> real positive trajectory.

    At residue 8 mod 9: a=1 gives a non-hit; a=7 gives one hit.
    Both exponents return the next odd state to residue 8 mod 9.
    """
    assert all(b in (0, 1) for b in bits)
    word = tuple(1 + 6 * b for b in bits)
    seed, modulus = seed_for_word(word, 8)
    states, hits = word_trace(seed, word)
    assert hits == tuple(bool(b) for b in bits)
    assert all(s % 9 == 8 for s in states)
    return seed, states[-1], modulus


def credited_hit_word(bits):
    """Embed any finite hit word after 10H nonhits with NO descent.

    H is the number of hit bits, and every positive odd state after the
    first move is STRICTLY above the original starting integer.
    """
    H = sum(bits)
    whole = (1,) * (10 * H) + tuple(1 + 6 * b for b in bits)
    seed, modulus = seed_for_word(whole, 8)
    states, hits = word_trace(seed, whole)
    assert hits == (False,) * (10 * H) + tuple(bool(b) for b in bits)
    assert all(x > seed for x in states[1:])
    return seed, states[-1], modulus


def gap_minimum(g):
    """Shortest 2-exponent sum for hit, g nonhits, hit.

    Exact dynamic program on 9 residue states. Each exponent modulo 6
    gives one residue transition; any higher same-class exponent costs
    at least 6 more. Checking up to tau[r]+5 is exhaustive.
    """
    assert g >= 0
    dp = {r: (0, (r,), ()) for r in range(9)}
    for target in (True,) + (False,) * g + (True,):
        following = {}
        for r, (cost, states, exps) in dp.items():
            for a in range(1, TAU[r] + 6):
                if (a >= TAU[r]) != target:
                    continue
                rr = ((3 * r + 1) * pow(2, -a, 9)) % 9
                candidate = (cost + a, states + (rr,), exps + (a,))
                if rr not in following or candidate[0] < following[rr][0]:
                    following[rr] = candidate
        dp = following
    return min(dp.values(), key=lambda v: v[0])


def fixed_gap_growth(g, repeats):
    """No-descent positive shadow of (1^g,2)^repeats with hit gap g."""
    assert g >= 1 and repeats >= 1
    word = ((1,) * g + (2,)) * repeats
    seed, modulus = seed_for_word(word, 4)
    states, hits = word_trace(seed, word)
    assert hits == tuple(j % (g + 1) == 0 for j in range(len(word)))
    assert all(y > seed for y in states[1:])
    return seed, states[-1], modulus


def no_hit_growth(length):
    """Closed-form positive shadow of the negative a=1 fixed point -1."""
    assert length >= 1
    seed = 9 * (1 << (length + 1)) - 1
    x = seed
    for j in range(length):
        assert x == 9 * 3**j * (1 << (length + 1 - j)) - 1
        assert x % 9 == 8 and not target_hit(x)
        y, a = odd_step(x)
        assert a == 1 and y > x
        x = y
    assert x == 18 * 3**length - 1
    return seed, x


def demonstrate():
    print('gap, least exponent cost, witness word, start / terminal mod9')
    for g in range(10):
        A, residues, exps = gap_minimum(g)
        assert A == (7 if g == 0 else g + 3)
        print(g, A, exps, residues[0], residues[-1])
    print('finite binary hit words:')
    for word in ('0000', '1111', '1010', '101101'):
        b = tuple(int(c) for c in word)
        print(word, finite_hit_word(b)[:2])
    print('fixed-gap growth (3 target hits):')
    for g in range(1, 6):
        print(g, fixed_gap_growth(g, 3)[:2])
    print('unbounded target-free growth:')
    for k in (5, 12, 30):
        print(k, no_hit_growth(k))
    for length in range(1, 13):
        for bits in product((0, 1), repeat=length):
            finite_hit_word(bits)
    print('PASS: all 8190 nonempty hit patterns through length 12')


if __name__ == '__main__':
    demonstrate()
