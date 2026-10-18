# 50 Practice Problems — Part 2 (CSIR‑NET/JRF style)

**Built from problems 11–20 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method as Part 1: extract the *core concept* of each original problem, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **51–100** to continue Part 1.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q11–Q13 = Dec 2011**, **Q14–Q20 = June 2012** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q11–Q20)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q11 | Wronskian | Abel's identity $W=W_0\,e^{-\int P\,dt}$ |
| Q12 | Laplace transform | Periodic / piecewise functions; geometric series of pulses |
| Q13 | Taylor series | Expansion about a **non‑zero** point; sign pattern |
| Q14 | Plane geometry | Normal to a plane $=\nabla(\text{LHS})$ |
| Q15 | Eigenvalues | Spectrum of a **rank‑1 / outer‑product** matrix |
| Q16 | Laurent series | Different expansions in different **annular regions** |
| Q17 | Harmonic conjugate | Recover $v$ from $u$ via Cauchy–Riemann |
| Q18 | $\delta$‑forced ODE | Jump in $y'$ across a delta source |
| Q19 | Probability | Law of total probability (weighted average) |
| Q20 | Eigenvalues | Skew‑symmetric / cross‑product matrix |

---

# SET 11 — Wronskian & Abel's identity
**Origin (Q11):** for $x''+2x'+f(t)x=0$, $W=W_0e^{-\int P\,dt}=e^{-2t}$, so $W(1)=e^{-2}$. **Twists:** sign of $P$, $t$‑dependent $P$, the vanishing theorem, normalizing the leading coefficient, direct computation.

**Problem 51.** $x_1,x_2$ are independent solutions of $x''-3x'+2x=0$, with $W(0)=2$. Then $W(1)=$
(a) $2e^{3}$  (b) $2e^{-3}$  (c) $e^{3}$  (d) $2e^{2}$
> **Ans (a).** $P=-3\Rightarrow W=W_0e^{-\int(-3)dt}=2e^{3t}$, so $W(1)=2e^3$. *Trick:* $P$ is **negative**, so the Wronskian **grows**, not decays.

**Problem 52.** For $x''+2t\,x'+q(t)x=0$ with $W(0)=1$, $W(1)=$
(a) $e^{-1}$  (b) $e^{-2}$  (c) $e$  (d) $1$
> **Ans (a).** $P=2t\Rightarrow W=e^{-\int_0^t 2t'\,dt'}=e^{-t^{2}}$, so $W(1)=e^{-1}$. *Trick:* $\int 2t\,dt=t^{2}$ — not $2t$; the answer is $e^{-1}$, not $e^{-2}$.

**Problem 53.** If the Wronskian of two solutions of a 2nd‑order linear homogeneous ODE vanishes at one point $t_0$, then
(a) $W(t)=0$ for all $t$  (b) $W=0$ only at $t_0$  (c) $W$ may be nonzero elsewhere  (d) the ODE has no solution
> **Ans (a).** By Abel, $W=W(t_0)e^{-\int P}$; if $W(t_0)=0$ then $W\equiv0$. *Trick:* a Wronskian of solutions is **either identically zero or never zero** — it can't dip to zero at one point only.

**Problem 54.** For $2x''+4x'+x=0$ with $W(0)=1$, $W(t)=$
(a) $e^{-2t}$  (b) $e^{-4t}$  (c) $e^{-t}$  (d) $e^{-t/2}$
> **Ans (a).** First put it in standard form: $x''+2x'+\tfrac12x=0$, so $P=2$. *Trick:* you must **divide by the leading coefficient** before reading off $P$; $P=4/2=2$, not $4$.

**Problem 55.** The Wronskian of $e^{t}$ and $e^{2t}$ is
(a) $e^{3t}$  (b) $e^{2t}$  (c) $0$  (d) $2e^{3t}$
> **Ans (a).** $W=e^{t}(2e^{2t})-e^{2t}(e^{t})=2e^{3t}-e^{3t}=e^{3t}$. *Trick:* it's $f g'-g f'$ — the two $e^{3t}$ terms don't cancel, they subtract to one.

