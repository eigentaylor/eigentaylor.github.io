---
layout: distill
title: The Approval Dynamics of Laslier's Leader Rule
date: 2026-03-07
description: How the leader rule induces a graph and dynamical system on candidate perceptions.
giscus_comments: true
importance: 2
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
  - name: Pairwise Rankings
  - name: Equilibrium Paths
  - name: Case Studies
    subsections:
      - name: Alaska House Special Election 2022
      - name: NYC Democratic Mayoral Primary 2025
      - name: Minneapolis City Council Ward 2 2021
  - name: Discussion
    subsections:
      - name: The Chicken Dilemma Explored
  - name: Other Considerations and Further Research
  - name: Appendix 
    subsections:
      - name: Alaska House Special Election 2022 Table
      - name: NYC Democratic Mayoral Primary 2025 Table
      - name: Minneapolis City Council Ward 2 2021 Table
  - name: References
---

WIP DRAFT (not finished)

## Introduction

In plurality voting, the optimal strategy for a voter is often to vote for the most preferred frontrunner, even if that candidate is not their most preferred candidate. A vote for a strongly preferred but nonviable candidate is often seen as a "wasted vote", and can even lead to the election of a least preferred candidate, since the voter could have failed to help a more viable candidate defeat them. This is the classic "spoiler effect" and "vote splitting" problem of plurality voting.

Approval voting is a simple and practical change to plurality voting, where voters can choose to vote for as many candidates as they like. This simple change has profound implications for voter strategy, as the spoiler effect and fear of vote splitting are greatly reduced. However, there is still a strategic element to approval voting, as voters must decide which candidates to approve of.

> **Definition:** A ballot is called **sincere** if a voter approves all candidates they strictly prefer to any candidate they approve.

This prevents a betrayal of preference, where a voter might approve a less preferred candidate while failing to approve a more preferred one. However, there are multiple sincere ballots a voter could cast, depending on where they draw their "line of acceptability".

For a voter who prefers candidates A > B > C, there are three possible sincere ballots they could cast:

1. Approve A only
2. Approve A and B
3. Approve A, B, and C

A common criticism of approval voting is that even a sincere voter may have to be strategic and decide where to draw their line of approval. While an approval for A and B may be sincere, and does not narrow the margin between A and B, it could lead to a situation where the voter could have instead approved only A, and had A win instead of B. The claim is that this would lead to regret for the voter, and thus the voter may feel compelled to approve of only their most preferred candidate, reducing approval voting to plurality voting in practice.

This fear has not materialized in practice, as voters consistently approved of multiple candidates in real elections in Fargo and St. Louis. However, the myth of the "regretful approval voter" has persisted. Jean-François Laslier, in his 2009 paper "[The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate.](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}", presents a strategy for approval voting that helps optimally draw the line for a sincere strategy to minimize regret, based on who the perceived frontrunners are. Laslier's model is primarily focused on "trembling ballots" in large electorates, but we consider it here for its broader implications. Paradoxically, this strategy can actually lead to significantly more majoritarian outcomes, as we will explore in this post.

> **Definition:** **(The Leader Rule)** Call the candidate perceived most likely to win the "leader", and the second most likely candidate to win the "challenger". The leader rule strategy is as follows:
>
> 1. Approve all candidates strictly preferred to the leader
> 2. Approve the leader if and only if you prefer them to the challenger
> 3. Approve no other candidates

We will not delve into the details of why this is an optimal strategy. Intuitively, the primary idea is to prioritize the impact on the most likely ties. The most important race is between the leader and challenger, so the voter should choose exactly one of them to approve. In the unlikely case that a non-frontrunner ties for first, it's most likely to be with the leader, so the voter should approve of all candidates they prefer to the leader. Our analysis here focuses on what happens when every voter applies the leader rule simultaneously.

> **Definition:** We denote the proportion of voters who prefer X over Y as $P(X>Y)$, as a shorthand for the probability that a randomly selected voter prefers X over Y given the complete profile of voter preferences. Note that $P(Y>X)=1-P(X>Y)$.

For our axioms of this analysis, we assume

1. Voters have complete and transitive preferences over candidates. Given any pair of candidates, a voter strictly prefers one over the other, and is not indifferent between them.
2. Voters have common knowledge of the perceived front-runners. That is, every voter knows who the leader and challenger are perceived to be.
3. Every voter applies the leader rule simultaneously, implying that all voters use a sincere strategy.
4. No two pairwise match-ups have the same margin, and no two candidates tie. That is, for any two pairs of candidates, $(X_1, Y_1) \neq (X_2, Y_2)$, then $P(X_1>Y_1)\neq P(X_2>Y_2)$, and $P(X_1>Y_1)\neq 0.5$. In a "large electorate",  which is the setting Laslier focuses on in his paper, this is a reasonable assumption, since the probability of ties goes to zero as the number of voters increases.
5. Voter preferences are fixed. No voter changes their underlying ranking at any point.

We identify the set of possible leader challenger pairs $(X,Y)$, where $X\neq Y$, as state nodes. We can imagine them as what the polls say prior to an election. We investigate the nature of how one node moves to another.

Note that Theorems \ref{thm:pairwise} and Corollary \ref{cor:unique_condorcet_winner} are adapted from Laslier's original paper. The rest of the results are new so far as I know.

> **Theorem:** (Laslier) Suppose the leader, challenger pair is $(X,Y)$. After every voter applies the leader rule, the candidates will have the following percent approvals: \label{thm:pairwise}
>
> 1. $X$: $P(X>Y)$
> 2. $Z$: $P(Z>X)$ for all $Z\neq X$

Note that for any candidate $X$, after every voter applies the leader rule, the percent of the vote that $X$ gets is $P(X>Z)$ for some candidate $Z$. We remark that by the assumption that no two pairwise match-ups have the exact same margin, we can be assured that there is a unique winner after every voter applies the leader rule.

**Proof**: Based on the leader rule,

1. A voter only approves of a non-leader Z if they prefer Z > X. Therefore, Z gets $P(Z>X)$ approvals.
2. A voter only approves of X if they prefer X > Y. So X gets $P(X>Y)$ approvals. **QED**

> **Definition:** a **unique Condorcet winner** is a candidate who strictly defeats every other candidate in pairwise comparisons. That is, if $X$ is a unique Condorcet winner, then for every other candidate $Z$, $P(X>Z) > 0.5$. Thus, $P(Z>X) < 0.5$ for all $Z \neq X$. A **Condorcet loser** is a candidate who is strictly defeated by every other candidate in pairwise comparisons.

We now establish some important ramifications of Theorem \ref{thm:pairwise}:

