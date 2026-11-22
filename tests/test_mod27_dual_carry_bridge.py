import sys
import unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from mod27_dual_carry_bridge import (
    THRESHOLDS,odd_step,actual_block_hits,target_hit_count,
    phase_threshold,suffix9,suffix27,minimum_consecutive_hit_cost,
    consecutive_hit_contraction,target_frequency_haar,
    adjacent_joint_frequency_haar,positive_shadow,
    no_descent_pair_budget,greedy_disjoint_target_pairs,
)

class Mod27Tests(unittest.TestCase):
    def test_all_n_mod9_threshold_and_all_shortcut_hits(self):
        self.assertEqual(THRESHOLDS,(11,13,9,17,1,15,5,7,3))
        for n in range(1,100001,2):
            hits=actual_block_hits(n)
            self.assertEqual(len(hits),target_hit_count(n))
            if hits:
                self.assertEqual(hits[0][0],phase_threshold(n%9))

    def test_suffix_mod9_and_mod27(self):
        for n in range(1,20001,2):
            x=n; a=[]
            for j in range(10):
                x,b=odd_step(x); a.append(b)
                if j>=1:self.assertEqual(x%9,suffix9(a[-2],a[-1]))
                if j>=2:self.assertEqual(x%27,suffix27(a[-3],a[-2],a[-1]))

    def test_minimum_pair_cost_and_equality(self):
        minima={r:minimum_consecutive_hit_cost(r)[0] for r in range(9)}
        self.assertEqual(minima,{0:17,1:19,2:15,3:23,
                                 4:7,5:21,6:11,7:13,8:9})
        self.assertEqual(consecutive_hit_contraction(661),(6,1,31,47))
        for n in range(1,200001,2):
            datum=consecutive_hit_contraction(n)
            if datum:
                a,b,y,z=datum
                self.assertGreaterEqual(a+b,7)
                self.assertLess(z,n)
                self.assertLessEqual(128*z,9*n+67)

    def test_exact_haar_moments_do_not_claim_individual_mixing(self):
        distribution, probability=target_frequency_haar()
        self.assertEqual(distribution,{1:Fraction(11,63),3:Fraction(22,63),
                                       7:Fraction(2,63),9:Fraction(16,63),
                                       13:Fraction(8,63),15:Fraction(4,63)})
        self.assertEqual(probability,Fraction(1079,4096))
        self.assertEqual(adjacent_joint_frequency_haar(),
                         Fraction(59345,8388608))
        self.assertLess(adjacent_joint_frequency_haar(),probability**2)

    def test_arbitrarily_long_finite_growing_shadows_with_targets(self):
        for q in range(1,60):
            data=positive_shadow(q)
            self.assertEqual(data['hits'],q-1)
            self.assertEqual(data['dual_carry'],1)
            self.assertEqual(data['endpoint_mod_3power'],9**q-5)
            self.assertGreater(data['endpoint'],data['seed'])

    def test_global_budget_only_on_no_descent_prefixes(self):
        for n in range(1,1000,2):
            for k in range(2,35):
                end,pairs,dipped,bound=no_descent_pair_budget(n,k)
                if not dipped:
                    self.assertGreaterEqual(bound,1)
                    self.assertLessEqual(Fraction(end+1,n+1),bound)
        for q in range(2,20):
            n=(1<<(3*q+1))-5
            end,pairs,dipped,bound=no_descent_pair_budget(n,2*q)
            self.assertEqual((pairs,dipped),(0,False))
            self.assertEqual(end,2*9**q-5)

if __name__=='__main__':unittest.main()