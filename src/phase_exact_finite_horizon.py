#!/usr/bin/env python3
"""Exact finite-horizon cylinders, additive remainders, and Euler phase.

Standard library only; not a proof of the Collatz conjecture.
Uses the shortcut map T(n)=n//2 if even, (3*n+1)//2 if odd.
"""
from itertools import product
from collections import defaultdict


def step(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2


def word_data(bits):
    """Unique n mod 2**k and true no-first-descent cap for a parity word.

    cap=None denotes unlimited n; otherwise 0<n<=cap is required.
    This is a necessary AND sufficient condition for seeds of this residue.
    """
    k = len(bits)
    assert k >= 1 and all(b in (0, 1) for b in bits)
    s = 0
    c = 0
    cap = None
    for j, b in enumerate(bits, 1):
        s += b
        c = (3 if b else 1) * c + (1 << (j - 1)) * b
        gap = (1 << j) - 3**s
        if gap > 0:
            local_cap = c // gap
            cap = local_cap if cap is None else min(cap, local_cap)
    modulus = 1 << k
    residue = (-c * pow(3**s, -1, modulus)) % modulus
    return residue, cap


def first_seed_at_least(residue: int, modulus: int, lower: int) -> int:
    """First positive seed >=lower in the given congruence class."""
    assert modulus > 0 and 0 <= residue < modulus
    lower = max(1, lower)
    return lower + ((residue - lower) % modulus)


def count_progression(residue: int, modulus: int, lower: int, upper: int) -> int:
    if upper < lower:
        return 0
    first = first_seed_at_least(residue, modulus, lower)
    return 0 if first > upper else 1 + (upper - first) // modulus


def exact_avoidance_by_cylinders(k: int, lo: int, hi: int):
    """(count, signed phase count, finite-cap anomalies) in [lo, hi].

    Exact O(k*2**k) integer enumeration of cylinders, not direct orbits.
    """
    modulus = 1 << k
    total = signed = anomalies = 0
    for bits in product((0, 1), repeat=k):
        residue, cap = word_data(bits)
        end = hi if cap is None else min(hi, cap)
        count = count_progression(residue, modulus, lo, end)
        total += count
        signed += count * (-1 if sum(bits) % 2 else 1)
        if cap is not None:
            anomalies += count
    return total, signed, anomalies


def brute_avoidance(k: int, lo: int, hi: int):
    """Independent direct-orbit check (count, phase, anomalies)."""
    total = signed = anomalies = 0
    for n in range(max(1, lo), hi + 1):
        x = n
        prod3 = 1
        prod2 = 1
        odd_count = 0
        coefficient_alive = True
        actual_alive = True
        for _ in range(k):
            b = x & 1
            odd_count += b
            prod2 *= 2
            prod3 *= (3 if b else 1)
            x = step(x)
            if prod3 < prod2:
                coefficient_alive = False
            if x < n:
                actual_alive = False
        if actual_alive:
            total += 1
            signed += (-1 if odd_count % 2 else 1)
            if not coefficient_alive:
                anomalies += 1
    return total, signed, anomalies


def coefficient_boundary_statistics(k: int):
    """Count and (-1)^S-signed count of coefficient-surviving words."""
    counts = {0: 1}
    for j in range(1, k + 1):
        new = defaultdict(int)
        for s, v in counts.items():
            if 3**s > 2**j:
                new[s] += v
            if 3**(s + 1) > 2**j:
                new[s + 1] += v
        counts = new
    return sum(counts.values()), sum(((-1)**s) * v for s, v in counts.items())


def safe_seed_threshold(k: int) -> int:
    """Sufficient but non-sharp finite-horizon coefficient/actual equivalence."""
    assert k >= 1
    return 3**k - 2**k + 1


def run_checks(max_k: int = 12):
    assert max_k >= 1
    for k in range(1, max_k + 1):
        m = 1 << k
        data = [word_data(bits) for bits in product((0, 1), repeat=k)]
        assert sorted(r for r, _ in data) == list(range(m))
        for lo, hi in ((1, m), (m//3 + 1, m//3 + m + 5)):
            assert exact_avoidance_by_cylinders(k, lo, hi) == brute_avoidance(k, lo, hi)
        threshold = safe_seed_threshold(k)
        expected_cnt, expected_phase = coefficient_boundary_statistics(k)
        observed = exact_avoidance_by_cylinders(k, threshold, threshold + m - 1)
        assert observed == (expected_cnt, expected_phase, 0), (k, observed)
        if k <= 10:
            assert observed == brute_avoidance(k, threshold, threshold + m - 1)
        small = exact_avoidance_by_cylinders(k, 1, m)
        print(f"k={k:2d} coeff={expected_cnt:5d} phase={expected_phase:5d} "
              f"[1,2^k] actual={small} large-block={observed}")
    print("PASS: residues, correction caps, large-block phase and direct checks")


if __name__ == "__main__":
    run_checks()
