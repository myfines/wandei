# Forced non-cheap excursion count — RETRACTED

Status: **retracted as a global counting argument**. See `notes/2026-10-01-erratum-cheap-excursion-global-count.md`.

The local lemma used here remains correct: the mechanical factor `(21)^4` is impossible, so at most three cheap `21 / a=12` excursions can occur **immediately back-to-back with no intervening boundary waiting transitions**.

The error was to promote that local adjacency statement to the global excursion sequence. After returning to `h=0`, the orbit may remain on the boundary for one or more mechanical transitions before the next departure. Those waiting transitions change the phase, so successive excursions need not correspond to adjacent `21` factors.

Therefore the inference

`E excursions => at least floor(E/4) non-cheap excursions`

is invalid in general.

The previously stated lower bound `181702471` is withdrawn, as is any later numerical non-cheap lower bound obtained from the same step.

Independent statements about individual excursions remain usable, including:

- every departure `0->1` has `r=2,a=1`;
- a two-step heavy `22 / a=13` immediate return is impossible;
- a three-step excursion has mechanical type `212` or `221`;
- sharp odd-height `r=2` direct repayments are globally limited to at most five in the first candidate.

Any future global frequency argument must model boundary waiting explicitly.
