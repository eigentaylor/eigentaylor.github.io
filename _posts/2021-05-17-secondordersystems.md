---
layout: page
title: Constructing Integer 2x2 Second Order Systems of Differential Equations with Integer Solutions
date: 2021-05-17
description: It's a lot messier.
comments: true
importance: 3
categories: works-in-progress
---

This post is based on the foundation of the [first order case](../firstordersystems), naturally. Though it is quite likely that there are other ways to do this, I'm going to focus on a method I found which gives quite a bit of control over the solutions. I feel, though, that I have only scratched the surface of this topic, and I think it's possible to nail down the science of it more than I have here. For most things in this post, there is likely more that could be said.

The good news is that when discussing $$n\times n$$ second order systems such as

$$x''=Px'+Qx$$

we are still only really talking about a first order system. We can reduce any second order system to a first order by adding $$n$$  more variables. So if $$x=(x_1,\ldots,x_n)$$ then we let $$y=(x_1,\ldots,x_n,x_1',\ldots,x_n')$$. Which gives us the system

$$\begin{equation} \label{reduction}
y'=\begin{bmatrix}
0&I\\Q&P
\end{bmatrix} y
\end{equation}$$

So theoretically, the solution to the second order system (and the initial value problem) is

$$\begin{equation} \label{exp1}
x=\begin{bmatrix}
I_n&0
\end{bmatrix}
\exp\left(\begin{bmatrix}
0&I\\Q&P
\end{bmatrix}t\right)
\begin{bmatrix}
x(0)\\x'(0)
\end{bmatrix}
\end{equation}$$

This tells us that the solutions to our $$2\times 2$$ second order system can have all the behaviors of a $$4\times 4$$ first order system. So we can have an eigenvalue repeated 4 times and get a $$t^3$$ term in our homogeneous solutions, and we can have up to two complex conjugate pairs of eigenvalues.

However, attempting to manipulate \eqref{reduction} or \eqref{exp1} to give us desired solutions is *highly* impractical, even if we started with a $$2\times 2$$ system. I don't frankly believe it is possible. This was my first approach to this problem and it felt like a dead end. That said, just because I couldn't do it doesn't mean it's impossible. Either way, I took a different approach to the problem.

When constructing simple second order constant coefficient differential equations like

$$y''+py'+qy=0$$

with nice solutions, it's *extremely* easy. All we need to do is find a quadratic polynomial which has the desired roots $$s_1,s_2\in\mathbb{C}$$. So starting with the characteristic polynomial $$(s-s_1)(s-s_2)=0$$ gives us

$$y''-(s_1+s_2)y'+s_1s_2y=0$$

We get our 3 different solution types based on if $$s_1\neq s_2$$, $$s_1=s_2$$, or if $$s_1,s_2$$ are complex pair of conjugates. Easy.

So what if I started in a similar place. Instead of $$s-s_i$$, starting with $$sI-S_i$$ where $$S_i\in\mathbb{Z}^{n\times n}$$? That would give us

$$x''-(S_1+S_2)x'+S_1S_2=0$$

I decided to start here and see how I could manipulate the $$S_i$$ matrices to give me a system with desired solutions.

## Theorem 1:

If $$x$$ is a solution to the system of differential equations

$$\begin{equation} \label{1st}
x'=Ax
\end{equation}$$

then for any matrix of proper size, $$B$$, $$x$$ is also a solution to the system of differential equations

$$\begin{equation} \label{2nd}
x''=(A+B)x'-BAx
\end{equation}$$

Proof:

Any solution to the system \eqref{1st} can be written as

$$\begin{equation} 
x=e^{At}c
\end{equation}$$

From this, we can substitute $$x'=Ae^{At}c$$ into the differential equation and verify that we get $$x''=A^2e^{At}c$$.

$$\begin{gather*}
(A+B)Ae^{At}c-BAe^{At}c\\
=A^2e^{At}c+BAe^{At}c-BAe^{At}c\\
=A^2e^{At}c\quad\blacksquare\\
\end{gather*}$$

Using this construction for an $$n\times n$$ system \eqref{2nd}, we can guarantee $$n$$ of the $$2n$$ solutions to be nice (assuming the solutions to \eqref{1st} were nice to begin with). And using our knowledge of constructing very nice $$2\times 2$$ system, that means we can guarantee two of our solutions to be just about anything.

