---
layout: page
title: Solving Second Order Systems of Differential Equations
date: 2021-06-20
description: ye
comments: true
importance: 4
categories: differential-equations
categories: systems-of-differential-equations
---

This was mentioned in my [post about constructing these kind of problems](../secondordersystems){:target="_blank"}, but the good news about these kind of problems is that is that when discussing $$n\times n$$ second order systems such as

$$\begin{equation} \label{sys}
x''+Px'+Qx=0
\end{equation}$$

we are still only really talking about a first order system. We can reduce any second order system to a first order by adding $$n$$  more variables. So if $$x=(x_1,\ldots,x_n)$$ then we let $$y=(x_1,\ldots,x_n,x_1',\ldots,x_n')$$. Which gives us the system

$$\begin{equation} \label{reduction}
y'=\begin{bmatrix}
0&I\\-Q&-P
\end{bmatrix} y
\end{equation}$$

So, **for an $$n\times n$$ system of second order differential equations, there will be $$2n$$ linearly independent solutions.**

In the $$2\times 2$$ case, this tells us that the solutions to our $$2\times 2$$ second order system can have all the behaviors of a $$4\times 4$$ first order system. So we can have an eigenvalue repeated 4 times and get a $$t^3$$ term in our homogeneous solutions, and if $$P,Q$$ are real, then we can have up to two complex conjugate pairs of eigenvalues.

At this point, there are two avenues to solve this problem using techniques you likely have already learned. A more standard one is to find a solution to \eqref{reduction},

$$y=c_1y_1(t)+\ldots+c_{2n}y_{2n}(t)$$

and then saying $$x_i(t)=\begin{bmatrix}
I_n&0
\end{bmatrix}y_i(t)$$. In other words, only take the first $$n$$ entries of the $$y$$ solutions. Another would be

$$\begin{equation} \label{exp1}
x=\begin{bmatrix}
I_n&0
\end{bmatrix}
\exp\left(\begin{bmatrix}
0&I\\-Q&-P
\end{bmatrix}t\right)
\begin{bmatrix}
x(0)\\x'(0)
\end{bmatrix}
\end{equation}$$

giving us a theoretical general solution. But computing large matrix exponentials is arguably harder than just finding the $$y$$ solutions. But even just *computing* the characteristic polynomial of a $$4\times 4$$ matrix can be a huge chore. Luckily, keeping it second order can actually make it easier. The computations are at least easier in my opinion, since the determinant one calculates is half as large. Especially since the computational power required for computing determinants increases factorially.

I have developed an approach to these problems which is very similar to the way one solves linear second order differential equation. And the computations here are far less arduous, in my opinion.

## The Characteristic Polynomial

Like most linear differential equations, we consider a characteristic polynomial, usually derived by supposing a solution of the form $$x=ce^{st}$$. Substituting this into \eqref{sys} gives us

$$\begin{equation} \label{charpoly}
(Is^2+Ps+Q)c=0
\end{equation}$$

We will denote $$L(s)=Is^2+Ps+Q$$. We can then write \eqref{sys} as

$$L(D)x=0$$

where $$D$$ is the differential operator such that $$Dx=x'$$.

If we want our solution to be nontrivial, we assume that $$c\neq 0$$. Therefore, $$Is^2+Ps+Q$$ must have a nontrivial null space. An alternative characterization is that

$$\begin{equation} \label{charpolydet}
\det(Is^2+Ps+Q)=0
\end{equation}$$

We will denote $$p(s)=\det(Is^2+Ps+Q)$$. Fun fact, this $$p(s)$$ is the same characteristic polynomial of the matrix in \eqref{reduction}. This should be no surprise since the problems are equivalent .

This will be a polynomial of degree $$2n$$. So these problems become quite difficult quite quickly. Even just a $$2\times 2$$ system requires solving a quartic polynomial, making it technically the largest system for which we can guarantee being able to find an exact solution. Once we get a $$3\times 3$$, we no longer have a formula to solve the degree $$6$$ polynomial. That said, the quartic formula is ridiculously unwieldy enough to make the case that unless you have some [savvy techniques to guarantee these problems will have have nice solutions](../secondordersystems){:target="_blank"}, they are effectively unsolvable in the general case.

Since these roots are the eigenvalues of the matrix in \eqref{reduction}, we will call them as such. Considering their algebraic and geometric multiplicity is also still indeed useful.

## Obtaining Solutions

