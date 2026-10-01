"""Exact combinatorial counts for clean 46-step windows with four upsteps.

No Syracuse seed enumeration is performed here.  This script only counts the
complete translated defect scripts in each possible exact-four-upstep height
pattern, over all 47 length-46 mechanical factors.

A clean script excludes a positive odd-height r=2 direct repayment to h=0,
the globally rare class handled by sharp_repayment_phase_cert.py.
"""

from collections import defaultdict

STEPS = 46

PATTERNS = {
    "U4": (4,),
    "U3V1": (3, 1),
    "U2V2": (2, 2),
    "U1V3": (1, 3),
    "U2V1T1": (2, 1, 1),
    "U1V2T1": (1, 2, 1),
    "U1V1T2": (1, 1, 2),
    "U1V1T1Q1": (1, 1, 1, 1),
}

EXPECTED = {
    "U4": 108_873_821,
    "U3V1": 832_402_470,
    "U2V2": 1_845_939_946,
    "U1V3": 1_168_612_420,
    "U2V1T1": 1_247_416_421,
    "U1V2T1": 2_580_273_296,
    "U1V1T2": 1_278_349_195,
    "U1V1T1Q1": 1_425_030_236,
}


def exact_mechanical_letters(count: int) -> list[int]:
    p = 1
    floors = []
    for _ in range(count + 1):
        floors.append(p.bit_length() - 1)
        p *= 3
    return [floors[j + 1] - floors[j] for j in range(count)]


def all_factors():
    mech = exact_mechanical_letters(400)
    seen = {}
    for shift in range(len(mech) - STEPS + 1):
        word = tuple(mech[shift : shift + STEPS])
        seen.setdefault(word, shift)
        if len(seen) == STEPS + 1:
            break
    assert len(seen) == 47
    return sorted((shift, word) for word, shift in seen.items())


def count_pattern(word: tuple[int, ...], target: tuple[int, ...]) -> int:
    max_height = len(target)
    zero = (0,) * max_height
    states = {(0, zero): 1}

    for r in word:
        nxt = defaultdict(int)
        for (h, counts), multiplicity in states.items():
            for next_h in range(max_height + 1):
                a = h + r - next_h
                if a < 1:
                    continue

                # Remove globally rare odd-height direct repayments at r=2.
                if h > 0 and (h & 1) and r == 2 and next_h == 0:
                    continue

                new_counts = list(counts)
                if next_h == h + 1:
                    if h >= max_height:
                        continue
                    new_counts[h] += 1
                    if new_counts[h] > target[h]:
                        continue

                nxt[(next_h, tuple(new_counts))] += multiplicity
        states = nxt

    return sum(
        multiplicity
        for (h, counts), multiplicity in states.items()
        if counts == target
    )


def main() -> None:
    factors = all_factors()
    totals = {}
    for name, target in PATTERNS.items():
        total = sum(count_pattern(word, target) for _, word in factors)
        totals[name] = total
        print(name, total)
        assert total == EXPECTED[name]

    assert sum(totals.values()) == 10_486_897_805
    print("TOTAL_EXACT_FOUR", sum(totals.values()))
    print("CERTIFIED")


if __name__ == "__main__":
    main()
