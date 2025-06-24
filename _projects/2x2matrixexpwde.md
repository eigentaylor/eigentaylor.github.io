---
layout: distill
title: 2x2 Matrix Exponential Formulas with Differential Equations
date: 2021-12-08
description:
comments: true
importance: 6
category: archive
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Formulas
  - name: Proofs
    subsections:
      - name: Intro
      - name: Distinct Eigenvalues
      - name: Complex Conjugate Eigenvalues
      - name: One Defective Eigenvalue
      - name: One Nondefective Eigenvalue
  - name: Applications
  - name: Closing Remarks
---

<details>
  <summary style="color:white;">This is a rewrite</summary>
    <p>This is a rewrite of an <a href="../ezmatrixexp" target="_blank">older post</a> I made a while ago. At the time I thought Laplace Transforms were the best way to do this, but I've come to realize that the best way is using the method outlined in <a href="../matrixexpwde" target="_blank">this post</a> using normalized solutions.</p>
</details>

**WARNING**: If you are in a differential equations class right now, turn back. This is black magic that your professor _will not_ want you to memorize or use on their tests. These are just cool and/or for the convenience of those who evaluate a lot of matrix exponentials, as I do.

# Formulas

Let $$A$$ be a $$2\times 2$$ matrix.

If $$A$$ has two distinct eigenvalues $$\lambda_1,\lambda_2$$, then

$$\begin{equation} \label{form1}
e^{At}=\frac{e^{\lambda_2t}(A-\lambda_1I)-e^{\lambda_1t}(A-\lambda_2I)}{\lambda_2-\lambda_1}
\end{equation}$$

Or alternatively,

$$\begin{equation} \label{form1a}
e^{At}=\frac{\lambda_2e^{\lambda_1t}-\lambda_1e^{\lambda_2t}}{\lambda_2-\lambda_1}I +
\frac{e^{\lambda_2t}-e^{\lambda_1t}}{\lambda_2-\lambda_1}A
\end{equation}$$

If $$A$$ has a real determinant, $$\operatorname{tr}(A)=0$$, and $$\det(A)<0$$, then an eigenvalue of $$A$$ is $$\lambda=\sqrt{-\det(A)}$$, and

$$\begin{equation} \label{form1b}
e^{At}=\cosh(\lambda t)I+\frac{\sinh(\lambda t)}{\lambda}A
\end{equation}$$

If $$A$$ is singular and has a nonzero trace,

$$\begin{equation}\label{form1c}
e^{At}=\frac{e^{\operatorname{tr}(A)t}A-(A-\operatorname{tr}(A)I)}{\operatorname{tr}(A)}
\end{equation}$$

$$\begin{equation}\label{form1cb}
e^{At}=I+\frac{e^{\operatorname{tr}(A)t}-1}{\operatorname{tr}(A)}A
\end{equation}$$

If $$A$$ is real and has complex conjugate eigenvalues $$a \pm bi$$, then

$$\begin{equation}\label{form2a}
e^{At}=e^{a  t}\left(\cos(b  t)I+\frac{\sin(b  t)}{b }(A-a  I)\right)
\end{equation}$$

$$\begin{equation} \label{form2b}
e^{At}=\frac{e^{at}}{b}\bigg(b\cos(b  t)I+\sin(b  t)(A-a  I)\bigg)
\end{equation}$$

If $$A$$ has one defective eigenvalue $$\lambda$$, then

$$\begin{equation} \label{form3}
e^{At}=e^{\lambda t}\left(I+t(A-\lambda I)\right)
\end{equation}$$

And if $$A$$ has only one eigenvalues $$\lambda$$ which is not defective (meaning $$A=\lambda I$$) then

$$\begin{equation} \label{form4}
e^{\lambda It}=e^{\lambda t}I
\end{equation}$$

# Proofs

I would not say it's required reading, but to prove these formulas, we are going to primarily use [this post](../matrixexpwde){:target="_blank"}. The method outlined in that post utilizes the [normalized solutions](../normalized){:target="_blank"} of the linear differential equation obtained from the characteristic polynomial. This is ideal for $$2\times2$$ matrices, because second order equations have very easy normalized solutions relative to anything of higher order. Since these normalized solutions are easy to remember, it makes these exponential formulas easy to remember too (if you know them).

## Intro