Since \eqref{charpoly} is merely an $$n\times n$$ matrix, if a root of the characteristic polynomial is repeated more than $$n$$ times, then it is a clearly defective eigenvalue. More often, however, for a particular root of the characteristic polynomial $$s_i$$, we obtain $$\operatorname{nullity}(L(s_i))=\operatorname{nullity}(Is_i^2+Ps_i+Q)$$ linearly independent solutions vectors and pray that the number we get is equal to the algebraic multiplicity of the eigenvalue.

To get solutions of the form $$x=ve^{s_it}$$, solve the system

$$\begin{equation} \label{eigenvector}
L(s_i)v=0
\end{equation}$$

## Complex Eigenvalues with Real Matrices

This is thankfully exactly the same as the first order case. If $$P$$ and $$Q$$ are real matrices.

Suppose one eigenvalue is $$\lambda+i\mu$$, where $$\lambda,\mu\in\mathbb{R}$$. Then we merely need one complex eigenvector $$v$$ such that $$L(\lambda+i\mu)v=0$$. We will then get two linearly independent solutions

$$\begin{gather}
x_1=\operatorname{Re}(e^{\lambda+i\mu}v)\\
x_2=\operatorname{Im}(e^{\lambda+i\mu}v)
\end{gather}$$

## Defective Eigenvalues

Unfortunately, this is the case which is far more difficult than the first order version. I believe the following method, which is reminiscent of reduction of order, is the most efficient way to do it.

So let us suppose we have a particular eigenvalue $$\lambda$$ which has geometric multiplicity $$g$$ and algebraic multiplicity $$g+m$$ for $$m\geq 1$$. Then we do a substitution

$$\begin{equation}
x(t)=e^{\lambda t}v(t)
\end{equation}$$

It can be verified that if we define

$$L'(s)=2Is+P$$

then \eqref{sys} can be simplified to

$$\begin{equation} \label{reductionoforder}
v''+L'(\lambda)v'+L(\lambda)v=0
\end{equation}$$

We will call this the shifted equation, because this can be viewed from the lens of an exponential shift,

$$L(D)(e^{\lambda t}v)=e^{\lambda t}L(D+\lambda)v$$

and matches with the Taylor series of $$L(x)$$ centered at $$\lambda$$.

To get the rest of the solutions associated with the eigenvalue $$\lambda$$ from \eqref{reductionoforder}, we suppose a solution of the form

$$\begin{equation}
v=c_0+c_1t+\ldots+c_mt^{m}
\end{equation}$$

for vectors $$c_0,\ldots,c_m$$. Substitute into \eqref{reductionoforder} and equate terms with the same power of $$t$$. This means that $$c_m$$ will be some linear combination of the eigenvectors associated with the eigenvalue.

This is consistent with the Obtaining Solutions section, as if the algebraic multiplicity of the eigenvalue is only one, \eqref{reductionoforder} simplifies down to \eqref{eigenvector} $$L(\lambda)v=0$$.

As a tip, always include the homogeneous solution. That way you will get all $$m$$ solutions from the eigenvalue.

## A remark on nonhomogeneous systems

I can't see any better way to solve nonhomogeneous systems than reducing the equation to \eqref{reduction} and solving it as a nonhomogeneous first order system of equations. I haven't experimented with it much, but I can only imagine the Method of Undetermined Coefficients being reasonable.

# Example

$$x''+\begin{bmatrix}2&-2\\2&4\end{bmatrix}x'+\begin{bmatrix}-2&-4\\4&4\end{bmatrix}x=0$$

This is a $$2\times 2$$ system, so we expect $$4$$ linearly independent solutions.

To start, as with all linear constant coefficient differential equations, we examine the characteristic polynomial.

$$\begin{gather*}
L(s)=Is^2+\begin{bmatrix}2&-2\\2&4\end{bmatrix}s+\begin{bmatrix}-2&-4\\4&4\end{bmatrix}\\
L(s)=\begin{bmatrix}s^2+2s-2&-2(s+2)\\2(s+2)&s^2+4s+4\end{bmatrix}\\
L(s)=\begin{bmatrix}s^2+2s-2&-2(s+2)\\2(s+2)&(s+2)^2\end{bmatrix}\\
p(s)=\begin{vmatrix}s^2+2s-2&-2(s+2)\\2(s+2)&(s+2)^2\end{vmatrix}
\end{gather*}$$

We can use determinant properties to simplify things by dividing out $$s+2$$ from the second column and second row.

$$\begin{gather*}
p(s)=(s+2)^2\begin{vmatrix}s^2+2s-2&-2\\2&1\end{vmatrix}\\
p(s)=(s+2)^2(s^2+2s+2)\\
p(s)=(s+2)^2((s+1)^2+1)\\
\end{gather*}$$

