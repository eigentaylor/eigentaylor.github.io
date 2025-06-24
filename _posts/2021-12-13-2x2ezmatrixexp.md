---
layout: distill
title: Matrix Exponential Formulas for 2x2 Matrices
date: 2021-12-13
description: Who needs eigenvectors?
comments: true
importance: 1
categories: differential-equations
tags: best matrix-exponentials systems-of-differential-equations
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Formulas
  - name: Proofs
    subsections:
      - name: One Defective Eigenvalue
      - name: Complex Conjugate Eigenvalues
      - name: Zero trace and negative determinant
      - name: One Nondefective Eigenvalue
      - name: Rank 1 matrix
      - name: Distinct Eigenvalues
  - name: Another approach
  - name: Applications
  - name: Closing Remarks
---

**WARNING**: If you are in a differential equations class right now, turn back. This is black magic that your professor _will not_ want you to memorize or use on their tests. These are just cool and/or for the convenience of those who evaluate a lot of matrix exponentials, as I do.

# Formulas

Let $$A$$ be a $$2\times 2$$ matrix.

- If $$A$$ has one defective eigenvalue $$\lambda$$, then

$$\begin{equation} \label{defect}
e^{At}=e^{\lambda t}\left(I+t(A-\lambda I)\right)
\end{equation}$$

- If $$A$$ is real and has complex conjugate eigenvalues $$a \pm bi$$, then

$$\begin{equation}\label{complex1}
e^{At}=e^{a  t}\left(\cos(b  t)I+\frac{\sin(b  t)}{b }(A-a  I)\right)
\end{equation}$$

$$\begin{equation} \label{complex2}
e^{At}=\frac{e^{at}}{b}\bigg(b\cos(b  t)I+\sin(b  t)(A-a  I)\bigg)
\end{equation}$$

- If $$A$$ has a real determinant, $$\operatorname{tr}(A)=0$$, and $$\det(A)<0$$, then an eigenvalue of $$A$$ is $$\lambda=\sqrt{-\det(A)}$$, and

$$\begin{equation} \label{0trace}
e^{At}=\cosh(\lambda t)I+\frac{\sinh(\lambda t)}{\lambda}A
\end{equation}$$

- If $$A$$ is singular and has a nonzero trace,

$$\begin{equation}\label{formsingular}
e^{At}=\frac{e^{\operatorname{tr}(A)t}A-(A-\operatorname{tr}(A)I)}{\operatorname{tr}(A)}
\end{equation}$$

$$\begin{equation}\label{formsingularb}
e^{At}=I+\frac{e^{\operatorname{tr}(A)t}-1}{\operatorname{tr}(A)}A
\end{equation}$$

- If $$A$$ has two distinct eigenvalues $$\lambda_1,\lambda_2$$, then

$$\begin{equation} \label{distinct}
e^{At}=\frac{e^{\lambda_2t}(A-\lambda_1I)-e^{\lambda_1t}(A-\lambda_2I)}{\lambda_2-\lambda_1}
\end{equation}$$

$$\begin{equation} \label{distinct2}
e^{At}=\frac{\lambda_2e^{\lambda_1t}-\lambda_1e^{\lambda_2t}}{\lambda_2-\lambda_1}I +
\frac{e^{\lambda_2t}-e^{\lambda_1t}}{\lambda_2-\lambda_1}A
\end{equation}$$

And if $$A$$ has only one eigenvalues $$\lambda$$ which is not defective (meaning $$A=\lambda I$$) then

$$\begin{equation} \label{scalar}
e^{\lambda It}=e^{\lambda t}I
\end{equation}$$

# Proofs

For these proofs, we are going to be using the Cayley-Hamilton theorem quite a bit. Without getting into all the details, subtleties, and its proof, the basic idea is

> A matrix satisfies its own characteristic polynomial

Maybe that makes intuitive sense, maybe it doesn't. But if you want to see for yourself, take the matrix $$\begin{pmatrix}a&b\\c&d\end{pmatrix}$$, and plug it into its characteristic polynomial

