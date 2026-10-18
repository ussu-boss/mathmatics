# 50 Practice Problems — Part 3 (CSIR‑NET/JRF style)

**Built from problems 21–30 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **101–150** to continue Parts 1–2.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q21–Q29 = Dec 2012**, **Q30 = June 2013** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q21–Q30)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q21 | Series convergence | Harmonic vs $\ln N$; the Euler–Mascheroni constant $\gamma$ |
| Q22 | Expected value | Mean with **non‑uniform** weights $P(k)\propto k$ |
| Q23 | Signal processing | Sampling theorem / Nyquist rate / aliasing |
| Q24 | Vector calculus | $\nabla F$ as the normal to an **ellipsoid** (normalization!) |
| Q25 | Linear algebra | $\det(cA)=c^{n}\det A$; turning $U(n)$ into $SU(n)$ |
| Q26 | Special functions | Recognizing $J_0(x)$ from its graph/behaviour |
| Q27 | Probability | Binomial distribution (coin tosses) |
| Q28 | Series | Maclaurin series of a **composite** function $\ln(\cosh x)$ |
| Q29 | Complex analysis | Residue theorem — only poles **inside** the contour |
| Q30 | Special functions | Hermite generating function; $H_n(0)$ |

---

# SET 21 — Series convergence & the Euler–Mascheroni constant
**Origin (Q21):** $\displaystyle\lim_{N\to\infty}\Big(\sum_{m=1}^N\tfrac1m-\ln N\Big)$ exists ($=\gamma$); the bare harmonic sum diverges. **Twists:** harmonic divergence, $p$‑series, alternating harmonic, $\sum 1/\sqrt m$ asymptotics, $\gamma$ itself.

**Problem 101.** The series $\displaystyle\sum_{m=1}^{\infty}\frac1m$
(a) diverges  (b) converges to $1$  (c) converges to $\gamma$  (d) converges to $\ln 2$
> **Ans (a).** The harmonic series diverges (like $\ln N$). *Trick:* terms $\to 0$ is **not** enough for convergence.

**Problem 102.** $\displaystyle\sum_{m=1}^{\infty}\frac{1}{m^{p}}$ converges for
(a) $p>1$  (b) $p\ge1$  (c) $p>0$  (d) all $p$
> **Ans (a).** A $p$‑series converges **iff** $p>1$. *Trick:* $p=1$ is the divergent harmonic case — the inequality is strict.

**Problem 103.** $\displaystyle\sum_{m=1}^{\infty}\frac{(-1)^{m+1}}{m}$ equals
(a) $\ln 2$  (b) diverges  (c) $\gamma$  (d) $1$
> **Ans (a).** The alternating harmonic series converges (conditionally) to $\ln2$. *Trick:* alternating signs rescue the same terms that diverge without them.

