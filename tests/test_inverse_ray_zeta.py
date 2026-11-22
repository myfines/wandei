"""Independent stdlib test suite for one-step inverse ray Collatz zeta."""
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from inverse_ray_zeta import (
    syracuse, ancestor, target_base, ray_sum, ray_continuation,
    lattice_pole, pole_residue, universal_real_residue,
    target_spectral_phase, first_harmonic_residue, finite_basin_square_sum,
)


class InverseRayZetaTests(unittest.TestCase):
    def test_inverse_ray_integer_dynamics(self):
        for m in range(1,100,2):
            if m%3==0:continue
            B=target_base(m)
            self.assertEqual(B%3,1)
            for t in range(25):
                x=ancestor(m,t)
                self.assertEqual(3*x+1,B*4**t)
                self.assertEqual(syracuse(x),m)
                if t<24:self.assertEqual(ancestor(m,t+1),4*x+1)

    def test_dirichlet_and_analytic_continuation_agree(self):
        for m in (1,5,7,11,17):
            for s in (.5, 1.3, 2.2, complex(.7,1.1), complex(1.4,14.1347)):
                lhs=ray_sum(m,s,150)
                rhs=ray_continuation(m,s,100)
                self.assertLess(abs(lhs-rhs),1e-9)

    def test_all_real_pole_residues_are_target_independent(self):
        for j in range(6):
            exact=universal_real_residue(j)
            self.assertAlmostEqual(exact, (-1)**j/(3**j*math.log(4)),places=13)
            for m in (1,5,7,11,17,101):
                self.assertLess(abs(pole_residue(m,j,0)-exact),1e-10)

    def test_first_nonreal_pole_is_target_phase_fingerprint(self):
        from cmath import exp
        phases=[]
        for m in range(1,100,2):
            if m%3==0:continue
            v=first_harmonic_residue(m)
            expected=exp(-2j*math.pi*target_spectral_phase(m))/math.log(4)
            self.assertLess(abs(v-expected),1e-12)
            phases.append((m,v))
        # Finite numerical sanity check; exact injectivity proved algebraically.
        for i in range(len(phases)):
            for j in range(i):
                self.assertGreater(abs(phases[i][1]-phases[j][1]),1e-6)

    def test_difference_cancels_real_poles_not_nonreal(self):
        self.assertLess(abs(pole_residue(1,2,0)-pole_residue(7,2,0)),1e-12)
        self.assertGreater(abs(pole_residue(1,0,1)-pole_residue(7,0,1)),0.1)
        for m in (1,5,7):
            for j in range(3):
                s=lattice_pole(j,0)
                eps=1e-7
                scaled=eps*ray_continuation(m,s+eps,80)
                self.assertLess(abs(scaled-universal_real_residue(j)),2e-6)

    def test_finite_basin_zeta_and_odd_riemann_zeta_bound(self):
        s20,c20=finite_basin_square_sum(301,20)
        s100,c100=finite_basin_square_sum(301,100)
        self.assertLessEqual(s20,s100)
        self.assertLessEqual(c20,c100)
        self.assertLess(float(s100),math.pi**2/8)
        s1001,c1001=finite_basin_square_sum(1001,150)
        self.assertEqual(c1001,501)
        self.assertLess(float(s1001),math.pi**2/8)
        self.assertGreater(float(s1001),float(s100))


if __name__=='__main__':unittest.main()
