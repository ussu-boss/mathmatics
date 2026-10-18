# 50 Practice Problems — Part 9 (CSIR‑NET/JRF style)

**Built from problems 81–90 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **401–450** to continue Parts 1–8.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q81–Q84 = Dec 2016**, **Q85–Q90 = June 2017** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q81–Q90)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q81 | Numerical methods | Newton's forward‑difference interpolation |
| Q82 | PDEs | Diffusion/heat equation; a spreading Gaussian |
| Q83 | Numerical methods | Fixed‑point iteration **stability** |
| Q84 | Group theory | Group closure; the Pauli group (16 elements) |
| Q85 | Linear algebra | Real matrices ⇒ complex‑conjugate eigenvalue pairs |
| Q86 | Complex analysis | Harmonicity of $e^{ax}\cos(by)$ ($a^2=b^2$) |
| Q87 | Complex analysis | Contour integral with multiple poles & orientation |
| Q88 | ODEs | Linear first‑order ODE (integrating factor) |
| Q89 | Probability | Transformation of random variables |
| Q90 | Math methods | Green's‑function construction (1‑D) |

---

# SET 81 — Newton's forward‑difference interpolation
**Origin (Q81):** tabulated $\sin$ values are interpolated to get $\sin52^\circ\approx0.788$ via forward differences with $u=(52-45)/5=\tfrac75$. **Twists:** the first/second differences, the variable $u$, the formula, the truncation rule.

**Problem 401.** The first forward difference $\Delta f(x_0)=$
(a) $f(x_1)-f(x_0)$  (b) $f(x_0)-f(x_1)$  (c) $f(x_1)+f(x_0)$  (d) $f(x_2)-f(x_0)$
> **Ans (a).** $\Delta$ subtracts consecutive values. *Trick:* it's "next minus current," the building block of Q81's table.

**Problem 402.** The second forward difference $\Delta^{2}f_0=$
(a) $f_2-2f_1+f_0$  (b) $f_2-f_1$  (c) $f_2+f_0$  (d) $f_2-2f_0$
> **Ans (a).** $\Delta^2=\Delta(\Delta)$ gives the $1,-2,1$ pattern. *Trick:* it mimics a second derivative.

**Problem 403.** In Newton's forward formula, the interpolation variable is $u=$
(a) $\dfrac{x-x_0}{h}$  (b) $x-x_0$  (c) $\dfrac xh$  (d) $\dfrac{h}{x-x_0}$
> **Ans (a).** $u$ counts step‑sizes past $x_0$. *Trick:* Q81 used $u=(52-45)/5=\tfrac75$.

**Problem 404.** Newton's forward interpolation formula is
(a) $f_0+u\Delta f_0+\dfrac{u(u-1)}{2!}\Delta^2 f_0+\cdots$  (b) $f_0+u\Delta f_0+u^2\Delta^2 f_0$  (c) $\sum f_n/n!$  (d) $f_0+\Delta f_0+\Delta^2 f_0$
> **Ans (a).** Binomial‑coefficient weights $u,\dfrac{u(u-1)}{2!},\dots$ . *Trick:* the coefficients are "$u$ choose $k$," not powers of $u$.

**Problem 405.** If the data come from a degree‑$n$ polynomial, the forward differences $\Delta^k f$ vanish for
(a) $k>n$  (b) $k<n$  (c) all $k$  (d) $k=n$
> **Ans (a).** The $(n+1)$‑th differences vanish, like the $(n+1)$‑th derivative. *Trick:* differences of order beyond the degree are zero.

---

# SET 82 — Diffusion / heat equation
**Origin (Q82):** $\partial_t f=D\partial_x^2 f$ with $f(x,0)=e^{-x^2}$ gives $f=\dfrac{1}{\sqrt{1+4Dt}}e^{-x^2/(1+4Dt)}$ — a spreading Gaussian. **Twists:** the equation, width growth, amplitude decay, the wave‑equation contrast, the solution.

