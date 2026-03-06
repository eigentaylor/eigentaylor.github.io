---
layout: distill
title: A Guide to Approval Voting Strategy
date: 2026-03-04
description: An explanation of "the leader rule" strategy in approval voting, and its positive ramifications.
giscus_comments: true
importance: 2
tags: voting
category: polisci
featured: false
related_posts: true
pretty_table: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: The Leader Rule
    subsections:
      - name: An Example of Application
      - name: Applying the Leader Rule to Alaska 2022
      - name: Other Alaska Possibilities
  - name: The Florida Tremble
  - name: Consistency with Practical Voter Psychology
  - name: Condorcet-efficiency of the Leader Rule
  - name: What if my information is faulty?
    subsections:
      - name: The Power of the Honest Ballot
  - name: Conclusion
  - name: Appendix 
    subsections:
      - name: The Descending Chain of Unlikely Ties
  - name: References
---

## Introduction

> Approval voting is a voting method where each voter can "approve" of as many candidates as they like, and the candidate with the most approvals wins.

This post is based on a paper by [Jean-François Laslier](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}, which introduces the leader rule and analyzes its properties. I would like to give a special thanks to Rob LeGrand for bringing this strategy to my attention. LeGrand, as far as we know, came up with this strategy back in 2002, and Laslier discovered it independently and published about it in his 2009 paper. I find this interesting to bring up, because it shows that this strategy is not just some random "someone just thought of it" strategy, but rather something natural, intuitive, and fundamentally optimal that multiple people have independently discovered.

In a [previous post](../avstratproof){:target="_blank"}, I gave an example to show that Approval voting is not technically strategyproof, but can be made so under a particular mindset that I called a "Dichotomous Goal". I explained how strategy simplifies down into drawing a line of acceptability, and once that line is set then the choice for how to vote is clear. In this post, we will explore a specific strategy called "the leader rule," which is a practical and effective way to help draw that line of acceptability optimally based on the perceived front-runners.

A common complaint I have heard about Approval voting is that, while it incentivizes voters to approve all candidates they truly like, it might result in regret if voters choose to approve the candidates they are lukewarm about, but are strongly better than the candidates that they truly hate. What happens when a voter votes for a candidate they only voted for out of fear of the worst, and that candidate ends up winning? Sure, I can vote for my favorite, and won't vote for my least favorite, but what do I do about the candidate in the middle?

The leader rule is a strategy that helps mitigate this concern by focusing the voter's approval on the most relevant candidates in the election: the front-runners.

Three common criticisms (I might call "myths") of Approval voting I hear are that

1. It encourages "bullet voting" and is susceptible to strategic voting.
2. It can be confusing for voters to decide which candidates to approve. By approving too many candidates, they risk electing a candidate they dislike and hurt their preferred candidate's chances.
3. It can violate majority rule, and fail to elect the Condorcet winner (the candidate who a majority prefer to any other alternative), when one exists.

The key insights I want to convey in this post are that

1. Bullet voting is not some sort of failure of Approval voting, it is a natural and optimal strategy in many cases.
2. Approval voting has the utmost incentive for sincerity. In practice, you should always vote "sincerely" (never leave "holes" in your ballot). The only question is where to draw the line of acceptability (i.e. how many candidates to vote for sincerely). We will see that one of the most psychologically natural ways to do so, whilst minimizing regret, is consistent with the leader rule.
3. Approval voting has more majoritarian outcomes, **including electing the ranked Condorcet winner**, *precisely when* voters are **strategic**. That is, strategy is not some Achilles heel of Approval voting, it is the one of the mechanisms by which Approval voting achieves optimal outcomes.

## The Leader Rule

First, we should establish that this strategy is not about impacting the "share" or percentage of votes that a candidate gets, but rather about impacting who wins. The goal under the leader rule is to maximize the chance that a more preferred candidate wins over a less preferred candidate, not to maximize number of votes one candidate gets over another. This is a subtle but important distinction, and it is the key to understanding the strategy.

> **The Leader Rule**: Identify the top two front-runners in the election: the "leader" (most likely to win) and the "challenger" (the most likely to overtake the leader). You, as the voter, then
>
> 1. approve all candidates that you prefer strictly to the leader
> 2. only approve the leader if you prefer them to the challenger.
> 3. Do not approve of any other candidates (i.e. those you like less than the leader).

For example, suppose I prefer A > B > C > D, and the leader is C and the challenger is B. Then, I first approve everyone I prefer to the leader, which is A and B. Then, I only approve of the leader C if I prefer them to the challenger B, but since I prefer B to C, I do not approve of C. Finally, I do not approve of D, since they are less preferred than the leader. Thus, I would approve of A and B, and not approve of C and D.

