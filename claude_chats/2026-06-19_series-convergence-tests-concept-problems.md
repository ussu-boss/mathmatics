# Exam preparation with concept problems

| | |
|---|---|
| **Started** | 2026-06-19 05:05:22 |
| **Last updated** | 2026-06-19 05:42:37 |
| **Messages** | 8 |
| **Conversation id** | `561d748b-b210-4230-89ed-6f02c7b7100f` |

> Exported from the Claude data export (`conversations-000.zip`, 2026-08-28).
> Files Claude generated in-chat are reproduced inline below and saved separately
> under `generated_files/`.


---

### [1] **You** - 2026-06-19 05:05:22

if i share any topic content , you have to give all important fact and tricky things where problem could land and also in past exams have been encountere, and generate at least 10 different problems around same concept. 
should i share now?


---

### [2] **Claude** - 2026-06-19 05:05:38

<details><summary>Claude's thinking</summary>

I'm looking at a project file for NET/JRF physics preparation focused on mathematical physics. The user wants me to extract key facts, identify common pitfalls and exam-relevant topics, and create at least ten practice problems based on the material.

</details>

Yes, go ahead and share. Just to confirm what you'll get back for each topic:

- **Core facts & must-know formulas** — the essentials you can't afford to forget
- **Tricky spots / common traps** — sign errors, edge cases, conditions people overlook, and the subtle conceptual confusions that cost marks
- **Past-exam relevance** — where and how the concept has shown up in NET/JRF (and the typical *style* of question)
- **10+ practice problems** — varied in difficulty and approach, covering the same concept from different angles

A couple of quick things that'll make my output sharper:

1. **Paste the topic content** (text, or tell me the section if it's from your Mathematical Physics file already in the project).
2. Tell me if you want the **practice problems with full solutions**, or **problems first, solutions hidden/separate** so you can attempt them yourself first.

Share whenever you're ready.


---

### [3] **You** - 2026-06-19 05:07:42

and also while explaining concept follow alsways rules 1. mathematical explanation in simple way 2. with proper example. then generate 10 problems along with solution around that.
now first topic is
|r| < 1, the geometric series converges. It clearly diverges (or is oscilla tory) for |r| ≥ 1,


---

### [4] **Claude** - 2026-06-19 05:10:34

> **File attached:** `1.Mathematical Physics_NETJRF 1.pdf`

> **File attached:** `1.Mathematical Physics_NETJRF 1.pdf`

> **File attached:** `1.Mathematical Physics_NETJRF 1.pdf`

> **File attached:** `1.Mathematical Physics_NETJRF 1.pdf`

<details><summary>Claude's thinking</summary>

I'm looking at the geometric series convergence topic from their Mathematical Physics NET/JRF material—specifically the convergence criteria where |r| < 1 leads to convergence while |r| ≥ 1 results in divergence or oscillation. Let me pull up the full context from their project knowledge to give them a complete explanation.

</details>

*Searched project knowledge: `geometric series convergence |r| < 1 diverges oscillatory ratio test`*

<details><summary>Claude's thinking</summary>

I'm looking for more specific context around geometric series in the NET/JRF problems they mentioned, particularly to understand how it connects to the broader topics of Taylor expansions and radius of convergence.

</details>

*Searched project knowledge: `sum of geometric series a/(1-r) common ratio first term partial sum`*

<details><summary>Claude's thinking</summary>

I'm seeing how the geometric series connects across multiple problem types in this material—from Laplace transforms and convergence analysis to stability questions. The pattern is becoming clearer as I trace these applications through the different topics.

Now I need to structure a comprehensive response that covers the mathematical foundation, practical examples, common pitfalls students encounter, how this appears in past exams, and then work through a substantial set of problems with detailed solutions. I'm realizing the user wants this as an iterative chat experience where they share topics one at a time, so keeping everything inline makes sense for flow. I should use LaTeX formatting for the math notation since it renders in Claude.ai, and while the content is substantial and structured, the conversational back-and-forth nature of their request means I should present it inline rather than as an artifact.

Now I'm diving into the actual math content. A geometric series is a sum where each term is the previous term multiplied by a constant ratio. I need to establish the formula for both infinite and finite series, then work through the key concepts like convergence conditions and the sum formula.

For a finite series with n terms, I can derive the formula by multiplying by the ratio and subtracting to get $S_n = a\frac{1-r^n}{1-r}$. For infinite series, convergence depends entirely on the common ratio: if the absolute value of r is less than 1, the series converges to $\frac{a}{1-r}$; otherwise it diverges. The edge cases matter too — when r equals 1 the sum grows without bound, and when r equals -1 the terms oscillate without settling.

A critical mistake students make is forgetting that the formula uses the actual first term of the series, not always 1. If a geometric series starts at $n=2$ instead of $n=0$, the first term is $r^2$, not 1, so the sum becomes $\frac{r^2}{1-r}$. Similarly, the index where the series begins changes which term counts as "first," so I need to be careful about whether I'm summing from $n=0$ or $n=1$ or some other starting point.

The geometric series also extends into the complex plane—when the ratio $r$ is complex, convergence still requires $|r| < 1$, which defines a disk in the complex plane with radius of convergence equal to 1. This geometric series formula is fundamental because it's the basis for expanding functions like $\frac{1}{1-x} = 1 + x + x^2 + \cdots$ for $|x| < 1$.

By substituting $x \to -x$, I get $\frac{1}{1+x} = 1 - x + x^2 - \cdots$, and this same principle extends to binomial series with negative integer powers, Laurent series expansions, and determining convergence regions for Taylor series.

The Laurent series expansion of $\frac{1}{z-a}$ in different regions is a classic NET problem—for $|z| < |a|$, I factor out $-1/a$ and expand as a power series in $z$, while for $|z| > |a|$ the expansion changes form entirely.

The key is recognizing which factor to pull out based on making the ratio less than 1 in magnitude, which determines the entire structure of the expansion.

Differentiating geometric series like $\frac{1}{1-x} = \sum x^n$ generates useful formulas for $\frac{1}{(1-x)^2}$ and higher powers, which then lets me compute sums involving $n x^n$ and $n^2 x^n$ terms—exactly the type NET loves to ask.

For periodic functions and Laplace transforms, geometric series appear naturally in the form $e^{-sT}$, creating denominators like $\frac{1}{e^s - 1}$ from the geometric series formula. I need to be careful about the sign convention: when $|r| < 1$, the denominator is $1-r$, not $r-1$.

At the boundary where $|r| = 1$, the formula breaks down entirely — at $r=1$ it's undefined (division by zero), and at $r=-1$ the result $\frac{a}{2}$ is only an Abel or Cesàro sum, not the actual sum, which doesn't converge. This is a subtle point NET might test: the series $1-1+1-1+\cdots$ does not equal $1/2$ in the ordinary sense.

Geometric series also show up constantly in physics applications like Fabry-Perot cavities with multiple reflections, successive scattering events, image charge problems between parallel plates, and calculating total distances for bouncing balls.

I'm recalling a past exam question involving a Laplace transform of a step function where the answer involved summing a geometric series with $r = e^{-s}$, giving something like $\frac{1}{s(e^s-1)}$, though I should be careful about citing exact exam details.

I don't need to use citation tags for the project knowledge material since those aren't web search results—I can just reference the topics naturally. Geometric series, radius of convergence, and Laurent series all appear in their standard material.

Now I'm thinking through how to design 10 problems with good variety and increasing difficulty in the NET/JRF style. Now I'm working through concrete examples with full solutions — starting with a basic geometric series where the first term is 2 and ratio is 1/3, then moving into convergence conditions for series like $(2x-1)^n$ to establish when they're valid. Alternatively, I can compute the full sum starting from $n=0$ to get 2, then subtract the first three terms totaling $7/4$ to arrive at $1/4$. Now for the repeating decimal $0.\overline{27}$, I'm recognizing this as a geometric series with first term $27/100$ and ratio $1/100$, which gives the sum $\frac{27/100}{99/100}$.

For complex series, the geometric series $\sum_{n=0}^\infty z^n$ converges when $|z| < 1$ with radius of convergence $R = 1$ and sum $\frac{1}{1-z}$. To evaluate $\sum_{n=1}^{\infty} \frac{n}{2^n}$, I'm using the derivative formula $\sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2}$ and substituting $x = 1/2$.

For the Laurent expansion of $\frac{1}{z-2}$ in the region $|z| > 2$, I'm rewriting it as $\frac{1}{z} \cdot \frac{1}{1 - 2/z}$ and expanding using the geometric series since $|2/z| < 1$ in that region.

I'm also showing the contrast by finding the expansion valid for $|z| < 2$, where I factor out $-\frac{1}{2}$ and expand $\frac{1}{1-z/2}$ as a power series in $z$ instead of $1/z$.

Now moving to a problem about impulse response and periodic trains: I need to evaluate the geometric series $\sum_{n=1}^{\infty} e^{-ns}$ where $\text{Re}(s) > 0$. The first term is $e^{-s}$ and the common ratio is also $e^{-s}$, which has magnitude less than 1 in the required region, so the series converges to $\frac{e^{-s}}{1 - e^{-s}}$, which simplifies nicely to $\frac{1}{e^{s}-1}$. This form actually connects directly to the Laplace transform of periodic functions.

For the bouncing ball problem, I'm tracking the total distance: the ball falls distance $h$ initially, then bounces up and down repeatedly, with each bounce reaching a fraction $f$ of the previous height. The up-and-down distances form the series $2hf + 2hf^2 + 2hf^3 + \cdots$, which I can factor as $2hf(1 + f + f^2 + \cdots)$. Using the geometric series formula, this becomes $2hf \cdot \frac{1}{1-f}$. Adding the initial drop, the total distance is $h + \frac{2hf}{1-f}$, which combines to $\frac{h(1+f)}{1-f}$.

For the alternating series $\sum_{n=0}^\infty (-1)^n$, the common ratio is $r = -1$, so $|r| = 1$ and the geometric series formula doesn't apply—the series diverges. The partial sums oscillate between 1 and 0 with no limit, but the value $\frac{1}{2}$ can be assigned through Cesàro or Abel summation as a regularized sum, not a true convergent sum. The key trap is that plugging $r = -1$ directly into the geometric formula is invalid.

Now I'm splitting the next series into two separate geometric series: $\sum \frac{3^n}{6^n} + \sum \frac{2^n}{6^n}$ becomes $\sum (1/2)^n + \sum (1/3)^n$, which converge to $2 + \frac{3}{2} = \frac{7}{2}$.

For the cosine series with $|r| < 1$, I'm using the complex exponential approach: expressing $\cos(n\theta)$ as the real part of $e^{in\theta}$, then summing the geometric series $\sum (re^{i\theta})^n = \frac{1}{1 - re^{i\theta}}$.

To extract the real part, I'm multiplying numerator and denominator by the conjugate $1 - re^{-i\theta}$, which gives me $\frac{1 - r\cos\theta + ir\sin\theta}{1 - 2r\cos\theta + r^2}$. The real part yields the final answer: $\sum r^n \cos n\theta = \frac{1 - r\cos\theta}{1 - 2r\cos\theta + r^2}$, and the imaginary part similarly gives the sine series formula.

Now I'm organizing the full response with the concept explanation, common pitfalls, connections to past exams, and all twelve problems with solutions, using LaTeX formatting throughout. I'll skip adding a visual since the user is in rapid study mode and asked specifically for math, examples, and problems. I'll keep everything text-based with clear LaTeX formatting using `$...$` for inline and `$$...$$` for display equations, and organize it with headers for readability. Time to write the full response.

</details>

Good—rules noted. I'll follow this exact format every time: **simple math explanation → worked example → key facts → traps → past-exam relevance → 10+ problems with solutions.**

I checked your fiziks Mathematical Physics notes, and here's the important thing to realize upfront: the geometric series looks trivial, but it is the *engine* behind a huge fraction of NET/JRF questions — radius of convergence, Laurent series, Laplace transforms of periodic functions, fixed-point stability. So mastering it pays off far beyond "find the sum."

---

## 1. The concept, simply

A **geometric series** is a sum where each term is the previous term multiplied by a fixed number $r$ (the *common ratio*):

$$S = a + ar + ar^2 + ar^3 + \cdots = \sum_{n=0}^{\infty} ar^n$$

- $a$ = **first term**
- $r$ = **common ratio** (term $\div$ previous term)

**Finite sum** (first $n$ terms):
$$S_n = a\,\frac{1-r^n}{1-r}\qquad (r\neq 1)$$

*Why:* multiply $S_n$ by $r$, subtract — almost everything cancels: $S_n - rS_n = a - ar^n$, so $S_n(1-r) = a(1-r^n)$.

**Infinite sum** — let $n\to\infty$ and watch $r^n$:

| condition | behaviour of $r^n$ | result |
|---|---|---|
| $\lvert r\rvert < 1$ | $r^n \to 0$ | **converges** to $\dfrac{a}{1-r}$ |
| $\lvert r\rvert > 1$ | $r^n \to \infty$ | diverges |
| $r = 1$ | $S_n = na$ | diverges |
| $r = -1$ | $S_n$ flips $a,0,a,0\dots$ | oscillates (no limit) |

So the whole statement you shared boils down to:

$$\boxed{\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r}\quad\text{if and only if}\quad |r|<1}$$

