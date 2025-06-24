---
layout: distill
title: Matrix Exponential Formulas for 2x2 Matrices Using Laplace Transforms
date: 2021-04-26
description: this has been rewritten
comments: true
importance: 6
tags: matrix-exponentials
categories: archive
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

**WARNING**: If you are in a differential equations class right now, turn back. This is black magic that your professor _will not_ want you to memorize or use on their tests. These are just cool and/or for the convenience of those who evaluate a lot of matrix exponentials, as I do.

# Formulas

Let $$A$$ be a $$2\times 2$$ matrix.

If $$A$$ has two distinct eigenvalues $$\lambda_1,\lambda_2$$, then

$$\begin{equation} \label{form1}
e^{At}=\frac{e^{\lambda_2t}(A-\lambda_1I)-e^{\lambda_1t}(A-\lambda_2I)}{\lambda_2-\lambda_1}
\end{equation}$$

If $$A$$ has a real determinant, $$\operatorname{tr}(A)=0$$, and $$\det(A)<0$$, then an eigenvalue of $$A$$ is $$\lambda=\sqrt{-\det(A)}$$, and

$$\begin{equation} \label{form1b}
e^{At}=\cosh(\lambda t)I+\frac{\sinh(\lambda t)}{\lambda}A
\end{equation}$$

If $$A$$ is singular and has a nonzero trace,

$$\begin{equation}\label{form1c}
e^{At}=\frac{e^{\operatorname{tr}(A)t}A-(A-\operatorname{tr}(A)I)}{\operatorname{tr}(A)}
\end{equation}$$

If $$A$$ is real and has complex conjugate eigenvalues $$a \pm bi$$, then

$$\begin{equation} 
e^{At}=e^{a  t}\left(\cos(b  t)I+\frac{\sin(b  t)}{b }(A-a  I)\right)
\end{equation}$$

$$\begin{equation} \label{form2}
e^{At}=\frac{e^{at}}{b}\left(b\cos(b  t)I+\sin(b  t)(A-a  I)\right)
\end{equation}$$

If $$A$$ has one defective eigenvalue $$\lambda$$, then

$$\begin{equation} \label{form3}
e^{At}=e^{\lambda t}\left(I+t(A-\lambda I)\right)
\end{equation}$$

And if $$A$$ has only one eigenvalues $$\lambda$$ which is not defective (meaning $$A=\lambda I$$) then

$$\begin{equation} \label{form4}
e^{At}=e^{\lambda t}I
\end{equation}$$

# Proofs

To prove these formulas, we are going to use the Laplace Transform :eyes:

If solving _systems_ of differential equations with the Laplace Transform seems strange, then the intro is probably worth reading. If this is nothing new to you, you can most likely skim the labeled equations.

## Intro

We first use the fact that

$$\begin{equation}
(sI-A)^{-1}=\mathcal{L}\{e^{At}\}
\end{equation}$$

I encourage trying to prove this using the inverse Laplace Transform and the geometric series for matrices. It's cool.

But just to get an idea of where this comes from, observe that if $$A$$ is an $$n\times n$$ constant matrix, then the solution to the system of differential equations

$$
x'=Ax,\quad x(0)=x_0
$$

will be

$$
x=e^{At}x_0
$$

Which is beautifully consistent with the solution to $$y'=ay,\; y(0)=y_0$$ being $$y=y_0e^{at}$$.

If we were to attempt to solve the original system of differential equations using the Laplace Transform (just transforming each entry individually), we would get

$$\begin{gather*}
sX-x_0=AX\\
(sI-A)X=x_0\\
X=(sI-A)^{-1}x_0\\
x=\mathcal{L}^{-1}\{(sI-A)^{-1}\}x_0
\end{gather*}$$

And we can see that $$\mathcal{L}^{-1}\{(sI-A)^{-1}\}$$ is in the place of $$e^{At}$$, so we may use the existence and uniqueness theorem to verify that they are in fact equal.

The second fact we use is that for $$2\times2$$ matrices, $$(sI-A)^{-1}$$ is _really_ easy to calculate.

$$(sI-A)^{-1}=\frac{1}{p(s)}\operatorname{adj}(sI-A)$$

$$\begin{equation} \label{firstlaplace}
(sI-A)^{-1}=\frac{1}{p(s)}(sI+A-\operatorname{tr}(A)I)
\end{equation}$$

where $$p(s)$$ is the characteristic polynomial. The above can be verified by first seeing that $$\operatorname{adj}(sI-A)=sI-\operatorname{adj}(A)$$, and then using

$$A+\operatorname{adj}(A)=\operatorname{tr}(A)I\implies \operatorname{adj}(A)=\operatorname{tr}(A)I-A$$

From this point on, we will abbreviate $$\operatorname{tr}(A)$$ as $$\Sigma$$, due to the fact that the trace is the sum of the eigenvalues $$\operatorname{tr}(A)=\sum\lambda_i$$.

$$\begin{equation}
\Sigma=\lambda_1+\lambda_2
\end{equation}$$