$$\det(A-\lambda I)=\lambda^2-(a+d)\lambda+(ad-bc)=0$$

$$
\begin{pmatrix}
a&b\\c&d
\end{pmatrix}^2-(a+d)
\begin{pmatrix}
a&b\\c&d
\end{pmatrix}+(ad-bc)
\begin{pmatrix}
1&0\\0&1
\end{pmatrix}
$$

You will indeed get the zero matrix. Pretty cool, right?

Another fact we will be using constantly is

\begin{equation}
e^{kt}e^{At}=e^{(A+kI)t}
\end{equation}

This is because $$e^{(A+kI)t}=e^{At}e^{kIt}=e^{At}e^{kt}$$.

Note: you cannot always split a matrix exponential this way. The two matrices must commute. Since scalar matrices always commute with every matrix of appropriate size, we can always use this sort of exponential shifty thing.

The reason this is so useful is that it may be difficult to compute the matrix exponential of $$A$$. But as it happens, there is always a value of $$k$$ for any $$2\times2$$s that gives $$A+kI$$ a nifty property which makes it easier to compute $$e^{(A+kI)t}$$.

In short, if its easy to calculate $$e^{(A+kI)t}$$, then its easy to calculate $$e^{At}$$.

## One Defective Eigenvalue

This one happens to be the simplest, in my opinion.

So let us say that $$A$$ is a $$2\times2$$ matrix with one defective eigenvalue $$\lambda$$. Then its characteristic polynomial is $$s^2-2\lambda s+\lambda^2=0$$. Therefore, by the Cayley-Hamilton theorem,

$$A^2-2\lambda A+\lambda^2I=0$$

$$(A-\lambda I)^2=0$$

This makes it easy to directly calculate the matrix exponential of $$A-\lambda I$$ by plugging it directly into the series $$I+tX+\frac{t^2}{2!}X^2+\ldots$$

$$e^{(A-\lambda I)t}=I+t(A-\lambda I)+(A-\lambda I)^2\left(\frac{t^2}{2!}I+\ldots\right)$$

$$e^{(A-\lambda I)t}=I+t(A-\lambda I)$$

$$e^{\lambda t}e^{(A-\lambda I)t}=e^{\lambda t}\bigg(I+t(A-\lambda I)\bigg)$$

$$e^{At}=e^{\lambda t}\bigg(I+t(A-\lambda I)\bigg)\quad\blacksquare$$

And that's it!

---

## Complex Conjugate Eigenvalues

If $$A\in\mathbb{R}^{2\times2}$$ has complex conjugate eigenvalues $$a\pm bi$$, then the characteristic polynomial of $$A$$ is $$t^2-2at+a^2+b^2=0$$. Therefore, again by the Cayley-Hamilton theorem,

$$A^2-2aA+(a^2+b^2)I=0$$

$$(A-aI)^2+b^2I=0$$

$$(A-aI)^2=-b^2I$$

For convenience, let us call $$B=A-aI$$ (note that this implies that $$e^{At}=e^{at}e^{Bt}$$)

$$B^2=-b^2I$$

Now this is interesting. Calculating even power of $$B$$ will have the *nifty* formula $$B^{2k}=(-b^2)^kI$$

$$B^{2k}=(-1)b^{2k}I$$

To get odd powers, we just multiply by $$B$$.

$$B^{2k+1}=(-1)b^{2k}B$$

Sweet. So if we split the series of $$e^{Bt}$$ into even and odd powers, we will just get the power series of a function multiplying $$I$$, and the power series of a function multiplying $$A$$. That is to say, no need to compute matrix powers at all!

$$e^{Bt}=\sum_{k=0}^\infty\frac{(-1)^kb^{2k}t^{2k}}{(2k)!}I+\sum_{k=0}^\infty\frac{(-1)^kb^{2k}t^{2k+1}}{(2k+1)!}B$$