That's the entire strategy! You could stop reading here and go apply this strategy in any Approval voting election. But if you want to understand *why* this strategy is optimal, how to apply it in real examples, and you're here for the practical examples and theory, read on.

The first observation here is that this strategy is "sincere", which we should formally define as follows:

> **Sincerity**: An approval vote is **sincere** if for any candidate you *do* vote for, you also approve all candidates you strictly prefer to them. That is, you do not leave any "holes" in your ballot between candidates you voted for. Alternatively, a sincere ballot is one where you draw a "line of acceptability" somewhere in your ranking, and approve everyone above that line.

For example, if I prefer A > B > C > D, then voting for A and C would be insincere, because I left a hole between A and C by not voting for B. Some people really don't like the term "sincere", as it implies there are multiple "sincere" ballots, but this is the terminology used by [Approval voting theorists](https://doi.org/10.2307/1955105){:target="_blank"}. We distinguish between the idea of an "honest ballot" (the approval ballot most truly consistent with the voter's inherent sense of acceptability towards the candidates) and one of many "sincere" ballots, which are consistent with some projection of the voter's nuanced ranking down to any "line of acceptability".

The leader rule says leaving a hole in your ballot is *never* optimal, in practice. You should always draw that line of acceptability right below the leader or right above (depending on how you feel about the most important race between the leader and challenger).

The basic idea is

1. to maximize the impact of your vote on the most likely pivotal outcomes of the election
2. vote in a way that promotes precisely better than expected outcomes

- By approving of all candidates you prefer to the leader, you strictly increase the chances of a more preferred candidate winning. Even if they have no chance, you still strictly help them overtake or maximize the distance between them and everyone you didn't approve. It's a "what the hell" vote that can't hurt you. Who knows, maybe other voters find them more appealing than the leader, like you, and when you all approve of them, they get a boost that helps them overtake the leader!
- If you prefer the challenger to the leader, then you approve of the challenger since you prefer them to the leader, and do not approve of the leader.
- If you prefer the leader to the challenger, you approve of the leader by the rule. And since the challenger is below the leader, you do not approve of the challenger.
- For anyone you prefer less than the leader, you do not approve of them, and that has the effect of your vote hurting everyone worse than the outcome you're already expecting.

The ultimate effect is that you have an impact on the most important race: between the leader and the challenger. You also help push forward any candidates you prefer to the leader. This has the effect of "bringing up" the election towards an outcome better than or equal to what you expect to be the most likely outcome (the leader winning). You then contribute to the best possible outcome, from your perspective.

### An Example of Application

I was recently talking to someone in the electoral reform space. They mentioned that they would be conflicted about how to vote under Approval voting in the 2012 US Presidential election. They said that they preferred Gary Johnson > Mitt Romney > Barack Obama, and thus voted for Romney under plurality. But there's ambiguity in Approval over how they should vote, if they actually want to vote for a winning candidate. Here was a loose summary of their thought process:

- Only voting for Johnson was a long shot, and so there's regret in not influencing the most important race.
- Voting for Johnson and Romney could lead to mixed success. If Romney loses, they would be disappointed that nobody they voted for won. But if Romney wins, then why not have just voted for Romney?
- Voting insincerely for Johnson and Obama could be technically a "success" if Obama wins, but it would be a betrayal of their preferences, which does not feel good.
- Voting for Romney and Obama would mean they "can't lose", but that wouldn't be honest either.
- Voting for all three would mean their ballot is basically pointless.

The leader rule cuts through all of this ambiguity and says that their optimal strategy, in any reasonable scenario (where we assume Romney and Obama are the two front-runners), is to vote for both Johnson and Romney. Here's why:

1. Johnson is a long shot, yes, but there's absolutely no reason *not* to approve of him. Approving of him can't hurt, and it could help. If they approve of him, and other voters who prefer him also approve of him, then he could get a boost that helps him overtake the leader leading to a "come from behind" victory. Regardless of who the leader is out of Romney and Obama, they prefer Johnson to the leader, so they should approve of him.
2. Obama versus Romney is the most important race. Therefore, they should always approve of exactly one of them, and never approve of both (or neither), if they want to maximize their impact. This means approving of Romney and not approving of Obama.

The original hesitation from this strategy was fear that they would be disappointed if neither of their chosen candidates won. But we can see this is effectively the best possible ballot this voter could cast. No other ballot would have a better chance of electing a more preferred candidate. And they can stand firm knowing they voted in a way that maximizes their chances of success, in a sincere way that reflects their preferences. Though Obama, their least favorite, would have likely won, they can take solace in the fact that they didn't have to agonize over *which* single other candidate to vote for instead. Rather, they could vote for everyone they find better than Obama, and know they did the best they could, and that their voice was heard.

### Applying the Leader Rule to Alaska 2022