---

# SET 12 — Laplace transforms (periodic / piecewise)
**Origin (Q12):** square wave $\to \dfrac{1}{s(1+e^{-s})}$ via a geometric series of unit pulses. **Twists:** single boxcar, the periodic‑function formula, shifted step, delta, the $\pm1$ wave.

**Problem 56.** The Laplace transform of $f(t)=1$ on $0\le t<1$ and $0$ thereafter (a single pulse) is
(a) $\dfrac{1-e^{-s}}{s}$  (b) $\dfrac1s$  (c) $\dfrac{1+e^{-s}}{s}$  (d) $\dfrac{e^{-s}}{s}$
> **Ans (a).** $\int_0^1 e^{-st}dt=\dfrac{1-e^{-s}}{s}$. *Trick:* a **finite** pulse gives $1-e^{-s}$ — there's no infinite geometric series to sum.

**Problem 57.** For a function $f(t)$ periodic with period $T$, its Laplace transform is
(a) $\dfrac{1}{1-e^{-sT}}\displaystyle\int_0^T e^{-st}f(t)\,dt$  (b) $\displaystyle\int_0^T e^{-st}f\,dt$  (c) $\dfrac{1}{1+e^{-sT}}\displaystyle\int_0^\infty e^{-st}f\,dt$  (d) $\dfrac1s\displaystyle\int_0^T f\,dt$
> **Ans (a).** Sum the geometric series over periods $\Rightarrow$ the factor $1/(1-e^{-sT})$. *Trick:* this $1/(1-e^{-sT})$ is exactly what produced Q12's $1/(1+e^{-s})$ after factoring.

**Problem 58.** $\mathcal L\{u(t-a)\}$ for the unit step (Heaviside) $u$ is
(a) $\dfrac{e^{-as}}{s}$  (b) $\dfrac1s$  (c) $e^{-as}$  (d) $\dfrac{e^{as}}{s}$
> **Ans (a).** Second shifting theorem: a time shift $a$ multiplies by $e^{-as}$. *Trick:* the step still carries a $1/s$; the shift only adds $e^{-as}$.

**Problem 59.** $\mathcal L\{\delta(t-a)\}=$
(a) $e^{-as}$  (b) $\dfrac{e^{-as}}{s}$  (c) $1$  (d) $s\,e^{-as}$
> **Ans (a).** $\int_0^\infty e^{-st}\delta(t-a)\,dt=e^{-as}$. *Trick:* the delta gives a **pure exponential** — **no** $1/s$ (unlike the step in Q58).

**Problem 60.** A square wave equal to $+1$ on $[0,1)$ and $-1$ on $[1,2)$, period $2$, has Laplace transform
(a) $\dfrac1s\tanh\!\big(\tfrac s2\big)$  (b) $\dfrac1s\coth\!\big(\tfrac s2\big)$  (c) $\dfrac{1}{s(1+e^{-s})}$  (d) $\dfrac{1-e^{-s}}{s}$
> **Ans (a).** Numerator $=\dfrac{(1-e^{-s})^2}{s}$, denominator $1-e^{-2s}=(1-e^{-s})(1+e^{-s})$, giving $\dfrac{1-e^{-s}}{s(1+e^{-s})}=\dfrac1s\tanh\tfrac s2$. *Trick:* the **alternating** $\pm1$ wave gives $\tanh$, while Q12's $0/1$ wave gives option (c).

---

# SET 13 — Taylor series about a non‑zero point
**Origin (Q13):** $\sin x$ about $\tfrac\pi4=\tfrac1{\sqrt2}\big[1+h-\tfrac{h^2}{2!}-\tfrac{h^3}{3!}\cdots\big]$, $h=x-\tfrac\pi4$. **Twists:** $\cos$ about $\tfrac\pi4$, $e^x$ about $1$, $\ln x$ about $1$, a coefficient, a square root.