Now you may be hoping that $$e^{Bt}c$$ would give us our other solutions, but it can be verified that this is only true if $$A$$ and $$B$$ commute. It's extremely unlikely (I'm going to conjecture probability zero) that any two given square matrices commute. But we can cheat a bit.

# Commuting $$A$$ and $$B$$

Fact: If $$A=PJ_1P^{-1}$$ and $$B=PJ_2P^{-1}$$, where $$J_1$$ and $$J_2$$ have the same Jordan block formation, then $$A$$ and $$B$$ commute. This is pretty obvious when $$A$$ and $$B$$ are diagonalizable since diagonal matrices definitely commute. But in fact, all matrices in Jordan normal form with the same form of Jordan blocks commute. 

## Theorem 2:

If the conjugation of a given real $$2\times2$$ matrix $$P$$ puts real matrices $$A$$ and $$B$$ into Jordan normal form of the same type -- That is to say $$A$$ and $$B$$ are both diagonalizable, both have a defective eigenvalue, or both have complex conjugate eigenvalues -- then $$A$$ and $$B$$ commute.

The downside of using this to make a nice \eqref{2nd}, is that the solution can look kind of the same since the system really only has two eigenvectors total. If the eigenvalues are not the same, a single eigenvector will just have two eigenvalues. Meaning two solutions are given by $$(c_1e^{\lambda_1t}+c_2e^{\lambda_2t})v$$ for a single eigenvector. If they are the same, then it's just the solution for regular linear second order systems: multiply the first solution $$x=x_1$$ by $$t$$, $$x_2=tx_1$$. In fact, if $$B=A$$, then $$te^{At}c$$ will give the other two solutions to \eqref{2nd}.

# Noncommuting $$A$$ and $$B$$

## Real Distinct Eigenvalues

Knowing where \eqref{2nd} comes from, we know the characteristic equation of the whole system is the product of the two characteristic equations.

$$\begin{equation} \label{char}
\det\left((sI-B)(sI-A)\right)=0
\end{equation}$$

And indeed, one can verify that supposing a solution to \eqref{2nd} is $$x=e^{st}v$$ does yield

$$\begin{equation}
(sI-B)(sI-A)v=0
\end{equation}$$

This also confirms that if $$v$$ is an eigenvector with eigenvalue $$s$$ of $$A$$, the result is zero regardless of $$B$$. The other upside of starting with \eqref{char} means that as long as $$A$$ and $$B$$ have integer eigenvalues, the eigenvalues of \eqref{2nd} will be those same integers.

Supposing that $$s_i$$ is an eigenvalue of $$B$$ and not $$A$$, that means $$\det(s_iI-A)\neq0$$, then assuming a solution $$x_i=v_ie^{s_it}$$ we can let $$v_i=(s_iI-A)^{-1}u_i$$, leading to

$$\begin{equation}
(s_iI-B)u_i=0
\end{equation}$$

So $$u_i$$ is just the eigenvector of $$B$$ with eigenvalue $$s_i$$. And that tells us that if we want a specific $$v_i$$ to be a solution, $$x_i=v_ie^{s_it}$$, then just make sure $$B$$ has an eigenvector $$u_i=(s_iI-A)v_i$$ with eigenvalue $$s_i$$. 

The problem here is that it's very hard to predict what $$(s_iI-A)v_i$$ will be. Starting with a given $$A$$, $$s_i$$, and $$v_i$$ can lead to $$u_i$$ being extremely large and not very pretty. More importantly, it can make the determinant of the modal matrix for $$B$$ very large, or at least hard to control. This causes the coefficient matrices $$A+B,-BA$$ to be large too, usually. Not to mention the computations are relatively laborious.

## Desired Eigenvectors

One solution to this problem if you insist on a having four specific vectors be parts of the solution of the system is simply choose $$s_2$$ to have the correct modulus so that $$B$$ is an integer matrix by adding a multiple of the determinant to $$s_1$$.