**Problem 406.** The 1‑D diffusion (heat) equation is
(a) $\partial_t f=D\,\partial_x^2 f$  (b) $\partial_t^2 f=D\,\partial_x^2 f$  (c) $\partial_t f=D\,\partial_x f$  (d) $\partial_t f=-D\,\partial_x^2 f$
> **Ans (a).** First order in time, second in space. *Trick:* contrast with the wave equation's second‑order time derivative.

**Problem 407.** Under diffusion, the width (standard deviation) of an initial Gaussian grows as
(a) $\sqrt t$  (b) $t$  (c) $t^{2}$  (d) constant
> **Ans (a).** The variance grows linearly in $t$. *Trick:* diffusive $\sqrt t$ spreading.

**Problem 408.** As a diffusing Gaussian spreads, its peak height falls as
(a) $\dfrac{1}{\sqrt t}$  (b) $\dfrac1t$  (c) $e^{-t}$  (d) constant
> **Ans (a).** Area is conserved, so height $\propto$ 1/width. *Trick:* the $1/\sqrt t$ matches the $1/\sqrt{1+4Dt}$ in Q82.

**Problem 409.** Compared to the wave equation, the diffusion equation
(a) is first‑order in time (irreversible)  (b) is second‑order in time  (c) has the same time order  (d) has no time derivative
> **Ans (a).** The time‑derivative order distinguishes them. *Trick:* diffusion **smooths/spreads**, while waves **propagate** (and reverse).

**Problem 410.** The heat‑equation solution for an initial $e^{-x^2}$ is
(a) $\dfrac{1}{\sqrt{1+4Dt}}\,e^{-x^2/(1+4Dt)}$  (b) $\dfrac{1}{\sqrt{1+Dt}}\,e^{-x^2/(1+Dt)}$  (c) $e^{-(x-vt)^2}$  (d) $e^{-x^2}\cos(Dt)$
> **Ans (a).** The $4Dt$ in the width and the $1/\sqrt{\cdot}$ prefactor. *Trick:* it spreads in place — **not** a traveling wave (Q82).

---

# SET 83 — Fixed‑point iteration stability
**Origin (Q83):** $x_{n+1}=1+\dfrac{3}{1+x_n}$ has the stable fixed point $x=2$, with error ratio $\epsilon_{n+1}/\epsilon_n=g'(2)=-\tfrac13$. **Twists:** the multiplier, the stability condition, the Q83 value, oscillation, Newton as a map.

**Problem 411.** For $x_{n+1}=g(x_n)$ near a fixed point $x^*$, the error ratio $\dfrac{\epsilon_{n+1}}{\epsilon_n}$ equals
(a) $g'(x^*)$  (b) $g(x^*)$  (c) $\dfrac{1}{g'(x^*)}$  (d) $x^*$
> **Ans (a).** Linearizing the map gives the multiplier $g'(x^*)$. *Trick:* this is the engine of Q83.

**Problem 412.** A fixed point $x^*$ of $x_{n+1}=g(x_n)$ is stable (attracting) if
(a) $|g'(x^*)|<1$  (b) $|g'(x^*)|>1$  (c) $g'(x^*)=0$  (d) $g'(x^*)=1$
> **Ans (a).** Errors shrink iff the multiplier has magnitude below $1$. *Trick:* $|g'|<1$ is the stability test.

**Problem 413.** For $g(x)=1+\dfrac{3}{1+x}$, the multiplier at $x=2$ is
(a) $-\dfrac13$  (b) $-\dfrac19$  (c) $-3$  (d) $\dfrac13$
> **Ans (a).** $g'(x)=-\dfrac{3}{(1+x)^2}$, so $g'(2)=-\tfrac39=-\tfrac13$. *Trick:* $|-\tfrac13|<1$, so $x=2$ is stable (Q83).