**Problem 61.** With $h=x-\tfrac\pi4$, the Taylor series of $\cos x$ about $\tfrac\pi4$ is
(a) $\tfrac1{\sqrt2}\big[1-h-\tfrac{h^2}{2!}+\tfrac{h^3}{3!}\cdots\big]$  (b) $\tfrac1{\sqrt2}\big[1+h-\tfrac{h^2}{2!}-\cdots\big]$  (c) $1-\tfrac{h^2}{2}+\cdots$  (d) $\tfrac1{\sqrt2}\big[1+h+\tfrac{h^2}{2!}+\cdots\big]$
> **Ans (a).** $f'=-\sin\Rightarrow f'(\tfrac\pi4)=-\tfrac1{\sqrt2}$, so the linear term is $-h$. *Trick:* $\cos$ starts $1-h$ (option (b) is the $\sin$ pattern from Q13).

**Problem 62.** The Taylor series of $e^{x}$ about $x=1$ is
(a) $e\big[1+(x-1)+\tfrac{(x-1)^2}{2!}+\cdots\big]$  (b) $1+x+\tfrac{x^2}{2!}+\cdots$  (c) $e\big[1-(x-1)+\cdots\big]$  (d) $\tfrac1e\big[1+(x-1)+\cdots\big]$
> **Ans (a).** Every derivative is $e^x$, equal to $e$ at $x=1$; center on $(x-1)$. *Trick:* pull out the constant $e$ and shift to $(x-1)$ — it's $e\cdot e^{x-1}$.

**Problem 63.** The Taylor series of $\ln x$ about $x=1$ is
(a) $(x-1)-\tfrac{(x-1)^2}{2}+\tfrac{(x-1)^3}{3}-\cdots$  (b) $1+(x-1)+\cdots$  (c) $(x-1)+\tfrac{(x-1)^2}{2}+\cdots$  (d) $x-\tfrac{x^2}{2}+\cdots$
> **Ans (a).** $\ln1=0$; derivatives give $1,-1,2,\dots$ so coefficients are $1,-\tfrac12,\tfrac13,\dots$. *Trick:* **no constant term**, and the coefficients are $1/n$ (not $1/n!$).

**Problem 64.** In the Taylor expansion of $\sin x$ about $\tfrac\pi4$, the coefficient of $(x-\tfrac\pi4)^2$ is
(a) $-\dfrac{1}{2\sqrt2}$  (b) $\dfrac{1}{2\sqrt2}$  (c) $-\dfrac1{\sqrt2}$  (d) $\dfrac12$
> **Ans (a).** $\dfrac{f''(\pi/4)}{2!}=\dfrac{-\sin(\pi/4)}{2}=-\dfrac{1}{2\sqrt2}$. *Trick:* include **both** the $-\sin$ sign and the $2!$.

**Problem 65.** The first two terms of the Taylor expansion of $\sqrt{x}$ about $x=4$ are
(a) $2+\tfrac14(x-4)$  (b) $2+\tfrac12(x-4)$  (c) $2+\tfrac14x$  (d) $\tfrac12+\tfrac14(x-4)$
> **Ans (a).** $f(4)=2$, $f'(x)=\tfrac1{2\sqrt x}\Rightarrow f'(4)=\tfrac14$. *Trick:* center on $(x-4)$; the slope is $\tfrac14$, not $\tfrac12$.

---

# SET 14 — Normal to a plane $=\nabla(\text{LHS})$
**Origin (Q14):** a vector $\perp$ to everything in $x+y+z=5$ is the normal $\hat i+\hat j+\hat k$. **Twists:** signed coefficients, unit normal, angle between planes, an **in‑plane** direction, distance.

**Problem 66.** A vector normal to the plane $2x-3y+z=7$ is
(a) $2\hat i-3\hat j+\hat k$  (b) $\hat i+\hat j+\hat k$  (c) $\hat i-\hat j+\hat k$  (d) $7(\hat i+\hat j+\hat k)$
> **Ans (a).** The coefficients are the normal components. *Trick:* keep the sign on $y$ ($-3$); the constant $7$ is irrelevant to direction.