We can then rewrite our original laplace transform \eqref{firstlaplace} as

$$\begin{equation}
(sI-A)^{-1}=\frac{1}{p(s)}(sI+A-\Sigma I)
\end{equation}$$

How we proceed depends on the form of $$p(s)$$.

## Distinct Eigenvalues

If the eigenvalues $$\lambda_1\neq\lambda_2$$, then $$p(s)=(s-\lambda_1)(s-\lambda_2)$$. Calculating the matrix exponential then only requires partial fractions and simplification.

Observe that the solution to

$$\begin{equation}
\frac{b_0+b_1s}{(s-\lambda_1)(s-\lambda_2)}=\frac{x_1}{s-\lambda_1}+\frac{x_2}{s-\lambda_2}
\end{equation}$$

is

$$\begin{equation}
x_1=-\frac{b_0+\lambda_1b_1}{\lambda_2-\lambda_1},\quad x_2=\frac{b_0+\lambda_2b_1}{\lambda_2-\lambda_1}
\end{equation}$$

Is there any reason we can't apply this to our matrix equation above? No! For a hand-wavy justification, just imagine we're doing the above equation for each entry.

$$\begin{equation}
\frac{A-\Sigma I+sI}{(s-\lambda_1)(s-\lambda_2)}=\frac{X_1}{s-\lambda_1}+\frac{X_2}{s-\lambda_2}
\end{equation}$$

We have that $$b_0=A-\Sigma I$$ and $$b_1=I$$. Plugging this into our formula,

$$\begin{equation}
X_1=\frac{\Sigma I-A-\lambda_1 I}{\lambda_2-\lambda_1},\quad X_2=\frac{A-\Sigma I+\lambda_2I}{\lambda_2-\lambda_1}
\end{equation}$$

By our definition of $$\Sigma$$,

$$\begin{equation}
X_1=\frac{\lambda_2 I-A}{\lambda_2-\lambda_1},\quad X_2=\frac{A-\lambda_1I}{\lambda_2-\lambda_1}
\end{equation}$$

Leading us to

$$\begin{equation}
(sI-A)^{-1}=\frac{1}{s-\lambda_1}\left(\frac{\lambda_2 I-A}{\lambda_2-\lambda_1}\right)+\frac{1}{s-\lambda_2}\left(\frac{A-\lambda_1I}{\lambda_2-\lambda_1}\right)
\end{equation}$$

$$\begin{equation}
\mathcal{L}\{e^{At}\}=\frac{1}{s-\lambda_2}\left(\frac{A-\lambda_1I}{\lambda_2-\lambda_1}\right)-\frac{1}{s-\lambda_1}\left(\frac{A-\lambda_2 I}{\lambda_2-\lambda_1}\right)
\end{equation}$$

This is a trivial Inverse Laplace Transform.

$$\begin{equation}
e^{At}=e^{\lambda_2t}\left(\frac{A-\lambda_1I}{\lambda_2-\lambda_1}\right)-e^{\lambda_1t}\left(\frac{A-\lambda_2 I}{\lambda_2-\lambda_1}\right)
\end{equation}$$

We may then simplify to \eqref{form1}.

$$e^{At}=\frac{e^{\lambda_2t}(A-\lambda_1I)-e^{\lambda_1t}(A-\lambda_2I)}{\lambda_2-\lambda_1}\quad \blacksquare$$

Note that if $$A$$ is a complex matrix with complex eigenvalues that _are not_ conjugates of each other, then \eqref{form1} will still work and be the best option.

Now for some bonus equations... First, if $$\det(A)$$ is real and strictly less than zero, and $$\operatorname{tr}(A)=0$$, then $$\lambda_1=-\lambda_2=\sqrt{-\det(A)}$$. This simplifies \eqref{form1} to \eqref{form1b}.

$$\begin{equation}
e^{At}=\cosh(\lambda t)I+\frac{\sinh(\lambda t)}{\lambda}A
\end{equation}$$

Bonus: If $$A$$ is singular and the other eigenvalue is not also zero, this simplifies to \eqref{form1c}

$$\begin{equation}
e^{At}=I+\frac{e^{\operatorname{tr}(A)t}-1}{\operatorname{tr}(A)}A
\end{equation}$$

The best part is that this formula actually holds for all square rank-one matrices regardless of size (as long as $$\operatorname{tr}(A)\neq0\;$$!) Bonus bonus: Since $$e^{(A+kI)t}=e^{kt}e^{At}$$, then if $$B=A+kI$$ where $$A$$ is a rank one matrix with a nonzero trace, then you can still use the above formula, just multiply by $$e^{kt}$$. That is to say, _any_ matrix which is a scalar matrix ($$kI$$) away from a rank-one matrix (with a nonzero trace) can use this above formula, no matter the size.

## Complex Conjugate Eigenvalues

If $$A$$ is real and the eigenvalues of $$A$$ are complex conjugates $$a\pm bi$$, where $$b\neq0$$, then $$p(s)=(s-a)^2+b^2$$ and $$\Sigma=2a$$.

