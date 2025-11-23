---
layout: distill
title: Is Approval Voting Strategyproof?
date: 2025-11-23
description: Well yes, but actually no. Unless...
giscus_comments: true
importance: 2
tags: voting
category: polisci
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: Sincerity and Strategy in Voting
    subsections:
      - name: Under Plurality
      - name: Strategy under Ranked Choice Voting
  - name: Issues with Dichotomous Preferences
  - name: The Game
    subsections:
      - name: Where did the strategy go?
  - name: Conclusion
---

## Introduction

Recently, I wrote a post about [approval voting](../approval/){:target="_blank"}, and I would like to go more in depth here about one of its most appealing properties: strategyproofness. Which it has under very specific and arguably unrealistic conditions.

For this discussion, it's worth being explicit about the definition of the three most commonly discussed voting systems we will be referencnig: plurality (our current system, also called PV), ranked choice voting (RCV), and approval voting (AV).

- **Plurality**: Each voter votes for one candidate. The candidate with the most votes wins.
- **Ranked Choice Voting (RCV)**: Each voter ranks the candidates in order of preference. If a candidate has a majority of first-choice votes, they win. If not, the candidate with the fewest first-choice votes is eliminated, and their votes are redistributed to the next choice on those ballots. This process continues until a candidate has a majority of remaining votes.
- **Approval Voting**: Each voter can vote for (approve of) as many candidates as they like. The candidate with the most approval votes wins.

However, our focus will be focused more on approval voting. The Gibbard-Satterthwaite theorem shows that no reasonable ranked voting system can be strategyproof. Indeed, RCV fails a number of other desirable properties like monotonicity, so beyond an example of strategic voting in RCV, we won't dwell on that system too much.

