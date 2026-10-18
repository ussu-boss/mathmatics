# 50 Practice Problems — Part 4 (CSIR‑NET/JRF style)

**Built from problems 31–40 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **151–200** to continue Parts 1–3.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q31–Q36 = June 2013**, **Q37–Q40 = Dec 2013** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q31–Q40)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q31 | Vector algebra | Dot product / angle with a **non‑orthogonal** pair |
| Q32 | Complex analysis | Which function is **not** analytic ($z$ vs $\bar z$) |
| Q33 | PDEs | 1‑D wave equation; separation of variables; normal modes |
| Q34 | ODEs | First‑order nonlinear; **finite‑time blow‑up** |
| Q35 | Integral transforms | Inverse Laplace transform |
| Q36 | Approximations | Small‑angle accuracy of $\cos\theta\approx1$ |
| Q37 | Vector calculus | Line integral / Stokes; **conservative** field ($\nabla\times\vec A=0$) |
| Q38 | Operators | Hermitian operators & commutators |
| Q39 | Complex analysis | Which $u$ can be $\operatorname{Re}f$ (**harmonic**?) |
| Q40 | Vector calculus | Laplacian **Green's function** / fundamental solution |

---

# SET 31 — Dot product & angle (non‑orthogonal vectors)
**Origin (Q31):** $\hat n$ at $120^\circ$ to $\hat i$, so $\hat n\!\cdot\!\hat i=\cos120^\circ=-\tfrac12$; the $60^\circ$ condition between $a\hat i+b\hat n$ and $a\hat n+b\hat i$ gives $b=\tfrac a2$. **Twists:** a basic angle, the $-\tfrac12$ overlap, the law‑of‑cosines magnitude, a hidden perpendicularity, a projection.

**Problem 151.** The angle between $(1,0)$ and $(1,1)$ is
(a) $45^\circ$  (b) $30^\circ$  (c) $60^\circ$  (d) $90^\circ$
> **Ans (a).** $\cos\theta=\dfrac{1}{\sqrt2}$. *Trick:* $\cos\theta=\dfrac{\vec u\cdot\vec v}{|\vec u||\vec v|}$ — the workhorse formula behind Q31.

**Problem 152.** Two unit vectors make an angle of $120^\circ$; their dot product is
(a) $-\tfrac12$  (b) $\tfrac12$  (c) $-\tfrac{\sqrt3}{2}$  (d) $0$
> **Ans (a).** $\cos120^\circ=-\tfrac12$. *Trick:* this $-\tfrac12$ overlap ($\hat n\!\cdot\!\hat i$) is exactly what makes Q31's algebra non‑trivial.

**Problem 153.** If $\hat n$ is at $120^\circ$ to $\hat i$, then $|a\hat i+b\hat n|=$
(a) $\sqrt{a^2-ab+b^2}$  (b) $\sqrt{a^2+ab+b^2}$  (c) $a+b$  (d) $\sqrt{a^2+b^2}$
> **Ans (a).** $|a\hat i+b\hat n|^2=a^2+b^2+2ab\cos120^\circ=a^2+b^2-ab$. *Trick:* the cross term is $2ab\cos120^\circ=-ab$, not zero.

**Problem 154.** With $\hat n$ a unit vector (any direction), the vectors $\hat i+\hat n$ and $\hat i-\hat n$ have dot product
(a) $0$ (perpendicular)  (b) $1$  (c) $-1$  (d) $\tfrac12$
> **Ans (a).** $(\hat i+\hat n)\!\cdot\!(\hat i-\hat n)=|\hat i|^2-|\hat n|^2=1-1=0$. *Trick:* two **unit** vectors' sum and difference are always perpendicular — independent of the angle.

**Problem 155.** The component of a unit vector $\hat b$ along a unit vector $\hat a$, with $60^\circ$ between them, is
(a) $\tfrac12$  (b) $\tfrac{\sqrt3}{2}$  (c) $1$  (d) $0$
> **Ans (a).** Projection $=\cos60^\circ=\tfrac12$. *Trick:* for unit vectors the scalar projection is just $\cos\theta$.

