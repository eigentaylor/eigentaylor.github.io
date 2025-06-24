---
layout: distill
title: Systems of Linear Difference Equations
date: 2021-12-14
description: Like systems of ODEs, but discrete 👀
comments: true
importance: 3
categories: works-in-progress
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Intro
    subsections:
      - name: Solution Behavior
      - name: New Solution Behaviors
  - name: The Best Solution
  - name: Solution Comparison (2x2)
    subsections:
      - name: Nondefective Repeated
      - name: Rank 1
      - name: Defective
      - name: Complex
      - name: Zero Trace
      - name: Singular
      - name: Distinct
---

# Intro

In differential equations, students learn about the system

$$\textbf{x}'(t)=A\textbf{x}(t)$$

But here we will discuss the discrete system

$$\textbf{x}(n+1)=A\textbf{x}(n)$$

Where $$n\in\mathbb{Z}_0^+$$, and instead of a continuous function, we get a discrete set of points

$$\textbf{x}(0),\textbf{x}(1),\ldots,\textbf{x}(n),\ldots$$

## Solution Behavior

With systems of DEs, its the sign of the eigenvalues that tells you the behavior. Negative is asymptotically stable (going to zero), positive is unstable, and zero is statically stable.

However, in these discrete systems, it's the *magnitude*. To understand why, we need to know what our solutions even look like!

With systems of DEs, the basic example is

$$x'(t)=ax(t)$$

Which has the solution $$x(t)=ce^{at}$$. Therefore, its the sign of $$a$$ which determines the behavior. However, with the discrete system

$$x(n+1)=ax(n)$$

the solutions are of the form $$x(t)=ca^n$$. So we still get the behavior of asymptotically stable (going to zero), unstable, and types of static stability, but it's not about the sign anymore, and there are some new types of behavior. I encourage you to try and think about what the differences could be before reading on! It's an interesting thing to try to reason out, in my opinion.

Repeatedly multiplying a number $$a$$ to some nonzero initial number $$c$$ gets big when $$|
a
| > 1$$, goes to zero when $$|a|<1$$, and has a consistent magnitude when $$|a|=1$$.

But the similarities don't stop there. The solutions are still generally obtained by finding eigenvectors and eigenvalues, just like with DE systems. But instead of having solutions of the form $$\textbf{x}(t)=ce^{\lambda t}\textbf{v}$$, they are of the form $$\textbf{x}(n)=c\lambda^n\textbf{v}$$.

### New Solution Behaviors

That said, there are type of behavior fpr discrete systems which does not occur for systems of ODEs. Specifically, if $$a\leq0$$.

When $$a<0$$, our solution is $$(-a)^n=(-1)^na^n$$, giving us an alternating pattern where each iteration flips its sign. This creates a sense of bouncing back and forth. With $$a<-1$$, it's bouncing back and forth with ever increasing magnitude. With $$-1<a<0$$, it's bouncing back and forth towards the origin. And if $$a=-1$$, it's simply bouncing back and forth without getting closer or further away.

When $$a=0$$, solutions of this type start constant, and then immediately disappear after finitely many iterations. For this reason, it is convenient to explicitly  define the function $$0^x$$ in the following way

$$\begin{equation}
0^x=\begin{cases}1,&x=0\\0,&x\neq0\end{cases}
\end{equation}$$

Now, I am not saying that $$0^0=1$$ always. It is indeed an indeterminate form. However, for our purposes, everything is simply cleaner if we take that as fact. Notice that we make the same assumption when we choose to write $$e^x$$ as $$e^x=\sum_{n=0}^\infty\frac{x^n}{n!}$$ rather than $$e^x=1+\sum_{n=1}^\infty\frac{x^n}{n!}$$.

I know which one I prefer. :unamused:

Either way, the most interesting similarity, in my opinion, is the analog for the matrix exponential.

# The Best Solution

In the system

$$\textbf{x}'(t)=A\textbf{x}(t)$$

the best general solution, though not always the most ideal to find, is

$$\textbf{x}(t)=e^{At}\textbf{x}(0)$$

Similarly, for the system

$$\textbf{x}(n+1)=A\textbf{x}(n)$$

the best general solution is

$$\textbf{x}(n)=A^n\textbf{x}(0)$$

Now, this is the coolest part, in my opinion.