> **Corollary:** (Laslier) If $X$ is a unique Condorcet winner, then after every voter applies the leader rule, $X$ will always have over 50% of the vote. Further, if the $X$ is the leader and a unique Condorcet winner, then $X$ will still be the leader after every voter applies the leader rule. \label{cor:unique_condorcet_winner}

**Proof:** As the unique Condorcet winner, $P(X>Z) > 0.5$ for all $Z \neq X$. Since the percent of votes $X$ gets must be some $P(X>Z)$ for some candidate $Z$, then $X$ must receive over 50% of the vote.

Suppose that X is the leader and Y is the challenger. Since $P(Z>X)<0.5$ for all $Z \neq X$, we must have that $P(X>Y) > P(Z>X)$ for all $Z \neq X$, meaning $X$ has strictly more votes than any other candidate. **QED**

> **Corollary:** After every voter applies the leader rule: (1) at least one candidate will have more than 50% of the vote, and (2) if $X$ is a Condorcet loser, then $X$ will never be the leader and will always have less than 50% of the vote. \label{cor:majority_and_loser}

**Proof:** For (1): if there exists a unique Condorcet winner, then by Corollary \ref{cor:unique_condorcet_winner}, that candidate will have over 50% of the vote. If there is no unique Condorcet winner, then there must exist some candidate $Z$ who defeats the leader $X$ in a pairwise match-up: $P(Z>X)>0.5>P(X>Z)$. Therefore, $Z$ will have more than 50% of the vote.

For (2): if $X$ is a Condorcet loser, then $P(X>Z) < 0.5$ for all $Z \neq X$, and thus $X$ will always have less than 50% of the votes by Theorem \ref{thm:pairwise}. By part (1), some candidate must have over 50% of the vote, and will thus have more votes than $X$. Therefore, $X$ will not be the leader. **QED**

This corollary tells us something important: even if there is a cycle of preferences, when the elections finally comes around and voters apply the leader rule, we can guarantee that not only will there be a unique winner--by the assumption that no two pairwise match-ups have the same margin--but also that

1. The winner will receive over 50% of the vote
2. The winner won't be a Condorcet loser

> **Definition:** A node $(X,Y)$ has an edge to a node $(X',Y')$ if after every voter applies the leader rule at node $(X,Y)$, $X'$ has the most votes and $Y'$ has the second most votes. We then declare them the new leader and challenger. An equilibrium is a node that has an edge to itself.

Intuitively, this could be thought of as either

1. the election results based on every voter applying the leader rule based on the perception of $(X,Y)$, or
2. the new perception of the leader and challenger after every voter applies the leader rule based on the perception of $(X,Y)$, in a poll or in the media.

For example, if all voters think $X$ is the leader and $Y$ is the challenger, then we suppose that voters apply the leader rule based on that perception to determine their expected strategy on election day. If another poll was taken, then $X'$ would rise to the top of the polls, and $Y'$ would be the second most popular candidate in the polls, leading to a new perception of $(X',Y')$ as the leader and challenger.

> **Definition:** We call $Y$ the **strongest challenger** of $X$ if $Y$ is the candidate with the best pairwise matchup against $X$. That is, $P(Y>X) > P(Z>X)$ for all $Z \notin \{X,Y\}$.

> **Theorem:** (Laslier) $(X,Y)$ is an equilibrium if and only if $X$ is a unique Condorcet winner and $Y$ is the strongest challenger of $X$. \label{thm:equilibrium}

**Proof:** By Corollary \ref{cor:unique_condorcet_winner}, if $X$ is a unique Condorcet winner, then $X$ will remain the leader after every voter applies the leader rule. Therefore, we know that $(X,Y)$ has an edge to $(X,Y')$ for some $Y'$ such that the votes $P(Y'>X) > P(Z>X)$ for all $Z \notin\{X,Y'\}$. That is, $Y'$ must have the best pairwise matchup against $X$. Therefore, if $Y$ is the strongest challenger of $X$, then $(X,Y)$ is an equilibrium.

Suppose now that $(X,Y)$ is an equilibrium. Then we must have that $P(X>Y) > P(Y>X) > P(Z>X)$ for all $Z \neq X$. Since $P(X>Y) > 0.5 > P(Y>X)$, we must have that $P(Z>X) < 0.5$ for all $Z \neq X$, meaning $X$ is a unique Condorcet winner. Since $P(Y>X) > P(Z>X)$ for all $Z \notin\{X,Y\}$, we must have that $Y$ is the strongest challenger of $X$. **QED**

In the language of our assumed reality, this means that if voters go into the voting booth expecting $X$ to win and $Y$ to be in second place, and they apply the leader rule based on that perception, then the expectation matches the reality if and only if $X$ is a unique Condorcet winner and $Y$ is the strongest challenger of $X$. In a sense, this implies that the polling is accurate to the results if and only if the winner is a unique Condorcet winner, and the second place candidate was actually the strongest candidate to challenge them.

The following Corollary is an immediate consequence of the previous theorem.

> **Corollary:** If there is no unique Condorcet winner, then there is no equilibrium. \label{cor:no_equilibrium}

In this case, there must instead be a cycle of nodes, where each node has an edge to another node, and the last node has an edge back to the first node. There is no stable leader-challenger pair in this case, however, the election must still occur eventually. We focus on the general dynamics of the leader rule to make conclusions about the possible outcomes in this case.

> **Definition:** We define the set of "Leader Rule Outcome Nodes" to be the nodes with at least one edge to them. We call the candidates who are the leader in at least one Leader Rule Outcome Node to be a "Leader Rule Outcome".

> **Corollary:** If $X$ is a unique Condorcet winner, then $X$ is a Leader Rule Outcome. If $X$ is a Condorcet loser, then $X$ is not a Leader Rule Outcome.

**Proof:** By theorem \ref{thm:equilibrium}, we know that $(X,Y)$ is an equilibrium if and only if $X$ is a unique Condorcet winner and $Y$ is the candidate with the best pairwise matchup against $X$. Therefore, if $X$ is a unique Condorcet winner, there exists at least one equilibrium node, which has an edge to itself, where $X$ is the leader, making $X$ a Leader Rule Outcome. Conversely, if $X$ is a Condorcet loser, by Corollary \ref{cor:majority_and_loser}, $X$ will never be the leader after all voters apply the leader rule, so $X$ is not a Leader Rule Outcome. **QED**

> **Lemma:** Candidate $X$ is a Leader Rule Outcome if and only if one of the following holds: \label{lem:lr_outcome}
>
> 1. $X$ has a pairwise match-up against some candidate $Y$ that is stronger than any pairwise match-up against $X$. That is, there exists some $Y$ such that $P(X>Y) > P(Z>X)$ for all $Z \neq X$. Then $(X,Y)$ has an edge to a node where $X$ is the leader, making $X$ a Leader Rule Outcome.
> 2. $X$ has the strongest pairwise match-up against some candidate $Y \neq X$, and that match-up is stronger than Y's match-up against some candidate $Y'\neq Y$. That is, there exists some $Y$ such that $P(X>Y) > P(Z>Y)$ for all $Z \neq X$ and there exists some $Y'$ such that $P(X>Y) > P(Y>Y')$ for some $Y'$. Then $(Y,Y')$ has an edge to a node where $X$ is the leader, making $X$ a Leader Rule Outcome.

