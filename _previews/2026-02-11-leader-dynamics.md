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
  - name: Case Studies
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

WIP DRAFT (not finished)

## Introduction

The Leader Rule is a strategy under approval voting by Jean-François Laslier where voters choose their sincere strategy based on who the perceived frontrunners are:

> **The Leader Rule**: Call the candidate perceived most likely to win the "leader", and the second most likely candidate to win the "challenger". The leader rule strategy is as follows:
>
> 1. Approve all candidates strictly preferred to the leader
> 2. Approve the leader if and only if you prefer them to the challenger
> 3. Approve no other candidates

We will not delve into the weeds of why this is an optimal strategy, but our analysis focuses on what happens when every voter applies the leader rule simultaneously.

**Definition**: We denote the proportion of voters who prefer X>Y as $$P(X>Y)$$, as a shorthand for the probability that a randomly selected voter prefers X over Y given the complete profile of voter preferences. Note that $$P(Y>X)=1-P(X>Y)$$.

For our axioms of this analysis, we assume

1. Voters have complete and transitive preferences over candidates. Given any pair of candidates, a voter strictly prefers one over the other, and is not indifferent between them.
2. Voters always use sincere strategies. That is, if they prefer candidate X over Y, then whenever they approve candidate Y, they must approve candidate X.
3. Voters have common knowledge of the perceived front-runners. That is, every voter knows who the leader and challenger are perceived to be.
4. Every voter applies the leader rule simultaneously.
5. No two pairwise match-ups have the same margin, and no two candidates tie. That is, for any two pairs of candidates, $$(X_1, Y_1) \neq (X_2, Y_2)$$, then $$P(X_1>Y_1)\neq P(X_2>Y_2)$$, and $$P(X_1>Y_1)\neq 0.5$$. In a "large electorate",  which is the setting Laslier focuses on in his paper, this is a reasonable assumption, since the probability of ties goes to zero as the number of voters increases.

We identify the set of possible leader challenger pairs $$(X,Y)$$, where $$X\neq Y$$, as state nodes. We can imagine them as what the polls say prior to an election. We investigate the nature of how one node moves to another.

Note that Theorems 1 and 2 are adapted from Laslier's original paper. The rest of the theorems and lemmas are new so far as I know.

**Theorem 1:** Suppose the leader, challenger pair is (X,Y). After every voter applies the leader rule, the candidates will have the following percent approvals:

1. X: $$P(X>Y)$$
2. Z: $$P(Z>X)$$ for all $$Z\neq X$$

Note that for any candidate X, after every voter applies the leader rule, the percent of the vote that X gets is $$P(X>Z)$$ for some candidate Z.

**Proof**: Based on the leader rule,

1. A voter only approves of a non-leader Z if they prefer Z > X. Therefore, Z gets $$P(Z>X)$$ approvals.
2. A voter only approves of X if they prefer X > Y. So X gets $$P(X>Y)$$ approvals. QED

**Definition:** a unique Condorcet winner is a candidate who strictly defeats every other candidate in pairwise comparisons. That is, if X is a unique Condorcet winner, then for every other candidate Z, $$P(X>Z) > 0.5$$. Thus, $$P(Z>X) < 0.5$$ for all $$Z \neq X$$. A Condorcet loser is a candidate who is strictly defeated by every other candidate in pairwise comparisons.

**Lemma 1:** If X is a unique Condorcet winner, then after every voter applies the leader rule, X will always have over 50% of the vote. Further, if the X is the leader and a unique Condorcet winner, then X will still be the leader after every voter applies the leader rule.

**Proof:** As the unique Condorcet winner, $$P(X>Z) > 0.5$$ for all $$Z \neq X$$. Since the percent of votes X gets must be some $$P(X>Z)$$ for some candidate Z, then X must receive over 50% of the vote.

Suppose that X is the leader and Y is the challenger. Since $$P(Z>X)<0.5$$ for all $$Z \neq X$$, we must have that $$P(X>Y) > P(Z>X)$$ for all $$Z \neq X$$, meaning X has strictly more votes than any other candidate. QED

