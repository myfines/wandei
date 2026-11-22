"""Nine independent integer/forward checks for the high-dimensional lift."""
import sys,unittest,math
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from inverse_height_spectral_lift import (
 S,a0,parent_preimage,first_turn,ancestor_count,envelope,
 inverse_levels,forward_first_hits,residues,phase_energy,sparse_energy_floor,
 ray_residues,full_phase_height,ray_phase_energy,
 full_ray_weighted_energy,exact_zeta_moment,total_node_bound,
 numeric_fourier,benchmark
)


class InverseHeightSpectrumTests(unittest.TestCase):
    def test_exact_inverse_edges(self):
        for m in range(1,100,2):
            if m%3==0:continue
            for t in range(15):
                n=parent_preimage(m,t)
                self.assertEqual(S(n),m)
                self.assertEqual(3*n+1,2**(a0(m)+2*t)*m)
                self.assertEqual(parent_preimage(m,t+1),4*n+1)
        self.assertEqual(first_turn(1),1)
        self.assertEqual(parent_preimage(1,0),1)
        self.assertEqual(parent_preimage(1,1),5)

    def test_exact_one_ray_height_count(self):
        for m in range(1,70,2):
            if m%3==0:continue
            for X in (1,4,5,21,81,1000):
                t=first_turn(m);manual=0
                while parent_preimage(m,t)<=X:
                    t+=1;manual+=1
                self.assertEqual(ancestor_count(m,X),manual)

    def test_reverse_tree_matches_forward_independently(self):
        for X,d in ((30,6),(201,8),(2000,8),(5000,8)):
            levels=inverse_levels(X,d)
            rev={(n,j) for j,row in enumerate(levels) for n in row if n<=X}
            fwd=set(forward_first_hits(X,d))
            self.assertEqual(rev,fwd)
            self.assertLessEqual(len(rev),total_node_bound(X,d))

    def test_exact_sharp_phase_height_threshold(self):
        for m in (1,5,7,11,13,17):
            for q in range(1,5):
                M=3**q
                self.assertEqual(ray_residues(m,q) and len(ray_residues(m,q)),M)
                X=full_phase_height(m,q)
                self.assertEqual(X,parent_preimage(m,first_turn(m)+M-1))
                self.assertEqual(ancestor_count(m,X),M)
                self.assertEqual(ancestor_count(m,X-1),M-1)

    def test_double_exponential_root_height(self):
        for q in range(1,7):
            X=full_phase_height(1,q)
            self.assertEqual(X,(4**(3**q+1)-1)//3)
            self.assertEqual(X.bit_length(),2*3**q+1)

    def test_sparse_fourier_energy_exact(self):
        for m in (1,5):
            for q in range(1,4):
                M=3**q
                for N in range(M+1):
                    self.assertEqual(ray_phase_energy(m,q,N),N*(M-N))
        for X,d,q in ((30,2,2),(201,4,3),(5000,8,3)):
            c=residues(X,d,q)
            self.assertGreaterEqual(phase_energy(c),sparse_energy_floor(c))

    def test_mellin_weights_prevent_full_phase_cancellation(self):
        for m in (1,5,7):
            for q in (1,2,3):
                W,E=full_ray_weighted_energy(m,q,2)
                self.assertGreater(E,0)
                self.assertGreater(W,0)
                self.assertEqual(ray_phase_energy(m,q,3**q),0)

    def test_parseval_matches_numeric_fft(self):
        for X,d,q in ((100,2,2),(800,5,2),(5000,6,3)):
            c=residues(X,d,q)
            F=numeric_fourier(c)
            val=sum(abs(z)**2 for z in F[1:])
            E=phase_energy(c)
            self.assertAlmostEqual(val,E,delta=1e-7+E*1e-9)

    def test_exact_dirichlet_weight_and_benchmark(self):
        for X,d in ((29,4),(111,6),(1000,9)):
            lhs=exact_zeta_moment(X,d)
            rhs=sum((Fraction(1,n*n) for n,j in forward_first_hits(X,d)),
                    Fraction(0))
            self.assertEqual(lhs,rhs)
        result=benchmark()
        self.assertEqual(result['rooted_count'],287)
        self.assertEqual(result['occupied_residues'],27)
        self.assertEqual(result['unweighted_fourier_energy'],4706)


if __name__=='__main__':unittest.main()
