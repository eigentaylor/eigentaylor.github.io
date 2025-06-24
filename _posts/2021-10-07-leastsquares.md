---
layout: distill
title: Introduction to Least Squares
date: 2021-10-7
description: How to find the best solution for an inconsistent system
comments: true
importance: 3
categories: linear-algebra
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Intro
  - name: An Application
  - name: Further Questions
---

Note: Updated 09/21/23.

## Intro

Suppose we have two vectors $$\mathbf{v},\mathbf{b}\in\mathbb{R}^n$$

The system

\begin{equation} \label{1}
\mathbf{v}x=\mathbf{b}
\end{equation}

in all likelihood has no solution unless $$\mathbf{b}$$ happens to be a scalar multiple of $$\mathbf{v}$$. So, let us attempt to find the value of $$x$$ which gives the best approximation.

To measure how accurate our solution is in terms of $$x$$, we can simply deal with the magnitude of the difference between $$\mathbf{v}x$$ and $$\mathbf{b}$$. We use the magnitude squared as it makes calculations easier and has no effect on the solution.

$$
\delta(x)= | \mathbf{v}x-\mathbf{b} | ^2
$$

We can take advantage of the fact that for real vectors,
$$| \mathbf{v}| ^2=\mathbf{v}^T\mathbf{v}$$.
Note also that for real vectors $$\mathbf{v}^T\mathbf{b}=\mathbf{v}\cdot \mathbf{b}$$.

$$\begin{gather*}
|\mathbf{v}x-\mathbf{b}|^2=(\mathbf{v}x-\mathbf{b})^T(\mathbf{v}x-\mathbf{b})\\
\delta(x)=\mathbf{v}^T\mathbf{v}x^2-(\mathbf{v}^T\mathbf{b}+\mathbf{b}^T\mathbf{v})x+\mathbf{b}^T\mathbf{b}
\end{gather*}$$

Being $$1\times1$$ matrices, $$\mathbf{b}^T\mathbf{v}=\mathbf{v}^T\mathbf{b}$$

$$
\delta(x)=\mathbf{v}^T\mathbf{v}x^2-2(\mathbf{v}^T\mathbf{b})x+\mathbf{b}^T\mathbf{b}
$$

Solve for $$\delta'(x)=0$$

$$
\delta'(x)=2\mathbf{v}^T\mathbf{v}x-2(\mathbf{v}^T\mathbf{b})=0
$$

\begin{equation} \label{6}
x=\frac{\mathbf{v}^T\mathbf{b}}{\mathbf{v}^T\mathbf{v}}=\frac{\mathbf{v}\cdot \mathbf{b}}{|\mathbf{v}|^2}
\end{equation}

Look at that! It's the coefficient for the projection of a vector $$\mathbf{b}$$ onto $$\mathbf{v}$$. And this should be a relatively intuitive answer to get. We can interpret the question of $$\mathbf{v}x=\mathbf{b}$$ as traveling along the line spanned by $$\mathbf{v}$$, and seeing where we get closest to the vector $$\mathbf{b}$$. And it hopefully makes sense that this should be the projection. I encourage you to draw it out and justify it to yourself!

If we go back a step and multiply both sides of \eqref{6} by $$\mathbf{v}^T\mathbf{v}$$, we get

$$ \label{7}
(\mathbf{v}^T\mathbf{v})x=\mathbf{v}^T\mathbf{b}
$$

Which is exactly the equation we started with \eqref{1} just with both sides multiplied by $$\mathbf{v}^T$$. And indeed, the best approximate solution (also called the least squares solution) of an inconsistent system

$$\mathbf{A}\mathbf{x}=\mathbf{b}$$

is found by instead solving the "normal equation of $$\mathbf{A}\mathbf{x}=\mathbf{b}$$"

$$ \label{8}
\mathbf{A}^T\mathbf{A}\mathbf{x}=\mathbf{A}^T\mathbf{b}
$$
equation
One thing to note: $$\mathbf{A}^T\mathbf{A}$$ will be invertible if and only if the columns of $$\mathbf{A}$$ are linearly independent.

