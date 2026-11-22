import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from collatz_claim_graph_audit import (
    TAU,STATES,EDGES,step,direct_shortcut_hit,positive_seed,
    audit,exact_frontier,check_potential
)

class ClaimGraphAudit(unittest.TestCase):
    def test_complete_representative_graph(self):
        self.assertEqual(len(STATES),15)
        self.assertEqual(len(EDGES),204)
        for u,v,a,h,p in EDGES:
            r,prev=STATES[u]
            self.assertEqual(h,int(a>=TAU[r]))
            self.assertEqual(p,h*prev)
            self.assertEqual(STATES[v],((3*r+1)*pow(2,-a,9)%9,h))

    def test_exact_two_parameter_frontier(self):
        for lam in range(4):
            for mu in range(9):
                x=audit(lam,mu)
                feasible=x['status']=='certified_graph_potential'
                self.assertEqual(feasible,exact_frontier(lam,mu))
                if feasible:
                    self.assertTrue(check_potential(x['potential'],lam,mu))
                else:
                    self.assertLess(x['cycle_weight'],0)

    def test_one_specific_negative_cycle_has_real_integer_witness(self):
        x=audit(1,5,repeats=8)
        self.assertEqual(x['cycle_weight'],-1)
        self.assertEqual(x['cycle_start'],(4,1))
        self.assertEqual(x['cycle_exponents'],[6])
        witness=x['positive_finite_witness']
        self.assertEqual(witness['hit_bits'],[1]*8)
        n=int(witness['seed'])
        for _ in range(8):
            self.assertTrue(direct_shortcut_hit(n))
            n,a=step(n)
            self.assertEqual(a,6)
        self.assertEqual(str(n),witness['end'])

    def test_independent_direct_shortcut_target(self):
        for n in range(1,20000,2):
            _,a=step(n)
            self.assertEqual(direct_shortcut_hit(n),a>=TAU[n%9])
        self.assertTrue(direct_shortcut_hit(31))
        self.assertEqual(step(31),(47,1))

    def test_arbitrary_exact_prefix_crt(self):
        for w in ((1,2)*8,(6,)*12,(7,1,2,7),(1,)*30):
            for r in (0,4,8):
                n,mod,end=positive_seed(list(w),r)
                self.assertEqual(n%9,r)
                x=n
                for a in w:
                    x,b=step(x)
                    self.assertEqual(a,b)
                self.assertEqual(x,end)
                self.assertEqual((n+mod)%9,r)

if __name__=='__main__':unittest.main()
