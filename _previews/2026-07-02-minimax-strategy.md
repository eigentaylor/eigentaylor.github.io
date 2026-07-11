---
layout: distill
title: Strategic Resilience of the Better Choices System
date: 2026-07-10
description: A model of manipulability in the Better Choices voting system, and why it's so difficult to game.
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
      name: Equal Vote Coalition (Volunteer)
toc:
  - name: Introduction
  - name: The Model
    subsections:
      - name: Permutations of Matchups
      - name: The Graph
  - name: Simple Manipulations
  - name: Starting with a Condorcet Winner
  - name: Profitable Cycles
  - name: Complex Manipulations
  - name: Conclusion
---

## Introduction

The [Better Choices system](../better-choices/){:target="_blank"} is a very interesting flavor of Condorcet where voters vote in all three head-to-head matchups between the candidates who make it to a top-3 runoff. I wrote about my complex thoughts on it in my last posts, but here I want to expound on the strategic resilience of the system.

The winner in this system is the candidate who wins both of their head-to-head matchups (a "Condorcet winner"). If there is a tie, and nobody wins both, the winner is determined by minimax (the candidate with the least bad loss wins if every candidate loses at least one matchup).

For example, if Alice wins both of her head-to-head matchups against Bob and Clark, then Alice is the winner outright. Suppose instead that Alice beats Bob by 10%, Bob beats Clark by 5%, and Clark beats Alice by 1%. Then Alice loses by the least amount (1%) and is the winner by the minimax tiebreaker.

As with any voting system, we can ask how manipulable the system is. That is, how much strategic pressure there is to spend the night before the election scheming up a complex strategy to game the election, or avoid walking into a trap where voting for your favorite candidate actually causes your least favorite candidate to win.

Compared to something like [Ranked-Choice Voting](../ditch-rcv/){:target="_blank"}, Condorcet methods are generally quite robust<d-cite key="brandt2025condorcet"></d-cite>.

But unlike a typical Condorcet method, where voters submit rankings, voters in the Better Choices system can submit much more complex preferences that cannot be expressed on a typical ranked ballot. For example, a voter can say they vote for Rock over Scissors, Scissors over Paper, and Paper over Rock. This is a perfectly valid ballot in the Better Choices system, but it is not a valid ranking because it is not transitive.

One might wonder if this system is *more* manipulable than a typical Condorcet method, since voters can submit more complex preferences. I will show that this system is no more manipulable than a typical Condorcet method, and the fact that the runoff is restricted to three candidates makes it even more robust.

In this post, I define a model of strategic manipulation in this system and show that it is *very* difficult to manipulate. In practice, there is essentially no reason to vote in any way but with complete honesty.

I primarily focus on the three candidate case, but some of these results generalize beyond that. Warning to the reader: this post is a bit more technical than my usual.

## The Model

Rather than have a profile or voter-centric model, we focus entirely on the election results themselves. Precise margins are not as important as their relative sizes (particularly for minimax). Hence, we identify election states with an ordered sequence of matchup results. We define a state as

$$P = \langle P_1 \mid P_2 \mid \cdots \mid P_m \rangle, \quad P_i = (w_i \to \ell_i), \quad m = \tbinom{n}{2}$$

where $w_i$ is the winner and $\ell_i$ is the loser of the $i$-th matchup, with matchups ordered so that $P_1$ has the smallest margin and $P_m$ has the largest. We write $\operatorname{win}(P_i)=w_i$ and $\operatorname{lose}(P_i)=\ell_i$. For example in $n=3$, the state $\langle C\to B \mid B\to A \mid A\to C\rangle$ means $C$ defeats $B$ by the smallest margin, $B$ defeats $A$ by the middle margin, and $A$ defeats $C$ by the largest margin. We also keep a mirror entry $P_0 = (\ell_1\to w_1)$, the reverse of the smallest-margin matchup.

Note that there are $\binom{3}{2}!\times 2^3=48$ possible states for 3 candidates, since there are $3!$ ways to order the matchups and $2^3$ ways to choose the winner of each matchup. Out of the 48 nodes, 12 contain a cycle, and each candidate has 12 nodes in which they are a Condorcet winner. In general, for $n$ candidates, there are $\binom{n}{2}!\times 2^{\binom{n}{2}}$ possible states, which grows rapidly as $n$ increases. Already at $n=4$, there are over 46 thousand possible states.

