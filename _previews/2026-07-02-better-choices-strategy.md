---
layout: distill
title: Strategic Resilience of the Better Choices System
date: 2026-07-16
description: A model of manipulability in the Better Choices voting system, and why it's so difficult to game.
importance: 3
tags: voting
category: polisci
featured: false
theorems: true
bibliography: voting.bib
chart:
  plotly: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: Equal Vote Coalition (Volunteer)
toc:
  - name: Introduction
  - name: The Model
    subsections:
      - name: Permutations of Matchups
      - name: The Graph
  - name: Simple Manipulations
    subsections:
      - name: A Playground
  - name: Starting with a Condorcet Winner
  - name: Profitable Cycles
  - name: Complex Manipulations
  - name: Conclusion
  - name: Appendix
    subsections:
      - name: Just How Likely Are These Scenarios?
      - name: A Jupyter Notebook
      - name: Final Remarks
---

## Introduction

The [Better Choices system](../better-choices/){:target="_blank"} is a very interesting flavor of Condorcet where voters vote in all three head-to-head matchups between the candidates who make it to a top-3 runoff. I wrote about my complex thoughts on it in my last posts, but here I want to expound on the strategic resilience of the system.

The winner in this system is the candidate who wins both of their head-to-head matchups (a "Condorcet winner"). If there is a "tie"--where every candidate wins and loses exactly one matchup, and nobody wins both--the winner is determined by "minimax" (the candidate with the least bad loss wins if every candidate loses at least one matchup).

For example, if Alice wins both of her head-to-head matchups against Bob and Clark, then Alice is the winner outright. Suppose instead that Alice beats Bob by 10%, Bob beats Clark by 5%, and Clark beats Alice by 1%. Then Alice loses by the least amount (1%) and is the winner by the minimax tiebreaker.

As with any voting system, we can ask how manipulable the system is. That is, how much strategic pressure there is to spend the night before the election scheming up a complex strategy to game the election, or avoid walking into a trap where voting for your favorite candidate actually causes your least favorite candidate to win.

Compared to something like [Ranked-Choice Voting](../ditch-rcv/){:target="_blank"}, Condorcet methods are generally quite robust<d-cite key="brandt2025condorcet"></d-cite>.

But unlike a typical Condorcet method, where voters submit rankings, voters in the Better Choices system can submit much more complex preferences that cannot be expressed on a typical ranked ballot. For example, a voter can say they vote for Rock over Scissors, Scissors over Paper, and Paper over Rock. This is a perfectly valid ballot in the Better Choices system, but it is not a valid ranking because it is not transitive.

One might wonder if this system is *more* manipulable than a typical Condorcet method, since voters can submit more complex preferences. I will show that this system is no more manipulable than a typical Condorcet method, and the fact that the runoff is restricted to three candidates makes it even more robust.

In this post, I define a model of strategic manipulation in this system and show that it is *very* difficult to manipulate. In practice, there is essentially no reason to vote in any way but with complete honesty.

I primarily focus on the three candidate case, but some of these results generalize beyond that. Warning to the reader: this post is a bit more technical than my usual.

## The Model

Rather than have a profile or voter-centric model, we focus entirely on the election results themselves. Precise margins are not as important as their relative sizes (particularly for minimax). Hence, we identify election states with an ordered sequence of matchup results. For an election with $n$ candidates, we define a state as

$$P = \langle P_1 \mid P_2 \mid P_3 \rangle, \quad P_i = (w_i \to \ell_i)$$

where $w_i$ is the winner and $\ell_i$ is the loser of the $i$-th matchup, with matchups ordered so that $P_1$ has the smallest margin and $P_3$ has the largest. We write $\operatorname{win}(P_i)=w_i$ and $\operatorname{lose}(P_i)=\ell_i$. For example, the state $\langle C\to B \mid B\to A \mid A\to C\rangle$ means $C$ defeats $B$ by the smallest margin, $B$ defeats $A$ by the middle margin, and $A$ defeats $C$ by the largest margin. We also keep a mirror entry $P_0 = (\ell_1\to w_1)$, the reverse of the smallest-margin matchup.

Note that there are $\binom{3}{2}!\times 2^3=48$ possible states for 3 candidates, since there are $3!$ ways to order the matchups and $2^3$ ways to choose the winner of each matchup<d-footnote>We can also understand the collection of these states as equivalence classes of all possible elections that can happen in this system. For any election (neglecting any with tied margins), it must fall into one of these 48 states, based on the raw results and order of the margins.</d-footnote>. Out of the 48 nodes, 12 contain a cycle, and each candidate has 12 nodes in which they are a Condorcet winner. In general, for $n$ candidates, there are $\binom{n}{2}!\times 2^{\binom{n}{2}}$ possible states, which grows rapidly as $n$ increases. Already at $n=4$, there are over 46 thousand possible states. For this discussion, we will restrict ourselves to the $n=3$ case, as that is the proposal by Better Choices for Democracy<d-footnote>It also makes the analysis exceptionally simple. You can decide the <em>real</em> reason.</d-footnote>.

The only way for the result of an election to possibly change is to change the relative sizes of the matchups. For example, if a coalition were to attempt to manipulate the election in $n=3$ by swapping their sincere votes for $\ell_2\succ w_2$ with $w_2\succ \ell_2$, then a sufficiently coordinated and large coalition might end up making the $w_2\to\ell_2$ matchup the largest margin, and the previous largest margin matchup $P_3$ would then become the middle margin matchup. Or, perhaps, the coalition might be able to change sincere votes for $w_1\to\ell_1$ into $\ell_1\to w_1$, which would reverse the smallest margin matchup such that $P_1=(\ell_1\to w_1)$, meaning that $\ell_1$ now *defeats* $w_1$ by the smallest margin.

