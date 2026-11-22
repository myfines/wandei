"""Independent integer-only checks of the adelic height no-go witnesses."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from archimedean_adelic_nogo import (
    v_p,syracuse,crt,frozen_shadow,two_recharge,three_discharge,
    odd_prime_excursion,witness_against_linear_height,potential_change
)

class AdelicNoGoTests(unittest.TestCase):
    def test_sharp_frozen_phase_growth(self):
        for L in (1,2,3,8,20,50,100):
            for r in (1,2,3,7):
                for q in (1,2,3,5):
                    n,states=frozen_shadow(L,r,q)
                    self.assertEqual(n+1,2**(L+r)*3**q)
                    for j,x in enumerate(states):
                        self.assertEqual(x+1,2**(L+r-j)*3**(q+j))
                        self.assertEqual(x%(2**r*3**q),2**r*3**q-1)
                        if j<L:self.assertEqual(syracuse(x),(states[j+1],1))

    def test_sharp_minimal_seed_divisibility(self):
        for L in range(1,25):
            for r in range(1,5):
                for q in range(1,4):
                    n,_=frozen_shadow(L,r,q)
                    self.assertEqual(n,2**(L+r)*3**q-1)
                    self.assertEqual((n+1)%(2**(L+r)*3**q),0)

    def test_unbounded_2adic_recharge(self):
        for h in range(2,150):
            n,y=two_recharge(h)
            self.assertEqual(syracuse(n),(y,2))
            self.assertEqual(v_p(n+1,2),1)
            self.assertGreaterEqual(v_p(y+1,2),h)
            self.assertEqual((v_p(n+1,3),v_p(y+1,3)),(0,0))

    def test_unbounded_3adic_discharge(self):
        for h in range(1,150):
            n,y=three_discharge(h)
            self.assertEqual(syracuse(n),(y,2))
            self.assertEqual((v_p(n+1,2),v_p(y+1,2)),(1,1))
            self.assertGreaterEqual(v_p(n+1,3),h)
            self.assertEqual(v_p(y+1,3),0)

    def test_independent_odd_prime_excursions(self):
        primes=(5,7,11,13,17,19)
        for p in primes:
            others=tuple(q for q in primes if q!=p)
            for h in (1,2,3,10,20):
                for kind in ('up','down'):
                    n,y=odd_prime_excursion(p,h,kind,others)
                    self.assertEqual(syracuse(n),(y,2))
                    for q in others:
                        self.assertEqual((v_p(n+1,q),v_p(y+1,q)),(0,0))

    def test_constructive_no_go_even_with_bounded_phase(self):
        coeffs=({}, {2:.3},{3:-.7},{2:-.9,3:.4},{5:.25},
                {7:-.12},{2:.2,5:.3,7:-.7},{2:-7,3:2},{3:4})
        for coeff in coeffs:
            for B in (0,1,4):
                d=witness_against_linear_height(coeff,bounded_error=B)
                n=d['seed'];x=n
                for _ in range(d['odd_steps']):x,_=syracuse(x)
                self.assertEqual(x,d['terminal'])
                self.assertGreater(potential_change(n,x,coeff),2*B)

    def test_crt_independent_moduli(self):
        for specs in (((4,1),(9,1),(25,24)),
                      ((8,-1),(27,4),(7,0)),
                      ((9,1),(16,3),(5,-1),(11,0))):
            x=crt(specs)
            for m,r in specs:self.assertEqual(x%m,r%m)

if __name__=='__main__': unittest.main()
