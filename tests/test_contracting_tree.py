from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import contracting_tree as ct


def test_residue_examples():
    assert ct.residue_for_word((1,)) == 2
    assert ct.residue_for_word((1, 1)) == 8
    assert ct.residue_for_word((1, 1, 1)) == 26


def test_contracting_word_counts():
    expected = {1: 1, 2: 3, 3: 4, 4: 15, 5: 21, 6: 84}
    for depth, count in expected.items():
        assert sum(1 for _ in ct.contracting_words(depth)) == count


def test_survivor_counts_first_layers():
    rows = ct.survivor_layers(6)
    assert [r["survivor_count"] for r in rows] == [1, 2, 6, 17, 51, 151]


def test_known_survivors_persist_to_depth_10():
    final = ct.survivor_layers(10)[-1]["survivors"]
    assert 1 in final
    assert 7 in final
    assert 19 in final
