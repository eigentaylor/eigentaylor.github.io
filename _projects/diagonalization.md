---
layout: distill
title: A Different Perspective of Diagonalization
date: 2020-11-02
description: An (atttempt at an) intuitive approach to similar matrix decomposition.
comments: true
importance: 5
category: linear algebra
authors:
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Diagonalization
  - name: General Decomposition
    subsections:
      - name: Complex Eigendecomposition of Real Matrices
---
$$\newcommand{\Re}{\operatorname{Re}}$$
$$\newcommand{\Im}{\operatorname{Im}}$$

Diagonalization
=

While this works for any dimension matrix, this will be of the example where the matrix is a $$2\times2$$.

Suppose $$A$$ is a $$2\times2$$ matrix with eigenvectors $$\textbf{v}_1,\textbf{v}_2$$ associated with eigenvalues $$\lambda_1,\lambda_2$$ respectively. By definition of an eigenvector, this would imply that for any scalars $$c_1,c_2$$.

\begin{equation}
A(c_1\textbf{v}_1+c_2\textbf{v}_2)=\lambda_1c_1\textbf{v}_1+\lambda_2c_2\textbf{v}_2
\end{equation}

Say we apply $$A$$ a second time...

$$\begin{gather*}
A(A(c_1\textbf{v}_1+c_2\textbf{v}_2))=A((\lambda_1c_1)\textbf{v}_1+(\lambda_2c_2)\textbf{v}_2)\\
A^2(c_1\textbf{v}_1+c_2\textbf{v}_2)=\lambda_1(\lambda_1c_1)\textbf{v}_1+\lambda_2(\lambda_2c_2)\textbf{v}_2\\
A^2(c_1\textbf{v}_1+c_2\textbf{v}_2)=\lambda_1^2c_1\textbf{v}_1+\lambda_2^2c_2\textbf{v}_2\\
\end{gather*}$$

We could easily repeat this as many times as we wanted. So it is also the case that

\begin{equation}\label{exp}
A^n(c_1\textbf{v}_1+c_2\textbf{v}_2)=\lambda_1^nc_1\textbf{v}_1+\lambda_2^nc_2\textbf{v}_2
\end{equation}

Since for those vectors, the transformation $$A$$ is just simple scaling, in the situation where we have to repeatedly apply $$A$$ to some vector $$w$$, it would clearly be preferable to get that vector in terms of $$\textbf{v}_1$$ and $$\textbf{v}_2$$. This seems like a job for change of basis...

So let us define the eigenbasis
$$\begin{equation}
B=\{\textbf{v}_1,\textbf{v}_2\}
\end{equation} $$

The change of basis matrix $$P_{\varepsilon\leftarrow B}$$ (where $$\varepsilon$$ is the standard basis $$\varepsilon=\{e_1,e_2\}$$), then is

$$\begin{equation}
P_{\varepsilon\leftarrow B}=
\bigg(
    \textbf{v}_1\quad \textbf{v}_2
\bigg)
\end{equation}$$

By extension,

\begin{equation}\label{inv change}
P_{B\leftarrow\varepsilon}=(P _{\varepsilon\leftarrow B})^{-1}
\end{equation}

So now suppose that

$$
\textbf{w}=c_1\textbf{v}_1+c_2\textbf{v}_2
$$

This tells us that the coordinate vector of $$w$$ with respect to the eigenbasis $$B$$, $$(\textbf{w})_B$$, is

$$\begin{equation}
\textbf{w}=c_1\textbf{v}_1+c_2\textbf{v}_2
\implies
(\textbf{w})_B=\begin{pmatrix}c_1\\c_2\end{pmatrix}
\end{equation}$$

We know from \eqref{exp} then that

$$
A^n\textbf{w}=A^n(c_1\textbf{v}_1+c_2\textbf{v}_2)=\lambda_1^nc_1\textbf{v}_1+\lambda_2^nc_2\textbf{v}_2
$$

So

$$
(A^n\textbf{w})_B=\begin{pmatrix}\lambda_1^nc_1\\\lambda_2^nc_2\end{pmatrix}
$$

But that's also the transformation

$$
(A^n\textbf{w})_B=\begin{pmatrix}\lambda_1^nc_1\\\lambda_2^nc_2\end{pmatrix}=\begin{pmatrix}\lambda_1^n&0\\0&\lambda_2^n\end{pmatrix}\begin{pmatrix}c_1\\c_2\end{pmatrix}
$$

If we call the diagonal matrix
$$D=\begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}$$, then we get

\begin{equation}
(A^n\textbf{w})_B=D^n(\textbf{w})_B
\end{equation}

We're so close now. Next, we change back to the standard basis by applying $$P_{\varepsilon\leftarrow B}$$ to both sides,

