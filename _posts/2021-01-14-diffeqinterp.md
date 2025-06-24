---
layout: page
title: Linear Differential Equation Interpolation
date: 2021-01-14
description: Linear Differential Equations with desired solutions using determinants.
comments: true
importance: 4
categories: differential-equations
---

Homogeneous Solutions
-

If the functions $$\{y_1,\ldots,y_n\}$$ are linearly independent, then the $$n$$th-order linear differential equation

$$\begin{equation}
\begin{vmatrix}
y&y'&\dots&y^{(n)}\\
y_1&y_1'&\dots&y_1^{(n)}\\
\vdots&\vdots&\ddots&\vdots\\
y_n&y_n'&\dots&y_n^{(n)}\\
\end{vmatrix}=0
\end{equation}$$

has the solution

$$\begin{equation}
y=c_1y_1+\ldots+c_ny_n
\end{equation}$$

The proof is relatively trivial. Substituting the solution into the determinant makes the first row a linear combination of the other rows. Therefore the determinant will be zero.

Particular Solutions
-

The goal of interpolating a particular solution $$y_p$$ for a differential equation is that when we plug in $$y_p$$ to the differential equation we get the forcing function. So... we just do that.

If the functions $$\{y_1,\ldots,y_n,\}$$ are linearly independent, then the $$n$$th-order linear differential equation

$$\begin{equation}
\begin{vmatrix}
y&y'&\dots&y^{(n)}\\
y_1&y_1'&\dots&y_1^{(n)}\\
\vdots&\vdots&\ddots&\vdots\\
y_n&y_n'&\dots&y_n^{(n)}\\
\end{vmatrix}=
\begin{vmatrix}
y_p&y_p'&\dots&y_p^{(n)}\\
y_1&y_1'&\dots&y_1^{(n)}\\
\vdots&\vdots&\ddots&\vdots\\
y_n&y_n'&\dots&y_n^{(n)}\\
\end{vmatrix}
\end{equation}$$

has the solution

$$\begin{equation}
y=c_1y_1+\ldots+c_ny_n+y_p
\end{equation}$$

$$y_p$$ need not be independent from the homogeneous solutions. If it is, the  determinant of the right-hand side will be zero leading back to the other case.

Examples
-

