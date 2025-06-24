---
layout: distill
title: New Ways to Calculate Normalized Solutions to Linear Constant-Coefficient Differential Equations
date: 2022-01-12
description: The fastest way for a computer, and a fast way by hand.
comments: true
importance: 3
category: differential equations
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: The Method
  - name: Wait, what are normalized solutions?
  - name: Proof and Derivation
    subsections:
      - name: Proof
      - name: Derivation
  - name: Some Interesting Consequences
  - name: Some notes on the Laplace Transforms
  - name: Normalized solutions recap
    subsections:
      - name: Solving n problems individually
      - name: Inverting the Wronskian
      - name: Solving the one system of first order IVPs
      - name: Using the recursive formula
      - name: Summary
---

## The Method

This is actually ridiculously simple. All you have to do is solve *one* system of first-order equations with a really simple matrix.

To get the normalized solutions $$Y_1,\ldots,Y_n$$, to

\begin{equation}\label{prob}
y^{(n)}=p_0y+p_1y'+\ldots+p_{n-1}y^{(n-1)}
\end{equation}

One only needs to solve the $$n\times n$$ system,

$$\begin{equation}\label{method}
\textbf{Y}'=
\begin{pmatrix}
0&0&\dots&0&p_0\\
1&0&\dots&0&p_1\\
0&1&\dots&0&p_2\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&\dots&1&p_n
\end{pmatrix}
\textbf{Y},\quad
\textbf{Y}(0)=
\begin{pmatrix}
1\\0\\\vdots\\0\\0
\end{pmatrix}
\end{equation}$$

This is very easy to put into a computer and quick to solve.

There are also some interesting consequences and relationships between the normalized solutions that this reveals.

## Wait, what are normalized solutions?

I made a [post](/math/normalized){:target="_blank"} about them before, but here is a short explanation.

Normalized solutions make solving initial value problems easy. They are the solutions $$Y_1,\ldots,Y_n$$ such that the solution to the initial value problem with initial conditions $$y(t_0)=y_0,\ldots,y^{(n-1)}(t_0)=y^{(n-1)}_0$$ is simply

\begin{equation} \label{normsol}
y=y_0Y_1+\ldots+y^{(n-1)}_0Y_n
\end{equation}

Basically, the constants are just the initial conditions. This way, you don't have to solve for the constants.

Consequently, each of the solutions satisfy the $$n$$ initial value problems

$$\begin{equation}
\begin{array}{cccc}
Y_1(t_0)=1&Y_1'(t_0)=0&\ldots&Y_1^{(n-1)}(t_0)=0\\
Y_2(t_0)=0&Y_2'(t_0)=1&\ldots&Y_2^{(n-1)}(t_0)=0\\
\vdots&\vdots&\ddots&\vdots&\\
Y_n(t_0)=0&Y_n'(t_0)=0&\ldots&Y_n^{(n-1)}(t_0)=1\\
\end{array}
\end{equation}$$

Note that these will be the entries of their Wronskian, and at $$t_0$$ the Wronskian is the identity matrix!

Now you may be asking yourself, "why would I want to solve $$n$$ initial value problems to get these solutions?" Apart from the fact that I have just detailed a method to make it solving just one initial value problem, in theory their use is solving multiple initial value problems.