**Proof:** If condition 1 holds, then consider the node $(X,Y)$. We have that $P(X>Y) > P(Z>X)$ for all $Z \neq X$, so $X$ will have the most votes after every voter applies the leader rule, making $X$ the leader. Note that condition 1 holds when $X$ is a unique Condorcet winner, since $P(X>Z) > 0.5 > P(Z>X)$ for all $Z \neq X$. If condition 1 does not hold, then for all $Y$, there exists some $Z$ such that $P(Z>X) > P(X>Y)$, meaning that $(X,Y)$ cannot have an edge to any node where $X$ is the leader. That is, no node where $X$ is the leader can have an edge to a node where $X$ is the leader.

If condition 2 holds, then consider the node $(Y,Y')$. We have that $P(X>Y) > P(Z>Y)$ for all $Z\notin\{X,Y\}$, so $X$ will have more votes than all candidates other than $Y$ after every voter applies the leader rule. However, since $P(X>Y) > P(Y>Y')$, $X$ will have more votes than $Y$ as well, making $X$ the leader. If condition 2 does not hold, then for all nodes where $X$ is not the leader, $(Y,Y')$ where $Y \neq X$, there exists some $Z$ such that $P(Z>Y) > P(X>Y)$, meaning that $(Y,Y')$ cannot have an edge to any node where $X$ is the leader. That is, no node where $X$ is not the leader can have an edge to a node where $X$ is the leader. **QED**

In short, we have essentially two archetypes for a candidate to be a Leader Rule Outcome:

1. A candidate on the offense (TODO: is this the best intuitive phrasing?): they beat some candidate by a stronger margin than any candidate beats them. This is the case of a unique Condorcet winner, but it can also be the case for a non-Condorcet winner if they have a sufficiently strong match-up against some candidate.
2. A candidate who strongly counters another candidate: they have the strongest match-up against some candidate, and that match-up is stronger than that candidate's match-up against some other candidate. Intuitively, this means that the electorate may have a strong "reaction" against some leader $Y$, and $X$ is more strongly preferred to $Y$ than $Y$ is to whoever the challenger is.

If the polling is incorrect in who the leader is, then the leader rule can cause an upset, where the candidate most preferred to the expected winner will win instead. However, by Corollary \ref{cor:unique_condorcet_winner}, if the Condorcet winner does not win, they still at least get 50%. Thus, even if the Condorcet winner is not elected, the actual winner necessarily gets over 50% of the vote and the mandate that comes with that, and the Condorcet winner gets at least 50% of the vote. The public perception of this result would not be that the Condorcet winner lost (which the voters could not discern from the ballot data), but instead it would look like the electorate was in strong agreement and multiple candidates had earned a majority of the vote.

## Pairwise Rankings

> **Definition:** A "Pairwise Ranked Ordering" is an ordered list: 1. $X_1 > Y_1$. 2. $X_2>Y_2$. etc. A "Coherent Pairwise Ranked Ordering" (CPRO) is one that does not contain contradictions. For example, if $A>B$ is the strongest pairwise margin at the top of the list, then $B>A$ must be the weakest, at the bottom of the list. More generally, if we have $m$ total candidates, and a list of the $\ell=m(m-1)$ pairwise match-ups, then if item $$i\in\{0,1,\ldots,\ell-1\}$$ is $X>Y$, then $Y>X$ must be item $\ell-i$. Since a CPRO is uniquely determined by the first half of the list, we sometimes omit the second half for brevity.

**Theorem:** The graph of state nodes is determined uniquely by the ranked ordering of pairwise match-up strengths (the CPRO). \label{thm:cpro_graph}

**Proof:** The determination of the new leader and challenger depend entirely on the relative strengths of the pairwise match-ups. That is, by sorting $P(X>Y),P(Z_1>X),\ldots$, we can uniquely determine the transitions between state nodes. QED

This gives us an algorithm to determine where the node (X,Y) will transition based on the CPRO.

**Algorithm 1:** Identifying the CPRO entry $X_i>Y_i$ as $(X_i,Y_i)$,

```py
def node_target_from_ranking(ranking_list, leader, challenger):
    new_leader = None
    for (i,j) in ranking_list:
        # we check for (leader,challenger) or (i,leader)
        if (i == leader and j == challenger) or j == leader:
            if not new_leader:
                new_leader = i
            else:
                return (new_leader, i)
```

Intuitively, we look for either 'leader > challenger' or 'candidate > leader' in the ranked list of pairwise match-ups. The first time we see one of those, we set the new leader to be the candidate that is listed first in that match-up. The second time we see one of those, we set the new challenger to be the candidate that is listed first in that match-up, and then we are done.

> **Proposition:** Any CPRO of pairwise match-ups can be realized.