Let's also take my favorite election to discuss: Alaska 2022 (it wouldn't be an eigentaylor post about voting if we didn't mention Alaska 2022). In this election, we had the following candidates and first round totals:

| Candidate       | Party | First Round Percent | Final Round Percent |
|-----------------|-------|---------------------|---------------------|
| Mary Peltola    | D     | ~40%                | ~47% (Winner)       |
| Sarah Palin     | R     | ~31%                | ~45%                |
| Nick Begich III | R     | ~28% (Eliminated)   | Eliminated          |

In this election under IRV, Peltola won after Begich was eliminated, despite most of his votes transferring to Palin. Further, this election was controversial partially because the ballot data showed that Begich was actually the Condorcet winner, meaning that he would have beaten both Peltola and Palin in a one-on-one race, but was eliminated first under IRV. Further, there was anger that despite nearly 60% of voters ranking a Republican candidate first, the Democrat won.

I want to go through how different voters might apply the leader rule in this election. In this race, the front-runner was Peltola (~40%), with Palin as the primary challenger (~31%). Begich was a relatively close third at (~28%). The most common voter types were:

- Palin > Begich > Peltola
- Begich > Palin > Peltola
- Begich > Peltola > Palin
- Peltola > Begich > Palin

Let's see how each of these voter types would apply the leader rule assuming Peltola is the leader and Palin is the challenger:

| Voter Type               | Approved Candidates (Peltola leader, Palin challenger)  |
|--------------------------|---------------------------------------------------------|
| Palin > Begich > Peltola | Palin, Begich                                           |
| Begich > Palin > Peltola | Begich, Palin                                           |
| Begich > Peltola > Palin | Begich, Peltola                                         |
| Peltola > Begich > Palin | Peltola                                                 |

These four groups show us the way that different voter groups might optimally utilize the nature of the Approval ballot to maximize their impact on the election.

- The Republican voters who rank Peltola last (under both Republicans) approve of both Republicans, showing how the Republican voters can unite behind both candidates against the Democrat. Despite Begich not being in the top two, even voters who rank him second still approve him. Together, these voters form a coalition that essentially acts as a single vote *against* Peltola.
- The Begich > Peltola > Palin voters approve of Begich and Peltola. They prefer Begich the most, so there's no harm in approving him. They also prefer Peltola over the challenger Palin, so voting for Peltola as well helps maintain her lead over Palin, this bloc's least preferred candidate.
- The Peltola > Begich > Palin voters only approve of Peltola, as she is both their most preferred candidate and the leader. Since Peltola is already the front-runner, it's not optimal for them to extend their approval to Begich, who is less preferred than Peltola.

The leader rule thus encourages voters to focus their approvals on the candidates that matter most in the election, helping to ensure that their votes have the maximum possible impact on the outcome. But notice something interesting: all blocs except the ones that rank Peltola first end up extending their approval to Begich, since they prefer Begich to Peltola.

For the Democratic voters who view Begich as a lesser evil compared to Palin (ex. Peltola > Begich > Palin voters), let us consider the strategy suggested by the leader rule in the different possible scenarios:

| Leader  | Challenger | Approved Candidates (Peltola > Begich > Palin) |
|---------|------------|------------------------------------------------|
| Peltola | Begich     | Peltola                                        |
| Peltola | Palin      | Peltola                                        |
| Begich  | Peltola    | Peltola                                        |
| Begich  | Palin      | Peltola, Begich                                |
| Palin   | Peltola    | Peltola, Begich                                |
| Palin   | Begich     | Peltola, Begich                                |

The only situations where they would approve of Begich is if

1. Begich is the leader and Palin is the challenger (in which case, they should approve Peltola and Begich to help push Palin down). That is, Peltola does not seem likely to win.
2. Palin is the leader (in which case, they should approve Peltola and Begich to help push Palin down). Even if Peltola is in second place.

In other words, if Peltola is not in the top two, or if their least preferred candidate Palin is the leader, then they approve of Begich. In every other case, they do not approve of Begich. This includes when Peltola is ahead, and most likely to win, or if Begich is the leader but Peltola is the challenger, in which case they withhold their approval from Begich to help minimize the distance between Peltola and Begich, maximizing Peltola's chances of winning.

We see that extending approval to that second least preferred candidate is optimal only when

1. Your two least preferred candidates are the front-runners, and you want to help the lesser evil win over the worse evil, or
2. Your least favorite candidate is the leader. Regardless of if your most preferred candidate is the challenger or not, you want to help push the leader down by approving every candidate over them.

The leader rule thus provides a clear and effective strategy for voters to maximize their impact in Approval voting elections, by focusing their approvals on the most relevant candidates and helping to ensure that their votes have the maximum possible impact on the outcome.

