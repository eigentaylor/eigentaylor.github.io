---
layout: page
title: Constructing 2x2 Markov Matrices
date: 2021-01-16
description: Build a Markov Chain with desired behavior.
comments: true
importance: 2
categories: linear-algebra
---

What We Want
-

We are looking for a regular stochastic matrix $$M$$ with all positive entries less than $$1$$ such that the columns add up to $$1$$. The 'steady-state' vector will be $$\vec{x}_f=(x_f,1-x_f)$$, where $$0< x_f<1$$, such that

1. 
    $$\begin{equation}
M\vec{x}_f=\vec{x}_f
\end{equation}$$

2. 
    $$\begin{equation}
\lim_{k\to\infty}M^k\vec{x}_0=\vec{x}_f,\;\forall \;\vec{x}_0
\end{equation}$$

So, essentially, we have a specific vector we want the system to converge to. That isn't too difficult so let's spice it up and get more specific. After $$n$$ iterations, for any given initial state $$\vec{x}_0=(x_0,1-x_0)$$ where $$0\leq x_0\leq1$$, the system must be within an error of $$\varepsilon>0$$ from the equilibrium solution.

$$\begin{equation}
|M^n\vec{x}_0-\vec{x}_f|\leq\varepsilon
\end{equation}$$

The solution which we will derive is as follows. 

---

For a $$\lambda$$ satisfying both

$$\begin{equation}\label{bounds}
|
\lambda
|\leq
\sqrt[\leftroot{-2}\uproot{2}n]{\frac{\varepsilon}{x_f\sqrt2}},\quad
\lambda>\frac{|2x_f-1|-1}{|2x_f-1|+1}
\end{equation}$$

---

The Matrix
-

$$M$$ is given by both of the following expressions,

---

$$\begin{equation} \label{M2Sum}
M=
\begin{bmatrix}x_f\\1-x_f\end{bmatrix}
\begin{bmatrix}1&1\end{bmatrix}+
\lambda\begin{bmatrix}-1\\1\end{bmatrix}
\begin{bmatrix}x_f-1&x_f\end{bmatrix}
\end{equation}$$

$$\begin{equation}\label{M1Sum}
M=
I+(1-\lambda)
\begin{bmatrix}1\\-1\end{bmatrix}\begin{bmatrix}x_f-1&x_f\end{bmatrix}
\end{equation}$$

---

The sign of $$\lambda$$ will determine whether the system approaches the equilibrium directly or if it bounces around like an alternating series.

Additionally, $$\vec{x}_n=M^n\vec{x}_0$$ is given by

$$\begin{equation} \label{xn}
M^n\vec{x}_0=
\vec{x}_f
+
\lambda^n(x_f-x_0)\begin{bmatrix}-1\\1\end{bmatrix}
\end{equation}$$

This looks exactly like what we want since 

$$\lim_{n\to \infty}\lambda^n=0$$ 

if $$|
\lambda
|<1$$ leaving us with our steady state vector in the limit.

Testing
-

Let's take an example to see if it works. 

I want the equilibrium of the system to be $$\vec{x}_f=(0.75,0.25)$$, and after $$4$$ iterations I want the system to be within $$0.01$$ from the equilibrium.

That gives me

$$\begin{equation}
|
\lambda
|\leq
\sqrt[\leftroot{-2}\uproot{2}4]{\frac{0.01}{0.75\sqrt2}}
\approx 0.3116,\quad 
\lambda > -\frac{1}{3}
\end{equation}$$

Let's take $$\lambda=0.3$$. That gives me 

$$\begin{equation}
M=
I+(0.7)
\begin{bmatrix}1\\-1\end{bmatrix}\begin{bmatrix}-0.25&0.75\end{bmatrix}=\begin{bmatrix}0.825&0.525\\0.175&0.475\end{bmatrix}
\end{equation}$$

We test our equilibrium vector,

$$\begin{equation}
\begin{bmatrix}0.825&0.525\\0.175&0.475\end{bmatrix}\begin{bmatrix}0.75\\0.25\end{bmatrix}=\begin{bmatrix}0.75\\0.25\end{bmatrix}
\end{equation}$$

Perfect. Now to maximize the error, $$x_0$$ has to be either $$0$$ or $$1$$ (because based on equation \eqref{xn} we want to maximize $$|
x_f-x_0
|$$ where they are both between $$0$$ and $$1$$). That means $$\vec{x}_0$$ is either $$(1,0)$$ or $$(0,1)$$. Therefore, the $$\vec{x}_n$$ furthest from the equilibrium vector will be one of the columns of $$M^n$$. Thus, we can just raise $$M$$ to the $$n$$th power and see how close each column is to $$\vec{x}_f$$.

$$\begin{equation}
M^4=\begin{bmatrix}0.752&0.7439\\0.248&0.2561\end{bmatrix}
\end{equation}$$

