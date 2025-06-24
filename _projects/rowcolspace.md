---
layout: distill
title: Bases for the fundamental spaces of a matrix
date: 2022-06-11
description: a lot of students struggle with this so here. row space, column space, null space, and left null space.
comments: true
importance: 2
category: linear algebra
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Preliminary vocab and notation
    subsections:
      - name: Dimensions of the spaces
  - name: Row reduction
  - name: Row Space
  - name: Column Space
  - name: Nullspace
  - name: Left Nullspace
---

In case you need a refresher on what things like pivots and the column space are. Otherwise, you can just skip to [Row Reduction](#row-reduction).

## Preliminary vocab and notation

As a note on notation, we typically say $$A$$ is an $$m\times n$$ matrix which we are looking at. And we will call its reduced row echelon form (or rref for short) $$R$$.

The matrix we will use as an example will be the following

$$A=\begin{pmatrix}
1&2&1&0&1\\
1&2&1&0&1\\
1&2&3&2&3\\
1&2&1&0&2
\end{pmatrix}$$

And its rref

$$R=\begin{pmatrix}
1&2&0&-1&0\\
0&0&1&1&0\\
0&0&0&0&1\\
0&0&0&0&0
\end{pmatrix}$$

In the discussion of this topic, it often helps to assign variables to each column, as if we were solving some arbitrary system $$A\textbf{x}=\textbf{b}$$. To explicitly define our variables,

$$
\begin{equation} \label{aeq}
\begin{pmatrix}
1&2&1&0&1\\
1&2&1&0&1\\
1&2&3&2&3\\
1&2&1&0&2
\end{pmatrix}\begin{pmatrix}
x_1\\x_2\\x_3\\x_4\\x_5
\end{pmatrix}=\textbf{b}
\end{equation}
$$

Which is row reduced to

$$
\begin{equation} \label{req}
\begin{pmatrix}
1&2&0&-1&0\\
0&0&1&1&0\\
0&0&0&0&1\\
0&0&0&0&0
\end{pmatrix}\begin{pmatrix}
x_1\\x_2\\x_3\\x_4\\x_5
\end{pmatrix}=\textbf{b}'
\end{equation}
$$

When we refer to "variables" in "the system", we will be referring to $$x_1,\ldots,x_5$$ in the above.

Other important vocab includes

- **Pivot**: A pivot is a leading one (the first nonzero entry of each nonzero row) in the rref. The pivots of $$R$$ are in the first, third, and fifth column.
- **Pivot column**: A column with a pivot. In rref, pivot columns are just columns of the identity matrix. The pivot columns of $$R$$ are then the first, third, and fifth columns. Pivot columns are also linearly independent.
- **Nonpivot column**: A column that doesn't have a pivot.
- **Leading variable**: The variables corresponding to pivot columns. They can be solved for in terms of free variables. So for the system \eqref{req}, the leading variables are $$x_1,x_3,x_5$$.
- **Free variable**: A variable corresponding to nonpivot columns. For the system mentioned above, they would be $$x_2,x_4$$.
- **Rank**: The dimension of the column and row space. Also the number of pivot columns.
- **Nullity**: The dimension of the nullspace. Also the number of nonpivot columns.

Next, the four fundamental spaces of a matrix $$A$$:

- **Column Space**: The range of the columns. Also every vector $$\textbf{b}$$ such that $$A\textbf{x}=\textbf{b}$$ is consistent.
- **Nullspace**: Every vector $$\textbf{n}$$ such that $$A\textbf{n}=\textbf{0}$$. Also called the kernel of $$A$$.
- **Row Space**: The range of the rows. Also the column space of $$A^T$$.
- **Left Nullspace**: Every vector $$\textbf{n}$$ such that $$\textbf{n}^TA=\textbf{0}^T$$. Also the kernel of $$A^T$$.

### Dimensions of the spaces

Finally, a quick summary on the dimensions of the four spaces of an $$m\times n$$ matrix $$A$$ with $$\operatorname{rank}(A)=r$$ using the rank-nullity theorem:

- $$\dim(\operatorname{col}(A))=\dim(\operatorname{row}(A))=\operatorname{rank}(A)=r=$$ the number of pivot columns.
- $$\dim(\operatorname{null}(A))=\operatorname{nullity}(A)=n-r=$$ the number of nonpivot columns.
- $$\dim\left(\operatorname{null}\left(A^T\right)\right)=\operatorname{nullity}(A^T)=m-r$$.

As a brief aside, I personally tend to go for a different kind of row echelon form other than rref. Because I hate fractions in my matrix, I don't force "leading ones". I do, however, try to keep pivot columns having the pivot be the only nonzero entry. That way, leading variables are still easy to solve for, and you avoid fractions.

To illustrate this point, basically I prefer $$\begin{pmatrix}
2&0&1\\
0&3&-1\\
\end{pmatrix}$$ to $$\begin{pmatrix}
1&0&\frac{1}{2}\\
0&1&-\frac{1}{3}\\
\end{pmatrix}$$

## Row reduction

First, It's important to make clear what row reduction *does* and *does not* change about a matrix.

- Row reduction does *not* change the row space or the null space.
- Row reduction *usually* changes the column space

Let's explain why the row and null spaces are unaffected real quick.

The row space is not changed because the rows of $$R$$ are just linear combinations of the rows of $$A$$. Thus, the rows of $$R$$ are in the span of the rows of $$A$$, leaving them contained in the row space. Since row operations are reversible (invertible), we don't lose any information about the row space either.

The reason the null space is not affected is a bit more complicated. The short answer is that column dependencies remain the same in both $$A$$ and $$R$$ (we will discuss this at length further on). The slightly longer and possibly more intuitive answer is that if $$R$$ is the rref of $$A$$, then there is an invertible matrix $$P$$ such that $$PA=R$$. It follows that if $$A\textbf{n}=\textbf{0}$$, then $$R\textbf{n}=PA\textbf{n}=P\textbf{0}=\textbf{0}$$.

Hopefully, it is obvious that the column space is usually completely different. Most of the columns of $$A$$ have a nonzero fourth entry, but all of the columns of $$R$$ have a zero fourth entry. So $$(1,1,1,1)$$, the first column of $$A$$ which is by definition in the column space, cannot be in the column space of $$R$$. Thus, the column spaces are not always the same.

## Row Space

So, this is actually pretty easy. A basis for the row space of $$A$$ is just the nonzero rows of $$R$$. As mentioned before, they are in the span of the rows of $$A$$. And they are also obviously linearly independent.

From our $$R=\begin{pmatrix}
1&2&0&-1&0\\
0&0&1&1&0\\
0&0&0&0&1\\
0&0&0&0&0
\end{pmatrix}$$ matrix, the nonzero rows are

$$(1,2,0,-1,0),\quad (0,0,1,1,0),\quad (0,0,0,0,1)$$

The first vector is the only one with a nonzero first entry, so it's definitely linearly independent from the others. The second is the only one with a nonzero third entry, so it's definitely linearly independent from the others. And the third is the only one with a nonzero fifth entry, so (etc.)

Our Row Space basis is then

$$\operatorname{row}(A)=\operatorname{span}\left\{(1,2,0,-1,0),(0,0,1,1,0),(0,0,0,0,1)\right\}$$

Those who remember that you have to look at the columns of the original matrix for the column space may be tempted to say that the first three rows of $$A$$ must be a basis for the row space as well. But that would be wrong here! Most of the time you are okay doing that, but in this case, the first two rows of $$A$$ are identical, and thus linearly dependent. They cannot be a basis, then.

## Column Space

Before, I mentioned that "column dependencies remain the same in both $$A$$ and $$R$$". Let's go over exactly what I mean by that.

Look at $$R$$:

$$R=\begin{pmatrix}
1&2&0&-1&0\\
0&0&1&1&0\\
0&0&0&0&1\\
0&0&0&0&0
\end{pmatrix}$$

The columns are very simple, so it's very easy to see the column dependencies of the nonpivot columns in terms of the pivot columns.

The second column, $$(2,0,0,0)$$ is twice the first column (col2=2col1)

$$(2,0,0,0)=2(1,0,0,0)$$

And the fourth column $$(-1,1,0,0)$$ is the difference of the first and third columns (col4=col3-col1)

$$(-1,1,0,0)=(0,1,0,0)-(1,0,0,0)$$

Now, this blew my mind when I first saw it. But the same relationships are true for $$A$$ as well!

$$\begin{pmatrix}
1&2&1&0&1\\
1&2&1&0&1\\
1&2&3&2&3\\
1&2&1&0&2
\end{pmatrix}$$

(col2=2col1)

$$(2,2,2,2)=2(1,1,1,1)$$

(col4=col3-col1)

$$(0,0,2,0)=(1,1,3,1)-(1,1,1,1)$$

This isn't just coincidence either! This is always true of a matrix and its rref. In other words, *the rref tells us the relationships between the columns*.

So, we know that column two is linearly dependent on column one, and column four is linearly dependent on columns one and three. Thus, we exclude them  from our basis.

**This is why we take the pivot columns of the original matrix!** It's because the rref tells us they are *linearly independent*.

Then our pivot columns are columns one, three, and five. So a basis for the column space is

$$\operatorname{col}(A)=\operatorname{span}\left\{
  \begin{pmatrix}
1\\1\\1\\1
\end{pmatrix},
  \begin{pmatrix}
1\\1\\3\\1
\end{pmatrix},
  \begin{pmatrix}
1\\1\\3\\2
\end{pmatrix}
  \right\}$$

Note: the nonpivot columns of $$R$$ are the coordinate vectors of the nonpivot columns of $$A$$ with respect to this pivot column basis!

## Nullspace

So, we actually already did all the work we needed to do in the previous section!

We found the following column dependencies:

(col2=2col1 $$\implies$$ 2col1-col2=0) and (col4=col3-col1 $$\implies$$ col1-col3+col4=0)

This actually gives us a basis for the null space, using [column perspective](../columnperspective/){:target="_blank"}.

If we take $$2$$ of column one, and $$-1$$ of column two, we get zero. So
$$(2,-1,0,0,0)$$
is in the null space.

$$
\begin{pmatrix}
1&2&1&0&1\\
1&2&1&0&1\\
1&2&3&2&3\\
1&2&1&0&2
\end{pmatrix}
\begin{pmatrix}
2\\-1\\0\\0\\0
\end{pmatrix}=
2\begin{pmatrix}
1\\1\\1\\1
\end{pmatrix}-
\begin{pmatrix}
2\\2\\2\\2
\end{pmatrix}=
\begin{pmatrix}
0\\0\\0\\0
\end{pmatrix}
$$

The other relationship tell us that $$1$$ of column one, $$-1$$ of column three, and $$1$$ of column four will also give us zero. Putting
$$(1,0,-1,1,0)$$
in the null space as well.

$$
\begin{pmatrix}
1&2&1&0&1\\
1&2&1&0&1\\
1&2&3&2&3\\
1&2&1&0&2
\end{pmatrix}
\begin{pmatrix}
1\\0\\-1\\1\\0
\end{pmatrix}=
\begin{pmatrix}
1\\1\\1\\1
\end{pmatrix}-
\begin{pmatrix}
1\\1\\3\\1
\end{pmatrix}+
\begin{pmatrix}
0\\0\\2\\0
\end{pmatrix}=
\begin{pmatrix}
0\\0\\0\\0
\end{pmatrix}
$$

$$(2,-1,0,0,0)$$ and $$(1,0,-1,1,0)$$ are pretty clearly independent, and since we have two nonpivot columns, we know the dimension of the null space is two. Thus, we have a proper basis for the null space!

$$\operatorname{null}(A)=\operatorname{span}\left\{
  \begin{pmatrix}
2\\-1\\0\\0\\0
\end{pmatrix},
\begin{pmatrix}
1\\0\\-1\\1\\0
\end{pmatrix}
  \right\}$$

## Left Nullspace

**PRO TIP**: You don't have to start at square one and row reduce the entirety of $$A^T$$. You can just take the pivot columns, tranpose them, and row reduce that!

For our example,

$$\operatorname{rref}\left(
\begin{pmatrix}
1&2&1&0&1\\
1&2&1&0&1\\
1&2&3&2&3\\
1&2&1&0&2
\end{pmatrix}^T
  \right)=
\begin{pmatrix}
1&1&0&0\\
0&0&1&0\\
0&0&0&1\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}$$

Whilst

$$\operatorname{rref}\left(
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&3&3\\
1&1&2
\end{pmatrix}^T
  \right)=
\begin{pmatrix}
1&1&0&0\\
0&0&1&0\\
0&0&0&1\\
\end{pmatrix}$$

Neat, huh? It's just the nonzero rows! This is because we already know the nonpivot columns are linearly dependent on the pivot columns. So, when row reducing the transpose, those columns (now rows) will end up zeroing out as we row reduce.

From the summary at the beginning, we know that since we have three pivot columns and four rows in $$A$$, the dimension of the left nullspace will be $$4-3=1$$. Thus, we will only get one vector in the left nullspace. The only nonpivot column is column two, and we can see that if we take col1-col2 we will get zero. So our null vector is $$(1,-1,0,0)$$.

Thus,

$$\operatorname{null}(A^T)=\operatorname{span}\left\{
  (1,-1,0,0)
  \right\}$$