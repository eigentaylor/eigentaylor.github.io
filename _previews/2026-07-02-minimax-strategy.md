---
layout: distill
title: Strategic Resilience of the Better Choices System
date: 2026-07-02
description: A model of manipulability in the Better Choices voting system, and why it's so difficult.
importance: 3
tags: voting
category: polisci
featured: false
theorems: true
related_posts: true
pretty_table: true
exclude_appendix_from_word_count: true
exclude_footnotes_from_word_count: true
exclude_proof_blocks_from_word_count: true
bibliography: voting.bib
chart:
  plotly: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: Equal Vote Coalition (volunteer)
toc:
  - name: Introduction
    subsections:
      - name: Condorcet Methods
  - name: The Better Choices System
---

## Introduction

The [Better Choices system](../better-choices/){:target="_blank"} is a very interesting flavor of Condorcet where voters vote in all three head-to-head matchups between the candidates. The winner is the candidate who wins the most head-to-head matchups. If there is a tie, the winner is determined by minimax (the candidate with the least bad loss wins if every candidate loses at least one matchup).

For example, if Alice wins both of her head-to-head matchups against Bob and Clark, then Alice is the winner outright. Suppose instead that Alice beats Bob by 100 votes, Bob beats Clark by 200 votes, and Clark beats Alice by 300 votes. Then Bob loses by the least amount (100 votes) and is the winner by the minimax tiebreaker.

Unlike a typical Condorcet method, where voters submit rankings, voters in the Better Choices system can submit much more complex preferences that cannot be expressed in a simple ranking. For example, a voter can say they vote for Alice over Bob, Bob over Clark, and Clark over Alice. This is a perfectly valid ballot in the Better Choices system, but it is not a valid ranking because it is not transitive.

One might wonder if this system is *more* manipulable than a typical Condorcet method, since voters can submit more complex preferences. I will show that this system is no more manipulable than a typical Condorcet method, and the fact that the runoff is restricted to three candidates makes it extremely robust.

In this post, I define a model of strategic manipulation in this system and show that it is *very* difficult to manipulate. In practice, there is essentially no reason to vote in any way but with complete honesty.

I primarily focus on the three candidate case, but some of these results generalize beyond that. Warning to the reader: this post is a bit more technical than my usual posts.

## The Model

Rather than have a profile or voter-centric model, we focus entirely on the election results themselves. Precise margins are not as important as their relative sizes. Hence, we identify election states with a triple of pairs of the candidates. For simplicity, we define a state as a function

$$P:\left\{0,1,\ldots,\binom{n}{2}\right\}\to\{X_1,X_2,\ldots,X_n\}^2$$

which we denote suggestively, for example in $n=3$, as $(X_1>Y_1)<(X_2>Y_2)<(X_3>Y_3)$, where $X_i$ and $Y_i$ are distinct candidates. The interpretation is that $X_1$ defeats $Y_1$ by the smallest margin, $X_2$ defeats $Y_2$ by the middle margin, and $X_3$ defeats $Y_3$ by the largest margin. However, formally, we would say that $P(1)=(X_1,Y_1)$ and $P(1)(1)=X_1$ and $P(1)(2)=Y_1$, and similarly for $P(2)$ and $P(3)$. We force that $P(0)=(Y_1,X_1)$, the reverse of the smallest margin matchup.

Note that there are $\binom{3}{2}!\times 2^3=48$ possible states for 3 candidates, since there are $3!$ ways to order the matchups and $2^3$ ways to choose the winner of each matchup. In general, for $n$ candidates, there are $\binom{n}{2}!\times 2^{\binom{n}{2}}$ possible states.

The only way for the result of an election to possibly change is to change the relative sizes of the matchups. For example, if a coalition were to attempt to manipulate the election in $n=3$ by swapping their sincere votes for $Y_2>X_2$ with $X_2>Y_2$, then a sufficiently coordinated and large coalition might end up making the $X_2>Y_2$ matchup the largest margin, and the previous largest margin matchup $X_3>Y_3$ would then become the middle margin matchup. Or, perhaps, the coalition might be able to change sincere votes for $X_1>Y_1$ into $Y_1>X_1$, which would reverse the smallest margin matchup such that $P(1)=(Y_1,X_1)$, meaning that $Y_1$ now *defeats* $X_1$ by the smallest margin.

