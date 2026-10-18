# 50 Practice Problems — Part 8 (CSIR‑NET/JRF style)

**Built from problems 71–80 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **351–400** to continue Parts 1–7.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q71–Q77 = June 2016**, **Q78–Q80 = Dec 2016** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q71–Q80)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q71 | Complex analysis | Radius of convergence $=$ distance to nearest **complex** singularity |
| Q72 | Complex analysis | Contour integral with $\cosh/\sinh$ (convert to exponentials) |
| Q73 | Special functions | Gauss hypergeometric series & its derivative |
| Q74 | Probability | Sum of independent **Gaussians** (means/variances add) |
| Q75 | Dimensional analysis | Planck units from $G,h,k_B,c$ |
| Q76 | Integral transforms | FT of summed $\delta$‑derivatives (geometric series) |
| Q77 | Numerical methods | Newton–Raphson root finding |
| Q78 | Linear algebra | Cayley–Hamilton theorem |
| Q79 | Integral transforms | Laplace transform of piecewise functions (unit steps) |
| Q80 | Integral transforms | Fourier transform of a **Lorentzian** |

---

# SET 71 — Radius of convergence $=$ distance to nearest complex singularity
**Origin (Q71):** $\dfrac{1}{\cosh x}$ has radius of convergence $\tfrac\pi2$ about $x=0$, since $\cosh x=0$ first at $x=i\tfrac\pi2$. **Twists:** the principle, $1/(1+x^2)$, $1/(1-x)$, $e^x$, the $1/\cosh$ singularity.

**Problem 351.** The radius of convergence of a Taylor series about $x_0$ equals
(a) the distance from $x_0$ to the nearest singularity (in $\mathbb C$)  (b) the largest real $x$ where $f$ is defined  (c) $\infty$ always  (d) $1$
> **Ans (a).** Even for a real function, **complex** singularities cap the radius. *Trick:* this is the principle behind Q71 (a real $1/\cosh x$ limited by an imaginary singularity).

**Problem 352.** The radius of convergence of the Taylor series of $\dfrac{1}{1+x^{2}}$ about $x=0$ is
(a) $1$  (b) $\infty$  (c) $\dfrac\pi2$  (d) $2$
> **Ans (a).** Poles at $x=\pm i$, distance $1$. *Trick:* it has **no real** singularity, yet the series diverges for $|x|>1$ because of the poles at $\pm i$.

**Problem 353.** The radius of convergence of $\displaystyle\sum_{n=0}^\infty x^n=\dfrac{1}{1-x}$ is
(a) $1$  (b) $\infty$  (c) $0$  (d) $2$
> **Ans (a).** The pole at $x=1$ is distance $1$ from the origin. *Trick:* the nearest singularity sets the radius.

**Problem 354.** The radius of convergence of the Taylor series of $e^{x}$ about $x=0$ is
(a) $\infty$  (b) $1$  (c) $\dfrac\pi2$  (d) $0$
> **Ans (a).** $e^x$ is entire (no singularities). *Trick:* entire functions have infinite radius of convergence.

**Problem 355.** The singularity of $\dfrac{1}{\cosh x}$ nearest to $x=0$ is at
(a) $x=i\dfrac\pi2$  (b) $x=\dfrac\pi2$  (c) $x=0$  (d) $x=\pi$
> **Ans (a).** $\cosh x=0$ at $x=i\big(\tfrac\pi2+n\pi\big)$; the nearest is $i\tfrac\pi2$. *Trick:* this gives the radius $\pi/2$ (Q71).

---

# SET 72 — Contour integration with hyperbolic functions
**Origin (Q72):** $\dfrac{1}{2\pi i}\oint\dfrac{e^{4z}-1}{\cosh z-2\sinh z}\,dz=-\dfrac8{\sqrt3}$; converting to exponentials gives a simple pole at $z=\tfrac{\ln3}{2}$. **Twists:** $\cosh$/$\sinh$ in exponentials, the simplified denominator, the pole location, and the zeros of $\cosh$.

