---
layout: distill
title: The Alpha Method (Generalized Exponential Response Formula)
date: 2021-01-04 
description: Easy particular solutions to nonhomoegenous constant coefficient linear differential equations with simple exponential/trigonometric forcing functions.
comments: true
importance: 1
categories: differential-equations
tags: best
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Basic Overview The Alpha Method
  - name: The problem
  - name: Real alpha
    subsections:
      - name: Alpha is not a root
      - name: Example 1
      - name: Alpha is a root
      - name: Alpha is a repeated root
      - name: Example 2
  - name: Complex alpha
    subsections:
      - name: Example 3
---

**Updated 11/14/23**

# Basic Overview: The Alpha Method

The results of the Alpha Method are so simple, I feel it's necessary I give them outright before the derivation.

If $$p(\alpha )\neq0$$, then

$$\begin{equation} \label{problem}
    p(D)y=Be^{\alpha t}
\end{equation}$$

has the particular solution

$$\begin{equation}
    y_p=\frac{Be^{\alpha t} }{p(\alpha )}
\end{equation}$$

Otherwise, there exists a positive integer $$m$$ such that \eqref{problem} has the particular solution

$$\begin{equation}
    y_p=\frac{Bt^me^{\alpha t} }{p^{(m)}(\alpha )}
\end{equation}$$

Additionally, a particular solution to

$$\begin{equation}
    p(D)y=Be^{\alpha t} \cos(\beta  t)+Ce^{\alpha t} \sin(\beta  t)
\end{equation}$$

Is given by

$$\begin{equation}
    y_p=B\operatorname{Re}(z_p)+C\operatorname{Im}(z_p)
\end{equation}$$

where $$z_p$$ is obtained by using the alpha method on

$$\begin{equation}
    p(D)z=e^{(\alpha+i\beta)t}
\end{equation}$$

Or, alternatively, if $$p^{(m)}(\alpha )=re^{i\theta}$$, then the particular solution will be

\begin{equation}
        y_p=\frac{t^me^{\alpha t}}{r}\left(B\cos(\beta t-\theta)+C\sin(\beta t-\theta)\right)
\end{equation}

