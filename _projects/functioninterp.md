---
layout: distill
title: Function Interpolation
date: 2021-08-16
description: Find a function that matches your requirements
comments: true
importance: 2
category: linear algebra
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: The Determinant Polynomial
    subsections:
      - name: Polynomial Example
  - name: Applications to polynomials
    subsections:
      - name: Evaluating unknown polynomials
      - name: Synthetic division
  - name: Generalizing Beyond Polynomials
    subsections:
      - name: The System Function
      - name: A non-polynomial example
---

This is a technique that I "discovered" on my own a few years ago. It's a way to find the unique function, which is a linear combination of any set of basis functions, which satisfies given conditions, using determinants.

The downside of this technique is that it suffers some of the same problems that determinants in general do, in that it can be unwieldy to use and require some substantial computational power. Additionally, it only works if the function you're looking for is unique. It is useless to get you a particular solution if there is more than one possibility. For example, if you have seven basis functions, but only three conditions, this will not be useful to you. However, it can do a number of neat things which may make it worth the effort. Especially if one is willing to use a computer to do the dirty work.

---

# The Determinant Polynomial

So let us start where I did when I found this: [Polynomial Interpolation](../polyinterp/){:target="_blank"}.

For the purposes of simplicity, we will assume that the constraints we require on our polynomial $$p(x)$$ will simply be that they pass through a set of points (with distinct $$x$$ values) $$\{(x_1,y_1),\ldots,(x_n,y_n)\}$$ (equivalent to requiring that $$p(x_1)=y_1,\ldots,p(x_n)=y_n$$).

However, this process can be generalized to have requirements on the $$k_i$$-th derivative of $$p(x)$$, $$p^{(k_i)}(x_i)=y_i$$, where $$k_i$$ is a nonnegative integer. The input $$x$$ values do not also have to be distinct if the requirements are on the derivatives. For example, you can have a condition on $$p(x_1),p'(x_1),p(x_2)$$.

If we have $$n$$ constraints on our polynomial, we can *usually* safely assume that our polynomial will be of the form

$$
\begin{equation}\label{px}
p(x)=a_0+a_1x+\ldots+a_{n-1}x^{n-1}
\end{equation}
$$

We then define the vectors

$$
\begin{equation}
\vec{a}=\begin{bmatrix}a_0\\\vdots\\a_{n-1}\end{bmatrix},\quad\vec{y}=\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix}
\end{equation}
$$

and the matrix $$F$$ such that

$$
\begin{equation}
F\vec{a}=\vec{y}
\end{equation}
$$

accurately demonstrates the constraints on the polynomial \eqref{px}. For us, since we are just requiring that $$p(x_1)=y_1,\ldots,p(x_n)=y_n$$, our system would be

$$
\begin{equation}
\begin{bmatrix}
1&x_1&x_1^2&\dots&x_1^{n-1}\\
1&x_2&x_2^2&\dots&x_2^{n-1}\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
1&x_n&x_n^2&\dots&x_n^{n-1}\\
\end{bmatrix}
\begin{bmatrix}a_0\\a_1\\a_2\\\vdots\\a_{n-1}\end{bmatrix}=\begin{bmatrix}y_1\\y_2\\\vdots\\y_n\end{bmatrix}
\end{equation}
$$

But if one of our requirements had been that $$p'(x_i)=y_i$$, for example, then the $$i$$-th row of $$F$$ would be

$$\begin{bmatrix}0&1&2x_i&\dots&(n-1)x_i^{n-2}\end{bmatrix}$$

**We now assume that** $$F$$ **is invertible.** If $$F$$ is not invertible, then a unique function which satisfies all $$n$$ constraints does not exist.

Define the vector

$$
\begin{equation}
\vec{x}^i=\begin{bmatrix}x_1^i\\\vdots\\x_n^i\end{bmatrix}
\end{equation}
$$

So that we may write the matrix $$F$$ we will be using as

$$
\begin{equation}
F=
\begin{bmatrix}
\vec{x}^0&\vec{x}^1&\vec{x}^2&\dots&\vec{x}^{n-1}
\end{bmatrix}
\end{equation}
$$

