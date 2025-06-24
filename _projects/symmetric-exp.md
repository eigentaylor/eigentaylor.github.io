---
layout: page
title: Exponentials of Symmetric Matrices Using the Spectral Theorem
date: 2020-12-01 
description: yeah
comments: true
importance: 5
category: linear algebra
---
If $$A$$ is an $$n\times n$$ symmetric matrix with eigenvectors $$\{v_1,\ldots,v_n\}$$ which form an orthonormal basis of $$R^n$$ corresponding to eigenvalues $$\lambda_1,\ldots,\lambda_n$$, then

$$\begin{equation}
e^{tA}=e^{\lambda_1t}v_1v_1^T+\ldots+e^{\lambda_nt}v_nv_n^T
\end{equation}$$

Derivation:
=
The spectral decomposition of $$A$$ is 

$$\begin{equation}
A=\lambda_1v_1v_1^T+\ldots+\lambda_nv_nv_n^T
\end{equation}$$

Define the matrix 

$$\begin{equation}
V_i=v_iv_i^T
\end{equation}$$

There are a few properties of these matrices which will be important later. Proofs are left as an exercise for the reader (they're not that bad). Using the fact that the vectors $$v_1,\ldots,v_n$$ form an orthonormal basis:

$$\begin{align}
&V_iV_j=0,\quad i\neq j\\
&V_iV_i=V_i\\
\implies &V_iV_j=V_jV_i
\end{align}$$

Now we can rewrite $$A$$ as a sum of commuting matrices.

$$\begin{equation}
A=\lambda_1V_1+\ldots+\lambda_nV_n
\end{equation}$$

We establish a few important properties of matrix exponentials

$$\begin{align}
AB=BA&\implies e^{A+B}=e^Ae^B\\
P^2=P&\implies e^{tP}=I+(e^t-1)P\\
\end{align}$$

The latter, I believe, deserves proof.

Suppose $$P^2=P$$ which trivially implies that for any natural number $$n$$, $$P^n=P$$.

$$\begin{equation}
e^{tP}=\sum_{n=0}^\infty \frac{(tP)^n}{n!}=I+\left(\sum_{n=1}^\infty \frac{t^n}{n!}\right)P=I+(e^t-1)P
\end{equation}$$

Using the established properties of matrix exponentials

$$\begin{gather}
e^{tA}=e^{t(\lambda_1V_1+\ldots+\lambda_nV_n)}\\
e^{tA}=e^{\lambda_1tV_1}\ldots e^{\lambda_ntV_n}\\
e^{tA}=(I+(e^{\lambda_1t}-1)V_1)\ldots(I+(e^{\lambda_nt}-1)V_n)\\
e^{tA}=I+(e^{\lambda_1t}-1)V_1+\ldots+(e^{\lambda_nt}-1)V_n
\end{gather}$$

The last line definitely requires proof. We will use induction.

Base case $$n=2$$:

$$\begin{gather}
(I+(e^{\lambda_1t}-1)V_1)(I+(e^{\lambda_2t}-1)V_2)\\
=I^2+(e^{\lambda_1t}-1)V_1+(e^{\lambda_2t}-1)V_2+(e^{\lambda_1t}-1)(e^{\lambda_2t}-1)V_1V_2\\
=I+(e^{\lambda_1t}-1)V_1+(e^{\lambda_2t}-1)V_2
\end{gather}$$

Now suppose it is true for $$n=k$$:

$$\begin{equation}
(I+(e^{\lambda_1t}-1)V_1)\ldots(I+(e^{\lambda_kt}-1)V_k)=I+(e^{\lambda_1t}-1)V_1+\ldots+(e^{\lambda_kt}-1)V_k
\end{equation}$$

It follows

$$\begin{gather}
(I+(e^{\lambda_1t}-1)V_1)\ldots(I+(e^{\lambda_kt}-1)V_k)(I+(e^{\lambda_{k+1}t}-1)V_{k+1})\\
=\bigg[(I+(e^{\lambda_1t}-1)V_1)\ldots(I+(e^{\lambda_kt}-1)V_k)\bigg] (I+(e^{\lambda_{k+1}t}-1)V_{k+1})\\
=\bigg[I+(e^{\lambda_1t}-1)V_1+\ldots+(e^{\lambda_kt}-1)V_k\bigg] (I+(e^{\lambda_{k+1}t}-1)V_{k+1})\\
=\bigg[I+(e^{\lambda_1t}-1)V_1+\ldots+(e^{\lambda_kt}-1)V_k\bigg] +\bigg[I+(e^{\lambda_1t}-1)V_1+\ldots+(e^{\lambda_kt}-1)V_k\bigg] (e^{\lambda_{k+1}t}-1)V_{k+1}\\
=I+(e^{\lambda_1t}-1)V_1+\ldots+(e^{\lambda_kt}-1)V_k
+(e^{\lambda_{k+1}t}-1)V_{k+1}+
(e^{\lambda_{k+1}t}-1)((e^{\lambda_1t}-1)V_1V_{k+1}+\ldots+(I+(e^{\lambda_kt}-1)V_kV_{k+1})\\
=I+(e^{\lambda_1t}-1)V_1+\ldots+(e^{\lambda_kt}-1)V_k
+(e^{\lambda_{k+1}t}-1)V_{k+1}\\
\end{gather}$$

Nearing the end we rewrite the exponential,

$$\begin{gather}
e^{tA}=I+(e^{\lambda_1t}-1)V_1+\ldots+(e^{\lambda_nt}-1)V_n\\
e^{tA}=e^{\lambda_1t}V_1+\ldots+e^{\lambda_nt}V_n+I-(V_1+\ldots+V_n)
\end{gather}$$

Proposition:

If $$v_1,\ldots,v_n$$ form an orthonormal basis of $$R^n$$, then

$$\begin{equation}
v_1v_1^T+\ldots+v_nv_n^T=I
\end{equation}$$

Proof:

Any vector $$w\in R^n$$ can be written as a linear combination of $$v_1,\ldots,v_n$$ because it is a basis.

$$\begin{equation}
w=c_1v_1+\ldots+c_nv_n
\end{equation}$$

Multiply $$w$$ by $$v_1v_1^T+\ldots+v_nv_n^T$$:

$$\begin{gather}
(v_1v_1^T+\ldots+v_nv_n^T)w=(v_1v_1^T+\ldots+v_nv_n^T)(c_1v_1+\ldots+c_nv_n)\\
=v_1v_1^T(c_1v_1+\ldots+c_nv_n)+\ldots+v_nv_n^T(c_1v_1+\ldots+c_nv_n)\\
=v_1(c_1v_1^Tv_1+\ldots+c_nv_1^Tv_n)+\ldots+v_n(c_1v_n^Tv_1+\ldots+c_nv_n^Tv_n)\\
=v_1(c_1(v_1\cdot v_1)+\ldots+c_n(v_1\cdot v_n))+\ldots+v_n(c_1(v_n\cdot v_1)+\ldots+c_n(v_n\cdot v_n))\\
=v_1(c_1(1)+0)+\ldots+(0+c_n(1))\\
=c_1v_1+\ldots+c_nv_n=w\\
(v_1v_1^T+\ldots+v_nv_n^T)w=w
\end{gather}$$

Since this transformation leaves all vectors in $$R^n$$ unchanged it's clear that $$v_1v_1^T+\ldots+v_nv_n^T$$ is the identity transformation.

Therefore,

$$\begin{equation}
I-(V_1+\ldots+V_n)=0
\end{equation}$$

and so it follows

$$\begin{equation}
e^{tA}=e^{\lambda_1t}v_1v_1^T+\ldots+e^{\lambda_nt}v_nv_n^T
\end{equation}$$

or more generally for an orthogonal set of vectors,

$$\begin{equation}
e^{tA}=\frac{e^{\lambda_1t}}{|v_1|^2}v_1v_1^T+\ldots+\frac{e^{\lambda_nt}}{|v_n|^2}v_nv_n^T
\end{equation}$$

An Application
=

This would make solving nonhomogeneous systems of first-order linear differential equations with a symmetric coefficient matrix much easier.

If $$A$$ is an $$n\times n$$ symmetric matrix with eigenvectors $$\{\vec{v}_1,\ldots,\vec{v}_n\}$$ which form an orthogonal basis of $$R^n$$ corresponding to eigenvalues $$\lambda_1,\ldots,\lambda_n$$.

Then the nonhomogeneous system of first order linear differential equations

$$\begin{equation}
\vec{x}'=A\vec{x}+\vec{g}(t),\quad \vec{x}(t_0)=\vec{x}_0
\end{equation}$$

has the solution

$$\begin{equation}
\vec{x}(t)
=\sum _{k=1}^n \left[\frac{e^{\lambda_kt}}{|\vec{v}_k|^2}\left\langle \vec{v} _k\cdot\left(\int _{t_0}^te^{-\lambda_ku}\,\vec{g}(u)\,du+\vec{x}_0\right)\right\rangle\vec{v}_k\right] 
\end{equation}$$

Proof:

Suppose the solution to the differential equation is of the form

$$\begin{equation}
\vec{x}(t)=e^{tA}\vec{z}(t)+e^{tA}\vec{x} _0
\end{equation}$$

Subsitituting into the differential equation,

$$\begin{gather}
\vec{x}'(t)=Ae^{tA}\vec{z}(t)+e^{tA}\vec{z}'(t)+Ae^{tA}\vec{x} _0=A(e^{tA}\vec{z}(t)+e^{tA}\vec{x} _0)+\vec{g}(t)\\
e^{tA}\vec{z}'(t)=\vec{g}(t)\\
\vec{z}'(t)=e^{-tA}\vec{g}(t)\\
\vec{z}(t)=\int _{t_0}^te^{-uA}\vec{g}(u)du\\
\vec{x}(t)=e^{tA}\int_{t_0}^te^{-uA}\vec{g}(u)du+e^{tA}\vec{x} _0\\
\vec{x}(t)=\int _{t_0}^te^{(t-u)A}\vec{g}(u)du+e^{tA}\vec{x} _0\\
\vec{x}(t)=\int _{t _0}^t\left(\sum _{k=1}^n\left[e^{\lambda _k(t-u)}\:\vec{v} _k\:\vec{v} _k^T\right]\right)\vec{g}(u)\,du
+\sum _{k=1}^n\left[e^{\lambda _kt}\:\vec{v} _k\:\vec{v} _k^T\right]\vec{x} _0\\
\vec{x}(t)=\sum _{k=1}^n\left[\int _{t _0}^te^{\lambda _k(t-u)}\:\vec{v} _k\:\vec{v} _k^T\vec{g}(u)\,du\right]
+\sum _{k=1}^n\left[e^{\lambda _kt}\vec{v} _k\:\vec{v} _k^T\vec{x} _0\right]\\
\vec{x}(t)=\sum _{k=1}^n\left[e^{\lambda _kt}\int _{t _0}^te^{-\lambda _ku}\:\vec{v} _k\:\vec{v} _k^T\vec{g}(u)\,du\right]
+\sum _{k=1}^n\left[e^{\lambda _kt}\:\vec{v} _k\:\left\langle\vec{v} _k^T\vec{x} _0\right\rangle\right]\\
\vec{x}(t)=\sum _{k=1}^n\left[e^{\lambda _kt}\int _{t _0}^t\vec{v} _k\left\langle\vec{v} _k^T\left(e^{-\lambda _ku}\:\vec{g}(u)\right)\right\rangle\,du\right]
+\sum _{k=1}^n\left[e^{\lambda _kt}\:\vec{v} _k\:\left\langle\vec{v} _k^T\vec{x} _0\right\rangle\right]\\
\vec{x}(t)=\sum _{k=1}^n\left[e^{\lambda _kt}\int _{t _0}^t\vec{v} _k\left\langle\vec{v} _k\cdot\left(e^{-\lambda _ku}\:\vec{g}(u)\right)\right\rangle\,du\right]
+\sum _{k=1}^n\left[e^{\lambda _kt}\:\vec{v} _k\:\left\langle\vec{v} _k\cdot\vec{x} _0\right\rangle\right]\\
\vec{x}(t)=\sum _{k=1}^n\left[e^{\lambda _kt}\int _{t _0}^t\left\langle\vec{v} _k\cdot\left(e^{-\lambda _ku}\:\vec{g}(u)\right)\right\rangle\vec{v} _k\,du\right]
+\sum _{k=1}^n\left[e^{\lambda _kt}\left\langle\vec{v} _k\cdot\vec{x} _0\right\rangle\:\vec{v} _k\right]\\
\vec{x}(t)=\sum _{k=1}^n\left[e^{\lambda _kt}\left(\int _{t _0}^t\left\langle\vec{v} _k\cdot\left(e^{-\lambda _ku}\:\vec{g}(u)\right)\right\rangle\,du\right)\vec{v} _k\right]
+\sum _{k=1}^n\left[e^{\lambda _kt}\left\langle\vec{v} _k\cdot\vec{x} _0\right\rangle\vec{v} _k\right]\\
\vec{x}(t)=\sum _{k=1}^n\left[e^{\lambda _kt}\left\langle\vec{v} _k\cdot\left(\int _{t _0}^te^{-\lambda _ku}\:\vec{g}(u)\,du\right)\right\rangle\vec{v} _k\right]+\sum _{k=1}^n\left[e^{\lambda _kt}\left\langle\vec{v} _k\cdot\vec{x} _0\right\rangle\vec{v} _k\right]\\
\vec{x}(t)=\sum _{k=1}^n\left[e^{\lambda _kt}\left(\left\langle\vec{v} _k\cdot\left(\int _{t _0}^te^{-\lambda _ku}\:\vec{g}(u)\,du\right)\right\rangle+\left\langle\vec{v} _k\cdot\vec{x} _0\right\rangle \right)\vec{v} _k\right]\\
\vec{x}(t)=\sum _{k=1}^n\left[e^{\lambda _kt}\left\langle\vec{v} _k\cdot\left(\int _{t _0}^te^{-\lambda _ku}\:\vec{g}(u)\,du+\vec{x} _0\right)\right\rangle\vec{v} _k\right]
\end{gather}$$

Alternatively, if the vectors $$\vec{v}_1,\ldots,\vec{v}_n$$ are orthogonal but not necessarily normalized,

$$\begin{equation}
\vec{x}(t)=\sum _{k=1}^n\left[\frac{e^{\lambda _kt}}{|\vec{v}_k|^2}\left\langle\vec{v} _k\cdot\left(\int _{t _0}^te^{-\lambda _ku}\:\vec{g}(u)\,du+\vec{x} _0\right)\right\rangle\vec{v} _k\right]
\end{equation}$$