Quick summary for those who don't want to read the other posts but also kind of want to know what's going on: normalized solutions are solutions to differential equations which are ideal to solve initial value problems. Take the example $$y_1=\cos(t),y_2=\sin(t)$$. The general solution $$\phi(t)$$ to the initial value problem

$$y''+y=0,\,y(0)=y_0,y'(0)=y'_0$$

can be written conveniently as

$$\phi(t)=y_0\cos(t)+y'_0\sin(t)$$

In short, the coefficients are just the initial conditions. Specifically, they satisfy the two initial value problems

$$Y_1''+Y_1=0,\,Y_1(0)=1,Y_1'(0)=0$$

$$Y_2''+Y_2=0,\,Y_2(0)=0,Y_2'(0)=1$$

My post on [normalized solutions](../normalized){:target="_blank"} covers ways to get them, but I'll just give them to you in the following section. Observe, though, that the initial conditions form the identity matrix :eyes:

The way we can use these normalized solutions to get our matrix exponential is done by considering $$e^{At}$$ to be the solution $$\Phi(t)$$ to the initial value problem

$$\begin{equation} \label{matrixIVP}
\textbf{X}''+b\textbf{X}'+c\textbf{X}=0,\,\textbf{X}(0)=I,\textbf{X}'(0)=A
\end{equation}$$

Where $$\lambda^2+b\lambda+c=\det(A-\lambda I)$$ is the characteristic polynomial of $$A$$.

Why can we do this? Without getting too technical, this comes from the Cayley–Hamilton theorem which tells us that $$A$$ satisfies it's own characteristic polynomial (actually the minimal polynomial but we don't have to worry about that for this post). Say the characteristic polynomial of $$A$$ is $$\lambda^2+b\lambda+c=0$$, then it is a fact that $$A^2+bA+cI=0$$.

So just as $$e^{rt}$$ is a solution to $$x''+bx'+cx=0$$ if $$r^2+br+c=0$$, we can say that if $$A^2+bA+cI=0$$, then $$e^{At}$$ is a solution to $$\textbf{X}''+b\textbf{X}'+c\textbf{X}=0$$.

Therefore, if we can find our normalized solutions $$Y_1,Y_2$$, then we can use the uniqueness of the solution of the initial value problem \eqref{matrixIVP} to say that

$$\begin{equation} \label{normform}
e^{At}=Y_1(t)I+Y_2(t)A
\end{equation}$$

Again, you may read [the other post](../matrixexpwde){:target="_blank"} if you want to see a more rigorous proof of this.

## Distinct Eigenvalues

Given the differential equation

$$y''+by'+cy=0$$

If $$\lambda^2+b\lambda+c=0$$ has two distinct roots $$\lambda_1,\lambda_2$$, the normalized solutions will be

$$\begin{gather}
Y_1(t)=\frac{\lambda_2e^{\lambda_1t}-\lambda_1e^{\lambda_2t}}{\lambda_2-\lambda_1}\\
Y_2(t)=\frac{e^{\lambda_2t}-e^{\lambda_1t}}{\lambda_2-\lambda_1}
\end{gather}$$

Thus, by \eqref{normform}, we obtain \eqref{form1a}

$$e^{At}=\frac{\lambda_2e^{\lambda_1t}-\lambda_1e^{\lambda_2t}}{\lambda_2-\lambda_1}I +
\frac{e^{\lambda_2t}-e^{\lambda_1t}}{\lambda_2-\lambda_1}A$$

We may then group terms to get \eqref{form1}.

$$e^{At}=\frac{e^{\lambda_2t}(A-\lambda_1I)-e^{\lambda_1t}(A-\lambda_2I)}{\lambda_2-\lambda_1}\quad \blacksquare$$

Note that if $$A$$ is a complex matrix with complex eigenvalues that _are not_ conjugates of each other, then \eqref{form1} will still work and be the best option.

Now for some bonus equations... First, if $$\det(A)$$ is real and strictly less than zero, and $$\operatorname{tr}(A)=0$$, then $$\lambda_1=-\lambda_2=\sqrt{-\det(A)}$$. This simplifies \eqref{form1a} to \eqref{form1b}.

$$\begin{equation}
e^{At}=\cosh(\lambda t)I+\frac{\sinh(\lambda t)}{\lambda}A
\end{equation}$$

