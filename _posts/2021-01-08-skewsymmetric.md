---
layout: page
title: Skew-Symmetric Matrices Are Cool
date: 2021-01-08 
description: top 10 things YOU didn't know about real skew-symmetric matrices!!! (GONE WRONG) (COPS CALLED)
comments: true
importance: 2
categories: linear-algebra
---

I was messing around with skew-symmetric matrices and derived some really interesting facts about them. If you have no idea why your Linear Algebra instructor ever mentioned them, perhaps this will convince you that they are arguably just as cool as symmetric matrices.
$$\newcommand{\a}{\alpha  }$$
$$\newcommand{\b}{\beta  }$$
$$\newcommand{\Re}{\operatorname{Re}}$$
$$\newcommand{\Im}{\operatorname{Im}}$$
$$\newcommand{\conj}[1]{\overline{#1}}$$

---

Let $$Q$$ be a real $$n\times n$$ skew-symmetric matrix. Most of the time, we will assume $$Q$$ is nonzero.

\begin{equation}
Q^T=-Q
\end{equation}

We are going to use the following theorem so often I think it's worth stating up front.

Theorem 0:
-
---

For all $$x,y\in\mathbb{C}^n$$,

\begin{equation}
x\cdot (Qy)=-y\cdot (Qx)
\end{equation}

Which is equivalent to

\begin{equation}
x^TQy=-y^TQx
\end{equation}

---

Proof:

We examine

\begin{equation}
x^TQy
\end{equation}

This is a $$1\times1$$ matrix, and therefore symmetric,

$$\begin{align}
x^TQy&=(x^TQy)^T\\
x^TQy&=y^TQ^Tx\\
x^TQy&=-y^TQx\quad \blacksquare
\end{align}$$

Theorem 1:
-
---
If $$\lambda$$ is an eigenvalue of $$Q$$, then $$\lambda$$ is purely imaginary. Its conjugate is also an eigenvalue, and the eigenvector's conjugate will be the eigenvector for the conjugate eigenvalue.

\begin{equation}
\Re(\lambda)=0
\end{equation}

---

Proof:

Suppose $$w$$ is an eigenvector of $$Q$$.

\begin{equation} \label{eigenvector}
Qw=\lambda w
\end{equation}

Consider

\begin{equation} \label{conj Q}
\conj{w}^TQw
\end{equation}

\begin{equation}
\conj{w}^TQw=\lambda \conj{w}^Tw=\lambda |w|^2
\end{equation}

By Theorem 0,

\begin{equation}
\conj{w}^TQw=-w^TQ\conj{w}
\end{equation}

If we take the conjugate of \eqref{eigenvector}, using the fact that $$Q$$ is real,

$$\begin{gather}
\conj{Qw}=\conj{\lambda w}\\
Q\conj{w}=\conj{\lambda} \conj{w}
\end{gather}$$

Therefore,

\begin{equation}
\conj{w}^TQw=-\conj{\lambda}w^T\conj{w}=-\conj{\lambda}|w|^2
\end{equation}

Equating both results,

\begin{equation}
\lambda=-\conj{\lambda}
\end{equation}

This is clearly only possible if $$\lambda$$ has a real part of zero. It follows that if $$\lambda$$ is real, then it must be zero. $$\blacksquare$$

Theorem 2:
-
---

$$Q$$ is normal, and is therefore always diagonalizable by a unitary matrix. It follows that, $$Q$$ also has no defective eigenvalues.

---

Proof:

A matrix is normal if it commutes with its conjugate transpose. Since $$Q$$ is a real skew-symmetric matrix

\begin{equation}
Q^*=-Q
\end{equation}

So if we consider $$Q^*Q$$ and $$QQ^*$$,

$$\begin{align}
Q^*Q&=-QQ&&QQ^*=Q(-Q)\\
Q^*Q&=-Q^2&&QQ^*=-Q^2\\
\end{align}$$

$$\begin{equation}
Q^*Q=QQ^*\quad\blacksquare
\end{equation}$$

Theorem 3:
-
---
If $$n$$ is odd, then $$Q$$ is singular.

---

Proof:

\begin{equation}
\det(Q)=\det(Q^T)=\det(-Q)=(-1)^n\det(Q)
\end{equation}

If $$n$$ is odd, then we get $$\det(Q)=-\det(Q)\implies \det(Q)=0\quad \blacksquare$$

Theorem 4:
-
---
The rank of $$Q$$ must be even.

\begin{equation}
\operatorname{rank}(Q)=2r,\quad r\in\mathbb{N}_0
\end{equation}

---

Proof:

Because all of $$Q$$'s nonzero eigenvalues are complex, they come in conjugate pairs. Since $$Q$$ is diagonalizable, its rank is equal to the number of nonzero eigenvalues. Since they come in pairs, the rank must be even $$\blacksquare$$.

Eigenvector Stuff
-

Suppose $$Q$$ is rank $$2r$$. Without loss of generality, let $$\{w_1,\ldots,w_r\}$$ be $$r$$ linearly independent complex eigenvectors associated with purely imaginary nonzero eigenvalues $$i\lambda_j$$, where 
$$\lambda_j=|\lambda_j|$$ 
(i.e. we choose the eigenvectors associated with the eigenvalues with a positive imaginary part. The other nonzero eigenvalues and their eigenvectors are just conjugates of the ones we are choosing to focus on).

\begin{equation}
Qw_j=\lambda_jiw_j\quad1\leq j\leq r
\end{equation}

Then

\begin{equation} \label{complex eigenvectors}
Q\Re (w_j)=-\lambda_j\Im (w_j)\quad Q\Im (w_j)=\lambda_j\Re (w_j)\quad1\leq j\leq r
\end{equation}

Proof:

$$\begin{gather}
Q(\Re(w_j)+i\Im(w_j))=\lambda_ji(\Re(w_j)+i\Im(w_j))\\
Q\Re(w_j)+iQ\Im(w_j)=-\lambda_j\Im(w_j)+i\lambda_j\Re(w_j)\\
\implies Q\Re(w_j)=-\lambda_j\Im(w_j),\quad Q\Im(w_j)=\lambda_j\Re(w_j) \quad\blacksquare
\end{gather}$$

Let us define

$$\begin{gather}
\Re (w_j)=\a _j\\
\Im (w_j)=\b_j
\end{gather}$$

We also suppose $$Q$$ has $$n-2r$$ linearly independent vectors in its null space $$v _j$$

\begin{equation}
Qv _j=0\quad 0\leq j\leq n-2r
\end{equation}

Then $$\{\a _1,\b_1,\ldots,\a _r,\b_{r},v_1,\ldots,v_{n-2r}\}$$ is a basis of $$\mathbb{R}^n$$.

Now suppose

$$\begin{equation}
x=c_1\a _1+c_2\b_1+\ldots+c_{2r-1}\a _r+c_{2r}\b_r+c_{2r+1}v_1+\ldots+c_{n}v_{n-2r}
\end{equation}$$

$$\begin{equation}\label{Qx}
Qx=-c_1\lambda_1\b_1+c_2\lambda_1\a _1+\ldots-c_{2r-1}\lambda_r\b_r+c_{2r}\lambda_r\a _r
\end{equation}$$

Therefore, a basis for $$\operatorname{col}(A)$$ is $$\{\a _1,\b_1,\ldots,\a _r,\b_{r}\}$$.

Theorem 5:
-

\begin{equation}
x^TQx=0 \;\forall \,x\in\mathbb{C}^n
\end{equation}

Proof:

By Theorem 0,

$$\begin{gather}
x^TQx=-x^TQx\\
\implies x^TQx=0\quad \blacksquare
\end{gather}$$

Corrolary 5.1:
-
---

$$Qx$$ is a vector orthogonal to $$x$$.

\begin{equation}
x\cdot (Qx)=0
\end{equation}

---

Proof:

\begin{equation}
x\cdot (Qx)=x^T(Qx)=x^TQx=0\quad \blacksquare
\end{equation}

This gives us an explicit formula for a vector orthogonal to any vector in $$\mathbb{R}^2$$, since there's really only one $$2\times2$$ skew-symmetric matrix (that is to say the subspace of skew-symmetric $$2\times2$$ matrices is one-dimensional).

$$\begin{equation}
Qv=\begin{bmatrix}0&1\\-1&0\end{bmatrix}\begin{bmatrix}v_1\\v_2\end{bmatrix}=\begin{bmatrix}v_2\\-v_1\end{bmatrix}
\end{equation}$$

This particular $$Q$$ represents a $$90^\circ$$ rotation, and it makes intuitive sense that this would create a vector orthogonal to the original, since the resulting vector has an angle of $$90^\circ$$ to the original.

Mega Theorem 6:
-

---
$$\begin{align}
|\lambda_j|\neq|\lambda_k|\implies &w_j\cdot w_k=0\\
&\alpha_j\cdot \alpha_k=0\\
&\alpha_j\cdot \beta_k=0\\
&\b_j\cdot \b_k=0\\
\end{align}$$

Additionally,

$$\begin{gather}
|\alpha_j|=|\beta_j|\\
\alpha_j\cdot \beta_j=0
\end{gather}$$

---

Proof:

Suppose 
$$|\lambda_j|\neq|\lambda_k|$$ 
where $$\lambda_j\neq0$$ and $$\lambda_k\neq0$$.

$$\begin{equation}
w_j^TQw_k=\lambda_kiw_j^Tw_k=\lambda_ki(w_j\cdot w_k)
\end{equation}$$

By Theorem 0,

$$\begin{gather}
w_j^TQw_k=-w_k^TQw_j\\
w_j^TQw_k=-\lambda_ji(w_j\cdot w_k)\\
\lambda_ki(w_j\cdot w_k)=-\lambda_ji(w_j\cdot w_k)
\end{gather}$$

Since $$\lambda_ji\neq\lambda_ki$$,

$$\begin{equation}
w_j^TQw_k=0
\end{equation}$$

and

$$\begin{equation}
w_j\cdot w_k=0\quad \blacksquare
\end{equation}$$

Consider 

$$\begin{gather}
w_j^TQw_k=0\\
(\alpha_j+i\beta_j)^TQ(\alpha_k+i\beta_k)=0\\
\alpha_j^TQ\alpha_k-\beta_j^TQ\beta_k+i\left(\alpha_j^TQ\beta_k+\beta_j^TQ\alpha_k\right)=0
\end{gather}$$

Use $$a+bi=0\implies a=b=0$$

$$\begin{equation}
\implies \alpha_j^TQ\alpha_k-\beta_j^TQ\beta_k=0,\quad \alpha_j^TQ\beta_k+\beta_j^TQ\alpha_k=0
\end{equation}$$

$$\begin{align}
\alpha_j^TQ\alpha_k&=\beta_j^TQ\beta_k&\alpha_j^TQ\beta_k&=-\beta_j^TQ\alpha_k\\
-\lambda_k\alpha_j^T\beta_k&=\lambda_k\beta_j^T\alpha_k&
\lambda_k\alpha_j^T\alpha_k&=\lambda_k\beta_j^T\beta_k\\
-\lambda_k(\alpha_j\cdot\beta_k)&=\lambda_k(\beta_j\cdot\alpha_k)&
\lambda_k(\alpha_j\cdot\alpha_k)&=\lambda_k(\beta_j\cdot\beta_k)\\
\end{align}$$

Applying Theorem 0,

$$\begin{align}
-\alpha_k^TQ\alpha_j&=-\beta_k^TQ\beta_j&
-\beta_k^TQ\alpha_j&=\alpha_k^TQ\beta_j\\
\lambda_j(\alpha_k^T\beta_j)&=-\lambda_j(\beta_k^T\alpha_j)&
\lambda_j(\beta_k^T\beta_j)&=-\lambda_j(\alpha_k^T\alpha_j)\\
\lambda_j(\beta_j\cdot\alpha_k)&=-\lambda_j(\alpha_j\cdot\beta_k)&
\lambda_j(\beta_j\cdot\beta_k)&=\lambda_j(\alpha_j\cdot\alpha_k)\\
\end{align}$$

This yields

$$\begin{align}
-\lambda_k(&\alpha_j\cdot\beta_k)=\lambda_k(\beta_j\cdot\alpha_k)=\lambda_j(\beta_j\cdot\alpha_k)=-\lambda_j(\alpha_j\cdot\beta_k)\\
\lambda_k(&\alpha_j\cdot\alpha_k)=\lambda_k(\beta_j\cdot\beta_k)=\lambda_j(\beta_j\cdot\beta_k)=\lambda_j(\alpha_j\cdot\alpha_k)
\end{align}$$

Therefore, if $$\lambda_j\neq\lambda_k$$

$$\begin{align}
\lambda_k(\beta_j\cdot\alpha_k)=\lambda_j(\beta_j\cdot\alpha_k)&\implies \beta_j\cdot\alpha_k=\alpha_j\cdot\beta_k=0&\blacksquare\\
\lambda_k(\beta_j\cdot\beta_k)=\lambda_j(\beta_j\cdot\beta_k)&\implies \beta_j\cdot\beta_k=\alpha_j\cdot\alpha_k=0&\blacksquare\\
\end{align}$$

Additionally, if $$j=k$$, then

$$\begin{align}
-\lambda_k(\alpha_k\cdot\beta_k)=\lambda_k(\beta_k\cdot\alpha_k)&\implies \alpha_k\cdot\beta_k=0&\blacksquare\\
\lambda_k(\alpha_k\cdot\alpha_k)=\lambda_k(\beta_k\cdot\beta_k)&\implies |\alpha_k|=|\beta_k|&\blacksquare
\end{align}$$

Corollary 6.1:
-
---
$$\begin{equation}
\{\a _1,\b_1,\ldots,\a _r,\b_{r}\}
\end{equation}$$

is an orthogonal basis for $$\operatorname{col}(A)$$.

---

Theorem 7:
-
---
\begin{equation}
w_j\cdot v_k=0
\end{equation}

---

Proof:

$$\begin{gather}
w_j^TQv_k=w_j^T(0)=0\\
w_j^TQv_k=-v_k^TQw_j\\
w_j^TQv_k=-i\lambda_jv_k^Tw_j=-i\lambda_j(v_k\cdot w_j)\\
-i\lambda_j(v_k\cdot w_j)=0
\end{gather}$$

Since $$-i\lambda_j\neq0$$, $$(v_k\cdot w_j)=0\quad \blacksquare$$

Corollary 7.1
-
---
\begin{equation}
v_k\cdot\a _j=v_k\cdot\b_j=0
\end{equation}

---

Proof:

$$\begin{gather}
v_k\cdot w_j=0\\
v_k\cdot (\a _j+i\b_j)=0\\
(v_k\cdot\a _j)+i(v_k\cdot\b_j)=0
\end{gather}$$

Both the real and imaginary parts have to be zero.

\begin{equation}
\therefore v_k\cdot\a _j=0\quad v_k\cdot\b_j=0\quad\blacksquare
\end{equation}

Using theorem 6 and 7 as well as their corrolaries, we get 

Corollary 7.2
-
---
$$\{\a _1,\b_1,\ldots,\a _r,\b_{r},v_1,\ldots,v_{n-2r}\}$$ is an orthogonal basis of $$\mathbb{R}^n$$

---

Theorem 8:
-
---
Define

$$\begin{gather}
P=\begin{bmatrix}
\frac{\a _1}{|\a _1|}&
\frac{\b_1}{|\b_1|}&\dots&
\frac{\a _r}{|\a _r|}&
\frac{\b_r}{|\b_r|}&
\frac{v_1}{|v_1|}&\dots&
\frac{v_{n-2r}}{|v_{n-2r}|}\end{bmatrix}\\
\Sigma=\begin{bmatrix}
0&\lambda_1&\dots&0&0&\dots&0\\
-\lambda_1&0&\dots&0&0&\dots&0\\
\vdots&\vdots&\ddots&\vdots&\vdots&\dots&0\\
0&0&\dots&0&\lambda_r&\dots&0\\
0&0&\dots&-\lambda_r&0&\dots&0\\
0&0&\dots&0&0&\dots&0\\
\vdots&\vdots&\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&\dots&0&0&\dots&0
\end{bmatrix}
\end{gather}$$

Then

\begin{equation}
Q=P\Sigma P^T
\end{equation}

This actually follows directly from \eqref{Qx} and the fact that $$P$$ is an orthogonal matrix (by Corollary 7.2 and the fact that the columns are normalized). $$P^T$$ is a change of basis to the orthonormal basis from Corollary 7.2, $$\Sigma$$ is the matrix transformation of $$Q$$ on that basis, and $$P$$ undoes the change of basis.

---

Corrolary 8.1:
-
---
\begin{equation}
Q=\frac{\lambda_1}{|\a _1||\b_1|}(\a _1\b_1^T-\b_1\a _1^T)+\ldots+
\frac{\lambda_r}{|\a _r||\b_r|}(\a _r\b_r^T-\b_r\a _r^T)
\end{equation}

---

Proof:

Define $$e_i$$ to be the column vector with zeros in all entries except for the $$i$$-th row.

We rewrite $$\Sigma$$ as

\begin{equation} \label{spectral}
\Sigma=\lambda_1(e_1e_2^T-e_2e_1^T)+\ldots+\lambda_r(e_{2r-1}e_{2r}^T-e_{2r}e_{2r-1}^T)
\end{equation}

Distribute $$P$$ on the left and $$P^T$$ on the right.

$$\begin{gather}
P\Sigma P^T=\lambda_1(Pe_1e_2^TP^T-Pe_2e_1^TP^T)+\ldots+\lambda_r(Pe_{2r-1}e_{2r}^TP^T-Pe_{2r}e_{2r-1}^TP^T)\\
Q=\lambda_1\left(\frac{\a _1}{|\a _1|}\frac{\b_1^T}{|\b_1|}-\frac{\b_1}{|\b_1|}\frac{\a _1^T}{|\a _1|}\right)+\ldots+
\lambda_r\left(\frac{\a _r}{|\a _r|}\frac{\b_r^T}{|\b_r|}-\frac{\b_r}{|\b_r|}\frac{\a _r^T}{|\a _r|}\right)
\end{gather}$$

By pulling the magnitudes from the denominator we get \eqref{spectral}. $$\blacksquare$$

Corrolary 8.2:
-
---

If $$\operatorname{rank}(Q)=2$$, then $$Q^3=-\lambda^2Q$$ where $$\pm\lambda i$$ are the nonzero eigenvalues of $$Q$$.

$$\begin{equation}
\operatorname{rank}(Q)=2\implies Q^3=-\lambda^2Q
\end{equation}$$

---

Proof:

Suppose $$\operatorname{rank}(Q)=2$$. If the nonzero eigenvalues of $$Q$$ are $$\lambda i,-\lambda i$$, and $$\a+i\b$$ is a complex eigenvector of $$Q$$ for unit vectors $$\a$$ and $$\b$$, then we may write $$Q$$ as

$$\begin{equation}
Q=\lambda(\a \b^T-\b\a^T)
\end{equation}$$

Now consider $$Q^3$$,

$$\begin{equation}
Q^3=\lambda^2Q(\a \b^T-\b\a^T)(\a \b^T-\b\a^T)
\end{equation}$$

Using the orthogonality of $$\a$$ and $$\b$$,

$$\begin{equation}
Q^3=\lambda^2Q(-\a \b^T\b\a^T-\b\a^T\a \b^T)
\end{equation}$$

$$\begin{equation}
Q^3=-\lambda^2Q(|b|^2\a \a^T+|a|^2\b\b^T)
\end{equation}$$

Because $$\a$$ and $$\b$$ are unit vectors,

$$\begin{equation}
Q^3=-\lambda^2Q(\a \a^T+\b\b^T)
\end{equation}$$

$$\begin{equation}
Q^3=-\lambda^3(\a \b^T-\b\a^T)(\a \a^T+\b\b^T)
\end{equation}$$

$$\begin{equation}
Q^3=-\lambda^3(\a \b^T\b\b^T-\b\a^T\a \a^T)
\end{equation}$$

$$\begin{equation}
Q^3=-\lambda^2\left(\lambda(\a\b^T-\b\a^T)\right)
\end{equation}$$

$$\begin{equation}
Q^3=-\lambda^2Q\quad \blacksquare
\end{equation}$$

This result applies to all real $$2\times 2$$ and $$3\times 3$$ skew-symmetric matrices since their maximum rank is two.

Theorem 9:
-
---

$$Q^2$$ is a symmetric negative semi-definite matrix.

\begin{equation} 
(Q^2)^T=Q^2,\quad x^TQ^2x\leq 0
\end{equation}

---

Proof:

First we consider

\begin{equation} 
(Q^2)^T=(Q^T)^2=(-Q)^2=Q^2\quad \blacksquare
\end{equation}

Next, we examine

$$\begin{gather} 
x^TQ^2x=x^TQQx=(-Qx)^T(Qx)=-|Qx|^2
\end{gather}$$

The negative of a real square quantity is less than or equal to zero, proving $$x^TQ^2x\leq 0\quad \blacksquare$$

Now we go into some neat properties of $$2\times2$$ and $$3\times 3$$ skew-symmetric matrices.

Theorem 10:
-
---

If $$Q$$ is a real nonzero $$3\times 3$$ skew-symmetric matrix, and for some nonzero vector $$v$$, $$Qv=0$$, then for some $$k\in\mathbb{R}$$ and any vector $$x\in\mathbb{R}^{3}$$

\begin{equation} 
Qx=k(v\times x)
\end{equation}

---

Proof:

Consider

\begin{equation}
x\cdot (Qx)=x^T(Qx)
\end{equation}

By Theorem 5,

\begin{equation}
x^TQx=0
\end{equation}

Therefore,

$$\begin{equation}
x\cdot (Qx)=0
\end{equation}$$

Next, consider 

$$\begin{gather}
v\cdot (Qx)=v^T(Qx)\\
v\cdot (Qx)=-(Qv)^Tx\\
v\cdot (Qx)=0\quad \blacksquare\\
\end{gather}$$

Therefore, $$Qx$$ is orthogonal to both $$v$$ and $$x$$.

This means that one admittedly strange way to compute a cross product of some vector $$v=(v_1,v_2,v_3)$$ with any other vector $$x$$ would be to compute the product of the vector $$x$$ multiplied on the left by the matrix

$$\begin{equation}
Q=\begin{bmatrix}
0&v_3&-v_2\\
-v_3&0&v_1\\
v_2&-v_1&0
\end{bmatrix}
\end{equation}$$

Another strange result of this is:

Corollary 10.1:
-
---

If $$Q$$ is a real nonzero $$3\times 3$$ skew-symmetric matrix, and for some nonzero vector $$v$$, $$Qv=0$$, then for any nonzero vector $$x\in\mathbb{R}^3$$ which is not a scalar multiple of $$v$$,

\begin{equation} 
w=\frac{Qx}{|Qx|}+i\frac{Q^2x}{|Q^2x|}
\end{equation}

is a complex eigenvector of $$Q$$.

---

Proof:

$$\begin{equation} 
Qw=\frac{Q^2x}{|Qx|}+i\frac{Q^3x}{|Q^2x|}
\end{equation}$$

Using Corollary 8.2,

$$\begin{equation} 
Qw=\frac{Q^2x}{|Qx|}-i\frac{\lambda^2Qx}{|Q^2x|}
\end{equation}$$

$$\begin{equation} \label{10.1 tbc}
Qw=-i\frac{\lambda^2|Qx|}{|Q^2x|}\left(\frac{Qx}{|Qx|}\right)-i\frac{|Q^2x|}{|Qx|}\left(i\frac{Q^2x}{|Q^2x|}\right)
\end{equation}$$

Consider

$$\begin{align} 
|Q^2x|^2&=(Q^2x)^T(Q^2x)\\
|Q^2x|^2&=x^TQ^4x\\
|Q^2x|^2&=x^T(-\lambda^2Q)Qx\\
|Q^2x|^2&=\lambda^2x^TQ^TQx\\
|Q^2x|^2&=\lambda^2(Qx)^T(Qx)\\
|Q^2x|^2&=\lambda^2|Qx|^2\\
|Q^2x|&=\lambda|Qx|
\end{align}$$

Substituting into \eqref{10.1 tbc},

$$\begin{equation} 
Qw=-i\lambda\left(\frac{Qx}{|Qx|}\right)-i\lambda\left(i\frac{Q^2x}{|Q^2x|}\right)
\end{equation}$$

$$\begin{equation} 
Qw=-i\lambda\left(\frac{Qx}{|Qx|}+i\frac{Q^2x}{|Q^2x|}\right)
\end{equation}$$

$$\begin{equation} 
Qw=-i\lambda w\quad \blacksquare
\end{equation}$$

The following is a way to construct $$2\times2$$ matrices with desired eigenvalues and eigenvectors in terms of them and skew symmetric matrices. We assume that $$Q$$ is nonzero.

Theorem 11:
-
---

The matrix

$$\begin{equation}
\exp(Q)
\end{equation}$$

is orthogonal.

---

Proof:

$$\begin{gather}
\exp(Q)^T=\exp(Q^T)=\exp(-Q)=\exp(Q)^{-1}\quad \blacksquare
\end{gather}$$

Theorem 12:
-
---

1. If $$A$$ is a diagonalizable $$2\times2$$ with linearly independent eigenvectors $$v_1,v_2$$ associated with eigenvalues $$\lambda_1,\lambda_2$$,

$$\begin{equation}
A=\frac{\lambda_1v_1v_2^T-\lambda_2v_2v_1^T}{v_2^TQv_1}Q
\end{equation}$$

2. If $$A$$ is a $$2\times2$$ with a defective eigenvalue $$\lambda$$, $$v$$ is an eigenvector, and $$w$$ is a generalized eigenvector of rank 2,

$$\begin{equation}
A=\lambda I+\frac{vv^T}{v^TQw}Q
\end{equation}$$

3. If $$A$$ is a real $$2\times 2$$ with complex eigenvalues $$\lambda=a\pm bi$$ and eigenvector $$v=\alpha+\beta i$$ associated with $$\lambda=a+bi$$ for $$\alpha,\beta\in\mathbb{R}^2$$,

$$\begin{equation}
A=a I+b\frac{\alpha\alpha^T+\beta\beta^T}{\alpha^TQ\beta}Q
\end{equation}$$

---

Proof:

We multiply each by the eigenvectors.

1. $$\begin{align}
Av_1&=\frac{\lambda_1v_1v_2^TQv_1-\lambda_2v_2v_1^TQv_1}{v_2^TQv_1}&Av_2&=\frac{\lambda_1v_1v_2^TQv_2-\lambda_2v_2v_1^TQv_2}{v_2^TQv_1}\\
Av_1&=\frac{\lambda_1v_1(v_2^TQv_1)}{v_2^TQv_1}&Av_2&=\frac{-\lambda_2v_2v_1^TQv_2)}{v_2^TQv_1}\\
Av_1&=\frac{\lambda_1v_1(v_2^TQv_1)}{v_2^TQv_1}&Av_2&=\frac{-\lambda_2v_2(-v_2^TQv_1)}{v_2^TQv_1}\\
Av_1&=\lambda_1v_1&Av_2&=\lambda_2v_2\quad \blacksquare\\
\end{align}$$

2. $$\begin{align}
Av&=\lambda Iv+\frac{vv^TQv}{v^TQw}&Aw&=\lambda Iw+\frac{vv^TQw}{v^TQw}\\
Av&=\lambda v&Aw&=\lambda w + v\quad \blacksquare\\
\end{align}$$

3. $$\begin{align}
A(\alpha+\beta i)&=a I(\alpha+\beta i)+b\frac{\big[\alpha\alpha^TQ\alpha+\beta\beta^TQ\alpha\big ]+i\big[\alpha\alpha^TQ\beta+\beta\beta^TQ\beta\big ]}{\alpha^TQ\beta}\\
A(\alpha+\beta i)&=a(\alpha+\beta i)+b\frac{\big[\beta\beta^TQ\alpha\big ]+i\big[\alpha\alpha^TQ\beta\big ]}{\alpha^TQ\beta}\\
A(\alpha+\beta i)&=a(\alpha+\beta i)+b\frac{\big[\beta(-\alpha^TQ\beta)\big ]+i\big[\alpha(\alpha^TQ\beta)\big ]}{\alpha^TQ\beta}\\
A(\alpha+\beta i)&=a(\alpha+\beta i)+b(i\alpha-\beta)\\
A(\alpha+\beta i)&=a(\alpha+\beta i)+bi(\alpha+\beta i)\\
A(\alpha+\beta i)&=(a+bi)(\alpha+\beta i)\\
\end{align}$$

If we take the conjugate of the last line, using the fact that $$A$$ is real,

$$\begin{align}
\conj{A(\alpha+\beta i)}&=\conj{(a+bi)(\alpha+\beta i)}\\
\conj{A}\conj{(\alpha+\beta i)}&=\conj{(a+bi)}\;\conj{(\alpha+\beta i)}\\
A(\alpha-\beta i)&=(a-bi)(\alpha-\beta i),\quad\blacksquare\\
\end{align}$$

For real matrices with complex eigenvectors, the conjugate of an eigenvector has the conjugate of the eigenvalue. Since this is the case, this concludes the proof.