**Problem 104.** As $N\to\infty$, $\displaystyle\sum_{m=1}^{N}\frac{1}{\sqrt m}$ grows like
(a) $2\sqrt N$  (b) $\ln N$  (c) $N$  (d) $\tfrac12\sqrt N$
> **Ans (a).** $\int dx/\sqrt x=2\sqrt x$, so the sum $\sim 2\sqrt N$. *Trick:* this grows **faster** than $\ln N$, so $\sum 1/\sqrt m-\ln N\to\infty$ (Q21's losing option).

**Problem 105.** $\displaystyle\lim_{N\to\infty}\Big(\sum_{m=1}^{N}\frac1m-\ln N\Big)$ equals
(a) $\gamma\approx0.577$  (b) $\ln2$  (c) $e$  (d) $\pi^2/6$
> **Ans (a).** This limit **defines** the Euler–Mascheroni constant. *Trick:* the divergences of $\sum1/m$ and $\ln N$ cancel, leaving the finite $\gamma$.

---

# SET 22 — Expected value with non‑uniform weights
**Origin (Q22):** $P(k)=\dfrac{k}{N(N+1)/2}\Rightarrow\langle k\rangle=\dfrac{2N+1}{3}$ (using $\sum k^2=\tfrac{N(N+1)(2N+1)}{6}$). **Twists:** uniform die, $\langle k^2\rangle$, the uniform formula, the $\sum k^2$ identity, the large‑$N$ limit.

**Problem 106.** The expected value of a single fair six‑sided die is
(a) $\tfrac72$  (b) $3$  (c) $4$  (d) $21$
> **Ans (a).** $\tfrac{1+2+\cdots+6}{6}=\tfrac{21}{6}=\tfrac72$. *Trick:* for a uniform $\{1,\dots,n\}$ the mean is $\tfrac{n+1}{2}$.

**Problem 107.** For the Q22 bag (where $P(k)\propto k$ on $\{1,\dots,N\}$), $\langle k^{2}\rangle=$
(a) $\dfrac{N(N+1)}{2}$  (b) $\dfrac{2N+1}{3}$  (c) $\dfrac{N^2}{3}$  (d) $\dfrac{(N+1)^2}{4}$
> **Ans (a).** $\langle k^2\rangle=\dfrac{\sum k^3}{N(N+1)/2}=\dfrac{[N(N+1)/2]^2}{N(N+1)/2}=\dfrac{N(N+1)}{2}$. *Trick:* it needs $\sum k^3=[N(N+1)/2]^2$, the square of the triangular number.

**Problem 108.** For a discrete **uniform** distribution on $\{1,2,\dots,n\}$, $E[X]=$
(a) $\dfrac{n+1}{2}$  (b) $\dfrac n2$  (c) $\dfrac{2n+1}{3}$  (d) $\dfrac{n(n+1)}{2}$
> **Ans (a).** Average of $1$ through $n$. *Trick:* uniform gives $\tfrac{n+1}{2}$ — **not** Q22's weighted $\tfrac{2N+1}{3}$.

**Problem 109.** $\displaystyle\sum_{k=1}^{n}k^{2}=$
(a) $\dfrac{n(n+1)(2n+1)}{6}$  (b) $\Big[\dfrac{n(n+1)}{2}\Big]^{2}$  (c) $\dfrac{n(n+1)}{2}$  (d) $\dfrac{n^3}{3}$
> **Ans (a).** The sum‑of‑squares formula used throughout Q22. *Trick:* (b) is $\sum k^3$, (c) is $\sum k$ — don't mix them up.

**Problem 110.** For $P(k)\propto k$ on $\{1,\dots,N\}$, the mean $\langle k\rangle$ for large $N$ is approximately
(a) $\dfrac{2N}{3}$  (b) $\dfrac N2$  (c) $N$  (d) $\dfrac N3$
> **Ans (a).** $\tfrac{2N+1}{3}\approx\tfrac{2N}{3}$. *Trick:* the mean sits at **two‑thirds** of the range because larger values are weighted more heavily.

---

# SET 23 — Sampling theorem / Nyquist / aliasing
**Origin (Q23):** a sinusoid at $f_0$ sampled at interval $\tfrac1{2f_0}$ is sampled **exactly at the Nyquist rate** ($f_s=2f_0$). **Twists:** the Nyquist rate, an aliased frequency, the Nyquist frequency, the Fourier line spectrum, the phase ambiguity at Nyquist.

**Problem 111.** To reconstruct a signal whose highest frequency is $f_{\max}$, the minimum sampling rate is
(a) $2f_{\max}$  (b) $f_{\max}$  (c) $\tfrac{f_{\max}}{2}$  (d) $4f_{\max}$
> **Ans (a).** The Nyquist rate is twice the maximum frequency. *Trick:* it's $2f_{\max}$, not $f_{\max}$.

**Problem 112.** A $5\,$kHz sinusoid sampled at $8\,$kHz appears (aliases) at
(a) $3\,$kHz  (b) $5\,$kHz  (c) $8\,$kHz  (d) $13\,$kHz
> **Ans (a).** Alias $=|f_s-f|=|8-5|=3\,$kHz. *Trick:* under‑sampling folds the frequency down into $[0,f_s/2]$.

**Problem 113.** For a sampling rate $f_s$, the highest representable frequency (Nyquist frequency) is
(a) $\tfrac{f_s}{2}$  (b) $f_s$  (c) $2f_s$  (d) $\tfrac{f_s}{4}$
> **Ans (a).** The Nyquist frequency is half the sampling rate. *Trick:* don't confuse the Nyquist **rate** ($2f_{\max}$, a sampling spec) with the Nyquist **frequency** ($f_s/2$, a signal limit).

**Problem 114.** The Fourier transform of $\cos(2\pi f_0 t)$ consists of delta functions at
(a) $\pm f_0$  (b) $f_0$ only  (c) $0$  (d) $\pm2f_0$
> **Ans (a).** A real cosine has spectral lines at **both** $+f_0$ and $-f_0$. *Trick:* the two‑sided spectrum is what Q23's analysis hinges on.

**Problem 115.** A sinusoid sampled **exactly** at the Nyquist rate ($f_s=2f_0$), with arbitrary starting phase, yields a measured amplitude that
(a) can be anything from $0$ to the true amplitude  (b) always equals the true amplitude  (c) is always zero  (d) is doubled
> **Ans (a).** Depending on phase, samples may land on peaks or zero‑crossings. *Trick:* this phase ambiguity is the whole point of Q23 (the "$0\le\bar A\le1\,$V" answer).

---

# SET 24 — Gradient as the normal to a surface (ellipsoid)
**Origin (Q24):** normal to $\tfrac{x^2}{a^2}+\tfrac{y^2}{b^2}+\tfrac{z^2}{c^2}=1$ is $\nabla F=\big(\tfrac{2x}{a^2},\tfrac{2y}{b^2},\tfrac{2z}{c^2}\big)$; the unit normal's denominator is $\sqrt{b^2c^2+c^2a^2+a^2b^2}$, **not** $\sqrt{a^2+b^2+c^2}$. **Twists:** the direction, the sphere case, the $z=f$ case, the correct normalization, the gradient concept.

**Problem 116.** The normal to the ellipsoid $\tfrac{x^2}{a^2}+\tfrac{y^2}{b^2}+\tfrac{z^2}{c^2}=1$ at $(x_0,y_0,z_0)$ is parallel to
(a) $\big(\tfrac{x_0}{a^2},\tfrac{y_0}{b^2},\tfrac{z_0}{c^2}\big)$  (b) $(x_0,y_0,z_0)$  (c) $(a^2x_0,b^2y_0,c^2z_0)$  (d) $(a,b,c)$
> **Ans (a).** $\nabla F$ divides each coordinate by the **square** of its semi‑axis. *Trick:* not radial (that would be the sphere), and the $a^2$ is in the denominator.

**Problem 117.** For the sphere $x^2+y^2+z^2=R^2$, the normal at a point is along
(a) the radial direction $(x,y,z)$  (b) $(1,1,1)$  (c) tangent to the surface  (d) zero
> **Ans (a).** Equal semi‑axes make the normal radial. *Trick:* the ellipsoid normal is **not** radial in general — the sphere is the special case.

**Problem 118.** For a surface written as $z=f(x,y)$, i.e. $F=z-f(x,y)=0$, the normal is
(a) $(-f_x,-f_y,1)$  (b) $(f_x,f_y,1)$  (c) $(f_x,f_y,-1)$  (d) $(f_x,f_y,0)$
> **Ans (a).** $\nabla(z-f)=(-f_x,-f_y,1)$. *Trick:* the $z$‑component is $+1$ and the in‑plane parts carry a minus sign.

**Problem 119.** The correct denominator normalizing the ellipsoid's gradient at $\big(\tfrac a{\sqrt3},\tfrac b{\sqrt3},\tfrac c{\sqrt3}\big)$ is proportional to
(a) $\sqrt{b^2c^2+c^2a^2+a^2b^2}$  (b) $\sqrt{a^2+b^2+c^2}$  (c) $abc$  (d) $a+b+c$
> **Ans (a).** $|\nabla F|\propto\sqrt{\tfrac1{a^2}+\tfrac1{b^2}+\tfrac1{c^2}}=\dfrac{\sqrt{b^2c^2+c^2a^2+a^2b^2}}{abc}$. *Trick:* this is exactly why **all** of Q24's printed options (which use $\sqrt{a^2+b^2+c^2}$) are wrong.

**Problem 120.** At any point, $\nabla F$ is
(a) perpendicular to the level surface $F=$const, pointing toward increasing $F$  (b) tangent to the surface  (c) toward decreasing $F$  (d) parallel to the surface
> **Ans (a).** The gradient is the direction of steepest increase, normal to the level set. *Trick:* it points "uphill," normal to the surface — never tangent.

---

# SET 25 — $\det(cA)=c^{n}\det A$ and $U(n)\to SU(n)$
**Origin (Q25):** from $\det U=e^{i\varphi}$, the matrix $V=e^{-i\varphi/2}U$ has $\det V=(e^{-i\varphi/2})^2 e^{i\varphi}=1$. **Twists:** the scaling identity, the $2\times2$ value, the $3\times3$ root, $|\det U|$ for unitary, the leftover phase.

**Problem 121.** For an $n\times n$ matrix $A$ and scalar $c$, $\det(cA)=$
(a) $c^{n}\det A$  (b) $c\det A$  (c) $c^{2}\det A$  (d) $\det A$
> **Ans (a).** One factor of $c$ pulls out of each of the $n$ rows. *Trick:* the exponent is the **matrix dimension** $n$.

**Problem 122.** If a $2\times2$ matrix has $\det U=e^{i\varphi}$, then $\det\!\big(e^{-i\varphi/2}U\big)=$
(a) $1$  (b) $e^{i\varphi}$  (c) $e^{-i\varphi}$  (d) $e^{i\varphi/2}$
> **Ans (a).** $(e^{-i\varphi/2})^2 e^{i\varphi}=e^{-i\varphi}e^{i\varphi}=1$. *Trick:* with $n=2$, the scalar squares to $e^{-i\varphi}$, cancelling the determinant — this is Q25.

**Problem 123.** For a $3\times3$ unitary $U$ with $\det U=e^{i\varphi}$, the scalar $\lambda$ making $\det(\lambda U)=1$ is
(a) $e^{-i\varphi/3}$  (b) $e^{-i\varphi/2}$  (c) $e^{i\varphi/3}$  (d) $e^{-i\varphi}$
> **Ans (a).** $\lambda^3 e^{i\varphi}=1\Rightarrow\lambda=e^{-i\varphi/3}$. *Trick:* for $3\times3$ it's the **cube** root (Q25 used the square root for $2\times2$).

**Problem 124.** The determinant of a unitary matrix satisfies
(a) $|\det U|=1$  (b) $\det U=1$ always  (c) $\det U$ is real  (d) $\det U=0$
> **Ans (a).** $U^\dagger U=\mathbb1\Rightarrow|\det U|^2=1$. *Trick:* the **modulus** is $1$, but the phase is free — that freedom is precisely the gap between $U(n)$ and $SU(n)$.

**Problem 125.** Writing a $U(2)$ element as (overall phase)$\times$(an $SU(2)$ element), the phase belongs to the group
(a) $U(1)$  (b) $SU(2)$  (c) $SO(2)$  (d) $U(2)$
> **Ans (a).** The determinant‑phase factor is a $U(1)$. *Trick:* $U(2)$ factors into a $U(1)$ phase and an $SU(2)$ "rotation" part.

---

# SET 26 — Recognizing special functions (Bessel $J_0$)
**Origin (Q26):** a curve starting at $1$ and oscillating with **decaying** amplitude is $J_0(x)$. **Twists:** $J_0(0)$, $J_n(0)$ for $n\ge1$, the decay rate, the envelope fingerprint, Bessel's equation.

**Problem 126.** $J_0(0)=$
(a) $1$  (b) $0$  (c) $\infty$  (d) $-1$
> **Ans (a).** The zeroth Bessel function starts at $1$. *Trick:* only $J_0$ is nonzero at the origin.

**Problem 127.** For $n\ge1$, $J_n(0)=$
(a) $0$  (b) $1$  (c) $\infty$  (d) $n$
> **Ans (a).** All higher Bessel functions vanish at the origin. *Trick:* this distinguishes $J_0$ (which is $1$ there) from every $J_{n\ge1}$.

**Problem 128.** For large $x$, $J_n(x)$ decays like
(a) $\dfrac{1}{\sqrt x}$  (b) $\dfrac1x$  (c) $e^{-x}$  (d) a constant
> **Ans (a).** $J_n(x)\sim\sqrt{\tfrac{2}{\pi x}}\cos(\cdots)$. *Trick:* the decay is the slow algebraic $1/\sqrt x$ — **not** exponential.

**Problem 129.** A function that oscillates with an envelope falling as $1/\sqrt x$ is best matched by
(a) $J_0(x)$  (b) $e^{-x}\cos x$  (c) $\cos x$  (d) $\tfrac1x\cos x$
> **Ans (a).** The $1/\sqrt x$ envelope is Bessel's fingerprint. *Trick:* $e^{-x}\cos x$ decays too fast, $\cos x$ not at all, $\tfrac1x\cos x$ too fast and blows up at $0$ — exactly Q26's elimination.

**Problem 130.** $J_0(x)$ is a solution of
(a) $x^{2}y''+xy'+x^{2}y=0$  (b) $y''+y=0$  (c) $y''-y=0$  (d) $xy''+y'=0$
> **Ans (a).** Bessel's equation of order $0$ (the $-n^2$ term vanishes). *Trick:* recognize Bessel's ODE; the order‑$0$ case drops the constant term.

---

# SET 27 — Binomial distribution
**Origin (Q27):** $5$ tosses, $P(3\text{ heads})=\binom53(\tfrac12)^5=\tfrac{5}{16}$. **Twists:** another $k$, all heads, biased coin, the mean, at‑least‑one.

**Problem 131.** In $5$ fair tosses, $P(\text{exactly }4\text{ heads})=$
(a) $\dfrac{5}{32}$  (b) $\dfrac{5}{16}$  (c) $\dfrac1{32}$  (d) $\dfrac1{16}$
> **Ans (a).** $\binom54(\tfrac12)^5=\tfrac{5}{32}$. *Trick:* $\binom54=5$, and the denominator is $2^5=32$.

**Problem 132.** In $5$ fair tosses, $P(\text{all }5\text{ heads})=$
(a) $\dfrac1{32}$  (b) $\dfrac15$  (c) $\dfrac{5}{32}$  (d) $\dfrac1{16}$
> **Ans (a).** $(\tfrac12)^5=\tfrac1{32}$. *Trick:* $\binom55=1$ — a single outcome.

**Problem 133.** A biased coin with $P(\text{H})=\tfrac13$ is tossed $3$ times. $P(\text{exactly }2\text{ heads})=$
(a) $\dfrac29$  (b) $\dfrac19$  (c) $\dfrac49$  (d) $\dfrac13$
> **Ans (a).** $\binom32(\tfrac13)^2(\tfrac23)=3\cdot\tfrac19\cdot\tfrac23=\tfrac{2}{9}$. *Trick:* use $p^2(1-p)$ with the **unequal** $p=\tfrac13$.

**Problem 134.** The mean number of heads in $10$ fair tosses is
(a) $5$  (b) $10$  (c) $2.5$  (d) $\tfrac12$
> **Ans (a).** $E=np=10\cdot\tfrac12=5$. *Trick:* the binomial mean is simply $np$.

**Problem 135.** In $5$ fair tosses, $P(\text{at least one head})=$
(a) $\dfrac{31}{32}$  (b) $\dfrac1{32}$  (c) $\dfrac{5}{32}$  (d) $\dfrac12$
> **Ans (a).** $1-(\tfrac12)^5=\tfrac{31}{32}$. *Trick:* "at least one" = $1-P(\text{none})$, not a direct sum.

---

# SET 28 — Maclaurin series of composite functions
**Origin (Q28):** $\ln(\cosh x)=\tfrac12x^2-\tfrac1{12}x^4+\cdots$ (even function, via $\tfrac{d}{dx}\ln\cosh x=\tanh x$). **Twists:** $\ln(\cos x)$, $e^{\sin x}$, parity, the derivative shortcut, a coefficient.

**Problem 136.** The Maclaurin series of $\ln(\cos x)$ begins
(a) $-\tfrac12x^2-\tfrac1{12}x^4-\cdots$  (b) $\tfrac12x^2-\tfrac1{12}x^4+\cdots$  (c) $-\tfrac12x^2+\tfrac1{12}x^4-\cdots$  (d) $-\tfrac12x^2-\tfrac16x^4-\cdots$
> **Ans (a).** Substitute $\cos x=1-\tfrac{x^2}{2}+\tfrac{x^4}{24}$ into $\ln(1+u)$: both leading coefficients come out negative. *Trick:* $\ln(\cos)$ is the sign‑flipped mirror of Q28's $\ln(\cosh)$.

**Problem 137.** The Maclaurin series of $e^{\sin x}$ to order $x^{2}$ is
(a) $1+x+\tfrac{x^2}{2}+\cdots$  (b) $1+x-\tfrac{x^2}{2}+\cdots$  (c) $1+x+x^2+\cdots$  (d) $x+\tfrac{x^2}{2}+\cdots$
> **Ans (a).** $e^{\sin x}=1+\sin x+\tfrac{\sin^2x}{2}+\cdots=1+x+\tfrac{x^2}{2}+\cdots$. *Trick:* to second order $\sin x\approx x$, so it matches $e^x$ — the cubic term is where they differ.

**Problem 138.** The Maclaurin series of $\ln(\cosh x)$ contains
(a) only even powers of $x$  (b) only odd powers  (c) all powers  (d) only $x^2$
> **Ans (a).** $\cosh$ is even $\Rightarrow\ln(\cosh)$ is even. *Trick:* an even function's series has no odd powers (Q28 had only $x^2,x^4,\dots$).

**Problem 139.** $\dfrac{d}{dx}\big[\ln(\cosh x)\big]=$
(a) $\tanh x$  (b) $\coth x$  (c) $\sinh x$  (d) $\operatorname{sech}x$
> **Ans (a).** $\dfrac{\sinh x}{\cosh x}=\tanh x$. *Trick:* this derivative is the engine of Q28's expansion.

**Problem 140.** In the Maclaurin series of $\ln(\cosh x)$, the coefficient of $x^{2}$ is
(a) $\dfrac12$  (b) $1$  (c) $\dfrac1{12}$  (d) $-\dfrac1{12}$
> **Ans (a).** $\dfrac{f''(0)}{2!}=\dfrac{\operatorname{sech}^2 0}{2}=\dfrac12$. *Trick:* $f''(0)=1$, then divide by $2!$.

---

# SET 29 — Residue theorem (which poles are inside)
**Origin (Q29):** $\displaystyle\oint_{|z|=5/2}\frac{z^3\,dz}{(z-2)(z-3)}$; only $z=2$ is inside, $\operatorname{Res}_{2}=\tfrac{8}{2-3}=-8$, giving $-16\pi i$. **Twists:** both poles, no poles, a single residue, the theorem itself, the inside/outside split.

**Problem 141.** $\displaystyle\oint_{|z|=4}\frac{z^3\,dz}{(z-2)(z-3)}=$
(a) $38\pi i$  (b) $-16\pi i$  (c) $54\pi i$  (d) $0$
> **Ans (a).** Now **both** poles are inside: $\operatorname{Res}_2=-8$, $\operatorname{Res}_3=\tfrac{27}{3-2}=27$; sum $19$, so $2\pi i(19)=38\pi i$. *Trick:* enlarging the contour to $|z|=4$ brings $z=3$ into play.

**Problem 142.** $\displaystyle\oint_{|z|=1}\frac{z^3\,dz}{(z-2)(z-3)}=$
(a) $0$  (b) $2\pi i$  (c) $-16\pi i$  (d) $38\pi i$
> **Ans (a).** Neither pole lies inside $|z|=1$. *Trick:* no enclosed singularity ⇒ Cauchy's theorem gives $0$.

**Problem 143.** The residue of $\dfrac{z^3}{(z-2)(z-3)}$ at $z=3$ is
(a) $27$  (b) $-8$  (c) $8$  (d) $-27$
> **Ans (a).** $\displaystyle\lim_{z\to3}(z-3)f=\dfrac{27}{3-2}=27$. *Trick:* evaluate $\dfrac{z^3}{z-2}$ at $z=3$.

**Problem 144.** For a closed contour $C$ traversed anticlockwise, $\displaystyle\oint_C f\,dz=$
(a) $2\pi i\sum(\text{residues inside }C)$  (b) $\pi i\sum\text{Res}$  (c) $\sum\text{Res}$  (d) $2\pi\sum\text{Res}$
> **Ans (a).** The residue theorem. *Trick:* the factor is $2\pi i$, and only residues **inside** $C$ count.

**Problem 145.** For $\displaystyle\oint_{|z|=2.5}\frac{z^3\,dz}{(z-2)(z-3)}$, which pole(s) contribute?
(a) only $z=2$  (b) only $z=3$  (c) both  (d) neither
> **Ans (a).** $|2|<2.5<|3|$, so only $z=2$ is enclosed. *Trick:* the radius $2.5$ deliberately splits the two poles — the heart of Q29.

---

# SET 30 — Hermite polynomials & generating function
**Origin (Q30):** $\displaystyle\sum_{n}H_n(x)\frac{t^n}{n!}=e^{-t^2+2tx}$; setting $x=0$ gives $e^{-t^2}$, from which $H_4(0)=12$. **Twists:** $H_2(0)$, odd $H_n(0)$, the recurrence, $H_1$, the $x=0$ substitution.

**Problem 146.** $H_2(0)=$
(a) $-2$  (b) $2$  (c) $0$  (d) $1$
> **Ans (a).** From $e^{-t^2}=1-t^2+\cdots$, the $t^2$ coefficient gives $\tfrac{H_2(0)}{2!}=-1\Rightarrow H_2(0)=-2$. *Trick:* the minus sign comes straight from $e^{-t^2}$.

**Problem 147.** $H_3(0)=$
(a) $0$  (b) $-2$  (c) $12$  (d) $-12$
> **Ans (a).** $e^{-t^2}$ has only even powers of $t$, so $H_n(0)=0$ for odd $n$. *Trick:* all odd‑index Hermite polynomials vanish at the origin.

**Problem 148.** Using the recurrence $H_{n+1}=2xH_n-2nH_{n-1}$ with $H_0=1,\,H_1=2x$, $H_2(x)=$
(a) $4x^{2}-2$  (b) $4x^{2}+2$  (c) $2x^{2}-1$  (d) $8x^{3}-12x$
> **Ans (a).** $H_2=2x(2x)-2(1)(1)=4x^2-2$. *Trick:* the physicists' recurrence; (d) is $H_3$.

**Problem 149.** The (physicists') Hermite polynomial $H_1(x)=$
(a) $2x$  (b) $x$  (c) $2x^{2}-1$  (d) $x^{2}-1$
> **Ans (a).** Physicists' convention: $H_1=2x$. *Trick:* the **probabilists'** $\mathrm{He}_1=x$ — Q30's generating function ($e^{2tx-t^2}$) fixes the physicists' version.

**Problem 150.** To compute $H_n(0)$, one sets $x=0$ in the generating function $e^{2tx-t^2}$, obtaining
(a) $e^{-t^{2}}$  (b) $e^{2t}$  (c) $e^{t^{2}}$  (d) $e^{-2t^{2}}$
> **Ans (a).** $x=0$ removes the $2tx$ term. *Trick:* this reduction to $e^{-t^2}$ is the single step that solves Q30.

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: harmonic divergence is hidden by sign or by $p>1$; a weighted mean ($\tfrac{2N+1}{3}$) sits above the uniform mean ($\tfrac{n+1}{2}$); Nyquist **rate** ($2f_{\max}$) vs Nyquist **frequency** ($f_s/2$); the ellipsoid normal normalizes with $\sqrt{b^2c^2+c^2a^2+a^2b^2}$; $\det(cA)=c^n\det A$ (cube root for $3\times3$); Bessel's $1/\sqrt x$ envelope; "at least one" via the complement; $\ln(\cos)$ as the mirror of $\ln(\cosh)$; only **enclosed** poles contribute; odd Hermite vanish at $0$. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 150 problems across the first 30 originals (Q1–Q30).**