The error of each column is $$\approx 0.00286,0.00859$$ which are both absolutely within our desired error. Just to check, let's see how far off $$\vec{x}_3$$ is.

$$\begin{equation}
M^3=\begin{bmatrix}0.7567&0.7297\\0.2432&0.2702\end{bmatrix}
\end{equation}$$

The error here is $$\approx 0.0095,0.0286$$, the latter of which it is not within our desired error. So we managed to set the rate of convergence to be just where we want it. In fact, we could get a lower bound on $$\lambda$$ by substituting $$3$$ into the upper bound expression in \eqref{bounds}. Since $$\lambda=-0.3$$ also fits between our bounds, we could have used that to get a different matrix where the answer oscillates. 

$$\begin{array}{c|ccccc}
\lambda&M^0&M&M^2&M^3&M^4\\
0.3&\begin{bmatrix}1&0\\0&1\end{bmatrix}
&\begin{bmatrix}0.825&0.525\\0.175&0.475\end{bmatrix}
&\begin{bmatrix}0.7725&0.6825\\0.2275&0.3175\end{bmatrix}
&\begin{bmatrix}0.7567&0.7297\\0.2432&0.2702\end{bmatrix}
&\begin{bmatrix}0.7520&0.7439\\0.2480&0.2561\end{bmatrix}&\hline\\
-0.3&\begin{bmatrix}1&0\\0&1\end{bmatrix}
&\begin{bmatrix}0.675&0.975\\0.325&0.025\end{bmatrix}
&\begin{bmatrix}0.7725&0.6825\\0.2275&0.3175\end{bmatrix}
&\begin{bmatrix}0.7433&0.7703\\    0.2567&    0.2297\end{bmatrix}
&\begin{bmatrix}0.7520 &   0.7439\\    0.2480 &   0.2561\end{bmatrix}
\end{array}$$

Beautifully, they are the same for even $$n$$, which is consistent with \eqref{xn}.

Proof / Derivation
-

We start by using an incredibly useful fact:

If $$v$$ is an eigenvector of $$A$$ with eigenvalue $$\lambda$$, and if $$v'$$ is an eigenvector of $$A^T$$ with eigenvalue $$\lambda'\neq\lambda$$, then

$$\begin{equation}
v\cdot v'=0
\end{equation}$$

I encourage the reader to prove this.

