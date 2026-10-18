# 50 Practice Problems — Part 10 (CSIR‑NET/JRF style)

**Built from problems 91–100 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **451–500** to continue Parts 1–9.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q91–Q93 = June 2017**, **Q94–Q100 = Dec 2017** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q91–Q100)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q91 | Group theory | $SU(2)$ adjoint action rotates the spin vector ($SU(2)\!\to\!SO(3)$) |
| Q92 | Group theory | Group **closure** of a matrix family |
| Q93 | Probability | Poisson distribution; $P(0)=e^{-\mu}$ |
| Q94 | Linear algebra | Dual / reciprocal basis (biorthogonality) |
| Q95 | Complex analysis | Radius of convergence via the binomial series |
| Q96 | Linear algebra | Homogeneous system; $\det=0$ for a non‑trivial solution |
| Q97 | ODEs | Solving an ODE via the Laplace transform |
| Q98 | ODEs | Frobenius method; regular singular points |
| Q99 | Group theory | Generators of unitary groups are **anti‑hermitian** |
| Q100 | Numerical methods | Euler's method; truncation error $\propto1/n$ |

---

# SET 91 — $SU(2)$ adjoint action & rotations
**Origin (Q91):** $e^{i\theta\sigma_z/2}(\vec\sigma\!\cdot\!\vec r)e^{-i\theta\sigma_z/2}$ rotates $\vec r$ by $\theta$ about $z$. **Twists:** the half‑angle, $4\pi$ periodicity, the double cover, the Pauli vector, determinant invariance.

**Problem 451.** The $SU(2)$ operator for a 3‑D rotation by $\theta$ about $\hat n$ is
(a) $\exp\!\big(i\theta\,\vec\sigma\!\cdot\!\hat n/2\big)$  (b) $\exp\!\big(i\theta\,\vec\sigma\!\cdot\!\hat n\big)$  (c) $\exp\!\big(i\theta\,\vec\sigma\!\cdot\!\hat n/4\big)$  (d) $\exp\!\big(2i\theta\,\vec\sigma\!\cdot\!\hat n\big)$
> **Ans (a).** The $\theta/2$ (spin‑½ half‑angle) produces a **full** $\theta$ rotation of the vector. *Trick:* this is exactly Q91's setup.

**Problem 452.** $e^{i\theta\sigma_z/2}$ returns to the identity when $\theta=$
(a) $4\pi$  (b) $2\pi$  (c) $\pi$  (d) $8\pi$
> **Ans (a).** At $\theta=2\pi$, $e^{i\pi\sigma_z}=-I$ (not $I$). *Trick:* the famous $4\pi$ periodicity of spinors.

**Problem 453.** $SU(2)$ and $SO(3)$ are related by
(a) $SU(2)$ is a $2$‑to‑$1$ (double) cover of $SO(3)$  (b) they are isomorphic  (c) $SO(3)$ covers $SU(2)$  (d) they are unrelated
> **Ans (a).** $\pm U$ map to the same rotation. *Trick:* the double cover is the mechanism behind Q91.