---

# SET 32 — Which function is NOT analytic ($z$ vs $\bar z$)
**Origin (Q32):** $(1-x+iy)^4(2+x+iy)^6$ is **not** analytic because $1-x+iy=1-\bar z$. **Twists:** spotting $\bar z$, $|z|^2$ differentiability, closure under products, a disguised conjugate, $\operatorname{Im}(z)$.

**Problem 156.** Which is **not** analytic?
(a) $(x-iy)^2$  (b) $(x+iy)^2$  (c) $(x+iy)^3$  (d) $e^{x+iy}$
> **Ans (a).** $x-iy=\bar z$. *Trick:* any genuine appearance of $\bar z$ breaks analyticity, even disguised as $(x-iy)$.

**Problem 157.** The function $f(z)=|z|^{2}$ is differentiable
(a) only at $z=0$  (b) everywhere  (c) nowhere  (d) on the real axis
> **Ans (a).** With $u=x^2+y^2,\ v=0$, the Cauchy–Riemann equations hold only at the origin. *Trick:* differentiable at a single point ≠ analytic — $|z|^2$ is **nowhere** analytic.

**Problem 158.** If $f$ and $g$ are analytic in a domain, then $fg$ is
(a) analytic  (b) not analytic  (c) analytic only if real  (d) harmonic
> **Ans (a).** Products (and sums) of analytic functions are analytic. *Trick:* this closure is why Q32's options are built as products of factors — each factor's analyticity is what matters.

**Problem 159.** Which is **not** analytic?
(a) $x-iy+3$  (b) $(x+iy)^2$  (c) $e^{x}(\cos y+i\sin y)$  (d) $(x+iy-5)^7$
> **Ans (a).** $x-iy=\bar z$; adding $3$ doesn't fix it. *Trick:* (c) is $e^z$ in disguise (analytic); only (a) hides a conjugate.

**Problem 160.** The function $f(z)=\operatorname{Im}(z)=y$ is
(a) analytic nowhere  (b) entire  (c) analytic in the upper half‑plane  (d) harmonic and analytic
> **Ans (a).** $y=\dfrac{z-\bar z}{2i}$ depends on $\bar z$. *Trick:* $\operatorname{Re}(z),\operatorname{Im}(z),|z|,\bar z$ are all nowhere analytic.

---

# SET 33 — Wave equation, separation of variables, normal modes
**Origin (Q33):** $u_{tt}-u_{xx}=0$, fixed ends, superposes the $n=1$ mode (from $u(x,0)$) and the $n=2$ mode (from $u_t(x,0)$). **Twists:** wave speed, mode frequencies, the spatial eigenfunctions, d'Alembert, which mode an IC excites.

**Problem 161.** The equation $u_{tt}-4u_{xx}=0$ describes waves of speed
(a) $2$  (b) $4$  (c) $\tfrac12$  (d) $\sqrt2$
> **Ans (a).** $c^2=4\Rightarrow c=2$. *Trick:* the speed is the square root of the coefficient — $2$, not $4$.

**Problem 162.** For a string of length $L$ (fixed ends, speed $c$), the allowed angular frequencies are
(a) $\dfrac{n\pi c}{L}$  (b) $\dfrac{n\pi}{L}$  (c) $\dfrac{nc}{L}$  (d) $\dfrac{\pi c}{L}$
> **Ans (a).** $\omega_n=ck_n=\dfrac{n\pi c}{L}$. *Trick:* the $\sin(n\pi x/L)$ modes fix the wavenumbers, and $\omega=ck$.

**Problem 163.** The spatial normal modes of the wave equation with zero (fixed) ends at $0$ and $L$ are
(a) $\sin(n\pi x/L)$  (b) $\cos(n\pi x/L)$  (c) $e^{nx}$  (d) $x^{n}$
> **Ans (a).** Zero boundary values pick out sines. *Trick:* fixed ends ⇒ sines; **free** ends would give cosines.

