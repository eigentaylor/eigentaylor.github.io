---
layout: distill
title: The Leader Rule in Approval Voting
date: 2026-06-08
description: An explanation of Laslier's the leader rule strategy in Approval voting, and its positive ramifications.
giscus_comments: true
importance: 2
tags: voting
category: polisci
featured: false
theorems: true
related_posts: true
pretty_table: true
exclude_appendix_from_word_count: true
bibliography: voting.bib
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
    subsections:
      - name: An Example of Application
  - name: The Florida Tremble
  - name: Condorcet-efficiency of the Leader Rule
  - name: What if my information is faulty?
  - name: Conclusion
  - name: Appendix
---

## Introduction

Approval voting is a voting method where each voter can "approve" of as many candidates as they like, and the candidate who is approved by the most voters wins. Rather than be an [advocacy post](../approval-only){:target="_blank"}, this post is more focused on the following question: how should a voter strategically decide which candidates to approve of, in order to maximize their influence on the election outcome?

This post is based on a paper by [Jean-François Laslier](https://journals.sagepub.com/doi/10.1177/0951629808097286)<d-cite key="laslier2009leaderRule"></d-cite>, which introduces the leader rule and analyzes its properties. I would like to give a special thanks to Rob LeGrand for bringing this strategy to my attention. LeGrand, as far as we know, came up with this strategy back in 2002, and Laslier discovered it independently and published about it in his 2009 paper. I find this interesting to bring up, because it shows that this strategy is not just some random "someone just thought of it" strategy, but rather something natural, intuitive, and fundamentally optimal that multiple people have independently discovered.

In a [recent post](../av-stratproof){:target="_blank"}, we discussed how Approval voting is not fully strategyproof, and that voters should be prudent in drawing their "line of acceptability" in a way that maximizes their influence on the election. The leader rule is a specific strategy for single winner approval <d-footnote>The leader rule does not apply cleanly to multi-winner Approval voting, such as the primary for a top 2 runoff. The fact that more than one candidate can win breaks some of the assumptions in the model the leader rule is based on.</d-footnote> that helps voters determine where to draw that line of acceptability in a way that maximizes their chances of electing a more preferred candidate over a less preferred candidate.

> **Definition:** (**The Leader Rule**) Identify the top two front-runners in the election: the "leader" (most likely to win) and the "challenger" (the most likely to overtake the leader). You, as the voter, then
>
> 1. approve all candidates that you prefer strictly to the leader
> 2. only approve the leader if you prefer them to the challenger.
> 3. Do not approve of any other candidates (i.e. those you like less than the leader).

The core intuition is that applying this strategy is attempting to maximize getting a 'better than (or equal to) expected' outcome, while also keeping your ballot efficient by distinguishing between the main race (between the leader and challenger). By drawing a line of acceptability right above or right below the leader, you are maximizing your influence on the most likely pivotal scenario. Hence, you should be stingy with your approvals when your favorite is likely to win, and prudently generous when your top candidates are unlikely to win.

In the 1978 paper by Brams and Fishburn <d-cite key="bramsFishburn1978approval"></d-cite>, they prove that a sincere strategy is not always optimal in Approval voting when there are four or more candidates. However, Laslier proves in his 2009 paper that the leader rule is a best response in his probabilistic large electorate model, which is always sincere, based on some reasonable assumptions about voters' beliefs. Laslier also claims the strategy is sound "from the behavioral point of view".<d-footnote>Laslier connects the leader rule to Tversky's "elimination by aspects" model of decision-making<d-cite key="laslier2009leaderRule"></d-cite>, which is a psychological model of how people make decisions. Laslier claims the leader rule corresponds to this model, by having voters eliminate the possible close races between candidates in order of their likelihood.</d-footnote>

This is actually a [real dynamic we see in real-world Approval elections](https://felixsargent.com/democracy/2025/08/29/st-louis-approval-voting.html) <d-cite key="sargent2025stlouis"></d-cite>. In an analysis of a St. Louis election by Felix Sargent, we saw heavy bullet voting for frontrunners, and *over 80%* of voters who supported a non-frontunner also supporting another candidate. <d-footnote>This example should be taken with a grain of salt, however, since St. Louis uses a top-2 Approval system, which does not apply neatly to the specific single-winner scenario Laslier's paper focuses on. The dynamics and strategy are significantly different for single-round Approval versus Approval with a runoff.<d-cite key="fishburnBrams1981runoff"></d-cite></d-footnote>

### An Example of Application

**Example:** Let's discuss the famous 2000 US Presidential election as an example of how the leader rule would have been applied. We had the following candidates:

| Candidate       | Ideology    |
|-----------------|-------------|
| George W. Bush  | Right       |
| Al Gore         | Center-left |
| Ralph Nader     | Left        |

We can ask how different voters would have applied the leader rule in this election, based on who they perceived as the leader and challenger. For example, in California, Gore was clearly the leader and Bush was the challenger. In Texas, Bush was the leader and Gore was the challenger<d-footnote>For the United States, this state-perspective is nice because depending on which state you were in, the leader and challenger were different. Though, this ignores the fact that the Electoral College puts a damper on the "benefits" of a third party win in a state, which could spoil the ability for your preferred major party candidate to get 270 electoral votes.</d-footnote>. Assuming a general left-right spectrum, we can assume that most voters had the following preferences, and this is how they would have applied the leader rule:

| Voter Type               | Approvals (Gore Leader) | Approvals (Bush Leader) |
|--------------------------|-------------------------|-------------------------|
| Bush $>$ Gore $>$ Nader  | Bush                    | Bush                    |
| Gore $>$ Bush $>$ Nader  | Gore                    | Gore                    |
| Gore $>$ Nader $>$ Bush  | Gore                    | Gore, Nader             |
| Nader $>$ Gore $>$ Bush  | Gore, Nader             | Gore, Nader             |

Each voter bloc tells us a different story about the leader rule. The top two blocs. which collectively prefer the frontrunners, approve of only their most preferred candidate, regardless of who the leader is. It would be a strategic error to approve of the other front-runner as well, because then you waste your vote. There's also no reason to approve the nonviable least preferred candidate. Let's walk through the logic of the leader rule for the Bush $>$ Gore $>$ Nader voters:

- If Bush is the leader, then no candidate is strictly preferred to Bush, so that's step 1. They now compare the leader Bush to the challenger Gore. Since they prefer Bush to Gore, they approve of Bush. And they do not approve of anyone they prefer less than Bush, which is Gore and Nader.
- If Gore is the leader, then they approve of Bush, since Bush is strictly preferred to the leader Gore. They do not approve of Gore, since they prefer the challenger Bush to the leader Gore. They also do not approve of Nader, since they prefer Nader less than the leader Gore.

Both reasonable scenarios lead to the same ballot, which is to approve of Bush and no one else. The same logic applies to the Gore $>$ Bush $>$ Nader voters, who approve of Gore and no one else regardless of who the leader is.

The fourth bloc also has only one dominant strategy, which is to approve of both Gore and Nader regardless of who the leader is. There's no reason *not* to approve of their favorite candidate Nader, on the off chance a miracle happens and Nader somehow wins. But given that the *real* race is between this bloc's least favorite candidates, they are incentivized to be prudent and approve of Gore as well, to not waste their vote.

The third bloc, however, has a more interesting story. This group most prefers a frontrunner Gore, but they prefer Nader to Bush. If Gore is the leader, then they should only approve of Gore to maximize their lead over all other candidates. However, if Bush is the leader, then they should approve of both Gore and Nader as a prudent defensive "anyone but Bush" strategy.

However, it's worth noting that, in practice, Nader was never a serious contender. Hence, these voters need not agonize over who the actual leader and challenger are. In this case, it's fairly safe to approve of Nader at their personal discretion, while still surely voting for their most preferred candidate Gore.

What I like about this example is that it really puts a damper on the claim that Approval is agonizingly strategic. In this election, where there are two clear front-runners, the leader rule strategy is actually quite straightforward.

It also stumps the "bullet voting" criticism, because we can see that for many of these voters, bullet voting is prudent for voters who like the front-runners, but voters who most prefer someone nonviable extend their approval to their second choice. This isn't earth-shattering stuff. Approval does not break when voters shrewdly bullet vote when appropriate.

However, it's a strict improvement over our choose-one system, because the voters who like Ralph Nader get to express their support for him without hurting Gore, the most preferred viable candidate. Voters can be [sincere *and* efficient](../av-stratproof){:target="_blank"}, using the leader rule as a simple heuristic to determine where to draw their line of acceptability.

## The Florida Tremble

Here we get into the basic theoretical justification for the leader rule. I won't get too deep into the math or technical details, but I will try to give an intuitive explanation of the logic behind it.

In a large election, the chance that your vote is decisive is essentially zero. Therefore, in a purely deterministic, perfect knowledge model of elections, strategy has basically no purpose. To get around this, Laslier introduces an element of uncertainty to allow for strategy to actually have any impact.

Laslier calls this the "Florida Tremble," after the infamous 2000 US Presidential election in Florida we just discussed, where it's believed that miscounted votes led to a different outcome. By assuming we have "many" voters, and there's a small chance for one of the bubbles on a voter's ballot to be "miscounted" (deleted), there is now a nonzero probability that our vote is decisive in some tie.

Our ballot then becomes a sort of lottery ticket, which *might* pay off by breaking a tie in a favorable way if we approve exactly one of the two tied candidates.

Without getting into the weeds of infinitesimal probabilities, and the effect of a "large electorate", the intuitive idea is actually quite straightforward: in a large election, ties are very, very, very unlikely.

> **Assumption:** In a large election, the most likely event is that your vote does not matter at all. The second most likely event is that your vote is decisive in a tie between the leader and challenger. The most likely pivotal scenario involving any other candidate besides the leader and challenger is that candidate against the leader. <d-footnote>This is actually proved by Laslier in his paper, but we can just treat this as an intuitive assumption.</d-footnote>

Since it's not particularly helpful to assume our vote is meaningless, we base our strategy on the second most likely event, which is that our vote is decisive in a tie between the leader and challenger. We should thus vote for one and only one of them. That way our vote gives us a better outcome under that most probable pivotal scenario.

Laslier also proves that the most likely pivotal scenario involving any other candidate besides the leader and challenger is still that candidate against the leader. Essentially, for any other "unlikely" candidate to possibly tie with the leader, we would need the leader to lose enough votes to tie with Mr. Unlikely, *and* for all other candidates who got more votes than Mr. Unlikely to lose enough votes to get fewer votes than Mr. Unlikely.

This is an absurdly improbable scenario, but significantly more likely than any other scenario where Mr. Unlikely has a chance to win. Thus, we compare these unlikely candidates to the leader. This tells us our optimal lottery ticket of a ballot--in regard to candidates who are not the leader or the challenger--is to approve of all candidates we strictly prefer to the leader, and not approve of any candidates we prefer less than the leader.

And that's the intuition behind the leader rule. Approve everyone you prefer to the leader, and only approve the leader if you prefer them to the challenger.

However, rather than assume the result is fixed, and variations in results are from *ballot errors*, we can loosely treat the leader as just an "expected winner" based on the information we have, and the challenger as the most likely candidate to overtake the leader, with uncertainty based on things like polling error or turnout (and that is how I've been generally presenting it in this post).

We distinguish between the leader and challenger on our ballot because the most likely upset is if the challenger has a surge of support. Similarly, the approval of unlikely candidates can also be thought of as hedging for a potential major upset, or dark horse surge for a non-front-runner (which we should only give to unlikely candidates we prefer to the leader).

## Condorcet-efficiency of the Leader Rule

One might ask "what happens if everyone uses the leader rule, all at once?" Laslier analyzes this in his paper and proves the following theorem:

> **Theorem:** For a large electorate, if there is an equilibrium with no tie, the winner of the election is a Condorcet winner. If there exists a Condorcet winner <d-footnote>For a unique equilibrium to exist, we need a Condorcet winner with a unique "strongest challenger", meaning there is a single candidate with a strongest head-to-head result against the Condorcet winner.</d-footnote>, then there is a unique equilibrium that elects the Condorcet winner.

Once we realize the mechanics of the leader rule when applied en masse, this is actually not too surprising. Notice that for a non-leader candidate, a voter only approves them *if and only if* they strictly prefer them to the leader. The leader, on the other hand, gets approved exclusively by a voter if and only if they prefer the leader to the challenger.

Thus, if $P(X > Y)$ is the proportion of voters who prefer candidate $X$ to candidate $Y$, then the leader $L$ gets $P(L > C)$ approvals, where $C$ is the challenger. Any other candidate $X$ gets $P(X > L)$ approvals.

Therefore, if the leader is a Condorcet winner, then a strict minority of voters prefer any other candidate to the leader, so they must get under 50% approvals ($P(X > L) < 0.5$ for all $X \neq L$). Whereas the leader gets over 50% approvals, since they are preferred, by definition, to any possible challenger ($P(L > Y) > 0.5$ for all $Y \neq L$). Hence, the leader retains their lead and wins outright. The equilibrium challenger will be the candidate with the strongest head-to-head result against the leader.

However, credit to Rob LeGrand for pointing out to me that it is not necessarily the case that the leader rule converges to the Condorcet winner under all initial conditions. I will put his example in [the appendix](#appendix).

Brams also proves in his 2008 book ["Mathematics and Democracy"](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy)<d-cite key="brams2008mathDemocracy"></d-cite> (pg 39) that any outcome which is a *strong* Nash equilibrium must elect a unique Condorcet winner<d-footnote>Note: the leader rule equilibrium is not necessarily a strong Nash equilibrium</d-footnote>. More humorously, he also proves that no Condorcet method can guarantee the election of a Condorcet winner as a Nash equilibrium. This means, in some ways, that Approval can elect the Condorcet winner more "stably" than any method specifically designed to elect such a candidate.

Rather than criticize Approval for being "too strategic", or "allowing for minority rule", the leader rule tells us that strategy is, paradoxically, one of the mechanisms which can lead to *more majoritarian* outcomes in Approval voting.

## What if my information is faulty?

It's important to contextualize the fundamental assumptions of the leader rule. To apply it, we are assuming that voters have some information on who the front-runners are, that they can identify a leader and challenger. We assume that we walk into the voting booth, cast our vote, and almost surely the leader wins and our vote was a drop in the bucket. But, *just in case*, our vote might just be a lottery ticket which breaks a tie favorably. But what if your information is wrong, or determining the leader and challenger with certainty is simply infeasible?

The fact that your vote is most likely a drop in the bucket goes both ways. It means that your vote is unlikely to be decisive, but it also means that your vote is unlikely to be *wrong* in a way that actively hurts you if you make some sort of strategic error (since Approval voting cannot [actively betray your preferences](../av-stratproof){:target="_blank"}). The leader rule is simply a reliable heuristic, and helps you bring the outcome to be better than or equal to what you expect.

However, when in doubt, you can fairly reliably fall back on an ["honest ballot" strategy](../av-stratproof){:target="_blank"}, and just vote with your gut. As discussed in that post, Approval has some very nice safety guarantees that make it fairly safe to just vote for everyone you find "acceptable" (however you define that), without worrying about the strategic implications of your vote (maybe include a preferable frontrunner if you have one). Further, when you vote for everyone you find acceptable, you maximize the chance of any acceptable candidate winning, since your ballot does maximal work for the candidates you vote for (which is not a given in other voting methods).

## Conclusion

In essence, we have two different mindsets for how to approach Approval voting strategically:

1. Optimizing for getting an outcome that is better than or equal to what you expect, which is achieved by the leader rule.
2. Optimizing for getting any outcome that is acceptable, which is achieved by [the honest ballot](../av-stratproof){:target="_blank"}.

Laslier's contribution to this conversation is an honest truth that your single vote is unlikely to be decisive, but that doesn't mean you shouldn't vote strategically. By applying the leader rule, you are doing your best to move the election towards the best outcome for you, and the magic is that many people doing this together leads to a more majoritarian outcome.

In the end, strategy boils down to drawing a line of acceptability. The leader rule is a simple, intuitive, and powerful heuristic for how to draw that line in a way that maximizes your influence on the election outcome. It also has some nice theoretical properties, such as electing the Condorcet winner at equilibrium. Strategy, I argue, is not a bug of Approval voting, but rather a feature that can lead to more majoritarian outcomes.

## Appendix

This is an example provided by Rob LeGrand of how the leader rule can fail to "find" or converge to the Condorcet winner, unless voters start by identifying the Condorcet winner as the leader.

**Example:**

| Number of Voters | Ranking of Candidates |
|------------------|-----------------------|
| 17               | $A > D > C > B$       |
| 17               | $A > B > D > C$       |
| 21               | $B > C > A > D$       |
| 18               | $C > B > A > D$       |
| 13               | $D > B > C > A$       |
| 14               | $D > C > A > B$       |

By ranking the pairwise wins, we will be able to see why the Condorcet winner $B$ cannot become the leader unless they start as the leader.

1. $A$ beats $D$ 73:27
2. $C$ beats $A$ 66:34
3. $D$ beats $C$ 61:39
4. $B$ beats $D$ 56:44
5. $B$ beats $A$ 52:48
6. $B$ beats $C$ 51:49

We can use this list to determine the exact number of approvals each candidate would get under the leader rule, depending on who the leader and challenger are.

For example, if $A$ is the leader, and $C$ is the challenger, then $A$ will get 66 approvals, from the 66 voters who prefer $A$ to $C$. $C$ will similarly get 34 approvals, from the 34 voters who prefer $C$ to $A$. $B$ and $D$ will get approvals based on their matchup against the leader $A$. $B$ will get 52 approvals, from the 52 voters who prefer $B$ to $A$. $D$ will get 27 approvals, from the 27 voters who prefer $D$ to $A$. Hence, in this case, $C$ becomes the new leader, and $A$ becomes the challenger.

If $B$ is the leader, then after an iteration of the leader rule, then after one iteration $C$ will be the new challenger. The approvals will be:

| Candidate | Relevant Matchup | Approvals |
|-----------|------------------|-----------|
| $B$       | $B > C$          | 51        |
| $C$       | $C > B$          | 49        |
| $A$       | $A > B$          | 48        |
| $D$       | $D > B$          | 44        |

Hence, $B$ remains the leader and wins. This is an equilibrium, since the leader and challenger are the same as the initial leader and challenger, so no voter has an incentive to change their vote.

However, if any other candidate starts as the leader, then consider what happens to $B$ and the other candidates:

- $B$ will always get over 50% approvals, since $B$ beats every other candidate in a head-to-head matchup.
- But there is some other candidate who beats the leader in a head-to-head matchup by 60% or more, so some other candidate will always get more approvals than $B$ and become the new leader instead of $B$.

For example, we saw that if $A$ starts as the leader, then $C$ can become the new leader, because $C$ has a strong head-to-head win against $A$. The cycle of leaders and challengers, denoting (leader, challenger) pairs, is as follows:

$$(A, B) \to (C, B) \to (D, B) \to (A, B) \to \ldots$$

When no Condorcet winner exists (meaning there is a cycle in the pairwise matchups), then the leader rule will have a cycle in "states" of leader and challenger pairs. But this example shows that a cycle can also occur when there is a Condorcet winner and equilibrium. I'd like to eventually publish a post about the dynamical system induced by en masse application of the leader rule.