Okay. Now it is time to bust out our good friend, Cramer's Rule. If we do so, we can find explicit expressions for each coefficient of the polynomial and write it out directly. In general,

$$
\begin{equation}
a_i=
\frac
{\begin{vmatrix}
\vec{x}^0&\vec{x}^1&\dots&\vec{x}^{i-1}&\vec{y}&\vec{x}^{i+1}&\dots&\vec{x}^{n-1}
\end{vmatrix}}
{\begin{vmatrix}
\vec{x}^0&\vec{x}^1&\dots&\vec{x}^{i-1}&\vec{x}^i&\vec{x}^{i+1}&\dots&\vec{x}^{n-1}
\end{vmatrix}}
\end{equation}
$$

We now do a step of simplification for the top determinant. We will swap the columns such that $$\vec{y}$$ is always the rightmost column, and the powers are still ascending left to right. This will require $$n-i+1$$ column swaps. Therefore,

$$\begin{vmatrix}
\vec{x}^0&\vec{x}^1&\dots&\vec{x}^{i-1}&\vec{y}&\vec{x}^{i+1}&\dots&\vec{x}^{n-1}
\end{vmatrix}=(-1)^{n-i+1}
\begin{vmatrix}
\vec{x}^0&\vec{x}^1&\dots&\vec{x}^{i-1}&\vec{x}^{i+1}&\dots&\vec{x}^{n-1}&\vec{y}
\end{vmatrix}$$

We use the fact that $$(-1)^{n-i+1}=(-1)^{1-n}(-1)^i$$, and define the matrix

$$
\begin{equation}
F_i=
\begin{bmatrix}
\vec{x}^0&\vec{x}^1&\dots&\vec{x}^{i-1}&\vec{x}^{i+1}&\dots&\vec{x}^{n-1}&\vec{y}
\end{bmatrix}
\end{equation}
$$

and the constant

$$
\begin{equation}
\Delta=
(-1)^{n-1}\det(F)
\end{equation}
$$

We then obtain a simpler expression for $$a_i$$,

$$
\begin{equation}
a_i=
\Delta^{-1}(-1)^i\det(F_i)
\end{equation}
$$

And now have an explicit formula for $$p(x)$$:

$$
\begin{equation}
p(x)=\Delta^{-1}(\det(F_0)+(-1)^1\det(F_1)x+\ldots+(-1)^{n-1}\det(F_{n-1})x^{n-1})
\end{equation}
$$

Observe that the expression in the parentheses looks suspiciously like Cofactor expansion, in that its a linear combination of determinants that pretty much have the same columns, except each is missing exactly one.

In fact, it looks like the determinant of a matrix of the form

$$
\begin{equation}\label{Pmatrix1}
P=
\begin{bmatrix}
p_{11}&p_{12}&\dots&p_{1(i-1)}&p_{1i}&p_{1(i+1)}&\dots&p_{1n}&p_{1(n+1)}\\
\vec{x}^0&\vec{x}^1&\dots&\vec{x}^{i-1}&\vec{x}^i&\vec{x}^{i+1}&\dots&\vec{x}^{n-1}&\vec{y}
\end{bmatrix}
\end{equation}
$$

Compare the general terms of cofactor expansion along the first row of $$P$$ and $$\Delta p(x)$$:

$$
\begin{equation}
\det(P)=\sum_{k=1}^{n+1} (-1)^{1+k}\det(F_{k-1})p_{1k},
\quad\Delta p(x)=\sum_{k=1}^n (-1)^{1+k}\det(F_{k-1})x^{k-1}
\end{equation}
$$

we can figure out exactly what the entries of the first row of \eqref{Pmatrix1} need to be. It appears that the first $$n$$ entries are powers of $$x$$, and $$p_{1(n+1)}$$ must be zero.

$$p_{1k}=\begin{cases}x^{k-1},&k\leq n\\0,&k=n+1\end{cases}$$

We find the matrix $$P$$ to then be

