---
layout: distill
title: The Wonderful World of Projectors
date: 2024-03-23
description: They're cool, I promise!
comments: true
importance: 1
featured: true
tags: 
category: linear-algebra
authors:
  - name: Taylor Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Projectors
    subsections:
      - name: Idempotent Matrices
      - name: Eigenspaces of Projectors
      - name: Complementary Projectors
      - name: Orthogonal Projectors
  - name: Constructing Projector Matrices
    subsections:
      - name: Diagonalization
      - name: Rank one oblique projectors
      - name: Column space orthogonal projectors
  - name: Orthonormal Bases
    subsections:
      - name: Why are orthonormal bases so great?
      - name: Finding coefficients of a linear combination
      - name: Example
  - name: Unitary matrices
    subsections:
      - name: Fun facts about unitary matrices
  - name: Orthogonal Projections when you have an orthonormal basis
---

The following is my final presentation for my numerical linear algebra class (Spring 2023), the first graduate math course I ever took! I was really proud of it, and I feel like there's not enough good resources about projectors, which I think are really really cool.

For simplicity, we will let $$\mathbb{F}$$ be $$\mathbb{R}$$ or $$\mathbb{C}$$.

# Projectors

## Idempotent Matrices

**Definition:** A matrix $$P \in \mathbb{F}^{n \times n}$$ is said to be a **Projector** if $$P^2 = P$$. This matrix is also said to be 'idempotent'. We say that $$P$$ projects vectors *onto* $$\text{im}(P)$$ *along* $$\text{ker}(P)$$.

Note that the only invertible projector is the identity matrix (this is a simple thing to prove).

Why would this be the *definition* for a projector? What does $$P^2 = P$$ have to do with projections? The general idea is this: Say $$\mathbb{F}^{n}=W\oplus K$$, and we have $$P$$ projects onto $$W$$ along $$K$$. That means that every vector $$x$$ can be written in the form $$x=w+k$$ for some $$w\in W$$ and $$k\in K$$, this representation is unique, and we expect that $$Px=w$$ and $$Pw=w$$, implying that $$Px=Pw$$. This is because $$w$$ is already in $$W$$, so it shouldn't change under the projection. If we examine this more closely, it means that

$$P^2x=P(Px)=Pw=Px$$

$$\implies P^2x=Px$$

for all $$x$$. Therefore, a projector should satisfy $$P^2=P$$.

We remark that this construction of $$Pw=w$$ and $$Pk=0$$ implies that we can decompose $$\mathbb{F}^n$$ into a direct sum of the eigenspaces with eigenvalues $$1$$ and $$0$$. We will prove this shortly.

To summarize: $$P$$ takes in $$x$$ and outputs the component of $$x$$ in the direction of $$W$$ (or the component in $$W$$). Thus, repeatedly applying $$P$$ shouldn't change the output because the result is already *in* $$W$$.

It's not necessarily obvious that if $$P^2=P$$ then $$P$$ is a projector, however. To prove that, we need some more groundwork. Some questions we need to answer first: How do we know that $$\mathbb{F}^n$$ will be a direct sum of the image and kernel of $$P$$?

From this point on, we assume that $$P$$ satisfies $$P^2=P$$.

**Proposition:** $$\text{im}(P) \oplus \text{ker}(P) = \mathbb{F}^n$$

**Proof:** For all $$x \in \mathbb{F}^n$$,

$$x = Px + (x - Px)$$

$$P(x - Px) = Px - P^2x = Px - Px = 0$$ 

$$\implies x - Px \in \text{ker}(P)$$ 

Therefore, all $$x$$ can be written as the sum of some $$Px \in \text{im}(P)$$ and $$x - Px \in \text{ker}(P)$$. Thus, $$\mathbb{F}^n = \text{im}(P) + \text{ker}(P)$$. If

$$\begin{multline*}
v \in \text{im}(P) \cap \text{ker}(P) \\\implies v = Px \land Pv = 0 = P(Px) = Px = v \\\implies v = 0
\end{multline*}$$

Therefore,

$$\mathbb{F}^n = \text{im}(P) \oplus \text{ker}(P)$$

## Eigenspaces of Projectors

Since all but the trivial projector ($$I$$) are not invertible, then they usually have a nontrivial kernel, which is the eigenspace for zero. 

