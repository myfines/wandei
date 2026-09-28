from src.cf_window import alpha_and_upper, first_upper_semiconvergent


def test_window_positive():
    alpha, upper = alpha_and_upper(2**71)
    assert upper > alpha


def test_first_hit_for_2pow71():
    hit = first_upper_semiconvergent(2**71)
    assert hit is not None
    j, q, err, slack, idx, t = hit
    assert (j, q) == (114_208_327_604, 72_057_431_991)
    assert err > 0
    assert slack >= 0
    assert idx == 23
    assert t == 1


def test_previous_upper_convergent_is_outside_window():
    alpha, upper = alpha_and_upper(2**71)
    j, q = 10_439_860_591, 6_586_818_670
    from decimal import Decimal, localcontext

    with localcontext() as ctx:
        ctx.prec = 140
        ratio = Decimal(j) / Decimal(q)
    assert ratio > upper > alpha


def test_current_project_bound_has_same_first_hit():
    hit = first_upper_semiconvergent(2075 * 2**60)
    assert hit is not None
    assert hit[:2] == (114_208_327_604, 72_057_431_991)
