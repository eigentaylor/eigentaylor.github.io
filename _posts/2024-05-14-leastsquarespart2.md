---
layout: distill
title: Introduction to Least Squares Part 2 (Electric Boogaloo)
date: 2024-05-14
description: Why the heck do we multiply by the transpose
comments: true
importance: 3
categories: linear-algebra
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Why is it consistent
  - name: Why is it the closest solution
  - name: The smallest closest solution
---

This is a short sequel to my previous post on [least squares](../leastsquares/){:target="_blank"}.

These are the questions I left at the end of that post (in the more general complex form).

1. Why is $$\mathbf{A}^*\mathbf{A}\mathbf{x}=\mathbf{A}^*\mathbf{b}$$ guaranteed a solution?
2. Why would the solution to the normal equation actually be the "closest" solution?

When I say "dot product" here, I mean the general euclidean inner product on $$\mathbb{C}^n$$, where we multiply by the *conjugate* transpose (adjoint) rather than the regular transpose. 

$$\langle w,v\rangle=v^*w=\left(\overline{v}\right)^Tw$$

Note that if we talk about $$\mathbb{R}^n$$, then the adjoint is just, of course, the regular transpose.

If you need a reminder for why we need the *conjugate*, it's because complex numbers get weird when you just square them:

$$\begin{pmatrix}1&i\end{pmatrix}\begin{pmatrix}1\\i\end{pmatrix}=1^2+i^2=0$$

In $$\mathbb{R}^n$$, we say $$\left\lVert v \right\rVert^2=v^Tv$$, but that would mean this nonzero vector has a magnitude of $$0$$. This is a big no-no, as we should *only* have that the zero vector has a magnitude of $$0$$.

So we can't just say $$w\cdot v=v^Tw$$ and call it a day if we want to be as general as possible. But you are more than welcome to just interpret $$v^*$$ as the transpose, and assume we're talking in terms of real vectors (my complex compulsion prevents me from doing so).

## Why is it consistent

Recall that a system of equations $${A}{x}={b}$$ is consistent when $$b$$ is in the image or column space of $$A$$. So the column space, $$W$$, is going to be the main character in our story today.

We know that every vector space can be decomposed as the direct sum of any subspace and its orthogonal complement. That is,

$$\mathbb{C}^n=W\oplus W^\perp$$

This means that $$b$$ can be written *uniquely* as $$b=w+w_\perp$$, where $$w$$ is $$W$$ and $$w_\perp$$ is orthogonal to everything in $$W$$. Conceptually this can be understood as writing $$b$$ as a sum of a vector which does make a consistent system, and a vector which can knock us out of being consistent (i.e. the system is consistent if and only if $$w_\perp=0$$).

Remember that to be orthogonal in $$\mathbb{C}^n$$, we need $$w\cdot v=v^*w=0$$. This definition *does* mean the complex dot product is not commutative, but it is conjugate commutative ($$v\cdot w=\overline{w\cdot v}$$). So, since we are only interested in orthogonality and dot products of zero, we still get a sort of orthogonal symmetry/commutativity ($$v\cdot w=0\iff w\cdot v=0$$).

This does add one complication. While in $$\mathbb{R}^n$$, $$An=0$$ implies that $$n$$ is orthogonal to the rows of $$A$$, that isn't quite so in $$\mathbb{C}^n$$, since the inner product requires one vector to be conjugated. That is, while in $$\mathbb{R}^n$$, the row space is the orthogonal complement of the null space, in $$\mathbb{C}^n$$, the null space is the orthogonal complement of the conjugated row space ($$\ker(B)^\perp=\operatorname{row}(\overline{B})$$, which is also $$\operatorname{col}(B^*)$$). Note that if $$B$$ is real, we do recover the result that the kernel is orthogonal to the row space.

But if we let $$B=A^*$$ in the expression above, this means the orthogonal complement of the null space of $$A^*$$ is the column space of $$A$$. That is, if a vector $$u$$ is orthogonal to the column space of $$A$$, then $$A^*u=0$$.