**Problem 454.** The Pauli vector $\vec\sigma\!\cdot\!\vec r=x\sigma_x+y\sigma_y+z\sigma_z$ equals
(a) $\begin{pmatrix}z&x-iy\\x+iy&-z\end{pmatrix}$  (b) $\begin{pmatrix}x&y\\y&z\end{pmatrix}$  (c) $\begin{pmatrix}z&x\\y&-z\end{pmatrix}$  (d) $\begin{pmatrix}0&x-iy\\x+iy&0\end{pmatrix}$
> **Ans (a).** Assemble the three Pauli matrices. *Trick:* the diagonal carries $\pm z$ (Q91's matrix).

**Problem 455.** Conjugation $\vec\sigma\!\cdot\!\vec r\to U(\vec\sigma\!\cdot\!\vec r)U^\dagger$ preserves
(a) $\det(\vec\sigma\!\cdot\!\vec r)=-r^2$ (so $|\vec r|$ is conserved)  (b) only the trace  (c) nothing  (d) the off‑diagonal entries
> **Ans (a).** $\det$ is conjugation‑invariant and equals $-(x^2+y^2+z^2)$. *Trick:* preserving $\det$ means preserving $|\vec r|$ — as a rotation must.

---

# SET 92 — Group closure of a matrix family
**Origin (Q92):** $\begin{pmatrix}1&0&a\\0&1&b\\0&0&1\end{pmatrix}$ is a group ($a,b$ add); the other parametrizations fail closure. **Twists:** why it closes, why (b) fails, identity, inverse, abelian.

**Problem 456.** The set $\begin{pmatrix}1&0&a\\0&1&b\\0&0&1\end{pmatrix}$ is a group because the product
(a) has the same form, with $a,b$ adding  (b) preserves the trace  (c) is orthogonal  (d) is symmetric
> **Ans (a).** Multiplying gives $(a+a',\,b+b')$ in the same slots. *Trick:* closure holds because the off‑diagonal entries simply add (Q92).

**Problem 457.** The set $\begin{pmatrix}1&a&0\\0&1&b\\0&0&1\end{pmatrix}$ is **not** closed because the product introduces
(a) a new $(1,3)$ entry $a_1b_2$  (b) a zero determinant  (c) a negative entry  (d) nothing — it is closed
> **Ans (a).** The product has a cross term $a_1b_2$ in the top‑right. *Trick:* this is the Heisenberg group, which needs **three** parameters — two don't close.

**Problem 458.** The identity element of the group $\begin{pmatrix}1&0&a\\0&1&b\\0&0&1\end{pmatrix}$ corresponds to
(a) $a=b=0$  (b) $a=b=1$  (c) $a=1,b=0$  (d) no identity
> **Ans (a).** Setting the parameters to $0$ gives $I$. *Trick:* the identity is at the origin of parameter space.

**Problem 459.** The inverse of $\begin{pmatrix}1&0&a\\0&1&b\\0&0&1\end{pmatrix}$ has parameters
(a) $(-a,-b)$  (b) $(a,b)$  (c) $(1/a,1/b)$  (d) $(b,a)$
> **Ans (a).** Since the entries add, the inverse negates them. *Trick:* the group is $\cong(\mathbb R^2,+)$, so inverses are negatives.

**Problem 460.** This group is
(a) abelian  (b) non‑abelian  (c) finite  (d) non‑associative
> **Ans (a).** Addition of $(a,b)$ commutes. *Trick:* the group is $\cong\mathbb R^2$ — abelian.

---

# SET 93 — Poisson distribution; $P(0)=e^{-\mu}$
**Origin (Q93):** $P(0)=10^{-6}=e^{-\mu}\Rightarrow\mu=6\ln10\approx14$. **Twists:** $P(0)$, the Q93 mean, $P(1)$, the ratio, the mode.

**Problem 461.** For a Poisson distribution with mean $\mu$, $P(n=0)=$
(a) $e^{-\mu}$  (b) $\mu$  (c) $\dfrac1\mu$  (d) $\mu e^{-\mu}$
> **Ans (a).** $\dfrac{\mu^0 e^{-\mu}}{0!}=e^{-\mu}$. *Trick:* the $n=0$ term is just $e^{-\mu}$ (Q93).

**Problem 462.** If $P(0)=10^{-6}$ for a Poisson variable, the mean $\mu$ is
(a) $\approx14$  (b) $\approx6$  (c) $\approx10^{6}$  (d) $\approx e$
> **Ans (a).** $e^{-\mu}=10^{-6}\Rightarrow\mu=6\ln10\approx13.8$. *Trick:* take logs — this is Q93.

**Problem 463.** For Poisson with mean $\mu$, $P(n=1)=$
(a) $\mu e^{-\mu}$  (b) $e^{-\mu}$  (c) $\dfrac{\mu^2 e^{-\mu}}{2}$  (d) $\mu$
> **Ans (a).** $\dfrac{\mu^1 e^{-\mu}}{1!}=\mu e^{-\mu}$. *Trick:* the $n=1$ term.

**Problem 464.** For Poisson, the ratio $\dfrac{P(1)}{P(0)}=$
(a) $\mu$  (b) $1$  (c) $e^{-\mu}$  (d) $\dfrac1\mu$
> **Ans (a).** $\dfrac{\mu e^{-\mu}}{e^{-\mu}}=\mu$. *Trick:* consecutive‑probability ratios reveal the mean directly.

**Problem 465.** For a Poisson distribution with non‑integer mean $\mu$, the most probable value (mode) is
(a) $\lfloor\mu\rfloor$  (b) $\mu$ exactly  (c) $0$  (d) $\mu+1$
> **Ans (a).** The largest integer $\le\mu$. *Trick:* the mode is near, but not equal to, the (non‑integer) mean.

---

# SET 94 — Dual / reciprocal basis (biorthogonality)
**Origin (Q94):** the columns $\vec u,\vec v,\vec w$ of $(A^T)^{-1}$ are biorthogonal to the columns $\vec a,\vec b,\vec c$ of $A$: $\vec u\!\cdot\!\vec a=1,\ \vec u\!\cdot\!\vec b=\vec u\!\cdot\!\vec c=0$. **Twists:** the biorthogonality relation, the crystallographic version, $(A^T)^{-1}$, the orthogonal case, the volume.

**Problem 466.** For non‑singular $A$ with columns $\vec a_j$, the columns $\vec u_i$ of $(A^T)^{-1}$ satisfy
(a) $\vec u_i\!\cdot\!\vec a_j=\delta_{ij}$  (b) $\vec u_i\!\cdot\!\vec a_j=1$  (c) $\vec u_i\!\cdot\!\vec a_j=0$  (d) $\vec u_i=\vec a_i$
> **Ans (a).** The dual basis is biorthogonal to the original. *Trick:* this is exactly Q94 ($\vec u\!\cdot\!\vec a=1$, others $0$).

**Problem 467.** Reciprocal lattice vectors $\vec b_i$ satisfy
(a) $\vec a_i\!\cdot\!\vec b_j=2\pi\delta_{ij}$  (b) $\vec a_i\!\cdot\!\vec b_j=1$  (c) $\vec a_i=\vec b_i$  (d) $\vec a_i\!\cdot\!\vec b_j=0$
> **Ans (a).** The reciprocal lattice is the physics dual basis. *Trick:* same biorthogonality as Q94, with a $2\pi$ convention.

**Problem 468.** $(A^{T})^{-1}=$
(a) $(A^{-1})^{T}$  (b) $A^{-1}$  (c) $A^{T}$  (d) $A$
> **Ans (a).** Transpose and inverse commute. *Trick:* the columns of $(A^{-1})^T$ are the rows of $A^{-1}$ — the dual vectors (Q94).

**Problem 469.** If $A$ is orthogonal (columns orthonormal), the dual basis $\vec u_i$ is
(a) the same as the original $\vec a_i$  (b) the negatives  (c) orthogonal to the original  (d) zero
> **Ans (a).** $A^T=A^{-1}\Rightarrow(A^T)^{-1}=A$. *Trick:* an orthonormal basis is **self‑dual** — the dual coincides with the original.

**Problem 470.** If the direct lattice has unit‑cell volume $V$, the reciprocal lattice unit‑cell volume is
(a) $\dfrac{(2\pi)^3}{V}$  (b) $V$  (c) $V^{2}$  (d) $2\pi V$
> **Ans (a).** The reciprocal volume is inversely proportional to $V$. *Trick:* the dual basis's "Jacobian" inverts the cell volume.

---

# SET 95 — Radius of convergence via the binomial series
**Origin (Q95):** $\dfrac{1}{x^2+4}=\dfrac14\big(1+\tfrac{x^2}{4}\big)^{-1}$ converges for $\big|\tfrac{x^2}{4}\big|<1$, i.e. $-2<x<2$. **Twists:** the binomial series, the Q95 region, the complex poles, the geometric special case, the radius.

**Problem 471.** The binomial series $(1+u)^p=\sum\binom pn u^n$ (non‑integer $p$) converges for
(a) $|u|<1$  (b) all $u$  (c) $|u|>1$  (d) $u>0$
> **Ans (a).** Radius $1$ in $u$. *Trick:* the binomial series has unit radius (unless $p$ is a non‑negative integer, when it terminates).

**Problem 472.** The Taylor series of $\dfrac{1}{x^{2}+4}$ about $x=0$ converges for
(a) $-2<x<2$  (b) all $x$  (c) $|x|>2$  (d) all $x$ except $\pm2$
> **Ans (a).** $\big|\tfrac{x^2}{4}\big|<1\Rightarrow|x|<2$. *Trick:* the binomial form caps convergence at $|x|<2$ (Q95).

**Problem 473.** $\dfrac{1}{x^{2}+4}$ has (complex) singularities at
(a) $\pm2i$  (b) $\pm2$  (c) $\pm4$  (d) $0$
> **Ans (a).** $x^2+4=0\Rightarrow x=\pm2i$. *Trick:* the radius equals the distance $2$ to these poles.

**Problem 474.** $\dfrac{1}{1-u}$ is the binomial series with exponent
(a) $p=-1$  (b) $p=1$  (c) $p=\tfrac12$  (d) $p=2$
> **Ans (a).** $(1-u)^{-1}=\sum u^n$. *Trick:* the geometric series is the $p=-1$ case of the binomial series.

**Problem 475.** The radius of convergence of the series for $\dfrac{1}{x^{2}+4}$ is
(a) $2$  (b) $4$  (c) $\infty$  (d) $1$
> **Ans (a).** $|\pm2i|=2$. *Trick:* radius $=$ distance to the nearest singularity (consistent with Part 8's principle).

---

# SET 96 — Homogeneous systems; $\det=0$
**Origin (Q96):** $A\vec x=0$ has a non‑trivial solution iff $\det A=0$, giving $b=c+1$ and $\tfrac{1}{\sqrt6}(1,-2,1)$. **Twists:** the condition, the trivial solution, the nullity, the Q96 condition, normalization.

**Problem 476.** The homogeneous system $A\vec x=0$ ($A$ square) has a non‑trivial solution iff
(a) $\det A=0$  (b) $\det A\neq0$  (c) $A$ is symmetric  (d) $A=0$
> **Ans (a).** A singular matrix has a non‑trivial null space. *Trick:* this is the gateway condition for Q96.

**Problem 477.** The homogeneous system $A\vec x=0$ always has
(a) the trivial solution $\vec x=0$  (b) infinitely many solutions  (c) no solution  (d) a unique non‑zero solution
> **Ans (a).** $\vec x=0$ always satisfies it. *Trick:* the question is only whether **other** solutions exist.

**Problem 478.** For a $3\times3$ matrix of rank $2$, the null space (solutions of $A\vec x=0$) has dimension
(a) $1$  (b) $2$  (c) $0$  (d) $3$
> **Ans (a).** Nullity $=n-\text{rank}=3-2=1$. *Trick:* a one‑parameter family of solutions (as in Q96).

**Problem 479.** For $\begin{pmatrix}1&1&1\\1&2&3\\2&b&2c\end{pmatrix}$, a non‑trivial solution exists iff
(a) $b=c+1$  (b) $b=2c$  (c) $c=2b$  (d) $b=c$
> **Ans (a).** $\det=0$ gives $2c-2b+2=0$. *Trick:* expand the determinant to get $b=c+1$ (Q96).

**Problem 480.** The null vector $(1,-2,1)$ normalized is
(a) $\dfrac{1}{\sqrt6}(1,-2,1)$  (b) $\dfrac{1}{\sqrt3}(1,-2,1)$  (c) $\dfrac13(1,-2,1)$  (d) $(1,-2,1)$
> **Ans (a).** $|(1,-2,1)|=\sqrt{1+4+1}=\sqrt6$. *Trick:* divide by $\sqrt6$ (Q96).

---

# SET 97 — Solving an ODE via the Laplace transform
**Origin (Q97):** $\dot y+ay=e^{-bt}$, $y(0)=0\Rightarrow Y(s)=\dfrac{1}{(s+a)(s+b)}$. **Twists:** $\mathcal L[\dot y]$, the transformed equation, $Y(s)$, the inverse, why it helps.

**Problem 481.** $\mathcal L\!\big[\dfrac{dy}{dt}\big]=$
(a) $sY(s)-y(0)$  (b) $sY(s)$  (c) $\dfrac{Y(s)}{s}$  (d) $Y'(s)$
> **Ans (a).** Differentiation $\to$ multiplication by $s$, minus the initial value. *Trick:* the $-y(0)$ is the first step of Q97.

**Problem 482.** Taking the Laplace transform of $\dot y+ay=e^{-bt}$ with $y(0)=0$ gives
(a) $(s+a)Y=\dfrac{1}{s+b}$  (b) $(s-a)Y=\dfrac{1}{s+b}$  (c) $sY=\dfrac{1}{s+b}$  (d) $(s+a)Y=\dfrac{s}{s+b}$
> **Ans (a).** $sY-0+aY=\dfrac{1}{s+b}$. *Trick:* the $y(0)=0$ removes the initial‑value term (Q97).

**Problem 483.** From $(s+a)Y=\dfrac{1}{s+b}$, $Y(s)=$
(a) $\dfrac{1}{(s+a)(s+b)}$  (b) $\dfrac{1}{s+a}$  (c) $\dfrac{s+b}{s+a}$  (d) $\dfrac{1}{s+a+b}$
> **Ans (a).** Divide to isolate $Y$. *Trick:* Q97's answer.

**Problem 484.** $\mathcal L^{-1}\!\Big[\dfrac{1}{(s+a)(s+b)}\Big]$ ($a\neq b$) is
(a) $\dfrac{e^{-bt}-e^{-at}}{a-b}$  (b) $e^{-at}+e^{-bt}$  (c) $e^{-(a+b)t}$  (d) $t\,e^{-at}$
> **Ans (a).** Partial fractions give a difference of exponentials. *Trick:* this is the full solution $y(t)$ behind Q97.

**Problem 485.** Applying the Laplace transform to a constant‑coefficient ODE turns it into
(a) an algebraic equation in $s$  (b) another ODE  (c) an integral equation  (d) a PDE
> **Ans (a).** Derivatives become powers of $s$. *Trick:* converting calculus to algebra is the whole point of Q97.

---

# SET 98 — Frobenius method; regular singular points
**Origin (Q98):** $xy''+y'+xy=0$ (Bessel order $0$) has a repeated indicial root $r=0$, so only **one** power series solution. **Twists:** the singular point, ordinary‑point count, the indicial equation, the repeated root, the Bessel identity.

**Problem 486.** For $xy''+y'+xy=0$, the point $x=0$ is
(a) a regular singular point  (b) an ordinary point  (c) an irregular singular point  (d) not special
> **Ans (a).** The leading ($y''$) coefficient $x$ vanishes there, but mildly enough for Frobenius. *Trick:* singular, but **regular** — Frobenius still applies.

**Problem 487.** At an **ordinary** point, a 2nd‑order linear ODE has how many independent power series solutions?
(a) $2$  (b) $1$  (c) $0$  (d) infinitely many
> **Ans (a).** Ordinary points always give two. *Trick:* contrast with Q98's singular point, which gives only one.

**Problem 488.** Substituting $y=\sum a_n x^{n+r}$ into $xy''+y'+xy=0$ gives the indicial equation
(a) $r^{2}=0$  (b) $r^{2}-1=0$  (c) $r=1$  (d) $r^{2}+1=0$
> **Ans (a).** The lowest‑order terms give $r^2 x^{r-1}=0$. *Trick:* a repeated root $r=0$.

**Problem 489.** When the indicial equation has a repeated root, the number of **pure power series** solutions is
(a) $1$  (b) $2$  (c) $0$  (d) $3$
> **Ans (a).** The second solution carries a $\ln x$. *Trick:* a repeated indicial root yields exactly one analytic solution (Q98's answer).

**Problem 490.** The equation $xy''+y'+xy=0$ is
(a) Bessel's equation of order $0$  (b) Legendre's equation  (c) Hermite's equation  (d) the harmonic oscillator
> **Ans (a).** Dividing by $x$ gives $y''+\tfrac1x y'+y=0$. *Trick:* its solutions are $J_0$ (analytic) and $Y_0$ (with a log) — confirming just one power series solution.

---

# SET 99 — Generators of unitary groups are anti‑hermitian
**Origin (Q99):** $U=e^{X}$ unitary requires $X^\dagger=-X$ (anti‑hermitian). **Twists:** the generator condition, $iX$, the $SU(2)$ generators, tracelessness, the exponential map.

**Problem 491.** For $U=e^{X}$ to be unitary, the generator $X$ must be
(a) anti‑hermitian ($X^\dagger=-X$)  (b) hermitian  (c) symmetric  (d) zero
> **Ans (a).** $U^\dagger U=I\Rightarrow X^\dagger=-X$. *Trick:* this is exactly Q99.

**Problem 492.** If $X$ is anti‑hermitian, then $iX$ is
(a) hermitian  (b) anti‑hermitian  (c) unitary  (d) zero
> **Ans (a).** Multiplying by $i$ flips $X^\dagger=-X$ to $(iX)^\dagger=iX$. *Trick:* this is why physics writes $U=e^{iH}$ with $H$ hermitian.

**Problem 493.** The generators of $SU(2)$ are proportional to
(a) the Pauli matrices $\sigma_j$  (b) the identity  (c) symmetric real matrices  (d) diagonal matrices
> **Ans (a).** $U=\exp(i\theta\,\vec\sigma\!\cdot\!\hat n/2)$. *Trick:* the (hermitian) Pauli matrices are the generators, entering with an $i$.

**Problem 494.** The generators of $SU(n)$ (not just $U(n)$) must additionally satisfy
(a) $\operatorname{Tr}X=0$  (b) $\operatorname{Tr}X=1$  (c) $\det X=1$  (d) $X=X^\dagger$
> **Ans (a).** $\det U=e^{\operatorname{Tr}X}=1\Rightarrow\operatorname{Tr}X=0$. *Trick:* the "$S$" (special, unit determinant) forces traceless generators.

**Problem 495.** A Lie‑group element near the identity is written as
(a) $U=e^{X}$  (b) $U=X$  (c) $U=1+X^{2}$  (d) $U=X^{-1}$
> **Ans (a).** The exponential map. *Trick:* $\exp$ connects the Lie algebra (generators) to the group (Q99's setup).

---

# SET 100 — Euler's method; truncation error
**Origin (Q100):** Euler's method for $\tfrac{dy}{dx}=\alpha x^2$ has relative error $\propto1/n$ (first‑order). **Twists:** the formula, the global order, local vs global, RK4 comparison, the Q100 result.

**Problem 496.** Euler's method updates as
(a) $y_{i+1}=y_i+h\,f(x_i,y_i)$  (b) $y_{i+1}=y_i+f(x_i,y_i)$  (c) $y_{i+1}=h\,f(x_i,y_i)$  (d) $y_{i+1}=y_i+h^{2}$
> **Ans (a).** Step forward by $h$ times the slope. *Trick:* the simplest forward step (Q100).

**Problem 497.** Euler's method has a **global** error proportional to
(a) $h$  (b) $h^{2}$  (c) $h^{3}$  (d) constant
> **Ans (a).** It is a first‑order method. *Trick:* global error $\propto h\propto1/n$ (Q100's answer).

**Problem 498.** The **local** (single‑step) truncation error of Euler's method is
(a) $O(h^{2})$  (b) $O(h)$  (c) $O(h^{3})$  (d) $O(1)$
> **Ans (a).** The per‑step error is $h^2$. *Trick:* it accumulates over $\sim1/h$ steps to give the global $O(h)$.

**Problem 499.** Compared to Euler (error $\propto h$), the fourth‑order Runge–Kutta method has global error proportional to
(a) $h^{4}$  (b) $h$  (c) $h^{2}$  (d) $h^{3}$
> **Ans (a).** RK4 is fourth‑order. *Trick:* far more accurate than Euler at the same step size.

**Problem 500.** For $\tfrac{dy}{dx}=\alpha x^{2}$ solved by Euler's method with $n$ steps, the relative error is proportional to
(a) $\dfrac1n$  (b) $\dfrac1{n^{2}}$  (c) $\dfrac1{n^{4}}$  (d) $\dfrac1{n^{3}}$
> **Ans (a).** First‑order $\Rightarrow$ error $\propto h=\dfrac{\text{interval}}{n}$. *Trick:* halving the step roughly halves the error (Q100).

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: an $SU(2)$ half‑angle gives a full $3$‑D rotation (with $4\pi$ periodicity and the double cover); a matrix family is a group only if products stay in the family (entries that **add** close, cross‑terms don't); Poisson $P(0)=e^{-\mu}$ lets you read off the mean; the columns of $(A^T)^{-1}$ are the biorthogonal **dual basis**; the binomial series caps convergence at the nearest complex pole; $A\vec x=0$ needs $\det A=0$ for a non‑trivial solution; the Laplace transform turns an ODE into algebra; a repeated indicial root gives only **one** power series solution; unitary‑group generators are anti‑hermitian (and traceless for $SU(n)$); and Euler's method is first‑order, with error $\propto1/n$. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 500 problems across the first 100 originals (Q1–Q100).**
