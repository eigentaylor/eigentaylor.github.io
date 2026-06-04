---
layout: distill
title: Is Approval Voting Strategyproof?
date: 2026-06-04
description: Well yes, but actually no. Unless...
giscus_comments: true
importance: 3
tags: voting
category: polisci
theorems: true
pretty_table: true
preview_redirect: true
published: true
exclude_appendix_from_word_count: true
collapse_appendix: false
bibliography: voting.bib
thumbnail: /assets/img/wellyesbutactuallyno.jpg
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: What is strategyproofness?
    subsections:
      - name: Approval is not strategyproof
      - name: Approval is strategyproof?
  - name: The Dichotomous Goal
    subsections:
      - name: Where to draw the line
      - name: Effectively Dichotomous Preferences
  - name: Conclusion
  - name: Appendix
    subsections:
      - name: Ballot-level strategyproofness
      - name: An Axiomatic Aside
---

## Introduction

This is a redo of my second post on Approval voting from November 2025. I was early in my journey learning about Approval voting, and I think I can explain this concept more clearly and concisely now. This post is primarily based on the seminal 1978 paper by Brams and Fishburn<d-cite key="bramsFishburn1978approval"></d-cite>.

Approval voting lets voters approve (vote for) as many candidates as they like. It's like the standard choose-one plurality system, except it removes the arbitrary restriction of voting for only one candidate. Surprisingly, despite being such a simple change, the system is [on par with the best of the most popular proposed systems](../approval-only/){:target="_blank"}.

The question we are trying to answer in this post is a simple one:

> **Is Approval voting strategyproof?**

The short answer is:

![well yes, but actually no](/assets/img/wellyesbutactuallyno.jpg)

## What is strategyproofness?

Strategyproofness is slippery and hard to define rigorously. Everyone can easily *grasp* the idea, but writing it down as a mathematical property is harder.

Brams and Fishburn<d-cite key="bramsFishburn1978approval"></d-cite> give a somewhat tailored definition in the context of Approval voting, which is what we use here. The following is a little oversimplified for pedagogical purposes.

> **Definition:** A strategy in Approval voting is **sincere** if there are no "holes" in the ballot. In other words, a voter draws a "line of acceptability" in their ranking and approves everyone above that line.
>
> A voting system is **strategyproof** for a given preference order if there is always only one "rational" strategy for any voter with that preference order to use in any scenario, and that strategy is sincere.

For example, you cannot approve of your first and third choices without approving your second choice on a sincere ballot, because that would imply a "hole" in your ballot.

I know some people, particularly [Condorcetists](../condorcet-approval/){:target="_blank"}, who dislike this definition of "sincere" because it allows a voter multiple sincere strategies. The objection gets the relationship backwards. Sincerity is defined based on how *ordinal* preferences--which [cannot capture acceptability](../why-condorcet/){:target="_blank"}--can "honestly" be projected onto an Approval ballot.

One positive aspect of this definition is that two voters who rank $A>B>C$ can vote exclusively for $A$ or for both $A$ and $B$ to show a meaningful difference in how they feel about $B$ relative to $A$. Is $B$ an acceptable backup for $A$, which you are happy to approve of, or is $B$ a lesser evil that you only approve of if you have to? Both of these are sincere strategies, and Approval allows them both to be expressed without forcing the voters to share only the ordinal information which cannot capture that distinction. This is a feature, not a bug, in my view.

Either way, this is the usage of the word "sincerity" in the literature, so we'll stick with it: a voter can be both sincere and strategic. For the pedants in the audience, the following blocks provides the formal definitions.

{% proof A remark on "rationality" %}
What we are calling "rational" is called "admissible" in the literature. Formally, it just means a strategy or ballot that is not "dominated" by any other strategy or ballot. In other words, there is no other ballot that would give you at least as good in all possible scenarios and strictly better in at least one scenario. So you can just ignore dominated strategies, since they are never optimal.

For example in Approval, why would you ever vote for a middle tier candidate, and not your favorite candidate? It doesn't hurt to include your favorite, because you might make them win! Similarly, you should never vote for your least favorite candidate, for the same reason.

We articulate this idea with the word "rational". It would be irrational to submit a ballot which is at most as good and sometimes worse than another ballot. So we can just ignore those ballots, and only consider the rational (admissible) ballots.
{% endproof %}

{% proof A remark on "sincerity" %}
Intuitively, sincerity can be easily understood as setting an "acceptability threshold" somewhere in your ranking. However, the precise definition which follows is necessary to deal with the case of equal ranks/indifference:

