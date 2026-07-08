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
      name: Equal Vote Coalition (Volunteer)
toc:
  - name: Introduction
  - name: The Model
    subsections:
      - name: Permutations of Matchups
      - name: The Graph
  - name: Starting with a Condorcet Winner
  - name: Profitable Cycles
  - name: Complex Manipulations
  - name: Conclusion
---

## Introduction

The [Better Choices system](../better-choices/){:target="_blank"} is a very interesting flavor of Condorcet where voters vote in all three head-to-head matchups between the candidates who make it to a top-3 runoff. I wrote about my complex thoughts on it in my last posts, but here I want to expound on the strategic resilience of the system.

The winner in this system is the candidate who wins both of their most head-to-head matchups. If there is a tie, and nobody wins both, the winner is determined by minimax (the candidate with the least bad loss wins if every candidate loses at least one matchup).

For example, if Alice wins both of her head-to-head matchups against Bob and Clark, then Alice is the winner outright. Suppose instead that Alice beats Bob by 300 votes, Bob beats Clark by 200 votes, and Clark beats Alice by 100 votes. Then Alice loses by the least amount (100 votes) and is the winner by the minimax tiebreaker.

[Ranked voting methods are not strategyproof](../gibbard-satt/){:target="_blank"}, but some are more manipulable than others. [Ranked-Choice Voting](../ditch-rcv/){:target="_blank"} is infamous (or should be) for its horrendous participation failures and strategic vulnerabilities. In both Burlington and Alaska, voters went to the polls, voted for their favorite candidate, and through that changed the outcome from their viable backup candidate to their least favorite candidate. Therefore, there is reason to consider a ranked voting system and ask "is this going to bite me for participating honestly?"

Condorcet methods do not generally satisfy the participation criterion, but [the Better Choices system *does*](../better-choices/){:target="_blank"}<d-cite key="brandt2025condorcet"></d-cite>. That is, you can generally feel safe that you aren't going to get a *worse* outcome by participating, but you might ask how much strategic pressure there is to spend the night before the election scheming up a complex strategy to game the election. Unlike RCV where there's probably good reason to check that you aren't about to walk into a center-squeeze and elect your worst nightmare, Condorcet methods are generally more robust.

But unlike a typical Condorcet method, where voters submit rankings, voters in the Better Choices system can submit much more complex preferences that cannot be expressed in a simple ranking. For example, a voter can say they vote for Rock over Scissors, Scissors over Paper, and Paper over Rock. This is a perfectly valid ballot in the Better Choices system, but it is not a valid ranking because it is not transitive.

One might wonder if this system is *more* manipulable than a typical Condorcet method, since voters can submit more complex preferences. I will show that this system is no more manipulable than a typical Condorcet method, and the fact that the runoff is restricted to three candidates makes it extremely robust.

In this post, I define a model of strategic manipulation in this system and show that it is *very* difficult to manipulate. In practice, there is essentially no reason to vote in any way but with complete honesty.

I primarily focus on the three candidate case, but some of these results generalize beyond that. Warning to the reader: this post is a bit more technical than my usual.

## The Model

Rather than have a profile or voter-centric model, we focus entirely on the election results themselves. Precise margins are not as important as their relative sizes. Hence, we identify election states with an ordered sequence of matchup results. We define a state as

$$P = \langle P_1 \mid P_2 \mid \cdots \mid P_m \rangle, \quad P_i = (w_i \to \ell_i), \quad m = \tbinom{n}{2}$$

where $w_i$ is the winner and $\ell_i$ is the loser of the $i$-th matchup, with matchups ordered so that $P_1$ has the smallest margin and $P_m$ has the largest. We write $\operatorname{win}(P_i)=w_i$ and $\operatorname{lose}(P_i)=\ell_i$. For example in $n=3$, the state $\langle C\to B \mid B\to A \mid A\to C\rangle$ means $C$ defeats $B$ by the smallest margin, $B$ defeats $A$ by the middle margin, and $A$ defeats $C$ by the largest margin. We also keep a mirror entry $P_0 = (\ell_1\to w_1)$, the reverse of the smallest-margin matchup.

