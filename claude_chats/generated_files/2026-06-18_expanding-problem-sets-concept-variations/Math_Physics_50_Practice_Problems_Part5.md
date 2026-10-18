# 50 Practice Problems — Part 5 (CSIR‑NET/JRF style)

**Built from problems 41–50 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **201–250** to continue Parts 1–4.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q41–Q44 = June 2013**, **Q45–Q49 = June 2014**, **Q50 = Dec 2014** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q41–Q50)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q41 | Integration | Parametric differentiation ("Feynman trick") / double‑pole residue |
| Q42 | Integral transforms | Fourier transform of a derivative ($\delta'$, the $ik$ rule) |
| Q43 | Linear algebra | Rank‑1 matrix — eigenvalue **degeneracy** |
| Q44 | Data analysis | Log–log plots & power laws (slope = exponent) |
| Q45 | ODEs | Critically damped (repeated roots); maximum of the solution |
| Q46 | Linear algebra | Hermitian eigenvalues via trace/det shortcuts |
| Q47 | Complex analysis | Residue at a higher‑order pole that **vanishes** |
| Q48 | Special functions | Legendre special values $P_n(\pm1),P_n(0)$ |
| Q49 | Integral transforms | Fourier transform of periodic functions → discrete spectrum |
| Q50 | Vector calculus | Divergence & curl of the position vector $\vec r$ |

---

# SET 41 — Parametric differentiation of integrals
**Origin (Q41):** $\displaystyle\int_0^\infty\frac{dx}{(y^2+x^2)^2}=\frac{\pi}{4y^3}$, obtained by differentiating $\int_0^\infty\frac{dx}{y^2+x^2}=\frac{\pi}{2y}$ with respect to $y$. **Twists:** the base integral, one more differentiation, the method, the residue route, a Gaussian.

**Problem 201.** $\displaystyle\int_0^\infty\frac{dx}{a^2+x^2}=$
(a) $\dfrac{\pi}{2a}$  (b) $\dfrac{\pi}{a}$  (c) $\dfrac{\pi}{2a^2}$  (d) $\dfrac1a$
> **Ans (a).** $\dfrac1a\arctan\dfrac xa\Big|_0^\infty=\dfrac1a\cdot\dfrac\pi2$. *Trick:* the half‑line gives $\pi/2$ (the full line would give $\pi$).

**Problem 202.** $\displaystyle\int_0^\infty\frac{dx}{(y^2+x^2)^3}=$
(a) $\dfrac{3\pi}{16y^5}$  (b) $\dfrac{\pi}{8y^5}$  (c) $\dfrac{\pi}{4y^5}$  (d) $\dfrac{3\pi}{8y^5}$
> **Ans (a).** Differentiate $\dfrac{\pi}{4y^3}$ again: $I_{n+1}=-\dfrac{1}{2ny}\dfrac{dI_n}{dy}$ gives $\dfrac{3\pi}{16y^5}$. *Trick:* iterate the parameter‑differentiation recursion (watch the $\tfrac{1}{2ny}$ factor).

**Problem 203.** The integral $\displaystyle\int_0^\infty\frac{dx}{(y^2+x^2)^2}$ is most easily found by
(a) differentiating $\int_0^\infty\frac{dx}{y^2+x^2}$ with respect to $y$  (b) integration by parts  (c) the substitution $x=y$  (d) partial fractions
> **Ans (a).** Differentiate the known integral with respect to the parameter $y$. *Trick:* this is Feynman's "differentiation under the integral sign," the cleanest route to Q41.

**Problem 204.** By residues, $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{x^2+a^2}=$
(a) $\dfrac{\pi}{a}$  (b) $\dfrac{\pi}{2a}$  (c) $\dfrac{2\pi}{a}$  (d) $\dfrac{\pi i}{a}$
> **Ans (a).** Close in the upper half‑plane; the pole at $x=ia$ has residue $\tfrac{1}{2ia}$, so $2\pi i\cdot\tfrac{1}{2ia}=\tfrac\pi a$. *Trick:* the full line gives $\pi/a$ — twice the half‑line result of Q201.

**Problem 205.** $\displaystyle\int_{-\infty}^{\infty}x^{2}e^{-ax^{2}}\,dx=$
(a) $\dfrac12\sqrt{\dfrac{\pi}{a^3}}$  (b) $\sqrt{\dfrac{\pi}{a}}$  (c) $\sqrt{\dfrac{\pi}{a^3}}$  (d) $\dfrac12\sqrt{\dfrac{\pi}{a}}$
> **Ans (a).** $-\dfrac{d}{da}\sqrt{\dfrac\pi a}=\dfrac12\sqrt{\dfrac{\pi}{a^3}}$. *Trick:* differentiate the Gaussian $\int e^{-ax^2}dx=\sqrt{\pi/a}$ with respect to $a$ to pull down an $x^2$.

---

# SET 42 — Fourier transform of derivatives
**Origin (Q42):** $\mathcal F[\delta'(x)]\propto ik$ — differentiation in $x$ becomes multiplication by $ik$. **Twists:** $\mathcal F[\delta]$, the derivative rule, the second derivative, $\delta''$, the $x$‑multiplication dual.

**Problem 206.** $\mathcal F[\delta(x)]=$
(a) $1$  (b) $ik$  (c) $\delta(k)$  (d) $0$
> **Ans (a).** The delta transforms to a flat (constant) spectrum. *Trick:* a point in $x$ is "everything" in $k$.

**Problem 207.** If $\mathcal F[f(x)]=F(k)$, then $\mathcal F[f'(x)]=$
(a) $ik\,F(k)$  (b) $\dfrac{F(k)}{ik}$  (c) $k^{2}F(k)$  (d) $F'(k)$
> **Ans (a).** Each $x$‑derivative brings a factor $ik$. *Trick:* this rule is exactly why $\mathcal F[\delta']\propto ik$ (Q42).

**Problem 208.** $\mathcal F[f''(x)]=$
(a) $-k^{2}F(k)$  (b) $+k^{2}F(k)$  (c) $ik\,F(k)$  (d) $k\,F(k)$
> **Ans (a).** $(ik)^2=-k^2$. *Trick:* two derivatives give $(ik)^2=-k^2$, not $+k^2$.

**Problem 209.** $\mathcal F[\delta''(x)]\propto$
(a) $-k^{2}$  (b) $ik$  (c) $k^{2}$  (d) $1$
> **Ans (a).** Two derivatives of $\delta$ each contribute $ik$: $(ik)^2=-k^2$. *Trick:* extends Q42's $\delta'\to ik$ to $\delta''\to-k^2$.

**Problem 210.** Multiplication by $x$ in real space corresponds, in $k$‑space, to
(a) a derivative, $i\,\dfrac{dF}{dk}$  (b) multiplication by $ik$  (c) multiplication by $k^{2}$  (d) integration
> **Ans (a).** It's the dual of the derivative rule. *Trick:* $x\leftrightarrow i\,d/dk$ mirrors $d/dx\leftrightarrow ik$.

---

# SET 43 — Rank‑1 matrix: eigenvalue degeneracy
**Origin (Q43):** $A_{ij}=ij$ (so $A=\vec u\,\vec u^{\,T}$ with $\vec u=(1,2,\dots,n)$) has the eigenvalue $0$ with degeneracy $n-1$. **Twists:** the degeneracy, the rank, the count of distinct eigenvalues, the nonzero value, diagonalizability.

**Problem 211.** For the $n\times n$ matrix $A_{ij}=ij$, the eigenvalue $0$ has degeneracy
(a) $n-1$  (b) $n$  (c) $1$  (d) $2$
> **Ans (a).** Rank $1\Rightarrow$ nullity $n-1$. *Trick:* the zero‑eigenspace is everything orthogonal to $\vec u$ — dimension $n-1$.

**Problem 212.** The rank of $A_{ij}=ij$ ($n\times n$) is
(a) $1$  (b) $n$  (c) $n-1$  (d) $0$
> **Ans (a).** Every row is a multiple of $(1,2,\dots,n)$. *Trick:* an outer product $\vec u\,\vec u^{\,T}$ always has rank $1$.

**Problem 213.** The $n\times n$ matrix $A_{ij}=ij$ has how many **distinct** eigenvalues?
(a) $2$  (b) $1$  (c) $n$  (d) $n-1$
> **Ans (a).** Just $0$ (repeated) and one nonzero value. *Trick:* rank‑1 ⇒ exactly two distinct eigenvalues (when the trace is nonzero).

**Problem 214.** The nonzero eigenvalue of $A_{ij}=ij$ ($n\times n$) is
(a) $\dfrac{n(n+1)(2n+1)}{6}$  (b) $n$  (c) $\dfrac{n(n+1)}{2}$  (d) $n^{2}$
> **Ans (a).** It equals the trace $\sum_{i}i^2=\dfrac{n(n+1)(2n+1)}{6}$. *Trick:* the lone nonzero eigenvalue is $|\vec u|^2=\sum i^2$ (e.g. $14$ for $n=3$).

**Problem 215.** Is $A_{ij}=ij$ diagonalizable?
(a) yes — it is real symmetric, so always diagonalizable  (b) no, it is defective  (c) only if $n=2$  (d) no, the zero eigenvalue lacks enough eigenvectors
> **Ans (a).** Symmetric matrices are always diagonalizable. *Trick:* a degenerate eigenvalue is **not** the same as a defective one — the zero eigenspace is a full $(n-1)$ dimensions.

---

# SET 44 — Log–log plots & power laws
**Origin (Q44):** on a log–log plot, $y=x^m$ is a straight line of slope $m$; the three data sets have slopes $-\tfrac12,\,1,\,2$ ($\tfrac1{\sqrt x},x,x^2$). **Twists:** slope = exponent, a negative slope, the semi‑log distinction, the intercept, reading set A.

**Problem 216.** On a log–log plot, a straight line of slope $2$ corresponds to
(a) $y\propto x^{2}$  (b) $y\propto 2x$  (c) $y\propto e^{2x}$  (d) $y\propto\log x$
> **Ans (a).** Slope = power. *Trick:* a straight log–log line **is** a power law; the slope is the exponent.

**Problem 217.** A log–log line with slope $-1$ represents
(a) $y\propto\dfrac1x$  (b) $y\propto-x$  (c) $y\propto x$  (d) $y\propto e^{-x}$
> **Ans (a).** Slope $-1\Rightarrow$ inverse proportionality. *Trick:* a negative slope is a negative exponent, not a negative coefficient.

**Problem 218.** An exponential $y=e^{kx}$ appears as a straight line on
(a) a semi‑log plot ($\log y$ vs linear $x$)  (b) a log–log plot  (c) a linear plot  (d) no plot
> **Ans (a).** $\log y=kx$ is linear in $x$. *Trick:* exponentials linearize on **semi‑log**; only power laws linearize on log–log.

**Problem 219.** On a log–log plot of $y=Cx^{m}$, the intercept (at $x=1$) gives
(a) $\log C$  (b) the exponent $m$  (c) zero  (d) $C\cdot m$
> **Ans (a).** At $x=1$, $\log y=\log C$. *Trick:* slope encodes the exponent $m$; the intercept encodes the coefficient $C$.

**Problem 220.** Q44's data set A is a downward line of slope $-\tfrac12$; its form is
(a) $x^{-1/2}$  (b) $x^{1/2}$  (c) $x^{-2}$  (d) $-\tfrac x2$
> **Ans (a).** Slope $-\tfrac12\Rightarrow y\propto x^{-1/2}=\dfrac1{\sqrt x}$. *Trick:* directly reads off Q44's set A.

---

# SET 45 — Critically damped ODE (repeated roots) & its maximum
**Origin (Q45):** $\ddot x+2\dot x+x=0,\ x(0)=0,\ \dot x(0)=1\Rightarrow x=te^{-t}$, peaking at $t=1$. **Twists:** the repeated‑root form, the damping class, the maximum location, an underdamped contrast, the peak value.

**Problem 221.** The general solution of $\ddot x+2\dot x+x=0$ is
(a) $(c_1+c_2t)e^{-t}$  (b) $c_1e^{-t}+c_2e^{t}$  (c) $c_1\cos t+c_2\sin t$  (d) $c_1e^{-t}+c_2e^{-2t}$
> **Ans (a).** $(m+1)^2=0$ gives a repeated root $m=-1$. *Trick:* a double root introduces the extra factor of $t$.

**Problem 222.** With characteristic equation $(m+1)^2=0$, the system is
(a) critically damped  (b) underdamped  (c) overdamped  (d) undamped
> **Ans (a).** Equal real roots = critical damping. *Trick:* it sits exactly at the boundary between over‑ and under‑damped.

**Problem 223.** For $x=te^{-t}$, the maximum occurs at $t=$
(a) $1$  (b) $0$  (c) $\tfrac12$  (d) $e$
> **Ans (a).** $\dot x=e^{-t}(1-t)=0$ at $t=1$. *Trick:* this is Q45 — the peak of $te^{-t}$.

**Problem 224.** The equation $\ddot x+2\dot x+5x=0$ describes a system that is
(a) underdamped (oscillatory decay)  (b) critically damped  (c) overdamped  (d) undamped
> **Ans (a).** Roots $-1\pm2i$ (discriminant $4-20<0$). *Trick:* complex roots ⇒ oscillation — unlike Q45's critical case.

**Problem 225.** For $x=te^{-t}$, the maximum value of $x$ is
(a) $\dfrac1e$  (b) $1$  (c) $e$  (d) $\dfrac12$
> **Ans (a).** $x(1)=1\cdot e^{-1}=\tfrac1e$. *Trick:* plug the peak time $t=1$ back in.

---

# SET 46 — Hermitian eigenvalues via trace/det shortcuts
**Origin (Q46):** the Hermitian $M=\begin{pmatrix}0&2i&3i\\-2i&0&6i\\-3i&-6i&0\end{pmatrix}$ has eigenvalues $-7,0,7$ (trace $0$, $\det 0$, $\operatorname{Tr}M^2=98$). **Twists:** real eigenvalues, the trace, eigenvalues from $\operatorname{Tr}M^2$, $\det=0\Rightarrow$ a zero eigenvalue, the full Q46.

**Problem 226.** The eigenvalues of a Hermitian matrix are
(a) real  (b) imaginary  (c) complex‑conjugate pairs  (d) on the unit circle
> **Ans (a).** Hermiticity forces a real spectrum. *Trick:* this is the property that makes Q46 solvable with real arithmetic.

**Problem 227.** For Q46's matrix (all diagonal entries $0$), the sum of the eigenvalues is
(a) $0$  (b) $7$  (c) $-7$  (d) $14$
> **Ans (a).** Trace $=\sum\lambda=0$. *Trick:* a zero diagonal forces the eigenvalues to balance to zero.

**Problem 228.** A $2\times2$ Hermitian matrix has trace $0$ and $\operatorname{Tr}(M^{2})=8$. Its eigenvalues are
(a) $2,\,-2$  (b) $0,\,8$  (c) $4,\,-4$  (d) $\sqrt8,\,0$
> **Ans (a).** $\lambda_1=-\lambda_2$ and $2\lambda_1^2=8\Rightarrow\lambda=\pm2$. *Trick:* trace $0$ makes them $\pm\lambda$; then $\operatorname{Tr}(M^2)=\sum\lambda^2$ pins $\lambda$.

**Problem 229.** A $3\times3$ Hermitian matrix with $\det M=0$ must have
(a) at least one zero eigenvalue  (b) all eigenvalues zero  (c) complex eigenvalues  (d) trace zero
> **Ans (a).** $\det=\prod\lambda=0$ forces some $\lambda=0$. *Trick:* this is why Q46's middle eigenvalue is exactly $0$.

**Problem 230.** Q46's matrix $M$ has eigenvalues
(a) $-7,\,0,\,7$  (b) $-5,\,-2,\,7$  (c) $-4i,\,2i,\,2i$  (d) $2,\,3,\,6$
> **Ans (a).** Trace $0$ (so $\pm\alpha,0$) and $\operatorname{Tr}(M^2)=2(2^2+3^2+6^2)=98=2\alpha^2\Rightarrow\alpha=7$. *Trick:* combine trace $0$, $\det 0$, and $\sum\lambda^2=\operatorname{Tr}M^2$ to nail $\pm7$.

---

# SET 47 — Residues at higher‑order poles (vanishing residue)
**Origin (Q47):** $\displaystyle\oint_{|z|=1/2}\frac{dz}{\sin^2z}=0$ because $\dfrac{1}{\sin^2z}=\dfrac{1}{z^2}+\dfrac13+\cdots$ has **no** $1/z$ term. **Twists:** even‑function residue, residue of $1/z^2$, residue of $\cot z$, the pole order, the integral.

**Problem 231.** The residue of $\dfrac{1}{\sin^2 z}$ at $z=0$ is
(a) $0$  (b) $1$  (c) $\infty$  (d) $\tfrac13$
> **Ans (a).** $1/\sin^2z$ is **even**, so its Laurent series has no odd powers — no $1/z$ term. *Trick:* even functions have zero residue, regardless of pole order.

**Problem 232.** The residue of $\dfrac{1}{z^{2}}$ at $z=0$ is
(a) $0$  (b) $1$  (c) $\infty$  (d) $2$
> **Ans (a).** The residue is the coefficient of $1/z$, which is $0$ here. *Trick:* "has a pole" ≠ "has a residue" — a pure $1/z^2$ pole contributes nothing to the integral.

**Problem 233.** The residue of $\cot z=\dfrac{\cos z}{\sin z}$ at $z=0$ is
(a) $1$  (b) $0$  (c) $-1$  (d) $\tfrac13$
> **Ans (a).** Simple pole; $\cot z=\tfrac1z-\tfrac z3-\cdots$. *Trick:* $\cot z$ has residue $1$ — contrast with $1/\sin^2z$ (even, residue $0$).

**Problem 234.** The function $\dfrac{1}{\sin^2 z}$ has a pole at $z=0$ of order
(a) $2$  (b) $1$  (c) $3$  (d) $\infty$
> **Ans (a).** $\sin z\sim z\Rightarrow\sin^2z\sim z^2$. *Trick:* it's an order‑2 pole — yet still with zero residue (Q47's subtlety).

**Problem 235.** $\displaystyle\oint_{|z|=1/2}\frac{dz}{\sin^2 z}=$
(a) $0$  (b) $2\pi i$  (c) $\pi i$  (d) $\infty$
> **Ans (a).** A double pole is enclosed, but its residue is $0$. *Trick:* an enclosed singularity does not guarantee a nonzero integral — exactly Q47.

---

# SET 48 — Legendre special values
**Origin (Q48):** $P_5(-1)=(-1)^5=-1$. **Twists:** even index at $-1$, value at $+1$, value at $0$, the parity relation, a quick orthogonality integral.

**Problem 236.** $P_4(-1)=$
(a) $1$  (b) $-1$  (c) $0$  (d) $\tfrac12$
> **Ans (a).** Even index $\Rightarrow P_n(-1)=+1$. *Trick:* the sign is $(-1)^n$, so even $n$ gives $+1$.

**Problem 237.** For all $n$, $P_n(1)=$
(a) $1$  (b) $(-1)^n$  (c) $0$  (d) $n$
> **Ans (a).** Every Legendre polynomial equals $1$ at $x=1$. *Trick:* this normalization is fixed for all $n$.

**Problem 238.** $P_5(0)=$
(a) $0$  (b) $-1$  (c) $1$  (d) $\tfrac58$
> **Ans (a).** Odd‑index Legendre polynomials are odd ⇒ vanish at $x=0$. *Trick:* parity — not the $(-1)^n$ rule, which applies at $x=-1$.

**Problem 239.** $P_n(-x)=$
(a) $(-1)^{n}P_n(x)$  (b) $P_n(x)$  (c) $-P_n(x)$  (d) $P_n(x)+1$
> **Ans (a).** The Legendre parity relation. *Trick:* this is the source of $P_n(-1)=(-1)^n$ (Q48).

**Problem 240.** $\displaystyle\int_{-1}^{1}P_5(x)\,dx=$
(a) $0$  (b) $\dfrac{2}{11}$  (c) $1$  (d) $-1$
> **Ans (a).** $\int P_5\,dx=\int P_5\,P_0\,dx=0$ by orthogonality. *Trick:* any $P_{n\ge1}$ is orthogonal to the constant $P_0$.

---

# SET 49 — Fourier transform of periodic functions
**Origin (Q49):** $\mathcal F[A\cos k_0x]=\dfrac A2\big[\delta(k-k_0)+\delta(k+k_0)\big]$ — two symmetric spikes; a real even function has a real even spectrum. **Twists:** cosine, sine, periodic ⇒ discrete, the Hermitian symmetry, the spike weight.

**Problem 241.** The Fourier transform of $\cos(k_0 x)$ consists of
(a) two deltas at $\pm k_0$  (b) one delta at $k_0$  (c) a continuous band  (d) a single peak at $0$
> **Ans (a).** A pure tone → two symmetric spectral lines. *Trick:* the real cosine's spectrum is two‑sided (Q49).

**Problem 242.** The Fourier transform of $\sin(k_0 x)$ is
(a) purely imaginary and antisymmetric in $k$  (b) purely real and symmetric  (c) a single delta  (d) zero
> **Ans (a).** $\sin$ is real and **odd**, so its transform is imaginary and odd. *Trick:* the contrast with cosine (real, even spectrum) is the whole point.

**Problem 243.** The Fourier transform of any periodic function is
(a) discrete (a sum of deltas at harmonics)  (b) a smooth continuum  (c) a single delta  (d) zero
> **Ans (a).** Periodicity ⇒ a discrete line spectrum. *Trick:* periodic in $x$ ⇒ spiky in $k$ (Fourier‑series harmonics).

**Problem 244.** For a **real** $f(x)$, the Fourier transform obeys
(a) $F(-k)=F^{*}(k)$  (b) $F(-k)=-F(k)$  (c) $F(k)$ is real  (d) $F(k)=0$
> **Ans (a).** A real signal has a Hermitian spectrum. *Trick:* this Hermitian symmetry is why $\operatorname{Re}F$ comes out **even** in Q49.

**Problem 245.** For $f(x)=A\cos(k_0 x)$, each spectral spike has weight
(a) $\dfrac A2$  (b) $A$  (c) $2A$  (d) $\dfrac{A}{\sqrt2}$
> **Ans (a).** $\cos=\tfrac12(e^{ik_0x}+e^{-ik_0x})$, so each delta carries $A/2$. *Trick:* the cosine splits its amplitude evenly between $\pm k_0$.

---

# SET 50 — Divergence & curl of the position vector
**Origin (Q50):** $\nabla\cdot\vec r=3$ and $\nabla\times\vec r=0$ in 3‑D. **Twists:** the divergence, the curl, $\nabla r$, $\nabla^2 r$, the inverse‑square field.

**Problem 246.** In 3‑D, $\nabla\cdot\vec r=$
(a) $3$  (b) $0$  (c) $1$  (d) $r$
> **Ans (a).** $\partial_x x+\partial_y y+\partial_z z=3$. *Trick:* it equals the **dimension** of space (would be $d$ in $d$‑D).

**Problem 247.** $\nabla\times\vec r=$
(a) $0$  (b) $\vec r$  (c) $2$  (d) $\hat r$
> **Ans (a).** $\vec r=\nabla\big(\tfrac{r^2}{2}\big)$ is a gradient. *Trick:* a gradient field is automatically curl‑free.

**Problem 248.** $\nabla r$ (gradient of the magnitude $r=|\vec r|$) is
(a) $\hat r=\dfrac{\vec r}{r}$  (b) $\vec r$  (c) $1$  (d) $3$
> **Ans (a).** $\nabla|\vec r|=\dfrac{\vec r}{|\vec r|}$. *Trick:* don't confuse $\nabla r$ (a unit vector $\hat r$) with $\nabla\cdot\vec r=3$.

**Problem 249.** $\nabla^{2}r=$
(a) $\dfrac2r$  (b) $0$  (c) $3$  (d) $r$
> **Ans (a).** $\nabla^2 r=\dfrac{1}{r^2}\dfrac{d}{dr}\!\big(r^2\cdot1\big)=\dfrac2r$. *Trick:* a small but easily‑forgotten identity — $r$ is **not** harmonic.

**Problem 250.** $\nabla\cdot\left(\dfrac{\hat r}{r^{2}}\right)=$
(a) $4\pi\,\delta^{3}(\vec r)$  (b) $0$  (c) $\dfrac2r$  (d) $3$
> **Ans (a).** Zero for $r\neq0$, but a delta at the origin. *Trick:* naively $0$ everywhere — the true answer carries $4\pi\delta^3(\vec r)$ (Gauss's law; ties back to the Green's‑function set).

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: differentiate an integral with respect to its parameter (Feynman) — and the Gaussian dual; each $x$‑derivative $\to ik$ in Fourier space; a rank‑1 matrix has a $0$ eigenvalue of degeneracy $n-1$ yet stays diagonalizable; log–log slope = exponent (semi‑log for exponentials); a repeated root $\to te^{-t}$ peaking at $t=1$; Hermitian eigenvalues fall out of trace, $\det$, and $\operatorname{Tr}M^2$; a higher‑order pole can have **zero** residue; $P_n(\pm1)=(\pm1)^n$ but $P_{\text{odd}}(0)=0$; periodic $\to$ discrete spectrum with Hermitian symmetry; and $\nabla\cdot\vec r=3$, $\nabla\times\vec r=0$, with the inverse‑square field hiding a delta. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 250 problems across the first 50 originals (Q1–Q50).**