## 2. Worked example

Evaluate $\displaystyle 5 + \frac{5}{2} + \frac{5}{4} + \frac{5}{8} + \cdots$

Here $a = 5$ (the first term) and $r = \tfrac12$ (each term is half the previous). Since $|r| = \tfrac12 < 1$:

$$S = \frac{a}{1-r} = \frac{5}{1-\tfrac12} = \frac{5}{\tfrac12} = 10.$$

## 3. Key facts you must keep ready

- $\displaystyle\sum_{n=0}^{\infty} r^n = \frac{1}{1-r}$ and $\displaystyle\sum_{n=1}^{\infty} r^n = \frac{r}{1-r}$ (both for $|r|<1$)
- $\displaystyle\frac{1}{1-x} = 1 + x + x^2 + \cdots$, and replacing $x\to -x$: $\displaystyle\frac{1}{1+x} = 1 - x + x^2 - \cdots$
- Differentiate the basic series: $\displaystyle\sum_{n=1}^{\infty} n\,x^{n-1} = \frac{1}{(1-x)^2}$, hence $\displaystyle\sum_{n=1}^{\infty} n\,x^{n} = \frac{x}{(1-x)^2}$
- For **complex** ratio, "$|r|<1$" is a *disk* $|z|<R$ — this is precisely the **radius of convergence**.

## 4. Tricky spots where people lose marks

1. **Forgetting $a$ is the *actual* first term.** $\sum_{n=2}^{\infty} r^n$ has first term $r^2$, so its sum is $\frac{r^2}{1-r}$, **not** $\frac{1}{1-r}$. This single mistake is the most common one.
2. **Index start matters.** $\sum_{n=0}$ vs $\sum_{n=1}$ differ by the $n=0$ term. Always write out the first term explicitly.
3. **$1-r$, not $r-1$.** Sign slips here are silent killers.
4. **The boundary $|r|=1$ is *not* covered.** Plugging $r=-1$ to "get $\tfrac12$" is illegal — that series oscillates and has no ordinary sum (the $\tfrac12$ is only an *Abel/Cesàro* averaged value).
5. **Laurent series — which factor to pull out.** To expand $\frac{1}{z-a}$ you must force the ratio below 1 in magnitude:
   - region $|z|<|a|$ → factor out $\frac{-1}{a}$, get powers of $z$;
   - region $|z|>|a|$ → factor out $\frac{1}{z}$, get powers of $1/z$.
   Choosing the wrong one gives a *divergent* series. NET loves this.
