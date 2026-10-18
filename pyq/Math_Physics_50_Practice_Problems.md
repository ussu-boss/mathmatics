# 50 Practice Problems — Mathematical Physics (CSIR‑NET/JRF style)

**Built from the first 10 problems of the *fiziks* "Mathematical Physics Solutions — NET/JRF (June‑2011 / Dec‑2011)" booklet.**
For each original problem I extracted the *core concept* and then wrote **5 new problems** that each twist a **different** subtlety of that concept, so the whole trap‑space gets explored. Every problem is multiple‑choice (CSIR style), with the answer and a one‑line **"why / what's the trick"** underneath.

> **Source of the original 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q1–Q6 = June 2011**, **Q7–Q10 = Dec 2011**. The PDF is *fiziks*' worked‑solution compilation (physicsbyfiziks.com). For textbook study of these topics: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (what each original problem tested)

| Q | Topic | Core idea being tested |
|---|-------|------------------------|
| Q1 | Complex contour integration | Cauchy's theorem; closing an open contour; antiderivative of an entire function |
| Q2 | Group $SU(2)$ | The form $\begin{pmatrix}\alpha&-\beta\\\bar\beta&\bar\alpha\end{pmatrix},\ |\alpha|^2+|\beta|^2=1$ |
| Q3 | Vector triple product | Perpendicular component of $\vec b$ to $\vec a$; BAC–CAB rule |
| Q4 | Orthonormal polynomials | Gram–Schmidt + normalization on a finite interval |
| Q5 | Analyticity | Dependence on $z$ vs $\bar z$; Cauchy–Riemann; branch points |
| Q6 | Eigenvalues & $e^{M}$ | All‑ones matrix spectrum; matrix exponential via diagonalization |
| Q7 | Probability (dice) | Counting favourable microstates / total $6^3$ |
| Q8 | Legendre polynomials | Generating function; $P_n(\pm1),P_n(0)$; recurrence |
| Q9 | Tangent plane | $\nabla F$ as the surface normal |
| Q10 | Traces & eigenvalues | Power sums $\operatorname{Tr}(M^k)=\sum\lambda_i^k$ |

---

# SET 1 — Complex contour integration
**Origin (Q1):** $\displaystyle\int_C z^2e^{z}\,dz$ on an open contour; close it, note $z^2e^z$ is *entire*, use $\oint=0$. **Twists below:** path‑independence, simple pole, higher‑order pole, essential singularity, cancelling residues.

**Problem 1.** $C$ is *any* path from $z=0$ to $z=i\pi$. Then $\displaystyle\int_C z\,e^{z}\,dz=$
(a) $2-i\pi$  (b) $i\pi-2$  (c) $2+i\pi$  (d) $-i\pi$
> **Ans (a).** $ze^z$ is entire ⇒ path‑independent; antiderivative $e^z(z-1)$, so $e^{i\pi}(i\pi-1)-e^0(0-1)=2-i\pi$. *Trick:* don't hunt for residues — there are none.

**Problem 2.** $\displaystyle\oint_{|z|=2}\frac{z}{(z-1)(z-3)}\,dz=$
(a) $-\pi i$  (b) $\pi i$  (c) $2\pi i$  (d) $0$
> **Ans (a).** Only $z=1$ lies inside $|z|=2$; $\operatorname{Res}_{z=1}=\frac{1}{1-3}=-\tfrac12$, so $2\pi i(-\tfrac12)=-\pi i$. *Trick:* the pole at $z=3$ is outside and contributes nothing.

**Problem 3.** $\displaystyle\oint_{|z|=1}\frac{e^{z}}{z^{2}}\,dz=$
(a) $2\pi i$  (b) $\pi i$  (c) $0$  (d) $2\pi i\,e$
> **Ans (a).** Pole of **order 2**: $\operatorname{Res}=\frac{d}{dz}e^{z}\big|_{0}=1$, so $2\pi i$. *Trick:* a double pole needs a derivative, not just $f(0)$.

