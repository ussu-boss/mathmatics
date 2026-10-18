# 50 Practice Problems — Part 7 (CSIR‑NET/JRF style)

**Built from problems 61–70 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **301–350** to continue Parts 1–6.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q61–Q62 = June 2015**, **Q63–Q70 = Dec 2015** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q61–Q70)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q61 | Integral transforms | Laplace transforms of $t^n$ and $\sin at$ |
| Q62 | PDEs | d'Alembert solution (zero initial velocity) |
| Q63 | Dimensional analysis | Building a quantity from $E,h,c$ |
| Q64 | Functions | Inverse hyperbolic functions ($\coth,\tanh$) |
| Q65 | Complex analysis | Poles and their **orders** |
| Q66 | Integral transforms | Fourier transform of $\delta$ and its derivatives |
| Q67 | ODEs | Separable nonlinear ODE with **saturation** |
| Q68 | Special functions | Hermite generating function & its PDE |
| Q69 | Numerical methods | Numerical integration (Simpson's $\tfrac13$ rule) |
| Q70 | Probability | Random walks / self‑avoiding walks |

---

# SET 61 — Laplace transforms of standard functions
**Origin (Q61):** $\mathcal L[6t^3+3\sin 4t]=\dfrac{36}{s^4}+\dfrac{12}{s^2+16}$, using $\mathcal L[t^n]=\dfrac{n!}{s^{n+1}}$ and $\mathcal L[\sin at]=\dfrac{a}{s^2+a^2}$. **Twists:** $t^n$, sine vs cosine, exponential, sinh/cosh, multiplication by $t$.

**Problem 301.** $\mathcal L[t^{3}]=$
(a) $\dfrac{6}{s^4}$  (b) $\dfrac{3}{s^4}$  (c) $\dfrac{6}{s^3}$  (d) $\dfrac{1}{s^4}$
> **Ans (a).** $\mathcal L[t^n]=\dfrac{n!}{s^{n+1}}$, so $t^3\to\dfrac{3!}{s^4}=\dfrac6{s^4}$. *Trick:* the factorial — $3!=6$, not $3$.

**Problem 302.** $\mathcal L[\cos 4t]=$
(a) $\dfrac{s}{s^2+16}$  (b) $\dfrac{4}{s^2+16}$  (c) $\dfrac{s}{s^2-16}$  (d) $\dfrac{4}{s^2-16}$
> **Ans (a).** Cosine has $s$ in the numerator. *Trick:* $\cos\to s/(s^2+a^2)$, whereas $\sin\to a/(s^2+a^2)$ (the $a$ in Q61).

**Problem 303.** $\mathcal L[e^{2t}]=$
(a) $\dfrac{1}{s-2}$  (b) $\dfrac{1}{s+2}$  (c) $\dfrac{2}{s-2}$  (d) $\dfrac1s$
> **Ans (a).** Pole at $s=a$. *Trick:* $e^{at}\to1/(s-a)$ — sign of the shift matters.

**Problem 304.** $\mathcal L[\sinh 4t]=$
(a) $\dfrac{4}{s^2-16}$  (b) $\dfrac{4}{s^2+16}$  (c) $\dfrac{s}{s^2-16}$  (d) $\dfrac{s}{s^2+16}$
> **Ans (a).** Hyperbolic sine gives $s^2-a^2$. *Trick:* the **minus** sign — $\sinh\to a/(s^2-a^2)$ vs $\sin\to a/(s^2+a^2)$.

**Problem 305.** $\mathcal L[t\,e^{2t}]=$
(a) $\dfrac{1}{(s-2)^2}$  (b) $\dfrac{1}{s-2}$  (c) $\dfrac{2}{(s-2)^2}$  (d) $\dfrac{1}{(s+2)^2}$
> **Ans (a).** Multiplying by $t$ differentiates $F(s)$: $\mathcal L[t f]=-\dfrac{dF}{ds}$. *Trick:* applied to $1/(s-2)$ gives $1/(s-2)^2$.

---

# SET 62 — d'Alembert solution of the wave equation
**Origin (Q62):** with $u(x,0)=\phi(x)$ and zero initial velocity, $u(x,t)=\tfrac12[\phi(x-vt)+\phi(x+vt)]$ — a Gaussian splits into two half‑pulses. **Twists:** the zero‑velocity formula, the general formula, pulse splitting, a one‑way launch, the speed.

**Problem 306.** For $u_{tt}=v^2u_{xx}$ with $u(x,0)=\phi(x)$ and $u_t(x,0)=0$, the solution is
(a) $\tfrac12[\phi(x-vt)+\phi(x+vt)]$  (b) $\phi(x-vt)$  (c) $\phi(x+vt)$  (d) $\phi(x)\cos(vt)$
> **Ans (a).** Zero initial velocity ⇒ symmetric split. *Trick:* each travelling copy carries **half** the amplitude (Q62).

**Problem 307.** With a nonzero initial velocity $\psi(x)$, d'Alembert's solution adds
(a) $\tfrac{1}{2v}\displaystyle\int_{x-vt}^{x+vt}\psi(s)\,ds$  (b) $\psi(x)\,t$  (c) nothing  (d) $\psi(x-vt)$
> **Ans (a).** The velocity contributes an integral term. *Trick:* it vanishes in Q62 because $\psi=0$, leaving only the half‑pulses.

**Problem 308.** An initial localized bump released **from rest** evolves into
(a) two half‑amplitude pulses moving in $\pm$ directions  (b) one pulse moving right  (c) a standing wave  (d) a decaying bump
> **Ans (a).** Symmetric splitting. *Trick:* the $\tfrac12$ factors mean each pulse is half as tall (Q62).

**Problem 309.** If $u(x,0)=\phi(x)$ and $u_t(x,0)=-v\phi'(x)$, the solution is
(a) $\phi(x-vt)$  (b) $\phi(x+vt)$  (c) $\tfrac12[\phi(x-vt)+\phi(x+vt)]$  (d) $\phi(x)$
> **Ans (a).** This special velocity launches a pure **right‑moving** wave. *Trick:* a tuned initial velocity suppresses the left‑mover entirely.

**Problem 310.** In Q62 the two pulses travel with speed
(a) $v$  (b) $2v$  (c) $v/2$  (d) $1$
> **Ans (a).** The arguments $x\pm vt$ move at speed $v$. *Trick:* the wave speed is $v$, the square root of the coefficient.

---

# SET 63 — Dimensional analysis
**Origin (Q63):** the cross‑section $\sigma$ (area, $L^2$) built from $E,h,c$ is $\big(\tfrac{hc}{E}\big)^2$; $[h]=ML^2T^{-1}$, $[c]=LT^{-1}$, $[E]=ML^2T^{-2}$. **Twists:** dimension of $h$, the $hc/E$ scale, a pendulum, an oscillator energy, the limits of the method.

**Problem 311.** The dimension of Planck's constant $h$ (energy $\times$ time) is
(a) $ML^{2}T^{-1}$  (b) $ML^{2}T^{-2}$  (c) $MLT^{-1}$  (d) $ML^{2}T$
> **Ans (a).** $[h]=[E][t]=(ML^2T^{-2})(T)=ML^2T^{-1}$. *Trick:* energy $\times$ time, not energy alone.

**Problem 312.** The dimension of $\dfrac{hc}{E}$ is
(a) $L$  (b) $L^{2}$  (c) $T$  (d) dimensionless
> **Ans (a).** $\dfrac{(ML^2T^{-1})(LT^{-1})}{ML^2T^{-2}}=L$. *Trick:* this is a length (the Compton scale); squaring it gives Q63's area.

**Problem 313.** By dimensional analysis, the period of a simple pendulum depends on length $L$ and gravity $g$ as
(a) $\sqrt{L/g}$  (b) $L/g$  (c) $\sqrt{Lg}$  (d) $g/L$
> **Ans (a).** $[\sqrt{L/g}]=\sqrt{L/(LT^{-2})}=T$. *Trick:* only $\sqrt{L/g}$ has the dimension of time.

**Problem 314.** A quantity with the dimension of energy built from mass $m$, frequency $\omega$, and amplitude $x_0$ is
(a) $m\omega^{2}x_0^{2}$  (b) $m\omega x_0$  (c) $m\omega^{2}x_0$  (d) $m\omega x_0^{2}$
> **Ans (a).** $[m\omega^2x_0^2]=M(T^{-1})^2L^2=ML^2T^{-2}$. *Trick:* this is the oscillator energy scale.

**Problem 315.** Dimensional analysis **cannot** determine
(a) dimensionless prefactors (e.g. $2\pi$, $\tfrac12$)  (b) the powers of the variables  (c) the units of the result  (d) which variables matter
> **Ans (a).** It fixes the form up to a pure number. *Trick:* the numerical constant always escapes dimensional analysis.

---

# SET 64 — Inverse hyperbolic functions
**Origin (Q64):** $y=\coth x=\tfrac1{\tanh x}\Rightarrow x=\tfrac12\ln\tfrac{y+1}{y-1}=\ln\sqrt{\tfrac{y+1}{y-1}}$. **Twists:** $\tanh^{-1}$, $\sinh^{-1}$, $\cosh^{-1}$, the Pythagorean identity, the derivative of $\tanh$.

**Problem 316.** The inverse of $y=\tanh x$ is
(a) $\tfrac12\ln\dfrac{1+y}{1-y}$  (b) $\tfrac12\ln\dfrac{y+1}{y-1}$  (c) $\ln(1+y)$  (d) $\tfrac12\ln\dfrac{1-y}{1+y}$
> **Ans (a).** $\tanh^{-1}y=\tfrac12\ln\tfrac{1+y}{1-y}$. *Trick:* $\tanh^{-1}$ uses $\tfrac{1+y}{1-y}$; $\coth^{-1}$ (Q64) uses $\tfrac{y+1}{y-1}$.

**Problem 317.** $\sinh^{-1}y=$
(a) $\ln\!\big(y+\sqrt{y^{2}+1}\big)$  (b) $\ln\!\big(y+\sqrt{y^{2}-1}\big)$  (c) $\ln\!\big(y-\sqrt{y^{2}+1}\big)$  (d) $\ln\sqrt{y^{2}+1}$
> **Ans (a).** $+1$ under the root. *Trick:* arcsinh has $+1$; arccosh has $-1$.

**Problem 318.** $\cosh^{-1}y=$ (for $y\ge1$)
(a) $\ln\!\big(y+\sqrt{y^{2}-1}\big)$  (b) $\ln\!\big(y+\sqrt{y^{2}+1}\big)$  (c) $\ln\!\big(y-\sqrt{y^{2}-1}\big)$  (d) $\tfrac12\ln y$
> **Ans (a).** $-1$ under the root. *Trick:* the sign distinguishes it from arcsinh (Q317).

**Problem 319.** $\cosh^{2}x-\sinh^{2}x=$
(a) $1$  (b) $-1$  (c) $\cosh 2x$  (d) $0$
> **Ans (a).** The hyperbolic Pythagorean identity. *Trick:* it's a **minus** sign (unlike $\sin^2+\cos^2=1$).

**Problem 320.** $\dfrac{d}{dx}\tanh x=$
(a) $\operatorname{sech}^{2}x$  (b) $\operatorname{sech}x\tanh x$  (c) $\cosh^{2}x$  (d) $-\operatorname{csch}^{2}x$
> **Ans (a).** $\tanh'=\operatorname{sech}^2x=1-\tanh^2x$. *Trick:* the analogue of $\sec^2x$ for $\tan$.

---

# SET 65 — Poles and their orders
**Origin (Q65):** $\dfrac{z}{\sin\pi z^2}$ has a **simple** pole at $z=0$ (denominator's double zero minus the numerator's simple zero) and poles at the zeros of $\sin\pi z^2$, namely $z^2=n\Rightarrow z=\pm\sqrt n,\pm i\sqrt n$. **Twists:** the order rule, the zero locations, a cancelled pole, a genuine double pole, $\tan z$.

**Problem 321.** For $\dfrac{z}{\sin\pi z^2}$ at $z=0$: $\sin\pi z^2\sim\pi z^2$ (double zero) and the numerator has a simple zero, so the pole order is
(a) $1$ (simple pole)  (b) $2$  (c) $3$  (d) removable
> **Ans (a).** Pole order $=$ (denominator zero order) $-$ (numerator zero order) $=2-1=1$. *Trick:* the numerator's $z$ cancels one power, leaving a **simple** pole.

**Problem 322.** $\sin\pi z^2=0$ at
(a) $z=\pm\sqrt n$ and $\pm i\sqrt n$  (b) $z=\pm n$  (c) $z=\pm\sqrt n$ only  (d) $z=n\pi$
> **Ans (a).** $z^2=n$ gives real $\pm\sqrt n$; $z^2=-n$ gives imaginary $\pm i\sqrt n$. *Trick:* don't forget the imaginary roots (Q65's option (b)).

