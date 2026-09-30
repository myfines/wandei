from fractions import Fraction


def terras(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def first_return_word(n: int, max_steps: int = 16):
    assert n % 9 == 2
    x = n
    q = 0
    word = []
    for t in range(1, max_steps + 1):
        if x & 1:
            q += 1
            word.append("O")
        else:
            word.append("E")
        x = terras(x)
        if x % 9 == 2:
            return "".join(word), t, q, x
    return None


def contracting_words():
    # Because gcd(9,2^16)=1, n=2+9k for 0<=k<2^16 runs through
    # every residue class modulo 2^16 exactly once. Hence this exhausts
    # every possible parity prefix of length <=16 starting at n == 2 mod 9.
    out = {}
    for k in range(1 << 16):
        n = 2 + 9 * k
        rec = first_return_word(n)
        if rec is None:
            continue
        word, t, q, endpoint = rec
        c = Fraction(3**q, 2**t)
        if c < 1:
            out.setdefault(word, (t, q, c, n, endpoint))
    return out


if __name__ == "__main__":
    words = contracting_words()
    assert len(words) == 34

    max_contract = max(rec[2] for rec in words.values())
    min_contract = min(rec[2] for rec in words.values())
    assert max_contract == Fraction(243, 256)
    assert min_contract == Fraction(1, 64)

    print("contracting first-return words:", len(words))
    print("coefficient range:", min_contract, "to", max_contract)
    for word, (t, q, c, n, endpoint) in sorted(words.items(), key=lambda z: (z[1][0], z[0])):
        print(f"{word:16s} t={t:2d} q={q:2d} c={c} witness={n}->{endpoint}")