**Problem 414.** If the multiplier $g'(x^*)<0$, the iterates approach $x^*$ by
(a) oscillating around it  (b) approaching from one side  (c) diverging  (d) staying constant
> **Ans (a).** A negative multiplier flips the error's sign each step. *Trick:* Q83's $-\tfrac13$ makes the iterates alternate sides.

**Problem 415.** Newton–Raphson is the fixed‑point map $g(x)=x-\dfrac{f(x)}{f'(x)}$; at a simple root its multiplier $g'(x^*)$ is
(a) $0$  (b) $1$  (c) $-1$  (d) $\dfrac12$
> **Ans (a).** $g'(x^*)=\dfrac{ff''}{f'^2}=0$ at a root. *Trick:* the **zero** multiplier explains Newton's quadratic convergence.

---

# SET 84 — Group closure & the Pauli group
**Origin (Q84):** $\{I,\sigma_x,\sigma_y,\sigma_z\}$ do not close; the smallest group containing them has **16** elements $\{\pm1,\pm i\}\times\{I,\sigma_x,\sigma_y,\sigma_z\}$. **Twists:** $\sigma_x\sigma_y$, $\sigma_x^2$, the group size, anticommutation, the closure axiom.

**Problem 416.** $\sigma_x\sigma_y=$
(a) $i\sigma_z$  (b) $\sigma_z$  (c) $-\sigma_z$  (d) $\sigma_y$
> **Ans (a).** The product introduces a factor of $i$. *Trick:* $i\sigma_z$ is **not** one of the original four — that's why they fail to close (Q84).

**Problem 417.** $\sigma_x^{2}=$
(a) $I$  (b) $\sigma_x$  (c) $0$  (d) $-I$
> **Ans (a).** Each Pauli matrix squares to the identity. *Trick:* $\sigma_j^2=I$.

**Problem 418.** The smallest group of $2\times2$ matrices containing $I,\sigma_x,\sigma_y,\sigma_z$ has
(a) $16$  (b) $4$  (c) $8$  (d) $2$
> **Ans (a).** $\{\pm1,\pm i\}\times4=16$ elements. *Trick:* closure forces in $\pm1,\pm i$ times each (Q84).

**Problem 419.** The Pauli matrices satisfy $\sigma_x\sigma_y+\sigma_y\sigma_x=$
(a) $0$  (b) $2I$  (c) $2i\sigma_z$  (d) $\sigma_z$
> **Ans (a).** Distinct Pauli matrices anticommute. *Trick:* $\{\sigma_x,\sigma_y\}=0$.

**Problem 420.** The first group axiom requires the set to be
(a) closed under the operation  (b) commutative  (c) finite  (d) endowed with a zero element
> **Ans (a).** Closure: any product stays in the set. *Trick:* this is exactly why $\{I,\sigma_x,\sigma_y,\sigma_z\}$ must be enlarged to $16$ (Q84).

---

# SET 85 — Real matrices ⇒ complex‑conjugate eigenvalue pairs
**Origin (Q85):** $\{i,1,0\}$ cannot be eigenvalues of a real $3\times3$ matrix, because $i$ appears without $-i$. **Twists:** the conjugate‑pair rule, the odd‑dimension consequence, the Q85 set, real‑symmetric, the determinant.

**Problem 421.** The complex (non‑real) eigenvalues of a real matrix
(a) occur in conjugate pairs  (b) can be any complex number  (c) are always purely imaginary  (d) are always real
> **Ans (a).** A real characteristic polynomial has conjugate complex roots. *Trick:* this rule is the basis of Q85.

**Problem 422.** A real $3\times3$ matrix must have at least
(a) one real eigenvalue  (b) three complex eigenvalues  (c) zero real eigenvalues  (d) three real eigenvalues
> **Ans (a).** Complex ones pair up, so an odd dimension leaves one real. *Trick:* you can't pair up three roots without a leftover real one.