Note that there are $\binom{3}{2}!\times 2^3=48$ possible states for 3 candidates, since there are $3!$ ways to order the matchups and $2^3$ ways to choose the winner of each matchup. In general, for $n$ candidates, there are $\binom{n}{2}!\times 2^{\binom{n}{2}}$ possible states.

The only way for the result of an election to possibly change is to change the relative sizes of the matchups. For example, if a coalition were to attempt to manipulate the election in $n=3$ by swapping their sincere votes for $\ell_2\to w_2$ with $w_2\to\ell_2$, then a sufficiently coordinated and large coalition might end up making the $w_2\to\ell_2$ matchup the largest margin, and the previous largest margin matchup $P_3$ would then become the middle margin matchup. Or, perhaps, the coalition might be able to change sincere votes for $w_1\to\ell_1$ into $\ell_1\to w_1$, which would reverse the smallest margin matchup such that $P_1=(\ell_1\to w_1)$, meaning that $\ell_1$ now *defeats* $w_1$ by the smallest margin.

Focusing instead on individual voters, or ranking profiles, is not necessary or helpful. Particularly because all the matchups are independent, any possible margins list can be achieved by some profile of voters. Hence, we can focus entirely on the election results themselves, through the only method of manipulation: a coalition of voters changing their sincere votes to attempt to change the relative sizes of the matchups.

We can thus define the decision rule of the Better Choices system as a function where if $P$ has a Condorcet winner $X$ (i.e. if there exist two distinct $i,j$ such that $\operatorname{win}(P_i)=\operatorname{win}(P_j)=X$, meaning that $X$ defeats both of the other candidates), then $f(P)=X$. Otherwise, if $P$ has no Condorcet winner, then minimax determines $f(P)=\operatorname{lose}(P_1)=\operatorname{win}(P_0)$, the candidate who loses by the least amount.

### Permutations of Matchups

We denote $$\sigma\in\left\{(i,i+1): 0\leq i<\binom{n}{2}\right\}\subset S_{\binom{n}{2}+1}$$ as permutations on the matchups themselves, and we define

$$(\sigma P)_i = P_{\sigma(i)}$$

For example, if $P=\langle A\to B\mid B\to C\mid C\to A\rangle$, then $(1,2)P=\langle B\to C\mid A\to B\mid C\to A\rangle$, and $(0,1)P=\langle B\to A\mid B\to C\mid C\to A\rangle$.

That is, permutations such as $(1,2)$ and $(2,3)$ swap the relative strengths of the matchups, while $(0,1)$ reverses the smallest matchup.

We are careful with compositions of permutations, since we always force that $P_0$ be the mirror of $P_1$. We typically consider only a single permutation of the matchups at a time.

We call a permutation $$\sigma=(i,i+1)$$ for $i>0$ a "swap of the first kind", and the permutation $(0,1)$ a "swap of the second kind". The first kind of swap preserves all current winners and losers of the matchups, while the second kind of swap changes the tournament structure of the matchups by reversing the smallest matchup.

### The Graph

Rather than considering the election states as a set of isolated nodes, we can consider them as a directed graph. The nodes are the election states, and the edges are the possible manipulations of the election. We can then ask questions about how easy it is to manipulate the election, and how many manipulations are required to achieve a profitable manipulation.

We define a directed graph on the set of all possible election states, where two states $P$ and $Q$ are connected by an edge if there exists a permutation $\sigma\in\{(0,1),(1,2),\ldots,(m-1,m)\}$ such that $Q=\sigma P$. That is, two states are connected if one can be obtained from the other by swapping the relative sizes of two matchups or reversing the smallest matchup.

We can understand this intuitively as $P$ being some sincere state of an election (where every voter is casting a fully honest ballot), and $Q$ being the result where a coalition of voters has insincerely changed their votes (deviated) such that they have successfully changed the relative sizes of the matchups. If $P$ and $Q$ are connected by an edge, then we say that $Q$ is achieved by a "simple manipulation" of $P$.

I remark that to even possibly do a simple manipulation, particularly in a large electorate, is going to be extremely difficult and require intense coordination. The goal of this post is to show just how futile such an effort is likely to be, even if it seemed possible to succeed.

