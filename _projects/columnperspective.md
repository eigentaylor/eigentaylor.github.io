---
layout: distill
title: Column and Row Perspective
date: 2022-06-06
description: How to simplify matrix multiplication with the best perspectives (and also find certain inverse matrices fast!)
comments: true
importance: 1
category: linear algebra
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Column Perspective
    subsections:
      - name: Applying this to general matrix multiplication
      - name: Column Perspective Examples
  - name: Row Perspective
    subsections:
      - name: Application to row reduction
  - name: Finding inverses by inspection
---

# Column Perspective

First, let's start with general matrix column vector multiplication. We'll focus on $$2\times2$$ matrices first, as the principles extend very naturally for larger matrices.

If we define the matrices

$$
\textbf{A}=\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix},\quad
\textbf{x}=\begin{pmatrix}
x_1\\x_2
\end{pmatrix}
$$

Then,

$$
\begin{equation}
\textbf{A}\textbf{x}=\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}
\begin{pmatrix}
x_1\\x_2
\end{pmatrix}
=\begin{pmatrix}
a_{11}x_1+a_{12}x_2\\
a_{21}x_1+a_{22}x_2\\
\end{pmatrix}
\end{equation}
$$

But look what happens when we separate this result by the $$x$$ values.

$$
\begin{pmatrix}
a_{11}x_1+a_{12}x_2\\
a_{21}x_1+a_{22}x_2\\
\end{pmatrix}=
\begin{pmatrix}
a_{11}x_1\\
a_{21}x_1\\
\end{pmatrix}+\begin{pmatrix}
a_{12}x_2\\
a_{22}x_2\\
\end{pmatrix}
$$

$$
\begin{pmatrix}
a_{11}x_1+a_{12}x_2\\
a_{21}x_1+a_{22}x_2\\
\end{pmatrix}=
x_1\begin{pmatrix}
a_{11}\\
a_{21}\\
\end{pmatrix}+x_2\begin{pmatrix}
a_{12}\\
a_{22}\\
\end{pmatrix}
$$

$$
\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}
\begin{pmatrix}
x_1\\x_2
\end{pmatrix}=x_1\begin{pmatrix}
a_{11}\\
a_{21}\\
\end{pmatrix}+x_2\begin{pmatrix}
a_{12}\\
a_{22}
\end{pmatrix}
$$

Which are just the original columns of $$\textbf{A}$$. So, if we denote the columns of $$\textbf{A}$$ by $$\textbf{A}_1,\textbf{A}_2$$, we can say that

$$
\begin{equation}
\textbf{A}
\begin{pmatrix}
x_1\\x_2
\end{pmatrix}=x_1\textbf{A}_1+x_2\textbf{A}_2
\end{equation}
$$

Which we can interpret as saying: "we want $$x_1$$ of the first column of $$\textbf{A}$$, and $$x_2$$ of the second column of $$\textbf{A}$$."

And, in general, if we denote the columns of an $$m\times n$$ matrix $$\textbf{A}$$ by $$\textbf{A}_1,\ldots,\textbf{A}_n$$, we can say that

$$
\textbf{A}\begin{pmatrix}
x_1\\x_2\\\vdots\\x_n
\end{pmatrix}=x_1\textbf{A}_1+x_2\textbf{A}_2+\ldots+x_n\textbf{A}_n
$$

Thus, when multiplying a matrix on the right by a column vector, the column vector tells us how many of each column we are taking.

## Applying this to general matrix multiplication

Suppose we have that

$$
\textbf{A}=\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix},\quad
\textbf{B}=\begin{pmatrix}
b_{11}&b_{12}\\
b_{21}&b_{22}
\end{pmatrix}
$$

Consider the product $$\textbf{A}\textbf{B}$$,

$$
\textbf{A}\textbf{B}=\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}
\begin{pmatrix}
b_{11}&b_{12}\\
b_{21}&b_{22}
\end{pmatrix}
$$

$$
\textbf{A}\textbf{B}
=\begin{pmatrix}
a_{11}b_{11}+a_{12}b_{21}&a_{11}b_{12}+a_{12}b_{22}\\
a_{21}b_{11}+a_{22}b_{21}&a_{21}b_{12}+a_{22}b_{22}
\end{pmatrix}
$$