**Problem 67.** The **unit** normal to the plane $x-2y+2z=0$ is
(a) $\tfrac13(1,-2,2)$  (b) $(1,-2,2)$  (c) $\tfrac13(1,2,2)$  (d) $\tfrac1{\sqrt3}(1,-2,2)$
> **Ans (a).** $|(1,-2,2)|=\sqrt{1+4+4}=3$. *Trick:* normalize by $3$, not $\sqrt3$ — $1+4+4=9$.

**Problem 68.** The angle between the planes $x+y+z=1$ and $x-y+z=2$ is
(a) $\cos^{-1}\!\tfrac13$  (b) $\cos^{-1}\!\tfrac1{\sqrt3}$  (c) $90^\circ$  (d) $\cos^{-1}\!\tfrac23$
> **Ans (a).** Use the normals: $\cos\theta=\dfrac{(1,1,1)\cdot(1,-1,1)}{\sqrt3\,\sqrt3}=\dfrac13$. *Trick:* the angle between planes is the angle between their **normals**.

**Problem 69.** A vector that **lies in** (is parallel to) the plane $x+y+z=5$ is
(a) $\hat i-\hat j$  (b) $\hat i+\hat j+\hat k$  (c) $(1,1,0)$  (d) $(2,2,2)$
> **Ans (a).** In‑plane vectors are $\perp$ to the normal $(1,1,1)$, i.e. their components sum to zero: $1-1+0=0$. *Trick:* (b) is the **normal itself**, the opposite of in‑plane.

**Problem 70.** The perpendicular distance from the origin to the plane $x+y+z=5$ is
(a) $\dfrac{5}{\sqrt3}$  (b) $\dfrac53$  (c) $5$  (d) $\dfrac{\sqrt3}{5}$
> **Ans (a).** Distance $=\dfrac{|d|}{|\vec n|}=\dfrac{5}{\sqrt3}$. *Trick:* divide the constant by the **magnitude** of the normal $(1,1,1)$.

---

# SET 15 — Eigenvalues of a rank‑1 (outer‑product) matrix
**Origin (Q15):** $A=\begin{pmatrix}1&2&3\\2&4&6\\3&6&9\end{pmatrix}=\vec u\,\vec u^{\,T}$, $\vec u=(1,2,3)$; eigenvalues $0,0,14$ ($=|\vec u|^2=$ trace). **Twists:** new $\vec u$, the general nonzero eigenvalue, the eigenvector, det, the power.

**Problem 71.** The eigenvalues of $\begin{pmatrix}1&1&2\\1&1&2\\2&2&4\end{pmatrix}$ are
(a) $0,0,6$  (b) $0,0,4$  (c) $1,1,4$  (d) $0,0,1$
> **Ans (a).** It is $\vec u\,\vec u^{\,T}$ with $\vec u=(1,1,2)$; nonzero eigenvalue $=|\vec u|^2=1+1+4=6=$ trace, rest $0$. *Trick:* the lone nonzero eigenvalue equals the trace.

**Problem 72.** The single nonzero eigenvalue of a rank‑1 matrix $\vec u\,\vec v^{\,T}$ is
(a) $\vec v\cdot\vec u$  (b) $|\vec u|\,|\vec v|$  (c) $|\vec u|^2$  (d) $1$
> **Ans (a).** $(\vec u\,\vec v^{\,T})\vec u=\vec u(\vec v^{\,T}\vec u)=(\vec v\!\cdot\!\vec u)\vec u$. *Trick:* it's the **dot product** $\vec v\cdot\vec u$ (= trace), not $|\vec u||\vec v|$.

**Problem 73.** For $A=\vec u\,\vec u^{\,T}$, the eigenvector of the nonzero eigenvalue is
(a) $\vec u$  (b) any vector $\perp\vec u$  (c) $(1,1,1)$  (d) $\vec u^{\,T}$
> **Ans (a).** $A\vec u=|\vec u|^2\vec u$. *Trick:* vectors **perpendicular** to $\vec u$ are the eigenvectors of the **zero** eigenvalue.

