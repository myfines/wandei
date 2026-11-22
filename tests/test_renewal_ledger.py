"""Exact standard-library tests for mixed Collatz renewal height ledger."""
import sys,unittest
from fractions import Fraction
from itertools import product
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from renewal_ledger import (WEIGHTS,one_renewal,verify_weight,ledger,cylinder,
                            word_endpoint,pair_family,find_first_local_not_global)

class LedgerTests(unittest.TestCase):
    def test_universal_sharp_weights(self):
        best={}
        for n in range(3,300001,2):
            typ,y,r=verify_weight(n)
            best[typ]=max(best.get(typ,Fraction(0)),r)
        self.assertEqual(best,WEIGHTS)
    def test_ledger_never_false_certifies(self):
        for n in range(3,3001,2):
            path=ledger(n,max_gate_steps=500)
            for typ,x,y,upper in path:
                self.assertLessEqual(Fraction(y+1,x+1),WEIGHTS[typ])
                if upper<1:self.assertLess(y,n)
    def test_every_three_symbol_finite_word_is_realizable(self):
        for depth in range(0,7):
            for word in product('135',repeat=depth):
                w=''.join(word)
                r,bits,y,A,p=cylinder(w)
                self.assertEqual(word_endpoint(r,w),y)
                self.assertEqual(word_endpoint(r+(1<<bits),w),y+4*3**p)
                self.assertEqual(bits,A+2)
    def test_half_good_pairs_can_expand_arbitrarily_long(self):
        for q in range(1,13):
            r,bits,y=pair_family(q)
            self.assertGreater(y,r)
            self.assertEqual(bits,6*q+2)
            self.assertEqual(word_endpoint(r,'15'*q),y)
    def test_local_descent_does_not_mean_global_descent(self):
        self.assertEqual(find_first_local_not_global(),(27,5,'G_odd',107,91))
    def test_27_prefix(self):
        trace=ledger(27)
        self.assertEqual([(typ,x,y) for typ,x,y,_ in trace[:5]],
                         [('B3',27,31),('B1',31,47),('B1',47,71),
                          ('B1',71,107),('G_odd',107,91)])
        self.assertGreater(trace[4][2],27)

if __name__=='__main__':unittest.main()
