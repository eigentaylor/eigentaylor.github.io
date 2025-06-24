---
layout: distill
title: Constructing Systems of Nonlinear First-Order Differential Equations to Model Population Dynamics
date: 2020-11-30 0
description: Build a system with desired behavior.
comments: true
importance: 3
category: systems of differential equations
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: The Formula
  - name: Example
---

# The Formula

The nonlinear system of differential equations,

$$\begin{align*}
\frac{dx}{dt}=&\frac{x}{x_0}\big[F_{x1}(x-x_0)+F_{y1}(y-y_0)\big]\\
\frac{dy}{dt}=&\frac{y}{y_0}\big[G_{x1}(x-x_0)+G_{y1}(y-y_0)\big]\\
\end{align*}$$

will have a locally linear critical point at $$(0,0)$$ and $$(x_0,y_0)$$, for which the latter has a corresponding linear system

$$\begin{equation}
\frac{d}{dt}\begin{bmatrix}x-x_0\\y-y_0\end{bmatrix}
=\begin{bmatrix}F_{x1}&F_{y1}\\G_{x1}&G_{y1}\end{bmatrix}\begin{bmatrix}x-x_0\\y-y_0\end{bmatrix}
\end{equation}$$

If you have specific eigenvectors and eigenvalues in mind rather than a matrix, you can always turn to diagonalization:

$$\begin{equation}
\begin{bmatrix}F_{x1}&F_{y1}\\G_{x1}&G_{y1}\end{bmatrix}
=\bigg[\textbf{v}_1\quad \textbf{v}_2\bigg]
\begin{bmatrix}\lambda_1&0\\0&\lambda_2\end{bmatrix}
\bigg[\textbf{v}_1\quad \textbf{v}_2\bigg]^{-1}
\end{equation}$$

## Example

Let's take an example.

I want a system which behaves like the system

$$\begin{equation}
\frac{d}{dt}\begin{bmatrix}x\\y\end{bmatrix}
=\begin{bmatrix}0&1\\-1&0\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix}
\end{equation}$$

at the point $$(1,1)$$. This linear system has the behavior of concentric circles around the origin, so I expect there to be some cycling around my center point.

Using the formula that would give me

$$\begin{align*}
\frac{dx}{dt}=&x(y-1)\\
\frac{dy}{dt}=&-y(x-1)\\
\\
\frac{dx}{dt}=&-x+xy\\
\frac{dy}{dt}=&y-xy\\
\end{align*}$$

This happens to be a lucky case where we can fairly easily get an implicit solution :eyes:

Since 

$$\begin{equation}
\frac{dy}{dx}=\frac{\frac{dy}{dt}}{\frac{dx}{dt}}
\end{equation}$$

$$\begin{equation}
\frac{dy}{dx}=\frac{y(1-x)}{x(y-1)}
\end{equation}$$

And this is a separable equation. :eyes::eyes:

$$\begin{equation}
x+y-\ln(xy)=C
\end{equation}$$

If we suppose an arbitrary condition such as $$y(x_1)=y_1$$, then

$$\begin{equation}
(x-x_1)+(y-y_1)-\ln\left(\frac{xy}{x_1y_1}\right)=0
\end{equation}$$

Plotting various solutions with initial points in the first quadrant indeed, as we predicted, shows some cycling around the critical point $$(1,1)$$. Most initial points result in some pretty mishapen ellipse, but initial points very close to the critical point indeed approach something very close to a circle.