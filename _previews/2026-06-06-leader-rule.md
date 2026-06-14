---
layout: distill
title: The Leader Rule in Approval Voting
date: 2026-06-13
description: An explanation of Laslier's leader rule strategy in Approval voting, and its positive ramifications.
giscus_comments: true
importance: 1
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
  - name: The Intuition
  - name: Condorcet-efficiency of the Leader Rule
  - name: What if my information is faulty?
  - name: Conclusion
  - name: Appendix
    subsections:
      - name: The Florida Tremble
      - name: The LeGrand Pathology
---

## Introduction

[Approval voting](../approval-only){:target="_blank"} is a voting method where each voter can "approve" of as many candidates as they like, and the candidate who is approved by the most voters wins. For many people, the system is quite straightforward: [you approve of all the candidates you like, and do not approve of any candidates you dislike](../av-stratproof){:target="_blank"}. However, for a voter who wants to be strategic, the question of "who should I approve?" can be a bit more complicated.

This post is based on a paper by Jean-François Laslier<d-cite key="laslier2009leaderRule"></d-cite>, which introduces the leader rule and analyzes its properties. I would like to give a special thanks to Rob LeGrand for bringing this strategy to my attention. LeGrand, as far as we know, came up with this strategy back in 2002<d-cite key="legrand2002strategyA"></d-cite>, and Laslier published about it in his 2009 paper independently. I find this interesting to bring up, because it shows that this strategy is not just some random "someone just thought of it" strategy, but rather something fundamentally natural and intuitive.

In [my last post](../av-stratproof){:target="_blank"}, we discussed how Approval voting is not fully strategyproof, and what it means for a ballot in Approval to be "sincere"<d-footnote>The definition of "sincere" in Approval essentially boils down to drawing a line of acceptability in your rankings and approving all candidates above that line. See my last post for the full formal definition. In the seminal 1978 paper by Brams and Fishburn<d-cite key="bramsFishburn1978approval"></d-cite>, they proved that under very contrived perfect-knowledge scenarios with four or more candidates, a strategy such as voting for your first and third choice, and not your second, can be optimal.</d-footnote>. Laslier proves that a sincere strategy is always optimal in his model of a large electorate with some uncertainty, and that the leader rule is that best response for single-winner Approval voting (which is sincere) based on relatively minimal information about the state of the race.<d-footnote>The leader rule does not apply cleanly to multi-winner Approval voting, such as the primary for a top 2 runoff. The fact that more than one candidate can win breaks some of the assumptions in the model the leader rule is based on. The dynamics and strategy are significantly different for single-round Approval versus Approval with a runoff<d-cite key="fishburnBrams1981runoff"></d-cite>.</d-footnote>

> **Definition:** (**The Leader Rule**) Identify the top two frontrunners in the election: the "leader" (most likely to win) and the "challenger" (the most likely to overtake the leader). You, as the voter, then
>
> 1. approve all candidates that you prefer strictly to the leader
> 2. only approve the leader if you prefer them to the challenger.
> 3. Do not approve of any other candidates (i.e. those you like less than the leader).

To phrase it another way, if you prefer the leader to the challenger, approve of the leader and all candidates you prefer to the leader (draw your line right under the leader). If you prefer the challenger to the leader, approve only the candidates you prefer to the leader, and do not approve of the leader (draw your line right above the leader).

The core intuition is that applying this strategy is attempting to maximize getting a 'better than (or equal to) expected outcome', while also keeping your ballot efficient by distinguishing in the main race (between the leader and challenger). By drawing a line of acceptability right above or right below the leader, you are maximizing your influence on the most likely pivotal scenarios.

Hence, you should be stingy with your approvals when your favorite is likely to win, and prudently generous when your top candidates are unlikely to win. Laslier also claims the strategy is sound "from the behavioral point of view".<d-footnote>Laslier connects the leader rule to Tversky's "elimination by aspects" model of decision-making<d-cite key="laslier2009leaderRule"></d-cite>. He claims the leader rule corresponds to this model, by having voters eliminate the possible close races between candidates in order of their likelihood.</d-footnote>