**Problem 4.** $\displaystyle\oint_{|z|=1}e^{1/z}\,dz=$
(a) $2\pi i$  (b) $0$  (c) $\pi i$  (d) $2\pi i\,e$
> **Ans (a).** **Essential** singularity; expand $e^{1/z}=\sum_n \frac{1}{n!}z^{-n}$, coefficient of $z^{-1}$ is $1$, so $\operatorname{Res}=1$. *Trick:* no pole‑order formula applies — read the residue off the Laurent series.

**Problem 5.** $\displaystyle\oint_{|z|=2}\frac{dz}{z^{2}+1}=$
(a) $0$  (b) $2\pi i$  (c) $\pi$  (d) $2\pi$
> **Ans (a).** Both poles $\pm i$ are inside; $\operatorname{Res}_{i}=\frac{1}{2i}$, $\operatorname{Res}_{-i}=-\frac{1}{2i}$, sum $=0$. *Trick:* enclosing a conjugate pair makes the residues cancel.

---

# SET 2 — The group $SU(2)$
**Origin (Q2):** recognize $U=\begin{pmatrix}\alpha&-\beta\\\bar\beta&\bar\alpha\end{pmatrix}$ with $|\alpha|^2+|\beta|^2=1$. **Twists:** the same form with complex entries, $\det=1$ vs unitary, exponential of a generator, the trace bound, the inverse.

**Problem 6.** Which matrix is an element of $SU(2)$?
(a) $\dfrac{1}{\sqrt2}\begin{pmatrix}1&i\\ i&1\end{pmatrix}$  (b) $\begin{pmatrix}1&1\\0&1\end{pmatrix}$  (c) $\begin{pmatrix}1&0\\0&2\end{pmatrix}$  (d) $\begin{pmatrix}0&1\\1&0\end{pmatrix}$
> **Ans (a).** Here $\alpha=\tfrac1{\sqrt2},\ \beta=-\tfrac{i}{\sqrt2}$; $|\alpha|^2+|\beta|^2=1$, $\det=1$, unitary. (b) not unitary; (c) $\det=2$; (d) $\det=-1$. *Trick:* the off‑diagonal pattern must be $-\beta$ above, $\bar\beta$ below.

**Problem 7.** For which $\theta\in[0,2\pi)$ is $e^{i\theta}\mathbb{1}_2\in SU(2)$?
(a) $\theta=0$ only  (b) $\theta=0,\ \pi$  (c) all $\theta$  (d) $\theta=\pi/2$
> **Ans (b).** $\det(e^{i\theta}\mathbb1_2)=e^{2i\theta}=1\Rightarrow\theta=0,\pi$; at $\theta=\pi$ this is $-\mathbb1\in SU(2)$. *Trick:* unitary ($\in U(2)$) is not enough — you need $\det=1$.

**Problem 8.** $\exp\!\big(i\theta\,\sigma_z/2\big)=$  (with $\sigma_z=\mathrm{diag}(1,-1)$)
(a) $\begin{pmatrix}e^{i\theta/2}&0\\0&e^{-i\theta/2}\end{pmatrix}$  (b) $\begin{pmatrix}\cos\theta&i\sin\theta\\ i\sin\theta&\cos\theta\end{pmatrix}$  (c) $\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}$  (d) $\begin{pmatrix}\cos\frac\theta2&-\sin\frac\theta2\\ \sin\frac\theta2&\cos\frac\theta2\end{pmatrix}$
> **Ans (a).** $\sigma_z$ is diagonal, so exponentiate the entries. *Trick:* the rotation angle is **$\theta/2$**, not $\theta$ — the famous spin‑½ half‑angle.

**Problem 9.** Which value **cannot** be the trace of an $SU(2)$ matrix?
(a) $2$  (b) $0$  (c) $-2$  (d) $3$
> **Ans (d).** Eigenvalues are $e^{\pm i\theta}$, so $\operatorname{Tr}=2\cos\theta\in[-2,2]$ and is real. *Trick:* $|\operatorname{Tr}|\le2$ always — anything bigger is impossible.

