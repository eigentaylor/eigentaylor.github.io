---
layout: distill
title: Is STAR more manipulable than IRV? A model of manipulability
date: 2026-07-15
description: Why 'just vote honestly' might not be the best policy in STAR voting.
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
    subsections:
      - name: Decoupled Metrics
      - name: The Obvious Differences 
  - name: The Model
  - name: The Moves
    subsections:
      - name: IRV
      - name: STAR
  - name: Profitable Manipulations
  - name: Complex Manipulations
  - name: Appendix
---

## Introduction

It should be clear up-front that this model says nothing about the probability of the situations we will be discussing. Rather, this is more in the vein of the Brams and Fishburn 1981 paper on strategy in Approval voting with a runoff <d-cite key="fishburnBrams1981runoff"></d-cite>.

We assume perfect knowledge of the underlying tournament structure, and the ranked order of candidates by their "votes" (or "points") in the case of STAR. We are simply asking how voters might strategize to optimize the outcome. We are also restricting our attention to a three-candidate election, which is the simplest case where we can have a non-trivial final round.

IRV (Instant-Runoff Voting or "Ranked Choice Voting"<d-footnote>We will be using IRV in this post for explicit clarity that we are discussing the system that eliminates the candidate with the lowest number of votes in each round until one candidate remains. So as not to be confused with other ranked voting system which do not have the problems we will be discussing today, like Condorcet methods.</d-footnote>) and STAR are very different systems in ballot and quality of outcomes <d-cite key="quinn2017vseSummary"></d-cite>, but they share some common features. The final result is determined by a pairwise comparison of candidates, and to get into the final round, you must not have the lowest number of votes among the top three candidates. With exactly three candidates, the two systems are essentially identical in mechanism: the candidate with the lowest number of votes is eliminated, and the winner is the candidate among the remaining two who defeats the other in a pairwise comparison.

### Decoupled Metrics

What got me thinking about this model is the fact that both systems have the outcome determined by a pairwise comparison, but *how* the candidates get into the final round has relatively little predictive power for pairwise competence.

In Burlington, Vermont, in 2009, the candidate who had the most votes among the top three candidates in the mayoral race, Kurt Wright, was a Condorcet loser. Meaning, in a pairwise comparison, he would have lost to each of the other two candidates (Bob Kiss and Andy Montroll). The lowest vote-getter, Andy Montroll, was the Condorcet winner, meaning he would have won in a pairwise comparison against each of the other two candidates. Montroll was also the majority second choice of both Kiss and Wright voters. In the final round, more votes transferred to Kiss than to Wright, and Kiss ended up winning. A "come-from-behind" victory for Kiss.