The roots of $$p(s)$$ appear to be $$s=-2,-1\pm i$$. Unfortunately $$-2$$ is repeated, but looks to only have one eigenvector. We also have a pair of complex conjugate eigenvalues.

First, we can start by finding the regular eigenvector associated with $$s=-2$$.

$$L(-2)=\begin{bmatrix}-2&0\\0&0\end{bmatrix}$$

An easy basis for the null space of this matrix would be $$(0,1)$$. Therefore, our first solution would be

$$x_1=\begin{bmatrix}0\\1\end{bmatrix}e^{-2t}$$

To get our second solution, we must examine the shifted equation. We definitely could have started with this and obtained both $$x_1$$ and $$x_2$$ at the same time, but I thought I would go through the standard procedure one goes through when finding a solution when the eigenvalue is not defective.

We calculate that

$$L'(s)=\begin{bmatrix}2s+2&-2\\2&2(s+2)\end{bmatrix}$$

Which tells us that

$$L'(-2)=\begin{bmatrix}-2&-2\\2&0\end{bmatrix}$$

So if $$x=ve^{-2t}$$, our shifted equation is

$$v''+\begin{bmatrix}-2&-2\\2&0\end{bmatrix}v'+\begin{bmatrix}-2&0\\0&0\end{bmatrix}v=0$$

The difference between our algebraic and geometric multiplicity is only $$1$$, so we suppose our solution for our $$-2$$ eigenvalue is

$$v=c_0+c_1t$$

Telling us that $$v'=c_1$$ and $$v''=0$$.

Substituting in,

$$\begin{bmatrix}-2&-2\\2&0\end{bmatrix}c_1+\begin{bmatrix}-2&0\\0&0\end{bmatrix}(c_0+c_1t)=0$$

Since all terms must be zero, we can separate the different power of $$t$$ into different equations. This gives us two equations,

$$\begin{gather*}
\begin{bmatrix}-2&0\\0&0\end{bmatrix}c_1=0\\
\begin{bmatrix}-2&-2\\2&0\end{bmatrix}c_1+\begin{bmatrix}-2&0\\0&0\end{bmatrix}c_0=0
\end{gather*}$$

The first equation is very easy. $$c_1=k_1\begin{bmatrix}0\\1\end{bmatrix}$$ (oh hey it's our eigenvector, what a coincidence). Substituting this into the second equation, dividing out the two common to both matrices, and moving the $$c_0$$ matrix to the other side of the equation gives us

$$\begin{bmatrix}1&0\\0&0\end{bmatrix}c_0=\begin{bmatrix}k_1\\0\end{bmatrix}c_1$$

So $$c_0=\begin{bmatrix}k_1\\0\end{bmatrix}+k_0\begin{bmatrix}0\\1\end{bmatrix}$$. Therefore,

$$v=k_0\begin{bmatrix}0\\1\end{bmatrix}+k_1\begin{bmatrix}1\\t\end{bmatrix}$$

Giving us two solutions

$$x=k_0\begin{bmatrix}0\\1\end{bmatrix}e^{-2t}+k_1\begin{bmatrix}1\\t\end{bmatrix}e^{-2t}$$

The first term is just $$x_1$$, so we get our second solution

$$x_2=\begin{bmatrix}1\\t\end{bmatrix}e^{-2t}$$

We will get our last two solutions from our last two eigenvalues $$s=-1\pm i$$. Since these matrices are real, we only need one complex eigenvector, and that will give us two solutions.

So examining $$L(-1+i)$$,

$$L(-1+i)=\begin{bmatrix}-4&-2-2i\\2+2i&2i\end{bmatrix}$$

It can be confirmed that this matrix is singular, and a basis for the null space is $$(1,-1+i)$$.

So now we just need to look at the real and imaginary parts of

$$\begin{bmatrix}1\\-1+i\end{bmatrix}e^{(-1+i)t}$$

Which are

$$\begin{gather*}
x_3=\begin{bmatrix}\cos t\\-\cos t-\sin t\end{bmatrix}e^{-t}\\
x_4=\begin{bmatrix}\sin t\\\cos t-\sin t\end{bmatrix}e^{-t}
\end{gather*}$$

Making our general solution

$$x=c_1\begin{bmatrix}0\\1\end{bmatrix}e^{-2t}+c_2\begin{bmatrix}1\\t\end{bmatrix}e^{-2t}+c_3\begin{bmatrix}\cos t\\-\cos t-\sin t\end{bmatrix}e^{-t}+c_4\begin{bmatrix}\sin t\\\cos t-\sin t\end{bmatrix}e^{-t}$$
