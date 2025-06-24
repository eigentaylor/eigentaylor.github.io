---
layout: distill
title: Change of Basis
date: 2022-10-06
description: the most confusing thing in linear algebra (don't @ me)
comments: true
importance: 2
categories: linear-algebra
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Reccommended viewing
  - name: Preface
  - name: Notation
    subsections:
      - name: The standard basis
      - name: Transformation matrices and coordinate vectors
      - name: Change of basis matrices
  - name: How coordinates work
    subsections:
      - name: Transformation matrix definition
      - name: Linear transformation example
      - name: Change of basis matrix properties
      - name: Wait what IS a coordinate vector
      - name: Coordinate vectors with matrices
      - name: Computing coordinate vectors
      - name: Coordinate vector example
  - name: How to change bases
    subsections:
      - name: Change of basis example
  - name: Transformations on other bases
    subsections:
      - name: Linear operators
      - name: Linear operator example
      - name: V to W
  - name: Finding change of basis matrices
---

### Recommended viewing

Before you subject yourself to this post, I recommend watching the following two linear algebra videos from 3blue1brown's "Essence of linear algebra" series. Grant Sanderson is the superior Grant when it comes to math explanations, and I think it's entirely possible that watching these two videos will answer pretty much every question you may have.

- [Linear transformations and matrices](https://youtu.be/kYB8IZa5AuE){:target="_blank"}
- [Change of basis](https://youtu.be/P2LTAUO1TdA){:target="_blank"}
- I'd also recommend reading my post on [*column perspective*](../columnperspective/){:target="_blank"}. Understanding column perspective is going to make a lot of this much easier, but it's not required.

### Preface

This topic is so infrequent that when it comes up in my tutoring practice, I have to rederive it for myself as I'm explaining it every single time. I recommend trying to focus on *understanding* where these formulas comes from, rather than memorizing what they are. In my opinion, if you intuitively understand what a change of basis matrix and a coordinate vector are, and how they interact, it all sort of comes together very naturally.

Not to say change of basis is natural, absolutely not. This is possibly the most confounding topic I have had to consistently tutor. I just mean that once you speak the language of change of basis, then forming sentences is relatively intuitive.

## Notation

This is important to get out of the way because there are *so* many different notations for all this stuff. So let's get it all straight right up front so the amount of confusion experienced later is (hopefully) minimized.

To be more general, we're going to talk about the coordinates being in $$F^n$$ rather than $$\mathbb{R}^n$$, like you will probably see in a lower division class. Just think $$\mathbb{R}^n$$ if you have no idea what a field is.

We will be denoting vectors as simply lowercase letters $$v$$. Vectors are also commonly denoted $$\textbf{v}$$ or $$\vec{v}$$, but this is linear algebra and there are a ton of vectors and it's a lot easier to type "v" than it is "\textbf{v}" or "\vec{v}" (and I am a lazy person). For a similar reason, we won't be distinguishing between column vectors and row vectors. As far as we are concerned here,

$$(x,y)=\begin{pmatrix}x\\y\end{pmatrix}$$

The vectors in this post are lazy and generally prefer to lay down on their sides. They will stand up when they need to be multiplied by a matrix.

### The standard basis

We denote the standard basis "$$\varepsilon$$". In the case of $$F^n$$, we say $$\varepsilon=\{e_1,\ldots,e_n\}$$, where $$e_i$$ is the $$i$$th column of the $$n\times n$$ identity matrix (that is, zeros everywhere except for a $$1$$ in the $$i$$th entry). For polynomial rings $$\varepsilon=\{1,x,\ldots,x^n\}$$, and so on.

### Transformation matrices and coordinate vectors

- The coordinate vector for a vector $$v$$ with respect to a basis $$\beta$$ is denoted
$$[v]_\beta$$.
- The matrix for a linear transformation $$T:V\to V$$ with respect to a basis $$\beta$$ is denoted
$$[T]_\beta$$
- The matrix for a linear transformation $$T:V\to W$$ with respect to bases $$\alpha$$ of $$V$$ and $$\beta$$ of $$W$$ is denoted
$$[T]_\alpha^\beta$$
- The matrix for a linear transformation $$T:V\to W$$ with respect to **standard** bases $$\varepsilon_v$$ of $$V$$ and $$\varepsilon_w$$ of $$W$$ is denoted
$$[T]_\varepsilon^\varepsilon$$

### Change of basis matrices

For "the matrix which changes coordinates from a basis $$\alpha$$ to a basis $$\beta$$", there are a bunch of different notations. Here are a few:

$$[I]_\alpha^\beta,\quad P_{\alpha\to\beta},\quad P_{\beta\gets\alpha}$$

We will use $$P_{\beta\gets\alpha}$$ for this post, because I like it best. To explain why, I am going to show a formula which will be explained later with all three different versions

$$\begin{array}{ccc}
[I]_\alpha^\beta&=&[I]_\varepsilon^\beta[I]_\alpha^\varepsilon\\
P_{\alpha\to\beta}&=&P_{\varepsilon\to\beta} P_{\alpha\to\varepsilon}\\
P_{\beta\gets\alpha}&=&P_{\beta\gets\varepsilon} P_{\varepsilon\gets\alpha}\\
\end{array}$$

Personally, I like the third one because you can easily read it right to left (which is important because transformations are always applied right to left). The second one is jarring for me because it mixes right to left with left to right. And while the first one isn't that bad, it's a little jumpy and dense, in my opinion. Use whatever you like, but I will use the third.

## How coordinates work

### Transformation matrix definition

A change of basis is just another linear transformation. So it is worth at least writing out the general formula for constructing a transformation matrix.
*Rarely* it is easier to directly compute a change of basis matrix using the following formulation. However, it is slightly more common that computing $$[T]_\alpha^\beta$$ directly is faster, because the systems of equations that come up when finding it may have very obvious solutions (for example, if a transformation just scales or permutes vectors. This happens when using an eigenbasis). For this reason, **it is often worth applying the transformation to the basis vectors of the domain and seeing if there is an obvious relationship between the outputs and the vectors in the basis of the codomain.**

If $$T:V\to W$$ is a linear transformation, and $$\alpha=(v_1,\ldots,v_n)$$ is a basis for $$V$$, then the matrix for the transformation $$T$$ with respect to the bases $$\alpha$$ of $$V$$ and $$\beta$$ of $$W$$ is given by the $$\dim(W)\times n$$ matrix

$$
\begin{equation}\label{transformation}
[T]_\alpha^\beta=\Big([T(v_1)]_\beta\quad\cdots\quad [T(v_n)]_\beta\Big)
\end{equation}
$$

### Linear transformation example

Here is an example where you don't actually need to do change of basis, really.

Consider the transformation $$T:P_2(F)\to F^2$$ defined by

$$T(a_0+a_1x+a_2x^2)=\begin{pmatrix}2a_1-a_2\\a_0+3a_1-3a_2\end{pmatrix}$$

Find the matrix for the transformation with respect to the bases $$\alpha=\{1+x+x^2,1+x^2,2+x+x^2\}$$ and $$\beta=\left\{\begin{pmatrix}1\\1\end{pmatrix},\begin{pmatrix}1\\2\end{pmatrix}\right\}$$.

First, we can apply $$T(\alpha)$$ just to see what happens. You can either directly plug in each basis vector into the transformation, or you could find the matrix for the transformation with respect to the standard bases and apply that to the coordinate vectors. We will do the latter as practice:

$$T(1)=\begin{pmatrix}0\\1\end{pmatrix},\quad T(x)=\begin{pmatrix}2\\3\end{pmatrix},\quad T(x^2)=\begin{pmatrix}-1\\-3\end{pmatrix}$$

Thus, $$[T]_\varepsilon^\varepsilon=\begin{pmatrix}0&2&-1\\1&3&-3\end{pmatrix}$$

Applying that matrix to the coordinate vectors of $$\alpha$$ with respect to the standard basis ($$P_{\varepsilon\gets\alpha}$$)

$$\begin{pmatrix}0&2&-1\\1&3&-3\end{pmatrix}\begin{pmatrix}1&1&2\\1&0&1\\1&1&1\end{pmatrix}=\begin{pmatrix}1&-1&1\\1&-2&2\end{pmatrix}$$

And as it so happens, the columns are just scalar multiples of our $$\beta$$ basis vectors (wow it's almost like this example was designed for that to happen). We can see that

$$T(\alpha_1)=1\beta_1,\quad T(\alpha_2)=-1\beta_2,\quad T(\alpha_3)=1\beta_2$$

Therefore, the matrix $$[T]_\alpha^\beta$$ is just

$$[T]_\alpha^\beta=\begin{pmatrix}1&0&0\\0&-1&1\end{pmatrix}$$

I encourage you to try this example with the tools later outlined in this post. It isn't *that* bad, but the purpose of this example is to let you know that there are often simpler ways to go about these problems. You shouldn't always bust out the formula just because you *can*.

### Change of basis matrix properties

Just to get this out of the way because it's quick, change of basis matrices are basically designed to have the following property

$$
\begin{equation}\label{changebasis}
P_{\beta\gets\alpha}[v]_\alpha=[v]_\beta
\end{equation}
$$

This is another reason I like the right to left notation. The $$\alpha$$s are on the same side and seem to cancel out.

We also have a property of when you do successive changes of basis, it's all just one big change of basis. That is, going from $$\alpha$$ to $$\beta$$ and then from $$\beta$$ to $$\gamma$$ is the same as just going from $$\alpha$$ to $$\gamma$$.

$$
\begin{equation}\label{basiscombine}
P_{\gamma\gets\beta}P_{\beta\gets\alpha}=P_{\gamma\gets\alpha}
\end{equation}
$$

One more important property that follows directly from \eqref{changebasis} (by multiplying the inverse matrix to both sides) is

$$
\begin{equation}\label{basisinverse}
P_{\alpha\gets\beta}=(P_{\beta\gets\alpha})^{-1}
\end{equation}
$$

That is, to reverse the change of basis, you just invert the matrix.

### Wait what IS a coordinate vector?

Given a vector $$v=(1,1)$$ and the basis $$\beta=\{(1,-1),(-1,2)\}$$, the coordinate vector of $$v$$ with respect to the basis $$\beta$$ is

$$[v]_\beta=(3,2)$$

But what does that *mean* and how could we find that?

The idea is that if we have a basis $$\alpha=\{v_1,\ldots,v_n\}$$, and $$[x]_\alpha=(c_1,\ldots,c_n)$$, then that is defined to mean

$$
\begin{equation}\label{coordinate}
x=c_1v_1+\ldots+c_nv_n
\end{equation}
$$

In words, $$[x]_\alpha=(c_1,\ldots,c_n)$$ tells us that "to get the vector $$x$$, we need $$c_1$$ of $$v_1$$, $$c_2$$ of $$v_2$$, ..., and $$c_n$$ of $$v_n$$".

For the example above, we can observe that it's true that

$$\begin{pmatrix}1\\1\end{pmatrix}=
3\begin{pmatrix}1\\-1\end{pmatrix}
+2\begin{pmatrix}-1\\2\end{pmatrix}$$

The question becomes, then, "how could we find the numbers $$3$$ and $$2$$? Don't worry, we will answer that [in time](#computing-coordinate-vectors){:target="_blank"}.

One observation to make is that for all $$v\in F^n$$, $$v=[v]_\varepsilon$$. To show an example in $$F^2$$, where $$\varepsilon=\left\{\begin{pmatrix}1\\0\end{pmatrix},\begin{pmatrix}0\\1\end{pmatrix}\right\}$$.

$$\begin{pmatrix}x\\y\end{pmatrix}=
x\begin{pmatrix}1\\0\end{pmatrix}
+y\begin{pmatrix}0\\1\end{pmatrix}$$

Which is to say

$$\left[\begin{pmatrix}x\\y\end{pmatrix}\right]_\varepsilon=
\begin{pmatrix}x\\y\end{pmatrix}$$

In words: "every vector in $$F^n$$ is its own coordinate vector with respect to the standard basis". In a sense, that is *why* it's the standard basis.

This gives us a method to compute coordinate vectors

$$
[x]_\beta=(P_{\varepsilon\gets\beta})^{-1}x
$$

We will see in the next section that finding the matrix $$P_{\varepsilon\gets\beta}$$ is actually very easy.

### Coordinate vectors with matrices

Now, if you're comfortable with [*column perspective*](../columnperspective/){:target="_blank"}, you may have seen \eqref{coordinate} and thought, "that looks like matrix multiplication!" If so, yes, it is! If you have no idea what I'm talking about, basically

$$
c_1v_1+\ldots+c_nv_n=
\Bigg(v_1\quad \cdots\quad v_n\Bigg)
\begin{pmatrix}c_1\\\vdots\\c_n\end{pmatrix}
$$

For a more concrete example, take the previous example of $$v=(1,1)$$ and the basis $$\beta=\{(1,-1),(-1,2)\}$$, for which $$[v]_\beta=(3,2)$$.

$$3\begin{pmatrix}1\\-1\end{pmatrix}
+2\begin{pmatrix}-1\\2\end{pmatrix}=
\begin{pmatrix}1&-1\\-1&2\end{pmatrix}\begin{pmatrix}3\\2\end{pmatrix}=
\begin{pmatrix}1\\1\end{pmatrix}$$

It appears that $$\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$$ is the matrix for which

$$\begin{pmatrix}1&-1\\-1&2\end{pmatrix}[v]_\beta=[v]_\varepsilon$$

And it is! $$\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$$ *is* the change of basis matrix $$P_{\varepsilon\gets\beta}$$.

**For a given basis $$\beta=\{v_1,\ldots,v_n\}$$, the change of basis matrix $$P_{\varepsilon\gets\beta}$$ is constructed by just sticking the vectors into the columns.**

So, for example, if the basis is $$B=\{(1,1,1),(1,-1,0),(1,1,-2)\}$$, then the change of basis matrix $$P_{\varepsilon\gets B}$$ is just

$$\begin{pmatrix}1&1&1\\1&-1&1\\1&0&-2\end{pmatrix}$$

### Computing coordinate vectors

A few sections ago, we stated the following formula for a coordinate vector

$$
\begin{equation}\label{coordinatecompute}
[x]_\beta=(P_{\varepsilon\gets\beta})^{-1}x
\end{equation}
$$

Now that we know how to get $$P_{\varepsilon\gets\beta}$$ (put the vectors as the columns), we can say more directly that the coordinate vector for a basis $$\beta=\{v_1,\ldots,v_n\}$$ can be computed by

$$
\begin{equation}\label{coordinatecomputetwo}
[x]_\beta=\bigg(v_1\quad \cdots\quad v_n\bigg)^{-1}x
\end{equation}
$$

Column perspective makes this formula very intuitive, as the definition of a coordinate vector is essentially to be the solution to the equation

$$c_1v_1+\ldots+c_nv_n=x$$

which can be expressed as the matrix equation

$$
\Bigg(v_1\quad \cdots\quad v_n\Bigg)\begin{pmatrix}c_1\\\vdots\\c_n\end{pmatrix}=x
$$

### Coordinate vector example

Let's calculate the coordinate vector from before: $$v=(1,1)$$ with the basis $$\beta=\left\{\begin{pmatrix}1\\-1\end{pmatrix},\begin{pmatrix}-1\\2\end{pmatrix}\right\}$$. We have that

$$P_{\varepsilon\gets\beta}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}
\implies
P_{\beta\gets\varepsilon}=\begin{pmatrix}2&1\\1&1\end{pmatrix}
$$

using the formula of $$\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$$. Thus,

$$[v]_\beta=P_{\beta\gets\varepsilon}v=\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}3\\2\end{pmatrix}$$

## How to change bases

We will be going into how to directly compute a general change of basis matrix [in a later section](#Finding-change-of-basis-matrices). This is a more practical formulation which works better for two and three dimensional vector spaces.

First, as an analogy, let's say you want to translate something from French into German, but you don't speak either all that well. It would be a lot easier if you could translate the sentence into English first, and then translate that English sentence into German (assuming you are more comfortable with $$\varepsilon$$nglish). That is the fundamental idea behind the following corollary to \eqref{basiscombine} (which is *incredibly* useful).

$$
\begin{equation}\label{ezchange}
P_{\beta\gets\alpha}=P_{\beta\gets\varepsilon}P_{\varepsilon\gets\alpha}=(P_{\varepsilon\gets\beta})^{-1}P_{\varepsilon\gets\alpha}
\end{equation}
$$

Why are these formulas great, you may ask? Well, it's because the matrix $$P_{\varepsilon\gets\alpha}$$ is *really* easy to find (it's just the vectors as the columns!), while $$P_{\beta\gets\alpha}$$ is *really* computationally intensive to find directly if neither $$\alpha$$ or $$\beta$$ are the standard basis.

### Change of basis example

Let's find the matrix, for example, which changes from the basis $$\alpha=\left\{\begin{pmatrix}2\\1\end{pmatrix},\begin{pmatrix}3\\2\end{pmatrix}\right\}$$ to the basis $$\beta=\left\{\begin{pmatrix}1\\1\end{pmatrix},\begin{pmatrix}1\\2\end{pmatrix}\right\}$$.

The matrix with the vectors as the columns will give us the matrix which changes from the basis to the standard basis.

$$
P_{\varepsilon\gets\alpha}=\begin{pmatrix}2&3\\1&2\end{pmatrix}$$

$$P_{\varepsilon\gets\beta}=\begin{pmatrix}1&1\\1&2\end{pmatrix}\implies
P_{\beta\gets\varepsilon}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}
$$

Using our formula of $$P_{\beta\gets\alpha}=P_{\beta\gets\varepsilon}P_{\varepsilon\gets\alpha}$$

$$P_{\beta\gets\alpha}=
\begin{pmatrix}2&-1\\-1&1\end{pmatrix}
\begin{pmatrix}2&3\\1&2\end{pmatrix}=
\begin{pmatrix}3&4\\-1&-1\end{pmatrix}
$$

How do we know we're right, though? Basically, you just need to ensure that the columns of your resulting matrix $$\begin{pmatrix}3\\-1\end{pmatrix},\begin{pmatrix}4\\-1\end{pmatrix}$$ are the correct coordinates of the old basis ($$\alpha$$) vectors in the new basis ($$\beta$$):

$$
\begin{array}{cccccc}
  3\begin{pmatrix}1\\1\end{pmatrix}&-&\begin{pmatrix}1\\2\end{pmatrix}&=&\begin{pmatrix}2\\1\end{pmatrix}\\
  4\begin{pmatrix}1\\1\end{pmatrix}&-&\begin{pmatrix}1\\2\end{pmatrix}&=&\begin{pmatrix}3\\2\end{pmatrix}
\end{array}
$$

And those are indeed the vectors of $$\alpha$$!

Note that (by column perspective) this computation is equivalent to multiplying $$P_{\varepsilon\gets\beta}P_{\beta\gets\alpha}$$ and making sure you get $$P_{\varepsilon\gets\alpha}$$.

## Transformations on other bases

One of the most common applications of change of basis is to find the matrix of a transformation with respect to other bases.

### Linear operators

One of the most common cases is that you have a matrix for a linear operator $$T:V\to V$$ with respect to some known basis $$\alpha$$ of $$V$$ (usually the standard basis $$\alpha=\varepsilon$$), and want to find the matrix with respect to another basis of $$V$$, $$\beta$$. The formula is as follows:

$$
\begin{equation}
[T]_\beta=P_{\beta\gets\alpha}[T]_\alpha P_{\alpha\gets\beta}
\end{equation}
$$

The basic idea is this: suppose you cannot speak French, so you are using a translator to speak to your eight-year-old nephew who only speaks French. In the conversation, your nephew says something in French, which the translator has to convey to you in English ($$P{\text{Eng}\gets\text{Fr}}$$). Then, you can respond in English $$[T]{\text{Eng}}$$. But, for your nephew to understand what you said, the translator must translate it back into French ($$P{\text{Fr}\gets\text{Eng}}$$). Giving the full "conversation" as

$$[T]_{\text{Fr}}=P_{\text{Fr}\gets\text{Eng}}[T]_{\text{Eng}}P_{\text{Eng}\gets\text{Fr}}$$

### Linear operator example

Take the transformation which is a reflection about the line $$y=x$$. That is, $$T:F^2\to F^2,\quad T(x,y)=(y,x)$$. From the definition of $$T(x,y)=(y,x)$$, you can verify very easily that the matrix for this transformation on the standard basis is

$$[T]_\varepsilon=\begin{pmatrix}0&1\\1&0\end{pmatrix}$$

Let's say that I want the matrix for the transformation on the basis $$\beta=\left\{\begin{pmatrix}1\\1\end{pmatrix},\begin{pmatrix}1\\2\end{pmatrix}\right\}$$ (from before). We previously computed the change of basis matrices between $$\beta$$ and the standard basis to be

$$P_{\varepsilon\gets\beta}=\begin{pmatrix}1&1\\1&2\end{pmatrix},\quad
P_{\beta\gets\varepsilon}=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}$$