> A strategy in Approval voting is **sincere** if given that the strategy includes candidate $X$, then the strategy also includes all candidates that the voter strictly prefers to $X$.

For example, a voter who ranks $A > B = C > D$ has four "rational" sincere strategies:

- approve $A$ only
- approve $A$ and $B$
- approve $A$ and $C$
- approve $A$, $B$, and $C$

All of these are strictly "sincere", by definition. If you approve of $B$, then only $A$ is *strictly* preferred. So any sincere strategy including $B$ must also include $A$. But we need not include candidates that are equally preferred, like $C$ in this example.
{% endproof %}

### Approval is not strategyproof

Let's start with the bad news. Approval is not *generally* strategyproof. We can show this easily with a simple example.

**Example:** Suppose you, as a voter, prefer $A > B > C$. With this preference, you have two sincere "rational" strategies: approve $A$ and $B$, or approve $A$ only.\label{strategy-not-proof}

Consider the following scenarios:

| Scenario   | $A$ Votes | $B$ Votes | $C$ Votes | Optimal Ballot |
|------------|-----------|-----------|-----------|----------------|
| Scenario 1 | 100       | 100       | 10        | $A$ only       |
| Scenario 2 | 10        | 100       | 100       | $A$ and $B$    |

In scenario 1, $A$ and $B$ are tied for first, with $C$ far behind. Approving both $A$ and $B$ preserves the tie; approving only $A$ breaks the tie in favor of your top choice. So in scenario 1 the optimal ballot is $A$ only.

In scenario 2, $B$ and $C$ are tied for first, with $A$ far behind. Approving only $A$ leaves the $B$–$C$ tie untouched; approving $A$ and $B$ breaks the tie in favor of $B$ and blocks $C$. So in scenario 2 the optimal ballot is $A$ and $B$.

These two scenarios show that a voter with the same preference order may need to choose different sincere strategies to obtain the best outcome. Therefore, Approval voting is not strategyproof in general. As Approval is still subject to Gibbard's 1973 theorem<d-cite key="gibbard1973manipulation"></d-cite>, we should not be surprised by this result.

### Approval is strategyproof?

Okay, why isn't the post over? We just proved that Approval voting is not strategyproof! Well, it turns out there's a little more to the story.

In 1978, Brams and Fishburn proved in their seminal paper on Approval voting that it is strategyproof for a voter if and only if that voter has dichotomous preferences.<d-cite key="bramsFishburn1978approval"></d-cite>

> **Definition:** A voter's preferences are **dichotomous** if they can partition the candidates into two tiers: a top tier of "good" candidates, and a bottom tier of "bad" candidates. The voter is indifferent between all the candidates in the top tier, and also indifferent between all the candidates in the bottom tier, but they strictly prefer all the candidates in the top tier to all the candidates in the bottom tier.

Strategyproofness follows from a result they prove in the paper:

> **Theorem:** Any "rational" strategy in Approval voting involves voting for all candidates in a voter's top tier and no candidates in a voter's bottom tier. Nothing can be said about the candidates in any middle tier. (Corollary 1<d-cite key="bramsFishburn1978approval"></d-cite>)

In other words, you have no reason to ever not approve of your absolute favorites, and you will never be compelled to approve of your absolute least favorites. This is not necessarily true in Approval with a runoff<d-cite key="fishburnBrams1981runoff"></d-cite>, which we will not be discussing here.

This theorem implies that all "rational" strategies are sincere if there are three or fewer tiers. But Brams and Fishburn also show that with four or more preference tiers, insincere strategies can sometimes be "rational" and optimal (under very contrived scenarios)<d-cite key="bramsFishburn1978approval"></d-cite>. However, Laslier proved in 2009 that under a fairly realistic probabilistic large-electorate model (with a few minor assumptions), a best response in single-winner Approval is always sincere<d-cite key="laslier2009leaderRule"></d-cite>.

Given this theorem, strategyproofness becomes trivial under dichotomous preferences: with only a top and bottom tier, there's exactly one optimal strategy--approve all "good" candidates and reject all "bad" ones. This strategy is necessarily sincere. Thus, Approval voting is strategyproof under dichotomous preferences. Specifically, Approval voting is strategyproof for *any* voter with dichotomous preferences, even if other voters have complex preferences.

## The Dichotomous Goal

