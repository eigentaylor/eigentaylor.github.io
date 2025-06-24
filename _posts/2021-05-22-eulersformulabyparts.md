---
layout: page
title: Skipping Integration by Parts Using Euler's Formula
date: 2021-05-22 0
description: skip or simplify integrals involving trig functions multiplied by exponentials
comments: true
importance: 2
categories: calculus
---

So here I want to use Euler's formula to skip the need to do the annoying recursive Integration by Parts for the following types of integrals
$$\newcommand{\a}{\alpha  }$$
$$\newcommand{\b}{\beta  }$$
$$\newcommand{\Re}{\operatorname{Re}}$$
$$\newcommand{\Im}{\operatorname{Im}}$$
$$\newcommand{\conj}[1]{\overline{#1}}$$

$$\begin{equation}
\int e^{at}\cos(bt)\,dt\quad\int e^{at}\sin(bt)\,dt
\end{equation}$$

This can also be used more generally to simplify the integration by parts for integrals like

$$\begin{equation}
\int f(t)e^{at}\cos(bt)\,dt\quad\int f(t)e^{at}\sin(bt)\,dt
\end{equation}$$

Imagine doing integration by parts for

$$\int t^2e^{3t}\cos(4t)\,dt$$

It would be horrible. But what about integrating something like $$\int t^2e^{ct}\,dt$$? That's a **lot** more reasonable. Well... if we let $$c=3+4i$$ then that will actually solve the other integral!

Now you may be thinking: "What is this sorcery, magic man?" And I'll tell you exactly what it is.

**Euler's Formula**
=

If you don't know what it is, this is an [explanation](../eulersformula/){:target="_blank"} of it. But the formula is

$$\begin{equation}
e^{ix}=\cos(x)+i\sin(x)
\end{equation}$$

Skipping Integration by Parts
-

With this method, it's possible to do the integrals

$$\begin{equation}
\int e^{at}\cos(bt)\,dt\quad\int e^{at}\sin(bt)\,dt
\end{equation}$$

*in your head* without memorizing any formulas. The first step is to realize that $$e^{at}\cos(bt)$$ and $$e^{at}\sin(bt)$$ are simply the two parts of one simple complex exponential, $$e^{(a+bi)t}$$.

$$\begin{equation}
e^{(a+bi)t}=e^{at}\cos(bt)+ie^{at}\sin(bt)
\end{equation}$$

Integrating the left side is incredibly easy, and if we can do the left side, we can do the right side too.

$$\begin{align*}
\int e^{(a+bi)t}\,dt&=\int\left[ e^{at}\cos(bt)+ie^{at}\sin(bt))\right]\,dt \\
\int e^{(a+bi)t}\,dt&=\int e^{at}\cos(bt)\,dt+\int ie^{at}\sin(bt))\,dt \\
\int e^{(a+bi)t}\,dt&=\int e^{at}\cos(bt)\,dt+i\int e^{at}\sin(bt))\,dt \\
\end{align*}$$

So

$$\begin{align}
\int e^{at}\cos(bt)\,dt&=\Re\left(\int e^{(a+bi)t}\,dt\right)\\
\int e^{at}\sin(bt)\,dt&=\Im\left(\int e^{(a+bi)t}\,dt\right)
\end{align}$$

Luckily, for these integrals, it's easy to split the real and imaginary parts.

$$\begin{align*}
\int e^{(a+bi)t}\,dt&=\frac{e^{(a+bi)t}}{a+bi}\\
\int e^{(a+bi)t}\,dt&=\frac{e^{at}e^{bit}(a-bi)}{a^2+b^2}\\
\int e^{(a+bi)t}\,dt&=\frac{e^{at}(\cos(bt)+i\sin(bt))(a-bi)}{a^2+b^2}\\
\int e^{(a+bi)t}\,dt&=\frac{e^{at}\left(a\cos(bt)+b\sin(bt)\right)}{a^2+b^2}+i\frac{e^{at}\left(a\sin(bt)-b\cos(bt)\right)}{a^2+b^2}\\
\end{align*}$$

And that's it!

$$\begin{align}
\int e^{at}\cos(bt)\,dt&=\frac{e^{at}\left(a\cos(bt)+b\sin(bt)\right)}{a^2+b^2}+C\\
\int e^{at}\sin(bt)\,dt&=\frac{e^{at}\left(a\sin(bt)-b\cos(bt)\right)}{a^2+b^2}+C\\
\end{align}$$

And while it may look like a mess at first, it's actually relatively easy to remember once you know where each part comes from.

First, both are multiplied by a common $$e^{at}$$, which we would expect to stick around after integration, and the squared magnitude of the complex exponent $$a^2+b^2$$, which always shows up when dividing by a complex number.

