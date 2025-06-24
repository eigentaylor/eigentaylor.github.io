---
layout: distill
title: Constant Coefficient ODEs Made Simple with Linear Operators
date: 2023-11-11
description: No more guessing. Let's make it intuitive with linear algebra.
comments: true
importance: 1
featured: true
tags: best
category: differential-equations
authors:
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Linear Algebra Recap
    subsections:
      - name: Linear Transformations
      - name: Eigenvectors
      - name: Linear Operators and Polynomials
  - name: The Differential Operator
  - name: The Most Important ODE
  - name: Repeated Roots
    subsections:
      - name: Exponential Shift
      - name: Exponential Shift Into Overdrive
  - name: Exponential Response Formula
  - name: nth Order. n Independent Solutions
  - name: A remark on undetermined coefficients
  - name: Complex Stuff
---

Last year, I made a post about [this same topic](../linconstcoef/){:target="_blank"}, but since then, I have developed a new way of understanding this topic through the lens of linear algebra which makes many of the seemingly arbitrary choices seem almost stupidly obvious. One time, I was discussing differential equations with a friend of mine at a bar who was taking a class in it at the time. He asked me, "why do we know that the solutions to these equations *have* to be exponentials?" My explanation was not great, but years later I presented the following explanation to him at a different bar which I think was much better. In his words, it was "mindblowing". I'm hoping you will feel similarly. **It does, however, require linear algebra.**

We will address the following questions in the context of constant coefficient linear ordinary differential equations:

$$a_ny^{(n)}+\ldots+a_1y'+a_0y=0$$

1. Why is our guess for the solution $$e^{\lambda t}$$?
2. Why do we multiply by $$t$$ when we have a repeated root of the characteristic polynomial?
3. Why does an $$n$$th order equation have exactly $$n$$ linearly independent homogeneous solutions?

And as a bonus, I'm going to explain why the [**exponential response formula**](../alphamethod/){:target="_blank"} is actually absurdly trivial!

# Linear Algebra Recap

Let us review some basic linear algebra facts and terminology.

A **subspace** is a nonempty subset of a vector space that is closed under linear combinations.

## Linear Transformations

A linear transformation $$T$$, is a function that preserves linear combinations.

\begin{equation}
T(c_1x_1+\ldots+c_kx_k)=c_1T(x_1)+\ldots+c_kT(x_k)
\end{equation}

The derivative $$\frac{d}{dt}$$ is an example of a linear transformation. This is by the linearity of differentiation. That is, by the fact that we can pull out constants from derivatives, and that the derivative of a sum is just the sum of derivatives.

If $$T(x)=y$$, then we say that $$y$$ is the **image** of $$x$$ under $$T$$ (often, we just say the image of $$x$$). The image is unique because $$T$$ is a function. We call $$x$$ the **preimage** of $$y$$ under $$T$$. A preimage is not necessarily unique.

If the image of an element $$x$$ is $$0$$ ($$T(x)=0$$), then we say that $$x$$ is in the **kernel** of $$T$$ ($$x\in\ker(T)$$). The kernel is the set of all preimages of $$0$$. We sometimes call the kernel the set of all **homogeneous solutions** to the equation $$T(x)=0$$. The kernel is a subspace.

### Preimage Theorem

Assume the equation $$T(x)=b$$ (which is asking the question "what is a preimage of $$b$$?") has at least one solution, $$x=x_p$$. Then *every* solution is of the form $$x=x_p+x_h$$ where $$x_h$$ is an element in $$\ker(T)$$. That is, **all preimages of a linear transformation are off from a single particular preimage by something in the kernel**.

**Proof:** If $$x_0$$ is a vector of the form $$x_0=x_p+x_h$$, then $$T(x_0)=T(x_p+x_h)=T(x_p)+T(x_h)=b+0=b$$. Hence, $$x_0$$ is also a preimage of $$b$$, showing that any vector of this form is also a solution.

Suppose we have some other solution $$x_1$$. Then $$T(x_1-x_p)=T(x_1)-T(x_p)=b-b=0$$. Hence, $$x_1-x_p\in\ker(T)$$, so $$x_1-x_p=x_h$$ for some $$x_h\in\ker(T)$$, and thus $$x_1=x_p+x_h$$, concluding the proof. $$\square$$