6. **"Looks like geometric but isn't."** $\sum n x^n$, $\sum n^2 x^n$ come from *differentiating* the geometric series, not from the plain formula.

## 5. Where this has shown up in NET/JRF (and your notes)

- **Laplace transform of a periodic / step function** (e.g. Q12 in your fiziks notes): the transform reduces to a geometric series in $e^{-s}$, summed as $\frac{a}{1-r}$ with $r = e^{-s}$.
- **Radius of convergence** of Taylor expansions (Q71, Q95): the underlying test is the geometric/binomial $|r|<1$ condition.
- **Laurent series in an annulus** (Q16, Q53): each piece is a geometric series expanded in the correct region.
- **Fixed-point / stability** (Q83): the ratio $\varepsilon_{n+1}/\varepsilon_n$ is effectively a geometric decay factor.

So the same $|r|<1$ idea is being tested in four different disguises.

---

## 6. Practice problems (with full solutions)

**Q1.** Evaluate $\displaystyle\sum_{n=0}^{\infty}\frac{2}{3^n}$.

> First term ($n=0$): $2$. Ratio $r=\tfrac13$, $|r|<1$. $S=\dfrac{2}{1-\tfrac13}=\dfrac{2}{2/3}=\boxed{3}$.

**Q2.** For which real $x$ does $\displaystyle\sum_{n=0}^{\infty}(2x-1)^n$ converge, and what is the sum?

> Ratio $r=2x-1$. Converge iff $|2x-1|<1\Rightarrow 0<x<1$. Sum $=\dfrac{1}{1-(2x-1)}=\dfrac{1}{2(1-x)}$.

**Q3.** *(Index trap)* Evaluate $\displaystyle\sum_{n=3}^{\infty}\left(\tfrac12\right)^n$.

> First term is the $n=3$ term: $(1/2)^3=\tfrac18$. Ratio $\tfrac12$. $S=\dfrac{1/8}{1-1/2}=\boxed{\tfrac14}$.
> Check: full sum $=2$; subtract $n=0,1,2$ terms $\big(1+\tfrac12+\tfrac14=\tfrac74\big)$ → $2-\tfrac74=\tfrac14$. ✓

**Q4.** Write the repeating decimal $0.\overline{27}=0.272727\ldots$ as a fraction.

> $=\dfrac{27}{100}+\dfrac{27}{100^2}+\cdots$, with $a=\tfrac{27}{100},\,r=\tfrac{1}{100}$. $S=\dfrac{27/100}{1-1/100}=\dfrac{27}{99}=\boxed{\tfrac{3}{11}}$.

**Q5.** *(Complex / radius of convergence)* For complex $z$, state where $\sum_{n=0}^{\infty} z^n$ converges and its radius of convergence.

> Converges iff $|z|<1$ — the open unit disk. Radius of convergence $R=1$. Sum $=\dfrac{1}{1-z}$ there.

**Q6.** *(Differentiated series)* Evaluate $\displaystyle\sum_{n=1}^{\infty}\frac{n}{2^n}$.

> Use $\sum_{n=1}^{\infty} n x^n=\dfrac{x}{(1-x)^2}$ (got by differentiating $\frac{1}{1-x}$ and multiplying by $x$). With $x=\tfrac12$: $\dfrac{1/2}{(1/2)^2}=\dfrac{1/2}{1/4}=\boxed{2}$.

**Q7.** *(Laurent series, region matters)* Expand $f(z)=\dfrac{1}{z-2}$ for $|z|>2$ in powers of $1/z$.

> Since $|z|>2\Rightarrow|2/z|<1$:
> $$\frac{1}{z-2}=\frac{1}{z}\cdot\frac{1}{1-2/z}=\frac{1}{z}\sum_{n=0}^{\infty}\left(\frac{2}{z}\right)^n=\frac1z+\frac{2}{z^2}+\frac{4}{z^3}+\cdots$$
> *(Contrast — for $|z|<2$: $\frac{1}{z-2}=-\tfrac12-\tfrac{z}{4}-\tfrac{z^2}{8}-\cdots$, powers of $z$.)*

**Q8.** *(Laplace-type sum — same as Q12 in your notes)* For $\operatorname{Re}(s)>0$, evaluate $\displaystyle\sum_{n=1}^{\infty} e^{-ns}$.

> $a=e^{-s},\,r=e^{-s}$, and $|r|=e^{-\operatorname{Re}(s)}<1$. $S=\dfrac{e^{-s}}{1-e^{-s}}=\boxed{\dfrac{1}{e^{s}-1}}$. This is exactly the structure behind the Laplace transform of a periodic train.

**Q9.** *(Physics application)* A ball dropped from height $h$ rebounds to fraction $f$ ($0<f<1$) of its previous height each bounce. Find the total vertical distance travelled.

> Initial drop $h$; thereafter each bounce contributes up + down $=2hf^{\,k}$:
> $$D=h+2hf+2hf^2+\cdots=h+2hf\cdot\frac{1}{1-f}=h\,\frac{1+f}{1-f}.$$

**Q10.** *(Boundary subtlety)* Does $\displaystyle\sum_{n=0}^{\infty}(-1)^n$ converge? Comment on the value $\tfrac12$.

> $r=-1$, so $|r|=1$ — the formula does **not** apply; the series **diverges**. Partial sums are $1,0,1,0,\ldots$ (oscillating, no limit). The number $\frac{1}{1-(-1)}=\tfrac12$ is only the *Abel/Cesàro averaged* value, **not** the ordinary sum. Plugging $r=-1$ into the formula is the trap.

**Q11.** *(Splitting two geometric series)* Evaluate $\displaystyle\sum_{n=0}^{\infty}\frac{3^n+2^n}{6^n}$.

> Split: $\sum\left(\tfrac12\right)^n+\sum\left(\tfrac13\right)^n=\dfrac{1}{1-1/2}+\dfrac{1}{1-1/3}=2+\tfrac32=\boxed{\tfrac72}$.

**Q12.** *(NET-level: complex ratio for a trig sum)* For $|r|<1$, sum $\displaystyle\sum_{n=0}^{\infty} r^n\cos(n\theta)$.

> Go complex: $\sum (re^{i\theta})^n=\dfrac{1}{1-re^{i\theta}}$ (since $|re^{i\theta}|=|r|<1$). Multiply by the conjugate:
> $$\frac{1}{1-re^{i\theta}}=\frac{1-r\cos\theta+ir\sin\theta}{1-2r\cos\theta+r^2}.$$
> Taking the **real part**:
> $$\sum_{n=0}^{\infty} r^n\cos n\theta=\boxed{\dfrac{1-r\cos\theta}{1-2r\cos\theta+r^2}}$$
> (and the imaginary part gives $\sum r^n\sin n\theta=\dfrac{r\sin\theta}{1-2r\cos\theta+r^2}$).

---

Notice how Q5, Q7, Q8, and Q12 are really the *same* convergence idea reappearing in complex analysis and Laplace transforms — that's the connection examiners exploit.

Want me to do a quick visual of partial sums converging, or shall we move to the next topic? Either way, share the next chunk whenever you're ready.


---

### [5] **You** - 2026-06-19 05:21:02

cauchy root test,d'alember(or cauchy) ratio test,cauchy (maclaurin)integral test,kummer, gauss test,


---

### [6] **Claude** - 2026-06-19 05:23:21

> **File attached:** `1.Mathematical Physics_NETJRF 1.pdf`

> **File attached:** `1.Mathematical Physics_NETJRF 1.pdf`

<details><summary>Claude's thinking</summary>

I'm organizing a comprehensive guide on convergence tests for infinite series, covering the root test, ratio test, integral test, Kummer's test, and Gauss's test. I'll structure each with clear mathematical explanations, worked examples, key takeaways, common pitfalls, and relevance to competitive exams like NET/JRF, then follow up with a set of problems and solutions.

</details>