**Problem 74.** For $A=\begin{pmatrix}1&2&3\\2&4&6\\3&6&9\end{pmatrix}$, $\det(A)=$
(a) $0$  (b) $14$  (c) $196$  (d) $1$
> **Ans (a).** Rank $1\Rightarrow$ two zero eigenvalues $\Rightarrow\det=0$ (the rows are proportional). *Trick:* proportional rows force a vanishing determinant.

**Problem 75.** For $A=\vec u\,\vec u^{\,T}$ from Q15 (where $|\vec u|^2=14$), $A^{2}=$
(a) $14A$  (b) $A$  (c) $196A$  (d) $0$
> **Ans (a).** $A^2=\vec u(\vec u^{\,T}\vec u)\vec u^{\,T}=14\,\vec u\vec u^{\,T}=14A$. *Trick:* $A^2=(\vec u\!\cdot\!\vec u)A$ — the same "$M^2\propto M$" collapse seen for the all‑ones matrix.

---

# SET 16 — Laurent series in annular regions
**Origin (Q16):** $\dfrac{1}{(z-1)(z-2)}$ in $1<|z|<2$ via partial fractions, each piece expanded for its region. **Twists:** inside disk, outside, counting regions, residue, partial fractions.

**Problem 76.** In the region $|z|<1$, the expansion of $\dfrac{1}{(z-1)(z-2)}$ about $z=0$ contains
(a) only non‑negative powers of $z$  (b) only negative powers  (c) both signs of powers  (d) a $1/z$ term
> **Ans (a).** The nearest singularity is at $z=1$, so the function is analytic in $|z|<1$ ⇒ a **Taylor** series. *Trick:* no principal part inside the disk.

**Problem 77.** In the region $|z|>2$, the expansion of $\dfrac{1}{(z-1)(z-2)}$ about $z=0$ contains
(a) only negative powers of $z$  (b) only positive powers  (c) a constant plus positive powers  (d) the form $\tfrac{1}{1-z}$
> **Ans (a).** Outside both singularities, expand in $1/z$ ⇒ only negative powers. *Trick:* the exterior region gives a series purely in $z^{-1}$.

**Problem 78.** How many distinct power/Laurent expansions about $z=0$ does $\dfrac{1}{(z-1)(z-2)}$ have?
(a) $3$  (b) $1$  (c) $2$  (d) infinitely many
> **Ans (a).** Singularities at $1$ and $2$ split the plane into $|z|<1,\ 1<|z|<2,\ |z|>2$. *Trick:* two singular radii ⇒ **three** annular regions, each with its own series.

**Problem 79.** The residue of $\dfrac{1}{(z-1)(z-2)}$ at $z=1$ is
(a) $-1$  (b) $1$  (c) $0$  (d) $-\tfrac12$
> **Ans (a).** $\displaystyle\lim_{z\to1}(z-1)f=\dfrac1{1-2}=-1$ (the coefficient of $(z-1)^{-1}$). *Trick:* the residue is this single Laurent coefficient.

**Problem 80.** The partial‑fraction form of $\dfrac{1}{(z-1)(z-2)}$ is
(a) $\dfrac{1}{z-2}-\dfrac{1}{z-1}$  (b) $\dfrac{1}{z-1}-\dfrac{1}{z-2}$  (c) $\dfrac{1}{z-1}+\dfrac{1}{z-2}$  (d) $\dfrac{2}{z-2}-\dfrac{1}{z-1}$
> **Ans (a).** Residues: $+1$ at $z=2$, $-1$ at $z=1$. *Trick:* watch the signs — the $z=1$ term is **subtracted**.

---

