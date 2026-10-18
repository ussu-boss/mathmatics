# 50 Practice Problems — Part 11 (CSIR‑NET/JRF style)

**Built from problems 101–110 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **501–550** to continue Parts 1–10.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q101–Q102 = Dec 2017**, **Q103–Q110 = June 2018** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q101–Q110)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q101 | Numerical methods | Trapezoidal rule; exactness for periodic functions |
| Q102 | Special functions | Legendre generating function ($G(1,x)$, products) |
| Q103 | ODEs | Nonlinear ODE solved by substitution |
| Q104 | Complex analysis | Cauchy–Riemann / analyticity |
| Q105 | Linear algebra | Linear dependence of vectors ($\det=0$) |
| Q106 | Integral transforms | Fourier transform of $e^{-|x|}$ |
| Q107 | Math methods | Delta‑function composition $\delta(g(x))$ |
| Q108 | Linear algebra | Orthogonal/rotation matrices & eigenvalues |
| Q109 | Calculus | Counting extrema of $P_n(x)e^{-x^2}$ |
| Q110 | Math methods | Green's‑function construction (oscillatory) |

---

# SET 101 — Trapezoidal rule; exactness for periodic functions
**Origin (Q101):** $\int_0^1 e^{i2\pi x}dx=0$, and the trapezoidal rule reproduces this exactly with just $n=2$. **Twists:** what it's exact for, the integral, the error order, periodic accuracy, the minimum $n$.

**Problem 501.** The trapezoidal rule is exact for
(a) linear functions  (b) quadratics  (c) cubics  (d) only constants
> **Ans (a).** It joins points by straight segments. *Trick:* exact for straight lines, approximate otherwise.

**Problem 502.** $\displaystyle\int_0^1 e^{i2\pi x}\,dx=$
(a) $0$  (b) $1$  (c) $2\pi$  (d) $i$
> **Ans (a).** A full period of a complex exponential integrates to zero. *Trick:* this is Q101's exact value.

**Problem 503.** The composite trapezoidal rule has an error proportional to
(a) $h^{2}$  (b) $h$  (c) $h^{4}$  (d) $h^{3}$
> **Ans (a).** Second‑order. *Trick:* one order better than Euler's $h$.

**Problem 504.** The trapezoidal rule is unusually accurate (often exact) for
(a) smooth periodic functions over a full period  (b) discontinuous functions  (c) polynomials only  (d) linear functions only
> **Ans (a).** The endpoint errors cancel for periodic integrands. *Trick:* this is why Q101 needs only $n=2$.

**Problem 505.** For $\int_0^1 e^{i2\pi x}dx$ by the trapezoidal rule, the smallest $n$ giving the exact value is
(a) $2$  (b) $3$  (c) $4$  (d) $\infty$
> **Ans (a).** $\tfrac14[1+2(-1)+1]=0$. *Trick:* the $n=2$ samples already cancel exactly (Q101).

---

# SET 102 — Legendre generating function
**Origin (Q102):** $G(t,x)=\dfrac{1}{\sqrt{1-2xt+x^2}}$; $G(1,x)=\dfrac{1}{1-x}$, and $\int_0^x f\,dx'=xG(1,x)$ gives $f=\dfrac{1}{(1-x)^2}=\sum x^{n+m}P_n(1)P_m(1)$. **Twists:** the generating function, $G(1,x)$, $\sum P_n(1)x^n$, the product, the Q102 function.

**Problem 506.** The Legendre generating function is
(a) $\dfrac{1}{\sqrt{1-2xt+x^2}}$  (b) $e^{xt}$  (c) $\dfrac{1}{1-xt}$  (d) $\dfrac{1}{\sqrt{1+x^2}}$
> **Ans (a).** The $\sqrt{1-2xt+x^2}$ form. *Trick:* memorize this — it generates all the $P_n$ (Q102).

**Problem 507.** $G(1,x)=\dfrac{1}{\sqrt{1-2x+x^2}}=$
(a) $\dfrac{1}{1-x}$  (b) $\dfrac{1}{1+x}$  (c) $\dfrac{1}{\sqrt{1-x}}$  (d) $1-x$
> **Ans (a).** $1-2x+x^2=(1-x)^2$. *Trick:* the radicand is a perfect square (Q102).