*Searched project knowledge: `convergence test ratio test root test comparison test series divergence`*

<details><summary>Claude's thinking</summary>

I'm seeing that these convergence tests—Kummer, Gauss, Raabe—form the theoretical backbone for NET/JRF problems around radius of convergence and series behavior, though they don't appear as standalone worked examples in the material I've found. The practical applications focus on ratio and root tests for convergence radius, integral tests for p-series and harmonic series, and the hypergeometric/Gauss test for more complex series.

Now I'm organizing all five convergence tests systematically with clear mathematical definitions, worked examples, and their exam relevance. I'm starting with the Cauchy root test and d'Alembert ratio test, laying out the convergence criteria and typical examples like geometric series and factorial-based series.

For the ratio test, I'm noting that it's particularly useful for finding the radius of convergence in power series, where we compute the limit of consecutive coefficient ratios. Now moving into the integral test, which connects series convergence to improper integrals when the terms come from a positive, continuous, decreasing function. $n+1}$ gives the limit form for Kummer's test, which determines convergence when positive: if the limit is greater than zero the series converges, if it's negative and the reciprocals of the $b_n$ sequence diverge then the original series diverges. This test generalizes several others—setting $b_n = 1$ recovers a version of the ratio test, $b_n = n$ yields Raabe's test (which looks at $n$ times the ratio of consecutive terms minus one), and $b_n = n \ln n$ gives Bertrand's test.

When the ratio test is inconclusive at $L = 1$, Raabe's test is the natural refinement to try next. Gauss's test pushes even further, handling cases where the ratio of consecutive terms can be expressed as $1 + h/n$ plus a bounded remainder term, allowing us to extract more information from the asymptotic expansion. Gauss's test elegantly resolves the boundary case where Raabe's test is inconclusive, definitively declaring divergence when $h = 1$. This makes it particularly useful for hypergeometric series and other boundary cases. Now I'm thinking through how to organize the hierarchy of tests—starting with the basic ratio and root tests, moving to the integral test for nice functions, then Raabe for the trickier $L=1$ cases, and finally Kummer as the overarching framework that encompasses these special cases.

The key pitfalls to watch: ratio and root tests both fail at $L=1$, so you need to escalate to Raabe or Gauss. The root test is technically stronger since it uses $\limsup$ and can succeed where the ratio test's limit doesn't exist. The integral test is easy to misapply if you forget the decreasing condition. And critically, ratio and root tests only detect absolute convergence—for alternating series at the boundary, I need to reach for tools like Leibniz's test instead.

Raabe's test flips the intuition: $R>1$ means convergence, opposite the ratio test's $L<1$. Kummer's test requires the auxiliary series $\sum 1/b_n$ to diverge, and Gauss's test has $h=1$ as a divergence boundary, not convergence. These tests tell me about convergence behavior, not the actual sum value, and they're really detecting absolute convergence. For past exams, radius of convergence problems lean on ratio/root, while p-series and harmonic series use the integral test.

The zeta function and partition functions from thermodynamics are key applications. Hypergeometric series convergence at the boundary $|z|=1$ is where Gauss's test shines. I'm now sketching out a problem set with 10+ varied questions in NET/JRF style, starting with basic ratio test on $\sum n/2^n$, then root test on $\sum (n/(3n+1))^n$, and radius of convergence for power series.

Continuing with radius of convergence for $\sum x^n/n$ giving $R = \infty$, then $\sum n! x^n$ with $R = 0$. I'll include p-series convergence and the integral test applied to $\sum 1/(n \ln n)$. For the trickier cases, I'm designing a problem where the ratio test gives 1 and Raabe's test is needed to resolve convergence, plus a classic Raabe's test example with double factorials. n+1} \to 1/2 < 1$, so this series diverges by Raabe's test, behaving asymptotically like $1/\sqrt{\pi n}$. Now for the Gauss test on a hypergeometric-like series with squared terms: $\sum \left[\frac{(2n-1)!!}{(2n)!!}\right]^2$. The ratio $a_n/a_{n+1}$ expands to $\left(1 + \frac{1}{2n+1}\right)^2$, which gives me $1 + \frac{2}{2n+1} + \frac{1}{(2n+1)^2}$, and I need to work out the asymptotic expansion of that first correction term.

Rewriting $\frac{2}{2n+1}$ by factoring out $2n$ from the denominator and expanding the geometric series, I get $\frac{1}{n} - \frac{1}{2n^2} + O(1/n^3)$, so the full ratio is $1 + \frac{1}{n} + O(1/n^2)$. This means $h = 1$, and by the Gauss test criterion, the series diverges since $h \le 1$.

For the squared case, $[(2n-1)!!/(2n)!!]^2 \sim \frac{1}{\pi n}$, which matches the divergence prediction from the harmonic series. Now testing the cubed version: the ratio becomes $(1 + \frac{3}{2n} + ...)$, giving $h = 3/2 > 1$, so this series converges. I'm reconsidering which problems to include, wanting to keep them clean and grounded in actual applications. I'm sketching out a revised set of questions: starting with the ratio test on $\sum \frac{n^2}{2^n}$, then the root test on a sequence that behaves like $\left(\frac{2n+1}{3n+2}\right)^n$, followed by radius of convergence problems for the exponential series and another power series. Q9 is about what the ratio test teaches when applied to both $\sum 1/n$ and $\sum 1/n^2$ — both yield a limit of 1, showing the test's inconclusiveness. Q10 involves Kummer's general test, demonstrating how choosing $b_n = n$ recovers Raabe's test. Q11 explores the hypergeometric series and its convergence at $z=1$ using Gauss's criterion. Q12 connects to the Riemann zeta function and $p$-series convergence in physical contexts. I should also include an alternating series example like $\sum (-1)^n/n$ to highlight that subtlety.

Now I'm verifying the radius of convergence for the central binomial coefficient series by computing the ratio of consecutive terms, which simplifies to $\frac{n+1}{2(2n+1)}$ approaching $\frac{1}{4}$, giving a radius of 4.

For Q11, I'm applying Gauss's test to the hypergeometric series at $z=1$ by examining the ratio of consecutive terms and expanding both numerator and denominator as quadratic polynomials in $n$.  The leading coefficient cancels, leaving a linear term that dominates: $h = c + 1 - a - b$. The series converges precisely when $h > 1$, which gives the classical result that ${}_2F_1$ at $z=1$ converges if and only if $\text{Re}(c - a - b) > 0$ — a key result that ties back to the hypergeometric questions in the exam.

Now I'm organizing the response with a clear structure: I'll start with a comparison table of all five tests, then give each test its own section with the definition and a worked example, followed by key facts, common traps, past-exam connections, and a set of problems with solutions.

</details>

These five form a **ladder of increasing power**: you start with the cheap tests (ratio, root), and when they fail at the boundary $L=1$, you climb to the sharper ones (Raabe → Kummer → Gauss). The whole point of the ladder is that **Gauss's test never fails** for the ratios that show up in physics (hypergeometric, Legendre, Bessel-type series). Let me build each rung, then show where NET/JRF tests them.

A note on what they all do: every test below is for **positive-term series** $\sum a_n$ (or detects *absolute* convergence). None of them tells you the sum — only whether it's finite.

---

## 1. Cauchy Root Test

**Rule (simple):** look at the $n$-th root of the term.
$$L=\lim_{n\to\infty}\sqrt[n]{a_n}=\lim_{n\to\infty}(a_n)^{1/n}$$
$$L<1\ \Rightarrow\ \text{converges},\qquad L>1\ \Rightarrow\ \text{diverges},\qquad L=1\ \Rightarrow\ \text{no conclusion}.$$

**Example:** $\displaystyle\sum\left(\frac{n}{2n+1}\right)^{n}$. The $n$-th root is $\dfrac{n}{2n+1}\to\dfrac12<1$ → **converges**. (Best when the term already carries an $n$-th power.)

## 2. d'Alembert (Ratio) Test