**Theorem 2:** (X,Y) is an equilibrium if and only if X is a unique Condorcet winner and Y is the candidate with the best pairwise matchup against X.

**Proof:** By the lemma, if X is a unique Condorcet winner, then X will remain the leader after every voter applies the leader rule. Therefore, we know that (X,Y) has an edge to (X,Y') for some Y' such that the votes $$P(Y'>X) > P(Z>X)$$ for all $$Z \notin\{X,Y'\}$$. That is, Y' must have the best pairwise matchup against X. Therefore, if Y is the candidate with the best pairwise matchup against X, then (X,Y) is an equilibrium.

Suppose now that (X,Y) is an equilibrium. Then we must have that $$P(X>Y) > P(Y>X) > P(Z>X)$$ for all $$Z \neq X$$. Since $$P(X>Y) > 0.5 > P(Y>X)$$, we must have that $$P(Z>X) < 0.5$$ for all $$Z \neq X$$, meaning X is a unique Condorcet winner. Since $$P(Y>X) > P(Z>X)$$ for all $$Z \notin\{X,Y\}$$, we must have that Y is the candidate with the best pairwise matchup against X. QED

**Corollary 1:** If there is no unique Condorcet winner, then there is no equilibrium.

In this case, there must instead be a cycle of nodes, where each node has an edge to another node, and the last node has an edge back to the first node. There is no stable leader-challenger pair in this case, however, the election must still occur eventually. We focus on the general dynamics of the leader rule to make conclusions about the possible outcomes in this case.

**Lemma 2:** If every voter applies the leader rule, then at least one candidate will have more than 50% of the vote.

**Proof:** If there exists a unique Condorcet winner, then by the previous lemma, that candidate will have over 50% of the vote after every voter applies the leader rule. If there is no unique Condorcet winner, then there must exist some candidate Z who defeats the leader X in a pairwise match-up: $$P(Z>X)>0.5>P(X>Z)$$. Therefore, Z will have more than 50% of the vote after every voter applies the leader rule. QED

**Lemma 3:** If X is a Condorcet loser, then X will never be the leader after all voters apply the leader rule. Further, X will always have less than 50% of the vote.

**Proof:** If X is a Condorcet loser, then $$P(X>Z) < 0.5$$ for all $$Z \neq X$$, and thus X will always have less than 50% of the votes by Theorem 1. By the previous lemma, some candidate must have over 50% of the vote, and will thus have more votes than X. Therefore, X will not be the leader.

These two lemmas do tell us something important: even if there is a cycle of preferences, when the elections finally comes around and voters apply the leader rule, we can guarantee that

1. The winner will win with over 50% of the vote
2. The winner won't be a Condorcet loser

Further, due to the nature of the Approval ballot data, the winner is always the Condorcet winner  induced by the literal dichotomous preferences expressed by the voters. That is, since the difference in total approvals is the difference in "strict approvals", the winner must defeat all other candidates in strict approvals. Any Condorcet cycle will be invisible in the ballot data, and instead voters will only see a single candidate with the most approvals (over 50%), who is the Condorcet winner of the strict approvals.

**Definition:** We define the set of "Leader Rule Outcome Nodes" to be the nodes with at least one edge to them. We call the candidates who are the leader in at least one Leader Rule Outcome Node to be a "Leader Rule Outcome".

**Corollary 2:** If X is a unique Condorcet winner, then X is a Leader Rule Outcome. If X is a Condorcet loser, then X is not a Leader Rule Outcome.

**Proof:** By theorem 2, we know that (X,Y) is an equilibrium if and only if X is a unique Condorcet winner and Y is the candidate with the best pairwise matchup against X. Therefore, if X is a unique Condorcet winner, there exists at least one equilibrium node, which has an edge to itself, where X is the leader, making X a Leader Rule Outcome. Conversely, if X is a Condorcet loser, by Lemma 3, X will never be the leader after all voters apply the leader rule, so X is not a Leader Rule Outcome. QED

**Lemma 4:** Candidate X is a Leader Rule Outcome if and only if one of the following holds:

1. X has a pairwise match-up against some candidate Y that is stronger than any pairwise match-up against X. That is, there exists some Y such that $$P(X>Y) > P(Z>X)$$ for all $$Z \neq X$$.
2. X has the strongest pairwise match-up against some candidate $$Y \neq X$$, and that match-up is stronger than Y's match-up against some candidate $$Y'\neq Y$$. That is, there exists some Y such that $$P(X>Y) > P(Z>Y)$$ for all $$Z \neq X$$ and there exists some Y' such that $$P(X>Y) > P(Y>Y')$$ for some Y'.