**Problem 10.** The inverse of $U=\begin{pmatrix}\alpha&-\beta\\\bar\beta&\bar\alpha\end{pmatrix}\in SU(2)$ is
(a) $\begin{pmatrix}\bar\alpha&\beta\\-\bar\beta&\alpha\end{pmatrix}$  (b) $\begin{pmatrix}\alpha&\beta\\-\bar\beta&\bar\alpha\end{pmatrix}$  (c) $\begin{pmatrix}\bar\alpha&-\beta\\\bar\beta&\alpha\end{pmatrix}$  (d) $U$ itself
> **Ans (a).** For $SU(2)$, $U^{-1}=U^{\dagger}$ (conjugate transpose). *Trick:* conjugate **and** transpose — keep the signs straight.

---

# SET 3 — Vector triple product & projections
**Origin (Q3):** component of $\vec b\perp\vec a$ is $\dfrac{\vec a\times(\vec b\times\vec a)}{a^{2}}$. **Twists:** the *parallel* component, the BAC–CAB identity itself, the *magnitude*, coplanarity, reflection.

**Problem 11.** The component of $\vec b$ **parallel** to $\vec a$ is
(a) $\dfrac{(\vec a\cdot\vec b)\,\vec a}{a^{2}}$  (b) $\dfrac{(\vec a\cdot\vec b)\,\vec b}{b^{2}}$  (c) $\dfrac{\vec a\times(\vec b\times\vec a)}{a^{2}}$  (d) $(\vec a\cdot\vec b)\,\vec a$
> **Ans (a).** Standard projection $(\hat a\cdot\vec b)\hat a$. *Trick:* (c) is the *perpendicular* part from Q3 — easy to grab the wrong one.

**Problem 12.** $\vec a\times(\vec b\times\vec c)=$
(a) $\vec b(\vec a\cdot\vec c)-\vec c(\vec a\cdot\vec b)$  (b) $\vec c(\vec a\cdot\vec b)-\vec b(\vec a\cdot\vec c)$  (c) $(\vec a\cdot\vec b)\vec c-(\vec b\cdot\vec c)\vec a$  (d) $(\vec a\times\vec b)\times\vec c$
> **Ans (a).** "BAC–CAB": $\vec b(\vec a\!\cdot\!\vec c)-\vec c(\vec a\!\cdot\!\vec b)$. *Trick:* the cross product is **not associative**, so (d) is a *different* vector.

**Problem 13.** The magnitude of the component of $\vec b$ perpendicular to $\vec a$ equals
(a) $\dfrac{|\vec a\times\vec b|}{|\vec a|}$  (b) $\dfrac{|\vec a\cdot\vec b|}{|\vec a|}$  (c) $|\vec a\times\vec b|$  (d) $\dfrac{|\vec a\times\vec b|}{|\vec a||\vec b|}$
> **Ans (a).** $|\vec b_\perp|=|\vec b|\sin\theta=\dfrac{|\vec a\times\vec b|}{|\vec a|}$. *Trick:* divide by $|\vec a|$ only (option d over‑divides; it gives $\sin\theta$).

**Problem 14.** Three vectors $\vec a,\vec b,\vec c$ are coplanar **iff**
(a) $\vec a\cdot(\vec b\times\vec c)=0$  (b) $\vec a\times(\vec b\times\vec c)=0$  (c) $\vec a\cdot(\vec b\cdot\vec c)=0$  (d) $(\vec a\times\vec b)\cdot\vec c\ne0$
> **Ans (a).** The scalar triple product is the parallelepiped volume; zero ⇒ coplanar. *Trick:* (c) is meaningless — $\vec b\cdot\vec c$ is a scalar, you can't dot $\vec a$ into it.

**Problem 15.** The reflection of vector $\vec v$ across a plane with unit normal $\hat n$ is
(a) $\vec v-2(\vec v\cdot\hat n)\hat n$  (b) $\vec v-(\vec v\cdot\hat n)\hat n$  (c) $2(\vec v\cdot\hat n)\hat n-\vec v$  (d) $(\vec v\cdot\hat n)\hat n$
> **Ans (a).** Flip the normal component: subtract it **twice**. *Trick:* (b) is the *projection onto the plane* (only one subtraction); (c) reflects through the normal line instead.

---