**Rule (simple):** look at the ratio of consecutive terms.
$$L=\lim_{n\to\infty}\frac{a_{n+1}}{a_n}$$
$$L<1\ \Rightarrow\ \text{converges},\qquad L>1\ \Rightarrow\ \text{diverges},\qquad L=1\ \Rightarrow\ \text{no conclusion}.$$

**Example:** $\displaystyle\sum\frac{1}{n!}$. Ratio $=\dfrac{n!}{(n+1)!}=\dfrac{1}{n+1}\to 0<1$ → **converges** (this sum is $e$). This is the test you use for **radius of convergence**: for $\sum c_n x^n$, $\;R=\lim\left|\dfrac{c_n}{c_{n+1}}\right|$.

## 3. Cauchy (Maclaurin) Integral Test

**Rule (simple):** if $a_n=f(n)$ with $f$ **positive, continuous, and decreasing**, then the sum and the integral live or die together:
$$\sum_{n=N}^{\infty}a_n\quad\text{converges}\iff\int_N^{\infty}f(x)\,dx\ \text{converges}.$$

**Example:** the $p$-series $\displaystyle\sum\frac{1}{n^{p}}$. Since $\int_1^\infty x^{-p}\,dx$ converges iff $p>1$:
$$\boxed{\sum \tfrac{1}{n^p}\ \text{converges} \iff p>1.}$$
So the harmonic series ($p=1$) **diverges**, while $\sum 1/n^2$ converges. (This benchmark is what every other test secretly compares against.)

## 4. Kummer's Test (the general machine)

**Rule (simple):** pick any positive sequence $b_n$ of your choice and form
$$K=\lim_{n\to\infty}\left(b_n\,\frac{a_n}{a_{n+1}}-b_{n+1}\right).$$
- $K>0\ \Rightarrow\ \sum a_n$ **converges**.
- $K<0$ **and** $\sum\frac{1}{b_n}$ diverges $\ \Rightarrow\ \sum a_n$ **diverges**.

It's a "machine" because choosing $b_n$ recovers the other tests:

| choice of $b_n$ | test you get |
|---|---|
| $b_n=1$ | (a form of the) ratio test |
| $b_n=n$ | **Raabe's test** |
| $b_n=n\ln n$ | Bertrand's test |

**Raabe's test** (the practically important special case, $b_n=n$):
$$R=\lim_{n\to\infty} n\left(\frac{a_n}{a_{n+1}}-1\right),\qquad R>1\Rightarrow\text{converges},\ \ R<1\Rightarrow\text{diverges},\ \ R=1\Rightarrow\text{inconclusive}.$$

**Example:** $\displaystyle\sum\frac{(2n-1)!!}{(2n)!!}$. Ratio $\dfrac{a_{n+1}}{a_n}=\dfrac{2n+1}{2n+2}\to1$ — ratio test **fails**. Raabe: $n\!\left(\dfrac{2n+2}{2n+1}-1\right)=\dfrac{n}{2n+1}\to\dfrac12<1$ → **diverges**.

## 5. Gauss's Test (never inconclusive)

**Rule (simple):** when the ratio is a rational function of $n$, expand it as
$$\frac{a_n}{a_{n+1}}=1+\frac{h}{n}+\frac{B(n)}{n^{2}}\quad(B(n)\ \text{bounded}).$$
$$\boxed{h>1\ \Rightarrow\ \text{converges};\qquad h\le 1\ \Rightarrow\ \text{diverges}.}$$
There is **no $h=1$ loophole** — Gauss resolves exactly the case that defeats Raabe ($R=1$ corresponds to $h=1$, and Gauss declares it divergent).

**Example:** $\displaystyle\sum\left[\frac{(2n-1)!!}{(2n)!!}\right]^{2}$. Here $\dfrac{a_n}{a_{n+1}}=\left(\dfrac{2n+2}{2n+1}\right)^{2}=1+\dfrac{1}{n}+O\!\left(\dfrac{1}{n^2}\right)$, so $h=1\le1$ → **diverges** (the term behaves like $\tfrac{1}{\pi n}$). For the **cube** $\left[\tfrac{(2n-1)!!}{(2n)!!}\right]^3$ you'd get $h=\tfrac32>1$ → converges.

---

## Decision strategy (how to actually pick)

| situation | reach for |
|---|---|
| term has an $n$-th power, e.g. $(\cdots)^n$ | **root** |
| term has factorials / $r^n$ | **ratio** |
| term $=f(n)$, $f$ nice & decreasing ($p$-series, $1/(n\ln n)$) | **integral** |
| ratio/root gave $L=1$ | **Raabe** |
| Raabe gave $R=1$, or it's a hypergeometric-type ratio | **Gauss** |

## Key facts to keep ready

- Root is **stronger** than ratio: whenever the ratio limit exists and decides, the root test gives the *same* answer — but the root test can also work when the ratio oscillates. (Rigorously, both use $\limsup$.)
- Ratio and root only ever prove **absolute** convergence. For alternating series at the boundary, they're blind — use Leibniz.
- $\sum \frac{1}{n^p}$ converges $\iff p>1$; $\sum \frac{1}{n(\ln n)^p}$ converges $\iff p>1$. These two are your comparison anchors.

## Tricky spots where marks are lost

1. **Direction flip in Raabe.** Ratio test: $L<1$ converges. Raabe: $R>\mathbf{1}$ converges. People carry over "less than 1 = good" and get it backwards.
2. **$L=1$ is genuinely inconclusive** — *both* $\sum 1/n$ (diverges) and $\sum 1/n^2$ (converges) give ratio/root limit $=1$. You **must** escalate; never conclude from $L=1$.
3. **Integral test needs *decreasing*.** Positivity and continuity alone aren't enough.
4. **Gauss boundary: $h=1$ means DIVERGES**, not converges. The single most common Gauss error.
5. **Kummer's divergence half needs the extra hypothesis** $\sum 1/b_n$ diverges. Skipping it invalidates the divergence conclusion.
6. These tests certify convergence, **not** the value. And on an alternating series, a "convergent" verdict from ratio/root means *absolutely* convergent — a divergent verdict there doesn't rule out *conditional* convergence.

## Where NET/JRF tests this

- **Radius of convergence** (your notes Q71, Q95): the engine is the ratio/root test.
- **$p$-series / harmonic divergence**: integral test — surfaces in partition functions, sums over states, and the Riemann $\zeta$-function.
- **Hypergeometric series convergence** (your notes Q73, ${}_2F_1$): the boundary case at $|z|=1$ is decided by **Gauss's test** — the classic result that ${}_2F_1(a,b;c;1)$ converges iff $c-a-b>0$.

---

## Practice problems (with full solutions)

**Q1.** *(Ratio)* Test $\displaystyle\sum_{n=1}^{\infty}\frac{n^{2}}{2^{n}}$.

> $\dfrac{a_{n+1}}{a_n}=\dfrac{(n+1)^2}{2^{n+1}}\cdot\dfrac{2^n}{n^2}=\dfrac12\left(\dfrac{n+1}{n}\right)^2\to\dfrac12<1$ → **converges**.

**Q2.** *(Root)* Test $\displaystyle\sum_{n=1}^{\infty}\left(\frac{2n+1}{3n+2}\right)^{n}$.

> $\sqrt[n]{a_n}=\dfrac{2n+1}{3n+2}\to\dfrac23<1$ → **converges**.

**Q3.** *(Radius of convergence — ratio)* Find $R$ for $\displaystyle\sum\frac{x^{n}}{n!}$.

