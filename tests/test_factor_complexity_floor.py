import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from factor_complexity_floor import guaranteed_distinct_starts,brute_check,syracuse

class FactorComplexityFloorTests(unittest.TestCase):
    def test_integer_bound_is_maximal(self):
        for seed in (1,3,27,97,6171,2**80-1):
            for L in range(1,160):
                count=guaranteed_distinct_starts(seed,L)
                if count:
                    K=count-1
                    self.assertLessEqual((seed+1)*3**K,2**(L+K+1))
                    self.assertGreater((seed+1)*3**(K+1),2**(L+K+2))
                else:
                    self.assertGreater(seed+1,2**(L+1))
    def test_distinct_prefix_words(self):
        for seed in (3,7,9,27,97,871,6171,2**80-1):
            for L in (8,16,32,64,96,128):
                count,distinct,words=brute_check(seed,L)
                if distinct: self.assertTrue(words)
    def test_simple_orbit(self):
        self.assertEqual(syracuse(7),(11,1))
        self.assertEqual(syracuse(11),(17,1))
        self.assertEqual(syracuse(17),(13,2))

if __name__=='__main__':
    unittest.main()
