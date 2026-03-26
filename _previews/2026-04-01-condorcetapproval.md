---
layout: distill
title: Approval is a Condorcet Method
date: 2026-03-25
description: Approval is the perfect Condorcet method, and I have permanently solved the Condorcet paradox. April Fools!
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
related_posts: true
theorems: true
pretty_table: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: Conclusion
  - name: References
---

## Introduction

Merry April Foolsmas, everyone! Fellow Condorcetists, I come bearing a gift: I have permanently solved the Condorcet paradox. There is in fact a *perfect* voting system: Approval voting, and it *is* indeed a Condorcet method.

[For an actually serious post on the fact that Approval is a practical Condorcet approximation, see this post.](../practicalapproval){:target="_blank"}

During the time of the French revolution, two titans battled out their ideas of what a good voting system were: Their names were Jean-Charles de Borda and the Marquis de Condorcet.

- Borda: Believed that we should give candidates points based on where they are ranked. My lowest ranked candidate gets zero. Next up gets one, and so on.
- Condorcet: Had a much better idea. If there is a Candidate who would defeat every other candidate in a one-on-one race, then they should be elected.

But it is impractical to hold an election for every $\frac{n(n-1)}{2}$ pair of candidates, so we need a voting system that can be used in a single election, but still satisfies the Condorcet criterion: if there is a Condorcet winner, they should win.

We compromise on the idea that we can simulate how voters would vote in each theoretical matchup by ranking candidates. If I rank Alice first, Bob and Clark second, and Dylan last, then I am saying that

- I would vote for Alice over Bob, Alice over Clark, and Alice over Dylan.
- I would vote for Bob over Dylan, and Clark over Dylan.

The single ranked ballot thus allows us to simulate how voters *might* vote in each theoretical matchup, and thus have an idea if there is a Condorcet winner. If there is, then by golly, they should win!

However, this is an approximation. Every Condorcetist must be honest about this. **So long as we do not directly ask how a voter would vote in every possible matchup, we cannot guarantee that there is a Condorcet winner, nor that we can find them.** We *must* compromise:

> **Axiom**: We do not require voters to directly express their preferences in every possible matchup. Instead, we ask them for a simplified transitive ranking of candidates. We assume that if a voter ranks candidate $A$ above candidate $B$, then that voter would vote for $A$ over $B$ in a head-to-head matchup, and if a voter ranks $A$ and $B$ equally, then that voter would abstain in a head-to-head matchup between $A$ and $B$.

This is a *huge* assumption. It is a *huge* compromise. Why can't a voter express that they would vote for Alice over Bob, they would vote for Bob over Clark, but they would vote for Clark over Alice? By restricting voters arbitrarily to a ranking, we are choosing to completely throw away all possible non-transitive preferences alongside all information about the distance and intensity of preferences. We Condorcetists are *all* about throwing away certain information so that preferences are easier to aggregate and treat faithfully!

> **Definition**: A voting system satisfies the *Condorcet criterion* if whenever there is a candidate who would defeat every other candidate in a head-to-head matchup **based on the ballot data**, then that candidate must win.

