# 50 Practice Problems — Part 12 (CSIR‑NET/JRF style)

**Built from problems 111–120 of the *fiziks* "Mathematical Physics Solutions" booklet — the final ten, completing the whole compilation.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **551–600** to continue Parts 1–11.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q111 = June 2018**, **Q112–Q120 = Dec 2018** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q111–Q120)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q111 | Numerical methods | Simpson's rule exactness (low‑degree polynomials) |
| Q112 | Linear algebra | Matrix exponential eigenvalues; $\det e^A=e^{\operatorname{Tr}A}$ |
| Q113 | Special functions | Expanding a polynomial in the Legendre basis |
| Q114 | Complex analysis | Contour integral with multiple poles |
| Q115 | Complex analysis | Path independence of analytic integrals |
| Q116 | ODEs | Euler–Cauchy (equidimensional) equation |
| Q117 | Math methods | Green's‑function construction ($y''=f$) |
| Q118 | Group theory | Unitary‑matrix parameter counting |
| Q119 | Complex analysis | Branch cuts & contour deformation |
| Q120 | Numerical methods | Trapezoidal rule |

---

# SET 111 — Simpson's rule exactness
**Origin (Q111):** the fractional error of $\int_0^1 x\,dx$ by Simpson's $\tfrac13$ rule is $0$ (linear is well within its exactness). **Twists:** the exact degree, the linear case, the error order, why cubics, the value.

**Problem 551.** Simpson's $\tfrac13$ rule integrates exactly all polynomials up to degree
(a) $3$  (b) $1$  (c) $2$  (d) $4$
> **Ans (a).** Exact for cubics. *Trick:* built from parabolas, but the cubic error term cancels by symmetry.

**Problem 552.** The error of Simpson's rule for $\int_0^1 x\,dx$ is
(a) $0$  (b) $0.01$  (c) $0.1$  (d) $0.5$
> **Ans (a).** A straight line is far below degree $3$. *Trick:* exact, so the fractional error is $0$ (Q111).

**Problem 553.** The composite Simpson's $\tfrac13$ rule has an error proportional to
(a) $h^{4}$  (b) $h^{2}$  (c) $h$  (d) $h^{3}$
> **Ans (a).** Fourth‑order accuracy. *Trick:* far better than the trapezoidal $h^2$.

**Problem 554.** Simpson's rule integrates cubics exactly because its leading error depends on
(a) $f^{(4)}$ (which is $0$ for cubics)  (b) $f''$  (c) $f'$  (d) $f$
> **Ans (a).** The error $\propto f^{(4)}$. *Trick:* the fourth derivative vanishes for any polynomial of degree $\le3$.

**Problem 555.** $\displaystyle\int_0^1 x\,dx=$
(a) $\dfrac12$  (b) $1$  (c) $\dfrac13$  (d) $0$
> **Ans (a).** The exact area. *Trick:* Simpson reproduces it exactly (Q111).

---

# SET 112 — Matrix exponential eigenvalues
**Origin (Q112):** $A=\begin{pmatrix}a&0&0\\0&0&a\\0&a&0\end{pmatrix}$ has eigenvalues $a,a,-a$, so $e^A$ has $e^a,e^a,e^{-a}$, and the two "other" eigenvalues multiply to $1$. **Twists:** the eigenvalue map, $\det e^A$, the swap block, the product, the trace.

**Problem 556.** If $A$ has eigenvalue $\lambda$, then $e^{A}$ has eigenvalue
(a) $e^{\lambda}$  (b) $\lambda$  (c) $e\lambda$  (d) $\ln\lambda$
> **Ans (a).** The matrix exponential maps $\lambda\to e^\lambda$ (eigenvectors unchanged). *Trick:* exponentiate the eigenvalues.

**Problem 557.** $\det(e^{A})=$
(a) $e^{\operatorname{Tr}A}$  (b) $e^{\det A}$  (c) $\operatorname{Tr}(e^{A})$  (d) $(\det A)^{e}$
> **Ans (a).** A key identity. *Trick:* $\det e^A=e^{\operatorname{Tr}A}$ (the product of $e^{\lambda_i}$ is $e^{\sum\lambda_i}$).