In [a future post](../leader-dynamics){:target="_blank"}, I analyze Alaska 2022 using the leader rule, and I found something interesting. Under certain assumptions, Begich is the only candidate who could possibly win if every voter applies the leader rule. This basically comes down to the fact that Begich is the Condorcet winner, and his match-ups against the other candidates are the strongest ones. Therefore, in response to any other leader, a majority would approve of Begich because they prefer him to any other leader. Further, the data also indicates that Palin, as the Condorcet loser, could never win under the leader rule.

The question is if Democratic voters might "regret" also approving Begich in the case where their support of Begich is what pushes him to victory. I argue no. Suppose that Palin is the leader the morning of the election. Regardless of who the challenger is, if the Peltola supporters go into the voting booth expecting Palin to win, they will vote defensively for Peltola and Begich in response to that expectation. My analysis indicates that Palin would get less than 50%, Peltola would get a meek majority of ballots, but Begich would get potentially over 60% of ballots, which would be a landslide victory. See [this post](../leader-dynamics){:target="_blank"} for my evidence of this claim when it comes out.

From their perspective, they went into the booth expecting their least favorite candidate, and then in a complete upset, their top two candidates win a majority of ballots, and their least favorite is in last place. Begich, their second favorite, winning is certainly a more preferable outcome than Palin. Further, it is hard to regret your vote as an individual when the difference between Peltola and Begich is so significant.

In the other case where they should vote for Begich, which is when Begich is the leader but Palin is the challenger, then Democratic voters go into the booth not even expecting their candidate to make it into the top two. In that case, they should still approve Peltola, but they should also vote for Begich, because reinforcing Begich's lead over Palin is the best way to prevent Palin from winning. That is, reinforcing against a worse outcome. The result of that strategy would likely be less of a landslide. My analysis indicates that Begich would win with over 50% and Peltola would be in second place with slightly under 50%.

### Other Alaska Possibilities

I gave the table for the four most common voter types in Alaska 2022 with the assumption based on the plurality results that Peltola was the leader and Palin was the challenger. However, given Palin's lack of broad appeal, and Condorcet loser status, it seems more likely that the leaders and challengers would actually be Peltola and Begich. Let's see how the leader rule would apply in these cases:

| Voter Type               | Peltola Leader (Begich Challenger) | Begich Leader (Peltola Challenger) |
|--------------------------|------------------------------------|------------------------------------|
| Palin > Begich > Peltola | Palin, Begich                      | Palin, Begich                      |
| Begich > Palin > Peltola | Begich, Palin                      | Begich                            |
| Begich > Peltola > Palin | Begich                             | Begich                      |
| Peltola > Begich > Palin | Peltola                           | Peltola |
| Palin > Peltola > Begich | Palin, Peltola                   | Palin, Peltola                    |
| Peltola > Palin > Begich | Peltola                           | Peltola, Palin                    |

In these two scenarios, we see that

- Palin-first voters always approve of their top two candidates, since she is assumed to be nonviable.
- Begich-first voters approve of Begich, but they split based on if they prefer Palin or Peltola second. For those who prefer Palin second, they only approve Palin if Begich is not the leader. If they prefer Peltola second, they always approve Begich only.
- Peltola-first voters always approve of Peltola, but they split based on if they prefer Palin or Begich second. For those who prefer Begich second, they never approve of Begich. For those who prefer Palin second, they approve of Palin only if Peltola is not the leader.

## The Florida Tremble

In a large election, the chance that your vote is decisive is essentially zero. Therefore, in a purely deterministic, perfect knowledge model of elections, strategy has basically no impact. To get around this, Laslier introduces an element of uncertainty to allow for strategy to actually have an impact. He calls this the "Florida Tremble," after the infamous 2000 US Presidential election in Florida, where it's believed that miscounted votes led to a different outcome. By assuming we have "many" voters, and there's a small chance for one of the bubbles on a voter's ballot to be "miscounted", we allow for strategic voting to have a non-zero expected impact on the outcome.

Without getting into the weeds of infinitesimal probabilities, and the effect of a "large electorate", the intuitive idea is actually quite straightforward: in a large election, ties are very, very, very unlikely. However, there are two observations to make:

1. If some votes are miscounted due to machine errors, then essentially any election, could be technically tied by some number of miscounted votes. The chance that your vote is decisive now becomes non-zero (though, still absurdly small).
2. Some ties are more unlikely than others. Laslier's rule essentially focuses on the most likely ties, which uniquely determine an optimal strategy.

Based on these two observations, Laslier's leader rule basically treats the voter's ballot as a lottery ticket. You fill it out in a way that maximizes the positive impact in the most likely pivotal scenarios (the ones where your vote could be decisive). The key insight about Approval voting is that by being able to cast multiple approvals, you can view your ballot as a lottery ticket which gives you the win in both the Powerball and Mega Millions at the same time. But you do so by prioritizing whichever lottery is more likely to pay off.