$$
\begin{equation}\label{Pmatrix}
P=
\begin{bmatrix}
1&x&x^2&\dots&x^{n-1}&0\\
\vec{x}^0&\vec{x}^1&\vec{x}^2&\dots&\vec{x}^{n-1}&\vec{y}
\end{bmatrix}
\end{equation}
$$

And it follows that

$$
\begin{equation}
p(x)=\Delta^{-1}\det\left(
\begin{bmatrix}
1&x&x^2&\dots&x^{n-1}&0\\
\vec{x}^0&\vec{x}^1&\vec{x}^2&\dots&\vec{x}^{n-1}&\vec{y}
\end{bmatrix}\right)
\end{equation}
$$

$$
\begin{equation}
p(x)=(-1)^{n+1}\frac{\det\left(
\begin{bmatrix}
1&x&x^2&\dots&x^{n-1}&0\\
\vec{x}^0&\vec{x}^1&\vec{x}^2&\dots&\vec{x}^{n-1}&\vec{y}
\end{bmatrix}\right)}
{\det\left(\begin{bmatrix}
\vec{x}^0&\vec{x}^1&\vec{x}^2&\dots&\vec{x}^{n-1}
\end{bmatrix}\right)}
\end{equation}
$$

If we define the vector

$$
\begin{equation}
\vec{x}=(1,x,x^2,\ldots,x^{n-1})
\end{equation}
$$

Then we can write this more compactly (and generally) as

$$
\begin{equation}\label{detpoly}
p(x)=(-1)^{n+1}\frac{\det\left(
\begin{bmatrix}
\vec{x}&0\\
F&\vec{y}
\end{bmatrix}\right)}
{\det(F)}
\end{equation}
$$

---

## Polynomial Example

Let's do a quick example just to show that it works. How about the classic quadratic passing through $$(1,9),(2,7),(3,-1)$$?

Well, for a polynomial of the form $$p(x)=a_0+a_1x+a_2x^2$$ to pass through these points, the coefficients must satisfy this system

$$\begin{equation}
\begin{bmatrix}
1&1&1^2\\
1&2&2^2\\
1&3&3^2
\end{bmatrix}
\begin{bmatrix}
a_0\\a_1\\a_2
\end{bmatrix}
=\begin{bmatrix}
9\\7\\-1
\end{bmatrix}
\end{equation}$$

Now, supposedly, if my derivation is correct, we should get the correct answer $$p(x)=5+7x-3x^2$$ when we evaluate

$$\begin{equation}
p(x)=(-1)^{3+1}
\frac{
\begin{vmatrix}
1&x&x^2&0\\
1&1&1^2&9\\
1&2&2^2&7\\
1&3&3^2&-1
\end{vmatrix}}{
\begin{vmatrix}
1&1&1^2\\
1&2&2^2\\
1&3&3^2
\end{vmatrix}}
\end{equation}$$

And as a matter of fact, you do! As a pro-tip for making the evaluation of these determinants easier, note that you can add any scalar multiple of one row to another without changing the determinant. So we could also say that

$$
p(x)=(-1)^{3+1}
\frac{
\begin{vmatrix}
1&x&x^2&0\\
1&1&1^2&9\\
0&1&3&-2\\
0&2&8&-10
\end{vmatrix}}{
\begin{vmatrix}
1&1&1^2\\
0&1&3\\
0&2&8
\end{vmatrix}}
$$

Which are much easier determinants to evaluate. There are other row operations you could perform to simplify the evaluating, and indeed I believe they are worth doing. In fact, I will perform a few more simplifications so that the solution is a bit more clear if you wish to view them:

<details style="color: white;"><summary>Further evaluation</summary>
$$
p(x)=
\frac{
\begin{vmatrix}
1&x&x^2&0\\
1&0&-2&11\\
0&1&3&-2\\
0&0&2&-6
\end{vmatrix}}{
\begin{vmatrix}
1&3\\
2&8
\end{vmatrix}}
$$

$$
p(x)=
\frac{
2\begin{vmatrix}
1&x&x^2&0\\
1&0&-2&11\\
0&1&3&-2\\
0&0&1&-3
\end{vmatrix}}{
2}
$$