But how would one remember the numerator terms? Well, when multiplying two complex numbers, the real part is always contains the product of the real parts and the product of the imaginary parts. Here the real parts were $$\cos(bt)$$ and $$a$$, and the imaginary parts $$\sin(bt)$$ and $$b$$. Normally, we subtract the product of the imaginary parts, but because we were *dividing* by $$a+bi$$, we're multiplying by the conjugate $$a-bi$$, so we don't need to subtract anything in evaluating the real part.

Similarly, the imaginary part of a product of complex numbers is the sum of the real and imaginary parts cross multiplied. Since, again, we're actually multiplying by the conjugate, we subtract that term with the imaginary part $$b$$.

If my rambling made no sense, then no worries. You may always just go through the process yourself at your own pace, and eventually you'll notice the patterns that I take advantage of.

Let's do an example. Suppose we want to evaluate either of

$$\int e^{3t}\cos(4t)\,dt\quad\int e^{3t}\sin(4t)\,dt$$

Then to get either/both, we just need to integrate

$$\int e^{(3+4i)t}\,dt$$

This is easy enough.

$$\int e^{(3+4i)t}\,dt=\frac{e^{(3+4i)t}}{3+4i}$$

Now we know what's going to happen. We're going to get a $$\frac{e^{3t}}{25}$$ multiplying everything because the real part is $$3$$ and the magnitude squared of the exponent $$| 
3+4i
|^2=25$$. 

Now to get the $$\cos$$ integral, we need the real part of the product. So we'll have $$\cos(4t)$$ times the real part of the complex exponent $$3$$ plus, since we're multiplying by the conjugate, $$\sin(4t)$$ times the imaginary part $$4$$.

$$\int e^{3t}\cos(4t)\,dt=\frac{e^{3t}(3\cos(4t)+4\sin(4t))}{25}$$

For the $$\sin$$ integral, we'll get $$\cos(4t)$$ times the negative of the imaginary part $$-4$$ plus $$\sin(4t)$$ times the real part $$3$$.

$$\int e^{3t}\sin(4t)\,dt=\frac{e^{3t}(-4\cos(4t)+3\sin(4t))}{25}$$

If you want to see the full work, however, here it is.

$$\begin{align*}
\int e^{(3+4i)t}\,dt&=\frac{e^{(3+4i)t}}{3+4i}\\
\int e^{(3+4i)t}\,dt&=\frac{e^{3t}e^{4it}(3-4i)}{3^2+4^2}\\
\int e^{(3+4i)t}\,dt&=\frac{e^{3t}(\cos(4t)+i\sin(4t))(3-4i)}{25}\\
\int e^{(3+4i)t}\,dt&=\frac{e^{3t}\left(3\cos(4t)+4\sin(4t)\right)}{25}+i\frac{e^{3t}\left(3\sin(4t)-4\cos(4t)\right)}{25}\\
\end{align*}$$

$$\begin{align*}
\int e^{3t}\cos(4t)\,dt&=\frac{e^{3t}(3\cos(4t)+4\sin(4t))}{25}\\
\int e^{3t}\sin(4t)\,dt&=\frac{e^{3t}(3\sin(4t)-4\cos(4t))}{25}\\
\end{align*}$$

Less Terrible Integration by Parts
-

Now, consider the integral

$$\int f(t)e^{(a+bi)t}\,dt$$

where $$f(t)$$ is a *real* function.

We're just going to do the same thing as we did above.

$$\begin{align*}
\int f(t)e^{(a+bi)t}\,dt&=\int f(t)e^{at}e^{i(bt)}\,dt \\
\int f(t)e^{(a+bi)t}\,dt&=\int f(t)e^{at}(\cos(bt)+i\sin(bt))\,dt \\
\int f(t)e^{(a+bi)t}\,dt&=\int\left[ f(t)e^{at}\cos(bt)+if(t)e^{at}\sin(bt))\right]\,dt \\
\int f(t)e^{(a+bi)t}\,dt&=\int f(t)e^{at}\cos(bt)\,dt+\int if(t)e^{at}\sin(bt))\,dt \\
\end{align*}$$

Giving us

$$\begin{equation}
\int f(t)e^{(a+bi)t}\,dt=\int f(t)e^{at}\cos(bt)\,dt+i\int f(t)e^{at}\sin(bt)\,dt
\end{equation}$$

We can then say, once again,

$$\begin{align}
\int f(t)e^{at}\cos(bt)\,dt&=\Re\left(\int f(t)e^{(a+bi)t}\,dt\right)\\
\int f(t)e^{at}\sin(bt)\,dt&=\Im\left(\int f(t)e^{(a+bi)t}\,dt\right)
\end{align}$$