Let's suppose you're an average, tired voter. You see a crowded field of candidates (the 2026 California governor's race, which is still being counted, has [61 candidates on the ballot](https://elections.cdn.sos.ca.gov/statewide-elections/2026-primary/cert-list-candidates.pdf)), and you don't have the time or energy to properly rank all of them, let alone calculate an optimal strategy based on viability and polling. You just know you like some of them and dislike others. You might therefore simplify the election into a sort of "game" as follows:

> If you only care about electing *any* "acceptable" candidate, however you define "acceptable", then you are adopting a dichotomous preference structure: you don't care which of the acceptable candidates wins, so long as none of the unacceptable ones do.

We can call this a **dichotomous goal**.

Under such a goal, you are in the dichotomous domain where Approval is strategyproof: approve every candidate you find acceptable, and that's your optimal (sincere) strategy. In many other systems you would need to make strategic calculations to avoid making the outcome worse by participating honestly.

### Where to draw the line

We haven't escaped strategy entirely: it's still prudent to consider the viability of your acceptable candidates. There is still the risk of "passive inefficiency": your acceptable set might be too narrow (you fail to approve any viable candidates) or too broad (you fail to distinguish between top contenders).

Even so, this is usually preferable to the kind of "active betrayal" that can occur in other systems. Laslier's leader rule is one such approach to drawing an informed acceptability line<d-cite key="laslier2009leaderRule"></d-cite>, but that's for another post.

However, if you feel you can only approve a small set of candidates in good conscience, Approval lets you express that honestly without penalty. And unlike some more complex systems, Approval [won't betray you for that choice (see the appendix)](#ballot-level-strategyproofness){:target="_blank"}: your ballot can only help elect someone you voted for.

This is, however, a point in favor of Approval with a top two runoff. Even if a voter fails to distinguish between the frontrunners, the runoff gives them another chance to influence the result. And although Approval with a runoff is more strategic and less sincere in theory with perfect knowledge<d-cite key="fishburnBrams1981runoff"></d-cite>, it can also make voters feel safer being more generous with their approvals, since they still have the runoff if they accidentally waste their vote.

### Effectively Dichotomous Preferences

The truth is that, although we *could* ask voters to rank candidates, many people find a dichotomous yes/no choice more natural.

"Vote blue no matter who" is an example of a dichotomous preference. A voter who would approve every candidate with an "R" next to their name and disapprove everyone else is effectively operating in the dichotomous domain. This applies to single-issue voters as well.

Many voters can readily categorize candidates into "acceptable" and "unacceptable" buckets without much thought, based on the criteria that matter to them. I have also [argued that compromise](../why-condorcet/){:target="_blank"} and consent are inherently binary concepts. "Acceptable" and "unacceptable" is precisely what Approval voting captures, which makes it a natural fit for these voters and these goals.

## Conclusion

As I explored in [this post](../why-condorcet/){:target="_blank"}, I think compromise and consent are essentially impossible to express with a ranked ballot. That is simply not what ranked ballots are *able* to capture. Two voters can give the same preference *order* yet disagree on who they'd find genuinely acceptable. "Second choice" does not imply "acceptable backup"--it could mean "lesser evil" (or vice versa). Scores are similarly ambiguous: is a 3/5 "acceptable" or not?

Acceptability isn't naturally categorized by ordinal rankings or utility scores. Approval voting is, to me, the natural language of compromise: each voter signals who they find acceptable, and the candidate with the largest base of acceptability earns the right to be called the consensus choice. Approval isn't perfect at capturing compromise--no practical system is--but it asks the right question. And I think that is something that we, in this polarized time, should [seriously consider](../approval-only){:target="_blank"}.

This is not to understate the strategic question of where to draw the line of acceptability--it's a real consideration. But in practice the strategic worry around Approval is often overstated.

In practice, your optimal ballot is almost surely sincere<d-cite key="laslier2009leaderRule"></d-cite>; the main strategic question is where you draw your acceptability threshold. If you can identify who you genuinely like, you can vote for them without fear of active betrayal. As the appendix explains, Approval takes your expressed preferences at face value rather than forcing exaggeration or misrepresentation. That's how strategyproofness on the dichotomous manifests in the real world, and it's a meaningful advantage for Approval over many other systems, in my view.

## Appendix

The remainder of this post covers a few more technical aspects I think are worth mentioning.

### Ballot-level strategyproofness

There is a small bonus that follows from strategyproofness on dichotomous preferences. Since any approval ballot is a projection of a voter's preferences onto the dichotomous domain, if we read those preferences literally (the voter prefers all approved candidates over all unapproved candidates), we get a simple guarantee under Approval voting:

- If a candidate you plan to approve is already winning before you cast your ballot, your vote will not change the winner. In particular, your ballot will not cause an unapproved candidate to beat a candidate you approved.
- If an unapproved candidate is winning even after you cast your ballot, there is no deviation from the ballot you submitted that would change the outcome to someone your current ballot already approves.

This means your ballot is already doing maximal work for the candidates you approved against those you did not. It's a nontrivial guarantee that few other systems can claim.

Take [ranked choice voting](../ditch-rcv/){:target="_blank"}, for example, in the infamous 2022 Alaska race. [Over 33,000 voters](https://ranked.vote/report/us/ak/2022/08/cd) ranked Republican Sarah Palin first with fellow Republican Nick Begich second, implying they preferred Begich to Democrat Mary Peltola<d-cite key="rankedVote2022alaskaCd"></d-cite>, but Peltola won.

If fewer than 3,000 of those voters had instead insincerely ranked Begich first (burying Palin second), they could have elected Begich instead of Peltola. They were already signaling "Begich over Peltola," but the ranked system required them to misrepresent their ordinal preferences to make their ballots decisive. That is a failure of the voting rule to respect explicitly stated preferences. Similar events occurred in [Burlington, Vermont in 2009](https://ranked.vote/report/us/vt/btv/2009/03/mayor).

Under Approval, such voters could simply approve both Palin and Begich and get Begich instead of Peltola without misrepresenting their preferences. There is no need to exaggerate or hide preferences to get the system to respect them (e.g., your feelings about Palin shouldn't prevent Begich from winning over *Peltola* if he's preferred). If this reminds you of [IIA](../iia/){:target="_blank"}, that's no accident.

If a sufficient number of voters find Begich acceptable, he wins. Given that both hardcore Palin supporters and Democrats found Begich more acceptable than their alternatives, it's plausible Begich would have won under Approval.

In RCV, Begich arguably already had the numbers to beat Peltola, but the ballot mechanics prevented that preference from being expressed without strategic distortion. Approval voting avoids that problem: if Begich has the numbers to win, a vote for him won't backfire and cause him to lose. Simplicity here is an advantage.

Condorcet methods can fail this way--where insincerity is required to get the most preferred outcome (see [this post](../iia/){:target="_blank"}), and [this post](../approval-only/){:target="_blank"} shows a case in STAR where participation backfires. Approval's strict monotonicity prevents these pathologies.

However, you might still get a *better* outcome in Approval by extending or reducing your approval threshold, as in Example \ref{strategy-not-proof}. This is a **passive inefficiency** rather than the **active betrayal** seen in some ranked systems. So Approval is not perfectly strategyproof, but it does offer a valuable guarantee.

We can summarize this "ballot-level strategyproofness" property as the system taking your preferences at face value. In many other systems you may need to exaggerate or misrepresent preferences to get the system to listen. In Approval, your ballot means what it says, and the simpler design helps protect against weaponization of honest ballots against the voters who cast them.

It should be noted that choose-one plurality voting also has a form of ballot-level strategyproofness: when you vote for a candidate you are doing the best you can for that one candidate given the rules. But that protection is limited to that one candidate; Approval's protection extends to all approved candidates.

A further distinction is that for choose-one voting, you essentially have exactly one efficient strategy: voting for the more preferred of the top two candidates, which often requires betraying your favorite. In Approval voting, you can, in practice, change any efficient strategy into a sincere efficient strategy, because there's really no harm in voting for your favorite candidates, regardless of viability. Approval easily satisfies "no favorite betrayal" better than most, if not all, other systems.

### An Axiomatic Aside

As a final note, I want to briefly justify why "Yes" is an acceptable answer to the question "Is Approval voting strategyproof?" even though we can clearly see that it is not.

Brams and Fishburn proved Approval is strategyproof on dichotomous preferences in 1978<d-cite key="bramsFishburn1978approval"></d-cite>, but the connection between Approval and strategyproofness actually goes much deeper. In 2007, Mark Vorsatz proved that Approval voting is *uniquely determined* axiomatically by strategyproofness on the dichotomous domain along with other properties like strict positive-responsiveness<d-cite key="vorsatz2007approvalDichotomous"></d-cite> as a canonical extension of May's theorem<d-cite key="may1952simpleMajority"></d-cite>. But we will discuss this in a future post.

I would argue it's probably more accurate to say that the dichotomous domain inherently allows for strategyproofness, and Approval is simply the natural language of that domain, rather than "Approval happens to be strategyproof as a happy coincidental loophole to Gibbard's theorem<d-cite key="gibbard1973manipulation"></d-cite>." This manifests in real-world implementation of Approval voting as a genuine protection against explicit ballot backfiring, which we have seen in RCV elections in Burlington and Alaska.