1. Find a linear differential equation for which $$y_1=e^{at}$$ and $$y_2=e^{bt}$$ are homogeneous solutions. We know the answer will be $$(D-a)(D-b)y=0$$, but let's try the determinant.

    $$\begin{equation}\begin{vmatrix}
    y&y'&y''\\
    e^{at}&ae^{at}&a^2e^{at}\\
    e^{bt}&be^{bt}&b^2e^{bt}
    \end{vmatrix}=0
    \end{equation}$$ 

    Pulling the exponentials out,

    $$\begin{equation}
    e^{at}e^{bt}\begin{vmatrix}
    y&y'&y''\\
    1&a&a^2\\
    1&b&b^2
    \end{vmatrix}=0
    \end{equation}$$ 

    General exponentials are always nonzero, so we can safely divide them out.

    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        1&a&a^2\\
        1&b&b^2
        \end{vmatrix}=0
    \end{equation}$$

    Using determinant properties to simplify just a bit,

    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        1&a&a^2\\
        0&b-a&b^2-a^2
        \end{vmatrix}=0
    \end{equation}$$

    $$\begin{equation}
    (b-a)\begin{vmatrix}
        y&y'&y''\\
        1&0&-ab\\
        0&1&b+a
        \end{vmatrix}=0
    \end{equation}$$

    Finally, expanding along the top row,

    $$\begin{equation}
    (b-a)\left(\begin{vmatrix}0&-ab\\1&b+a\end{vmatrix}y-\begin{vmatrix}1&-ab\\0&a+b\end{vmatrix}y'+\begin{vmatrix}1&0\\0&1\end{vmatrix}y''\right)=0
    \end{equation}$$

    $$\begin{equation}
    (b-a)\left(y''-(a+b)y'+aby\right)=0
    \end{equation}$$

    Assuming $$a\neq b$$, we can divide out to get

    $$\begin{equation}
    y''-(a+b)y'+aby=0
    \end{equation}$$

    As expected.
        
    You will get the same result if $$a=b$$, and $$y_2=e^{at}(mt+c)$$ or something of that sort.

2. Find a linear differential equation for which $$y_1=x^{r}$$ and $$y_2=x^{r}\ln(x)$$  are homogeneous solutions.
    
    Setting up the determinant,

    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        x^r&rx^{r-1}&r(r-1)x^{r-2}\\
        x^r\ln(x)&rx^{r-1}\ln(x)+x^{r-1}&r(r-1)x^{r-2}\ln(x)+rx^{r-2}+(r-1)x^{r-2}
        \end{vmatrix}=0
    \end{equation}$$
        
    The third row has the second row times $$\ln(x)$$ added to it, so we can subtract it out.
        
    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        x^r&rx^{r-1}&r(r-1)x^{r-2}\\
        0&x^{r-1}&(2r-1)x^{r-2}
        \end{vmatrix}=0
    \end{equation}$$

    Factoring out,

    $$\begin{equation}
    x^{r-2}x^{r-2}\begin{vmatrix}
        y&y'&y''\\
        x^2&rx&r(r-1)\\
        0&x&(2r-1)
        \end{vmatrix}=0
    \end{equation}$$

    We can just divide out the powers of $$x$$, since $$x=0$$ is already out of our domain by having a factor of $$\ln(x)$$ as one of our solutions.

    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        x^2&0&-r^2\\
        0&x&(2r-1)
        \end{vmatrix}=0
    \end{equation}$$

    When expanded, we get

    $$\begin{equation}
    x^3y''-(2r-1)x^2y'+r^2xy=0
    \end{equation}$$

    Dividing out an $$x$$,

    $$\begin{equation}
    x^2y''-(2r-1)xy'+r^2y=0
    \end{equation}$$

3. Let's now find a differential equation for which the general solution is $$y=c_1\cos(x)+c_2\sin(x)+x\sin(x)+\cos(2x)$$. This would give us $$y_1=\cos(x)$$, $$y_2=\sin(x)$$, and $$y_p=x\sin(x)+\cos(2x)$$. 
    
    We start with zero on the right side even though we want a particular solution, since these simplification steps would be identical on both sides.

    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        \cos(x)&-\sin(x)&-\cos(x)\\
        \sin(x)&\cos(x)&-\sin(x)\\
        \end{vmatrix}=0
    \end{equation}$$

    $$\begin{equation}\begin{vmatrix}
        y&y'&y''\\
        \cos^2(x)&-\sin(x)\cos(x)&-\cos^2(x)\\
        \sin^2(x)&\sin(x)\cos(x)&-\sin^2(x)\\
        \end{vmatrix}=0
    \end{equation}$$
        

    $$\begin{equation}\begin{vmatrix}
        y&y'&y''\\
        \cos^2(x)&-\sin(x)\cos(x)&-\cos^2(x)\\
        \sin^2(x)+\cos^2(x)&0&-(\sin^2(x)+\cos^2(x))\\
        \end{vmatrix}=0
    \end{equation}$$
        
    $$\begin{equation}\begin{vmatrix}
        y&y'&y''\\
        0&-\sin(x)\cos(x)&0\\
        1&0&-1\\
        \end{vmatrix}=0
    \end{equation}$$
    
    $$\begin{equation}\begin{vmatrix}
        y&y'&y''\\
        0&1&0\\
        -1&0&1\\
        \end{vmatrix}=0
    \end{equation}$$

    Expanding along the second row,
    
    $$\begin{equation}\begin{vmatrix}
        y&y''\\
        -1&1\\
        \end{vmatrix}=0
    \end{equation}$$
        
    It is now a good time to get the particular solution determinants. By linearity, we can deal with them separately. 

    $$\begin{equation}\begin{vmatrix}
        y&y''\\
        -1&1\\
        \end{vmatrix}=\begin{vmatrix}
        x\sin(x)&-x\sin(x)+2\cos(x)\\
        -1&1\\
        \end{vmatrix}+\begin{vmatrix}
        \cos(2x)&-4\cos(2x)\\
        -1&1\\
        \end{vmatrix}
    \end{equation}$$
        
    $$\begin{equation}
    y''+y=2\cos(x)-3\cos(2x)
    \end{equation}$$

4. And as a final example, $$y_1=x+1$$, and $$y_2=e^x$$.

    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        x+1&1&0\\
        e^x&e^x&e^x
        \end{vmatrix}=0
    \end{equation}$$

    Dividing out $$e^x$$,

    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        x+1&1&0\\
        1&1&1
        \end{vmatrix}=0
    \end{equation}$$

    $$\begin{equation}
    \begin{vmatrix}
        y&y'&y''\\
        x+1&1&0\\
        -x&0&1
        \end{vmatrix}=0
    \end{equation}$$

    $$\begin{equation}
    \begin{vmatrix}
        1&0\\0&1
        \end{vmatrix}-y'\begin{vmatrix}
        x+1&0\\-x&1
        \end{vmatrix}+y''\begin{vmatrix}
        x+1&1\\
        -x&0
        \end{vmatrix}=0
    \end{equation}$$

    $$\begin{equation}
    xy''-(x+1)y'+y=0
    \end{equation}$$

Note that this is not limited to second-order equations. Evaluating the determinant just gets factorially more tedious as you add more solutions and I didn't want to deal with that because I am incredibly lazy.