Thus, $$A^*w_\perp=0$$ and so $$A^*b=A^*(w+w_\perp)=A^*w$$. Essentially, this means that multiplying by the adjoint *sort of* projects us into the column space of $$A$$ (or, at least, zeros out the part that isn't in the column space).

Since $$w$$ is by definition in the column space of $$A$$, we know $$Ax=w$$ is consistent. Let $$x=c$$ be the solution (that is, $$w=Ac$$).

So let's write out what happens when we multiply $$Ax=b$$ by $$A^*$$.

$$A^*Ax=A^*b=A^*w=A^*Ac$$

This clearly has a solution: $$x=c$$, which actually implies that the solution to $$A^*Ax=A^*b$$ is the same as the solution to $$Ax=w$$.

That is, the least squares solution is the solution to the system projected onto the column space. Which actually makes some sense intuitively. If we want the closest solution, we want it to be the solution to the system where the vector is projected orthogonally to the column space. Which actually answers both our questions.

## Why is it the closest solution

Now, I said it answers both of our questions, but perhaps you aren't quite convinced that just because it's the solution to the system where $$b$$ has been projected into the column space it actually minimizes our error. Let's see if I can change your mind.

We measure the "closest" solution using $$\left\lVert b-Ax \right\rVert^2$$ (minimizing the squares of error: hence, 'least squares').

Note that by orthogonality, we can say that $$\left\lVert w+w_\perp \right\rVert^2=\left\lVert w \right\rVert^2+\left\lVert w_\perp \right\rVert^2$$. But, since $$w$$ and $$Ax$$ are both in $$W$$, we can rewrite

$$\left\lVert b-Ax \right\rVert^2=\left\lVert w+w_\perp-Ax \right\rVert^2=\left\lVert w-Ax \right\rVert^2+\left\lVert w_\perp \right\rVert^2$$

Notice that no matter *what* $$x$$ is, our squared error will always be $$\geq\left\lVert w_\perp \right\rVert^2$$. This is hopefully somewhat intuitive. Since $$w_\perp$$ is the part of $$b$$ that makes our system inconsistent, its size acts as a lower bound for our error, telling us in a sense *how* inconsistent our system is. Cool, right?

Thus, the only thing we *can* do to minimize error, is to minimize $$\left\lVert w-Ax \right\rVert^2$$. The best we can do is make it zero. But... like we said before, $$w=Ac$$ for some $$c$$. Then, $$x=c$$ will give us zero. So $$x=c$$, the solution to $$Ax=w$$, really *is* the solution that minimizes the error!

One might object: what if $$A$$ has dependent columns and there are multiple solutions to $$Ax=w$$? Well, we can see that *all* of those solutions will minimize the error. That is, even if the least squares solution is not unique, every single one will minimize the error! This is because the error is in terms of the magnitude of $$w-Ax$$. And $$w-Ax=0$$ if and only if $$x$$ is a preimage of $$w$$ of $$A$$ (there is no restriction on *which preimage*).

## The smallest closest solution

If you're very picky, and you want to pick *just one* least squares solution, then you *could* theoretically pick the least squares solution with the minimum magnitude. If $$c$$ is one least squares solution, then any other least squares solution will be of the form $$c+u$$ where $$u\in\ker(A)$$. Then, we can play a similar game in trying to minimize

$$\left\lVert c+u \right\rVert^2=\left\lVert k+k_\perp+u \right\rVert^2=\left\lVert k+u \right\rVert^2+\left\lVert k_\perp \right\rVert^2$$

where we are decomposing $$c$$ in terms of $$k\in\ker(A)$$ and $$k_\perp\in\ker(A)^\perp$$. Since our degree of freedom is in choosing $$u$$, we should pick $$u=-k$$, and then we find that the 'least squares least squares solution' is the solution in the orthogonal complement of $$\ker(A)$$.

$$x_{least}=\operatorname{proj}_{\ker(A)^\perp}(c)$$

If you are hankering for an expression for the projector into $$\ker(A)^\perp$$, then one method one could use (especially if they're in some sort of computing/programming environment) is to use the $$QR$$ decomposition of $$A^*=QR$$, and then

$$x_{least}=QQ^*c$$

This is because, as we said above, the orthogonal complement of $$\ker(A)$$ is the column space of $$A^*$$, and $$QQ^*$$ from the $$QR$$ decomposition projects orthogonally into the column space.

We can actually do much better using the reduced SVD of $$A=USV^*$$, where $$S$$ is square and invertible. Then, you can show that

$$x_{least}=VS^{-1}U^*b$$

Which is why we call $$VS^{-1}U^*$$ the "pseudo-inverse of $$A$$". It always gives the smallest least squares solution! This is absolutely as good as it gets for a singular matrix.

I think it's a good exercise to try and show that $$VS^{-1}U^*b$$ is in fact the smallest least squares solution! If you need some hints to get started,

- $$UU^*$$ is a projector onto the column space of $$A$$
- $$VV^*$$ is a projector onto the column space of $$A^*$$, which is orthogonal to $$\ker(A)$$
- If $$b=w+w_\perp$$, then what is $$w$$ in terms of $$b$$ and $$U$$?

[hyperlink](https://youtu.be/M5CeQG1YfEQ?si=2J5M9Tdyq01GVAsc){:target="_blank"}