Focusing instead on individual voters, or ranking profiles, is not necessary or helpful, particularly because all the matchups are independent: any possible margins list can be achieved by some profile of voters. Hence, we can focus entirely on the election results themselves, through the only method of manipulation: a coalition of voters changing their sincere votes to attempt to change the relative sizes of the matchups.

> **Lemma:** For $n=3$ candidates, every cycle involves each candidate losing and winning exactly one matchup. Hence, for $n=3$, a candidate's worst loss and their only loss are the same thing.

We can thus define the decision rule of the Better Choices system as a function where if $P$ has a Condorcet winner $W$ (i.e. if there exist two distinct $i,j$ such that $\operatorname{win}(P_i)=\operatorname{win}(P_j)=W$, meaning that $W$ defeats both of the other candidates), then $f(P)=W$. Otherwise, if $P$ has no Condorcet winner, then minimax determines $f(P)=\operatorname{lose}(P_1)=\operatorname{win}(P_0)$, the candidate who loses by the least amount.

The question we investigate is not in the realm of game theory or psychology. Instead, we ask "if an omniscient coalition of voters had the ability to perfectly coordinate and execute a manipulation, would it be profitable for them to do so?"

### Permutations of Matchups

We denote $$\sigma\in\left\{(i,i+1): 0\leq i<m\right\}\subset S_{m+1}$$ as permutations on the matchups themselves, and we define

$$(\sigma P)_i = P_{\sigma(i)}$$

For example, if $P=\langle A\to B\mid B\to C\mid C\to A\rangle$, then $(2,3)P=\langle A\to B\mid C\to A\mid B\to C\rangle$, and $(0,1)P=\langle B\to A\mid B\to C\mid C\to A\rangle$.

That is, permutations such as $(1,2)$ and $(2,3)$ swap the relative strengths of the matchups, while $(0,1)$ reverses the smallest matchup.

We are careful with compositions of permutations, since we always force that $P_0$ be the mirror of $P_1$. We typically consider only a single permutation of the matchups at a time.

We call a permutation $$\sigma=(i,i+1)$$ for $i>0$ a "swap of the first kind", and the permutation $(0,1)$ a "swap of the second kind". The first kind of swap preserves all current winners and losers of the matchups, while the second kind of swap changes the tournament structure of the matchups by reversing the smallest matchup.

### The Graph

Rather than considering the election states as a set of isolated nodes, we can consider them as a directed graph. The nodes are the election states, and the edges are the possible manipulations of the election. We can then ask questions about how easy it is to manipulate the election, and how many manipulations are required to achieve a profitable manipulation.

We define a directed graph on the set of all possible election states, where two states $P$ and $Q$ are connected by an edge if there exists a permutation $$\sigma\in\{(0,1),(1,2),\ldots,(m-1,m)\}$$ such that $Q=\sigma P$. That is, two states are connected if one can be obtained from the other by swapping the relative sizes of two matchups or reversing the smallest matchup.

We can understand this intuitively as $P$ being some sincere state of an election (where every voter is casting a fully honest ballot), and $Q$ being the result where a coalition of voters has insincerely changed their votes (deviated) such that they have successfully changed the relative sizes of the matchups. If $P$ and $Q$ are connected by an edge, then we say that $Q$ is achieved by a "simple manipulation" of $P$.

I remark that to even possibly do a simple manipulation, particularly in a large electorate, is going to be extremely difficult and require intense coordination. The goal of this post is to show just how futile such an effort is likely to be, even if it seemed possible to succeed.

