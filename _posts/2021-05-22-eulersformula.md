---
layout: distill
title: Introduction to Euler's Formula
date: 2021-05-22 0
description: the best formula
comments: true
importance: 1
categories: calculus
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
---

Say you were a curious mathematician investigating what happens if you evaluate something like $$e^{ix}$$. How do you multiply something $$i$$ times? Well don't think of exponentiation as repeated multiplication, because it's not, really. Instead, think of exponentiation of $$e$$ as being *defined* by
$$\newcommand{\a}{\alpha  }$$
$$\newcommand{\b}{\beta  }$$
$$\newcommand{\Re}{\operatorname{Re}}$$
$$\newcommand{\Im}{\operatorname{Im}}$$
$$\newcommand{\conj}[1]{\overline{#1}}$$

\begin{equation} \label{exp}
e^x=\sum_{n=0}^\infty\frac{x^n}{n!}
\end{equation}

Now if you're groaning because you hate Taylor Series, don't worry we're just going to take it as fact that

\begin{equation} \label{trig}
\cos(x)=\sum_{n=0}^\infty\frac{(-1)^nx^{2n}}{(2n)!}\quad
\sin(x)=\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{(2n+1)!}
\end{equation}

And go ahead with evaluating $$e^{ix}$$. We can start by splitting up \eqref{exp} into even and odd terms. I mean, there are infinitely many, so there are infinitely many even and odd terms individually.

$$\begin{gather}
e^x=\sum_{n=0}^\infty\left(\frac{x^n}{n!}\right)\\
e^x=\sum_{n=0}^\infty\left(\frac{x^{2n}}{(2n)!}+\frac{x^{2n+1}}{(2n+1)!}\right)\\
e^x=\sum_{n=0}^\infty\frac{x^{2n}}{(2n)!}+\sum_{n=0}^\infty\frac{x^{2n+1}}{(2n+1)!}\\
\end{gather}$$

oh hey it's $$\cosh$$ and $$\sinh$$. anyway, plugging in $$ix$$

$$\begin{gather}
e^{ix}=\sum_{n=0}^\infty\frac{(ix)^{2n}}{(2n)!}+\sum_{n=0}^\infty\frac{(ix)^{2n+1}}{(2n+1)!}\\
e^{ix}=\sum_{n=0}^\infty\frac{i^{2n}x^{2n}}{(2n)!}+\sum_{n=0}^\infty\frac{i^{2n+1}x^{2n+1}}{(2n+1)!}\\
\end{gather}$$

Now we can just use the fact that that the definition of $$i=\sqrt{-1}$$ means we can say that $$i^2=-1$$. So then

$$\begin{gather}
i^{2n}=(i^{2})^{n}\\
i^{2n}=(-1)^{n}\\
\end{gather}$$

And since $$i^{2n+1}=i\cdot i^{2n}$$, we can say that $$i^{2n+1}=i(-1)^n$$.

$$\begin{gather}
e^{ix}=\sum_{n=0}^\infty\frac{(-1)^nx^{2n}}{(2n)!}+\sum_{n=0}^\infty\frac{i(-1)^nx^{2n+1}}{(2n+1)!}\\
e^{ix}=\sum_{n=0}^\infty\frac{(-1)^nx^{2n}}{(2n)!}+i\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{(2n+1)!}\\
\end{gather}$$

And well would you look at that. It's our old pals $$\cos(x)$$ and $$\sin(x)$$.

\begin{equation}
e^{ix}=\cos(x)+i\sin(x)
\end{equation}

Hopefully this is enough to explain Euler's formula for most people. But if you're like me, you may be wondering why $$\cos$$ and $$\sin$$ just *happen* to be here. And in my opinion, the best explanation is that one can **define** $$\cos(x)$$ and $$\sin(x)$$ as the real and imaginary parts of $$e^{ix}$$. The [prologue of the third edition of Walter Rudin’s Real and Complex Analysis](https://59clc.files.wordpress.com/2011/01/real-and-complex-analysis.pdf){:target="_blank"} does this and manages to *define* $$\pi$$ in terms of the exponential function. It may be difficult to follow, however. If you really want to understand it, the first [thing I ever wrote in LaTeX](https://www.overleaf.com/read/kfgvxfxmsxps){:target="_blank"} almost two years ago was attempting to make that derivation more intuitive. Note, though, that it was even more poorly written than the posts on this blog (yikes) and remains unfinished.

Rather than go into applications of this formula, I will save those for other posts. The main ones being [skipping integration by parts](../eulersformulabyparts/){:target="_blank"} for integrals involve the product of an exponential and a trig function, and easy ways to remember trig identities.

Alternate Derivation with Differential Equations
-

If you've taken differential equations, this might be interesting to consider.

There is another way one can arrive at Euler's formula by examining the differential equation

$$\begin{equation}\label{diffeq}
y''+y=0
\end{equation}$$

You can verify that $$\cos(t)$$ and $$\sin(t)$$ are solutions to this, because they do satisfy the condition that their second derivative is just $$-1$$ times the original function ($$y''=-y$$). There's also some differential equations mumbo-jumbo we can use to say that *every* solution to this differential equation is of the form

$$\begin{equation} \label{sol1}
y=c_1\cos(t)+c_2\sin(t)
\end{equation}$$

If you have taken DE, the specific logic is that their Wronskian is nonzero, making them linearly independent. Since it's second order, two linearly independent solutions are a sufficient basis for every solution.

However, the general method for solving these kinds of differential equations is to suppose the solution is of the form $$y=e^{rt}$$. Since this implies that $$y''=r^2e^{rt}$$ we get

$$r^2e^{rt}+e^{rt}=0$$

We know $$e^{rt}\neq0$$ so we can safely divide it out.

$$r^2+1=0$$

Well if you've taken calculus, you can probably see that the roots of this quadratic are $$r=\pm i$$. So our general solution would be

$$\begin{equation}\label{sol2}
y=k_1e^{it}+k_2e^{-it}
\end{equation}$$

And you can verify that plugging this into \eqref{diffeq} will indeed give you zero. That same logic of the nonzero Wronskian still applies, telling us that *every* solution can be written in the form \eqref{sol2}.

But this is a strange result. We have two different general solutions that look totally different but are apparently totally equivalent (existence and uniqueness theorem).

So that means we should be able to write a solution of one set in terms of the solutions in the other. In other words, for all values of $$t$$, there *is* a solution to the equation

$$\begin{equation}
e^{it}=c_1\cos(t)+c_2\sin(t)
\end{equation}$$

Since this is true for *all* $$t$$, let's plug in some nice ones. Such as $$t=0$$.

$$1=c_1$$

Oh, well that was easy. Let's take the derivative of both sides.

$$\begin{equation}
ie^{it}=-c_1\sin(t)+c_2\cos(t)
\end{equation}$$

Plug in $$t=0$$ again.

$$i=c_2$$

Well... there we go.

$$e^{it}=\cos(t)+i\sin(t)$$

You can do this same process to get $$e^{-it}$$ in terms of $$\cos(t)$$ and $$\sin(t)$$, and also both $$\cos(t)$$ and $$\sin(t)$$ in terms of $$e^{it}$$ and $$e^{-it}$$!
