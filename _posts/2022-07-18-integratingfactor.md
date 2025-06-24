---
layout: distill
title: Integrating Factors Explained
date: 2022-07-18 0
description: the most common way to solve first order linear ODE's
comments: true
importance: 3
categories: differential-equations
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: What is a first order linear ODE
  - name: How do we solve them
  - name: Finding the integrating factor
    subsections:
      - name: A detour with exponentials
  - name: Solving for μ
  - name: Solving the equation
  - name: Unnecessary further simplifications
  - name: Further notes
---

This is one of the first things taught in an intro to differential equations class, and I think it is very accessible to students who have taken basic calculus. The only snag might be that you may not know how to do the integral you inevitably obtain, but the overall idea for the process is straightforward enough, I think.

As usual I kind of go overboard on the additional facts which you don't really *need* to know. So just ignore them if you don't care. I'll put **Aside** in front of those kind of things.

## What is a first order linear ODE?

A first order linear differential equation is one of the form

$$
\begin{equation}
y'+p(t)y=g(t)
\end{equation}
$$

Maybe you have a function on the $$y'$$ term, but dividing it out gives the standard form above. An initial condition such as $$y(0)=3$$ is also common, but that only needs to be worried about near the end of the solving process.

We also won't be concerning ourselves about where solutions to the equation (initial value problems) exist. That's a bit too technical for the purposes of this post.

We will also be using some compact prime notation. Basically

$$
\begin{equation}
\frac{d}{dt}(f(t)h(t))=(fh)'
\end{equation}
$$

## How do we solve them?

Well, first, let's review some basic calculus. Specifically, the product rule!

$$
\begin{equation}
(fh)'=fh'+f'h
\end{equation}
$$

The order doesn't matter because it's a sum. Now, observe what happens if we replace $$h$$ with $$y$$

$$(fy)'=fy'+f'y$$

That looks sort of close to the left side of our original differential equation!

So, the motivating idea is to find some function <a href="https://puu.sh/JbL0d/bbacfdb2ca.mp4" target="_blank">$$\mu(t)$$</a> which will make the left side of our equation a simple product rule. Because then we can integrate both sides and solve for $$y$$.

## Finding the integrating factor

Now, this is the idea behind almost every single technique you learn in a differential equations class: "*the solution probably looks like this, so let's plug it in and solve for the unknowns*".

When we multiply our original equation by $$\mu$$, we get

$$\mu y'+\mu p(t)y=\mu g(t)$$

And our goal, remember, is to get that left side to look like

$$\mu y'+p(t)\mu y=(fy)'$$

Well, if we expand it out, we get

$$\mu y'+p(t)\mu y=fy'+f'y$$

So, matching up the terms, we get that $$\mu=f$$ and $$p(t)\mu=f'=\mu'$$.

Then, to solve for $$\mu$$, we need to solve

$$
\begin{equation}
\mu'=p(t)\mu
\end{equation}
$$

Now, you can solve this differential equation in a lot of different ways. Usually as a separable equation. But instead of teaching you that technique which you may not know, I'm just going to show you the differentiation rule for exponentials:

### A detour with exponentials

$$
\begin{equation}
\left(e^{f(t)}\right)'=f'(t)e^{f(t)}
\end{equation}
$$

In words, the observation to make is that differentiating an exponential function is the same as multiplying it by some function. That is,

$$y'=f'(t)y\iff y=Ce^{f(t)}$$

Note that we can multiply by a constant since it doesn't change anything about the differentiation.

## Solving for μ

All this to say, we just need some function $$P(t)$$ such that $$P'(t)=p(t)$$. Basically, $$P(t)=\int p(t)dt$$. Any one will do!  **Aside**: This is because $$e^{P(t)+K}=Ce^{P(t)}$$, and any scalar multiple of an integrating factor is also an integrating factor. So just pick one antiderivative and go with it.

So, if we plug that into our differential equation,

$$e^{P(t)}y'+p(t)e^{P(t)}y=e^{P(t)}g(t)$$

We can verify that, under the assumption that $$P'(t)=p(t)$$, the left side is indeed $$e^{P(t)}y'+p(t)e^{P(t)}y=\left(e^{P(t)}y\right)'$$.

$$\left(e^{P(t)}y\right)'=e^{P(t)}g(t)$$

In summary, the basic equation for the integrating factor is

$$
\begin{equation}
\mu(t)=e^{\int p(t)dt}
\end{equation}
$$

## Solving the equation

Now, we can just integrate both sides (not forgetting our constant of integration).

$$e^{P(t)}y=C+\int e^{P(t)}g(t)dt$$

