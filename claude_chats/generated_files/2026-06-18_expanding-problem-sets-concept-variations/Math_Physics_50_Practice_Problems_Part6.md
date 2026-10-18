# 50 Practice Problems — Part 6 (CSIR‑NET/JRF style)

**Built from problems 51–60 of the *fiziks* "Mathematical Physics Solutions" booklet.** Same method: extract the *core concept* of each original, then write **5 new problems** that each attack a **different** subtlety. Every problem is MCQ with the answer and a one‑line **"why / what's the trick"** beneath it. Problems are numbered **251–300** to continue Parts 1–5.

> **Source of these 10:** Official **CSIR‑UGC NET/JRF Physical Sciences** previous‑year papers — **Q51–Q58 = Dec 2014**, **Q59–Q60 = June 2015** — with *fiziks* (physicsbyfiziks.com) supplying the worked solutions. Textbook study: **Arfken–Weber–Harris**, **Boas**, **Riley–Hobson–Bence**.

---

## Concept map (originals Q51–Q60)

| Q | Topic | Core idea tested |
|---|-------|------------------|
| Q51 | Linear algebra | Simultaneous eigenvectors of commuting matrices |
| Q52 | Complex analysis | Principal‑value integral; higher‑order pole residue |
| Q53 | Complex analysis | Laurent series with an **essential** singularity |
| Q54 | Probability | Poisson distribution (mean $=$ variance; additivity) |
| Q55 | Complex analysis | Classifying singularities (removable / pole / branch) |
| Q56 | Special functions | Bessel functions & Bessel's equation of order $n$ |
| Q57 | Group theory | Group axioms for sets of matrices |
| Q58 | Mechanics/algebra | Levi‑Civita symbol & Poisson brackets |
| Q59 | Complex analysis | Contour integral of a rational function |
| Q60 | ODEs | Linear ODE **boundary‑value** problem (distinct roots) |

---

# SET 51 — Simultaneous eigenvectors of commuting matrices
**Origin (Q51):** $(a,b,a)^T$ is a common eigenvector of the swap $A=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}$ and $B=J-I=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$ when $b=a$ or $b=-2a$. **Twists:** the commuting condition, eigenvectors of $J-I$, the eigenvalue shift, and the symmetric/antisymmetric eigenvectors of the swap.

**Problem 251.** Two diagonalizable matrices can be **simultaneously** diagonalized if and only if
(a) $[A,B]=0$  (b) they are symmetric  (c) they have the same eigenvalues  (d) one is the identity
> **Ans (a).** Commuting matrices share a complete common eigenbasis. *Trick:* commutation, not symmetry, is the condition for simultaneous eigenvectors.

**Problem 252.** $(1,1,1)^T$ is an eigenvector of $B=J-I$ (with $J$ the $3\times3$ all‑ones matrix) with eigenvalue
(a) $2$  (b) $3$  (c) $0$  (d) $-1$
> **Ans (a).** $J(1,1,1)^T=3(1,1,1)^T$, so $(J-I)(1,1,1)^T=(3-1)(1,1,1)^T$. *Trick:* the $-I$ shifts $J$'s eigenvalue $3$ down to $2$.

**Problem 253.** If $\vec v$ is an eigenvector of $A$ with eigenvalue $\lambda$, then $\vec v$ is an eigenvector of $A+cI$ with eigenvalue
(a) $\lambda+c$  (b) $c\lambda$  (c) $\lambda$  (d) $c$
> **Ans (a).** Adding $cI$ shifts every eigenvalue by $c$ but keeps the eigenvectors. *Trick:* this is exactly the $J\to J-I$ relation underlying Q51.

**Problem 254.** The swap matrix $A=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}$ has $(1,0,1)^T$ as an eigenvector with eigenvalue
(a) $1$  (b) $-1$  (c) $0$  (d) $2$
> **Ans (a).** $A(1,0,1)^T=(1,0,1)^T$. *Trick:* vectors **symmetric** under the swap are fixed (eigenvalue $+1$).

**Problem 255.** For the same swap matrix, $(1,0,-1)^T$ is an eigenvector with eigenvalue
(a) $-1$  (b) $1$  (c) $0$  (d) $2$
> **Ans (a).** $A(1,0,-1)^T=(-1,0,1)^T=-(1,0,-1)^T$. *Trick:* the **antisymmetric** combination flips sign (eigenvalue $-1$).

---