For a more formal and thorough examination of this problem and method, take a look at [this](https://www.overleaf.com/read/xtxskmmnjphy){:target="_blank"}.

If you're just here for the formulas and you don't care about the derivation or seeing examples, then this is all you need. The rest of this post is derivations and examples.

# The problem
Here we look for particular solutions differential equations such as

$$\begin{align*}
    &y''+y=10e^{2t} & y''+4y'+4y=e^{-3t}\\
    &y'''-5y'+6y=e^{3t} & y^{(9)}-2y'+y=e^t&\\
    &y''+4y'+3y=\sin(3t) & y''+2y'+26y=e^{-3t}\cos(2t)\\
    &y^{(4)}+4y=\cos(2t) & y''+2y'+2y=e^{-t}\sin(t)
\end{align*}$$

However, these all really have the same form, \eqref{problem}.

Where $$D$$ is the differential operator such that

$$\begin{equation}
    Dy=y'
\end{equation}$$

and $$p(x)$$ is the characteristic polynomial.

Take the example, $$y''-5y'+6y$$, which has a characteristic polynomial $$p(x)=x^2-5x+6$$. We could rewrite this with the $$D$$ operator as

$$\begin{equation*}
    D^2y-5Dy+6y
\end{equation*}$$

We can factor out a $$y$$ from the right (not the left because the $$D$$ is not commutative),
and indeed that is still the characteristic polynomial with $$D$$ instead of $$x$$.

$$\begin{equation*}
    (D^2-5D+6)y=p(D)y
\end{equation*}$$

Not all of these equations look like they have an exponential on the other side, though. Using Euler's Identity, they might as well be. To take two examples of the cases where it's not so obvious,

$$\begin{gather*}
    \sin(3t)=\operatorname{Im}(e^{3it})\\
    e^{-3t}\cos(2t)=\operatorname{Re}(e^{(-3+2i)t})
\end{gather*}$$

# Real alpha 

## Alpha is not a root
$$p(\alpha)\neq0$$

So let's examine the general problem

$$\begin{equation}
    ay''+by'+cy=Be^{\alpha t}
\end{equation}$$

First, notice the characteristic polynomial is $$p(x)=ax^2+bx+c$$. Now if we had to guess the form of the solution, a good guess would be some constant times $$e^{\alpha t} $$ since adding that with its derivatives would give us some scalar multiple of $$e^{\alpha t} $$.

$$\begin{gather*}
    y_p=Ae^{\alpha t} \\
    y_p'=A(\alpha )e^{\alpha t} \\
    y_p''=A(\alpha ^2)e^{\alpha t}
\end{gather*}$$

When we plug into the differential equation,
$$\begin{gather*}
    aA(\alpha ^2)e^{\alpha t} +bA(\alpha )e^{\alpha t} +cAe^{\alpha t} =Be^{\alpha t} \\
    A(a\alpha ^2+b\alpha +c)e^{\alpha t} =Be^{\alpha t} \\
\end{gather*}$$

$$\begin{equation} \label{Ap(a)=B}
    Ap(\alpha )e^{\alpha t} =Be^{\alpha t}
\end{equation}$$

Therefore, as long as $$p(\alpha )\neq 0$$, a particular solution is

$$\begin{equation*}
    A=\frac{B}{p(\alpha )}
\end{equation*}$$

So we get as a result, if $$p(\alpha )\neq 0$$, then \eqref{problem} has the particular solution

$$\begin{equation} \label{alpha0}
    y_p=\frac{Be^{\alpha t} }{p(\alpha )}
\end{equation}$$

This is not restricted to second-order equations, by the way. I recommend trying to prove that it works for $$n$$-th order equations as well.

### Example 1

$$\begin{equation*}
    y''+y=10e^{-2t}
\end{equation*}$$

Here $$\alpha =-2$$, $$B=10$$, and $$p(x)=x^2+1$$. So $$p(\alpha )=5$$ and $$\frac{B}{p(\alpha )}=2$$. Therefore,

$$\begin{equation*}
    y_p=2e^{-2t}
\end{equation*}$$

And it can be verified that this is indeed a solution :sunglasses:

However, if $$p(\alpha )=0$$ then we're in a bit of a pickle, because \eqref{Ap(a)=B} is only true if $$B=0$$. So our solution cannot be of the form $$y_p=Ae^{\alpha t} $$. In other words, $$Ae^{\alpha t} $$ is in the kernel of $$p(D)$$.

## Alpha is a root
$$p(\alpha )=0, \; p'(\alpha )\neq 0$$

When you run into trouble with linear differential equations, sometimes the solution is multiplying by the independent variable. And indeed, this is *nearly* the solution.

Let's go back to

$$\begin{equation*}
    ay''+by'+cy=Be^{\alpha t}
\end{equation*}$$

But this time, we suppose $$p(\alpha )=0$$. Now if you plug in $$y_p=Ae^{\alpha t} $$ you'll get zero. If we suppose $$y_p=Ate^{\alpha t} $$, then we get

$$\begin{gather*}
    y_p=Ate^{\alpha t} \\
    y_p'=A(\alpha  t+1)e^{\alpha t} \\
    y_p''=A(\alpha ^2t+2\alpha )e^{\alpha t}
\end{gather*}$$

Substituting in,

$$\begin{gather*}
    aA(\alpha ^2t+2\alpha )e^{\alpha t} +bA(\alpha  t+1)e^{\alpha t} +cAte^{\alpha t} =Be^{\alpha t} \\
    Ae^{\alpha t} ((a\alpha ^2+b\alpha +c)t+(2a\alpha +b))=Be^{\alpha t} \\
    Ae^{\alpha t} (p(\alpha )t+p'(\alpha ))=Be^{\alpha t} 
\end{gather*}$$

How curious... This is no coincidence. It has everything to do with (one of the) exponential shift theorems and how that interacts with Taylor series. The linked writeup at the top of this page goes more in depth on exactly how that works.

Since we assumed that $$p(\alpha )=0$$, we're left with

$$\begin{equation}
    Ae^{\alpha t} p'(\alpha )=Be^{\alpha t}
\end{equation}$$

Then as long as $$p'(\alpha )\neq0$$,

$$\begin{equation}
    A=\frac{B}{p'(\alpha )}
\end{equation}$$

and

$$\begin{equation} \label{Bt/pprime}
    y_p=\frac{Bte^{\alpha t} }{p'(\alpha )}
\end{equation}$$

Once again, this is not limited to second-order equations. In general,

If $$p(\alpha )=0$$ but $$p'(\alpha )\neq 0$$, then \eqref{problem} has the particular solution \eqref{Bt/pprime}.

## Alpha is a repeated root
$$p(\alpha )=p'(\alpha )=\ldots=p^{(m-1)}(\alpha )=0,\;\; p^{(m)}(\alpha )\neq 0$$

You may notice a pattern when comparing $$\frac{Bte^{\alpha t} }{p'(\alpha )}$$ and $$\frac{Be^{\alpha t} }{p(\alpha )}$$. You may be hoping that if $$p(\alpha )=p'(\alpha )=0$$ but $$p''(\alpha )\neq 0$$ then

$$\begin{equation}
    y_p=\frac{Bt^2e^{\alpha t} }{p''(\alpha )}
\end{equation}$$

Well I have good news: It's absolutely true :smirk:

If $$p^{(k)}(\alpha )$$ keeps equaling zero, you simply have to multiply by $$t$$ and divide by the next derivative instead until it works.

**Pro-tip**: The fastest way to evaluate multiple derivatives at the same point is by synthetic division. Do synthetic division on $$p(x)$$ at $$\alpha$$ until the remainder is nonzero. Multiply the first nonzero remainder by how many zero remainders there were.

Let's take an example:

### Example 2

Find the general solution for

$$\begin{equation*}
    y^{(4)}+4y'''+6y''+4y'+y=72e^{-t}
\end{equation*}$$

Now they teach you in school to find the homogeneous solution first, and then get the particular solution. But this is why the Alpha Method is so ballin'. By starting with the particular solution, the alpha method sometimes does the rest of the problem for you.

This particular equation is not very difficult. The homogeneous solution can be obtained by inspection if you're familiar with Pascal's Triangle. But let's pretend we aren't.

Now I'm going to go ahead and bust out the Alpha Method \eqref{alpha0} by calculating

$$\begin{equation*}
    y_p=^?\frac{72e^{-t}}{p(-1)}
\end{equation*}$$

But when I calculate $$p(-1)$$ I 'mysteriously' get zero... Then that tells me that $$-1$$ is a root of the characteristic polynomial :eyes: So one of my homogeneous solutions is $$y_1=e^{-t}$$. So we didn't completely waste our time.

Alright, so let's go with the derivative and multiply by $$t$$.

$$\begin{equation*}
    y_p=^?\frac{72te^{-t}}{p'(-1)}
\end{equation*}$$

But oh no $$p'(-1)=0$$ too :weary:

Alas, not all is lost. We at least get a second homogeneous solution $$y_2=te^{-t}$$.

Let's cut to the chase. If we continue trying to use the Alpha Method,

$$\begin{gather*}
    p''(-1)=0&\implies &y_3=t^2e^{-t}\\
    p'''(-1)=0&\implies &y_4=t^3e^{-t}
\end{gather*}$$

And hey wait a minute, we now have four homogeneous solutions to a fourth-order differential equation. That means we have our entire homogeneous solution. :eyes:

$$\begin{equation*}
    y_h=c_1e^{-t}+c_2te^{-t}+c_3t^2e^{-t}+c_4t^3e^{-t}
\end{equation*}$$

Now lucky for us (though not at all unexpected) $$p^{(4)}(-1)\neq 0$$. Specifically, $$p^{(4)}(-1)=24$$. That means our solution will be of the form

$$\begin{equation*}
    y_p=\frac{72t^4e^{-t}}{p^{(4)}(-1)}
\end{equation*}$$

$$\begin{equation*}
    y_p=\frac{72t^4e^{-t}}{24}
\end{equation*}$$

$$\begin{equation*}
    y_p=3t^4e^{-t}
\end{equation*}$$

If you were doing synthetic division to evaluate $$p^{(k)}(-1)$$, you may notice that your final remainder is $$1$$, which is not $$24$$. However, there were $$4$$ zero remainders, so we multiply our result, $$1$$, by $$4!$$. And, indeed, $$1\cdot4!=24$$.

Therefore, our general solution is

$$\begin{equation*}
    y_g=3t^4e^{-t}+(c_1+c_2t+c_3t^2+c_4t^3)e^{-t}
\end{equation*}$$

# Complex alpha

In my opinion, this is the other area where the Alpha Method shines. Finding particular solutions to problems like this

$$\begin{equation} \label{complex example}
    y^{(4)}+2y'''+3y''+2y'+2y=e^{-t}(6\cos(t)+2\sin(t))
\end{equation}$$

using conventional methods is just atrocious. However, with the Alpha Method, a particular solution is just a bit of algebra.

When dealing with a problem where the forcing function is a $$\sin$$ or $$\cos$$, it can ironically make things simpler to 'complexify' the problem. That is to turn problems like

$$\begin{equation}
    p(D)y=Be^{\alpha t} \cos(\beta  t)+Ce^{\alpha t} \sin(\beta t)
\end{equation}$$

into this

$$\begin{equation} \label{complex problem}
    p(D)y=B\operatorname{Re}(e^{(\alpha +i\beta ) t})+C\operatorname{Im}(e^{(\alpha +i\beta ) t})
\end{equation}$$

using Euler's formula.

Okay maybe that doesn't look much easier, but I promise it is. This way you're just doing the regular Alpha Method as we did before. You just have to do some extra complex arithmetic in addition. But I promise it's better than undetermined coefficients almost all of the time.

This is the general idea:

Say you have something like this,

$$\begin{equation} \label{complex case}
    p(D)y=Be^{\alpha t} \cos(\beta  t)+Ce^{\alpha t} \sin(\beta  t)
\end{equation}$$

Instead of solving that problem, we solve this one:

$$\begin{equation}
    p(D)z=e^{(\alpha +i\beta ) t}
\end{equation}$$

using the Alpha Method. Nothing is different here, the solution is either

$$\begin{equation}
    z_p=\frac{e^{(\alpha +i\beta ) t}}{p(\alpha +\beta  i)}
\end{equation}$$

or there exists some positive integer $$m$$ such that

$$\begin{equation}
    z_p=\frac{t^me^{(\alpha +i\beta ) t}}{p^{(m)}(\alpha +\beta  i)}
\end{equation}$$

Now the solution to \eqref{complex case} will be

$$\begin{equation*}
    y_p=B\operatorname{Re}(z_p)+C\operatorname{Im}(z_p)
\end{equation*}$$

But we can actually simplify this further. If we suppose that $$p(\alpha +\beta  i)=re^{i\theta}$$, then we get

$$z_p=\frac{t^me^{(\alpha +i\beta ) t}}{re^{i\theta}}=\frac{t^me^{\alpha t}}{r}e^{i(\beta t-\theta)}$$

So the real and imaginary parts are much more explicit:

$$z_p=\frac{t^me^{\alpha t}}{r}\left(\cos(\beta t-\theta)+i\sin(\beta t-\theta)\right)$$

giving us

$$\begin{equation}
    y_p=\frac{t^me^{\alpha t}}{r}\left(B\cos(\beta t-\theta)+C\sin(\beta t-\theta)\right)
\end{equation}$$

And... that's it. Now we can solve \eqref{complex example}.

### Example 3

First, we turn

$$\begin{equation*}
    y^{(4)}+2y'''+3y''+2y'+2y=e^{-t}(6\cos(t)+2\sin(t))
\end{equation*}$$

into

$$\begin{equation*}
z^{(4)}+2z'''+3z''+2z'+2z=e^{(-1+i) t}
\end{equation*}$$

Now we compute $$p(-1+i)$$ which happens to be... zero. Rats. Well at least we know two homogeneous solutions now to our original differential equation $$y_1=e^{-t}\cos(t)$$ and $$y_2=e^{-t}\sin(t)$$.

$$p'(-1+i)=4+2i$$ however, so we're back in business.

$$\begin{equation*}
    z_p=\frac{te^{(-1+i)t}}{4+2i}
\end{equation*}$$

Now we can write $$4+2i$$ in its polar form: $$4+2i=\sqrt{4^2+2^2}e^{i\tan^{-1}\left(\frac{2}{4}\right)}=2\sqrt{5}e^{i\tan^{-1}\left(0.5\right)}$$ and get

$$\begin{equation*}
    z_p=\frac{te^{-t}}{2\sqrt 5}\left(6\cos\left(t-\theta\right)+2\sin\left(t-\theta\right)\right)
\end{equation*}$$

where $$\theta=\tan^{-1}\left(0.5\right)$$. However, while easy to write, and great for a computer plotter, this answer is hard to verify by hand! You could use the angle sum formula to combine it, or expand it further. But the alternative way to get a more explicit answer is the following:

We multiply the numerator and denominator by the conjugate.

$$\begin{equation*}
    z_p=\frac{te^{(-1+i)t}}{4+2i}=
\frac{te^{(-1+i)t}(4-2i)}{4^2+2^2}
\end{equation*}$$

$$\begin{equation*}
    z_p=
\frac{te^{(-1+i)t}(2-i)}{10}
\end{equation*}$$

While it may not look like it, this numerator has a product of binomials. Because $$e^{it}=\cos(t)+i\sin(t)$$, we have

$$\begin{equation*}
    (\cos(t)+i\sin(t))(2-i)=(2\cos(t)+\sin(t))+i(2\sin(t)-\cos(t))
\end{equation*}$$

$$\begin{equation*}
    z_p=\frac{1}{10}te^{-t}(2\cos(t)+\sin(t))+i\frac{1}{10}te^{-t}(2\sin(t)-\cos(t))
\end{equation*}$$

Now because we have $$6$$ on the $$\cos$$ and $$2$$ on the $$\sin$$ term, \eqref{complex problem} asks us for  

$$\begin{equation*}
    y_p=6\operatorname{Re}(z_p)+2\operatorname{Im}(z_p)
\end{equation*}$$

$$\begin{equation*}
    y_p=te^{-t}(\cos(t)+\sin(t))
\end{equation*}$$

And that's it. Once you get experienced with this method, the steps go very quickly (especially if you use [synthetic division](../synthetictaylor){:target="_blank"} :eyes:). Yeah, I agree this is the best method.
