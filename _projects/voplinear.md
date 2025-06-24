---
layout: page
title: Variation of Parameters Using Linear Algebra
date: 2021-06-24 0
description: linear is best frend :)
comments: true
importance: 4
category: differential equations
---

Consider the differential equation

$$\begin{equation}
y''+p(t)y'+q(t)y=f(t)
\end{equation}$$

Given two linearly independent homogeneous solutions $$y_1(t),y_2(t)$$, we wish to find the general solution. To do this, we are going to reduce this second order linear nonhomogeneous differential equation into a system of first order linear nonhomogeneous differential equations.

We let $$x(t)=(x_1(t),x_2(t))=(y(t),y'(t))$$.

$$\begin{align}
x_1(t)=y(t)&&x_2(t)=&y'(t)\\
x_1'(t)=y'(t)&&x_2'(t)=&y''(t)\\
&&x_2'(t)=&-q(t)y(t)-p(t)y'(t)+f(t)\\
x_1'(t)=x_2(t)&&x_2'(t)=&-q(t)x_1(t)-p(t)x_2(t)+f(t)
\end{align}$$

Then we reduce the original differential equation into

$$\begin{equation}
x'(t)=\begin{bmatrix}0&1\\-q(t)&-p(t)\end{bmatrix}x(t)+\begin{bmatrix}0\\f(t)\end{bmatrix}
\end{equation}$$

If we define

$$A(t)=\begin{bmatrix}0&1\\-q(t)&-p(t)\end{bmatrix},\quad g(t)=\begin{bmatrix}0\\f(t)\end{bmatrix}$$

it becomes

$$\begin{equation}
x'(t)=A(t)x(t)+g(t)
\end{equation}$$

One can confirm that two linearly independent homogeneous solutions are $$x^{(1)}(t)=\begin{bmatrix}y_1(t)\\y_1'(t)\end{bmatrix},\quad x^{(2)}(t)=\begin{bmatrix}y_2(t)\\y_2'(t)\end{bmatrix}$$

based on the assumption that $$y_1,y_2$$ are solutions to the original differential equation.

We then have a *fundamental matrix* $$\Psi(t)=\begin{bmatrix}x^{(1)}(t)&x^{(2)}(t)\end{bmatrix}$$

$$\begin{equation}
\Psi(t)=\begin{bmatrix}y_1(t)&y_2(t)\\y_1'(t)&y_2'(t)\end{bmatrix}
\end{equation}$$

We call this a fundamental matrix because it is an invertible matrix (at least for some point $$t=t_0$$) that has the nifty property that

$$\begin{equation}
\Psi'(t)=A(t)\Psi(t)
\end{equation}$$

Now we define the vector $$u(t)=(u_1(t),u_2(t))$$ for some unknown functions $$u_1(t),u_2(t)$$, and suppose that the general solution to the system is

$$\begin{equation}
x(t)=\Psi(t)u(t)
\end{equation}$$

$$\begin{bmatrix}x_1(t)\\x_2(t)\end{bmatrix}=\begin{bmatrix}y_1(t)&y_2(t)\\y_1'(t)&y_2'(t)\end{bmatrix}\begin{bmatrix}u_1(t)\\u_2(t)\end{bmatrix}$$

Since the solution to our original differential equation is $$y(t)=x_1(t)$$, this equation tells us that

$$\begin{equation}
y(t)=y_1(t)u_1(t)+y_2(t)u_2(t)
\end{equation}$$

Which is exactly what we suppose the solution is when doing variation of parameters!

Take the derivative of $$x(t)$$,

$$x'(t)=\Psi'(t)u(t)+\Psi(t)u'(t)$$

We can simplify the first term using our nifty property,

$$x'(t)=A(t)\Psi(t)u(t)+\Psi(t)u'(t)$$

$$x'(t)=A(t)x(t)+\Psi(t)u'(t)$$

Since $$x'(t)=A(t)x(t)+g(t)$$, clearly we need

$$\Psi(t)u'(t)=g(t)$$

$$\begin{bmatrix}y_1(t)&y_2(t)\\y_1'(t)&y_2'(t)\end{bmatrix}\begin{bmatrix}u_1'(t)\\u_2'(t)\end{bmatrix}=\begin{bmatrix}0\\f(t)\end{bmatrix}$$

And indeed! This is the system of equations one gets when deriving variation of parameters. This is a good sign...

The columns of $$\Psi(t)$$ are linearly independent so it is invertible

$$\begin{equation}
u'(t)=\Psi^{-1}(t)g(t)
\end{equation}$$

$$\begin{bmatrix}u_1'(t)\\u_2'(t)\end{bmatrix}=\begin{bmatrix}y_1(t)&y_2(t)\\y_1'(t)&y_2'(t)\end{bmatrix}^{-1}\begin{bmatrix}0\\f(t)\end{bmatrix}$$

Using the simple formula for the inverse of a $$2\times 2$$ matrix,

$$\begin{bmatrix}u_1'(t)\\u_2'(t)\end{bmatrix}=\frac{1}{y_1(t)y_2'(t)-y_2(t)y_1'(t)}\begin{bmatrix}y_2'(t)&-y_2(t)\\-y_1'(t)&y_1(t)\end{bmatrix}\begin{bmatrix}0\\f(t)\end{bmatrix}$$

Hopefully, you recognize that determinant $$\det(\Psi(t))$$ as the Wronskian, $$W [ y_1(t),y_2(t) ] (t)=y_1(t)y_2'(t)-y_2(t)y_1'(t)$$, which we will just denote as $$W(t)$$.

$$\begin{equation}
\begin{bmatrix}u_1'(t)\\u_2'(t)\end{bmatrix}=\begin{bmatrix}-y_2(t)\\y_1(t)\end{bmatrix}\frac{f(t)}{W(t)}
\end{equation}$$

If you are familiar with the formula for variation of parameters with second-order linear differential equations, hopefully, the pieces of the puzzle seem to be falling into place.

Next, we integrate to get $$u_1$$ and $$u_2$$.

$$\begin{equation}
\begin{bmatrix}u_1(t)\\u_2(t)\end{bmatrix}=
\begin{bmatrix}
\int_{t_0}^t-y_2(s)\frac{f(s)}{W(s)}\,ds\\
\int_{t_0}^ty_1(s)\frac{f(s)}{W(s)}\,ds
\end{bmatrix}
+\begin{bmatrix}c_1\\c_2\end{bmatrix}
\end{equation}$$

These don't *have* to be definite integrals in $$s$$, and indefinite integrals would be totally fine. However, the benefit of doing it this way is that our particular solution will satisfy rest conditions, $$y(t_0)=y'(t_0)=0$$. It doesn't really matter that much, though.

$$\begin{align}
u_1(t)=-&\int_{t_0}^t\frac{y_2(s)}{W(s)}f(s)\,ds+c_1\\
u_2(t)=&\int_{t_0}^t\frac{y_1(s)}{W(s)}f(s)\,ds+c_2
\end{align}$$

Therefore we have derived the formula for variation of parameters!

$$\begin{equation}
y_p(t)=-y_1(t)\int_{t_0}^t\frac{y_2(s)}{W(s)}f(s)\,ds+y_2(t)\int_{t_0}^t\frac{y_1(s)}{W(s)}f(s)\,ds
\end{equation}$$

By doing a definite integral in $$s$$, we can also condense the two integrals into one. The general solution can then be written as

$$\begin{equation}
y(t)=\int_{t_0}^t\frac{y_1(s)y_2(t)-y_2(s)y_1(t)}{y_1(s)y_2'(s)-y_2(s)y_1'(s)}f(s)\,ds+c_1y_1(t)+c_2y_2(t)
\end{equation}$$

This process can absolutely be repeated for higher order equations. The tricky part is calculating $$\Psi^{-1}$$. The good news is that you only need the rightmost column. The entries of those columns will then be the cofactors obtained by covering up the bottom row and one of the other columns. In general, for an $$n$$-th order differential equation, if we denote the cofactor of the entry in the $$i$$-th row and $$j$$-th column of $$\Psi$$ as $$(\Psi)_{ij}$$, then

$$\begin{equation}
u_i'=\frac{(\Psi)_{ni}}{\det(\Psi(t))}f(t)
\end{equation}$$

So basically cover up the bottom row and $$i$$-th column of $$\Psi$$ and take the determinant.
