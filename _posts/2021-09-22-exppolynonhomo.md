---
layout: page
title: A Formula for Some Particular Solutions
date: 2021-09-22 0
description: Yet another obnoxious formula for solutions to constant coefficient nonhomogeneous ODE's with common forcing functions.
comments: true
importance: 4
categories: differential-equations
---

I found this a few days ago, and while I may call it obnoxious, I wouldn't necessarily call it useless (or at least as useless as I thought it was when I originally derived it).

It is a general form for a particular solution of differential equations of the forms

$$
\begin{align}\label{real}
a_ny^{(n)}+\ldots+a_1y'+a_0y=&(b_0+b_1t+\ldots+b_mt^m)e^{\alpha t}\\\label{re}
a_ny^{(n)}+\ldots+a_1y'+a_0y=&(b_0+b_1t+\ldots+b_mt^m)e^{at}\cos(bt)\\\label{im}
a_ny^{(n)}+\ldots+a_1y'+a_0y=&(b_0+b_1t+\ldots+b_mt^m)e^{at}\sin(bt)\\
\end{align}
$$

The more compact way to write all of these is

$$\begin{equation} \label{1}
p(D)y=(b_0+b_1t+\ldots+b_mt^m)e^{\alpha t}
\end{equation}$$

Where $$D$$ is the differential operator $$Dy=y'$$, $$p(x)$$ is the characteristic equation of the differential equation, and $$\alpha=a+bi$$ for the cases with sines and cosines.

The formula is as follows:

---

Let $$s$$ be the smallest integer such that $$p^{(s)}(\alpha)\neq0$$.

A particular solution is given by

$$\begin{equation}\label{2}
y_p=(-1)^mt^se^{\alpha t}
\frac{\begin{vmatrix}
1&t&t^2&\dots&t^m&0\\
p^{(s)}(\alpha)\binom{s}{0}&p^{(s+1)}(\alpha)\binom{s+1}{0}&p^{(s+2)}(\alpha)\binom{s+2}{0}&\dots&p^{(s+m)}(\alpha)\binom{s+m}{0}&b_0\\
0&p^{(s)}(\alpha)\binom{s+1}{1}&p^{(s+1)}(\alpha)\binom{s+2}{1}&\dots&p^{(s+m-1)}(\alpha)\binom{s+m}{1}&b_1\\
0&0&p^{(s)}(\alpha)\binom{s+2}{2}&\dots&p^{(s+m-2)}(\alpha)\binom{s+m}{2}&b_2\\
\vdots&\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&0&\dots&p^{(s)}(\alpha)\binom{s+m}{m}&b_m
\end{vmatrix}}{p^{(s)}(\alpha)^{m+1}\frac{(s+1)^m(s+2)^{m-1}\dots(s+m)}{1^m2^{m-1}\dots m}}
\end{equation}$$

For the case \eqref{re} take the real part of the above expression, and for \eqref{im} take the imaginary part.

---

Now I know what you're thinking: "Oh dear god what is that hidious and disgusting thing"

### When would this monstrosity save time?

Here's the deal: This formula is only going to save you time if $$m$$ is small and $$n$$ is large. That is to say when the order of the equation is high and the highest power on the forcing function is low.

The reason for this is relatively straightforward: This formula relies on computing a determinant, and big determinants *suck* to evaluate. If $$m$$ is small, then the determinant is small. If $$m=1$$, it's just a $$3\times 3$$ matrix which can be evaluated relatively easily.

Take an example:

$$y^{(7)}-y^{(6)}+y^{(5)}-y^{(4)}-y'''+y''-y'+y=te^t$$

Undetermined coefficients would be the most efficient method for solving this, but would require you to:

1. Solve the homogeneous equation (which involves factoring a **7th** degree polynomial)
2. Differentiate a function of the form $$t^s(A+Bt)e^t$$ ***seven*** times
3. Plug in that mess of terms and simplify
4. Solve a system of equations

The system of equations would be in two variables which isn't that bad but I don't want to differentiate $$t^s(A+Bt)e^t$$ seven times and simplify that mess.

In contrast, to evaluate the formula you would simply

1. Evaluate $$p(1),p'(1),\ldots$$ in total $$s+m$$ times (for this specific problem, $$s=2$$ so you'd just need to go up to $$p'''(1)$$). Plus, this nets you $$s$$ homogeneous solutions for your trouble.
2. Evaluate $$\frac{(2+1)^1(2+2)^{1-1}}{1^12^{1-1}}$$
3. Evaluate 3 binomial coefficients (only one of which is not just $$1$$)
4. Evaluate a $$3\times 3$$ determinant (with a lot of zeros)