**Problem 558.** The matrix $\begin{pmatrix}0&a\\a&0\end{pmatrix}$ has eigenvalues
(a) $\pm a$  (b) $a,a$  (c) $0,a$  (d) $\pm ia$
> **Ans (a).** Symmetric/antisymmetric eigenvectors. *Trick:* the off‑diagonal swap gives $\pm a$ (Q112's block).

**Problem 559.** For $A$ with eigenvalues $a,a,-a$, the product of the eigenvalues of $e^{A}$ other than $e^{a}$ is
(a) $1$  (b) $e^{2a}$  (c) $e^{-2a}$  (d) $e^{a}$
> **Ans (a).** $e^a\cdot e^{-a}=1$. *Trick:* the surviving pair multiplies to $1$ (Q112).

**Problem 560.** For $A=\begin{pmatrix}a&0&0\\0&0&a\\0&a&0\end{pmatrix}$, the trace is
(a) $a$  (b) $3a$  (c) $0$  (d) $2a$
> **Ans (a).** $\operatorname{Tr}A=a+0+0=a$. *Trick:* it equals $\sum\lambda_i=a+a-a=a$, so $\det e^A=e^a$ (consistent with Q112).

---

# SET 113 — Expanding a polynomial in the Legendre basis
**Origin (Q113):** $1+5x+3x^2=2P_0+5P_1+2P_2$, so $c_0=2$. **Twists:** $x^2$ in the basis, $c_0$, $c_2$, the coefficient formula, parity.

**Problem 561.** $x^{2}$ in terms of Legendre polynomials is
(a) $\dfrac{2P_2+P_0}{3}$  (b) $P_2$  (c) $\dfrac{P_2+1}{2}$  (d) $2P_2$
> **Ans (a).** Invert $P_2=\tfrac12(3x^2-1)$. *Trick:* $x^2=\tfrac13(2P_2+1)$ (Q113).

**Problem 562.** For $f=1+5x+3x^2=\sum c_n P_n$, the coefficient $c_0$ is
(a) $2$  (b) $1$  (c) $4$  (d) $\dfrac12$
> **Ans (a).** $3x^2$ contributes a $P_0$ (from the $+1$ in $x^2$), plus the explicit $1$. *Trick:* $c_0=1+1=2$ (Q113).

**Problem 563.** For the same $f$, $c_2$ is
(a) $2$  (b) $3$  (c) $1$  (d) $5$
> **Ans (a).** $3\cdot\tfrac23=2$ is the $P_2$ coefficient. *Trick:* from $3x^2=2P_2+P_0$.

**Problem 564.** The Legendre expansion coefficient is
(a) $c_n=\dfrac{2n+1}{2}\displaystyle\int_{-1}^{1}f\,P_n\,dx$  (b) $c_n=\displaystyle\int_{-1}^{1}f\,P_n\,dx$  (c) $c_n=\dfrac{2}{2n+1}\displaystyle\int_{-1}^{1}f\,P_n\,dx$  (d) $c_n=\displaystyle\int_{-1}^{1}f\,dx$
> **Ans (a).** From $\int_{-1}^1 P_n^2\,dx=\tfrac{2}{2n+1}$. *Trick:* the normalization puts $\tfrac{2n+1}{2}$ out front.

**Problem 565.** An **even** function expanded in Legendre polynomials contains
(a) only even‑index $P_n$  (b) only odd‑index $P_n$  (c) all $P_n$  (d) only $P_0$
> **Ans (a).** Parity. *Trick:* $x^2$ (even) uses only $P_0,P_2$ — no $P_1$ (Q113).

---

# SET 114 — Contour integration with multiple poles
**Origin (Q114):** $\oint\dfrac{dz}{z}\dfrac{\tanh 2z}{\sin\pi z}$ over $|z|=\tfrac\pi2$ sums residues at the enclosed poles. **Twists:** the simple‑pole residue, $1/\sin\pi z$, $\tanh$, the residue theorem, counting poles.

**Problem 566.** The residue of $f(z)=\dfrac{g(z)}{h(z)}$ at a simple pole $z_0$ (where $h(z_0)=0$) is
(a) $\dfrac{g(z_0)}{h'(z_0)}$  (b) $\dfrac{g'(z_0)}{h(z_0)}$  (c) $g(z_0)h'(z_0)$  (d) $\dfrac{g(z_0)}{h(z_0)}$
> **Ans (a).** The quotient rule for residues. *Trick:* divide by $h'$ (the derivative) at the pole.

**Problem 567.** The residue of $\dfrac{1}{\sin\pi z}$ at $z=n$ (integer) is
(a) $\dfrac{(-1)^n}{\pi}$  (b) $\dfrac1\pi$  (c) $(-1)^n$  (d) $\pi$
> **Ans (a).** $\dfrac{d}{dz}\sin\pi z=\pi\cos\pi z$ and $\cos\pi n=(-1)^n$. *Trick:* $\dfrac{1}{\pi(-1)^n}=\dfrac{(-1)^n}{\pi}$.

**Problem 568.** $\tanh z$ has simple poles where $\cosh z=0$, with residue
(a) $1$  (b) $-1$  (c) $i$  (d) $0$
> **Ans (a).** $\dfrac{\sinh z}{(\cosh z)'}=\dfrac{\sinh z}{\sinh z}=1$. *Trick:* every pole of $\tanh$ has residue $1$.

**Problem 569.** The residue theorem states $\displaystyle\oint_C f\,dz=$
(a) $2\pi i\sum\text{Res}$  (b) $\pi i\sum\text{Res}$  (c) $\sum\text{Res}$  (d) $2\pi\sum\text{Res}$
> **Ans (a).** Multiply the enclosed residue sum by $2\pi i$. *Trick:* this gives Q114's result.

**Problem 570.** For $\oint$ over $|z|=\tfrac\pi2\approx1.57$, the integer poles of $1/\sin\pi z$ enclosed are
(a) $0,\,1,\,-1$  (b) $0$ only  (c) all integers  (d) $\pm\tfrac\pi2$
> **Ans (a).** Only integers with $|z|<1.57$. *Trick:* $0,\pm1$ lie inside, $\pm2$ don't (Q114).

---

# SET 115 — Path independence of analytic integrals
**Origin (Q115):** $\int_C e^z\,dz$ along a parabola from $(-1,0)$ to $(1,0)$ equals $2\sinh1$ — path‑independent because $e^z$ is entire. **Twists:** Cauchy's theorem, path independence, the antiderivative, the value, when path matters.

**Problem 571.** The integral of an analytic function around a closed contour (enclosing no singularities) is
(a) $0$  (b) $2\pi i$  (c) $\infty$  (d) the residue
> **Ans (a).** Cauchy's integral theorem. *Trick:* analytic ⇒ zero closed‑loop integral.

**Problem 572.** For an analytic $f$, $\int_C f\,dz$ between two points depends on
(a) only the endpoints  (b) the path length  (c) the curvature  (d) the area enclosed
> **Ans (a).** Path independence. *Trick:* analyticity makes only the endpoints matter (Q115).

**Problem 573.** $\displaystyle\int_C e^{z}\,dz$ from $a$ to $b$ equals
(a) $e^{b}-e^{a}$  (b) $e^{b-a}$  (c) $e^{a}-e^{b}$  (d) $e^{ab}$
> **Ans (a).** $e^z$ is its own antiderivative. *Trick:* evaluate at the endpoints (Q115).

**Problem 574.** $\displaystyle\int_C e^{z}\,dz$ from $(-1,0)$ to $(1,0)$ equals
(a) $2\sinh1$  (b) $2\cosh1$  (c) $e+e^{-1}$  (d) $0$
> **Ans (a).** $e^1-e^{-1}=2\sinh1$. *Trick:* the parabolic path is irrelevant (Q115).

**Problem 575.** $\oint\dfrac{dz}{z}$ around a closed loop is path‑**dependent** because
(a) $1/z$ has a singularity at $z=0$  (b) $1/z$ is analytic everywhere  (c) $z$ is real  (d) the contour is closed
> **Ans (a).** The pole at $z=0$ breaks path‑independence. *Trick:* the contrast with the entire $e^z$ of Q115.

---

# SET 116 — Euler–Cauchy (equidimensional) equation
**Origin (Q116):** $x^2y''+5xy'+3y=0$; trying $y=x^m$ gives $m^2+4m+3=0$, so $y=\dfrac Ax+\dfrac B{x^3}$. **Twists:** the form, the substitution, the indicial equation, the roots, the solution.

**Problem 576.** An Euler–Cauchy (equidimensional) ODE has the form
(a) $x^{2}y''+bxy'+cy=0$  (b) $y''+by'+cy=0$  (c) $x^{2}y''+by'+cy=0$  (d) $y''+bxy'+cx^{2}y=0$
> **Ans (a).** Powers of $x$ match the derivative orders. *Trick:* $x^2y'',\ xy',\ y$ — the equidimensional pattern (Q116).

**Problem 577.** To solve an Euler–Cauchy equation, one tries
(a) $y=x^{m}$  (b) $y=e^{mx}$  (c) $y=e^{mx^2}$  (d) $y=mx$
> **Ans (a).** A power‑law trial. *Trick:* $x^m$ (not $e^{mx}$, which is for constant‑coefficient ODEs).

**Problem 578.** For $x^2y''+5xy'+3y=0$, substituting $y=x^m$ gives
(a) $m^{2}+4m+3=0$  (b) $m^{2}+5m+3=0$  (c) $m^{2}+4m+6=0$  (d) $m^{2}-4m+3=0$
> **Ans (a).** $m(m-1)+5m+3=m^2+4m+3$. *Trick:* the $m(m-1)$ comes from $x^2y''$ (Q116).

**Problem 579.** The roots of $m^{2}+4m+3=0$ are
(a) $-1,\,-3$  (b) $1,\,3$  (c) $-1,\,3$  (d) $-2,\,-2$
> **Ans (a).** $(m+1)(m+3)=0$. *Trick:* both negative.

**Problem 580.** The general solution of $x^2y''+5xy'+3y=0$ is
(a) $y=\dfrac Ax+\dfrac B{x^3}$  (b) $y=Ax+\dfrac B{x^3}$  (c) $y=Ax+Bx^{3}$  (d) $y=\dfrac Ax+\dfrac Bx$
> **Ans (a).** $y=Ax^{-1}+Bx^{-3}$. *Trick:* the negative roots give inverse powers (Q116).

---

# SET 117 — Green's‑function construction ($y''=f$)
**Origin (Q117):** for $y''=f$ on $[0,1]$ with $y(0)=y(1)=0$, $G=x(x'-1)$ for $x<x'$ and $x'(x-1)$ for $x'<x$. **Twists:** the homogeneous solutions, left/right pieces, the jump, the full $G$.

**Problem 581.** The two independent solutions of $y''=0$ are
(a) $1$ and $x$  (b) $\sin x$ and $\cos x$  (c) $e^{x}$ and $e^{-x}$  (d) $x$ and $x^{2}$
> **Ans (a).** Constant and linear. *Trick:* $y''=0$ has linear solutions (Q117's building blocks).

**Problem 582.** The solution of $y''=0$ vanishing at $x=0$ is
(a) $x$  (b) $1$  (c) $1-x$  (d) $x^{2}$
> **Ans (a).** $x$ vanishes at $0$. *Trick:* use it on the **left** (Q117).

**Problem 583.** The solution of $y''=0$ vanishing at $x=1$ is
(a) $x-1$  (b) $x$  (c) $1$  (d) $x^{2}$
> **Ans (a).** $(x-1)$ vanishes at $1$. *Trick:* use it on the **right** (Q117).

**Problem 584.** For $G''=\delta(x-x')$, the jump in $G'$ across $x'$ is
(a) $1$  (b) $0$  (c) $-1$  (d) $\infty$
> **Ans (a).** Integrating $\delta$ gives a unit jump. *Trick:* the slope jumps by $1$ (same as the general Green's‑function rule).

**Problem 585.** For $y''=f$ on $[0,1]$ with $y(0)=y(1)=0$, the Green's function is
(a) $x(x'-1)$ for $x<x'$, $x'(x-1)$ for $x'<x$  (b) $x(1-x')$, $x'(1-x)$  (c) $\sin x\sin x'$  (d) constant
> **Ans (a).** Combine the left piece $x$ and right piece $(x-1)$, Wronskian $-1$. *Trick:* this is Q117's answer.

---

# SET 118 — Unitary‑matrix parameter counting
**Origin (Q118):** a $4\times4$ complex $A$ with $A^\dagger A=4I$ makes $A/2$ unitary; $U(4)$ has $4^2=16$ real parameters. **Twists:** the $U(n)$ count, the Q118 count, $SU(n)$, $O(n)$, a general complex matrix.

**Problem 586.** The number of independent real parameters of an $n\times n$ unitary matrix is
(a) $n^{2}$  (b) $2n^{2}$  (c) $n^{2}-1$  (d) $n$
> **Ans (a).** $\dim U(n)=n^2$. *Trick:* this is the count behind Q118.

**Problem 587.** A $4\times4$ complex matrix with $A^\dagger A=4I$ has
(a) $16$  (b) $32$  (c) $10$  (d) $12$
> **Ans (a).** $A/2$ is unitary ($n=4$), so $n^2=16$. *Trick:* Q118.

**Problem 588.** The number of real parameters of an $n\times n$ special‑unitary $SU(n)$ matrix is
(a) $n^{2}-1$  (b) $n^{2}$  (c) $2n^{2}$  (d) $n$
> **Ans (a).** The $\det=1$ constraint removes one. *Trick:* $SU(2)$ has $3$, $SU(3)$ has $8$.

**Problem 589.** The number of real parameters of an $n\times n$ real orthogonal matrix is
(a) $\dfrac{n(n-1)}{2}$  (b) $n^{2}$  (c) $n^{2}-1$  (d) $n$
> **Ans (a).** $\dim O(n)=\tfrac{n(n-1)}{2}$. *Trick:* $SO(3)$ has $3$ — the three rotation angles.

**Problem 590.** A general (unrestricted) $n\times n$ complex matrix has how many real parameters?
(a) $2n^{2}$  (b) $n^{2}$  (c) $n^{2}-1$  (d) $n$
> **Ans (a).** $n^2$ complex entries $\times2$. *Trick:* unitarity (Q118) halves this to $n^2$.

---

# SET 119 — Branch cuts & contour deformation
**Origin (Q119):** $\dfrac{\sqrt{(z-1)(z-3)}}{(z^2-25)^3}$ has branch points at $z=1,3$ (cut between them) and order‑3 poles at $z=\pm5$; a contour around the cut deforms to encircle the poles. **Twists:** branch points, the cut, infinity, deformation, pole order.

**Problem 591.** $\sqrt{(z-1)(z-3)}$ has branch points at
(a) $z=1$ and $z=3$  (b) $z=\pm5$  (c) $z=0$  (d) $z=\infty$
> **Ans (a).** The square root branches where its argument vanishes. *Trick:* at $z=1,3$ (Q119).

**Problem 592.** A branch cut for $\sqrt{(z-1)(z-3)}$ is typically drawn
(a) between $z=1$ and $z=3$  (b) from $0$ to $\infty$  (c) along the imaginary axis  (d) nowhere — there is no cut
> **Ans (a).** Join the two branch points. *Trick:* the cut makes the function single‑valued outside (Q119).

**Problem 593.** For $\sqrt{(z-1)(z-3)}$, the point $z=\infty$ is
(a) not a branch point  (b) a branch point  (c) a pole  (d) an essential singularity
> **Ans (a).** Two finite branch points "pair up." *Trick:* an even number of finite branch points leaves infinity single‑valued (Q119's key fact).

**Problem 594.** A contour wrapping the cut $[1,3]$ can be deformed into contours around
(a) the poles at $z=\pm5$  (b) the origin  (c) infinity  (d) nothing
> **Ans (a).** Deform outward to the only other singularities. *Trick:* the equivalent contours encircle $\pm5$ (Q119).

**Problem 595.** The poles of $\dfrac{\sqrt{(z-1)(z-3)}}{(z^2-25)^3}$ at $z=\pm5$ have order
(a) $3$  (b) $1$  (c) $2$  (d) $6$
> **Ans (a).** $(z^2-25)^3=(z-5)^3(z+5)^3$. *Trick:* the cube gives order‑$3$ poles (Q119).

---

# SET 120 — Trapezoidal rule
**Origin (Q120):** $\int_0^1 x^2\,dx$ by the trapezoidal rule with $h=0.2$ gives $0.34$ (vs the exact $\tfrac13$). **Twists:** the formula, the value, the exact comparison, the over/under‑estimate, vs Simpson.

**Problem 596.** The composite trapezoidal rule is
(a) $\dfrac h2\big[y_0+2(y_1+\cdots+y_{n-1})+y_n\big]$  (b) $\dfrac h3\big[y_0+4y_1+y_2\big]$  (c) $h\big[y_0+y_1+\cdots\big]$  (d) $\dfrac h2\big[y_0+y_n\big]$
> **Ans (a).** Endpoints weight $1$, interior $2$, times $h/2$. *Trick:* the uniform interior weight $2$ (Q120).

**Problem 597.** $\displaystyle\int_0^1 x^2\,dx$ by the trapezoidal rule with $h=0.2$ is
(a) $0.34$  (b) $0.30$  (c) $0.39$  (d) $0.27$
> **Ans (a).** $0.1\big[0+2(0.04+0.16+0.36+0.64)+1\big]=0.1(3.4)=0.34$. *Trick:* Q120.

**Problem 598.** The exact value $\displaystyle\int_0^1 x^2\,dx=$
(a) $\dfrac13$  (b) $\dfrac12$  (c) $0.34$  (d) $\dfrac14$
> **Ans (a).** $\approx0.333$. *Trick:* the trapezoidal $0.34$ slightly overshoots (Q120).

**Problem 599.** For a convex (concave‑up) function, the trapezoidal rule gives
(a) an overestimate  (b) an underestimate  (c) the exact value  (d) zero
> **Ans (a).** Chords lie above the curve. *Trick:* convexity ⇒ overestimate — why $0.34>\tfrac13$ (Q120).

**Problem 600.** Comparing Simpson and trapezoidal at equal step size, Simpson is generally
(a) more accurate  (b) less accurate  (c) equally accurate  (d) always exact
> **Ans (a).** Error $h^4$ vs $h^2$. *Trick:* the parabolic fit captures curvature — Simpson wins.

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: Simpson's rule is exact through cubics (error $\propto f^{(4)}$); $e^A$ exponentiates the eigenvalues, and $\det e^A=e^{\operatorname{Tr}A}$; any polynomial expands in finitely many Legendre $P_n$ (even functions use even $n$ only); simple‑pole residues are $g/h'$, and the residue theorem multiplies by $2\pi i$; an analytic integral is path‑independent ($\int e^z=e^b-e^a$); Euler–Cauchy equations yield to $y=x^m$; the $y''=f$ Green's function is built from $x$ and $x-1$; unitary $U(n)$ has $n^2$ real parameters ($SU(n)$ has $n^2-1$, $O(n)$ has $\tfrac{n(n-1)}2$); a contour around a branch cut deforms onto the enclosed poles; and the trapezoidal rule overestimates convex integrands with $h^2$ error. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 600 problems across all 120 originals (Q1–Q120) — the complete booklet.**

---

## 🎯 Milestone: the full compilation is covered

This Part 12 completes the project. Across **twelve parts** you now have **600 original practice problems** systematically engineered from every one of the **120 CSIR‑NET/JRF previous‑year questions** in the *fiziks* Mathematical Physics booklet (exam papers spanning **June 2011 → Dec 2018**). Each block of five is tuned to expose a *different* trap around one core concept, so the bank covers — across its twelve parts — complex analysis (contour integration, residues, singularities, branch cuts, analyticity, radius of convergence), linear algebra (eigenvalues, Cayley–Hamilton, rank, matrix exponentials, unitary/orthogonal groups), ODEs (constant‑coefficient, Euler–Cauchy, nonlinear substitutions, Green's functions, Frobenius, BVPs), integral transforms (Laplace, Fourier, deltas), special functions (Legendre, Hermite, Bessel, hypergeometric), vector calculus, probability (Poisson, Gaussian, random walks, transformations), group theory (SU(2), Pauli, Levi‑Civita), numerical methods (Newton–Raphson, Simpson, trapezoidal, Euler, interpolation, fixed points), and dimensional analysis.
