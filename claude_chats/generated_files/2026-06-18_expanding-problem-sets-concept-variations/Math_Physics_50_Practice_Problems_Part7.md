# 50 Practice Problems — Part 7 (CSIR‑NET/JRF style)

**Built from problems 61–70 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **301–350** to continue Parts 1–6.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q61–Q62 = June 2015**, **Q63–Q70 = Dec 2015** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q61–Q70)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q61 | Integral transforms | Laplace transform (polynomials, sines) |
| Q62 | PDEs | d'Alembert solution; zero initial velocity ⇒ pulse splits |
| Q63 | Dimensional analysis | Building a target dimension from constants |
| Q64 | Functions | Hyperbolic & inverse‑hyperbolic functions |
| Q65 | Complex analysis | Locating/classifying poles (zeros of the denominator) |
| Q66 | Integral transforms | Fourier transform **properties** (shift, scale, convolution) |
| Q67 | ODEs | Separable ODE with **saturation** at an equilibrium |
| Q68 | Special functions | Hermite ODE ↔ generating‑function PDE |
| Q69 | Numerical methods | Numerical integration (Simpson's rule) |
| Q70 | Probability | Random walk / self‑avoiding paths |

---

# SET 61 — Laplace transforms (forward)
**Origin (Q61):** $\mathcal L[6t^3+3\sin4t]=\dfrac{36}{s^4}+\dfrac{12}{s^2+16}$, using $\mathcal L[t^n]=\dfrac{n!}{s^{n+1}}$ and $\mathcal L[\sin at]=\dfrac{a}{s^2+a^2}$. **Twists:** a power, a sine, a cosine, an $e^{-at}t$, a hyperbolic sine.

**Problem 301.** $\mathcal L[t^{3}]=$
(a) $\dfrac{6}{s^4}$  (b) $\dfrac{3}{s^4}$  (c) $\dfrac{1}{s^4}$  (d) $\dfrac{6}{s^3}$
> **Ans (a).** $\dfrac{n!}{s^{n+1}}=\dfrac{3!}{s^4}=\dfrac{6}{s^4}$. *Trick:* the numerator is $n!=6$, not $n$.

**Problem 302.** $\mathcal L[\sin 4t]=$
(a) $\dfrac{4}{s^2+16}$  (b) $\dfrac{s}{s^2+16}$  (c) $\dfrac{4}{s^2-16}$  (d) $\dfrac{1}{s^2+16}$
> **Ans (a).** $\dfrac{a}{s^2+a^2}$ with $a=4$. *Trick:* the numerator is $a$ for sine.

**Problem 303.** $\mathcal L[\cos 4t]=$
(a) $\dfrac{s}{s^2+16}$  (b) $\dfrac{4}{s^2+16}$  (c) $\dfrac{s}{s^2-16}$  (d) $\dfrac{1}{s^2+16}$
> **Ans (a).** $\dfrac{s}{s^2+a^2}$. *Trick:* cosine puts $s$ (not $a$) in the numerator.

**Problem 304.** $\mathcal L[t\,e^{-2t}]=$
(a) $\dfrac{1}{(s+2)^2}$  (b) $\dfrac{1}{s+2}$  (c) $\dfrac{1}{(s-2)^2}$  (d) $\dfrac{2}{(s+2)^2}$
> **Ans (a).** Apply the shift $s\to s+2$ to $\mathcal L[t]=1/s^2$. *Trick:* the $e^{-2t}$ shifts $s$ by $+2$.

**Problem 305.** $\mathcal L[\sinh 3t]=$
(a) $\dfrac{3}{s^2-9}$  (b) $\dfrac{3}{s^2+9}$  (c) $\dfrac{s}{s^2-9}$  (d) $\dfrac{1}{s^2-9}$
> **Ans (a).** $\dfrac{a}{s^2-a^2}$ with $a=3$. *Trick:* the **hyperbolic** sine gives $s^2-a^2$ (minus), unlike $\sin$'s plus.

---

# SET 62 — Wave equation / d'Alembert (zero initial velocity)
**Origin (Q62):** with $f(x,0)=e^{-x^2}$ and $\partial_t f(x,0)=0$, the solution is $\tfrac12\big[e^{-(x-vt)^2}+e^{-(x+vt)^2}\big]$ — the pulse splits in two. **Twists:** the d'Alembert form, the half‑amplitudes, a single‑wave condition, the general solution, the peak positions.

**Problem 306.** For the wave equation with initial shape $\phi(x)$ and **zero** initial velocity, the solution is
(a) $\tfrac12\big[\phi(x-vt)+\phi(x+vt)\big]$  (b) $\phi(x-vt)$  (c) $\phi(x+vt)$  (d) $\phi(x)\cos(vt)$
> **Ans (a).** Zero initial velocity ⇒ the pulse splits into two half‑amplitude copies. *Trick:* this is exactly Q62.

**Problem 307.** With zero initial velocity, each of the two traveling pulses has amplitude
(a) half the original  (b) the full original  (c) double  (d) zero
> **Ans (a).** The shape divides equally between left‑ and right‑movers. *Trick:* the $\tfrac12$ in the d'Alembert formula.

**Problem 308.** For the solution to be a **single** right‑moving wave $\phi(x-vt)$ (no left‑mover), the initial velocity must be
(a) $-v\,\phi'(x)$  (b) $0$  (c) $+v\,\phi'(x)$  (d) $\phi(x)$
> **Ans (a).** $\partial_t\phi(x-vt)\big|_{t=0}=-v\phi'(x)$. *Trick:* a pure traveling wave needs a **nonzero** initial velocity — zero gives the splitting of Q62.

**Problem 309.** The general solution of $u_{tt}=v^2u_{xx}$ is
(a) $f(x-vt)+g(x+vt)$  (b) $f(x)g(t)$  (c) $f(x-vt)$ only  (d) $f(x)+g(t)$
> **Ans (a).** A superposition of two arbitrary traveling waves. *Trick:* d'Alembert's general form.

**Problem 310.** At time $t$, the two pulses from an initial peak at $x=0$ are centered at
(a) $x=\pm vt$  (b) $x=0$  (c) $x=vt$ only  (d) $x=v^2t^2$
> **Ans (a).** One moves right to $+vt$, the other left to $-vt$. *Trick:* the peaks separate symmetrically at speed $v$.

---

# SET 63 — Dimensional analysis
**Origin (Q63):** the cross‑section $\sigma$ (an area) is built from $E,h,c$ as $\big(\tfrac{hc}{E}\big)^2$. **Twists:** the dimension of $h$, the length $hc/E$, the pendulum, the limits of the method, $E=h\nu$.

**Problem 311.** Planck's constant $h$ has dimensions
(a) $[ML^2T^{-1}]$  (b) $[ML^2T^{-2}]$  (c) $[MLT^{-1}]$  (d) $[ML^2T]$
> **Ans (a).** $h=$ energy $\times$ time $=[ML^2T^{-2}][T]$. *Trick:* $h$ has the dimensions of **action** ($J\cdot s$).

**Problem 312.** The quantity $\dfrac{hc}{E}$ has dimensions of
(a) length  (b) area  (c) energy  (d) time
> **Ans (a).** $\dfrac{[ML^3T^{-2}]}{[ML^2T^{-2}]}=[L]$. *Trick:* this is why $(hc/E)^2$ is an **area** (Q63).

**Problem 313.** By dimensional analysis, the period of a simple pendulum (depending on length $L$ and $g$) goes as
(a) $\sqrt{L/g}$  (b) $L/g$  (c) $\sqrt{Lg}$  (d) $L$
> **Ans (a).** $\sqrt{[L]/[LT^{-2}]}=\sqrt{[T^2]}=[T]$. *Trick:* the classic dimensional result for $T$.

**Problem 314.** Dimensional analysis can determine the **form** of a relation but **not**
(a) dimensionless numerical factors  (b) the dimensions  (c) which variables matter  (d) the units
> **Ans (a).** It fixes the powers, not pure numbers. *Trick:* e.g. it can't supply the $2\pi$ in the pendulum period.

**Problem 315.** Combining $h$ with a frequency $\nu$ gives an energy as
(a) $h\nu$  (b) $h/\nu$  (c) $h\nu^{2}$  (d) $h/c$
> **Ans (a).** $[h][\nu]=[ML^2T^{-1}][T^{-1}]=[ML^2T^{-2}]=$ energy. *Trick:* $E=h\nu$ falls straight out of the dimensions.

---

# SET 64 — Hyperbolic & inverse‑hyperbolic functions
**Origin (Q64):** $y=\coth x\Rightarrow x=\ln\sqrt{\tfrac{y+1}{y-1}}$, by writing $\coth$ in exponentials and solving. **Twists:** the identity, $\sinh^{-1}$, $\tanh^{-1}$, the derivative of $\tanh$, the limit of $\coth$.

**Problem 316.** $\cosh^{2}x-\sinh^{2}x=$
(a) $1$  (b) $-1$  (c) $\cosh 2x$  (d) $0$
> **Ans (a).** The hyperbolic Pythagorean identity. *Trick:* it equals $+1$ (the trig version $\cos^2+\sin^2=1$ has a $+$, but here it's a difference equal to $+1$).

**Problem 317.** $\sinh^{-1}(x)=$
(a) $\ln\!\big(x+\sqrt{x^2+1}\big)$  (b) $\ln\!\big(x+\sqrt{x^2-1}\big)$  (c) $\tfrac12\ln\dfrac{1+x}{1-x}$  (d) $\ln x$
> **Ans (a).** Solve $x=\tfrac12(e^y-e^{-y})$. *Trick:* note the $+1$ under the root (that's $\cosh^{-1}$ that has $-1$).

**Problem 318.** $\tanh^{-1}(x)=$
(a) $\tfrac12\ln\dfrac{1+x}{1-x}$  (b) $\ln\!\big(x+\sqrt{x^2+1}\big)$  (c) $\ln\!\big(x+\sqrt{x^2-1}\big)$  (d) $\tfrac12\ln\dfrac{x+1}{x-1}$
> **Ans (a).** $\tanh^{-1}x=\tfrac12\ln\dfrac{1+x}{1-x}$. *Trick:* contrast with Q64's $\coth^{-1}$, which has $\dfrac{x+1}{x-1}$ (arguments swapped).

**Problem 319.** $\dfrac{d}{dx}\tanh x=$
(a) $\operatorname{sech}^2 x$  (b) $\operatorname{sech}x\tanh x$  (c) $\cosh^2 x$  (d) $-\operatorname{sech}^2 x$
> **Ans (a).** $\dfrac{d}{dx}\tanh x=1-\tanh^2x=\operatorname{sech}^2x$. *Trick:* it's positive $\operatorname{sech}^2$ (the same derivative used in the $\ln\cosh$ series).

**Problem 320.** As $x\to\infty$, $\coth x\to$
(a) $1$  (b) $0$  (c) $\infty$  (d) $x$
> **Ans (a).** $\dfrac{e^x+e^{-x}}{e^x-e^{-x}}\to1$. *Trick:* the growing exponentials dominate, so the ratio approaches $1$.

---

# SET 65 — Locating & classifying poles
**Origin (Q65):** $\dfrac{z}{\sin(\pi z^2)}$ has a **simple** pole at $0$ (the numerator $z$ lowers the order) and further poles at $\pm\sqrt n$ **and** $\pm i\sqrt n$ (since $\sin(\pi z^2)=0$ at $z^2=\pm n$). **Twists:** where $\sin(\pi z^2)$ vanishes, the simple pole at $0$, the imaginary poles, order from the denominator, $1/\sin z$.

**Problem 321.** $\sin(\pi z^2)=0$ when $z^2$ equals
(a) any integer $n$  (b) any half‑integer  (c) $0$ only  (d) $\pi$
> **Ans (a).** $\sin(\pi w)=0\Leftrightarrow w$ is an integer; here $w=z^2$. *Trick:* set the argument to integer multiples of $\pi$.

**Problem 322.** At $z=0$, the function $\dfrac{z}{\sin(\pi z^2)}$ has
(a) a simple pole  (b) an order‑2 pole  (c) a removable singularity  (d) an essential singularity
> **Ans (a).** Near $0$, $\dfrac{z}{\sin(\pi z^2)}\sim\dfrac{z}{\pi z^2}=\dfrac{1}{\pi z}$. *Trick:* the $z$ in the numerator cancels one power, leaving a **simple** pole.

**Problem 323.** Besides $\pm\sqrt n$, the function $\dfrac{z}{\sin(\pi z^2)}$ also has poles at
(a) $\pm i\sqrt n$  (b) $0$ only  (c) $\pm n$  (d) nowhere else
> **Ans (a).** $\sin(\pi z^2)=0$ also when $z^2=-n$, i.e. $z=\pm i\sqrt n$. *Trick:* the **negative** integers $z^2=-n$ give the imaginary‑axis poles (easily missed — and the key to Q65's answer).

**Problem 324.** If $g(z)$ has a **simple** zero at $z_0$ and $f(z_0)\neq0$, then $\dfrac{f}{g}$ at $z_0$ has
(a) a simple pole  (b) an order‑2 pole  (c) a removable singularity  (d) an essential singularity
> **Ans (a).** The pole order equals the order of the denominator's zero. *Trick:* a simple zero downstairs (with nonzero numerator) gives a simple pole.

**Problem 325.** The function $\dfrac{1}{\sin z}$ has
(a) simple poles at $z=n\pi$  (b) a pole at $z=0$ only  (c) simple poles at $z=n$  (d) order‑2 poles at $z=n\pi$
> **Ans (a).** $\sin z$ has simple zeros at $n\pi$. *Trick:* simple zeros of the denominator ⇒ simple poles at every $n\pi$.

---

# SET 66 — Fourier transform properties
**Origin (Q66):** $\mathcal F[\alpha\delta+\beta\delta'+\gamma\delta'']=\alpha-i\beta k-\gamma k^2$ (linearity plus the derivative rule). **Twists:** linearity, the shift theorem, scaling, convolution, Parseval.

**Problem 326.** The Fourier transform is linear, so $\mathcal F[\alpha f+\beta g]=$
(a) $\alpha\,\mathcal F[f]+\beta\,\mathcal F[g]$  (b) $\mathcal F[f]\,\mathcal F[g]$  (c) $\alpha\beta\,\mathcal F[f+g]$  (d) $\mathcal F[\alpha f]\cdot\mathcal F[\beta g]$
> **Ans (a).** Linearity. *Trick:* Q66 is just the FT applied term‑by‑term to the sum of deltas.

**Problem 327.** With the convention $F(k)=\int f(x)e^{ikx}dx$, $\mathcal F[f(x-a)]=$
(a) $e^{ika}F(k)$  (b) $F(k-a)$  (c) $e^{-ika}F(k)$  (d) $a\,F(k)$
> **Ans (a).** A real‑space shift multiplies by a phase. *Trick:* shifting in $x$ by $a$ gives the factor $e^{ika}$.

**Problem 328.** $\mathcal F[f(ax)]=$
(a) $\dfrac{1}{|a|}F\!\Big(\dfrac ka\Big)$  (b) $F(ak)$  (c) $a\,F(k)$  (d) $F\!\Big(\dfrac ka\Big)$
> **Ans (a).** Compressing in $x$ stretches in $k$, with a $1/|a|$ amplitude factor. *Trick:* the reciprocal‑scaling rule.

**Problem 329.** The Fourier transform of a convolution $(f*g)$ is
(a) $F(k)\,G(k)$  (b) $F(k)+G(k)$  (c) $\dfrac{F(k)}{G(k)}$  (d) $F(k)*G(k)$
> **Ans (a).** Convolution becomes a product. *Trick:* convolution $\leftrightarrow$ multiplication under the FT.

**Problem 330.** Parseval's (Plancherel's) theorem states $\displaystyle\int|f(x)|^{2}dx\ \propto$
(a) $\displaystyle\int|F(k)|^{2}dk$  (b) $\displaystyle\int F(k)\,dk$  (c) $\Big|\displaystyle\int F(k)\,dk\Big|^{2}$  (d) $\displaystyle\int f(x)\,dx$
> **Ans (a).** Total "energy" is preserved between real and Fourier space. *Trick:* it's the integral of $|F|^2$, not of $F$.

---

# SET 67 — Separable ODE with saturation
**Origin (Q67):** $\dot x=2\sqrt{1-x^2},\ x(0)=0$ gives $x=\sin2t$ until $x=1$ at $t=\tfrac\pi4$, after which $x$ stays at $1$ (an equilibrium where the RHS vanishes). **Twists:** the pre‑saturation solution, the equilibrium, why $x\le1$, the saturation time, the logistic analogue.

**Problem 331.** $\dot x=2\sqrt{1-x^2}$ with $x(0)=0$ gives, before saturation,
(a) $\sin 2t$  (b) $\cos 2t$  (c) $2t$  (d) $\tanh 2t$
> **Ans (a).** Separate: $\dfrac{dx}{\sqrt{1-x^2}}=2\,dt\Rightarrow\arcsin x=2t$. *Trick:* $\arcsin x=2t\Rightarrow x=\sin2t$.

**Problem 332.** $x=1$ is an equilibrium of $\dot x=2\sqrt{1-x^2}$ because
(a) the RHS $=0$ there  (b) the LHS diverges  (c) $x$ grows without bound  (d) it is the initial condition
> **Ans (a).** $\sqrt{1-1}=0\Rightarrow\dot x=0$, so $x$ stops. *Trick:* the solution **saturates** at $x=1$ rather than overshooting (Q67).

**Problem 333.** The real solution of $\dot x=2\sqrt{1-x^2}$ cannot exceed $1$ because
(a) $\sqrt{1-x^2}$ is undefined (imaginary) for $x>1$  (b) the ODE is linear  (c) the initial value is $0$  (d) $t$ is bounded
> **Ans (a).** The square root forces $x\in[-1,1]$. *Trick:* the equation itself caps $x$ at $1$.

**Problem 334.** Starting from $x=0$, the solution $x=\sin2t$ first reaches $x=1$ at
(a) $t=\dfrac\pi4$  (b) $t=\dfrac\pi2$  (c) $t=\pi$  (d) $t=1$
> **Ans (a).** $\sin 2t=1\Rightarrow2t=\dfrac\pi2$. *Trick:* the saturation time is $\pi/4$ (Q67).

**Problem 335.** The logistic equation $\dot x=x(1-x)$ has equilibria at
(a) $x=0$ and $x=1$  (b) $x=1$ only  (c) $x=\pm1$  (d) none
> **Ans (a).** The RHS vanishes at $x=0$ and $x=1$. *Trick:* another saturating ODE — $x=1$ is the carrying capacity.

---

# SET 68 — Hermite ODE ↔ generating‑function PDE
**Origin (Q68):** the Hermite ODE $H_n''-2xH_n'+2nH_n=0$ turns into a PDE for $G(t,x)=\sum H_n t^n/n!$, namely $G_{xx}-2xG_x+2tG_t=0$. **Twists:** the ODE, the $n\to t\partial_t$ translation, Rodrigues, the weight, the recurrence.

**Problem 336.** The Hermite differential equation is
(a) $y''-2xy'+2ny=0$  (b) $y''+2xy'+2ny=0$  (c) $y''-2xy'-2ny=0$  (d) $y''-xy'+ny=0$
> **Ans (a).** Physicists' Hermite ODE. *Trick:* the $-2x$ and $+2n$ are the signature terms.

**Problem 337.** In the generating function $G=\sum H_n t^n/n!$, the term $2nH_n$ of the ODE corresponds to
(a) $2t\,\dfrac{\partial G}{\partial t}$  (b) $2\,\dfrac{\partial G}{\partial t}$  (c) $2nG$  (d) $2G$
> **Ans (a).** $t\partial_t(t^n)=n\,t^n$, so $n\leftrightarrow t\partial_t$. *Trick:* this substitution is the single step that turns Q68's ODE into a PDE.

**Problem 338.** Rodrigues' formula for the Hermite polynomials is $H_n(x)=$
(a) $(-1)^n e^{x^2}\dfrac{d^n}{dx^n}e^{-x^2}$  (b) $e^{x^2}\dfrac{d^n}{dx^n}e^{x^2}$  (c) $\dfrac{d^n}{dx^n}e^{-x^2}$  (d) $e^{-x^2}\dfrac{d^n}{dx^n}e^{x^2}$
> **Ans (a).** The standard Rodrigues form. *Trick:* the $(-1)^n$ and the $e^{+x^2}$ prefactor.

**Problem 339.** Hermite polynomials are orthogonal on $(-\infty,\infty)$ with weight
(a) $e^{-x^2}$  (b) $e^{-x}$  (c) $1$  (d) $1-x^2$
> **Ans (a).** The Gaussian weight. *Trick:* Hermite $\leftrightarrow e^{-x^2}$ (Laguerre would be $e^{-x}$).

**Problem 340.** Using $H_{n+1}=2xH_n-2nH_{n-1}$ with $H_0=1,\,H_1=2x$, $H_3(x)=$
(a) $8x^{3}-12x$  (b) $4x^{2}-2$  (c) $8x^{3}+12x$  (d) $16x^{4}-48x^{2}+12$
> **Ans (a).** $H_2=4x^2-2$, then $H_3=2x(4x^2-2)-4(2x)=8x^3-12x$. *Trick:* apply the recurrence twice; (b) is $H_2$, (d) is $H_4$.

---

# SET 69 — Numerical integration (Simpson's & trapezoidal)
**Origin (Q69):** $\displaystyle\int_0^8\frac{dx}{x^2+5}$ by Simpson's $\tfrac13$ rule with $h=2$. **Twists:** the Simpson formula, the trapezoidal rule, the even‑interval requirement, the weight pattern, the exactness.

**Problem 341.** Simpson's $\tfrac13$ rule over two subintervals (points $x_0,x_1,x_2$) is
(a) $\dfrac h3\big[y_0+4y_1+y_2\big]$  (b) $\dfrac h2\big[y_0+y_1\big]$  (c) $h\big[y_0+y_1+y_2\big]$  (d) $\dfrac h3\big[y_0+2y_1+y_2\big]$
> **Ans (a).** The $1\!-\!4\!-\!1$ weighting with $h/3$. *Trick:* the middle point is weighted $4$.

**Problem 342.** The trapezoidal rule over $[a,b]$ is
(a) $\dfrac{b-a}{2}\big[f(a)+f(b)\big]$  (b) $(b-a)f(a)$  (c) $\dfrac{b-a}{3}\big[f(a)+f(b)\big]$  (d) $(b-a)\big[f(a)+f(b)\big]$
> **Ans (a).** Average of the endpoints times the width. *Trick:* the $\tfrac12$ comes from the trapezoid area.

**Problem 343.** Simpson's $\tfrac13$ rule requires the number of subintervals to be
(a) even  (b) odd  (c) prime  (d) any
> **Ans (a).** It pairs intervals (each parabola spans two). *Trick:* an odd count can't be tiled by these pairs.

**Problem 344.** In composite Simpson's $\tfrac13$ rule, the node weights follow the pattern
(a) $1,4,2,4,2,\dots,4,1$  (b) $1,2,2,\dots,2,1$  (c) $1,1,1,\dots,1$  (d) $1,3,3,1$
> **Ans (a).** Endpoints $1$; odd interior nodes $4$; even interior nodes $2$. *Trick:* the alternating $4,2$ pattern (option b is the trapezoidal pattern).

**Problem 345.** Simpson's $\tfrac13$ rule integrates exactly all polynomials up to degree
(a) $3$  (b) $1$  (c) $2$  (d) $4$
> **Ans (a).** It is exact for cubics. *Trick:* surprisingly one degree beyond the parabola it is built from (the cubic error term cancels by symmetry).

---

# SET 70 — Random walk / self‑avoiding paths
**Origin (Q70):** a walker on a square lattice takes $3$ steps; $P(\text{no site revisited})=\dfrac{4\cdot3\cdot3}{4^3}=\dfrac{9}{16}$. **Twists:** the Q70 count, the total paths, the 2‑step return, the mean displacement, the RMS displacement.

**Problem 346.** A walker on a square lattice takes $3$ steps. The probability that no site is visited more than once is
(a) $\dfrac{9}{16}$  (b) $\dfrac{27}{64}$  (c) $\dfrac38$  (d) $\dfrac12$
> **Ans (a).** $\dfrac{4\cdot3\cdot3}{4^3}=\dfrac{36}{64}=\dfrac{9}{16}$. *Trick:* $4$ choices first, then only $3$ each (can't step back) — Q70.

**Problem 347.** The total number of distinct $3$‑step paths on a square lattice is
(a) $64$  (b) $12$  (c) $81$  (d) $16$
> **Ans (a).** $4^3=64$. *Trick:* $4$ directions per step, $3$ steps.

**Problem 348.** A $2$‑step walk returns to the origin with probability
(a) $\dfrac14$  (b) $\dfrac12$  (c) $\dfrac1{16}$  (d) $0$
> **Ans (a).** Only $1$ of the $4$ second‑step directions reverses the first. *Trick:* $P=\tfrac14$ — the step back is one specific choice.

**Problem 349.** For an unbiased random walk, the **mean** displacement after $N$ steps is
(a) $0$  (b) $N$  (c) $\sqrt N$  (d) $N^2$
> **Ans (a).** Symmetry cancels the vector sum. *Trick:* the *mean* is zero; it's the mean **square** that grows.

**Problem 350.** For an unbiased random walk of $N$ steps with step length $a$, the root‑mean‑square displacement is
(a) $a\sqrt N$  (b) $aN$  (c) $a$  (d) $aN^{2}$
> **Ans (a).** $\langle r^2\rangle=Na^2\Rightarrow r_{\text{rms}}=a\sqrt N$. *Trick:* diffusive $\sqrt N$ scaling — contrast with the zero mean of Q349.

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: $\mathcal L[t^n]=n!/s^{n+1}$ and $\sinh$ gives $s^2-a^2$; zero initial velocity splits a pulse into two half‑amplitude copies; build a target dimension from $h,c,E$ (but never the pure‑number prefactor); $\sinh^{-1}$ has $+1$ under the root while $\tanh^{-1}$/$\coth^{-1}$ are logs of ratios; poles sit at the **zeros of the denominator** (including the imaginary $\pm i\sqrt n$); FT properties — shift $\to$ phase, scale $\to1/|a|$, convolution $\to$ product; a separable ODE **saturates** at an equilibrium where its RHS vanishes; the Hermite ODE becomes a PDE via $n\leftrightarrow t\partial_t$; Simpson is exact for cubics and needs an even number of intervals; and a random walk has zero mean but $\sqrt N$ RMS. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 350 problems across the first 70 originals (Q1–Q70).**
