---
layout: distill
title: Series Solutions Done Quick
date: 2022-06-06
description: the fast way to do series solutions. no reindexing required.
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
  - name: Important Series
  - name: Euler Equations (Intro)
  - name: Example (Legendre equation)
  - name: The Straggler Coefficients
    subsections:
      - name: The direct way to calculate coefficients
  - name: When the IVP is not centered at 0
  - name: More Examples


---

# Important Series

$$
\begin{align}
y&=\sum_{n=0}^\infty a_nx^n\\
y'&=\sum_{n=0}^\infty (n+1)a_{n+1}x^{n}&=&\sum_{n=0}^\infty na_{n}x^{n-1}\\
y''&=\sum_{n=0}^\infty (n+1)(n+2)a_{n+2}x^{n}&=&\sum_{n=0}^\infty n(n-1)a_{n}x^{n-2}\\
\end{align}
$$

Note: For the series with $$x^{n-1}$$ or $$x^{n-2}$$, you may have to have the starting index be $$n=1$$ or $$n=2$$ respectively. However, we can technically start at zero generally, because when $$n=0$$, we get that $$na_{n}x^{n-1}=0$$ too. Try not to worry too much about it, as it really speeds things along when you start them all on $$n=0$$.

---

Here I will present the fast way to do series solutions. Essentially, we rearrange the differential equation such that reindexing is unnecessary. To explain how that works, let's start by looking at Euler Equations.

# Euler Equations (Intro)

An Euler equation is of the form

$$\begin{equation}
p_2x^2y''+p_1xy'+p_0y=0
\end{equation}$$

Where $$p_0,p_1,p_2$$ are constants.

The solutions to these equations are generally of polynomial form (similar to how solutions to constant coefficient linear ODEs are of exponential form), as we multiply by the independent variable with every differentiation, canceling the decreasing power which occurs when differentiating polynomials. We can use this fact to skip reindexing the series!

Suppose we plug in our series solution to this differential equation. Because we have $$xy'$$, we want to use $$y'=\sum_{n=0}^\infty na_{n}x^{n-1}$$, and because we have $$x^2y''$$, we want to use $$y''=\sum_{n=0}^\infty n(n-1)a_{n}x^{n-2}$$, since that will give us $$x^n$$ on all the terms. Notice how all three terms will also have $$a_n$$! Thus, when we combine it all, we get

$$\begin{equation}
\sum_{n=0}^\infty(p_2n(n-1)+p_1n+p_0)a_nx^n=0
\end{equation}$$

Notice how the term multiplying $$a_nx^n$$ is *almost* the characteristic polynomial if it was constant coefficients. This is actually called the "indicial equation", which is slightly different. For the $$p_mt^my^{(m)}$$ term in the ODE, the corresponding term in the indicial equation is $$p_mn(n-1)\ldots(n-m+1)=p_m\frac{n!}{(n-m)!}$$.

So, what happens when it isn't exactly an Euler equation? Then you just group them up by shifted powers. For example,

$$(x^2+x+1)y''+(x^2+1)y'+(x^2+x+1)y=0$$

can be grouped up as follows:

$$(x^2y''+y'+y)+(xy''+y')+(y'')+(x^2y)+(xy)$$

Basically, you want groups of descending powers and orders. We'll call these "EE groups", for Euler Equation groups.

$$(x^2y''+y'+y)+\frac{1}{x}(x^2y''+xy')+\frac{1}{x^2}(x^2y'')+x^2(y)+x(y)$$

Then you will have to shift the index by some amount. To see this, compare $$y''\mapsto(n+1)(n+2)a_{n+2}$$ and $$x^2y''\mapsto n(n-1)a_n$$. The first is just the second, but $$n$$ has been shifted **up** by 2.

So if you have a positive power of $$x$$ multiplying an Euler Equation, you shift the index of the EE group down by that power.

If you have a positive power of $$x$$ dividing an Euler Equation, you shift the index of the EE group up by that power.

Let's look at an example.

# Example (Legendre equation)

$$(1-x^2)y''-2xy'+\alpha(\alpha+1)y=0$$

Notice how this is *almost* an Euler equation. We have an $$x^2y''$$ and an $$xy'$$ term, but there's a $$y''$$ all by itself bringing down the party. So let's rearrange the equation as such:

$$y''-(x^2y''+2xy'-\alpha(\alpha+1)y)=0$$

And, well, we actually know the series expansion for both terms. We know that $$y''=\sum_{n=0}^\infty (n+1)(n+2)a_{n+2}x^{n}$$ and

$$x^2y''+2xy'-\alpha(\alpha+1)y=\sum_{n=0}^\infty(n(n-1)+2n-\alpha(\alpha+1))a_nx^n$$

We can factor $$n(n-1)+2n-\alpha(\alpha+1)=(n-\alpha)(n+\alpha+1)$$.

So, plugging in our series will yield us

$$\sum_{n=0}^\infty
\bigg(
  (n+1)(n+2)a_{n+2}-(n-\alpha)(n+\alpha+1)a_n
\bigg)x^n=0
$$

Observe that there was no point to even writing the sum. We could have jumped straight to

$$(n+1)(n+2)a_{n+2}-(n-\alpha)(n+\alpha+1)a_n=0\implies a_{n+2}=\frac{(n-\alpha)(n+\alpha+1)a_n}{(n+1)(n+2)}$$

And there's our recurrence relation! That was quick. Now we can start plugging in $$n=0,1,2,\ldots$$ to find our power series coefficients. Such as,

$$a_2=-\frac{\alpha(\alpha+1)}{2}a_0$$

$$a_3=-\frac{(\alpha-1)(\alpha+2)}{3!}a_0$$

# The Straggler Coefficients

When doing series solutions the normal way, often you get stragglers that end up outside of the sum. Rather than worry about them at all, we can skip that entirely by calculating the relationship between the first few coefficients directly from the original ODE itself.

## The direct way to calculate coefficients

Once you see it, you may think "wait, we can just do that?" And the answer will be a resounding "YES". Also, **this is almost always the fastest way to do problems which ask you to find the first few terms of the series solution to an initial value problem, but not a closed form**!

Basically, for the initial value problem,

$$
\begin{equation}
y''=p(x)y'+q(x)y,\quad y(0)=y_0,\;y'(0)=y'_0
\end{equation}
$$

First, we know that $$a_0=y_0$$ and $$a_1=y'_0$$. That directly follows from Taylor's theorem.

Now, check out what happens if we just plug in $$x=0$$ to the equation. Note that if $$y=a_0+a_1x+a_2x^2+\ldots$$, then using Taylor's theorem we know that $$a_n=\frac{y^{(n)}(0)}{n!}$$. Which implies that $$y^{(n)}(0)=n!\,a_n$$.

$$y''(0)=p(0)y'(0)+q(0)y(0)\implies 2!\,a_2=p(0)y'_0+q(0)y_0$$

Thus, we can solve for $$a_2$$ directly:

$$a_2=\frac{1}{2}(p(0)y'_0+q(0)y_0)$$

There is really no need to memorize this formula, but just remember that you can use this method to directly calculate the coefficients which are left out of the series (or cannot be directly computed from the recurrence relation).

But wait, there's more! You can find more than just $$a_2$$, if you differentiate the whole ODE.

$$y'''=p(x)y''+(p'(x)+q(x))y'+q'(x)y$$

Then you can just plug in $$x=0$$ again!

**Important note**: If there is a coefficient on the $$y''$$ term, then it is often advantageous NOT to divide it out. This usually simplifies the differentiation greatly, since you're doing the product rule and not the quotient rule. And there are tricks for multiple applications of the product rule (like using Pascal's triangle), but nothing like that for the quotient rule.

# When the IVP is not centered at 0

This is actually really great. You can do a quick change of variables and then carry on as if $$x_0=0$$. Just do $$t=x-x_0\implies x=t+x_0$$. So,

$$P(x)y''+Q(x)y'+R(x)y=0,\quad y(x_0)=y_0,\;y'(x_0)=y'_0$$

becomes

$$P(t+x_0)y''+Q(t+x_0)y'+R(t+x_0)y=0,\quad y(0)=y_0,\;y'(0)=y'_0$$

And then you just do as you do normally. No need to write $$y=\sum_{n=0}^\infty a_n(x-x_0)^n$$, or to find the Taylor series of $$P,Q,R$$ centered around $$x_0$$. Do you *want* to do that? Because I don't.

Instead, just do the normal solution method with $$y=\sum_{n=0}^\infty a_nt^n$$.

# More Examples


Find closed forms for the general solution of

$$
(x^2-4x-1)y''-2(x-2)y'+2y=0
$$

We rearrange it into EE groups:

$$(x^2y''-2xy'+2y)-4(xy''-y')-y''=0$$

The first term will be $$x^2y''-2xy'+2y\mapsto (n(n-1)-2n+2)a_n=(n-1)(n-2)a_n$$.

The second term will be $$4(n(n-1)-n)a_n=4n(n-2)a_n$$ but shifted up by one, since it's a power below an Euler Equation. Thus, $$4(xy''-y')\mapsto 4(n+1)(n-1)a_{n+1}$$.

And finally, we are very familiar with $$y''\mapsto(n+1)(n+2)a_{n+2}$$.

In total, giving us

$$(n-1)(n-2)a_n-4(n+1)(n-1)a_{n+1}-(n+1)(n+2)a_{n+2}=0$$

Solving for the highest index term,

$$a_{n+2}=(n-1)\frac{(n-2)a_n-4(n+1)a_{n+1}}{(n+1)(n+2)}$$

The most interesting thing to observe is the $$(n-1)$$ multiplying the whole thing. This means that plugging in $$n=1$$ gives us

$$a_3=0$$

And if we plug in anything higher than $$n=1$$, such as $$n=2$$, we get

$$a_4=1\frac{0a_2-8a_3}{12}=0$$

So it seems our solutions don't have Taylor series which go higher than a quadratic. Plugging in $$n=0$$ yields

$$a_2=a_0+2a_1$$

So we can say that our solution is

$$y=a_0+a_1x+(a_0+2a_1)x^2=a_0(1+x^2)+a_1(x+2x^2)$$

We can let $$a_0$$ and $$a_1$$ be our arbitrary constants, and it gives us the [normalized solutions](../normalized/){:target="_blank"}!

$$y=c_1(1+x^2)+c_2(x+2x^2)$$

Setting $$c_1=-2,\;c_2=1$$ gives us that $$y=x-2$$ is a solution. As a pro-tip, you could have actually seen that solution by inspection!

In general, if you have a linear function on $$y'$$ and the slope constant on $$y$$,

$$P(x)y''+(mx+b)y'-my=0$$

then $$y=mx+b$$ will be a solution. This is especially useful if you have something like

$$P(x)y''-xy'+y=0$$

Then $$y=x$$ is a solution to this, for example.

---

Find the solution to

$$y''+(t-1)y'+2y=0,\quad y(1)=0,\;y'(1)=1$$

We can start by simplifying the problem with a change of variables which will center the initial value problem around zero: $$x=t-1$$. Plugging that in gives us

$$y''+xy'+2y=0,\quad y(0)=0,\;y'(0)=1$$

We can rearrange it into two EE groups

$$y''+(xy'+2y)=0$$

$$xy'+2y$$ is fairly straightforward as $$(n+2)a_n$$. And, once again, $$y''\mapsto(n+1)(n+2)a_{n+2}$$. So our recurrence relation is

$$((n+1)(n+2)a_{n+2})+((n+2)a_n)=0$$

Since $$n\geq0\implies n+2\neq0$$, we can divide out the $$n+2$$ from the equation to get

$$a_{n+2}=-\frac{a_n}{n+1}$$

Now, we can find our coefficients.

$$a_2=-a_0=0$$

We can see that every even $$n$$ will result in zero. So we can just focus on the odd terms. In cases where every other coefficient is zero, it is sometimes the case that the solution (or part of it) is a function of $$x^2$$. Let's keep that in mind.

$$a_3=-\frac{a_1}{2}=-\frac{1}{2}$$

$$a_5=\frac{1}{2\cdot 4}=\frac{1}{2^2(2!)}$$

Often, it can make it easier to see the pattern when you force a factorial in there.

$$a_7=-\frac{1}{2^2(2!)\cdot 6}=-\frac{1}{2^3(3!)}$$

And we can see that this pattern will repeat. So it appears that

$$a_{2n+1}=\frac{\left(-\frac{1}{2}\right)^n}{n!}$$

Making our solution $$y=\sum_{n=0}^\infty \frac{\left(-\frac{1}{2}\right)^nx^{2n+1}}{n!}$$, which we can manipulate into

$$y=x\sum_{n=0}^\infty \frac{\left(-\frac{x^2}{2}\right)^n}{n!}=xe^{-\frac{x^2}{2}}$$

Finally, we undo the substitution to get our actual solution

$$y=(t-1)e^{-\frac{(t-1)^2}{2}}$$

---

Note, we could have sorta cheesed it by using the direct method. By solving for $$y''$$, we get

$$y''=-(t-1)y'-2y$$

Then, plugging in $$t=1$$ and then differentiating, we get the following:

$$2a_2=0a_1-2(0)=0$$

$$y'''=-(t-1)y''-3y'$$

$$3!a_3=-3a_1\implies a_3=-\frac{1}{2}$$

$$y^{(4)}=-(t-1)y'''-4y''$$

We can observe once again, that the even terms produce zero.

$$y^{(5)}=-(t-1)y^{(4)}-5y'''$$

$$5!a_5=-5(3!)a_3\implies a_5=\frac{1}{8}$$

And so on...
