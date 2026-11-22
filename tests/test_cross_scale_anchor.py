"""Independent finite regression tests for the cross-scale Collatz conjecture research.

Run: python -m unittest discover -s tests -p 'test_cross_scale_anchor.py' -v
"""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from cross_scale_anchor import (
    anchor_shadow_seed, anchor_shadow_at, first_departure_certificate,
    min_turn_for_height, phase_height_certificate, adelic_pair_certificate
)
from inverse_phase_odometer import (
    ancestor, odd_step, first_exponent, v2, phase_lift
)


class CrossScaleAnchorTests(unittest.TestCase):
    def test_forced_anchor_shadow_and_departure(self):
        for k in range(1, 30):
            for q in (1,3,5,11):
                n, end, dep = first_departure_certificate(k,q)
                self.assertEqual(n,anchor_shadow_seed(k,q))
                self.assertEqual(end, 1+2*q*3**k)
                self.assertEqual(dep,1)
                self.assertEqual(odd_step(end), (3*end+1)//2)

    def test_adelic_pair_conservation(self):
        for k in range(1,30):
            for q in (1,3,5):
                c = adelic_pair_certificate(1,anchor_shadow_seed(k,q),k)
                self.assertEqual(c['A'],2*k)
                self.assertEqual(c['real_ratio'],(3**k,4**k))
                self.assertEqual(c['two_adic_ratio'],4**k)
                self.assertEqual(c['three_adic_ratio'],(1,3**k))

    def test_phase_height_non_direct(self):
        for m in (1,5,7,11,13,17):
            for n in (1,3,7,11,17,21,37,53,91):
                for k in range(1,17):
                    t,lower,direct = phase_height_certificate(m,n,k)
                    self.assertEqual(direct,odd_step(n)==m)
                    self.assertEqual(t,phase_lift(m,n,k))
                    if not direct and 3**k > n:
                        self.assertGreaterEqual(t,lower)

    def test_direct_lifts_stabilize(self):
        for m in (1,5,11):
            for index in range(18):
                n=ancestor(m,index)
                for k in range(1,9):
                    t, lower, direct = phase_height_certificate(m,n,k)
                    self.assertTrue(direct)
                    self.assertEqual(t,index%(3**k))

    def test_shadows_not_direct_predecessors_of_one(self):
        for k in range(1,30):
            n=anchor_shadow_seed(k)
            self.assertNotEqual(odd_step(n),1)
            self.assertEqual(n%8,1)
            for index in range(1,10):
                self.assertEqual(ancestor(1,index)%8,5)

    def test_shadow_exponent_pattern(self):
        for k in range(1,23):
            for j in range(k):
                self.assertEqual(v2(3*anchor_shadow_at(k,j)+1),2)
            self.assertEqual(v2(3*anchor_shadow_at(k,k)+1),1)


if __name__ == '__main__':
    unittest.main()
