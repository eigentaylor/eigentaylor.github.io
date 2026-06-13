---
layout: distill
title: The Leader Rule in Approval Voting
date: 2026-06-08
description: An explanation of Laslier's leader rule strategy in Approval voting, and its positive ramifications.
giscus_comments: true
importance: 2
tags: voting
category: polisci
featured: false
theorems: true
related_posts: true
pretty_table: true
exclude_appendix_from_word_count: true
tikzjax: true
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

[Approval voting](../approval-only){:target="_blank"} is a voting method where each voter can "approve" of as many candidates as they like, and the candidate who is approved by the most voters wins.

This post is based on a paper by [Jean-François Laslier](https://journals.sagepub.com/doi/10.1177/0951629808097286)<d-cite key="laslier2009leaderRule"></d-cite>, which introduces the leader rule and analyzes its properties. I would like to give a special thanks to Rob LeGrand for bringing this strategy to my attention. LeGrand, as far as we know, came up with this strategy back in 2002, and Laslier discovered it independently and published about it in his 2009 paper. I find this interesting to bring up, because it shows that this strategy is not just some random "someone just thought of it" strategy, but rather something natural, intuitive, and fundamentally optimal that multiple people have independently discovered.

In [my last post](../av-stratproof){:target="_blank"}, we discussed how Approval voting is not fully strategyproof, and what it means for a ballot in Approval to be "sincere"<d-footnote>The definition of "sincere" in Approval essentially boils down to drawing a line of acceptability in your rankings and approving all candidates above that line. See my last post for the full formal definition. In the seminal 1978 paper by Brams and Fishburn<d-cite key="bramsFishburn1978approval"></d-cite>, they proved that under very contrived scenarios, a sincere strategy might not be optimal.</d-footnote>. Laslier proves that a sincere strategy is always optimal in his model of a large electorate with some uncertainty, and that the leader rule is that sincere best response for single-winner Approval voting based on relatively minimal information about the state of the race.<d-footnote>The leader rule does not apply cleanly to multi-winner Approval voting, such as the primary for a top 2 runoff. The fact that more than one candidate can win breaks some of the assumptions in the model the leader rule is based on.</d-footnote>

> **Definition:** (**The Leader Rule**) Identify the top two frontrunners in the election: the "leader" (most likely to win) and the "challenger" (the most likely to overtake the leader). You, as the voter, then
>
> 1. approve all candidates that you prefer strictly to the leader
> 2. only approve the leader if you prefer them to the challenger.
> 3. Do not approve of any other candidates (i.e. those you like less than the leader).

The core intuition is that applying this strategy is attempting to maximize getting a 'better than (or equal to) expected outcome', while also keeping your ballot efficient by distinguishing in the main race (between the leader and challenger). By drawing a line of acceptability right above or right below the leader, you are maximizing your influence on the most likely pivotal scenario. Hence, you should be stingy with your approvals when your favorite is likely to win, and prudently generous when your top candidates are unlikely to win. Laslier also claims the strategy is sound "from the behavioral point of view".<d-footnote>Laslier connects the leader rule to Tversky's "elimination by aspects" model of decision-making<d-cite key="laslier2009leaderRule"></d-cite>, which is a psychological model of how people make decisions. Laslier claims the leader rule corresponds to this model, by having voters eliminate the possible close races between candidates in order of their likelihood.</d-footnote>

This is actually a [real dynamic we see in real-world Approval elections](https://felixsargent.com/democracy/2025/08/29/st-louis-approval-voting.html) <d-cite key="sargent2025stlouis"></d-cite>. In an analysis of a St. Louis election by Felix Sargent, we saw heavy bullet voting for frontrunners, and *over 80%* of voters who supported a non-frontunner also supporting another candidate. <d-footnote>This example should be taken with a grain of salt, however, since St. Louis uses a top-2 Approval system, which does not apply neatly to the specific single-winner scenario Laslier's paper focuses on. The dynamics and strategy are significantly different for single-round Approval versus Approval with a runoff<d-cite key="fishburnBrams1981runoff"></d-cite>. But the observation stands.</d-footnote>

### An Example of Application

**Example:** Let's discuss the infamous 2000 US Presidential election as an example of how the leader rule would have been applied. We had the following candidates:

| Candidate       | Ideology    |
|-----------------|-------------|
| George W. Bush  | Right       |
| Al Gore         | Center-left |
| Ralph Nader     | Left        |

We can ask how different voters would have applied the leader rule in this election, based on who they perceived as the leader and challenger. For example, in California, Gore was clearly the leader and Bush was the challenger, while Bush was the leader and Gore was the challenger in Texas<d-footnote>For the United States, this state-perspective is nice because depending on which state you were in, the leader and challenger were different. Though, this ignores the fact that the Electoral College puts a damper on the "benefits" of a third party win in a state, which could spoil the ability for your preferred viable candidate to get 270 electoral votes.</d-footnote>. Assuming a general left-right spectrum, we can assume that most voters had the following preferences, and this is how they would have applied the leader rule:

| Voter Type               | Approvals (Gore Leader) | Approvals (Bush Leader) |
|--------------------------|-------------------------|-------------------------|
| Bush $>$ Gore $>$ Nader  | Bush                    | Bush                    |
| Gore $>$ Bush $>$ Nader  | Gore                    | Gore                    |
| Nader $>$ Gore $>$ Bush  | Gore, Nader             | Gore, Nader             |
| Gore $>$ Nader $>$ Bush  | Gore                    | Gore, Nader             |

Each voter bloc tells us a different story about the leader rule. The top two blocs, which collectively prefer the frontrunners over the nonviable candidate, approve of only their most preferred candidate, regardless of who the leader is. It would be a strategic error to approve of the other frontrunner as well, because then you waste your vote and do not help your preferred candidate<d-footnote>When you approve both frontrunners, you maintain the difference in their approval, which means you do not contribute to the outcome.</d-footnote>. There's also no reason to approve the nonviable least preferred candidate. Let's walk through the logic of the leader rule for the Bush $>$ Gore $>$ Nader voters:

- If Bush is the leader, then no candidate is strictly preferred to Bush, so that's step 1. They now compare the leader Bush to the challenger Gore. Since they do prefer the leader Bush to the challenger Gore, they approve of Bush. And they do not approve of anyone they prefer less than Bush, which is Gore and Nader.
- If Gore is the leader, then they approve of Bush, since Bush is strictly preferred to the leader Gore. They do not approve of the leader Gore, since they prefer the challenger Bush to the leader Gore. They also do not approve of Nader, since they prefer Nader less than the leader Gore.

Both reasonable scenarios lead to the same ballot, which is to approve of Bush and no one else. The same logic applies to the Gore $>$ Bush $>$ Nader voters, who approve of Gore and no one else regardless of who the leader is.

The third bloc also has only one dominant strategy, which is to approve of both Gore and Nader regardless of who the leader is. There's no reason *not* to approve of their favorite candidate Nader, on the off chance a miracle happens and Nader somehow wins (ignoring the Electoral College). But given that the *real* race is between this bloc's least favorite candidates, they are incentivized to be prudent and approve of Gore as well, to not waste their vote.

The fourth bloc, however, has a more interesting story. This group most prefers a frontrunner Gore, but they prefer Nader to Bush. If Gore is the leader, then they should only approve of Gore to maximize their lead over all other candidates. However, if Bush is the leader, then they should approve of both Gore and Nader as a prudent defensive "anyone but Bush" strategy.

However, it's worth noting that, in practice, Nader was never a serious contender. Hence, these voters need not agonize over who the actual leader and challenger are. In this case, it's fairly safe to approve of Nader at their personal discretion, while still surely voting for their most preferred candidate Gore.

It's hard to really claim that Approval is "agonizingly strategic" here. Rather, the leader rule makes it quite intuitive and straightforward to determine how to vote--so long as you can identify the leader and challenger. We can note that even in Florida, or another state where it's not entirely clear which of the frontrunners is the leader, since you will still only approve exactly one of the two frontrunners in either case, you will not waste your vote even if you misidentify the leader and challenger.

This example also stumps the "bullet voting" criticism, because we can see that for many of these voters, bullet voting is prudent for voters who like the frontrunners, but voters who most prefer someone nonviable extend their approval to their second choice. This isn't earth-shattering stuff. Approval does not break when voters shrewdly bullet vote when appropriate.

However, this is a strict improvement over our choose-one system, because the voters who like Ralph Nader get to express their support for him without hurting their viable backup Gore. Voters can be [sincere and efficient simultaneously](../av-stratproof){:target="_blank"}, using the leader rule as a simple heuristic to determine where to draw their line of acceptability.

## The Florida Tremble

Here we get into the basic theoretical justification for the leader rule. I won't get too deep into the math or technical details, but I will try to give an intuitive explanation of the logic behind it.

In a large election, the chance that your vote is decisive is essentially zero. Therefore, in a purely deterministic, perfect knowledge model of elections, strategy has basically no purpose. To get around this, Laslier introduces an element of uncertainty to allow for strategy to actually have any impact.

Laslier calls this the "Florida Tremble," after the infamous 2000 US Presidential election in Florida we just discussed, where it's believed that miscounted votes led to a different outcome. By assuming we have "many" voters, and there's a small chance for one of the bubbles on a voter's ballot to be "miscounted" (deleted), there is now a nonzero probability that our vote is decisive in some tie.

Our ballot then becomes a sort of lottery ticket, which *might* pay off by breaking a tie in a favorable way if we approve exactly one of the two tied candidates.

Without getting into the weeds of the relative size of near-infinitesimal probabilities, the intuitive idea is actually quite straightforward: in a large election, ties are very, very, very unlikely.

> **Assumption:** In a large election, the most likely event is that your vote does not matter at all. The second most likely event is that your vote is decisive in a tie between the leader and challenger. The most likely pivotal scenario involving any other candidate besides the leader and challenger is that candidate against the leader. <d-footnote>This is actually proved by Laslier in his paper, but we can just treat this as an intuitive assumption.</d-footnote>

Since it's not particularly helpful to assume our vote is meaningless, we determine our strategy by the most likely pivotal scenarios involving each candidate. The most important being between the leader and challenger. Hence, we always approve exactly one of the two, depending on which one we prefer.

Laslier proves that the most likely pivotal scenario involving any non-leader candidate is still that candidate against the leader (and the leader with the challenger). Essentially, for any other "unlikely" candidate (even including the challenger) to possibly tie for first place, we would need all other candidates who got more votes than Mr. Unlikely (which includes at least the leader) to lose enough votes to get the same or fewer votes than Mr. Unlikely<d-footnote>Laslier spends considerable time discussing the probability of three-way ties, which we will completely ignore here</d-footnote>.

For example, think about the candidate in fourth place. For them to tie for first place, we would need the top 3 candidates to all lose enough votes to make 4th place relevant. The one candidate they're most likely to tie with is the leader, since for it to be anyone else, the leader would have to lose way more votes than, say, the second place candidate. It would require *way more* votes to be miscounted, so the leader comparison is most relevant.

Thus, we compare these unlikely candidates to the leader. This tells us our optimal lottery ticket of a ballot--in regard to candidates who are not the leader--is to approve of all candidates we strictly prefer to the leader, and not approve of any candidates we prefer less than the leader.

And that's the intuition behind the leader rule. Approve everyone you prefer to the leader, and only approve the leader if you prefer them to the challenger.

However, rather than assume the result is fixed, and variations in results are from *ballot errors*, we can loosely treat the leader as just an "expected winner" based on the information we have, and the challenger as the most likely candidate to overtake the leader, with uncertainty based on things like polling error or turnout (and that is how I've been generally presenting it in this post).

## Condorcet-efficiency of the Leader Rule

One might ask "what happens if everyone uses the leader rule, all at once?" Laslier analyzes this in his paper, but we must briefly define what a "[Condorcet winner](../condorcet-approval){:target="_blank"}" is. At its core, it is just a candidate who would defeat every other candidate in a head-to-head matchup. Many claim that electing the Condorcet winner is the "gold standard", though [I argue that is debatable](../why-condorcet){:target="_blank"}. Laslier proves the following result about the leader rule:

> **Theorem:** For a large electorate all applying the leader rule, if there is an equilibrium with no tie, the winner of the election is a Condorcet winner. If there exists a Condorcet winner <d-footnote>For a unique equilibrium to exist, we need a Condorcet winner with a unique "strongest challenger", meaning there is a single candidate with a strongest head-to-head result against the Condorcet winner.</d-footnote>, then there is a unique equilibrium that elects the Condorcet winner.

An "equilibrium" in this context would mean that the result of the election is exactly the same as the expected result (the expected first and second place candidates are the actual first and second place candidates).

Once we realize the mechanics of the leader rule when applied en masse, this is actually not too surprising. Notice that for a non-leader candidate, a voter only approves them *if and only if* they strictly prefer them to the leader. The leader, on the other hand, gets approved exclusively by a voter if and only if they prefer the leader to the challenger.

Thus, if $P(X > Y)$ is the proportion of voters who prefer candidate $X$ to candidate $Y$, then the leader $L$ gets $P(L > C)$ approvals (where $C$ is the challenger), while any other candidate $X$ gets $P(X > L)$ approvals.

If the leader is a Condorcet winner, they receive over 50% approvals (since $P(L > Y) > 0.5$ for all $Y \neq L$), while all others receive under 50% (since $P(X > L) < 0.5$ for all $X \neq L$). The leader thus wins, with the equilibrium challenger being their strongest head-to-head competitor.

In almost all realistic elections, you only need a few iterations of the leader rule to converge to the Condorcet winner from any reasonable starting assumption. However, credit to Rob LeGrand for pointing out to me that it is not necessarily the case that the leader rule converges to the Condorcet winner under all initial conditions. I have included his excellent pathological example in [the appendix](#appendix).

However, even if the Condorcet winner is perceived as nonviable, the leader rule has a natural effect of "bubbling up" strong candidates towards the top, and toppling weak frontrunners with thin support. When voters naturally approve everyone they prefer to the expected winner, and a majority of voters truly prefer a strong but underestimated candidate to the expected winner, then that strong candidate will naturally get more approvals than the expected winner, and an upset will occur.

For example, based on what we've said, after one iteration of the leader rule, a Condorcet winner will naturally accumulate 50%+ approval. If the leader loses head-to-head matchups against one or more candidates, then those candidates will accumulate more than 50% approval, overtaking the leader. The leader rule naturally brings the outcome to something better than or equal to the expected outcome. Further, under the leader rule, someone always gets over 50% approval, so the outcome feels very majoritarian.

Brams also proves in his 2008 book ["Mathematics and Democracy"](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy)<d-cite key="brams2008mathDemocracy"></d-cite> (pg 39) that any outcome which is a *strong* Nash equilibrium must elect a unique Condorcet winner<d-footnote>Note: the leader rule equilibrium is not necessarily a strong Nash equilibrium</d-footnote>. More humorously, he also proves that no Condorcet method can guarantee the election of a Condorcet winner as a Nash equilibrium. This means, in some ways, that Approval can elect the Condorcet winner more "stably" than any method specifically designed to elect such a candidate.

Rather than criticize Approval for being "too strategic", or "allowing for minority rule", the leader rule tells us that strategy is, paradoxically, one of the mechanisms which can lead to *more majoritarian* outcomes in Approval voting.

## What if my information is faulty?

The leader rule requires you to identify the frontrunners. But what if you misidentify them, or cannot determine them reliably?

Your vote is most likely a drop in the ocean and unlikely to matter, which cuts both ways: it's unlikely to be decisive *and* unlikely to backfire if you misjudge. Approval voting cannot [actively betray your preferences](../av-stratproof){:target="_blank"} like Ranked Choice Voting does. The leader rule is simply a reliable heuristic, and helps you improve on your expected outcome.

If uncertain, you can always fall back on an ["honest ballot" strategy](../av-stratproof){:target="_blank"}: vote for everyone "acceptable" to you (however you define that). Approval's safety guarantees make this safe, and it still maximizes the strength of your ballot for those you vote for.

## Conclusion

In essence, we have two different mindsets for how to approach Approval voting strategically:

1. Optimizing for getting an outcome that is better than or equal to what you expect, which is achieved by the leader rule.
2. Optimizing for getting any outcome that is acceptable, which is achieved by [the honest ballot](../av-stratproof){:target="_blank"}.

Laslier's contribution to this conversation is an honest truth that your single vote is unlikely to be decisive, but that doesn't mean you can't vote strategically. By applying the leader rule, you are doing your best to move the election towards the best outcome for you, and the magic is that many people doing this together leads to a more majoritarian outcome.

In the end, strategy boils down to drawing a line of acceptability. The leader rule is a simple, intuitive, and powerful heuristic for how to draw that line in a way that maximizes your influence on the election outcome. It also has some nice theoretical properties, such as electing the Condorcet winner at equilibrium.

Strategy, I argue, is not a bug of Approval voting, but rather a feature that can lead to more majoritarian outcomes. The paradox here is striking: by acting strategically with imperfect information, voters do not degrade, but actually improve the electoral outcome. Individual self-interest, when channeled through the leader rule, naturally aligns with the collective good. This suggests that Approval voting, far from being a naive or vulnerable method, is remarkably robust to human behavior. The leader rule shows us that even (or especially) when voters are savvy enough to think strategically, Approval naturally produces outcomes that the electorate, as a whole, prefers. That is a [system worth taking seriously](../approval-only){:target="_blank"}.

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

The exact numbers are not as important as the pairwise matchups. By ranking the pairwise margins, we will be able to see why the Condorcet winner $B$ cannot become the leader unless they start as the leader.

1. $A$ beats $D$ 73:27
2. $C$ beats $A$ 66:34
3. $D$ beats $C$ 61:39
4. $B$ beats $D$ 56:44
5. $B$ beats $A$ 52:48
6. $B$ beats $C$ 51:49

We can use this list to determine the exact number of approvals each candidate would get under the leader rule, depending on who the leader and challenger are.

For example, if $A$ is the leader, and $C$ is the challenger, then $A$ will get 34 approvals, from the 34 voters who prefer $A$ to $C$. $C$ will similarly get 66 approvals, from the 66 voters who prefer $C$ to $A$. $B$ and $D$ will get approvals based on their matchup against the leader $A$. $B$ will get 52 approvals, from the 52 voters who prefer $B$ to $A$. $D$ will get 27 approvals, from the 27 voters who prefer $D$ to $A$. Hence, in this case, $C$ becomes the new leader, and $B$ becomes the challenger.

If $B$ is the leader, then after an iteration of the leader rule $C$ will be the new challenger. The approvals will be:

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

The structure of this pathology is specifically that $B$ is a milquetoast Condorcet winner, who only wins by very narrow margins, while the other candidates have a volatile cyclic relationship with each other. It should be noted, however, that from the perspective of the electorate, if the election has an outcome at one of these cyclic nodes, then all we would see is a major upset. The expected leader would have a pitiful performance, their strongest challenger would get over 60% of the vote, and $B$ would get over 50%.

From one perspective, this is actually a harmonious outcome, where multiple candidates get majority support, and the candidate who is preferred by a majority over whoever was expected to win, takes office instead. That is, the outcome under the leader rule is still better than expected by a strong majority of voters, even if there was non-convergence that would be invisible to voters.