Focusing instead on individual voters, or ranking profiles, is not necessary or helpful. Particularly because all the matchups are independent, any possible margins list can be achieved by some profile of voters. Hence, we can focus entirely on the election results themselves, through the only method of manipulation: a coalition of voters changing their sincere votes to attempt to change the relative sizes of the matchups.

We can thus define the decision rule of the Better Choices system as a function where if $P$ has a Condorcet winner $X$ (i.e. if there exists two distinct $i,j$ such that $P(i)(1)=P(j)(1)=X$, meaning that $X$ defeats both of the other candidates), then $f(P)=X$. Otherwise, if $P$ has no Condorcet winner, then minimax determines $f(P)=P(1)(2)=P(0)(1)$, the candidate who loses by the least amount.

### Permutations of Matchups

We denote $$\sigma\in\{(0,1),(1,2),\ldots,(n-1,n)\}\subset S_{n+1}$$ as permutations on the matchups themselves, and we define

$$\sigma P(i)=P(\sigma(i))$$

For example, if $P=(A>B)<(B>C)<(C>A)$, then $(1,2)P=(B>C)<(A>B)<(C>A)$, and $(0,1)P=(B>A)<(B>C)<(C>A)$.

That is, permutations such as $(1,2)$ and $(2,3)$ swap the relative strengths of the matchups, while $(0,1)$ reverses the smallest matchup.

We are careful with compositions of permutations, since we always force that $P(0)$ be the mirror of $P(1)$. We typically consider only a single permutation of the matchups at a time.

We call a permutation $$\sigma=(i,i+1)$$ for $i>0$ a "swap of the first kind", and the permutation $(0,1)$ a "swap of the second kind". The first kind of swap preserves all current winners and losers of the matchups, while the second kind of swap changes the tournament structure of the matchups by reversing the smallest matchup.

### The Graph

Rather than considering the election states as a set of isolated nodes, we can consider them as a directed graph. The nodes are the election states, and the edges are the possible manipulations of the election. We can then ask questions about how easy it is to manipulate the election, and how many manipulations are required to achieve a profitable manipulation.

We define a directed graph on the set of all possible election states, where two states $P$ and $Q$ are connected by an edge if there exists a permutation $\sigma\in\{(0,1),(1,2),\ldots,(n-1,n)\}$ such that $Q=\sigma P$. That is, two states are connected if one can be obtained from the other by swapping the relative sizes of two matchups or reversing the smallest matchup.

We can understand this intuitively as $P$ being some sincere state of an election (where every voter is casting a fully honest ballot), and $Q$ being the result where a coalition of voters has insincerely changed their votes (deviated) such that they have successfully changed the relative sizes of the matchups. If $P$ and $Q$ are connected by an edge, then we say that $Q$ is achieved by a "simple manipulation" of $P$.

I remark that to even possibly do a simple manipulation, particularly in a large electorate, is going to be extremely difficult and require intense coordination. The goal of this post is to show just how futile such an effort is likely to be, even if it seemed possible to succeed.