> $\left|\dfrac{c_n}{c_{n+1}}\right|=\dfrac{(n+1)!}{n!}=n+1\to\infty$ → $\boxed{R=\infty}$ (converges for all $x$ — it's $e^x$).

**Q4.** *(Radius of convergence — ratio)* Find $R$ for $\displaystyle\sum n!\,x^{n}$.

> $\left|\dfrac{c_n}{c_{n+1}}\right|=\dfrac{n!}{(n+1)!}=\dfrac{1}{n+1}\to0$ → $\boxed{R=0}$ (converges only at $x=0$).

**Q5.** *(Radius — central binomial, NET favourite)* Find $R$ for $\displaystyle\sum\frac{(2n)!}{(n!)^{2}}\,x^{n}$.

> $\dfrac{c_n}{c_{n+1}}=\dfrac{(2n)!/(n!)^2}{(2n+2)!/((n+1)!)^2}=\dfrac{(n+1)^2}{(2n+2)(2n+1)}=\dfrac{n+1}{2(2n+1)}\to\dfrac14$ → $\boxed{R=\tfrac14}$.

**Q6.** *(Integral)* For which $p$ does $\sum\frac{1}{n^p}$ converge, and does $\sum\frac{1}{n\ln n}$ converge?

> $p$-series: $\int_1^\infty x^{-p}dx$ finite iff $p>1$ → **converges iff $p>1$.** For $\sum\frac{1}{n\ln n}$: substitute $u=\ln x$, $\int \frac{dx}{x\ln x}=\ln(\ln x)\to\infty$ → **diverges** (just barely).

**Q7.** *(Ratio fails → Raabe)* Test $\displaystyle\sum\frac{(2n-1)!!}{(2n)!!}$.

> Ratio $=\dfrac{2n+1}{2n+2}\to1$ (inconclusive). Raabe: $n\!\left(\dfrac{2n+2}{2n+1}-1\right)=\dfrac{n}{2n+1}\to\dfrac12<1$ → **diverges**.

**Q8.** *(Gauss)* Test $\displaystyle\sum\left[\frac{(2n-1)!!}{(2n)!!}\right]^{2}$, then state the verdict for the cube.

> $\dfrac{a_n}{a_{n+1}}=\left(\dfrac{2n+2}{2n+1}\right)^2=1+\dfrac{1}{n}+O\!\left(\tfrac1{n^2}\right)$, so $h=1\le1$ → **square diverges**. For the cube, $\left(\tfrac{2n+2}{2n+1}\right)^3=1+\tfrac{3}{2n}+\cdots$, $h=\tfrac32>1$ → **cube converges**.

**Q9.** *(Why $L=1$ is useless — conceptual)* Apply the ratio test to both $\sum\frac1n$ and $\sum\frac1{n^2}$. What does the result teach?

> Both give $\dfrac{a_{n+1}}{a_n}\to1$. Yet $\sum\frac1n$ **diverges** and $\sum\frac1{n^2}$ **converges**. Lesson: $L=1$ carries *zero* information — you must switch to Raabe/Gauss or the integral test.

**Q10.** *(Kummer → Raabe)* Show that choosing $b_n=n$ in Kummer's test reproduces Raabe's test.

> Kummer: $K=\lim\!\big(b_n\tfrac{a_n}{a_{n+1}}-b_{n+1}\big)=\lim\!\big(n\tfrac{a_n}{a_{n+1}}-(n+1)\big)=\lim\!\big[n(\tfrac{a_n}{a_{n+1}}-1)-1\big]=R-1.$ So $K>0\iff R>1$ (converge) and $K<0\iff R<1$; and $\sum\frac1{b_n}=\sum\frac1n$ diverges, satisfying Kummer's divergence hypothesis automatically. ∎

**Q11.** *(Gauss on the hypergeometric series — directly relevant to your Q73)* For ${}_2F_1(a,b;c;z)=\sum\frac{(a)_n(b)_n}{(c)_n\,n!}z^n$ at $z=1$, find the convergence condition.

> Term ratio: $\dfrac{u_n}{u_{n+1}}=\dfrac{(n+1)(c+n)}{(a+n)(b+n)}=\dfrac{n^2+(c+1)n+c}{n^2+(a+b)n+ab}=1+\dfrac{\,c+1-a-b\,}{n}+O\!\left(\tfrac1{n^2}\right).$ So $h=c+1-a-b$. Gauss: converges iff $h>1$, i.e.
> $$\boxed{c-a-b>0.}$$
> This is the classic Gauss result for ${}_2F_1$ at the boundary $z=1$.

**Q12.** *(Boundary blindness of ratio test)* Does the ratio test settle $\sum\frac{(-1)^{n}}{n}$? What is the true behaviour?

> Ratio of absolute values $\to1$ — the ratio test says **nothing**. The series **converges conditionally** by the Leibniz (alternating series) test, though $\sum\frac1n$ diverges, so it is *not* absolutely convergent. Moral: ratio/root only see absolute convergence.

---

Notice that Q5, Q8, and Q11 all funnel into the same NET pattern — convergence of the standard physics special-function series — which is exactly why the syllabus pairs these tests together.

Want a quick visual of the test-selection ladder, or shall we move to the next topic?


---

### [7] **You** - 2026-06-19 05:40:37

alternating series


---

### [8] **Claude** - 2026-06-19 05:42:37

> **File attached:** `1.Mathematical Physics_NETJRF 1.pdf`

> **File attached:** `1.Mathematical Physics_NETJRF 1.pdf`

<details><summary>Claude's thinking</summary>

I need to structure an explanation of alternating series following a specific format: starting with a simple mathematical explanation, then working through an example, key facts, common pitfalls and exam-related issues, and finally providing over ten problems with solutions. Let me first look into how alternating series are covered in the existing material and check for any relevant past-exam questions.

</details>

*Searched project knowledge: `alternating series Leibniz test conditional absolute convergence (-1)^n`*

<details><summary>Claude's thinking</summary>

I notice the project knowledge doesn't have a dedicated worked example on alternating series, but this connects directly to the convergence tests I just reviewed—particularly the conditional convergence subtlety from the previous material. The NET/JRF relevance centers on classic alternating series like the Leibniz series for ln 2 and π/4, plus how they behave at the radius of convergence for Taylor series, and the important Riemann rearrangement theorem. Now I'm structuring a comprehensive response following the established format for alternating series.

The core definition is a series whose terms alternate in sign. The Leibniz test gives the convergence criterion: the terms must be monotonically decreasing and approach zero—both conditions are essential. What makes this particularly useful is the error bound: when the test conditions hold, the error between the partial sum and the true sum is bounded by the first omitted term, which gives a practical way to estimate accuracy and shows the sum lies between consecutive partial sums.

Now I'm distinguishing between absolute and conditional convergence. A series converges absolutely if the series of absolute values converges, which guarantees the original series converges too. But conditional convergence is trickier—the series itself converges while the absolute value series diverges, like the alternating harmonic series summing to ln 2. This distinction matters because of the Riemann Rearrangement Theorem: conditionally convergent series can be rearranged to sum to any real number or infinity, whereas absolutely convergent series always sum to the same value no matter how you rearrange them. This is a classic conceptual question on exams.

I'm working through some key examples—the alternating harmonic series and the Leibniz series for π/4 are both conditionally convergent, while the alternating series of reciprocal squares converges absolutely since the p-series with p=2 converges. I'm verifying the π²/12 result using the Dirichlet eta function and its relationship to the Riemann zeta function.

For the general alternating p-series, the pattern is clear: when p > 1 it's absolutely convergent, for 0 < p ≤ 1 it's conditionally convergent (the terms decrease to zero so the alternating test applies, but the underlying p-series diverges), and for p ≤ 0 the terms don't approach zero so it diverges outright. This gives a nice framework for classifying convergence behavior.

Now looking at some common pitfalls — the Leibniz test requires both conditions: the terms must go to zero AND be monotone decreasing. It's easy to forget the monotonicity part, and there are indeed alternating series where the terms approach zero but aren't monotone, and these can diverge. I'm trying to construct a clean counterexample to illustrate this trap, something where the non-monotonicity causes the series to fail despite having terms that vanish. ternating series diverges is when the terms go to zero but aren't monotone decreasing. The classic example is something like $\sum (-1)^n a_n$ where $a_n = \frac{1}{\sqrt{n}} + \frac{(-1)^n}{n}$, which fails the alternating series test because the sequence isn't monotone. The alternating harmonic series $\frac{1}{1} - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$ works fine precisely because it is monotone decreasing.

Now here's a concrete trap example: a series where odd-indexed terms are $\frac{1}{2k-1}$ and even-indexed terms are $-\frac{1}{(2k)^2}$. The individual terms go to zero, but the odd terms form a divergent harmonic-like series while the even terms form a convergent series. When I group them into partial sums, the divergent part dominates and the whole series blows up to infinity, even though the terms vanish. This happens precisely because the sequence isn't monotone—it oscillates in a way that violates the alternating series test conditions. The magnitudes don't decrease monotonically, so the alternating series test doesn't apply and the series diverges. I'm also noting some key conceptual traps: confusing convergence with absolute convergence, incorrectly rearranging terms as if the series were absolutely convergent, misapplying error bounds when Leibniz conditions fail, and overlooking that ratio and root tests have their own limitations.

I should also watch for sign conventions with $(-1)^n$ versus $(-1)^{n-1}$, which affect the sum's sign but not convergence itself. And grouping or bracketing terms in conditionally convergent or divergent series can artificially change the apparent value — like how $1 - 1 + 1 - 1 + \cdots$ can be manipulated to equal 0 or 1 depending on how you parenthesize it.

For exam purposes, I need to be solid on conditional versus absolute classification, and recognize how the Leibniz test and Gregory series for $\pi/4$ and the $\ln 2$ series show up in power series expansions. At the radius of convergence boundary, the series often becomes alternating, so I test endpoint behavior with the Leibniz criterion — like how $\ln(1+x)$ at $x=1$ gives the $\ln 2$ series (converges) but at $x=-1$ gives the harmonic series (diverges). The Riemann rearrangement theorem is worth understanding conceptually, and I should be comfortable estimating errors for alternating series.

Now I'm setting up a problem set with a dozen or more questions and solutions, starting with basic Leibniz tests like whether $\sum (-1)^{n-1}/n$ converges and whether it's conditional or absolute.

Q2 asks me to classify $\sum (-1)^{n-1}/n^2$ as absolutely convergent. Q3 generalizes this to $\sum (-1)^{n-1}/n^p$ and asks how convergence depends on $p$. For Q4, I'm finding how many terms of the alternating harmonic series I need to approximate within 0.01 — the error bound tells me the $(N+1)$-th term must be less than 0.01, so $1/(N+1) < 0.01$ means $N \geq 100$. Q5 tests the divergence test on $\sum (-1)^n \frac{n}{n+1}$, where the terms approach 1 instead of 0, so it diverges. Q6 emphasizes that monotonicity is essential for the Leibniz test, and Q7 continues building out the problem set.

Now for rearrangements: the alternating harmonic series can be rearranged to converge to 5 because it's only conditionally convergent, but $\sum (-1)^{n-1}/n^2$ cannot be rearranged arbitrarily since it converges absolutely. Q8 applies the Leibniz test to $\sum (-1)^n \frac{1}{\ln n}$ — the terms decrease to 0, so it converges by Leibniz, but $\sum 1/\ln n$ diverges (since $1/\ln n$ dominates $1/n$), making this series conditionally convergent. Q9 notes that the Taylor series for $\ln(1+x) = \sum (-1)^{n-1} x^n/n$ has radius of convergence 1.

At the endpoints, I need to check convergence at $x=1$ and $x=-1$. Q10 connects this to the known result that $\sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} = \ln 2$, which comes directly from evaluating the series at $x=1$. Q11 is a fundamental principle: absolute convergence implies convergence, so if $\sum |a_n|$ converges then $\sum a_n$ must converge. Q12 looks at a trickier case with $\sum \frac{(-1)^n}{n + (-1)^n}$ for $n \geq 2$ — the terms behave roughly like $(-1)^n/n$ with a small correction, making this a subtle convergence question.

