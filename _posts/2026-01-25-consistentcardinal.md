---
layout: distill
title: Approval Voting is the Only Internally Consistent Cardinal Method
date: 2026-01-25
description: A proof that Approval voting is the unique cardinal voting method that satisfies "Score-Condorcet-Consistency", a necessary property for a trustworthy voting system.
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
  - name: Score-Condorcet-Consistency
    subsections:
      - name: Approval is SCC
      - name: Uniqueness of Approval Voting
      - name: An Example
  - name: STAR is Not SCC
  - name: Caveats
  - name: The Importance of Legitimacy
  - name: Appendix
---

## Introduction

In my [last post](../practicalapproval/){:target="_blank"}, I focused a lot on the concept of internal consistency as a desirable property for voting methods. The primary purpose of a voting system is to aggregate potentially millions of complex individual preferences into a single name: the winner. This is done by collecting a simpler, easier to aggregate, set of inputs from each voter (ballots), which gives data about their preferences. I define the concept of internal consistency as using the data collected "properly", in a way that is consistent with the preferences expressed by the voters. That is, it does not produce a winner, where another candidate has a legitimate claim to victory based on the data collected.

For example, a ranked system collects ordinal preferences from each voter. If 51 voters rank candidate A over candidate B, while only 49 voters rank candidate B over candidate A, then it's clear that a majority of voters prefer A over B. If the system were to declare B the winner, then A would have a legitimate claim to victory, and the expressed will of the voters would have been ignored. If it can be further shown that A beats every other candidate, this would mean the system improperly used the data it collected, which destroys trust in the system. IRV, AKA "Ranked Choice Voting", is infamous for this exact failure (e.g. the 2022 Alaska special election). See my [previous post](../practicalapproval/){:target="_blank"} for more details.

It seems to be a desirable property for a voting system to produce a winner, where no other candidate has a legitimate claim to victory based on the preferences expressed by the voters. This is the essential idea behind what I mean by internal consistency.

I gave proofs in that post and my other [post on Approval Voting](../approval/){:target="_blank"} that Approval Voting is internally consistent. However, I am actually going to prove that Approval voting is the *uniquely* internally consistent cardinal voting method. That is, if you want a system where voters can score candidates (cardinal voting), then the only such system that is internally consistent is Approval Voting: where the only scores are 0 (disapprove) and 1 (approve). This cannot be simply fixed by adding a runoff step, as in STAR voting, either.

## Internal Consistency

For a ranked system, I define internal consistency as follows, using the idea of a "Condorcet winner":

> A ranked voting system is internally consistent if, whenever there is a candidate who would beat every other candidate in a head-to-head matchup (called a Condorcet winner), that candidate is declared the overall winner.

This is a relatively intuitive definition, particularly if we're asking voters to rank candidates and are thus collecting data about their ordinal preferences. If there's a candidate who is preferred by a majority over every other candidate, that candidate should win.

However, due to the general [issues with ranked voting systems](../practicalapproval/){:target="_blank"}, many (but certainly not all) in the electoral reform community have shifted focus to cardinal voting systems, where voters can give candidates scores rather than rankings. This allows voters to express more nuanced preferences, such as intensity of support or opposition. I personally believe in Approval voting as it asks what I believe is the most important question: "Which candidates do you consent to govern you?" This is inherently a cardinal question that cannot be properly inferred from rankings alone.

## Score-Condorcet-Consistency

For a cardinal system, we need to adjust the definition for the vague notion of "internal consistency" slightly, since we're collecting a different flavor of data. However, it still makes sense to ask if the actual winner would have won in head-to-head match-ups against every other candidate, based on the data collected. Thus, I define internal consistency for cardinal systems as follows:

**Definition:** We define the following notational shorthands:

- Let $$T(X>Y)$$ be the number of voters who give candidate X a strictly higher score than candidate Y. This is the number of voters who prefer X over Y based on their provided ballot data.
- Let $$S(X)$$ be the total score given to candidate X by all voters.