[Brams and Fishburn](https://www.jstor.org/stable/1955105) showed that approval voting satisfies a number of highly desirable properties. In particular, sincerity under two or three tiered preferences, and strategyproofness under dichotomous (two tiered) preferences. Let's first define what these terms mean.

- A **strategy** is essentially a ballot that a voter casts. For example, under plurality, voting for candidate A is a strategy. Under RCV, ranking candidates as $$A > B > C$$ (which we will denote $$ABC$$) is a strategy. Under approval voting, approving of candidates A and B is a strategy. For PV and AV, we can represent the strategy of a voter $$v$$ as a subset $$S_v$$ of the candidate set $$\mathcal{C}$$. For PV, $$S_v$$ must have exactly one element, and for AV, $$S_v$$ can have any number of elements from 0 to the total number of candidates (it can be any subset of $$\mathcal{C}$$).
- To avoid getting too bogged down in game theoretic terminology, we will call a strategy **optimal** for a voter in a given scenario if they cannot improve their outcome by changing their strategy.
- We call a voter's preference **dichotomous** (or two-tiered) if the voter partitions the candidate set $$\mathcal{C}$$ into two tiers (ex. $$A > B=C=D > E=F$$ is not dichotomous, but $$A=B=C > D=E=F$$ is). For example, a voter might consider the two tiers to be "acceptable" and "unacceptable" candidates.
- We call a strategy $$S_v$$ of candidates **sincere** for a voter if there is no pair of candidates $$C_1 \in S_v$$ and $$C_2 \notin S_v$$ such that the vote $$v$$ strictly prefers $$C_2$$ over $$C_1$$. Intuitively, a sincere strategy is not "missing" any candidates that the voter prefers over candidates in the set.

Note that a sincere strategy doesn't need to include all candidates that the voter is indifferent to in the lowest included tier. For example, if a voter prefers $$A > B=C > D$$, then the sincere strategies are: $$\{A\}$$, $$\{A,B\}$$, $$\{A,C\}$$, and $$\{A,B,C\}$$. Including B but not C, or vice versa, is still sincere, since the voter is indifferent between B and C.

Finally, we say that a voting system is **strategyproof** if there is always only one optimal strategy for any voter in any scenario, and that strategy is sincere.

In their 1978 paper, Brams and Fishburn showed that

1. In plurality voting, the only strategy that is never optimal is to vote for a voter's least preferred candidate. Any other strategy can be optimal in some scenario. This can include the optimal strategy being to vote for the voter's second least preferred candidate.
2. In approval voting, every optimal strategy includes voting for all candidates in the voter's top tier of preferences and no candidates in the voter's bottom tier of preferences. All strategy is always exclusively about how to handle candidates in the middle tiers.
3. Therefore, if there are only two tiers of preferences (dichotomous), then there is one and only one optimal strategy under approval voting: vote for all candidates in the top tier, and no candidates in the other tier. That is, approval voting is strategyproof under dichotomous preferences.

The issue is that real voter preferences are rarely dichotomous. Most voters have more nuanced preferences, with at least three tiers of preference (ex. love, like, lukewarm, weak dislike, strong dislike). Brams and Fishburn showed that under three tiers, approval voting is sincere but not strategyproof. This is because a voter should always include all candidates in their top tier, and exclude all candidates in their bottom tier, but any combination of candidates in the middle tier would still technically be sincere. Therefore, there can be multiple optimal strategies, but all of them are sincere.

Under four or more tiers of preferences, however, approval voting cannot be guaranteed to be sincere (and therefore not strategyproof). For example, consider a voter with preferences $$A > B > C > D$$. Voting for $$A$$ and $$C$$ is not sincere, since the voter is missing $$B$$, which they prefer over $$C$$. However, this strategy can be optimal in some scenarios. For example, suppose the votes before this voter's ballot are:

- A: 10 votes
- B: 10 votes
- C: 9 votes
- D: 9 votes

If the voter votes sincerely for $$A$$ and $$B$$, then they preserve the tie, which is not as good as having $$A$$ win outright. Voting for $$C$$ also doesn't help or hurt. Consider another scenario:

- A: 10 votes
- B: 9 votes
- C: 11 votes
- D: 11 votes

Here, the voter would definitely want to vote for $$C$$. Voting for $$A$$ or $$B$$ will have no effect, since neither can win. However, voting for $$C$$ alone would lead to $$C$$ winning outright over the less preferred $$D$$.

Note: We use $$\subset$$ to denote any subset, including the possibility of equality. We use $$\subsetneq$$ to denote a proper subset, excluding equality.

## Sincerity and Strategy in Voting

### Under Plurality

Let's consider an election with three candidates: A, B, and C, and suppose you are a voter with the preference ABC. Now, let's say that your favorite candidate, A, has basically no chance of winning, and the real contest is between B and C. How you should vote highly depends on what voting system is being used.

Under plurality, where you can only vote for one candidate, voting for A is effectively a wasted vote. Suppose that the final result before your vote is:

- A: 9 votes
- B: 21 votes
- C: 22 votes

And C wins by one vote. If you vote sincerely for A, the result is unchanged. You might as well have stayed home. However, if you vote strategically for B, the result becomes:

- A: 9 votes
- B: 22 votes
- C: 22 votes

And now B and C are tied! This is a strictly better outcome for you, since you prefer B over C. Now, however the tie is broken, there's still a chance that B could win. Whether it's a coin flip (50% chance), or a runoff election is held between B and C, where A can't potentially spoil the election, your strategic vote has improved your expected outcome.

This is a problem, however. You as a voter had an honest preference which would have led to your least preferred candidate winning if expressed sincerely.

### Strategy under Ranked Choice Voting

This can also happen under ranked choice voting (RCV). Suppose a situation with ranked ballots, where you still prefer ABC, and the votes are as follows:

- ABC: 21 votes
- BCA: 21 votes
- CAB: 22 votes

Before your vote, the final result depends on which candidate is determined to be eliminated first. If your favorite A is eliminated first, then your second choice B wins. However, if B is eliminated first, then C wins. Therefore, your vote is incredibly important. If you vote sincerely for A first, then you *force* B to be eliminated first, and C will win. You changed the outcome from a tie that could have gone to your second choice or worst choice, to your worst choice winning for sure.

However, if you vote strategically for B first, then B is safe from elimination, and you force your favorite to be eliminated, leading to B winning for sure. Again, strategically voting for your second choice has improved your outcome, at the cost of sincerity.

It could be even worse under RCV, however. Consider the situation:

- ABC: 22 votes
- BAC: 21 votes
- CBA: 21 votes

Now, without your vote, either B or C could be eliminated first, leading to either A or C winning. Your sincere vote for A first would be completely inconsequential, because it only matters how the votes for B and C are distributed. However, if you vote strategically for B first, then you guarantee that C is eliminated first, leading to B winning for sure.

But if you had instead voted for your *least* favorite C first, then B would be eliminated first, leading to your favorite A winning for sure! In this case, voting for your least favorite candidate has led to your most preferred candidate winning!

## Issues with Dichotomous Preferences

We have seen that under plurality and RCV, strategic voting can improve a voter's outcome, at the cost of sincerity. We have also seen examples where voting insincerely can improve a voter's outcome even undder approval voting, when the voter's preferences are not dichotomous.

In reality, voters have nuanced preferences that are rarely dichotomous. The idea that a voter can be indifferent between all candidates that they approve of versus all candidates that they disapprove of is unrealistic. Most voters have at least three tiers of preference, if not more.

But what if there was an alternate framing that could make voter preferences dichotomous?

## The Game

Consider a hypothetical election with three or more candidates. Perhaps we're talking about a crowded primary of 10 or more candidates. As a voter, you probably have a favorite, a few candidates you like, a few you dislike, and a few you really dislike. However, with so many options, it's unlikely that your favorite candidate can be guaranteed to win. Voting for them only would not be strategically prudent, as you could be throwing away your vote when it comes to the real contest between more viable candidates.

We might reframe the situation away from thinking about a strict ranking of 10+ candidates, and choosing among the thousand possible approval votes to get one's most favorite viable candidate to win, and instead think about which candidates we consider "acceptable" versus "unacceptable".

Now, this isn't much different from regular approval voting, where we necessarily have to project our nuanced preferences onto a dichotomous split of "checked" versus "not checked". However, instead of thinking about two distinct checks as "this would get me this much utility if they win which is more than the utility I would get from this other candidate winning" (i.e. though both simply get checked, one check has more "value" than another), we can frame it under a simpler game.

Suppose we instead choose our goal to be "I just want *any* acceptable candidate to win, and I want to avoid *any* unacceptable candidate winning". While the individual utility between candidates may vary, under our goal, all candidates in each tier are truly equivalent. If anyone we find acceptable wins, then we "win". Otherwise, we "lose". Under this framing, our preferences are truly dichotomous.

> Definition:
>
> We call a voter's goal a **dichotomous goal** if their only concern is having any candidate in an arbitrarily chosen non-empty subset $$S\subset \mathcal{C}$$ win, and avoiding any candidate outside of $$S$$ winning. We can call say that any subset $$S$$ of candidates induces a dichotomous goal for a voter.

Intuitively, this is equivalent to a voter constructing a dichotomous preference where all candidates in $$S$$ are in the top tier, and all candidates outside of $$S$$ are in the bottom tier. This allows us to say:

> Theorem (AV Goal-Relative Strategyproofness):
>
> Consider an approval voting election with candidates $$\mathcal{C}$$. If a voter $$v$$ has the goal of having any candidate in any arbitrarily chosen non-empty subset $$S\subset \mathcal{C}$$ win, and avoiding any candidate outside of $$S$$ winning, then the only optimal strategy for voter $$v$$, under any scenario, is to vote for all candidates in $$S$$, and no candidates outside of $$S$$: $$S_v = S$$

This theorem follows directly from the strategyproofness of approval voting under dichotomous preferences. Think about it this way:

- If you vote for a candidate outside of $$S$$, you risk being the deciding vote that causes that candidate to win, which is against your goal. Therefore, $$S_v\subset S$$. You should never vote for candidates outside of $$S$$.
- If you do not vote for a candidate inside of $$S$$, consider a case where where the candidate you omitted from your ballot is tied for first place with a candidate outside of $$S$$ (or is losing by one vote). Then it wasn't optimal to omit that candidate, since your vote could have caused an acceptable candidate to win over an unacceptable candidate. Therefore, $$S \subset S_v$$. You should always vote for all candidates inside of $$S$$.

Therefore, the only optimal strategy is to vote for all candidates in $$S$$, and no candidates outside of $$S$$. Any deviation *could* lead to you contributing to a failure to achieve your goal, and no deviation can ever improve your chances of achieving your goal.

Note that monotonicity certainly helps here. Unlike in RCV, where a sincere vote can hurt your favorites, voting for candidates in $$S$$ cannot hurt their chances of winning, and, in fact, strictly helps them. And also unlike in plurality, you need not worry about which candidate in $$S$$ has the best chance of winning. The fact you can vote for all of them simultaneously is what simplifies the strategy so significantly (to essentially no strategy at all).

Note that this theorem says nothing about

1. How the voter feels about candidates within $$S$$. They might actually hate them! The point is that under a dichotomous goal, there is one and only one optimal strategy, regardless of how the voter feels about candidates within $$S$$.
2. How the voter chose the set $$S$$. They could have used a random number generator to pick the candidates they put in $$S$$. Or this could be a very honest reflection of what they feel, in their heart, that "acceptable" means. Either way, there's only one optimal strategy under this goal.
3. What any other voters are doing. Even if every candidate in $$S$$ has absolutely no chance of winning, voting for them is still the only optimal and rational strategy under this goal. If multiple candidates in $$S$$ have a chance, there's still no reason to exclude any of them from your ballot, because what if there's an upset, or a polling miss, and a witheld vote causes a candidate outside of $$S$$ to win?

However, if this dichotomous goal is a rational projection of a voter's nuanced preferences (i.e. if the voter's set $$S$$ defines a sincere strategy for them), then we can in fact say