We can combine the all of the $$b$$ terms with the $$t$$ terms using $$b^{2k}=\frac{b^{2k+1}}{b}$$, and dividing out/multiplying a $$b$$ into the sum.

$$e^{Bt}=\sum_{k=0}^\infty\frac{(-1)^k(bt)^{2k}}{(2k)!}I+\frac{1}{b}\sum_{k=0}^\infty\frac{(-1)^k(bt)^{2k+1}}{(2k+1)!}B$$

And look at that! It's our old pals, $$\cos$$ and $$\sin$$.

$$e^{Bt}=\cos(bt)I+\frac{1}{b}\sin(bt)B$$

Now we're good to go in writing things in terms of $$A$$.

$$e^{(A-aI)t}=\cos(bt)+\frac{1}{b}\sin(bt)(A-aI)$$

Now we need only multiply by $$e^{at}$$ to obtain $$e^{At}$$ in \eqref{complex1}.

$$e^{At}=e^{at}\left(\cos(bt)+\frac{1}{b}\sin(bt)(A-aI)\right)$$

We get \eqref{complex2} when we factor out $$\frac{1}{b}$$.

$$e^{At}=\frac{e^{at}}{b}\bigg(b\cos(bt)I+\sin(bt)(A-aI)\bigg)\quad\blacksquare$$

---

Now we can do something very similar to get \eqref{0trace}.

## Zero trace and negative determinant

If $$A$$ has a trace of zero and a real determinant strictly less than zero, (let us say $$\det(A)=-\lambda^2$$), then the characteristic polynomial is

$$A^2-\lambda^2I=0$$

$$A^2=\lambda^2I$$

You can repeat the process detailed above, and it will actually be easier since there's no negative to worry about. But you will get to

$$e^{At}=\sum_{k=0}^\infty\frac{(-1)^k\lambda^{2k}t^{2k}}{(2k)!}I+\sum_{k=0}^\infty\frac{(-1)^k\lambda^{2k}t^{2k+1}}{(2k+1)!}A$$

$$e^{At}=\sum_{k=0}^\infty\frac{(\lambda t)^{2k}}{(2k)!}I+\frac{1}{\lambda}\sum_{k=0}^\infty\frac{(\lambda t)^{2k+1}}{(2k+1)!}A$$

And this time we have our acquaintances who we had a class with a while back and we kind of forgot their names but they remember ours so things are a bit awkward. That being $$\cosh$$ and $$\sinh$$, naturally.

$$e^{At}=\cosh(\lambda t)I+\frac{1}{\lambda}\sinh(\lambda t)A$$

Placing the $$\sinh$$ in the numerator gives us \eqref{0trace}.

## One Nondefective Eigenvalue

This only occurs when $$A$$ is a scalar matrix, but it's also technically a case so it's worth mentioning. So let's say that $$A=\lambda I$$. Then

$$e^{At}=\sum_{n=0}^\infty \frac{(\lambda tI)^n}{n!}$$

$$e^{At}=\sum_{n=0}^\infty \frac{(\lambda t)^n}{n!}I^n$$

$$e^{At}=\left(\sum_{n=0}^\infty \frac{(\lambda t)^n}{n!}\right)I=e^{\lambda t}I$$

Thus, \eqref{scalar}

$$e^{\lambda It}=e^{\lambda t}I$$

## Rank 1 matrix

Now, if $$A$$ has a rank of one, and does not have a trace of zero, there is a nice way to obtain $$e^{At}$$, and this works for any rank one $$n\times n$$ matrix! The first key fact is to observe that if $$A$$ is rank one, then

$$A^2=\operatorname{tr}(A)A$$

You can prove this with the Cayley-Hamilton theorem! Anyway, this also implies that for $$n\geq1$$,

$$A^n=\operatorname{tr}(A)^{n-1}A$$

We may then compute $$e^{At}$$.

