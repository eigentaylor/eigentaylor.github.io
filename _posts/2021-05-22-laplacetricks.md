---
layout: distill
title: Tricks for Remembering Laplace Transforms
date: 2021-05-22
description: for students and people who forgot
comments: true
importance: 2
categories: differential-equations
tags: best 
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Intro
  - name: The Transforms to Memorize
    subsections:
      - name: Linearity
      - name: Powers of t
      - name: Exponential Shift
      - name: Derivatives
      - name: Multiplied By t
      - name: Polynomials
      - name: Exponentials
      - name: Hyperbolic Trig
  - name: Discontinuous Functions
    subsections:
      - name: The Dirac Delta Impulse Function
      - name: The Heaviside Step Function
  - name: The Convolution Integral
  - name: The Ladder
    subsections:
      - name: Differentiation in Physical Space
      - name: Differentiation in Frequency Space
      - name: Example of Using the Ladder
---

# Intro

I'm hoping some of my rambling sticks in your brain and helps you remember these rules. Or maybe you just see more of the connections between the formulas and think that's neat.

Obligatory definition of the Laplace Transform.
$$\newcommand{\a}{\alpha  }$$
$$\newcommand{\b}{\beta  }$$
$$\newcommand{\L}{\mathcal{L}  }$$
$$\newcommand{\laplace}[1]{\mathscr{L}\left\{ #1 \right\}}$$
$$\newcommand{\lapinv}[1]{\mathscr{L}^{-1}\left\{ #1 \right\}}$$
$$\newcommand{\Re}{\operatorname{Re}}$$
$$\newcommand{\Im}{\operatorname{Im}}$$
$$\newcommand{\conj}[1]{\overline{#1}}$$

\begin{equation} \label{def}
\laplace{f(t)}=\int_0^\infty e^{-st}f(t)\,dt
\end{equation}

I will generally stick to

$$\begin{equation*}
\laplace{f(t)}=F(s),\quad \lapinv{F(s)}=f(t)
\end{equation*}$$

but occasionally use $$\laplace{f(t)}$$ in place of $$F(s)$$ because I think it may be more helpful. Also I just like it.

I am going to denote the Dirac Delta (unit impulse) function and Heaviside (unit step) function as $$\delta(t-c)$$ and $$u(t-c)$$, respectively, and call them the "Dicontinuous Functions".

Also I'm going to assume that all the functions $$f(t)$$ satisfy the required conditions so that we can take the Laplace Transform. Exponential order and all that.

---

# The Transforms to Memorize

In my opinion, these are all the things you really need to get pretty much every Laplace Transform you'll probably use.

$$\begin{gather} \label{cis}
e^{bit}=\cos(bt)+i\sin(bt)\\ \label{lin}
\laplace{c_1f_1(t)+c_2f_2(t)}=c_1\laplace{f_1(t)}+c_2\laplace{f_2(t)} \\ \label{poly}
\laplace{t^n}=\frac{n!}{s^{n+1}}\\ \label{exp}
\laplace{e^{ct}f(t)}=F(s-c)\\ \label{prime}
\laplace{f'(t)}=sF(s)-f(0)\\ \label{ladder1}
\laplace{tf(t)}=-F'(s) \\ \label{step}
\laplace{u(t-c)f(t)}=e^{-cs}\laplace{f(t+c)} \\  \label{dirac}
\laplace{\delta(t-c)}=e^{-cs} \\
\end{gather}$$

Notice that I only have two explicit Laplace Transforms on here, \eqref{poly} and \eqref{dirac}, with the rest being rules of how common things *affect* Laplace Transforms (and also the illustrious [Euler's Formula](../eulersformula/){:target="_blank"}).

I'll go over some tips for how I remember the other important Laplace Transforms using these rules.

Also here are some inverse transforms I like to keep handy.

$$\begin{gather}
\lapinv{e^{-cs}\laplace{f(t)}}=u(t-c)f(t-c)\\\label{conv}
\lapinv{F(s)G(s)}=f*g=\int_0^tf(\tau)g(t-\tau)d\tau\\
\end{gather}$$

The second equation \eqref{conv} is the Convolution Integral. It's an incredibly useful tool for the generalizations of certain initial value problems, and can turn an inverse Laplace Transform problem into an integration problem. But I would consider it optional.

And finally, there is the "Ladder", as my former professor calls it. This will be detailed at the end and analyzes the affects of differentiation in physical an frequency space on Laplace Transforms. This can certainly speed up certain inverse Laplace Transforms, but I would not consider it necessary. You can usually get away with just knowing \eqref{prime} and \eqref{ladder1}.

First though, I will give some brief justifications for some of the first couple formulas.

## The First Set

### Linearity

$$\begin{gather*}
\laplace{c_1f_1(t)+c_2f_2(t)}\\
=c_1\laplace{f_1(t)}+c_2\laplace{f_2(t)}
\end{gather*}$$

This comes from the linearity of integration.

$$\int c_1f(x)+c_2g(x)dx=c_1\int f(x)dx+c_2\int g(x)dx$$

### Powers of t

$$\laplace{t^n}=\frac{n!}{s^{n+1}}$$

When integrating $$t^ne^{-st}$$, we use integration by parts. Differentiating $$t^n$$ will give us the $$n!$$, and integrating $$e^{-st}$$ will divide by $$s$$.

### Exponential Shift

$$\laplace{e^{ct}f(t)}=F(s-c)$$

Multiplying the integrand by $$e^{ct}$$ will just change $$e^{-st}$$ to $$e^{-(s-c)t}$$. So we need only replace every $$s$$ with an $$s-c$$ in the Laplace transform of $$f(t)$$.

### Derivatives

$$\laplace{f'(t)}=sF(s)-f(0)$$

This is another case of integration by parts, but instead we integrate $$f'(t)$$ and differentiate $$e^{-st}$$ which has the effect of multiplying by $$-s$$. I recommend actualy computing $$\int_0^\infty e^{-st}f'(t)\,dt$$ to see how it all shakes out to \eqref{prime}.

### Multiplied By t

$$\laplace{tf(t)}=-F'(s)$$

For this it's actually easier to go backwards. We can use the Leibniz integral rule to calculate the derivative of $$F(s)$$.

$$\frac{d}{ds}\int_0^\infty e^{-st}f(t)\,dt=\int_0^\infty \frac{\partial}{\partial s} e^{-st}f(t)\,dt$$

$$\frac{d}{ds}F(s)=\int_0^\infty -t e^{-st}f(t)\,dt$$

$$F'(s)=\laplace{-tf(t)}$$

So tl;dr differentiation under the integral sign.

I will discuss the step and impulse functions [later](#discontinuous-functions).

### Polynomials

I'm doing these first because it's from one of these transforms that we will get most of the others. By plugging in $$n=0$$ into \eqref{poly} (or alternatively just evaluating \eqref{def} with $$f(t)=1$$) we get

$$\begin{equation} \label{1}
\laplace{1}=\frac{1}{s}
\end{equation}$$

And to transform any polynomial, you can just use \eqref{lin} and \eqref{poly}:

$$\begin{equation*}
\laplace{c_0+c_1t+\ldots+c_nt^n}
\end{equation*}$$
$$\begin{equation}
=c_0\frac{1}{s}+c_1\frac{1}{s^2}+\ldots+c_n\frac{n!}{s^{n+1}}
\end{equation}$$

### Exponentials

These are arguably the most important. Fortunately, they are also the Laplace Transforms which are easiest to evaluate, assuming you know how to use [Euler's Formula](../eulersformula/){:target="_blank"} to [skip integration by parts](../eulersformulabyparts/){:target="_blank"}.

We will make heavy use of the incredible '**Exponential Shift**' rule, \eqref{exp}. To get the basic exponential, we use \eqref{exp} with the Laplace Transform of $$1$$, \eqref{1}.

$$\begin{equation}
\laplace{e^{at}}=\frac{1}{s-a}
\end{equation}$$

The clearly natural question I'm sure you were definitely asking yourself is "What happens when I put an imaginary value in there?" By real-izing the denominator with the complex conjugate we obtain

$$\begin{equation*}
\laplace{e^{bit}}=\frac{s+ib}{s^2+b^2}
\end{equation*}$$

You may be unimpressed, but we actually have both the transforms for $$\sin(bt)$$ and $$\cos(bt)$$. We just whip it out (it being [Euler's Formula](../eulersformula/){:target="_blank"} \eqref{cis}) and use \eqref{lin},

$$\begin{gather*}
\laplace{e^{bit}}=\laplace{\cos(bt)+i\sin(bt)}\\
\laplace{e^{bit}}=\laplace{\cos(bt)}+i\laplace{\sin(bt)}\\
\laplace{\cos(bt)}=\Re\left(\laplace{e^{bit}}\right)\\
\laplace{\sin(bt)}=\Im\left(\laplace{e^{bit}}\right)\\
\end{gather*}$$

$$\begin{gather}\label{trig}
\laplace{\cos(bt)}=\frac{s}{s^2+b^2}\\
\laplace{\sin(bt)}=\frac{b}{s^2+b^2}
\end{gather}$$

So instead of memorizing these formulas, I just remember that Euler's Identity leads to multiplying by the conjugate for the imaginary exponential case. Then I use the real part for $$\cos$$ and the imaginary part for $$\sin$$.

And why would we ever memorize *two more* formulas for $$e^{at}\sin(bt)$$ and $$e^{at}\cos(bt)$$ when we have our wonderful '**Exponential Shift**' rule, \eqref{exp}?

$$\begin{gather} \label{triga}
\laplace{e^{at}\cos(bt)}=\frac{s-a}{(s-a)^2+b^2}\\
\laplace{e^{at}\sin(bt)}=\frac{b}{(s-a)^2+b^2}
\end{gather}$$

### Hyperbolic Trig

**Fun fact:** We can write $$\sin(t)$$, $$\cos(t)$$, $$\sinh(t)$$, and $$\cosh(t)$$ in terms of simple exponentials like $$e^t$$.

$$\begin{align*}
\cosh(t)&=\frac{e^{t}+e^{-t}}{2}&\sinh(t)&=\frac{e^{t}-e^{-t}}{2}\\
\cos(t)&=\frac{e^{it}+e^{-it}}{2}&\sin(t)&=\frac{e^{it}-e^{-it}}{2i}
\end{align*}$$

You can get the bottom two formulas by solving for $$\sin(bt)$$ and $$\cos(bt)$$ in the two equations \eqref{cis} and $$e^{-bit}=\cos(bt)-i\sin(bt)$$, obtained by substituting $$-t$$ for $$t$$.

If you know they're not so different, it makes more sense that their Laplace Transforms are almost identical, and can be obtained literally by using \eqref{lin} and plugging in the Laplace Transforms for $$e^{\pm t}$$ and $$e^{\pm it}$$.

$$\begin{gather}
\laplace{e^{at}\cosh(bt)}=\frac{s-a}{(s-a)^2-b^2}\\
\laplace{e^{at}\sinh(bt)}=\frac{b}{(s-a)^2-b^2}
\end{gather}$$

Just flip the plus to a minus and you're done. And really, that's usually how it works out in the Calculus between the two sets of trig functions, because they are barely different.

---

## Discontinuous Functions

### The Dirac Delta Impulse Function
$$\delta(t)$$

This one's easy. Basically, you can get away with thinking of the Dirac Delta function as being defined to have a Laplace Transform of $$1$$.

So we're done! Bam!$$^{[1]}$$

$$\begin{equation}
\laplace{\delta(t)} =1
\end{equation}$$

<details>
  <summary style="color:white;">[1]</summary>
    <p>This is a gross oversimplification that you probably don't have to worry about.</p>
    <p>Also a really bad impluse pun.</p>
</details>

<br>

And interestingly enough, we get a sort of reverse exponential shift with \eqref{dirac}.

$$\laplace{\delta(t-c)}=e^{-cs}\laplace{\delta(t)}$$

Shifting the delta function in physical space is multiplying by $$e^{-cs}$$ in *frequency* space. I justify this by observing that it's basically a step function transformation: $$\delta(t-c)=u(t-c)\delta(t-c)$$, which we are going to be speaking about in the next section...

### The Heaviside Step Function
$$u(t)$$

This one is a bit trickier mostly because the way texts often write it is confusing and hard to apply, in my opinion. It's also the one that I feel is most easily forgettable. Technically, the rule is

$$\begin{equation} \label{badstep}
\laplace{u(t-c)f(t-c)} =e^{-ct}F(s)
\end{equation}$$

but that's only easy to apply for inverse Laplace Transforms. Otherwise, you have to go through hoops writing your function in terms of $$t-c$$. Just don't, and instead memorize \eqref{step}.

If it helps, I think of it as changing the lower bound on the Laplace Transform integral, because that's exactly what it is. Doing a probably-not-$$u$$-substitution of $$v=t-c\implies t=v+c$$ has the effect of being a regular Laplace Transform of the function shifted by $$c$$ and multiplied by an extra $$e^{-ct}$$, corresponding to how shifting an exponential is just scaling it. \eqref{badstep} is just the case where the *shifted* function is $$f(t)$$, so the only difference is being scaled by the exponential term $$e^{-ct}$$. I assume they do this because the math works out the nicest, but it's an awful rule to use to *evaluate* Laplace Transforms.

---

## The Convolution Integral

The proof that $$\laplace{f*g}=F(s)G(s)$$ is not something I want to go into here, but this fact can be incredibly useful for taking inverse Laplce Transforms, as we will see in [the ladder](#the-ladder).

The way I remember the Convolution Integral is through the Cauchy product of two infinite series$$^{[2]}$$.

<details>
  <summary style="color:white;">[2]</summary>
    <p>This is a lie. It's actually the other way around. I apologize for attempting to deceive you.</p>
</details>

$$\begin{equation*}
\left(\sum_{i=0}^\infty f_i\right)\cdot\left(\sum_{j=0}^\infty g_j\right)=
\sum_{k=0}^\infty\left(\sum_{m=0}^kf_mg_{k-m} \right)
\end{equation*}$$

If we examine that coefficient in the series on the right and, *arbitrarily* let $$k=t$$ and $$m=\tau$$.

$$\begin{equation*}
\sum_{\tau=0}^tf_\tau g_{t-\tau}
\end{equation*}$$

Then it looks *remarkably* similar to

$$\begin{equation*}
\int_0^tf(\tau)g(t-\tau)d\tau
\end{equation*}$$

The convolution just looks like the continuous version of the sum formula. It kind of makes sense that this is possible; integration is just a continuous summation, after all.

Also, the order of \eqref{conv} really doesn't matter. You can show that they are equal with a simple variable substitution. Just choose the order that makes the integral easiest to evaluate. Make good choices like letting the constant or exponential function take the $$t-\tau$$ argument.

$$\begin{equation}
f*g=\int_0^tf(\tau)g(t-\tau)d\tau
\end{equation}$$

Note that we can also say that

$$f*g=\int_0^tg(\tau)f(t-\tau)d\tau$$

---

## The Ladder

Here we discuss the effects of differentiation in physical and frequency space. Physical space being basically the $$t$$ domain and frequency space being the $$s$$ domain. These are helpful but uneccessary if you only need the basics. If it interests you, and you like big brain moves, however, read on.

### Differentiation in Physical Space

The rule most people (who know what a Laplace Transform is) are familiar with is \eqref{prime}, in which differentiation in physical space corresponds *basically* to multiplying by $$s$$ in frequency space.

As you repeat this process, you get this descending list of initial values as a polynomial in $$s$$.

$$\begin{align*}
\laplace{f''(t)}&=s\laplace{f'(t)}-f''(0)\\
\laplace{f''(t)}&=s(sF(s)-f'(0))-f''(0)\\
\laplace{f''(t)}&=s^2F(s)-sf'(0)-f''(0)\\
\end{align*}$$

You could prove by induction that

$$\begin{equation*}
\laplace{f^{(n)}(t)}
\end{equation*}$$
$$\begin{equation}
=s^nF(s)-s^{n-1}f(0)-\ldots-f^{(n-1)}(0)
\end{equation}$$

You may wonder, will $$\frac{F(s)}{s}$$ correspond to the Laplace Transform of the integral of $$f$$? Yeah, actually, kind of. There are a lot of ways to prove it, but I'm satisfied by viewing $$\frac{F(s)}{s}$$ as a convolution \eqref{conv}.

$$\begin{gather*}
\frac{F(s)}{s}=\laplace{f(t)}\laplace{1}\\
\frac{F(s)}{s}=\laplace{f*1}\\
\end{gather*}$$

$$\begin{equation}
\frac{F(s)}{s}=\laplace{\int_0^tf(\tau)d\tau}
\end{equation}$$

So in summary: differentiation in physical space is basically multiplying by the independent variable in frequency space. This relationship also works in reverse, so that integrating in physical space is dividing by the independent variable in frequency space.

### Differentiation in Frequency Space

There's an interesting symmetry in here. When you take the inverse laplace transform of a derivative in frequency space, $$F'(s)$$, that's multiplying by the (negative) independent variable in physical space.

$$\begin{align}
\laplace{f'(t)}&=sF(s)-f(0) \\ \label{sladderdown}
\lapinv{F'(s)}&=-tf(t) \\
\end{align}$$

Alternatively, you could view the effect of differentiation in one space as (sort of) corresponding to multiplying by the independent variable in the other.

$$\begin{equation}
\laplace{t^nf(t)}=(-1)^nF^{(n)}(s)
\end{equation}$$

You can use this when doing the inverse Laplace Transform. If what you have looks like the derivative of something you *do* know the inverse Laplace Transform of, \eqref{sladderdown} tells us it's just that multiplied by $$-t$$. Since Laplace Transforms usually have things going on in the denominator, the derivative is usually negative; so often we really have $$-F'(s)$$ meaning it's simply multiplying by just $$t$$. We can of course repeat this as many times as we want.

$$\begin{gather}
\lapinv{-F'(s)}=tf(t) \\
\lapinv{F^{(n)}(s)}=(-t)^nf(t)
\end{gather}$$

And yes, dividing $$f(t)$$ by $$t$$ when possible can correspond to integrating $$F(s)$$. This integral doesn't always converge, but it generally works out in theory, even if you have to sometimes disregard the lower bound.

$$\begin{equation}
\laplace{\frac{f(t)}{t}}=-\int_{-\infty}^sF(\tau)\,d\tau
\end{equation}$$

For example,

$$\laplace{\frac{\sin t}{t}}=\frac{\pi}{2}-\tan^{-1}s $$

### Example of Using the Ladder

For an example of applying this, do *not* waste your time doing partial fractions on

$$\begin{equation*}
F(s)=\frac{6s+24}{(s^2+8s+25)^2}
\end{equation*}$$

Any time you see a complicated $$F(s)$$ with a squared denominator, be suspicious. This is equivalent to
$$-\frac{d}{ds}\left(\frac{3}{s^2+8s+25}\right)$$
which is a nice derivative that gives us a nice inverse Laplace Transform after completing the square.

$$\begin{gather*}
\frac{6s+24}{(s^2+8s+25)^2}=-\frac{d}{ds}\left(\frac{3}{s^2+8s+25}\right)\\
F(s)=-\frac{d}{ds}\left(\frac{3}{(s+4)^2+9}\right)\\
F(s)=-\frac{d}{ds}\left(\laplace{e^{-4t}\sin(3t)}\right)\\
f(t)=te^{-4t}\sin(3t)
\end{gather*}$$