**Problem 164.** d'Alembert's solution of $u_{tt}=c^2u_{xx}$ (infinite string) is
(a) $f(x-ct)+g(x+ct)$  (b) $f(x)g(t)$  (c) $f(x-ct)$ only  (d) $f(x)+g(t)$
> **Ans (a).** A right‑mover plus a left‑mover. *Trick:* the general 1‑D wave is a superposition of both travelling directions.

**Problem 165.** In Q33, the initial velocity $\sin(2\pi x/L)$ excites which spatial mode?
(a) $n=2$  (b) $n=1$  (c) $n=4$  (d) all modes
> **Ans (a).** By orthogonality, $\sin(2\pi x/L)$ is purely the $n=2$ mode. *Trick:* each Fourier mode is driven independently — that's why Q33's answer carries an $\tfrac{L}{2\pi}$ factor on the $n=2$ sine.

---

# SET 34 — First‑order nonlinear ODE & finite‑time blow‑up
**Origin (Q34):** $\dot x=x^2,\ x(0)=1\Rightarrow x=\dfrac{1}{1-t}$, which blows up at $t=1$. **Twists:** another IC, the general blow‑up time, the linear (no‑blow‑up) contrast, the integration step, the decaying sign.

**Problem 166.** $\dot x=x^{2}$ with $x(0)=2$ blows up as $t\to$
(a) $\tfrac12$  (b) $2$  (c) $1$  (d) $\infty$
> **Ans (a).** $x=\dfrac{1}{\tfrac12-t}$, singular at $t=\tfrac12$. *Trick:* the blow‑up time is $1/x_0=\tfrac12$ — a larger start blows up **sooner**.

**Problem 167.** For $\dot x=x^{2}$ with $x(0)=x_0>0$, the blow‑up time is
(a) $\dfrac1{x_0}$  (b) $x_0$  (c) $\infty$  (d) $1$
> **Ans (a).** $x=\dfrac{x_0}{1-x_0t}$, singular at $t=1/x_0$. *Trick:* the nonlinearity forces a singularity in **finite** time.

**Problem 168.** $\dot x=x$ with $x(0)=1$ has solution
(a) $e^{t}$, finite for all finite $t$  (b) $\dfrac{1}{1-t}$  (c) blows up at $t=1$  (d) a constant
> **Ans (a).** Linear growth gives $e^t$. *Trick:* a **linear** equation never blows up in finite time — only the quadratic $x^2$ term does (the key contrast with Q34).