## An Application

One of the big applications is linear interpolation, or finding a line of best fit. Let's say we have a list of points $$\{(x_1,y_1),\ldots,(x_n,y_n)\}$$. If we had a line $$y=c_0+c_1x$$ that theoretically passed through all $$n$$ of these points, then that means

$$\begin{gather*}
c_0+c_1x_1=y_1\\
\vdots\\
c_0+c_1x_n=y_n
\end{gather*}$$

Of course, we can express this as a system of equations:

$$
\begin{bmatrix}1&x_1\\\vdots&\vdots\\1&x_n\end{bmatrix}\begin{bmatrix}c_0\\c_1\end{bmatrix}=\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix}
$$

Let's not be naive. This system probably has no solution. In which case, we can multiply by the transpose of the coefficient matrix to get the normal equation. Do observe that the columns will be linearly independent unless $$x_1=x_2=\ldots=x_n$$ (which would be dumb).

$$
\begin{bmatrix}1&\dots&1\\x_1&\dots&x_n\end{bmatrix}
\begin{bmatrix}1&x_1\\\vdots&\vdots\\1&x_n\end{bmatrix}\begin{bmatrix}c_0\\c_1\end{bmatrix}=
\begin{bmatrix}1&\dots&1\\x_1&\dots&x_n\end{bmatrix}
\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix}
$$

If we denote the vectors $$\mathbf{1}=(1,\ldots,1)\in\mathbb{R}^n$$, $$\mathbf{x}=(x_1,\ldots,x_n)$$, and $$\mathbf{y}=(y_1,\ldots,y_n)$$, the system becomes

$$
\begin{bmatrix}n&\mathbf{1}\cdot\mathbf{x}\\\mathbf{1}\cdot\mathbf{x}&|\mathbf{x}|^2\end{bmatrix}
\begin{bmatrix}c_0\\c_1\end{bmatrix}=
\begin{bmatrix}\mathbf{1}\cdot\mathbf{y}\\\mathbf{x}\cdot\mathbf{y}\end{bmatrix}
$$

If you think I'm going to row reduce this, you are out of your mind. Cramer's Rule is bae once again :sunglasses:

$$
c_0=\frac{\begin{vmatrix}\mathbf{1}\cdot\mathbf{y}&\mathbf{1}\cdot\mathbf{x}\\\mathbf{x}\cdot\mathbf{y}&|\mathbf{x}|^2\end{vmatrix}}{\begin{vmatrix}n&\mathbf{1}\cdot\mathbf{x}\\\mathbf{1}\cdot\mathbf{x}&|\mathbf{x}|^2\end{vmatrix}},\;
c_1=\frac{\begin{vmatrix}n&\mathbf{1}\cdot\mathbf{y}\\\mathbf{1}\cdot\mathbf{x}&\mathbf{x}\cdot\mathbf{y}\end{vmatrix}}{\begin{vmatrix}n&\mathbf{1}\cdot\mathbf{x}\\\mathbf{1}\cdot\mathbf{x}&|\mathbf{x}|^2\end{vmatrix}}
$$

And you could always use my [determinant polynomial](../functioninterp/){:target="_blank"} to get the equation for the line of best fit as

$$
y=\frac{\begin{vmatrix}1&x&0\\n&\mathbf{1}\cdot\mathbf{x}&\mathbf{1}\cdot\mathbf{y}\\\mathbf{1}\cdot\mathbf{x}&|\mathbf{x}|^2&\mathbf{x}\cdot\mathbf{y}\end{vmatrix}}
{n(x_1^2+\ldots+x_n^2)-(x_1+\ldots+x_n)^2}
$$

## Further Questions

Some questions to ponder.

1. Why is $$\mathbf{A}^T\mathbf{A}\mathbf{x}=\mathbf{A}^T\mathbf{b}$$ guaranteed a solution?
2. Why would the solution to the normal equation actually be the "closest" solution?

These are questions I plan to tackle in an updated least squares post soon.
