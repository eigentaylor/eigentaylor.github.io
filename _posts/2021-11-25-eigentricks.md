---
layout: distill
title: Shortcuts for Finding Eigenvalues and Eigenvectors
date: 2021-11-25 0
description: diagonalization speedrun, let's go
comments: true
importance: 1
categories: linear-algebra
tags: best 
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: The Characteristic Polynomial
  - name: Eigenvalues
    subsections:
      - name: Example
      - name: Shifted Eigenvalues
  - name: Eigenvectors
    subsections:
      - name: A Quick Trick
      - name: Our example continued
  - name: The Eigenvector Columns Theorem
    subsections:
      - name: Example of Applying the E.C.T.
  - name: By Inspection
  - name: Proof of the The Eigenvector Columns Theorem
---

(Updated 4/17/24 with a smoother proof for the ECT)

# The Characteristic Polynomial

First we examine the general characteristic polynomial of any $$2\times2$$ matrix
$$A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$.

$$A-\lambda I=
\begin{pmatrix}a-\lambda&b\\c&d-\lambda\end{pmatrix}$$

$$\det(A-\lambda I)=(a-\lambda)(d-\lambda)-bc$$

$$\det(A-\lambda I)=\lambda^2-(a+d)\lambda+ad-bc$$

\begin{equation}
\det(A-\lambda I)=\lambda^2-\operatorname{tr}(A)\lambda+\det(A)
\end{equation}

Well ain't that nifty. I would always use this formula for $$2\times2$$ matrices.

Note: For any square matrix, the characteristic polynomial will always be of the form
\begin{equation}
\det(\lambda I-A)=\lambda^n-\operatorname{tr}(A)\lambda^{n-1}+\ldots+(-1)^n\det(A)
\end{equation}

Using $$\det(\lambda I-A)$$ is preferable in generalizing, as then the $$\lambda^n$$ term will always be positive. Using $$A-\lambda I$$ will give you the exact same results for matrices of even dimension, and will simply flip the sign of your entire equation for matrices of odd dimension. Use whichever you prefer.

For $$3\times3$$ matrices, specifically, denoting the Cofactor of the $$ij$$ entry as $$C_{ij}$$, the characteristic polynomial is
\begin{equation}
\det(\lambda I-A)=\lambda^3-\operatorname{tr}(A)\lambda^2+(C_{11}+C_{22}+C_{33})\lambda-\det(A)
\end{equation}

---

# Eigenvalues

Now, in the $$2\times2$$ case, we also know that if $$\lambda_1,\lambda_2$$ are our eigenvalues, then the characteristic polynomial has to factor to

$$\det(A-\lambda I)=(\lambda-\lambda_1)(\lambda-\lambda_2)$$

$$\lambda^2-\operatorname{tr}(A)\lambda+\det(A)=
\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$$

Comparing coefficients we obtain

\begin{equation}
\operatorname{tr}(A)=\lambda_1+\lambda_2,\quad \det(A)=\lambda_1\lambda_2
\end{equation}

Therefore, the trace will be the sum of the eigenvalues, and the determinant will be the product.

So if instead we can think of two numbers which add up the trace and multiply to the determinant, there's no need to compute the characteristic polynomial at all. Sometimes an obvious eigenvalue/eigenvector presents itself by inspection. You can then find the other eigenvalue(s) by subtracting the first from the trace and/or dividing the determinant by the first (assuming it is nonzero...).

Note: __This is true for any sized square matrix. The trace will be the sum of the eigenvalues, and the determinant will be the product.__

### Example:

Let $$A=\begin{pmatrix}-1&2\\-3&4\end{pmatrix}$$. Suppose we want to find the eigenvalues of this matrix. It (hopefully) does not take a lot of mental computational power to observe that $$\operatorname{tr}(A)=3$$ and $$\det(A)=2$$. So can we think of two numbers which add up to 3 and multiply to 2? Well, yeah, how about 1 and 2? And, yes, those are the eigenvalues.

Just to check, we can compute the characteristic polynomial

$$\det(A-\lambda I)=\lambda^2-3\lambda+2=0$$

Which does indeed factor to $$(\lambda-1)(\lambda-2)$$. So $$\lambda_1=1$$ and $$\lambda_2=2$$.

#### Shifted Eigenvalues

If the matrix $$A$$ is a scalar matrix off from a matrix where the eigenvalues are very obvious $$B=A-kI$$, then the eigenvalues of $$A$$ will be the eigenvalues of $$B$$ plus $$k$$, and the eigenvectors will be the same.

For example, $$A=\begin{pmatrix}-3&0&0\\1&-2&1\\1&1&-2\end{pmatrix}$$ is equal to $$\begin{pmatrix}0&0&0\\1&1&1\\1&1&1\end{pmatrix}-3I$$.