In a recent [video posted by The Equal Vote Coalition](https://youtu.be/Vte4nly_Neg?si=Pu7zC9ajh9oZf4x5), they rightly highlight one of (the many) major flaws in IRV: The promise that **"if my candidate can't win, then my vote will transfer"** is a complete **lie**. Kurt Wright *literally* could not win, but their votes did not transfer to a more viable second choice, like Montroll. Had these voters betrayed their nonviable first choice and insincerely ranked Montroll first, they would have secured a better outcome than their least preferred candidate winning.

Here's the problem: STAR can have the exact same problem. Suppose your favorite candidate is Alice. She's a firebrand who gets the most stars, but she's polarizing and would lose in a pairwise comparison against the other two candidates, Bob and Clark. Bob is your backup, but gets third place, while Clark gets second place. The runoff is then between Alice and Clark, and Clark wins. But you look at the reported precinct level pairwise results and see that Bob would have defeated both Alice and Clark in a pairwise comparison. If you, and all the other Alice-first-Bob-second voters had just given Bob more stars, then maybe Bob would have made it to the final round instead of Clark. Alice still loses, but at least you get your backup candidate as the winner instead of your least preferred candidate.

This situation is possible in both STAR and IRV. The fundamental issue being an inevitable reliance on a pairwise check of competence, when pairwise competence is not the metric used to decide *which two candidates to check*.

### The Obvious Differences

Now, I should be up-front that as far as voting systems go, [IRV is far, far worse](../ditch-rcv/) than STAR voting. It's not even close.

However, I have been working on a post investigating the manipulability of the [Better Choices voting system](../better-choices/) (a form of minimax), and I wanted to design a similar model for IRV. Eventually, I realized that STAR is an even better fit for the model, due to the structural similarities.

There are a number of differences that make STAR better, but the most important difference to highlight with respect to this model is that stars are genuinely a *better* measure of the strength of a candidate than conditional transfers of active votes. What inspired this investigation is the dissonance between the pairwise check and how we get there. STAR supporters claim that their system has great "honesty" incentives<d-footnote>We won't be touching on the philosophical question of what "honesty" means with a score ballot. That's a can of worms not worth delving into.</d-footnote>, but I want to challenge this by viewing it through a different angle: is there strategic pressure to alter your vote in order to get a better outcome? If so, then I would say the system has questionable "honesty" incentives.<d-footnote>As a supporter of Approval voting, perhaps stones should not be thrown from glass houses. However, I find the volatile participation failures and betrayals that we will investigate far more troubling than "Approval encourages you to vote strategically". It does. But paradoxically, that tends to make outcomes better. My contention is more that "if you care about being able to cast an "honest" ballot without worry, I think you should be looking at Condorcet methods instead, rather than STAR voting.</d-footnote>

## The Model

We define a set of equivalence classes of "election states" involving three candidates. We identify an election state via the following notation:

$$P=\langle X < Y < Z\mid T\rangle$$

Where $X$ is the candidate with the least votes, $Y$ is the candidate with the second most votes, and $Z$ is the candidate with the most votes. $T$ is the "tournament structure", which is the set of pairwise comparisons between candidates.

For example, $T$ could be $X\to Y, X\to Z, Y\to Z$, which would mean that $X$ beats $Y$ and $Z$, and $Y$ beats $Z$. In this case, $X$ is the Condorcet winner, and $Z$ is the Condorcet loser. The 2009 Burlington election would be an element of this node's equivalence class, with $X$ being Andy Montroll, $Y$ being Bob Kiss, and $Z$ being Kurt Wright.

In both STAR and IRV, the decision rule is as follows:

> $f(P)=Y$ if $Y\to Z$ and $f(P)=Z$ if $Z\to Y$.

In other words, the winner is the candidate among the top two vote-getters who wins the pairwise comparison. In IRV, $X$ is eliminated and their votes will transfer such that the candidate who wins the pairwise comparison will end up with more votes, and in STAR $X$ simply is ignored for the runoff step.

We focus our assumption on a coalition of voters who prefer $A\succ B\succ C$. We assume that $P$ is some "sincere" election state, meaning that the voters in the coalition are all voting "honestly". We then ask what potential manipulations that coalition could make to move it to another election state $P'$, and whether that manipulation would lead to a better outcome for the coalition (i.e. if $f(P')\succ f(P)$ where $\succ$ denotes the coalition's preference relation).

In IRV, the sincere vote is exactly $A\succ B\succ C$. In STAR, the sincere vote is assumed to be $A=5, B=x, C=0$ where $x$ is some number between 0 and 5. We denote this vote as "$5-x-0$".

We have $3!\cdot 2^3=48$ possible election states ($3!$ for the permutations of $X,Y,Z$ and $2^3$ for all possible tournament structures). We can then define a directed graph where the nodes are these election states, and there is a directed edge from $P$ to $P'$ if there is some manipulation that voters could make to move from $P$ to $P'$. We can then analyze the structure of this graph to understand the manipulability of the system.

Suppose, for example, that we are in STAR voting, and the sincere election state is $P=\langle B<A<C\mid T\rangle$ where $T$ is $B\to A, B\to C, C\to A$. If the coalition all change their votes to $5-4-0$, then $B$ gets a sudden influx of stars, and the new election state could be $P'=\langle A<B<C\mid T\rangle$. In this case, the winner changes from $C$ to $B$, which is a better outcome for the coalition.

This can also work in IRV. If the coalition abandons $A$ (perhaps realizing they cannot win) and insincerely ranks $B$ first, then the same manipulation can occur<d-footnote>The node $P=\langle B<A<C\mid T\rangle$ where $T$ is $B\to A, B\to C, C\to A$ contains the Alaska 2022 special election in IRV where $B$ is Nick Begich, $A$ is Sarah Palin, and $C$ is mary Peltola. Indeed, had Palin voters abandoned her for Begich, Begich would have won instead of Peltola. Nearly 60% of voters cast a ballot with a Republican as their first choice, but a Democrat ended up representing Alaska.</d-footnote>. We would thus say that $P$ "has an edge" to $P'$ in both IRV and STAR. This is one example of a "profitable" manipulation".

> **Definition:** A "simple manipulation" involves an adjacent swap of candidates in the total points order (i.e. $X<Y<Z$ becomes $Y<X<Z$ or $X<Z<Y$).