**Problem 423.** The set that **cannot** be eigenvalues of a real $3\times3$ matrix is
(a) $\{i,1,0\}$  (b) $\{2i,0,-2i\}$  (c) $\{1,1,1\}$  (d) $\{e^{i\theta},e^{-i\theta},1\}$
> **Ans (a).** $i$ appears without $-i$. *Trick:* (b) and (d) are valid conjugate pairs; only (a) breaks the rule (Q85).

**Problem 424.** The eigenvalues of a real **symmetric** matrix are
(a) all real  (b) complex‑conjugate pairs  (c) imaginary  (d) on the unit circle
> **Ans (a).** Symmetry forces real eigenvalues. *Trick:* a stronger statement than the general conjugate‑pair rule.

**Problem 425.** A conjugate eigenvalue pair $\lambda,\bar\lambda$ contributes to the determinant a factor
(a) $|\lambda|^{2}$ (real, positive)  (b) imaginary  (c) $\lambda^{2}$  (d) $0$
> **Ans (a).** $\lambda\bar\lambda=|\lambda|^2$. *Trick:* the pair's product is real, keeping the determinant of a real matrix real.

---

# SET 86 — Harmonicity of $e^{ax}\cos(by)$
**Origin (Q86):** $u=e^{ax}\cos(by)$ is the real part of an analytic function iff it is harmonic, i.e. $a^2=b^2$ ($b=\pm a$). **Twists:** the Laplacian, the condition, the analytic function, $\cos(by)$ alone, the cancellation.

**Problem 426.** $\nabla^{2}\!\big[e^{ax}\cos(by)\big]=$
(a) $(a^{2}-b^{2})e^{ax}\cos(by)$  (b) $(a^{2}+b^{2})e^{ax}\cos(by)$  (c) $(a^{2}-b^{2})e^{ax}\sin(by)$  (d) $0$ always
> **Ans (a).** $u_{xx}$ gives $+a^2$, $u_{yy}$ gives $-b^2$. *Trick:* the $\cos$ differentiates twice to $-\cos$, producing the $-b^2$.

**Problem 427.** $e^{ax}\cos(by)$ is harmonic if and only if
(a) $b=\pm a$  (b) $b=0$  (c) $a=0$  (d) $b=2a$
> **Ans (a).** Set $a^2-b^2=0$. *Trick:* this is exactly Q86's condition.

**Problem 428.** When $b=a$, the function $e^{ax}\cos(ay)$ is the real part of
(a) $e^{az}$  (b) $e^{a\bar z}$  (c) $e^{a^2 z}$  (d) $\cos(az)$
> **Ans (a).** $\operatorname{Re}(e^{a(x+iy)})=e^{ax}\cos(ay)$. *Trick:* recognize it as $\operatorname{Re}(e^{az})$.

**Problem 429.** The function $\cos(by)$ alone (no $e^{ax}$) has Laplacian
(a) $-b^{2}\cos(by)$  (b) $0$  (c) $b^{2}\cos(by)$  (d) $-b^{2}\sin(by)$
> **Ans (a).** $\partial_y^2\cos(by)=-b^2\cos(by)$. *Trick:* $\cos(by)$ by itself is **not** harmonic — it needs the matching $e^{ax}$ factor.

**Problem 430.** $e^{kx}\cos(ky)$ (matching exponents) is harmonic because
(a) the $x$‑ and $y$‑Laplacian contributions cancel  (b) it is bounded  (c) it is separable  (d) $\cos$ is periodic
> **Ans (a).** The $+k^2$ from the $x$‑part cancels the $-k^2$ from the $y$‑part. *Trick:* the cancellation $a^2-b^2=0$ with both equal to $k$ (Q86).

---

# SET 87 — Contour integration with multiple poles
**Origin (Q87):** $\oint\dfrac{ze^{i\pi z/2}}{z^2-1}\,dz$ over a contour enclosing $z=+1$ (CCW) and $z=-1$ (CW); the residues combine to $-2\pi$. **Twists:** partial fractions, the two residues, orientation, and the combination.

