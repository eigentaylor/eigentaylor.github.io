---
layout: page
title: Intro To Solving Systems of First Order Differential Equations
date: 2021-07-18 0
description: An attempt at an intuitive derivation
comments: true
importance: 4
category: systems of differential equations
---

Because this topic is usually taught pretty late in a differential equations course and requires some linear algebra, this post is aimed towards people who either already have some differential equations and/or linear algebra experience.

If you don't know much linear algebra, I would highly recommend looking into constant coefficient linear differential equations first before diving into this topic, since in many ways this is a continuation of/step up from that.

On the other hand, if you are relatively comfortable with linear algebra and basic calculus but don't know a lot about differential equations, this may be an easier differential equations topic to get your feet wet with.

---

The goal here is to make the solving of the following type of differential equation intuitive:

\begin{equation} \label{1}
\vec{x}'(t)=A\vec{x}(t)
\end{equation}

This is a system of linear first-order homogeneous differential equations. Here $$\vec{x}(t)$$ is a column vector of functions, and $$A$$ is a square matrix. Before we tackle that, however, let's examine the one-dimensional case, where $$A$$ is just a number $$a$$:

\begin{equation}\label{1d}
x'(t)=ax(t)
\end{equation}

This is what I would consider to be the most fundamental and important differential equation there is. Partly because if you have any experience with taking derivatives, you may just be able to figure out the solution.

The way that I would look at this differential equation \eqref{1d} is the question

"What function has the property that when I take the derivative, it is exactly the same as just multiplying by the constant $$a$$?"

If you are unsure, maybe this specific example where $$a=1$$ may be more familiar:

\begin{equation}\label{et}
f(t)=f'(t)
\end{equation}

Hopefully the function that comes to mind is $$f(t)=e^t$$. And now maybe the answer to \eqref{1d} is a little more obvious. The chain rule tells us that if $$\frac{d}{dt}e^t=e^t$$, then $$\frac{d}{dt}e^{at}=ae^{at}$$. So maybe that's just the solution? Well... yes but there are more.

Notice that $$\frac{d}{dt}2e^t=2e^t$$ also satisfies \eqref{et}. And in fact, no matter what the constant $$C$$ is, $$f(t)=Ce^t$$ will have the property that it it equal to its own derivative, making it a solution to \eqref{et}.

Similarly, the general solution to \eqref{1d} is $$x(t)=Ce^{at}$$. However, to be consistent with where we're going, we are going to write it as $$x(t)=e^{at}C$$, with the constant on the right side.

So perhaps you're looking at

$$\vec{x}'(t)=A\vec{x}(t)$$

and wondering if the solution is something like $$\vec{x}(t)=e^{At}$$. And actually, it kind of is! One general solution is in fact $$\vec{x}(t)=e^{At}\vec{C}$$. Here $$\vec{C}$$ is a column vector of arbitrary constants. The only problem is that calculating $$e^{At}$$ is usually *really* hard. And the work required to do it is actually the same work you'd do solving the system the normal way.

So instead of solving these systems by calculating matrix exponentials, we need to talk about eigenvectors.

### Wait, what the heck is an eigenvector?

Linear algebra is usually not a prerequisite for differential equations, so not everyone taking a DE class knows what an eigenvector is. However, the concept is not as new or unfamiliar as it sounds. An eigenvector $$\vec{v}$$ of a matrix $$A$$ with eigenvalue $$\lambda$$ is a nonzero vector which satisfies the equation

\begin{equation}
A\vec{v}=\lambda \vec{v}
\end{equation}

This is really just asking the question

"What vector has the property that when I multiply by the matrix $$A$$, it is exactly the same as just multiplying by the constant $$\lambda$$?"

That question sounds a bit familiar. But the answer to this question really depends on the matrix $$A$$. And usually, there is more than one answer. A matrix with $$n$$ rows and $$n$$ columns can have up to $$n$$ linearly independent eigenvectors.

### But how do we find eigenvectors?

Well if we start with the equation $$A\vec{v}=\lambda \vec{v}$$, then we can move everything to one side of the equation.

$$A\vec{v}-\lambda\vec{v}=0$$

By writing out $$\lambda\vec{v}$$ as $$\lambda I\vec{v}$$, where $$I$$ is the identity matrix which acts like the number $$1$$,

$$I_2=\begin{bmatrix}1&0\\0&1\end{bmatrix},\;I_3=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix},\ldots,
I_n=\begin{bmatrix}1&0&0&\dots&0\\0&1&0&\dots&0\\0&0&1&\dots&0\\\vdots&\vdots&\vdots&\ddots&\vdots\\0&0&0&\dots&1\end{bmatrix}
$$

we can factor out the vector like so,

$$(A-\lambda I)\vec{v}=0$$

Now in linear algebra, there is something known as the "Equivalence theorem", which give us about 25-30 different equivalent statements we can make about square matrices if they are "invertible" or not. For our purposes, we just need these two,