This last step actually implies that a **general solution** to $$T(x)=b$$ is an expression of the form

$$x=c_1x_1+\ldots+c_nx_n+x_p$$

where $$x_1,\ldots,x_n$$ form a basis for $$\ker(T)$$ and $$x_p$$ is any particular solution. This is because if for any solution $$x-x_p\in\ker(T)$$, then by establishing a basis $$x_1,\ldots,x_n$$ we are saying that $$x-x_p$$ can be written in the form $$c_1x_1+\ldots+c_nx_n$$.

For the derivative operator, the kernel is just the set of all constant functions. Any preimage under the operator is also just an antiderivative. And one of the important theorems of calculus is that any two antiderivatives differ by a constant, which is exactly what the preimage theorem states for this example.

## Eigenvectors

An **eigenvector** of $$T$$ is a nonzero vector $$v$$ for which $$T$$ just scales $$v$$. That is, $$T(v)=\lambda v$$ for some $$\lambda\in F$$ (note we are using $$F$$ here because this works for any field. Eventually we are going to be assuming $$F$$ is $$\mathbb{R}$$ or $$\mathbb{C}$$). $$\lambda$$ is called the **eigenvalue** of $$v$$. Note that this means that

$$(T-\lambda I)v=0\implies v\in\ker(T-\lambda I)$$

As a very mundane but useful fact, if the eigenvalue of $$v$$ is nonzero, then we can just divide both sides of $$T(v)=\lambda v$$ by $$\lambda$$ to get that $$T\left(\frac{v}{\lambda}\right)=v\implies\frac{v}{\lambda}$$ is an easy preimage of $$v$$.

\begin{equation}\label{divide}
T(v)=\lambda v\neq0\implies T\left(\frac{v}{\lambda}\right)=v
\end{equation}

Another important fact is that $$T^n(v)=\lambda^n v$$.

We call the set of all eigenvectors with eigenvalue $$\lambda$$ the **eigenspace of $$\lambda$$**. The **generalized eigenspace of $$\lambda$$** is the set of all generalized eigenvectors which we denote $$E_\lambda$$. Recall that generalized eigenvectors are all vectors $$w$$ for which

$$(T-\lambda I)^kw=0$$

for some integer $$k$$.

## Linear Operators and Polynomials

Given a polynomial $$p(x)=a_0+a_1x+\ldots+a_nx^n$$, we define

\begin{equation}
p(T)=a_0I+a_1T+\ldots+a_nT^n
\end{equation}

$$\implies p(T)x=a_0x+a_1T(x)+\ldots+a_nT^n(x)$$

Here are some insanely important facts