**Problem 169.** Integrating $\displaystyle\int\frac{dx}{x^{2}}$ gives
(a) $-\dfrac1x$  (b) $\ln x$  (c) $\dfrac{x^3}{3}$  (d) $\dfrac1x$
> **Ans (a).** $\displaystyle\int x^{-2}dx=-x^{-1}$. *Trick:* the power rule, not the logarithm (that's $\int dx/x$).

**Problem 170.** $\dot x=-x^{2}$ with $x(0)=1$ gives
(a) $\dfrac{1}{1+t}$  (b) $\dfrac{1}{1-t}$  (c) $e^{-t}$  (d) $-\dfrac{1}{1+t}$
> **Ans (a).** $\dfrac1x=t+1\Rightarrow x=\dfrac{1}{1+t}\to0$. *Trick:* the minus sign turns blow‑up into a graceful decay to zero.

---

# SET 35 — Inverse Laplace transforms
**Origin (Q35):** $\mathcal L^{-1}\!\big[\tfrac{1}{s^2(s+1)}\big]=t-1+e^{-t}$ via partial fractions. **Twists:** the exponential pair, $1/s^2$, the Q35 partial fractions, $1/(s^2+a^2)$, the $s$‑shift.

**Problem 171.** $\mathcal L^{-1}\!\Big[\dfrac{1}{s+a}\Big]=$
(a) $e^{-at}$  (b) $e^{at}$  (c) $\dfrac1a$  (d) $\delta(t)$
> **Ans (a).** A shift in $s$ corresponds to an exponential. *Trick:* the pole at $s=-a$ gives $e^{-at}$ (sign!).

**Problem 172.** $\mathcal L^{-1}\!\Big[\dfrac{1}{s^{2}}\Big]=$
(a) $t$  (b) $1$  (c) $t^{2}$  (d) $\dfrac1t$
> **Ans (a).** $\dfrac{1}{s^{n+1}}\leftrightarrow\dfrac{t^n}{n!}$, so $\dfrac1{s^2}\leftrightarrow t$. *Trick:* the building block of Q35's $t$ term.

**Problem 173.** The partial‑fraction form of $\dfrac{1}{s^{2}(s+1)}$ is
(a) $-\dfrac1s+\dfrac1{s^2}+\dfrac1{s+1}$  (b) $\dfrac1s+\dfrac1{s^2}-\dfrac1{s+1}$  (c) $\dfrac1{s^2}+\dfrac1{s+1}$  (d) $\dfrac1s-\dfrac1{s^2}$
> **Ans (a).** Matching the $s^2$ coefficient forces the $1/s$ term to be $-1$. *Trick:* the easily‑missed $-\tfrac1s$ is what produces the $-1$ in $t-1+e^{-t}$.

**Problem 174.** $\mathcal L^{-1}\!\Big[\dfrac{1}{s^{2}+a^{2}}\Big]=$
(a) $\dfrac1a\sin(at)$  (b) $\cos(at)$  (c) $\sin(at)$  (d) $\dfrac1a\cos(at)$
> **Ans (a).** Note the $1/a$ factor. *Trick:* this is **sine** — $\dfrac{s}{s^2+a^2}$ would give cosine.

**Problem 175.** $\mathcal L^{-1}\!\Big[\dfrac{1}{(s+1)^{2}}\Big]=$
(a) $t\,e^{-t}$  (b) $e^{-t}$  (c) $t^{2}e^{-t}$  (d) $e^{-2t}$
> **Ans (a).** First shifting theorem applied to $1/s^2\leftrightarrow t$. *Trick:* the shift $s\to s+1$ multiplies $t$ by $e^{-t}$.

---

# SET 36 — Small‑angle approximations & their accuracy
**Origin (Q36):** $\cos\theta\approx1$ holds to $3$ decimals while $\tfrac{\theta^2}{2}<0.0005$, i.e. $|\theta|\lesssim1.81^\circ$. **Twists:** sine's first correction, cosine's error term, tangent's correction, sine's (much wider) accuracy, the binomial approximation.

**Problem 176.** The first correction to $\sin\theta\approx\theta$ is
(a) $-\dfrac{\theta^3}{6}$  (b) $-\dfrac{\theta^2}{2}$  (c) $+\dfrac{\theta^3}{3}$  (d) $-\dfrac\theta2$
> **Ans (a).** $\sin\theta=\theta-\dfrac{\theta^3}{6}+\cdots$. *Trick:* sine's leading error is **cubic** (cosine's is quadratic).

**Problem 177.** The leading error in $\cos\theta\approx1$ is
(a) $\dfrac{\theta^2}{2}$  (b) $\dfrac{\theta^3}{6}$  (c) $\theta$  (d) $\dfrac{\theta^4}{24}$
> **Ans (a).** $\cos\theta=1-\dfrac{\theta^2}{2}+\cdots$. *Trick:* the quadratic error is exactly what Q36 sets $<0.0005$.

**Problem 178.** The first correction to $\tan\theta\approx\theta$ is
(a) $+\dfrac{\theta^3}{3}$  (b) $-\dfrac{\theta^3}{6}$  (c) $+\dfrac{\theta^2}{2}$  (d) $\dfrac{\theta^3}{6}$
> **Ans (a).** $\tan\theta=\theta+\dfrac{\theta^3}{3}+\cdots$. *Trick:* positive sign and coefficient $\tfrac13$ (not $\tfrac16$).