**Problem 431.** $\dfrac{z}{z^{2}-1}=$
(a) $\dfrac12\Big(\dfrac{1}{z-1}+\dfrac{1}{z+1}\Big)$  (b) $\dfrac{1}{z-1}-\dfrac{1}{z+1}$  (c) $\dfrac{1}{z^{2}-1}$  (d) $\dfrac{z}{z-1}$
> **Ans (a).** Partial fractions give residue $\tfrac12$ at each of $\pm1$. *Trick:* both residues are $\tfrac12$ (for the bare $z/(z^2-1)$).

**Problem 432.** The residue of $\dfrac{ze^{i\pi z/2}}{z^{2}-1}$ at $z=1$ is
(a) $\dfrac i2$  (b) $\dfrac12$  (c) $-\dfrac i2$  (d) $i$
> **Ans (a).** $\dfrac{z e^{i\pi z/2}}{z+1}\Big|_{z=1}=\dfrac{e^{i\pi/2}}{2}=\dfrac i2$. *Trick:* $e^{i\pi/2}=i$.

**Problem 433.** The residue of $\dfrac{ze^{i\pi z/2}}{z^{2}-1}$ at $z=-1$ is
(a) $-\dfrac i2$  (b) $\dfrac i2$  (c) $\dfrac12$  (d) $i$
> **Ans (a).** $\dfrac{ze^{i\pi z/2}}{z-1}\Big|_{z=-1}=\dfrac{(-1)(-i)}{-2}=-\dfrac i2$. *Trick:* $e^{-i\pi/2}=-i$; mind the signs.

**Problem 434.** A contour that encircles a pole **clockwise** contributes
(a) $-2\pi i\times(\text{residue})$  (b) $+2\pi i\times\text{residue}$  (c) $\pi i\times\text{residue}$  (d) $0$
> **Ans (a).** Reversing orientation flips the sign. *Trick:* Q87's contour wraps the two poles in opposite senses.

**Problem 435.** With the two poles encircled in **opposite** orientations, the integral $\oint\dfrac{ze^{i\pi z/2}}{z^2-1}dz=$
(a) $-2\pi$  (b) $0$  (c) $2\pi i$  (d) $4\pi i$
> **Ans (a).** $2\pi i\big(\tfrac i2-(-\tfrac i2)\big)=2\pi i\cdot i=-2\pi$. *Trick:* opposite orientations **subtract** the residues, giving a nonzero $-2\pi$ (Q87).

---

# SET 88 — Linear first‑order ODE (integrating factor)
**Origin (Q88):** $x\,y'+2y=\dfrac{\cos\pi x}{x}$, i.e. $y'+\dfrac2x y=\dfrac{\cos\pi x}{x^2}$; integrating factor $x^2$, and $y(2)=\tfrac14$. **Twists:** standard form, the IF formula, the Q88 IF, the perfect‑derivative step, the answer.

**Problem 436.** A linear first‑order ODE has the form
(a) $y'+P(x)y=Q(x)$  (b) $y'+Py^{2}=Q$  (c) $yy'+P=Q$  (d) $y''+Py'=Q$
> **Ans (a).** Linear in $y$ and $y'$, with $P,Q$ functions of $x$. *Trick:* the coefficient of $y$ is a function of $x$ only.

**Problem 437.** For $y'+P(x)y=Q(x)$, the integrating factor is
(a) $e^{\int P\,dx}$  (b) $e^{-\int P\,dx}$  (c) $e^{\int Q\,dx}$  (d) $\int P\,dx$
> **Ans (a).** Multiplying by $e^{\int P}$ makes the LHS a perfect derivative. *Trick:* the IF uses $P$, not $Q$.

