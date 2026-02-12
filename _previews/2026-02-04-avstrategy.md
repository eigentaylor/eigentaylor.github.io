---
layout: distill
title: A Guide to Approval Voting Strategy
date: 2026-02-04
description: An explanation of "the leader rule" strategy in approval voting, and its positive ramifications.
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
    subsections:
      - name: Other Alaska Possibilities
  - name: Contrast to the Dichotomous Goal
  - name: The Florida Tremble
    subsections:
      - name: The Descending Chain of Unlikely Ties
  - name: Consistency with Practical Voter Psychology
  - name: Condorcet-efficiency of the Leader Rule
  - name: Can the leader rule fail?
    subsections:
      - name: Not Following the Leader Rule
  - name: A Practical Simulation 
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

## Introduction

> Approval voting (AV) is a voting method where each voter can "approve" of as many candidates as they like, and the candidate with the most approvals wins.

This post is based on a paper by [Jean-François Laslier](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}, which introduces the leader rule and analyzes its properties. I would like to give a special thanks to Rob LeGrand for bringing this strategy to my attention.

In a [previous post](../avstratproof){:target="_blank"}, I gave an example to show that Approval voting is not technically strategyproof, but can be made so under a particular mindset that I called a "Dichotomous Goal". I explained how strategy simplifies down into drawing a line of acceptability, and once that line is set then the choice for how to vote is clear. In this post, we will explore a specific strategy called "the leader rule," which is a practical and effective way to help draw that line of acceptability optimally.

A common complaint I have heard about Approval voting is that, while it incentivizes voters to approve all candidates they truly like, it might result in regret if voters choose to approve the candidates they are lukewarm about, but are strongly better than the candidates that they truly hate. What happens when a voter votes for a candidate they only voted for out of fear of the worst, and that candidate ends up winning?

The leader rule is a strategy that helps mitigate this concern by focusing the voter's approval on the most relevant candidates in the election: the front-runners.

Three common criticisms (I might call "myths") of Approval voting I hear are that

1. It encourages "bullet voting" and is susceptible to strategic voting.
2. It can be confusing for voters to decide which candidates to approve. By approving too many candidates, they risk electing a candidate they dislike and hurt their preferred candidate's chances.
3. It can violate majority rule, and fail to elect the Condorcet winner (the candidate who a majority prefer to any other alternative), when one exists.

The key insights I want to convey in this post are that

1. Bullet voting is not some sort of failure of Approval voting, it is a natural and optimal strategy in many cases.
2. Approval voting has the utmost incentive for sincerity. In practice, you should always vote sincerely. The only question is where to draw the line of acceptability (i.e. how many candidates to vote for sincerely). We will see that one of the most psychologically natural ways to do so, whilst minimizing regret, is consistent with the leader rule.
3. Approval voting has more majoritarian outcomes, **including electing the ranked Condorcet winner**, *precisely when* voters are **strategic**. That is, strategy is not some Achilles heel of Approval voting, it is the one of the mechanisms by which Approval voting achieves optimal outcomes.

## The Leader Rule

> **The Leader Rule**: Identify the top two front-runners in the election: the leader (most likely to win) and the "challenger" (the most likely to overtake the leader). You, as the voter, then
>
> 1. approve all candidates that you prefer to the leader
> 2. only approve the leader if you prefer them to the challenger.
>
> Do not approve of any other candidates (i.e. those you like  less than the leader).

That's the entire strategy! You could stop reading here and go apply this strategy in any Approval voting election. But if you want to understand *why* this strategy is optimal, and you're here for the practical examples and theory, read on.

The basic idea is to maximize the impact of your vote on the most likely pivotal outcomes of the election.

- By approving of all candidates you prefer to the leader, you strictly increase the chances of a more preferred candidate winning. Even if they have no chance, you still strictly help them by monotonicity. It's a "what the hell" vote that can't hurt you.
- If you prefer the challenger to the leader, then you approve of the challenger since you prefer them to the leader, and do not approve of the leader.
- If you prefer the leader to the challenger, you approve of the leader by the rule. And since the challenger is below the leader, you do not approve of the challenger.

The ultimate effect is that you have an impact on the most important race: between the leader and the challenger. You also help push forward any candidates you prefer to the leader.

As an example, let's take my favorite election to yap about: Alaska 2022. In this election, we had the following candidates:

- Mary Peltola (D)
- Sarah Palin (R)
- Nick Begich III (R)

In this election under IRV, Peltola won after Begich was eliminated, despite most of his votes transferring to Palin. Further, this election was controversial because the ballot data showed that Begich was actually the Condorcet winner, beating both Peltola and Palin head-to-head, but was eliminated first under IRV.

