"""Exact independent regression tests for the periodic-phase research module."""
import sys
import unittest
from itertools import product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from phase_switch_budget import (
    template, syracuse, v2, minimum_seed, direct_matches,
    common_phase_budget, common_prefix_divergence,
    sync_transition, recharged_seed,
)

class PhaseBudgetTests(unittest.TestCase):
    def test_every_finite_script_matches_exact_modulus(self):
        for length in range(1,5):
            for word in product(range(1,5),repeat=length):
                w=template(word)
                for q in range(1,4):
                    n=minimum_seed(w,q)
                    self.assertTrue(w.matching(n,q))
                    self.assertTrue(direct_matches(n,w,q))
                    self.assertTrue(direct_matches(n+(1<<(q*w.A+1)),w,q))
                    if q*w.A <= 8:
                        for x in range(1,min(250,1<<(q*w.A+2)),2):
                            self.assertEqual(w.matching(x,q),direct_matches(x,w,q))
    def test_direct_iteration_vs_repetition_budget(self):
        for word in [(1,),(2,),(1,2),(2,1),(3,1),(2,3),(1,1,2),(4,2,1)]:
            w=template(word)
            for x in range(1,300,2):
                for q in range(1,5):
                    self.assertEqual(w.matching(x,q),direct_matches(x,w,q))
    def test_periodic_fixed_points_are_correct_in_Z2(self):
        for length in range(1,5):
            for word in product(range(1,6),repeat=length):
                w=template(word)
                x=w.fixed_point
                for a in word:
                    y=3*x+1
                    self.assertEqual(v2(y.numerator),a)
                    x=y/(1<<a)
                self.assertEqual(x,w.fixed_point)
    def test_holonomy_is_only_common_symbolic_prefix(self):
        words=[template(w) for length in range(1,4)
               for w in product(range(1,5),repeat=length)]
        for w in words:
            for z in words:
                self.assertEqual(common_phase_budget(w,z),
                                 common_prefix_divergence(w,z))
    def test_exact_switching_identity(self):
        words=[template(x) for x in [(1,),(2,),(1,2),(2,1),(3,1),(2,3)]]
        for w in words:
            for z in words:
                for q in (1,2,3):
                    n=minimum_seed(z,q)
                    sync_transition(w,z,n)
    def test_arbitrarily_large_recharge_witnesses(self):
        for h in range(2,80):
            n,x,achieved=recharged_seed(h)
            self.assertEqual(v2(n-1),1)
            self.assertGreaterEqual(achieved,h)
            self.assertEqual(syracuse(n)[1],1)
    def test_sharp_expanding_shadow_family(self):
        w=template((1,2))
        self.assertEqual(str(w.fixed_point),'-5')
        for q in range(1,50):
            n=minimum_seed(w,q)
            self.assertEqual(n,2**(3*q+1)-5)
            self.assertEqual(w.repeats(n),q)
            x=n
            for _ in range(2*q): x,_=syracuse(x)
            self.assertEqual(x,2*9**q-5)
            self.assertEqual(syracuse(x)[1],3)

if __name__=='__main__':
    unittest.main()