**Problem 438.** For $y'+\dfrac2x y=\dfrac{\cos\pi x}{x^2}$, the integrating factor is
(a) $x^{2}$  (b) $x$  (c) $\dfrac1{x^2}$  (d) $e^{2x}$
> **Ans (a).** $\int\dfrac2x dx=2\ln x$, so IF $=e^{2\ln x}=x^2$. *Trick:* the IF is $x^2$, not $e^{2x}$ (Q88).

**Problem 439.** Multiplying $y'+\dfrac2x y=\dfrac{\cos\pi x}{x^2}$ by the integrating factor gives
(a) $(x^{2}y)'=\cos\pi x$  (b) $(x^{2}y)'=x^{2}\cos\pi x$  (c) $y'=\cos\pi x$  (d) $(xy)'=\cos\pi x$
> **Ans (a).** The LHS becomes $\dfrac{d}{dx}(x^2 y)$ and the RHS is $x^2\cdot\dfrac{\cos\pi x}{x^2}=\cos\pi x$. *Trick:* the $x^2$ cancels on the right.

**Problem 440.** For $y'+\dfrac2x y=\dfrac{\cos\pi x}{x^2}$ with $y(1)=1$, the value $y(2)=$
(a) $\dfrac14$  (b) $1$  (c) $\dfrac12$  (d) $\pi$
> **Ans (a).** $y=\dfrac{\sin\pi x}{\pi x^2}+\dfrac1{x^2}$; at $x=2$, $\sin2\pi=0$, so $y(2)=\tfrac14$. *Trick:* the sine term vanishes at integer $x$ (Q88).

---

# SET 89 — Transformation of random variables
**Origin (Q89):** for $x\sim N(0,\sigma^2)$ and $y=x^2$, the density is $f_y(y)=\dfrac{1}{\sqrt{2\pi\sigma^2 y}}e^{-y/2\sigma^2}$. **Twists:** the transformation rule, the two‑to‑one map, the Jacobian, the Q89 result, a linear map.

**Problem 441.** For $y=g(x)$ (monotonic), the density transforms as
(a) $p_y(y)=p_x(x)\Big|\dfrac{dx}{dy}\Big|$  (b) $p_y(y)=p_x(x)$  (c) $p_y(y)=p_x(x)\Big|\dfrac{dy}{dx}\Big|$  (d) $p_y(y)=p_x(g(y))$
> **Ans (a).** Include the Jacobian $|dx/dy|$ to conserve probability. *Trick:* it's $|dx/dy|$, not $|dy/dx|$.

**Problem 442.** For $y=x^{2}$ with a symmetric $p_x$, the density $p_y$ includes
(a) contributions from both $\pm\sqrt y$ (a factor of $2$)  (b) only $x=+\sqrt y$  (c) no Jacobian  (d) a delta function
> **Ans (a).** A two‑to‑one map sums both branches. *Trick:* the factor of $2$ in Q89 comes from $\pm\sqrt y$.

**Problem 443.** For $y=x^{2}$, the Jacobian $\Big|\dfrac{dx}{dy}\Big|=$
(a) $\dfrac{1}{2\sqrt y}$  (b) $2\sqrt y$  (c) $\dfrac{1}{2y}$  (d) $2y$
> **Ans (a).** $x=\sqrt y\Rightarrow\dfrac{dx}{dy}=\dfrac{1}{2\sqrt y}$. *Trick:* the $1/\sqrt y$ singularity at $y=0$ comes from here.

**Problem 444.** For $x\sim N(0,\sigma^{2})$ and $y=x^{2}$, the density of $y$ is
(a) $\dfrac{1}{\sqrt{2\pi\sigma^{2}y}}\,e^{-y/2\sigma^{2}}$  (b) $\dfrac{1}{\sqrt{2\pi\sigma^{2}}}\,e^{-y/2\sigma^{2}}$  (c) $\dfrac{1}{\sqrt{2\sigma^{2}y}}\,e^{-y/2\sigma^{2}}$  (d) $\dfrac{1}{\sqrt{2\pi\sigma^{2}y}}\,e^{-y/\sigma^{2}}$
> **Ans (a).** The factor of $2$ and the $1/(2\sqrt y)$ combine, leaving the $1/\sqrt y$. *Trick:* this is a chi‑squared (1 d.o.f.) shape (Q89).