**Problem 356.** $\cosh z=$
(a) $\dfrac{e^{z}+e^{-z}}{2}$  (b) $\dfrac{e^{z}-e^{-z}}{2}$  (c) $e^{z}+e^{-z}$  (d) $\dfrac{e^{z}}{2}+e^{-z}$
> **Ans (a).** The definition. *Trick:* $\cosh$ uses the **sum** of exponentials.

**Problem 357.** $\cosh z-2\sinh z=0$ when
(a) $e^{2z}=3$  (b) $e^{2z}=2$  (c) $z=0$  (d) $e^{z}=3$
> **Ans (a).** $\dfrac{e^z+e^{-z}}{2}-(e^z-e^{-z})=\dfrac{-e^z+3e^{-z}}{2}=0\Rightarrow e^{2z}=3$. *Trick:* combine the exponentials to find the pole (Q72).

**Problem 358.** The pole at $z=\tfrac{\ln3}{2}\approx0.55$, relative to the unit circle $|z|=1$, is
(a) inside  (b) outside  (c) on the circle  (d) at the origin
> **Ans (a).** $\tfrac{\ln3}{2}\approx0.55<1$. *Trick:* it lies inside $|z|=1$, so it contributes to Q72's integral.

**Problem 359.** $\sinh z=$
(a) $\dfrac{e^{z}-e^{-z}}{2}$  (b) $\dfrac{e^{z}+e^{-z}}{2}$  (c) $e^{z}-e^{-z}$  (d) $\dfrac{e^{z}}{2}-e^{-z}$
> **Ans (a).** The definition. *Trick:* $\sinh$ uses the **difference** (the minus distinguishes it from $\cosh$).

**Problem 360.** $\cosh z$ has zeros at
(a) $z=i\big(n+\tfrac12\big)\pi$  (b) $z=n\pi$  (c) $z=in\pi$  (d) $z=\big(n+\tfrac12\big)\pi$
> **Ans (a).** $\cosh z=\cos(iz)$ vanishes at purely imaginary $z=i\big(n+\tfrac12\big)\pi$. *Trick:* $\cosh$ never vanishes on the real axis — only on the imaginary axis.

---

# SET 73 — Gauss hypergeometric series & its derivative
**Origin (Q73):** $\dfrac{d}{dz}\,{}_2F_1(a,b;c;z)=\dfrac{ab}{c}\,{}_2F_1(a+1,b+1;c+1;z)$. **Twists:** the series form, the derivative, the geometric special case, term‑by‑term differentiation, the Pochhammer symbol.

**Problem 361.** The coefficient of $z^n$ in ${}_2F_1(a,b;c;z)$ involves
(a) rising factorials $\dfrac{(a)_n(b)_n}{(c)_n\,n!}$  (b) $\dfrac{a^nb^n}{c^n}$  (c) binomial coefficients  (d) $1/n$
> **Ans (a).** Pochhammer (rising‑factorial) ratios. *Trick:* the building blocks are rising factorials, not plain powers.

**Problem 362.** $\dfrac{d}{dz}\,{}_2F_1(a,b;c;z)=$
(a) $\dfrac{ab}{c}\,{}_2F_1(a+1,b+1;c+1;z)$  (b) ${}_2F_1(a-1,b-1;c-1;z)$  (c) $\dfrac{c}{ab}\,{}_2F_1(a+1,b+1;c+1;z)$  (d) ${}_2F_1(a,b;c;z)$
> **Ans (a).** Differentiation raises all three parameters by $1$ and pulls out $ab/c$. *Trick:* this is exactly Q73.

**Problem 363.** ${}_2F_1(1,1;1;z)=$
(a) $\dfrac{1}{1-z}$  (b) $e^{z}$  (c) $\ln(1-z)$  (d) $1+z$
> **Ans (a).** The hypergeometric series reduces to the geometric series here. *Trick:* the parameters collapse it to $\sum z^n=1/(1-z)$.