**Problem 179.** $\sin\theta\approx\theta$ stays accurate to $\sim3$ decimal places up to roughly
(a) $\approx8^\circ$  (b) $\approx1.8^\circ$  (c) $\approx90^\circ$  (d) $\approx45^\circ$
> **Ans (a).** $\dfrac{\theta^3}{6}<0.0005\Rightarrow\theta<0.144\,$rad $\approx8.3^\circ$. *Trick:* because the error is **cubic**, $\sin\theta\approx\theta$ holds to a far larger angle than $\cos\theta\approx1$ ($\sim1.8^\circ$).

**Problem 180.** For small $x$, $(1+x)^{n}\approx$
(a) $1+nx$  (b) $1+x$  (c) $1+nx+x^2$  (d) $nx$
> **Ans (a).** First‑order binomial/Taylor expansion. *Trick:* the slope at $x=0$ is $n$, giving $1+nx$.

---

# SET 37 — Line integrals & Stokes (conservative fields)
**Origin (Q37):** $\vec A=(yz,xz,xy)$ has $\nabla\times\vec A=0$ (so $\vec A=\nabla(xyz)$), making the closed‑loop integral $0$. **Twists:** the curl test, the closed‑loop result, the potential, Stokes, the divergence partner.

**Problem 181.** A vector field is conservative (path‑independent) when
(a) $\nabla\times\vec A=0$  (b) $\nabla\cdot\vec A=0$  (c) $\nabla^{2}\vec A=0$  (d) $\vec A=0$
> **Ans (a).** Zero curl (in a simply connected region) ⇒ conservative. *Trick:* it's the **curl**, not the divergence, that governs path‑independence.

**Problem 182.** For a conservative field, $\displaystyle\oint_C\vec A\cdot d\vec l$ around any closed loop is
(a) $0$  (b) $2\pi$  (c) the enclosed area  (d) $\nabla\cdot\vec A$
> **Ans (a).** Conservative ⇒ the loop integral vanishes. *Trick:* this is precisely Q37's result, via $\nabla\times\vec A=0$.

**Problem 183.** The field $\vec A=(yz,xz,xy)$ is the gradient of
(a) $xyz$  (b) $x+y+z$  (c) $x^2+y^2+z^2$  (d) $\dfrac{xyz}{3}$
> **Ans (a).** $\nabla(xyz)=(yz,xz,xy)$. *Trick:* recognizing the scalar potential immediately tells you the loop integral is $0$.

**Problem 184.** Stokes' theorem states $\displaystyle\oint_C\vec A\cdot d\vec l=$
(a) $\displaystyle\int_S(\nabla\times\vec A)\cdot d\vec a$  (b) $\displaystyle\int_S(\nabla\cdot\vec A)\,dV$  (c) $\displaystyle\int_V(\nabla\times\vec A)\,dV$  (d) $\displaystyle\int_S\vec A\cdot d\vec a$
> **Ans (a).** The line integral equals the curl's flux through any spanning surface. *Trick:* curl‑flux through a surface bounded by the loop — the basis of Q37.

**Problem 185.** The divergence theorem states $\displaystyle\oint_S\vec A\cdot d\vec a=$ (closed surface $S$)
(a) $\displaystyle\int_V(\nabla\cdot\vec A)\,dV$  (b) $\displaystyle\int_S(\nabla\times\vec A)\cdot d\vec a$  (c) $\displaystyle\oint_C\vec A\cdot d\vec l$  (d) $\displaystyle\int_V\vec A\,dV$
> **Ans (a).** Gauss relates surface flux to enclosed divergence. *Trick:* don't confuse Gauss (divergence, closed surface→volume) with Stokes (curl, loop→surface).

---

# SET 38 — Hermitian operators & commutators
**Origin (Q38):** $[A,B]=C$ with $A,B,C$ all Hermitian is impossible, because $[A,B]$ is anti‑Hermitian. **Twists:** the commutator's character, $i[A,B]$, the anticommutator, real eigenvalues, when a product is Hermitian.