Unlike a Condorcet method, where your ranked ballot is a single lottery ticket that impacts every possible head-to-head match-up, Approval voting sacrifices some of that influence in exchange for simplicity and practicality (while [maintaining the same quality of outcomes](../practicalapproval){:target="_blank"}). With approval, the choice in one race can contradict the choice in another.

For example, if you approve of only your most preferred candidate, you cast a lottery ticket that only pays off if the pivotal scenario is between your most preferred candidate and someone else. If the most likely pivotal scenario is between your second most preferred candidate and your least preferred candidate, then your lottery ticket is a dud in the most likely scenario where it could have made a difference. If you choose to approve your top two candidates, your lottery ticket pays off if the pivotal scenario is between either of your top two candidates and any other candidate. However, if the most likely pivotal scenario is between your top two candidates, then your lottery ticket is a dud again in that most likely scenario, because you didn't impact that race. You preserved the margin between your top two candidates, instead of helping your most preferred candidate win over the second most preferred candidate.

The leader rule simplifies all of these considerations by making the reasonable assumption that

1. The most likely pivotal scenario is between the leader and the challenger
2. The most likely pivotal scenarios involving any other candidate besides the leader and challenger is still that candidate against the leader.

I give a full [explanation of this in the appendix](#appendix), but using this assumption to rank the pivotal scenarios by their likelihood, we can derive the leader rule as the optimal strategy for maximizing the chance of a more preferred candidate winning over a less preferred candidate. However, the intuition is that:

1. Because the most likely pivotal scenario is between the leader and challenger, you should approve of exactly one of them, and that should be the one you prefer more.
2. Because the most likely pivotal scenarios involving any other candidate is between that candidate and the leader, you should approve of all candidates you prefer to the leader, and no candidates you prefer less than the leader.

By noting that the first point is the most important one, we prioritize our lottery ticket to pay off in the most likely pivotal scenarios.

## Consistency with Practical Voter Psychology

In Laslier's paper, he makes two key observations about voter psychology that make the leader rule particularly appealing:

1. Voters consider pivotal scenarios sequentially, starting with the most likely scenarios. This means that they focus on the most probable outcomes first, and make their decisions based on those scenarios.
2. The leader rule corresponds to Tversky's "elimination by aspects" model of decision-making. People tend to eliminate options that do not meet certain ranked criteria.

The leader rule boils down to ranking the pivotal scenarios by their likelihood, and making decisions based on how their internal preferences align with those scenarios.

The most likely pivotal scenario is the leader vs. the challenger. Therefore, the voter focuses on approving exactly one of these two candidates based on their preference. The next most likely scenarios involve the leader vs. other candidates, leading the voter to approve all candidates they prefer to the leader.

However, from another perspective, the leader rule can also be intuitively (but loosely) understood as voting for a strictly better than the expected outcome. The expected outcome is the leader winning. Therefore, you want to vote in a way that promotes any outcome that is better than the leader winning, and does not promote any outcome that is worse than the leader winning. Thus, you approve of all candidates you prefer to the leader, and none of the candidates you prefer less than the leader. The decision for the leader comes down to considering that the next expected outcome is the challenger winning, so you approve of the leader if you prefer them to the challenger.

Therefore, the leader rule aligns well with the "mental shortcuts" that voters naturally use when making decisions. It provides a clear and straightforward strategy that maximizes the voter's impact on the election outcome, while also being consistent with how people typically think about choices.

In my view, however, the most surprising aspect of the leader rule is its majoritarian properties, which we will explore next.

## Condorcet-efficiency of the Leader Rule

One might ask "what happens if everyone uses the leader rule, all at once?" Laslier analyzes this in his paper, and [I tackle this question in more depth in a future post](../leader-dynamics){:target="_blank"}, but the short answer is that

1. First, we have to assume that all voters have the same common perception of the leader and challenger.
2. The leader rule only has one unique equilibrium when there exists a unique Condorcet winner, and the leader is that Condorcet winner. If the leader is not a unique Condorcet winner, then a new candidate (who beats the leader head-to-head) will get more approvals than the current leader, and overtake them.
3. If there is no unique Condorcet winner, then there is no equilibrium under the leader rule.
4. After any iteration of everyone using the leader rule, if a unique Condorcet winner exists, they will have over 50% approvals.

However, credit to Rob LeGrand for pointing out to me that it is not necessarily the case that the leader rule converges to the Condorcet winner under all initial conditions. See [my forthcoming post](../leader-dynamics){:target="_blank"} for a pathological (but intriguing) example of this.

The proof and explanation of these ideas is actually relatively straightforward. Consider what happens when everyone uses the leader rule at the same time:

- For any candidate X who is not the leader, the voters who approve them will be precisely those who rank X above the leader. Therefore, X's total approval percentage will be equal to the percentage of voters who prefer X to the leader. That is, the head-to-head result of X vs. the leader.
- The leader's approval percentage will be equal to the percentage of voters who prefer the leader to the challenger (since only those voters approve the leader). Thus, the leader's approval percentage is equal to the head-to-head result of the leader vs. the challenger.

This means that after an iteration of every voter using the leader rule, the approval percentages precisely equal head-to-head percentages.

Thus, if the leader is a unique Condorcet winner, then after the iteration they will have over 50% approvals, and everyone else will have under 50% approvals. Therefore, the leader remains the leader, and must strictly win. The equilibrium challenger will be the candidate with the least bad head-to-head result against the leader.

In conjunction with the previous section, what we see is that the way approval voting reacts with the way humans make decisions leads to a natural majoritarian outcome when everyone uses the leader rule. In that way, Approval voting is more majoritarian when voters are strategic, which significantly dampens the common criticism that Approval voting is both non-majoritarian and susceptible to strategic voting. In particular, if every voter applies the leader rule, then the outcome is the same or strictly better than the expectation of the voters going into the election.

## What if my information is faulty?

The fundamental assumption of the leader rule is that voters have some information on who the front-runners are, and thus can identify the leader and challenger. But, chances are, you maybe don't have the most detailed polls and news coverage of the school board election you're voting in. Or maybe you do, but the polls aren't exactly Nate Silver-level accurate. What if your information is wrong? What if you misidentify the leader and challenger? What if there are three or four candidates who all seem viable, and you can't identify the leader and challenger at all?

When information is sparse or untrustworthy, the leader rule loses some of its global optimality guarantees. However, I think once we get into the weeds of uncertainty, this is where recognizing the safety of casting an "honest ballot" in Approval voting becomes particularly useful. The truth is that Approval is a very "safe" voting method for the voter, because it's strongly "monotonic" (more support for a candidate cannot hurt their chances of winning) and consistent with its ballot data. When in doubt, voting sincerely, according to your gut feeling of where the line of approval should be, is a very safe strategy.

Laslier does prove that a sincere strategy is generally always optimal under Approval voting, in practice with a large electorate, at least. That is, you should always draw a line of acceptability somewhere. The strategy creeps in when there's pressure to adjust from that "gut" line to something else. The primary risks you are balancing when you adjust that line are:

1. Your approval line is too strict. If you, for example, only approve of Palin, then you risk failing to help Begich win over Peltola, which could lead to Peltola winning. That is, you risk failing to be decisive in the Begich vs. Peltola race.
2. Your approval line is too generous. If you, perhaps, approve of Palin and Begich, you might fail to help Palin win over Begich, which could lead to Begich winning. That is, you risk failing to be decisive in the Palin vs. Begich race.

The leader rule is precisely the optimized balance of these two risks, by essentially working under the assumption of which races seem most likely to be pivotal. Withholding approval from Begich because you're focused on the Palin vs. Begich race when Peltola is the leader is a mistake because it's far more likely that the pivotal race will involve Peltola than not.

It's important to contextualize the assumptions of the leader rule. To apply it, we are assuming that the leader is truly the most likely candidate to win. We assume that we walk into the voting booth, cast our vote, and almost surely the leader wins and our vote was a drop in the bucket. But, *just in case*, our vote might just be a lottery ticket which breaks a tie favorably.

Suppose the favorite to win is also your favorite candidate. The leader rule says to bullet vote to preserve their lead. But what happens if the results come back and your favorite is in last place, your least favorite won, and your second favorite was a close second? If you genuinely liked your second favorite, then perhaps you'll regret not voting "honestly" for both and hedging your bets. And, when you're not particularly trusting of the polls, then honesty might just be the best policy.

But, from another perspective, the reality is that the electorate saw your favorite was likely to win, and overwhelmingly voted for everyone else. That's the system converging to the secret consensus candidate that was hidden under low quality polling. And no strategy can save an unacceptable candidate from losing to a much more broadly supported one.

However, it's worth emphasizing that upsets *do* happen. In fact, the leader rule actually makes them more likely when the perceived leader is actually a weak candidate. If a majority of voters preferred someone else to the candidate everyone expects to win, then it's certainly not unreasonable for that someone else to pull off an upset victory when that majority is freed to vote for multiple candidates. In my [future post](../leader-dynamics){:target="_blank"}, I explore this in detail, and explain how the leader rule, when used en masse, tends to lead to a more majoritarian-preferred outcome than whatever voters expect going into the voting booth.

But when you have no idea who the leader and challenger are, then it's very hard to know which races are the most likely to be pivotal. In that case, you might as well just draw your line of approval based on your gut feeling of who you *actually approve* of, and not worry about the strategic implications of your vote. Let's call this the "honest ballot", which is a particular choice of a sincere ballot that is based on your gut feeling of who is acceptable to you, and who is not.

### The Power of the Honest Ballot

When you choose an "honest ballot", you optimize away from getting the *most* **preferred** candidate possible, and instead optimize on getting *any* **acceptable** candidate. For some, like myself, this is just as good. [As long as an acceptable candidate wins, I don't really care so much about which one wins](../avstratproof){:target="_blank"}. But I understand this is not a universal experience.

An "honest ballot" optimally impacts the share and margin between candidates, in a way that the Leader rule fails to do. An honest ballot strictly increases the gap between all candidates you approve of, and all candidates you do not approve of. It is an honest signal of your true preferences, and your voice *will* be heard in the election results *directly* through the approval percentages.

Think of it this way: suppose you are a Republican in Alaska who prefers Palin > Begich > Peltola, but it seems like all three candidates are viable. What exactly does your ballot do when you vote for Palin and Begich?

Well, obviously, it gives Palin and Begich two votes. But we already knew that. However, think of it in terms of the margins between the candidates. By approving of Palin and Begich, you

1. Increase the margin between Palin and Peltola, which helps Palin win over Peltola.
2. Increase the margin between Begich and Peltola, which helps Begich win over Peltola.
3. Preserve the margin between Palin and Begich, which does not affect the relative chances of Palin and Begich winning over each other.

Therefore, your ballot is strictly hurting Peltola, and is strictly helping both Palin and Begich. It is not hurting Palin relative to Begich, but it is helping both of them relative to Peltola.

By approving only Palin, you either strengthen her lead or narrow the gap between her and everyone else. By extending approval to Begich, you don't narrow the gap between Palin and Begich anymore, but you do widen the gap between Peltola and Begich (i.e. Peltola and everyone else). The one that feels more "honest" to you is the one that is more optimal in achieving an acceptable outcome. This is the key piece of information that ordinal voting methods fail to capture. Palin voters who approve of Begich are distinct from Palin voters who do not approve of Begich, but still prefer Begich to Peltola.

This may seem obvious, but this is not the case in other voting methods. For example, in Ranked-Choice voting, the Republican voters who sincerely ranked Palin first and Begich second did not help get a Republican elected. In fact, they actually elected Peltola, their least preferred candidate indirectly. If [less than 3,000 of the approximately 33,000 voters who did so](https://substack.com/@whelmedcitizen/p-182659376){:target="_blank"}, had instead insincerely ranked Begich first and Palin second, then Palin would have been eliminated instead and Begich would have won, which is a much more preferable outcome for those voters. Approval has no such pathologies. Your ballot can only ever help elect someone you consciously vote for, and will *never* help someone you did *not* vote for.

In short: the leader rule optimally pushes the election towards a more **preferable** outcome, but the honest ballot strictly and optimally pushes the election towards an **acceptable** outcome.

Therefore, even when you have no idea who the leader and challenger are, you can still vote sincerely based on your gut feeling of who is acceptable to you, and know that you are playing optimally in the sense that you are maximizing the chance of electing an acceptable candidate.

## Conclusion

In essence, we have two different mindsets for how to approach Approval voting strategically:

1. Optimizing for getting an outcome that is better than what you expect, which is achieved by the leader rule.
2. Optimizing for getting an outcome that is acceptable, which is achieved by the honest ballot.

## Appendix

The following is my attempt at an intuitive explanation of the mathematical proof of why the leader rule is optimal under the Florida Tremble model. The actual proof is more rigorous and formal, but I want to give a more intuitive explanation of the key ideas.

### The Descending Chain of Unlikely Ties

We imagine that we have a front-runner $$x_1$$, who we call the leader, and a challenger $$x_2$$. The challenger is the most likely candidate to beat the leader (ex. the most likely candidate for the leader to tie or lose to). We imagine that every other candidate $$x_3, x_4, \ldots$$ is less likely to beat the leader than the challenger is.

However, let's keep it concrete with a recent example: the 2025 NYC Mayoral Democratic Primary. In that race, Andrew Cuomo was seen as the clear front-runner (leader), and the challenger was Zohran Mamdani (who ended up winning in an upset victory). We also have other candidates like Brad Lander, Adrienne Adams, and others. Let's assume that the order is based on their first choice vote shares in the actual election. That gives the ordering $$x_1 = \text{Cuomo}$$, $$x_2 = \text{Mamdani}$$, $$x_3 = \text{Lander}$$, $$x_4 = \text{Adams}$$, etc. all the way down to the last place candidates like Paperboy Love Prince.

We then have the following events in decreasing order of likelihood (by ignoring three or more way ties), assuming our identification of the leader and challenger is correct:

1. Most likely: Cuomo wins by more than 1 vote over Mamdani. In this case, technically your vote has no effect, so it doesn't matter what you do.
2. Next most likely (but far less likely): Cuomo ties with Mamdani. In this case, your vote could be decisive in determining the winner between these two candidates. Therefore, you should vote for one and only one of these candidates, depending on which you prefer. If you prefer the leader to the challenger, approve the leader (you strengthen their lead). If you prefer the challenger to the leader, approve the challenger (you help them overtake the leader). This is the most likely lottery you're going to win, so you should prioritize your ballot to be decisive in this one.
3. Far less likely: Cuomo and Lander tie for first place. Say that, perhaps, many voters really like Lander and he surges in votes over Mamdani up to tie with Cuomo. In this case, your vote could be decisive in determining the winner between these two candidates. If you prefer Lander to Cuomo, you should definitely approve Lander to help them overtake Cuomo. If you prefer Cuomo to Lander, then what you chose in the previous step might put you in a pickle. If you are already approving Cuomo, then you're fine, you're approving exactly one between the leader and Lander. But you prefer Mamdani > Cuomo > Lander, meaning you aren't approving Cuomo, then we have to weigh the probabilities. Since it's far more likely that Cuomo and Mamdani tie than Cuomo and Lander do, you should stick with your original choice of approving only Mamdani (not the leader). That's more important than being the decider between Cuomo and Lander, which is far less likely. This is, in effect, like seeing that your ticket for the Powerball would conflict with your ticket for the Mega Millions, so you choose to prioritize the more likely lottery. Similarly, if you prefer Lander > Cuomo > Mamdani, meaning you are approving Cuomo, then you should approve Lander as well, because otherwise you risk helping Cuomo win over Lander. The key is, again, helping Cuomo win over Mamdani would be more important than helping Lander win over Cuomo. Therefore, it simply comes down to **approve Lander if and only if you prefer Lander to Cuomo**.
4. The next most likely (but very, very unlikely): Cuomo and Adams tie for first place. By the same reasoning as before, you should approve Adams if and only if you prefer Adams to Cuomo.
5. etc. etc. until you get to the tie between Cuomo and the last place candidate Paperboy Love Prince. Same logic: approve the last place candidate if and only if you prefer them to Cuomo. But now you have uniquely determined your entire ballot!

One may ask whether or not it's more likely that Cuomo ties with Paperboy Love Prince or that Mamdani ties with Lander. The key is that *both* the Cuomo-Mamdani tie and Cuomo-Lander tie is far more likely than the Mamdani-Lander tie. That is, we should compare each candidate only to the leader. If you happen to draw one candidate in the lottery, it's far more likely that the leader is involved in that lottery than any other candidate. So how the candidate compares to the *leader* is the absolute most important factor in determining whether or not you should approve of them. The leader is the common thread that runs through all of the most likely pivotal scenarios, so your ballot should be designed to maximize your impact in those scenarios, in order of their likelihood.

In summary, your ballot comes down to two rules:

1. Approve every candidate you prefer to the leader $$x_1$$. No matter what. You have nothing to lose by approving them, particularly in the case that they might overtake the leader.
2. Approve the leader $$x_1$$ if and only if you prefer them to the challenger $$x_2$$. This is the most important race, so you should make sure to approve exactly one of these two candidates based on your preference.
3. Do not approve any candidates you prefer less than the leader $$x_1$$. This is because, if you approve of any of them, you risk being the deciding vote that gets them elected over the leader, resulting in a worse outcome for you.

Note that this actually means that your optimal ballot under the leader rule is sincere! It's not optimal to have any "holes" in your approvals. For any candidate you approve, you should also approve all candidates you prefer to them.

## References

- Brams, S. J., & Fishburn, P. C. (1978). Approval Voting. The American Political Science Review, 72(3), 831–847. [https://doi.org/10.2307/1955105](https://doi.org/10.2307/1955105){:target="_blank"}

Laslier, J. F. (2009). The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate. *Journal of Theoretical Politics*, 21(1), 113-136. [https://journals.sagepub.com/doi/10.1177/0951629808097286](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}

Mahlendorf, A. (2026). Fear of Vote Splitting. Substack. [https://substack.com/@whelmedcitizen/p-182659376](https://substack.com/@whelmedcitizen/p-182659376){:target="_blank"}

[ranked.vote](https://ranked.vote){:target="_blank"} Election Reports:

- Alaska House Special Election 2022: [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}
- NYC Democratic Mayoral Primary 2025: [https://ranked.vote/report/us/ny/nyc/2025/07/mayor](https://ranked.vote/report/us/ny/nyc/2025/07/mayor){:target="_blank"}
- Minneapolis City Council Ward 2 2021: [https://ranked.vote/report/us/mn/2021/11/ward-2](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}

[hyperlink](https://www.youtube.com/watch?v=VXZUjn41dbw){:target="_blank"}
