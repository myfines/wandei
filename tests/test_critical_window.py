from fractions import Fraction
import importlib.util
from pathlib import Path

MODULE = Path(__file__).parents[1] / "src" / "critical_window.py"
spec = importlib.util.spec_from_file_location("critical_window", MODULE)
cw = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(cw)


def test_log_bounds_contain_simple_known_decimal_relation():
    ln2 = cw.log_bounds(Fraction(2), 80)
    # 0.69 < log 2 < 0.70, checked entirely as rationals.
    assert Fraction(69, 100) < ln2.lo < ln2.hi < Fraction(70, 100)


def test_certificate_candidate():
    cert = cw.critical_window_certificate()
    assert cert["candidate"] == Fraction(72057431991, 114208327604)
    assert cert["denominator_lower_bound"] == 114208327604


def test_candidate_is_strictly_in_certified_true_window():
    cert = cw.critical_window_certificate()
    c = cert["candidate"]
    assert cert["alpha_n"].hi < c
    assert c < cert["alpha"].lo


def test_cf_split_is_9_10_after_23_terms():
    cert = cw.critical_window_certificate()
    assert len(cert["common_cf"]) == 23
    assert {cert["left_next"], cert["right_next"]} == {9, 10}