**Proposition:** The only eigenvalues for a projector $$P$$ are $$\lambda=0,1$$.

**Proof:** Suppose that $$\lambda$$ is an eigenvalue of $$P$$ with eigenvector $$v \neq 0$$. Then

$$Pv=\lambda v \implies P^2v=Pv=\lambda v=\lambda Pv=\lambda^2v$$

$$\implies (\lambda^2-\lambda) v=0 \implies \lambda=0,1$$

**Proposition:** For a projector $$P$$, the eigenspace for $$\lambda=1$$, $$E_1=\text{im}(P)$$.

**Proof:** Suppose $$v \in \text{im}(P)$$. Then there exists an $$x \in \mathbb{R}^n$$ such that

$$v=Px \implies Pv=P^2x=Px=v$$

Then $$Pv=v$$. If $$v \in \text{ker}(P)$$, then $$Pv=0=v$$. Thus, either $$v$$ is an eigenvector with eigenvalue $$1$$, or $$v=0$$. That is, $$\text{im}(P) \subseteq E_1$$.

The other direction is quite simple. If $$v$$ is an eigenvector with eigenvalue $$1$$, then $$Pv=v$$ implies $$v \in \text{im}(P)$$. Therefore,

$$\text{im}(P)=E_1$$

**Proposition:** All projectors are diagonalizable.

**Proof:** Since $$\text{im}(P)=E_1$$ and $$\text{ker}(P)=E_0$$, by Proposition, we can say that

$$\mathbb{F}^n=\text{im}(P) \oplus \text{ker}(P)=E_1 \oplus E_0$$

Since $$\mathbb{F}^n$$ is a direct sum of eigenspaces of $$P$$, then $$P$$ must be diagonalizable (as this implies there exists a basis of eigenvectors).

For a slightly slicker and less intuitive proof (something I definitely love), we can also use that

$$P^2=P \implies P^2-P=P(P-I)=0$$

A rather obscure linear algebra factoid: $$A$$ is diagonalizable if and only if there is some polynomial $$f(x)$$ that is a product of distinct linear factors such that $$f(A)=0$$. This is basically saying that a matrix is diagonalizable matrix if its minimal polynomial is a product of distinct linear factors (we only want Jordan blocks of size 1).

Hence, if $$f(x)=x(x-1)$$, which is a product of distinct linear factors, then $$f(P)=0$$. Since such a polynomial exists, that is enough to prove $$P$$ is diagonalizable.

## Complementary Projectors

**Theorem:** Suppose $$P$$ is the projector onto the subspace $$W \leq \mathbb{F}^n$$, and let $$K=\ker(P)$$. We previously proved that $$\mathbb{F}^n=W \oplus K$$, so for all vectors $$v \in \mathbb{F}^n$$, $$v$$ can be written uniquely as a linear combination

$$v=w+k$$

where $$w \in W$$ and $$k \in K$$.

How can we find $$w$$ and $$k$$? To find $$w$$, we can use the projector $$P$$ for $$W$$. But what about $$k$$? To find it, we can do

$$k=v-w=v-Pv=(I-P)v$$

We can verify as well that $$I-P$$ is indeed also a projector.

$$\begin{multline*}
(I-P)^2=I^2-2P+P^2\\=I-2P+P=I-P
\end{multline*}$$

Therefore, we define the complementary projector of $$P$$ as follows:

**Definition:** The **complementary projector** of the projector $$P$$ is $$I-P$$, which projects onto the kernel of $$P$$.

So if $$P$$ is a projector, it projects onto its image along its kernel. While $$I-P$$ is also a projector, which projects onto the kernel of $$P$$ along the image of $$P$$. It's a good exercise to convince yourself of this. If $$Pv=\lambda v$$, then what is $$(I-P)v$$? Then see what happens if $$\lambda=0,1$$.

If you look back at the proof for Proposition, you'll notice that we essentially wrote

$$x=Px+(I-P)x$$

which is writing $$x$$ as the sum of its component in $$\text{im}(P)$$ and its component in $$\text{im}(I-P)=\ker(P)$$.

## Orthogonal Projectors

