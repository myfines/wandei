"""Integer-only independent regression for finite target gap/language theorems."""
import sys
import unittest
from pathlib import Path
from itertools import product
from fractions import Fraction
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from mod27_gap_language import (
    TAU, odd_step, target_hit, actual_shortcut_hit, word_trace,
    seed_for_word, finite_hit_word, credited_hit_word,
    gap_minimum, fixed_gap_growth, no_hit_growth,
)


class TargetGapLanguageTests(unittest.TestCase):
    def test_bit_language_exhaustive(self):
        for length in range(1, 13):
            for bits in product((0, 1), repeat=length):
                seed, last, mod = finite_hit_word(bits)
                self.assertGreater(seed, 0)
                self.assertEqual(seed % 9, 8)

    def test_actual_shortcut_target_matches_indicator(self):
        for n in range(1, 25000, 2):
            self.assertEqual(target_hit(n), actual_shortcut_hit(n))
        for bits in product((0, 1), repeat=7):
            word = [1 + 6*b for b in bits]
            seed, _ = seed_for_word(word, 8)
            x = seed
            for b in bits:
                self.assertEqual(actual_shortcut_hit(x), bool(b))
                x, _ = odd_step(x)

    def test_exact_gap_cost_and_minimizing_witness(self):
        for g in range(0, 151):
            A, rs, ws = gap_minimum(g)
            self.assertEqual(A, 7 if g == 0 else g + 3)
            self.assertEqual(len(ws), g + 2)
            seed, _ = seed_for_word(ws, rs[0])
            _, hits = word_trace(seed, ws)
            self.assertEqual(hits, (True,) + (False,)*g + (True,))
            if g >= 1:
                self.assertEqual(ws, (1,)*g + (2, 1))
                self.assertEqual(rs[0], 4)

    def test_gap_zero_per_residue(self):
        minima = []
        for r in range(9):
            best = 10**9
            for a in range(TAU[r], TAU[r]+6):
                y = ((3*r+1)*pow(2, -a, 9)) % 9
                best = min(best, a + TAU[y])
            minima.append(best)
        self.assertEqual(minima, [17,19,15,23,7,21,11,13,9])

    def test_arbitrary_finite_word_with_positive_height_credit(self):
        for L in range(1, 10):
            for bits in product((0, 1), repeat=L):
                seed, final, mod = credited_hit_word(bits)
                self.assertGreater(final, seed)
                self.assertEqual(seed % 9, 8)
        self.assertGreater(Fraction(3,2)**10 * Fraction(3,128), 1)

    def test_fixed_gap_expanding_shadows(self):
        for g in range(1, 19):
            C = 3**(g+1) - 2**(g+1)
            D = 2**(g+2) - 3**(g+1)
            self.assertLess(D, 0)
            for q in range(1, 16):
                seed, final, mod = fixed_gap_growth(g, q)
                self.assertGreater(final, seed)
                self.assertEqual(seed % 9, 4)
                self.assertEqual(mod, 9*2**(q*(g+2)+1))
                x = seed
                for _ in range(q):
                    self.assertEqual((3**(g+1)*x+C) % 2**(g+2), 0)
                    x = (3**(g+1)*x+C)//2**(g+2)
                self.assertEqual(x, final)

    def test_target_free_ever_longer_prefixes(self):
        for length in range(1, 101):
            n, final = no_hit_growth(length)
            self.assertEqual(n, 9*2**(length+1)-1)
            self.assertEqual(final, 18*3**length-1)
            self.assertGreater(final, n)

    def test_crt_class_preserves_pattern(self):
        words = ((1,2,1,7), (1,7,7,1,1), (1,1,2), (7,7,7))
        for word in words:
            seed, mod = seed_for_word(word, 8)
            states, hits = word_trace(seed, word)
            for delta in (1,2,7):
                lifted = seed + delta*mod
                states2, hits2 = word_trace(lifted, word)
                self.assertEqual(hits2, hits)
                self.assertEqual(
                    states2[-1]-states[-1],
                    delta*mod*3**len(word)//2**sum(word)
                )


if __name__ == '__main__':
    unittest.main()