Our question is when a coalition of voters can manipulate the election to change the winner profitably. That is, if $f(P)=X$ and $f(Q)=Y$, then we say that the coalition can manipulate the election from $P$ to $Q$ if $Y$ is preferred to $X$ by the coalition ($f(Q)\succ f(P)$, where we use $\succ$ to denote the manipulating coalition's preference). The work of Gibbard<d-cite key="gibbard1973manipulation"></d-cite> ensures that such manipulations are always possible, but we will show that they are *very* difficult to achieve in practice.

## Starting with a Condorcet Winner

We start with an extremely cheery theorem.

> **Theorem:** If $P$ has a Condorcet winner $X$, then there is no simple manipulation of $P$ that can profitably change the winner. That is, if $f(P)=X$ and $Q$ is connected to $P$ by an edge, then either $f(Q)=X$ or $f(P)\succ f(Q)$. In other words, $f(P)\succeq f(Q)$.

{% proof Click to expand proof %}
**Proof:** Suppose $P$ has a Condorcet winner $W$. Then $W$ wins both of its head-to-head matchups against the other two candidates. Hence, a swap of the first kind cannot change the winner, since it preserves all current winners and losers of the matchups. We thus only need to consider a swap of the second kind, which reverses the smallest matchup.

We consider three cases exhaustively. Let $X_1>Y_1$ be the smallest matchup, and $Q=(0,1)P$ be the result of the swap. Then we have three cases:

1. If $W\neq X_1$, then $W$ still wins both of their matchups after the swap, and hence is still the Condorcet winner.
2. If $W=X_1$, then $Y_1$ now wins their matchup against $W$. If this creates a cycle, then $f(Q)=Q(1)(2)=X_1=W$, and the winner is unchanged.
3. If $W=X_1$ and $Y_1$ becomes the new Condorcet winner, then $f(Q)=Y_1$. However, the swap of the second kind is only possible if the coalition sincerely preferred $X_1\succ Y_1$, and hence $f(P)\succ f(Q)$.

In all cases, we have $f(P)\succeq f(Q)$, and the theorem is proven. $\square$
{% endproof %}

The contrapositive of this theorem is that any profitable simple manipulation must start with a state that has no Condorcet winner, and must instead begin in a cycle. Cycles are empirically rare (in RCV elections, at least), and hence it seems unlikely that such a scenario is likely to occur. However, we can further show that the exact requirements for a cycle with profitable manipulations are even stricter still.

> **Corollary:** A simple manipulation using a swap of the second kind (reversing the smallest matchup) is never profitable.

{% proof Click to expand proof %}
**Proof:** The above theorem handles the case where $P$ has a Condorcet winner, so we only need to consider the case where $P$ has no Condorcet winner. Suppose $P$ has no Condorcet winner, and let $Q=(0,1)P$ be the result of a swap of the second kind.

If $Q$ is still in a cycle, then $f(P)=P(1)(2)=Y_1$ and $f(Q)=Q(1)(2)=X_1$. However, the swap of the second kind is only possible if the coalition sincerely preferred $X_1\succ Y_1$, but insincerely voted $Y_1\succ X_1$ to reverse it. Hence, $f(P)\succ f(Q)$, and the manipulation is not profitable.

If $Q$ now has a Condorcet winner, then that must be from $Y_1$ now winning their second matchup against $X_1$. Thus, $f(Q)=Y_1=f(P)$. Hence, the manipulation is not profitable. $\square$
{% endproof %}

This further narrows the field of possible ways to profitably manipulate the election. Not only must the election begin in a cycle, but it cannot be profitably changed by changing the winner of the weakest margin. The only remaining possibility is to swap the relative strengths of the existing matchups. But we have yet to eliminate all never-profitable manipulations.

**Lemma:** The permutation $(i,i+1)$ for $i>1$ never changes the winner of an election, and hence is never profitable.

{% proof Click to expand proof %}
**Proof:** If $P$ has a Condorcet winner, then the $(i,i+1)$ swap for $i>1$ preserves the winner, and hence is not profitable. If $P$ has no Condorcet winner, then $f(P)=P(1)(2)$. But $Q(1)=P(1)$, and hence $f(Q)=Q(1)(2)=P(1)(2)=f(P)$. Hence, the manipulation is not profitable. $\square$
{% endproof %}

Therefore, we need *only* consider the $(1,2)$ swap of the first kind, which swaps the relative strengths of the two weakest matchups, on $P$ which contains a cycle. We have eliminated $(0,1)$ and $(2,3),(3,4),\ldots,(n-1,n)$ as profitable manipulations, and hence we have reduced the field of possible profitable manipulations to a very small set of possibilities.

## Profitable Cycles

> **Theorem:** For $n=3$ candidates, there are exactly two $P$ out of the 48 total nodes which have a profitable simple manipulation, and they both contain a cycle. Specifically, they are
>
> 1. $P=(C>B)<(B>A)<(A>C)$, with $f(P)=B$ which can be manipulated to $Q=(B>A)<(C>B)<(A>C)$ with $f(Q)=A$ by voters who prefer $A\succ B\succ C$ choosing to insincerely vote $C\succ B$ instead of $B\succ C$.
> 2. $P=(B>C)<(A>B)<(C>A)$, with $f(P)=C$ which can be manipulated to $Q=(A>B)<(B>C)<(C>A)$ with $f(Q)=B$ by voters who prefer $A\succ B\succ C$ choosing to insincerely vote $B\succ A$ instead of $A\succ B$.

{% proof Click to expand proof %}
**Proof:** Based on our results above, we can restrict ourselves to considering cases where $f((1,2)P)\succ f(P)$, and $P$ has no Condorcet winner. Since $(1,2)$ is a swap of the first kind, $Q=(1,2)P$ must also be a cycle.

We then have that $f(P)=P(1)(2)=Y_1$ and $f(Q)=Q(1)(2)=Y_2$. Hence, we must have that a coalition of voters sincerely prefers $Y_2\succ Y_1$, but change their ballot in some other way. There are exactly two ways for a coalition to manipulate the election to achieve a $(1,2)$ swap.

| Manipulation         | Sincere Preference | Insincere Deviation |
|----------------------|--------------------|---------------------|
| Strengthen $X_1>Y_1$ | $Y_1\succ X_1$     | $X_1\succ Y_1$      |
| Weaken $X_2>Y_2$     | $X_2\succ Y_2$     | $Y_2\succ X_2$      |

We consider each case individually:

**Case 1**: Strengthen $X_1>Y_1$. In this case, the coalition must sincerely prefer $Y_1\succ X_1$, and prefer the altered outcome $Y_2\succ Y_1$. Hence, we must have that $Y_2\succ Y_1\succ X_1$. Let us label this preference $A\succ B\succ C$ ($A=Y_2$, $B=Y_1$, $C=X_1$). Then we have that $P(1)=(C,B)$ and $P(2)(2)=A$.

Using that $P$ is a cycle, meaning every candidate must lose exactly one matchup, we deduce that $Y_3=C$, $X_3=A$, and $P(2)(1)=B$. Hence, $P=(C>B)<(B>A)<(A>C)$, and $Q=(1,2)P=(B>A)<(C>B)<(A>C)$. This is one of the two profitable manipulations, where $f(P)=B$ and $f(Q)=A$. The manipulation done, specifically, by voters who sincerely prefer $B\succ C$ but insincerely vote $C\succ B$ instead. By burying their second favorite, they cause their favorite to win.

**Case 2**: Weaken $X_2>Y_2$. In this case, the coalition must sincerely prefer $X_2\succ Y_2$, and prefer the altered outcome $Y_2\succ Y_1$. Hence, we must have that $X_2\succ Y_2\succ Y_1$. Let us label this preference $A\succ B\succ C$ ($A=X_2$, $B=Y_2$, $C=Y_1$). Then we have that $P(2)=(A,B)$ and $P(1)(2)=C$.

Using that $P$ is a cycle, meaning every candidate must lose exactly one matchup, we deduce that $Y_3=C$, $X_3=A$, and $P(1)(1)=B$. Hence, $P=(B>C)<(A>B)<(C>A)$, and $Q=(1,2)P=(A>B)<(B>C)<(C>A)$. This is the second profitable manipulation, where $f(P)=C$ and $f(Q)=B$. The manipulation done, specifically, by voters who sincerely prefer $A\succ B$ but insincerely vote $B\succ A$ instead. By betraying their favorite, they allow their second favorite to win instead of their least favorite.
{% endproof %}

## Complex Manipulations

We have found exactly two states for $n=3$ that have a profitable simple manipulation. However, we can also ask if these two nodes are themselves reachable by manipulations from other nodes via the same coalition of voters. For example, is it possible for there to be a $P$ with a Condorcet winner such that by multiple manipulations, the coalition can eventually reach one of these two nodes and profitably change the winner?

The answer is yes. We can consider a "complex manipulation" to be a sequence of simple manipulations" where each intermediate node is weakly preferred to the previous node by the coalition. That is, if $P_0\to P_1\to\cdots\to P_k$ is a complex manipulation, then we have that $f(P_i)\succeq f(P_{i+1})$ for all $i<k$.

For the $P=(C>B)<(B>A)<(A>C)$ case, we can "move backwards" along the insincere misrepresentation of $C\succ B$, by fortifying the $B>C$ matchup. Hence, we get a chain

$$\begin{align*}
(B>A)<(C>B)<(A>C)&\leftarrow (C>B)<(B>A)<(A>C)\\
&\leftarrow (B>C)<(B>A)<(A>C)\\
&\leftarrow (B>A)<(B>C)<(A>C)\\
&\leftarrow (B>A)<(A>C)<(B>C)
\end{align*}$$

This gives four nodes for which a coalition of sufficient size who prefer $A\succ B\succ C$ can manipulate the election to achieve a profitable outcome, theoretically through a very large manipulation. That is, if the scenario is $(B>A)<(A>C)<(B>C)$, meaning that $B$ defeats $C$ by the largest margin, then if you can manage to convince a large enough coalition of $A\succ B\succ C$ voters to insincerely bury $B$ under $C$, such that $C$ eventually defeats $B$ by the second largest margin $(B>A)<(C>B)<(A>C)$, then you can indeed manipulate the election to achieve a profitable outcome. Perhaps this is achievable  in an election where the margins are particularly close together, but I find simple manipulations implausible enough already.

For the second profitable manipulation, $P=(B>C)<(A>B)<(C>A)$, we can similarly move backwards along the insincere misrepresentation of $B\succ A$, by fortifying the $A>B$ matchup, but this can only be done once. Hence, we get a chain

$$\begin{align*}
(A>B)<(B>C)<(C>A)&\leftarrow (B>C)<(A>B)<(C>A)\\
&\leftarrow (B>C)<(C>A)<(A>B)
\end{align*}$$

This gives us six nodes total. Six scenarios where, theoretically, a coalition of sufficient strength could employ some insincere strategy like burial or betrayal that, if strong enough to radically shift the margins, could achieve a profitable outcome. However, I find this to be an extremely unlikely scenario, and I do not see it as a practical concern.

### Generalizing to More Candidates

All of these theorems easily generalize to more than three candidates, except for the last theorem, which is specific to $n=3$. The first three theorems are independent of the number of candidates.

What we find is that the *only* way to potentially profit from a simple manipulation is to start in a cycle, and to swap the relative strengths of the two weakest matchups, which are structured precisely in such a way that

1. You *can* actually insincerely manipulate the election to achieve the swap, and
2. The coalition sincerely prefers the new winner to the old winner.

## Conclusion

In practice, to subvert or profitably manipulate this type of election, you would have to

1. Foresee that the election will produce a cycle
2. Be able to gauge the relative strengths of the matchups to know *which* two matchups are the weakest (and you better be sure about the order)
3. Be able to coordinate a large coalition of voters to insincerely change their votes in the exact right way to achieve the swap.
4. Have that coalition be sufficiently large that you can actually change the relative strengths of the matchups, and hopefully disturb nothing else in the election.

Or, if you somehow actually have the resources to perform a *strong* manipulation, then you still have to be quite confident about the relative margins of the other matchups.

I simply do not see this as a practical concern. If you are a voter voting in such an election, I cannot recommend enough that you vote sincerely. There is effectively no way to do this without an unrealistic amount of knowledge, foresight, confidence, and *resources*.

Just vote honestly. Vote for your favorite in their matchups. Vote for your second choice against your last choice.