> Corollary (AV Strategyproofness under Dichotomous Goals):
>
> If a voter has a sincere strategy $$S_v$$, then choosing the dichotomous goal induced by $$S_v$$ leads to approval voting being strategyproof for that voter under that goal.

Note that, again, this says nothing about how what any other voter is doing. If you, as a voter, choose your approval set $$S_v$$ sincerely, and decide to adopt the dichotomous goal induced by $$S_v$$, then there is no scenario where voting for $$S_v$$ is not optimal for you. We have essentially eliminated all strategy from your perspective. The only ballot it is rational to cast is a sincere expression of this preference.

### Where did the strategy go?

So where did the strategy go? The sleight of hand here is in *how* we constructed the sincere strategy $$S_v$$ for which our dichotomous goal is induced. If a voter has preference $$A > B > C > D > E$$, then there are four possible sincere approval strategies depending on where the voter draws their line:

1. $$\{A\}$$
2. $$\{A,B\}$$
3. $$\{A,B,C\}$$
4. $$\{A,B,C,D\}$$

And it gets more complex if it's not a strict ranking. If the voter is actually indifferent between B and C, then $$\{A,C\}$$ is also a sincere strategy. Each of these sincere strategies induces a different dichotomous goal. Therefore, the strategy has not disappeared, it has just been moved to a much simpler decision: where to draw the line between acceptable and unacceptable candidates.

