---
layout: distill
title: The Approval Dynamics of Laslier's Leader Rule
date: 2026-02-11
description: How the leader rule induces a graph and dynamical system on candidate perceptions.
giscus_comments: true
importance: 2
tags: voting
category: polisci
featured: false
related_posts: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: The Leader Rule
  - name: A Practical Simulation 
    subsections:
      - name: Alaska House Special Election 2022
      - name: NYC Democratic Mayoral Primary 2025
      - name: Minneapolis City Council Ward 2 2021
  - name: Appendix 
    subsections:
      - name: Alaska House Special Election 2022 Table
      - name: NYC Democratic Mayoral Primary 2025 Table
      - name: Minneapolis City Council Ward 2 2021 Table
  - name: References
---

## Introduction

The Leader Rule is a strategy under approval voting where voters choose their sincere strategy based on who the perceived frontrunners are:

> **The Leader Rule**: Call the candidate perceived most likely to win the "leader", and the second most likely candidate to win the "challenger". The leader rule strategy is as follows:
>
> 1. Approve all candidates strictly preferred to the leader
> 2. Approve the leader if and only if you prefer them to the challenger

We will not delve into the weeds of why this is an optimal strategy, but our analysis focuses on what happens when every voter applies the leader rule simultaneously.

**Definition**: We denote the percentage of voters who prefer X>Y as $$P(X>Y)$$. Note that $$P(Y>X)=1-P(X>Y)$$.

For our axioms of this analysis, we assume

1. Voters have complete and transitive preferences over candidates. They do not prefer any candidates equally.
2. Voters always use sincere strategies. That is, if they prefer candidate X over Y, then whenever they approve candidate Y, they must approve candidate X.
3. Voters have common knowledge of the perceived front-runners. That is, every voter knows who the leader and challenger are perceived to be.
4. Every voter applies the leader rule simultaneously.
5. No two pairwise match-ups have the same margin. That is, for any two pairs of candidates, $$(X_1, Y_1) \neq (X_2, Y_2)$$, then $$P(X_1>Y_1)\neq P(X_2>Y_2)$$.

We identify the set of possible leader challenger pairs $$(X,Y)$$, where $$X\neq Y$$, as state nodes. We can imagine them as what the polls say prior to an election. We investigate the nature of how one node moves to another.

**Theorem 1:** Suppose the leader, challenger pair is (X,Y). After every voter applies the leader rule, the candidates will have the following percent approvals:

1. X: $$P(X>Y)$$
2. Z: $$P(Z>X)$$ for all $$Z\neq X$$

Note that for any candidate X, after every voter applies the leader rule, the percent of the vote that X gets is $$P(X>Z)$$ for some candidate Z.

**Proof**: Based on the leader rule,

1. A voter only approves of a non-leader Z if they prefer Z > X. Therefore, Z gets $$P(Z>X)$$ approvals.
2. A voter only approves of X if they prefer X > Y. So X gets $$P(X>Y)$$ approvals. QED

**Definition:** a unique Condorcet winner is a candidate who strictly defeats every other candidate in pairwise comparisons. That is, if X is a unique Condorcet winner, then for every other candidate Z, $$P(X>Z) > 0.5$$. Thus, $$P(Z>X) < 0.5$$ for all $$Z \neq X$$. A Condorcet loser is a candidate who is strictly defeated by every other candidate in pairwise comparisons.

**Lemma 1:** If X is a unique Condorcet winner, then after every voter applies the leader rule, X will always have over 50% of the vote. Further, if the X is the leader, then X will still be the leader after every voter applies the leader rule.

**Proof:** As the unique Condorcet winner, $$P(X>Z) > 0.5$$ for all $$Z \neq X$$. Since the percent of votes X gets must be some $$P(X>Z)$$ for some candidate Z, then X must receive over 50% of the vote.

Suppose that X is the leader and Y is the challenger. Since $$P(Z>X)<0.5$$ for all $$Z \neq X$$, we must have that $$P(X>Y) > P(Z>X)$$ for all $$Z \neq X$$, meaning X has strictly more votes than any other candidate. QED

**Theorem 2:** (X,Y) is an equilibrium if and only if X is a unique Condorcet winner and Y is the candidate with the best pairwise matchup against X.

