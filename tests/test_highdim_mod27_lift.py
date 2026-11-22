"""Independent regressions for the exact high-dimensional Collatz phase lift.

Run: python -m unittest discover -s tests -p test_highdim_mod27_lift.py -v
"""
import sys
import unittest
from itertools import product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))

from highdim_mod27_lift import (
 TAU,STATES,PSI,edge,verify_all_edges,step,Lift,lift_orbit,
 positive_seed,explicit_minimum_script
)
from mod27_tropical_transfer import (
 MATRIX,exact_min_cost,explicit_cost,canonical_word,partition_at
)

def direct_shortcut_hit(n):
    x=n
    y,a=step(n)
    hit=0
    for _ in range(a):
        x=(3*x+1)//2 if x%2 else x//2
        hit|=int(x%27==20)
    assert x==y
    return hit

class HighDimMod27Tests(unittest.TestCase):
    def test_204_finite_edge_certificate_and_all_exponents_through_500(self):
        self.assertEqual(verify_all_edges(),204)
        self.assertEqual(len(STATES),15)
        for st in STATES:
            for a in range(1,501):
                nxt,h,p,slack=edge(st,a)
                self.assertGreaterEqual(slack,0)
                self.assertEqual(h,int(a>=TAU[st[0]]))
                self.assertEqual(p,st[1]*h)

    def test_real_orbit_height_charge_and_independent_shortcut(self):
        for seed in range(1,10001,2):
            z=Lift.start(seed)
            prev=0
            origin=PSI[(seed%9,0)]
            for k in range(1,41):
                h=direct_shortcut_hit(z.n)
                st0=z.n%9
                a,h1,p,slack=z.advance()
                self.assertEqual(h,h1)
                self.assertEqual(p,prev*h)
                self.assertEqual(z.r,z.n%9)
                self.assertGreaterEqual(slack,0)
                self.assertEqual(
                   z.A-k-z.H-4*z.P,
                   PSI[(z.r,z.previous_hit)]-origin+z.sigma)
                self.assertGreaterEqual(z.A,k+z.H+4*z.P-1)
                prev=h

    def test_sharp_constant_and_sharp_pair_price(self):
        z=lift_orbit(31,1)
        self.assertEqual((z.A,z.k,z.H,z.P),(1,1,1,0))
        for k in (1,2,3,5,10,25,60):
            seed=positive_seed((6,)*k,4)
            z=lift_orbit(seed,k)
            self.assertEqual((z.A,z.H,z.P),(6*k,k,k-1))
            self.assertEqual(z.A-z.k-z.H-4*z.P,4)
            if k>=25:
                self.assertLess(z.A-z.k-z.H-5*z.P,0)

    def test_every_hit_word_exact_tropical_cost(self):
        total=0
        for k in range(1,13):
            for bits in product((0,1),repeat=k):
                A,r,word,end=exact_min_cost(bits)
                A2,initial,explicit,end2=explicit_minimum_script(bits)
                self.assertEqual(A,explicit_cost(bits))
                self.assertEqual(A,A2)
                self.assertEqual(sum(explicit),A)
                self.assertEqual((explicit,initial),canonical_word(bits))
                seed=positive_seed(explicit,initial)
                z=Lift.start(seed)
                actual=[]
                for a in explicit:
                    actual.append(direct_shortcut_hit(z.n))
                    observed=z.advance()[0]
                    self.assertEqual(observed,a)
                self.assertEqual(tuple(actual),bits)
                total+=1
        self.assertEqual(total,8190)

    def test_simple_phase_nilpotence(self):
        self.assertEqual(partition_at(1,-1),-2)
        for k in range(2,15):
            self.assertEqual(partition_at(k,-1),0)
        self.assertEqual(partition_at(2,1),4)
        self.assertEqual(partition_at(5,1),32)

    def test_expanding_2adic_ghost_does_not_prove_integer_escape(self):
        for k in range(1,35):
            seed=positive_seed((1,2)*k,4)
            z=lift_orbit(seed,2*k)
            self.assertEqual((z.A,z.H,z.P,z.sigma),(3*k,k,0,0))
            self.assertGreater(z.n,seed)
            self.assertEqual((z.n+5)*8**k,(seed+5)*9**k)

if __name__=="__main__":
    unittest.main()
