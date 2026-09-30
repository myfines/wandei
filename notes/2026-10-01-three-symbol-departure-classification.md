# Three-symbol mechanical classification after a boundary departure

Status: exact irrational-rotation lemma. Not a Collatz proof.

Let beta=log2(3)-1 and theta_n={n log2(3)}. The mechanical symbol r_n is 2 iff theta_n >= 1-beta.

A boundary departure 0->1 requires r_n=2. We classify the next two mechanical symbols.

Because 1/2 < beta < 2/3. The lower inequality follows from 3^2>2^3 (9>8), and the upper from 3^3<2^5 (27<32).

After r_n=2, theta_{n+1}=theta_n+beta-1 lies in [0,beta).

If r_{n+1}=1, then theta_{n+1}<1-beta. Hence theta_{n+2}=theta_{n+1}+beta >= beta > 1-beta, so r_{n+2}=2. Thus 21 must extend to 212; 211 is impossible.

If r_{n+1}=2, then theta_{n+1}>=1-beta and theta_{n+2}=theta_{n+1}+beta-1 < 2beta-1. Since beta<2/3, we have 2beta-1 < 1-beta, so r_{n+2}=1. Thus 22 must extend to 221; 222 is impossible.

Therefore every length-three mechanical word beginning with a boundary departure symbol 2 is exactly one of

212 or 221.

This reduces the classification of shortest extended excursions to two mechanical cylinders.