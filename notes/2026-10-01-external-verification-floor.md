# External verification floor check — 2026-10-01

Proof dependency check only; not a new Collatz theorem.

The live David Barina convergence-verification page currently states that all starting values below

\[
\boxed{2075\cdot2^{60}}
\]

have been verified to converge. The next work-unit target is `2076*2^60` and is not yet complete.

Sources checked on 2026-10-01:

- https://pcbarina.fit.vutbr.cz/
- Barina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81 (2025), which records the `2^71` milestone.

Therefore the repository's current lower bound

\[
N_0=2075\cdot2^{60}
\]

remains the appropriate live computational floor for the first-contraction certificate.