Finally, we can solve for $$y$$ by dividing both sides by $$e^{P(t)}$$ (or multiplying by $$e^{-P(t)}$$).

$$y=Ce^{-P(t)}+e^{-P(t)}\int e^{P(t)}g(t)dt$$

**Aside**: One interesting observation is that we can express this solution more compactly in terms of $$\mu$$.

$$y=\frac{C}{\mu}+\frac{\int \mu g}{\mu}$$

And if you're in differential equations or basic calculus now, your professor may not like this more compact way of writing the integral without the d(whatever). But the textbook I used for my intro to analysis class (Understanding Analysis by Stephen Abbott) used it, so just tell your professor that you're using Abbott (i.e. big brain advanced baller) notation (and then don't blame me if your professor isn't having that).

## Unnecessary further simplifications

The rest of the post is an **aside**. This is just gravy if you're still interested in knowing more and going further with these ideas. The post is over; you can leave and go home now if you want.

There are some other simplifications you can make which I personally like. They aren't really super practical in terms of actually solving these equations, usually, but I think they're cool!

Personally, I like to use dummy variables for integration.

$$y=Ce^{-P(t)}+e^{-P(t)}\int_{t_0}^t e^{P(s)}g(s)ds$$

We can also use another dummy variable $$P(t)$$:

$$P(t)=\int_{t_0}^tp(r)dr$$

Also using that $$P(s)=\int_{t_0}^sp(r)dr$$. Changing our solution to

$$y=Ce^{-\int_{t_0}^tp(r)dr}+e^{-\int_{t_0}^tp(r)dr}\int_{t_0}^t e^{\int_{t_0}^sp(r)dr}g(s)ds$$

This has the added benefit of making it so that we can replace $$C$$ with $$y(t_0)$$. This is because plugging in $$t=t_0$$ makes all the integrals zero, leaving us with just $$C$$. This eliminates the need to solve for $$C$$ in an initial value problem. Just be careful that the integrals do not diverge when integrating from $$t_0$$. If they do, choose any other arbitrary starting bound that gives a convergent (gucci) integral.

$$y=y(t_0)e^{-\int_{t_0}^tp(r)dr}+e^{-\int_{t_0}^tp(r)dr}\int_{t_0}^t e^{\int_{t_0}^sp(r)dr}g(s)ds$$

We may also distribute the exponential into the integral now, because we are using a dummy variable for the integration. Note that in the exponent we will get

$$\int_{t_0}^sp(r)dr-\int_{t_0}^tp(r)dr$$

Which we can simplify to $$\int_t^{t_0}p(r)dr+\int_{t_0}^sp(r)dr=\int_{t}^sp(r)dr$$ using our rules for integration.

$$y=y(t_0)e^{-\int_{t_0}^tp(r)dr}+\int_{t_0}^t e^{\int_{t}^sp(r)dr}g(s)ds$$

Another personal preference is to use $$\exp(x)$$ instead of $$e^x$$ when the exponent is big and messy (such as when we stick a whole integral up in there).

$$y=y(t_0)\exp\left(-\int_{t_0}^tp(r)dr\right)+\int_{t_0}^t\exp\left(\int_{t}^sp(r)dr\right)g(s)ds$$

## Further notes

Here's some more information on how this concept generalizes to second order equations, if you're interested.

Did you know every linear second order differential equation also has an integrating factor? The reason nobody ever uses this, though, is that, usually, finding it is just as hard as solving the equation normally.

For example, trying to use an integrating factor to solve

$$y''+y=0$$

ends up giving you the following differential equation for the integrating factor $$\mu$$:

$$\mu''+\mu=0$$

Which means that the integrating factor for the differential equation must be a solution to the differential equation. Making this method absolutely useless for this problem.

If you want to know how the method works, though, basically the idea is to find a function $$\mu$$ and $$f$$ such that when you multiply $$P(t)y''+Q(t)y'+R(t)y$$ by $$\mu$$, you get

$$P(t)\mu y''+Q(t)\mu y'+R(t)\mu y=(P(t)\mu y'+fy)'$$

Setting equal the coefficients gives you

$$f'=R\mu,\quad P\mu'+P'\mu+f=Q\mu$$

If you differentiate the right equation and substitute in $$R\mu$$ for $$f'$$, you get

$$P\mu''+(2P'-Q)\mu'+(P''-Q'+R)\mu=0$$

This is also called the Adjoint Equation, and it's usually not much nicer than the original. If $$P''-Q'+R=0$$, though, then the adjoint equation is first order (and linear) in $$\mu'$$, allowing you to solve it either with another integrating factor or as a separable equation. When this happens, the original equation is called "exact" (yes, this is the second order version of exact equations!).