And now we can solve a *much* easier integral and get answer by covering up about half of the result. *Not to mention* that it solves it for both $$\sin$$ *and* $$\cos$$. So going back to the example above, by solving

$$I=\int t^2e^{(3+4i)t}\,dt$$

we will get both the answer to $$\int t^2e^{3t}\cos(4t)\,dt$$ and $$\int t^2e^{3t}\sin(4t)\,dt$$.

This is an easy enough integral to solve by the tabular method.

$$\begin{array}{c|cc}
&\frac{d}{dt}&\int\\
\hline
+&t^2&e^{(3+4i)t}\\
-&2t&\frac{e^{(3+4i)t}}{3+4i}\\
+&2&\frac{e^{(3+4i)t}}{(3+4i)^2}\\
-&0&\frac{e^{(3+4i)t}}{(3+4i)^3}
\end{array}$$

$$I=t^2\frac{e^{(3+4i)t}}{3+4i}-2t\frac{e^{(3+4i)t}}{(3+4i)^2}+2\frac{e^{(3+4i)t}}{(3+4i)^3}$$

$$I=e^{(3+4i)t}\frac{(3+4i)^2t^2-2(3+4i)t+2}{(3+4i)^3}$$

The difficult part is the complex arithmetic to isolate the real and imaginary parts of this expression. Doing that, however, requires no calculus. The arithmetic can also be done on most calculators.

$$\begin{gather*}
\int t^2e^{(3+4i)t}\,dt=e^{(3+4i)t}\frac{(3+4i)^2t^2-2(3+4i)t+2}{(3+4i)^3}\\
I=e^{3t}e^{4it}\frac{(-7+24i)t^2-2(3+4i)t+2}{-117+44i}\\
I=e^{3t}(\cos(4t)+i\sin(4t))\frac{(1875-2500i)t^2+(350+1200i)t-(234+88i)}{(-117)^2+(44)^2}\\
I=\frac{e^{3t}\cos(4t)}{15625}\left((1875-2500i)t^2+(350+1200i)t-(234+88i)\right)\\
+\frac{e^{3t}\sin(4t)}{15625}\left((2500+1875i)t^2+(-1200+350i)t+(88-234i)\right)\\
I=\frac{e^{3t}}{15625}\left((1875t^2+350t-234)\cos(4t)+(2500t^2-1200t+88)\sin(4t) \right)\\
+i\frac{e^{3t}}{15625}\left((-2500t^2+1200t-88)\cos(4t)+(1875t^2+350t-234)\sin(4t) \right)+C
\end{gather*}$$

So we obtain that (neglecting the $$+C$$ to conserve space)

$$\begin{align}
\int t^2e^{3t}\cos(4t)\,dt&=\frac{e^{3t}}{15625}\left((1875t^2+350t-234)\cos(4t)+(2500t^2-1200t+88)\sin(4t) \right)\\
\int t^2e^{3t}\sin(4t)\,dt&=\frac{e^{3t}}{15625}\left((-2500t^2+1200t-88)\cos(4t)+(1875t^2+350t-234)\sin(4t) \right)
\end{align}$$

The arithmetic was a bit laborious, but not nearly as bad as doing the multiple looping integration by parts for both integrals, in my view.

If we were looking specifically for $$\int t^2e^{3t}\cos(4t)\,dt$$, we could have taken a shortcut through the last two steps by only taking the real parts obtained when multiplying through by $$\cos(4t)+i\sin(4t)$$. That is to say, by defining $$p(t)=(2500+1875i)t^2+(-1200+350i)t+(88-234i)$$,

$$\int t^2e^{3t}\cos(4t)\,dt=\frac{e^{3t}}{15625}\left(\Re(p(t))\cos(4t)-\Im(p(t))\sin(4t) \right)$$

If you are unsure how I got this, recall that that when multiplying two complex numbers, the real part is going to be the product of the real parts minus the product of the imaginary parts, since the $$i^2$$ will negate the term. The products of the real and imaginary parts of each one will not be real, because there won't be a second $$i$$ term to cancel out the one from the imaginary part of origin. This extends to the product of complex functions too, as we used above.

So using that we could have also skipped to get $$\int t^2e^{3t}\sin(4t)\,dt$$ through

$$\int t^2e^{3t}\sin(4t)\,dt=\frac{e^{3t}}{15625}\left(\Im(p(t))\cos(4t)+\Re(p(t))\sin(4t) \right)$$

Only taking half the terms is *usually* what you'll be doing when using this method, since it usually comes from wanting the answer to just one part, not both.

Additionally, there's no need to memorize the formulas like $$\Re(p(t))\cos(4t)-\Im(p(t))\sin(4t)$$, just remember which part you want and multiply based on which terms will be in it.
