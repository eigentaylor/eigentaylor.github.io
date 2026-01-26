---
layout: distill
title: Approval Voting is the Only Internally Consistent Cardinal Method
date: 2026-01-25
description: A proof that Approval voting is the unique cardinal voting method that satisfies "Ballot-Condorcet-Consistency", a necessary property for a trustworthy voting system.
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
  - name: Internal Consistency
  - name: Ballot-Condorcet-Consistency
    subsections:
      - name: Approval is BCC
      - name: Uniqueness of Approval Voting
      - name: An Example
  - name: STAR is Not BCC
  - name: The Importance of Legitimacy
---

## Introduction

In my [last post](../practicalapproval/){:target="_blank"}, I focused a lot on the concept of internal consistency as a desirable property for voting methods. The primary purpose of a voting system is to aggregate potentially millions of complex individual preferences into a single name: the winner. This is done by collecting a simpler, easier to aggregate, set of inputs from each voter (ballots), which gives data about their preferences. I define the concept of internal consistency as using the data collected "properly", in a way that is consistent with the preferences expressed by the voters. That is, it does not produce a winner, where another candidate has a legitimate claim to victory based on the data collected.

For example, a ranked system collects ordinal preferences from each voter. If 51 voters rank candidate A over candidate B, while only 49 voters rank candidate B over candidate A, then it's clear that a majority of voters prefer A over B. If the system were to declare B the winner, then A would have a legitimate claim to victory, and the expressed will of the voters would have been ignored. If it can be further shown that A beats every other candidate, this would mean the system improperly used the data it collected, which destroys trust in the system. IRV, AKA "Ranked Choice Voting", is infamous for this exact failure (e.g. the 2022 Alaska special election). See my [previous post](../practicalapproval/){:target="_blank"} for more details.

It seems to be a desirable property for a voting system to produce a winner, where no other candidate has a legitimate claim to victory based on the preferences expressed by the voters. This is the essential idea behind what I mean by internal consistency.

I gave proofs in that post and my other [post on Approval Voting](../approval/){:target="_blank"} that Approval Voting is internally consistent. However, I am actually going to prove that Approval voting is the *uniquely* internally consistent cardinal voting method. That is, if you want a system where voters can score candidates (cardinal voting), then the only such system that is internally consistent is Approval Voting: where the only scores are 0 (disapprove) and 1 (approve).

## Internal Consistency

For a ranked system, I defined internal consistency as follows, using the idea of a "Condorcet winner":

> A ranked voting system is internally consistent if, whenever there is a candidate who would beat every other candidate in a head-to-head matchup (called a Condorcet winner), that candidate is declared the overall winner.

This is a relatively intuitive definition, particularly if we're asking voters to rank candidates and are thus collecting data about their ordinal preferences. Thus, if there's a candidate who is preferred by a majority over every other candidate, that candidate should win.

However, due to the general [issues with ranked voting systems](../practicalapproval/){:target="_blank"}, many in the electoral reform community have shifted focus to cardinal voting systems, where voters can give candidates scores rather than rankings. This allows voters to express more nuanced preferences, such as intensity of support or opposition. I personally believe in Approval voting as it asks what I believe is the most important question: "Which candidates do you consent to govern you?" This is inherently a cardinal question that cannot be properly inferred from rankings alone.

## Ballot-Condorcet-Consistency

For a cardinal system, we need to adjust the definition for the vague notion of "internal consistency" slightly, since we're collecting different data. However, it still makes sense to ask if the actual winner would have won in head-to-head match-ups against every other candidate, based on the data collected. Thus, I define internal consistency for cardinal systems as follows:

**Definition:** We define the following notational shorthands:

- Let $$T(X>Y)$$ be the number of voters who give candidate X a strictly higher score than candidate Y. This is the number of voters who prefer X over Y based on their provided ballot data.
- Let $$S(X)$$ be the total score given to candidate X by all voters.

Then, we say a cardinal voting system is **Ballot-Condorcet-Consistent** (BCC) if, whenever $$T(X>Y) > T(Y>X)$$, then $$S(X) > S(Y)$$. That is, if more voters give X a higher score than Y than vice versa, then the total score given to X must be greater than the total score given to Y.

If this is not satisfied, then we have a situation where more voters prefer X over Y, but Y has a higher total score than X, meaning that Y could be declared the winner over X, despite more voters preferring X. This would give X a legitimate claim to victory over Y, particularly if this is true against all other candidates, making them the Condorcet winner "induced by the ballots". It is sufficient to check this is a general condition that holds for any arbitrary pair of candidates, since the winner of a typical cardinal system is the candidate with the highest total score. Thus, being BCC is necessary to guarantee that the Condorcet winner induced by the ballots must have the highest total score.

