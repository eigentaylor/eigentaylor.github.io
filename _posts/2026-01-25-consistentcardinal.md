---
layout: distill
title: Approval voting is the Only Internally Consistent Cardinal Method
date: 2026-01-25
description: A proof that Approval voting is the unique score aggregation voting method that satisfies Score-Condorcet-Consistency, an arguably necessary property for a trustworthy voting system.
giscus_comments: true
importance: 2
tags: voting
category: polisci
featured: false
related_posts: true
pretty_table: true
exclude_appendix_from_word_count: true
collapse_appendix: false
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
      - name: Uniqueness of Approval voting
      - name: An Example
  - name: STAR is Not SCC
  - name: Caveats
  - name: But does Approval elect the best candidates?
  - name: The Importance of Legitimacy
  - name: Appendix
bibliography: voting.bib
---

## Introduction

In my [last post](../practicalapproval/){:target="_blank"}, I focused a lot on the concept of internal consistency as a desirable property for voting methods. The primary purpose of a voting system is to aggregate potentially millions of complex individual preferences into a single name: the winner. This is done by collecting a simpler, easier to aggregate, set of inputs from each voter (ballots), which gives data about their preferences. I define the concept of internal consistency as using the data collected "properly", in a way that is consistent with the preferences expressed by the voters. That is, it does not produce a winner, where another candidate has a legitimate claim to victory based on the data collected in a non-tied election.

For example, a ranked system collects ordinal preferences from each voter. If 51 voters rank candidate A over candidate B, while only 49 voters rank candidate B over candidate A, then it's clear that a majority of voters prefer A over B. If the system were to declare B the winner, for example because of how others rank a third candidate C, then A would have a legitimate claim to victory, and the expressed will of the voters would have been ignored. If it can be further shown that A beats every other candidate, this would mean the system improperly used the data it collected, which destroys trust in the system. IRV, AKA "Ranked Choice Voting", is infamous for this exact failure (e.g. Burlington 2009 or the 2022 Alaska House special election). See my [previous post](../practicalapproval/){:target="_blank"} for more details. However, these failures led to repeal efforts that succeeded in Burlington and narrowly failed in Alaska.

It seems to be a desirable property for a voting system, whenever it produces a unique winner, to have no other candidate with a legitimate claim to victory based on the preferences expressed by the voters. This is the essential idea behind what I mean by internal consistency. In this post, I define an analogous concept for cardinal voting systems, "Score-Condorcet-Consistency" (SCC), which requires the highest scoring candidate to be the one who is preferred by a majority of concerned voters over every other candidate, based on the scores given.

I gave proofs in previous posts that Approval voting is internally consistent. However, I am actually going to prove that Approval voting is the *uniquely* internally consistent cardinal voting method. That is, if you want a system where voters can score candidates (cardinal voting), and elect the candidate with the highest score, then the only such system that is fully internally consistent is Approval voting: where the only scores are 0 (disapprove) and 1 (approve). As we shall see, this cannot be simply fixed by adding a runoff step, as in STAR voting, either.