I want to go through how different voters might apply the leader rule in this election. In this race, the front-runner was Peltola (~40%), with Palin as the primary challenger (~31%). Begich was a relatively close third at (~28%). The most common voter types were:

- Palin > Begich > Peltola
- Begich > Palin > Peltola
- Begich > Peltola > Palin
- Peltola > Begich > Palin

Let's see how each of these voter types would apply the leader rule assuming Peltola is the leader and Palin is the challenger:

| Voter Type               | Approved Candidates  |
|--------------------------|----------------------|
| Palin > Begich > Peltola | Palin, Begich        |
| Begich > Palin > Peltola | Begich, Palin        |
| Begich > Peltola > Palin | Begich, Peltola      |
| Peltola > Begich > Palin | Peltola              |

These four groups show us the way that different voter groups might optimally utilize the nature of the Approval ballot to maximize their impact on the election.

- The Republican voters who rank both Palin and Begich above Peltola approve of both candidates, showing how the Republican voters can unite behind both candidates against the Democrat. Despite Begich not being in the top two, even voters who rank him second still approve him. Together, these voters form a coalition that essentially acts as a single vote *against* Peltola.
- The Begich > Peltola > Palin voters approve of Begich and Peltola. They prefer Begich the most, so there's no harm in approving him. They also prefer Peltola over the challenger Palin, so voting for Peltola as well helps maintain her lead over Palin, this bloc's least preferred candidate.
- The Peltola > Begich > Palin voters only approve of Peltola, as she is both their most preferred candidate and the leader. Since Peltola is already the frontrunner, it's not optimal for them to extend their approval to Begich, who is less preferred than Peltola.

The leader rule thus encourages voters to focus their approvals on the candidates that matter most in the election, helping to ensure that their votes have the maximum possible impact on the outcome. But notice something interesting: all blocs except the ones that rank Peltola first end up extending their approval to Begich.

For the Democratic voters who view Begich as a lesser evil compared to Palin (ex. Peltola > Begich > Palin voters), let us consider the strategy suggested by the leader rule in the different possible scenarios:

| Leader | Challenger | Approved Candidates (Peltola > Begich > Palin)                |
|--------|------------|---------------------------------------------------------------|
| Peltola | Begich     | Peltola                                                       |
| Peltola | Palin      | Peltola                                                       |
| Begich  | Peltola    | Peltola                                              |
| Begich  | Palin      | Peltola, Begich                                             |
| Palin   | Peltola    | Peltola, Begich                                             |
| Palin   | Begich     | Peltola, Begich                                             |

The only situations where they would approve of Begich is if

1. Begich is the leader and Palin is the challenger (in which case, they should approve Peltola and Begich to help push Palin down). That is, Peltola does not seem likely to win.
2. Palin is the leader (in which case, they should approve Peltola and Begich to help push Palin down). Even if Peltola is in second place.

In every other case (Peltola is the leader or Begich is the leader with Peltola as the challenger), they do not approve of Begich. We see that extending approval to that second least preferred candidate is optimal only when

1. Your favorite candidate is not in the top two, and
2. Your least favorite candidate is the leader.

The leader rule thus provides a clear and effective strategy for voters to maximize their impact in Approval voting elections, by focusing their approvals on the most relevant candidates and helping to ensure that their votes have the maximum possible impact on the outcome.

The claim, then, that Democratic voters might approve Begich out of fear and regret it when Begich wins, is not consistent with the leader rule strategy. While we will analyze this election in more depth, and show that it's very likely Begich would be the ultimate winner under Approval voting, can already see that Democratic voters should only give Begich their approval if it seems extremely unlikely that a Democrat can win. In which case, approving Begich is a rational way to prevent the strongly disliked Palin from winning.

In short, if it seems likely that the most important race is between Peltola and Begich, then it is not optimal for Democratic voters who prefer Peltola to approve Begich.

### Other Alaska Possibilities

I gave the table for the four most common voter types in Alaska 2022 with the assumption based on the plurality results that Peltola was the leader and Palin was the challenger. However, given Palin's lack of broad appeal, it seems more likely that the leaders and challengers would actually be Peltola and Begich. Let's see how the leader rule would apply in these cases:

| Voter Type               | Peltola Leader (Begich Challenger) | Begich Leader (Peltola Challenger) |
|--------------------------|------------------------------------|------------------------------------|
| Palin > Begich > Peltola | Palin, Begich                    | Palin, Begich                      |
| Begich > Palin > Peltola | Begich, Palin                    | Begich                            |
| Begich > Peltola > Palin | Begich | Begich                      |
| Peltola > Begich > Palin | Peltola                           | Peltola |
| Palin > Peltola > Begich | Palin, Peltola                   | Palin, Peltola                    |
| Peltola > Palin > Begich | Peltola                           | Peltola, Palin                    |

