---
layout: page
title: Constructing Integer 2x2 First Order Systems of Differential Equations with Integer Solutions
date: 2021-05-15
description: Nice solutions? Nice.
comments: true
importance: 2
categories: works-in-progress
toc: true
---

Most of the results here are based on [this paper](https://ericthewry.github.io/pdfs/imies.pdf){:target="_blank"} by Christopher Towse and Eric Campbell. It's a fun read if you, like me, find constructing nice looking problems with nice looking solutions interesting.
$$\newcommand{\Re}{\operatorname{Re}}$$
$$\newcommand{\Im}{\operatorname{Im}}$$

They do a wonderful job defining great sufficient conditions for a matrix to be an IMIE--Integer Matrix (with all) Integer Eigenvalues--for matrices with real eigenvalues, and include an easy way to make the matrix undiagonalizable. They also, however, say that their results do not "capture all of the subtley of IMIE’s", which is surely an extremely difficult, if not impossible task in the $$n\times n$$ case. So I decided that I wanted to try and capture those subtleys for the $$2\times 2$$ case myself.

---

Here we look to generate constant integer $$2\times 2$$ matrices $$A$$ such that the solution to

$$\begin{equation}\label{xax}
x'=Ax
\end{equation}$$

is of the form

$$\begin{equation}
x=c_1x_1(t)+c_2x_2(t)
\end{equation}$$

where the functions $$x_i(t)$$ are of one of the following forms, with $$\lambda_i,\mu_i\in\mathbb{Z}$$ and all the vectors $$v_j,u_{ij}\in\mathbb{Z}^2$$,

$$\begin{gather}
x_i=v_ie^{\lambda_it}\\
x_i=(u_{i0}+u_{i1}t)e^{\lambda_it}\\
x_i=u_{i1}e^{\lambda_it}\cos(\mu_it)+u_{i2}e^{\lambda_it}\sin(\mu_it)\\
\end{gather}$$

These three cases corresponding to three different kinds of eigenvalues:

1. Real
2. Defective
3. Complex

We will tackle them in that order.

# Real Eigenvalues

Suppose we want all of the solutions to \eqref{xax} to be of the first form: $$x_i(t)=v_ie^{\lambda_it}$$ for a given linearly independent pair of vectors in $$\mathbb{Z}^2$$, $$v_1,v_2$$.

We start with the full set of reduced integer eigenvectors that our solution will consist of, $$v_i$$, and place them all as the columns of a matrix $$P$$. By reduced, I mean that the greatest common factor of the two entries is $$1$$. So for example, using $$v_1=(1,-3)$$ instead of $$(7,-21)$$.

For particular choices of the eigenvalues $$\lambda_i$$ corresponding to the vectors $$v_i$$, $$A$$ will then be

$$\begin{equation}
A=P\begin{bmatrix}
\lambda_1&0\\
0&\lambda_2
\end{bmatrix}P^{-1}
\end{equation}$$

In order for $$A$$ to have integer entries, the eigenvalues must be congruent modulo $$\det(P)$$. 

$$\begin{equation}
\lambda_1\bmod{\det P}=\lambda_2\bmod{\det P}
\end{equation}$$

In other words,

$$\begin{equation} \label{realeig}
\lambda_i=k_i\det(P)+\Delta
\end{equation}$$

for any integers $$k_i$$ and the same $$\Delta$$ for all the eigenvalues. 

Taking an example, if $$\det(P)=7$$ and you _really_ want a certain eigenvector to have an eigenvalue of $$1$$, the smallest eigenvalues the other eigenvectors can have will be $$8$$ and $$-6$$. Therefore, if you want $$A$$ to have relatively small integer entries, you must carefully choose your eigenvectors such that $$P$$ will have a small determinant. If your choice of eigenvectors cause $$P$$ to have a determinant of $$1$$, then there is no restriction on what the eigenvalues can be. But this can be quite limiting.

Occasionally, however, this condition is merely sufficient and not necessary. It's possible that rather than be congruent $$\det P$$, it's only necessary that they be congruent mod one factor of $$\det P$$. 

One (and possibly the only) example of this, is if the greatest common factor of the $$j$$th column is $$g_j$$, then rather than being congruent mod $$\det P$$, they actually have to be congruent mod $$h=\frac{\det P}{g_1g_2}$$. However, the reason I specified earlier that we use the reduced eigenvectors, is exactly because then we don't need to do this since $$g_1=g_2=1$$.

## Proof:

Suppose all of the eigenvalues of $$A$$ are of the form \eqref{realeig}, and the eigenvectors, and by extension the columns of $$P$$, have integer entries.

$$\begin{gather*}
A=P\begin{bmatrix}
k_1\det(P)+\Delta&0\\
0&k_1\det(P)+\Delta
\end{bmatrix}P^{-1}\\
A=P\left(\det(P)\begin{bmatrix}
k_1&0\\
0&k_1
\end{bmatrix}+\Delta I\right)P^{-1}\\
A=P\left(\det(P)\begin{bmatrix}
k_1&0\\
0&k_1
\end{bmatrix}\right)\left(\frac{1}{\det(P)}P^{adj}\right)+\Delta I\\
A=P\begin{bmatrix}
k_1&0\\
0&k_1
\end{bmatrix}P^{adj}+\Delta I\\
\end{gather*}$$

Since $$P$$ is a matrix of integers, $$P^{adj}$$ is also a matrix of integers. We defined all the values $$k_i$$ to be integers, as well as $$\Delta$$, and therefore we have the product of integer matrices added to an integer matrix. 

Since the integers are closed under addition and multiplication, \eqref{realeig} is a sufficient condition for $$A$$ to have integer entries. $$\blacksquare$$

The paper linked at the beginning of this post has a proof that this is also a necessary condition for $$2\times 2$$ matrices.

# Defective Eigenvalue

Now suppose we want the general solution of \eqref{xax} to be of the form

$$\begin{equation}
x(t)=c_1ve^{\lambda t}+c_2(u_0+u_1t)e^{\lambda t}
\end{equation}$$

for given linearly independent vectors $$v,u_0\in\mathbb{Z}^2$$.

Let us have the matrix $$P$$ have columns $$v,u_0$$ and denote the $$\det P=\delta$$. Next, given a vector $$w=(w_1,w_2)$$ let us define the vector

$$\begin{equation}
w^\perp=(-w_2,w_1)
\end{equation}$$

The matrix $$A$$ with the solution

$$\begin{equation}
x(t)=c_1ve^{\lambda t}+c_2(u+c\delta vt)e^{\lambda t}
\end{equation}$$

for some $$c\in\mathbb{Z}$$, to \eqref{xax} is then

$$\begin{equation}
A=\lambda I+cvv^\perp
\end{equation}$$

Do notice that $$u$$ is completely absent in this expression, making it relatively arbitrary. The only difference it really makes is in changing $$\delta$$. It is, in my opinion, optimal to simply select a $$u$$ which makes $$\delta$$ small. If one chooses a large $$u$$, it's almost surely the case that anyone solving the system will *not* get that particular $$u$$ in their second solution, *unless* you specify an initial condition of $$x(0)=u$$. Then the solution to that initial value problem will indeed be $$x(t)=(u+c\delta vt)e^{\lambda t}$$. In general, though, don't overthink the $$u$$ vector.

# Complex Eigenvalues (Conjecture)

Say we want a matrix $$A\in\mathbb{Z}^{2\times 2}$$ to satisfy \eqref{xax}, where one solution--for $$\lambda,\mu\in\mathbb{Z}$$, where $$\mu$$ is nonzero, and linearly independent $$u_1,u_2\in\mathbb{Z}^2$$--is

$$\begin{equation}
x_1(t)=e^{\lambda t}(u_1\cos(\mu t)+u_2\sin(\mu t))
\end{equation}$$

Note that another linearly independent solution will be 

$$\begin{equation}
x_2(t)=e^{\lambda t}(u_1\sin(\mu t)-u_2\cos(\mu t))
\end{equation}$$

Let the matrix $$P$$ be

$$\begin{equation}
P=
\begin{bmatrix}
u_1&u_2
\end{bmatrix}
\end{equation}$$

$$A$$ will then be

$$\begin{equation}
A=\lambda I+\mu P
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
P^{-1}
\end{equation}$$

Let $$g$$ be the greatest common factor of the entries of $$PP^T$$ and $$\det(P)$$.

**$$A$$ will be in $$\mathbb{Z}^{2\times 2}$$, if and only if $$\mu$$ is divisible by $$\frac{\det(P)}{g}$$.**

Another way to write $$A$$ is

$$\begin{equation}
A=\lambda I+\frac{\mu}{\det(P)}
PP^T
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\end{equation}$$

## Proof:

Suppose we have a particular $$P\in\mathbb{Z}^{2\times 2}$$. Given that $$g$$ is the greatest common factor of $$\det(P)$$ and the entries of $$PP^T$$, we want to show that

$$A=P
\begin{bmatrix}
\lambda&-\mu\\
\mu&\lambda
\end{bmatrix}
P^{-1}$$

will be an integer matrix with Gaussian integer complex eigenvalues $$\lambda\pm\mu i$$ if and only if $$\mu$$ is divisible by $$\Delta=\frac{\det(P)}{g}$$.

Briefly note that $$A$$ will have the eigenvalues $$\lambda\pm\mu i$$ because it is by definition similar to the matrix $$\begin{bmatrix}
\lambda&-\mu\\
\mu&\lambda
\end{bmatrix}$$, for which it can be verified to have the eigenvalues $$\lambda\pm\mu i$$.

---

We begin by supposing that $$\frac{\det(P)}{g}$$ divides $$\mu$$. Let $$\mu=k\frac{\det(P)}{g}$$ for $$k\in\mathbb{Z}$$, and define the matrix

$$\begin{equation}
Q=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\end{equation}$$

noting, also, that

$$\begin{equation} \label{qadj}
X^{adj}=Q^{-1}X^TQ
\end{equation}$$

Then we may write $$A$$ as

$$\begin{gather*}
A=\lambda I+\mu P
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
P^{-1}\\
A=\lambda I+k\frac{\det(P)}{g}\frac{1}{\det(P)} PQP^{adj}\\
A=\lambda I+\frac{k}{g} PQ(Q^{-1}P^TQ)\\
A=\lambda I+\frac{k}{g} PP^TQ\\
\end{gather*}$$

Let $$\frac{1}{g}PP^T=B$$. Note that $$B\in\mathbb{Z}^{2\times 2}$$ based on the definition of $$g$$.

$$A=\lambda I+kBQ$$

$$\lambda I,B,Q$$ are all integer matrices, and $$k$$ is also an integer. Therefore, $$A$$ is also an integer matrix. This completes the first half of the proof. $$\blacksquare$$

---

We next suppose that $$A$$ is an integer matrix with complex Gaussian integer eigenvalues $$\lambda\pm\mu i$$. We can therefore decompose $$A$$ as

$$A=P
\begin{bmatrix}
\lambda&-\mu\\
\mu&\lambda
\end{bmatrix}
P^{-1}$$

for some matrix $$P\in\mathbb{Z}^{2\times 2}$$.

We can ensure that there exists an integer matrix $$P$$, as the columns are obtained from a basis for the null space of the rank one matrix $$A-(\lambda+\mu i)I$$, which has Gaussian integer entries. The one linearly independent equation for the homogeneous system is then $$a_1n_1+a_2n_2=0$$ for some $$a_1,a_2\in\mathbb{Z}[i]$$. One solution will always be $$n=(a_2,-a_1)$$ which contains only Gaussian integer entries. It can be shown that the columns of $$P$$ can be $$\begin{bmatrix}\Re(n)&\Im(n)\end{bmatrix}$$, which would place $$P\in\mathbb{Z}^{2\times 2}$$. By extension, $$\det(P)\in\mathbb{Z}$$.

$$\begin{gather*}
A=\lambda I+\mu PQP^{-1}\\
A=\lambda I+\frac{\mu}{\det(P)} PQP^{adj}
\end{gather*}$$

Repeating the steps from above, we obtain

$$A=\lambda I+\frac{\mu}{\det(P)} PP^TQ$$

Now with the same definitions from above, $$\det(P)=g\Delta$$ and $$PP^T=gB$$, where $$\Delta$$ and the entries of $$B$$ are integers. This simplifies $$A$$ to

$$A=\lambda I+\frac{\mu}{\Delta} BQ$$

First observe that the simple nature of $$Q$$ causes $$BQ$$ to have the same exact entries as $$B$$, differing only by a sign. Therefore, if $$X$$ is an integer matrix, then $$XQ$$ is also an integer matrix. Because $$g$$ is the greatest common factor of the entries of $$PP^T$$, then the greatest common factor of the entries of $$B$$ is $$1$$. Therefore, for $$\frac{\mu}{\Delta} B$$ to be an integer matrix, $$\mu$$ must be divisible by $$\Delta=\frac{\det(P)}{g}$$. This concludes the proof. $$\blacksquare$$

# Derivations:

There is no *real* derivation for the Real Eigenvalues case (haha), as I think Towse and Campbell do a fine job in the paper linked at the beginning.

## Defective Eigenvalue Derivation

It can be easily verified by equating the terms of $$x'$$ and $$Ax$$ that for $$x_2(t)=(u_0+u_1t)e^{\lambda t}$$ to be a solution to \eqref{xax} given that $$x_1(t)=ve^{\lambda t}$$, $$u_1$$ must be a scalar multiple of $$v$$. Another condition is that $$Au_0=\lambda u_0+u_1$$. So $$u_0$$ must be a generalized eigenvector of $$A$$.

It's possible to go through a differential equations course without ever hearing the term or concept of a generalized eigenvector, however. Jordan normal forms are a bit beyond the scope of this post, but one can confirm that if $$v$$ and $$u_0$$ form the columns of an invertible $$P$$, then based on knowing that $$Av=\lambda v$$ and $$Au_0=\lambda u_0+u_1$$ we can write $$A$$ as $$PJP^{-1}$$ where $$J$$ is the $$2\times 2$$ Jordan normal form of a matrix with one defective eigenvalue $$\lambda$$. This matrix being,

$$\begin{equation}
J=\begin{bmatrix}\lambda&1\\0&\lambda\end{bmatrix}=\lambda I+\begin{bmatrix}0&1\\0&0\end{bmatrix}
\end{equation}$$

Denote the matrix $$\begin{bmatrix}0&1\\0&0\end{bmatrix}$$ as $$N$$. When $$J$$ is conjugated by $$P$$, we get

$$\begin{equation}
PJP^{-1}=\lambda I+PNP^{-1}
\end{equation}$$

So, once again, we need only ensure $$PNP^{-1}$$ is an integer matrix, and then we can adjust the eigenvalues by adding a scalar matrix.

One can verify that if $$\det P=\delta$$ and $$v$$ is the first column of $$P$$, then $$PNP^{-1}=\frac{1}{\delta}vv^\perp$$. This may seem problematic, as this will only be guaranteed to be an integer matrix if $$\delta=\pm1$$, but there is good news. Scaling the $$N$$ matrix has no effect on the one eigenvalue or eigenvector of the overall product. Because $$vv^\perp v=0$$, $$v$$ will always be an eigenvector with eigenvalue $$\lambda$$ of $$\lambda I+cvv^\perp$$ for all scalars $$c$$. We can then adjust $$c$$ until the solution $$x_2$$ is to our liking. Since smaller integers are generally nicer, $$c=\pm1$$ is usually the best choice.

If we multiply out $$Au_0$$ we get $$\lambda u+cvv^\perp u_0$$. Notice that $$v^\perp u_0=\det P$$. So $$Au_0=\lambda u_0+c\delta v$$. And... well that's it. We did it.

$$A(u_0+c\delta vt)e^{\lambda t}=(\lambda u_0+c\delta v+\lambda c\delta vt)e^{\lambda t}$$

which is indeed the derivative of $$x_2(t)=(u_0+c\delta vt)e^{\lambda t}$$, satisfying \eqref{xax}.

bodacious. 😏

## Complex Eigenvalues Derivation

Suppose we want a real matrix $$A$$ to satisfy \eqref{xax} where one solution is

$$\begin{equation}
x(t)=e^{\lambda t}(u_1\cos(\mu t)+u_2\sin(\mu t))
\end{equation}$$

Taking the derivative,

$$\begin{equation}
x'(t)=e^{\lambda t}((\lambda u_1+\mu u_2))\cos(\mu t)+(-\mu u_1+\lambda u_2)\sin(\mu t))
\end{equation}$$

So to satisfy \eqref{xax}, we have

$$\begin{equation}
Au_1=\lambda u_1+\mu u_2\quad Au_2=-\mu u_1+\lambda u_2
\end{equation}$$

So if we let $$u_1$$ and $$u_2$$ be the columns of $$P$$, then we have

$$\begin{equation}
A=P
\begin{bmatrix}
\lambda&-\mu\\
\mu&\lambda
\end{bmatrix}
P^{-1}
\end{equation}$$

Define the matrix

$$\begin{equation}
Q=
\begin{bmatrix}
0&-1\\
1&0
\end{bmatrix}
\end{equation}$$

We then have that

$$\begin{equation}
A=\lambda I+\mu PQP^{-1}
\end{equation}$$

Wonderful. We were expecting that $$A$$ would have complex eigenvalues $$\lambda\pm \mu i$$ which would be Gaussian integers, so we can disregard the $$\lambda I$$ and simply add it at the end. Therefore, without loss of generality, we assume that $$\lambda=0$$ and just try to make sure $$\mu PQP^{-1}\in\mathbb{Z}^{2\times 2}$$.

One cool fact to verify, that we mentioned before, is that the conjugation of any $$2\times 2$$ matrix $$X$$ by $$Q$$ yields the adjoint.

$$\begin{equation}
X^{adj}=Q^{-1}X^TQ
\end{equation}$$

So by letting $$\delta=\det(P)$$, as usual, we may therefore write $$A=\mu PQP^{-1}$$ as

$$\begin{equation}
A=\mu PQ\left(\frac{1}{\delta}Q^{-1}P^TQ\right)=\frac{\mu}{\delta}PP^TQ
\end{equation}$$

We don't have to worry about $$Q$$ changing an integer matrix into a noninteger matrix or vice versa, so we need only focus on making sure

$$\begin{equation}
\frac{\mu}{\delta}PP^T\in\mathbb{Z}^{2\times 2}
\end{equation}$$

One can verify that the columns of $$P$$, $$u_1,u_2$$, correspond to $$\operatorname{Re}(v),\operatorname{Im}(v)$$ for some eigenvector of $$A$$, $$v\in\mathbb{Z}[i]^2$$.

Since $$v$$ is an eigenvector, any scalar multiple of $$v$$ should result in the same $$A$$. 

From now on, we denote the matrix corresponding to a complex vector $$v$$ as

$$\begin{equation}
P(v)=
\begin{bmatrix}
\operatorname{Re}(v)&\operatorname{Im}(v)
\end{bmatrix}
\end{equation}$$

It's possible to simulate the multiplication of $$v$$ by any complex scalar using the matrix $$P(v)$$.

$$\begin{equation} \label{complexmult}
\begin{bmatrix}
\operatorname{Re}(kv)&\operatorname{Im}(kv)
\end{bmatrix}=
\begin{bmatrix}
\operatorname{Re}(v)&\operatorname{Im}(v)
\end{bmatrix}
\begin{bmatrix}
\operatorname{Re}(k)&\operatorname{Im}(k)\\
-\operatorname{Im}(k)&\operatorname{Re}(k)
\end{bmatrix}
\end{equation}$$

Define

$$\begin{equation}
C(k)=\begin{bmatrix}
\operatorname{Re}(k)&\operatorname{Im}(k)\\
-\operatorname{Im}(k)&\operatorname{Re}(k)
\end{bmatrix}
\end{equation}$$

We can then rewrite \eqref{complexmult} as

$$\begin{equation}
P(kv)=P(v)C(k)
\end{equation}$$

Fun facts:

$$\begin{gather}
\det(C(k))=|k|^2\\
\implies\det(P(kv))=\det(P(v))|k|^2\\
C(k)^{adj}=C(k)^T\\
\implies C(k)C(k)^T=|k|^2I\\
\implies \frac{\mu}{\det(P(v))}P(v)P(v)^T=\frac{\mu}{\det(P(kv))}P(kv)P(kv)^T
\end{gather}$$

So what? Well, this means that if all the entries of $$P(v)P(v)^T$$ have a greatest common factor with $$\det(P(v))$$ larger than $$1$$, they will cancel with $$\det P$$ and reduce the entries. Additionally, it implies that there exists a different matrix $$P(kv)$$ corresponding to a scalar multiple of the eigenvector for which that _won't_ happen. 

Take for example, the eigenvector $$v=(2,-1+3i)$$. Looks perfectly fine, right? Wrong. With this eigenvector, $$P(v)P(v)^T$$ evaluates to

$$\begin{equation}
\begin{bmatrix}
2&0\\-1&3
\end{bmatrix}
\begin{bmatrix}
2&-1\\0&3
\end{bmatrix}=
\begin{bmatrix}
4&-2\\-2&10
\end{bmatrix}
\end{equation}$$

All the entries have a common factor of $$2$$. $$\det(P(v))=6$$ which is divisible by $$2$$, meaning there will be cancellation and reduction. But... what if we multiplied $$v$$ by $$\frac{1-i}{2}$$? :flushed:

$$\begin{equation}
v'=\frac{1-i}{2}v
\end{equation}$$

$$\begin{equation}
P(v')=\begin{bmatrix}
2&0\\-1&3
\end{bmatrix}
\begin{bmatrix}
\frac{1}{2}&-\frac{1}{2}\\
\frac{1}{2}&\frac{1}{2}
\end{bmatrix}=
\begin{bmatrix}
1&-1\\1&2
\end{bmatrix}
\end{equation}$$

Then

$$\begin{equation}
\begin{bmatrix}
1&-1\\1&2
\end{bmatrix}
\begin{bmatrix}
1&1\\-1&2
\end{bmatrix}=
\begin{bmatrix}
2&-1\\-1&5
\end{bmatrix}
\end{equation}$$

As expected, it's the first matrix we got divided by $$2$$. As we know, $$\frac{P(v)P(v)^T}{\det(P(v))}=\frac{P(v')P(v')^T}{\det P(v')}$$, but the latter requires no dividing out by $$2$$. Why does this happen with our original eigenvector? Well, it's because $$2=(1+i)(1-i)$$ and $$-1+3i=(1+i)(1+2i)$$, which is why I multiplied by $$\frac{1}{1+i}=\frac{1-i}{2}$$, _obviously_. Only an dum dumb wouldn't see that by inspection. :roll_eyes:

All kidding aside, this exemplifies a problem with constructing real matrices with complex eigenvectors corresponding to the smallest possible Gaussian integer eigenvalues. It's easy to not use a real eigenvector with a common factor because common factors over the integers are very easy to spot and check, but it's even easier to make up an arbitrary complex eigenvector for which the entries have a hidden Gaussian integer common factor, and have no idea until it becomes clear that the entries of $$P(v)P(v)^T$$ and $$\det(P(v))$$ have a real common factor. In our example, we had an eigenvector which looked alright. $$\det(P(v))$$ was $$6$$, but the real requirement for the matrix with that eigenvector to be in $$\mathbb{Z}^{2\times 2}$$ is that $$\mu$$ must be divisible by $$3$$, not $$6$$. Therefore, $$\det(P(v))$$ does _not_ always tell us the true divisibility requirement on the imaginary parts of the complex eigenvalues.

Luckily, there are a few facts we can use to (sometimes) determine if a given eigenvector $$v=(z_1,z_2)$$ is reduced or not. 

1. If the squared magnitudes of the eigenvector's entries are coprime, then the entries are coprime. As a bonus, if you compute them before multiplying $$P(v)P(v)^T$$, then the magnitudes will be the diagonal entries, and since the matrix is symmetric you need only multiply to get one of the off diagonal entries and then you also have the other. It also makes sense because if two entries of $$P(v)P(v)^T$$ are coprime, there is no common factor to the whole matrix.

