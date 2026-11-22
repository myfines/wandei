"""Exact, independent edge and actual-orbit tests of one-bit charge potential."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from mod27_phase_charge import (
    TAU,bit_phi,edge_charge,odd_step,orbital_charge,no_descent_density_ceiling
)
from mod27_gap_language import seed_for_word


class ChargeTests(unittest.TestCase):
    def test_every_mod9_edge_and_threshold(self):
        for r in range(9):
            for a in range(1,601):
                rp,h,slack=edge_charge(r,a)
                self.assertEqual(rp,(3*r+1)*pow(2,-a,9)%9)
                self.assertEqual(h,int(a>=TAU[r]))
                self.assertEqual(slack,(a-1-h)-(bit_phi(rp)-bit_phi(r)))
                self.assertGreaterEqual(slack,0)

    def test_10000_integer_orbits(self):
        for seed in range(1,20001,2):
            d=orbital_charge(seed,50)
            self.assertGreaterEqual(d['A'],d['k']+d['H']-1)
            self.assertEqual(
                d['A']-d['k']-d['H'],
                d['phi_end']-d['phi_start']+d['slack']
            )

    def test_sharp_loss_one_at_any_odd_horizon(self):
        for q in range(0,50):
            word=(1,2)*q+(1,)
            seed,_=seed_for_word(word,4)
            d=orbital_charge(seed,len(word))
            self.assertEqual(d['A'],d['k']+d['H']-1)
            self.assertEqual(d['slack'],0)

    def test_exact_saturation_over_repeating_pair(self):
        for q in range(1,50):
            word=(1,2)*q
            seed,_=seed_for_word(word,4)
            d=orbital_charge(seed,len(word))
            self.assertEqual(d['A'],d['k']+d['H'])
            self.assertEqual(d['slack'],0)

    def test_no_descent_ceiling_on_real_prefixes(self):
        for seed in range(1,500,2):
            for k in (2,4,8,16,40):
                b=no_descent_density_ceiling(seed,k)
                if b is not None:
                    self.assertLessEqual(orbital_charge(seed,k)['H']/k,b+1e-12)


if __name__=='__main__':
    unittest.main()