Note: We focus primarily on score aggregation methods here, where the candidate with the highest total score wins, alongside the popular STAR voting method which adds a runoff step. There are lesser-known cardinal methods that do not simply elect the candidate with the highest total score, and satisfy majority rule as best as a score method can. But such systems run into a different set of legitimacy issues, which I briefly discuss in the [Caveats](#caveats) section. In this post, we focus our attention on score aggregation methods and STAR, which are the most commonly proposed cardinal voting systems.

## Internal Consistency

For a ranked system, I define internal consistency as follows, using the idea of a "Condorcet winner":

> A ranked voting system is internally consistent if, whenever there is a candidate who would be preferred to every other candidate in a head-to-head matchup (called a Condorcet winner), that candidate is declared the overall winner.

This is a relatively intuitive definition, particularly if we're asking voters to rank candidates and are thus collecting data about their ordinal preferences. If there's a candidate who is preferred by a majority over every other candidate, that candidate should win. If you pick anyone else, that candidate can not only say "I was preferred by a majority over the winner", but they can also say "I was preferred by a majority over *every other candidate*".

However, due to the general [issues with ranked voting systems](../practicalapproval/){:target="_blank"}, many (but certainly not all) in the electoral reform community have shifted focus to cardinal voting systems, where voters can give candidates scores rather than rankings. This allows voters to express more nuanced preferences, such as intensity of support or opposition. I personally believe in Approval voting as it asks what I believe is the most important question: "Which candidates do you consent to govern you?" This is inherently a cardinal question that cannot be properly inferred from rankings alone.

## Score-Condorcet-Consistency

For a cardinal system, we need to adjust the definition for the vague notion of "internal consistency" slightly, since we're collecting a different flavor of data. However, it still makes sense to ask if the actual winner would have won in head-to-head match-ups against every other candidate, based on the data collected. Thus, I define internal consistency for cardinal systems as follows:

> **Definition:** We define the following notational shorthands:
>
> - Let $$T(X>Y)$$ be the number of voters who give candidate X a strictly higher score than candidate Y. This is the number of voters who prefer X over Y based on their provided ballot data.
> - Let $$S(X)$$ be the total score given to candidate X by all voters.
>
> Then, we say a cardinal voting system is **Score-Condorcet-Consistent** (SCC) if, whenever $$T(X>Y) > T(Y>X)$$, then $$S(X) > S(Y)$$. That is, if more voters give X a higher score than Y than vice versa, then the total score given to X must be greater than the total score given to Y.

If this is not satisfied, then we can have a situation where more voters prefer X over Y, but Y has a higher total score than X, meaning that Y could be declared the winner over X, despite more voters preferring X. This would give X a legitimate claim to victory over Y, particularly if this is true against all other candidates, making them the Condorcet winner "induced by the ballots". It is sufficient to check that this condition holds for any arbitrary pair of candidates, since the winner of a typical cardinal system is the candidate with the highest total score. Thus, being SCC is necessary to guarantee that the Condorcet winner induced by the ballots must have the highest total score.

### Approval is SCC

> **Approval voting** allows voters to approve of (vote for) as many candidates as they like. Simply put a check mark next to each candidate you approve of. The candidate with the most votes wins.

> **Theorem 1:** Approval voting is Score-Condorcet-Consistent.

The proof is straightforward, since the total score for each candidate is precisely the number of voters who approved them.

$$
S(X)-S(Y) = T(X>Y) - T(Y>X)
$$

We have that $$S(X) > S(Y)$$ if and only if $$T(X>Y) > T(Y>X)$$.

This is because

$$S(X)-S(Y)=(T(X>Y)+T(X=Y))-(T(Y>X)+T(Y=X))$$

$$=T(X>Y)-T(Y>X)$$

where $$T(X=Y)=T(Y=X)$$ are the number of voters who approved both candidates.

Subtracting the total approvals cancels out the common approvals. Thus, if $$T(X>Y)>T(Y>X)$$, then $$S(X)>S(Y)$$, satisfying the SCC condition. The difference in total approvals is exactly equal to the difference in "strict approvals", so Approval voting is SCC. QED.

> **Corollary 1:** Approval voting always elects the Condorcet winner induced by the ballots, if one exists. A unique Condorcet winner induced by the ballots exists whenever one candidate gets the highest total approvals (without a tie).

**Proof:** Suppose candidate A wins the election under Approval voting. Then, for any other candidate B, we have that $$S(A) > S(B)$$. By the SCC property, this implies that $$T(A>B) > T(B>A)$$. Thus, A beats every other candidate in head-to-head match-ups, making them the Condorcet winner induced by the ballots.

The only other case is if there is a tie for highest total approvals, in which case all tied candidates are weak Condorcet winners induced by the ballots. That is, $$S(A) > S(B)$$ implies $$T(A>B) > T(B>A)$$ for all candidates A tied for first and B any other candidate not tied for first, with $$S(A)=S(B)$$ implying $$T(A>B)=T(B>A)$$ for all candidates A and B tied for first. Therefore, the Approval winner(s) are always at least weak Condorcet winner(s) induced by the ballots. But if the election is not tied, then the candidate with the most approvals will be a unique strong Condorcet winner. QED.

The only way for a losing candidate to have a legitimate claim to victory over the Approval winner is if they tied in total approvals with the winner.

> **Corollary 2:** There can be no Condorcet cycles induced by the ballots in Approval voting.

**Proof:** Since Approval voting is SCC, if $$T(A>B) > T(B>A)$$, and $$T(B>C) > T(C>B)$$, then we have that $$S(A) > S(B)$$ and $$S(B) > S(C)$$, implying that $$S(A) > S(C)$$, and thus $$T(A>C) > T(C>A)$$. Therefore, there can be no cycles of the form $$A>B>C>A$$. QED.

### Uniqueness of Approval voting

While most cardinal systems usually give voters integer scores such as from 0 to 5 or 0 to 10, we can without loss of generality assume that voters can only give scores between 0 and 1, inclusive. This is because if we, say, allowed voters to score from 0 to 10, we could simply divide all scores by 10 to get scores from 0 to 1 without changing any relative comparisons.

From this perspective, every score system is just Approval voting but with fractional approvals. The common 0 to 5 system is just Approval voting where voters can also give 0.2, 0.4, 0.6, or 0.8 of an approval to each candidate.

> **Theorem 2:** The only cardinal voting system that is Score-Condorcet-Consistent is Approval voting. That is, if there exists a score s with $$0 < s < 1$$ that voters can give to candidates, then candidates X and Y can be constructed such that X beats Y in head-to-head match-ups, but Y has a higher total score than X.

Proof of Theorem 2 is given in the [appendix](#appendix). However, a concrete example is given [in the next section](#an-example).

The key insight is that by allowing fractional approvals (anything between the minimum and maximum score), we can create situations where a minority-preferred candidate snakes ahead in total score by accumulating many small fractional approvals from voters who prefer the other candidate. This is impossible in Approval voting, where each voter can only give a full approval or disapproval.

> **Theorem 3:** Every non-Approval cardinal voting system can produce a Condorcet cycle induced by the ballots.

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

Any system which allows a Condorcet cycle necessarily fails to be completely internally consistent, since no candidate can be declared the winner without another candidate having a legitimate claim to victory over them. This makes Approval voting uniquely internally consistent, even among ranked systems, since any ranked system with three or more candidates can produce Condorcet cycles.

### An Example

In the appendix of my [other post](../practicalapproval/){:target="_blank"}, I gave an example for a SCC failure in a 0, 1, 2 scoring system. And, of course, the above construction works for any non-Approval cardinal system. But let's use the more common 0-5 system, and I'll leave you with a less conventional example to work through, which illustrates the generality of the proof for Theorem 2 in the [appendix](#appendix), where voters can give a score out of 100.

Consider the general SCORE system where voters can rate a candidate 0,1,2,3,4,5. But let's just focus on 0, 1, and 5. We can normalize this to scores 0, 0.2, and 1, giving us $$s=0.2$$.

We focus on the points of the two frontrunner candidates, A and B. Let us assume that there is an unpopular third candidate C, that both A and B voters dislike strongly, and that is why they give B a nonzero score. In a two candidate race, there is no rational reason for A voters to give B any score other than 0. Using the construction from the proof in the [appendix](#appendix), we have the following profile when we un-normalize:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| 6 | 5 | 1 | A > B |
| 5 | 0 | 5 | B > A |

We still have more voters preferring A over B (6 to 5), but the total scores are:

| Candidate | Total Score |
|-----------|-------------|
| A | $$6\cdot5 + 5\cdot0 = 30$$ |
| B | $$6\cdot1 + 5\cdot5 = 31$$ |

Thus, B has a higher total score than A, despite more voters preferring A over B. This violates the SCC condition, so this non-Approval voting system is not SCC.

What happens after an election like this? Well, candidate A can step up to the podium and refuse to concede. They may claim that they were the rightful winner, since a majority of voters preferred them over B. They can point to the ballot data and say, "if we were still using plurality, I would have won!". Regardless of whether or not this claim is compelling to the electorate, it plants a seed of doubt in the minds of voters. Candidate B is seen as having won only because of the strange and unfamiliar scoring system, a technicality for anti-reform advocates to point to, rather than being a proper representative of the electorate. Supporters of A might feel cheated, and when A asks them for signatures to put a repeal effort on the ballot next cycle, they might just listen.

## STAR is Not SCC

STAR voting is a popular cardinal-esque voting system that seems to attempt to fix this issue with score methods, by injecting in some majority rule. It is a 0 to 5 score system, where the winner is chosen by adding an additional runoff step: take the top two candidates by total score and then choose the winner by majority runoff between them (based on voters who gave them different scores). This helps it from some particularly damning examples, but it does not fix the underlying problem.

Since STAR voting is a 0 to 5 score system, by the above theorem, it is not SCC. However, we can show that the runoff does not fix the underlying legitimacy issues that arise from SCC violations, nor does it guarantee that the Condorcet winner induced by the ballots will win.

Take this particular example with three candidates A, B, and C, and 11 voters:

| Number of Voters | Score for A | Score for B | Score for C | Ranking   |
|------------------|-------------|-------------|-------------|-----------|
| 5                | 1           | 0           | 5           | C > A > B |
| 4                | 1           | 5           | 0           | B > A > C |
| 2                | 5           | 1           | 0           | A > B > C |

If we look at the head-to-head match-ups:

| Match-up | Winner | Vote Count |
|----------|--------|------------|
| A vs B | A | 7 to 4 |
| A vs C | A | 6 to 5 |
| B vs C | B | 6 to 5 |

Therefore, A is the Condorcet winner and C is the Condorcet loser.

When we add up the scores, however, something odd happens:

| Candidate | Total Score |
|-----------|-------------|
| A         | $$5\cdot1 + 4\cdot1 + 2\cdot5 = 19$$ |
| B         | $$5\cdot0 + 4\cdot5 + 2\cdot1 = 22$$ |
| C         | $$5\cdot5 + 4\cdot0 + 2\cdot0 = 25$$ |

We get that the Condorcet loser C has the highest total score, while the Condorcet winner A has the lowest total score. Thus, in a regular cardinal system, C would be declared the winner, despite being the Condorcet loser induced by the ballots. This would be an extreme violation of internal consistency, since a majority of voters would have preferred both A and B over C.

In STAR voting, however, we take the top two candidates by total score (B and C) and have a runoff. In the runoff, B beats C by a vote of 6 to 5, so B is declared the winner. While this prevents the Condorcet loser from ever winning, we still have two major problems:

1. The Condorcet winner A still loses, despite having a legitimate claim to victory over both B and C.
2. C got the highest total score, but lost in the runoff. This gives them a legitimate claim to victory over A and B, since they got the highest total score, despite fewer voters preferring them over the other two alternatives.

This creates a legitimacy-crisis where every candidate has a legitimate claim to victory. A is the majority's favorite, C got the highest total score, but B won by the system's rules. This would create serious trust issues with the system, since it can't guarantee the winner a bulletproof claim to victory based on the preferences expressed by the voters.

## How bad it can get

As it turns out, the closer the fractional score s is to 1, the worse the SCC violation can get. We can make the head-to-head win of A over B arbitrarily large, while B's total score over A is still greater. For example, let s=0.9999. Similar to the above proof, let us assume we have some nonviable third candidate C that both A and B voters dislike strongly, and that is why A voters give B a nonzero score.

Consider the following profile (after un-normalizing):

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| 9,999            | 10,000      | 9,999       | A > B      |
| 1                | 0           | 10,000      | B > A      |

Here, A beats B by 9,999 to 1 (99.99% of voters prefer A over B), but B has a higher total score:

| Candidate | Total Score                                     |
|-----------|-------------------------------------------------|
| A         | $$1\cdot0 + 9,999\cdot10,000 = 99,990,000$$     |
| B         | $$1\cdot10,000 + 9,999\cdot9,999 = 99,990,001$$ |

giving B a higher total score than A by 1 point, despite nearly all voters preferring A over B. The greater the granularity of the scoring system (the closer s is to 1), the worse majority rule can be violated.

The issue with these examples is not that a clear consensus choice like B, who was rated at least 99.99% of the maximum score by every voter, has no legitimate claim to victory themselves. In fact, it seems very likely that, under Approval voting, all voters would approve of B. The problem that arises, however, is that the ballot data leaves evidence of an absurd violation of majority rule, that the losing candidate A could use to fuel distrust in the system.

> **Theorem 4:** For any rational number $$r\in(0.5,1)$$, there exists a cardinal score aggregation voting system that allows a candidate B to have a higher total score than candidate A, despite more voters giving A a higher score than B by a head-to-head ratio of $$r$$. That is, the head-to-head ratio of A over B in the ballot data can get arbitrarily close to 100% of voters declaring a preference for A over B, while B still has a higher total score than A.

A formal proof is given in the [appendix](#appendix).

In general, to achieve a head-to-head win of size $$r=\frac{T(A>B)}{T(A>B)+T(B>A)}\in(0.5,1)$$ (where r is rational), while having B get a higher total score than A, we need:

$$
2-\frac1r < s < 1
$$

If $$\frac{r}{1-r}=\frac{p}{q}$$ then the following profile will do the trick:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| p | 1 | $$s$$ | A > B |
| q | 0 | 1 | B > A |

One might ask the maximum head-to-head win size r achievable for a given score s. Rearranging the above inequality, we have that:

$$
r < \frac{1}{2 - s}
$$

Which gives us one upper bound on the head-to-head win size achievable for a given score s, in this structure of profile. As s approaches 1, this upper bound approaches 1 as well, allowing for arbitrarily large head-to-head wins.

## Caveats

There are [systems](https://electowiki.org/wiki/Smith//Score){:target="_blank"} that attempt to make cardinal systems Condorcet-consistent by electing Condorcet winners when they exist based on the ballot data, or eliminating candidates outside the Smith set (which we will not get into here). However, they are not SCC, as the above proof shows that no non-Approval cardinal system can be. That is, they cannot encode the head-to-head preferences of voters into the scores. Thus, they can still produce losers with legitimate claims to victory:

1. The highest scoring candidate can still fail to be the Condorcet winner induced by the ballots, and not be elected. This is the SCC violation shown above. Such a candidate can claim that they had the highest total score, so they should have won.
2. No candidate may be a Condorcet winner induced by the ballots, leading the eventual winner to necessarily have been beaten head-to-head by some other candidate, giving that candidate a legitimate claim to victory.

This highlights the commonality between non-Approval cardinal systems and ranked systems: by allowing more complex expressions of preference, we open the door to internal consistency failures, where winners can be challenged based on the data collected by the ballots. Approval voting uniquely avoids this issue by entirely eliminating Condorcet cycles through having the score encode the head-to-head preferences directly.

One can rightly argue that the SCC property is too strict, and the fact that non-Approval systems can violate it is not a fatal flaw. After all, the purpose of cardinal systems is to allow voters to express more nuanced preferences, and sometimes that may lead to situations where the majority's preference is not reflected in the total scores. I claim not that a minority preferred, but widely acceptable candidate is necessarily a bad outcome, but rather than when voters can see that their favorite candidate was majority-preferred over the winner and still lost, that destroys trust in the system. Those are the outcomes that lead to repeal efforts, setting back electoral reform as a whole.

## But does Approval elect the best candidates?

There is, in my estimation, a common misconception that is pervasive in the electoral reform community: that Approval voting is too "simple" or "blunt" to elect better candidates. That we need more expressiveness in our ballots to elect the "best" candidates. How can a system that looks just like plurality voting, where voters only check boxes, elect better candidates than a ranked system or a system that allows for granular scoring?

I have argued in [previous posts](../practicalapproval/){:target="_blank"} that Approval voting does not elect milquetoast, beige wall candidates, but rather candidates that are both broadly acceptable and can inspire passionate support. But it still seems counterintuitive to many that increasing the granularity or expressiveness of ballots does not necessarily lead to better outcomes.

The literature, however, shows otherwise. Approval voting has a [strong pull towards the median voter](https://www.jstor.org/stable/2111214){:target="_blank"} <d-cite key="cox1985approvalEquilibrium"></d-cite>, promoting representative outcomes. Simulations put Approval voting at 89-95% VSE (Voter Satisfaction Efficiency), depending on the model used (see [here](https://electionscience.github.io/vse-sim/VSEbasic){:target="_blank"} <d-cite key="quinn2017vseSummary"></d-cite>).

Compared to STAR's 91-98% VSE, and SCORE's 84-96%, Approval voting is extremely comparable. And the extremely minor improvement from Approval to STAR comes at [serious costs beyond the SCC property](../practicalapproval/){:target="_blank"}, in terms of complexity, cost, and trustworthiness. Plurality voting, by comparison, scores around 75% and IRV around 79% ("better than plurality, but worse than all the other methods above").

Given Approval's simplicity, logistical ease of implementation, the bulletproof legitimacy it yields the winner, and strong performance in electing representative candidates, the burden of proof lies on the more complex systems to show that their added complexity, and loss of internal consistency, is worth the trade-off. So far, I have not seen convincing evidence that it is.

## The Importance of Legitimacy

The point of this post is not to try to claim that non-Approval cardinal systems are unusable. The point of these systems is to give voters greater ability to express their preferences of the candidates. Thus, not being tied to the Condorcet criterion is arguably a strength, as I have argued in other posts. I don't believe that the ranked Condorcet winner is necessarily the best candidate to always win.

However, being Score-Condorcet-Consistent is, in my estimation, an incredibly important property for a voting system to have. Without it, the system cannot maintain or hold trust with its voters, since it can give losing candidates legitimate claims to victory, resulting in distrust and anger from the electorate. People like majority rule, and when it appears that a majority preferred one candidate over another, only for the other candidate to win, that destroys trust in the system.

If a system can point to the data it collected and show that no losing candidate has a claim that they were swindled out of victory by the system, then that builds trust. Approval voting is uniquely positioned to provide that guarantee in a cardinal voting system. In fact, plurality voting and even Condorcet methods, designed precisely to have this bulletproof legitimacy for the winner, fail this to some extent:

- In a Condorcet method, it's possible that the Condorcet winner is not the plurality (first-choice) winner, so the plurality winner could argue that they should have won, since they had the most intense support. There can also be no Condorcet winner at all, leading to ambiguity and distrust in the particular cycle-breaking method used. Whoever wins was beaten head-to-head by someone else, giving that candidate a legitimate claim to victory.
- In a plurality system, it's commonplace for a third-party candidate to have far more votes than the difference between the two main candidates. This give the runner-up a claim that they were robbed of victory by the spoiler effect.
- Any non-Condorcet ranked method is exactly that: not Condorcet-consistent. This leads to trust-destroying elections like Alaska 2022 and Burlington 2009, which both fueled massive repeal efforts against ranked choice voting. Since the 2022 Alaska failure, a strong repeal effort in 2024 barely failed by less than 1% of the vote, and it appears that it will be on the ballot again in 2026.

Approval voting has no such issues. Since there is no spoiler effect, and since the winner always has the highest total approvals, no other candidate can have a legitimate claim to victory. If Alice wins with 600 approvals, and Bob has 550 approvals, then Bob can't convincingly claim that he was somehow robbed of victory.

There's no ranked data to pour through, to see if maybe those who approved both or neither actually preferred Bob to Alice. The 100 votes a third candidate Carl got weren't votes that "could have gone to Bob *instead*", as could be claimed under plurality. Exactly 50 more voters approved Alice-and-not-Bob than Bob-and-not-Alice. 50 more voters had the choice to approve Bob alongside Alice. They had the pen in their hand, looked at the box, and they chose not to. Alice can rightly say, "Skill issue, Bob. Try being more acceptable next time."

In an age where trust in our institutions and elections are at an all-time low, having a voting system that can provide such a guarantee is invaluable. Approval voting is not just mathematically elegant, it's not just [the most practical and cost-effective solution for our electoral problems](../practicalapproval/){:target="_blank"}, it is the only voting system (cardinal or otherwise) that can guarantee an unassailable claim to victory for its winners in ALL non-tied elections.

---

## Appendix

Here we include formal proofs of the two major theorems stated above.

> **Theorem 2:** The only cardinal voting system that is Score-Condorcet-Consistent is Approval voting. That is, if there exists a score s with $$0 < s < 1$$ that voters can give to candidates, then a candidate X and Y can be constructed such that X beats Y in head-to-head match-ups, but Y has a higher total score than X.

**Proof:** Suppose that we have a non-Approval cardinal voting system. That is, there is some possible score s with $$0 < s < 1$$ that a voter can give to a candidate.

Let $$t=\text{ceil}\left(\frac1s\right)$$. Note that this means that $$st=\text{ceil}\left(\frac1s\right)s\geq 1$$.

It suffices to show one counterexample where more voters prefer candidate A over candidate B, but B has a higher total score than A. Consider the following profile of voters:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| $$t+1$$ | 1 | $$s$$ | A > B |
| $$t$$ | 0 | 1 | B > A |

It is clear that more voters prefer A over B, since $$T(A>B)=t+1$$ and $$T(B>A)=t$$. However, the total scores are as follows:

$$
S(A) = t\cdot0 + (t+1)\cdot1 = t+1
$$

$$
S(B) = t\cdot1 + (t+1)\cdot s = t + (t+1)s=t + ts + s
$$

However, since $$ts\geq 1$$, we have that $$S(B)\geq t+1+s > S(A)$$. Thus, B has a higher total score than A, despite more voters preferring A over B. This violates the SCC condition, so any non-Approval voting system is not SCC. QED.

**Example:** Consider a system where voters can give scores 0, 1, or 100. We can normalize this to scores 0, 0.01, and 1, giving us $$s=0.01$$. Then, we have $$t=\text{ceil}(100)=100$$. This gives the profile

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| 101              | 100         | 1           | A > B      |
| 100              | 0           | 100         | B > A      |

We still have more voters preferring A over B (101 to 100), but the total scores are:

| Candidate | Total Score                            |
|-----------|----------------------------------------|
| A         | $$100\cdot 0 + 101\cdot 100 = 10,100$$ |
| B         | $$100\cdot 100 + 101\cdot 1 = 10,101$$ |

Once again B wins by one point despite a majority preferring A.

> **Theorem 4:** For any rational number $$r\in(0.5,1)$$, there exists a cardinal score aggregation voting system that allows a candidate B to have a higher total score than candidate A, despite more voters giving A a higher score than B by a head-to-head ratio of $$r$$. That is, the head-to-head ratio of A over B in the ballot data can get arbitrarily close to 100%, while B still has a higher total score than A.

**Proof:** Suppose we have a rational number $$r\in(0.5,1)$$, and let $$\frac{r}{1-r}=\frac{p}{q}$$ for some positive integers p and q. Then, consider the following profile of voters:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| p | 1 | $$s$$ | A > B |
| q | 0 | 1 | B > A |

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