Then, we say a cardinal voting system is **Score-Condorcet-Consistent** (SCC) if, whenever $$T(X>Y) > T(Y>X)$$, then $$S(X) > S(Y)$$. That is, if more voters give X a higher score than Y than vice versa, then the total score given to X must be greater than the total score given to Y.

If this is not satisfied, then we can have a situation where more voters prefer X over Y, but Y has a higher total score than X, meaning that Y could be declared the winner over X, despite more voters preferring X. This would give X a legitimate claim to victory over Y, particularly if this is true against all other candidates, making them the Condorcet winner "induced by the ballots". It is sufficient to check this is a general condition that holds for any arbitrary pair of candidates, since the winner of a typical cardinal system is the candidate with the highest total score. Thus, being SCC is necessary to guarantee that the Condorcet winner induced by the ballots must have the highest total score.

### Approval is SCC

> **Approval voting** allows voters to approve of (vote for) as many candidates as they like. Simply put a check mark next to each candidate you approve of. The candidate with the most votes wins.

The proof that Approval Voting is SCC is straightforward, since the total score for each candidate is precisely the number of voters who approved them.

$$
S(X)-S(Y) = T(X>Y) - T(Y>X)
$$

This is because

$$S(X)-S(Y)=(T(X>Y)+T(X=Y))-(T(Y>X)+T(Y=X))$$

$$=T(X>Y)-T(Y>X)$$

where $$T(X=Y)=T(Y=X)$$ are the number of voters who approved both candidates.

Subtracting the total approvals cancels out the common approvals. Thus, if $$T(X>Y)>T(Y>X)$$, then $$S(X)>S(Y)$$, satisfying the SCC condition. The difference in total approvals is exactly equal to the difference in "strict approvals", so Approval Voting is SCC.

**Corollary:** Approval voting always elects the Condorcet winner induced by the ballots, if one exists.

**Proof:** Suppose candidate A wins the election under Approval voting. Then, for any other candidate B, we have that $$S(A) > S(B)$$. By the SCC property, this implies that $$T(A>B) > T(B>A)$$. Thus, A beats every other candidate in head-to-head match-ups, making them the Condorcet winner induced by the ballots.

The only other case is if there is a tie for highest total approvals, in which case all tied candidates are weak Condorcet winners induced by the ballots. That is, $$S(A) > S(B)$$ implies $$T(A>B) > T(B>A)$$ for all candidates A tied for first and B any other candidate not tied for first, with $$S(A)=S(B)$$ implying $$T(A>B)=T(B>A)$$ for all candidates A and B tied for first. Therefore, the Approval winner(s) are always at least weak Condorcet winner(s) induced by the ballots. QED.

The only way for a losing candidate to have a legitimate claim to victory over the Approval winner is if they tied in total approvals with the winner.

**Corollary:** There can be no Condorcet cycles induced by the ballots in Approval voting.

**Proof:** Since Approval voting is SCC, if $$T(A>B) > T(B>A)$$, and $$T(B>C) > T(C>B)$$, then we have that $$S(A) > S(B)$$ and $$S(B) > S(C)$$, implying that $$S(A) > S(C)$$, and thus $$T(A>C) > T(C>A)$$. Therefore, there can be no cycles of the form $$A>B>C>A$$. QED.

### Uniqueness of Approval Voting

While most cardinal systems usually give voters integer scores such as from 0 to 5 or 0 to 10, we can without loss of generality assume that voters can only give scores between and including 0 and 1. This is because if we, say, allowed voters to score from 0 to 10, we could simply divide all scores by 10 to get scores from 0 to 1 without changing any relative comparisons.

From this perspective, every score system is just Approval voting but with fractional approvals. The common 0 to 5 system is just Approval voting where voters can also give 0.2, 0.4, 0.6, or 0.8 of an approval to each candidate.

**Theorem:** The only cardinal voting system that is Score-Condorcet-Consistent is Approval Voting.

**Proof:** Suppose that we have a non-Approval cardinal voting system. That is, there is some possible score s with $$0 < s < 1$$ that a voter can give to a candidate.

Let $$t=\text{ceil}\left(\frac1s\right)$$. Note that this means that $$st=\text{ceil}\left(\frac1s\right)s\geq 1$$, since $$s>0$$.

