from fractions import Fraction
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import reverse_barrier as rb


def test_min_reverse_step():
    assert rb.min_reverse_step(5) == (3, 1)
    assert rb.min_reverse_step(7) == (9, 2)
    assert rb.min_reverse_step(3) is None


def test_chain_terminates_correctly():
    p = rb.reverse_profile_for_residue(5, 2)
    assert p.exponents == (1,)
    assert p.stopped_on_multiple_of_three


def test_known_all_ones_barrier():
    # 26 mod 27 realizes reverse exponents (1,1,1).
    # The canonical residue is even, but the class contains odd states,
    # e.g. 53 -> 35 -> 23 -> 15.
    p = rb.reverse_profile_for_residue(26, 3)
    assert p.exponents == (1, 1, 1)
    assert p.barrier == Fraction(27, 8)


def test_word_residue_bijection_small_m():
    for m in range(1, 8):
        assert rb.verify_word_bijection(m)


def test_full_depth_count():
    for m in range(1, 7):
        s = rb.brute_force_summary(m)
        assert s["full_depth_count"] == 2**m
        assert s["full_depth_fraction"] == Fraction(2, 3) ** (m - 1)