1. A square matrix $$X$$ is invertible if and only if $$\det(X)\neq 0$$.

2. The system $$X\vec{v}=0$$ has only the trivial solution ($$\vec{v}=0$$) if and only if $$X$$ is invertible.

Combining these,

The system $$X\vec{v}=0$$ has only the trivial solution ($$v=0$$) if and only if $$\det(X)\neq 0$$.

Which also tells us

The system $$X\vec{v}=0$$ has a nontrivial solution ($$\vec{v}\neq0$$) if and only if $$\det(X)=0$$.

What does this mean? Well, if for some particular $$\lambda$$ we have $$\det(A-\lambda I)\neq0$$, then the only vector $$\vec{v}$$ that satisfies

$$A\vec{v}=\lambda\vec{v}$$

is $$\vec{v}=0$$. If $$\vec{v}=0$$ then our only solution of the form $$\vec{v}e^{\lambda t}$$ is $$0e^{\lambda t}=0$$ which is not a solution we care about.

All this to say, we need $$\det(A-\lambda I)=0$$ for there to be an eigenvector with eigenvalue $$\lambda$$. We call

$$\det(A-\lambda I)=0$$

the characteristic polynomial. And yes! This characteristic polynomial is very closely related to the characteristic polynomial you are familiar with when discussing linear constant coefficient differential equations. The roots of the characteristic equations are the eigenvalues of the matrix.

### Solving the system of differential equations

We've discussed two questions that the topics of eigenvectors, $$A\vec{v}=\lambda\vec{v}$$, and differential equations such as $$x'(t)=\lambda x(t)$$ essentially ask of us.

1\. "What **vector** has the property that when I **multiply by the matrix** $$A$$, it is exactly the same as just multiplying by the constant $$\lambda$$?"

2\. "What **function** has the property that when I **take the derivative**, it is exactly the same as just multiplying by the constant $$\lambda$$?"

As a reminder, the answer to the second question was $$ce^{\lambda t}$$, since $$\frac{d}{dt}(ce^{\lambda t})=\lambda(ce^{\lambda t})$$. Or to write it another way,

$$(ce^{\lambda t})'=\lambda(ce^{\lambda t})$$

The question that our system $$\vec{x}'(t)=A\vec{x}(t)$$ asks is

3\. "What **vector function** has the property that when I **take the derivative**, it is exactly the same as just **multiplying by the matrix** $$A$$?"

Which is just a mix of the other two questions.

So we have two mathematical objects, a type of **vector** and a **function** with two similar properties.

$$\begin{align*}
A\vec{v}&=\lambda\vec{v}\\
\frac{d}{dt}e^{\lambda t}&=\lambda e^{\lambda t}\\
\end{align*}$$

What if we just combine them directly? Consider the **vector function** $$\vec{x}(t)=\vec{v}e^{\lambda t}$$.

$$\begin{align*}
\frac{d}{dt}\vec{x}(t)&=\frac{d}{dt}(\vec{v}e^{\lambda t})&A\vec{x}(t)&=A(\vec{v}e^{\lambda t})&\\
\vec{x}'(t)&=\left(\frac{d}{dt}e^{\lambda t}\right)\vec{v}&A\vec{x}(t)&=(A\vec{v})e^{\lambda t}&\\
\vec{x}'(t)&=(\lambda e^{\lambda t})\vec{v}&A\vec{x}(t)&=(\lambda\vec{v})e^{\lambda t}&\\
\vec{x}'(t)&=\lambda(\vec{v}e^{\lambda t})&A\vec{x}(t)&=\lambda(\vec{v}e^{\lambda t})&\\
\vec{x}'(t)&=\lambda \vec{x}(t)&A\vec{x}(t)&=\lambda \vec{x}(t)&\\
\end{align*}$$

$$\vec{x}'(t)=A\vec{x}(t)$$

So there it is. The solutions to these systems are obtained by multiplying an eigenvector of the matrix by an exponential with the eigenvalue in its power.

And just like with linear differential equations you may be more familiar with solving, the general solution is a linear combination of each of your linearly independent solutions.

So to summarize:

1. Find the roots of the characteristic polynomial $$\det(A-\lambda I)=0$$, $$\lambda=\lambda_1,\lambda_2,\ldots,\lambda_n$$

2. Solve the systems $$(A-\lambda_i I)\vec{v}_i=0$$ to get your eigenvectors

3. The general solution will be $$\vec{x}(t)=c_1\vec{v}_1e^{\lambda_1 t}+\ldots+c_n\vec{v}_ne^{\lambda_n t}$$

Now there are some hiccups that you may run into. One being when an eigenvalue can be complex, and another that you not get $$n$$ total eigenvectors. But this should hopefully be enough to get you started on most of the problems you are likely to encounter in an intro class.
