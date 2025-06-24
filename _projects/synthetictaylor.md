---
layout: page
title: Finding Taylor Series of Polynomials Using Synthetic Division
date: 2021-09-27 0
description: Wait you can do that? YUP
comments: true
importance: 3
category: calculus
---

Ah... synthetic division. One of the most underrated techniques taught in algebra. For it is not *just* a method of dividing polynomials by linear factors, but has a number of uses beyond that.

For example, it is the fastest way to evaluate a polynomials with many nonzero terms. For a concrete demonstration on why this is, compare these two ways to write a cubic polynomial:

$$\begin{gather}
a_0+a_1x+a_2x^2+a_3x^3\\
a_0+x(a_1+x(a_2+x(a_3)))
\end{gather}$$

Now consider all the arithmetic calculations necessary to evaluate each at a specific point.

For the first you need to do three multiplications ($$x\cdot x\cdot x\cdot a_3$$), then two multiplications ($$x\cdot x\cdot a_2$$), then one addition ($$a_2x^2+a_3x^3$$), then one multiplication ($$x\cdot a_1$$), then two additions ($$a_0+(a_1x)+(a_2x^2+a_3x^3)$$). In total, that is nine arithmetic operations.

The second (this is actually called Horner's method), working inside out, is one multiplication ($$x\cdot a_3$$), then one addition ($$(a_2+x(a_3))$$), then one multiplication ($$x(a_2+x(a_3))$$), then one addition ($$a_1+x(a_2+x(a_3))$$), then one multiplication ($$x(a_1+x(a_2+x(a_3)))$$), and then finally one addition $$a_0+x(a_1+x(a_2+x(a_3)))$$. In total, that was six arithmetic operations.

Now, when we actually did the steps for the second method you *may* have noticed that these were the exact arithmetic steps one does when doing synthetic division. That is because we are.

In general, doing it the normal way for an $$n$$-th degree polynomial requires up to $$\frac{n(n+3)}{2}$$ arithmetic operations, while synthetic division requires up to $$2n$$. Linear growth is definitely much better than quadratic growth.

Now you may ask "how much of a difference does this actually make if I'm putting it into a calculator?" And the answer is that it doesn't make any difference. Calculators are nice because they can do more calculations faster. However, if you are like me and prefer to evaluate polynomials by hand, then this is by far the most efficient way to do it (at least for polynomials of degree 3 or higher).

That said! If you want to calculate $$p(c)$$ *and* $$p'(c)$$ (or any other derivatives of $$p$$ evaluated at the same point), then synthetic division will be the most efficient way to do it (when it isn't trivial), as you can simply repeat it over and over again. And this is where Taylor series come in: since to calculate a Taylor series you need $$p(c),p'(c),p''(c),\ldots$$.

So let's cut to the chase. How does synthetic division give us our Taylor coefficients? Let's start by looking at the polynomial $$p(x)=4x^3-21x^2+38x-23$$ and synthetically dividing all the way down at $$x=2$$:

$$
\begin{array}{c|cccc}
2&4&-21&38&-23\\
&&8&-26&24\\
\hline
2&4&-13&12&1\\
&&8&-10&\\
\hline
2&4&-5&2\\
&&8&\\
\hline
2&4&3\\
\\
\hline
&4
\end{array}
$$

Now let's do the seemingly unrelated task of finding the Taylor series of $$p(x)$$ centered at $$x=2$$.

One may compute that $$p(2)=1,p'(2)=2,p''(2)=6,p'''(2)=24$$ and every subsequent derivative is zero. So the Taylor series is

$$p(x)=1+2(x-2)+\frac{6}{2!}(x-2)^2+\frac{24}{3!}(x-2)^3$$

$$p(x)=1+2(x-2)+3(x-2)^2+4(x-2)^3$$

Now those coefficients may seem familiar. In fact, they are the remainders from doing synthetic division. The remainders were 1, then 2, then 3, then 4. And this will in fact work in general. If you do synthetic division until you reach a constant term, the remainders will be the coefficients for the powers of $$x-c$$.

In general, given the polynomial $$p(x)=a_0+a_1(x-c_1)+\ldots+a_n(x-c_1)^n$$, repeatedly performing synthetic division at the point $$x=c_2$$ yields

$$
\begin{equation}
\begin{array}{c|ccccc}
c_2&a_n&a_{n-1}&\dots&a_1&a_0\\
&&ca_n&\dots&*&*\\
\hline
c_2&a_n&ca_n+a_{n-1}&\dots&*&b_0\\
&&ca_n&\dots&*\\
\hline
c_2&a_n&2ca_n+a_{n-1}&\dots&b_1\\
&\vdots&\vdots&\vdots\\
\hline
&a_n&b_{n-1}\\
\\
\hline
&a_n
\end{array}
\end{equation}
$$

And the Taylor series of $$p(x)$$ centered at $$x=c_1-c_2$$ will be

$$
\begin{equation}
p(x)=b_0+b_1(x-c_1+c_2)+\ldots+b_{n-1}(x-c_1+c_2)^{n-1}+b_n(x-c_1+c_2)^n
\end{equation}
$$

So not only does this allow us to calculate Taylor series, but it allows us to shift them too. So one small application of this is to save us the time of expanding out a Taylor series if we want to put it into standard form.

For example, to get the polynomial $$p(x)=4x^3-21x^2+38x-23$$, I started with $$1+2(x-2)+3(x-2)^2+4(x-2)^3$$, and then performed synthetic division repeatedly at $$x=-2$$. The remainders were $$-23,38,-21,4$$. Though I don't feel like counting out the specific arithmetic operations necessary to expand out the binomials and combine like terms, I know for a fact that the arithmetic operations required for synthetic division are *much* simpler and easier to do mentally.