We start with simple manipulations because those are the most likely effects of an attempted manipulation by a coalition.

## The Moves

We now define the possible manipulations that voters can make in each system.

### IRV

In IRV, the room for manipulation is fairly limited. You really only have two moves:

1. Abandon $A$ and rank $B$ first ($A\succ B\succ C$ becomes $B\succ A\succ C$). This makes $A$ lose votes and $B$ gain votes.
2. Abandon $A$ and rank $C$ first ($A\succ B\succ C$ becomes $C\succ A\succ B$). This makes $A$ lose votes and $C$ gain votes.

In short, "betraying" your first choice and voting for someone else. Doing one of the can change the tournament structure. However, for now, we assume that the amount of flipped votes needed to flip the order of total votes is small enough that it does not change the tournament structure. We will relax this assumption later.

> **Lemma:** Any simple manipulations in IRV by an $A\succ B\succ C$ coalition has a net effect of one of the following:
>
> 1. If $B$ and $C$ are adjacent in scores, then a valid move is to swap their positions in total votes.
> 2. If $A$ and $X$ are adjacent in scores, with $A$ being above $X$, then a valid move is to swap their positions in total votes.
>
> In particular, we cannot swap $A$ and $Y$ if $Y$ is adjacent to $A$ in scores but $Y$ has more votes than $A$.\label{irv-moves}

{% proof Click to expand proof %}
**Proof:** Suppose $B$ and $C$ are adjacent in scores. Then, if the coalition abandons $A$ and ranks the lower of $B$ and $C$ first, then that candidate will gain votes. This can potentially flip the order of $B$ and $C$ in total votes. This applies symmetrically to both $B$ and $C$, so any adjacent swap of $B$ and $C$ is a valid manipulation.

Suppose $A$ and $X$ are adjacent in scores, with $A$ being above $X$. Then, if the coalition abandons $A$ and ranks $X$ first, then $X$ will gain votes and $A$ will lose votes. This can potentially flip the order of $A$ and $X$ in total votes.

However, if $Y$ is adjacent to $A$ in scores but $Y$ has more votes than $A$, then any change in the first rank by the coalition can only ever increase the distance between $A$ and $Y$ in total votes, but cannot flip their order. Therefore, swapping $A$ and $Y$ is not a valid manipulation if $Y$ has more votes than $A$. $\square$
{% endproof %}

### STAR

In STAR, the room for manipulation is much larger, due to the more expressive ballot. However, will will generously restrict ourselves to "sincere strategies", meaning that the coalition voters will always give $A$ a strictly higher score than $B$, and $B$ a strictly higher score than $C$.

> **Lemma:** Any adjacent swap of candidates in total votes can be achieved in STAR by a simple manipulation except for if $C$ and $A$ are adjacent in scores, with $C$ being above $A$.\label{start-moves}

The intuition for this is straightforward. If the coalition, en masse, moves from $5-x-0$ to $5-4-0$, then $B$ gets a sudden influx of stars, and $B$ can move above any candidate that was previously above it. If the coalition moves from $5-x-0$ to $5-1-0$, then $B$ suddenly loses a lot of stars, and $B$ can move below any candidate that was previously below it.

If the coalition moves from $5-x-0$ to $(x+1)-x-0$ or $5-x-(x-1)$, then that can move $A$ down or $C$ up. What cannot be done, however, is to close the distance between $A$ and $C$ if $C$ is above $A$ in scores, because the coalition cannot give $A$ more stars than 5, and cannot give $C$ fewer stars than 0. So if $C$ is above $A$, then the coalition cannot swap their positions in total votes.

The above describe "sincere deviations", where the order of the candidates is preserved on all ballots of the coalition. If we allow for insincere deviations, then these manipulations become easier, but may alter the tournament structure.

This means that STAR has a "greater attack surface" than IRV. Unlike IRV, there is no possible way to move your favorite candidate up above anyone else. You can only ever move your favorite *down*. In STAR, this is not the case. Because your support for all candidates is counted simultaneously, that allows for more "levers" of manipulation.

## Profitable Manipulations

> **Theorem:** If $P$ has a profitable simple manipulation in IRV or STAR ($n=3$), then it involves swapping the positions of the candidates in second and third place in total votes.

{% proof Click to expand proof %}
**Proof:** Swapping the top two candidates in total votes has no impact on the outcome, because the winner is determined by the pairwise comparison between the top two candidates.

The only way to change the outcome is to change who the runoff is between. That can only be done by an adjacent swap of the candidates in second and third place in total votes. $\square$
{% endproof %}