The key is that once a voter has drawn that line, then choosing a dichotomous goal induced by that line makes approval voting strategyproof for them. There is no longer any incentive to try to game the system by including or excluding candidates in the middle tiers of their preferences. The only rational choice is to vote sincerely according to their chosen line.

The practical upshot for you as a voter is that once you draw your line, then you no longer need to worry about strategy. If you are extremely principled, and you only approve of your absolute favorite candidate, then so be it. Choosing the dichotomous goal induced by that strategy, where it's your favorite or bust, then there's still no reason to second guess yourself (even if that goal is unlikely to be achieved, bullet voting is still the only optimal strategy under that goal).

If you are more pragmatic, you can **choose** to be strategic and might be more inclusive, which effectively strengthens your vote *against* the candidates you omit from your strategy, or less inclusive if you feel your favorites have a better chance. Either way, **once you have drawn your line, there is no further strategy to consider under this goal.**

## Conclusion

The purpose of this post is not to argue that approval voting is actually strategyproof in practice. Rather, it is a suggestion for you as a voter. I am offering you a mental model. A goal for you to frame your approval vote, which allows you to cast a sincere ballot without worrying about strategy.

I know many people who feel very strongly about a few favorites. For them, the strategy of drawing that line would also be something they would cast aside. If you feel similarly, then this framing could greatly simplify your voting experience. You can just pick your favorites, and not worry about the rest.

Personally, this is how I approach approval voting. I am generally less strict about my approval set. I would be generally generous with my approvals, and that makes AV very robust and appealing to me. Sure, I could construct a ranking. I could try to game the system and betray a candidate I like in order to help my favorite win. But I also got other stuff going on, man. I'd rather just vote my conscience, and feel good knowing that my voice will be heard:

- my vote will strictly help the candidates I approve of
- my vote will strictly hurt the candidates I don't approve of
- I was able to express my preferences sincerely without worrying that sincerity will cost me
- the cognitive load of deciding my ballot was extremely low.

I simply cannot say the same under plurality or RCV.

[hyperlink](https://youtu.be/_iKn27LsQ9Y?si=yNil-WKiyD8HOItY){:target="_blank"}