Note that if $$m=0$$, however, then this does just reduce down to [the Alpha Method](../alphamethod/){:target="_blank"}, which is far more straightforward and *does* always save time.

And finally, you can use this for forcing functions like $$(b_0+\ldots+b_mt^m)e^{at}\sin(bt)$$ and $$(b_0+\ldots+b_mt^m)e^{at}\cos(bt)$$. All you need to do is **use** $$\alpha=a+bi$$, and then **take the real part if it was originally cosine** and the **imaginary part if it was sin**.

### An example

Let us actually go through the process of applying this formula to

$$y^{(7)}-y^{(6)}+y^{(5)}-y^{(4)}-y'''+y''-y'+y=te^t$$

Here we identify $$\alpha=1$$ and $$m=1$$. We see that $$b_0=0$$ and $$b_1=1$$. Additionally,

$$p(x)=x^7-x^6+x^5-x^4-x^3+x^2-x+1$$

Our particular solution will then be, for some $$s$$ yet to be determined,

$$
y_ p=(-1)^1t^se^t
\frac
{\begin{vmatrix}
1&t&0\\
p^{(s)}(\alpha)\binom{s}{0}&p^{(s+1)}(\alpha)\binom{s+1}{0}&0\\
0&p^{(s)}(\alpha)\binom{s+1}{1}&1\\
\end{vmatrix}}
{p^{(s)}(\alpha)^{1+1}\frac{(s+1)^1(s+2)^{1-1}}{1^m2^{1-1}}}
$$

We can easily compute $$\frac{(s+1)^1(s+2)^{1-1}}{1^m2^{1-1}}=s+1$$, but most importantly we can already expand along the third column. This eliminates any need to compute binomial coefficients and reduces the determinant to be $$2\times 2$$. Then our particular soultion will be

$$
y_ p=-\frac{t^se^t}{(s+1)p^{(s)}(\alpha)^2}
\begin{vmatrix}
1&t\\
p^{(s)}(\alpha)&p^{(s+1)}(\alpha)\\
\end{vmatrix}
$$

A quick remark: The fastest way to evaluate polynomials is actually *Synthetic Division*. In fact, it would be the fastest way to evaluate multiple derivatives at the same point (by repeatedly doing synthetic division). I hope to someday make a post on that method in the future. (EDIT: [I did](../synthetictaylor/){:target="_blank"})

Regardless, one can calculate that $$p(1)=0$$. This actually tells us a homogeneous solution is $$y_1=e^t$$. So now if we go back to solving the homogeneous equation it's only a 6th degree polynomial.

Take the derivative:

$$p'(x)=7x^6-6x^5+5x^4-4x^3-3x^2+2x-1$$

We find that $$p'(1)=0$$ as well. Well at least we get another homogeneous solution $$y_2=te^t$$.

Another derivative:

$$p''(x)=42x^5-30x^4+20x^3-12x^2-6x+2$$

$$p''(1)=16$$ and at last we find our $$s=2$$, and by extension the most important part of our solution $$p^{(s)}(\alpha)=16$$. All that is missing is $$p^{(s+1)}(\alpha)$$, for which we need $$p'''(1)$$:

$$p'''(x)=210x^4-120x^3+60x^2-24x-6$$

And, finally, $$p'''(1)=120$$. We now have everything we need:

$$
y_ p=-\frac{t^2e^t}{(2+1)(16)^2}
\begin{vmatrix}
1&t\\
16&120\\
\end{vmatrix}
$$

$$
y_ p=\frac{t^2e^t(16t-120)}{768}
$$

$$
y_ p=\frac{e^t(2t^3-15t^2)}{96}
$$