# SET 17 — Harmonic conjugate (Cauchy–Riemann)
**Origin (Q17):** $u=x+\tfrac12(x^2-y^2)\Rightarrow v=y+xy$ by integrating the CR equations. **Twists:** $u\to v$, $v\to u$, assemble $f(z)$, a cubic, the uniqueness clause.

**Problem 81.** If $u=x^{2}-y^{2}$ is the real part of an analytic $f$, then (up to a constant) $v=$
(a) $2xy$  (b) $x^{2}-y^{2}$  (c) $-2xy$  (d) $x^{2}+y^{2}$
> **Ans (a).** $u_x=2x=v_y$ and $-u_y=2y=v_x$ both give $v=2xy$. *Trick:* this is just $f=z^2$ ($v=\operatorname{Im}z^2$).

**Problem 82.** If $v=2xy$ is the **imaginary** part of an analytic $f$, then (up to a constant) $u=$
(a) $x^{2}-y^{2}$  (b) $2xy$  (c) $x^{2}+y^{2}$  (d) $-x^{2}+y^{2}$
> **Ans (a).** $v_y=2x=u_x$ and $v_x=2y=-u_y$ give $u=x^2-y^2$. *Trick:* going $v\to u$ uses the CR equations the **other** way; mind the sign that flips.

**Problem 83.** If $u=x^{2}-y^{2}$ and $v=2xy$, the analytic function is $f(z)=$
(a) $z^{2}$  (b) $\bar z^{2}$  (c) $2z$  (d) $e^{z}$
> **Ans (a).** $u+iv=(x^2-y^2)+2ixy=z^2$. *Trick:* assemble $u+iv$ and recognize $z^2$ — not $\bar z^2$.

**Problem 84.** The harmonic conjugate $v$ (with $v(0)=0$) of $u=x^{3}-3xy^{2}$ is
(a) $3x^{2}y-y^{3}$  (b) $y^{3}-3x^{2}y$  (c) $3xy^{2}$  (d) $x^{3}-3xy^{2}$
> **Ans (a).** $u=\operatorname{Re}(z^3)$, so $v=\operatorname{Im}(z^3)=3x^2y-y^3$. *Trick:* recognize $u$ as $\operatorname{Re}(z^3)$; the conjugate is the imaginary part.

**Problem 85.** Given a harmonic function $u$, its harmonic conjugate $v$ is determined up to
(a) an additive real constant  (b) a multiplicative constant  (c) an additive function of $x$  (d) nothing — it is unique
> **Ans (a).** Only an additive real constant is free (so $f$ is fixed up to a pure imaginary constant). *Trick:* it's an additive **constant**, not an arbitrary function.

---

# SET 18 — Delta‑forced ODEs (jump conditions)
**Origin (Q18):** $\sin x\,y''+\cos x\,y'=\delta(x-\tfrac\pi2)$; integrating across $\tfrac\pi2$ gives a jump in $y'$ of $1$ (because $\sin\tfrac\pi2=1$). **Twists:** unit jump, scaled coefficient, what stays continuous, the general $1/p(a)$ rule, a different point.

