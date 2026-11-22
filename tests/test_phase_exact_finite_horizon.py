"""Regression tests for finite-horizon Collatz parity cylinders.

Run: python -m unittest discover -s tests -p 'test_phase_exact_finite_horizon.py'
"""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from phase_exact_finite_horizon import (
    brute_avoidance, coefficient_boundary_statistics,
    count_progression, exact_avoidance_by_cylinders,
    safe_seed_threshold, step, word_data,
)


class TestFiniteHorizonCylinder(unittest.TestCase):
    def test_residue_bijection_and_parity_words(self):
        from itertools import product
        for k in range(1, 9):
            residues = []
            for bits in product((0, 1), repeat=k):
                r, cap = word_data(bits)
                residues.append(r)
                x = r or (1 << k)
                for b in bits:
                    self.assertEqual(x % 2, b)
                    x = step(x)
            self.assertEqual(sorted(residues), list(range(1 << k)))

    def test_exact_cylinders_match_direct_orbits(self):
        for k in range(1, 11):
            for lo, hi in ((1, 1 << k), (10, 10 + (1 << k)),
                           (123, 123 + (1 << k))):
                self.assertEqual(exact_avoidance_by_cylinders(k, lo, hi),
                                 brute_avoidance(k, lo, hi))

    def test_sufficiently_large_blocks(self):
        for k in range(1, 13):
            n = safe_seed_threshold(k)
            m = 1 << k
            count, signed, anomalies = exact_avoidance_by_cylinders(k, n, n+m-1)
            self.assertEqual((count, signed), coefficient_boundary_statistics(k))
            self.assertEqual(anomalies, 0)

    def test_small_seed_exceptions_are_finite_observations_only(self):
        # Do not extrapolate to all horizons: Terras CST conjecture is OPEN.
        for k in range(2, 13):
            m = 1 << k
            count, signed, anomalies = exact_avoidance_by_cylinders(k, 1, m)
            co_count, co_signed = coefficient_boundary_statistics(k)
            self.assertEqual((count, anomalies), (co_count + 1, 1))
            self.assertEqual(signed-co_signed, (-1)**((k+1)//2))

    def test_progressions_and_zero_residue(self):
        self.assertEqual(count_progression(0, 8, 1, 16), 2)
        self.assertEqual(count_progression(3, 8, 4, 20), 2)
        self.assertEqual(count_progression(3, 8, 1, 2), 0)


if __name__ == "__main__":
    unittest.main()