We give a proof by construction, using [McGarvey's theorem](https://www.jstor.org/stable/1907926){:target="_blank"}. Let $m$ be the total number of candidates, $\ell=m(m-1)$ the total number of pairwise match-ups, and list the first half of the match-ups $i=0,1,\ldots,\ell/2-1$ match-up as $X_i > Y_i$.

To ensure that $X_i > Y_i$ is the $i+1$th strongest match-up, we add $\frac{\ell}2-i$ voters of the following two types:

1. $X_iY_iZ_1\ldots Z_{m-2}$, for $Z_1\ldots Z_{m-2}$ being any arbitrary ordering of the remaining candidates.
2. $Z_{m-2}\ldots Z_1X_iY_i$

By reversing the other candidates, these two voters types cancel out all pairwise match-ups except it gives +2 to $X_i>Y_i$ for each pair of voters of these types:

1. For $X_i$ versus $Z_j$, the first type of voter gives +1 to $X_i>Z_j$, while the second type of voter gives -1 to $X_i>Z_j$, so they cancel out.
2. For $Y_i$ versus $Z_j$, the first type of voter gives -1 to $Y_i>Z_j$, while the second type of voter gives +1 to $Y_i>Z_j$, so they cancel out.
3. For $Z_j$ versus $Z_k$, the first type of voter gives +1 to $Z_j>Z_k$, while the second type of voter gives -1 to $Z_j>Z_k$, so they cancel out.
4. For $X_i$ versus $Y_i$, both types of voters give +1 to $X_i>Y_i$, so they add up to +2.

As an example, take the following CPRO on three candidates.

1. $A > B$
2. $C > A$
3. $B > C$

To ensure A > B is the strongest matchup, we add the following voters:

- $ABC$: 3 voters
- $CAB$: 3 voters

With only three candidates, there is only one trivial way to order the remaining candidates, making this construction unique. The remaining two match-ups induce the following voters:

- $CAB$: 2 voters (for the C > A match-up)
- $BCA$: 2 voters (for the C > A match-up)
- $BCA$: 1 voter (for the B > C match-up)
- $ABC$: 1 voter (for the B > C match-up)

In total, this gives

- $ABC$: 4 voters
- $BCA$: 3 voters
- $CAB$: 5 voters

In summary, this tells us that we can analyze the possible graphs by instead considering the possible CPROs.

**Definition:** We define the pairwise matrix such that entry (i,j) represents the number of voters who prefer candidate i over candidate j. We define the diagonal entries to be zero.

The pair-wise matrix for the above profile is as follows: Entry the row candidate is the one preferred over the column candidate.

|     | $A$ | $B$ | $C$ |
|-----|-----|-----|-----|
| $A$ | --  | 9   | 4   |
| $B$ | 3   | -   | 7   |
| $C$ | 8   | 5   | -   |

We can confirm that the match-up strengths match the precise list we defined.

Let us apply the algorithm on the CPRO to determine the edges of the graph, for at least one edge. For convenience, let us list the full list:

1. $A > B$
2. $C > A$
3. $B > C$
4. $C > B$
5. $A > C$
6. $B > A$

Let us consider the $(A,B)$ node. We look for $A>B$ or $X>A$, since $A$ is the leader. We see that the first entry is $A>B$, so $A$ will be the leader. The second entry is $C>A$, so $C$ will be the challenger. Thus, $(A,B)$ has an edge to $(A,C)$.

> **Theorem:** The pairwise matrix can be used to determine the precise votes or percents that each candidate will get after all voters apply the leader rule at a particular node.
>
> 1. Take the column corresponding to the leader $X$. The non-diagonal entries will be the precise share that each non-leader candidate $Z$ receives. That is because the entry $(Z,X)$ in the pairwise matrix represents the probability that $Z$ is preferred over $X$.
> 2. Replace the diagonal entry (which is zero) with the entry in the same row corresponding to the challenger. That is because the entry $(Y,X)$ in the pairwise matrix represents the probability that $X$ is preferred over $Y$.

## Equilibrium Paths

> **Theorem:** With three candidates, if a Condorcet winner and equilibrium exists, the leader rule always converges to that equilibrium, from any starting node, in a maximum of three steps. However, the Condorcet winner will win after at most two steps.

**Proof:** Note that the CPRO is uniquely determined by three pairwise match-ups. Suppose that candidate A is a Condorcet winner. That is, we have $A>B$ and $A>C$ in the first half of the CPRO. By previous results, we know that any node where $A$ is the leader has an edge to the equilibrium. Therefore, we prove the theorem by showing that any node where $A$ is not the leader has an edge to a node where $A$ is the leader, or another node that has an edge to a node where $A$ is the leader, in at most two steps.

We have two cases:

**Case 1**: If the top two match-ups involve $A$, then without loss of generality suppose that it is $A>B$ and then $A>C$. This means $C$ has the best pairwise match-up against $A$, so $(A,C)$ is the unique equilibrium. We consider the cases of the three possible starting leaders:

- If $A$ is the leader, and $B$ is the challenger, then the node must have an edge to $(A,C)$, since $B>A$ is the weakest pairwise match-up, $B$ must have the fewest approvals.
- If $B$ is the leader, then $A>B$ is the strongest pairwise match-up, so any node where $B$ is the leader must have an edge to a node where $A$ is the leader.
- If $C$ is the leader, then $A>C$ is the strongest relevant pairwise match-up, since $A>B$ is not possibly relevant. Thus, any node where $C$ is the leader must have an edge to a node where $A$ is the leader.

In any case, we have that $A$ will be the leader after at most one step. We have already established that any node where $A$ is the leader has an edge to the equilibrium, so we have that the equilibrium will be reached after at most two steps.

**Case 2**: If there exists any match-up not involving $A$ that is stronger than one of $A$'s match-ups against another candidate, then that induces a possible non-Condorcet Leader Rule Outcome.

Without loss of generality, suppose that $B>C$ is one of the top two strongest match-ups, making $C$ a Condorcet loser.

- If the $B>C$ match-up is stronger than $A>C$, then $(C,B)$ will have an edge to $(B,A)$.
- If $B>C$ is not stronger than $A>C$ (meaning $A>C$ is the strongest pairwise match-up), then $(B,C)$ will have an edge to $(B,A)$.

In either case, $B$ must have fewer than 50% approvals in the outcome after $(B,A)$, while $A$ must have more than 50% approvals, by the assumption that $A$ is the Condorcet winner. Since $C$ is a Condorcet loser, they must also have less than 50% approvals, so $A$ will be the leader in at most two steps. This node may not be the equilibrium, but must have an edge to the equilibrium, giving it at most three steps. **QED**

This makes three candidate Approval highly Condorcet efficient, using the leader rule. While the Condorcet winner may not be the unique Leader rule outcome, we can assure that the Condorcet winner will win after at most two steps, even if the voter perception is wildly off.

> **Theorem:** With four or more candidates, even if a unique Condorcet winner and equilibrium exist, it may not be reachable by every starting node. \label{thm:non_convergence}

**Proof:** We present a counterexample based on a profile created by Rob LeGrand. Their example is included in the [appendix](#appendix). Suppose we have the CPRO:

1. $A > D$
2. $C > A$
3. $D > C$
4. $B > D$
5. $B > A$
6. $B > C$

Here, we clearly have a Condorcet winner, $B$. However, they have the weakest pairwise wins, and thus we can show that $B$ will never be the leader unless $B$ starts as the leader. All nodes where $B$ is the leader will have an edge to $(B,C)$, since $C$ is the candidate with the best pairwise match-up against $B$, and by Corollary \ref{cor:unique_condorcet_winner}, a Condorcet winner stays the leader when starting as the leader.

If we have a leader who is not $B$, then at least one candidate will have a stronger margin against that leader than $B$. Therefore, $B$ cannot become the leader unless $B$ starts as the leader.

In particular, we can see that there will be a cycle $(A,B)$ to $(C,B)$ to $(D,B)$ and back to $(A,B)$. **QED**

<img src="/assets/img/leader_rule/island.png" alt="Leader Rule Non-Convergence Example" style="max-width: 600px;">

The primary aspect of this pathology is when the Condorcet winner has the weakest pairwise wins. If every other candidate has a stronger pairwise win against some candidate than all of the Condorcet winner's pairwise wins (particularly, if there is a cycle "below" the Condorcet winner), then the Condorcet winner will never be the leader, and remain the challenger, unless they start as the leader. Thus, if a Condorcet winner is "lukewarm" and only very minimally preferred to the other candidates, then by failing to inspire passionate support, they may fail to win despite being the Condorcet winner, and always earning over 50% of the vote by Corollary \ref{cor:unique_condorcet_winner}.

## Case Studies

We shall analyze three elections using ranked.vote pairwise data, to see what the leader rule dynamics would have looked like in those elections. The percentages are based on the head-to-head match-ups of voters who expressed a preferences, which may not extend to the all voters if asked directly. For example, in the 2025 NYC election, a large proportion of voters bullet voted for Andrew Cuomo, and thus did not express a preference between Zohran Mamdani and Brad Lander. Therefore, the nearly 70% head-to-head result for Mamdani vs. Lander may not be representative of the entire electorate, but rather only of the subset of voters who expressed a preference between those two candidates. However, we use the simplifying assumption that the head-to-head results are representative of the entire electorate, to get a rough picture of the leader rule dynamics in these elections, along with the other axioms we have laid out in the introduction.

### Alaska House Special Election 2022

[ranked.vote page for this election](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}.

Alaska's 2022 House Special Election was a controversial election where the IRV winner, Mary Peltola (D), was not the Condorcet winner, while the true Condorcet winner, Nick Begich III (R), was eliminated in the first round. The third candidate, Sarah Palin (R), was the Condorcet loser. The election was widely seen as a failure of IRV, and led to a backlash against IRV in Alaska, with the state failing to repeal it by only about 700 voters out of over 320,000 votes cast in the 2024 ballot measure. Another repeal effort is currently underway in 2026.

An aspect of the pathology was the unintuitive vote splitting and spoiler effect that occured between the Republican candidates. The voters who sincerely voted for Palin first and Begich second managed to get themselves their least preferred candidate, Peltola, elected. By voting first for Palin, the Condorcet loser, they kept her in the race long enough to eliminate the only viable Republican candidate, Begich. Thus, Peltola was able to win the final round since an insufficient number of Begich voters had Palin as their second choice.

The actual first round results were:

| Candidate       | First Round Percentage               |
|-----------------|--------------------------------------|
| Mary Peltola    | 38.9%                                |
| Sarah Palin     | 30.5%                                |
| Nick Begich III | 27.5%                                |

Using the head-to-head results from Alaska 2022, we can simulate the leader rule. The head-to-head results were:

| Head-to-Head       | Winner      | Percentage    |
|--------------------|-------------|---------------|
| Begich vs. Palin   | Begich      | 61.4% : 38.6% |
| Begich vs. Peltola | Begich      | 52.5% : 47.5% |
| Peltola vs. Palin  | Peltola     | 51.4% : 48.6% |

Thus, the CPRO is as follows:

1. Begich > Palin
2. Begich > Peltola
3. Peltola > Palin

A reader may confirm by Lemma \ref{lem:lr_outcome} that Begich is the only Leader Rule Outcome, since no other candidate has a pairwise match-up against some candidate that is stronger than Begich's match-ups.

Based on Corollary \ref{cor:majority_and_loser}, Palin's Condorcet loser status would have made it impossible for her to win under the leader rule, even if she had been the perceived leader. Further, Begich's strong head-to-heads against both Palin and Peltola would have given him an extremely strong pull. In fact, he is the only Leader Rule Outcome. If every voter applied the leader rule, and these head to heads extend to the entire electorate, Begich would be the only candidate who could have won.

The directed graph of leader-challenger pairs is as follows:

<img src="/assets/img/leader_rule/alaska.png" alt="Leader Rule Alaska 2022" style="max-width: 600px;">

Here is how to read this graph:

- A node like "Peltola, Palin" represents the scenario where Peltola is the leader and Palin is the challenger. This node points to the red node "Begich, Peltola", which means that if all voters enter the voting booth expecting Peltola to be the leader, and see Palin as the challenger, then after everyone applies the leader rule, the final result will have Begich in first place and Peltola in second place.
- Similarly, the node "Peltola, Begich" actually points to the "Begich, Palin" node, meaning that if everyone expects Peltola to be the leader and Begich to be the challenger, then after everyone applies the leader rule in the voting booth, the final result will have Begich in first place and Palin in second place. Peltola actually falls to third place in this scenario, because Begich's head-to-head against Peltola was stronger than Palin's head-to-head against Peltola, which was stronger than Peltola's head-to-head against Begich.
- A node is colored red if it is an equilibrium (it points to itself), and blue if any nodes have an edge to it (it is a Leader Rule Outcome Node), but is not an equilibrium.

The equilibrium has Begich as the leader and Peltola as the challenger. This is consistent with Begich being the Condorcet winner, and Peltola having the best head-to-head result against Begich.

Notice that after any starting point, Begich becomes the leader, as confirmed by Lemma \ref{lem:lr_outcome}. However, interestingly, in the case where Peltola is the leader and Begich is the challenger, the next iteration has Begich as the leader and Palin as the challenger. This is because Palin's head-to-head against Peltola was stronger than Peltola's head-to-head against Begich. Therefore, if Peltola was the leader, and Begich the challenger, and every voter voted using the leader rule, the result would actually have the leader come in last place in approval percentage.

If we assume that Begich truly had the two strongest pairwise wins, then the leader rule would have guaranteed his election in Alaska, by over 50%, and potentially over 60%. The full table is included [in the Appendix](#alaska-house-special-election-2022-table), but we display the results of the leader rule when Begich is correctly assumed to be the leader.

| Leader | Challenger | Approvals                                   |
|--------|------------|---------------------------------------------|
| Begich | Peltola    | Begich: 52.5%, Peltola: 47.5%, Palin: 38.6% |
| Begich | Palin      | Begich: 61.4%, Peltola: 47.5%, Palin: 38.6% |

Both cases are strongly majoritarian outcomes which would have likely resulted in less outrage at the results.

### NYC Democratic Mayoral Primary 2025

[ranked.vote page for this election](https://ranked.vote/report/us/ny/nyc/2025/07/mayor){:target="_blank"}.

The 2025 NYC Democratic Mayoral Primary was a very crowded field, with over 10 candidates. Before the election, it was widely perceived that Andrew Cuomo was the frontrunner, with Zohran Mamdani as the main challenger. It was expected that Cuomo would win the first round under IRV, but that Mamdani might get enough transfers to win in the final round.

Here we reduce the field to the top four candidates: Zohran Mamdani, Brad Lander, Andrew Cuomo, and Adrienne Adams.

The first round results were:

| Candidate       | First Round Percentage (Approximate) |
|-----------------|--------------------------------------|
| Zohran Mamdani  | 43.6%                                |
| Andrew Cuomo    | 35.9%                                |
| Brad Lander     | 11.2%                                |
| Adrienne Adams  | 4.1%                                 |

The head-to-head results were:

| Head-to-Head        | Winner      | Percentage    |
|---------------------|-------------|---------------|
| Mamdani vs. Adams   | Mamdani     | 74.8% : 25.2% |
| Lander vs. Adams    | Lander      | 72.7% : 27.3% |
| Mamdani vs. Lander  | Mamdani     | 69.6% : 30.4% |
| Mamdani vs. Cuomo   | Mamdani     | 56.4% : 43.6% |
| Lander vs. Cuomo    | Lander      | 54.4% : 45.6% |
| Adams vs. Cuomo     | Adams       | 50.3% : 49.7% |

We can see that, in fact, the perceived leader Cuomo was actually a Condorcet loser (when compared among the top four candidates), while the perceived challenger Mamdani was the Condorcet winner. Lander was a strong contender, with strong head-to-head results against both Cuomo and Adams, but was not the Condorcet winner due to his weaker head-to-head against Mamdani. Adams, while narrowly beating Cuomo head-to-head, was not perceived as a particularly strong candidate, and had very weak head-to-head results against both Mamdani and Lander.

The two leader rule outcomes are Mamdani and Lander, with Mamdani being the equilibrium, as the Condorcet winner. Lander is a Leader Rule Outcome because of his strong head-to-head against Adams. The node with Lander as the leader and Adams as the challenger has an edge to the node with Lander as the leader and Mamdani as the challenger, since Lander's head-to-head against Adams is stronger than Mamdani's head-to-head against Lander. However, the plausibility of this node being the perception of voters is extremely low, since Adams was perceived as a very weak candidate. Therefore, it's extremely likely that Mamdani would win in any reasonable perception of the race, assuming voters vote strategically using the leader rule and the head-to-head results extend to the entire electorate.

The directed graph of leader-challenger pairs is as follows:

<img src="/assets/img/leader_rule/nyc.png" alt="Leader Rule NYC 2025" style="max-width: 600px;">

We see the red equilibrium node with Mamdani as the leader and Cuomo as the challenger, and two other blue Leader Rule Outcome Nodes: (Lander, Mamdani) and (Mamdani, Lander).

### Minneapolis City Council Ward 2 2021

[ranked.vote page for this election](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}.

This was a very notable election because it actually had a Condorcet cycle. The cycle was between Cam Gordon, Robin Wonsley, and Yusra Arab. The actual winner was Robin Wonsley, who defeated Yusra Arab in the final round of IRV. However, Cam Gordon beat Robin Wonsley head-to-head, and Yusra Arab beat Cam Gordon head-to-head, creating a Condorcet cycle.

The first round results were:

| Candidate       | First Round Percentage |
|-----------------|------------------------|
| Robin Wonsley   | 28.1%                  |
| Yusra Arab      | 27.7%                  |
| Cam Gordon      | 25.6%                  |

The head-to-head results were:

| Head-to-Head         | Winner      | Percentage    |
|----------------------|-------------|---------------|
| Arab vs. Gordon      | Arab        | 51.3% : 48.7% |
| Gordon vs. Wonsley   | Gordon      | 50.5% : 49.5% |
| Wonsley vs. Arab     | Wonsley     | 50.1% : 49.9% |

There was a fourth and fifth candidate who was not competitive, so we will omit them from this analysis. The directed graph of leader-challenger pairs is as follows:

<img src="/assets/img/leader_rule/mn.png" alt="Leader Rule Minneapolis 2021" style="max-width: 600px;">

We color the cycle in orange. There is no equilibrium in this case, due to the Condorcet cycle. But we have two other blue outcome nodes involving Gordon that eventually lead into the cycle.

Observe the four-node cycle between Wonsley, Arab, and Gordon:

| Leader | Challenger | Approvals | Target |
|--------|------------|-----------|--------|
| Arab   | Wonsley    | Wonsley: 50.1%, Arab: 49.9%, Gordon: 48.7% | (Wonsley, Arab) |
| Wonsley | Arab | Gordon: 50.5%, Wonsley: 50.1%, Arab: 49.9% | (Gordon, Wonsley) |
| Gordon | Wonsley | Arab: 51.3%, Gordon: 50.5%, Wonsley: 49.5% | (Arab, Gordon) |
| Arab | Gordon | Arab: 51.3%, Wonsley: 50.1%, Gordon: 48.7% | (Arab, Wonsley) |

If we interpret nodes as possible perceptions of the race, and suppose voters update their strategy based on the leader rule when they answer a poll, then we would basically see a cycle like this:

- Week 1: Voters think Wonsley is the leader, Arab is the challenger. They update their strategies and answer the next poll.
- Week 2: Gordon shoots up to be the leader, since he has the strongest head-to-head against Wonsley. Wonsley falls to challenger, and Arab falls out of the top two (and under 50%), since Wonsley beats Arab and that match-up decides the next approval percentages.
- Week 3: Arab shoots up to be the leader, since she has the strongest head-to-head against Gordon. Gordon falls to challenger, and Wonsley falls out of the top two like Arab did last week.
- Week 4: Arab remains the leader, but Wonsley shoots up to be the challenger, since she has the strongest head-to-head against Arab. Arab's strong head-to-head against Gordon keeps Arab in first place.
- Week 5: Wonsley becomes the leader again, since she has the strongest head-to-head against Arab. Arab falls to challenger, and Gordon falls out of the top two again. And now we're back to week 1.

If we were to imagine this happening in a campaign cycle, we would still eventually have to run the election at some point. And depending on who the perceived leader and challenger are at that moment, we would end up with one of the three candidates winning. Since Approval voting is consistent with its ballot data, the actual winner would be the Condorcet winner of the implied preferences expressed by the ballots, flattening out the cycle. The ballots won't catch fire, the machines won't explode, and no loser will be able to credibly claim they would have beaten the actual winner in a head-to-head match-up, because the ballots won't show that. The result will be legitimate, but close. The winner will get over 50% approvals.

## Discussion

What we can see from these theorems and results is that the leader rule leads to strongly majoritarian outcomes. At least one candidate will have over 50%, including the Condorcet winner if they exist. While the Condorcet winner may not be the final winner, the winner is always the candidate whom the voters most strongly prefer over the expected outcome. That is, the outcome is always either the same or strictly better, to the collective voters, than the expectation of voters going into the voting booth. Further, the actual winner will have a mandate of over 50% approvals.

### The Chicken Dilemma Explored

Many criticize Approval voting for being susceptible to strategic voting, and a chicken dilemma between supporters of two similar candidates. The leader rule actually provides a direct answer to this.

The claim is that if we have two candidates, R and C, who perhaps are conservatives running in a generally right-leaning electorate, then their supporters might bullet vote sufficiently such that a left-leaning candidate L might snake in and win. However, the leader rule reframes this scenario.

Let us assume a generally 1-dimensional spatial model where L voters prefer L>C>R, R voters prefer R>C>L, and C voters split with some preferring C>L>R and others preferring C>R>L. Consider the cases:

| Leader | Challenger | RCL | CRL | CLR | LCR |
|--------|------------|-----|-----|-----|-----|
| R      | C          | R   | C   | C,L | L,C |
| C      | R          | R   | C   | C   | L,C |
| R      | L          | R   | C,R | C,L | L,C |
| C      | L          | R,C | C   | C   | L   |
| L      | C          | R,C | C,R | C   | L   |
| L      | R          | R,C | C,R | C,L | L   |

We notice something very interesting.

- When L is not considered a serious candidate (first two rows), the criticism of the chicken dilemma is that R and C voters *might* bullet vote and cause L to win. The claim is that sufficient bullet voting might end up breaking up the coalition and resulting in plurality-style vote splitting. However, the leader rule actually says that R and C voters (who rank L last) *should* bullet vote, and that this is the optimal strategy. The missing consideration of the criticism is what L voters would do: if they know their candidate is nonviable or unlikely to win, it is optimal to also give an approval to the more agreeable viable candidate, C. Thus, C, in all cases, gets approvals from the moderate C supporters *and* the liberal L supporters, while R only gets approvals from the more extreme R supporters. If C is the Condorcet winner, then the moderate and liberal blocs will coalesce around C, outnumbering the more extreme R, resulting in a C win.
- If L is the leader, however, then the conservative voters who rank L last both team up and form a coalition around both R and C, giving them both a strong pull against L. Therefore, the Chicken dilemma also falls apart here. Assuming that their least favorite candidate is the leader, the optimal strategy for both R and C voters is to approve of both R and C. The game of chicken and bullet voting become non-optimal when they expect the outside candidate to be the most likely winner.
- When L is the challenger, then the leader rule does say that one group of the coalition of R and C voters should bullet vote and defect. The supporters of the likely winner bullet vote to maintain their lead, but the supporters of the candidate who is trailing behind both the leader and the challenger should approve of both candidates to try to push their least preferred candidate down.

In every case, however, the centrist C gets a boost from one side of the more extreme R and L voters, depending on who the leader and challenger are. If C is the Condorcet winner, then the system will settle down with C as the leader, the challenger supporters bullet voting, and the last place supporters also approving C.

However, against the other criticism that Approval elects only bland candidates, there is another consideration to make. If the median voter is more extreme, and closer to R, then the R supporting wing will be larger than the combined C and L supporting wings, and thus R will still win. The outcome from the Leader rule is not always on the *middle* candidate, but rather strongly favors the Condorcet winner. It is entirely possible for one of the "outside" candidates to be the Condorcet winner if the electorate leans sufficiently towards that candidate.

It should be acknowledged, however, that this is not any sort of guarantee that voters would or should bullet vote. While it may be optimal for R and C voters to bullet vote when both are ahead, we do see in real Approval elections in Fargo (TODO: include source) and St. Louis that voters are willing to approve multiple candidates, and support a coalition. Rather, this example should illustrate that Approval would not likely suddenly collapse when voters are strategic. Instead, it is actually robust to strategy when voters are prudent (ex. if their favorite candidate is trailing behind the top two). If a sufficient number of both R and CRL voters choose to approve R and C--say due to the candidates forming a coalition and encouraging their voters to do so--it's even more likely that either R or C will win, strengthening their lead over L. If the electorate is sufficiently right-leaning, then this is a highly representative outcome.

In short, we have a balance between the risk-minimizing strategy of the Leader rule, which is not compatible with coalitions of candidates who are both viable, and the fact that we do, in fact, see coalitions in real Approval elections. In real elections, it's likely we will see coalitions between viable candidates and bullet voting for non-viable candidates, which would weaken the strongly majoritarian guarantees of the leader rule. However, the leader rule still shows that widespread strategy and majoritarian outcomes are not necessarily at odds, and that strategic voting can actually lead to more majoritarian outcomes, rather than less.

## Other Considerations and Further Research

Some considerations must be made to the plausibility or realism of the axioms. For one, this analysis does not take into account sincere voters who do not adjust their acceptability line strategically. It also does not allow for the possibility that some voters may not agree on the perceived leader and challenger. In our increasingly divisive media bubbles, the perception of a race to one bloc of voters could be significantly different from another. If the supporters of the two major candidates believe their candidate is the leader, then that would result in more bullet voting, and less support for the more moderate candidates who might be the compromise often ranked between the two major candidates. This could lead to more extreme outcomes, and less majoritarian outcomes, than the leader rule would predict.

Some potential questions to explore in future research include:

- If we allow ties in the pairwise match-ups, and allow one node to have edges to multiple nodes probabilistically, how does this affect the dynamics?
- How many non-strategic voters, who apply a fixed sincere strategy, would it take to break the convergence to the equilibrium?
- If, instead of all voters applying the leader rule simultaneously, we have voter adjusting their strategy based on some probability (ex. 50% of voters apply the leader rule, while 50% maintain their current strategy), will the edges of the graph stay the same, or will they change?
- If we suppose that voters of different demographics have different perceptions of the leader and challenger, or suppose that polls are intentionally misleading, can the outcome be manipulated by a malicious actor who controls the polls?

## Appendix

Here is the original example by Rob LeGrand where the Leader rule does not converge to the Condorcet winner:

| Voter Type     | Count |
|----------------|-------|
| A>B>C>D        | 17    |
| A>D>C>B        | 17    |
| B>C>A>D        | 21    |
| C>B>A>D        | 18    |
| D>B>C>A        | 13    |
| D>C>A>B        | 14    |

Total voters: 100

The head-to-head results are:

| Head-to-Head| Winner | Percentage |
|-------------|--------|------------|
| A vs. D     | A      | 73% : 27%  |
| C vs. A     | C      | 66% : 34%  |
| D vs. C     | D      | 61% : 39%  |
| B vs. D     | B      | 56% : 44%  |
| B vs. A     | B      | 52% : 48%  |
| B vs. C     | B      | 51% : 49%  |

The Condorcet winner is B, and there is an equilibrium under the leader rule with B as the leader and C as the challenger:

| Candidate | Approval Percentage (Equilibrium) |
|-----------|-----------------------------------|
| B         | 51%                               |
| C         | 49%                               |
| A         | 48%                               |
| D         | 44%                               |

However, unless the initial leader is B, the leader rule does not converge to B. Instead, it will settle into a cycle where B is always the challenger, but never the leader.

| Leader | Challenger | Next Leader | Next Challenger  |
|--------|------------|-------------|------------------|
| A (73%)| B (56%)    | C (66%)     | B (52%)          |
| C (66%)| B (52%)    | D (61%)     | B (51%)          |
| D (61%)| B (51%)    | A (73%)     | B (56%)          |

The key observation is that while B is the Condorcet winner, we have a cycle among A, C, and D where each one has a very strong head-to-head win against one of the others, allowing B to stay perpetually above 50% approval as the challenger, but never becoming the leader.

Here is a graph of the leader-challenger pairs in this example:

<img src="/assets/img/leader_rule/island.png" alt="Leader Rule Non-Convergence Example" style="max-width: 600px;">

---

Here are the full tables for the three example elections analyzed above.

### Alaska House Special Election 2022 Table

| Leader | Challenger | Approvals | Target |
|--------|------------|-----------|--------|
| Begich | Peltola | Begich: 52.5%, Peltola: 47.5%, Palin: 38.6% | (Begich, Peltola) |
| Begich | Palin | Begich: 61.4%, Peltola: 47.5%, Palin: 38.6% | (Begich, Peltola) |
| Peltola | Begich | Begich: 52.5%, Palin: 48.6%, Peltola: 47.5% | (Begich, Palin) |
| Peltola | Palin | Begich: 52.5%, Peltola: 51.4%, Palin: 48.6% | (Begich, Peltola) |
| Palin | Peltola | Begich: 61.4%, Peltola: 51.4%, Palin: 48.6% | (Begich, Peltola) |
| Palin | Begich | Begich: 61.4%, Peltola: 51.4%, Palin: 38.6% | (Begich, Peltola) |

### NYC Democratic Mayoral Primary 2025 Table

| Leader | Challenger | Approvals | Target |
|--------|------------|-----------|--------|
| Mamdani | Cuomo | Mamdani: 56.4%, Cuomo: 43.6%, Lander: 30.4%, Adams: 25.2% | (Mamdani, Cuomo) |
| Mamdani | Lander | Mamdani: 69.6%, Cuomo: 43.6%, Lander: 30.4%, Adams: 25.2% | (Mamdani, Cuomo) |
| Mamdani | Adams | Mamdani: 74.8%, Cuomo: 43.6%, Lander: 30.4%, Adams: 25.2% | (Mamdani, Cuomo) |
| Cuomo | Mamdani | Mamdani: 56.4%, Lander: 54.4%, Adams: 50.3%, Cuomo: 43.6% | (Mamdani, Lander) |
| Cuomo | Lander | Mamdani: 56.4%, Lander: 54.4%, Adams: 50.3%, Cuomo: 45.6% | (Mamdani, Lander) |
| Cuomo | Adams | Mamdani: 56.4%, Lander: 54.4%, Adams: 50.3%, Cuomo: 49.7% | (Mamdani, Lander) |
| Lander | Mamdani | Mamdani: 69.6%, Cuomo: 45.6%, Lander: 30.4%, Adams: 27.3% | (Mamdani, Cuomo) |
| Lander | Cuomo | Mamdani: 69.6%, Lander: 54.4%, Cuomo: 45.6%, Adams: 27.3% | (Mamdani, Lander) |
| Lander | Adams | Lander: 72.7%, Mamdani: 69.6%, Cuomo: 45.6%, Adams: 27.3% | (Lander, Mamdani) |
| Adams | Mamdani | Mamdani: 74.8%, Lander: 72.7%, Cuomo: 49.7%, Adams: 25.2% | (Mamdani, Lander) |
| Adams | Cuomo | Mamdani: 74.8%, Lander: 72.7%, Adams: 50.3%, Cuomo: 49.7% | (Mamdani, Lander) |
| Adams | Lander | Mamdani: 74.8%, Lander: 72.7%, Cuomo: 49.7%, Adams: 27.3% | (Mamdani, Lander) |

### Minneapolis City Council Ward 2 2021 Table

| Leader | Challenger | Approvals | Target |
|--------|------------|-----------|--------|
| Wonsley | Arab | Gordon: 50.5%, Wonsley: 50.1%, Arab: 49.9% | (Gordon, Wonsley) |
| Wonsley | Gordon | Gordon: 50.5%, Arab: 49.9%, Wonsley: 49.5% | (Gordon, Arab) |
| Arab | Wonsley | Wonsley: 50.1%, Arab: 49.9%, Gordon: 48.7% | (Wonsley, Arab) |
| Arab | Gordon | Arab: 51.3%, Wonsley: 50.1%, Gordon: 48.7% | (Arab, Wonsley) |
| Gordon | Wonsley | Arab: 51.3%, Gordon: 50.5%, Wonsley: 49.5% | (Arab, Gordon) |
| Gordon | Arab | Arab: 51.3%, Wonsley: 49.5%, Gordon: 48.7% | (Arab, Wonsley) |

The cycle, in particular, is between the nodes:

| Leader | Challenger | Approvals | Target |
|--------|------------|-----------|--------|
| Arab | Wonsley | Wonsley: 50.1%, Arab: 49.9%, Gordon: 48.7% | (Wonsley, Arab) |
| Wonsley | Arab | Gordon: 50.5%, Wonsley: 50.1%, Arab: 49.9% | (Gordon, Wonsley) |
| Gordon | Wonsley | Arab: 51.3%, Gordon: 50.5%, Wonsley: 49.5% | (Arab, Gordon) |
| Arab | Gordon | Arab: 51.3%, Wonsley: 50.1%, Gordon: 48.7% | (Arab, Wonsley) |

## References

A very big thank you to Rob LeGrand for his contributions, the counterexample that inspired Theorem \ref{thm:non_convergence}, and for telling me about this strategy.

Laslier, J. F. (2009). The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate. *Journal of Theoretical Politics*, 21(1), 113-136. [https://journals.sagepub.com/doi/10.1177/0951629808097286](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}

McGarvey, D. C. (1953). A Theorem on the Construction of Voting Paradoxes. Econometrica, 21(4), 608–610. [https://doi.org/10.2307/1907926](https://doi.org/10.2307/1907926){:target="_blank"}

[ranked.vote](https://ranked.vote){:target="_blank"} Election Reports:

- Alaska House Special Election 2022: [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}
- NYC Democratic Mayoral Primary 2025: [https://ranked.vote/report/us/ny/nyc/2025/07/mayor](https://ranked.vote/report/us/ny/nyc/2025/07/mayor){:target="_blank"}
- Minneapolis City Council Ward 2 2021: [https://ranked.vote/report/us/mn/2021/11/ward-2](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}