It suffices to show one counterexample where more voters prefer candidate A over candidate B, but B has a higher total score than A. Consider the following profile of voters:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| $$t$$ | 0 | 1 | B > A |
| $$t+1$$ | 1 | $$s$$ | A > B |

It is clear that more voters prefer A over B, since $$T(A>B)=t+1$$ and $$T(B>A)=t$$. However, the total scores are as follows:

$$
S(A) = t\cdot0 + (t+1)\cdot1 = t+1
$$

$$
S(B) = t\cdot1 + (t+1)\cdot s = t + (t+1)s=t + ts + s
$$

However, since $$ts\geq 1$$, we have that $$S(B)\geq t+1+s > S(A)$$. Thus, B has a higher total score than A, despite more voters preferring A over B. This violates the SCC condition, so any non-Approval voting system is not SCC. QED.

The key insight here is that by allowing fractional approvals, we can create situations where a minority-preferred candidate snakes ahead in total score by accumulating many small fractional approvals from voters who prefer the other candidate. This is impossible in Approval voting, where each voter can only give a full approval or disapproval.

**Theorem:** Every non-Approval cardinal voting system can produce a Condorcet cycle induced by the ballots.

**Proof:** As per the above construction, suppose voters can give a score s with $$0 < s < 1$$. Then, consider three candidates A, B, and C, and the following profile of voters:

| Number of Voters | Score for A | Score for B | Score for C | Preference |
|------------------|-------------|-------------|-------------|------------|
| 1 | 1 | s | 0 | A > B > C |
| 1 | 0 | 1 | s | B > C > A |
| 1 | s | 0 | 1 | C > A > B |

In this profile, we have that:

| Match-up | Winner | Vote Count |
|---------|--------|------------|
| A vs B | A | 2 to 1 |
| B vs C | B | 2 to 1 |
| C vs A | C | 2 to 1 |

Thus, we have a Condorcet cycle A > B > C > A induced by the ballots. QED.

This is quite straightforward: by allowing just a third level of preference intensity, we can create a rock-paper-scissors style cycle among three candidates. As shown above, Approval voting cannot produce such cycles. SCC guarantees a transitive ordering of candidates based on head-to-head match-ups, preventing cycles.

### An Example

In the appendix of my [other post](../practicalapproval/){:target="_blank"}, I gave an example for a SCC failure in a 0, 1, 2 scoring system. And, of course, thd above construction works for any non-Approval cardinal system. But let's do something less conventional to illustrate the generality of the above proof.

As an example, consider a system where voters can give scores 0, 1, or 100. We can normalize this to scores 0, 0.01, and 1, giving us $$s=0.01$$. Then, we have $$t=\text{ceil}(100)=100$$. Thus, we have the following profile when we un-normalize:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| 100 | 0 | 100 | B > A |
| 101 | 100 | 1 | A > B |

We still have more voters preferring A over B (101 to 100), but the total scores are:

$$
S(A) = 100\cdot0 + 101\cdot100 = 10,100
$$

$$
S(B) = 100\cdot100 + 101\cdot1 = 10,101
$$

Thus, B has a higher total score than A, despite more voters preferring A over B. This violates the SCC condition, so this non-Approval voting system is not SCC.

What happens after an election like this? Well, the supporters of A might realize that giving B any score except 0 is dangerous. By being "generous" or "nice" and being honest about how they feel about B, they actually caused their preferred candidate to lose! This creates a perverse incentive to instead just give 0 to every candidate you don't want to win, and the maximum score to the candidates you do want to win, bringing us right back to Approval voting with extra steps and unnecessary complexity.

## STAR is Not SCC

STAR voting is a popular cardinal-esque voting system that seems to attempt to fix this issue with score methods, by injecting in some majority rule. It is a 0 to 5 score system, where the winner is chosen by adding an additional runoff step: take the top two candidates by total score and then choose the winner by majority runoff between them (based on voters who gave them different scores). This helps it from some particularly damning examples, but it does not fix the underlying problem.