2. If the greatest common factor, $$g$$, of 
$$\det (P(v)), |z_1| ^2, |z_2| ^2$$ 
is greater than $$1$$, then all of the entries of $$P(v)P(v)^T$$ are divisible by $$g$$.

### Proof of 2:

Given the vector $$v=(z_1,z_2)\in\mathbb{Z}[i]^2$$, suppose that the greatest common factor of 
$$\det (P(v)), |z_1| ^2, |z_2| ^2$$
is $$g>1$$.

The following two facts are not difficult to verify.

$$\begin{equation}
\det(P(v))=-\operatorname{Im}(z_1\overline{z_2})
\end{equation}$$

$$\begin{equation}
P(v)P(v)^T=
\begin{bmatrix}
|z_1|^2&\operatorname{Re}(z_1\overline{z_2})\\
\operatorname{Re}(z_1\overline{z_2})&|z_2|^2
\end{bmatrix}
\end{equation}$$

We can then use the relationship

$$\begin{gather*}
(\operatorname{Re}(z_1\overline{z_2}))^2+(-\operatorname{Im}(z_1\overline{z_2}))^2=|z_1\overline{z_2}|^2\\
((P(v)P(v)^T)_{12})^2+(\det (P(v)))^2=|z_1| ^2 |z_2| ^2\\
((P(v)P(v)^T)_{12})^2\bmod{g}+(\det (P(v)))^2\bmod{g}=|z_1| ^2 |z_2| ^2\bmod{g}\\
((P(v)P(v)^T)_{12})^2\bmod{g}+0=0\\
((P(v)P(v)^T)_{12})^2\bmod{g}=0\\
\end{gather*}$$

Therefore, $$(P(v)P(v)^T) _{12}$$ and by extension $$(P(v)P(v)^T) _{21}$$ are divisible by $$g$$, and there will be cancellation in all of the entries of $$\frac{1}{\det(P(v))}P(v)P(v)^T$$.

Note that this also shows that if $$\det(P(v))$$ is not divisible by the GCF of 
$$|z_1| ^2, |z_2| ^2$$ then the entries $$PP^T$$ will not have a common factor greater than $$1$$. So a vector like $$v=(1+2i,1+3i)$$ will not end up reducing, despite the fact that the greatest common factor of the magnitudes squared is $$5$$.  This is because $$\det(P(v))=1$$ which is not divisible by $$5$$.