Our question is when a coalition of voters can manipulate the election to change the winner profitably. That is, if $f(P)=X$ and $f(Q)=Y$, then we say that the coalition can manipulate the election from $P$ to $Q$ if $Y$ is preferred to $X$ by the coalition ($f(Q)\succ f(P)$, where we use $\succ$ to denote the manipulating coalition's preference). The work of Gibbard<d-cite key="gibbard1973manipulation"></d-cite> ensures that such manipulations are always possible, but we will show that they are *very* difficult to achieve in practice.

## Starting with a Condorcet Winner

We start with an extremely cheery theorem.

> **Theorem:** If $P$ has a Condorcet winner $X$, then there is no simple manipulation of $P$ that can profitably change the winner. That is, if $f(P)=X$ and $Q$ is connected to $P$ by an edge, then either $f(Q)=X$ or $f(P)\succ f(Q)$. In other words, $f(P)\succeq f(\sigma P)$.

{% proof Click to expand proof %}
**Proof:** Suppose $P$ has a Condorcet winner $W$. Then $W$ wins both of its head-to-head matchups against the other two candidates. Hence, a swap of the first kind cannot change the winner, since it preserves all current winners and losers of the matchups. We thus only need to consider a swap of the second kind, which reverses the smallest matchup.

We consider three cases exhaustively. Let $P_1=(w_1\to\ell_1)$ be the smallest matchup, and $Q=(0,1)P$ be the result of the swap. Then we have three cases:

1. If $W\neq w_1$, then $W$ still wins both of their matchups after the swap, and hence is still the Condorcet winner.
2. If $W=w_1$, then $\ell_1$ now wins their matchup against $W$. If this creates a cycle, then $f(Q)=\operatorname{lose}(Q_1)=w_1=W$, and the winner is unchanged.
3. If $W=w_1$ and $\ell_1$ becomes the new Condorcet winner, then $f(Q)=\ell_1$. However, the swap of the second kind is only possible if the coalition sincerely preferred $w_1\succ\ell_1$, and hence $f(P)\succ f(Q)$.

In all cases, we have $f(P)\succeq f(Q)$, and the theorem is proven. $\square$
{% endproof %}

The contrapositive of this theorem is that any profitable simple manipulation must start with a state that has no Condorcet winner, and must instead begin in a cycle. Cycles are empirically rare (in RCV elections, at least), and hence it seems unlikely that such a scenario is likely to occur. However, we can further show that the exact requirements for a cycle with profitable manipulations are even stricter still.

> **Corollary:** A simple manipulation using a swap of the second kind (reversing the smallest matchup) is never profitable for $n=3$. It can be profitable for $n>3$.

{% proof Click to expand proof %}
**Proof:** The above theorem handles the case where $P$ has a Condorcet winner, so we only need to consider the case where $P$ has no Condorcet winner. Suppose $P$ has no Condorcet winner, and let $Q=(0,1)P$ be the result of a swap of the second kind.

For $n=3$, a cycle means that every candidate loses exactly one matchup. Hence, flipping any single matchup results in the existence of a Condorcet winner. In particular, because we have given $\ell_1$ the victory over $w_1$ by reversing the smallest matchup, $\ell_1$ now wins two matchups and is the Condorcet winner of $Q$. Hence, $f(Q)=\ell_1$. Thus, $f(Q)=\ell_1=f(P)$. Hence, the manipulation is not profitable.

Consider $n=4$. For $n=4$, it's possible to flip a matchup in a cycle and stay in a cycle, in which case this is genuinely profitable. If $f(P)=\operatorname{lose}(P_1)=\ell_1$ and $Q=(0,1)P$, then $\operatorname{lose}(Q_1)=w_1$. To flip the weakest matchup of $w_1\to\ell_1$ to $\ell_1\to w_1$, the coalition must sincerely prefer $w_1\succ\ell_1$, and insincerely bury $w_1$ under $\ell_1$ until $\ell_1$ defeats $w_1$ by the smallest margin. Thus, $f(Q)=w_1\succ\ell_1=f(P)$, and the manipulation is profitable. $\square$
{% endproof %}

This is genuinely one spot where the massive dominance of $n=3$ elections is a benefit over taking the system to $n>3$ (at least with a minimax tiebreaker). This showcases how minimax is less robust for larger $n$, but is extremely robust for $n=3$ [due to its agreement with Ranked Pairs and Schulze](../better-choices/){:target="_blank"}<d-cite key="brandt2025condorcet"></d-cite>.

This further narrows the field of possible ways to profitably manipulate the election for $n=3$. Not only must the election begin in a cycle, but it cannot be profitably changed by changing the winner of the weakest margin. The only remaining possibility is to swap the relative strengths of the existing matchups. But we have yet to eliminate all never-profitable manipulations.

> **Lemma:** A simple manipulation created by the permutation $(i,i+1)$ for $i>1$ never changes the winner of an election, and hence is never profitable for any $n$.

{% proof Click to expand proof %}
**Proof:** If $P$ has a Condorcet winner, then the $(i,i+1)$ swap for $i>1$ preserves the winner, and hence is not profitable. If $P$ has no Condorcet winner, then $f(P)=\operatorname{lose}(P_1)$. But $Q_1=P_1$, and hence $f(Q)=\operatorname{lose}(Q_1)=\operatorname{lose}(P_1)=f(P)$. Hence, the manipulation is not profitable. $\square$
{% endproof %}

Therefore, we need *only* consider the $(1,2)$ swap of the first kind, which swaps the relative strengths of the two weakest matchups, on $P$ which contains a cycle. We have eliminated $(0,1)$ and $(2,3),(3,4),\ldots,(m-1,m)$ as profitable manipulations, and hence we have reduced the field of possible profitable manipulations to a very small set of possibilities.

## Profitable Cycles

> **Theorem:** For $n=3$ candidates, fix a coalition with preferences $A\succ B\succ C$. For this coalition, exactly two $P$ out of the 48 total nodes have a profitable simple manipulation for this coalition, and they both contain a cycle. Specifically, they are
>
> 1. $P=\langle C\to B\mid B\to A\mid A\to C\rangle$, with $f(P)=B$ which can be manipulated to $Q=\langle B\to A\mid C\to B\mid A\to C\rangle$ with $f(Q)=A$ by the coalition choosing to insincerely vote $C\succ B$ instead of $B\succ C$.
> 2. $P=\langle B\to C\mid A\to B\mid C\to A\rangle$, with $f(P)=C$ which can be manipulated to $Q=\langle A\to B\mid B\to C\mid C\to A\rangle$ with $f(Q)=B$ by the coalition choosing to insincerely vote $B\succ A$ instead of $A\succ B$.

{% proof Click to expand proof %}
**Proof:** Based on our results above, we can restrict ourselves to considering cases where $f((1,2)P)\succ f(P)$, and $P$ has no Condorcet winner. Since $(1,2)$ is a swap of the first kind, $Q=(1,2)P$ must also be a cycle.

We then have that $f(P)=\operatorname{lose}(P_1)=\ell_1$ and $f(Q)=\operatorname{lose}(Q_1)=\ell_2$. Hence, we must have that a coalition of voters sincerely prefers $\ell_2\succ\ell_1$, but change their ballot in some other way. There are exactly two ways for a coalition to manipulate the election to achieve a $(1,2)$ swap.

| Manipulation                | Sincere Preference  | Insincere Deviation | Outcome Change     |
|-----------------------------|---------------------|---------------------|--------------------|
| Strengthen $w_1\to\ell_1$   | $\ell_1\succ w_1$   | $w_1\succ\ell_1$    | $\ell_1\to \ell_2$ |
| Weaken $w_2\to\ell_2$       | $w_2\succ\ell_2$    | $\ell_2\succ w_2$   | $\ell_1\to \ell_2$ |

We consider each case individually:

**Case 1**: Strengthen $w_1\to\ell_1$. In this case, the coalition must sincerely prefer $\ell_1\succ w_1$, and prefer the altered outcome $\ell_2\succ\ell_1$. Hence, we must have that $\ell_2\succ\ell_1\succ w_1$. Let us label this preference $A\succ B\succ C$ ($A=\ell_2$, $B=\ell_1$, $C=w_1$). Then we have that $P_1=(C\to B)$ and $\operatorname{lose}(P_2)=A$.

Using that $P$ is a cycle, meaning every candidate must lose exactly one matchup, we deduce that $\ell_3=C$, $w_3=A$, and $\operatorname{win}(P_2)=B$. Hence, $P=\langle C\to B\mid B\to A\mid A\to C\rangle$, and $Q=(1,2)P=\langle B\to A\mid C\to B\mid A\to C\rangle$. This is one of the two profitable manipulations, where $f(P)=B$ and $f(Q)=A$. The manipulation done, specifically, by voters who sincerely prefer $B\succ C$ but insincerely vote $C\succ B$ instead. By burying their second favorite, they cause their favorite to win.

**Case 2**: Weaken $w_2\to\ell_2$. In this case, the coalition must sincerely prefer $w_2\succ\ell_2$, and prefer the altered outcome $\ell_2\succ\ell_1$. Hence, we must have that $w_2\succ\ell_2\succ\ell_1$. Let us label this preference $A\succ B\succ C$ ($A=w_2$, $B=\ell_2$, $C=\ell_1$). Then we have that $P_2=(A\to B)$ and $\operatorname{lose}(P_1)=C$.

Using that $P$ is a cycle, meaning every candidate must lose exactly one matchup, we deduce that $\ell_3=C$, $w_3=A$, and $\operatorname{win}(P_1)=B$. Hence, $P=\langle B\to C\mid A\to B\mid C\to A\rangle$, and $Q=(1,2)P=\langle A\to B\mid B\to C\mid C\to A\rangle$. This is the second profitable manipulation, where $f(P)=C$ and $f(Q)=B$. The manipulation done, specifically, by voters who sincerely prefer $A\succ B$ but insincerely vote $B\succ A$ instead. By betraying their favorite, they allow their second favorite to win instead of their least favorite.
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

> **Corollary:** For a coalition of voters with preference $A\succ B\succ C$, the simple manipulation caused by performing a non-adjacent deviation of voting for $C$ over $A$ is never profitable. That is, a coalition of voters who sincerely prefer $A\succ B\succ C$ can never profitably manipulate the election by insincerely voting $C\succ A$ instead of $A\succ C$.

{% proof Click to expand proof %}
**Proof:** Copying the logic from the previous proof, suppose that $f(P)=\ell_1$ and $f(Q)=\ell_2$ for $Q=(1,2)P$, both cyclic scenarios. We want a profitable deviation, meaning the voters prefer $\ell_2\succ\ell_1$. By the table in the previous proof we must either have

- $\ell_1\succ w_1$ where $A=\ell_1$ and $C=w_1$, or
- $w_2\succ\ell_2$ where $A=w_2$ and $C=\ell_2$.

For case 1: $A=\ell_1$ is the most preferred candidate, so we cannot have $\ell_2\succ\ell_1=A$.

For case 2: $C=\ell_2$ is the least preferred candidate, so we cannot have $\ell_2=C\succ\ell_1$.

Therefore, in both cases, we cannot have a profitable manipulation by insincerely voting $C\succ A$ instead of $A\succ C$. $\square$
{% endproof %}

We can thus guarantee that there is *never* a reason in any scenario to vote for your *least favorite candidate* over your *most favorite candidate*. This proves that this system is no more manipulable than a typical Condorcet method, but is in fact *less* manipulable than some Condorcet methods involving four or more candidates.

## Complex Manipulations

We have found exactly two states for $n=3$ that have a profitable simple manipulation. However, we can also ask if these two nodes are themselves reachable by manipulations from other nodes via the same coalition of voters. For example, is it possible for there to be a $P$ with a Condorcet winner such that by multiple manipulations, the coalition can eventually reach one of these two nodes and profitably change the winner?

The answer is yes. We can consider a "complex manipulation" to be a sequence of simple manipulations where the final state is strictly preferred to the initial state by the coalition. That is, if $S^{(0)}\to S^{(1)}\to\cdots\to S^{(k)}$ is a complex manipulation, then we have that $f(S^{(k)})\succ f(S^{(0)})$. This is a much weaker requirement than having a chain of weakly preferred states, since we only require that the final state be strictly preferred to the initial state. It turns out that all complex manipulations are weakly preferred at all intermediate states, but we do not require that to be the case.

For the $P=\langle C\to B\mid B\to A\mid A\to C\rangle$ case, we can "move backwards" along the insincere misrepresentation of $C\succ B$, by fortifying the $B\to C$ matchup. Hence, we get a chain

$$\begin{gather*}
\langle B\to A\mid C\to B\mid A\to C\rangle\leftarrow\\
\langle C\to B\mid B\to A\mid A\to C\rangle\leftarrow\\
\langle B\to C\mid B\to A\mid A\to C\rangle\leftarrow\\
\langle B\to A\mid B\to C\mid A\to C\rangle\leftarrow\\
\langle B\to A\mid A\to C\mid B\to C\rangle
\end{gather*}$$

This gives four nodes for which a coalition of sufficient size who prefer $A\succ B\succ C$ can manipulate the election to achieve a profitable outcome, theoretically through a very large manipulation. That is, if the scenario is $\langle B\to A\mid A\to C\mid B\to C\rangle$, meaning that $B$ defeats $C$ by the largest margin, then if you can manage to convince a large enough coalition of $A\succ B\succ C$ voters to insincerely bury $B$ under $C$, such that $C$ eventually defeats $B$ by the second largest margin $\langle B\to A\mid C\to B\mid A\to C\rangle$, then you can indeed manipulate the election to achieve a profitable outcome. Perhaps this is achievable in an election where the margins are particularly close together, but I find simple manipulations implausible enough already.

For the second profitable manipulation, $P=\langle B\to C\mid A\to B\mid C\to A\rangle$, we can similarly move backwards along the insincere misrepresentation of $B\succ A$, by fortifying the $A\to B$ matchup, but this can only be done once. Hence, we get a chain

$$\begin{gather*}
\langle A\to B\mid B\to C\mid C\to A\rangle\leftarrow\\
\langle B\to C\mid A\to B\mid C\to A\rangle\leftarrow\\
\langle B\to C\mid C\to A\mid A\to B\rangle
\end{gather*}$$

This gives us six nodes total (four plus two). Six scenarios where, theoretically, a coalition of sufficient strength could employ some insincere strategy like burial or betrayal that, if strong enough to radically shift the margins, could achieve a profitable outcome. However, I find this to be an extremely unlikely scenario, and I do not see it as a practical concern.

### Generalizing to More Candidates

Some of these theorems do generalize beyond $n=3$, but I caution at the overall expectation of robustness. Minimax, for its wonderful simplicity and ease of explanation (relative to something like Schulze), is not a very robust Condorcet method.

If you can use this model to say more interesting things about Minimax<d-footnote>I bet you can maybe generalize this model to say some interesting things about Ranked Pairs, too.</d-footnote> for $n>3$, let me know in the comments below!

## Conclusion

In practice, to subvert or profitably manipulate this type of election, you would have to

1. Foresee that the election will produce a cycle
2. Be able to gauge the relative strengths of the matchups to know *which* two matchups are the weakest (and you better be sure about the order)
3. Be able to coordinate a large coalition of voters to insincerely change their votes in the exact right way to achieve the swap.
4. Have that coalition be sufficiently large that you can actually change the relative strengths of the matchups, and hopefully disturb nothing else in the election (and hope nobody performs any counterstrategy to negate your efforts).

Or, if you somehow actually have the resources to perform a *strong* manipulation, then you still have to be quite confident about the relative margins of the other matchups.

I simply do not see this as a practical concern. If you are a voter voting in such an election, I cannot recommend enough that you vote sincerely. There is effectively no way to do this without an unrealistic amount of knowledge, foresight, confidence, and *resources*.

Just vote honestly. Vote for your favorite in their matchups. Vote for your second choice against your last choice. This system gives you the opportunity to have say in every single race, whether it is competitive or not. Don't think about strategy, just vote.