<details>
  <summary>Hint</summary>
    Consider $$(v')^TAv$$
</details>

Now we also use the fact that $$(1,1)$$ is an eigenvector with eigenvalue $$1$$ of $$M^T$$ because the columns of $$M$$ add up to $$1$$. 

Therefore, $$(-1,1)$$ is an eigenvector of $$M$$ with an eigenvalue that is *not* $$1$$ (let's say $$\lambda$$). 

Since we want $$(x_f,1-x_f)$$ (which is linearly independent of $$(-1,1)$$ if $$0< x_f<1$$) to be an eigenvector with eigenvalue $$1$$, we have a basis of eigenvectors and everything we need to construct a diagonalization of $$M$$.

$$\begin{equation}
M=\begin{bmatrix}x_f&-1\\1-x_f&1\end{bmatrix}
\begin{bmatrix}1&0\\0&\lambda\end{bmatrix}\begin{bmatrix}x_f&-1\\1-x_f&1\end{bmatrix}^{-1}
\end{equation}$$

To get \eqref{M2Sum} we just write the center matrix as

$$\begin{equation}
\begin{bmatrix}1&0\\0&\lambda\end{bmatrix}=e_1e_1^T+\lambda e_2e_2^T
\end{equation}$$

Then we just distribute the matrices on the left and right.

For \eqref{M1Sum}, we simplify calculating by removing an $$I$$ from $$M$$.

$$\begin{equation}
M=I+\begin{bmatrix}x_f&-1\\1-x_f&1\end{bmatrix}
\begin{bmatrix}0&0\\0&\lambda-1\end{bmatrix}\begin{bmatrix}x_f&-1\\1-x_f&1\end{bmatrix}^{-1}
\end{equation}$$

Big brain row/column perspective tells us that we want $$(\lambda-1)$$ of the second column of the eigenvector matrix times the second row of its inverse.

$$\begin{equation}
M=I+(\lambda-1)\begin{bmatrix}-1\\1\end{bmatrix}
\begin{bmatrix}x_f-1&x_f\end{bmatrix}
\end{equation}$$

$$\lambda-1$$ is always negative, so just to make it nice we negate both it and the column vector to get \eqref{M1Sum}.

To prove \eqref{xn} we use the wonderful properties of diagonalization $$M^n=PD^nP^{-1}$$ and do the same steps that we did to get \eqref{M2Sum} to say that

$$\begin{equation}
M^n=
\begin{bmatrix}x_f\\1-x_f\end{bmatrix}
\begin{bmatrix}1&1\end{bmatrix}+
\lambda^n\begin{bmatrix}-1\\1\end{bmatrix}
\begin{bmatrix}x_f-1&x_f\end{bmatrix}
\end{equation}$$

Multiply on the right by $$\vec{x}_0=(x_0,1-x_0)$$,

$$\begin{equation}
M^n\vec{x}_0=
\begin{bmatrix}x_f\\1-x_f\end{bmatrix}
\begin{bmatrix}1&1\end{bmatrix}
\begin{bmatrix}x_0\\1-x_0\end{bmatrix}+
\lambda^n\begin{bmatrix}-1\\1\end{bmatrix}
\begin{bmatrix}x_f-1&x_f\end{bmatrix}
\begin{bmatrix}x_0\\1-x_0\end{bmatrix}
\end{equation}$$

$$\begin{equation}
M^n\vec{x}_0=
\begin{bmatrix}x_f\\1-x_f\end{bmatrix}+
\lambda^n(x_f-x_0)\begin{bmatrix}-1\\1\end{bmatrix}
\end{equation}$$

Leaving us with \eqref{xn}.

Now to get the bounds on $$\lambda$$, we examine $$|
M^n\vec{x}_0-\vec{x}_f
|
<\varepsilon$$,

$$\begin{gather}
|
M^n\vec{x}_0-\vec{x}_f
|
<\varepsilon\\
\left|
\vec{x}_f+\lambda^n(x_f-x_0)\begin{bmatrix}-1\\1\end{bmatrix}-\vec{x}_f
\right|
<\varepsilon\\
\left|
\lambda^n(x_f-x_0)\begin{bmatrix}-1\\1\end{bmatrix}
\right|
<\varepsilon\\
|
\lambda^n(x_f-x_0)
|\left|
\begin{bmatrix}-1\\1\end{bmatrix}
\right|
<\varepsilon\\
|
\lambda|^n
|x_f-x_0|
\sqrt2
<\varepsilon\\
|
\lambda|^n
|x_f-x_0|
<\frac{\varepsilon}{\sqrt2}\\
\end{gather}$$

Now we observe that the maximum value of $$| 
x_f-x_0
|$$ is $$x_f$$ given our constraints on $$x_0$$ and $$x_f$$ to be between zero and one. Therefore, to maximize the distance, $$x_0$$ would have to be either of the bounds, zero or one. Substituting $$| 
x_f-x_0
|=x_f$$ and dividing it over,

$$\begin{equation}
|
\lambda|^n
<\frac{\varepsilon}{x_f\sqrt2}
\end{equation}$$

By taking the $$n$$-th root, we get the first part (upper bound) of \eqref{bounds}.

Now to get the lower bound, we make sure the entries of $$M$$ satisfy $$0< M_{ij}<1$$. We need only ensure one entry in each column, as $$0< M_{ij}<1\implies 0< 1-M_{ij}<1$$. So we choose to look at $$M_{12}$$ and $$M_{21}$$ because it'll be just slightly easier.

$$\begin{gather}
M_{12}=e_1^TMe_2\\
0< e_1^TMe_2<1\\
0< e_1^T\left(
I+(\lambda-1)\begin{bmatrix}-1\\1\end{bmatrix}
\begin{bmatrix}x_f-1&x_f\end{bmatrix}
\right)e_2<1\\
0< 0+(\lambda-1)(-1)(x_f)<1\\
-\frac{1}{x_f}< \lambda-1<0\\
1-\frac{1}{x_f}< \lambda<1\\
\left(1-\frac{1}{x_f}\right)^{1}< \lambda<1\\
\end{gather}$$

hhhh

$$\begin{gather}
M_{21}=e_2^TMe_1\\
0< e_2^TMe_1<1\\
0< e_2^T\left(
I+(\lambda-1)\begin{bmatrix}-1\\1\end{bmatrix}
\begin{bmatrix}x_f-1&x_f\end{bmatrix}
\right)e_1<1\\
0< 0+(\lambda-1)(1)(x_f-1)<1
\end{gather}$$

We know that $$x_f-1< 0$$ so we flip the inequality.

$$\begin{gather}
-\frac{1}{1-x_f}< \lambda-1<0\\
1-\frac{1}{1-x_f}< \lambda<1\\
\left(1-\frac{1}{x_f}\right)^{-1}< \lambda<1\\
\end{gather}$$

Therefore, for a lower bound on $$\lambda$$,

$$\begin{equation}
\left(1-\frac{1}{x_f}\right)^{\pm1}< \lambda
\end{equation}$$

We can simplify this, however. The following are equivalent expressions:

$$\begin{equation}
\left(1-\frac{1}{x_f}\right)^{\pm1}< \lambda \implies \frac{|2x_f-1|-1}{|2x_f-1|+1} < \lambda
\end{equation}$$

concluding the proof of \eqref{bounds}.