**Problem 364.** $\dfrac{d}{dz}\displaystyle\sum_{n}a_n z^{n}=$
(a) $\displaystyle\sum_n n\,a_n z^{n-1}$  (b) $\displaystyle\sum_n a_n z^{n-1}$  (c) $\displaystyle\sum_n a_n z^{n+1}$  (d) $\displaystyle\sum_n \frac{a_n}{n}z^{n}$
> **Ans (a).** Bring down the power $n$. *Trick:* term‑by‑term differentiation is the mechanism behind Q73.

**Problem 365.** The Pochhammer symbol $(a)_n=$
(a) $a(a+1)\cdots(a+n-1)$  (b) $a(a-1)\cdots(a-n+1)$  (c) $a^{n}$  (d) $n!$
> **Ans (a).** The rising factorial ($n$ ascending factors from $a$). *Trick:* "rising," not falling.

---

# SET 74 — Sum of independent Gaussians
**Origin (Q74):** $X\sim N(\mu,\sigma^2)$, $Y\sim N(-\mu,\sigma^2)$ independent $\Rightarrow X+Y\sim N(0,2\sigma^2)$, SD $\sigma\sqrt2$ — unimodal, **not** bimodal. **Twists:** sum is Gaussian, means/variances, the SD, the difference, FWHM.

