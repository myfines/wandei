"""Independent exact moments and finite residue-audit regression tests."""
import sys,unittest
from fractions import Fraction
from math import log2
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from renewal_moments import exact_moment,theoretical_exponents,finite_block_audit

class MomentsTests(unittest.TestCase):
    def test_exact_moments(self):
        self.assertEqual(exact_moment(0),1)
        self.assertEqual(exact_moment(1),Fraction(27,26))
        self.assertEqual(exact_moment(2),Fraction(2097,1540))
        self.assertEqual(theoretical_exponents(),(Fraction(5,3),Fraction(3,1)))
        self.assertLess((5/3)*log2(3)-3,0)
    def test_finite_residue_block_audit(self):
        p,A,M,freq=finite_block_audit(2**15)
        self.assertLess(abs(float(p)-5/3),0.002)
        self.assertLess(abs(float(A)-3),0.002)
        self.assertLess(abs(float(M)-27/26),0.002)
        self.assertEqual(sum(freq.values()),2**15)
        self.assertEqual(freq[1],2**14)
        self.assertEqual(freq[2],2**13)

if __name__=='__main__':unittest.main()
