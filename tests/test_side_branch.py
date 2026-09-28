import importlib.util
from pathlib import Path

MODULE = Path(__file__).parents[1] / "src" / "side_branch.py"
spec = importlib.util.spec_from_file_location("side_branch", MODULE)
sb = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(sb)


def test_exact_side_branch_relation():
    z, a = sb.syracuse_step(21)
    assert (z, a) == (1, 6)

    y1 = sb.lowered_predecessor(z, a, 1)
    y2 = sb.lowered_predecessor(z, a, 2)
    assert y1 == 5
    assert y2 == 1
    assert 21 == 4 * y1 + 1
    assert 21 == 16 * y2 + 5


def test_altitude_floor():
    N = 1000
    assert sb.altitude_floor_for_exponent(1, N) == N
    assert sb.altitude_floor_for_exponent(2, N) == N
    assert sb.altitude_floor_for_exponent(3, N) == 4 * N + 1
    assert sb.altitude_floor_for_exponent(4, N) == 4 * N + 1
    assert sb.altitude_floor_for_exponent(5, N) == 16 * N + 5
    assert sb.altitude_floor_for_exponent(6, N) == 16 * N + 5


def test_low_altitude_caps():
    assert sb.exponent_cap_below_height_multiplier(1) == 2
    assert sb.exponent_cap_below_height_multiplier(3) == 2
    assert sb.exponent_cap_below_height_multiplier(4) == 4
    assert sb.exponent_cap_below_height_multiplier(15) == 4
    assert sb.exponent_cap_below_height_multiplier(16) == 6