$$B=\begin{pmatrix}0&0&0\\1&1&1\\1&1&1\end{pmatrix}$$ is a rank one $$3\times3$$, and therefore has an eigenvalue of $$0$$ with multiplicity $$3-1=2$$. The remaining eigenvalue will be the trace which is 2. So the eigenvalues of $$A$$ will be $$\lambda=0-3,0-3,2-3\implies \lambda=-3,-3,-1$$.

---

# Eigenvectors

## A Quick Trick

Before we continue on our journey with the matrix above, I present to you a convinient trick for getting eigenvectors from any $$2\times2$$ matrix.

If $$\lambda$$ is an eigenvalue of $$A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$, then, as long as it is nonzero, the vector

\begin{equation}
\textbf{v}=(b,\lambda-a)
\end{equation}

is an eigenvector. If that vector is zero, then $$\textbf{v}=(\lambda-d,c)$$ should be a nonzero alternative.

Using $$(b,\lambda-a)$$ is quite convinient with complicated eigenvalues/entries (especially when the eigenvalue is complex).

You can take this as it is, or if you are clammering for an explanation:

The idea is that if $$\lambda$$ is an eigenvalue, then $$\det(A-\lambda I)=0$$, so the rows of $$A-\lambda I$$ are linearly dependent, so you never have to bother row reducing it in the $$2\times2$$ case because we know one of the rows is a multiple of the other. We then just use the fact that $$(y,-x)$$ will always be orthogonal to the vector $$(x,y)$$. So $$(b,\lambda-a)$$ will be orthogonal to the first row of $$A-\lambda I$$ $$(a-\lambda,b)$$, and by extension the second row since they are linearly dependent, putting it in the null space.

## Our example continued

Let $$A$$ be the same matrix as the section above, $$A=\begin{pmatrix}-1&2\\-3&4\end{pmatrix}$$. Suppose we now want to find the eigenvectors of this matrix. For the sake of example, we will not use the trick presented in the previous section. That said, you can verify that using it will give consistent results with what we find.

$$A-\lambda I=\begin{pmatrix}-1-\lambda&2\\-3&4-\lambda\end{pmatrix}$$

So now we find the null space of $$A-\lambda I$$ for $$\lambda_1=1$$ and $$\lambda_2=2$$.

$$\lambda=1$$:

$$A-1I=\begin{pmatrix}-2&2\\-3&3\end{pmatrix}$$

We can solve to find the eigenvector with eigenvalue $$1$$ is $$\textbf{v}_1=(1,1)$$. Cool.

$$\lambda=2$$:

$$A-2I=\begin{pmatrix}-3&2\\-3&2\end{pmatrix}$$

Okay, hold up. The columns of $$A-2I$$ are just scalar multiples of the eigenvector for $$\lambda=1$$, $$(1,1)$$. Maybe this is just a coincidence...

We continue to see the other eigenvector is $$\textbf{v}_2=(2,3)$$. And... no... it couldn't be... The columns of $$A-1I$$ were scalar multiples of $$(2,3)$$, which is the eigenvector of the other eigenvalue again!

No, this is not a lucky coincidence or conveniently true for just this particular matrix. This will be true for any $$2\times2$$. In the case of a defective eigenvalue, this will give you the one eigenvector.

---

## The Eigenvector Columns Theorem

In general, if $$A$$ is a $$2\times2$$ matrix with eigenvalues $$\lambda_1,\lambda_2$$, then The Eigenvector Columns Theorem (which is a name I just made up) guarantees that

1. The columns of $$A-\lambda_1I$$ will be scalar multiples of the eigenvector with eigenvalue $$\lambda_2$$.

2. The columns of $$A-\lambda_2I$$ will be scalar multiples of the eigenvector with eigenvalue $$\lambda_1$$.

A proof of this "theorem" is included at the end.

This generalizes to any matrix which has a degree two minimal polynomial. This includes any diagonalizable matrix with two distinct eigenvalues, or any matrix with only one distinct eigenvalue that has Jordan blocks of size two or smaller. Basically, you just need that

$$(A-\lambda_1I)(A-\lambda_2I)=0$$

for some $$\lambda_1,\lambda_2$$.

### Example of Applying the E.C.T.

Take $$A=\begin{pmatrix}-1&2\\4&-3\end{pmatrix}$$. The trace is $$-4$$ and the determinant is $$-5$$. So the eigenvalues will be $$1$$ and $$-5$$ since they satisfy the sum and product. Now to get the eigenvector for $$\lambda=1$$, we look at the columns of $$A-(-5)I$$

$$A-(-5)I=\begin{pmatrix}4&2\\4&2\end{pmatrix}$$

The columns are scalar multiples of $$(1,1)$$, so the eigenvector for $$\lambda=1$$ is $$(1,1)$$.

To get the other eigenvector, we look at 

$$A-1I=\begin{pmatrix}-2&2\\4&-4\end{pmatrix}$$

The columns are scalar multiples of $$(1,-2)$$, so the eigenvector for $$\lambda=-5$$ is $$(1,-2)$$. Donezo Washington.