**Definition:** A projector $$P$$ is an **orthogonal projector** if $$\ker(P)^\perp=\text{im}(P)$$. That is, if the subspace it is projecting onto is orthogonal to the subspace it is projecting along. If $$P$$ is not an orthogonal projector, then it is an **oblique** projector.

**Proposition:** A projector $$P$$ is an orthogonal projector if and only if $$P$$ is hermitian.

**Proof:** Suppose $$P \in \mathbb{F}^{n\times n}$$ is an orthogonal projection matrix. That is, $$\text{im}(P)$$ is the orthogonal complement to $$\ker(P)$$. Suppose $$\beta_i=\{v_1,\ldots,v_r\}$$ is an orthonormal basis for the image ($$E_1$$), and $$\beta_k=\{u_1,\ldots,u_k\}$$ is an orthonormal basis for the kernel ($$E_0$$). As we proved previously, $$\beta=\beta_i \cup \beta_k$$ is an eigenbasis for $$\mathbb{F}^n$$. But, since they are orthogonal complements, $$\beta$$ is an orthogonal basis. Since $$P$$ has an orthonormal eigenbasis, and it has purely real eigenvalues, then $$P$$ must be hermitian.

If $$P$$ is a hermitian projector, then its eigenspaces are orthogonal, because it is hermitian. Therefore, $$E_0^\perp=\ker(P)^\perp=E_1=\text{im}(P)$$. Hence, $$\ker(P)^\perp=\text{im}(P)$$. Therefore, $$P$$ is an orthogonal projector.

Since $$\ker(P)$$ is the orthogonal complement to $$\text{im}(P)$$, then $$I-P$$ is specifically the projection onto the orthogonal complement of $$\text{im}(P)$$. Thus, we get this next nice little corollary

**Corollary:** If $$P$$ is the orthogonal projector onto a subspace $$W$$, then $$I-P$$ is the orthogonal projector onto $$W^\perp$$.

## Constructing Projector Matrices

### Diagonalization
There are two ways to do this. If you have a basis for the image (suppose it is $$r$$ dimensional) and kernel (making sure the union is a basis for $$\mathbb{F}^n$$), then put the vectors as columns in a matrix $$M$$, and

$$P=M\begin{pmatrix}I_r & 0 \\ 0 & 0\end{pmatrix}M^{-1}$$

Which is... unwieldy at best. Especially since you actually need a basis for the kernel. But looking at it *this* way does make it a little more clear why $$P$$ is a projector. This essentially tells us we can get a basis for $$\mathbb{F}^n$$ which are either vectors in $$E_1$$ or in $$E_0$$. If we are in $$E_1$$, then $$P$$ doesn't change it (which is how a projection should act), and if we are anywhere else but $$E_1$$, then we are in $$E_0$$, so $$P$$ takes it to zero (also the way we would expect a projector to act).

This form also makes it a little more clear why $$I-P$$ is a projector. Since

$$I-P=M\begin{pmatrix}0 & 0 \\ 0 & I_{n-r}\end{pmatrix}M^{-1}$$

This is also pretty much one of the only ways to construct an oblique projector.

But this is generally not how we generally compute projectors.

### Rank one oblique projectors
A special case of this is when the subspace we are projecting along is one-dimensional. So suppose that $$w$$ is a basis for a one-dimensional subspace $$W$$, $$v$$ is a basis for the orthogonal complement of another $$n-1$$ dimensional subspace $$K$$ such that $$\mathbb{F}^n=W \oplus K$$, and $$v^*w \neq 0$$. Then

$$P=\frac{wv^*}{v^*w}$$

is the projector onto $$W$$ along $$K$$. You can also just start with any $$v$$ not orthogonal to $$w$$, and then the above matrix automatically projects onto $$W$$ along $$\text{span}\{v\}^\perp$$.

For example, 

$$P=\begin{pmatrix}1 \\ 1\end{pmatrix}\begin{pmatrix}3 & -2\end{pmatrix}=\begin{pmatrix}3 & -2 \\ 3 & -2\end{pmatrix}$$

is the oblique projector onto $$\text{span}\left\{\begin{pmatrix}1 \\ 1\end{pmatrix}\right\}$$ along $$\text{span}\left\{\begin{pmatrix}2 \\ 3\end{pmatrix}\right\}$$.