(possibly more axiomatic characterization of the manipulability of IRV and STAR)

> **Theorem:** (IRV Simple Manipulability) There are exactly 8 election states that have a profitable simple manipulation in IRV. Six of them involving betraying your first choice for your second choice, and two of them involve betraying your first choice for your third choice.

And STAR

> **Theorem:** (STAR Simple Manipulability) There are exactly 12 election states that have a profitable simple manipulation in STAR. Six of them can be achieved by changing the ballots to $5-4-0$ (boosting $B$), and six of them involve changing the ballots to $5-1-0$ (starving $B$). In fact, moving $A$ below $C$ is never profitable.

{% proof Click to expand proof %}
**Proof:** We suffice to list the profitable manipulations that were found by the computer search. But I think it's worth proving why moving $A$ below $C$ is never profitable. For moving $A$ below $C$ to be a feasible simple manipulation that *could* be profitable, we would need to have the election state $P=\langle C<A<B\mid T\rangle$, so that moving $A$ below $C$ would change the runoff. However, in this case, the outcome is only between $A$ or $B$. For this to be profitable, we cannot have the best candidate win in the initial state, since then it can only get worse. Hence, $f(P)=B$, implying that $B\to A$ in the tournament structure.

Suppose we do the simple manipulation of moving $A$ below $C$ to the node $P'=\langle A<C<B\mid T\rangle$. Then, the outcome is between $C$ and $B$. Regardless of the choice, this is weakly dispreferred to the original outcome of $B$, meaning a profitable manipulation is impossible. $\square$
{% endproof %}