**Proof:** By the lemma, if X is a unique Condorcet winner, then X will remain the leader after every voter applies the leader rule. Therefore, we know that (X,Y) has an edge to (X,Y') for some Y' such that the votes $$P(Y'>X) > P(Z>X)$$ for all $$Z \notin\{X,Y'\}$$. That is, Y' must have the best pairwise matchup against X. Therefore, if Y is the candidate with the best pairwise matchup against X, then (X,Y) is an equilibrium. For uniqueness, we use our assumption that no two pairwise match-ups have the same margin, so there must be one unique Y' with the best pairwise matchup. For any other $$Y\neq Y'$$, we must have that $$P(Y>X) < P(Y'>X)$$, meaning (X,Y) must have an edge to (X,Y'). Therefore, it is the only equilibrium. QED

**Definition:** We define the set of "Leader Rule Outcome Nodes" to be the nodes with at least one edge to them. We call the candidates who are the leader in at least one Leader Rule Outcome Node to be a "Leader Rule Outcome".

**Lemma 2:** If every voter applies the leader rule, then at least one candidate will have more than 50% of the vote.

**Proof:** If there exists a unique Condorcet winner, then by the previous lemma, that candidate will have over 50% of the vote after every voter applies the leader rule. If there is no unique Condorcet winner, then there must exist some candidate Z who defeats the leader X in a pairwise match-up: $$P(Z>X)>0.5>P(X>Z)$$. Therefore, Z will have more than 50% of the vote. QED

**Lemma 3:** If X is a Condorcet loser, then X will never be the leader after all voters apply the leader rule. Further, X will always have less than 50% of the vote.

**Proof:** If X is a Condorcet loser, then $$P(X>Z) < 0.5$$ for all $$Z \neq X$$, and thus X will always have less than 50% of the votes. By the previous lemma, some candidate must have over 50% of the vote, and will thus have more votes than X. Therefore, X will not be the leader.

**Corollary 1:** If X is a unique Condorcet winner, then X is a Leader Rule Outcome. If X is a Condorcet loser, then X is not a Leader Rule Outcome.

**Proof:** By the previous theorem, we know that (X,Y) is an equilibrium if and only if X is a unique Condorcet winner and Y is the candidate with the best pairwise matchup against X. Therefore, if X is a unique Condorcet winner, there exists at least one equilibrium node, which has an edge to itself, where X is the leader, making X a Leader Rule Outcome. Conversely, if X is a Condorcet loser, by Lemma 3, X will never be the leader after all voters apply the leader rule, so X is not a Leader Rule Outcome. QED

## Pairwise Rankings

**Definition:** A "Pairwise Ranked Ordering" is an ordered list: 1. $$X_1 > Y_1$$. 2. $$X_2>Y_2$$. etc. A "Coherent Pairwise Ranked Ordering" (CPRO) is one that does not contain contradictions. For example, if A>B is the strongest pairwise margin at the top of the list, then B>A must be the weakest, at the bottom of the list. More generally, if we have m total candidates, and a list of the $$\ell=m(m-1)$$ pairwise match-ups, then if item $$i$$ is $$X>Y$$, then $$Y>X$$ must be item $$\ell-i$$. Since a CPRO is uniquely determined by the first half of the list, we sometimes omit the second half for brevity.

**Theorem 3:** The graph of state nodes is determined uniquely by the ranked ordering of pairwise match-up strengths (the CPRO).

**Proof:** The determination of the new leader and challenger depend entirely on the relative strengths of the pairwise match-ups. That is, by sorting $$P(X>Y),P(Z_1>X),\ldots$$, we can uniquely determine the transitions between state nodes. QED

This gives us an algorithm to determine where the node (X,Y) will transition based on the CPRO.

**Algorithm 1:** Identifying the CPRO entry $$X_i>Y_i$$ as $$(X_i,Y_i)$$,

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

**Theorem 4:** Any CPRO of pairwise match-ups can be realized.

We give a proof by construction, using [McGarvey's theorem](https://www.jstor.org/stable/1907926){:target="_blank"}. Let $$m$$ be the total number of candidates, $$\ell=m(m-1)$$ the total number of pairwise match-ups, and list the first half of the match-ups $$i=0,1,\ldots,\ell/2-1$$ match-up as $$X_i > Y_i$$.

To ensure that $$X_i > Y_i$$ is the $$i+1$$th strongest match-up, we add $$\frac{\ell}2-i$$ voters of the following two types:

1. $$X_iY_iZ_1\ldots Z_{m-2}$$, for $$Z_1\ldots Z_{m-2}$$ being any arbitrary ordering of the remaining candidates.
2. $$Z_{m-2}\ldots Z_1X_i_Y_i$$

By reversing the other candidates, these two voters types cancel out all pairwise match-ups except it gives +2 to $$X_i>Y_i$$ for each pair of voters of these types.

As an example, take the following CPRO on three candidates.

1. A>B
2. C>A
3. B>C

To ensure A>B is the strongest matchup, we add the following voters:

- ABC: 3 voters
- CAB: 3 voters

With only three candidates, there is only one trivial way to order the remaining candidates, making this construction unique. The remaining two match-ups induce the following voters:

- CAB: 2 voters (for the C>A match-up)
- BCA: 2 voters (for the C>A match-up)
- BCA: 1 voter (for the B>C match-up)
- ABC: 1 voter (for the B>C match-up)

In total, this gives

- ABC: 4 voters
- BCA: 3 voters
- CAB: 5 voters

**Definition:** We define the pairwise matrix such that entry (i,j) represents the number of voters who prefer candidate i over candidate j. We define the diagonal entries to be zero.

The pair-wise matrix for the above profile is as follows: Entry the row candidate is the one preferred over the column candidate.

|   | A | B | C |
|---|---|---|---|
| A | - | 9 | 4 |
| B | 3 | - | 7 |
| C | 8 | 5 | - |

We can confirm that the match-up strengths match the precise list we defined.

Let us apply the algorithm on the CPRO to determine the edges of the graph, for at least one edge. For convenience, let us list the full list:

1. A>B
2. C>A
3. B>C
4. C>B
5. A>C
6. B>A

Let us consider the (A,B) node. We look for A>B or X>A, since A is the leader. We see that the first entry is A>B, so A will be the leader. The second entry is C>A, so C will be the challenger.

**Theorem 5:** The pairwise matrix can be used to determine the precise votes or percents that each candidate will get after voters apply the leader rule at a particular node.

1. Take the column corresponding to the leader X. The non-diagonal entries will be the precise share that each non-leader candidate Z receives. That is because the entry (Z,X) in the pairwise matrix represents the probability that Z is preferred over X.
2. Replace the diagonal entry (which is zero) with the entry in the same row corresponding to the challenger. That is because the entry (Y,X) in the pairwise matrix represents the probability that X is preferred over Y.

## Equilibrium Paths

**Theorem 6:** With three candidates, if a Condorcet winner and equilibrium exists, the leader rule always converges to that equilibrium, from any starting node, in a maximum of three steps. However, the Condorcet winner will win after at most two steps.

**Proof:** Note that the CPRO is uniquely determined by three pairwise match-ups. Suppose that candidate A is a Condorcet winner. That is, we have A>B and A>C in the first half of the CPRO. By previous lemmas, we know that any node where A is the leader has an edge to the equilibrium. Therefore, we prove the theorem by 

We have two cases:

Case 1: If the top two match-ups involve A, then without loss of generality suppose that it is A>B and then A>C. This means C has the best pairwise match-up against A, so (A,C) is the unique equilibrium. If A is the leader, and B is the challenger, then the node must have an edge to (A,C), since B>A is the weakest pairwise match-up, B must have the fewest approvals.

Case 2: If there exists any match-up not involving A that is stronger than one of A's match-ups against another candidate, then that induces a possible non Condorcet Leader Rule Outcome. Without loss of generality, suppose that B>C is one of the top two strongest match-ups, making C a Condorcet loser. If the B>C match-up is stronger than A>C, then (C,B) will have an edge to (B,A). If B>C is not stronger than A>C (meaning A>C is the strongest pairwise match-up), then (B,C) will have an edge to (B,A). In either case, B must have fewer than 50% approvals in the outcome after (B,A), while A must have more than 50% approvals. Since C is a Condorcet loser, they must also have less than 50% approvals, so A will be the leader in at most two steps. This node may not be the equilibrium, but must have an edge to the equilibrium, giving it at most three steps.

**Theorem 7:** With four or more candidates, even if a unique Condorcet winner and equilibrium exist, it may not be reachable by every starting node.

**Proof:** We present a counterexample based on a profile created by Rob LeGrand. Suppose we have the CPRO:

1. A>B
2. B>C
3. C>A
4. D>B
5. D>C
6. D>A

Here, we clearly have a Condorcet winner, D. However, they have the weakest pairwise wins, and thus we can show that D will never be the leader unless D starts as the leader. All nodes where D is the leader will have an edge to (D,A), since A is the candidate with the best pairwise match-up against B.

If we have a leader who is not D, then at least one candidate will have a stronger margin against that leader than D. Therefore, D cannot become the leader unless D starts as the leader.

In particular, we can see that there will be a cycle (A,D) to (C,D) to (B,D) and back to (A,D). QED

## Conclusion

What we can see from these theorems and results is that the leader rule leads to strongly majoritarian outcomes. At least one candidate will have over 50%, including the Condorcet winner if they exist. While the Condorcet winner may not be the final winner, the winner is always the candidate whom the voters most strongly prefer over the expected outcome. That is, the outcome is always either the same or strictly better, to the collective voters, than the expectation of voters going into the voting booth.

Some considerations must be made to the plausibility or realism of the axioms. For one, this analysis does not take into account sincere voters who do not adjust their acceptability line strategically. It also does allow for the possibility that some voters may not agree on the perceived leader and challenger. In our increasingly divisive media bubbles, the perception of a race to one bloc of voters could be significantly different from another.

## References

A very big thank you to Rob LeGrand for his contributions, the counterexample that inspired Theorem 7, and for telling me about this strategy.

Laslier, J. F. (2009). The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate. *Journal of Theoretical Politics*, 21(1), 113-136. [https://journals.sagepub.com/doi/10.1177/0951629808097286](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}

McGarvey, D. C. (1953). A Theorem on the Construction of Voting Paradoxes. Econometrica, 21(4), 608–610. [https://doi.org/10.2307/1907926](https://doi.org/10.2307/1907926){:target="_blank"}

[ranked.vote](https://ranked.vote){:target="_blank"} Election Reports:

- Alaska House Special Election 2022: [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}
- NYC Democratic Mayoral Primary 2025: [https://ranked.vote/report/us/ny/nyc/2025/07/mayor](https://ranked.vote/report/us/ny/nyc/2025/07/mayor){:target="_blank"}
- Minneapolis City Council Ward 2 2021: [https://ranked.vote/report/us/mn/2021/11/ward-2](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}