**Problem 323.** $\dfrac{\sin z}{z^{2}}$ at $z=0$ has a pole of order
(a) $1$ (simple)  (b) $2$  (c) removable  (d) $3$
> **Ans (a).** $\sin z\sim z$ (simple zero) cancels one power of $z^2$. *Trick:* the numerator's zero drops the order from $2$ to $1$.

**Problem 324.** $\dfrac{1}{(z^{2}+1)^{2}}$ at $z=i$ has a pole of order
(a) $2$  (b) $1$  (c) $4$  (d) removable
> **Ans (a).** $(z^2+1)^2=(z-i)^2(z+i)^2$. *Trick:* a genuine order‑2 pole (nothing in the numerator cancels it).

**Problem 325.** $\tan z=\dfrac{\sin z}{\cos z}$ has poles
(a) of order $1$, at $z=(n+\tfrac12)\pi$  (b) of order $2$, at $z=n\pi$  (c) of order $1$, at $z=n\pi$  (d) of order $2$, at $z=(n+\tfrac12)\pi$
> **Ans (a).** $\cos z$ has simple zeros at odd multiples of $\pi/2$. *Trick:* simple zeros of the denominator ⇒ simple poles.

---

# SET 66 — Fourier transform of $\delta$ and its derivatives
**Origin (Q66):** with $\tilde f(k)=\int f e^{ikx}dx$, $\mathcal F[\alpha\delta+\beta\delta'+\gamma\delta'']=\alpha-i\beta k-\gamma k^2$. **Twists:** the general $\delta^{(n)}$ rule, $\delta'$, $\delta''$, assembling a combination, the inverse view.

**Problem 326.** With the convention $\int f\,e^{ikx}dx$, $\mathcal F[\delta^{(n)}(x)]=$
(a) $(-ik)^{n}$  (b) $(ik)^{n}$  (c) $k^{n}$  (d) $n!$
> **Ans (a).** $\int\delta^{(n)}g\,dx=(-1)^n g^{(n)}(0)$ with $g=e^{ikx}$ gives $(-1)^n(ik)^n=(-ik)^n$. *Trick:* the systematic pattern behind Q66.

**Problem 327.** $\mathcal F[\delta'(x)]=$ (same convention)
(a) $-ik$  (b) $ik$  (c) $k$  (d) $1$
> **Ans (a).** One integration by parts gives $-ik$. *Trick:* this is Q66's $\beta$ term, $-i\beta k$.

**Problem 328.** $\mathcal F[\delta''(x)]=$
(a) $-k^{2}$  (b) $k^{2}$  (c) $-ik$  (d) $ik$
> **Ans (a).** $(-ik)^2=-k^2$. *Trick:* Q66's $\gamma$ term, $-\gamma k^2$.

**Problem 329.** $\mathcal F[2\delta(x)+3\delta'(x)]=$
(a) $2-3ik$  (b) $2+3ik$  (c) $2-3k$  (d) $5$
> **Ans (a).** Linearity: $2(1)+3(-ik)=2-3ik$. *Trick:* combine the individual transforms (the structure of Q66).

**Problem 330.** If $F(k)=a+bk+ck^{2}$ (a polynomial in $k$), then $f(x)$ is
(a) a combination of $\delta,\delta',\delta''$  (b) a Gaussian  (c) a constant  (d) $e^{ikx}$
> **Ans (a).** A polynomial spectrum corresponds to delta‑derivative terms. *Trick:* this is Q66 read backwards.

---

# SET 67 — Separable nonlinear ODEs with saturation
**Origin (Q67):** $\dot x=2\sqrt{1-x^2},\ x(0)=0\Rightarrow x=\sin 2t$ until $x=1$ (at $t=\pi/4$), after which $x\equiv1$ (since $\dot x=0$ there). **Twists:** the separation, the saturation, why it sticks, equilibria of the logistic ODE, another separation.

**Problem 331.** Separating $\dot x=2\sqrt{1-x^2}$ gives
(a) $\arcsin x=2t$  (b) $\arccos x=2t$  (c) $x=2t^{2}$  (d) $\ln x=2t$
> **Ans (a).** $\displaystyle\int\frac{dx}{\sqrt{1-x^2}}=\arcsin x$. *Trick:* recognize the arcsine integral.

**Problem 332.** The solution $x=\sin 2t$ is valid only for
(a) $0\le t<\pi/4$ (then $x$ stays at $1$)  (b) all $t$  (c) $t>\pi/4$  (d) $t<\pi/2$
> **Ans (a).** Once $x=1$, $\sqrt{1-x^2}=0$ so $\dot x=0$ and $x$ sticks. *Trick:* $x$ cannot exceed $1$ — it saturates (Q67).

**Problem 333.** The value $x=1$ is an equilibrium of $\dot x=2\sqrt{1-x^2}$ because
(a) $\dot x=0$ there  (b) $x=1$ maximizes $t$  (c) the ODE is undefined at $x=1$  (d) $x=1$ is unstable
> **Ans (a).** The rate vanishes at $x=1$. *Trick:* a fixed point is where $\dot x=0$ — the solution can only approach it.

**Problem 334.** The equilibria of the logistic equation $\dot x=x(1-x)$ are
(a) $x=0$ and $x=1$  (b) $x=1$ only  (c) $x=0$ only  (d) none
> **Ans (a).** $\dot x=0\Rightarrow x(1-x)=0$. *Trick:* set the right‑hand side to zero to find fixed points.

**Problem 335.** Separating $\dot x=x$ gives
(a) $\ln x=t+C$  (b) $x=t+C$  (c) $x^{2}=2t$  (d) $\arcsin x=t$
> **Ans (a).** $\displaystyle\int\frac{dx}{x}=\ln x$. *Trick:* exponential growth ($x=Ae^t$), the simplest separable case.

---

# SET 68 — Hermite generating function & its PDE
**Origin (Q68):** $G(t,x)=\sum_n\tfrac1{n!}H_n(x)t^n$ satisfies $\partial^2_xG-2x\,\partial_xG+2t\,\partial_tG=0$, built from Hermite's ODE. **Twists:** Hermite's ODE, the generating function, the role of $\partial_t$, the derivative recurrence, the PDE.

**Problem 336.** The Hermite polynomial $H_n(x)$ satisfies
(a) $H''-2xH'+2nH=0$  (b) $H''+2xH'+2nH=0$  (c) $H''-xH'+nH=0$  (d) $H''+H=0$
> **Ans (a).** The physicists' Hermite equation. *Trick:* the $-2x$ and $+2n$ — Q68 reconstructs exactly this term by term.

**Problem 337.** The generating function of the Hermite polynomials is
(a) $e^{2xt-t^{2}}$  (b) $e^{-t^{2}+t}$  (c) $(1-2xt+t^{2})^{-1/2}$  (d) $e^{xt}$
> **Ans (a).** $G(t,x)=e^{2xt-t^2}$. *Trick:* option (c) is the **Legendre** generating function — don't confuse the two.

**Problem 338.** In the PDE for $G$, the operator $\partial_t$ acting on $\sum_n H_n\tfrac{t^n}{n!}$ brings down a factor of
(a) $n$  (b) $n!$  (c) $t$  (d) $1$
> **Ans (a).** $\partial_t\big(t^n/n!\big)=t^{n-1}/(n-1)!$, i.e. a factor $n$. *Trick:* this $n$ becomes the $2n$ in Hermite's equation.

**Problem 339.** Differentiating $G=e^{2xt-t^2}$ in $x$ gives $\partial_xG=2tG$, which yields
(a) $H_n'(x)=2n\,H_{n-1}(x)$  (b) $H_n'=H_{n-1}$  (c) $H_n'=2H_n$  (d) $H_n'=n\,H_n$
> **Ans (a).** The derivative recurrence. *Trick:* $\partial_xG=2tG$ generates $H_n'=2nH_{n-1}$.

**Problem 340.** The Hermite generating function $G$ satisfies the PDE
(a) $\partial^2_xG-2x\,\partial_xG+2t\,\partial_tG=0$  (b) $\partial^2_xG+2x\,\partial_xG=0$  (c) $\partial_tG=\partial^2_xG$  (d) $\partial^2_xG-2x\,\partial_xG+2\,\partial_x\partial_tG=0$
> **Ans (a).** Substituting the series and using Hermite's ODE term by term. *Trick:* the $2t\,\partial_t$ (not $2\partial_x\partial_t$) is the correct closure — Q68.

---

# SET 69 — Numerical integration (Simpson's rule)
**Origin (Q69):** $\int_0^8\frac{dx}{x^2+5}$ by Simpson's $\tfrac13$ rule with $h=2$ (five points) $\approx0.59$. **Twists:** the Simpson formula, the trapezoidal formula, the interval‑count requirement, Simpson's accuracy, trapezoidal accuracy.

**Problem 341.** Simpson's $\tfrac13$ rule for $\int$ over points $y_0,\dots,y_4$ (spacing $h$) is
(a) $\dfrac h3[y_0+4y_1+2y_2+4y_3+y_4]$  (b) $\dfrac h2[y_0+2y_1+2y_2+2y_3+y_4]$  (c) $h[y_0+y_1+y_2+y_3+y_4]$  (d) $\dfrac h3[y_0+y_1+y_2+y_3+y_4]$
> **Ans (a).** Weight pattern $1,4,2,4,1$ with $h/3$. *Trick:* the alternating $4,2,4$ interior weights are the signature of Simpson's rule.

**Problem 342.** The trapezoidal rule for $\int$ is
(a) $\dfrac h2[y_0+2y_1+\cdots+2y_{n-1}+y_n]$  (b) $\dfrac h3[1,4,2,\dots]$  (c) $h\sum y_i$  (d) $\dfrac h2[y_0+y_n]$
> **Ans (a).** Weights $1,2,2,\dots,2,1$ with $h/2$. *Trick:* trapezoidal uses $h/2$ and weight $2$ on interior points — distinct from Simpson's.

**Problem 343.** Simpson's $\tfrac13$ rule requires the number of intervals to be
(a) even  (b) odd  (c) a multiple of $3$  (d) any number
> **Ans (a).** It pairs intervals into parabolic arcs. *Trick:* an **even** number of intervals (odd number of points) is mandatory.

**Problem 344.** Simpson's $\tfrac13$ rule integrates exactly all polynomials up to degree
(a) $3$  (b) $1$  (c) $2$  (d) $4$
> **Ans (a).** Surprisingly, it is exact for cubics too. *Trick:* although built from parabolas (degree 2), the symmetry makes it exact through degree $3$.

**Problem 345.** The trapezoidal rule integrates exactly all polynomials up to degree
(a) $1$  (b) $2$  (c) $3$  (d) $0$
> **Ans (a).** It matches straight lines. *Trick:* degree $1$ only — far less accurate than Simpson's degree $3$.

---

# SET 70 — Random walks / self‑avoiding walks
**Origin (Q70):** a walker on a square lattice (4 neighbours) takes 3 steps; $P(\text{no site revisited})=\dfrac{4\cdot3\cdot3}{4^3}=\dfrac9{16}$. **Twists:** the path count, the Q70 probability, a return probability, mean displacement, RMS (diffusion).

**Problem 346.** A walker on a square lattice taking $3$ steps (4 choices each) has how many total paths?
(a) $64$  (b) $12$  (c) $48$  (d) $4$
> **Ans (a).** $4^3=64$. *Trick:* $4$ choices per step, independent — the denominator of Q70.

**Problem 347.** The probability that a $3$‑step square‑lattice walk never revisits a site is
(a) $\dfrac9{16}$  (b) $\dfrac38$  (c) $\dfrac{27}{64}$  (d) $\dfrac12$
> **Ans (a).** $\dfrac{4\cdot3\cdot3}{64}=\dfrac9{16}$. *Trick:* the first step has $4$ choices, each later step only $3$ (can't reverse).

**Problem 348.** A walker takes $2$ steps on a square lattice. The probability of returning to the origin is
(a) $\dfrac14$  (b) $\dfrac12$  (c) $\dfrac1{16}$  (d) $\dfrac18$
> **Ans (a).** Step 2 must reverse step 1: $\dfrac{4\cdot1}{16}=\dfrac14$. *Trick:* exactly one of the four second‑step directions returns to start.

**Problem 349.** For an unbiased random walk, the **mean** displacement $\langle x\rangle$ after $N$ steps is
(a) $0$  (b) $N$  (c) $\sqrt N$  (d) $N/2$
> **Ans (a).** By symmetry, positive and negative steps cancel. *Trick:* the mean is zero — it's the spread that grows.

**Problem 350.** For an unbiased random walk of step length $a$, the root‑mean‑square displacement after $N$ steps scales as
(a) $\sqrt N\,a$  (b) $N a$  (c) $a$  (d) $N^{2}a$
> **Ans (a).** $\langle x^2\rangle=Na^2$, so RMS $\propto\sqrt N$. *Trick:* diffusive ($\sqrt N$) scaling, not ballistic ($N$).

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: $\mathcal L[t^n]=n!/s^{n+1}$ and $\sinh\to s^2-a^2$ (minus); zero initial velocity splits a pulse into two half‑amplitude copies; dimensional analysis gives the form but never the prefactor; arcsinh has $+1$, arccosh has $-1$ under the root; pole order $=$ (denominator zero) $-$ (numerator zero); $\mathcal F[\delta^{(n)}]=(-ik)^n$; a separable ODE can **saturate** at an equilibrium; the Hermite generating function obeys a $2t\,\partial_t$ PDE; Simpson's rule (weights $1,4,2,4,1$, even intervals) is exact through cubics; and a random walk has zero mean but $\sqrt N$ RMS displacement. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 350 problems across the first 70 originals (Q1–Q70).**
