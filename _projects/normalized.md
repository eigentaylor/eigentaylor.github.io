---
layout: page
title: Solving Multiple Initial Value Problems with Normalized Solutions
date: 2021-02-10
description: Solve one, solve them all.
comments: true
importance: 3
category: differential equations
---

When would this technique be useful?
=

If you know you will be working with one specific differential equation with many different initial conditions, this technique will remove the need to solve more than the homogeneous solution, and merely requires finding a matrix inverse.

Normalized Solutions
=

Less important is the equation than the solution.

$$\begin{gather} \label{ivp}
L[y]=0,\quad y(t_0)=y_0,\ldots,y^{(n-1)}(t_0)=y^{(n-1)}_0\\
y=c_1y_1+\ldots+c_ny_n
\end{gather}$$

In the case that the differential equation is nonhomogeneous, one may use the convolution or any other technique to get a $$y_p$$ such that $$y_p(t_0)=y_p'(t_0)=\ldots=y_p^{(n-1)}(t_0)=0$$ and simply add it at the end.

To use the technique, we construct the matrix

$$\begin{equation}
W(t)=
\begin{bmatrix}
y_1(t)&\dots&y_n(t)\\
\vdots&\ddots&\vdots\\
y_1^{(n-1)}(t)&\dots&y_n^{(n-1)}(t)
\end{bmatrix}
\end{equation}$$

And define the following vectors:

$$\begin{gather}
\vec{y}(t)=
\begin{bmatrix}
y_1(t)\\\vdots\\y_n(t)
\end{bmatrix}\\
\vec{y}_0=
\begin{bmatrix}
y_0\\\vdots\\y^{(n-1)}_0
\end{bmatrix}
\end{gather}$$

The solution to any initial value problem is then

$$\begin{equation}
y=\vec{y}(t)^TW(t_0)^{-1}\vec{y}_0
\end{equation}$$

More specifically, each entry $$Y_i$$ of $$\vec{y}(t)^TW(t_0)^{-1}$$ will be a solution to the initial value problem,

$$\begin{gather*}
L[y]=0\\
y(y_0)=\ldots=y^{(i-2)}(t_0)=y^{(i)}(t_0)=\ldots=y^{(n-1)}(t_0)=0\\
y^{(i-1)}(t_0)=1
\end{gather*}$$

More simply, each normalized solution is obtained by considering each column of $$W(t_0)^{-1}$$ to be its coordinate vector in therms of the basis $$\{y_1,\ldots,y_n\}$$.

Therefore, the solution to \eqref{ivp} will be

$$\begin{equation}
y=y_0Y_1+y'_0Y_2+\ldots+y^{(n-1)}_0Y_n
\end{equation}$$

This makes solving any initial value problem trivial. We just change the coefficients to the initial conditions and we're done.

This, of course, would be a waste of time if we only had to solve one equation. But given an extensive list of initial value problems with the same differential equation, this is well worth the effort so that we don't have to solve a system of equations *every time*.

A Big-Brain Remark On Autonomous Equations:
-

Note that for an autonomous equation, (i.e. constant coefficients), if $$t_0\neq 0$$, then we can still use

$$\begin{equation}
y=\vec{y}(t-t_0)^TW(0)^{-1}\vec{y}_0
\end{equation}$$

which is of great help because $$W(t_0)$$ for $$t\neq0$$ is usually an algebraic nightmare, while $$W(0)$$ is quite nice most of the time.

Without Linear Algebra
-

If finding the inverse of a matrix intimidates you, then instead suppose

$$\begin{equation}
Y_i=k_1y_1+\ldots+k_ny_1
\end{equation}$$

and solve $$n$$ systems of equations of the form

$$\begin{gather*}
k_1y_1(t_0)+\ldots+k_ny_n(t_0)=0\\
\vdots\\
k_1y_1^{(i-1)}(t_0)+\ldots+k_ny_n^{(i-1)}(t_0)=1\\
\vdots\\
k_1y_1^{(n-1)}(t_0)+\ldots+k_ny_n^{(n-1)}(t_0)=0\\
\end{gather*}$$

for $$1\leq i\leq n$$. If $$n>3$$ however, it would be faster to learn how to invert a matrix than it would be to solve all those systems.

An Example
-

Suppose we need to solve the two initial value problems,

$$\begin{align}
y'''+2y''+y'+2y&=0,&y(1)&=\ln(2),&y'(1)&=e^{-420\pi},&y''(1)&=\cos(69)\\
y'''+2y''+y'+2y&=0,&y(\sqrt{\pi} )&=5^{\ln(3)},&y'(\sqrt{\pi} )&=\sqrt{666},&y''(\sqrt{\pi} )&=(27)^{4/5}\\
\end{align}$$

