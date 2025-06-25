---
layout: about
title: about
permalink: /
subtitle: i am a math phd student and tutor

profile:
  align: right
  image: eigenvector.png
  image_circular: false # crops the image to make it circular
  more_info: > 
    <p>Taylor Fisher</p> 
    <p>discord: eigentaylor</p>   
    <p>california CA</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: true
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

$$\exp(x)=\sum_{n=0}^\infty \frac{x^n}{n!}$$

math phd student, dork extraordinaire.

i like differential equations and linear algebra.

[here are some math posts ive written if you want to look at them i guess](./blog){:target="_blank"}

if you want to support me, i have a [ko-fi](https://ko-fi.com/eigentaylor){:target="_blank"}.

---

personal favorites:

- [Constant Coefficient ODEs Made Simple with Linear Operators](./blog/linalglinconstcoef){:target="_blank"}
- [Shortcuts for Finding Eigenvalues and Eigenvectors](./blog/eigentricks){:target="_blank"}
- [Solving systems of first-order ODEs like a baller](./blog/firstordersystemsquick){:target="_blank"}
- [The Alpha Method (Generalized Exponential Response Formula)](./blog/alphamethod){:target="_blank"}

---

my research stuff:

things ive ~~discovered~~ independently derived. i think they're all cool, but only a few of them are actually useful, in my opinion.

- [Function Interpolation](./blog/functioninterp){:target="_blank"}: a method to get a function (which is a linear combination of some given set of basis functions) that satisfies certain conditions using determinants, given that one exists and is unique. for example, a determinant which gives the unique lowest degree polynomial that passes through a certain set of points.

- [A formula for some particular solutions to certain ODEs](./blog/exppolynonhomo){:target="_blank"}: a determinant formula which gives a particular solution to any linear constant-coefficient ordinary differential equation which has a forcing function of exponential nature (ex. $$g(t)=t^ne^{\alpha t}\cos(\beta t)$$). Uses results from [Function Interpolation](./blog/functioninterp){:target="_blank"}.

- [Constructing integer systems of differential equations with integer solutions](./blog/firstordersystems){:target="_blank"}: methods to construct nice systems with nice solutions. useful for professors/textbook authors to make good lecture examples or exam problems. somewhat of a work in progress. i also have a post for [second order systems](./blog/secondordersystems){:target="_blank"}.

- matrix exponential stuff: i really love matrix exponentials.
1. [Matrix Exponential Formulas for 2x2 Matrices](./blog/2x2ezmatrixexp){:target="_blank"}
2. [Matrix Exponentials Using Differential Equations](./blog/matrixexpwde){:target="_blank"}
3. [Exponentials of Symmetric Matrices Using the Spectral Theorem](./blog/symmetric-exp){:target="_blank"}
4. [Matrix Exponential Formulas for 2x2 Matrices Using Laplace Transforms](./blog/ezmatrixexp){:target="_blank"}
5. Another approach to matrix exponential formulas: coming soon...

- [New Ways to Calculate Normalized Solutions to Linear Constant-Coefficient Differential Equations](./blog/newnormalized){:target="_blank"}: solve just *one* set of $$n$$ first-order initial value problems to get the $$n$$ normalized solutions to an $$n$$-th order differential equation. this should be the fastest way to find them using a computer. alternatively, find one normalized solution and get the others recursively.