\eqref{firstlaplace} is then

$$\begin{equation}
(sI-A)^{-1}=\frac{sI+A-2a I}{(s-a)^2+b^2}
\end{equation}$$

With foresight into inverse Laplace transforms, we can rewrite this as

$$\begin{equation} 
(sI-A)^{-1}=\frac{(s-a)I+A-a I}{(s-a)^2+b^2}
\end{equation}$$

And we can already take the Laplace transform, actually, but for the sake of completeness we will go one more step.

$$\begin{equation}
\mathcal{L}\{e^{At}\}=\left(\frac{s-a}{(s-a)^2+b^2}\right)I+\frac{1}{b}\left(\frac{b}{(s-a)^2+b^2}\right)(A-a I)
\end{equation}$$

Finally arriving at \eqref{form2} when we factor out $$e^{at}$$ from both terms.

$$\begin{equation}
e^{At}=e^{at}\left(\cos(bt)I+\frac{\sin(bt)}{b}(A-a I)\right)\quad \blacksquare
\end{equation}$$

## One Defective Eigenvalue

If $$A$$ has only one eigenvalue of multiplicity two $$\lambda$$, then $$p(s)=(s-\lambda)^2$$ and $$\Sigma=2\lambda$$.

If $$A$$ is just a scalar matrix, $$A=\lambda I$$, then $$e^{At}=e^{\lambda t}I$$, which isn't very interesting. If $$A$$ is not a scalar matrix, however, then

Substituting into \eqref{firstlaplace},

$$\begin{equation}
(sI-A)^{-1}=\frac{sI+A-2\lambda I}{(s-\lambda)^2}
\end{equation}$$

This simplifies quite nicely into

$$\begin{equation}
(sI-A)^{-1}=\frac{1}{s-\lambda}I+\frac{1}{(s-\lambda)^2}(A-\lambda I)
\end{equation}$$

The inverse Laplace yields exactly \eqref{form3} when we factor out $$e^{\lambda t}$$

$$\begin{equation}
e^{At}=e^{\lambda t}\left(I+t(A-\lambda I)\right)\quad \blacksquare
\end{equation}$$

### One Nondefective Eigenvalue

This only occurs when $$A$$ is a scalar matrix, but it's techinically a case so it's worth mentioning. So let's say that $$A=\lambda I$$. Then

$$e^{At}=\sum_{n=0}^\infty \frac{(\lambda tI)^n}{n!}$$

$$e^{At}=\sum_{n=0}^\infty \frac{(\lambda t)^n}{n!}I^n$$

$$e^{At}=\left(\sum_{n=0}^\infty \frac{(\lambda t)^n}{n!}\right)I=e^{\lambda t}I$$

# Applications

The matrix exponential is incredibly useful in solving systems differential equations, and especially initial value problems.

As we mentioned in the intro, if $$A$$ is an $$n\times n$$ constant matrix, then the solution to the system of differential equations is as such

$$\begin{equation}
x'=Ax,\quad x(0)=x_0\implies x=e^{At}x_0
\end{equation}$$

So to use our formulas, we need only solve the characteristic polynomial. For $$2\times 2$$ matrices, there is the convenient formula

$$\begin{equation}
p(s)=s^2-\operatorname{tr}(A)s+\det(A)
\end{equation}$$

And if you are doing differential equations, you should be able to solve quadratic equations with little effort. Then we use whichever formula applies to the roots. This skips the work of computing eigenvectors entirely. As a bonus, the columns will be the normalized solutions. 

That said If one wishes to go back to the something vaguely of the form

$$x=c_1e^{\lambda_1t}v_1+c_2e^{\lambda_2t}v_2$$

For \eqref{form1}, you can let $$v_1$$ be any basis for the column space of $$A-\lambda_2I$$, and similarly let $$v_2$$ be any basis for the column space of $$A-\lambda_1I$$. This coming directly from the matrices multiplying $$e^{\lambda_it}$$ in \eqref{form1}.

In \eqref{form2} you can let $$v_1$$ and $$v_2$$ be the column of $$e^{At}$$.

The eigenvector $$v_1$$ of $$A$$ in \eqref{form3} can be any basis for the column space of $$A-\lambda I$$. For $$v_2$$, any column of $$e^{At}$$ which has a nonzero term with a $$t$$ on it should suffice.

Closing Remarks
-

I enjoyed verifying that taking the derivative of the first three formulas is the same as multiplying by $$A$$. 

$$\begin{equation}
\frac{d}{dt}e^{At}=Ae^{At}
\end{equation}$$

If you choose to attempt to do so as well, you may need the Cayley-Hamilton theorem.

Even more fun than that is verifying that substituting $$-t$$ for $$t$$ does in fact give the inverse.

$$\begin{equation}
e^{At}e^{-At}=I\implies e^{-At}=\left(e^{At}\right)^{-1}
\end{equation}$$