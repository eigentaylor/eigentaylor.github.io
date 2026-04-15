---
layout: distill
title: The Perfection of Approval Voting
date: 2026-04-15
description: A mathematical dive into the fundamentalness of Approval voting on Dichotomous preferences.
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
related_posts: true
theorems: true
pretty_table: true
chart:
  plotly: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introductionn
  - name: Conclusion
  - name: References
---

## Introduction

I've made plenty of [cases for Approval voting recently](../approval-only/){:target="_blank"}. I've talked about it in direct comparison with other methods and why I think it wins out for [various practical reasons](../practicalapproval/){:target="_blank"}. But that's not what I want to do in this post.

Here, I'm going back to my roots. I'm going to just talk about the pure math underlying Approval voting, and why it's fundamental in a way that other voting systems just aren't. I will talk about the proofs that--under certain assumptions--Approval actually breaks the famous impossibility theorems like [Gibbard-Satterthwaite](../gibbart-satt/){:target="_blank"} and [Arrow's Theorem](../arrows/){:target="_blank"}, and what that means.

This post is inspired and borrows heavily on an amazing paper by [Marc Vorsatz: "Approval voting on dichotomous preferences"](http://www.jstor.org/stable/41106808).

### May's Theorem

In 1952, just a year after Kenneth Arrow published his impossibility theorem, another Kenneth in social choice theory, Kenneth May, published a theorem of his own.

> **Theorem:** (May's Theorem) Given a race between two candidates, the unique voting system that is anonymous, neutral, and strictly monotone is majority rule.

To put this in very simple terms:

- **Anonymous:** No voter bias. Everyone's vote is equal. Waldo doesn't contribute 5 votes just because he donates to charity.
- **Neutral:** No candidate bias. The system treats all candidates equally. No bias for Bob because his name starts with a B.
- **Strictly Monotone:** Your vote actually *matters*. If candidate $x$ is tied for first, then voting for $x$ makes them win outright.
- **Majority Rule:** (AKA [Condorcet](../condorcet-approval/){:target="_blank"}) You can either give one vote to either candidate, or abstain. The candidate with the most votes wins. If there is a tie, then we just say that both candidates win.

This is... painfully obvious. I mean, how else would you possibly pick between two people? Just choose the one with the most votes, right?

Well, for two candidates, this is obvious. But for decades, the extension of this theorem to more than two candidates was an open problem. The main problem being [the Condorcet paradox](../condorcet-approval/){:target="_blank"}, which throws a wrench into majority rule. For example, take the following electorate:

| Voters | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 5      | Rock     | Scissors | Paper    |
| 4      | Scissors | Paper    | Rock     |
| 3      | Paper    | Rock     | Scissors |

A majority of eight prefers Rock to Scissors, a majority of nine prefers Scissors to Paper, and a majority of seven prefers Paper to Rock. So who wins? Majority rule doesn't work here. There is no candidate for which it truly makes sense to elect.

But even before May, we already knew that [three candidates is a big problem, thanks to Arrow](../arrows/){:target="_blank"}. Arrow's theorem says that if you have three or more candidates, there is no voting system that can satisfy a certain set of (supposedly) "reasonable" criteria. You essentially have to pick one of the following:

- **Dictatorship:** One voter gets to decide everything. Waldo's ballot is the only one that counts.
- **Infinitely many voters:** If you allow for infinitely many voters, Peter Fishburn showed, hilariously, that you can get a "perfect" majority rule voting system using measure theory. See [this post](../arrows/){:target="_blank"} for more on that.
- **IIA Violation:** The voting system violates the "Independence of Irrelevant Alternatives" criterion, which *loosely* means that an irrelevant spoiler candidate can change the outcome of the election. For example, if Alice originally beats Bob, then the entrance of Clark into the race can cause Bob to win, even if a majority still prefers Alice to Bob.
- A secret fourth choice we will get to shortly...

The knife was twisted in the 70's when Gibbard went on to show that strategy is a fundamental part of voting systems, when you have three or more candidates. Essentially, either the system has to be completely unresponsive to your preferences, or you will have opportunities to get a better outcome by lying to the system. While Gibbard's more general theorem in 1972 hits essentially every voting system, while the [Gibbard-Satterthwaite](../gibbart-satt/){:target="_blank"} theorem is a corollary that applies specifically to ranked voting systems.

The standard conclusion to take from these theorems is that there is no "perfect" voting system.  You have to compromise somewhere. If you want something democratic and responsive to the voters, you won't be able to guarantee it works ideally in all scenarios. You'll always get a case where lying is profitable, or a spoiler candidate throws the system into chaos. But it turns out that this conclusion is not quite the full story.

## Dichotomous Preferences

It turns out that the true underlying key to May's theorem is not exactly that it's just two *candidates*. But, rather, that there are at most two *preference tiers* in the minds of the voters.

> **Definition:** A voter's preferences are *dichotomous* if they can be represented in a maximum of two tiers. In other words, the voter declares each candidate either "acceptable" or "unacceptable", with no further ranking or differentiation between candidates within those tiers. This can include complete indifference (where all candidates are in the same tier).

It may seem like we're basically lobotomizing the voters here. But, from another perspective, when faced with many options, there's an argument that we often do simplify our preferences by just partitioning candidates into "good" and "bad" buckets. Particularly when information is scarce, or we haven't had time to develop more nuanced preferences.

Vorsatz proposes an example of a committee trying to hire a specialized contractor. At the early stages of the process, it may be easier to just label candidates as "qualified" or "unqualified", rather than trying to rank them in a more detailed way. But, more generally, there is an argument to make that even in high stakes elections, voters can identify a set of "acceptable" candidates that they would be happy to see win, and a set of "unacceptable" candidates that they would not want to see win, even if they have an underlying ranking of the candidates.

For example, suppose I love Alice, I think Bob is okay, and I hate Clark. While I technically have three-tiered preferences here, I might decide that Clark is so "unacceptable" that Alice and Bob are both "acceptable" to me. Sure, if it was a runoff between Alice and Bob, I would vote for Alice. But given this is a race between all three, I might decide to just express my preferences more simply as "please, Alice or Bob, just not Clark". If expressed in this way, my preferences have become dichotomous.

However, we won't dwell too much more on this. Regardless of if you think Dichotomous preferences are realistic or not, it turns out that they are our fundamental ticket out of all the messiness of voting.

The question is: in this three candidate race, can we extend May's theorem to find a unique voting system to decide the winner(s) that satisfy basic fairness criteria? If we restrict ourselves to dichotomous preferences, the answer is yes!

## Approval Voting as the Natural Language of Dichotomous Preferences

The most natural system we might devise for dichotomous preferences is to just count how many voters find each candidate acceptable, and then pick the candidate with the most "approvals". This is exactly what Approval voting does.

> **Definition:** In Approval voting, voters mark each candidate as either "approved" or "not approved". The candidate(s) with the most approvals wins.

We stated May's theorem above as satisfying three criteria: anonymity, neutrality, and strict monotonicity. For two candidates, this was sufficient. These three criteria are enough to prove that the system *has* to be majority rule. We can also see that Approval voting satisfies these three criteria.

- Nobody's vote counts more than anyone else's, so it's anonymous.
- The system treats all candidates equally, so it's neutral.
- If a candidate is tied for first, then voting for them makes them win outright, so it's strictly monotone. Your vote actually matters.

But to extend May's theorem to more than two candidates, we need a fourth criterion.

> **Definition:** A voting system is **strategyproof** if no voter can ever "manipulate" the outcome by misrepresenting their preferences.

To get a sense for what this means in practice, let's say that initially we have that Alice and Bob are currently tied for first. I prefer Alice over Clark, and so I voted accordingly (voting that Alice is good and Clark is bad). Strategyproofness means that I can't change my ballot to something else and get a better outcome, such as making Alice win.

Here's an example to show what that might look like. Suppose we have a voting system where you submit your "good" and "bad" candidates. If you say that $n$ candidates are good, then each gets $\frac{1}{n}$ points, and the candidate with the most points wins.

Suppose that currently, Alice and Clark are tied for first, and my current ballot is saying that both Alice and Bob are both good. Then I'm currently giving Alice and Bob half of a point. If I change my ballot to say that only Alice is good, and lie about liking Bob, then my vote now gives Alice a *full* point, and Bob gets zero. This would give Alice half a point more than Clark, and make her win outright. Assuming I prefer a good candidate winning outright over a tie between a good and bad candidate, I have an incentive to lie about my preferences, and so this system is not strategyproof.

But Gibbard's theorem tells us that if we have three or more candidates, then it can't be strategyproof, right? Not on dichotomous preferences!

In [1978, Brams and Fishburn](https://doi.org/10.2307/1955105) prove that Approval voting is the unique "single ballot non-ranked" voting system (a system where you can give single votes to some number of candidates) which is strategyproof on dichotomous preferences.

The intuition being that

- If you vote for any "unacceptable" candidate, then you might make them win over an "acceptable" candidate, which is bad.
- If you don't vote for any "acceptable" candidate, then you might fail to break a tie between an "acceptable" candidate and an "unacceptable" candidate, which is also bad.

So voting exclusively for all good candidates and no bad candidates is weakly dominant. There's no reason to submit any other ballot, and you'll never get anything but a potentially worse outcome by doing so.

Alright, so Approval is anonymous, neutral, strictly monotone, and strategyproof on dichotomous preferences. Big whoop, right? Why does that matter? It turns out this is a *huge* whoop.

> **Theorem:** (Vorsatz, 2007) Approval voting is the unique voting system that is anonymous, neutral, strictly monotone, and strategyproof on dichotomous preferences.

It's not just that Approval happens to be so, it's that Approval is the *only* system that can satisfy these criteria. If you define a voting system that is anonymous, neutral, strictly monotone, and strategyproof on dichotomous preferences, then you can show it is *exactly* Approval voting. No other system can satisfy these criteria. And it gets even better...

> **Theorem:** (Vorsatz, 2007) The four criteria of anonymity, neutrality, strict monotonicity, and strategyproofness on dichotomous preferences are independent. That is, for each criterion, there exists a voting system that satisfies the other three criteria but violates that one.

Vorsatz shows that if you drop any single one of the four criteria, you can define some other voting system that satisfies the other three criteria but violates the one you dropped. So these four criteria are sufficient *and necessary* to define Approval voting on dichotomous preferences.

This, in a sense, makes Approval the "natural language" of dichotomous preferences. It satisfies the most basic fairness properties like neutrality and anonymity by holding no bias for voters or candidates. It's responsive to the voters' preferences by being strictly monotone. And it escapes manipulation by being strategyproof.

Intuitively, it might make sense that Approval is the most basic and intuitive possible voting system you might define if people are labeling candidates "good" and "bad". Just find the candidate(s) the most people think are "good". Done. But Vorsatz shows that it's more fundamental than that.

### The Extension of May's Theorem

One can verify that strategyproofness actually fits perfectly into majority rule one just two candidates. If you prefer one candidate over the other, then the only reasonable ballot is to vote for that candidate and not the other! And if you're indifferent, then abstaining is also weakly dominant. So strategyproofness is satisfied by majority rule with two candidates.

Further, notice that majority rule on two candidates is also equivalent to Approval voting. Voting for one candidate and not the other is exactly the same as approving of one candidate and not the other. Abstaining is the same as approving both candidates. Therefore, we can say that it's not quite majority rule or Condorcet that May's theorem describes, but Approval voting! Which isn't a big surprise as [Approval is a two-tiered Condorcet method](../condorcet-approval/){:target="_blank"}. Thus,

> **Theorem:** (Extension of May's Theorem) The unique voting system that is anonymous, neutral, strictly monotone, and strategyproof on dichotomous preferences is Approval voting.

Brams and Fishburn also proved in 1978 that, on dichotomous preferences, Approval voting is exactly the same as Condorcet. So the fact that May's original theorem is usually stated as majority rule or Condorcet means that this extension via dichotomous preferences through Approval voting is actually quite natural.

## References

Brams, S. J., & Fishburn, P. C. (1978). Approval Voting. *The American Political Science Review*, 72(3), 831-847. [https://doi.org/10.2307/1955105](https://doi.org/10.2307/1955105)

Vorsatz, M. (2007). Approval voting on dichotomous preferences. Social Choice and Welfare, 28(1), 127–141. [http://www.jstor.org/stable/41106808](http://www.jstor.org/stable/41106808)