No thank you, am I right? Well, if we find normalized solutions it won't  be that bad.

First we solve the homogeneous equation to get the solution

$$\begin{equation}
y=c_1e^{-2t}+c_2\cos(t)+c_3\sin(t)
\end{equation}$$

$$W(0)$$ is then

$$\begin{equation}
W(0)=
\begin{bmatrix}
1&1&0\\
-2&0&1\\
4&-1&0\\
\end{bmatrix}
\end{equation}$$

Next we invert the matrix,

$$\begin{equation}
W(0)^{-1}=
\frac{1}{5}
\begin{bmatrix}
1&0&1\\
4&0&-1\\
2&5&2
\end{bmatrix}
\end{equation}$$

And... that's enough to solve both problems. We compute $$\vec{y}(t-t_0)^TW(0)^{-1}$$ (i.e. get the coordinates from the columns):

$$\begin{align*}
Y_1&=\frac{1}{5}[e^{-2(t-t_0)}+4\cos(t-t_0)+2\sin(t-t_0)]\\
Y_2&=\sin(t-t_0)\\
Y_3&=\frac{1}{5}[e^{-2(t-t_0)}-\cos(t-t_0)+2\sin(t-t_0)]\\
\end{align*}$$

And the two solutions are as follows:

$$\begin{align*}
y=&
\frac{\ln(2)}{5}[e^{-2(t-1)}+4\cos(t-1)+2\sin(t-1)]\\
&+e^{-420\pi}\sin(t-1)\\
&+\frac{\cos(69)}{5}[e^{-2(t-1)}-\cos(t-1)+2\sin(t-1)]
\end{align*}$$

and

$$\begin{align*}
y=&
\frac{5^{\ln(3)}}{5}[e^{-2(t-\sqrt{\pi} )}+4\cos(t-\sqrt{\pi} )+2\sin(t-\sqrt{\pi} )]\\
&+\sqrt{666}\sin(t-\sqrt{\pi} )\\
&+\frac{(27)^{4/5}}{5}[e^{-2(t-\sqrt{\pi} )}-\cos(t-\sqrt{\pi} )+2\sin(t-\sqrt{\pi} )]
\end{align*}$$

Proof
-

Consider the function

$$\begin{equation}
y(t)=\vec{y}(t)^TW(t_0)^{-1}\vec{y}_0
\end{equation}$$

where

$$\begin{gather}
\vec{y}(t)=
\begin{bmatrix}
y_1(t)\\\vdots\\y_n(t)
\end{bmatrix}\\
\vec{y}_0=
\begin{bmatrix}
y_0\\\vdots\\y^{(n-1)}_0
\end{bmatrix}\\
W(t)=
\begin{bmatrix}
y_1(t)&\dots&y_n(t)\\
\vdots&\ddots&\vdots\\
y_1^{(n-1)}(t)&\dots&y_n^{(n-1)}(t)
\end{bmatrix}
\end{gather}$$

Notice that 

$$\begin{equation}
\vec{y}(t)=W(t)^T\vec{e}_1\implies \vec{y}(t)^T=\vec{e}^T_1W(t)
\end{equation}$$

where $$\vec{e}_i$$ is the $$i$$-th standard basis vector.

By linearity,

$$\begin{equation}
\vec{y}^{(i)}(t)=
\begin{bmatrix}
y_1^{(i)}(t)\\\vdots\\y_n^{(i)}(t)
\end{bmatrix}
\end{equation}$$

which implies

$$\begin{equation}
\vec{y}^{(i)}(t)=W(t)^T\vec{e}_{i+1}\implies \vec{y}^{(i)}(t)^T=\vec{e}^T_{i+1}W(t)
\end{equation}$$

Additionally, since $$W(t_0)$$ and $$\vec{y}_0$$ are constant,

$$\begin{equation}
y^{(i)}(t)=\vec{y}^{(i)}(t)^TW(t_0)^{-1}\vec{y}_0
\end{equation}$$

Consider $$y^{(i)}(t_0)$$,

$$\begin{equation}
y^{(i)}(t_0)=\vec{y}^{(i)}(t_0)^TW(t_0)^{-1}\vec{y}_0
\end{equation}$$

$$\begin{equation}
y^{(i)}(t_0)=\vec{e}^T_{i+1}W(t_0)W(t_0)^{-1}\vec{y}_0
\end{equation}$$

$$\begin{equation}
y^{(i)}(t_0)=\vec{e}^T_{i+1}\vec{y}_0
\end{equation}$$

$$\begin{equation}
y^{(i)}(t_0)=y_0^{(i)}
\end{equation}$$

Therefore, the function $$y(t)$$ satisfies the conditions

$$y(t_0)=y_0,\ldots,y^{(n-1)}(t_0)=y^{(n-1)}_0\quad \blacksquare$$