$$e^{At}=I+\sum_{n=1}^\infty\frac{\operatorname{tr}(A)^{n-1}t^n}{n!}A
$$

$$e^{At}=I+\frac{1}{\operatorname{tr}(A)}\sum_{n=1}^\infty\frac{(\operatorname{tr}(A)t)^n}{n!}A
$$

$$e^{At}=I+\frac{1}{\operatorname{tr}(A)}\bigg(e^{\operatorname{tr}(A)t}-1\bigg)A$$

Which is \eqref{formsingularb}. You can rearrange the terms to get \eqref{formsingular}.

$$e^{At}=\frac{e^{\operatorname{tr}(A)t}A-(A-\operatorname{tr}(A)I)}{\operatorname{tr}(A)}$$

## Distinct Eigenvalues

Now you, the nonexistent hypothetical reader, may be thinking to yourself, "Hey, nix, why are you doing the most common case *last*?" The reason is that the formulas... kind of suck? These ones are just not as good.

So for this, we're assuming that $$A$$ does not have an eigenvalue of zero. Then our nifty trick for this is to subtract a scalar matrix such that it *is* singular. If we suppose $$A$$ has eigenvalues $$\lambda_1,\lambda_2$$, then, by definition of an eigenvalue, $$A-\lambda_1I$$ is singular. Thus, we may use \eqref{formsingular}.

Again for convinience, we denote $$B=A-\lambda_1I\implies e^{At}=e^{\lambda_1t}e^{Bt}$$. One can also verify that the trace of $$B$$ is $$\lambda_2-\lambda_1$$. Hence,

$$e^{Bt}=\frac{e^{(\lambda_2-\lambda_1)t}B-(B-(\lambda_2-\lambda_1)I)}{\lambda_2-\lambda_1}$$

There's not a lot to simplify, but observe that $$B-(\lambda_2-\lambda_1)I=A-\lambda_2I$$.

$$e^{Bt}=\frac{e^{(\lambda_2-\lambda_1)t}(A-\lambda_1I)-(A-\lambda_2I)}{\lambda_2-\lambda_1}$$

And thus we get \eqref{distinct}

$$e^{At}=\frac{e^{\lambda_2t}(A-\lambda_1I)-e^{\lambda_1t}(A-\lambda_2I)}{\lambda_2-\lambda_1}$$

You can get \eqref{distinct2} by isolating $$A$$ and $$I$$.

---

## Another approach

You may have noticed that so far every formula can be rearranged to be in the form

$$e^{At}=x_1(t)I+x_2(t)A$$

And, in fact, yes. This will be true for any $$2\times2$$ matrix. More generally, for any $$n\times n$$ matrix $$A$$, you can write $$e^{At}$$ in the form

$$e^{At}=x_1(t)I+\ldots+x_n(t)A^{n-1}$$

See [this post](../matrixexpwde){:target="_blank"} to learn more about that... But I'm going to present *another* kind of similar and totally equivalent method here.

Now, there are a few ways you can go about this. One way is to get a first order initial value problem for which $$e^{At}$$ is the solution.

$$\Phi'=A\Phi, \quad \Phi(0)=I$$

$$x_1'(t)I+x_2'(t)A=x_1(t)A+x_2(t)A^2$$

Using Cayley-Hamilton, if the characteristic polynomial of $$A$$ is $$t^2-pt+q=0$$, then $$A^2=pA-qI$$.

$$x_1'(t)I+x_2'(t)A=x_1(t)A+x_2(t)(pA-qI)$$

Setting the terms on $$I$$ and $$A$$ equal gives,

$$\begin{array}{ccccc}
x_1'&=&&&-qx_2\\
x_2'&=&x_1&+&px_2
\end{array}$$

$$
\textbf{x}'=
\begin{pmatrix}
0&-q\\1&p
\end{pmatrix}
\textbf{x},\quad
\textbf{x}(0)=
\begin{pmatrix}
1\\0
\end{pmatrix}
$$