Our question is when a coalition of voters can manipulate the election to change the winner profitably. That is, if $f(P)=X$ and $f(Q)=Y$, then we say that the coalition can manipulate the election from $P$ to $Q$ if $Y$ is preferred to $X$ by the coalition ($f(Q)\succ f(P)$, where we use $\succ$ to denote the manipulating coalition's preference). The work of Gibbard<d-cite key="gibbard1973manipulation"></d-cite> ensures that no reasonable voting rule can escape manipulability entirely, but we will show how narrow the openings are here.

## Simple Manipulations

To define what a "profitable manipulation" truly is, we have to establish the perspective of the coalition who is attempting to game the system.

> **Definition:** A simple manipulation is **profitable** for a coalition if the winner of the election after the manipulation is strictly preferred by the coalition to the winner before the manipulation. That is, if $P$ and $Q$ are connected by an edge, then the manipulation from $P$ to $Q$ is profitable if $f(Q)\succ f(P)$.

For example, if $f(P)=B$ and $f(Q)=A$, then the manipulation from $P$ to $Q$ is profitable for a coalition with preference $A\succ B\succ C$, but not for a coalition with preference $B\succ A\succ C$<d-footnote>We assume the coalition has transitive preferences. However, technically, there isn't a strong reason to require this. But it simplifies the analysis, and is a reasonable assumption to make about voters.</d-footnote>.

We now have to connect what kinds of manipulations are possible by a fixed coalition of voters.

> **Lemma:** (One-Way Push) On each pair of candidates, the coalition can move the margin only **toward** its less preferred candidate. Therefore, a swap of the second kind (changing the smallest matchup from $w_1\to\ell_1$ to $\ell_1\to w_1$) is only achievable if the coalition sincerely prefers $w_1\succ\ell_1$. A swap of the first kind (swapping the relative sizes of $P_i$ and $P_{i+1}$ for $i>0$) is only achievable if the coalition sincerely prefers $w_{i+1}\succ \ell_{i+1}$ or $\ell_i\succ w_i$.\label{one-way-push}

{% proof Click to expand proof %}
**Proof**: To achieve a swap of the second kind, the initial sincere state must have more voters preferring $w_1\succ \ell_1$ than the opposite. To flip this, the coalition must initially be sincerely voting this way. Thus, the coalition must sincerely prefer $w_1\succ \ell_1$ to achieve a swap of the second kind.

For a swap of the first kind, there are two ways to achieve this.

| Manipulation                 | Sincere Preference      | Insincere Deviation      |
|------------------------------|-------------------------|--------------------------|
| Strengthen $w_i\to\ell_i$    | $\ell_i\succ w_i$       | $w_i\succ\ell_i$         |
| Weaken $w_{i+1}\to\ell_{i+1}$| $w_{i+1}\succ\ell_{i+1}$| $\ell_{i+1}\succ w_{i+1}$|

1. Strengthen the $w_i\to\ell_i$ matchup to be stronger than the $w_{i+1}\to\ell_{i+1}$ matchup. To do this, the coalition must initially be voting $\ell_i\succ w_i$, and flip their vote. Hence, they sincerely prefer $\ell_i\succ w_i$.
2. Weaken the $w_{i+1}\to\ell_{i+1}$ matchup to be weaker than the $w_i\to\ell_i$ matchup. To do this, the coalition must initially be voting $w_{i+1}\succ \ell_{i+1}$, and flip their vote. Hence, they sincerely prefer $w_{i+1}\succ \ell_{i+1}$. $\square$
{% endproof %}

Intuitively, we can imagine the manipulations that a coalition can do as only being able to "push" the margins away from their more preferred candidate and toward their less preferred candidate. If the election is three simultaneous games of tug-of-war, a sincere vote is pulling as hard as possible on the correct side of each rope. To manipulate the election is to let slack into the rope, in order to get a better outcome. You can't pull the rope any harder, but you can let it slacken.

## Starting with a Condorcet Winner

We start with an extremely cheery theorem.

> **Theorem:** For any $n\geq 3$, if $P$ has a Condorcet winner $W$, then there is no simple manipulation of $P$ that can profitably change the winner. That is, if $f(P)=W$ and $Q$ is connected to $P$ by an edge, then either $f(Q)=W$ or $f(P)\succ f(Q)$ ($f(P)\succeq f(\sigma P)$).\label{condorcet-stability}

{% proof Click to expand proof %}
**Proof:** Suppose $P$ has a Condorcet winner $W$. Then $W$ wins both of its head-to-head matchups against the other two candidates. Hence, a swap of the first kind cannot change the winner, since it preserves all current winners and losers of the matchups. We thus only need to consider a swap of the second kind, which reverses the smallest matchup.

We consider three cases exhaustively. Let $P_1=(w_1\to\ell_1)$ be the smallest matchup, and $Q=(0,1)P$ be the result of the swap. Then we have three cases:

1. If $W\neq w_1$, then $W$ still wins all of its matchups after the swap, and hence is still the Condorcet winner.
2. If $W=w_1$, then $\ell_1$ now wins their matchup against $W$. If this creates a cycle, then $w_1$ now has exactly one pairwise loss, which is the smallest margin of the whole election. Thus, $w_1$ will be chosen by the minimax tiebreaker and the winner is unchanged.
3. If $W=w_1$ and $\ell_1$ becomes the new Condorcet winner, then $f(Q)=\ell_1$. However, by lemma \ref{one-way-push}, this swap of the second kind is only possible if the coalition sincerely preferred $w_1\succ\ell_1$, and hence $w_1=f(P)\succ f(Q)=\ell_1$.

In all cases, we have $f(P)\succeq f(Q)$, and the theorem is proven. $\square$
{% endproof %}

And already, in most elections, we have proven there's no serious need for strategic voting.

We note that this theorem is only about *simple manipulations*--that is, a single swap of the first or second kind. We have not yet said anything about whether a manipulation that could perform a more radical adjustment to the matchups could be profitable. We will consider that question in the [Complex Manipulations](#complex-manipulations) section below (in fact, some nodes with a Condorcet winner *are* susceptible to profitable complex manipulations, theoretically gameable by a sufficiently massive coordinated coalition). However, if we assume that a coalition is only powerful enough to perform a single manipulation, then this theorem shows that the far and away most common scenario (starting with a Condorcet winner) is completely immune to profitable manipulation.

From another perspective, if we view this from the perspective that, as an individual voter, changing our one vote to something insincere is at most going to change the result via a single swap, then the theorem assures us that if there is a Condorcet winner, there is no reason not to just vote sincerely according to our true preferences. Any deviation from sincere voting, if it can only enact a simple manipulation, will lead to an outcome that is no better, or worse, than voting sincerely.

The contrapositive of this theorem is that any profitable simple manipulation must start with a state that has no Condorcet winner, and must instead begin in a cycle. Cycles are empirically rare (in RCV elections, at least), and hence it seems unlikely that such a scenario is likely to occur. However, we can further show that the exact requirements for a cycle with profitable manipulations are even stricter still.

> **Corollary:** A simple manipulation using a swap of the second kind (reversing the smallest matchup) is never profitable.\label{second-kind-manipulation}

{% proof Click to expand proof %}
**Proof:** The above theorem handles the case where $P$ has a Condorcet winner, so we only need to consider the case where $P$ has no Condorcet winner. Suppose $P$ has no Condorcet winner, and let $Q=(0,1)P$ be the result of a swap of the second kind.

For $n=3$, a cycle means that every candidate loses exactly one matchup. Hence, flipping any single matchup results in the existence of a Condorcet winner. In particular, because we have given $\ell_1$ the victory over $w_1$ by reversing the smallest matchup, $\ell_1$ now wins two matchups and is the Condorcet winner of $Q$. Hence, $f(Q)=\ell_1$. Thus, $f(Q)=\ell_1=f(P)$. Therefore, the manipulation is not profitable. $\square$
{% endproof %}

This further narrows the field of possible ways to profitably manipulate the election for $n=3$. Not only must the election begin in a cycle by Theorem \ref{condorcet-stability}, but it cannot be profitably changed by changing the winner of the weakest margin. The only remaining possibility is to swap the relative strengths of the existing matchups. But we have yet to eliminate all never-profitable manipulations.

> **Lemma:** A simple manipulation created by the permutation $(2,3)$ never changes the winner of an election, and hence is never profitable. For $n>3$, a manipulation of the form $(i,i+1)$ for $i>1$, can be profitable.\label{first-kind-manipulation}

{% proof Click to expand proof %}
**Proof:** If $P$ has a Condorcet winner, then the $(i,i+1)$ swap for $i>1$ preserves the winner, and hence is not profitable. If $P$ has no Condorcet winner, then $f(P)=\operatorname{lose}(P_1)$. But $Q_1=P_1$, and hence $f(Q)=\operatorname{lose}(Q_1)=\operatorname{lose}(P_1)=f(P)$. Hence, the manipulation is not profitable for $n=3$. 

Consider the following case for $n=4$:

1. $B\to A$ (smallest margin)
2. $C\to A$
3. $D\to A$
4. $B\to C$
5. $D\to B$
6. $C\to D$ (largest margin)

No candidate wins all of their matchups, so we examine the worst loss suffered by each candidate. In this case, all of $A$'s losses are by smaller margins than of any other candidate, so minimax would select $A$. But if we apply $(3,4)$, which swaps the third and fourth matchups, then $C$'s only loss becomes smaller than $A$'s worst loss, and hence $C$ is the new winner.

The manipulation would be possible if a coalition of voters who sincerely prefer $C\succ A\succ D$ were to insincerely vote $D\succ A$ in order to strengthen $A$'s loss to $D$ enough to make it worse than $C$'s loss to $B$, which would be profitable. $\square$
{% endproof %}

This is a stark case where the choice of $n=3$ elections is a benefit over taking the system to $n>3$ (at least with a minimax tiebreaker). In the original state, it had selected the Condorcet loser $A$, and was manipulated to pick someone else. This showcases how minimax is less robust for larger $n$, but is extremely robust for $n=3$ [due to its agreement with Ranked Pairs and Schulze](../better-choices/){:target="_blank"}<d-cite key="brandt2025condorcet"></d-cite>.

Therefore, for $n=3$, we need *only* consider the $(1,2)$ swap of the first kind, which swaps the relative strengths of the two weakest matchups, on $P$ which contains a cycle. We have eliminated $(0,1)$ and $(2,3)$ as profitable manipulations, and hence we have reduced the field of possible profitable manipulations to a very small set of possibilities.

## Profitable Cycles

> **Theorem:** For $n=3$ candidates, fix a coalition with preferences $A\succ B\succ C$. For this coalition, exactly two $P$ out of the 48 total nodes have a profitable simple manipulation for this coalition, and they both contain a cycle. Specifically, they are
>
> 1. $G_1=\langle C\to B\mid B\to A\mid A\to C\rangle$, with $f(G_1)=B$ which can be manipulated to $Q_1=\langle B\to A\mid C\to B\mid A\to C\rangle$ with $f(Q_1)=A$ by the coalition choosing to insincerely vote $C\succ B$ instead of $B\succ C$.
> 2. $G_2=\langle B\to C\mid A\to B\mid C\to A\rangle$, with $f(G_2)=C$ which can be manipulated to $Q_2=\langle A\to B\mid B\to C\mid C\to A\rangle$ with $f(Q_2)=B$ by the coalition choosing to insincerely vote $B\succ A$ instead of $A\succ B$.\label{profitable-cycles}

{% proof Click to expand proof %}
**Proof:** Based on our results above, we can restrict ourselves to considering cases where $f((1,2)P)\succ f(P)$, and $P$ has no Condorcet winner. Since $(1,2)$ is a swap of the first kind, $Q=(1,2)P$ must also be a cycle.

We then have that $f(P)=\operatorname{lose}(P_1)=\ell_1$ and $f(Q)=\operatorname{lose}(Q_1)=\ell_2$. To be profitable, we must have that the coalition of voters sincerely prefers $\ell_2\succ\ell_1$, and change their ballot in some way. There are exactly two ways for a coalition to manipulate the election to achieve a $(1,2)$ swap, as per lemma \ref{one-way-push}:

| Manipulation                | Sincere Preference  | Insincere Deviation | Outcome Change     |
|-----------------------------|---------------------|---------------------|--------------------|
| Strengthen $w_1\to\ell_1$   | $\ell_1\succ w_1$   | $w_1\succ\ell_1$    | $\ell_1\to \ell_2$ |
| Weaken $w_2\to\ell_2$       | $w_2\succ\ell_2$    | $\ell_2\succ w_2$   | $\ell_1\to \ell_2$ |

We consider each case individually:

**Case 1**: Strengthen $w_1\to\ell_1$. In this case, the coalition must sincerely prefer $\ell_1\succ w_1$, and prefer the altered outcome $\ell_2\succ\ell_1$. Hence, we must have that $\ell_2\succ\ell_1\succ w_1$. Let us label this preference $A\succ B\succ C$ ($A=\ell_2$, $B=\ell_1$, $C=w_1$). Then we have that $P_1=(C\to B)$ and $\operatorname{lose}(P_2)=A$.

Using that $P$ is a cycle, meaning every candidate must lose exactly one matchup, we deduce that $\ell_3=C$, $w_3=A$, and $\operatorname{win}(P_2)=B$. Hence, $P=\langle C\to B\mid B\to A\mid A\to C\rangle$, and $Q=(1,2)P=\langle B\to A\mid C\to B\mid A\to C\rangle$. This is one of the two profitable manipulations, where $f(P)=B$ and $f(Q)=A$. The manipulation is done, specifically, by voters who sincerely prefer $B\succ C$ but insincerely vote $C\succ B$ instead. By burying their second favorite, they cause their favorite to win.

**Case 2**: Weaken $w_2\to\ell_2$. In this case, the coalition must sincerely prefer $w_2\succ\ell_2$, and prefer the altered outcome $\ell_2\succ\ell_1$. Hence, we must have that $w_2\succ\ell_2\succ\ell_1$. Let us label this preference $A\succ B\succ C$ ($A=w_2$, $B=\ell_2$, $C=\ell_1$). Then we have that $P_2=(A\to B)$ and $\operatorname{lose}(P_1)=C$.

Using that $P$ is a cycle, meaning every candidate must lose exactly one matchup, we deduce that $\ell_3=C$, $w_3=A$, and $\operatorname{win}(P_1)=B$. Hence, $P=\langle B\to C\mid A\to B\mid C\to A\rangle$, and $Q=(1,2)P=\langle A\to B\mid B\to C\mid C\to A\rangle$. This is the second profitable manipulation, where $f(P)=C$ and $f(Q)=B$. The manipulation is done, specifically, by voters who sincerely prefer $A\succ B$ but insincerely vote $B\succ A$ instead. By betraying their favorite, they allow their second favorite to win instead of their least favorite.
{% endproof %}

Something worth observing is how $G_1$ and $G_2$ are mirror images of each other. The candidates in each matchup are the same, but the winners and losers are reversed. This can be achieved by taking an election in $G_1$ and reversing the preferences of all voters. In that sense, $G_1$ and $G_2$ are "dual" to each other, and the manipulations are also dual to each other.

Perhaps more intriguingly, the mirror symmetry extends to $Q_1$ and $Q_2$ as well, as does the manipulation. The mirror of a burial for a $A\succ B\succ C$ coalition is a betrayal for a $C\succ B\succ A$ coalition, and vice versa. What does not carry over is profitability.

This [interactive tool](https://eigentaylor.github.io/weakest-link/graph.html) visualizes these states and the manipulations available to a coalition preferring $A\succ B\succ C$.

### A Playground

If you are interested, you can use the playground below to see the profitable strategies in action. Suppose you are a voter who most prefers Alice, then Bob, then Clark. Then insincere voting would involve moving any of the sliders to the left.

<iframe id="condorcet-election-frame" src="/assets/html/condorcet-election.html?strategy"
  width="100%" height="480" scrolling="yes"
  frameborder="0"
  style="border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.18); display: block; margin-top: 1rem; overflow: hidden;"
  title="Interactive Condorcet/minimax election visualization">
</iframe>
<script>
window.addEventListener("message", function(e) {
  if (e.data && e.data.condorcetElectionHeight) {
    var f = document.getElementById("condorcet-election-frame");
    if (f) f.style.height = e.data.condorcetElectionHeight + "px";
  }
});
</script>
<br>

We also get a few corollaries from this result.

> **Corollary:** A node has a profitable simple manipulation for some coalition of voters if and only if it is cyclic. Further, that coalition is unique.

{% proof Click to expand proof %}
**Proof:** The proof for Theorem \ref{profitable-cycles} is exhaustive, and explicitly constructs the precise coalition preference which leads to a profitable simple manipulation for each cyclic node ($\ell_2\succ\ell_1\succ w_1$ or $w_2\succ\ell_2\succ\ell_1$). Using any relabeling of the candidates (from the six elements of $S_3$) will yield a unique alternate cycle structure and a new unique coalition. In total, this will yield $$\vert S_3\vert \cdot \vert\{G_1,G_2\}\vert=12$$ unique nodes, each containing a cycle. However, there are only 12 cyclic nodes total, so each cyclic $P$ must admit some profitable simple manipulation for some coalition. $\square$
{% endproof %}

We can thus say that in any cycle, there is some group who could stand to profit. However, this would require foreknowledge of both that there would be a cycle, and the exact cycle structure for that coalition to know a manipulation is even possible, in addition to the resources required to perform the manipulation.

> **Corollary:** For $n=3$ and a coalition of voters with preference $A\succ B\succ C$, the simple manipulation caused by performing a non-adjacent deviation of voting for $C$ over $A$ is never profitable. That is, submitting an intransitive ballot like $A\succ B$, $B\succ C$, and $C\succ A$ instead of the sincere $A\succ B$, $A\succ C$, and $B\succ C$ is never profitable for any $P$.\label{no-intransitive-manipulation}

{% proof Click to expand proof %}
**Proof:** Copying the logic from the proof of Theorem \ref{profitable-cycles}, suppose that $f(P)=\ell_1$ and $f(Q)=\ell_2$ for $Q=(1,2)P$, both cyclic scenarios. We want a profitable deviation, meaning the voters must prefer $\ell_2\succ\ell_1$. By lemma \ref{one-way-push}, the only way to achieve the $(1,2)$ swap is by either sincerely preferring

- $\ell_1\succ w_1$. For the manipulation to require betraying $A\succ C$, we need $A=\ell_1$ and $C=w_1$, or
- $w_2\succ\ell_2$ where, similarly, we would need $A=w_2$ and $C=\ell_2$.

For case 1: $A=\ell_1$ is the most preferred candidate, so we cannot have $\ell_2\succ\ell_1=A$.

For case 2: $C=\ell_2$ is the least preferred candidate, so we cannot have $\ell_2=C\succ\ell_1$.

Therefore, in both cases, we cannot have a profitable manipulation by insincerely voting $C\succ A$ instead of $A\succ C$. $\square$
{% endproof %}

We can thus guarantee that there is *never* a reason in any scenario to vote for your *least favorite candidate* over your *most favorite candidate*. This proves that, despite allowing greater expression than a ranked Condorcet method (in allowing intransitive ballots), this system is no more manipulable than a typical Condorcet method that uses a ranked ballot. Voting intransitively never provides an advantage in any scenario for $n=3$.

## Complex Manipulations

We have found exactly two states for $n=3$ that have a profitable simple manipulation per coalition. However, we can also ask if these two nodes are themselves reachable by manipulations from other nodes by the same coalition of voters. For example, is it possible for there to be a $P$ with a Condorcet winner such that by multiple manipulations, the coalition can eventually reach one of these two nodes and profitably change the winner?

The answer is yes--but since only one election ever really happens, we have to be careful about what a "complex manipulation" is. For this section, we will fix a coalition of voters with preference $A\succ B\succ C$, and also assume $n=3$ for the remainder of the discussion.

> **Definition:** Fix the sincere state $P_0$ (every voter, including the coalition, votes honestly), and define $R(P_0)$ as the set of states $Q$ the coalition can produce by chaining simple manipulations admissible by the one-way push lemma--treating $P_0$ itself as the ground truth, independently of what the one-way push lemma would allow at intermediate nodes. A **complex manipulation** is a state $Q\in R(P_0)$ with $f(Q)\succ f(P_0)$.

Though we have so far avoided talking about "margins", or specific profiles, it is worth considering that perspective here for intuitive purposes. We can imagine this as moving from $P_0$ to $Q$ through the coalition choosing to insincerely vote in various ways, changing the margins enough to reorder the matchups, or perhaps to flip some matchups which start out "favorable" to the coalition to be "unfavorable". We do not require that lies cannot be "undone", so long as at no point are the margins more favorable to the coalition than in $P_0$.

For example, if $A\to B$ is a sincere 71%-margin matchup--favoring the coalition who prefers $A\succ B$--in $P_0$, any intermediate margins can land anywhere from 71% for $A$ down to however far the coalition can force it toward $B$--including landing right back at 71% for $A$, by completely undoing all the lies. We only require that at no point can the margin be more than 71% for $A$.

> **Definition:** Fix a coalition with preference $A\succ B\succ C$. A matchup $w\to \ell$ is **concordant** (with the coalition) if the coalition prefers $w\succ \ell$, and **discordant** otherwise. The coalition's sincere ballot is to vote $A\succ B$, $A\succ C$, and $B\succ C$. A matchup is concordant exactly when its current winner is the candidate the coalition sincerely votes for in that pair.

Using "concordant" and "discordant" as defined above, we can characterize the states reachable from $P_0$ by the coalition's manipulations.

> **Lemma:** (Reachability) $Q\in R(P_0)$ if and only if
>
> **(a)** every matchup concordant in $Q$ is concordant in $P_0$; and
>
> **(b)** whenever $d$ is discordant in $P_0$, $c$ is concordant in $Q$, and $d$ outranks $c$ in $P_0$, then $d$ outranks $c$ in $Q$.\label{reachability}

{% proof Click to expand proof %}
**Proof:** By lemma \ref{one-way-push}, the coalition can only push a matchup's final value, relative to its $P_0$ value, toward the coalition's dispreferred candidate: a concordant matchup can only weaken (possibly flipping to discordant), and a discordant matchup can only strengthen. Hence, if a matchup ends up concordant in $Q$, it cannot possibly have been discordant in $P_0$, since the coalition could not have pushed it toward the preferred candidate. This proves **(a)**.

**(b):** a concordant matchup's value can only decrease from $P_0$ to $Q$, and a discordant one's can only increase. So if $d$ already outranks $c$ in $P_0$, then

$$\text{value}(d)_Q\geq\text{value}(d)_{P_0}>\text{value}(c)_{P_0}\geq\text{value}(c)_Q$$

and $d$ still outranks $c$ in $Q$. $\square$
{% endproof %}

A complex manipulation is profitable exactly when $Q$ satisfies (a) and (b) relative to $P_0$, and $f(Q)\succ f(P_0)$.

We note that $R$ is transitive: if $G\in R(P_0)$ and $Q\in R(G)$, then $Q\in R(P_0)$ (pushing further, in the same dispreferred direction, from an already-reachable state is still reachable from $P_0$--conditions (a) and (b) chain directly). This lets us reuse the two single-step profitable manipulations we already found:

> **Lemma:** (Gates) Every profitable complex manipulation passes through a gate: its first strictly-improving step is the simple manipulation out of $G_1$ (to $Q_1$) or out of $G_2$ (to $Q_2$).\label{gates}

{% proof Click to expand proof %}
**Proof:** By Theorem \ref{profitable-cycles}, these are the only two strictly $f$-improving edges in the entire deviation graph for this coalition. Any profitable path must contain at least one strictly improving step, and that step must be one of these two. $\square$
{% endproof %}

If $G_1\in R(P_0)$ and $f(P_0)\neq A$, then $Q_1\in R(P_0)$ and $f(Q_1)=A\succ f(P_0)$--a profitable complex manipulation. If $G_2\in R(P_0)$ and $f(P_0)=C$, then $Q_2\in R(P_0)$ and $f(Q_2)=B\succ C$--likewise profitable. Thus, the problem of classifying complex manipulations reduces to the problem of classifying for which states $P_0$ we have $G_1\in R(P_0)$ or $G_2\in R(P_0)$, with $f(G_1)\succeq f(P_0)$ or $f(G_2)\succeq f(P_0)$ respectively (since the gates themselves are not profitable, but the next step is). We are, for example, uninterested in $P_0$ with $f(P_0)=A$ that can reach $G_2$, since that would not be a profitable manipulation. One such example is

$$P_0=\langle C\to A\mid B\to C\mid A\to B\rangle \xrightarrow{C\succ A} \langle B\to C\mid A\to B\mid C\to A\rangle=G_2$$

achieved by the coalition insincerely voting $C\succ A$. The initial state $P_0$ has outcome $A$, and the gate $G_2$ has outcome $C$, which can be manipulated to $B$. But this is overall a loss for the coalition. Hence, we need $f(G_2)\succeq f(P_0)$ to ensure these are actually profitable manipulations.

So a state admits a profitable complex manipulation if and only if it can reach $G_1$ or $G_2$ without starting at a more preferable outcome--that is, we are really asking which states are *ancestors* of a gate ($P_0$ such that $G_i\in R(P_0)$ that have the same or a worse outcome than $G_i$), not which states a gate can reach.

> **Theorem:** For $n=3$ and a fixed coalition $A\succ B\succ C$, exactly six of the 48 states admit a profitable complex manipulation: $G_1$ and three ancestors of $G_1$:
>
> $$\langle B\to A\mid A\to C\mid B\to C\rangle \xrightarrow{C\succ B} \langle B\to A\mid B\to C\mid A\to C\rangle \xrightarrow{C\succ B} \langle B\to C\mid B\to A\mid A\to C\rangle \xrightarrow{C\succ B} G_1 \xrightarrow{C\succ B} Q_1$$
>
> (outcomes $B,B,B,B,A$ respectively). As well as $G_2$ and one ancestor of $G_2$:
>
> $$\langle B\to C\mid C\to A\mid A\to B\rangle \xrightarrow{B\succ A} G_2 \xrightarrow{B\succ A} Q_2$$
>
> (outcomes $C,C,B$ respectively).<d-footnote>By relabeling symmetry, each of the six coalition orders has its own version of these two chains, giving 36 (state, coalition) pairs across 30 distinct states: all 12 cyclic states (six of them manipulable this way by exactly two distinct coalitions) plus exactly half--18 of 36--of the Condorcet-winner states, each by a unique coalition. Machine-verified.</d-footnote>\label{complex-classification}

This was a machine-verified result, and is not worth the space to write out the full proof here (which would involve tedious backtracking). But you can see for yourself by following [this link](https://eigentaylor.github.io/weakest-link/graph.html), hovering over gates ($G_1$ and $G_2$), and then holding down the "ctrl" key to see the single step preimages of the gates, and following the paths backwards to weakly worse outcomes. $G_2$ has *one* $C$ outcome preimage, which only has an $A$ outcome preimage (which marks the end of the betrayal chain). $G_1$ can go back up to three steps, all with $B$ outcomes, before reaching a state with only an $A$ outcome preimage (which marks the end of the burial chain).

> **Corollary:** (Single-lie sufficiency) Every profitable complex manipulation can be reduced to a single lie told at increasing strength. The four burial-chain states are profitably manipulated by the lone insincere vote $C\succ B$ (burying $B$), pushed to increasing depth; the two betrayal-chain states by the lone insincere vote $B\succ A$ (betraying $A$). The six states differ only in *how far* the lie must be pushed--1 to 4 margin ranks.\label{single-lie}

{% proof Click to expand proof %}
**Proof:** Read the arrows in the chains above: every edge in the burial chain is the $C\succ B$ deviation applied with more mass; every edge in the betrayal chain is $B\succ A$. $\square$
{% endproof %}

You can also verify this yourself in [the playground](#a-playground): from the two scenarios, moving the sliders to the right (simulating moving backwards through a complex manipulation chain) does not ever make the outcome worse for the coalition.

Three of the four burial-chain states have a Condorcet winner--namely $B$, the coalition's *middle* candidate. This turns out to be the only way a Condorcet winner can be complexly overturned: it must be the coalition's middle choice, dragging the election into a cycle that resolves in the coalition's favor. When the coalition's *least favorite* candidate is the genuine Condorcet winner, the coalition is provably powerless--both $C$-class starting points are themselves cycles.

Perhaps it does not feel so cheery to be "powerless" to overturn the election when your least favorite candidate is the Condorcet winner, but perhaps from another perspective this is a comforting guarantee that a fringe group cannot spoil the election against the majority's clear preference. This is in contrast to [Ranked-Choice Voting](../ditch-rcv/){:target="_blank"}, where a Condorcet winner can sometimes be eliminated early due to vote splitting, allowing a less-preferred candidate to win.

> **Corollary:** (One-notch bound) A coalition can never improve the outcome by two notches via a complex manipulation. In particular, if $f(P_0)=C$ and $f(Q)=A$, then $Q\notin R(P_0)$.\label{one-notch}

{% proof Click to expand proof %}
**Proof:** Reaching outcome $A$ from a $P_0$ such that $A\succ f(P_0)$ requires passing through $G_1$, which contains $A\to C$. But any path out of the $C$-outcome class passes through $G_2$'s exit $Q_2=\langle A\to B\mid B\to C\mid C\to A\rangle$, which contains $C\to A$, contradicting the reachability lemma. $\square$
{% endproof %}

This result was also machine-verified. From $Q_2$, you can reach a few $B$-outcome states (none that can reach $G_1$), but eventually all paths lead to $C$-outcome state. This result also follows from the fact that $G_2\notin R(G_1)$.

Even a maximally resourced, perfectly informed coalition improves its outcome by at most one preference notch, and only from six of the forty-eight starting states, half of which are cycles.

We leave one final cheery corollary:

> **Corollary:** (No Favorite Betrayal Under a Condorcet Winner) If $P$ has a Condorcet winner, there is no profitable manipulation (complex or otherwise) for any coalition of voters involving betraying their favorite candidate in favor of a less-preferred candidate. That is, for any voter preferring $A\succ B\succ C$ in a state with a sincere Condorcet winner, then they can always vote $A\succ B$ and $A\succ C$ without fear of a profitable manipulation that would have been available had they instead voted $B\succ A$ or $C\succ A$.\label{no-favorite-betrayal}

{% proof Click to expand proof %}
**Proof:** This is also a machine-verified result, but there is some intuition for this. Gate 2 has two concordant matchups, and hence can only be reached from a state with two or more concordant matchups. If all three matchups are concordant, then $A$ would be a Condorcet winner, meaning there would be no profitable deviation from that node. Hence, any ancestor node where $A$ does not win must have the exact same matchup structure (a cycle). $\square$
{% endproof %}

Betrayal is only profitable if you happen to be in $G_2$, or its single cyclic ancestor (where $A$ is not the winner). This cyclic ancestor is *not reachable* from any state with a Condorcet winner that is not your favorite candidate.

### Generalizing to More Candidates

Some of these theorems do generalize beyond $n=3$, but many do not. If you can use this model to say more interesting things about Minimax for $n>3$, or perhaps generalize this model to say some interesting things about Ranked Pairs, let me know in the comments below! I developed a somewhat analogous model for IRV (Ranked-Choice Voting) and STAR voting, which I plan to write about in a future post.

## Conclusion

In practice, to subvert or profitably manipulate this type of election, you would first need the resources to organize widespread dishonesty (without tipping off opponents who could organize counterstrategy). But in addition to that, the amount of foreknowledge about the precise structure of the matchups is extensive--you'd need to know that a coalition with your exact preference ordering even has an opportunity to manipulate the election.

Further, the manipulations would require convincing voters to either vote for their least favorite over their backup choice, or to betray their favorite in favor of their second choice.

I simply do not see this as a practical concern. If you are a voter voting in such an election, I cannot recommend enough that you vote sincerely. There is effectively no way to game the result without an unrealistic amount of knowledge, foresight, confidence, and *resources*.

Just vote honestly. Vote for your favorite in its matchups. Vote for your second choice against your last choice. This system gives you the opportunity to have say in every single race, whether it is competitive or not. Don't think about strategy, just vote.

## Appendix

For the particularly technical readers, or those who want to look at pretty graphs, I have included a Jupyter notebook with the code and results for some simulations investigating the likelihood of these scenarios occurring in practice, and how detectable and affordable they are.

### Just How Likely Are These Scenarios?

The model I've developed is pure in the sense that it gives us the objective election states that *might* be manipulable, and the precise manipulations that *could* be profitable. This is a necessary condition, but it is not sufficient. For example, if we have a node at the start of a burial chain where $B$ is a Condorcet winner, then is it even necessarily possible that there are *enough* $A\succ B\succ C$ voters to even push the election into $Q_1$? If there are not, then the manipulation is not just impractical, but impossible.

To give at least a *basic* answer to this, we look at a few models for how voters might be distributed, and do some basic simulations.

We use a few different models for how voters might be distributed, including a few "impartial culture" models, a mallows model, and a spatial model. Impartial culture models ["maximize the probability of Condorcet cycles"](https://electowiki.org/wiki/Condorcet_paradox#Modeling_Condorcet_cycles), and hence these results are very likely upper bounds on the *actual* probability of these scenarios. All of this to say, please take the following results with a healthy dose of salt.

We investigate the following questions:

1. How likely are these manipulable scenarios to occur at all? Particularly, how common are cycles, the gates we have found, and the states that can reach the gates?
2. What do the *margins* tend to look like at these states? This tells us both how *feasible* it would be to manipulate, and simultaneously how *precise* the knowledge would have to be to both (a) know that the scenario is manipulable, and (b) know *exactly how much* to manipulate it.
3. What proportion of the $A\succ B\succ C$ voters would need to insincerely vote to enact the manipulation? This gives us a sense of how *practically* feasible the manipulation is (assuming the coalition had the perfect knowledge and resources to pull it off).

### A Jupyter Notebook

The following is a Jupyter notebook with the code and results for these simulations.

{::nomarkdown}
{% assign jupyter_path = 'assets/jupyter/better_choices_simulations.ipynb' | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/better_choices_simulations.ipynb %}{% endcapture %}
{% if notebook_exists == 'true' %}
  {% jupyter_notebook jupyter_path %}
{% else %}
  <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}

### Final Remarks

The lesson? When it comes to manipulation, you may pick at most one of the following:

1. The opportunity is likely
2. The opportunity is detectable in advance
3. The manipulation is affordable

Cycles are fairly rare. And even when a more common manipulable state occurs-- one with a Condorcet winner from the burial chain--it is exceptionally likely that the number of voters required to manipulate the election (pushing it into a cycle and beyond to $Q_1$) is more than the coalition can muster.

If a manipulation could be detected, then it generally requires more insincere voters than the coalition is likely to be able to coordinate.

If a manipulation is cheap, that means the margins are close (too close to identify in advance with any confidence<d-cite key="ShiraniMehrpolling"></d-cite>).

Note that this model says nothing about psychology or human messiness. Will voters naively attempt to game the system anyway? Perhaps, conditioned by choose-one voting, will they perform the betrayal because they believe their favorite is nonviable? Probably. And that could potentially harm the outcomes.

We must keep in mind that these are toy models. Impartial culture models are not exactly known for their realism, and even the more "realistic" models are still just that--models. The real world is messy, and there are many factors that could make these scenarios more or less likely, more or less detectable, and more or less affordable.

However, I do feel confident *enough* to say that voting insincerely in this system is more likely to make things worse than better. Just vote honestly.