Take this particular example with three candidates A, B, and C, and 5 voters:

| Number of Voters | Score for A | Score for B | Score for C | Ranking |
|------------------|-------------|-------------|-------------|----------|
| 3 | 5 | 4 | 3 | A > B > C |
| 2 | 0 | 3 | 5 | C > B > A |

Clearly, if we look at the head-to-head match-ups:

| Match-up | Winner | Vote Count |
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

This creates a legitimacy-crisis where every candidate has a legitimate claim to victory. A is the majority's favorite, C got the highest total score, but B won by the system's rules. This would create serious trust issues with the system, since it can't guarantee the winner a bulletproof claim to victory based on the preferences expressed by the voters.

## How bad it can get

As it turns out, the closer the fractional score s is to 1, the worse the SCC violation can get. We can make the head-to-head win of A over B arbitrarily large, while B's total score over A is still greater. For example, let s=0.9999. Consider the following profile (after un-normalizing):

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| 1 | 0 | 10,000 | B > A |
| 9,999 | 10,000 | 9,999 | A > B |

Here, A beats B by 9,999 to 1 (99.99% of voters prefer A over B), but B has a higher total score:

$$
S(A) = 1\cdot0 + 9,999\cdot10,000 = 99,990,000
$$

$$
S(B) = 1\cdot10,000 + 9,999\cdot9,999 = 10,000 + 99,980,001 = 99,990,001
$$

giving B a higher total score than A by 1 point, despite nearly all voters preferring A over B. The greater the granularity of the scoring system (the closer s is to 1), the worse majority rule can be violated.

In general, to achieve a head-to-head win of size $$r=\frac{T(A>B)}{T(A>B)+T(B>A)}\in(0.5,1)$$ (where r is rational), while having B get a higher total score than A, we need:

$$
2-\frac1r < s < 1
$$

If $$\frac{r}{1-r}=\frac{p}{q}$$ then the following profile will do the trick:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| q | 0 | 1 | B > A |
| p | 1 | $$s$$ | A > B |