**Problem 445.** For $y=ax+b$ with $x\sim N(\mu,\sigma^{2})$, $y$ is distributed as
(a) $N(a\mu+b,\ a^{2}\sigma^{2})$  (b) $N(\mu+b,\ \sigma^{2})$  (c) $N(a\mu,\ a\sigma^{2})$  (d) $N(a\mu+b,\ a\sigma^{2})$
> **Ans (a).** A linear map scales the variance by $a^2$. *Trick:* the variance scales by $a^2$ (not $a$); the mean shifts by $b$.

---

# SET 90 — Green's‑function construction (1‑D)
**Origin (Q90):** $\dfrac{d^2g}{dx^2}=\delta(x-x_0)$ with $g(\pm L)=0$; piecewise‑linear $g$ matching the boundary conditions, continuity, and a unit jump in $g'$. **Twists:** the homogeneous form, continuity, the jump, the boundary pieces, symmetry.

**Problem 446.** For $\dfrac{d^2g}{dx^2}=\delta(x-x_0)$, away from $x_0$ the Green's function satisfies
(a) $g''=0$ (so $g$ is linear)  (b) $g''=\delta$  (c) $g=0$  (d) $g''=1$
> **Ans (a).** The delta acts only at $x_0$; elsewhere $g$ solves the homogeneous equation. *Trick:* $g$ is piecewise **linear**.

**Problem 447.** At the source point $x=x_0$, the Green's function $g(x,x_0)$ is
(a) continuous  (b) discontinuous by $1$  (c) zero  (d) infinite
> **Ans (a).** $g$ itself is continuous. *Trick:* it's the **derivative**, not $g$, that jumps.

**Problem 448.** Integrating $g''=\delta(x-x_0)$ across $x_0$, the jump in $g'$ is
(a) $1$  (b) $0$  (c) $-1$  (d) $\infty$
> **Ans (a).** $\int g''\,dx=[g']=\int\delta=1$. *Trick:* the unit area of $\delta$ becomes a unit jump in the first derivative.

**Problem 449.** With $g(-L)=g(L)=0$, the two linear pieces are proportional to
(a) $(x+L)$ on the left and $(x-L)$ on the right  (b) $x$ on both  (c) constants  (d) $(x^{2}-L^{2})$
> **Ans (a).** Each piece must vanish at its own boundary. *Trick:* $g(-L)=0\Rightarrow(x+L)$ left, $g(L)=0\Rightarrow(x-L)$ right (Q90).

**Problem 450.** The Green's function of a self‑adjoint operator is
(a) symmetric, $g(x,x_0)=g(x_0,x)$  (b) antisymmetric  (c) zero on the diagonal  (d) discontinuous in $x_0$
> **Ans (a).** Reciprocity. *Trick:* swapping source and field points leaves $g$ unchanged for a self‑adjoint operator.

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: forward differences mimic derivatives and truncate beyond the polynomial degree; the diffusion equation **spreads** a Gaussian ($\sqrt t$ width, $1/\sqrt t$ height) — it does not propagate; a fixed point is stable when $|g'(x^*)|<1$ (and a negative multiplier oscillates); Pauli matrices fail to close, generating a $16$‑element group; a real matrix's complex eigenvalues come in conjugate pairs; $e^{ax}\cos(by)$ is harmonic only when $a^2=b^2$; opposite contour orientations **subtract** residues; a linear ODE is cracked by the integrating factor $e^{\int P}$; transforming a variable needs the Jacobian $|dx/dy|$ (with a factor of $2$ for $y=x^2$); and a $1$‑D Green's function is piecewise linear, continuous, with a unit jump in its slope. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 450 problems across the first 90 originals (Q1–Q90).**