The only way for the result of an election to possibly change is to change the relative sizes of the matchups. For example, if a coalition were to attempt to manipulate the election in $n=3$ by swapping their sincere votes for $\ell_2\succ w_2$ with $w_2\succ \ell_2$, then a sufficiently coordinated and large coalition might end up making the $w_2\to\ell_2$ matchup the largest margin, and the previous largest margin matchup $P_3$ would then become the middle margin matchup. Or, perhaps, the coalition might be able to change sincere votes for $w_1\to\ell_1$ into $\ell_1\to w_1$, which would reverse the smallest margin matchup such that $P_1=(\ell_1\to w_1)$, meaning that $\ell_1$ now *defeats* $w_1$ by the smallest margin.

Focusing instead on individual voters, or ranking profiles, is not necessary or helpful. Particularly because all the matchups are independent, any possible margins list can be achieved by some profile of voters. Hence, we can focus entirely on the election results themselves, through the only method of manipulation: a coalition of voters changing their sincere votes to attempt to change the relative sizes of the matchups.

We can thus define the decision rule of the Better Choices system as a function where if $P$ has a Condorcet winner $W$ (i.e. if there exist two distinct $i,j$ such that $\operatorname{win}(P_i)=\operatorname{win}(P_j)=W$, meaning that $W$ defeats both of the other candidates), then $f(P)=W$. Otherwise, if $P$ has no Condorcet winner, then minimax determines $f(P)=\operatorname{lose}(P_1)=\operatorname{win}(P_0)$, the candidate who loses by the least amount.

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

> **Definition:** Fix a coalition with preference $A\succ B\succ C$. A matchup $w\to \ell$ is **concordant** (with the coalition) if the coalition prefers $w\succ \ell$, and **discordant** otherwise. The coalition's sincere ballot is to vote $A\succ B$, $A\succ C$, and $B\succ C$. A matchup is concordant exactly when its current winner is the candidate the coalition sincerely votes for in that pair.

Note: we assume the coalition has transitive preferences. However, technically, there is not a particular reason to require this. But it simplifies the analysis, and is a reasonable assumption to make about voters.

To define what a "profitable manipulation" truly is, we have to establish the perspective of the coalition who is attempting to game the system.

> **Definition:** A simple manipulation is **profitable** for a coalition if the winner of the election after the manipulation is strictly preferred by the coalition to the winner before the manipulation. That is, if $P$ and $Q$ are connected by an edge, then the manipulation from $P$ to $Q$ is profitable if $f(Q)\succ f(P)$.

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

## Starting with a Condorcet Winner

We start with an extremely cheery theorem.

> **Theorem:** If $P$ has a Condorcet winner $W$, then there is no simple manipulation of $P$ that can profitably change the winner. That is, if $f(P)=W$ and $Q$ is connected to $P$ by an edge, then either $f(Q)=W$ or $f(P)\succ f(Q)$ ($f(P)\succeq f(\sigma P)$).\label{condorcet-stability}

{% proof Click to expand proof %}
**Proof:** Suppose $P$ has a Condorcet winner $W$. Then $W$ wins both of its head-to-head matchups against the other two candidates. Hence, a swap of the first kind cannot change the winner, since it preserves all current winners and losers of the matchups. We thus only need to consider a swap of the second kind, which reverses the smallest matchup.

We consider three cases exhaustively. Let $P_1=(w_1\to\ell_1)$ be the smallest matchup, and $Q=(0,1)P$ be the result of the swap. Then we have three cases:

1. If $W\neq w_1$, then $W$ still wins both of their matchups after the swap, and hence is still the Condorcet winner.
2. If $W=w_1$, then $\ell_1$ now wins their matchup against $W$. If this creates a cycle, then $f(Q)=\operatorname{lose}(Q_1)=w_1=W$, and the winner is unchanged.
3. If $W=w_1$ and $\ell_1$ becomes the new Condorcet winner, then $f(Q)=\ell_1$. However, by lemma \ref{one-way-push}, this swap of the second kind is only possible if the coalition sincerely preferred $w_1\succ\ell_1$, and hence $w_1=f(P)\succ f(Q)=\ell_1$.

In all cases, we have $f(P)\succeq f(Q)$, and the theorem is proven. $\square$
{% endproof %}

The contrapositive of this theorem is that any profitable simple manipulation must start with a state that has no Condorcet winner, and must instead begin in a cycle. Cycles are empirically rare (in RCV elections, at least), and hence it seems unlikely that such a scenario is likely to occur. However, we can further show that the exact requirements for a cycle with profitable manipulations are even stricter still.

> **Corollary:** A simple manipulation using a swap of the second kind (reversing the smallest matchup) is never profitable for $n=3$. It can be profitable for $n>3$.\label{second-kind-manipulation}

