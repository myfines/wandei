"""Independent exact arithmetic tests for bidirectional Collatz carries."""
import sys
import unittest
from pathlib import Path
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from dual_carry_arithmetic import (
    cylinder,extend_slow,extend_fast,syracuse,critical_rotation_word,log_lock_depth
)


def backward(word,y):
    for a in reversed(word):
        numerator=(1<<a)*y-1
        assert numerator%3==0
        y=numerator//3
        assert y>0 and y%2
    return y


class DualCarryTests(unittest.TestCase):
    def test_exhaustive_small_words_and_independent_reverse_decode(self):
        for length in range(6):
            for word in product(range(1,5),repeat=length):
                d=cylinder(word)
                self.assertEqual(d.overlap,1-d.endpoint_residue%2)
                self.assertLess(d.endpoint,2*3**length)
                self.assertEqual(backward(word,d.endpoint),d.seed)
                x=d.seed
                for a in word:
                    x,b=syracuse(x)
                    self.assertEqual(a,b)
                self.assertEqual(x,d.endpoint)

    def test_two_independent_carry_algorithms(self):
        for length in range(5):
            for word in product(range(1,5),repeat=length):
                d=cylinder(word)
                for a in (1,2,3,4,5,7):
                    nxt,u,v=extend_slow(d,a)
                    self.assertEqual((nxt,u,v),extend_fast(d,a))
                    self.assertEqual((1<<a)*nxt.overlap+v,d.overlap+2*u)

    def test_all_real_seeds_lock(self):
        for n in range(1,1500,2):
            d=cylinder(())
            x=n
            K=log_lock_depth(n)
            for k in range(1,K+6):
                x,a=syracuse(x)
                d,u,v=extend_fast(d,a)
                if k>=K:
                    self.assertEqual((d.seed,d.endpoint_residue,d.overlap),(n,x,0))
                if k>K:
                    self.assertEqual((u,v),(0,0))

    def test_mechanical_rotation_uses_exact_integer_floors(self):
        d=cylinder(())
        ca=cv=0
        for j,a in enumerate(critical_rotation_word(1500),1):
            d,u,v=extend_fast(d,a)
            self.assertEqual(d.A,(3**j).bit_length()-1)
            ca+=(u!=0);cv+=(v!=0)
        self.assertGreater(d.seed.bit_length(),1400)
        self.assertGreater(ca,900)
        self.assertGreater(cv,900)

    def test_explicit_small_cases(self):
        self.assertEqual((cylinder((1,)).seed,cylinder((1,)).endpoint),(3,5))
        self.assertEqual((cylinder((2,)).seed,cylinder((2,)).endpoint),(1,1))
        self.assertEqual((cylinder((1,1,1)).seed,cylinder((1,1,1)).endpoint),(15,53))


if __name__=="__main__":
    unittest.main()