There are formulas for $$A^n$$ which look nearly *identical* to the formulas for [Matrix Exponentials](../2x2ezmatrixexp/){:target="_blank"} that I found. I will compare them here, but first! I would like to let you in on how I found them. I used the method described in [that matrix exponential post](../2x2ezmatrixexp/#another-approach). Basically, if the characteristic polynomial is $$s^2=p_0+p_1s$$, solve

$$
\begin{pmatrix}
x(n+1)\\y(n+1)
\end{pmatrix}=
\begin{pmatrix}
0&p_0\\1&p_1
\end{pmatrix}
\begin{pmatrix}
x(n)\\y(n)
\end{pmatrix},\quad
\textbf{x}(0)=
\begin{pmatrix}
1\\0
\end{pmatrix}
$$

Then $$A^n=x(n)I+y(n)A$$ (for 2x2s!). This does generalize, and I will at some point make a post about that.

Theoretically, I'm fairly certain you can achieve the same results by solving for the [normalized solutions](/math/normalized){:target="_blank"} of the linear difference equation

$$a_{n+2}-p_1a_{n+1}-p_0a_n=0$$

# Solution Comparison (2x2)

$$\begin{array}{cccccccc}
\textbf{x}'(t)&=&A\textbf{x}(t)&\implies&\textbf{x}(t)&=&e^{At}\textbf{x}(0)\\
\textbf{x}(n+1)&=&A\textbf{x}(n)&\implies&\textbf{x}(n)&=&A^n\textbf{x}_0
\end{array}$$

The following two are quite simple, and we actually used them to find the matrix exponential formula.

## Nondefective Repeated

This occurs when $$A=kI$$.

$$\begin{array}{ccc}
e^{kIt}&=&e^{kt}I\\
(kI)^n&=&k^nI
\end{array}$$

## Rank 1

If $$A$$ is any square matrix of rank one that also has a nonzero trace.

$$\begin{array}{ccccc}
e^{At}&=&\frac{e^{\operatorname{tr}(A)t}A-(A-\operatorname{tr}(A)I)}{\operatorname{tr}(A)}&=&I+\frac{e^{\operatorname{tr}(A)t}-1}{\operatorname{tr}(A)}A\\
A^n&=&\frac{\operatorname{tr}(A)^nA-0^n(A-\operatorname{tr}(A)I)}{\operatorname{tr}(A)}&=&0^nI+\frac{\operatorname{tr}(A)^n-0^n}{\operatorname{tr}(A)}A
\end{array}$$

As you can see, defining $$0^n$$ as we did makes things very convenient, and allows us to take advantage of the underlying similarities between the two system types.

## Defective

If $$A$$ is any $$2\times2$$ matrix with a defective eigenvalue $$k\neq0$$,

$$\begin{array}{ccc}
e^{At}&=&e^{kt}\bigg(I+t\big(A-kI\big)\bigg)\\
A^n&=&k^n\bigg(I+\frac{n}{k}\big(A-kI\big)\bigg)
\end{array}$$

If $$k=0$$, then the solution is kind of... disturbing.

$$\begin{array}{ccc}
e^{At}&=&I+tA\\
A^n&=&0^nI+0^{n-1}A
\end{array}$$

But looking at it, it does *actually* work. At $$n=0$$ it's $$I$$, and at $$n=1$$ it's $$A$$, and then its zero ever after. Which is indeed what happens with this kind of matrix (nilpotent). I'm not writing $$0^n(I+0^{-1}A)$$, though. This is clearly not a case where we can use regular exponent rules.

## Complex

If $$A\in\mathbb{R}^{2\times2}$$ has complex eigenvalues $$a\pm bi=re^{\pm i\theta}$$, then

$$\begin{align*}
e^{At}=&e^{at}\bigg(\cos(bt)I+\frac{\sin(bt)}{b}\big(A-aI\big)\bigg)\\
A^n=&r^n\bigg(\cos(\theta n)I+\frac{\sin(\theta n)}{b}\big(A-aI\big)\bigg)
\end{align*}$$

## Distinct

If $$A$$ has two distinct eigenvalues $$\lambda_1,\lambda_2$$, then

$$\begin{align*}
e^{At}=&\frac{e^{\lambda_2t}(A-\lambda_1I)-e^{\lambda_1t}(A-\lambda_2I)}{\lambda_2-\lambda_1}\\
A^n=&\frac{\lambda_2^n(A-\lambda_1I)-\lambda_1^n(A-\lambda_2I)}{\lambda_2-\lambda_1}
\end{align*}$$