# SET 4 — Orthonormal polynomials (Gram–Schmidt)
**Origin (Q4):** orthonormal $p_n$ on $[2,4]$ with $\int_2^4 p_np_m\,dx=\delta_{nm}$; $p_0=\tfrac1{\sqrt2}$, $p_1=\sqrt{\tfrac32}(3-x)$. **Twists:** different interval (normalization), Gram–Schmidt for $p_1$, Legendre normalization, weight ⇒ classical families, a Parseval‑type norm.

**Problem 16.** On $[0,1]$ with weight $1$, the normalized constant polynomial $p_0(x)$ is
(a) $1$  (b) $\dfrac1{\sqrt2}$  (c) $\sqrt2$  (d) $\dfrac12$
> **Ans (a).** $\int_0^1 c^2\,dx=1\Rightarrow c=1$. *Trick:* the interval has length $1$ here (Q4's had length $2$, giving $1/\sqrt2$).

**Problem 17.** The first‑degree orthonormal polynomial on $[0,1]$ (weight $1$) is
(a) $\sqrt3\,(2x-1)$  (b) $\sqrt3\,x$  (c) $2\sqrt3\,(x-1)$  (d) $\sqrt{12}\,x$
> **Ans (a).** Gram–Schmidt: $x-\langle x,1\rangle=x-\tfrac12$, norm $\tfrac1{\sqrt{12}}$, normalize ⇒ $\sqrt3(2x-1)$. *Trick:* you must subtract the projection onto $p_0$ **before** normalizing.

**Problem 18.** The constant $N_n$ making $N_nP_n(x)$ orthonormal on $[-1,1]$ (Legendre $P_n$) is
(a) $\sqrt{\dfrac{2n+1}{2}}$  (b) $\sqrt{\dfrac{2}{2n+1}}$  (c) $\dfrac{2n+1}{2}$  (d) $\sqrt{2n+1}$
> **Ans (a).** $\int_{-1}^1P_n^2\,dx=\dfrac{2}{2n+1}$, so divide by its square root. *Trick:* it's the **reciprocal** square root of the known integral.

**Problem 19.** Polynomials orthogonal on $(-\infty,\infty)$ with weight $w(x)=e^{-x^{2}}$ are the
(a) Hermite  (b) Laguerre  (c) Legendre  (d) Chebyshev
> **Ans (a).** Weight + interval fix the family: $e^{-x^2}$ on $\mathbb R$ ⇒ Hermite. *Trick:* Laguerre go with $e^{-x}$ on $[0,\infty)$; don't swap them.

**Problem 20.** Using Q4's orthonormal set on $[2,4]$, $\displaystyle\int_2^4\big(3p_0(x)+2p_1(x)\big)^2dx=$
(a) $13$  (b) $25$  (c) $5$  (d) $1$
> **Ans (a).** Cross term vanishes by orthogonality: $9\!\int p_0^2+4\!\int p_1^2=9+4=13$. *Trick:* it's a Parseval/Pythagoras sum, **not** $(3+2)^2$.

---

# SET 5 — Analyticity & Cauchy–Riemann
**Origin (Q5):** analytic in $|z|<2$ ⇒ no $\bar z$, no fractional power. **Twists:** $z^2$ hidden in real form vs $|z|^2$, the CR equations, locating poles, harmonicity, $e^z$ disguised.

**Problem 21.** Which function is analytic everywhere (entire)?
(a) $e^{\bar z}$  (b) $\bar z^{2}$  (c) $(x^{2}-y^{2})+2ixy$  (d) $x^{2}+y^{2}$
> **Ans (c).** That's exactly $z^2$. *Trick:* (d) is $|z|^2$ (real, analytic only at $0$); (a),(b) carry $\bar z$.

**Problem 22.** For $f=u+iv$ to be analytic, $u,v$ must satisfy
(a) $u_x=v_y,\ u_y=-v_x$  (b) $u_x=-v_y,\ u_y=v_x$  (c) $u_x=v_x,\ u_y=v_y$  (d) $u_x=u_y,\ v_x=v_y$
> **Ans (a).** The Cauchy–Riemann equations. *Trick:* the **minus sign** sits on $u_y=-v_x$; option (b) flips it.

**Problem 23.** $f(z)=\dfrac{z}{z^{2}+1}$ is analytic everywhere **except** at
(a) $z=\pm i$  (b) $z=\pm1$  (c) $z=0$  (d) nowhere
> **Ans (a).** Singular where the denominator vanishes: $z^2+1=0$. *Trick:* $z=0$ is a *zero*, not a singularity.

**Problem 24.** Which can be the real part $u(x,y)$ of an analytic function (i.e. is harmonic)?
(a) $x^{2}-y^{2}$  (b) $x^{2}+y^{2}$  (c) $x^{2}y^{2}$  (d) $xy^{2}$
> **Ans (a).** Need $\nabla^2u=0$: $u_{xx}+u_{yy}=2-2=0$. *Trick:* (b) gives $4$, (c) gives $2(x^2+y^2)$, (d) gives $2x$ — none harmonic.

**Problem 25.** Which function is analytic throughout $\mathbb C$?
(a) $x^{2}+iy^{2}$  (b) $e^{x}(\cos y+i\sin y)$  (c) $x-iy$  (d) $x^{2}-y^{2}$
> **Ans (b).** That equals $e^{x}e^{iy}=e^{z}$. *Trick:* it's $e^z$ in disguise; (a) fails CR except on $x=y$, (c) is $\bar z$, (d) is real‑valued (fails CR off $x=0$).

---

# SET 6 — Eigenvalues & matrix functions (all‑ones matrix)
**Origin (Q6):** $M=$ all‑ones $3\times3$ has eigenvalues $0,0,3$ and $e^{M}=\mathbb1+\frac{e^{3}-1}{3}M$ (because $M^2=3M$). **Twists:** $n\times n$ spectrum, $a\mathbb1+bJ$, $e^P$ for a projector, $\det(M+\mathbb1)$, $M^k$.

**Problem 26.** The eigenvalues of the $4\times4$ all‑ones matrix are
(a) $0,0,0,4$  (b) $1,1,1,1$  (c) $0,0,4,4$  (d) $1,1,1,4$
> **Ans (a).** Rank‑1: eigenvalue $n=4$ once, $0$ with multiplicity $n-1=3$. *Trick:* it's "$n$ then zeros," regardless of size.

**Problem 27.** With $J=$ the $3\times3$ all‑ones matrix, the eigenvalues of $A=2\mathbb1+3J$ are
(a) $2,2,11$  (b) $5,5,5$  (c) $2,2,2$  (d) $5,5,11$
> **Ans (a).** $\lambda_A=2+3\lambda_J=2+3\{3,0,0\}=\{11,2,2\}$. *Trick:* the diagonal entries are $5$, which tempts "$5,5,5$" — but eigenvalues shift as $a+b\lambda_J$.

**Problem 28.** For any projection matrix $P$ (i.e. $P^{2}=P$), $e^{P}=$
(a) $\mathbb1+(e-1)P$  (b) $\mathbb1+eP$  (c) $eP$  (d) $\mathbb1+P+\tfrac{P^{2}}{2}$
> **Ans (a).** $e^{P}=\mathbb1+P\big(1+\tfrac1{2!}+\dots\big)=\mathbb1+(e-1)P$. *Trick:* $P^n=P$ collapses the whole series — same mechanism as Q6's $M^n=3^{n-1}M$.

**Problem 29.** For the $3\times3$ all‑ones matrix $M$, $\det(M+\mathbb1)=$
(a) $4$  (b) $0$  (c) $3$  (d) $27$
> **Ans (a).** Eigenvalues of $M+\mathbb1$ are $1,1,4$; product $=4$. *Trick:* $\det=\prod(\lambda_i+1)$, not $(\det M)+1$ (which would be wrong anyway since $\det M=0$).

**Problem 30.** For the $3\times3$ all‑ones matrix $M$, $M^{5}=$
(a) $81\,M$  (b) $243\,M$  (c) $3^{5}M$  (d) $125\,M$
> **Ans (a).** From $M^2=3M$ we get $M^n=3^{\,n-1}M$, so $M^5=3^4M=81M$. *Trick:* the exponent is $n-1$, so $3^4=81$, **not** $3^5$.

---

# SET 7 — Probability with dice
**Origin (Q7):** three dice, $P(\text{sum}=16)=\frac{6}{216}=\frac1{36}$ (partitions $665,654$... actually $(6,5,5)$ & $(6,6,4)$). **Twists:** a near‑max sum, two‑dice sum, binomial (exactly two sixes), conditional, at‑least‑one.

**Problem 31.** Three unbiased dice are rolled. $P(\text{sum}=17)=$
(a) $\dfrac1{72}$  (b) $\dfrac1{36}$  (c) $\dfrac1{108}$  (d) $\dfrac1{216}$
> **Ans (a).** Only $(6,6,5)$ works → $3$ orderings; $3/216=1/72$. *Trick:* a single partition near the maximum gives only $3$ microstates.

**Problem 32.** Two unbiased dice are rolled. $P(\text{sum}=9)=$
(a) $\dfrac19$  (b) $\dfrac16$  (c) $\dfrac{5}{36}$  (d) $\dfrac1{12}$
> **Ans (a).** $(3,6),(4,5),(5,4),(6,3)=4$ outcomes; $4/36=1/9$. *Trick:* count ordered pairs out of $36$, not unordered.

**Problem 33.** Three dice are rolled. The probability of getting **exactly two** sixes is
(a) $\dfrac{5}{72}$  (b) $\dfrac1{72}$  (c) $\dfrac1{36}$  (d) $\dfrac{25}{216}$
> **Ans (a).** Binomial: $\binom{3}{2}\big(\tfrac16\big)^2\big(\tfrac56\big)=\tfrac{15}{216}=\tfrac{5}{72}$. *Trick:* the third die must be a **non‑six**, and there are $\binom32=3$ placements.

**Problem 34.** Two dice are rolled. Given the sum is **even**, the probability that the sum is $8$ is
(a) $\dfrac{5}{18}$  (b) $\dfrac{5}{36}$  (c) $\dfrac16$  (d) $\dfrac59$
> **Ans (a).** $P(8\cap\text{even})/P(\text{even})=\tfrac{5/36}{18/36}=\tfrac{5}{18}$. *Trick:* the denominator shrinks to the $18$ even‑sum outcomes.

**Problem 35.** Three dice are rolled. The probability of getting **at least one** six is
(a) $\dfrac{91}{216}$  (b) $\dfrac12$  (c) $\dfrac{125}{216}$  (d) $\dfrac16$
> **Ans (a).** Complement: $1-\big(\tfrac56\big)^3=1-\tfrac{125}{216}=\tfrac{91}{216}$. *Trick:* "at least one" ≠ $3\times\tfrac16$ — use the complement.

---

# SET 8 — Legendre polynomials
**Origin (Q8):** generating function $G=(1-2xt+t^2)^{-1/2}$, and $P_3(-1)=-1$. **Twists:** parity at $0$, $G$ at $x=1$, Bonnet recurrence, the norm integral, an expansion‑in‑Legendre integral.

**Problem 36.** $P_3(0)=$
(a) $0$  (b) $-1$  (c) $1$  (d) $-\dfrac32$
> **Ans (a).** Odd‑index Legendre polynomials are odd functions ⇒ vanish at $x=0$. *Trick:* parity, not the $P_n(-1)=(-1)^n$ rule.

**Problem 37.** At $x=1$, the generating function $(1-2xt+t^{2})^{-1/2}$ simplifies to
(a) $\dfrac{1}{1-t}$  (b) $\dfrac{1}{1+t}$  (c) $\dfrac1{\sqrt{1-t}}$  (d) $1-t$
> **Ans (a).** $1-2t+t^2=(1-t)^2$, so $G=\frac1{1-t}=\sum t^n$, confirming $P_n(1)=1$. *Trick:* spot the perfect square under the root.

**Problem 38.** Using Bonnet's recurrence $(n+1)P_{n+1}=(2n+1)xP_n-nP_{n-1}$ with $P_0=1,P_1=x$, $P_2(x)=$
(a) $\dfrac{3x^{2}-1}{2}$  (b) $\dfrac{3x^{2}+1}{2}$  (c) $\dfrac{5x^{3}-3x}{2}$  (d) $x^{2}-1$
> **Ans (a).** $2P_2=3x\cdot x-1=3x^2-1$. *Trick:* divide by $n+1=2$ at the end; (c) is $P_3$.

**Problem 39.** $\displaystyle\int_{-1}^{1}\big[P_2(x)\big]^{2}\,dx=$
(a) $\dfrac25$  (b) $\dfrac23$  (c) $1$  (d) $\dfrac27$
> **Ans (a).** $\int_{-1}^1P_n^2=\frac{2}{2n+1}$ with $n=2$. *Trick:* it's **not** $1$ — Legendre polynomials are orthogonal but **not** normalized.

**Problem 40.** $\displaystyle\int_{-1}^{1}x^{2}\,P_2(x)\,dx=$
(a) $\dfrac{4}{15}$  (b) $\dfrac25$  (c) $0$  (d) $\dfrac{2}{15}$
> **Ans (a).** Write $x^2=\tfrac{2P_2+P_0}{3}$; only the $P_2$ piece survives: $\tfrac23\cdot\tfrac25=\tfrac{4}{15}$. *Trick:* it's **nonzero** — expand $x^2$ in Legendre first (it contains a $P_2$ component).

---

# SET 9 — Tangent planes & gradients
**Origin (Q9):** tangent plane to $xyz=8$ at $(1,2,4)$ is $4x+2y+z=12$ via $\nabla(xyz)=(yz,xz,xy)$. **Twists:** sphere, the normal direction concept, directional derivative, $z=f(x,y)$ form, the normal line.

**Problem 41.** The plane tangent to $x^{2}+y^{2}+z^{2}=9$ at $(1,2,2)$ is
(a) $x+2y+2z=9$  (b) $2x+4y+4z=9$  (c) $x+y+z=5$  (d) $x+2y+2z=3$
> **Ans (a).** $\nabla F=(2,4,2\cdot2)=(2,4,4)\parallel(1,2,2)$; plane $1(x-1)+2(y-2)+2(z-2)=0$. *Trick:* the RHS is $1{+}4{+}4=9$ (the point is on the sphere); (b) forgets to simplify the normal.

**Problem 42.** The direction **normal** to a surface $F(x,y,z)=c$ at a point is along
(a) $\nabla F$  (b) the tangent to the level curve  (c) $\partial F/\partial x$ alone  (d) $F$ itself
> **Ans (a).** The gradient is always perpendicular to its level surface. *Trick:* purely conceptual — $\nabla F\perp$ surface.

**Problem 43.** The directional derivative of $\phi=x^{2}yz$ at $(1,1,1)$ along $\hat n=\tfrac{1}{\sqrt3}(1,1,1)$ is
(a) $\dfrac{4}{\sqrt3}$  (b) $4$  (c) $\dfrac43$  (d) $2\sqrt3$
> **Ans (a).** $\nabla\phi=(2xyz,x^2z,x^2y)=(2,1,1)$; $\nabla\phi\cdot\hat n=\tfrac{2+1+1}{\sqrt3}=\tfrac4{\sqrt3}$. *Trick:* you **must normalize** the direction; forgetting gives $4$.

**Problem 44.** The plane tangent to $z=x^{2}+y^{2}$ at $(1,1,2)$ is
(a) $2x+2y-z=2$  (b) $2x+2y+z=2$  (c) $x+y-z=0$  (d) $2x+2y-z=6$
> **Ans (a).** $z=2+2(x-1)+2(y-1)=2x+2y-2$, i.e. $2x+2y-z=2$. *Trick:* for $z=f(x,y)$ the normal is $(f_x,f_y,-1)$ — note the $-z$.

**Problem 45.** The normal line to $xyz=8$ at $(1,2,4)$ has direction ratios
(a) $(4,2,1)$  (b) $(1,2,4)$  (c) $(1,1,1)$  (d) $(2,4,8)$
> **Ans (a).** $\nabla(xyz)=(yz,xz,xy)=(8,4,2)\parallel(4,2,1)$. *Trick:* same gradient as Q9's plane normal — the **point coordinates $(1,2,4)$** are a distractor.

---

# SET 10 — Traces, eigenvalues & power sums
**Origin (Q10):** $\operatorname{Tr}M=6,\operatorname{Tr}M^2=26,\operatorname{Tr}M^3=90$ ⇒ eigenvalues $\{-1,3,4\}$. **Twists:** $2\times2$ Newton, $\det$ from three traces, $\operatorname{Tr}(M^4)$, Cayley–Hamilton, another "which set" with new numbers.

**Problem 46.** A $2\times2$ matrix has $\operatorname{Tr}(M)=3$ and $\operatorname{Tr}(M^{2})=5$. Its eigenvalues are
(a) $1,2$  (b) $0,3$  (c) $-1,4$  (d) $1.5,1.5$
> **Ans (a).** $\lambda_1\lambda_2=\tfrac{(\sum\lambda)^2-\sum\lambda^2}{2}=\tfrac{9-5}{2}=2$; solve $\lambda^2-3\lambda+2=0$. *Trick:* convert power sums to the product, then to the characteristic equation.

**Problem 47.** A $3\times3$ matrix has $\operatorname{Tr}(M)=6,\ \operatorname{Tr}(M^{2})=14,\ \operatorname{Tr}(M^{3})=36$. Then $\det(M)=$
(a) $6$  (b) $11$  (c) $36$  (d) $14$
> **Ans (a).** Newton: $e_1=6,\ e_2=\tfrac{6^2-14}{2}=11,\ e_3=\tfrac{e_1^3-3e_1e_2+2p_3}{6}=\tfrac{216-252+72}{6}=6$; eigenvalues $\{1,2,3\}$. *Trick:* $\det=e_3$ (the product), reached only after $e_1,e_2$.

**Problem 48.** A $3\times3$ matrix has eigenvalues $1,-1,2$. Then $\operatorname{Tr}(M^{4})=$
(a) $18$  (b) $8$  (c) $16$  (d) $6$
> **Ans (a).** $\operatorname{Tr}(M^4)=\sum\lambda_i^4=1+1+16=18$. *Trick:* $(-1)^4=+1$, so the negative eigenvalue still adds $1$.

**Problem 49.** A $2\times2$ matrix has $\operatorname{Tr}(M)=5$ and $\det(M)=6$. Then $M^{2}=$
(a) $5M-6\mathbb1$  (b) $6M-5\mathbb1$  (c) $5M+6\mathbb1$  (d) $M-6\mathbb1$
> **Ans (a).** Cayley–Hamilton: $M^2-(\operatorname{Tr}M)M+(\det M)\mathbb1=0$. *Trick:* the characteristic polynomial is $\lambda^2-(\operatorname{Tr})\lambda+\det$ — sign on $\det$ is $+$.

**Problem 50.** A $3\times3$ matrix has $\operatorname{Tr}(M)=2,\ \operatorname{Tr}(M^{2})=6,\ \operatorname{Tr}(M^{3})=8$. A possible set of eigenvalues is
(a) $\{-1,1,2\}$  (b) $\{0,1,1\}$  (c) $\{2,0,0\}$  (d) $\{1,1,0\}$
> **Ans (a).** Check all three: $-1{+}1{+}2=2$; $1{+}1{+}4=6$; $-1{+}1{+}8=8$. *Trick:* a set must match **all three** power sums at once — (b),(c),(d) each fail the $\operatorname{Tr}(M^2)=6$ test.

---

### How to use this set
Do each block of 5 cold, then check the **trick line** — that line is the actual lesson. The five within a block are deliberately *not* harder copies of each other; they each fail a *different* way if you're not careful (wrong pole inside the contour, half‑angle in $SU(2)$, projection‑vs‑reflection, un‑normalized Legendre, $n{-}1$ exponent, "at least one" complement, normalize‑the‑direction, match‑all‑three‑traces, …). If a block feels easy, you've internalized the original CSIR‑NET question it grew from.