Now, look at each column of the product. Notice that the second column of $$\textbf{B}$$ has no bearing on the first column of $$\textbf{A}\textbf{B}$$. Similarly, the first column of $$\textbf{B}$$ has no effect on the second column of $$\textbf{A}\textbf{B}$$.

If you don't quite see what I mean, look at what happens if we separate the multiplication by the columns of $$\textbf{B}$$.

$$
\textbf{A}\textbf{B}_1=\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}
\begin{pmatrix}
b_{11}\\b_{21}
\end{pmatrix}
$$

$$
\textbf{A}\textbf{B}_1
=\begin{pmatrix}
a_{11}b_{11}+a_{12}b_{21}\\
a_{21}b_{11}+a_{22}b_{21}
\end{pmatrix}=
b_{11}\textbf{A}_1+b_{21}\textbf{A}_2
$$

Which is the first column of $$\textbf{A}\textbf{B}$$.

$$
\textbf{A}\textbf{B}_2=\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}
\begin{pmatrix}
b_{12}\\b_{22}
\end{pmatrix}
$$

$$
\textbf{A}\textbf{B}_2
=\begin{pmatrix}
a_{11}b_{12}+a_{12}b_{22}\\
a_{21}b_{12}+a_{22}b_{22}
\end{pmatrix}=
b_{12}\textbf{A}_1+b_{22}\textbf{A}_2
$$

Which is the second column of $$\textbf{A}\textbf{B}$$.

Thus, we see that

$$
\textbf{A}\textbf{B}=
\bigg(
\textbf{A}\textbf{B}_1\quad\textbf{A}\textbf{B}_2
\bigg)
$$

And more generally,

$$
\begin{equation}
\textbf{A}
\bigg(
\textbf{B}_1\quad\cdots\quad\textbf{B}_n
\bigg)=
\bigg(
\textbf{A}\textbf{B}_1\quad\cdots\quad\textbf{A}\textbf{B}_n
\bigg)
\end{equation}
$$

That is to say, each column of the product, is just the left matrix times the individual column. Hence, we can use the column perspective for each column individually.

## Column Perspective Examples

This can GREATLY speed up certain computations.

For example,

$$\textbf{A}\begin{pmatrix}
1\\0\\0
\end{pmatrix}=\textbf{A}_1$$

will just give us the first column of $$\textbf{A}$$. And

$$\textbf{A}\begin{pmatrix}
1\\1\\0
\end{pmatrix}=\textbf{A}_1+\textbf{A}_2$$

is just the first column and the second column added together.

This can also help us in the reverse direction! Take the example of solving

$$
\left(
\begin{array}{ccc|c}
1&0&3&0\\
0&1&-1&0\\
0&0&0&0
\end{array}
\right)
$$

We can see that if we take the third column as it is (that is to say, taking exactly $$1$$ of it), we can cancel out the nonzero entries by taking $$-3$$ of column one, and $$1$$ of column two. Thus, a solution will be $$(-3,1,1)$$. Since any scalar multiple of this vector will also yield the zero vector, the general solution will be

$$\textbf{x}=c\begin{pmatrix}
-3\\1\\1
\end{pmatrix}$$

since taking $$-3$$ of the first column, $$1$$ of the second column, and $$1$$ of the third column, will cancel everything out. No need to turn it back into equations and solve or whatever.

Let's use an example of matrix multiplication

$$
\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}
\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}
$$

The first column of the right matrix tells us to add up the second and third columns: $$(1,-2,1)+(1,1,-2)=(2,-1,-1)$$. The second column tells us to add the first and third columns: $$(-2,1,1)+(1,1,-2)=(-1,2,-1)$$. And the third column tells us to add up the first and second columns: $$(-2,1,1)+(1,-2,1)=(-1,-1,2)$$. Therefore, the product will be

$$
\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}
\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}=
\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix}
$$

Personally, I can say that I prefer adding up the columns as opposed to doing nine three-dimensional dot products.

---

# Row Perspective