**Problem 186.** For Hermitian $A,B$, the commutator $[A,B]$ is
(a) anti‑Hermitian  (b) Hermitian  (c) unitary  (d) zero
> **Ans (a).** $[A,B]^\dagger=B^\dagger A^\dagger-A^\dagger B^\dagger=BA-AB=-[A,B]$. *Trick:* anti‑Hermitian — which is exactly why Q38's $[A,B]=C$ (with $C$ Hermitian, nonzero) is impossible.

**Problem 187.** For Hermitian $A,B$, the operator $i[A,B]$ is
(a) Hermitian  (b) anti‑Hermitian  (c) zero  (d) unitary
> **Ans (a).** Multiplying an anti‑Hermitian operator by $i$ makes it Hermitian. *Trick:* this is why physical observables (e.g. angular momentum) appear as $i[\,\cdot\,,\,\cdot\,]$.

**Problem 188.** For Hermitian $A,B$, the anticommutator $\{A,B\}=AB+BA$ is
(a) Hermitian  (b) anti‑Hermitian  (c) zero  (d) undefined
> **Ans (a).** $(AB+BA)^\dagger=BA+AB$. *Trick:* the anticommutator stays Hermitian — that's why Q38's option $AB+BA=C$ is allowed.

**Problem 189.** The eigenvalues of a Hermitian operator are
(a) real  (b) imaginary  (c) on the unit circle  (d) positive
> **Ans (a).** Hermiticity forces real eigenvalues. *Trick:* this is the reason quantum observables are represented by Hermitian operators.

**Problem 190.** For Hermitian $A,B$, the product $AB$ is Hermitian **iff**
(a) $[A,B]=0$  (b) always  (c) never  (d) $A=B$
> **Ans (a).** $(AB)^\dagger=BA$, which equals $AB$ only when they commute. *Trick:* a product of Hermitian operators is **not** generally Hermitian — commutation is required.

---

# SET 39 — Which $u$ can be the real part (harmonic?)
**Origin (Q39):** $x^2y$ cannot be $\operatorname{Re}f$ because $\nabla^2(x^2y)=2y\neq0$. **Twists:** the criterion, testing $x^3-3xy^2$, testing $3x^2y-y^3$, $\nabla^2(xy)$, the $|z|^2$ trap.

**Problem 191.** $u(x,y)$ can be the real part of an analytic function **iff**
(a) $\nabla^{2}u=0$  (b) $\nabla u=0$  (c) $u_x=u_y$  (d) $u$ is bounded
> **Ans (a).** It must satisfy Laplace's equation (be harmonic). *Trick:* harmonicity is the make‑or‑break condition behind Q39.