And this is indeed the correct answer!

### What is this sorcery, magic man?

The mechanics behind this formula involve the technique of [Function Interpolation](../functioninterp/){:target="_blank"}, that I've previously written about, and the exponential shift identity's interaction with Taylor series.

The exponential shift identity is as follows

$$\begin{equation} \label{eshift}
p(D)(e^{\alpha t}f(t))=e^{\alpha t}p(D+\alpha)f(t)
\end{equation}$$

For intuition on why this works, observe that

$$D(e^{\alpha t}f(t))=e^{\alpha t}(f'(t)+\alpha f(t))=e^{\alpha t}(D+\alpha)f(t)$$

You can prove using induction that $$D^n(e^{\alpha t}f(t))=e^{\alpha t}(D+\alpha)^nf(t)$$. \eqref{eshift} then follows because differentiation is linear.

We know that our particular solution to \eqref{1} will be of the form

$$y_p=t^s(c_0+c_1t+\ldots+c_mt^m)e^{\alpha t}$$

where $$s$$ is the multiplicity of the root $$\alpha$$ in $$p(x)$$ so that we do not duplicate any homogeneous solutions (Note that this implies $$p^{(k)}(\alpha)=0$$ for $$0\leq k\leq s$$). Keep in mind that $$s$$ could be zero.

We will use the shorthand $$c(t)=c_0+c_1t+\ldots+c_mt^m$$ and $$b(t)=b_0+b_1t+\ldots+b_mt^m$$.

Our exponential shift formula (vaguely) tells us what will happen when we plug in our particular solution to the differential equation:

$$p(D)y_p=e^{\alpha t}p(D+\alpha)\left(c_0t^s+c_1t^{s+1}+\ldots+c_mt^{s+m}\right)$$

Note that normally I would write $$y_p$$ in sigma notation, but I found that it just makes things more complicated to do so.

Using Taylor Series, we can write $$p(x)$$ as

$$p(x)=\sum_{k=s}^n\frac{p^{(k)}(\alpha)(x-\alpha)^k}{k!}$$

Note: We begin at $$k=s$$ because we assume that $$p^{(k)}(\alpha)=0$$ for $$0\leq k\leq s$$.

Why would we do this? Well, because

$$p(x+\alpha)=\sum_{k=s}^n\frac{p^{(k)}(\alpha)x^k}{k!}$$

Therefore,

$$p(D+\alpha)=\sum_{k=s}^n\frac{p^{(k)}(\alpha)D^k}{k!}$$

Now we can simply deal with derivatives and values of $$p^{(k)}(\alpha)$$.

$$p(D+\alpha)t^sc(t)=\left(\frac{p^{(s)}(\alpha)D^s}{s!}+\ldots+\frac{p^{(n)}(\alpha)D^{n}}{n!}\right)(c_0t^s+c_1t^{s+1}+\ldots+c_mt^{s+m})$$

Now, since $$t^sc(t)$$ is of degree $$s+m$$, any power of $$D$$ greater than $$s+m$$ will disappear. Therefore, we can change $$\frac{p^{(s)}(\alpha)D^s}{s!}+\ldots+\frac{p^{(n)}(\alpha)D^{n}}{n!}$$ to

$$\frac{p^{(s)}(\alpha)D^s}{s!}+\ldots+\frac{p^{(s+m)}(\alpha)D^{s+m}}{(s+m)!}$$

Observe that this is still true if $$m>n$$, since this, in that case, is equivalent to just adding a bunch of zeros to the sum.

$$p(D+\alpha)t^sc(t)=\left(\frac{p^{(s)}(\alpha)}{s!}+\ldots+\frac{p^{(s+m)}(\alpha)D^{m}}{(s+m)!}\right)t^sc(t)$$

Now our goal is to have the output give us $$b_0+b_1t+\ldots+b_mt^m$$, so we should group up the terms of each power.

The constant term, we will have

$$b_0=\left(\frac{p^{(s)}(\alpha)D^s}{s!}\right)c_0t^s+\left(\frac{p^{(s+1)}(\alpha)D^{s+1}}{(s+1)!}\right)c_1t^{s+1}+\ldots+\left(\frac{p^{(s+m)}(\alpha)D^{s+m}}{(s+m)!}\right)c_mt^{s+m}$$

Consider that $$D^kt^j=\begin{cases}\frac{j!}{(j-k)!}t^{j-k},&k\leq j\\0,&k>j\end{cases}$$.

$$b_0=\frac{p^{(s)}(\alpha)}{s!}\frac{s!}{0!}c_0+\frac{p^{(s+1)}(\alpha)}{(s+1)!}\frac{(s+1)!}{0!}c_1+\ldots+\frac{p^{(s+m)}(\alpha)}{(s+m)!}\frac{(s+m)!}{0!}c_m$$

Now you may be wondering why I'm bothering to write the $$0!$$ and not cancelling the factorials. The reason is that we happen to have our good friends: the binomial coefficients!

\begin{equation}
\binom{n}{k}=\frac{n!}{k!(n-k)!}
\end{equation}

So we can write this instead as

$$b_0=p^{(s)}(\alpha)\binom{s}{0}c_0+p^{(s+1)}(\alpha)\binom{s+1}{0}c_1+\ldots+p^{(s+m)}(\alpha)\binom{s+m}{0}c_m$$

$$b_0=\sum_{j=0}^mp^{(s+j)}(\alpha)\binom{s+j}{0}c_j$$

And in general, to find $$b_k$$ ($$0\leq k\leq m$$),

$$b_k=\sum_{j=k}^{m}p^{(s+j)}(\alpha)\binom{s+j}{k}c_j$$

We start with higher and higher coefficients $$c_j$$ because when taking $$s$$ or more derivatives, only terms with power $$s+k$$ (corresponding to $$c_k$$) or higher will yield terms with power $$t^k$$.

So we may write the system of equations for our coefficients of $$c(t)$$ in matrix form as

$$\begin{equation}
\begin{bmatrix}
p^{(s)}(\alpha)\binom{s}{0}&p^{(s+1)}(\alpha)\binom{s+1}{0}&p^{(s+2)}(\alpha)\binom{s+2}{0}&\dots&p^{(s+m)}(\alpha)\binom{s+m}{0}\\
0&p^{(s)}(\alpha)\binom{s+1}{1}&p^{(s+1)}(\alpha)\binom{s+2}{1}&\dots&p^{(s+m-1)}(\alpha)\binom{s+m}{1}\\
0&0&p^{(s)}(\alpha)\binom{s+2}{2}&\dots&p^{(s+m-2)}(\alpha)\binom{s+m}{2}\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\dots&p^{(s)}(\alpha)\binom{s+m}{m}\\
\end{bmatrix}
\begin{bmatrix}
c_0\\c_1\\c_2\\\vdots\\c_m
\end{bmatrix}=
\begin{bmatrix}
b_0\\b_1\\b_2\\\vdots\\b_m
\end{bmatrix}
\end{equation}$$

So here is where the [determinant polynomial](../functioninterp/){:target="_blank"} comes in. We have a system of equations corresponding to the coefficients of a linear function (a polynomial). To save a lot of space, we will write the above equation as

$$\begin{equation}
F\vec{c}=\vec{b}
\end{equation}$$

We can write $$c(t)$$ using the determinant polynomial as

$$\begin{equation} \label{pform}
c(t)=(-1)^{m+1+1}\frac
{\begin{vmatrix}
1&\dots&t^m&0\\
&F&&\vec{b}
\end{vmatrix}}
{\det(F)}
\end{equation}$$

The good news is that the coefficient matrix is upper triangular, so its derivative is actually relatively simple. The determinant of the matrix is in fact

$$\det(F)=\prod_{k=0}^mp^{(s)}(\alpha)\binom{s+k}{k}$$

You can use the definition of the binomial coefficients to show that this is equal to

$$\begin{equation}
\det(F)=p^{(s)}(\alpha)^{m+1}\frac{(s+1)^m(s+2)^{m-1}\dots(s+m)}{1^m2^{m-1}\dots m}
\end{equation}$$

And... that's it. Substituting the results into \eqref{pform} yields \eqref{2}.