Now, we can use the fact that $$p=\operatorname{tr}(A)$$ and $$q=\det(A)$$.

$$
\textbf{x}'=
\begin{pmatrix}
0&-\det(A)\\1&\operatorname{tr}(A)
\end{pmatrix}
\textbf{x},\quad
\textbf{x}(0)=
\begin{pmatrix}
1\\0
\end{pmatrix}
$$

A neat observation is that this coefficient matrix has the same trace and determinant as $$A$$. It is, in fact, similar to $$A$$. So we already know the eigenvalues going in (assuming you found them before).

We can use the fact that $$\operatorname{tr}(A)=\lambda_1+\lambda_2$$ and $$\det(A)=\lambda_1\lambda_2$$.

$$\begin{equation}\label{1stsys}
\textbf{x}'=
\begin{pmatrix}
0&-\lambda_1\lambda_2\\1&\lambda_1+\lambda_2
\end{pmatrix}
\textbf{x},\quad
\textbf{x}(0)=
\begin{pmatrix}
1\\0
\end{pmatrix}
\end{equation}$$

And at this point, we have an initial value problem, and we can solve for $$x_1,x_2$$ by finding the eigenvectors.

If you feel inclined, I do recommend trying to solve \eqref{1stsys} for all the different cases of eigenvalues! I found it satisfying to get the same formulas derived above.

---

*Another* another option is to convert \eqref{1stsys} to a linear second order differential equation.

$$x_1=x_2'-(\lambda_1+\lambda_2)x_2$$

$$\implies x_1'=x_2''-(\lambda_1+\lambda_2)x_2'=-\lambda_1\lambda_2x_2$$

$$x_2''-(\lambda_1+\lambda_2)x_2'+\lambda_1\lambda_2x_2=0$$

ᵒʰ ʰᵉʸ ˡᵒᵒᵏ ⁱᵗ'ˢ ᵗʰᵉ ᶜʰᵃʳᵃᶜᵗᵉʳⁱˢᵗⁱᶜ ᵖᵒˡʸⁿᵒᵐⁱᵃˡ

Then you could solve it like a normal initial value problem. If you want, I guess.

# Applications

For ways to apply matrix exponentials to solve $$2\times2$$ systems of differential equations, check out [this post](../firstordersystemsquick){:target="_blank"} on solving them like a baller.

It's also possible to find very similar formulas for $$A^n$$ using these methods. The formulas for the $$2\times2$$ cases are *extremely* similar to the formulas derived here.

For example, if $$A\in\mathbb{R}^{2\times2}$$ has complex eigenvalues $$a\pm bi=re^{\pm i\theta}$$, then, as mentioned above

$$e^{At}=e^{at}\left(\cos(bt)I+\frac{\sin(bt)}{b}\bigg(A-aI\bigg)\right)$$

But in addition,

$$A^n=r^n\left(\cos(n\theta)I+\frac{\sin(n\theta)}{b}\bigg(A-aI\bigg)\right)$$

The method discussed in [Another Approach](#another-approach) is my preferred choice for finding these formulas. But the system is not a differential equation, and instead a discrete analog.

$$\textbf{x}(n+1)=A\textbf{x}(n)$$

And while $$e^{At}\textbf{x}(0)$$ is the solution to $$\textbf{x}'=A\textbf{x}$$, the solution to the equation above is $$A^n\textbf{x}(0)$$

I may choose to write a post about these in the future... EDIT: [I totally did. I couldn't wait.](../discretesystems){:target="_blank"}

## Closing Remarks

I enjoyed verifying that taking the derivative of these formulas is indeed the same as multiplying by $$A$$.

$$\begin{equation}
\frac{d}{dt}e^{At}=Ae^{At}
\end{equation}$$

Possibly even more fun than that is verifying that substituting $$-t$$ for $$t$$ does in fact give the inverse.

$$\begin{equation}
e^{At}e^{-At}=I\implies e^{-At}=\left(e^{At}\right)^{-1}
\end{equation}$$