Say you have a differential equation which models some physical model (like a circuit or something idk I'm not an engineer), and you want to know what the response to many different inputs is. Say you have 100 different initial conditions you want to test. Rather than solve for the general solution and then solve 100 different systems of equations for the constants, just solve for the $$n$$ normalized solutions and then the solution to the 100 different initial value problems will require no solving.

## Proof and Derivation

### Proof

Consider the initial value problem

\begin{equation} \label{ivp}
y^{(n)}=p_0y+p_1y'+\ldots+p_{n-1}y^{(n-1)},\quad y(0)=y_0,\ldots,y^{(n-1)}(0)=y^{(n-1)}_0
\end{equation}

If the normalized solutions are $$Y_1,\ldots,Y_n$$, then the solution is \eqref{normsol}. This can be rewritten as

$$y_0Y_1+\ldots+y^{(n-1)}_0Y_n=\textbf{Y}\cdot\textbf{y}_0$$

Letting $$\textbf{Y}=(Y_1,\ldots,Y_n)$$ be the vector of our normalized solutions, and $$\textbf{y}_0=(y_0,\ldots,y^{(n-1)}_0)$$ the vector of our initial conditions.

Or, alternatively,

$$y=\textbf{Y}^T\textbf{y}_0$$

It is a fact that the $$n$$-th order \eqref{ivp} can be rewritten as a system of first order equations with the change of variables $$y_1=y,\ldots,y_n=y^{(n-1)}$$. Let $$B$$ be the matrix for which the matrix form of the reduced system is

$$\begin{equation}
\textbf{y}'=B\textbf{y},\quad \textbf{y}(0)=\textbf{y}_0
\end{equation}$$

$$B=\begin{pmatrix}
0&1&0&\dots&0\\
0&0&1&\dots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots&\\
0&0&0&\dots&1\\
p_0&p_1&p_2&\dots&p_{n-1}
\end{pmatrix}
=\left(\begin{array}{ccccccc}
\begin{array}{cc}
0&I_{n-1}
\end{array}\\\vec{p}
\end{array}\right)$$

The solution to this system is $$\textbf{y}(t)=e^{Bt}\textbf{y}_0$$.

From our definition of our variables, $$y=y_1=(1,\ldots,0)\cdot\textbf{y}$$. Denoting the first standard basis vector of $$\mathbb{R}^n$$, $$\textbf{e}_1=(1,\ldots,0)$$, we can rewrite this neatly as

$$y=\textbf{e}_1^T\textbf{y}$$

$$y=\textbf{e}_1^Te^{Bt}\textbf{y}_0$$

$$y=\left(\left(e^{Bt}\right)^T \textbf{e}_1\right)^T\textbf{y}_0$$

$$y=\left(e^{B^Tt}\textbf{e}_1\right)^T\textbf{y}_0$$

Now we have two solutions to this initial value problem: $$y=\textbf{Y}^T\textbf{y}_0=\left(e^{B^Tt}\textbf{e}_1\right)^T\textbf{y}_0$$. Therefore, by the existence and uniqueness theorem,

\begin{equation}
\textbf{Y}=e^{B^Tt}\textbf{e}_1
\end{equation}

However, $$\textbf{Y}=e^{B^Tt}\textbf{e}_1$$ is the unique solution to the initial value problem

$$\begin{equation}
\textbf{Y}'=
B^T
\textbf{Y},\quad
\textbf{Y}(0)=
\textbf{e}_1
\end{equation}$$

Q.E.D.

### Derivation

Now, the proof may seem like a fine derivation. But I think there is a more intuitive approach to reveal this.

We start by letting $$s$$ be any root/solution of the characteristic polynomial

$$s^n=p_0+p_1s+\ldots+p_{n-1}s^{n-1}$$

Then $$y=e^{st}$$ must be a solution to \eqref{prob}, with the initial conditions $$y(0)=1,y'(0)=s,\ldots,y^{n-1}(0)=s^{n-1}$$. By the uniqueness theorem, it follows that

$$
e^{st}=Y_1+sY_2+\ldots+s^{n-1}Y_n
$$

Now, I was certainly surprised by this formula at first. But it checks out! For example, $$e^{it}$$ is a solution to $$y''=-y$$, and the normalized solutions are $$Y_1=\cos(t),Y_2=\sin(t)$$. And indeed

$$e^{it}=\cos(t)+i\sin(t)$$

is Euler's formula! I enjoyed verifying this for some other problems like $$e^{kt}$$ and $$y''=-k^2y+2ky$$.

Differentiate this expression,

$$
se^{st}=Y_1'+sY_2'+\ldots+s^{n-1}Y_n'
$$

$$
s(Y_1+sY_2+\ldots+s^{n-1}Y_n)=Y_1'+sY_2'+\ldots+s^{n-1}Y_n'
$$

$$
sY_1+s^2Y_2+\ldots+s^{n}Y_n=Y_1'+sY_2'+\ldots+s^{n-1}Y_n'
$$

$$
sY_1+s^2Y_2+\ldots+(p_0+p_1s+\ldots+p_{n-1}s^{n-1})Y_n=Y_1'+sY_2'+\ldots+s^{n-1}Y_n'
$$

Combine terms by the power of $$s$$.

$$
p_0Y_n+s(Y_1+p_1Y_n)+\ldots+s^{n-1}(Y_{n-1}+p_{n-1}Y_n)=Y_1'+sY_2'+\ldots+s^{n-1}Y_n'
$$

*something something* linear independence.

$$\begin{gather*}
Y_1'=p_0Y_n\\
Y_2'=Y_1+p_1Y_n\\
\vdots\\
Y_n'=Y_{n-1}+p_{n-1}Y_n
\end{gather*}$$

We also know by the definition of our normalized solutions that

$$Y_1(0)=1,Y_2(0)=0,\ldots,Y_n(0)=0$$

In matrix form,

$$
\begin{pmatrix}
Y_1'\\Y_2'\\\vdots\\Y_{n-1}'\\Y_n'
\end{pmatrix}=
\begin{pmatrix}
0&0&\dots&0&p_0\\
1&0&\dots&0&p_1\\
0&1&\dots&0&p_2\\
\vdots&\vdots&\ddots&\vdots&\vdots\\
0&0&\dots&1&p_n
\end{pmatrix}
\begin{pmatrix}
Y_1\\Y_2\\\vdots\\Y_{n-1}\\Y_n
\end{pmatrix},\quad
\begin{pmatrix}
Y_1(0)\\Y_2(0)\\\vdots\\Y_{n-1}(0)\\Y_n(0)
\end{pmatrix}=
\begin{pmatrix}
1\\0\\\vdots\\0\\0
\end{pmatrix}$$

And hey, that's the transpose of our $$B$$ matrix!

$$
\textbf{Y}'=
B^T
\textbf{Y},\quad
\textbf{Y}(0)=
\textbf{e}_1
$$

## Some Interesting Consequences

Now the most interesting equation that comes out of this is

$$\begin{equation} \label{proportional}
Y_1'=p_0Y_n
\end{equation}$$

Implying that the integral of $$Y_n$$ is proportional to $$Y_1$$. Not going to lie, I don't have an intuitive explanation for why this is true, but it is verifiable. :man_shrugging: Below I discuss the Laplace Transforms of the normalized solutions, and the properties are more obvious when looking at those.

One observation to make is that if $$p_0=0$$, then the expression for $$Y_1$$ becomes

$$Y_1'=0,\quad Y_1(0)=1$$

And the solution to that is just $$Y_1(t)=1$$. Since that function obviously satisfies the conditions, it makes sense that we can just jump right ahead to that being the first normalized solution. Similarly, depending on the multiplicity of the root $$0$$, the first couple of normalized solutions should be $$Y_k=\frac{t^k}{k!}$$.

Also, we see that for $$1\leq k\leq n-1$$

$$\begin{equation} \label{recursive}
Y_k=Y_{k+1}'-p_kY_n
\end{equation}$$

Giving a recursive formula for each normalized solution.

Now, both of these equations involve $$Y_n$$. So if you can solve for that, then you can get all of the other solutions. You can get $$Y_1$$ by integrating it (or, alternatively, solve for $$Y_1$$ and then differentiate it to get $$Y_n$$, assuming $$p_0\neq0$$), and you can directly get $$Y_{n-1}$$ with

$$Y_{n-1}=Y_n'-p_{n-1}Y_n$$

In the case with complex roots, especially with a nonzero real part, differentiation is going to be easier than integration.

And then you could get $$Y_{n-2}$$ with

$$
Y_{n-2}=Y_{n-1}'-p_{n-2}Y_n
$$

And so on.

## Some notes on the Laplace Transforms

One thing to note is that $$Y_n$$ is particularly easy to find using the Laplace Transform. In fact, it turns out to actually be the weight function, giving it even more applications than one (including me) might originally expect. The weight function, briefly, is the inverse Laplace Transform of the transfer function (the reciprocal of the characteristic polynomial),

$$
\mathscr{L}\{Y_n\}=\frac{1}{s^n-p_{n-1}s^{n-1}-\ldots-p_1s-p_0}
$$

For convenience, we will from now on denote $$p(s)=s^n-p_{n-1}s^{n-1}-\ldots-p_1s-p_0$$

The weight function's primary application is in solving for particular solutions. As the unique solution to the initial value problem

$$
y^{(n)}=p_0y+p_1y'+\ldots+p_{n-1}y^{(n-1)}+g(t),\quad y(0)=0,\ldots,y^{(n-1)}(0)=0
$$

will be the convolution

$$y_p(t)=Y_n(t)*g(t)=\int_0^tY_n(t-\tau)g(\tau)\,d\tau$$

Using superposition, this gives a formula for the solution to the general nonhomogeneous initial value problem

$$
y^{(n)}=p_0y+p_1y'+\ldots+p_{n-1}y^{(n-1)}+g(t),\quad y(0)=y_0,\ldots,y^{(n-1)}(0)=y^{(n-1)}_0
$$

$$
y(t)=y_0Y_1(t)+\ldots+y^{(n-1)}_0Y_n(t)+Y_n(t)*g(t)
$$

My conjecture is that the reason $$Y_n$$ is so useful/shows up so much in the above formulas is exactly because it is the weight function.

There are similar formulas for the Laplace Transforms of the other normalized solutions.

$$\begin{gather*}
\mathscr{L}\{Y_n\}=\frac{1}{p(s)}\\
\mathscr{L}\{Y_{n-1}\}=\frac{s-p_{n-1}}{p(s)}\\
\mathscr{L}\{Y_{n-2}\}=\frac{s^2-p_{n-1}s-p_{n-2}}{p(s)}\\
\vdots\\
\mathscr{L}\{Y_1\}=\frac{s^{n-1}-p_{n-1}s^{n-2}+\ldots-p_2s-p_1}{p(s)}
\end{gather*}$$

In general, the numerator of $$\mathscr{L}\{Y_k\}$$ is just the characteristic polynomial after lobbing off the first $$k$$ lowest degree terms, and then dividing by the lowest power of $$s$$ ($$s^k$$).

$$s^kp(s)\mathscr{L}\{Y_k\}=s^{n}-\sum_{i=k}^{n-1}p_{i}s^{i}$$

Viewing normalized solutions this way makes the properties \eqref{proportional} and \eqref{recursive} much easier to see and verify.

Now, when solving a system of initial value problems,

$$\textbf{x}'=A\textbf{x},\quad \textbf{x}(0)=\textbf{x}_0$$

In general, one can use the Laplace Transform to solve it as

$$(sI-A)\mathscr{L}\{\textbf{x}\}=\textbf{x}_0$$

$$\mathscr{L}\{\textbf{x}\}=(sI-A)^{-1}\textbf{x}_0$$

For our system,

$$\mathscr{L}\{\textbf{Y}\}=(sI-B^T)^{-1}\textbf{e}_1$$

Thus, we can see that the Laplace Transforms of our normalized solutions will be the first column of $$(sI-B^T)^{-1}$$. Consequently, the numerators will be the first column of $$(sI-B^T)^{adj}$$, which will also be the cofactors of the first row of $$sI-B^T$$, which will also be the cofactors of the first column of $$sI-B$$. Thankfully, because $$B$$ is relatively simple, the cofactors are not too difficult to calculate.

Of course, why do any of that when I have most *graciously* provided the results for you, already?

## Normalized solutions recap

Now here are all of the ways I know of to calculate normalized solutions. I am going to compare and assess each of their uses.

1. Solve all $$n$$ initial value problems individually
2. Invert the Wronskian
3. Solve the one system of initial value problems detailed above \eqref{method}
4. Get $$Y_n$$ and obtain the others recursively

You could also take the first row of $$e^{Bt}$$ or take the inverse laplace transform of the first column of $$(sI-B^T)^{-1}$$, but these are just longer and more difficult/roundabout ways to do method 3.

When discussing using a "computer" I'm generally imagining putting it into Wolfram Alpha or MATLAB. I usually prefer doing stuff by hand though, to be honest.

Generally, the pattern is that all of these methods are "fine" for the second order case and require *approximately* the same amount of work by hand. Some are better than others for the third order case using certain shortcuts. But for fourth order and higher, doing things by hand gets to be too difficult.

### Solving n problems individually

You could solve the $$n$$ initial value problems with the following initial conditions

$$
\begin{array}{cccc}
Y_1(t_0)=1&Y_1'(t_0)=0&\ldots&Y_1^{(n-1)}(t_0)=0\\
Y_2(t_0)=0&Y_2'(t_0)=1&\ldots&Y_2^{(n-1)}(t_0)=0\\
\vdots&\vdots&\ddots&\vdots&\\
Y_n(t_0)=0&Y_n'(t_0)=0&\ldots&Y_n^{(n-1)}(t_0)=1\\
\end{array}
$$

Maybe do this once to see how tedious it can be and why you will never want to do it ever again.

### Inverting the Wronskian

This requires inverting an $$n\times n$$ matrix. While this is very manageable for a $$2\times 2$$ and tolerable for a $$3\times 3$$ (using the adjugate) in the second and third order cases respectively, this becomes very tedious to do by hand for anything larger.

The general idea is that to solve an initial value problem you get your general solution $$y=c_1y_1+\ldots+c_ny_n$$. Then you solve the system of equations

$$
\begin{array}{cccccc}
c_1y_1(0)&+&\ldots&+&c_ny_n(0)&=&y_0\\
c_1y_1'(0)&+&\ldots&+&c_ny_n'(0)&=&y_0'\\
\vdots&\vdots&\ddots&\vdots&\vdots&\vdots&\vdots\\
c_1y_1^{(n-1)}(0)&+&\ldots&+&c_ny_n^{(n-1)}(0)&=&y_0^{(n-1)}\\
\end{array}
$$

In augmented matrix form, this ends up being

$$
\left(
\begin{array}{ccc|c}
y_1(0)&\ldots&y_n(0)&y_0\\
y_1'(0)&\ldots&y_n'(0)&y_0'\\
\vdots&\ddots&\vdots&\vdots\\
y_1(0)^{(n-1)}&\ldots&y_n^{(n-1)}(0)&y_0^{(n-1)}\\
\end{array}
\right)
$$

Since no matter what the initial conditions are, you do the same row operations to solve for the coefficients, we can put all $$n$$ of our initial value problems in $$n$$ different columns.

$$
\left(
\begin{array}{ccc|ccc}
y_1(0)&\ldots&y_n(0)&1&\ldots&0\\
y_1'(0)&\ldots&y_n'(0)&0&\ldots&0\\
\vdots&\ddots&\vdots&\vdots&\ddots&\vdots\\
y_1(0)^{(n-1)}&\ldots&y_n^{(n-1)}(0)&0&\ldots&1\\
\end{array}
\right)
$$

The coefficient matrix is our Wronskian, so if we abbreviate $$W[y_1,\ldots,y_m](0)$$ as $$W$$, we can rewrite that system simply as

$$
\left(
\begin{array}{c|c}
W&I
\end{array}
\right)
$$

And, well, putting that augmented matrix into reduced row echelon form is just a general method for finding $$W^{-1}$$.

$$
\left(
\begin{array}{c|c}
W&I
\end{array}
\right)
\to
\left(
\begin{array}{c|c}
I&W^{-1}
\end{array}
\right)
$$

Thus, the columns of $$W^{-1}$$ give you the coefficients for each of the normalized solutions.

Now, this gets difficult quickly because you have to actually find $$y_j^{(i)}(0)$$. Meaning you have to differentiate all $$n$$ of your solutions $$n-1$$ times. For the second order case, it's just one derivative, meaning 2 total. For the third order case, however, it's 6 differentiations. Then it's 12, 20, etc. And differentiation can be kind of tedious, so it is not ideal.

So even if you do the inversion using Wolfram Alpha, you have to calculate the entries manually.

### Solving the one system of first order IVPs

This method requires no differentiating, but it requires finding the eigenvectors of an $$n\times n$$ matrix. This is trivial for a computer, and for this reason it is by far the fastest way to compute them that way. This system is very easy to put into Wolfram Alpha, for example.

Doing this by hand, however, is a different story. Even just computing the characteristic polynomial can be tedious to do by hand. That said! The roots of the characteristic polynomial of $$B^T$$ are the same as the roots of the characteristic polynomial of \eqref{prob}. So, assuming you already factored the characteristic polynomial in the process of solving the for the homogeneous solutions, you know the eigenvalues going in.

Furthermore, the matrix is simple enough that finding eigenvectors is not too difficult. In fact, I found a formula for the eigenvectors:

$$v_\lambda=\begin{pmatrix}
\lambda^{n-1}-p_{n-1}\lambda^{n-2}-\ldots-p_2\lambda-p_1\\
\lambda^{n-2}-p_{n-1}\lambda^{n-3}-\ldots-p_2\\
\vdots\\
\lambda-p_{n-1}\\
1
\end{pmatrix}$$

In general, the entries are

$$v_i=\left(\lambda^{n-i}-\sum_{k=i}^{n-1}p_k\lambda^{k-i}\right)v_n$$

Hold on... What??? It's the numerators of the Laplace Transforms evaluated at each of the roots!

Now, generalized eigenvectors for the repeated case are not quite as easy to find. I have not found a simple general formula, and I don't think it would be worth looking for.

Finding eigenvectors when you already know the eigenvalues is basically equivalent to finding vectors in the null space of $$B^T-\lambda I$$. Of course, generalized eigenvectors complicate things a bit, but overall it's just row reduction.

However, once you find all the eigenvectors, you have to solve the initial value problem. Luckily, there is a shortcut which is to calculate the cofactors of the first row of the matrix of eigenvectors (or modal matrix in the general case) and then divide by the determinant. This is equivalent to using Cramer's rule, which is actually not a bad idea in this case since the $$\textbf{b}$$ vector has only one nonzero entry, making it a good choice to expand the determinant along its column.

In conclusion, this is not the best way to do it by hand, in my opinion. Choosing between this and inverting the Wronskian, I would probably choose this, though, because I find solving these systems a lot more fun than differentiating a bunch of different functions and then inverting a matrix.

### Using the recursive formula

For this method, you can solve just *one* $$n$$-th order equation to get $$Y_n$$, and then use the recursive formula \eqref{recursive}

$$Y_k=Y_{k+1}'-p_kY_n$$

And if $$Y_n$$ is easy to integrate, then you can also use \eqref{proportional}

$$Y_1'=p_0Y_n$$

Overall, though, this would probably be the second worst method for a computer. Because you would still have to do $$n$$ separate commands. However, they wouldn't be quite as bad as inputting $$n$$ initial value problems.

But by hand, this is not bad.

## Summary

1. Solving $$n$$ problems individually: Requires solving $$n$$ $$n$$-th order initial value problems. This includes factoring an $$n$$-th degree polynomial, evaluating $$n^2-n$$ derivatives and solving $$n$$ systems of $$n$$ equations with $$n$$ variables.
2. Inverting the Wronskian requires no initial value problem solving, but instead turns it into a linear algebra problem where one must invert an $$n\times n$$ matrix. You, of course first need to factor an $$n$$-th degree polynomial, but then you also need to differentiate and evaluate your $$n$$ solutions (making that $$n^2-n$$ derivatives total).
3. Solving the one system of first order IVPs unsurprisingly requires solving one system of $$n$$ first order initial value problems. This requires no derivatives but requires solving for a basis of $$n$$ eigenvectors and solving one system of $$n$$ equations with $$n$$ variables.
4. Using the recursive formula requires solving one $$n$$-th order initial value problem and then differentiating ($$n-1$$ functions total) and linearly combining functions.

I would say that, by hand, one $$n$$-th order IVP is better than $$n$$ first order IVPs (as well as $$n$$ $$n$$-th order IVPs of course).

Finally ranking them by which method would be best to use in my opinion:

|                  | $$n$$ $$n$$-th order IVPs | Wronskian inverse | $$n$$ first order IVPs | Recursive Formula |
|------------------|---------------------------|-------------------|------------------------|-------------------|
| By hand          | 4th                       | 3rd               | 2nd                    | 1st               |
| Using a computer | 4th                       | 2nd               | 1st                    | 3rd               |

For non-constant coefficients, the Wronskian inverse is really your only option.