1. Polynomials in an operator commute. That is, for all polynomials $$p,q$$, $$p(T)q(T)=q(T)p(T)$$. This includes the specific case of first order factors $$(T-aI)(T-bI)=(T-bI)(T-aI)$$.
2. The kernel is just the eigenspace of $$0$$. That is, finding the kernel of an operator can be done by finding all eigenvectors with eigenvalue zero.
3. If $$v$$ is an eigenvector of $$T$$ with eigenvalue $$\lambda$$, then $$v$$ is also an eigenvector of $$p(T)$$ with eigenvalue $$p(\lambda)$$ (this is a very good thing to prove, and it's a very short proof).
4. $$p(T)$$ can have eigenvectors that are not eigenvectors of $$T$$. One example is that $$\begin{pmatrix}1\\0\end{pmatrix}$$ is an eigenvector of $$J=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$$, but $$\begin{pmatrix}0\\1\end{pmatrix}$$ is an eigenvector of $$(J-\lambda I)^2=\begin{pmatrix}0&0\\0&0\end{pmatrix}$$ and not of $$J$$.
5. Combining the above three points tells us that finding all eigenvectors of $$T$$ with eigenvalue $$\lambda$$ such that $$p(\lambda)=0$$ will definitely give a subset of the kernel of $$p(T)$$. However, it may not necessarily give a full basis for $$\ker(p(T))$$.

# The Differential Operator

We are going to focus in on the differential operator $$D$$ defined by

\begin{equation}
Dy=y'
\end{equation}

This is a linear operator as mentioned before. As a note, we will omit the $$I$$ when writing something like $$(D-\lambda I)$$. We will just write $$(D-\lambda)$$. Further, $$y^{(k)}=D^ky$$.

Okay, so now, let's bring everything we talked about above together:

The differential equation

\begin{equation}
a_ny^{(n)}+\ldots+a_1y'+a_0y=g(t)
\end{equation}

where the $$a_i$$'s can be complex numbers.

$$a_nD^ny+\ldots+a_1Dy+a_0y=g(t)$$

$$\left(a_nD^n+\ldots+a_1D+a_0\right)y=g(t)$$

is just the equation $$p(D)y=g(t)$$, where $$p(x)=a_nx^n+\ldots+a_1x+a_0$$. That is, we are looking for preimages of $$g(t)$$ under $$p(D)$$, and every solution will be of the form $$y=y_p+y_h$$ where $$y_p$$ is some preimage of $$g(t)$$, and $$y_h$$ is any vector in the kernel of $$p(D)$$. Note that because the kernel is always a subspace, this gives us the superposition property of homogeneous solutions for free.

i.e. If $$y_1,\ldots,y_n$$ are solutions to $$p(D)y=0$$, then so will $$c_1y_1+\ldots+c_ny_n$$.

As before, to find the **general solution**, we need a basis $$\{y_1,\ldots,y_k\}$$ of the kernel of $$p(D)$$. Then, any solution $$y$$ can be written as

$$y=y_p+c_1y_1+\ldots+c_ky_k$$

So how can we start to find a basis for the kernel? And how many vectors will be in it? Well, we know that any eigenvector of $$D$$ with eigenvalue $$\lambda$$ will be an eigenvector of $$p(D)$$ with eigenvalue $$p(\lambda)$$. So we can try to find some solutions by solving $$p(\lambda)=0$$. 

$$p(\lambda)=a_n\lambda^n+\ldots+a_1\lambda+a_0=0$$

And there we go: the characteristic polynomial is now something obvious to try, and we have yet to even *mention* exponentials.

So let $$\lambda$$ be any solution to $$p(\lambda)=0$$. Now we are looking for eigenvectors $$y$$ of $$D$$ with eigenvalue $$\lambda$$. That is, we want $$Dy=\lambda y\implies y'=\lambda y$$.

# The Most Important ODE

\begin{equation}
y'=\lambda y
\end{equation}

Yeah, I said it.

Just getting down to business solving it, we can divide both sides by $$y$$ to get help us utilize the chain rule to reverse the differentiation. However, dividing by $$y$$ eliminates the valid solution $$y=0$$, so keep that in mind.

$$\frac{y'}{y}=\lambda$$

But $$\frac{y'}{y}=\frac{d}{dt}\ln\left\lvert y \right\rvert$$. So $$\frac{d}{dt}\ln\left\lvert y \right\rvert=\lambda$$. That is,

$$\ln\left\lvert y \right\rvert=\lambda t+c\implies \left\lvert y \right\rvert=e^ce^{\lambda t}$$

Eliminating the absolute value would give us a $$\pm$$, and since we also know $$y=0$$ is a soultion, we can just say

$$\implies y=Ce^{\lambda t}\implies y\in\operatorname{span}(e^{\lambda t})$$

Remember, $$y\in\operatorname{span}(e^{\lambda t})$$ just means that $$y$$ is some linear combination of $$e^{\lambda t}$$, which just means $$y=c_1e^{\lambda t}$$.

We have demonstrated that $$y'=\lambda y\implies y\in\operatorname{span}(e^{\lambda t})$$, and I encourage you to verify that $$y'=\lambda y\impliedby y\in\operatorname{span}(e^{\lambda t})$$. However, how do we *know* this provides us with *every* solution? No, get that Picard–Lindelöf s#!% out of here (it's beautiful, yes, but not particularly intuitive). Suppose we have two solutions $$y_1,y_2$$ with $$y_1\neq0$$. Then

$$\frac{d}{dt}\left(\frac{y_2}{y_1}\right)=\frac{y_1y_2'-y_2y_1'}{y_1^2}$$

$$=\frac{y_1(\lambda y_2)-y_2(\lambda y_1)}{y_1^2}=0$$

So $$\frac{y_2}{y_1}$$ is just some constant $$C$$, which implies that $$y_2=Cy_1$$, which implies $$y_2$$ is necessarily linearly dependent on $$y_1$$. Therefore, we've shown that the solution space of $$y'=\lambda y$$ (which is just $$(D-\lambda)y=0$$: the kernel of $$(D-\lambda)$$) has dimension exactly 1, and it has a basis $$e^{\lambda t}$$. In other words,

\begin{equation}\label{kerda}
\ker(D-\lambda)=\operatorname{span}(e^{\lambda t})
\end{equation}

This demonstrates that **every eigenvector of the differential operator is an exponential function $$Ce^{\lambda t}$$**.

Now, we have answered our first question:

**Why is our guess for the solution $$e^{\lambda t}$$?**

*Because exponentials are the unique functions that can be eigenvectors of the differential operator*. Therefore, they will also be eigenvectors of the polynomial differential operator.

$$p(D)e^{\lambda t}=p(\lambda)e^{\lambda t}$$

So if $$p(\lambda)=0$$, then $$e^{\lambda t}$$ is a solution. That is why we consider

$$p(\lambda)=a_n\lambda^n+\ldots+a_1\lambda+a_0=0$$

Thus, because the kernel is a subspace closed under linear combinations, we can take a linear combination of exponentials $$e^{\lambda_1t},\ldots,e^{\lambda_nt}$$, where $$\lambda_1,\ldots,\lambda_n$$ are the roots of $$p(x)$$, to say

$$y=c_1e^{\lambda_1t}+\ldots+c_ke^{\lambda_nt}$$

will be a solution to $$p(D)y=0$$. Note: we do not say the *general* solution quite yet, as any repeated roots will make the set of these exponentials trivially linearly dependent.

We remark that \eqref{kerda} equivalently tells us that if $$q(x)$$ is a degree one polynomial, then $$\ker(q(D))$$ has a basis $$\{e^{\lambda t}\}$$ for $$\lambda$$ such that $$q(\lambda)=0$$, implying that the general solution to $$q(D)y=0$$ is $$y=Ce^{\lambda t}$$.

We actually have enough now to prove that an $$n$$th order equation has homogeneous solution space of dimension exactly $$n$$, but I want to take a detour to repeated roots first.

# Repeated Roots

i.e. why in the sweet heavenly cheese husk do we multiply by $$t$$ of all things to get our other solutions?

I brushed over this topic with a meme about reduction of order last time, but I actually have a good explanation this time.

Let's start with the simplest case. What's the solution to the differential equation

$$D^ky=0\implies y^{(k)}=0?$$

This is one of the easiest differential equations, because we can just integrate $$n$$ times to get

$$y=c_1+c_2t+\ldots+c_kt^{k-1}$$

Okay, easy enough. Now you may be thinking, "okay, when you put it like that, yeah repeated roots means repeated differentiation so that's where the $$t$$'s come from *in this case*. But what about $$(D-\lambda)^k$$?"

## Exponential Shift

Consider the derivative of $$e^{\lambda t}f(t)$$.

$$D\left(e^{\lambda t}f(t)\right)=e^{\lambda t}(f'(t)+\lambda f(t))=e^{\lambda t}(D+\lambda)f(t)$$

If you've taken enough derivatives, you may have caught on to this little shortcut. Since exponentials just get scaled by derivatives, we can just sum up the derivatives of the function multiplying it and scale by the constant appropriately. But let me tell you, this generalizes incredibly. We call this property the **exponential shift**:

\begin{equation}
De^{\lambda t}=e^{\lambda t}(D+\lambda),\quad e^{\lambda t}D=(D-\lambda)e^{\lambda t}
\end{equation}

I encourage you to prove that linearity actually guarantees that

$$
\begin{gather}
p(D)e^{\lambda t}=e^{\lambda t}p(D+\lambda)\\
e^{\lambda t}p(D)=p(D-\lambda)e^{\lambda t}
\end{gather}
$$

And this is going to make our lives *so* much easier. Let's go back to

$$(D-\lambda)y=0$$

If we multiply by $$e^{-\lambda t}$$, then we can change that pesky $$(D-\lambda)$$ into just $$D$$. That is,

$$e^{-\lambda t}(D-\lambda)y=(D-(-\lambda)-\lambda)e^{-\lambda t}y$$

$$=D(e^{-\lambda t}y)=0$$

And if $$e^{-\lambda t}y$$ is in the kernel of $$D$$, then it's just a constant. So $$e^{-\lambda t}y=C\implies y=Ce^{\lambda t}$$. 

To summarize,

\begin{equation}
e^{-\lambda t}(D-\lambda)=De^{-\lambda t}
\end{equation}

If you look at what we did closely, you'll notice this is basically just an [integrating factor](../integratingfactor/){:target="_blank"}.

The takeaway from this is: **we can leverage the exponential shift to look at the kernel of just $$D$$, which is equivalent to integration**.

## Exponential Shift Into Overdrive

Alright, so let's answer the question. What happens when we have a repeated root in $$p(x)$$ in general? Say that $$(x-\lambda)^k$$ divides $$p(x)$$. That is, $$p(x)=q(x)(x-\lambda)^k$$. Then if we multiply $$e^{-\lambda t}$$ to $$p(D)y=0$$, we get

$$e^{-\lambda t}q(D)(D-\lambda)^ky=q(D+\lambda)D^k(e^{-\lambda t}y)$$

If we let $$u=e^{-\lambda t}y$$, then we get $$q(D+\lambda)D^ku=0$$. Thus, any solution to $$D^ku=0$$ will also be a solution to $$q(D+\lambda)D^ku=0$$. And we know the solution to that is just $$c_1+c_2t+\ldots+c_kt^{k-1}$$. Therefore,

$$u=e^{-\lambda t}y=c_1+c_2t+\ldots+c_kt^{k-1}$$

$$y=e^{\lambda t}\left(c_1+c_2t+\ldots+c_kt^{k-1}\right)$$

is a solution to $$p(D)y=0$$.

And we have now answered our second question, **"Why do we multiply by $$t$$ when we have a repeated root of the characteristic polynomial?"**

*Because exponentials shift derivatives, and the kernel of repeated differentiation is a polynomial.*

What we have shown also essentially implies that every $$n$$th order differential equation of the form $$p(D)y=g(t)$$ can be solved using $$n$$ integrating factors. The first of which can be $$e^{-\lambda t}$$, where $$\lambda$$ is any root of $$p(x)$$. After doing $$n$$ integrations, we will be left with $$n$$ arbitrary constants. This is consistent with the dimension of the kernel of an $$n$$th order linear equation's solution space being dimension $$n$$, but it does not answer why the functions on each arbitrary constant will necessarily be linearly independent. That is what we intend to prove in [a later section](#second-order-two-independent-solutions).

But, this actually *does* imply something else very important: A particular solution to $$p(D)y=Be^{\lambda t}$$ is guaranteed to exist, and can be obtained by factoring $$p(D)$$, applying integrating factors, and integrating (taking all integration constants to be zero) until it is solved. However, we can actually find this particular solution directly using the exponential response formula, which is what we are going to do next.

As a final remark for this section: for constant coefficients, reduction of order *is* just the exponential shift, but more roundabout. This is because you basically insert an exponential into the equation with $$y=ve^{\lambda t}$$, which will cause things to shift. For example, if you've done reduction of order on $$y''-2ky'+k^2y=0$$, $$y=e^{kt}v$$, then you do end up with $$v''=0$$. Which is exactly what we would expect:

$$(D-k)^2e^{kt}v=e^{kt}D^2v=0\implies v''=0$$

Except we didn't have to do the product rule a bunch of times, plug in, and simplify.

## Exponential Response Formula

Alright, I'm going to prove and motivate the exponential response formula (ERF) in one line. Please try not to laugh too hard at how absurdly simple it is. By \eqref{divide} (yeah, remember *that* one?), if $$p(\lambda)\neq0$$, then

$$p(D)e^{\lambda t}=p(\lambda)e^{\lambda t}\implies p(D)\left(\frac{Be^{\lambda t}}{p(\lambda)}\right)=Be^{\lambda t}$$

so $$\frac{Be^{\lambda t}}{p(\lambda)}$$ is a particular solution. Okay, that's all folks. Seeya next time!

---

No, but really, it is that simple. We get $$\frac{Be^{\lambda t}}{p(\lambda)}$$ as a preimage of $$Be^{\lambda t}$$ because it's an eigenvector, and we can just divide by the eigenvalue when it's nonzero.

We can use some of our techniques here to get the generalized exponential response formula (GERF) as well. However, it requires a result I don't feel like proving:

**$$p^{(k)}(\lambda)=0$$ for $$0\leq k<m$$ and $$p^{(m)}(\lambda)\neq0$$ if and only if $$\lambda$$ is a root of $$p(x)$$ with multiplicity exactly $$m$$. And $$p(x)=q(x)(x-\lambda)^m$$ where $$q(\lambda)=\frac{p^{(m)}(\lambda)}{m!}\neq0$$**

Then for $$p(D)y=q(D)(D-\lambda)^my=Be^{\lambda t}$$, we can use our good ol' exponential shift with $$e^{-\lambda t}$$.

$$q(D+\lambda)D^m(e^{-\lambda t}y)=B$$

Letting $$u=D^m(e^{-\lambda t}y)$$, we get $$q(D+\lambda)u=B$$, where we know that plugging in $$x=0$$ into $$q(x+\lambda)$$ will give us something nonzero. Hence, we can use our ERF to say a particular solution is $$u_p=\frac{B}{q(0+\lambda)}=\frac{Bm!}{p^{(m)}(\lambda)}$$. That is,

$$D^m(e^{-\lambda t}y_p)=u_p=\frac{Bm!}{p^{(m)}(\lambda)}$$

Now, since we're just looking for a single particular solution, we can just integrate $$m$$ times and take all the constants to be $$0$$. And since the $$m$$th integral of $$1$$ is $$\frac{t^m}{m!}$$, we basically just multiply by $$t^m$$ and divide by $$m!$$. Thus,

\begin{equation}\label{gerf}
y_p=\frac{Bt^me^{\lambda t}}{p^{(m)}(\lambda)}
\end{equation}

and there we go. If $$p^{(k)}(\lambda)=0$$ for $$0\leq k<m$$ and $$p^{(m)}(\lambda)\neq0$$, then \eqref{gerf} is a particular solution to $$p(D)y=Be^{\lambda t}$$.

# nth Order. n Independent Solutions

We can prove that \eqref{kerda}'s implication that a first order equation has kernel of dimension exactly one actually generalizes to $$n$$th order equations by induction. \eqref{kerda} is our base case, so let us assume that an $$n$$th order equation has a kernel of exactly degree $$n$$. That is, if $$q(x)$$ is degree $$n$$, then $$\ker(q(D))$$ has a basis $$y_1,\ldots,y_n$$.

Suppose $$p(x)$$ is an $$n+1$$th degree polynomial. Then $$p(x)=(x-\lambda)q(x)$$ for some $$q(x)$$ that is degree $$n$$ (this is guaranteed by the fundamental theorem of algebra, meaning $$\lambda$$ might be complex). Hence,

$$p(D)y=0\implies (D-\lambda)q(D)y=0$$

$$\implies q(D)y\in\ker(D-\lambda)$$

\eqref{kerda} then tells us that $$q(D)y=Ce^{\lambda t}$$ for some $$C$$. Let us first consider $$q(D)y=e^{\lambda t}$$ (as we can multiply the particular solution by $$C$$ to get a solution to the preceding equation). We know we can get some particular solution $$y_p$$ to $$q(D)y=e^{\lambda t}$$ using the GERF.

That is, $$y_p$$ is a preimage of $$e^{\lambda t}$$ under $$q(D)$$, so the general solution to $$q(D)y=e^{\lambda t}$$ is $$y=c_1y_1+\ldots+c_ny_n+y_p$$, where $$y_1,\ldots,y_n$$ is a basis for $$\ker(q(D))$$ (guaranteed to be size $$n$$ by the inductive hypothesis) by the preimage theorem.

But, if $$y_p$$ is a preimage of $$e^{\lambda t}$$ under $$q(D)$$, then $$Cy_p$$ is a preimage of $$Ce^{\lambda t}$$ under $$q(D)$$. Hence, the general solution to $$q(D)y=Ce^{\lambda t}$$ is

$$y=c_1y_1+\ldots+c_ny_n+Cy_p$$

We claim that $$y$$ is a solution to $$p(D)y=0$$. If we take the image of $$y$$ under $$q(D)$$, we get $$Ce^{\lambda t}$$ as we already defined $$y_1,\ldots,y_n$$ to be a basis for its kernel and $$y_p$$ to be a preimage of $$e^{\lambda t}$$. That is,

$$q(D)\left(c_1y_1+\ldots+c_ny_n+Cy_p\right)=Ce^{\lambda t}$$

But if we then take the image of the result under $$(D-\lambda)$$, we will get zero by \eqref{kerda}. Hence, $$y$$ is in the kernel of $$(D-\lambda)\circ q(D)=(D-\lambda)q(D)=p(D)$$.

Now, $$y_p$$ cannot be linearly dependent with $$y_1,\ldots,y_n$$, because then it would be in the kernel of $$q(D)$$ and thus could not be a preimage of $$e^{\lambda t}\neq0$$ under $$q(D)$$. Hence, $$\left\{y_1,\ldots,y_n,y_p\right\}$$ form a set of $$n+1$$ linearly independent vectors in $$\ker(p(D))$$, making its dimension at least $$n+1$$. We now need to show that there cannot be another linearly independent solution.

Suppose that $$y_{n+2}$$ is also a solution to $$p(D)y=0$$ which is linearly independent with $$\{y_1,\ldots,y_n,y_p\}$$. $$y_{n+2}$$ can't be in the kernel of $$q(D)$$, because then it would be linearly dependent with $$y_1,\ldots,y_n$$. So 

$$q(D)y_{n+2}\neq0\implies q(D)y_{n+2}\in\ker(D-\lambda)$$

That is, $$q(D)y_{n+2}=c_{n+2}e^{\lambda t}$$. But, like before, we know that $$c_{n+2}y_p$$ will be a preimage of $$c_{n+2}e^{\lambda t}$$ under $$q(D)$$, so by the preimage theorem $$y_{n+2}=c_{n+2}y_p+y_h$$ where $$y_h\in\ker(q(D))$$. But, since $$y_h=d_1y_1+\ldots+d_ny_n$$ for some constants $$d_i$$, that means $$y_{n+2}=c_{n+2}y_p+d_1y_1+\ldots+d_ny_n$$, contradicting that $$y_{n+2}$$ is linearly independent from $$\{y_1,\ldots,y_n,y_p\}$$. Therefore, the dimension of $$\ker(p(D))$$ is exactly $$n+1$$!

This answers our third question, **"Why does an $$n$$th order equation have exactly $$n$$ linearly independent homogeneous solutions?"**

Because a homogeneous $$n$$th order equation is equivalent to a nonhomogeneous $$(n-1)$$th order equation, for which the particular solution is necessarily linearly independent from the homogeneous solution in the dimension $$n-1$$ kernel. And the particular solution for the reduced equation will then be a homogeneous solution for the $$n$$th order equation. And by the preimage theorem, any other solution will be linearly dependent on the general solution.

As an unfortunate remark: this argument does not work for every type of differential equation. You do generally need more heavy duty techniques like reduction to a first order system of differential equations to prove this when the coefficients are not constant. Still, I like this very concrete proof for this very special case.

## A remark on undetermined coefficients

You can also utilize the exponential shift to more easily solve for more difficult particular solutions. If you have something like

$$p(D)y=q(t)e^{\alpha t}$$

where $$q(t)$$ is some polynomial, then you can multiply by $$e^{-\alpha t}$$ to make the RHS a simple polynomial. This will shift the equation to

$$p(D+\alpha)e^{-\alpha t}y=q(t)$$

In general, it's slightly easier to solve this equation since your "guess" for a particular solution is just also a polynomial, removing the need to do product rules. Also, you can use [synthetic division](../synthetictaylor/){:target="_blank"} to more easily calculate the coefficients of $$p(D+\alpha)$$ without having to expand out the expressions and collect like terms. This is arguably a waste of time, and doesn't cut down the computation time *too* much overall. I like to do it though.

## Complex Stuff

You may have noticed that I didn't really specify what all the constants where in any of what I did. That's because this general theory works for *all* polynomials, even complex ones. It's only the very specific real polynomial case where you *can* always convert complex roots to sines and cosines. In most textbooks, they present this stuff in operator notation, but I'll just speedrun through it for completion's sake.

If $$p(x)$$ is a real polynomial (it has real coefficients, not complex ones), then $$p(D)$$ is an operator that maps real functions to real functions. That is, if $$f(x)$$ is a real valued function, then $$p(D)f(x)$$ is also always real valued.

Thus, if $$F(x)=u(x)+iv(x)$$, then by linearity of linear transformations

$$p(D)F(x)=p(D)u(x)+ip(D)v(x)$$

So the real part of $$p(D)F(x)$$ is $$p(D)$$ applied to the real part of $$F(x)$$, and similarly with the imaginary part.

Hence, if $$p(D)F(x)=0$$, then both the real and imaginary parts must be zero, so $$p(D)u(x)=p(D)v(x)=0$$. That is, the real and imaginary parts of any complex element of the kernel are also individually in the kernel.

It follows from [Euler's Formula](../eulersformula/){:target="_blank"} that if $$\alpha=a+bi$$ is a root of $$p(x)$$, then

$$e^{(a+bi)t}=e^{at}\left(\cos(bt)+i\sin(bt)\right)$$

will be a solution, so we can take the real and imaginary parts blah blah blah

$$y=e^{at}\left(c_1\cos(bt)+c_2\sin(bt)\right)$$

will be a solution.

So, similar with repeated roots, the case of

$$y=(c_1+\ldots+c_kt^{k-1})e^{\alpha t}$$

just means two individual sets of solutions

$$
\begin{align*}
y_1=(c_1+\ldots+c_kt^{k-1})e^{at}\cos(bt)\\
y_2=(d_1+\ldots+d_kt^{k-1})e^{at}\sin(bt)\\
\end{align*}
$$

It may seem like we're doubling the number of solutions, but nah. This is because if $$p(x)$$ is real valued, then any complex root will also have a corresponding complex conjugate root. And, since Euler's formula basically just makes the conjugate flip the sign of the imaginary part, the two solutions taken from the conjugate solution will be linearly dependent on the two solutions obtained from the original complex root. That is, normally we have

$$y=(c_1+\ldots+c_kt^{k-1})e^{\alpha t}+(d_1+\ldots+d_kt^{k-1})e^{\overline\alpha t}$$

so we're still left with $$2k$$ solutions in the end.

---

## Final Thoughts

I love this perspective. The ideas of "exponentials would be an expected guess", "to get the other solutions, multiply one solution by an arbitrary function $$v(t)$$", or "just reduce the $$n$$th order equation down to a system of first order equations" would be mildly intuitive, but only in retrospect. As someone who questions a lot, and wants to know *why* something is true, the answers felt very contrived.

But once we change from a differential equation to a linear operator, suddenly everything is a lot simpler (at least to me). The progression from first order to $$n$$th order is smooth and things just work out exactly the way you would expect them to.

- Exponentials are an expected guess because they are eigenvectors of the differential operator.
- To get the other solutions, we do an exponential shift, which effectively has us multiply by our first given solution.
- The dimension is $$n$$ because each linear differential factor increases the dimension of the kernel by one.

Granted, these justifications *only* work for constant coefficients. And, in general, reduction of order and reduction to a system of first order equations is necessary to generalize these ideas. But I greatly relish in the idea that we can make a much more elementary argument for this most special of cases that doesn't end up relying on Picard–Lindelöf.

But this is coming from someone who thinks a lot about these subjects, so perhaps it isn't much easier for you. Especially if you don't know any linear algebra (and if you got here without knowing linear algebra, uh... why? thank you for reading, but why?) I hope this was helpful, though.

Also, this is a heavily condensed version of a chapter from a Linear Algebra + Differential Equations textbook I'm working on in my spare time (for which I have almost none now that I am in a PhD program). I hope you liked it, and maybe you'll want to check out the textbook when it's done (ETA: probably never). Alright, thanks for reading.

[hyperlink](https://youtu.be/Tptx8boeGhE?si=1G60x2ZMJgUPC8Gr){:target="_blank"}