For example, suppose that $$A=\begin{bmatrix}-2&1\\1&-2\end{bmatrix}$$, which has very nice eigenvalues and eigenvectors. The general solution to \eqref{1st} and two solutions to \eqref{2nd} using this matrix are $$x=c_1\begin{bmatrix}1\\1\end{bmatrix}e^{-t}+c_2\begin{bmatrix}1\\-1\end{bmatrix}e^{-3t}$$. Now say I really want the other two solutions to be of the form $$x=k_1\begin{bmatrix}2\\1\end{bmatrix}e^{2t}+k_2\begin{bmatrix}1\\2\end{bmatrix}e^{s_2t}$$ and let's suppose I don't care at all what $$s_2$$ is.

Computing $$(2I-A)\begin{bmatrix}2\\1\end{bmatrix}$$ gives $$\begin{bmatrix}7\\2\end{bmatrix}$$, and $$(s_2I-A)\begin{bmatrix}1\\2\end{bmatrix}=\begin{bmatrix}s_2\\2s_2+3\end{bmatrix}$$. So now we need $$s_2\equiv2\pmod{\det P}$$ where $$P=\begin{bmatrix}7&s_2\\2&2s_2+3\end{bmatrix}$$.

$$\det P=3(4s_2+7)$$ so we need $$s_2-2$$ to be divisible by that. But... that's clearly not going to work. So is this eigenvector a bust? Maybe not. If we suppose $$s_2$$ is divisible by 3, $$s_2=3k$$, we can reduce the eigenvector to $$\begin{bmatrix}k\\2k+1\end{bmatrix}$$. The new determinant is $$12k+7$$. So we need $$3k-2$$ to be divisible by that. There does happen to be exactly one value that satisfies this when $$k=-1$$. Making $$s_2=-3$$ the only eigenvalue for $$B$$ which that will work, with eigenvector $$(1,1)$$ (once $$(-3,-3)$$ simplified). 

Then we may construct $$B$$.

$$\begin{equation} 
B=\begin{bmatrix}7&1\\2&1\end{bmatrix}\begin{bmatrix}2&0\\0&-3\end{bmatrix}\begin{bmatrix}7&1\\2&1\end{bmatrix}^{-1}=\begin{bmatrix}4&-7\\2&-5\end{bmatrix}
\end{equation}$$

Substituting into \eqref{2nd} give us our system

$$\begin{equation} 
x''=\begin{bmatrix}2&-6\\3&-7\end{bmatrix}x'+\begin{bmatrix}15&-18\\9&-12\end{bmatrix}x
\end{equation}$$

which indeed does have the solution

$$\begin{equation} 
x=c_1\begin{bmatrix}1\\1\end{bmatrix}e^{-t}+c_2\begin{bmatrix}1\\-1\end{bmatrix}e^{-3t}+c_3\begin{bmatrix}2\\1\end{bmatrix}e^{2t}+c_4\begin{bmatrix}1\\2\end{bmatrix}e^{-3t}
\end{equation}$$

The problem with this method of doing things is that our knowledge of how to make nice integer $$2\times 2$$ matrices is much harder to apply because the eigenvectors of $$B$$ and the eigenvalues of $$B$$ are intertwined (in that the entries of the eigenvectors include the eigenvalues). I suspect that this case just happened to luckily have an integer solution for the eigenvalue, and I don't think that will always be the case. The problem of simply finding the eigenvalue was itself a difficult task specific to each set of eigenvectors.

The other option is to choose just one vector you want to be a solution, and then just arbitrarily make the second column of the modal matrix for $$B$$ such that the eigenvalues are congruent to its determinant. This does mean that one vectors of the solution may be slightly ugly, but it's certainly better than nothing. One upside is that you won't know one solution ahead of time, I suppose.

I do have an alternate method for generating these problems with some similar upsides that I will detail later.

## Repeated Solutions

As mentioned earlier, if $$A$$ and $$B$$ commute _and_ have the same eigenvalue for one of their shared eigenvectors, then two solutions are given by

$$\begin{equation} \label{rep}
x=(c_1+c_2t)v_ie^{s_1t}
\end{equation}$$