# By Inspection

Often, eigenvectors or eigenvalues can present themselves quite "obviously" by inspection (if you know where to look, that is). Take the example

$$A=\begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}$$

Hopefully it is obvious by inspection that this is a rank one matrix. Rank one meaning, in the context of eigenvalues, "only one nonzero eigenvalue". And "only one nonzero eigenvalue" means "the eigenvalue is equal to the trace" (which in this case is 3).

Additionaly, Since it is a $$3\times3$$ and $$\operatorname{rank}(A)=1$$, we can say by the rank-nullity theorem that $$\operatorname{nullity}(A)=2$$ which is equivalent to saying it has an eigenvalue of zero repeated twice. Thus, we have all the eigenvalues without doing any work. No determinant required.

We can also see that $$(1,1,1)$$ is an eigenvector (in fact, any nonzero column of a rank one matrix is an eigenvector). You could also perhaps see that $$(1,-1,0)$$ and $$(0,1,-1)$$ would work as the other two eigenvectors as they would be an easy basis for the null space.

---

$$A=\begin{pmatrix}0&2&1\\2&0&1\\1&1&1\end{pmatrix}$$

This is another case where it may be clear by inspection that $$(1,1,1)$$ is an eigenvector for this matrix too, since all the rows (and columns) add up to 3 (meaning 3 is an eigenvalue!). If you calculate the trace and determinant (I recommend using the diagonal method), you will get $$1$$ for the trace and $$0$$ for the determinant. Since the determinant is zero, zero will be an eigenvalue. So if we want the sum of all the eigenvalues to be $$1$$ (the trace), $$3+0+\lambda_3=1$$, then we can see that the remaining eigenvalue must be $$-2$$. Another case where we don't have to calculate the characteristic polynomial! Assuming you spotted that the columns add up to the same number, which is admittedly not easy. With practice, however, you start to notice these things.

---

$$A=\begin{pmatrix}4&0&1\\-2&1&0\\-2&0&1\end{pmatrix}$$

The trace and determinant are both $$6$$, meaning we need three numbers which add up to $$6$$ and multiply to $$6$$. A combination that comes to mind is $$1,2,3$$. Unfortunately, unlike the $$2\times2$$ case where if you can find a combination, then those will be the eigenvalues, the $$3\times3$$ is more ambiguous. Luckily, there is an eigenvector that can be spotted by inspection, $$(0,1,0)$$ with eigenvalue $$1$$. Therefore, we can be confident in our guess that $$2$$ and $$3$$ will be the other eigenvalues (since after subtracting the eigenvalue from the trace and dividing it from the determinant, we see the other two must add up to $$6-1=5$$ and multiply to $$6/1=6$$).

---

At least *most* of the time, mathematics profesors tend to use matrices with nice eigenvalues and eigenvectors. Before jumping straight into the hell that the characteristic polynomial can be, try looking it over and seeing if you can spot any eigenvectors.

## Proof of the The Eigenvector Columns Theorem

(Updated 4/17/24) This revised proof is cleaner and shows that this actually generalizes to some special cases of larger matrices.

This theorem relies on the fact that the minimal polynomial has a quadratic degree or lower. By the Cayley-Hamilton theorem,

$$(A-\lambda_1I)(A-\lambda_2I)=0$$

Now, remember that a vector is in the eigenspace of eigenvalue $$\lambda$$ if it's in $$\ker(A-\lambda I)$$. But,

$$(A-\lambda_1I)(A-\lambda_2I)=0\implies (A-\lambda_2 I)\in\ker(A-\lambda_1I)$$

This means the columns of $$A-\lambda_2I$$ must be in the eigenspace of $$\lambda_1$$. That is, the columns of $$A-\lambda_2I$$ satisfy $$Av=\lambda_1v$$. So the columns must be scalar multiples of the eigenvectors with eigenvalue $$\lambda_1$$.

Similarly, since

$$(A-\lambda_1I)(A-\lambda_2I)=(A-\lambda_2I)(A-\lambda_1I)$$

we can see that $$(A-\lambda_1I)\in\ker(A-\lambda_2I)$$. 

This also works if $$\lambda_1=\lambda_2$$, which takes care of the case of repeated eigenvalues.

Further, this implies that this principle holds for any matrix which has a degree two minimal polynomial (degree one is trivial, as that means it's a scalar matrix). This includes any diagonalizable matrix with two distinct eigenvalues, or any matrix with only one distinct eigenvalue that has Jordan blocks of size two or smaller.

Note that this actually also gives a general theoretical method of finding eigenvectors if you have the factored minimal polynomial. If

$$(A-\lambda_1I)\ldots(A-\lambda_nI)=0$$

Then the columns of $$(A-\lambda_2I)\ldots(A-\lambda_nI)$$ will be scalar multiples of eigenvectors with eigenvalue $$\lambda_1$$. This is probably more work, though (and requires that you happen to know the minimal polynomial). But, hey, it's a thing.