This tells us that the transformation matrix with respect to $$\beta$$, $$[T]_\beta$$, should be

$$[T]_\beta=P_{\beta\gets\varepsilon}[T]_\varepsilon P_{\varepsilon\gets\beta}$$

$$[T]_\beta=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&1\\1&2\end{pmatrix}=\begin{pmatrix}1&3\\0&-1\end{pmatrix}$$

We can check that this is indeed the correct answer by transforming the basis vectors of $$\beta$$.

$$
\begin{array}{cccccc}
  T\begin{pmatrix}1\\1\end{pmatrix}&=&\begin{pmatrix}1\\1\end{pmatrix}&=&1\begin{pmatrix}1\\1\end{pmatrix}&+&0\begin{pmatrix}1\\2\end{pmatrix}\\
  T\begin{pmatrix}1\\2\end{pmatrix}&=&\begin{pmatrix}2\\1\end{pmatrix}&=&3\begin{pmatrix}1\\1\end{pmatrix}&-&1\begin{pmatrix}1\\2\end{pmatrix}
\end{array}
$$

We can confirm that the coordinate vector for $$T(v_1)=\begin{pmatrix}1\\1\end{pmatrix}$$ with respect to the basis $$\beta$$ is $$\begin{pmatrix}1\\0\end{pmatrix}$$, the first column of $$[T]_\beta$$, and similarly $$[T(v_2)]_\beta=\begin{pmatrix}3\\-1\end{pmatrix}$$, the second column of $$[T]_\beta$$.