Row perspective, while not *quite* as useful as column perspective, still has its share of uses and applications. It is essentially the transpose of column perspective. Then, we will define our notation for the rows of an $$m\times n$$ matrix $$A$$ as $$\textbf{a}_1^T,\ldots,\textbf{a}_m^T$$.

Row perspective, is as follows.

$$
\begin{equation}
\begin{pmatrix}
\textbf{a}_1^T\\\textbf{a}_2^T\\\vdots\\\textbf{a}_m^T
\end{pmatrix}\textbf{B}=
\begin{pmatrix}
\textbf{a}_1^T\textbf{B}\\\textbf{a}_2^T\textbf{B}\\\vdots\\\textbf{a}_m^T\textbf{B}
\end{pmatrix}
\end{equation}
$$

Where the entries of $$\textbf{a}_i^T$$ tell you how many of each **row** of $$B$$ to take.

To see this for a $$2\times2$$,

$$
\begin{pmatrix}
\textbf{a}_1^T\\
\textbf{a}_2^T\\
\end{pmatrix}\textbf{B}
=\begin{pmatrix}
a_{11}&a_{12}\\
a_{21}&a_{22}
\end{pmatrix}
\begin{pmatrix}
b_{11}&b_{12}\\
b_{21}&b_{22}
\end{pmatrix}
$$

$$
\begin{pmatrix}
\textbf{a}_1^T\\
\textbf{a}_2^T\\
\end{pmatrix}\textbf{B}
=\begin{pmatrix}
a_{11}b_{11}+a_{12}b_{21}&a_{11}b_{12}+a_{12}b_{22}\\
a_{21}b_{11}+a_{22}b_{21}&a_{21}b_{12}+a_{22}b_{22}
\end{pmatrix}
$$

$$
\begin{pmatrix}
\textbf{a}_1^T\\
\textbf{a}_2^T\\
\end{pmatrix}\textbf{B}
=\begin{pmatrix}
a_{11}(b_{11}\quad b_{12})+a_{12}(b_{21}\quad b_{22})\\
a_{21}(b_{11}\quad b_{12})+a_{22}(b_{21}\quad b_{22})\\
\end{pmatrix}
$$

$$
\begin{pmatrix}
\textbf{a}_1^T\\
\textbf{a}_2^T\\
\end{pmatrix}\textbf{B}
=\begin{pmatrix}
(a_{11}\quad a_{12})\begin{pmatrix}
b_{11}&b_{12}\\
b_{21}&b_{22}
\end{pmatrix}\\
(a_{21}\quad a_{22})\begin{pmatrix}
b_{11}&b_{12}\\
b_{21}&b_{22}
\end{pmatrix}\\
\end{pmatrix}
$$

$$
\begin{pmatrix}
\textbf{a}_1^T\\
\textbf{a}_2^T\\
\end{pmatrix}\textbf{B}
=\begin{pmatrix}
\textbf{a}_1^T\textbf{B}\\
\textbf{a}_2^T\textbf{B}\\
\end{pmatrix}
$$

So an example of this would be

$$
\begin{pmatrix}0&1&1\\1&1&0\\1&0&1\end{pmatrix}
\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}
$$

The first row of the left matrix tells us we want $$1$$ of the second row and $$1$$ of the third row: $$(1,-2,1)+(1,1,-2)=(2,-1,-1)$$. The second row tells us to add up the first and second rows: $$(-2,1,1)+(1,-2,1)=(-1,-1,2)$$. And the third rows tells us to add the first and third rows: $$(-2,1,1)+(1,1,-2)=(-1,2,-1)$$. Therefore, the product will be

$$
\begin{pmatrix}0&1&1\\1&1&0\\1&0&1\end{pmatrix}
\begin{pmatrix}-2&1&1\\1&-2&1\\1&1&-2\end{pmatrix}=
\begin{pmatrix}2&-1&-1\\-1&-1&2\\-1&2&-1\end{pmatrix}
$$

## Application to row reduction

I use row perspective often when row reducing matrices. It helps me do multiple steps at the same time. So, let's say I am trying to row reduce