$$
p(x)=
\begin{vmatrix}
1&x&x^2&0\\
1&0&0&5\\
0&1&0&7\\
0&0&1&-3
\end{vmatrix}
$$

$$
p(x)=
1\begin{vmatrix}
0&0&5\\
1&0&7\\
0&1&-3
\end{vmatrix}-1\begin{vmatrix}
x&x^2&0\\
1&0&7\\
0&1&-3
\end{vmatrix}
$$

Expand along first column:

$$
p(x)=
5-(-7x+3x^2)=5+7x-3x^2
$$
</details>

## Applications to polynomials

### Evaluating unknown polynomials

Let's say we don't know that $$p(x)=-3x^2+7x+5$$ is the unique quadratic that passes through $$(1,9),(2,7),(3,-1)$$. Now consider the following problem:

**If a quadratic $$p(x)$$ passes through the points $$(1,9),(2,7),(3,-1)$$, then what is $$p(-1)$$?**

Since we know what the polynomial is, we can know what the answer is ahead of time. $$p(-1)=-3(-1)^2+7(-1)+5=-5$$. But we also have our determinant form of the polynomial:

$$\begin{equation}
p(-1)=(-1)^{3+1}
\frac{
\begin{vmatrix}
1&-1&(-1)^2&0\\
1&1&1^2&9\\
1&2&2^2&7\\
1&3&3^2&-1
\end{vmatrix}}{
\begin{vmatrix}
1&1&1^2\\
1&2&2^2\\
1&3&3^2
\end{vmatrix}}
\end{equation}$$

And, indeed, if you evaluate these determinants, you will in fact get $$p(-1)=-5$$. Therefore, if you don't know *what* the polynomial is, but you know the constraints it satisfies, you can use the determinant polynomial to evaluate it at any point.

Compare this to solving for the polynomial first, and *then* evaluating it. This is just a simple computation, which can be done very quickly with a computer.

### Synthetic division

Now if you were viewing some of the simplification steps above, you may have wondered why I didn't subtract the second row from the first row to get a column with only one nonzero entry. The reason is because I didn't want to spoil the surprise. First I want to use synthetic division on $$p(x)=-3x^2+7x+5$$ at the point $$x=1$$.

$$
\begin{array}{c|ccc}
1&-3&7&5\\
&&-3&4\\
\hline
&-3&4&9
\end{array}
$$

This tells us that $$-3x^2+7x+5=9+(x-1)(-3x+4)$$.

Now let's go back to the step $$
p(x)=(-1)^{3+1}
\frac{
\begin{vmatrix}
1&x&x^2&0\\
1&1&1^2&9\\
0&1&3&-2\\
0&2&8&-10
\end{vmatrix}}{
\begin{vmatrix}
1&1&1^2\\
0&1&3\\
0&2&8
\end{vmatrix}}
$$ and subtract the second row from the first.

$$
p(x)=(-1)^{3+1}
\frac{
\begin{vmatrix}
0&x-1&x^2-1^2&-9\\
1&1&1^2&9\\
0&1&3&-2\\
0&2&8&-10
\end{vmatrix}}{
\begin{vmatrix}
1&1&1^2\\
0&1&3\\
0&2&8
\end{vmatrix}}
$$

Now we can do a few simplification steps.

<details style="color: white;">
We know that $$(-1)^{3+1}=1$$ and $$\begin{vmatrix}
1&1&1^2\\
0&1&3\\
0&2&8
\end{vmatrix}=2$$ We can also expand along the first column of the top determinant, and divide out a 2 from the fourth row.

$$
p(x)=
\frac{
-2\begin{vmatrix}
x-1&x^2-1^2&-9\\
1&3&-2\\
1&4&-5
\end{vmatrix}}{
2}
$$

$$
p(x)=
-\begin{vmatrix}
x-1&x^2-1^2&-9\\
1&3&-2\\
1&4&-5
\end{vmatrix}
$$

Distribute the negative to the third column:

$$
p(x)=
\begin{vmatrix}
x-1&x^2-1^2&9\\
1&3&2\\
1&4&5
\end{vmatrix}
$$

Now this is the weird step. The determinant function is linear in its rows and columns, so we can say that