### Approval is BCC

The proof that Approval Voting is BCC is straightforward, since the total score for each candidate is precisely the number of voters who approved them.

$$
S(X) = T(X>Y) + T(X=Y)
$$

$$
\implies S(X)-S(Y) = T(X>Y) - T(Y>X)
$$

where $$T(X=Y)=T(Y=X)$$ is the number of voters who gave both candidates the same score (either both approved or both disapproved).

This is because

$$S(X)-S(Y)=(T(X>Y)+T(X=Y))-(T(Y>X)+T(Y=X))$$

$$=T(X>Y)-T(Y>X)$$

cancelling out the common approvals, since $$T(X=Y)=T(Y=X)$$. Thus, if $$T(X>Y)>T(Y>X)$$, then $$S(X)>S(Y)$$, satisfying the BCC condition. The difference in total approvals is exactly equal to the difference in "strict approvals", so Approval Voting is BCC.

### Uniqueness of Approval Voting

While most cardinal systems usually give voters integer scores from 0 to 5 or 0 to 10, we can without loss of generality assume that voters can only give scores between and including 0 and 1. This is because if we, say, allowed voters to score from 0 to 10, we could simply divide all scores by 10 to get scores from 0 to 1 without changing any relative comparisons.

From this perspective, every score system is just Approval voting but with fractional approvals. The common 0 to 5 system is just Approval voting where voters can also give 0.2, 0.4, 0.6, or 0.8 of an approval to each candidate.

**Theorem:** The only cardinal voting system that is Ballot-Condorcet-Consistent is Approval Voting.

**Proof:** Suppose that we have a non-Approval cardinal voting system. That is, there is some possible score s with $$0 < s < 1$$ that a voter can give to a candidate.

Let $$t=\text{ceil}\left(\frac1s\right)+1$$. Note that this means that $$st=\text{ceil}\left(\frac1s\right)s+s>1+s>1$$, since $$s>0$$.

It suffices to show exactly one counterexample where more voters prefer candidate A over candidate B, but B has a higher total score than A. Consider the following profile of voters:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| $$t$$ | 0 | 1 | B > A |
| $$t$$ | 1 | $$s$$ | A > B |
| 1 | 1 | 0 | A > B |

It is clear that more voters prefer A over B, since $$T(A>B)=t+1$$ and $$T(B>A)=t$$. However, the total scores are as follows:

$$
S(A) = t\cdot0 + t\cdot1 + 1\cdot1 = t+1
$$

$$
S(B) = t\cdot1 + t\cdot s + 1\cdot0 = t + ts
$$

However, since $$ts>1$$, we have that $$S(B) > S(A)$$. Thus, B has a higher total score than A, despite more voters preferring A over B. This violates the BCC condition, so any non-Approval voting system is not BCC. QED.

### An Example

As an example, consider a system where voters can give scores 0, 1, or 100. A very silly system, but it illustrates the point. We can normalize this to scores 0, 0.01, and 1, giving us $$s=0.01$$. Then, we have $$t=\text{ceil}(100)+1=101$$. Thus, we have the following profile when we un-normalize:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| 101 | 0 | 100 | B > A |
| 101 | 100 | 1 | A > B |
| 1 | 100 | 0 | A > B |

We still have more voters preferring A over B (102 to 101), but the total scores are:

$$
S(A) = 101\cdot0 + 101\cdot100 + 1\cdot100 = 10,200
$$

$$
S(B) = 101\cdot100 + 101\cdot1 + 1\cdot0 = 10,201
$$

Thus, B has a higher total score than A, despite more voters preferring A over B. This violates the BCC condition, so this non-Approval voting system is not BCC.

## STAR is Not BCC

STAR voting is a popular pseudo-cardinal voting system that seems to attempt to fix this issue. It is a 0 to 5 score system, where the winner is chosen by adding an additional runoff step: take the top two candidates by total score and then choose the winner by majority runoff between them. This helps it from some particularly damning examples, but it does not fix the underlying problem.

Take this particular example with three candidates A, B, and C, and 5 voters:

| Number of Voters | Score for A | Score for B | Score for C | Ranking |
|------------------|-------------|-------------|-------------|----------|
| 3 | 5 | 4 | 3 | A > B > C |
| 2 | 0 | 3 | 5 | C > B > A |