### Column space orthogonal projectors
The other way to construct a projector matrix is to use a basis for the image. Let's say we want $$P$$ to be a projector on a subspace $$W$$, and we have a basis $$\{v_1, \ldots, v_r\}$$ and we put them as the columns of a matrix $$A$$. Note that $$A$$ will have full column rank, so $$A^*A$$ will be invertible. Then 

$$P=A(A^*A)^{-1}A^*$$

**Proof:**
For all $$x \in \mathbb{F}^n$$, we can write

$$x=x_W+x_{W^\perp}$$

uniquely, where $$x_W \in W$$ and $$x_{W^\perp} \in W^\perp$$. Our goal is to find some projector $$P$$ such that $$Px=x_W$$.    
Since the columns of $$A$$ form a basis for $$W$$, then there exists some $$c \in \mathbb{F}^r$$ (the coordinate vector with respect to the basis) such that $$x_W=Ac$$. Multiplying $$x=x_W+x_{W^\perp}=Ac+x_{W^\perp}$$ on both sides by $$A^*$$, we obtain

$$A^*x=A^*Ac+A^*x_{W^\perp}=A^*Ac+0$$

Since the entries of $$A^*x_{W^\perp}$$ will be the inner product of vectors in $$W$$ with a vector in $$W^\perp$$, then that term zeros out. Because $$A$$ is full rank, then $$A^*A$$ is invertible so,

$$c=(A^*A)^{-1}A^*x $$

$$\implies A(A^*A)^{-1}A^*x = Ac = x_W$$

Therefore, $$P=A(A^*A)^{-1}A^*$$ is the projector.

Now, while I think it makes it a little less intuitive why this should be a projector, this is definitely *much* easier to compute. And it makes the fact that it satisfies $$P^2=P$$ pretty clear. Verify it!

The only thing to note is that this always produces an orthogonal projector (since we can see this matrix is Hermitian by inspection). But that is actually a good thing because orthogonal projectors are actually much better than oblique projectors.

Now, I think you'd agree that the $$A^*A$$ inverse is pretty annoying. How can we get rid of it? Well, the easiest way would be to ensure that $$A^*A=I$$. Then the projector is just $$AA^*$$. So, how can we construct a matrix such that $$A^{-1}=A^*$$? The answer is: use an orthonormal basis.

# Orthonormal Bases

**Definition:** A set of vectors is **orthogonal** if all of the vectors have inner product 0.

Note that an orthogonal set of vectors may not be linearly independent, because a set can have the zero vector and still be orthogonal. This is because the zero vector is orthogonal to all vectors. However, we *can* say it is linearly independent if all the vectors are nonzero. We won't prove this for an orthogonal set, but only for orthonormal sets. The proof is almost identical, however.

For the sake of simplicity, though, when we say a set is "orthogonal" we will assume all the vectors are nonzero.

**Definition:** A set is **orthonormal** if it is an orthogonal set and all of the vectors are unit vectors.

**Remark:** One way we notate an orthonormal basis is as follows: Suppose $$\{u_1, \ldots, u_n\}$$ is orthonormal, then 

$$\langle u_i, u_j \rangle = u_j^*u_i = 
\begin{cases} 
1, & i=j \\
0, & i \neq j
\end{cases}$$

**Theorem:** An orthonormal set is linearly independent.

**Proof:** Suppose $$\{v_1, \ldots, v_n\}$$ is an orthonormal set, and

$$c_1v_1 + \ldots + c_nv_n = 0$$

Dot both sides with $$v_i$$, and all terms will cancel except for $$v_i \cdot c_iv_i$$.

$$c_i(v_i \cdot v_i) = c_i||v_i||^2 = c_i = 0$$

Therefore, the vectors are linearly independent.

## Why are orthonormal bases so great?

Let's list some reasons:

1. We don't have to check linear independence to verify it's a valid basis. Only that we have the right number of unit vectors, and they are orthogonal. Orthogonality is much easier to check than linear independence or span.
2. If a square matrix has orthonormal columns, then the inverse is as almost as easy as it gets. It's just the adjoint! Even if it isn't square, it will be easy to cancel.
3. It is *extremely* easy to find the coefficients of a linear combination. We don't have to solve a system of equations.
4. It's really easy to project onto a subspace when you have an orthonormal basis for it.
5. Creating a projection matrix is *so much easier* if you have an orthonormal basis.
6. You can always make a basis orthonormal.