Actually, I'll use the cleaner example $\sum \frac{(-1)^n}{\sqrt{n}}$ instead, which converges conditionally since $1/\sqrt{n}$ decreases to zero but $\sum 1/\sqrt{n}$ diverges (p-series with $p = 1/2 < 1$). Q13 is a bonus on the Abel grouping trap: the series $1 - 1 + 1 - 1 + \cdots$ shows why different groupings can yield different sums. I should also include the famous rearrangement of the alternating harmonic series that produces $\frac{3}{2}\ln 2$ — a concrete example of how rearranging conditionally convergent series changes their sum.

Now checking Q8: for $\sum_{n=2}^\infty \frac{(-1)^n}{\ln n}$, the terms $1/\ln n$ decrease to zero, so the alternating series test confirms convergence. But since $\ln n < n$, we have $1/\ln n > 1/n$, and since the harmonic series diverges, so does $\sum 1/\ln n$. This is conditional convergence. For Q9, I'm working with the Taylor series for $\ln(1+x)$, which is $\sum_{n=1}^\infty (-1)^{n-1} \frac{x^n}{n}$.

At $x = 1$, this gives the alternating harmonic series which converges to $\ln 2$. At $x = -1$, the series becomes $-\sum 1/n$, which diverges. For Q12, $\sum_{n=1}^\infty \frac{(-1)^n}{\sqrt{n}}$ converges by the alternating series test since $1/\sqrt{n}$ decreases to zero, but $\sum 1/\sqrt{n}$ diverges as a p-series with $p = 1/2 < 1$, so this is also conditional. Now I'm ready to write up the full response with these distinctions clearly marked. why these series converge so slowly and are impractical for computation. I'll organize the response with the core concept, a concrete example, key facts, common pitfalls, a past exam question, and then twelve problems. I'm deciding whether to include a visual of how partial sums bracket the limit in an alternating series—it's a clean illustration of the error bound, but I'll hold off for now and offer it if needed.

</details>

Alternating series is where convergence gets *subtle* — the famous traps (conditional vs absolute, the Riemann rearrangement) live here, and NET/JRF loves the conceptual gotchas. The good news: there's one clean test (Leibniz) and a beautiful error bound that makes these very tractable.

These connect directly to what we just did — the ratio/root tests only see *absolute* convergence, so alternating series are exactly the case where those tests go blind. They also decide the **endpoint behaviour** of Taylor series (e.g. $\ln(1+x)$ at $x=\pm1$), which is a recurring NET theme.

---

## 1. The concept, simply

An **alternating series** has terms that flip sign each step:
$$\sum_{n=1}^{\infty}(-1)^{n-1}a_n = a_1 - a_2 + a_3 - a_4 + \cdots,\qquad a_n>0.$$

**Leibniz Test (the only test you need):** the series converges if **both**
1. $a_n$ is **eventually decreasing** ($a_{n+1}\le a_n$), and
2. $a_n\to 0$.

If $a_n\not\to0$, it diverges immediately (term test). If $a_n\to0$ but is *not* monotone, Leibniz is silent — and the series may actually diverge (see traps).

## 2. Worked example

$\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}=1-\tfrac12+\tfrac13-\tfrac14+\cdots$

Here $a_n=\tfrac1n$: decreasing, and $\to0$. Both conditions hold → **converges** (its value is $\ln 2$). But $\sum\tfrac1n$ diverges, so it does **not** converge absolutely — this is the textbook example of **conditional** convergence.

## 3. The error bound (the practical gem)

When Leibniz conditions hold, the truncation error is at most the **first omitted term**:
$$\boxed{\,|S-S_N|\le a_{N+1}\,}$$
and the true sum always lies *between* two consecutive partial sums (they bracket it from above and below). This single fact answers most "how many terms for accuracy $\epsilon$" questions.

## 4. Absolute vs conditional — and why it matters

- **Absolutely convergent:** $\sum|a_n|$ converges. Then $\sum a_n$ converges too (absolute $\Rightarrow$ ordinary). Safe to rearrange or regroup freely.
- **Conditionally convergent:** $\sum a_n$ converges but $\sum|a_n|$ diverges. **Fragile.**

