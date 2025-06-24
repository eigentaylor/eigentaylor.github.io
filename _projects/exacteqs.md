---
layout: distill
title: Exact Equations Done Quick
date: 2021-09-09 0
description: speedrun WR
comments: true
importance: 3
category: differential equations
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: How to Solve Exact Equations Quickly
    subsections:
      - name: Example
      - name: Why does this work
  - name: An Intuitive Approach To Solving Exact Equations
  - name: Integrating Factors
---

Originally published Sept. 9, 2021. Heavily revised Dec. 6, 2021.

Quick note: it is generally incorrect to say that a solution to an exact equation is simply $$\psi(x,y)$$. The actual solution would be $$\psi(x,y)=C$$. However, for brevity, the $$=C$$  will be implied.

# How to Solve Exact Equations Quickly

The method is pretty simple and straightforward, so it doesn't take long to explain.

Given an exact equation $$M(x,y)+N(x,y)y'=0$$, the solution $$\psi(x,y)$$ can be obtained by integrating $$M$$ with respect to $$x$$ and $$N$$ with respect to $$y$$. Write every term that appears in each solution exactly once. That is, leave out duplicate terms in your answer.

#### Example

It can be shown that the following equation is exact

$$(2xy^2+4x+e^x)+(3+\cos(y)+2x^2y)y'=0$$

Integrating $$M$$ with respect to $$x$$ gives $$x^2y^2+2x^2+e^x$$

Integrating $$N$$ with respect to $$y$$ gives $$3y+\sin(y)+x^2y^2$$.

Putting those both together (ignoring the second $$x^2y^2$$) we get the solution

$$\psi(x,y)=x^2y^2+2x^2+e^x+3y+\sin(y)=C$$

Done.

### Why does this work?

The reasoning is a bit mundane, but based on the information provided by the following section. But the general idea is that if $$\psi(x,y)$$ is supposed to be a solution to $$M(x,y)+N(x,y)y'=0$$, then

$$\psi_x=M,\quad \psi_y=N$$

If we integrate both sides

$$\psi=\int M\,dx+h_1(y),\quad \psi=\int N\,dy+h_2(x)$$

So integrating $$M$$ and $$N$$ is a "direct" way to get the solution $$\psi(x,y)$$. However, doing just one of these will not give us everything.

For example, integrating $$M$$ will not give us any terms of $$\psi$$ which are purely functions of $$y$$, not counting constants (as they will be lost completely in the process of taking the partial derivative with respect to $$x$$). But integrating $$N$$ with respect to $$y$$ *will* give us all of those pure nonconstant functions of $$y$$, which *weren't* completely lost taking the partial derivative with repsect to $$y$$.

So between the two integrations, we will get every term of $$\psi$$. Of course, there are almost always duplicates in the results of the integration, but counting them twice would be incorrect. Taking a general example to get an idea, suppose that, neglecting any constants/functions of integration, we get the explicit results

$$\int M\,dx=f(x,y)+g_1(x),\quad\int N\,dy=f(x,y)+g_2(y)$$

for known functions $$f,g_1,g_2$$. Then

$$\psi(x,y)=f(x,y)+g_1(x)+h_1(y)=f(x,y)+g_2(y)+h_2(x)$$

where $$h_1,h_2$$ are *unknown*. Comparing terms, it's clear that $$h_1(y)=g_2(y)$$ and $$h_2(x)=g_1(x)$$. Thus, if we take the left solution,

$$\psi(x,y)=f(x,y)+g_1(x)+g_2(y)$$

Observe that we get an equivalent expression if we take the right solution of $$f(x,y)+g_2(y)+g_1(x)$$.

So although it may initially *seem* like we are just adding the results of integration together, that is *not* what we are doing.

$$\psi(x,y)\neq\bigg(f(x,y)+g_1(x)\bigg)+\bigg(f(x,y)+g_2(y)\bigg)$$

The solution has $$f$$ in it, not $$2f$$. So the end result is that the solution will be a *combination*/union (not an sum) of the two integration results, where we only write repeated terms *once*.

# An Intuitive Approach To Solving Exact Equations

This is an attempt at a more intuitive derivation for the way that is usually taught in a differential equations course.

We seek to find the solution to the differential equation

$$\begin{equation}
M(x,y)+N(x,y)\frac{dy}{dx}=0
\end{equation}$$

We are hoping that there exists some function $$\psi(x,y)$$ such that

$$\begin{equation}
\frac{d}{dx}\psi(x,y)=M(x,y)+N(x,y)\frac{dy}{dx}
\end{equation}$$

Using the multivariable definition of the chain rule to calculate $$\frac{d}{dx}\psi(x,y)$$,