# SET 52 — Principal‑value integrals & higher‑order pole residues
**Origin (Q52):** $\text{P}\!\int_{-\infty}^{\infty}\frac{\sin 2x}{x^3}\,dx=-2\pi$; the order‑3 pole at $0$ has residue $-2$, and one takes the imaginary part. **Twists:** the half‑residue, the residue itself, the odd‑integrand case, Jordan's lemma, the value.

**Problem 256.** A small semicircular indentation around a **simple** pole lying on the contour contributes
(a) $\pi i\times(\text{residue})$  (b) $2\pi i\times\text{residue}$  (c) $0$  (d) the full residue
> **Ans (a).** A pole on the contour gives half the usual factor. *Trick:* indentation $\Rightarrow\pi i$, not $2\pi i$.

**Problem 257.** The residue of $\dfrac{e^{2iz}}{z^3}$ at $z=0$ is
(a) $-2$  (b) $2$  (c) $-2i$  (d) $4$
> **Ans (a).** Order‑3 pole: $\dfrac{1}{2!}\dfrac{d^2}{dz^2}e^{2iz}\big|_0=\dfrac{(2i)^2}{2}=-2$. *Trick:* the second derivative and $(2i)^2=-4$.

**Problem 258.** $\text{P}\!\displaystyle\int_{-\infty}^{\infty}\frac{\cos 2x}{x^{3}}\,dx=$
(a) $0$  (b) $-2\pi$  (c) $2\pi$  (d) $\pi$
> **Ans (a).** $\cos(2x)/x^3$ is an **odd** function, so its principal value vanishes. *Trick:* only the $\sin$ part of $e^{2ix}/x^3$ survives — which is why Q52 evaluates the sine integral.