$$
\begin{vmatrix}
x-1&x^2-1^2&9\\
1&3&2\\
1&4&5
\end{vmatrix}=\begin{vmatrix}
x-1&x^2-1^2&0\\
1&3&2\\
1&4&5
\end{vmatrix}+\begin{vmatrix}
0&0&9\\
1&3&2\\
1&4&5
\end{vmatrix}
$$

The right determinant evaluates to 9, and we can factor out a common x-1 from the top row of the left determinant.

$$
p(x)=(x-1) \begin{vmatrix}
1&x+1&0\\
1&3&2\\
1&4&5
\end{vmatrix}+9
$$

$$
p(x)=(x-1) \begin{vmatrix}
0&x-2&-2\\
1&3&2\\
0&1&3
\end{vmatrix}+9
$$

$$
p(x)=-(x-1) \begin{vmatrix}
x-2&-2\\
1&3
\end{vmatrix}+9
$$
</details>

We finally obtain

$$
p(x)=
(x-1)(-3x+4)+9
$$

Which is exactly the result of using synthetic division on $$p(x)$$ at $$x=1$$. And indeed, one can preemptively perform synthetic division on the determinant polynomial at any point for which a point is guaranteed.

I encourage you to try and derive the point-slope form of a line $$y=y_1+\frac{y_2-y_1}{x_2-x_1}(x-x_1)$$ using the system

$$
\begin{bmatrix}
1&x_1\\
1&x_2\\
\end{bmatrix}
\begin{bmatrix}
a_0\\a_1
\end{bmatrix}
=\begin{bmatrix}
y_1\\y_2
\end{bmatrix}
$$

In fact, one can perform synthetic division multiple times if there is a constraint on not just the value of $$p(x_1)$$, but also $$p'(x_1),\ldots,p^{(m)}(x_1)$$. [Here](http://mathb.in/63109) is an example of finding a simplified form of a quadratic with a vertex as $$(x_1,y_1)$$ which also passes through $$(x_2,y_2)$$. I call it the point-vertex form of a parabola as it has striking similarities to the point-slope form of a line.

$$\begin{equation}
p(x)=y_1+\frac{y_2-y_1}{(x_2-x_1)^2}(x-x_1)^2
\end{equation}$$

# Generalizing Beyond Polynomials

What if instead of using $$p(x)=a_0+a_1x+\ldots+a_{n-1}x^{n-1}$$, we used different functions than powers of $$x$$?

Instead, what if we had

$$\begin{equation}
g(x)=a_1f_1(x)+\ldots+a_nf_n(x)
\end{equation}$$

Where $$f_1(x),\ldots,f_n(x)$$ are linearly independent functions.

Our equations won't be quite as nice, but they will still have a relatively consistent form.

If a constraint is $$g(x_i)=y_i$$, then our equation would be

$$\begin{equation}
a_1f_1(x_i)+\ldots+a_nf_n(x_i)=y_i
\end{equation}$$

And if we had a more general constraint such as $$g^{(k_i)}(x_i)=y_i$$, for some nonnegative integer $$k_i$$, it would be

$$\begin{equation}
a_1f_1^{(k_i)}(x_i)+\ldots+a_nf_n^{(k_i)}(x_i)=y_i
\end{equation}$$

Then the general form of our $$F$$ matrix can be

$$\begin{equation}
F=\begin{bmatrix}
f_1^{(k_1)}(x_1)&\dots&f_n^{(k_1)}(x_1)\\
\vdots&\ddots&\vdots\\
f_1^{(k_n)}(x_n)&\dots&f_n^{(k_n)}(x_n)\\
\end{bmatrix}
\end{equation}$$

And our general system is still $$F\vec{a}=\vec{y}$$

$$\begin{equation}
\begin{bmatrix}
f_1^{(k_1)}(x_1)&\dots&f_n^{(k_1)}(x_1)\\
\vdots&\ddots&\vdots\\
f_1^{(k_n)}(x_n)&\dots&f_n^{(k_n)}(x_n)\\
\end{bmatrix}
\begin{bmatrix}
a_1\\\vdots\\a_n
\end{bmatrix}
=\begin{bmatrix}
y_1\\\vdots\\y_n
\end{bmatrix}
\end{equation}$$

