---
layout: page
title: Matrix Exponentials Using Differential Equations
date: 2021-09-13 0
description: ok
comments: true
importance: 3
category: systems of differential equations
---

Yet another impractical way to calculate matrix exponentials found by yours truly. This method requires

1. Finding the characteristic/minimal polynomial (and its roots)
2. Calculating powers of the matrix
3. Finding solutions to a linear constant coefficient differential equation for which you know the roots of the characteristic polynomial
4. Finding the [normalized solutions](../normalized/){:target="_blank"} of said differential equation

You may wonder why you would ever use this method when finding the eigenvectors requires fewer steps. However, it does somewhat simplify the cases of defective and complex eigenvalues, and changes the computation into one that is more familiar and approachable. In short: more easier steps.

EDIT 12/8/21: This is actually very convinient for $$2\times2$$ matrices. [For more details.](../2x2ezmatrixexp/){:target="_blank"}

---

Suppose $$A$$ is an $$n\times n$$ matrix and $$p(t)=\det(tI-A)$$ is its minimal polynomial.

Next given that $$Y_1(t),\ldots,Y_n(t)$$ are the solutions to the linear constant coefficient differential equation $$p(D)y=0$$ such that the Wronskian $$W[Y_1,\ldots,Y_n] (t)$$ evaluated at $$t=0$$ is the identity matrix, where $$D$$ is the differential operator such that $$Dy=y'$$. That is to say $$Y_1(t),\ldots,Y_n(t)$$ are the [normalized solutions](../normalized/){:target="_blank"} of $$p(D)y=0$$.

It follows then that

$$\begin{equation}
e^{At}=\sum_{k=1}^nY_k(t)A^{k-1}
\end{equation}$$

### Proof:

Assuming the givens above, let

$$\begin{align}
\Psi(t)&=\sum_{k=1}^nY_k(t)A^{k-1}\\
\Phi(t)&=e^{At}
\end{align}$$

Because $$Y_1(t),\ldots,Y_n(t)$$ are all solutions to $$p(D)y=0$$, by linearity $$\Psi(t)$$ is also a solution $$p(D)\Psi(t)=0$$.

It follows that because $$W[Y_1,\ldots,Y_n] (0)=I$$, we have that for $$0\leq m< n$$

$$Y_k^{(m)}(0)=
\begin{cases}
1,&m=k-1\\
0,&m\neq k-1
\end{cases}$$

Therefore, $$\Psi(t)$$ also solves the initial value problem

$$\begin{equation}
p(D)\Psi=0,\quad \Psi(0)=I,\Psi'(0)=A,\ldots,\Psi^{(n-1)}(0)=A^{n-1}
\end{equation}$$

Essentially, we are talking about $$n^2$$ initial value problems, and just putting all of them into a matrix.

Next we examine $$\Phi(t)=e^{At}$$.

$$\Phi'(t)=Ae^{At}=A\Phi(t)$$. It immediately follows that

$$\begin{equation}\label{mth}
\Phi^{(m)}(t)=A^m\Phi(t)
\end{equation}$$

Alternatively, one can write this as $$D^m\Phi(t)=A^m\Phi(t)$$. By linearity, this then implies that

$$\begin{equation}
p(D)\Phi(t)=p(A)\Phi(t)
\end{equation}$$

By the Cayley-Hamilton theorem, $$p(A)=0$$. So $$\Phi(t)$$ is a solution to $$p(D)\Phi=0$$.

The fact that $$\Phi(0)=I$$ along with \eqref{mth} implies $$\Phi^{(m)}(0)=A^m$$.

Therefore, $$\Phi(t)$$ is also a solution to the initial value problem

$$\begin{equation}
p(D)\Phi=0,\quad \Phi(0)=I,\Phi'(0)=A,\ldots,\Phi^{(n-1)}(0)=A^{n-1}
\end{equation}$$

By the Existence and Uniqueness theorem, $$\Phi$$ and $$\Psi$$ must be the same. Therefore,

$$\begin{equation}
e^{At}=\sum_{k=1}^nY_k(t)A^{k-1}\quad \blacksquare
\end{equation}$$

We can invoke the Existence and Uniqueness theorem for each of the $$n^2$$ intial value problems, so this is valid.

### Example

Take the matrix $$A=\begin{bmatrix}1&-1&0\\1&0&-1\\0&1&-1\end{bmatrix}$$.

We can find its characteristic polynomial with the formula $$p(t)=\lambda^3-\operatorname{tr}(A)\lambda^2+(C_{11}+C_{22}+C_{33})\lambda-\det(A)$$ (where $$C_{ij}$$ is the cofactor of the $$ij$$ entry of $$A$$). With a trace and determinant of zero, and the cofactors adding up to 1, we obtain.

$$\lambda^3+\lambda=0$$

We now examine the differential equation with this characteristic polynomial:

$$y'''+y'=0$$

Factoring the characteristic polynomial gives us the roots $$\lambda=0,\pm i$$. Therefore, a fundamental set of solutions is given by

$$y_1=1,y_2=\cos(t),y_3=\sin(t)$$

To find the normalized solutions at a given point $$t=t_0$$, we may use the nifty property that

$$\begin{equation}
W[y_1,\ldots,y_n] (t)W[y_1,\ldots,y_n]  (t_0)^{-1}=W[Y_1,\ldots,Y_n] (t)
\end{equation}$$

For our problem,

$$W[y_1,y_2,y_3] (t)=\begin{bmatrix}1&\cos(t)&\sin(t)\\0&-\sin(t)&\cos(t)\\0&-\cos(t)&-\sin(t)\end{bmatrix}$$

And

$$W[y_1,y_2,y_3] (0)=\begin{bmatrix}1&1&0\\0&0&1\\0&-1&0\end{bmatrix}
\implies
W[y_1,y_2,y_3](0)^{-1} =\begin{bmatrix}1&0&1\\0&0&-1\\0&1&0\end{bmatrix}$$

Therefore,

$$\begin{bmatrix}1&\cos(t)&\sin(t)\\0&-\sin(t)&\cos(t)\\0&-\cos(t)&-\sin(t)\end{bmatrix}\begin{bmatrix}1&0&1\\0&0&-1\\0&1&0\end{bmatrix}=W[Y_1,\ldots,Y_n] (t)$$

$$\begin{bmatrix}1&\sin(t)&1-\cos(t)\\0&\cos(t)&\sin(t)\\0&-\sin(t)&\cos(t)\end{bmatrix}=W[Y_1,\ldots,Y_n] (t)$$

The first row gives us the normalized solutions themselves, making them

$$Y_1=1,Y_2=\sin(t),Y_3=1-\cos(t)$$

Then, according to my derivation, we should find that

$$e^{At}=1I+\sin(t)A+(1-\cos(t))A^2$$

$$e^{At}=I+\sin(t)\begin{bmatrix}1&-1&0\\1&0&-1\\0&1&-1\end{bmatrix}+(1-\cos(t)\begin{bmatrix}0&-1&1\\1&-2&1\\1&-1&0\end{bmatrix}$$

$$e^{At}=\begin{bmatrix}1+\sin(t)&-1-\sin(t)+\cos(t)&1-\cos(t)\\1+\sin(t)-\cos(t)&-1+2\cos(t)&1-\sin(t)-\cos(t)\\1-\cos(t)&-1+\sin(t)+\cos(t)&1-\sin(t)\end{bmatrix}$$

Which is indeed the correct answer!

As a side note, one may also utilize $$W[y_1,\ldots,y_n]  (t_0)^{-1}$$ to separate the parts by the original fundamental set of solutions rather than the normalized one.

So for our example,

$$W[y_1,y_2,y_3] (0)^{-1}=\begin{bmatrix}1&0&1\\0&0&-1\\0&1&0\end{bmatrix}$$

The first row of $$W[y_1,y_2,y_3]  (0)^{-1}$$ was $$(1,0,1)$$ telling us that the part of $$e^{At}$$ multiplied by $$y_1=1$$ is $$I+A^2$$.

The second row being $$(0,0,-1)$$ tells us that the part of $$e^{At}$$ multiplied by $$y_2=\cos(t)$$ is $$-A^2$$.

Finally, the third row is $$(0,1,0)$$, so the part of $$e^{At}$$ multiplied by $$\sin(t)$$ is simply $$A$$.

This is my preferred way to calculate it, since the combining of like terms is done beforehand.

### Another example

Suppose that $$A=\begin{bmatrix}0&2&-1\\-1&3&-1\\0&1&0\end{bmatrix}$$.

The characteristic polynomial is $$\lambda^3-3\lambda^2+3\lambda-1=(\lambda-1)^3$$. Which unfortunately means we have a defective eigenvalue.

However, we don't need to worry ourselves with generalized eigenvectors. Instead, we find our fundamental set of solutions to the differential equation

$$y'''-3y''+3y'-y=0$$

Since we know the characteristic polynomial factors into $$(\lambda-1)^3$$, we know we have a repeated root giving the set of solutions

$$y_1=e^t,y_2=te^t,y_3=t^2e^t$$

The Wronskian of those solutions is

$$W[y_1,y_2,y_3] (t)=\begin{bmatrix}e^t&te^t&t^2e^t\\e^t&(t+1)e^t&(t^2+2t)e^t\\e^t&(t+2)e^t&(t^2+4t+2)e^t\end{bmatrix}$$

$$W[y_1,y_2,y_3] (t)=e^t\begin{bmatrix}1&t&t^2\\1&t+1&t^2+2t\\1&t+2&t^2+4t+2\end{bmatrix}$$

evaluating the Wronskian at $$t=0$$

$$W[y_1,y_2,y_3] (0)=\begin{bmatrix}1&0&0\\1&1&0\\1&2&2\end{bmatrix}
\implies W[y_1,y_2,y_3] (0)^{-1}=\begin{bmatrix}1&0&0\\-1&1&0\\\frac{1}{2}&-1&\frac{1}{2}\end{bmatrix}$$

We now read the rows of $$W[y_1,y_2,y_3] (0)^{-1}$$ to get $$e^{At}$$:

$$e^{At}=e^tI+te^t(A-I)+t^2e^t\left(\frac{1}{2}I-A+\frac{1}{2}A^2\right)$$

$$e^{At}=e^t\left(I+t(A-I)+\frac{1}{2}t^2\left(I-2A+A^2\right)\right)$$

$$e^{At}=e^t\left(I+t(A-I)+\frac{1}{2}t^2\left(A-I\right)^2\right)$$

Computing $$A^2$$ to be $$A^2=\begin{bmatrix}-2&5&-2\\-3&6&-2\\-1&3&-1\end{bmatrix}$$, we evaluate the following

$$\begin{align*}
I&=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}\\
A-I&=\begin{bmatrix}-1&2&-1\\-1&2&-1\\0&1&-1\end{bmatrix}\\
\frac{1}{2}(A-I)^2&=\frac{1}{2}\begin{bmatrix}-1&-2&0\\-1&1&0\\-1&1&0\end{bmatrix}
\end{align*}$$

Adding it all up we obtain

$$e^{At}=e^t\begin{bmatrix}1-t-\frac{1}{2}t^2&2t-t^2&-t\\-t-\frac{1}{2}t^2&1+2t+\frac{1}{2}t^2&-t\\-\frac{1}{2}t^2&t+\frac{1}{2}t^2&1-t\end{bmatrix}$$