**Problem 508.** $\displaystyle\sum_{n=0}^\infty P_n(1)\,x^n=$
(a) $\dfrac{1}{1-x}$  (b) $\dfrac{1}{1+x}$  (c) $e^{x}$  (d) $1$
> **Ans (a).** $P_n(1)=1$, so it's the geometric series. *Trick:* the special value $P_n(1)=1$ collapses the sum.

**Problem 509.** $\Big(\displaystyle\sum_n x^n P_n(1)\Big)\Big(\sum_m x^m P_m(1)\Big)=$
(a) $\dfrac{1}{(1-x)^2}$  (b) $\dfrac{1}{1-x}$  (c) $\dfrac{1}{1-x^2}$  (d) $\dfrac{1}{1-2x}$
> **Ans (a).** Squaring $\dfrac{1}{1-x}$. *Trick:* this double sum is the form in Q102's answer.

**Problem 510.** With $\int_0^x f(x')dx'=\dfrac{x}{1-x}$, the function $f(x)=$
(a) $\dfrac{1}{(1-x)^2}$  (b) $\dfrac{1}{1-x}$  (c) $\dfrac1x$  (d) $\ln(1-x)$
> **Ans (a).** $\dfrac{d}{dx}\dfrac{x}{1-x}=\dfrac{1}{(1-x)^2}$. *Trick:* differentiate to recover $f$ (Q102).

---

# SET 103 — Nonlinear ODE solved by substitution
**Origin (Q103):** $\ddot x+\tfrac1x\dot x^2-\dot x=0$ with $x(0)=0,x(1)=1$; the substitution $y=x\dot x$ linearizes it, giving $x(2)=\sqrt{e+1}$. **Twists:** the exact‑derivative trick, the substitution, the reduced equation, recovering $x$, the answer.

**Problem 511.** The combination $x\ddot x+\dot x^2$ equals
(a) $\dfrac{d}{dt}(x\dot x)$  (b) $\dfrac{d}{dt}(x^2)$  (c) $(x\dot x)^2$  (d) $x^2\ddot x$
> **Ans (a).** It's the derivative of a product. *Trick:* spotting $x\ddot x+\dot x^2=(x\dot x)'$ unlocks Q103.

**Problem 512.** Multiplying $\ddot x+\tfrac1x\dot x^2-\dot x=0$ by $x$ and setting $y=x\dot x$ gives
(a) $\dot y-y=0$  (b) $\dot y+y=0$  (c) $\ddot y=0$  (d) $\dot y=y^2$
> **Ans (a).** $x\ddot x+\dot x^2=\dot y$ and $x\dot x=y$. *Trick:* the substitution turns it linear (Q103).

**Problem 513.** The solution of $\dot y-y=0$ is
(a) $c_1 e^{t}$  (b) $c_1 e^{-t}$  (c) $c_1 t$  (d) $c_1\cos t$
> **Ans (a).** The simplest first‑order linear ODE. *Trick:* exponential growth $e^t$.

**Problem 514.** From $x\dot x=c_1 e^{t}$, integrating gives
(a) $\dfrac{x^2}{2}=c_1 e^{t}+c_2$  (b) $x=c_1 e^{t}$  (c) $x^2=c_1 t$  (d) $\ln x=c_1 e^{t}$
> **Ans (a).** $x\dot x=\big(\tfrac{x^2}{2}\big)'$. *Trick:* integrate the perfect derivative (Q103).

**Problem 515.** For $\ddot x+\tfrac1x\dot x^2-\dot x=0$ with $x(0)=0,x(1)=1$, the value $x(2)=$
(a) $\sqrt{e+1}$  (b) $\sqrt{e^2+1}$  (c) $\sqrt{e-1}$  (d) $\sqrt{e^2-1}$
> **Ans (a).** $x^2(2)=\dfrac{e^2-1}{e-1}=e+1$. *Trick:* the constants cancel into $e+1$ (Q103).

---

# SET 104 — Cauchy–Riemann / analyticity
**Origin (Q104):** $f=2x+3(x^2-y^2)+2i(3xy+ay)$ is analytic iff $a=1$ (from Cauchy–Riemann). **Twists:** the CR equations, $u_x$, the condition, analytic⇒harmonic, the $\bar z$ counterexample.

**Problem 516.** For $f=u+iv$ to be analytic, the Cauchy–Riemann equations are
(a) $u_x=v_y,\ u_y=-v_x$  (b) $u_x=v_x,\ u_y=v_y$  (c) $u_x=-v_y,\ u_y=v_x$  (d) $u_x=u_y,\ v_x=v_y$
> **Ans (a).** The cross‑pairing with one minus sign. *Trick:* $u_x=v_y$ **and** $u_y=-v_x$.

**Problem 517.** For $u=2x+3(x^2-y^2)$, $u_x=$
(a) $2+6x$  (b) $6x$  (c) $2-6y$  (d) $2x$
> **Ans (a).** $\partial_x[2x+3x^2-3y^2]=2+6x$. *Trick:* the $y^2$ term drops out under $\partial_x$.

**Problem 518.** For $f=2x+3(x^2-y^2)+2i(3xy+ay)$, analyticity requires $a=$
(a) $1$  (b) $0$  (c) $3$  (d) $2$
> **Ans (a).** $u_x=v_y$: $2+6x=6x+2a\Rightarrow a=1$. *Trick:* match $u_x=v_y$ (Q104).

**Problem 519.** If $f=u+iv$ is analytic, then $u$ and $v$ are both
(a) harmonic  (b) constant  (c) linear  (d) zero
> **Ans (a).** Real/imaginary parts satisfy Laplace's equation. *Trick:* analytic ⇒ harmonic conjugates.

**Problem 520.** The function $f(z)=\bar z=x-iy$ is
(a) nowhere analytic  (b) analytic everywhere  (c) analytic at $z=0$ only  (d) analytic for $x>0$
> **Ans (a).** $u_x=1$ but $v_y=-1$, so CR fails everywhere. *Trick:* $\bar z$ is the classic non‑analytic example.

---

# SET 105 — Linear dependence of vectors
**Origin (Q105):** three vectors are linearly dependent iff the determinant of their matrix vanishes; here $a=\tfrac{31}{4}$. **Twists:** the criterion, the geometry, the scalar triple product, the Q105 value, independence.

**Problem 521.** Three vectors in 3‑D are linearly dependent iff
(a) the determinant of the matrix formed from them is zero  (b) the determinant is nonzero  (c) they are orthogonal  (d) they are unit vectors
> **Ans (a).** Zero determinant ⇔ dependence. *Trick:* this is the test used in Q105.

**Problem 522.** Three linearly dependent vectors in 3‑D
(a) are coplanar  (b) are orthogonal  (c) span all of 3‑D  (d) are equal
> **Ans (a).** They span at most $2$ dimensions. *Trick:* dependence means coplanar (zero enclosed volume).

**Problem 523.** The determinant of three column vectors equals their
(a) scalar triple product $\vec a\!\cdot\!(\vec b\times\vec c)$  (b) $\vec a\!\cdot\!\vec b\,\vec c$  (c) $\vec a\times\vec b\times\vec c$  (d) $|\vec a||\vec b||\vec c|$
> **Ans (a).** The signed volume of the parallelepiped. *Trick:* $\det=$ scalar triple product.

**Problem 524.** For $\vec v_1=(2,0,3),\ \vec v_2=(1,2,2),\ \vec v_3=(5,1,a)$ (as columns), dependence requires $a=$
(a) $\dfrac{31}{4}$  (b) $\dfrac{23}{4}$  (c) $\dfrac{27}{4}$  (d) $0$
> **Ans (a).** Expanding $\det=0$ gives $4a-31=0$. *Trick:* this is Q105.

**Problem 525.** Three linearly **independent** vectors in 3‑D
(a) form a basis  (b) are coplanar  (c) must be orthonormal  (d) have zero determinant
> **Ans (a).** $n$ independent vectors in $n$‑D span the space. *Trick:* independence ⇒ basis (nonzero determinant).

---

# SET 106 — Fourier transform of $e^{-|x|}$
**Origin (Q106):** $\int e^{-|x|}e^{ikx}dx=\dfrac{2}{1+k^2}$. **Twists:** the transform, the cosine reduction, general decay, the dual, the $k=0$ value.

**Problem 526.** $\displaystyle\int_{-\infty}^\infty e^{-|x|}e^{ikx}\,dx=$
(a) $\dfrac{2}{1+k^2}$  (b) $\dfrac{1}{1+k^2}$  (c) $\dfrac{2}{2+k^2}$  (d) $-\dfrac{2}{1+k^2}$
> **Ans (a).** A two‑sided exponential gives a Lorentzian with numerator $2$. *Trick:* this is Q106.

**Problem 527.** Since $e^{-|x|}$ is even, its FT reduces to
(a) $2\displaystyle\int_0^\infty e^{-x}\cos kx\,dx$  (b) $2\displaystyle\int_0^\infty e^{-x}\sin kx\,dx$  (c) $\displaystyle\int e^{-x}dx$  (d) $0$
> **Ans (a).** The odd $\sin$ part cancels. *Trick:* even functions need only the cosine integral (Q106's method).

**Problem 528.** $\displaystyle\int_{-\infty}^\infty e^{-a|x|}e^{ikx}\,dx=$
(a) $\dfrac{2a}{k^2+a^2}$  (b) $\dfrac{2}{k^2+a^2}$  (c) $\dfrac{a}{k^2+a^2}$  (d) $e^{-a|k|}$
> **Ans (a).** General decay rate $a$. *Trick:* Q106 is the $a=1$ case of $\dfrac{2a}{k^2+a^2}$.

**Problem 529.** $\displaystyle\int_{-\infty}^\infty\frac{e^{ikx}}{x^{2}+1}\,dx=$
(a) $\pi e^{-|k|}$  (b) $\dfrac{2}{1+k^2}$  (c) $e^{-|k|}$  (d) $\dfrac{\pi}{1+k^2}$
> **Ans (a).** The dual pair. *Trick:* Lorentzian $\leftrightarrow$ exponential (the reverse of Q106).

**Problem 530.** The FT of $e^{-|x|}$ at $k=0$ equals
(a) $2$  (b) $1$  (c) $0$  (d) $\pi$
> **Ans (a).** $\displaystyle\int_{-\infty}^\infty e^{-|x|}dx=2$. *Trick:* the $k=0$ value is the area.

---

# SET 107 — Delta‑function composition $\delta(g(x))$
**Origin (Q107):** $\int_{-\pi/2}^{\pi/2}\!\int_{-1}^{1}\delta(\sin2x)\delta(x-y)\,dy\,dx=\tfrac12$, using $\delta(g(x))=\sum\delta(x-x_n)/|g'(x_n)|$. **Twists:** the composition rule, $\delta(ax)$, $\delta(\sin2x)$ near $0$, $\delta(x^2-a^2)$, the Q107 integral.

**Problem 531.** For $g$ with simple zeros $x_n$, $\delta(g(x))=$
(a) $\displaystyle\sum_n\frac{\delta(x-x_n)}{|g'(x_n)|}$  (b) $\delta(x-x_n)$  (c) $\displaystyle\sum_n\delta(x-x_n)\,|g'(x_n)|$  (d) $\dfrac{1}{g(x)}$
> **Ans (a).** Divide by $|g'|$ at each root. *Trick:* the composition rule behind Q107.

**Problem 532.** $\delta(ax)=$
(a) $\dfrac{\delta(x)}{|a|}$  (b) $\delta(x)$  (c) $a\,\delta(x)$  (d) $\dfrac{\delta(x)}{a^2}$
> **Ans (a).** The simplest scaling. *Trick:* $\delta(ax)=\delta(x)/|a|$.

**Problem 533.** Near $x=0$, $\sin2x\approx2x$, so $\delta(\sin 2x)\approx$
(a) $\dfrac{\delta(x)}{2}$  (b) $\delta(x)$  (c) $2\delta(x)$  (d) $\delta(2x)$
> **Ans (a).** $|{\tfrac{d}{dx}\sin2x}|_0=2$. *Trick:* the factor $\tfrac12$ comes from $g'=2\cos2x$ at $0$ (Q107).

**Problem 534.** $\delta(x^{2}-a^{2})=$
(a) $\dfrac{\delta(x-a)+\delta(x+a)}{2|a|}$  (b) $\delta(x-a)+\delta(x+a)$  (c) $\dfrac{\delta(x-a)}{2a}$  (d) $\dfrac{\delta(x^2)}{a}$
> **Ans (a).** Two roots $\pm a$, each with $|g'|=2|a|$. *Trick:* sum both roots, divide by $2|a|$.

**Problem 535.** $\displaystyle\int_{-\pi/2}^{\pi/2}\!\!\int_{-1}^{1}\delta(\sin2x)\,\delta(x-y)\,dy\,dx=$
(a) $\dfrac12$  (b) $1$  (c) $0$  (d) $\dfrac{1}{\sqrt2}$
> **Ans (a).** The inner integral is $1$ (since $0\in[-1,1]$); then $\delta(\sin2x)$ gives $\tfrac12$ at $x=0$. *Trick:* this is Q107.

---

# SET 108 — Orthogonal/rotation matrices & eigenvalues
**Origin (Q108):** a $3\times3$ real orthogonal matrix with $\det=+1$ (a rotation) has at least one eigenvalue $+1$ (the rotation axis). **Twists:** eigenvalue modulus, the axis, the determinant, the trace, reflections.

**Problem 536.** The eigenvalues of an orthogonal matrix all have modulus
(a) $1$  (b) $0$  (c) any value  (d) $>1$
> **Ans (a).** Orthogonal matrices preserve length. *Trick:* $|\lambda|=1$ — they sit on the unit circle.

**Problem 537.** For a $3$‑D rotation matrix, the eigenvalue $+1$ corresponds to
(a) the rotation axis  (b) the angle of rotation  (c) a reflection  (d) the trace
> **Ans (a).** The $+1$ eigenvector stays fixed. *Trick:* every $3$‑D rotation has an axis — the $+1$ eigenvalue (Q108).

**Problem 538.** The determinant of a proper rotation (no reflection) is
(a) $+1$  (b) $-1$  (c) $0$  (d) any
> **Ans (a).** Proper rotation ⇒ $\det=+1$. *Trick:* $\det=-1$ would include a reflection (Q108's condition).

**Problem 539.** The trace of a $3\times3$ rotation by angle $\theta$ is
(a) $1+2\cos\theta$  (b) $3\cos\theta$  (c) $2\cos\theta$  (d) $\cos\theta$
> **Ans (a).** $\operatorname{Tr}=1+e^{i\theta}+e^{-i\theta}$. *Trick:* the eigenvalue sum $1+2\cos\theta$.

**Problem 540.** A $3\times3$ reflection matrix has determinant
(a) $-1$  (b) $+1$  (c) $0$  (d) $2$
> **Ans (a).** Improper orthogonal. *Trick:* $\det=-1$ marks a reflection (vs $+1$ for a rotation).

---

# SET 109 — Counting extrema of $P_n(x)e^{-x^2}$
**Origin (Q109):** $P_n(x)e^{-x^2}$ has at most $n+1$ extrema, because its derivative bracket $P_n'-2xP_n$ has degree $n+1$. **Twists:** extrema from the derivative, the derivative itself, the bracket's degree, the maximum, why $e^{-x^2}$ adds none.

**Problem 541.** The extrema of $f(x)$ occur where
(a) $f'(x)=0$  (b) $f(x)=0$  (c) $f''(x)=0$  (d) $f(x)=1$
> **Ans (a).** Set the first derivative to zero. *Trick:* the method of Q109.

**Problem 542.** $\dfrac{d}{dx}\big[P_n(x)e^{-x^2}\big]=$
(a) $\big[P_n'(x)-2xP_n(x)\big]e^{-x^2}$  (b) $P_n'(x)e^{-x^2}$  (c) $-2xP_n(x)e^{-x^2}$  (d) $\big[P_n'(x)+2xP_n(x)\big]e^{-x^2}$
> **Ans (a).** Product rule; $e^{-x^2}$ brings down $-2x$. *Trick:* the bracket is what matters (Q109).

**Problem 543.** The polynomial $P_n'(x)-2xP_n(x)$ has degree
(a) $n+1$  (b) $n$  (c) $n-1$  (d) $2n$
> **Ans (a).** $2x\cdot(\text{degree }n)=$ degree $n+1$. *Trick:* the $2xP_n$ term dominates $P_n'$ (degree $n-1$).

**Problem 544.** The maximum number of extrema of $P_n(x)e^{-x^2}$ is
(a) $n+1$  (b) $n$  (c) $n-1$  (d) $n+2$
> **Ans (a).** A degree‑$(n+1)$ polynomial has at most $n+1$ real roots. *Trick:* this is Q109's answer.

**Problem 545.** In counting extrema, the factor $e^{-x^2}$
(a) never vanishes, so adds no extrema  (b) adds $2$ extrema  (c) makes the function zero  (d) doubles the roots
> **Ans (a).** $e^{-x^2}>0$ always. *Trick:* it can't create roots of the derivative — only the polynomial bracket can (Q109).

---

# SET 110 — Green's‑function construction (oscillatory)
**Origin (Q110):** for $y''+y=f$ with $y(0)=y(\pi/2)=0$, the Green's function uses $\sin x$ (satisfies the left BC) and $\cos x$ (satisfies the right BC). **Twists:** the homogeneous solutions, matching each BC, the structure, the Wronskian.

**Problem 546.** For $y''+y=0$, the two independent solutions are
(a) $\sin x$ and $\cos x$  (b) $e^{x}$ and $e^{-x}$  (c) $x$ and $1$  (d) $e^{x}$ and $xe^{x}$
> **Ans (a).** The SHO equation. *Trick:* trigonometric solutions (Q110).

**Problem 547.** The homogeneous solution satisfying $y(0)=0$ is
(a) $\sin x$  (b) $\cos x$  (c) $e^{x}$  (d) $1$
> **Ans (a).** $\sin0=0$. *Trick:* use $\sin x$ on the **left** (Q110).

**Problem 548.** The homogeneous solution satisfying $y(\pi/2)=0$ is
(a) $\cos x$  (b) $\sin x$  (c) $e^{x}$  (d) $x$
> **Ans (a).** $\cos(\pi/2)=0$. *Trick:* use $\cos x$ on the **right** (Q110).

**Problem 549.** The $1$‑D Green's function takes the form
(a) $\dfrac{y_1(x_<)\,y_2(x_>)}{W}$  (b) $y_1(x)\,y_2(x)$  (c) $y_1(x)+y_2(x)$  (d) $\delta(x-x')$
> **Ans (a).** Use the left‑BC solution for $x<x'$ and the right‑BC one for $x>x'$, divided by the Wronskian. *Trick:* the standard construction (Q110).

**Problem 550.** The Wronskian of $\sin x$ and $\cos x$ is
(a) $-1$  (b) $+1$  (c) $0$  (d) $\sin 2x$
> **Ans (a).** $\sin x(-\sin x)-\cos x\cos x=-1$. *Trick:* a constant Wronskian $-1$ normalizes the Green's function (Q110).

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: the trapezoidal rule is exact for lines and for smooth periodic functions over a period; $G(1,x)=\tfrac{1}{1-x}$ turns the Legendre generating function into a geometric series; a nonlinear ODE can collapse via the substitution $y=x\dot x$; Cauchy–Riemann ($u_x=v_y,\ u_y=-v_x$) pins down analyticity; vectors are dependent iff their determinant (scalar triple product) vanishes; $\mathcal F[e^{-|x|}]=\tfrac{2}{1+k^2}$ (and the dual Lorentzian $\to$ exponential); $\delta(g(x))$ divides by $|g'|$ at each root; a $3$‑D rotation always has a $+1$ eigenvalue (its axis) and trace $1+2\cos\theta$; $P_n(x)e^{-x^2}$ has at most $n+1$ extrema (the Gaussian adds none); and an oscillatory Green's function is built from the two homogeneous solutions matching each boundary, normalized by the Wronskian. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 550 problems across the first 110 originals (Q1–Q110).**