**Proof:** If condition 1 holds, then consider the node (X,Y). We have that $$P(X>Y) > P(Z>X)$$ for all $$Z \neq X$$, so X will have the most votes after every voter applies the leader rule, making X the leader. Note that condition 1 holds when X is a unique Condorcet winner, since $$P(X>Z) > 0.5 > P(Z>X)$$ for all $$Z \neq X$$. If condition 1 does not hold, then for all Y, there exists some Z such that $$P(Z>X) > P(X>Y)$$, meaning that (X,Y) cannot have an edge to any node where X is the leader. That is, no node where X is the leader can have an edge to a node where X is the leader.

If condition 2 holds, then consider the node (Y,Y'). We have that $$P(X>Y) > P(Z>Y)$$ for all $$Z\notin\{X,Y\}$$, so X will have more votes than all candidates other than Y after every voter applies the leader rule. However, since $$P(X>Y) > P(Y>Y')$$, X will have more votes than Y as well, making X the leader. If condition 2 does not hold, then for all nodes where X is not the leader, (Y,Y') where $$Y \neq X$$, there exists some Z such that $$P(Z>Y) > P(X>Y)$$, meaning that (Y,Y') cannot have an edge to any node where X is the leader. That is, no node where X is not the leader can have an edge to a node where X is the leader. QED

In short, we have essentially two archetypes for a candidate to be a Leader Rule Outcome:

1. A candidate on the offense (TODO: is this the best intuitive phrasing?): they beat some candidate by a stronger margin than any candidate beats them. This is the case of a unique Condorcet winner, but it can also be the case for a non-Condorcet winner if they have a sufficiently strong match-up against some candidate.
2. A candidate who strongly counters another candidate: they have the strongest match-up against some candidate, and that match-up is stronger than that candidate's match-up against some other candidate. Intuitively, this means that the electorate may have a strong "reaction" against some leader Y, and X is more strongly preferred to Y than Y is to whoever the challenger is.

## Pairwise Rankings

**Definition:** A "Pairwise Ranked Ordering" is an ordered list: 1. $$X_1 > Y_1$$. 2. $$X_2>Y_2$$. etc. A "Coherent Pairwise Ranked Ordering" (CPRO) is one that does not contain contradictions. For example, if A>B is the strongest pairwise margin at the top of the list, then B>A must be the weakest, at the bottom of the list. More generally, if we have m total candidates, and a list of the $$\ell=m(m-1)$$ pairwise match-ups, then if item $$i$$ is $$X>Y$$, then $$Y>X$$ must be item $$\ell-i+1$$. Since a CPRO is uniquely determined by the first half of the list, we sometimes omit the second half for brevity.

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
2. $$Z_{m-2}\ldots Z_1X_iY_i$$

By reversing the other candidates, these two voters types cancel out all pairwise match-ups except it gives +2 to $$X_i>Y_i$$ for each pair of voters of these types:

1. For $$X_i$$ versus $$Z_j$$, the first type of voter gives +1 to $$X_i>Z_j$$, while the second type of voter gives -1 to $$X_i>Z_j$$, so they cancel out.
2. For $$Y_i$$ versus $$Z_j$$, the first type of voter gives -1 to $$Y_i>Z_j$$, while the second type of voter gives +1 to $$Y_i>Z_j$$, so they cancel out.
3. For $$Z_j$$ versus $$Z_k$$, the first type of voter gives +1 to $$Z_j>Z_k$$, while the second type of voter gives -1 to $$Z_j>Z_k$$, so they cancel out.
4. For $$X_i$$ versus $$Y_i$$, both types of voters give +1 to $$X_i>Y_i$$, so they add up to +2.

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

