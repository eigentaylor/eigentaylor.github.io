---
layout: page
title: Eigendecomposition of Real Matrices with Complex Eigenvalues
date: 2021-04-20
description: An attempt at an intuitive derivation.
comments: true
importance: 5
categories: linear-algebra
---

This works for any real square matrix with dimension 2 or greater, but we will focus on the $$2\times 2$$ case first. Then we will look at how to apply that case to matrices of higher dimension using block matrices.

The $$2\times 2$$ Case

Let us suppose we have a real $$2\times 2$$ matrix $$A$$ with complex eigenvalue $$\lambda=a+ib$$ where $$a,b\in\mathbb{R}$$ and $$b\neq 0$$. By definition, that means there exists a nonzero vector $$v$$ such that

\begin{equation} \label{eig}
Av=(a+ib)v
\end{equation}

Note that it is necessary that the real and imaginary parts of $$v$$ are both nonzero, since otherwise, after dividing out any common complex scalars, the left side would be purely real and the right side would have a nonzero imaginary part, leading to a contradiction. 

We will therefore define $$v$$ as

\begin{equation}
v=u+iw
\end{equation}

where $$u,w\in\mathbb{R}^2$$. 

As an aside, note that if we take the conjugate of both sides of \eqref{eig}, using the fact that because $$A$$ is real, $$\bar{A}=A$$

\begin{equation}
A\bar{v}=\overline{(a+ib)}\bar{v}
\end{equation}

\begin{equation}
A(u-iw)=(a-ib)(u-iw)
\end{equation}

$$\lambda=a-ib$$ is then the other eigenvalue of $$A$$, and its eigenvector is $$u-iw$$. That is to say, the other eigenvector and eigenvalue are both simply the conjugates of the original eigenvalue and eigenvector. 

Pro tip: once you find one complex eigenvector/eigenvalue of a real matrix, you've already found the eigenvector of the other complex eigenvalue. Don't do the same work twice.

Substituting into \eqref{eig} yields

\begin{equation} \label{eig2}
Au+iAw=(au-bw)+i(bu+aw)
\end{equation}

Since the real and imaginary parts of both sides of this equation are all real, we can equate them.

$$\begin{align} \label{basis1}
Au&=au-bw\\
Aw&=bu+aw \label{basis2}
\end{align}$$

If $$u$$ and $$w$$ happen to form a basis (which they do), then knowing how $$A$$ acts on it is sufficient to decompose it. Firstly, to prove they form a basis, suppose that $$u$$ and $$w$$ are linearly dependent. Then there exist constants $$c_1,c_2$$ not both zero such that

$$c_1u+c_2w=0$$

Since both $$u,w$$ are nonzero vectors, either both constants are zero or both are nonzero. Since not both of them are zero, both would have to be nonzero. We could then define the real scalar $$k=-\frac{c_1}{c_2}$$ implying $$w=ku\implies v=(1+ik)u$$. Substituting this into \eqref{eig} gives

$$(1+ki)(Au)=(a+ib)(1+ik)u$$

$$Au=(a+ib)u$$

Since both $$A$$ and $$u$$ are real, the imaginary part of the left side is zero. The imaginary part of the right side is not zero however, since both $$u$$ and $$b$$ are nonzero. This is a contradiction, and therefore, $$u$$ and $$w$$ are linearly independent and thus form a basis.

We can then rewrite \eqref{basis1} and \eqref{basis2} as

$$\begin{align} \label{basis3}
Au&=\begin{bmatrix}u&w\end{bmatrix}\begin{bmatrix}a\\-b\end{bmatrix}\\
Aw&=\begin{bmatrix}u&w\end{bmatrix}\begin{bmatrix}b\\a\end{bmatrix}
\end{align}$$

Due to the independence of columns in matrix multiplication, we can say

$$\begin{equation}
A\begin{bmatrix}u&w\end{bmatrix}=\begin{bmatrix}u&w\end{bmatrix}\begin{bmatrix}a&b\\-b&a\end{bmatrix}
\end{equation}$$

The matrix $$\begin{bmatrix}u&w\end{bmatrix}$$ is invertible since $$u$$ and $$w$$ form a basis. So we find that

$$\begin{equation}
A=\begin{bmatrix}u&w\end{bmatrix}\begin{bmatrix}a&b\\-b&a\end{bmatrix}\begin{bmatrix}u&w\end{bmatrix}^{-1}
\end{equation}$$

If we define the matrices,

$$\begin{gather}
P=\begin{bmatrix}u&w\end{bmatrix}\\
C=\begin{bmatrix}a&b\\-b&a\end{bmatrix} \label{complexspectral}
\end{gather}$$

Then

$$\begin{equation}
A=PCP^{-1}
\end{equation}$$

Notice that the entries of the matrix $$C$$ are essentially just the eigenvalues. More specifically the real and imaginary parts of them.

Another cool thing to notice is that if we say that $$a+bi=re^{i\theta}$$, then we can write the matrix $$C$$ as

$$\begin{equation}
C=\begin{bmatrix}r\cos \theta&r\sin \theta\\-r\sin \theta&r\cos \theta\end{bmatrix}
\end{equation}$$

$$\begin{equation}
C=r\begin{bmatrix}\cos \theta&\sin \theta\\-\sin \theta&\cos \theta\end{bmatrix}
\end{equation}$$

Which looks a lot like $$re^{i\theta}$$, just instead of a complex exponential, its a rotation matrix.

This shouldn't be entirely surprising, that a matrix with complex eigenvalues is similar to a simple transformation which scales and rotates.

Larger Matrices
-

Suppose instead we have other eigenvectors. If we can figure it out with a $$3\times 3$$ then we can figure it out with any matrix.

Then let $$A$$ be a real $$3\times3$$ matrix with eigenvalues $$\lambda=a\pm ib$$ and $$\lambda=c$$, where once again $$a,b,c\in\mathbb{R}$$ and $$b\neq 0$$. If the eigenvectors are $$v_1=u+iw, v_2=u-iw$$ and $$v_3$$, we can do the same song and dance

$$\begin{align}
Au&=au-bw\\
Aw&=bu+aw\\
Av_3&=cv_3
\end{align}$$

which allows us to say 

$$\begin{equation}
A=\begin{bmatrix}\\u&w&v_3\\&\end{bmatrix}\begin{bmatrix}a&b&0\\-b&a&0\\0&0&c\end{bmatrix}\begin{bmatrix}\\u&w&v_3\\&\end{bmatrix}^{-1}
\end{equation}$$

So in general, when we have the eigenvalues $$a\pm ib$$ for any real matrix $$A$$, in the normal eigendecomposition $$A=PDP^{-1}$$, place the real and imaginary parts of the eigenvector separately into the two columns corresponding to the eigenvalues in the _modal_ matrix $$P$$, and in the _spectral_ matrix $$D$$, put the $$2\times2$$ block of the form \eqref{complexspectral} in place of the normal $$\begin{bmatrix}\lambda_j&0\\0&\lambda_{j+1}\end{bmatrix}$$.