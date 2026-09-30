# Forced non-cheap excursion count

Status: exact combinatorial consequence of the certified excursion lower bound and cheap-run cap. Not a Collatz proof.

The first-candidate defect budget and boundary-run certificate force at least E = 726809885 boundary excursions.

The rotation lemma proves that at most three cheap two-step excursions can occur consecutively. Therefore, in any sequence of E excursions with no run of four cheap excursions, the number Q of non-cheap excursions satisfies

Q >= floor(E/4) = 181702471.

Hence a first-candidate survivor requires at least 181702471 non-cheap excursions.

Every excursion leaves the boundary through 0->1, necessarily with r=2 and a=1. If it returns immediately on the next step, then h=1 must go to 0, so a=1+r.

If the next mechanical symbol is r=1, then a=2 and the excursion is exactly the cheap 21 / a=12 type already counted.

If a non-cheap excursion nevertheless returns in two steps, the next symbol must therefore be r=2 and a=3. This is an odd-height direct repayment at an r=2 phase, so the direct-repayment phase gate applies:

theta > log2(128/65) = 0.9776321869...

Otherwise the non-cheap excursion cannot return in two steps and has length at least 3.

Thus at least 181702471 forced interruptions obey the dichotomy:

(A) a two-step heavy return 0->1->0 of mechanical type 22 and valuation type 13, confined to the top roughly 2.24 percent phase window; or

(B) an excursion of length at least 3.

This is the first deterministic bridge between the cheap-run cap and the heavy-repayment phase gate. The next target is to bound how many type-A interruptions can occur in the rotation word; the remainder are then forced to be length at least 3 and can be charged against the global defect/correction budget.