In summary, this tells us that we can analyze the possible graphs by instead considering the possible CPROs.

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

Let us consider the (A,B) node. We look for A>B or X>A, since A is the leader. We see that the first entry is A>B, so A will be the leader. The second entry is C>A, so C will be the challenger. Thus, (A,B) has an edge to (A,C).

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

<img src="/assets/img/leader_rule/alt_profile.png" alt="Leader Rule Non-Convergence Example" style="max-width: 600px;">

## Case Studies

We shall analyze three elections using ranked.vote pairwise data, to see what the leader rule dynamics would have looked like in those elections. The percentages are based on the head-to-head matchups of voters who expressed a preferences, which may not extend to the entire electorate. For example, in the 2025 NYC election, a large proportion of voters who voted for Cuomo bullet voted for him, and thus did not express a preference between Zohran Mamdani and Brad Lander. Therefore, the nearly 70% head-to-head result for Mamdani vs. Lander may not be representative of the entire electorate, but rather only of the subset of voters who expressed a preference between those two candidates. However, we use a simplifying assumption that the head-to-head results are representative of the entire electorate, to get a rough picture of the leader rule dynamics in these elections, along with the other axioms we have laid out in the introduction.

### Alaska House Special Election 2022

[ranked.vote page for this election](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}.

Alaska's 2022 House Special Election was a controversial election where the IRV winner, Mary Peltola, was not the Condorcet winner, and lost to the Condorcet winner, Nick Begich III, in a head-to-head match-up. The third candidate, Sarah Palin, was the Condorcet loser. The election was widely seen as a failure of IRV, and led to a backlash against IRV in Alaska, with the state failing to repeal it by only about 700 voters out of over 320,000 votes cast in the 2024 ballot measure. Another repeal effort is currently underway in 2026.

An aspect of the pathology was the uninutive vote splitting and spoiler effect that occured between the Republican candidates. The voters who sincerely voted for Palin first and Begich second managed to get themselves their least preferred candidate, Peltola, elected. By voting first for Palin, the Condorcet loser, they kept her in the race long enough to eliminate the only viable Republican candidate, Begich.

Using the head-to-head results from Alaska 2022, we can simulate the leader rule. The head-to-head results were:

| Head-to-Head       | Winner      | Percentage    |
|--------------------|-------------|---------------|
| Begich vs. Palin   | Begich      | 61.4% : 38.6% |
| Begich vs. Peltola | Begich      | 52.5% : 47.5% |
| Peltola vs. Palin  | Peltola     | 51.4% : 48.6% |

Based on the results above, Palin's Condorcet loser status would have made it impossible for her to win under the leader rule, even if she had been the perceived leader. Further, Begich's strong head-to-heads against both Palin and Peltola would have given him an extremely strong pull. In fact, he is the only Leader Rule Outcome. If every voter applied the leader rule, and these head to heads extend to the entire electorate, Begich would be the only candidate who could have won.

The directed graph of leader-challenger pairs is as follows:

<img src="/assets/img/leader_rule/alaska.png" alt="Leader Rule Alaska 2022" style="max-width: 600px;">

Here is how to read this graph:

- A node like "Peltola, Palin" represents the scenario where Peltola is the leader and Palin is the challenger. This node points to the red node "Begich, Peltola", which means that if all voters enter the voting booth expecting Peltola to be the leader, and see Palin as the challenger, then after everyone applies the leader rule, the final result will have Begich in first place and Peltola in second place.
- Similarly, the node "Peltola, Begich" actually points to the "Begich, Palin" node, meaning that if everyone expects Peltola to be the leader and Begich to be the challenger, then after everyone applies the leader rule in the voting booth, the final result will have Begich in first place and Palin in second place. Peltola actually falls to third place in this scenario, because Begich's head-to-head against Peltola was stronger than Palin's head-to-head against Peltola, which was stronger than Peltola's head-to-head against Begich.
- A node is colored red if it is an equilibrium (it points to itself), and blue if any nodes have an edge to it (it is a Leader Rule Outcome Node), but is not an equilibrium.