In these two scenarios, we see that

- Palin-first voters always approve of their top two candidates, since she is assumed to be nonviable.
- Begich-first voters approve of Begich, but they split based on if they prefer Palin or Peltola second. For those who prefer Palin second, they only approve Palin if Begich is not the leader. If they prefer Peltola second, they always approve Begich only.
- Peltola-first voters always approve of Peltola, but they split based on if they prefer Palin or Begich second. For those who prefer Begich second, they never approve of Begich. For those who prefer Palin second, they approve of Palin only if Peltola is not the leader.

## Contrast to the Dichotomous Goal

In my [other post](../avstratproof){:target="_blank"}, I provided a mindset which makes Approval voting strategyproof:

> A **Dichotomous Goal** is a goal where a voter only cares that a candidate they find acceptable wins, and does not care which acceptable candidate wins. If any acceptable candidate wins, that is a success. If an unacceptable candidate wins, that is a failure.

If a voter chooses to adopt a Dichotomous Goal, then there is only one optimal strategy: approve all acceptable candidates, and do not approve any unacceptable candidates. This strategy is simple and straightforward, and also sincere. The reason this strategy is optimal is because

- If you approve an unacceptable candidate, you risk being the deciding vote that gets them elected over an acceptable candidate. Therefore, approving unacceptable candidates can only be strictly harmful.
- If you do not approve an acceptable candidate, you risk being the deciding vote that breaks a tie between that acceptable candidate and an unacceptable candidate. Therefore, not approving acceptable candidates can only be strictly harmful.

The sleight of hand here is that we are pretending that we have dichotomous (two-tiered) preferences. If we view the election as a binary win/lose outcome based on whether an acceptable candidate wins, then Approval voting is strategy proof under this mindset. For example, if all you care about is having a Democrat win the seat, then you can vote for all democrats exclusively, and there's no better strategy.

This is a freeing way to think about Approval voting, and it is likely how I would personally approach it if I were a voter lucky enough to vote in an Approval election. The missing piece, however, from that post was how to optimally draw that line of acceptability, to maximize the chance of electing the most preferred possible candidate. Because, in reality, some unacceptable candidates are less unacceptable than others. And some acceptable candidates are more acceptable than others. Therefore, we want to draw that line of acceptability in a way that maximizes our chance of success.

A sincere voter can always decide they want to adopt a Dichotomous Goal based on their sincere and innate line of acceptability, and then vote sincerely based on that goal, knowing that they are playing optimally. However, the leader rule provides a very simple heuristic to help uncertain voters draw that line of acceptability optimally. Therefore, the leader rule can be viewed as a practical implementation of the Dichotomous Goal mindset.

However, it is a little more than that. Because Laslier proves that the leader rule is actually an optimal best response under a probabilistic model of elections. Therefore, the leader rule and dichotomous goal are, in my opinion, two sides of the same coin that is the empowering strength of sincerity under Approval voting. The dichotomous goal represents the game theoretic guarantee of strategyproofness and sincerity under Approval voting under a simplified goal, while the leader rule is the proof that sincerity is the best response to a probabilistic model of large elections.

## The Florida Tremble

In a large election, the chance that your vote is decisive is essentially zero. Therefore, in a purely deterministic, perfect knowledge model of elections, strategy has basically no impact. To get around this, Laslier introduces an element of uncertainty to allow for strategy to actually have an impact. He calls this the "Florida Tremble," after the infamous 2000 US Presidential election in Florida, where it's believed that miscounted votes led to a different outcome. By assuming we have "many" voters, and there's a small chance for one of the bubbles on a voter's ballot to be "miscounted", we allow for strategic voting to have a non-zero expected impact on the outcome.

Without getting into the weeds of infinitesimal probabilities, and the effect of a "large electorate", the intuitive idea is actually quite straightforward: in a large election, ties are very, very, very unlikely. However, there are two observations to make:

1. If some votes are miscounted due to machine errors, then essentially any election, could be technically tied by some number of miscounted votes. The chance that your vote is decisive now becomes non-zero (though, still small).
2. Some ties are more unlikely than others. Laslier's rule essentially focuses on the most likely ties, which uniquely determine an optimal strategy.

Based on these two observations, Laslier's leader rule basically treats the voter's ballot as a lottery ticket. You fill it out in a way that maximizes the positive impact in the most likely pivotal scenarios (the ones where your vote could be decisive). The key insight about Approval voting is that by being able to cast multiple approvals, you can view your ballot as a lottery ticket which gives you the win in both the Powerball and Mega Millions at the same time. But you do so by prioritizing whichever lottery is more likely to pay off.

What I want you to keep in mind is that the complexity of the next section is basically the mathematical proof of why the natural mental shortcuts we take when making decisions optimally align with the leader rule. It can be freely skipped if you just want to understand the practical implications of the leader rule.