$$\textbf{A}=\begin{pmatrix}
1&1&3&2\\-1&0&-2&-3\\2&2&6&7
\end{pmatrix}
$$

My thought process is as follows:

First, the second row would be better if its negative was the first row, because then we would have a pivot in the first column and a zero in the second entry. Thus, the first row of my row reduction matrix should be $$(0,-1,0)$$, since we want $$-1$$ of the second row.

Next, if we add up the first two rows, then we get a pivot in the second column and a zero in the first entry. So, the second row of our row reduction matrix will be $$(1,1,0)$$, since we want to add up the first and second row.

Finally, we can cancel out the first three entries of the third row by adding $$-2$$ of row one. The third column should then be $$(-2,0,1)$$, since we want to take the third row and subtract $$2$$ times the first row.

Putting it all together, our row reduction matrix is

$$\textbf{R}=\begin{pmatrix}
0&-1&0\\1&1&0\\-2&0&1
\end{pmatrix}
$$

And if we multiply $$\textbf{A}$$ by our row reduction matrix, we get

$$
\textbf{R}\textbf{A}=
\begin{pmatrix}
0&-1&0\\1&1&0\\-2&0&1
\end{pmatrix}\begin{pmatrix}
1&1&3&2\\-1&0&-2&-3\\2&2&6&7
\end{pmatrix}
$$

$$
\textbf{R}\textbf{A}=
\begin{pmatrix}
1&0&2&3\\
0&1&1&-1\\
0&0&0&3
\end{pmatrix}
$$

The final steps of row reduction are then very simple. Divide row three by $$3$$, and then add the correct multiples of it to the first two rows to get the final pivot column.

---

# Finding inverses by inspection

We can also use these perspectives to find inverses relatively easily (depending on the matrix). Of course, this is relatively pointless for a $$2\times2$$ since there is the very easy formula. But I try to do this when possible for larger matrices.

Let's say we want to invert our row reduction matrix from before

$$\textbf{R}=\begin{pmatrix}
0&-1&0\\1&1&0\\-2&0&1
\end{pmatrix}
$$

This is a *good* candidate for the perspectives, because there are lots of zeros! The more zeros, the easier it is to use this. If a matrix has no nonzero entries, unless there is some amazingly obvious pattern, I would just use either the adjugate matrix if it's $$3\times3$$ or row reduction.

So, to do this, we want to find combinations of the rows and columns to get the identity matrix.

The most obvious one to me is that if we take just $$1$$ of the third column, we get the third column of the identity matrix. So that means the third column of $$\textbf{R}^{-1}$$ will be $$(0,0,1)$$

$$\textbf{R}^{-1}=\begin{pmatrix}
*&*&0\\**&*&0\\**&*&1
\end{pmatrix}
$$

Also, if we take $$-1$$ of the first row, we will get the second row of the identity matrix. So the second row should be $$(-1,0,0)$$

$$\textbf{R}^{-1}=\begin{pmatrix}
*&*&0\\-1&0&0\\**&*&1
\end{pmatrix}
$$

I can also see that to get the second column of the identity matrix we can take $$1$$ of column one and $$2$$ of column three: $$(0,1,-2)+2(0,0,1)=(0,1,0)$$. So the second column of our inverse will be $$(1,0,2)$$

$$\textbf{R}^{-1}=\begin{pmatrix}
*&1&0\\-1&0&0\\**&2&1
\end{pmatrix}
$$

Finally, to get the first column, we need a combination of columns one and three to get $$(1,0,0)$$, given that we have $$-1$$ of column two (from the 2,1 entry), $$-1(-1,1,0)$$. To cancel out the second entry, it looks like we need $$1$$ of column one:

$$1(0,1,-2)-1(-1,1,0)=(1,0,-2)$$

So, to cancel out that $$-2$$, we can take $$2$$ of column three. Thus, the first column of the inverse is $$(1,-1,2)$$.

$$\textbf{R}^{-1}=\begin{pmatrix}
1&1&0\\-1&0&0\\2&2&1
\end{pmatrix}
$$

We could have also looked at rows one and three individually! I chose to do the whole column at once because that was my personal preference. You can do it in whatever order you like. I just do whatever is most obvious to me first.