The equilibrium has Begich as the leader and Peltola as the challenger. This is consistent with Begich being the Condorcet winner, and Peltola having the best head-to-head result against Begich.

Notice that after any starting point, Begich becomes the leader. However, interestingly, in the case where Peltola is the leader and Begich is the challenger, the next iteration has Begich as the leader and Palin as the challenger. This is because Palin's head-to-head against Peltola was stronger than Peltola's head-to-head against Begich. Therefore, if Peltola was the leader, and Begich the challenger, and every voter voted using the leader rule, the result would actually have the leader come in last place in approval percentage.

However, this does mean that, potentially, in the case where Palin is the leader, a Democratic voter who prefers Peltola and Begich to Palin should approve of both Peltola and Begich, to help push Palin down (even if Peltola is the challenger). But the result *would*, under this analysis, be a Begich victory. Would this cause "regret" among Democratic voters? It is hard to say for sure, especially because the ballot data we have seems to indicate that Palin would have done quite poorly in an Approval election.

But suppose we assume poor quality polls, that had the Condorcet loser Palin as the leader, and then suppose that Begich won (as his Condorcet winner status would make very likely to have done by over 60%), then from their perspective, they would have successfully prevented Palin from winning. This was their primary goal, and a Palin victory appeared to be the most likely outcome.

If the voter went into the voting booth expecting Palin to win, voted for both Peltola and Begich, and then Begich won with over 60% and Peltola in second place with 51%, they might feel satisfied that they prevented Palin from winning. And such a strong victory for Begich would make it difficult to second guess their strategy. It would simply look like *both* Peltola and Begich were broadly acceptable to the electorate, that Palin was not, but that Begich was the most preferred candidate overall. This would be a strong majoritarian outcome, unlikely to fuel the massive repeal efforts that have plagued Alaska in the years since the 2022 Condorcet failure of IRV there in 2024 and now again in 2026.

### NYC Democratic Mayoral Primary 2025