**Problem 259.** To evaluate $\displaystyle\int_{-\infty}^{\infty}f(x)e^{iax}\,dx$ with $a>0$ by residues, one closes the contour
(a) in the upper half‑plane  (b) in the lower half‑plane  (c) along the real axis  (d) either way
> **Ans (a).** $e^{iaz}=e^{iax}e^{-ay}$ decays for $y>0$ when $a>0$ (Jordan's lemma). *Trick:* the sign of $a$ fixes which half‑plane lets the arc vanish.

**Problem 260.** $\text{P}\!\displaystyle\int_{-\infty}^{\infty}\frac{\sin 2x}{x^{3}}\,dx=$
(a) $-2\pi$  (b) $2\pi$  (c) $-\pi$  (d) $\pi$
> **Ans (a).** $\operatorname{Im}\big[\pi i(-2)\big]=\operatorname{Im}(-2\pi i)=-2\pi$. *Trick:* take the imaginary part of $\pi i\times$ residue (Q52).

---

# SET 53 — Laurent series with essential singularities
**Origin (Q53):** $e^z+e^{1/z}=\sum_{n\ge0}\big(z^n+z^{-n}\big)\tfrac1{n!}$, valid in $0<|z|<\infty$. **Twists:** classifying $e^{1/z}$, its residue, the region of convergence, pole vs essential, removable.

**Problem 261.** The function $e^{1/z}$ has, at $z=0$,
(a) an essential singularity  (b) a simple pole  (c) a removable singularity  (d) a branch point
> **Ans (a).** Its Laurent series has infinitely many negative powers. *Trick:* an infinite principal part = essential singularity.

**Problem 262.** The residue of $e^{1/z}$ at $z=0$ is
(a) $1$  (b) $0$  (c) $\infty$  (d) $e$
> **Ans (a).** $e^{1/z}=\sum_n\dfrac{z^{-n}}{n!}$; the $z^{-1}$ coefficient ($n=1$) is $1$. *Trick:* read the residue off the Laurent series — there's no pole formula for essential singularities.

**Problem 263.** The Laurent series of $e^{z}+e^{1/z}$ converges for
(a) $0<|z|<\infty$  (b) $|z|<1$  (c) $|z|>1$  (d) $|z|<\infty$ including $0$
> **Ans (a).** $e^z$ converges everywhere; $e^{1/z}$ for $z\neq0$. *Trick:* the intersection is the **punctured** plane (Q53).

**Problem 264.** A Laurent series with a **finite** number of negative‑power terms indicates
(a) a pole (of finite order)  (b) an essential singularity  (c) a removable singularity  (d) a branch point
> **Ans (a).** Finite principal part $\Rightarrow$ pole. *Trick:* finite = pole, infinite = essential (the contrast with Q53's $e^{1/z}$).

**Problem 265.** The function $\dfrac{\sin z}{z}$ at $z=0$ has
(a) a removable singularity  (b) a simple pole  (c) an essential singularity  (d) a branch point
> **Ans (a).** Its Laurent series has no negative powers; the limit is $1$. *Trick:* no principal part at all ⇒ removable.

---

# SET 54 — Poisson distribution
**Origin (Q54):** for independent Poissons (means $\mu,\nu$), $m+n$ is Poisson$(\mu+\nu)$, so $\operatorname{Var}(m+n)=\mu+\nu$. **Twists:** mean $=$ variance, the sum, the (non‑Poisson) difference, the variance of the difference, the binomial limit.

**Problem 266.** For a Poisson distribution with parameter $\lambda$, the variance is
(a) $\lambda$  (b) $\sqrt\lambda$  (c) $\lambda^{2}$  (d) $1$
> **Ans (a).** Poisson's signature: mean $=$ variance $=\lambda$. *Trick:* this equality is what makes Q54(c) correct.

**Problem 267.** If $X\sim\text{Poisson}(\mu)$ and $Y\sim\text{Poisson}(\nu)$ are independent, then $X+Y\sim$
(a) $\text{Poisson}(\mu+\nu)$  (b) $\text{Poisson}(\mu\nu)$  (c) binomial  (d) Gaussian
> **Ans (a).** Poisson is closed under addition; the parameters add. *Trick:* sums of independent Poissons stay Poisson.

**Problem 268.** The difference $m-n$ of two independent Poissons is
(a) not a Poisson distribution  (b) $\text{Poisson}(\mu-\nu)$  (c) $\text{Poisson}(\mu+\nu)$  (d) always zero
> **Ans (a).** It can be **negative**, so it cannot be Poisson (it's a Skellam distribution). *Trick:* this is why Q54's option (b) is false.

**Problem 269.** The variance of $m-n$ (independent Poissons, means $\mu,\nu$) is
(a) $\mu+\nu$  (b) $\mu-\nu$  (c) $\mu^{2}+\nu^{2}$  (d) $0$
> **Ans (a).** Variances **add** for independent variables, even for a difference. *Trick:* $\operatorname{Var}(m-n)=\operatorname{Var}m+\operatorname{Var}n=\mu+\nu$, **not** $\mu-\nu$.

**Problem 270.** The Poisson distribution arises as a limit of the binomial when
(a) $n\to\infty,\ p\to0$ with $np=\lambda$ fixed  (b) $n\to\infty,\ p\to1$  (c) $p=\tfrac12$  (d) $n$ finite
> **Ans (a).** Rare events in many trials. *Trick:* the "law of small numbers" — $np$ held fixed.

---

# SET 55 — Classifying singularities
**Origin (Q55):** $\dfrac1z\ln(1-z)$ has a **removable** singularity at $z=0$ (since $\ln(1-z)\sim-z$ cancels the $1/z$) and branch points at $z=1,\infty$. **Twists:** the removable case, log's branch point, another removable, a genuine pole, the branch point at infinity.

**Problem 271.** The function $\dfrac1z\ln(1-z)$ at $z=0$ has
(a) a removable singularity  (b) a simple pole  (c) an essential singularity  (d) a branch point
> **Ans (a).** $\ln(1-z)=-z-\tfrac{z^2}{2}-\cdots$, so $\tfrac1z\ln(1-z)=-1-\tfrac z2-\cdots$ (finite, $\to-1$). *Trick:* the $1/z$ is killed by $\ln(1-z)\sim-z$.

**Problem 272.** The function $\ln z$ has, at $z=0$,
(a) a branch point  (b) a simple pole  (c) an essential singularity  (d) a removable singularity
> **Ans (a).** Log is multivalued around $z=0$. *Trick:* a branch point, not a pole — there's no Laurent series there.

**Problem 273.** $\dfrac{e^{z}-1}{z}$ at $z=0$ has
(a) a removable singularity  (b) a simple pole  (c) an essential singularity  (d) a double pole
> **Ans (a).** $e^z-1=z+\tfrac{z^2}{2}+\cdots$, so the ratio $\to1$. *Trick:* the numerator's zero cancels the pole.

**Problem 274.** $\dfrac{\cos z}{z^{2}}$ at $z=0$ has a pole of order
(a) $2$  (b) $1$  (c) $0$  (d) $3$
> **Ans (a).** $\cos0=1\neq0$, so the $z^2$ is uncancelled. *Trick:* contrast with Q273 — here the numerator does **not** vanish, giving a genuine order‑2 pole.

**Problem 275.** $\ln(1-z)$ has branch points at
(a) $z=1$ and $z=\infty$  (b) $z=0$  (c) $z=-1$  (d) nowhere
> **Ans (a).** The argument $1-z$ vanishes at $z=1$, and log also branches at $\infty$. *Trick:* these are exactly the branch points of Q55.

---

# SET 56 — Bessel functions & Bessel's equation
**Origin (Q56):** $f(x)=\sum_n\dfrac{(-1)^n}{n!(n+1)!}\big(\tfrac x2\big)^{2n+1}=J_1(x)$, satisfying $x^2f''+xf'+(x^2-1)f=0$. **Twists:** Bessel's general equation, recognizing $J_1$, $J_1(0)$, the derivative relation, the leading power.

**Problem 276.** Bessel's equation of order $n$ is
(a) $x^{2}y''+xy'+(x^{2}-n^{2})y=0$  (b) $x^{2}y''+xy'+(x^{2}+n^{2})y=0$  (c) $y''+n^{2}y=0$  (d) $xy''+y'+xy=0$
> **Ans (a).** Note the $-n^2$ term and the $x^2y''+xy'$ structure. *Trick:* Q56 is just the $n=1$ case of this.

**Problem 277.** The series $\displaystyle\sum_n\frac{(-1)^n}{n!(n+1)!}\Big(\frac x2\Big)^{2n+1}$ is
(a) $J_1(x)$  (b) $J_0(x)$  (c) $Y_1(x)$  (d) $I_1(x)$
> **Ans (a).** The $(n+1)!$ and the odd power $2n+1$ mark it as order $1$. *Trick:* the structure of the series fixes the order.

**Problem 278.** $J_1(0)=$
(a) $0$  (b) $1$  (c) $\tfrac12$  (d) $\infty$
> **Ans (a).** Its lowest term is $\propto(x/2)^1$. *Trick:* only $J_0(0)=1$; every $J_{p\ge1}$ vanishes at the origin.

**Problem 279.** $J_0'(x)=$
(a) $-J_1(x)$  (b) $J_1(x)$  (c) $J_0(x)$  (d) $-J_0(x)$
> **Ans (a).** A standard Bessel recurrence. *Trick:* $J_0'=-J_1$ (mind the minus sign).

**Problem 280.** The leading power of $x$ in $J_p(x)$ is
(a) $x^{p}$  (b) $x^{0}$  (c) $x^{2p}$  (d) $x^{p+1}$
> **Ans (a).** $J_p(x)\sim\dfrac{1}{p!}\big(\tfrac x2\big)^p$ near $0$. *Trick:* the order equals the leading power.

---

# SET 57 — Group axioms for matrices
**Origin (Q57):** the set $\begin{pmatrix}\alpha&\beta\\-\beta^*&\alpha^*\end{pmatrix}$ with $|\alpha|^2+|\beta|^2=1$ is a group; the other options fail closure, identity, or inverse. **Twists:** the no‑inverse failure, the identity requirement, closure via determinant, closure under inverse, a non‑closure example.

**Problem 281.** A set of matrices containing a singular ($\det=0$) matrix cannot form a group under multiplication because
(a) the singular matrix has no inverse  (b) they don't commute  (c) they aren't square  (d) the identity is missing
> **Ans (a).** Invertibility is required by the inverse axiom. *Trick:* Q57's option (a), $\begin{pmatrix}\alpha&\beta\\0&0\end{pmatrix}$, is singular — instantly disqualified.

**Problem 282.** For a set of matrices to be a group under multiplication, it must contain
(a) the identity $I$  (b) the zero matrix  (c) a diagonal matrix  (d) a symmetric matrix
> **Ans (a).** Every group needs an identity element. *Trick:* the multiplicative identity is $I$ — a set lacking it isn't a group.

**Problem 283.** $SL(2)$ (matrices with $\det=1$) is closed under multiplication because
(a) $\det(AB)=\det(A)\det(B)$  (b) the trace is preserved  (c) they commute  (d) they are orthogonal
> **Ans (a).** $\det(AB)=1\cdot1=1$. *Trick:* the multiplicative property of determinants guarantees closure.

**Problem 284.** $SU(2)$ is a group partly because each element's inverse (its conjugate transpose) is
(a) also in $SU(2)$  (b) the zero matrix  (c) singular  (d) undefined
> **Ans (a).** Closure under inverses. *Trick:* the inverse must stay inside the set — for $SU(2)$, $U^{-1}=U^\dagger$ does.

**Problem 285.** Do all $2\times2$ matrices with $\det=2$ form a group under multiplication?
(a) no — the product has $\det=4$, leaving the set  (b) yes  (c) only if symmetric  (d) yes, with identity $I$
> **Ans (a).** Closure fails: $\det(AB)=4\notin\{\det=2\}$ (and $I$ has $\det=1$). *Trick:* only $\det=1$ (or $\det\neq0$ with no fixed value) can be closed.

---

# SET 58 — Levi‑Civita symbol & Poisson brackets
**Origin (Q58):** $\sum_{ijk}\epsilon_{ijk}\{x_i,\{p_j,L_k\}\}=6$, using Poisson brackets and the fully‑contracted $\epsilon_{ijk}\epsilon_{ijk}=6$. **Twists:** the full contraction, the two‑index identity, the single contraction, canonical PBs, the angular‑momentum algebra.

**Problem 286.** $\displaystyle\sum_{i,j,k}\epsilon_{ijk}\epsilon_{ijk}=$
(a) $6$  (b) $3$  (c) $1$  (d) $9$
> **Ans (a).** $\epsilon_{ijk}\epsilon_{ijk}=3!=6$. *Trick:* this fully‑contracted value is what produces Q58's answer.

**Problem 287.** $\displaystyle\sum_i\epsilon_{ijk}\epsilon_{ilm}=$
(a) $\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$  (b) $\delta_{jl}\delta_{km}+\delta_{jm}\delta_{kl}$  (c) $\delta_{jk}\delta_{lm}$  (d) $\delta_{jm}\delta_{kl}$
> **Ans (a).** The fundamental $\epsilon$–$\epsilon$ identity (one common index). *Trick:* the "$\delta\delta-\delta\delta$" pattern underlies most vector identities.

**Problem 288.** $\displaystyle\sum_{i,j}\epsilon_{ijk}\epsilon_{ijl}=$
(a) $2\delta_{kl}$  (b) $\delta_{kl}$  (c) $6\delta_{kl}$  (d) $\tfrac12\delta_{kl}$
> **Ans (a).** Two common indices give $2\delta_{kl}$. *Trick:* the factor of $2$ is easy to drop.

**Problem 289.** The canonical Poisson bracket $\{x_i,p_j\}=$
(a) $\delta_{ij}$  (b) $\epsilon_{ijk}$  (c) $0$  (d) $1$
> **Ans (a).** The fundamental phase‑space bracket. *Trick:* it's the Kronecker delta $\delta_{ij}$.

**Problem 290.** The angular‑momentum Poisson bracket $\{L_i,L_j\}=$
(a) $\epsilon_{ijk}L_k$  (b) $\delta_{ij}$  (c) $0$  (d) $L_iL_j$
> **Ans (a).** The components close into the rotation ($\mathfrak{so}(3)$) algebra. *Trick:* $\{L_i,L_j\}=\epsilon_{ijk}L_k$ — the classical analogue of $[L_i,L_j]=i\hbar\epsilon_{ijk}L_k$.

---

# SET 59 — Contour integrals of rational functions
**Origin (Q59):** $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^4}=\frac{\pi}{\sqrt2}$; poles at the fourth roots of $-1$, summing the upper‑half‑plane residues. **Twists:** the basic case, the squared denominator, which poles, the value, the degree condition.

**Problem 291.** $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^{2}}=$
(a) $\pi$  (b) $\dfrac\pi2$  (c) $2\pi$  (d) $\dfrac\pi{\sqrt2}$
> **Ans (a).** $2\pi i\cdot\operatorname{Res}_{i}\tfrac{1}{1+z^2}=2\pi i\cdot\tfrac1{2i}=\pi$. *Trick:* the full line gives $\pi$ (the half‑line would give $\pi/2$).

**Problem 292.** $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{(1+x^{2})^{2}}=$
(a) $\dfrac\pi2$  (b) $\pi$  (c) $\dfrac\pi4$  (d) $\dfrac\pi{\sqrt2}$
> **Ans (a).** A double pole at $z=i$; the residue gives $\pi/2$. *Trick:* also obtainable by differentiating the $\pi$ result with respect to a parameter.

**Problem 293.** For $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^{4}}$, the poles in the upper half‑plane are
(a) $e^{i\pi/4},\,e^{3i\pi/4}$  (b) $e^{i\pi/2},\,e^{-i\pi/2}$  (c) all four roots  (d) $e^{-i\pi/4},\,e^{-3i\pi/4}$
> **Ans (a).** Only the two fourth roots of $-1$ with positive imaginary part. *Trick:* closing in the upper half‑plane selects the upper poles.