$$
P_{\varepsilon\leftarrow B}(A^n\textbf{w}) _{B} = P _{\varepsilon\leftarrow B}D^n
(\textbf{w}) _B
$$

\begin{equation}\label{close}
A^n\textbf{w}=P _{\varepsilon\leftarrow B}D^n(\textbf{w}) _B
\end{equation}

To get things entirely in terms of the standard basis, we start by rewriting

$$
(\textbf{w}) _B=P _{B\leftarrow\varepsilon}(\textbf{w}) _{\varepsilon}
$$

Using \eqref{inv change} and the fact that $$(\textbf{w}) _{\varepsilon}=w$$ (by definition of the standard basis),

\begin{equation}
(\textbf{w}) _B=(P _{\varepsilon\leftarrow B})^{-1}\textbf{w}
\end{equation}

we substitute into \eqref{close}

$$
A^n\textbf{w}=P _{\varepsilon\leftarrow B}D^n(P _{\varepsilon\leftarrow B})^{-1}\textbf{w}
$$

If we just denote $$P _{\varepsilon\leftarrow B}$$ as $$P$$, then we finally get

\begin{equation}
A^n\textbf{w}=PD^nP^{-1}\textbf{w}
\end{equation}

General Decomposition
=

In general, if we know how a matrix $$A$$ acts on a basis, then we may either construct or decompose it via a $$PDP^{-1}$$ decomposition.

Complex Eigendecomposition of Real Matrices
-

Let's take the example of a real $$2\times2$$ with complex eigenvalues. Suppose $$A$$ is such a matrix with a complex eigenvalue $$a+bi$$, where $$b\neq0$$, associated with a complex eigenvector $$v$$.

\begin{equation} \label{complex eigenvector}
A\textbf{v}=(a+bi)\textbf{v}
\end{equation}

Let's get a bit more specific by decomposing $$v$$ into its real and imaginary parts.

$$\begin{gather*}
A(\Re(\textbf{v})+i\Im(\textbf{v}))=(a+bi)(\Re(\textbf{v})+i\Im(\textbf{v}))\\
A\Re(\textbf{v})+i(A\Im(\textbf{v}))=(a\Re(\textbf{v})-b\Im(\textbf{v}))+i(b\Re(\textbf{v})+a\Im(\textbf{v}))
\end{gather*}$$

We can equate the real and imaginary parts on both sides,

\begin{equation}
A\Re(\textbf{v})=a\Re(\textbf{v})-b\Im(\textbf{v}),\quad A\Im(\textbf{v})=b\Re(\textbf{v})+a\Im(\textbf{v})
\end{equation}

Now we know that $$\{\Re(\textbf{v}),\Im(\textbf{v})\}$$ is a basis of $$\mathbb{R}^2$$ because if they were linearly dependent, then $$\Im(\textbf{v})=k\Re(\textbf{v})$$. That would change \eqref{complex eigenvector} into

$$
A(1+ki)\Re(\textbf{v})=(a+bi)(1+ki)\Re(\textbf{v})
$$

Dividing by the common $$1+ki$$,

$$
A\Re(\textbf{v})=(a+bi)\Re(\textbf{v})
$$

This implies a contradiction since the imaginary part of the left side is zero due to $$A$$ being real, but the right is not if $$b\neq0$$. Therefore,

$$\begin{equation} \label{complex basis}
B=\{\Re(\textbf{v}),\Im(\textbf{v})\} \text{ is a basis for } \mathbb{R}^2
\end{equation}$$

It then follows that

$$\begin{equation}
P=
\bigg(
    \Re(\textbf{v})\quad\Im(\textbf{v})
\bigg)
\end{equation}$$

is invertible.

Well, we know how $$A$$ acts on the basis $$B$$ \eqref{complex basis}:

$$
(A\Re(\textbf{v}))_B=\begin{pmatrix}a\\-b\end{pmatrix},\quad (A\Im(\textbf{v}))_B=\begin{pmatrix}b\\a\end{pmatrix}
$$

So our matrix $$D$$ is then,

$$\begin{equation}
D=\begin{pmatrix}a&b\\-b&a\end{pmatrix}
\end{equation}$$

And our eigendecomposition of $$A$$ is

$$\begin{equation}
A=\bigg(
    \Re(\textbf{v})\quad\Im(\textbf{v})
\bigg)
\begin{pmatrix}a&b\\-b&a\end{pmatrix}
\bigg(
    \Re(\textbf{v})\quad\Im(\textbf{v})
\bigg)^{-1}
\end{equation}$$

It can be verified that the eigenvalues of this particular $$D$$ are $$\lambda=a\pm bi$$.