[ranked.vote page for this election](https://ranked.vote/report/us/ny/nyc/2025/07/mayor){:target="_blank"}.

Here we reduce the field to the top four candidates: Zohran Mamdani, Brad Lander, Andrew Cuomo, and Adrienne Adams. In the actual election, Cuomo was seen as the leader, with Mamdani as the main challenger. Lander and Adams were seen as long-shot candidates.

The head-to-head results were:

| Head-to-Head        | Winner      | Percentage    |
|---------------------|-------------|---------------|
| Mamdani vs. Adams   | Mamdani     | 74.8% : 25.2% |
| Lander vs. Adams    | Lander      | 72.7% : 27.3% |
| Mamdani vs. Lander  | Mamdani     | 69.6% : 30.4% |
| Mamdani vs. Cuomo   | Mamdani     | 56.4% : 43.6% |
| Lander vs. Cuomo    | Lander      | 54.4% : 45.6% |
| Adams vs. Cuomo     | Adams       | 50.3% : 49.7% |

We can see that, in fact, the perceived leader Cuomo was actually a Condorcet loser, while the perceived challenger Mamdani was the Condorcet winner. Lander was a strong contender, with strong head-to-head results against both Cuomo and Adams, but was not the Condorcet winner due to his weaker head-to-head against Mamdani. Adams, while narrowly beating Cuomo head-to-head, was not perceived as a particularly strong candidate, and had very weak head-to-head results against both Mamdani and Lander.

The two leader rule outcomes are Mamdani and Lander, with Mamdani being the equilibrium, as the Condorcet winner. Lander is a Leader Rule Outcome because of his strong head-to-head against Adams. The node with Lander as the leader and Adams as the challenger has an edge to the node with Lander as the leader and Mamdani as the challenger, since Lander's head-to-head against Adams is stronger than Mamdani's head-to-head against Lander. However, the plausibility of this node being the perception of voters is extremely low, since Adams was perceived as a very weak candidate. Therefore, it's extremely likely that Mamdani would win in any reasonable perception of the race, assuming voters vote strategically using the leader rule and the head-to-head results extend to the entire electorate.

The directed graph of leader-challenger pairs is as follows:

<img src="/assets/img/leader_rule/nyc.png" alt="Leader Rule NYC 2025" style="max-width: 600px;">

We see the red equilibrium node with Mamdani as the leader and Cuomo as the challenger, and two other blue Leader Rule Outcome Nodes: (Lander, Mamdani) and (Mamdani, Lander).

### Minneapolis City Council Ward 2 2021

[ranked.vote page for this election](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}.

This was a very notable election because it actually had a Condorcet cycle. The cycle was between Cam Gordon, Robin Wonsley, and Yusra Arab. The actual winner was Robin Wonsley, who defeated Yusra Arab in the final round of IRV. However, Cam Gordon beat Robin Wonsley head-to-head, and Yusra Arab beat Cam Gordon head-to-head, creating a Condorcet cycle.

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
| Arab | Wonsley | Wonsley: 50.1%, Arab: 49.9%, Gordon: 48.7% | (Wonsley, Arab) |
| Wonsley | Arab | Gordon: 50.5%, Wonsley: 50.1%, Arab: 49.9% | (Gordon, Wonsley) |
| Gordon | Wonsley | Arab: 51.3%, Gordon: 50.5%, Wonsley: 49.5% | (Arab, Gordon) |
| Arab | Gordon | Arab: 51.3%, Wonsley: 50.1%, Gordon: 48.7% | (Arab, Wonsley) |

If we interpret nodes as possible perceptions of the race, and suppose voters update their strategy based on the leader rule when they answer a poll, then we would basically see a cycle like this:

- Week 1: Voters think Wonsley is the leader, Arab is the challenger. They update their strategies and answer the next poll.
- Week 2: Gordon shoots up to be the leader, since he has the strongest head-to-head against Wonsley. Wonsley falls to challenger, and Arab falls out of the top two (and under 50%), since Wonsley beats Arab and that match-up decides the next approval percentages.
- Week 3: Arab shoots up to be the leader, since she has the strongest head-to-head against Gordon. Gordon falls to challenger, and Wonsley falls out of the top two like Arab did last week.
- Week 4: Arab remains the leader, but Wonsley shoots up to be the challenger, since she has the strongest head-to-head against Arab. Arab's strong head-to-head against Gordon keeps Arab in first place.
- Week 5: Wonsley becomes the leader again, since she has the strongest head-to-head against Arab. Arab falls to challenger, and Gordon falls out of the top two again. And now we're back to week 1.

If we were to imagine this happening in a campaign cycle, we would still eventually have to run the election at some point. And depending on who the perceived leader and challenger are at that moment, we would end up with one of the three candidates winning. Since Approval voting is consistent with its ballot data, the actual winner would be the Condorcet winner of the implied preferences expressed by the ballots, flattening out the cycle. The ballots won't catch fire, the machines won't explode, and no loser will be able to credibly claim they would have beaten the actual winner in a head-to-head match-up, because the ballots won't show that. The result will be legitimate, but close. Someone will get over 50% approvals, and

## Discussion

What we can see from these theorems and results is that the leader rule leads to strongly majoritarian outcomes. At least one candidate will have over 50%, including the Condorcet winner if they exist. While the Condorcet winner may not be the final winner, the winner is always the candidate whom the voters most strongly prefer over the expected outcome. That is, the outcome is always either the same or strictly better, to the collective voters, than the expectation of voters going into the voting booth. Further, the actual winner will have a mandate of over 50% approvals.

### The Chicken Dilemma Explored

Many criticize Approval voting for being susceptible to strategic voting, and a chicken dilemma between supporters of two similar candidates. The leader rule actually provides a direct answer to this.

The claim is that if we have two candidates, L and C, who perhaps are leftists running in a generally left-leaning electorate, then their supporters might bullet vote sufficiently such that a right leaning candidate R might snake in and win. However, the leader rule reframes this scenario.

Let us suppose that one of L, a more extremist left candidate, and C, a center left candidate, are is the leader. And let R be a right-leaning candidate who is neither the leader or challenger. We will analyze the case in which one of the two left candidates is the leader and the other is the challenger. Let us assume a generally 1-dimensional spatial model where L voters prefer L>C>R, R voters prefer R>C>L, and C voters split with some preferring C>L>R and others preferring C>R>L. Consider the cases:

| Leader | Challenger | LCR | CLR | CRL | RCL |
|--------|------------|-----|-----|-----|-----|
| L      | C          | L   | C   | C,R | R,C |
| C      | L          | L   | C   | C   | R,C |

We notice something very interesting. The criticism of the chicken dilemma is that L and C voters *might* bullet vote and cause R to win. The claim is that sufficient bullet voting might end up breaking up the coalition and resulting in plurality-style vote splitting. However, the leader rule actually says that L and C voters (who rank R last) *should* bullet vote, and that this is the optimal strategy. The missing consideration of the criticism is what R voters would do: if they know their candidate is nonviable or unlikely to win, it is optimal to also give an approval to the more agreeable viable candidate, C. Thus, C, in all cases, gets approvals from the moderate C supporters *and* the conservative R supporters, while L only gets approvals from the more extreme L supporters. If C is the Condorcet winner, then the moderate and conservative blocs will coalesce around C, outnumbering the more extreme L, resulting in a C win.

However, against the other criticism that Approval elects only bland candidates, there is another consideration to make. If the median voter is more extreme, and closer to L, then the L supporting wing will be larger than the combined C and R supporting wings, and thus L will still win. The outcome from the Leader rule is not always on the *middle* candidate, but rather strongly favors the Condorcet winner. It is entirely possible for one of the "outside" candidates to be the Condorcet winner if the electorate leans sufficiently towards that candidate.

It should be acknowledged, however, that this is not any sort of guarantee that voters would or should bullet vote. While it may be optimal for L and C voters to bullet vote when both are ahead, we do see in real Approval elections in Fargo (TODO: include source) and St. Louis that voters are willing to approve multiple candidates, and support a coalition. Rather, this example should illustrate that Approval would not likely suddenly collapse when voters are strategic. Instead, it is actually robust to strategy when voters are prudent (ex. if their favorite candidate is trailing behind the top two). If a sufficient number of both L and CLR voters choose to approve L and C--say due to the candidates forming a coalition and encouraging their voters to do so--it's even more likely that either L or C will win, strengthening their lead over R. If the electorate is sufficiently left-leaning, then this is a highly representative outcome.

## Other Considerations and Further Research

Some considerations must be made to the plausibility or realism of the axioms. For one, this analysis does not take into account sincere voters who do not adjust their acceptability line strategically. It also does allow for the possibility that some voters may not agree on the perceived leader and challenger. In our increasingly divisive media bubbles, the perception of a race to one bloc of voters could be significantly different from another.

## Appendix

Here is an example where the Leader rule does not converge to the Condorcet winner: (Credit to Rob LeGrand)

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
| B vs. A     | B      | 52% : 48%  |
| B vs. C     | B      | 51% : 49%  |
| B vs. D     | B      | 56% : 44%  |
| A vs. D     | A      | 73% : 27%  |
| D vs. C     | D      | 61% : 39%  |
| C vs. A     | C      | 66% : 34%  |

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

We can see that if B is the initial leader, we converge to the equilibrium in one step (colored red). However, otherwise we get stuck in the cycle between A, C, and D (colored orange).

---

Here are the full tables for the three example elections analyzed above.

### Alaska House Special Election 2022 Table

| Leader | Challenger | Approvals | Target |
|--------|------------|-----------|--------|
| Peltola | Begich | Begich: 52.5%, Palin: 48.6%, Peltola: 47.5% | (Begich, Palin) |
| Peltola | Palin | Begich: 52.5%, Peltola: 51.4%, Palin: 48.6% | (Begich, Peltola) |
| Begich | Peltola | Begich: 52.5%, Peltola: 47.5%, Palin: 38.6% | (Begich, Peltola) |
| Begich | Palin | Begich: 61.4%, Peltola: 47.5%, Palin: 38.6% | (Begich, Peltola) |
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
| Wonsley | Arab | Gordon: 50.5%, Wonsley: 50.1%, Arab: 49.9%, Anderson: 36.2% | (Gordon, Wonsley) |
| Wonsley | Gordon | Gordon: 50.5%, Arab: 49.9%, Wonsley: 49.5%, Anderson: 36.2% | (Gordon, Arab) |
| Wonsley | Anderson | Wonsley: 63.8%, Gordon: 50.5%, Arab: 49.9%, Anderson: 36.2% | (Wonsley, Gordon) |
| Arab | Wonsley | Wonsley: 50.1%, Arab: 49.9%, Gordon: 48.7%, Anderson: 26.7% | (Wonsley, Arab) |
| Arab | Gordon | Arab: 51.3%, Wonsley: 50.1%, Gordon: 48.7%, Anderson: 26.7% | (Arab, Wonsley) |
| Arab | Anderson | Arab: 73.3%, Wonsley: 50.1%, Gordon: 48.7%, Anderson: 26.7% | (Arab, Wonsley) |
| Gordon | Wonsley | Arab: 51.3%, Gordon: 50.5%, Wonsley: 49.5%, Anderson: 35.5% | (Arab, Gordon) |
| Gordon | Arab | Arab: 51.3%, Wonsley: 49.5%, Gordon: 48.7%, Anderson: 35.5% | (Arab, Wonsley) |
| Gordon | Anderson | Gordon: 64.5%, Arab: 51.3%, Wonsley: 49.5%, Anderson: 35.5% | (Gordon, Arab) |
| Anderson | Wonsley | Arab: 73.3%, Gordon: 64.5%, Wonsley: 63.8%, Anderson: 36.2% | (Arab, Gordon) |
| Anderson | Arab | Arab: 73.3%, Gordon: 64.5%, Wonsley: 63.8%, Anderson: 26.7% | (Arab, Gordon) |
| Anderson | Gordon | Arab: 73.3%, Gordon: 64.5%, Wonsley: 63.8%, Anderson: 35.5% | (Arab, Gordon) |

The cycle, in particular, is between the nodes:

| Leader | Challenger | Approvals | Target |
|--------|------------|-----------|--------|
| Arab | Wonsley | Wonsley: 50.1%, Arab: 49.9%, Gordon: 48.7%, Anderson: 26.7% | (Wonsley, Arab) |
| Wonsley | Arab | Gordon: 50.5%, Wonsley: 50.1%, Arab: 49.9%, Anderson: 36.2% | (Gordon, Wonsley) |
| Gordon | Wonsley | Arab: 51.3%, Gordon: 50.5%, Wonsley: 49.5%, Anderson: 35.5% | (Arab, Gordon) |
| Arab | Gordon | Arab: 51.3%, Wonsley: 50.1%, Gordon: 48.7%, Anderson: 26.7% | (Arab, Wonsley) |

## References

A very big thank you to Rob LeGrand for his contributions, the counterexample that inspired Theorem 7, and for telling me about this strategy.

Laslier, J. F. (2009). The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate. *Journal of Theoretical Politics*, 21(1), 113-136. [https://journals.sagepub.com/doi/10.1177/0951629808097286](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}

McGarvey, D. C. (1953). A Theorem on the Construction of Voting Paradoxes. Econometrica, 21(4), 608–610. [https://doi.org/10.2307/1907926](https://doi.org/10.2307/1907926){:target="_blank"}

[ranked.vote](https://ranked.vote){:target="_blank"} Election Reports:

- Alaska House Special Election 2022: [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}
- NYC Democratic Mayoral Primary 2025: [https://ranked.vote/report/us/ny/nyc/2025/07/mayor](https://ranked.vote/report/us/ny/nyc/2025/07/mayor){:target="_blank"}
- Minneapolis City Council Ward 2 2021: [https://ranked.vote/report/us/mn/2021/11/ward-2](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}
