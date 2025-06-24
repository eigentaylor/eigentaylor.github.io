---
layout: page
title: Introduction to Least Squares
date: 2021-10-07
description: How to find the best solution for an inconsistent system
comments: true
importance: 3
category: linear algebra
---

Suppose we have two vectors $$\vec{v},\vec{b}\in\mathbb{R}^n$$

The system

\begin{equation} \label{1}
\vec{v}x=\vec{b}
\end{equation}

in all likelihood has no solution unless $$\vec{b}$$ happens to be a scalar multiple of $$\vec{v}$$. So, let us attempt to find the value of $$x$$ which gives the best approximation.

To measure how accurate our solution is in terms of $$x$$, we can simply deal with the magnitude of the difference between $$\vec{v}x$$ and $$\vec{b}$$. We use the magnitude squared as it makes calculations easier and has no effect on the solution.

\begin{equation} \label{2}
\delta(x)= | \vec{v}x-\vec{b} | ^2
\end{equation}

We can take advantage of the fact that for real vectors,
$$| \vec{v}| ^2=\vec{v}^T\vec{v}$$.
Note also that for real vectors $$\vec{v}^T\vec{b}=\vec{v}\cdot \vec{b}$$.

\begin{gather} \label{3}
|\vec{v}x-\vec{b}|^2=(\vec{v}x-\vec{b})^T(\vec{v}x-\vec{b})\\
\delta(x)=\vec{v}^T\vec{v}x^2-(\vec{v}^T\vec{b}+\vec{b}^T\vec{v})x+\vec{b}^T\vec{b}
\end{gather}

Being $$1\times1$$ matrices, $$\vec{b}^T\vec{v}=\vec{v}^T\vec{b}$$

\begin{equation} \label{4}
\delta(x)=\vec{v}^T\vec{v}x^2-2(\vec{v}^T\vec{b})x+\vec{b}^T\vec{b}
\end{equation}

Solve for $$\delta'(x)=0$$

\begin{equation} \label{5}
\delta'(x)=2\vec{v}^T\vec{v}x-2(\vec{v}^T\vec{b})=0
\end{equation}

\begin{equation} \label{6}
x=\frac{\vec{v}^T\vec{b}}{\vec{v}^T\vec{v}}=\frac{\vec{v}\cdot \vec{b}}{|\vec{v}|^2}
\end{equation}

Look at that! It's the coefficient for the projection of a vector $$\vec{b}$$ onto $$\vec{v}$$. Looks like we were on the right track all along!

If we go back a step and multiply both sidesof \eqref{6} by $$\vec{v}^T\vec{v}$$, we get

\begin{equation} \label{7}
(\vec{v}^T\vec{v})x=\vec{v}^T\vec{b}
\end{equation}

Which is exactly the equation we started with \eqref{1} just with both sides multiplied by $$\vec{v}^T$$. And indeed, the best approximate solution (also called the least squares solution) of an inconsistent system

$$A\vec{x}=\vec{b}$$

is found by instead solving the "normal equation of $$A\vec{x}=\vec{b}$$"

\begin{equation} \label{8}
A^TA\vec{x}=A^T\vec{b}
\end{equation}

One thing to note: $$A^TA$$ will be invertible if and only if the columns of $$A$$ are linearly independent.

## An Application

One of the big applications is linear interpolation, or finding a line of best fit. Let's say we have a list of points $$\{(x_1,y_1),\ldots,(x_n,y_n)\}$$. If we had a line $$y=c_0+c_1x$$ that theoretically passed through all $$n$$ of these points, then that means

$$\begin{gather*}
c_0+c_1x_1=y_1\\
\vdots\\
c_0+c_1x_n=y_n
\end{gather*}$$

Of course, we can express this as s system of equations:

$$\begin{equation}
\begin{bmatrix}1&x_1\\\vdots&\vdots\\1&x_n\end{bmatrix}\begin{bmatrix}c_0\\c_1\end{bmatrix}=\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix}
\end{equation}$$

Let's not be naive. This system probably has no solution. In which case, we can multiply by the transpose of the coefficient matrix to get the normal equation. Do observe that the columns will be linearly independent unless $$x_1=x_2=\ldots=x_n$$ (which would be dumb).

$$\begin{equation}
\begin{bmatrix}1&\dots&1\\x_1&\dots&x_n\end{bmatrix}
\begin{bmatrix}1&x_1\\\vdots&\vdots\\1&x_n\end{bmatrix}\begin{bmatrix}c_0\\c_1\end{bmatrix}=
\begin{bmatrix}1&\dots&1\\x_1&\dots&x_n\end{bmatrix}
\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix}
\end{equation}$$

If we denote the vectors $$\vec{1}=(1,\ldots,1)\in\mathbb{R}^n$$, $$\vec{x}=(x_1,\ldots,x_n)$$, and $$\vec{y}=(y_1,\ldots,y_n)$$, the system becomes

$$\begin{equation}
\begin{bmatrix}n&\vec{1}\cdot\vec{x}\\\vec{1}\cdot\vec{x}&|\vec{x}|^2\end{bmatrix}
\begin{bmatrix}c_0\\c_1\end{bmatrix}=
\begin{bmatrix}\vec{1}\cdot\vec{y}\\\vec{x}\cdot\vec{y}\end{bmatrix}
\end{equation}$$

If you think I'm going to row reduce this, you are out of your mind. Cramer's Rule is bae once again :sunglasses:

$$\begin{equation}
c_0=\frac{\begin{vmatrix}\vec{1}\cdot\vec{y}&\vec{1}\cdot\vec{x}\\\vec{x}\cdot\vec{y}&|\vec{x}|^2\end{vmatrix}}{\begin{vmatrix}n&\vec{1}\cdot\vec{x}\\\vec{1}\cdot\vec{x}&|\vec{x}|^2\end{vmatrix}},\;
c_1=\frac{\begin{vmatrix}n&\vec{1}\cdot\vec{y}\\\vec{1}\cdot\vec{x}&\vec{x}\cdot\vec{y}\end{vmatrix}}{\begin{vmatrix}n&\vec{1}\cdot\vec{x}\\\vec{1}\cdot\vec{x}&|\vec{x}|^2\end{vmatrix}}
\end{equation}$$

And you could always use my [determinant polynomial](../functioninterp/){:target="_blank"} to get the equation for the line of best fit as

$$\begin{equation}
y=\frac{\begin{vmatrix}1&x&0\\n&\vec{1}\cdot\vec{x}&\vec{1}\cdot\vec{y}\\\vec{1}\cdot\vec{x}&|\vec{x}|^2&\vec{x}\cdot\vec{y}\end{vmatrix}}
{n(x_1^2+\ldots+x_n^2)-(x_1+\ldots+x_n)^2}
\end{equation}$$