$$\begin{equation}
\frac{d}{dx}\psi(x,y)=\psi_x(x,y)+\psi_y(x,y)\frac{dy}{dx}
\end{equation}$$

By matching up terms, we see

$$\begin{equation}
M(x,y)=\psi_x(x,y),\quad N(x,y)=\psi_y(x,y)
\end{equation}$$

We can use a *very* bodacious result of multivariable calculus that

$$\begin{equation}
\psi_{xy}(x,y)=\psi_{yx}(x,y)\implies M_y=N_x
\end{equation}$$

Therefore, if that is so the equation is exact and we may find $$f$$!

We have two options now: We can start by integrating $$M$$ with respect to $$x$$, or $$N$$ with respect to $$y$$. We choose whichever integral looks easier, but we'll assume for now that we are choosing $$M$$.

$$\begin{equation}
\psi(x,y)=\int M(x,y)\,dx+h(y)
\end{equation}$$

If this is to be truly the $$\psi$$ we want, then its partial derivative with respect to $$y$$ has to be $$N$$ as we defined above. So we set $$\psi_y=N$$

$$\begin{equation}
N(x,y)=\frac{\partial}{\partial y}\left(\int M(x,y)\,dx\right)+h'(y)
\end{equation}$$

Now we can solve for $$h'(y)$$ and integrate it to get the correct $$h(y)$$ and then we have our answer $$\psi(x,y)$$.

We could have instead integrated $$N$$ with respect to $$y$$ to get an $$h(x)$$ and instead find that $$h$$ through the equation

$$\begin{equation}
M(x,y)=\frac{\partial}{\partial x}\left(\int N(x,y)\,dy\right)+h'(x)
\end{equation}$$

In summary,

1. Integrate $$M$$ with respect to $$x$$ and get a function of integration $$h(y)$$
2. Partially differentiate with respect to $$y$$ and set it equal to $$N$$
3. Solve for $$h'(y)$$ and integrate
4. Profit

or

1. Integrate $$N$$ with respect to $$y$$ and get a function of integration $$h(x)$$
2. Partially differentiate with respect to $$x$$ and set it equal to $$M$$
3. Solve for $$h'(x)$$ and integrate
4. Profit

## Integrating Factors

If $$M_y\neq N_x$$, then it is not exact. But we can make it so (most of the time)!

As a quick sidenote, if there is a common factor to both $$M$$ and $$N$$, it's possible that that common factor can make it impossible to find an integrating factor using the methods that will be described. Even if the common factor is a simple $$x$$ or $$y$$.

First we suppose there is an integrating factor which is just a function of $$x$$, $$\mu(x)$$ giving us

$$\begin{equation}
\mu(x)M(x,y)+\mu(x)N(x,y)\frac{dy}{dx}=0
\end{equation}$$

We set the partials equal,

$$\begin{equation}
\frac{\partial}{\partial y}
\left(\mu(x)M\right)=
\frac{\partial}{\partial x}
\left(\mu(x)N\right)
\end{equation}$$

$$\begin{equation}
\mu(x)M_y=
\mu'(x)N+\mu(x)N_x
\end{equation}$$

Solving for $$\mu'$$,

$$\begin{equation}
\mu'(x)=\frac{M_y-N_x}{N}\mu(x)
\end{equation}$$

So if $$\frac{M_y-N_x}{N}$$ is a function of only $$x$$, then this is an easy first-order equation we can solve to find $$\mu$$. Then we just execute the process detailed in the previous section.

If $$\frac{M_y-N_x}{N}$$ is not a function of only $$x$$, then we can instead seek an integrating factor $$\mu(y)$$. Repeating the process above,

$$\begin{equation}
\mu(y)M(x,y)+\mu(y)N(x,y)\frac{dy}{dx}=0
\end{equation}$$

$$\begin{equation}
\mu'(y)M+\mu(y)M_y=
\mu(y)N_x
\end{equation}$$

$$\begin{equation}
\mu'(y)=\frac{N_x-M_y}{M}\mu(y)
\end{equation}$$

If $$\frac{N_x-M_y}{M}$$ is a function only $$y$$, then we can again solve for $$\mu$$ and execute the steps in the first section.

If neither of those work... then the integrating factor is probably a function of both $$x$$ and $$y$$, in which case it is *not* an easy task to find it. There are some specific formulas for particular forms of integrating factors, but in most questions given in a Differential Equations class, these should suffice.

The equations for integrating factors are, in summary,

$$\begin{align}
\mu'(x)&=\frac{M_y-N_x}{N}\mu(x)\\
\mu'(y)&=\frac{N_x-M_y}{M}\mu(y)
\end{align}$$