### The Descending Chain of Unlikely Ties

This is a section that gets into the weeds of why the leader rule is optimal. If you are not interested in the technical details, feel free to skip ahead to the [next section](#consistency-with-practical-voter-psychology){:target="_blank"}.

We imagine that we have a front-runner $$x_1$$, who we call the leader, and a challenger $$x_2$$. The challenger is the most likely candidate to beat the leader (ex. the most likely candidate for the leader to tie or lose to). We imagine that every other candidate $$x_3, x_4, \ldots$$ is less likely to beat the leader than the challenger is.

However, let's keep it concrete with a recent example: the 2025 NYC Mayoral Democratic Primary. In that race, Andrew Cuomo was seen as the clear frontrunner (leader), and the challenger Zohran Mamdani (who ended up winning in an upset victory). We also have other candidates like Brad Lander, Adrienne Adams, and others. Let's assume that the order is based on their first choice vote shares in the actual election. That gives the ordering $$x_1 = \text{Cuomo}$$, $$x_2 = \text{Mamdani}$$, $$x_3 = \text{Lander}$$, $$x_4 = \text{Adams}$$, etc. all the way down to the last place candidates like Paperboy Love Prince.

We then have the following events in decreasing order of likelihood (by ignoring three or more way ties), assuming our identification of the leader and challenger is correct:

1. Most likely: Cuomo wins by more than 1 vote over Mamdani. In this case, technically your vote has no effect, so it doesn't matter what you do.
2. Next most likely (but far less likely): Cuomo ties or wins by exactly 1 vote over Mamdani. In this case, your vote could be decisive in determining the winner between these two candidates. Therefore, you should vote for one and only one of these candidates, depending on which you prefer. If you prefer the leader to the challenger, approve the leader (you strengthen their lead). If you prefer the challenger to the leader, approve the challenger (you help them overtake the leader). This is the most likely lottery you're going to win, so you should prioritize your ballot to be decisive in this one.
3. Far less likely: Cuomo and Lander tie or are within 1 vote of each other for first place. In this case, your vote could be decisive in determining the winner between these two candidates. If you prefer Lander to Cuomo, you should definitely approve Lander to help them overtake Cuomo. If you prefer Cuomo to Lander, then what you chose in the previous step might put you in a pickle. If you are already approving Cuomo, then you're fine, you're approving exactly one between the leader and Lander. But you prefer Mamdani > Cuomo > Lander, meaning you aren't approving Cuomo, then we have to weigh the probabilities. Since it's far more likely that Cuomo and Mamdani are close than Cuomo and Lander, you should stick with your original choice of approving only Mamdani (not the leader). That's more important than being the decider between Cuomo and Lander, which is far less likely. This is, in effect, like seeing that your ticket for the Powerball would conflict with your ticket for the Mega Millions, so you choose to prioritize the more likely lottery. Therefore, it simply comes down to **approve Lander if and only if you prefer Lander to Cuomo**.
4. The next most likely (but very, very unlikely): Cuomo and Adams tie or are within 1 vote of each other for first place. By the same reasoning as before, you should approve Adams if and only if you prefer Adams to Cuomo.
5. etc. etc. until you get to the tie between Cuomo and the last place candidate Paperboy Love Prince. Same logic: approve the last place candidate if and only if you prefer them to Cuomo. But now you have uniquely determined your entire ballot!

One may ask whether or not it's more likely that Cuomo ties with Paperboy Love Prince or that Mamdani ties with Lander. The key is that *both* the Cuomo and Mamdani tie and Cuomo Lander tie is far more likely than the Mamdani and Lander tie. That is, we should compare each candidate only to the leader. If you happen to draw one candidate in the lottery, it's far more likely that the leader is involved in that lottery than any other candidate.

In summary, your ballot comes down to two rules:

1. Approve every candidate you prefer to the leader $$x_1$$. No matter what. You have nothing to lose by approving them, particularly in the case that they might overtake the leader.
2. Approve the leader $$x_1$$ if and only if you prefer them to the challenger $$x_2$$. This is the most important race, so you should make sure to approve exactly one of these two candidates based on your preference.

Note that this actually means that your optimal ballot under the leader rule is sincere! It's not optimal to have any "holes" in your approvals. For any candidate you approve, you should also approve all candidates you prefer to them.

In fact, the leader rule essentially tells you that the line of acceptability should be precisely right above, or right below, the leader. By drawing it here, you maximize your impact to get a favorable outcome. In particular, this means you should always approve your most preferred candidate.

## Consistency with Practical Voter Psychology

In Laslier's paper, he makes two key observations about voter psychology that make the leader rule particularly appealing:

1. Voters consider pivotal scenarios sequentially, starting with the most likely scenarios. This means that they focus on the most probable outcomes first, and make their decisions based on those scenarios.
2. The leader rule corresponds to Tversky's "elimination by aspects" model of decision-making. People tend to eliminate options that do not meet certain ranked criteria.

The leader rule boils down to ranking the pivotal scenarios by their likelihood, and making decisions based on how their internal preferences align with those scenarios.

The most likely pivotal scenario is the leader vs. the challenger. Therefore, the voter focuses on approving exactly one of these two candidates based on their preference. The next most likely scenarios involve the leader vs. other candidates, leading the voter to approve all candidates they prefer to the leader.

Therefore, the leader rule aligns well with the "mental shortcuts" that voters naturally use when making decisions. It provides a clear and straightforward strategy that maximizes the voter's impact on the election outcome, while also being consistent with how people typically think about choices.

The most surprising aspect of the leader rule, however, is its majoritarian properties, which we will explore next.

## Condorcet-efficiency of the Leader Rule

One might ask "what happens if everyone uses the leader rule, all at once?" Laslier analyzes this in his paper, and there are some interesting results:

1. The leader rule only has an equilibrium when the leader is also the unique Condorcet winner. If the leader is not a unique Condorcet winner, then a new candidate (who beats the leader head-to-head) will get more approvals than the current leader, and overtake them.
2. If there is no unique Condorcet winner, then there is no equilibrium under the leader rule.
3. After any iteration of everyone using the leader rule, if a unique Condorcet winner exists, they will have over 50% approvals.

However, credit to Rob LeGrand for pointing out to me that it is not necessarily the case that the leader rule converges to the Condorcet winner under all initial conditions. See [the appendix](#appendix) for a pathological (but intruiging) example of this.

The proof and explanation of this is actually relatively straightforward. Consider what happens when everyone uses the leader rule at the same time:

- For any candidate X who is not the leader, the voters who approve them will be precisely those who rank X above the leader. Therefore, X's total approval percentage will be equal to the percentage of voters who prefer X to the leader. That is, the head-to-head result of X vs. the leader.
- The leader's approval percentage will be equal to the percentage of voters who prefer the leader to the challenger (since only those voters approve the leader). Thus, the leader's approval percentage is equal to the head-to-head result of the leader vs. the challenger.

This means that after an iteration of every voter using the leader rule, the approval percentages precisely equal head-to-head percentages.

Thus, if the leader is a unique Condorcet winner, then after the iteration they will have over 50% approvals, and everyone else will have under 50% approvals. Therefore, the leader remains the leader, and must strictly win. The equilibrium challenger will be the candidate with the least bad head-to-head result against the leader.

In conjunction with the previous section, what we see is that the way approval voting reacts with the way humans make decisions leads to a natural majoritarian outcome when everyone uses the leader rule. In that way, Approval voting is more majoritarian when voters are strategic, which significantly dampens the common criticism that Approval voting is both non-majoritarian and susceptible to strategic voting.

Note that this means that we can loosely simulate the leader rule iteratively by simply looking at pairwise matrix of head-to-head results. However, first we should talk about the "failure" cases of the leader rule.

## Can the leader rule fail?

To answer this question, we have to even define what a "failure" of a strategy even means. If it's to ensure that a Condorcet winner is always elected when one exists, then yes. But take it from another perspective: after any iteration of everyone using the leader rule, the resulting leader is either the Condorcet winner or someone who a majority of voters prefer over the previous leader they expected to win when they stepped into the voting booth. Therefore, the leader rule always pushes the election towards a more majoritarian outcome than the previous expected outcome. That is nontrivial.

And here's the thing about Approval voting that we should keep in mind: It is always [100% consistent with its ballot data](../consistentcardinal){:target="_blank"}. That is, whoever wins under Approval voting is *always* the Condorcet winner of the implied preferences expressed by the Approval ballots. Therefore, in a real election, there is no way to know if the actual winner was the ranked Condorcet winner or not, because we do not have access to the full ranked preferences of the voters (it is, [as I have previously called it](../practicalapproval){:target="_blank"}, a "You can't prove it's not Condorcet" method).

However, we can analyze the cases in which the leader rule does not converge to the Condorcet winner, assuming we have access to the full ranked preferences of the voters.

As mentioned above, if there is a unique Condorcet winner, then the leader rule has an equilibrium where that candidate is the leader, and after any number of iterations of everyone using the leader rule, that Condorcet winner will have over 50% approvals. An example by Rob LeGrand is given in the [appendix](#appendix) where a cycle can occur that does not converge to the Condorcet winner (that is, the Condorcet winner perpetually has over 50%, but there is always another candidate with even more). But there are two considerations to make here:

1. Because Approval voting is always consistent with its ballot data, if the leader rule does not converge to the Condorcet winner, then the actual winner still just looks like the Condorcet winner of the implied preferences expressed by the Approval ballots, regardless. Therefore, this failure is purely speculative. The true Condorcet winner of the full ranked preferences may suspect that they should have won, but there would be no evidence in the ballot data for that conclusion. Instead, the point of focus should be that the leader rule makes the election of that ranked Condorcet winner extremely likely to begin with, and it results in more majoritarian outcomes overall.
2. In practice, such a case is likely to be extremely rare. Condorcet cycles are already absurdly rare in real elections, and usually only happen in small, local elections with few voters and candidates. The leader rule will have no equilibrium in such cases, but, as per point 1, Approval voting will still elect the Condorcet winner of the implied preferences expressed by the ballots.

This means that the leader rule would be extremely effective at ensuring majoritarian outcomes in practice, and the cases where it fails are likely to be extremely rare and of little practical consequence. Such failures are purely speculative, and can't undermine trust in the system. For instance, since after any iteration of every voter using the leader rule, at least one candidate has over 50% approvals, and if a unique Condorcet winner exists, they will be one such candidate. This means that with strategic voting under the leader rule, Approval voting is guaranteed to elect *some* candidate (likely to be the true Condorcet winner) with over 50% approvals, which is a strong majoritarian outcome.

This strongly contradicts the assumption that Approval voting strategy promotes bullet voting all the way back to plurality outcomes. The leader rule says something more nuanced: Bullet voting *is* optimal when you're ahead! But when you're behind, it's optimal to approve of multiple candidates when there are multiple candidates you like better than the current favorite to win. Bullet voting is not a failure, it can be a natural and optimal strategy when the likely outcome is favorable.

From the voter's perspective, the leader rule is a single action based on a snapshot in time of who the perceived leader and challenger are. The voter does not need to worry about the long-term dynamics of the election, or whether their vote will lead to a cycle or not (as cycles are impossible in Approval voting data). Instead, the leader rule provides a clear and effective strategy for how to draw the line of a sincere strategy that maximizes the voter's chance of a favorable outcome. Whether or not there is a Condorcet cycle is irrelevant to the voter's decision-making process and will be invisible in the final results.

However, there is one more concern: What if the voters do not have good information on who the leader and challenger are? For example, in 2024, different social media bubbles ad vastly different expectations of who would win the presidential election between Harris and Trump. Or what if there are three or four candidates who all seem viable? Or what if the race is so low profile that there's no polling data? In that case, one may want to default to a sincere strategy (ex. a dichotomous goal). The wonderful thing about Approval voting is that sincerity is always a reasonable default strategy. The leader rule simply provides a practical heuristic to help draw that line of sincerity optimally when you do have some information on the likely front-runners.

### Not Following the Leader Rule

I want to briefly address the possible concern of a sincere voter, like myself. The leader rule tells us to not approve of any candidates less preferred than the leader. However, I would never encourage a voter who sincerely prefers those candidates to not approve of them. If I genuinely like both the leader and challenger, I may just want to vote for both of them, regardless of the strategic implications. While it does not *maximize* my impact in the infinitesimal chance my vote is decisive, it does still have a concretely positive impact against my least preferred candidates.

The Dichotomous Goal mindset becomes stronger the wider your genuine line of acceptability is drawn. If you genuinely would be happy with 3/4ths of the candidates, even if the leader rule tells you to only approve of one, then your sincere vote for all of those candidates is the strongest possible vote *against* the 1/4th of the candidates you truly detest. That is powerful in its own right. And if you want to be a sincere voter in Approval voting, more power to you. You may find my other post about the [dichotomous goal](../avstratproof){:target="_blank"} helpful in that regard.

## A Practical Simulation

We can estimate the leader rule without the full ballot data by using the pairwise matrix of head-to-head results. This does, however, require assuming that the expressed preferences in head-to-head match-ups are representative of the full preference orderings of the voters.

This is not likely true in all cases. For example, in the 2025 NYC Democratic Mayoral Primary, the head-to-head results of the winner Zohran Mamdani vs. Brad Lander were nearly 70% in favor of Mamdani. However, given that many Cuomo voters likely preferred Lander to Mamdani, but only bullet voted for Cuomo, the fact that they did not express a preference in that race means that the head-to-head result likely overstates Mamdani's true preference share. Still, this can give us a rough estimate of how the leader rule might play out in a real election, using existing ranked data.

We can simulate the leader rule iteratively using the head-to-head matrix as follows:

1. Take all ordered pairs of candidates (X, Y), representing X as the leader and Y as the challenger.
2. For each pair, set the approval percentage of X to be the head-to-head result of X vs. Y. Set the approval percentage of every other candidate Z to be the head-to-head result of Z vs. X.
3. Rank the candidates by their approval percentages to determine the next leader and challenger. The next leader is the candidate with the highest approval percentage, and the next challenger is the candidate with the second highest approval percentage.

This, in fact, defines a directed graph over the pairs of candidates (X, Y). Each node is a pair (X, Y), and there is a directed edge from (X, Y) to (X', Y') if the next leader and challenger after applying the leader rule to (X, Y) are (X', Y'). That is, (X', Y') are the candidates with the highest and second highest approval percentages after every voter applies the leader rule assuming X is the leader and Y is the challenger.

Since the result of all voters applying the leader rule is deterministic based on who the perceived leader and challenger are, the edges in this graph are deterministic, if we do not have any ties for first or second place in approval percentage. Laslier's paper assumed a "large electorate" to avoid ties, and real elections with many voters are unlikely to have exact ties in approval percentage, so this analysis is reasonably deterministic.

Equilibria under the leader rule correspond to self-loops in this graph, where (X, Y) maps to itself, which occur precisely when X is a unique Condorcet winner, and Y is the candidate with the best head-to-head record against X. Cycles in this graph correspond to situations where the leader rule does not converge to a single outcome, but instead cycles through a set of leaders and challengers. Here are a few examples of this simulation applied to real elections:

### Alaska House Special Election 2022

[ranked.vote page for this election](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}.

Using the head-to-head results from Alaska 2022, we can simulate the leader rule. The head-to-head results were:

| Head-to-Head       | Winner      | Percentage    |
|--------------------|-------------|---------------|
| Peltola vs. Palin  | Peltola     | 51.4% : 48.6% |
| Begich vs. Peltola | Begich      | 52.5% : 47.5% |
| Begich vs. Palin   | Begich      | 61.4% : 38.6% |

The directed graph of leader-challenger pairs is as follows:

<img src="/assets/img/leader_rule/alaska.png" alt="Leader Rule Alaska 2022" style="max-width: 600px;">

Here is how to read this graph:

- A node like "Peltola, Palin" represents the scenario where Peltola is the leader and Palin is the challenger. This node points to the red node "Begich, Peltola", which means that if all voters enter the voting booth expecting Peltola to be the leader, and see Palin as the challenger, then after everyone applies the leader rule, the final result will have Begich in first place and Peltola in second place.
- Similarly, the node "Peltola, Begich" actually points to the "Begich, Palin" node, meaning that if everyone expects Peltola to be the leader and Begich to be the challenger, then after everyone applies the leader rule in the voting booth, the final result will have Begich in first place and Palin in second place. Peltola actually falls to third place in this scenario, because Begich's head-to-head against Peltola was stronger than Palind's head-to-head against Peltola, which was stronger than Peltola's head-to-head against Begich.
- A node is colored red if it is an equilibrium (it points to itself), and blue if any nodes have an edge to it, but is not an equilibrium. This means that only the red and blue nodes are possible outcomes after all voters apply the leader rule.

The equilibrium has Begich as the leader and Peltola as the challenger. This is consistent with Begich being the Condorcet winner, and Peltola having the least bad head-to-head result against Begich.

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
| Mamdani vs. Cuomo   | Mamdani     | 56.4% : 43.6% |
| Mamdani vs. Lander  | Mamdani     | 69.6% : 30.4% |
| Mamdani vs. Adams   | Mamdani     | 74.8% : 25.2% |
| Cuomo vs. Lander    | Lander      | 54.4% : 45.6% |
| Cuomo vs. Adams     | Adams       | 50.3% : 49.7% |
| Lander vs. Adams    | Lander      | 72.7% : 27.3% |

The directed graph of leader-challenger pairs is as follows:

<img src="/assets/img/leader_rule/nyc.png" alt="Leader Rule NYC 2025" style="max-width: 600px;">

We see the red equilibrium node with Mamdani as the leader and Cuomo as the challenger, and two other blue outcome nodes: (Lander, Mamdani) and (Mamdani, Lander).

Due to Lander's strong head-to-head results, we see that many nodes converge to Mamdani the leader and Lander as the challenger. Almost every node points to a node with Mamdani as the leader (the one exception is Lander as the leader and Adams as the challenger, pointing to Lander as the leader and Mamdani as the challenger, which would be very unlikely to be the perception voters have), consistent with Mamdani being the Condorcet winner. Therefore, it seems highly likely that Mamdani would win under approval voting with strategic voters using the leader rule.

The most likely two initial nodes would be (Cuomo, Mamdani) and (Mamdani, Cuomo), as they were the top two frontrunners. The former leads to (Mamdani, Lander), due to both Mamdani and Lander's strong head-to-head against Cuomo. The latter, however, is the equilibrium. In either case, we converge to Mamdani winning.

### Minneapolis City Council Ward 2 2021

[ranked.vote page for this election](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}.

This was a very notable election because it actually had a Condorcet cycle. The cycle was between Cam Gordon, Robin Wonsley, and Yusra Arab. The actual winner was Robin Wonsley, who defeated Yusra Arab in the final round of IRV. However, Cam Gordon beat Robin Wonsley head-to-head, and Yusra Arab beat Cam Gordon head-to-head, creating a Condorcet cycle.

The head-to-head results were:

| Head-to-Head         | Winner      | Percentage    |
|----------------------|-------------|---------------|
| Wonsley vs. Arab     | Wonsley     | 50.1% : 49.9% |
| Wonsley vs. Gordon   | Gordon      | 50.5% : 49.5% |
| Wonsley vs. Anderson | Wonsley     | 63.8% : 36.2% |
| Arab vs. Gordon      | Arab        | 51.3% : 48.7% |
| Arab vs. Anderson    | Arab        | 73.3% : 26.7% |
| Gordon vs. Anderson  | Gordon      | 64.5% : 35.5% |

There was a fifth candidate who was not competitive, so we will omit them from this analysis. The directed graph of leader-challenger pairs is as follows:

<img src="/assets/img/leader_rule/mn.png" alt="Leader Rule Minneapolis 2021" style="max-width: 600px;">

We color the cycle in orange. There is no equilibrium in this case, due to the Condorcet cycle. But we have two other blue outcome nodes involving Gordon that eventually lead into the cycle.

Observe the four-node cycle between Wonsley, Arab, and Gordon:

| Leader | Challenger | Approvals | Target |
|--------|------------|-----------|--------|
| Arab | Wonsley | Wonsley: 50.1%, Arab: 49.9%, Gordon: 48.7%, Anderson: 26.7% | (Wonsley, Arab) |
| Wonsley | Arab | Gordon: 50.5%, Wonsley: 50.1%, Arab: 49.9%, Anderson: 36.2% | (Gordon, Wonsley) |
| Gordon | Wonsley | Arab: 51.3%, Gordon: 50.5%, Wonsley: 49.5%, Anderson: 35.5% | (Arab, Gordon) |
| Arab | Gordon | Arab: 51.3%, Wonsley: 50.1%, Gordon: 48.7%, Anderson: 26.7% | (Arab, Wonsley) |

If we interpret nodes as possible perceptions of the race, and suppose voters update their strategy based on the leader rule when they answer a poll, then we would basically see a cycle like this:

- Week 1: Voters think Wonsley is the leader, Arab is the challenger. They update their strategies and answer the next poll.
- Week 2: Gordon shoots up to be the leader, since he has the strongest head-to-head against Wonsley. Wonsley falls to challenger, and Arab falls out of the top two (and under 50%), since Wonsley beats Arab and that match-up decides the next approval percentages.
- Week 3: Arab shoots up to be the leader, since she has the strongest head-to-head against Gordon. Gordon falls to challenger, and Wonsley falls out of the top two like Arab did last week.
- Week 4: Arab remains the leader, but Wonsley shoots up to be the challenger, since she has the strongest head-to-head against Arab. Arab's strong head-to-head against Gordon keeps Arab in first place.
- Week 5: Wonsley becomes the leader again, since she has the strongest head-to-head against Arab. Arab falls to challenger, and Gordon falls out of the top two again. And now we're back to week 1.

If we were to imagine this happening in a campaign cycle, we would still eventually have to run the election at some point. And depending on who the perceived leader and challenger are at that moment, we would end up with one of the three candidates winning. Since Approval voting is consistent with its ballot data, the actual winner would be the Condorcet winner of the implied preferences expressed by the ballots, flattening out the cycle. The ballots won't catch fire, the machines won't explode, and no loser will be able to credibly claim they would have beaten the actual winner in a head-to-head match-up, because the ballots won't show that. The result will be legitimate, but close. Someone will get over 50% approvals, and

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

Laslier, J. F. (2009). The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate. *Journal of Theoretical Politics*, 21(1), 113-136. [https://journals.sagepub.com/doi/10.1177/0951629808097286](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}

[ranked.vote](https://ranked.vote){:target="_blank"} Election Reports:

- Alaska House Special Election 2022: [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}
- NYC Democratic Mayoral Primary 2025: [https://ranked.vote/report/us/ny/nyc/2025/07/mayor](https://ranked.vote/report/us/ny/nyc/2025/07/mayor){:target="_blank"}
- Minneapolis City Council Ward 2 2021: [https://ranked.vote/report/us/mn/2021/11/ward-2](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}

[hyperlink](https://www.youtube.com/watch?v=VXZUjn41dbw){:target="_blank"}