{% proof Click to expand proof %}
**Proof:** The above theorem handles the case where $P$ has a Condorcet winner, so we only need to consider the case where $P$ has no Condorcet winner. Suppose $P$ has no Condorcet winner, and let $Q=(0,1)P$ be the result of a swap of the second kind.

For $n=3$, a cycle means that every candidate loses exactly one matchup. Hence, flipping any single matchup results in the existence of a Condorcet winner. In particular, because we have given $\ell_1$ the victory over $w_1$ by reversing the smallest matchup, $\ell_1$ now wins two matchups and is the Condorcet winner of $Q$. Hence, $f(Q)=\ell_1$. Thus, $f(Q)=\ell_1=f(P)$. Therefore, the manipulation is not profitable.

Consider $n=4$. For $n=4$, it's possible to flip a matchup in a cycle and stay in a cycle, in which case this is genuinely profitable. If $f(P)=\operatorname{lose}(P_1)=\ell_1$ and $Q=(0,1)P$, then $f(Q)=\operatorname{lose}(Q_1)=w_1$. By lemma \ref{one-way-push}, the coalition must sincerely prefer $w_1\succ\ell_1$ to perform a swap of the second kind. Thus, $f(Q)=w_1\succ\ell_1=f(P)$, and the manipulation is profitable. $\square$
{% endproof %}

This is a stark case where the choice of $n=3$ elections is a benefit over taking the system to $n>3$ (at least with a minimax tiebreaker). This showcases how minimax is less robust for larger $n$, but is extremely robust for $n=3$ [due to its agreement with Ranked Pairs and Schulze](../better-choices/){:target="_blank"}<d-cite key="brandt2025condorcet"></d-cite>.

This further narrows the field of possible ways to profitably manipulate the election for $n=3$. Not only must the election begin in a cycle by Theorem \ref{condorcet-stability}, but it cannot be profitably changed by changing the winner of the weakest margin. The only remaining possibility is to swap the relative strengths of the existing matchups. But we have yet to eliminate all never-profitable manipulations.

> **Lemma:** A simple manipulation created by the permutation $(i,i+1)$ for $i>1$ never changes the winner of an election, and hence is never profitable for any $n$.\label{first-kind-manipulation}

{% proof Click to expand proof %}
**Proof:** If $P$ has a Condorcet winner, then the $(i,i+1)$ swap for $i>1$ preserves the winner, and hence is not profitable. If $P$ has no Condorcet winner, then $f(P)=\operatorname{lose}(P_1)$. But $Q_1=P_1$, and hence $f(Q)=\operatorname{lose}(Q_1)=\operatorname{lose}(P_1)=f(P)$. Hence, the manipulation is not profitable. $\square$
{% endproof %}

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