**Problem 366.** The sum of two **independent** Gaussian random variables is
(a) Gaussian  (b) bimodal  (c) uniform  (d) Poisson
> **Ans (a).** Gaussians are closed under addition. *Trick:* the sum is a single‑peaked Gaussian — **not** two‑peaked (Q74's trap).

**Problem 367.** For independent $X\sim N(\mu_1,\sigma_1^2)$, $Y\sim N(\mu_2,\sigma_2^2)$, the sum $X+Y$ has
(a) mean $\mu_1+\mu_2$, variance $\sigma_1^2+\sigma_2^2$  (b) mean $\mu_1+\mu_2$, variance $\sigma_1+\sigma_2$  (c) mean $\mu_1\mu_2$, variance $\sigma_1^2\sigma_2^2$  (d) mean $\mu_1-\mu_2$, variance $\sigma_1^2-\sigma_2^2$
> **Ans (a).** Means add; **variances** add. *Trick:* it's the variances that add, not the standard deviations.

**Problem 368.** For $X\sim N(\mu,\sigma^2)$ and $Y\sim N(-\mu,\sigma^2)$ independent, $X+Y$ has standard deviation
(a) $\sigma\sqrt2$  (b) $2\sigma$  (c) $\sigma$  (d) $0$
> **Ans (a).** Variance $=\sigma^2+\sigma^2=2\sigma^2$, so SD $=\sigma\sqrt2$. *Trick:* $\sqrt{2}\,\sigma$, not $2\sigma$ (Q74).

**Problem 369.** For independent $X,Y$ (each variance $\sigma^2$), $X-Y$ has variance
(a) $2\sigma^{2}$  (b) $0$  (c) $\sigma^{2}$  (d) $\sigma^2-\sigma^2$
> **Ans (a).** Variances add even for a difference. *Trick:* $\operatorname{Var}(X-Y)=\sigma^2+\sigma^2=2\sigma^2$ — same as the sum.

**Problem 370.** The full width at half maximum (FWHM) of a Gaussian relates to $\sigma$ by
(a) $\approx2.355\,\sigma$  (b) $\sigma$  (c) $2\sigma$  (d) $\sigma/2$
> **Ans (a).** $\text{FWHM}=2\sqrt{2\ln2}\,\sigma\approx2.355\sigma$. *Trick:* a standard but non‑obvious numerical factor.

---

# SET 75 — Dimensional analysis (Planck units)
**Origin (Q75):** $T_P\propto\sqrt{\dfrac{hc^5}{k_B^2 G}}$. **Twists:** dimension of $k_B$, dimension of $G$, the Planck length, the Planck mass, the $T_P$ combination.

**Problem 371.** The Boltzmann constant $k_B$ has dimensions
(a) $[ML^2T^{-2}\Theta^{-1}]$  (b) $[ML^2T^{-2}]$  (c) $[\Theta]$  (d) $[ML^2T^{-1}]$
> **Ans (a).** $k_B=$ energy/temperature. *Trick:* it carries a $\Theta^{-1}$ (per kelvin).

**Problem 372.** The gravitational constant $G$ has dimensions
(a) $[M^{-1}L^{3}T^{-2}]$  (b) $[ML^{3}T^{-2}]$  (c) $[M^{-1}L^{2}T^{-2}]$  (d) $[LT^{-2}]$
> **Ans (a).** From $F=Gm_1m_2/r^2$, $G=[F][L^2]/[M^2]$. *Trick:* note the $M^{-1}$.

**Problem 373.** The Planck length is built as
(a) $\sqrt{\dfrac{\hbar G}{c^{3}}}$  (b) $\sqrt{\dfrac{Gc}{\hbar}}$  (c) $\dfrac{G\hbar}{c}$  (d) $\sqrt{\dfrac{\hbar c}{G}}$
> **Ans (a).** $\ell_P=\sqrt{\hbar G/c^3}$. *Trick:* $G$ in the numerator, $c^3$ below.

**Problem 374.** The Planck mass is built as
(a) $\sqrt{\dfrac{\hbar c}{G}}$  (b) $\sqrt{\dfrac{\hbar G}{c}}$  (c) $\dfrac{\hbar c}{G}$  (d) $\sqrt{\dfrac{G\hbar}{c^{3}}}$
> **Ans (a).** $m_P=\sqrt{\hbar c/G}$. *Trick:* here $G$ sits in the **denominator** (opposite to the length).

**Problem 375.** The Planck temperature is proportional to
(a) $\sqrt{\dfrac{hc^{5}}{k_B^{2}G}}$  (b) $\sqrt{\dfrac{hc^{3}}{k_B^{2}G}}$  (c) $\sqrt{\dfrac{G}{hc^{4}k_B^{2}}}$  (d) $\sqrt{\dfrac{hk_B^{2}}{Gc^{3}}}$
> **Ans (a).** $T_P=m_Pc^2/k_B=\sqrt{\hbar c^5/(Gk_B^2)}$. *Trick:* the $c^5$ is the giveaway (Q75).

---

# SET 76 — Fourier transform of summed $\delta$‑derivatives
**Origin (Q76):** $\mathcal F\!\big[\sum_{n=0}^\infty\delta^{(n)}\big]=\sum_n(-ik)^n=\dfrac{1}{1+ik}$. **Twists:** $\mathcal F[\delta^{(n)}]$, summing the series, the geometric formula, $\mathcal F[\delta]$, the operator series.

**Problem 376.** With the kernel $e^{ikx}$, $\mathcal F[\delta^{(n)}(x)]=$
(a) $(-ik)^{n}$  (b) $(ik)^{n}$  (c) $k^{n}$  (d) $\dfrac{n!}{k^{n}}$
> **Ans (a).** Each derivative brings $-ik$. *Trick:* $n$ derivatives give $(-ik)^n$ (this convention).

**Problem 377.** $\displaystyle\sum_{n=0}^{\infty}(-ik)^{n}=$
(a) $\dfrac{1}{1+ik}$  (b) $\dfrac{1}{1-ik}$  (c) $e^{-ik}$  (d) $\dfrac{1}{ik}$
> **Ans (a).** Geometric series with ratio $-ik$: $\dfrac{1}{1-(-ik)}$. *Trick:* the $-(-ik)$ becomes $+ik$ in the denominator (Q76).

**Problem 378.** $\displaystyle\sum_{n=0}^{\infty}r^{n}=$ (for $|r|<1$)
(a) $\dfrac{1}{1-r}$  (b) $\dfrac{1}{1+r}$  (c) $\dfrac{r}{1-r}$  (d) $1-r$
> **Ans (a).** The geometric series. *Trick:* the sum that powers Q76.

**Problem 379.** $\mathcal F[\delta(x)]=$
(a) $1$  (b) $ik$  (c) $\delta(k)$  (d) $0$
> **Ans (a).** The $n=0$ term of the sum. *Trick:* $\mathcal F[\delta]=1$ (a flat spectrum).

**Problem 380.** The operator series $\displaystyle\sum_{n=0}^{\infty}\Big(\frac{d}{dx}\Big)^{n}$ formally equals
(a) $\Big(1-\dfrac{d}{dx}\Big)^{-1}$  (b) $e^{d/dx}$  (c) $\dfrac{d}{dx}$  (d) $1$
> **Ans (a).** A geometric series in the derivative operator. *Trick:* its Fourier transform is the geometric series in $(-ik)$, i.e. Q76.

---

# SET 77 — Newton–Raphson method
**Origin (Q77):** $f(x)=3x^3-4x-5$, $x_0=2\Rightarrow x_1=2-\tfrac{11}{32}\approx1.656$. **Twists:** the formula, the first step, the geometry, the convergence rate, the failure case.

**Problem 381.** The Newton–Raphson iteration is
(a) $x_{n+1}=x_n-\dfrac{f(x_n)}{f'(x_n)}$  (b) $x_{n+1}=x_n-\dfrac{f'(x_n)}{f(x_n)}$  (c) $x_{n+1}=x_n+\dfrac{f(x_n)}{f'(x_n)}$  (d) $x_{n+1}=\dfrac{f(x_n)}{f'(x_n)}$
> **Ans (a).** Subtract $f/f'$. *Trick:* the correction is $f/f'$ (not $f'/f$), with a minus sign.

**Problem 382.** For $f(x)=3x^3-4x-5$ with $x_0=2$, the next estimate is
(a) $1.656$  (b) $1.5$  (c) $2.34$  (d) $1.0$
> **Ans (a).** $f(2)=11,\ f'(2)=32\Rightarrow x_1=2-\tfrac{11}{32}\approx1.656$. *Trick:* this is Q77.

**Problem 383.** Newton–Raphson takes the next estimate to be
(a) the $x$‑intercept of the tangent line at the current point  (b) the interval midpoint  (c) the average of the $f$ values  (d) a random point
> **Ans (a).** It follows the tangent down to the axis. *Trick:* the geometry is "tangent → axis."

**Problem 384.** Near a simple root, Newton–Raphson converges
(a) quadratically (correct digits roughly double each step)  (b) linearly  (c) logarithmically  (d) not at all
> **Ans (a).** Quadratic convergence. *Trick:* this fast (digit‑doubling) rate is the method's main appeal.

**Problem 385.** Newton–Raphson can fail or diverge when
(a) $f'(x_n)=0$  (b) $f(x_n)=0$  (c) $x_n>0$  (d) $f$ is continuous
> **Ans (a).** A horizontal tangent gives division by zero. *Trick:* $f'=0$ breaks the iteration.

---

# SET 78 — Cayley–Hamilton theorem
**Origin (Q78):** $M=\begin{pmatrix}1&3&2\\3&-1&0\\0&0&1\end{pmatrix}$ satisfies $M^3-M^2-10M+10I=0$. **Twists:** the statement, the $2\times2$ form, finding the inverse, reducing powers, the Q78 polynomial.

**Problem 386.** The Cayley–Hamilton theorem states that a matrix
(a) satisfies its own characteristic equation  (b) is always diagonalizable  (c) has real eigenvalues  (d) commutes with its inverse
> **Ans (a).** Substitute $M$ for $\lambda$ in the characteristic polynomial. *Trick:* the matrix "annihilates" its own characteristic polynomial (Q78).

**Problem 387.** A $2\times2$ matrix with trace $\tau$ and determinant $\Delta$ satisfies
(a) $M^{2}-\tau M+\Delta I=0$  (b) $M^{2}+\tau M+\Delta I=0$  (c) $M^{2}-\tau M-\Delta I=0$  (d) $M^{2}-\Delta M+\tau I=0$
> **Ans (a).** Characteristic polynomial $\lambda^2-\tau\lambda+\Delta$. *Trick:* $-$trace, $+$det.

**Problem 388.** For a $2\times2$ matrix with $M^2-\tau M+\Delta I=0$ ($\Delta\neq0$), $M^{-1}=$
(a) $\dfrac{\tau I-M}{\Delta}$  (b) $\dfrac{M-\tau I}{\Delta}$  (c) $\dfrac{M}{\Delta}$  (d) $\tau I-M$
> **Ans (a).** Rearrange $M(M-\tau I)=-\Delta I$. *Trick:* Cayley–Hamilton gives the inverse without row reduction.

**Problem 389.** For a $3\times3$ matrix, Cayley–Hamilton lets $M^{3}$ be written in terms of
(a) $M^{2},M,I$  (b) $M^{4},M^{5}$  (c) only $I$  (d) $M^{-1}$
> **Ans (a).** The characteristic equation reduces $M^3$ to lower powers. *Trick:* in Q78, $M^3=M^2+10M-10I$.

**Problem 390.** The matrix $M=\begin{pmatrix}1&3&2\\3&-1&0\\0&0&1\end{pmatrix}$ has characteristic polynomial
(a) $\lambda^{3}-\lambda^{2}-10\lambda+10$  (b) $\lambda^{3}+\lambda^{2}-10\lambda+10$  (c) $\lambda^{3}-10\lambda$  (d) $\lambda^{3}-\lambda^{2}+10\lambda-10$
> **Ans (a).** Expanding along the third row gives $(1-\lambda)(\lambda^2-10)$. *Trick:* this yields $M^3-M^2-10M+10I=0$ (Q78).

---

# SET 79 — Laplace transform of piecewise functions
**Origin (Q79):** the ramp‑then‑constant ($t/T$ for $0<t<T$, then $1$) has $\mathcal L=\dfrac{1-e^{-sT}}{s^2T}$, assembled from unit steps. **Twists:** the shifted step, the second shifting theorem, the decomposition, $\mathcal L[t]$, the result.

**Problem 391.** $\mathcal L[u(t-a)]$ (the Heaviside step) is
(a) $\dfrac{e^{-as}}{s}$  (b) $e^{-as}$  (c) $\dfrac1s$  (d) $\dfrac{e^{as}}{s}$
> **Ans (a).** A delayed step. *Trick:* the step keeps its $1/s$ and gains a delay factor $e^{-as}$.

**Problem 392.** $\mathcal L[f(t-a)\,u(t-a)]=$
(a) $e^{-as}F(s)$  (b) $F(s-a)$  (c) $e^{as}F(s)$  (d) $\dfrac{F(s)}{a}$
> **Ans (a).** The second shifting theorem. *Trick:* a time delay $a$ multiplies the transform by $e^{-as}$ (used to build Q79).

**Problem 393.** The function $f(t)=\tfrac tT$ for $0<t<T$ and $1$ for $t>T$ can be written as
(a) $\dfrac tT-\dfrac{t-T}{T}\,u(t-T)$  (b) $\dfrac tT\,u(t-T)$  (c) $u(t-T)$ only  (d) $\dfrac tT+u(t-T)$
> **Ans (a).** Subtract a **delayed** ramp so the slope flattens to $1$ after $t=T$. *Trick:* the delayed‑ramp cancellation is the key decomposition.

**Problem 394.** $\mathcal L[t]=$
(a) $\dfrac{1}{s^{2}}$  (b) $\dfrac1s$  (c) $\dfrac{2}{s^{3}}$  (d) $s$
> **Ans (a).** $\mathcal L[t^n]=n!/s^{n+1}$ with $n=1$. *Trick:* the ramp gives $1/s^2$ (Q79's $t/T\to1/(Ts^2)$).

**Problem 395.** The Laplace transform of the ramp‑then‑constant function (slope $1/T$, capping at $1$) is
(a) $\dfrac{1-e^{-sT}}{s^{2}T}$  (b) $\dfrac{1+e^{-sT}}{s^{2}T}$  (c) $\dfrac{1}{s^{2}T}$  (d) $\dfrac{e^{-sT}}{s^{2}T}$
> **Ans (a).** The ramp minus its delayed copy gives the $(1-e^{-sT})$ factor. *Trick:* this is Q79's result.

---

# SET 80 — Fourier transform of a Lorentzian
**Origin (Q80):** $\mathcal F\!\big[\tfrac{1}{x^2+a^2}\big]=\tfrac\pi a e^{-a|k|}$; for $a^2=2$ it is $\tfrac\pi{\sqrt2}e^{-\sqrt2|k|}$. **Twists:** the standard pair, the Q80 value, the reverse pair, the width reciprocity, the value at $k=0$.

**Problem 396.** The Fourier transform of $\dfrac{1}{x^{2}+a^{2}}$ is
(a) $\dfrac{\pi}{a}\,e^{-a|k|}$  (b) $\dfrac{\pi}{a}\,e^{-ak}$  (c) $\pi\,e^{-a|k|}$  (d) $\dfrac{\pi}{a^{2}}\,e^{-a|k|}$
> **Ans (a).** A Lorentzian transforms to a two‑sided decaying exponential. *Trick:* note the $|k|$ (the function is even, so the transform is even).

**Problem 397.** The Fourier transform of $\dfrac{1}{x^{2}+2}$ is
(a) $\dfrac{\pi}{\sqrt2}\,e^{-\sqrt2|k|}$  (b) $\dfrac\pi2\,e^{-2|k|}$  (c) $\sqrt2\,\pi\,e^{-\sqrt2 k}$  (d) $\pi\,e^{-2|k|}$
> **Ans (a).** $a^2=2\Rightarrow a=\sqrt2$. *Trick:* substitute $a=\sqrt2$ into $\tfrac\pi a e^{-a|k|}$ (Q80).

**Problem 398.** The Fourier transform of $e^{-a|x|}$ is
(a) $\dfrac{2a}{k^{2}+a^{2}}$  (b) $\dfrac{1}{k^{2}+a^{2}}$  (c) $e^{-a|k|}$  (d) $\dfrac\pi a e^{-a|k|}$
> **Ans (a).** A two‑sided exponential transforms to a Lorentzian. *Trick:* the **inverse** of Q80 — exponential $\leftrightarrow$ Lorentzian.

**Problem 399.** As the Lorentzian width $a$ decreases, its transform $e^{-a|k|}$
(a) decays more slowly (gets wider)  (b) decays faster  (c) is unchanged  (d) becomes a delta
> **Ans (a).** Narrow in $x$ ⇔ wide in $k$. *Trick:* the Fourier reciprocity (uncertainty‑principle) relationship.

**Problem 400.** The Fourier transform of $\dfrac{1}{x^{2}+a^{2}}$ at $k=0$ equals
(a) $\dfrac\pi a$  (b) $0$  (c) $1$  (d) $\infty$
> **Ans (a).** At $k=0$ the FT is just $\displaystyle\int\frac{dx}{x^2+a^2}=\frac\pi a$. *Trick:* the $k=0$ value of any FT is the integral of the function.

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: radius of convergence is set by the nearest **complex** singularity (even for real functions); convert $\cosh/\sinh$ to exponentials to find poles; differentiating a hypergeometric function shifts all parameters up by $1$; the sum of independent Gaussians is Gaussian with variances **adding** (SD $\sigma\sqrt2$, not bimodal); Planck $T_P\propto\sqrt{hc^5/(k_B^2G)}$ (the $c^5$ gives it away); $\mathcal F[\sum\delta^{(n)}]$ is a geometric series $=1/(1+ik)$; Newton–Raphson subtracts $f/f'$ and converges quadratically; Cayley–Hamilton lets a matrix annihilate its own characteristic polynomial (and gives $M^{-1}$); a piecewise Laplace transform is built from delayed steps; and a Lorentzian's FT is a two‑sided exponential $\tfrac\pi a e^{-a|k|}$. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 400 problems across the first 80 originals (Q1–Q80).**