**Problem 192.** Which of the following **is** harmonic?
(a) $x^{3}-3xy^{2}$  (b) $x^{2}y$  (c) $x^{3}$  (d) $x^{2}+y$
> **Ans (a).** $\nabla^2(x^3-3xy^2)=6x-6x=0$ (it's $\operatorname{Re}(z^3)$). *Trick:* $x^3$ alone has $\nabla^2=6x\neq0$ — the cross term in $x^3-3xy^2$ is what cancels it.

**Problem 193.** The function $3x^{2}y-y^{3}$ is
(a) harmonic  (b) not harmonic  (c) analytic itself  (d) anti‑harmonic
> **Ans (a).** $\nabla^2=6y-6y=0$; it is $\operatorname{Im}(z^3)$. *Trick:* both $\operatorname{Re}$ and $\operatorname{Im}$ of an analytic function are harmonic.

**Problem 194.** $\nabla^{2}(xy)=$
(a) $0$  (b) $2$  (c) $x+y$  (d) $1$
> **Ans (a).** $\partial_{xx}(xy)+\partial_{yy}(xy)=0+0=0$. *Trick:* $xy$ **is** harmonic ($=\tfrac12\operatorname{Im}z^2$).

**Problem 195.** Which **cannot** be the real part of an analytic function?
(a) $x^{2}+y^{2}$  (b) $x^{2}-y^{2}$  (c) $e^{x}\cos y$  (d) $x$
> **Ans (a).** $\nabla^2(x^2+y^2)=4\neq0$. *Trick:* $x^2+y^2=|z|^2$ is the classic non‑harmonic trap; the others all satisfy $\nabla^2=0$.

---

# SET 40 — Laplacian Green's function / fundamental solution
**Origin (Q40):** $\nabla^2_{(4\text{D})}\dfrac{1}{r^2}\propto\delta^4(\vec r)=\delta(x_1)\delta(x_2)\delta(x_3)\delta(x_4)$. **Twists:** 3‑D Coulomb, behaviour away from origin, the dimensional pattern, the 2‑D log case, the 4‑D result.

**Problem 196.** In 3‑D, $\nabla^{2}\dfrac1r$ equals
(a) $-4\pi\,\delta^{3}(\vec r)$  (b) $0$ everywhere  (c) $\dfrac1{r^2}$  (d) $\delta^{3}(\vec r)$
> **Ans (a).** The Coulomb/Poisson identity. *Trick:* $1/r$ is harmonic *except* at the origin, where it produces $-4\pi\delta^3$.

**Problem 197.** For $r\neq0$ in 3‑D, $\nabla^{2}\dfrac1r=$
(a) $0$  (b) $-4\pi$  (c) $\dfrac1{r^3}$  (d) $\delta^{3}(\vec r)$
> **Ans (a).** Away from the origin $1/r$ is harmonic. *Trick:* the singular source is a pure delta at the origin (same as $1/r^2$ in 4‑D for Q40).

**Problem 198.** In $d$ dimensions ($d\ge3$), the Green's function of $\nabla^{2}$ behaves as
(a) $\dfrac{1}{r^{\,d-2}}$  (b) $\dfrac{1}{r^{d}}$  (c) $\dfrac1r$  (d) $\ln r$
> **Ans (a).** The fundamental solution scales as $r^{2-d}$. *Trick:* $d=3\to1/r$, $d=4\to1/r^2$ — the exponent is $d-2$ (the Q40 case).

**Problem 199.** In 2‑D, the fundamental solution of Laplace's equation is proportional to
(a) $\ln r$  (b) $\dfrac1r$  (c) $\dfrac1{r^2}$  (d) a constant
> **Ans (a).** Two dimensions is special. *Trick:* the $1/r^{d-2}$ formula breaks at $d=2$, replaced by a **logarithm**.

**Problem 200.** In 4‑D, $\nabla^{2}\dfrac{1}{x_1^2+x_2^2+x_3^2+x_4^2}$ is proportional to
(a) $\delta(x_1)\delta(x_2)\delta(x_3)\delta(x_4)$  (b) $\delta(x_1+x_2+x_3+x_4)$  (c) $\dfrac1{r^3}$  (d) $(r^2)^{-2}$
> **Ans (a).** The 4‑D Laplacian of the $1/r^2$ Green's function is a product of four 1‑D deltas. *Trick:* it's a **product** $\delta(x_1)\cdots\delta(x_4)$, not a single delta of the sum — exactly Q40.

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: the $-\tfrac12$ overlap in a $120^\circ$ pair (and that $\hat i\pm\hat n$ are always perpendicular); a single $\bar z$ kills analyticity; wave speed $=\sqrt{\text{coeff}}$ and fixed ends select **sines**; quadratic growth blows up in finite time while linear growth never does; the sneaky $-\tfrac1s$ in a Laplace partial fraction; $\sin\theta\approx\theta$ survives to $\sim8^\circ$ but $\cos\theta\approx1$ only to $\sim1.8^\circ$; zero **curl** (not divergence) means conservative; the commutator of Hermitians is anti‑Hermitian; $|z|^2$ is the non‑harmonic trap; and the Laplacian Green's function scales as $1/r^{d-2}$ (log in 2‑D). Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 200 problems across the first 40 originals (Q1–Q40).**