### V to W

If $$T:V\to W$$ is a linear transformation to a different vector space $$W$$, then you have to deal with two different bases for each space: let's say $$\alpha,\alpha'$$ for $$V$$, and $$\beta,\beta'$$ for $$W$$.

Here's the thing... A formula for $$[T]_{\alpha'}^{\beta'}$$ given $$[T]_\alpha^\beta$$ is simply *not* worth memorizing, in my opinion. So, instead of just giving it to you, I'm going to explain the intuition behind what the formula *does*. Hopefully, that can give you the capability to come up with the formula on your own.

We can transform $$\alpha$$ vectors in terms of $$\beta$$ vectors using $$[T]_\alpha^\beta$$, and we want to transform $$\alpha'$$ vectors in terms of $$\beta'$$ vectors. Thus, we could translate our input of $$\alpha'$$ vectors to $$\alpha$$ vectors first ($$P_{\alpha\gets\alpha'}$$), and apply the transformation which gives us the results in terms of $$\beta$$ vectors ($$[T]_\alpha^\beta$$). Finally, to get things in terms of $$\beta'$$ vectors, we translate one last time from $$\beta$$ to $$\beta'$$ ($$P_{\beta'\gets\beta}$$). Putting it all together:

$$
\begin{equation}
[T]_{\alpha'}^{\beta'}=P_{\beta'\gets\beta}[T]_\alpha^\beta P_{\alpha\gets\alpha'}
\end{equation}
$$

Imagine you have a magical French to German translation machine, and you want to translate English to Spanish. Then you could put the magical machine between intermediary machines that take English to French and German to Spanish. That is, translate English to what your magical machine takes in (French), so that it can take the input. Then, the output of the magical machine will be German. So, we take the magical machine output of German, and translate it to Spanish, which is what we want. The resulting combination of the three machines is something that takes in English, and outputs something in Spanish.

$$[T]_\text{Eng}^\text{Spa}=P_{\text{Spa}\gets\text{Ger}}[T]_\text{Fr}^\text{Ger} P_{\text{Fr}\gets\text{Eng}}$$

## Finding change of basis matrices

While \eqref{ezchange} is great for two and three dimensional vector spaces (because $$2\times2$$ and $$3\times3$$ matrix inverses are relatively easy), if you have a larger vector space, it can be quite difficult to invert the matrix and multiply it all out. Instead, there is a direct process that uses row reduction of a super-augmented matrix instead.

To find $$P_{\beta\gets\alpha}$$,

$$
\begin{eqnarray}
  \big[\begin{array}{c|c}
  P_{\varepsilon\gets\beta}&P_{\varepsilon\gets\alpha}
  \end{array}\big]
  &\quad\underrightarrow{\text{row reduce}}\quad&
  \big[\begin{array}{c|c}
  I&P_{\beta\gets\alpha}
  \end{array}\big]\\
  \big[\begin{array}{c|c}
  \text{new basis}&\text{old basis}
  \end{array}\big]
  &\quad\underrightarrow{\text{row reduce}}\quad&
  \big[\begin{array}{c|c}
  I&P_{\text{new}\gets\text{old}}
  \end{array}\big]
\end{eqnarray}
$$

It's similar to finding the inverse of a matrix, but instead we have a non-identity matrix on both sides.

If you want to know why this works, there are two explanations. If you don't, then idk the post is over you can leave now.

1. You can get to this by solving $$n$$ systems of equations at once: trying to find the coordinate vectors of the vectors in $$\beta$$ with respect to the vectors in $$\alpha$$
2. Using [*column perspective*](../columnperspective/){:target="_blank"}, you can see that if you multiply the matrix by
$$(P_{\varepsilon\gets\alpha})^{-1}$$, you get
$$(P_{\varepsilon\gets\beta})^{-1}\big[\begin{array}{c|c}
  P_{\varepsilon\gets\beta}&P_{\varepsilon\gets\alpha}
  \end{array}\big]=
  \big[\begin{array}{c|c}
  (P_{\varepsilon\gets\beta})^{-1}P_{\varepsilon\gets\beta}&P_{\beta\gets\varepsilon}P_{\varepsilon\gets\alpha}
  \end{array}\big]=
  \big[\begin{array}{c|c}
  I&P_{\alpha\gets\beta}
  \end{array}\big]$$
  and, if you didn't know, row reducing an invertible matrix is exactly equivalent to multiplying on the left by the inverse.

  $$A^{-1}\big[\begin{array}{c|c}
  A&I
  \end{array}\big]=
  \big[\begin{array}{c|c}
  A^{-1}A&A^{-1}I
  \end{array}\big]=
  \big[\begin{array}{c|c}
  I&A^{-1}
  \end{array}\big]$$

(so that's why that works if you were wondering)

[hyperlink](https://youtu.be/GxPSApAHakg){:target="_blank"}