This is actually a [real dynamic we see in real-world Approval elections](https://felixsargent.com/democracy/2025/08/29/st-louis-approval-voting.html) <d-cite key="sargent2025stlouis"></d-cite>. In an analysis of a St. Louis election by Felix Sargent, we saw around 60% of frontrunner supporters bullet voted, while *over 80%* of voters who supported a non-frontunner also approved another candidate. <d-footnote>This example should be taken with a grain of salt, since St. Louis uses a top 2 Approval system, which does not map neatly to the specific single-winner scenario Laslier's paper focuses on. But the observation stands.</d-footnote>

### An Example of Application

**Example:** Let's discuss the infamous 2000 US Presidential election as an example of how the leader rule would have been applied. We will assume a national popular vote election, and neglect the Electoral College<d-footnote>The Electoral College adds complexity when it comes to third party wins, which could spoil the ability for your preferred viable candidate to get 270 electoral votes. Under a national popular vote, the leader rule applies cleanly, but with a universal leader and challenger across all states, rather than the leader depending on which state you are in.</d-footnote>. We had the following candidates:

| Candidate       | Ideology    |
|-----------------|-------------|
| George W. Bush  | Right       |
| Al Gore         | Center-left |
| Ralph Nader     | Left        |

We can ask how different voters would have applied the leader rule in this election, based on who they perceived as the leader and challenger. Assuming a general left-right spectrum, we can assume that most voters had the following preferences, and this is how they would have applied the leader rule:

| Voter Type               | Approvals (Gore Leader) | Approvals (Bush Leader) |
|--------------------------|-------------------------|-------------------------|
| Bush $>$ Gore $>$ Nader  | Bush                    | Bush                    |
| Gore $>$ Bush $>$ Nader  | Gore                    | Gore                    |
| Nader $>$ Gore $>$ Bush  | Gore, Nader             | Gore, Nader             |
| Gore $>$ Nader $>$ Bush  | Gore                    | Gore, Nader             |

Each voter bloc tells us a different story about the leader rule. The top two blocs, which collectively prefer the frontrunners over the nonviable candidate, approve of only their most preferred candidate, regardless of who the leader is. It would be a strategic error to approve of the other frontrunner as well, because then you waste your vote and do not help your preferred candidate<d-footnote>When you approve both frontrunners, you maintain the difference in their approval, which means you do not contribute to the outcome. I call this "passive inefficiency". It's like voting for a nonviable candidate in our choose-one system: you don't directly elect your worst nightmare, but you don't do the best you can to stop them (by holding your nose and voting for the preferable frontrunner).</d-footnote>. There's also no reason to approve the nonviable least preferred candidate. Let's walk through the logic of the leader rule for the Bush $>$ Gore $>$ Nader voters, specifically:

- If Bush is the leader, then you definitely prefer the leader Bush to the challenger Gore, so you draw your line right below the leader Bush, meaning you approve of Bush and no one you like less (Gore and Nader).
- If Gore is the leader, then you prefer the challenger Bush to the leader Gore, so you draw your line right above the leader Gore, meaning you approve of Bush (who is above the line) but not Gore or Nader (who are below the line).

Both reasonable scenarios lead to the same ballot, which is to approve of Bush and no one else. The same logic applies to the Gore $>$ Bush $>$ Nader voters, who approve of Gore and no one else regardless of which of the frontrunners is the leader.

The third bloc also has only one dominant strategy, which is to approve of both Gore and Nader regardless of who the leader is. There's no reason *not* to approve of their favorite candidate Nader, on the off chance a miracle happens and Nader somehow wins (ignoring the Electoral College). But given that the *real* race is between this bloc's least favorite candidates, they are incentivized to be prudent and approve of Gore as well, to not waste their vote.

The fourth bloc, however, has a more interesting story. This group most prefers a frontrunner Gore, but they prefer Nader to Bush. If Gore is the leader, then the line is drawn right below the leader Gore, and they thus only approve of Gore to maximize Gore's lead over all other candidates. However, if Bush is the leader, then they draw their line right above Bush, meaning they approve of both Gore and Nader as a prudent defensive "anyone but Bush" strategy.

However, it's worth noting that, in practice, Nader was never a serious contender. Hence, the voters in this bloc need not agonize over who the actual leader and challenger are. In this case, it's fairly safe to approve of Nader at their personal discretion, while still surely voting for their most preferred candidate Gore.

It's hard to really claim that Approval is "agonizingly strategic" here. Rather, the leader rule makes it quite intuitive and straightforward to determine how to vote--so long as you can identify the leader and challenger. We can note that even if it's not entirely clear which of the two frontrunners is the leader, since you will still only approve exactly one of the two frontrunners in either case, you will likely not waste your vote even if you misidentify the leader and challenger.

This example also stumps the "bullet voting" criticism, because we can see that for many of these voters, bullet voting is prudent for voters who like the frontrunners, but voters who most prefer someone nonviable extend their approval to their second choice. This isn't earth-shattering stuff. Approval does not break when voters shrewdly bullet vote when appropriate.

However, this is a strict improvement over our choose-one system, because the voters who like Ralph Nader get to express their support for him without hurting their viable backup Gore. Voters can be [sincere and efficient simultaneously](../av-stratproof){:target="_blank"}, using the leader rule as a simple heuristic to determine where to draw their line of acceptability.

In the real 2000 election, Gore won the popular vote, but Bush won the electoral college through Florida by a razor-thin margin of 537 votes (out of millions), while Nader received over 90,000 votes in the same state. If Nader voters were able to approve of both Gore and Nader, then Gore would have likely won Florida and thus the presidency. This is a clear example of how Approval can fix the spoiler effect.

## The Intuition

Here we get into the basic theoretical justification for the leader rule. I won't get too deep into the math or technical details, but I will try to give an intuitive explanation of the logic behind it. For the actual model Laslier uses, see [the appendix](#appendix). For the full technical details, see Laslier's original paper<d-cite key="laslier2009leaderRule"></d-cite>.

In a large election, the chance that your vote is decisive is essentially zero. Therefore, in a purely deterministic, perfect knowledge model of elections, strategy has basically no purpose. To get around this, Laslier introduces an element of uncertainty to allow for strategy to actually have any impact.

We can imagine that we have some "expected winner" which we call the leader, but there is some small chance that a candidate could surge and overtake the leader. We also have a "challenger" who appears the most likely to have a last-minute surge to overtake the leader.<d-footnote>Laslier actually has a completely different framing in terms of deleted votes, which we detail in the appendix, but the intuition gets us largely to the same place.</d-footnote>

We might imagine that many voters who think like us will apply the same strategy, and cause a surge for the candidates we approve of. So we want to be strategic about which candidates we actually want to surge. Though, our one ballot is merely a contribution to a potential surge, rather than a guarantee.

The most likely upset scenario is that the challenger surges past the leader. If we prefer the leader, we approve of the leader and not the challenger to fortify against that. If we prefer the challenger, we approve of the challenger and not the leader to contribute to that upset. Hence, we approve of exactly one of the two frontrunners, depending on which one we prefer.

For any other upset involving an underdog, the path of least resistance is that they surge to compete with the leader<d-footnote>To see this, consider that it requires fewer assumptions for that one candidate to have a single surge to first place, than it is for, say, the challenger <i>and</i> the dark horse to both surge past the leader.</d-footnote>. We want this to happen if we prefer that candidate to the leader, and we want to prevent it if we prefer the leader to that candidate. Thus, we approve of all candidates we prefer to the leader, and do not approve of any candidates we prefer less than the leader.

And that's the intuition behind the leader rule. Approve everyone you prefer to the leader, and only approve the leader if you prefer them to the challenger.

## Condorcet-efficiency of the Leader Rule

One might ask "what happens if everyone uses the leader rule, all at once?" Laslier analyzes this in his paper, but we must briefly define what a "Condorcet winner" is. It is simply a candidate who would defeat every other candidate in a head-to-head matchup. Many claim that electing the Condorcet winner is the "gold standard", though [I argue that is debatable](../why-condorcet){:target="_blank"}. Laslier proves the following result about the leader rule:

> **Theorem:** For a large electorate all applying the leader rule, if there is an equilibrium<d-footnote>An "equilibrium" in this context would mean that the result of the election is exactly the same as the expected result (the expected first and second place candidates are the actual first and second place candidates).</d-footnote> with no tie, the winner of the election is a Condorcet winner. If there exists a Condorcet winner <d-footnote>For a unique equilibrium to exist, we need a Condorcet winner with a unique "strongest challenger", meaning there is a single candidate with a strongest head-to-head result against the Condorcet winner.</d-footnote>, then there is a unique equilibrium that elects the Condorcet winner.

Once we realize the mechanics of the leader rule when applied en masse, this is actually not too surprising. Notice that for a non-leader candidate, a voter only approves them *if and only if* they strictly prefer them to the leader. The leader, on the other hand, gets approved exclusively by a voter if and only if they prefer the leader to the challenger.

If the leader is a Condorcet winner, then a majority of voters prefer the leader to any other challenger, so the leader gets over 50% approval. Since a minority of voters would prefer any other candidate to the leader, all other candidates get under 50% approval. Hence, the Condorcet winner leader must win with a majority of the votes!

In almost all realistic elections, you only need a few iterations of the leader rule to converge to the Condorcet winner from any reasonable starting assumption. However, credit to Rob LeGrand for pointing out to me that there are exceptions. I have included his excellent pathological example in [the appendix](#appendix).

However, even if the Condorcet winner is perceived as nonviable, the leader rule has a natural effect of "bubbling up" strong candidates towards the top, and toppling weak frontrunners with thin support.

When voters naturally approve everyone they prefer to the expected winner, and a majority of voters truly prefer a strong but underestimated candidate to the expected winner, then that strong candidate will naturally get more approvals than the expected winner, and an upset will occur. This matches our intuition about surges and upsets, and is a natural consequence of the leader rule.

For example, based on what we've said, after one iteration of the leader rule, a Condorcet winner will naturally accumulate 50%+ approval--leader or not. If the leader loses head-to-head matchups against one or more candidates, then those candidates will accumulate more than 50% approval, overtaking the leader.

The leader rule naturally brings the outcome to something better than or equal to the expected outcome, from the collective perspective. Further, under the leader rule, someone always gets over 50% approval, so the outcome feels very majoritarian.

Brams also proves in his 2008 book ["Mathematics and Democracy"](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy)<d-cite key="brams2008mathDemocracy"></d-cite> (pg 39) that any outcome which is a *strong* Nash equilibrium must elect a unique Condorcet winner<d-footnote>Note: the leader rule equilibrium is not necessarily a strong Nash equilibrium.</d-footnote>. More humorously, he also proves that no Condorcet method can guarantee the election of a Condorcet winner as a Nash equilibrium. This means, in some ways, that Approval can elect the Condorcet winner more "stably" than any method specifically designed to elect such a candidate.

Rather than criticize Approval for being "too strategic", or "allowing for minority rule", the leader rule tells us that strategy is, paradoxically, one of the mechanisms which can lead to *more majoritarian* outcomes in Approval voting.

## What if my information is faulty?

The leader rule requires you to identify the frontrunners. But what if you misidentify them, or cannot determine them reliably?

By being strictly monotonic, Approval voting will never weaponize your vote against you (like [Ranked-Choice Voting](../ditch-rcv){:target="_blank"} has done). Your vote will only help the candidates you approve of, and does so maximally. The safety guarantees Approval has mean that, at worst, your ballot can be "[passively inefficient](../av-stratproof){:target="_blank"}".

Applying the leader rule even with faulty information is still a decent strategy, because it still attempts to bring the election towards a better outcome than you expect, given the information you have. Indeed, if you at least get the top two candidates right, then your ballot will still likely be efficient, since you will distinguish between them. This is a fairly low bar to clear.

## Conclusion

In essence, we have two different mindsets for how to approach Approval voting strategically:

1. Optimizing for getting an outcome that is better than or equal to what you expect, which is achieved by the leader rule.
2. Optimizing for getting any outcome that is "acceptable", which is achieved by [the honest ballot](../av-stratproof){:target="_blank"}.

The leader rule can seem selfish and ruthless. But it, in my view, effectively counters a number of criticisms leveled against Approval voting. Voting strategically really is not that complicated, and involves only identifying the top two frontrunners.

Bullet voting *can be prudent* for voters who like the frontrunners, but voters who most prefer someone nonviable are incentivized to be more generous. This is something voters in St. Louis already intuitively understand<d-cite key="sargent2025stlouis"></d-cite>. The leader rule cuts through the noise and ambiguity with a clean and simple heuristic that is easy to understand and apply.

Strategy, I argue, is not a bug of Approval voting, but rather a feature that can lead to more majoritarian outcomes. The paradox here is striking: by acting strategically with imperfect information, voters do not degrade, but actually improve the electoral outcome. Underlooked consensus options accumulate support, and paper tigers with thin support get toppled.

Individual self-interest, when channeled through the leader rule, naturally aligns with the collective good. This suggests that Approval voting, far from being a naive or vulnerable method, is remarkably robust to human behavior. The leader rule shows us that even (or especially) when voters are savvy enough to think strategically, Approval naturally produces outcomes that the electorate, as a whole, prefers. That is a [system worth taking seriously](../approval-only){:target="_blank"}.

## Appendix

For the interested reader, I have included more technical details about the mathematical model Laslier uses to justify the leader rule, as well as a pathological example provided by Rob LeGrand of how the leader rule can fail to converge to the Condorcet winner.

### The Florida Tremble

This is an explanation of the actual mathematical model that Laslier uses to justify the leader rule, for those interested in the technical details.

Laslier calls his uncertainty model the "Florida Tremble," after the infamous 2000 US Presidential election in Florida we just discussed, where it's believed that miscounted votes led to a different outcome. By assuming we have "many" voters, and there's a small chance for one of the bubbles on a voter's ballot to be "miscounted" (deleted), there is now a nonzero probability that our vote is decisive in some tie.

We thus want our ballot to act like a lottery ticket for the most likely of these unlikely pivotal scenarios.

Without getting into the weeds of the relative size of near-infinitesimal probabilities, the intuitive idea is actually quite straightforward: in a large election, ties are very, very, very unlikely.

> **Assumption:** In a large election, the most likely event is that your vote does not matter at all. The second most likely event is that your vote is decisive in a tie between the leader and challenger. The most likely pivotal scenario involving any other candidate besides the leader and challenger is that candidate against the leader. <d-footnote>This is actually proved by Laslier in his paper, but we can just treat this as an intuitive assumption.</d-footnote>

Since it's not particularly helpful to assume our vote is meaningless, we determine our strategy by the most likely pivotal scenarios involving each candidate. The most important being between the leader and challenger. Therefore, we always approve exactly one of the two, depending on which one we prefer.

Laslier proves that the most likely pivotal scenario involving any non-leader candidate is still that candidate against the leader (and the leader with the challenger). Essentially, for any other "unlikely" candidate (even including the challenger) to possibly tie for first place, we would need all other candidates who got more votes than Mr. Unlikely (which includes at least the leader) to lose enough votes to get the same or fewer votes than Mr. Unlikely<d-footnote>Laslier spends considerable time discussing the probability of three-way ties, which we will completely ignore here.</d-footnote>.

For example, think about the candidate in fourth place. For them to tie for first place, we would need the top 3 candidates to all lose enough votes to make 4th place relevant. The one candidate they're most likely to tie with is the leader, since for it to be anyone else, the leader would have to lose way more votes than, say, the second place candidate. It would require *way more* votes to be miscounted, so the leader comparison is most relevant.

Thus, we compare these unlikely candidates to the leader. This tells us our optimal lottery ticket of a ballot--in regard to candidates who are not the leader--is to approve of all candidates we strictly prefer to the leader, and not approve of any candidates we prefer less than the leader.

However, rather than assume the result is fixed, and variations in results are from *ballot errors*, I think it's more intuitive to loosely treat the leader as just an "expected winner" based on the information we have, and the challenger as the most likely candidate to overtake the leader, with uncertainty based on things like polling error or turnout.

### The LeGrand Pathology

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

For example, if $A$ is the leader, and $B$ is the challenger, then

- $A$ will get 48 approvals, from the 48 voters who prefer $A$ to $B$.
- $C$ will similarly get 66 approvals, from the 66 voters who prefer $C$ to $A$.
- $B$ will get 52 approvals, from the 52 voters who prefer $B$ to $A$.
- $D$ will get 27 approvals, from the 27 voters who prefer $D$ to $A$.

Hence, in this case, $C$ becomes the new leader, and $B$ stays the challenger. We can denote this as a transition from the state (leader, challenger) = $(A, B)$ to the state $(C, B)$.

If $B$ is the leader, then after an iteration of the leader rule $C$ will be the new challenger. The approvals at the equilibrium state $(B, C)$ are as follows:

| Candidate | Relevant Matchup | Approvals |
|-----------|------------------|-----------|
| $B$       | $B > C$          | 51        |
| $C$       | $C > B$          | 49        |
| $A$       | $A > B$          | 48        |
| $D$       | $D > B$          | 44        |

We see, $B$ remains the leader and wins. This is an equilibrium, since the leader and challenger are the same as the initial leader and challenger, so no voter has an incentive to change their vote. That is, $(B, X)\to (B, C)$ for any $X$ and $(B, C) \to (B, C)$.

However, if any other candidate starts as the leader, then consider what happens to $B$ and the other candidates:

- $B$ will always get over 50% approvals, since $B$ beats every other candidate in a head-to-head matchup.
- But there is some other candidate who beats the leader in a head-to-head matchup by 60% or more, so some other candidate will always get more approvals than $B$ and become the new leader instead of $B$.

For example, we saw that if $A$ starts as the leader, then $C$ can become the new leader, because $C$ has a strong head-to-head win against $A$. The cycle of leaders and challengers is as follows:

$$(A, B) \to (C, B) \to (D, B) \to (A, B) \to \dots$$

When no Condorcet winner exists (meaning there is a cycle in the pairwise matchups), then the leader rule will have a cycle in "states" of leader and challenger pairs. But this example shows that a cycle can also occur when there is a Condorcet winner and equilibrium. I'd like to eventually publish a post about the dynamical system induced by en masse application of the leader rule.

The structure of this pathology is specifically that $B$ is a milquetoast Condorcet winner, who only wins by very narrow margins, while the other candidates have a volatile cyclic relationship with each other. It should be noted, however, that from the perspective of the electorate, if the election has an outcome at one of these cyclic nodes, then all we would see is a major upset. The expected leader would have a pitiful performance, their strongest challenger would get over 60% of the vote, and $B$ would get over 50%.

From one perspective, this is actually a harmonious outcome, where multiple candidates get majority support, and the candidate who is preferred by a majority over whoever was expected to win, takes office instead. That is, the outcome under the leader rule is still better than expected by a strong majority of voters, even if there was non-convergence that would be invisible to voters.