**Problem 86.** Integrating $y''=\delta(x)$ across $x=0$, the jump in $y'$ is
(a) $1$  (b) $0$  (c) $\infty$  (d) undefined
> **Ans (a).** $\displaystyle\int_{0^-}^{0^+}y''\,dx=\big[y'\big]=\int\delta=1$. *Trick:* the unit area of $\delta$ becomes a unit jump in the **first** derivative.

**Problem 87.** For $2y''=\delta(x-a)$, the jump in $y'$ at $a$ is
(a) $\tfrac12$  (b) $2$  (c) $1$  (d) $0$
> **Ans (a).** $2\big[y'\big]=1\Rightarrow\big[y'\big]=\tfrac12$. *Trick:* divide the delta's strength by the **leading coefficient** $2$.

**Problem 88.** For $y''+y=\delta(x)$, across $x=0$
(a) $y$ is continuous and $y'$ jumps by $1$  (b) $y$ jumps by $1$  (c) both are continuous  (d) both jump
> **Ans (a).** A single $\delta$ in the highest ($2$nd) derivative makes $y'$ discontinuous but $y$ continuous. *Trick:* the discontinuity lands one order **below** the highest derivative.

**Problem 89.** For $p(x)\,y''+(\text{lower order})=\delta(x-a)$, the jump in $y'$ at $a$ equals
(a) $\dfrac{1}{p(a)}$  (b) $p(a)$  (c) $1$  (d) $0$
> **Ans (a).** Integrating, only the $p\,y''$ term survives the limit, giving $p(a)\big[y'\big]=1$. *Trick:* this is exactly Q18 — at $x=\tfrac\pi2$, $p=\sin\tfrac\pi2=1$, so the jump is $1$.

**Problem 90.** For $\sin x\,y''+\cos x\,y'=\delta\!\big(x-\tfrac\pi6\big)$, the jump in $y'$ at $\tfrac\pi6$ is
(a) $2$  (b) $1$  (c) $\tfrac12$  (d) $\sqrt3$
> **Ans (a).** $p(\tfrac\pi6)=\sin\tfrac\pi6=\tfrac12$, so jump $=1/p=2$. *Trick:* moving the delta to $\tfrac\pi6$ changes $p$ to $\tfrac12$ — the jump is now $2$, not $1$.

---

# SET 19 — Law of total probability
**Origin (Q19):** two boxes, equal prior, $P(\text{white})=\tfrac12(\tfrac35+\tfrac47)=\tfrac{41}{70}$. **Twists:** new counts, unequal priors, the Bayes reverse, three sources, the formula.

**Problem 91.** Box I has 1 red, 2 green; Box II has 2 red, 2 green. A box is chosen at random, then a ball. $P(\text{red})=$
(a) $\tfrac{5}{12}$  (b) $\tfrac12$  (c) $\tfrac13$  (d) $\tfrac{7}{12}$
> **Ans (a).** $\tfrac12\big(\tfrac13+\tfrac12\big)=\tfrac12\cdot\tfrac56=\tfrac{5}{12}$. *Trick:* average the two **unlike** fractions, don't add raw counts.

**Problem 92.** Box I (chosen with prob $\tfrac23$) is $\tfrac12$ white; Box II (prob $\tfrac13$) is $\tfrac14$ white. $P(\text{white})=$
(a) $\tfrac{5}{12}$  (b) $\tfrac38$  (c) $\tfrac12$  (d) $\tfrac14$
> **Ans (a).** $\tfrac23\cdot\tfrac12+\tfrac13\cdot\tfrac14=\tfrac13+\tfrac1{12}=\tfrac{5}{12}$. *Trick:* the priors are **unequal** — weight by $\tfrac23$ and $\tfrac13$.

**Problem 93.** In Q19's setup (Box I: 2B 3W; Box II: 3B 4W; equal prior), given a **white** ball was drawn, the probability it came from Box I is
(a) $\tfrac{21}{41}$  (b) $\tfrac{20}{41}$  (c) $\tfrac35$  (d) $\tfrac12$
> **Ans (a).** Bayes: $\dfrac{(\tfrac35)(\tfrac12)}{41/70}=\dfrac{3/10}{41/70}=\dfrac{21}{41}$. *Trick:* the posterior reuses Q19's total $\tfrac{41}{70}$ as the denominator.

**Problem 94.** Three urns are equally likely, with white fractions $\tfrac12,\tfrac13,\tfrac14$. The probability a drawn ball is white is
(a) $\tfrac{13}{36}$  (b) $\tfrac13$  (c) $\tfrac{13}{12}$  (d) $\tfrac14$
> **Ans (a).** $\tfrac13\big(\tfrac12+\tfrac13+\tfrac14\big)=\tfrac13\cdot\tfrac{13}{12}=\tfrac{13}{36}$. *Trick:* $\tfrac12+\tfrac13+\tfrac14=\tfrac{13}{12}$, then divide by $3$.

**Problem 95.** The law of total probability writes $P(A)$ over a partition $\{B_i\}$ as
(a) $\displaystyle\sum_i P(A\mid B_i)P(B_i)$  (b) $\displaystyle\sum_i P(B_i\mid A)$  (c) $P(A\mid B)P(B\mid A)$  (d) $\displaystyle\prod_i P(A\mid B_i)$
> **Ans (a).** Sum the conditional probabilities weighted by the priors. *Trick:* it's a **weighted sum** over the partition — the structure behind Q19.

---

# SET 20 — Skew‑symmetric / cross‑product matrix eigenvalues
**Origin (Q20):** $A=\begin{pmatrix}0&-n_3&n_2\\ n_3&0&-n_1\\ -n_2&n_1&0\end{pmatrix}$, $\hat n$ a unit vector; eigenvalues $0,\,i,\,-i$ (char. equation $\lambda^3+\lambda=0$). **Twists:** the general spectrum, odd‑$n$ singularity, non‑unit vector, the cross‑product meaning, $e^A$.

**Problem 96.** The eigenvalues of any real skew‑symmetric matrix are
(a) purely imaginary or zero  (b) all real  (c) all positive  (d) complex with positive real part
> **Ans (a).** $A^T=-A$ forces eigenvalues onto the imaginary axis. *Trick:* skew‑symmetric ⇒ imaginary spectrum (symmetric would be real).

**Problem 97.** The determinant of any $3\times3$ real skew‑symmetric matrix is
(a) $0$  (b) $1$  (c) $\pm1$  (d) depends on entries
> **Ans (a).** $\det A=\det A^T=\det(-A)=(-1)^3\det A\Rightarrow\det A=0$. *Trick:* **odd‑dimensional** skew‑symmetric matrices are always singular (one eigenvalue is $0$).

**Problem 98.** If in Q20 the vector $(n_1,n_2,n_3)$ has magnitude $n$ (not necessarily $1$), the eigenvalues are
(a) $0,\,in,\,-in$  (b) $0,\,i,\,-i$  (c) $0,\,n,\,-n$  (d) $0,0,0$
> **Ans (a).** Char. equation $\lambda^3+n^2\lambda=0\Rightarrow\lambda=0,\pm in$. *Trick:* the $\pm i$ scale to $\pm i|n|$; only a **unit** vector gives exactly $\pm i$.

**Problem 99.** The matrix $A$ in Q20 acts on a vector $\vec r$ as
(a) $\hat n\times\vec r$  (b) $\hat n(\hat n\cdot\vec r)$  (c) $(\hat n\cdot\vec r)\vec r$  (d) $\vec r\times\vec r$
> **Ans (a).** This $[\hat n]_\times$ matrix **is** the cross product $\hat n\times(\cdot)$. *Trick:* its zero eigenvalue has eigenvector $\hat n$, since $\hat n\times\hat n=0$.

**Problem 100.** For a real skew‑symmetric $A$ ($A^T=-A$), the matrix $e^{A}$ is
(a) orthogonal (a rotation), i.e. $e^{A}(e^{A})^{T}=I$  (b) skew‑symmetric  (c) symmetric  (d) singular
> **Ans (a).** $(e^A)^T=e^{A^T}=e^{-A}=(e^A)^{-1}$. *Trick:* exponentiating $\mathfrak{so}(3)$ gives $SO(3)$ — the cross‑product generator of Q20 exponentiates to a **rotation**.

---

### How to use this set
Same drill as Part 1: do each block of 5 cold, then read the **trick line** — that's the lesson. The five inside a block fail in *five different ways* (sign of $P$, $1/(1-e^{-sT})$ factor, $\ln$ has no constant term, normalize‑by‑$3$‑not‑$\sqrt3$, eigenvalue $=$ trace, three annular regions, the sign‑flip in $u\!\leftrightarrow\!v$, jump $=1/p(a)$, weight‑by‑the‑prior, det $=0$ for odd skew‑symmetric). If a block feels automatic, you own the CSIR‑NET concept it grew from.