If you do not elect such a candidate, then **what are you even** ***doing***? [Why ask for rankings if you aren't even going to use or respect them?](../ditch-rcv){:target="_blank"}. If you do not elect such a candidate, then you have elected someone else who has to serve their constituents knowing that a majority of voters wanted someone else more. That creates a [legitimacy problem](../consistentcardinal){:target="_blank"}.

We also cannot guarantee that we elect the correct Condorcet winner, because we are not asking all those direct head-to-head questions. Especially if we allow ties or ballot truncation. If 45% of voters say they prefer Bob over Alice, and 40% of voters say they prefer Alice over Bob, but 15% of voters did not express a preference between Alice and Bob, then we have no way to prove that Bob truly would defeat Alice in a head-to-head matchup, because those 15% of voters could be split in any way. They *could* all prefer Alice over Bob, and would vote that way in a runoff, but were too tired to rank them, or didn't want to rank either because while they do prefer Alice, they hate both candidates. Therefore, we must work purely with the data we are given, and trust that it is accurate to the whole electorate.

Further, it's far more efficient to just count up the individual pairwise votes. This is precinct summable: It is realistic for the high school gymnasium to count up the approximately $n(n-1)$ number of pairwise votes, and just post them on the door. This can be added up across precincts, and it only requires simple addition to determine if such a candidate exists. This is much easier than doing something like a *ridiculously complex* algorithm where we count up first choices only, arbitrarily, eliminate the candidate with the least votes, and transfer votes around until someone gets a majority. This would require central tabulation, be more opaque, and have worse outcomes in simulations. That'd be a really stupid voting system, who would even want to use that? If we count rankings, we should use them! Condorcet only, baby!

The biggest question is, however, does such a candidate even exist? How likely is it that if we hold an election with hundreds, thousands, or even millions of voters, that there will be a single candidate who would be ranked above every other candidate by a majority of voters in the ballot data? It turns out the answer can be 100%, or not 100%, depending on the system.

## Generalized Condorcet Methods

> **Definition**: A (Generalized) *Condorcet method* (GCM) is a voting system where voters can rank candidates, with ties allowed, among some number of tiers. If a voter ranks candidate X strictly over candidate Y, then that voter casts a vote for X in the X vs Y matchup. If there is a candidate who wins all of their matchups, then that candidate is declared the Condorcet winner and *must* win. We denote a GCM with $k\geq 2$ tiers as $C_k$. If there is no limit on the number of tiers, then we denote it as $C_\infty$.

Simple enough. If 100 voters rank Alice above Bob, and 50 voters rank Bob above Alice, while 600 voters rank Alice and Bob equally, then we choose to assume that Alice defeats Bob and Bob does not defeat Alice. If there is a candidate who defeats every other candidate, then we assume they are the Condorcet winner, and they must win.

We treat the voting system as a function $C_k(P)$, for $k \geq 2$ or $k = \infty$, that takes in a profile $P$ of ballot preferences (compatible with $C_k$) and outputs a set of winners. If there is a Condorcet winner, then that candidate must be the unique winner

> **Axiom**: If no candidate wins all of their matchups, based on the ballot data, then we make no assumption about which candidate is the Condorcet winner or should win. If $\mathcal{C}$ is the set of all candidates, and $P$ induces no Condorcet winner, then $C_k(P)$ is defined to output $\mathcal{C}$, the set of all candidates.

Generally, a Condorcet method uses the same number of tiers as there are candidates, so that voters could theoretically rank all candidates in a complete transitive order, which is effectively $C_\infty$. But what if we only allow voters to rank candidates in a limited number of tiers?

## Limited Tiers and the Condorcet Paradox

> **Lemma**: A Condorcet winner can fail to exist if $k>2$.

**Proof:** Consider the following profile:

| Voters | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 1      | A        | B        | C        |
| 1      | B        | C        | A        |
| 1      | C        | A        | B        |

In this profile, $A$ defeats $B$ (a majority of voters rank $A$ above $B$), $B$ defeats $C$, and $C$ defeats $A$. There is no Condorcet winner, and this only requires 3 tiers. $\square$

> **Definition**: For $C_2$, we denote $S(A)$ as the number of voters who put candidate $A$ in the approved tier. We denote $S(A>B)$ as the number of voters who put candidate $A$ in the approved tier and candidate $B$ in the not approved tier. And $S(A=B)$ as the number of voters who put both candidates in the approved tier.

Thus, $S(A)=S(A>B)+S(A=B)$, and $S(B)=S(B>A)+S(A=B)$.

> **Lemma**: Candidate $A$ defeats candidate $B$ in $C_2$ if and only if more voters put $A$ in the approved tier.

**Proof:** If more voters put $A$ in the approved tier, then $S(A)>S(B)$. Thus, $S(A>B)+S(A=B)>S(B>A)+S(A=B)$, so $S(A>B)>S(B>A)$, so $A$ defeats $B$. Conversely, if $A$ defeats $B$, then $S(A>B)>S(B>A)$, so $S(A)=S(A>B)+S(A=B)>S(B>A)+S(A=B)=S(B)$. $\square$

> **Proposition**: $C_2$ induces a transitive majority relation.

**Proof:** By the previous lemma, $A$ defeats $B$ if and only if $S(A)>S(B)$. Thus, the ordinal ranking of candidates by $S(\cdot)$ is the same as the majority relation. Since the ordinal ranking of candidates by $S(\cdot)$ is a sequence of real numbers, it is totally ordered and thus transitive. $\square$

> **Corollary**: There can never be a Condorcet paradox in $C_2$.

**Proof:** Suppose that $A$ defeats $B$, and $B$ defeats $C$. Then $S(A)>S(B)$ and $S(B)>S(C)$, so $S(A)>S(C)$ by transitivity of the real numbers, so $A$ defeats $C$. $\square$

> **Theorem**: A Condorcet winner always exists for $C_k$ if and only if $k=2$ and if there is no tie for the most approved candidate. Further, as a GCM, that Condorcet winner must win.

**Proof:** If $k=2$, then by the previous results, the candidate with the most approvals must defeat every other candidate, so there is a Condorcet winner. Conversely, if $k>2$, then by the first lemma, there can be a profile with no Condorcet winner. As a GCM, the Condorcet winner must win by definition. $\square$

## Approval Voting

> **Definition**: *Approval voting* is a voting system where voters can rank candidates among two tiers: approved and not approved. The candidate who is in the approved tier of the most voters wins.

## Conclusion

## References