# Low-G survival forces a huge density of one neutral mod-16 cylinder

Status: exact unconditional arithmetic consequence inside the first coefficient-contraction candidate. Not a Collatz proof.

Let

`G = #{j<k : r_j=2, a_j=1}`

be the total defect-upstep count.

## 1. A trivial but strong global lower bound for `a=1`

For the fixed first candidate

`k = 72,057,431,991`,

`A_k = 114,208,327,604`,

and

`h_k=floor(k log_2 3)-A_k=-1`.

Hence

`floor(k log_2 3)=A_k-1=114,208,327,603`.

Since

`sum_{j<k} r_j=floor(k log_2 3)`

and every `r_j` is 1 or 2, the exact mechanical counts are

`R2 = 42,150,895,612`,

`R1 = 29,906,536,379`.

Write `A1=#{j<k:a_j=1}`. Since every non-`a=1` exponent is at least 2,

`A_k >= A1 + 2(k-A1) = 2k-A1`.

Therefore

`boxed: A1 >= 2k-A_k = 29,906,536,378 = R1-1.`

## 2. Split the `r=1,a=1` events modulo 16

Every `a=1` odd state is `3 mod4`, hence lies in one of

`3,7,11,15 mod16`.

Consider an event with `r_j=1,a_j=1`. The mechanical word has no `11` factor, so necessarily `r_{j+1}=2`.

### Start `x_j == 3 mod16`

After the `a_j=1` step,

`x_{j+1}=(3x_j+1)/2`

lies in `5 or13 mod16`. These classes have next exponent at least 4 or exactly 3, respectively. Thus

`a_{j+1}>=3`.

Since `r_{j+1}=2`, the next defect increment is at most `-1`. Therefore every such event injects into a negative-defect transition. If `D` denotes total negative defect mass, then

`C3 <= D`.

Because `h_0=0`, `h_k=-1`, and there are `G` unit upward increments,

`D=G+1`.

Hence

`boxed: C3 <= G+1.`

### Start `x_j == 7 or15 mod16`

After the `a_j=1` step the next odd state is again `3 mod4`, hence

`a_{j+1}=1`.

With `r_{j+1}=2`, this next transition is exactly a defect upstep. Distinct starts have distinct successors, so

`boxed: C7+C15 <= G.`

### Start `x_j == 11 mod16`

Here the exact valuation prefix is

`(a_j,a_{j+1})=(1,2)`.

Since the mechanical pair is necessarily

`(r_j,r_{j+1})=(1,2)`,

both defect increments are zero. This is the unique neutral escape cylinder among `r=1,a=1` events.

Let

`C11 = #{j<k : r_j=1, a_j=1, x_j==11 mod16}`.

## 3. Global inequality

Every `a=1` event is either

- an `r=2,a=1` upstep counted by `G`, or
- one of `C3,C7,C11,C15`.

Thus

`A1 = G + C3 + C7 + C11 + C15`.

Using the two bounds above,

`A1 <= G + (G+1) + G + C11`,

so

`boxed: C11 >= A1 - 3G - 1.`

Combining with `A1>=29,906,536,378`,

`boxed: C11 >= 29,906,536,377 - 3G.`

Equivalently, any independent upper bound `C11<=M` gives

`boxed: G >= ceil((29,906,536,377-M)/3).}`

Using the current live lower bound

`G >= 3,191,033,238`,

survival near that lower edge would require as many as

`29,906,536,377 - 3*3,191,033,238 = 20,333,436,663`

occurrences of the single exact neutral cylinder

`x_j == 11 mod16`, `r_jr_{j+1}=12`, `a_ja_{j+1}=12`.

## 4. New main target

The global `r=1,a=1` problem has therefore reduced to one concrete density problem:

> Upper-bound the number of exact neutral `11 mod16 / 12->12` blocks.

Every improvement below `20.33` billion immediately strengthens the global lower bound on `G`; a sufficiently strong bound can close the first candidate when combined with the existing correction budget.