It is for these reasons that real symmetric/hermitian matrices are simply the best matrices, objectively. Because they are guaranteed to have an orthonormal eigenbasis. And we all know that an eigenbasis is the best basis, so an orthonormal eigenbasis is as good as it gets.

The other classes of normal matrices (matrices which are unitarily diagonalizable) are also good for similar reasons (Unitary matrices are also fantastic), but *their* eigenvalues aren't guaranteed to be real.

### Finding coefficients of a linear combination

Imagine we have some vector $$x \in \mathbb{F}^n$$, and we want to find the coefficients for a linear combination of an orthonormal basis $$B=\{v_1, \ldots, v_n\}$$. Then we want

$$x = c_1v_1 + \ldots + c_nv_n$$

As we did before, we can dot both sides by $$v_i$$ to obtain just $$c_i$$ on the right-hand side.

$$v_i \cdot x = c_i$$

And there we go. The coefficients are obtained simply from the dot product. No system of equations required.

**Theorem:** If $$\{v_1, \ldots, v_n\}$$ is an orthonormal basis for $$\mathbb{F}^n$$, then for all $$x \in \mathbb{F}^n$$

$$x = (v_1 \cdot x)v_1 + \ldots + (v_n \cdot x)v_n$$

But notice that $$v_i \cdot x = v_i^*x$$. If we let $$U = \left( v_1 \quad \cdots \quad v_n \right)$$, then we can obtain the vector of coefficients from

$$\begin{pmatrix} v_1^*x \\ \vdots \\ v_n^*x \end{pmatrix} = U^*x$$

**Remark:** It follows that

$$\begin{multline*}
x = (v_1 \cdot x)v_1 + \ldots + (v_n \cdot x)v_n \\= U(U^*x) = UU^*x
\end{multline*}$$

implying that $$UU^* = I$$.

### Example

Take the orthonormal basis for $$\mathbb{R}^2$$

$$\beta = \left\{ \frac{1}{\sqrt{2\pi^2+e^2}}\begin{pmatrix} \pi\sqrt{2} \\ e \end{pmatrix}, \frac{1}{\sqrt{2\pi^2+e^2}}\begin{pmatrix} -e \\ \pi\sqrt{2} \end{pmatrix} \right\}$$

and say we want to express the vector $$\begin{pmatrix} \sqrt{5} \\ \pi^2 \end{pmatrix}$$ as a linear combination of those vectors.

$$\begin{pmatrix} \sqrt{5} \\ \pi^2 \end{pmatrix} =c_1 \frac{\begin{pmatrix} \pi\sqrt{2} \\ e \end{pmatrix}}{\sqrt{2\pi^2+e^2}} + c_2\frac{\begin{pmatrix} -e \\ \pi\sqrt{2} \end{pmatrix}}{\sqrt{2\pi^2+e^2}}$$

I do not care what you say, you simply *cannot* make me solve that system of equations. But, luckily, we don't have to! The dot products are given by the transpose of the matrix

$$\frac{\begin{pmatrix} \pi\sqrt{2} & e \\ -e & \pi\sqrt{2} \end{pmatrix}}{\sqrt{2\pi^2+e^2}}\begin{pmatrix} \sqrt{5} \\ \pi^2 \end{pmatrix} = \frac{\begin{pmatrix} \pi\sqrt{10} + e\pi^2 \\ \pi^3\sqrt{2} - e\sqrt{5} \end{pmatrix}}{\sqrt{2\pi^2+e^2}} $$

Therefore,

$$\begin{multline*}
\begin{pmatrix} \sqrt{5} \\ \pi^2 \end{pmatrix} \\= \frac{\pi\sqrt{10} + e\pi^2}{2\pi^2 + e^2}\begin{pmatrix} \pi\sqrt{2} \\ e \end{pmatrix} + \frac{\pi^3\sqrt{2} - e\sqrt{5}}{2\pi^2 + e^2}\begin{pmatrix} -e \\ \pi\sqrt{2} \end{pmatrix}
\end{multline*}$$