A proof is given in the [appendix](#appendix).

## Caveats

There are [systems](https://electowiki.org/wiki/Smith//Score){:target="_blank"} that attempt to make cardinal systems Condorcet-consistent by electing Condorcet winners when they exist based on the ballot data, or eliminating candidates outside the Smith set (which we will not get into here). However, they are not SCC, as the above proof shows that no non-Approval cardinal system can be. That is, they cannot encode the head-to-head preferences of voters into the scores. Thus, they can still produce losers with legitimate claims to victory:

1. The highest scoring candidate can still fail to be the Condorcet winner induced by the ballots, and not be elected. This is the SCC violation shown above. They can claim that they had the highest total score, so they should have won.
2. No candidate may be a Condorcet winner induced by the ballots, leading the eventual winner to necessarily have been beaten head-to-head by some other candidate, giving that candidate a legitimate claim to victory.

This highlights the commonality between non-Approval cardinal systems and ranked systems: by allowing more complex expressions of preference, we open the door to internal consistency failures, where winners can be challenged based on the data collected by the ballots. Approval voting uniquely avoids this issue by entirely eliminating Condorcet cycles by having the score encode the head-to-head preferences directly.

## The Importance of Legitimacy

The point of this post is not to try to claim that non-Approval cardinal systems are unusable. The point of these systems is to give voters greater ability to express their preferences of the candidates. And, thus, not being tied to the Condorcet criterion is arguably a strength, as I have argued in other posts. I don't believe that the ranked Condorcet winner is necessarily the best candidate to always win.

However, being Score-Condorcet-Consistent is, in my estimation, an incredibly important property for a voting system to have. Without it, the system cannot maintain or hold trust with its voters, since it can give losing candidates legitimate claims to victory, resulting in distrust and anger from the electorate. People like majority rule, and when it appears that a majority preferred one candidate over another, only for the other candidate to win, that destroys trust in the system.

If a system can point to the data it collected and show that no other candidate, besides the declared victor, has a claim that they were swindled out of victory by the system, then that builds trust. Approval Voting is uniquely positioned to provide that guarantee in a cardinal voting system. In fact, plurality voting and even Condorcet methods, designed precisely to have this bulletproof legitimacy for the winner, fail this to some extent:

- In a Condorcet method, it's possible that the Condorcet winner is not the plurality (first-choice) winner, so the plurality winner could argue that they should have won, since they had the most intense support. There can be no Condorcet winner at all, leading to ambiguity and distrust in the particular cycle-breaking method used.
- In a plurality system, it's commonplace for a third-party candidate to have far more votes than the difference between the two main candidates. This give the runner-up a claim that they were robbed of victory by the spoiler effect.
- Any non-Condorcet ranked method is exactly that: not Condorcet-consistent. This leads to trust-destroying elections like Alaska 2022 and Burlington 2009, which both fueled massive repeal efforts against ranked choice voting.

Approval voting has no such issues. Since there is no spoiler effect, and since the winner always has the highest total approvals, no other candidate can have a legitimate claim to victory. If Jones wins with 600 approvals, and Bob has 550 approvals, then Bob can't claim that he was somehow robbed of victory.

There's no ranked data to pour through, to see if maybe those who approved both or neither actually preferred Bob to Jones. The 100 votes a third candidate Alice got weren't votes that "could have gone to Bob instead", as could be claimed under plurality. Exactly 50 more voters approved Jones and not Bob than Bob and not Jones. 50 more voters had the choice to approve Bob alongside Jones, they had the pen in their hand and looked at the box, and they chose not to. Jones can rightly say, "Skill issue, Bob. Try being more acceptable next time."

In an age where trust in our institutions and elections are at an all-time low, having a voting system that can provide such a guarantee is invaluable. Approval Voting is not just [mathematically elegant](../approval/){:target="_blank"}, it's not just [the most practical and cost-effective solution for our electoral problems](../practicalapproval/){:target="_blank"}, it is the only voting system that can guarantee an unassailable claim to victory for its winners in ALL elections.

## Appendix

Here we prove the claim from the ["How bad it can get"](#how-bad-it-can-get) section.

Suppose we have a rational number $$r\in(0.5,1)$$, and let $$\frac{r}{1-r}=\frac{p}{q}$$ for some positive integers p and q. Then, consider the following profile of voters:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| q | 0 | 1 | B > A |
| p | 1 | $$s$$ | A > B |

Note that $$f(x)=\frac{x}{1-x}$$ is a continuous increasing function on (0,1). Since $$f(0.5)=1$$, we have that for any $$r\in(0.5,1)$$, we have that $$f(r)$$ is a rational number greater than 1. Therefore, if $$\frac{r}{1-r}=\frac{p}{q}$$, then $$p>q>0$$. This guarantees that $$T(A>B)=p$$ and $$T(B>A)=q$$ are positive integers with $$p>q$$, so more voters prefer A over B.

The precise head-to-head ratio for A over B, further, is

$$\begin{align*}
\frac{T(A>B)}{T(A>B)+T(B>A)} &= \frac{p}{p+q} \\
&= \frac{p/q}{1+p/q} \\
&= \frac{\frac{r}{1-r}}{1+\frac{r}{1-r}} \\
&= \frac{r}{(1-r) + r} \\
&= r
\end{align*}$$

This gives us the desired head-to-head win of size r for A over B.

We now show that B has a higher total score than A whenever $$2-\frac1r < s < 1$$. That is, we want to show that $$S(A)=p<q +ps=S(B)$$.

We prove this using a chain of equivalent inequalities:

$$\begin{align*}
s > 2-\frac1r & \iff rs>2r-1  \\
&\iff 1 - r + rs > r \\
&\iff 1 + \frac{rs}{1-r} > \frac{r}{1-r} \\
&\iff 1 + \frac{sp}{q} > \frac{p}{q} \\
&\iff q + sp > p\\
&\iff S(B) > S(A)
\end{align*}$$

Therefore, B has a higher total score than A and more voters prefer A over B, completing the proof. QED.

---

[hyperlink](https://youtu.be/saoSEaSDsrY?si=3-8d_6_kd72_WTYR){:target="_blank"}
