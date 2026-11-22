"""Exact standard-library regression checks for the Collatz two-gate model."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from renewal_gate_fractal import S,gate,survive_word,cylinders,dimension,min_seed_per_depth
from renewal_interval_frontier import scan

class RenewalTests(unittest.TestCase):
    def test_all_gate_cases(self):
        kinds=set()
        for n in range(3,100000,4):
            kind,end,steps,e=gate(n)
            kinds.add(kind)
            x=n
            for _ in range(steps): x=S(x)
            self.assertEqual(x,end)
            if kind in ('B1','B3'):
                self.assertGreater(end,n)
                self.assertEqual(end%4,3)
                self.assertIn(e,(1,3))
                self.assertEqual(kind,'B1' if n%8==7 else 'B3')
            else:
                self.assertLess(end,n)
                self.assertNotIn(e,(1,3))
        self.assertEqual(kinds,{'B1','B3','G_odd','G_even'})

    def test_exact_cylinder_prefixes(self):
        for depth in range(7):
            for residue,bits,A,p,endpoint,word in cylinders(depth):
                self.assertEqual(bits,A+2)
                self.assertEqual(residue%4,3)
                self.assertLess(residue,2**bits)
                target=tuple('B'+x for x in word)
                for j in range(3):
                    n=residue+j*2**bits
                    self.assertEqual(survive_word(n,depth),target)
                    x=n
                    for _ in range(depth):
                        _,x,_,_=gate(x)
                    self.assertEqual(x,endpoint+4*(3**p)*j)

    def test_exact_haar_count(self):
        for depth in range(5):
            M=2+3*depth
            modulus=2**M
            allowed=set()
            for residue,bits,*_ in cylinders(depth):
                allowed.update(range(residue,modulus,2**bits))
            brute={n for n in range(3,modulus,4)
                   if len(survive_word(n,depth))==depth}
            self.assertEqual(allowed,brute)
            self.assertEqual(len(allowed),5**depth)

    def test_finite_minimum_seed_frontier(self):
        rows=min_seed_per_depth(12)
        self.assertEqual([r[2] for r in rows],
                         [3,7,15,27,27,91,111,111,111,871,871,871,4591])
        self.assertEqual([r[2] for r in rows],sorted(r[2] for r in rows))

    def test_dimension(self):
        d=dimension()
        self.assertAlmostEqual(2**(-d)+8**(-d),1,places=14)
        self.assertTrue(.55<d<.56)

    def test_bounded_scan_matches_cylinder_minima(self):
        _,_,first,_=scan(20000)
        for depth,count,minimum,*_ in min_seed_per_depth(12):
            if depth and minimum<=20000:
                self.assertEqual(first[depth],minimum)

    def test_small_frontier(self):
        maximum,witness,first,hist=scan(110)
        self.assertEqual(first[1],7)
        self.assertEqual(first[2],15)
        self.assertEqual(first[3],27)
        self.assertEqual(first[4],27)
        self.assertEqual(first[5],91)
        self.assertGreaterEqual(maximum,5)

if __name__=='__main__':
    unittest.main()