We will include a jupyter notebook with all of the election states and their profitable manipulations in the [appendix](#appendix).

This means that in STAR voting, the strategy can, theoretically live entirely in how many stars you give your second choice candidate. A voter could theoretically maintain their sincere ordering by moving their second choice to 4 stars or 1 star, but a more desperate coalition might move them to 5 stars or 0 stars--as well as potentially move their favorite to 0 or their least favorite to 5, depending on how confident they are that the runoff needs to be changed--which could alter the tournament structure.

From another perspective, this could be seen as strategic pressure to give your second choice candidate a score that is more or fewer than you would otherwise. That is, perhaps you would have given your second choice 3 stars, but because of the unfavorable tournament structure, you are pressured to move them up or down to try to get a more favorable runoff.

## Complex Manipulations

> **Definition:** A "complex manipulation" is any manipulation of states $P_0\to\ldots\to P_k$ such that $f(P_k)\succ f(P_0)$ by the coalition.

We now characterize what complex manipulations are possible in IRV and STAR. For this section, we focus on the three candidate case for simplicity.

> **Lemma:** For $n=3$, in both STAR and IRV, all complex manipulations reduce down to moving the candidate with the greatest total votes down to third place ($X<Y<Z$ to $Z<X<Y$). In STAR this is possible if and only if $Z\neq C$. In IRV, this is possible if and only if $Z=A$.

{% proof Click to expand proof %}
**Proof:** By lemma \ref{star-moves}, if $C$ is the candidate with the greatest total votes, then there is no way to move $C$ down to third place, because at some point it would have to swap with $A$, which is impossible. If $Z\neq C$, then there is no restriction on which candidates it can be moved below.

For IRV, by lemma \ref{irv-moves}, if $Z\neq A$, then there is no way to move $Z$ down to third place, because at some point it would have to swap with $A$, which is impossible. If $Z=A$, then there is no restriction on which candidates it can be moved below. $\square$
{% endproof %}

> **Theorem:** Any complex manipulation in IRV is achievable by a simple manipulation. That is, if moving the candidate in first place down to last is profitable, then the same outcome could be achieved by just moving third place to second. There exist cases in STAR where a complex manipulation is profitable from a state that cannot be achieved by a simple manipulation from that state.

This is machine verified. This does indeed narrow down where manipulations in IRV need occur (for $n=3$). This does also mean that there are more states in STAR such that there's pressure to really try to bury whichever candidate is in first place.

> **Theorem:** For $n=3$, there are exactly 8 election states that have a profitable manipulation (of any sort) in IRV. There are exactly 18 states in STAR that have a profitable manipulation (of any sort).

This means that there are more than twice as many states in STAR for which there is pressure to consider how to rank your second choice candidate to attempt to manipulate the election. However, once again, this says nothing about the probability of these states occurring in practice. It could very well be that the 8 states in IRV are more likely to occur than the 18 states in STAR. What we can say is that there are more states in STAR where strategic consideration of how to fill out your ballot could occur (should you be able to predict an unfavorable tournament structure and total star placement of the candidates).

## Conclusion

I think the comparison between IRV and STAR has to be done carefully. With IRV, it's much harder to manipulate the outcome. Your vote is a precious resource that has to be spent wisely, and the transfers are unpredictable. Further, to manipulate the outcome, you have to vote insincerely.

STAR, however, has much more room for manipulation while voting in a sincere order. That is, these manipulations are in a sense "free". Changing from $5-1-0$ to $5-4-0$ costs nothing in your influence in the runoff step, but can legitimately alter the outcome based on who gets into the runoff step. I think this means that voters in STAR have to be genuinely conscious of how their vote might affect the runoff.

One of my biggest problems with IRV is that it's so short-sighted. The candidates who make it into the final round are not decided, in my opinion, by a good metric (first-choice or active votes potentially after transfer). In STAR, I find a similar problem. I think simultaneously counted scores *are* certainly a *better* metric to measure the quality of a candidate, but I still feel uncomfortable that this metric is still fairly decoupled from pairwise competence.

If my favorite candidate is a Condorcet loser who gets the most stars, and my backup didn't even make it into the runoff (and was a Condorcet winner), I am going to feel a bit swindled. Just as I would be in IRV in the same situation (like the Kurt Wright > Andy Montroll voters in Burlington).

Even though there are significantly *more* situations in STAR where strategic voting can be profitable, that doesn't mean they will be more common than the fewer cases that exist in IRV. It could very well be the opposite is true.

But I have to wonder: if we care about pairwise competence, why not just use a system that elects the Condorcet winner (for which it is far safer to vote with complete honesty)? Or if we care about stars and scores, why not just go with straight SCORE voting? Or we could just go for [Approval voting](../approval-only/) which will give us maximal legitimacy, outcome quality essentially *as good as STAR*, all with a much simpler ballot.

I do not see STAR as a system that is the "best" at anything, but rather tries to be "very good" at basically everything almost all of the time, in practice. I don't think there's anything wrong with that, but I, personally, very much care about the ["safety" of a voter in casting their ballot](../av-stratproof/). And after the [failure of IRV](../ditch-rcv/), where the supporters *knew* of the flaws that had happened in Burlington but flagrantly ignored them so that it happened *again* in Alaska, I am **extremely wary** of systems with highly visible failure modes, or runoff mechanics that can betray voters who are trying to vote sincerely. I think Condorcet methods and Approval are generally safer systems to vote in without causing a catastrophic change to who the runoff is between.

This is not to pass any sort of final judgment on STAR voting as a system. I [still do not quite endorse it](../approval-only/), and I do think that the "honesty" incentives are not as strong as some supporters claim. But is it more manipulable than IRV? Probably not. But I think there is good reason to be cautious in how you fill out your STAR ballot.

## Appendix

### A Jupyter Notebook

{::nomarkdown}
{% assign jupyter_path = 'assets/jupyter/irv_star_graph.ipynb' | relative_url %}
{% capture notebook_exists %}{% file_exists assets/jupyter/irv_star_graph.ipynb %}{% endcapture %}
{% if notebook_exists == 'true' %}
  {% jupyter_notebook jupyter_path %}
{% else %}
  <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}

### A Remark on Approval Top-2

It's worth mentioning at least that theoretically we could apply this model to Approval Top-2 (Approval with a runoff step). If we assume the sincere state for an $A\succ B\succ C$ coalition is to approve $A$, not approve $C$, and either approve or not approve $B$ (varying from voter to voter), then the effective moves are *identical* to that of STAR voting. This is, in fact, essentially the model used by Brams and Fishburn in their 1981 paper on Approval with a runoff <d-cite key="fishburnBrams1981runoff"></d-cite>.

However, I would argue a very slight nuance between the two systems. With STAR, the tournament structure is truly set in stone during the election. The runoff is automatic. But in Approval, the runoff is delayed. Hence, the expected tournament during the primary election could change during the campaign leading up to the general, as people learn about the candidates and watch the debates, they could change their minds.

I believe there is a stark difference between the following two scenarios:

1. Approving a seemingly strong candidate into the runoff who, during the general election campaign, suffers a scandal which makes them nonviable, and wishing you had approved of a safer candidate who didn't make it into the runoff.
2. Voting sincerely for your candidates, only to find out the candidate you supported into the runoff had objectively no chance of winning, and the system did not allow your support to transfer to a more viable backup (which can occur in both IRV and STAR).

The second seems like a betrayal of a different nature.