then we can repeat the same process that we did before to get the determinant polynomial, since this too is a function which is a linear combination of functions.

## The System Function

$$
\begin{equation}
g(x)=(-1)^{n+1}\frac{\det\left(
\begin{bmatrix}
f_1(x)&\dots&f_n(x)&0\\
f_1^{(k_1)}(x_1)&\dots&f_n^{(k_1)}(x_1)&y_1\\
\vdots&\ddots&\vdots&\vdots\\
f_1^{(k_n)}(x_n)&\dots&f_n^{(k_n)}(x_n)&y_n\\
\end{bmatrix}\right)}
{\det\left(
\begin{bmatrix}
f_1^{(k_1)}(x_1)&\dots&f_n^{(k_1)}(x_1)\\
\vdots&\ddots&\vdots\\
f_1^{(k_n)}(x_n)&\dots&f_n^{(k_n)}(x_n)\\
\end{bmatrix}\right)}
\end{equation}
$$

If we define the vector

$$
\begin{equation}
\vec{f}(x)=\begin{bmatrix}f_1(x)&\dots&f_n(x)\end{bmatrix}
\end{equation}
$$

we can again write this more compactly as

$$
\begin{equation}
g(x)=(-1)^{n+1}\frac{\det\left(
\begin{bmatrix}
\vec{f}(x)&0\\
F&\vec{y}
\end{bmatrix}\right)}
{\det(F)}
\end{equation}
$$

### A non-polynomial example

In my post on Polynomial Interpolation, I discussed the example of having a function of the form $$g(x)=a_1+a_2e^{x}+a_3e^{-x}$$ that passes through the same points as our original quadratic, $$(1,9),(2,7),(3,-1)$$. The equations remaining similar,

$$
\begin{array}{cc}
g(1)=9&\implies&a_1+a_2e^{1}+a_3e^{-1}=9\\
g(2)=7&\implies&a_1+a_2e^{2}+a_3e^{-2}=7\\
g(3)=-1&\implies&a_1+a_2e^{3}+a_3e^{-3}=-1\\
\end{array}
$$

The system of equations in matrix form being

$$\begin{equation}
\begin{bmatrix}
1&e^1&e^{-1}\\
1&e^2&e^{-2}\\
1&e^3&e^{-3}
\end{bmatrix}
\begin{bmatrix}
a_1\\a_2\\a_3
\end{bmatrix}
=\begin{bmatrix}
9\\7\\-1
\end{bmatrix}
\end{equation}$$

So the system function would be

$$
\begin{equation}
g(x)=(-1)^{3+1}\frac{\det\left(
\begin{bmatrix}
1&e^x&e^{-x}&0\\
1&e^1&e^{-1}&9\\
1&e^2&e^{-2}&7\\
1&e^3&e^{-3}&-1
\end{bmatrix}\right)}
{\det\left(
\begin{bmatrix}
1&e^1&e^{-1}\\
1&e^2&e^{-2}\\
1&e^3&e^{-3}
\end{bmatrix}\right)}
\end{equation}
$$

Now, before getting your hopes up, the answer for this problem will not be pretty, regardless of how carefully you perform row operations. The main weakness of the system is now readily apparent. However, since one of our functions is constant, it is easy to reduce the size of the determinants by one, allowing us to expand manually. I'm not going to do that though, and instead put it into Wolfram Alpha because I am lazy. :)

$$
\begin{equation}
g(x)=\frac{2e^{x-1}-8e^x+2e^{4-x}-8e^{3-x}+7-e-e^2+7e^3}{(e-1)^2(1+e)}
\end{equation}
$$

Absolutely horrendous. BUT, it works. As you can see in this [desmos graph](https://www.desmos.com/calculator/clsuujrtpq){:target="_blank"}, it passes through the points.

Is this better than solving the system manually and finding the coefficients? I dunno; probably not. But at least the answer is in one nice package, and you can write it without needing to solve anything. Then you can put it into a calculator to expand it for you.
