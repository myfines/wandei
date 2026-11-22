"""Exact checks: inverse odd-Collatz ray, 3-adic phase and height sieve.

Run: python -m unittest discover -s tests -p 'test_inverse_phase_odometer.py' -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from inverse_phase_odometer import (
    odd_step, v2, v3, ancestor, turn_coordinates, ancestor_mod,
    phase_lift, largest_turn_under, represented_residue_count,
    inverse_tree_counts,
)


class InversePhaseTests(unittest.TestCase):
    def test_every_positive_odd_integer_has_a_unique_pair(self):
        for n in range(1, 10000, 2):
            m, t = turn_coordinates(n)
            self.assertEqual(ancestor(m, t), n)
            self.assertEqual(odd_step(n), m)
            self.assertNotEqual(m % 3, 0)

    def test_exact_ternary_phase_bijection_and_isometry(self):
        for m in (1, 5, 7, 11, 13, 17):
            for k in range(1, 7):
                modulus = 3**k
                residues = [ancestor_mod(m, t, k) for t in range(modulus)]
                self.assertEqual(set(residues), set(range(modulus)))
                for r in (0, 1, 2, 7, 17, 101, 2026):
                    t = phase_lift(m, r, k)
                    self.assertEqual(ancestor_mod(m, t, k), r % modulus)
            for t in range(1, 20):
                for u in range(t):
                    self.assertEqual(
                        v3(ancestor(m, t)-ancestor(m, u)), v3(t-u)
                    )

    def test_stable_target_and_power_of_four_phase_lock(self):
        self.assertEqual(
            [ancestor(1, t) for t in range(7)],
            [1, 5, 21, 85, 341, 1365, 5461],
        )
        for t in range(30):
            n = ancestor(1, t)
            self.assertEqual(odd_step(n), 1)
            self.assertEqual(v2(3*n + 1), 2*t + 2)
        for n in range(1, 10000, 2):
            x = 3*n + 1
            is_power_of_four = (x & (x-1)) == 0 and v2(x) % 2 == 0
            self.assertEqual(odd_step(n) == 1, is_power_of_four)

    def test_phase_digit_lifts(self):
        self.assertEqual(
            [phase_lift(1, 7, k) for k in range(1, 11)],
            [0, 6, 6, 60, 141, 384, 1842, 1842, 8403, 47769],
        )

    def test_height_restriction_vs_3adic_density(self):
        self.assertEqual(largest_turn_under(1, 10**6), 9)
        self.assertEqual(represented_residue_count(1, 10**6, 8), 10)
        for m in (1, 5, 7, 11):
            for upper in (10, 100, 10000):
                for k in (1, 2, 3, 4):
                    residues = {
                        ancestor(m, t) % 3**k
                        for t in range(largest_turn_under(m, upper) + 1)
                    }
                    self.assertEqual(
                        len(residues),
                        represented_residue_count(m, upper, k),
                    )

    def test_five_levels_of_inverse_tree(self):
        counts = inverse_tree_counts(10**6, 5)
        self.assertEqual(counts, [10, 44, 122, 298, 580])
        # Independently enumerate every odd seed and its first five odd steps.
        direct = [0]*5
        for n in range(1, 10**6 + 1, 2):
            x = n
            if x == 1:
                for j in range(5):
                    direct[j] += 1
                continue
            for j in range(5):
                x = odd_step(x)
                if x == 1:
                    for r in range(j, 5):
                        direct[r] += 1
                    break
        self.assertEqual(counts, direct)


if __name__ == "__main__":
    unittest.main()
