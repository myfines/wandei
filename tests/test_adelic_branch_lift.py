"""Integer-only tests for finite CRT witnesses in the adelic Collatz lift."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from adelic_branch_lift import (
    branch_residue, crt_branch_seed, image_limit_residue,
    verify_fiber_limit, double_padics_crt
)
from inverse_phase_odometer import odd_step, v2


class AdelicLiftTests(unittest.TestCase):
    def test_unique_branch_residue(self):
        for a in range(1,15):
            M=2**(a+1)
            r=branch_residue(a)
            self.assertEqual([x for x in range(1,M,2) if v2(3*x+1)==a],[r])

    def test_crt_witnesses_for_every_anchor(self):
        for anchor in (1,3,5,7,11,19,101):
            for a in range(1,8):
                for k in range(1,12):
                    n,y,predicted=verify_fiber_limit(anchor,a,k)
                    self.assertGreater(n,anchor)
                    self.assertEqual((n-anchor)%(3**k),0)
                    self.assertEqual(v2(3*n+1),a)
                    self.assertEqual(y%(3**k),predicted)

    def test_incompatible_limits_at_fixed_point(self):
        for k in range(1,12):
            n1=crt_branch_seed(1,1,k)
            n2=crt_branch_seed(1,2,k)
            self.assertEqual((n1-1)%(3**k),0)
            self.assertEqual((n2-1)%(3**k),0)
            self.assertEqual(odd_step(n1)%(3**k),2%(3**k))
            self.assertEqual(odd_step(n2)%(3**k),1%(3**k))

    def test_positive_odd_diagonal_is_dense(self):
        for k2 in range(1,7):
            for k3 in range(1,6):
                for r2 in range(1,2**k2,2):
                    for r3 in range(3**k3):
                        n=double_padics_crt(r2,r3,k2,k3)
                        self.assertEqual(n%(2**k2),r2)
                        self.assertEqual(n%(3**k3),r3)

    def test_branch_limits_distinct_at_all_odd_anchors(self):
        for n in (1,3,5,7,11,19,101):
            self.assertNotEqual(image_limit_residue(n,1,1),
                                image_limit_residue(n,2,1))


if __name__=='__main__':
    unittest.main()