This [interactive tool](https://eigentaylor.github.io/weakest-link/graph.html) visualizes these states and the manipulations available to a coalition preferring $A\succ B\succ C$.

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

We can thus say that in any cycle, there is some group who could stand to profit. However, this would require foreknowledge of the exact cycle structure for that coalition to know a manipulation is even possible, in addition to the resources required to perform the manipulation.

> **Corollary:** For a coalition of voters with preference $A\succ B\succ C$, the simple manipulation caused by performing a non-adjacent deviation of voting for $C$ over $A$ is never profitable. That is, a coalition of voters who sincerely prefer $A\succ B\succ C$ can never profitably manipulate the election by insincerely voting $C\succ A$ instead of $A\succ C$.

{% proof Click to expand proof %}
**Proof:** Copying the logic from the proof of Theorem \ref{profitable-cycles}, suppose that $f(P)=\ell_1$ and $f(Q)=\ell_2$ for $Q=(1,2)P$, both cyclic scenarios. We want a profitable deviation, meaning the voters must prefer $\ell_2\succ\ell_1$. By lemma \ref{one-way-push}, the only way to achieve the $(1,2)$ swap is by either sincerely preferring

- $\ell_1\succ w_1$. For the manipulation to require betraying $A\succ C$, we need $A=\ell_1$ and $C=w_1$, or
- $w_2\succ\ell_2$ where, similarly, we would need $A=w_2$ and $C=\ell_2$.

For case 1: $A=\ell_1$ is the most preferred candidate, so we cannot have $\ell_2\succ\ell_1=A$.

For case 2: $C=\ell_2$ is the least preferred candidate, so we cannot have $\ell_2=C\succ\ell_1$.

Therefore, in both cases, we cannot have a profitable manipulation by insincerely voting $C\succ A$ instead of $A\succ C$. $\square$
{% endproof %}

We can thus guarantee that there is *never* a reason in any scenario to vote for your *least favorite candidate* over your *most favorite candidate*. This proves that this system is no more manipulable than a typical Condorcet method, but is in fact *less* manipulable than some Condorcet methods involving four or more candidates.

## Complex Manipulations

We have found exactly two states for $n=3$ that have a profitable simple manipulation per coalition. However, we can also ask if these two nodes are themselves reachable by manipulations from other nodes by the same coalition of voters. For example, is it possible for there to be a $P$ with a Condorcet winner such that by multiple manipulations, the coalition can eventually reach one of these two nodes and profitably change the winner?

The answer is yes. We can consider a "complex manipulation" to be a sequence of simple manipulations where the final state is strictly preferred to the initial state by the coalition. That is, if $P^{(0)}\to P^{(1)}\to\cdots\to P^{(k)}$ is a complex manipulation, then we have that $f(P^{(k)})\succ f(P^{(0)})$. We place no requirement on intermediate states--only the endpoint matters.<d-footnote>It turns out this makes no difference: the six profitable states below are the same whether one requires every intermediate state to be weakly preferred, or only that the final state beat the initial one. The necessary conditions used in the classification theorem are conditions on the starting state alone (the ratchets below are path-independent), so allowing non-monotone dips can't enlarge the set of profitable starting states; and the chains exhibited below are already monotone, so requiring monotonicity can't shrink it either.</d-footnote>

To see exactly which states these are, we need one more piece of machinery: a sense of which way a coalition's lies can push a matchup, and how that accumulates over a sequence of deviations.

> **Lemma:** (Ratchets) Along any sequence of deviations available to a fixed coalition:
>
> **(R1, direction ratchet)** each matchup changes direction at most once, from concordant to discordant. Discordance is permanent--once the coalition has flipped $A\to C$ into $C\to A$, no further deviation by this coalition can ever restore $A\to C$.
>
> **(R2, rank ratchet)** the relative margin order of a discordant matchup $d$ and a concordant matchup $c$ can change only by $d$ rising above $c$. Once a discordant matchup outranks a concordant one, that order is permanent.\label{ratchets}

{% proof Click to expand proof %}
**Proof:** By lemma \ref{one-way-push}, the coalition can only push a margin toward its dispreferred candidate.

(R1): a flip pushes a margin through zero, so only a concordant matchup can be flipped, and the result is discordant--which the coalition can never push back through zero.

(R2): a rank swap is an adjacent transposition in the margin order. A swap placing $d$ above an adjacent $c$ requires strengthening $d$ or weakening $c$, both legal pushes toward the coalition's dispreferred candidate. A swap placing $c$ above an adjacent $d$ requires strengthening $c$ or weakening $d$, both pushes toward a coalition-*preferred* candidate, hence impossible. Flips do not change ranks. $\square$
{% endproof %}

In plain terms: a coalition can deepen its lies, but it can never take them back. Every deviation is a one-way valve.

> **Lemma:** (Gates) Every profitable complex manipulation passes through a gate: its first strictly-improving step is the simple manipulation out of $G_1$ (to $Q_1$) or out of $G_2$ (to $Q_2$).\label{gates}

{% proof Click to expand proof %}
**Proof:** By Theorem \ref{profitable-cycles}, these are the only two strictly $f$-improving edges in the entire deviation graph for this coalition. Any profitable path must contain at least one strictly improving step, and that step must be one of these two. $\square$
{% endproof %}

So a state admits a profitable complex manipulation if and only if it can reach $G_1$ or $G_2$ without ever crossing a strictly improving edge first--that is, we are really asking which states are *ancestors* of a gate, not which states a gate can reach.

> **Theorem:** For $n=3$ and a fixed coalition $A\succ B\succ C$, exactly six of the 48 states admit a profitable complex manipulation: the four states of the burial chain
>
> $$\langle B\to A\mid A\to C\mid B\to C\rangle \xrightarrow{C\succ B} \langle B\to A\mid B\to C\mid A\to C\rangle \xrightarrow{C\succ B} \langle B\to C\mid B\to A\mid A\to C\rangle \xrightarrow{C\succ B} G_1 \xrightarrow{C\succ B} Q_1$$
>
> (outcomes $B,B,B,B,A$ respectively), and the two states of the betrayal chain
>
> $$\langle B\to C\mid C\to A\mid A\to B\rangle \xrightarrow{B\succ A} G_2 \xrightarrow{B\succ A} Q_2$$
>
> (outcomes $C,C,B$ respectively).<d-footnote>By relabeling symmetry, each of the six coalition orders has its own version of these two chains, giving 36 (state, coalition) pairs over 30 distinct states: all 12 cyclic states (six of them manipulable this way by exactly two distinct coalitions) plus exactly half--18 of 36--of the Condorcet-winner states, each by a unique coalition. Machine-verified; not worth main-text space, but a fun consistency check.</d-footnote>\label{complex-classification}

{% proof Click to expand proof %}
**Proof (outline):** By the Gate Lemma, a profitable starting state either has $f=B$ and reaches $G_1$ through $f=B$ states, or has $f=C$ and reaches $G_2$ through $f=C$ states.

By the Ratchets, reaching $G_1=\langle C\to B\mid B\to A\mid A\to C\rangle$ requires the starting state to already contain the concordant $A\to C$ (R1--a discordant $C\to A$ could never be repaired), ranked above both discordant matchups $B\to A$ and $C\to B$ (R2--such an inversion could never be undone). Reaching $G_2=\langle B\to C\mid A\to B\mid C\to A\rangle$ requires the starting state to already contain both concordant matchups $A\to B$ and $B\to C$.

Hand-enumerating the states satisfying these conditions (ruling out states where these conditions would force a different Condorcet winner) leaves exactly four $B$-outcome candidates for $G_1$ and two $C$-outcome candidates for $G_2$--and the chains displayed above show each candidate reaches its gate through legal, outcome-preserving steps, which gives sufficiency. *(Full case-by-case enumeration to be filled in.)* $\square$
{% endproof %}

> **Corollary:** (Single-lie sufficiency) Every profitable complex manipulation reduces to a single lie told at increasing strength. The four burial-chain states are profitably manipulated by the lone insincere vote $C\succ B$ (burying $B$), pushed to increasing depth; the two betrayal-chain states by the lone insincere vote $B\succ A$ (betraying $A$). The six states differ only in *how far* the lie must be pushed--1 to 4 margin ranks.\label{single-lie}

{% proof Click to expand proof %}
**Proof:** Read the arrows in the chains above: every edge in the burial chain is the $C\succ B$ deviation applied with more mass; every edge in the betrayal chain is $B\succ A$. $\square$
{% endproof %}

You can verify this yourself in the playground: from the two scenarios, moving the sliders to the right (simulating moving backwards through a complex manipulation chain) does not ever make the outcome worse for the coalition.

Three of the four burial-chain states have a Condorcet winner--namely $B$, the coalition's *middle* candidate. This turns out to be the only way a Condorcet winner can be complexly overturned: it must be the coalition's middle choice, dragging the election into a cycle that resolves in the coalition's favor. When the coalition's *least favorite* candidate is the genuine Condorcet winner, the coalition is provably powerless--both $C$-class starting points are themselves cycles.

> **Corollary:** (One-notch bound) A coalition can never improve the outcome by two notches via a complex manipulation. In fact, no $f=C$ state has any deviation path to any $f=A$ state at all, monotone or otherwise.\label{one-notch}

{% proof Click to expand proof %}
**Proof:** Reaching outcome $A$ requires passing through $G_1$, which contains $A\to C$. But any path out of the $C$-outcome class passes through $G_2$'s exit $Q_2=\langle A\to B\mid B\to C\mid C\to A\rangle$, which contains $C\to A$--permanently, by (R1). $\square$
{% endproof %}

Even a maximally resourced, perfectly informed coalition improves its outcome by at most one preference notch, and only from six of the forty-eight starting states.

### Generalizing to More Candidates

Some of these theorems do generalize beyond $n=3$, but I caution at the overall expectation of robustness. Minimax, for its wonderful simplicity and ease of explanation (relative to something like Schulze), is not a very robust Condorcet method.

If you can use this model to say more interesting things about Minimax for $n>3$, or perhaps generalize this model to say some interesting things about Ranked Pairs, let me know in the comments below! I developed a somewhat analogous model for IRV (Ranked-Choice voting), which I may write about in a future post.

## Conclusion

In practice, to subvert or profitably manipulate this type of election, you would first need the resources to organize widespread dishonesty (without tipping off opponents who could organize counterstrategy). But in addition to that, the amount of foreknowledge of the precise structure of the matchups is extensive to be able to predict that the coalition with your exact ordering of the three candidates has opportunity to manipulate the election.

Further, the manipulations would require convincing voters to either vote for their least favorite over their backup choice, or to betray their favorite in favor of their second choice. 

I simply do not see this as a practical concern. If you are a voter voting in such an election, I cannot recommend enough that you vote sincerely. There is effectively no way to game the result without an unrealistic amount of knowledge, foresight, confidence, and *resources*.

Just vote honestly. Vote for your favorite in their matchups. Vote for your second choice against your last choice. This system gives you the opportunity to have say in every single race, whether it is competitive or not. Don't think about strategy, just vote.