**Problem 294.** $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^{4}}=$
(a) $\dfrac{\pi}{\sqrt2}$  (b) $\dfrac\pi2$  (c) $\pi$  (d) $2\pi$
> **Ans (a).** $2\pi i$ times the sum of the two upper residues. *Trick:* the standard result $\pi/\sqrt2$ (Q59).

**Problem 295.** Closing a real‑line integral with a large upper semicircle is valid when
(a) $\deg Q\ge\deg P+2$ (so the arc vanishes)  (b) $\deg Q=\deg P$  (c) $\deg P>\deg Q$  (d) always
> **Ans (a).** The semicircle contribution $\to0$ only if the integrand falls faster than $1/|z|$. *Trick:* you need a degree gap of at least $2$ between denominator and numerator.

---

# SET 60 — Linear ODE boundary‑value problems
**Origin (Q60):** $\ddot x-3\dot x+2x=0$ with $x(0)=0,\ x(1)=1$ gives $x(2)=e^2+e$ (roots $1,2$; two‑point conditions). **Twists:** the roots, the general solution, BVP vs IVP, applying a condition, the answer.

**Problem 296.** $\ddot x-3\dot x+2x=0$ has characteristic roots
(a) $1,\,2$  (b) $-1,\,-2$  (c) $1,\,-2$  (d) $3,\,2$
> **Ans (a).** $m^2-3m+2=(m-1)(m-2)=0$. *Trick:* distinct positive roots — note both signs are positive (the $-3\dot x$ doesn't make them negative).

**Problem 297.** The general solution of $\ddot x-3\dot x+2x=0$ is
(a) $c_1e^{t}+c_2e^{2t}$  (b) $c_1e^{-t}+c_2e^{-2t}$  (c) $(c_1+c_2t)e^{t}$  (d) $c_1\cos t+c_2\sin t$
> **Ans (a).** Distinct real roots give two pure exponentials. *Trick:* no factor of $t$ (that's only for repeated roots).

**Problem 298.** In Q60, the conditions are imposed at $t=0$ **and** $t=1$. This is a
(a) boundary‑value problem  (b) initial‑value problem  (c) eigenvalue problem  (d) homogeneous‑only problem
> **Ans (a).** Conditions at two distinct points = BVP. *Trick:* contrast with Q45 (both conditions at $t=0$ = IVP).

**Problem 299.** For $x=c_1e^{t}+c_2e^{2t}$, the condition $x(0)=0$ gives
(a) $c_1+c_2=0$  (b) $c_1=1$  (c) $c_2=0$  (d) $c_1=c_2$
> **Ans (a).** At $t=0$ both exponentials equal $1$. *Trick:* $x(0)=c_1+c_2=0$.

**Problem 300.** For $\ddot x-3\dot x+2x=0$ with $x(0)=0,\ x(1)=1$, the value $x(2)=$
(a) $e^{2}+e$  (b) $e^{2}+1$  (c) $e+2$  (d) $2e$
> **Ans (a).** Solving gives $x(t)=\dfrac{e^{2t}-e^{t}}{e^2-e}$, so $x(2)=\dfrac{e^4-e^2}{e^2-e}=e(e+1)=e^2+e$. *Trick:* the messy constants cancel into a clean $e^2+e$.

---

### How to use this set
Same drill: do each block of $5$ cold, then read the **trick line**. Across the ten blocks the lessons are: commuting matrices share eigenvectors (and $A+cI$ shifts eigenvalues); a pole **on** the contour gives $\pi i$, and odd integrands have zero principal value; an infinite principal part means an essential singularity; Poisson has variance $=\lambda$ and the difference's variance still **adds**; $\tfrac1z\ln(1-z)$ is removable, not a pole; Bessel order $=$ leading power; a group needs an identity and invertible (non‑singular) elements; $\epsilon_{ijk}\epsilon_{ijk}=6$; close in the upper half‑plane and mind the degree gap; and a two‑point ODE is a BVP, not an IVP. Master a block and you own the CSIR‑NET concept it grew from. **You now have a continuous bank of 300 problems across the first 60 originals (Q1–Q60).**