As a bonus, we get the inverse of that nasty matrix to be

$$\begin{multline*}
\left(\frac{1}{\sqrt{2\pi^2+e^2}}\begin{pmatrix}\pi\sqrt{2}&-e\\e&\pi\sqrt{2}\end{pmatrix}\right)^{-1}\\
=\frac{1}{\sqrt{2\pi^2+e^2}}\begin{pmatrix}\pi\sqrt{2}&e\\-e&\pi\sqrt{2}\end{pmatrix}
\end{multline*}$$

## Unitary matrices

The matrix $$A^*A$$ is Hermitian, and every entry is just the inner product of the columns. Thus, if the columns are orthonormal, then everything off the diagonal will be zero, and every diagonal entry will be the norm squared, which is one. Thus, $$A^*A=I$$ if and only if the columns of $$A$$ form an orthonormal basis. This means $$A^{-1}=A^*$$ if $$A$$ is square. But, even if it isn't, $$A^*A$$ will still yield an identity matrix, allowing us to cancel both sides.

### Fun facts about unitary matrices
If $$U$$ is a square unitary matrix, then
1. $$U$$ is unitarily diagonalizable
2. All of the eigenvalues of $$U$$ are of the form $$\lambda_j=e^{i\theta_j}$$. That is, $$\vert \lambda_j\vert=1$$.
3. There exists a hermitian matrix $$H$$ such that $$U=e^{iH}$$. If $$U=VDV^*$$, and $$\lambda_j=e^{i\theta_j}$$, then one such matrix is $$H=V\text{diag}\{\theta_1, \ldots, \theta_n\}V^*$$.
4. $$\langle x, y \rangle = \langle Ux, Uy \rangle$$. That is, $$U$$ preserves the angle between vectors.
5. $$\vert\vert x\vert\vert = \vert\vert Ux\vert\vert$$. That is, $$U$$ preserves the length of all vectors.

Just know, this only scratches the surface. Unitary matrices are simply astounding.

## Orthogonal Projections when you have an orthonormal basis

**Theorem:** If the columns of $$Q$$ form an orthonormal basis for a subspace $$W$$, then

$$P=QQ^*$$

is the orthogonal projector onto $$W$$.

If $$\{v_1, \ldots, v_r\}$$ is an orthonormal basis for a subspace $$W$$, then we can simply obtain the projection as

$$\text{proj}_W(x) = (v_1 \cdot x)v_1 + \ldots + (v_r \cdot x)v_r$$

Since no matter what the other vectors in the orthogonal complement to $$W$$ happen to be (which, if we completed the orthonormal basis, the rest of the vectors would have to be a basis for $$W^\perp$$), they would dot to zero. Therefore, if $$Q = \left( v_1 \quad \cdots \quad v_r \right)$$, then the projection matrix is simply

$$P = QQ^*$$

No $$A^*A$$ inverse shenanigans. The reason is that $$Q^*Q = I$$, so the formula $$Q(Q^*Q)^{-1} Q^*$$ just reduces to $$QQ^*$$.

**Remark:** The $$Q$$ in

$$P = QQ^*$$

can actually be a $$Q$$ from the $$QR$$ factorization of any matrix $$A$$ with full column rank and the same column space. Since $$R$$ will be invertible,

$$\begin{multline*}
A(A^*A)^{-1} A^* \\
= QR((QR)^*QR)^{-1} (QR)^* \\
= QR(R^*Q^*QR)^{-1}(R^*Q^*)\\
= QR(R^*R)^{-1} R^*Q^* \\
= QR(R^{-1} (R^*)^{-1})R^*Q^* \\
= QQ^*
\end{multline*}$$

**Remark:** If $$A$$ has orthogonal columns instead of orthonormal, then $$A^*A \neq I$$, but it will be diagonal. So $$A(A^*A)^{-1} A^*$$ is not that bad. However, the diagonal entries are just the norm squared, so putting $$(A^*A)^{-1}$$ is equivalent to dividing the columns of $$A$$ (and the rows of $$A^*$$) by the norm, normalizing the columns. Thus, we still get the same answer.



[hyperlink](https://youtu.be/T2kOj-GFN8k?si=So_pJbTwG_n3-BWH){:target="_blank"}