This is not exclusive to commuting $$A$$ and $$B$$, however. The condition of sharing an eigenvector with the same eigenvalue is enough to guarantee a solution of the form \eqref{rep}. As we know these $$2\times 2$$ second order systems are $$4\times 4$$ first order systems in disguise, we know you can get solutions with up to $$t^3$$ terms by having $$A$$ and $$B$$ be defective with the same eigenvalue and having $$(s_1I-B)(s_1I-A)\neq 0$$.

There are so many cases to consider that rigorously defining and proving the behavior of each one is not worth the time for a post on a blog that nobody reads. So... yeah, sorry. Investigate it yourself and leave a comment with a [mathb.in](http://mathb.in/) link if you have a proof or find anything interesting. I would love to read it.

## Another Way to Generate Systems

There are a lot more variables in second order systems in terms of tuning the solutions. The eigenvectors of $$B$$ have an implicit relationship with $$A$$ and the solution vectors which is not direct. So instead of trying to control the **B**eastly matrix $$B$$, we could instead choose a simpler matrix with desired eigenvalues and general behavior. And what simpler matrix is there than a Jordan matrix?

$$\begin{equation} 
J_r=\begin{bmatrix}s_1&0\\0&s_2\end{bmatrix}\quad J_d=\begin{bmatrix}s_1&1\\0&s_1\end{bmatrix}\quad J_c=\begin{bmatrix}s_1&s_2\\-s_2&s_1\end{bmatrix}
\end{equation}$$

Corresponding to the three different cases: **r**eal, **d**efective, and **c**omplex conjugate eigenvalues.

Not only are Jordan matrices simple, changing their eigenvalues is as simple as changing the entries. This way we don't even need to worry about making sure the system will have integer entries. If $$A$$ is an integer matrix with all integer eigenvalues (IMIE) and the entries (eigenvalues) of $$J$$ are integers, then the coefficient matrices in \eqref{2nd} will also be integer matrices, and the system will have integer eigenvalues. This along with $$A$$ having integer eigenvectors also guarantees the system as a whole will have integer eigenvectors.

The eigenvectors of Jordan matrices are just the standard basis vectors (denoted by $$e_i$$) (or in the complex case a simple complex relationship $$(1,i)$$). Making the solution vectors scalar multiples of

$$\begin{equation} 
v_i=(s_iI-A)^{adj}e_i
\end{equation}$$

or the columns of the adjoint of $$s_iI-A$$ (we use the adjoint to ensure $$v_i\in\mathbb{Z}^2$$ since we can always scale eigenvectors). And since $$2\times2$$ adjoints are just rearrangements of the entries, the simpler and nicer looking $$A$$ is, and the smaller $$s_i$$ is, the nicer and smaller $$v_i$$ will be. As a bonus, solving this problem is slightly more fun since you don't know _all_ the solutions ahead of time.

$$\begin{equation}
x''=(A+J)x'-JAx
\end{equation}$$

### Another Easy Matrix Choice

Another type of matrix which gives easy controls over the eigenvalues is the one obtained by reducing a second order linear differential equation into a first order system of differential equations. So whereas in the Jordan form you use the eigenvalue(s) directly, here you use the coefficients of the characteristic polynomial.

As mentioned before, it's easy to generate second order linear differential equations by starting with the characteristic polynomial. If you have a second order linear differential equation with the desired roots and behavior

$$y''+py'+qy=0$$

Then by defining the vector function $$x(t)=(y(t),y'(t))$$, the above differential equation becomes equivalent to

$$x'=\begin{bmatrix}0&1\\-q&-p\end{bmatrix}x$$

Which is exactly the $$1\times 1$$ case of \eqref{reduction}.

We also already know what $$p$$ and $$q$$ have to be, as we determined earlier. So the alternative matrix is

$$\begin{equation}
\begin{bmatrix}0&1\\-s_1s_2&s_1+s_2\end{bmatrix}
\end{equation}$$

I call these reduction matrices.

This is an easy way to generate matrices with defective or complex eigenvalues that aren't too simple, as a Jordan normal form is. The eigenvectors are a bit predictable, however. All being of the form $$(1,s_i)$$. But it's absolutely better than nothing.

Personally, my goto choices for $$A$$ and $$B$$ are to have $$B$$ be a Jordan matrix, and $$A$$ be a reduction matrix. It's a very reliable way to generate problems which aren't too simple, and have exactly the behavior I desire.