Clearly, if we look at the head-to-head match-ups:

| Matchup | Winner | Vote Count |
|---------|--------|------------|
| A vs B | A | 3 to 2 |
| A vs C | A | 3 to 2 |
| B vs C | B | 3 to 2 |

Therefore, A is the Condorcet winner and C is the Condorcet loser.

When we add up the scores, however, something odd happens:

$$
S(A) = 3\cdot5 + 2\cdot0 = 15
$$

$$
S(B) = 3\cdot4 + 2\cdot3 = 18
$$

$$
S(C) = 3\cdot3 + 2\cdot5 = 19
$$

We get that the Condorcet loser C has the highest total score, while the Condorcet winner A has the lowest total score. Thus, in a regular cardinal system, C would be declared the winner, despite being the Condorcet loser induced by the ballots. This would be an extreme violation of internal consistency, since a majority of voters would have preferred both A and B over C.

In STAR voting, however, we take the top two candidates by total score (B and C) and have a runoff. In the runoff, B beats C by a vote of 3 to 2, so B is declared the winner. While this prevents the Condorcet loser from ever winning, we still have two major problems:

1. The Condorcet winner A still loses, despite having a legitimate claim to victory over both B and C.
2. C got the highest total score, but lost in the runoff. This gives them a legitimate claim to victory over B, since they got a higher total score, despite fewer voters preferring them over B.

This creates a mess where every candidate has a legitimate claim to victory. A is the majority's favorite, C got the highest total score, but B won by the system's rules. This would create serious trust issues with the system, since it can't guarantee the winner a bulletproof claim to victory based on the preferences expressed by the voters.

## The Importance of Legitimacy

The point of this post is not to try to claim that non-Approval cardinal systems are unusable. The point of these systems is to give voters greater ability to express their preferences of the candidates. And, thus, not being tied to the Condorcet criterion is arguably a strength, as I have argued in other posts. I don't believe that the ranked Condorcet winner is necessarily the best candidate to always win.

However, being Ballot-Condorcet-Consistent is, in my estimation, an incredibly important property for a voting system to have. Without it, the system cannot maintain or hold trust with its voters, since it can give losing candidates legitimate claims to victory, resulting in distrust and anger from the electorate. People like majority rule, and when it appears that a majority preferred one candidate over another, only for the other candidate to win, that destroys trust in the system.

If a system can point to the data it collected and show that no other candidate, besides the declared victor, has a claim that they were swindled out of victory by the system, then that builds trust. Approval Voting is uniquely positioned to provide that guarantee in a cardinal voting system. In fact, plurality voting and even Condorcet methods, designed precisely to be BCC, fail this to some extent:

- In a Condorcet method, it's possible that the Condorcet winner is not the plurality (first-choice) winner, so the plurality winner could argue that they should have won, since they had the most intense support. There can also not be a Condorcet winner at all, leading to ambiguity and distrust in the particular cycle-breaking method used.
- In a plurality system, it's commonplace for a third-party candidate to have far more votes than the difference between the two main candidates. This give the runner-up a claim that they were robbed of victory by the spoiler effect.
- Any non-Condorcet ranked method is trivially not BCC, leading to trust-destroying elections like Alaska 2022 and Burlington 2009.

Approval voting has no such issues. Since there is no spoiler effect, and since the winner always has the highest total approvals, no other candidate can have a legitimate claim to victory. If Jones wins with 600 approvals, and Bob has 550 approvals, then Bob can't claim that he was somehow robbed of victory.

There's no ranked data to pour through, to see if maybe those who approved both actually preferred Bob to Jones. Exactly 50 more voters approved Jones and not Bob than Bob and not Jones. Those 50 voters weren't held hostage, or forced to only vote for one, or discouraged from approving Bob. They had the choice to approve Bob alongside Jones, and they chose not to. Jones can rightly say, "Skill issue, Bob. Try being more acceptable next time."

In an age where trust in our institutions and elections are at an all-time low, having a voting system that can provide such a guarantee is invaluable. Approval Voting is not just [mathematically elegant](../approval/){:target="_blank"}, it's not just [the most practical and cost-effective solution for our electoral problems](../practicalapproval/){:target="_blank"}, it is the only voting system that can guarantee an unassailable claim to victory for its winners in ALL elections.

[hyperlink](https://youtu.be/saoSEaSDsrY?si=3-8d_6_kd72_WTYR){:target="_blank"}
