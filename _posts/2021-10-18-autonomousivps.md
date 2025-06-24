---
layout: distill
title: Easily Solving Autonomous IVPs Off the Origin
date: 2021-10-18 0
description: Easily solving linear homogeneous constant coefficient initial problems when the initial point is not t=0
comments: true
importance: 2
category: differential-equations
authors:
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: An Example
  - name: Summary
  - name: Proof?
---

**Updated 11/13/23**

Given constant coefficients $$a_0,a_1,\ldots,a_n$$, with $$a_n\neq0$$, and the $$n$$-th order Initial Value Problem

$$
\begin{gather*}
a_ny^{(n)}+\ldots+a_1y'+a_0y=0,\\y(t_0)=y_0,\ldots,y^{(n-1)}(t_0)=y^{(n-1)}_0
\end{gather*}
$$

The solution to this initial value problem will be $$y(t)=x(t-t_0)$$, where $$x(t)$$ is a solution to the same IVP centered instead at the origin.

$$
\begin{gather*}
a_nx^{(n)}+\ldots+a_1x'+a_0x=0,\\x(0)=y_0,\ldots,x^{(n-1)}(0)=y^{(n-1)}_0
\end{gather*}
$$

In other words, simply solve the IVP as if it was centered at the origin and then shift the solution.

*Alternatively*, you could simply take your general solution

$$y(t)=c_1y_1(t)+\ldots+c_ny_n(t)$$

And instead use the *other* valid general solution

$$y(t)=c_1y_1(t-t_0)+\ldots+c_ny_n(t_0)$$

---

## An Example

Take the example IVP of

$$y''+y=0,\quad y\left(0\right)=4,\;y'\left(0\right)=13$$

This is very easy, because the standard homogeneous solutions are already [normalized](../normalized/){:target="_blank"}. The solution is simply

$$y=4\cos(t)+13\sin(t)$$

Now compare this to the shifted IVP,

$$y''+y=0,$$

$$y\left(\frac{\pi}{20}\right)=4,\;y'\left(\frac{\pi}{20}\right)=13$$

I won't lie, solving this is kind of awful. You need to solve the system of equations

$$
\begin{array}{ccccc}
c_1\cos\left(\frac{\pi}{20}\right)&+&c_2\sin\left(\frac{\pi}{20}\right)&=&4\\
-c_1\sin\left(\frac{\pi}{20}\right)&+&c_2\cos\left(\frac{\pi}{20}\right)&=&13\\
\end{array}
$$

which just sucks. Cramer's rule is probably your best bet since the coefficient matrix has a determinant $$1$$, but solving this by using a matrix inverse is another not so bad way to do it. Good luck trying to use elimination or substitution though lol.

However you solve it, the solution turns out to be

$$y=\left(4\cos\left(\frac{\pi}{20}\right)-13\sin\left(\frac{\pi}{20}\right)\right)\cos(t)$$

$$+\left(13\cos\left(\frac{\pi}{20}\right)+4\sin\left(\frac{\pi}{20}\right)\right)\sin(t)$$

If we rearange to collect the terms with $$4$$ and $$13$$,

$$y=4\left(\cos\left(\frac{\pi}{20}\right)\cos(t)+\sin\left(\frac{\pi}{20}\right)\sin(t)\right)$$

$$+13\left(\cos\left(\frac{\pi}{20}\right)\sin(t)-\sin\left(\frac{\pi}{20}\right)\cos(t)\right)$$

We can actually combine the terms using the angle sum formulas,

$$y=4\cos\left(t-\frac{\pi}{20}\right)+13\sin\left(t-\frac{\pi}{20}\right)$$

Well... that is interesting. It's just our solution to the initial value problem at the origin, but shifted by the initial point. Exactly as described above.

So yes! You can simply write down the solution without needing to do a bit of scratch work.

In fact, in general the solution to the initial value problem

$$y''+\omega_0^2y=0,\quad y(t_0)=y_0,\;y'(t_0)=y'_0$$

will be simply

$$y(t)=y_0\cos(\omega_0(t-t_0))+\frac{y'_0}{\omega_0}\sin(\omega_0(t-t_0))$$

The similarly simple $$\sinh$$ and $$\cosh$$ provide a beautiful nearly identical formula.

$$y''-\omega_0^2y=0,\quad y(t_0)=y_0,\;y'(t_0)=y'_0$$

will have the solution

$$y(t)=y_0\cosh(\omega_0(t-t_0))+\frac{y'_0}{\omega_0}\sinh(\omega_0(t-t_0))$$

---

## Summary

I believe this concept to be quite straightforward. The big brain move here being to not use your big brain to think about the initial point at all until the very end.

So the big question: Is this worth knowing? Sure, I think so. The solutions to linear constant coefficient differential equations behave so nicely at $$t=0$$ and so grossly outside of it, why subject yourself to solving such a tedious system of equations when you dont have to?

---

## Proof?

I guess. I don't believe there is a strong need for a rigorous proof of this property, as it follows relatively straightforwardly from the most basic properties of exponentials. Namely:

**Shifting an exponential is equivalent to simply scaling it.**

So if $$e^{\alpha t}$$ is a homogeneous solution, then so is $$e^{\alpha(t-t_0)}$$, since that is simply a constant multiple of $$e^{\alpha t}$$ ($$e^{\alpha(t-t_0)}=e^{-t_0}e^{\alpha t}$$).

Does this apply to *every* solution of a linear constant coefficient homogeneous differential equation? Yes. Yes it does.

Every homogeneous solution to a linear constant coefficient homogeneous differential equation

\begin{equation}
p(D)y=0
\end{equation}

is of the form

\begin{equation}
y(t)=t^ke^{\alpha t}
\end{equation}

for some $$\alpha\in\mathbb{C}$$ and $$k\in\mathbb{Z}_{\geq0}$$.

Keep in mind that if $$t^ke^{\alpha t}$$ is a homogeneous solution, then so are $$e^{\alpha t},te^{\alpha t},\ldots,t^{k-1}e^{\alpha t}$$. Therefore, since $$y(t-t_0)=(t-t_0)^ke^{t-t_0}$$ is simply a linear combination of other homogeneous solutions, it too is a homogeneous solution. Specifically, a homogeneous solution for which, conviniently, $$y(t_0)=y'(t_0)=\ldots=y^{(k-1)}(t_0)=0$$. Making it highly favorable for use in solving a system of equations related to $$y(t_0),y'(t_0),\ldots,y^{(n-1)}(t_0)$$!

How do we know that $$y_1(t-t_0),\ldots,y_n(t-t_0)$$ will form a fundamental set of solutions, though? Well, we can use the Wronskian. Abel's theorem tells us that the Wronskian of a set of solutions is either always zero or always nonzero on an interval where the coefficients of the differential equation are continuous. Since our constant coefficients are contiuous everywhere, as long as the Wronskian is nonzero at one point, it will be nonzero for all values of $$t$$. We can then say

$$
\begin{gather*}
W[y_1,\ldots,y_n](t)\neq0\;\forall t\\\implies W[y_1,\ldots,y_n](t-t_0)\neq0\;\forall t
\end{gather*}
$$

Therefore, if the functions $$y_1(t),\ldots,y_n(t)$$ are linearly independent, then so are $$y_1(t-t_0),\ldots,y_n(t-t_0)$$. As we already showed $$y_1(t-t_0),\ldots,y_n(t-t_0)$$ are still solutions to the differential equation, we have thus proved that $$y_1(t-t_0),\ldots,y_n(t-t_0)$$ form a fundamental set of solutions, and can be used to solve any initial value problem.