If $$A$$ is singular and the other eigenvalue is not also zero, this simplifies to \eqref{form1c}

$$\begin{equation}
e^{At}=I+\frac{e^{\operatorname{tr}(A)t}-1}{\operatorname{tr}(A)}A
\end{equation}$$

The best part of this particular formula is that it actually holds for all square rank-one matrices regardless of size (as long as $$\operatorname{tr}(A)\neq0\;$$!) 

Bonus: Since $$e^{(A+kI)t}=e^{kt}e^{At}$$, then if $$B=A+kI$$ where $$A$$ is a rank one matrix with a nonzero trace, then you can still use the above formula, just multiply by $$e^{kt}$$. That is to say, _any_ matrix which is a scalar matrix ($$kI$$) away from a rank-one matrix (with a nonzero trace) can use this above formula, no matter the size.

## Complex Conjugate Eigenvalues

Given the differential equation

$$y''+by'+cy=0$$

If $$\lambda^2+b\lambda+c=0$$ has complex conjugate roots $$a\pm bi$$, the normalized solutions will be

$$\begin{gather}
Y_1(t)=e^{at}\left(\cos(bt)-\frac{a}{b}\sin(bt)\right)\\
Y_2(t)=\frac{e^{at}}{b}\sin(bt)
\end{gather}$$

Then, by \eqref{normform},

$$e^{At}=e^{at}\left(\cos(bt)-\frac{a}{b}\sin(bt)\right)I
+\frac{e^{at}}{b}\sin(bt)A$$

Factoring out the $$e^{at}$$ and combining like terms, we obtain \eqref{form2a}

$$e^{At}=e^{a  t}\left(\cos(b  t)I+\frac{\sin(b  t)}{b }(A-a  I)\right)$$

And arriving at \eqref{form2b} when we factor out $$\frac{1}{b}$$ from both terms.

$$e^{At}=\frac{e^{at}}{b}\bigg(b\cos(b  t)I+\sin(b  t)(A-a  I)\bigg)$$

## One Defective Eigenvalue

Given the differential equation

$$y''+by'+cy=0$$

If $$\lambda^2+b\lambda+c=0$$ has a repeated root $$\lambda$$, the normalized solutions will be

$$\begin{gather}
Y_1(t)=(1-\lambda t)e^{\lambda t}\\
Y_2(t)=te^{\lambda t}
\end{gather}$$

We use \eqref{normform} to get

$$e^{At}=(1-\lambda t)e^{\lambda t}I+te^{\lambda t}A$$

Factor out $$e^{\lambda t}$$ to get \eqref{form3}

$$\begin{equation}
e^{At}=e^{\lambda t}\left(I+t(A-\lambda I)\right)\quad \blacksquare
\end{equation}$$

An alternate derivation can be done by using that $$(A-\lambda I)^2=0$$, allowing $$e^{At}$$ to be computed directly as \eqref{form3}.

### One Nondefective Eigenvalue

This only occurs when $$A$$ is a scalar matrix, so there's no need to use normalized solutions, but it's also technically a case so it's worth mentioning. So let's say that $$A=\lambda I$$. Then

$$e^{At}=\sum_{n=0}^\infty \frac{(\lambda tI)^n}{n!}$$

$$e^{At}=\sum_{n=0}^\infty \frac{(\lambda t)^n}{n!}I^n$$

$$e^{At}=\left(\sum_{n=0}^\infty \frac{(\lambda t)^n}{n!}\right)I=e^{\lambda t}I$$

Thus, \eqref{form4}

$$e^{\lambda It}=e^{\lambda t}I$$

# Applications

For ways to apply matrix exponentials to solve $$2\times2$$ systems of differential equations, check out [this post](../firstordersystemsquick){:target="_blank"} on solving them like a baller.

Closing Remarks
-

I enjoyed verifying that taking the derivative of these formulas is indeed the same as multiplying by $$A$$.

$$\begin{equation}
\frac{d}{dt}e^{At}=Ae^{At}
\end{equation}$$

If you choose to attempt to do so as well, you will need the Cayley-Hamilton theorem.

Even more fun than that is verifying that substituting $$-t$$ for $$t$$ does in fact give the inverse.

$$\begin{equation}
e^{At}e^{-At}=I\implies e^{-At}=\left(e^{At}\right)^{-1}
\end{equation}$$