**Riemann Rearrangement Theorem** (the deep one NET tests conceptually): a *conditionally* convergent series can be rearranged to sum to **any real number** you like (or $\pm\infty$). An *absolutely* convergent series gives the same sum no matter how you reorder. So order matters only in the conditional case.

The clean classification rule — the **alternating $p$-series** $\sum\frac{(-1)^{n-1}}{n^p}$:

| $p$ | behaviour |
|---|---|
| $p>1$ | absolutely convergent |
| $0<p\le 1$ | conditionally convergent |
| $p\le 0$ | diverges (terms don't $\to0$) |

## 5. Famous values to recognise

- $\displaystyle\ln 2 = 1-\tfrac12+\tfrac13-\tfrac14+\cdots$ (conditional)
- $\displaystyle\frac{\pi}{4}=1-\tfrac13+\tfrac15-\tfrac17+\cdots$ (Leibniz–Gregory series, conditional)
- $\displaystyle\frac{\pi^2}{12}=1-\tfrac1{4}+\tfrac19-\cdots=\sum\frac{(-1)^{n-1}}{n^2}$ (absolute)

## 6. Tricky spots where marks are lost

1. **Both Leibniz conditions are required.** Dropping monotonicity is fatal: there exist alternating series with $a_n\to0$ that still **diverge** (Q6 below shows one).
2. **"Converges" ≠ "absolutely converges."** You must check $\sum|a_n|$ separately to classify.
3. **Rearranging a conditional series is illegal** if you want a fixed sum. (The alternating harmonic series can even be rearranged to $\tfrac32\ln2$.)
4. **The error bound $|S-S_N|\le a_{N+1}$ only holds under Leibniz conditions** — don't quote it otherwise.
5. **Grouping/bracketing a divergent series is meaningless:** $1-1+1-1+\cdots$ "equals" $0$ or $1$ depending on how you bracket — proof that it has no sum.
6. **Ratio/root tests are blind here:** they only detect absolute convergence, so a "divergent" verdict from them says nothing about conditional convergence.

## 7. Where NET/JRF tests this

- **Conditional vs absolute classification** of a given series (direct MCQ).
- **Endpoint of a Taylor series:** at $|x|=R$ the series typically becomes alternating, tested with Leibniz — e.g. $\ln(1+x)$ converges at $x=1$ (gives $\ln2$) but diverges at $x=-1$ (harmonic).
- **Riemann rearrangement** as a conceptual question.
- **Truncation-error estimates** for alternating expansions.

---

## 8. Practice problems (with full solutions)

**Q1.** Does $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$ converge? Absolutely or conditionally?

> $a_n=\tfrac1n\downarrow0$ → Leibniz gives **convergence**. But $\sum\tfrac1n$ diverges → **conditionally** convergent.

**Q2.** Classify $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^{2}}$.

> $\sum\tfrac1{n^2}$ converges ($p=2>1$), so the series is **absolutely** convergent (value $\tfrac{\pi^2}{12}$).

**Q3.** For which real $p$ is $\displaystyle\sum\frac{(-1)^{n-1}}{n^{p}}$ absolutely convergent, conditionally convergent, or divergent?

> $p>1$: **absolute**. $0<p\le1$: converges by Leibniz but $\sum n^{-p}$ diverges → **conditional**. $p\le0$: $a_n\not\to0$ → **diverges**.

**Q4.** *(Error bound)* How many terms of $1-\tfrac12+\tfrac13-\cdots$ are needed to approximate $\ln2$ within $0.001$?

> Need first omitted term $a_{N+1}=\tfrac{1}{N+1}<0.001\Rightarrow N+1>1000\Rightarrow \boxed{N\ge1000}$. (Illustrates how *slowly* conditionally convergent series converge — useless for computation.)

**Q5.** *(Term test)* Does $\displaystyle\sum_{n=1}^{\infty}(-1)^{n}\frac{n}{n+1}$ converge?

> $a_n=\tfrac{n}{n+1}\to1\ne0$, so the terms don't vanish → **diverges** (Leibniz never even applies).

**Q6.** *(Monotonicity matters)* Examine $1-\tfrac{1}{4}+\tfrac13-\tfrac{1}{16}+\tfrac15-\tfrac{1}{36}+\cdots$ where odd terms are $\tfrac{1}{2k-1}$ and even terms are $\tfrac{1}{(2k)^2}$.

> Terms $\to0$ but are **not monotone** ($\tfrac14<\tfrac13$), so Leibniz fails. Group: $S_{2N}=\sum_{k=1}^{N}\tfrac{1}{2k-1}-\sum_{k=1}^{N}\tfrac{1}{(2k)^2}$. The first sum diverges, the second converges → $S_{2N}\to\infty$. **Diverges**, despite $a_n\to0$. This is *why* monotonicity is non-negotiable.

**Q7.** *(Rearrangement)* Can $\sum\frac{(-1)^{n-1}}{n}$ be reordered to sum to $5$? Can $\sum\frac{(-1)^{n-1}}{n^2}$?

> First is **conditional** → yes, by Riemann's theorem it can be rearranged to *any* value including 5. Second is **absolute** → no, every rearrangement gives the same $\tfrac{\pi^2}{12}$.

**Q8.** Classify $\displaystyle\sum_{n=2}^{\infty}\frac{(-1)^{n}}{\ln n}$.

> $a_n=\tfrac{1}{\ln n}\downarrow0$ → converges by Leibniz. Since $\ln n<n$, $\tfrac{1}{\ln n}>\tfrac1n$, so $\sum\tfrac1{\ln n}$ diverges → **conditionally** convergent.

**Q9.** *(Taylor endpoint)* The series $\ln(1+x)=\sum_{n=1}^{\infty}(-1)^{n-1}\tfrac{x^n}{n}$ has $R=1$. Test convergence at $x=1$ and $x=-1$.

> At $x=1$: $\sum(-1)^{n-1}\tfrac1n=\ln2$ → **converges** (conditional). At $x=-1$: terms become $-\tfrac1n$, giving $-\sum\tfrac1n$ → **diverges** (consistent with $\ln(1+x)\to-\infty$ as $x\to-1^+$).

**Q10.** Using Q9, evaluate $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}$.

> Set $x=1$ in $\ln(1+x)=\sum(-1)^{n-1}\tfrac{x^n}{n}$: $\;\boxed{\sum_{n=1}^\infty\tfrac{(-1)^{n-1}}{n}=\ln2}$.

**Q11.** *(Conceptual)* Prove that absolute convergence implies convergence.

> If $\sum|a_n|$ converges, then $0\le a_n+|a_n|\le 2|a_n|$, so $\sum(a_n+|a_n|)$ converges by comparison. Hence $\sum a_n=\sum(a_n+|a_n|)-\sum|a_n|$ is a difference of two convergent series → converges. ∎ (The converse fails — conditional series are the counterexamples.)

**Q12.** Classify $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n}}{\sqrt{n}}$.

> $a_n=\tfrac{1}{\sqrt n}\downarrow0$ → converges by Leibniz. But $\sum n^{-1/2}$ diverges ($p=\tfrac12\le1$) → **conditionally** convergent.

**Q13.** *(Grouping trap)* Why can't you assign $1-1+1-1+\cdots$ a value by bracketing?

> Bracketing gives $(1-1)+(1-1)+\cdots=0$, but $1+(-1+1)+(-1+1)+\cdots=1$. Two answers ⟹ the series **diverges** (partial sums oscillate $1,0,1,0,\dots$). Regrouping is only valid for convergent series.

---

The throughline: **Leibniz tells you it converges; the $\sum|a_n|$ check tells you whether that convergence is robust (absolute) or fragile (conditional)** — and fragility is exactly what the rearrangement and endpoint questions exploit.

Want a quick zig-zag visual showing partial sums bracketing the limit (it makes the error bound click), or move to the next topic?
