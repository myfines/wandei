# Final boundary repayment is forced into the last 44 odd steps

Status: exact consequence inside the first coefficient-contraction candidate. Not a proof of Collatz.

Assume a least counterexample survives the first candidate

\[
(k,A_k)=(72057431991,114208327604),
\]

and let `m` be the last return to the critical boundary `h=0` before the terminal crossing `h_k=-1`. Put

\[
\ell=k-m.
\]

The previous suffix-rigidity lemma shows that once `m` is fixed, the entire exponent suffix is forced: it is the critical mechanical word up to the last step, and the terminal exponent is exactly one larger than mechanical.

The exact certificate is implemented in `src/last_boundary_44_cert.py`.

## 1. Uniform height band for a boundary state

For any `h_m=0` state,

\[
\frac{x_m}{N}
=2^{\{m\log_2 3\}}
\prod_{i<m}\left(1+\frac1{3x_i}\right).
\]

Using `x_i>=N>=N_0`, where

\[
N_0=2075\,2^{60},
\]

and `m<k`, we have

\[
\prod_{i<m}\left(1+\frac1{3x_i}\right)
<\exp\left(\frac{k}{3N_0}\right)
<\frac{65}{64}.
\]

Hence

\[
\boxed{\frac{x_m}{N}<\frac{65}{32}.}
\]

Together with

\[
N<\frac43\,2^{71},
\]

this gives

\[
\boxed{x_m<\frac{65}{24}\,2^{71}.}
\]

## 2. Exact terminal cylinder residues

Using a rigorous rational interval for `log_2 3`, the final mechanical exponents are certified exactly. Backward cylinder lifting gives the least positive residues

\[
R_{45}=7511355327673617840953,
\]

\[
R_{46}=5007570218449078560635,
\]

\[
R_{47}=57048669441874987026937.
\]

For `ell=45`, the cylinder modulus is `2^73`, already larger than the whole admissible boundary-state band. The unique possible representative is `R_45`, but

\[
R_{45}>\frac{65}{24}\,2^{71},
\]

so `ell=45` is impossible.

For `ell=46`, the modulus is `2^74`, so again there is only one possible representative, namely `R_46`. The exact phase satisfies

\[
\{(k-46)\log_2 3\}<\frac12.
\]

Since the correction product is `<65/64` and

\[
\sqrt2\,\frac{65}{64}<\frac32,
\]

we obtain

\[
\frac{x_{k-46}}N<\frac32.
\]

But `R_46>2^72`, hence

\[
N>\frac23R_{46}>\frac43\,2^{71},
\]

contradicting the first-candidate upper bound. Therefore `ell=46` is also impossible.

## 3. All longer suffixes are impossible at once

For `ell>=47`, extend backward from the exact residue `R_47`. At each additional mechanical step with exponent `a in {1,2}`, the lifted least positive residue has the form

\[
R' = \frac{2^aR-1+q2^M}{3},\qquad q\in\{0,1,2\}.
\]

Dropping the nonnegative wrap term gives

\[
R'\ge\frac{2^aR-1}{3}.
\]

Over any contiguous critical mechanical block of `s` steps, the multiplicative factor satisfies

\[
\frac12<\frac{2^A}{3^s}<2,
\]

because

\[
A=\lfloor(n+s)L\rfloor-\lfloor nL\rfloor,
\qquad L=\log_2 3.
\]

Every accumulated `-1/3` correction is multiplied by a later mechanical subblock whose factor is `<2`, so the total subtraction is `<2s/3`. Therefore every longer lifted residue satisfies

\[
R_{47+s}>rac12R_{47}-\frac{2s}{3}
>\frac12R_{47}-\frac{2k}{3}.
\]

The exact integer certificate verifies

\[
\frac12R_{47}-\frac{2k}{3}
>\frac{65}{24}\,2^{71}.
\]

Thus every `ell>=47` cylinder lies entirely above the admissible boundary-state band.

## Conclusion

All suffix lengths `ell>=45` are impossible. Hence any first-candidate survivor must make its final repayment to `h=0` extremely late:

\[
\boxed{k-m\le44.}
\]

Equivalently,

\[
\boxed{m\ge k-44=72057431947.}
\]

Combined with the earlier 46-step prefix exclusion, a hypothetical survivor must create a positive critical defect near the very beginning, remain in the nonnegative-defect regime for essentially the entire `72`-billion-step candidate window, and make its final repayment only within the last 44 odd-only steps.

This does not yet eliminate the first candidate, but it compresses the remaining terminal freedom to 44 exact suffix cylinders.