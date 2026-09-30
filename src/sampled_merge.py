"""Exact merge-or-descend experiments for the 2 mod 9 sampled Terras map.

Research code only. A finite scan is evidence, not a Collatz proof.

State convention:
    sampled n satisfies n == 2 (mod 9)
    M = 4*n + 1, hence M == 9 (mod 36)

The exact induced map is the one documented in notes/2026-09-29-induced-mod9-map.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional


def vp(n: int, p: int) -> int:
    if n <= 0:
        raise ValueError("vp expects n>0")
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


@dataclass(frozen=True)
class Branch:
    e: int
    eta: int
    t: int
    q: int


@dataclass(frozen=True)
class Certificate:
    kind: str  # "drop" or "merge"
    depth: int
    state: int
    smaller: Optional[int] = None


def induced(M: int) -> tuple[int, Branch]:
    """One exact sampled return in M-coordinates."""
    if M <= 0 or M % 36 != 9:
        raise ValueError("sampled M must be positive and 9 mod 36")

    n = (M - 1) // 4
    v = vp(n, 2)
    e = 2 * min(v // 2, 2)
    eta = (1 << (e + 2)) - 1
    t = vp(M + eta, 2)
    w = (M + eta) >> t

    candidates = [q for q in (t - e - 2, t - e - 1) if q >= 0]
    qs = [q for q in candidates if (pow(3, q, 4) * (w % 4)) % 4 == 1]
    if len(qs) != 1:
        raise AssertionError((M, e, eta, t, w, candidates, qs))

    q = qs[0]
    out = (3**q) * w
    if out % 36 != 9:
        raise AssertionError((M, out, e, eta, t, q))
    return out, Branch(e=e, eta=eta, t=t, q=q)


def predecessors(Y: int) -> list[int]:
    """Enumerate every positive one-return sampled predecessor of Y."""
    if Y <= 0 or Y % 36 != 9:
        raise ValueError("sampled Y must be positive and 9 mod 36")

    V = vp(Y, 3)
    ans: set[int] = set()

    for e in (0, 2, 4):
        eta = (1 << (e + 2)) - 1
        for delta in (0, 1):
            for q in range(V + 1):
                r = q - delta
                if r < 0:
                    continue
                t = e + r + 2
                s = Y // (3**q)
                X = (1 << t) * s - eta
                if X <= 0 or X % 36 != 9:
                    continue
                try:
                    out, _ = induced(X)
                except (AssertionError, ValueError):
                    continue
                if out == Y:
                    ans.add(X)

    return sorted(ans)


def certificate(M0: int, max_returns: int = 100) -> Optional[Certificate]:
    """Find a direct-descent or one-step-merge induction certificate."""
    if M0 == 9:
        return Certificate("drop", 0, 9, 9)

    y = M0
    for depth in range(max_returns + 1):
        if y < M0:
            return Certificate("drop", depth, y)

        ps = predecessors(y)
        if ps and ps[0] < M0:
            return Certificate("merge", depth, y, ps[0])

        if depth < max_returns:
            y, _ = induced(y)

    return None


def scan(limit: int, max_returns: int = 100) -> dict[str, object]:
    """Exact finite scan over M == 9 mod 36 below limit."""
    counts = {"drop": 0, "merge": 0, "unresolved": 0}
    max_depth = 0
    worst: list[tuple[int, Certificate]] = []
    unresolved: list[int] = []

    for M in range(9, limit, 36):
        if M == 9:
            continue
        cert = certificate(M, max_returns=max_returns)
        if cert is None:
            counts["unresolved"] += 1
            unresolved.append(M)
            continue

        counts[cert.kind] += 1
        if cert.depth > max_depth:
            max_depth = cert.depth
            worst = [(M, cert)]
        elif cert.depth == max_depth:
            worst.append((M, cert))

    return {
        "limit": limit,
        "max_returns": max_returns,
        "counts": counts,
        "max_depth": max_depth,
        "worst": worst,
        "unresolved": unresolved,
    }


if __name__ == "__main__":
    # Deliberately modest default. Increase explicitly for experiments.
    result = scan(1_000_000, max_returns=100)
    print(result)
