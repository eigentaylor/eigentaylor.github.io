---
layout: distill
title: Is Approval Voting Strategyproof?
date: 2026-05-31
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
      - name: Approval is strategyproof
  - name: The Game
    subsections:
      - name: Where to draw the line
      - name: Genuinely Dichotomous Preferences
  - name: Conclusion
  - name: Appendix
    subsections:
      - name: Ballot level strategyproofness
      - name: An Axiomatic Digression
---

## Introduction

This is a sort of "redo" of my second post on Approval voting, from November 2025. I was early on in my journey of learning about Approval voting, and I think I can explain this concept much better now (and far more concisely). This post is primarily based on the seminal 1978 paper by Brams and Fishburn <d-cite key="bramsFishburn1978approval"></d-cite>.

The question we are trying to answer in this post is a simple one:

> **Is Approval voting strategyproof?**

The short answer is:

![well yes, but actually no](/assets/img/wellyesbutactuallyno.jpg)

## What is strategyproofness?

Strategyproofness is a sort of slippery concept that's hard to define rigorously. Everyone can easily *grasp* the concept, but writing it down as a mathematical property is hard.

There is a straightforward definition in the context of [ranked voting systems](../gibbard-satt/){:target="_blank"}, but outside of that it's a little hard to articulate. Gibbard's seminal 1973 paper <d-cite key="gibbard1973manipulation"></d-cite> gave a super general and abstract definition, but Brams and Fishburn <d-cite key="bramsFishburn1978approval"></d-cite> gave a more specific definition in the context of Approval voting, which is what we use here. The following is a little oversimplified for pedagogical purposes.

> **Definition:** A strategy in Approval voting is **sincere** if there are no "holes" in the ballot. In other words, a voter draws a "line of acceptability" in their ranking and approves everyone above that line.
>
> A voting system is **strategyproof** if there is always only one "rational" strategy for any voter in any scenario, and that strategy is sincere.

Before I lose you, we need to be precise with the language! I know some people, particularly [Condorcetists](../condorcet-approval/){:target="_blank"}, who do not like this definition of the term "sincere". They don't like that a voter can have multiple sincere strategies! But this is what is used in the literature, so we will stick with it. A voter can thus be both sincere and strategic. For the pedants in the audience, the following blocks provide the formal definitions.

{% proof A remark on "rationality" %}
What we are calling "rational" is called "admissible" in the literature. Formally, it just means a strategy or ballot that is not "dominated" by any other strategy or ballot. In other words, there is no other ballot that would give you the same or a better outcome in all possible scenarios.

For example, why would you ever vote for a middle tier candidate, and not your favorite candidate? It doesn't hurt to include your favorite, because you might make them win! Similarly, you should never vote for your least favorite candidate, for the same reason.

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

In scenario 1, $A$ and $B$ are tied for first, with $C$ far behind. If you approve both $A$ and $B$, you preserve the tie (50/50 between your top two). If you approve only $A$, you break the tie and make your favorite win outright. So in scenario 1, the optimal ballot is $A$ only.

In scenario 2, $B$ and $C$ are tied for first, with $A$ far behind. If you approve only $A$, you leave the $B$-$C$ tie untouched (50/50 between your second choice and your least favorite). If you approve both $A$ and $B$, you break that tie for $B$ and fully block $C$. So in scenario 2, the optimal ballot is $A$ and $B$.

We have thus shown that there are two scenarios where someone with the same preference order must choose a different strategy to achieve the best outcome. Therefore, Approval voting is not strategyproof.

### Approval is strategyproof

Okay, why isn't the post over? We just proved that Approval voting is not strategyproof! Well, it turns out there's a little more to the story.

In 1978, when Brams and Fishburn published their seminal paper on Approval <d-cite key="bramsFishburn1978approval"></d-cite>, they proved that Approval voting is strategyproof under dichotomous preferences.

Dichotomous preferences are when a voter has two tiers of candidates: those who are "good", and those who are "bad". In other words, the voter is indifferent between all the candidates they consider "good", and also indifferent between all the candidates they consider "bad", but they strictly prefer all the candidates they consider "good" to all the candidates they consider "bad".

Strategyproofness comes directly from a nice result that they prove in the paper:

> **Theorem:** Any "rational" strategy in Approval voting involves voting for all candidates in a voter's top tier and no candidates in a voter's bottom tier. Nothing can be said about the candidates in any middle tier. (Corollary 1 <d-cite key="bramsFishburn1978approval"></d-cite>)

In other words, you have no reason to ever not approve of your absolute favorites, and you will never be compelled to approve of your absolute least favorites. This is not true in Approval with a runoff <d-cite key="fishburnBrams1981runoff"></d-cite>, which we will not be discussing here.

But, given this, strategyproofness is trivial under dichotomous preferences. Because you only have a top tier and a bottom tier, you approve all the candidates in your top tier and none of the candidates in your bottom tier. There are no middle tiers to worry about! So there is only one optimal strategy, and it is sincere. It is the pure, honest expression of your preferences. Thus, Approval voting is strategyproof under dichotomous preferences.

This can also be understood quite intuitively. If you don't support all of your "good" candidates, then you might fail to help break a tie between a good candidate and a bad candidate, which is bad. If you support any of your "bad" candidates, then you might help break a tie between a good candidate and a bad candidate in favor of the bad candidate, which is also bad. So you should support all of your "good" candidates, and none of your "bad" candidates.

## The Game

![let's play a game](/assets/img/playagame.gif)

Let's suppose you are an average tired voter. You see a crowded field of candidates (the current California Governor's race has [61 candidates on the ballot](https://elections.cdn.sos.ca.gov/statewide-elections/2026-primary/cert-list-candidates.pdf)), and you don't have the time or energy to properly rank all of them, let alone calculate the optimal strategy based on viability and polling. You just know that you like some of them, and you don't like the others. You have a choice to simplify the election into a kind of "game" as follows:

> If you only care about electing *any* "acceptable" candidate, however you define that, then you are adopting a dichotomous preference structure. You are saying, "I don't care which of these candidates wins, as long as it's not one of those other candidates."

We can call this a **dichotomous goal**.

Under such a goal, you are in the dichotomous domain where Approval is strategyproof. You can just approve of all the candidates you find acceptable, and that's that. In any other system, you have to make strategic considerations about which candidates to support, lest the system backfire and give you a worse outcome just for participating honestly.

Looking back at Example \ref{strategy-not-proof}, we can consider the two dichotomous goals:

- If your only acceptable candidate is $A$, then there's no reason to approve $B$.
- If your dichotomous goal includes both $A$ and $B$ as acceptable candidates, then you should approve both.

Except, not so fast. There are a couple of wrinkles to consider here. If your dichotomous goal is $A$ only, then in Scenario 2, you waste your vote on a nonviable candidate and allow a 50% chance to elect your least favorite. And if your dichotomous goal includes both $A$ and $B$, then you might fail to break a tie for your favorite $A$ in Scenario 1.

The latter is a little less problematic, since if you define both $A$ and $B$ as acceptable, then you still have a 100% chance to elect an acceptable candidate in Scenario 1. However, there is still room for strategic optimization, because both of the above scenarios failed to account for viability.

### Where to draw the line

We have not escaped strategy with the dichotomous goal. It's still prudent to consider the viability of your acceptable candidates. If the only candidates you find "acceptable" are completely nonviable, then this isn't exactly a particularly compelling strategy, especially if you could actually affect the outcome by expanding your definition of "acceptable" to include some more viable candidates. Laslier's leader rule is one such strategy to prudently draw the line of acceptability <d-cite key="laslier2009leaderRule"></d-cite>, but that is for another post.

However, if you feel, deep in your heart, that you can only stand to approve some candidates, viable or not, then Approval allows you to express this honestly and without judgment. And, unlike more complex systems, Approval [will not betray you for that choice (see the appendix)](#ballot-level-strategyproofness){:target="_blank"}.

This is, however, a point in favor of Approval with a top two runoff. Even if a voter fails to distinguish between the frontrunners, the runoff gives them another chance to influence the result. And although Approval with a runoff is more strategic and less sincere in theory with perfect knowledge <d-cite key="fishburnBrams1981runoff"></d-cite>, it can also make voters feel safer being more generous with their approvals, since they still have the runoff if they accidentally waste their vote.

### Genuinely Dichotomous Preferences

The truth is that, despite the fact that we *could* ask voters to rank candidates and distinguish between the candidates they like or don't like, many genuinely find dichotomous or binary "yes/no" as more natural.

"Vote blue no matter who" is a dichotomous preference structure. Any voter who would readily approve every single name with an "R" next to it and disapprove of everyone else is also acting as if they have dichotomous preferences. Single issue voters act dichotomously as well.

Many voters naturally and easily can categorize candidates into "acceptable" and "unacceptable" buckets, without much thought or effort. I would also argue that [compromise](../why-condorcet/){:target="_blank"} and consent are inherently binary concepts.

I look at this all as something simpler. Approval voting is the natural language of compromise. From this perspective, every voter tells the system who they find "acceptable", and the candidate who has earned consent for their support from the largest group has earned the right to be called the consensus choice. Approval isn't perfect at capturing compromise, no voting system truly can, but I believe it is closer than any other voting method because it is *asking the right question*.

## Conclusion

As I explored in [this post](../why-condorcet/){:target="_blank"}, I think compromise and consent are incompatible with a ranked ballot. Two voters can give the same preference *order*, but disagree on who they would find genuinely acceptable as their representative (who they would be willing to compromise on). "Second choice" does not imply "acceptable backup", and could instead mean "lesser evil" (or vice versa). Scores can be exaggerated and ambiguous. Is a 3/5 "acceptable" or not?

Acceptability isn't naturally categorized by ordinal rankings or utility scores. In that sense, Approval stands alone in most strongly capturing "satisfaction" from an election. And I think that is something that we, in this polarized time, should [seriously consider](../approval-only){:target="_blank"}.

Many like to point to Approval as a "highly strategic" system, as if that is a bad thing. I would instead argue that Approval is a system where strategy is optional. And, as expanded on in the appendix, Approval is one of the few systems you can trust to take your expressed preferences at face value, without needing to exaggerate or misrepresent them to get the system to listen to you.

This is how strategyproofness on dichotomous preferences manifests in the real world, and I think it's a genuinely strong point in its favor.

## Appendix

The remainder of this post is dedicated to a few bonus topics I think should be mentioned.

### Ballot level strategyproofness

There is one nice little bonus that we get from strategyproofness on dichotomous preferences. Since any approval ballot is necessarily a projection of the voter's preferences onto the dichotomous domain, if we take those preferences completely literally (the voter prefers all approved candidates over all unapproved candidates), then we do actually get a comfy little guarantee under Approval voting:

If an unapproved candidate is currently winning, then there is *no deviation* from your current ballot to change the outcome to an approved candidate. That means your ballot is already doing maximal work for all the candidates you voted for. This is a nontrivial guarantee that essentially no other system can claim.

Take [ranked choice voting](../ditch-rcv/){:target="_blank"}, for example, in the infamous 2022 Alaska race. [Over 33,000 voters](https://ranked.vote/report/us/ak/2022/08/cd) ranked Republican Sarah Palin first with Nick Begich as a second choice, implying that they preferred Begich over Democrat Mary Peltola <d-cite key="rankedVote2022alaskaCd"></d-cite>, but Peltola won.

However, if fewer than [3,000 of those voters](https://substack.com/@whelmedcitizen/p-182659376) <d-cite key="mahlendorf2026fearVoteSplitting"></d-cite> had instead insincerely ranked Nick Begich as their first choice, burying their favorite Palin second, then they would have elected Begich instead of Peltola (their backup instead of their worst nightmare).

Notice, they were *already* saying, "I want Begich over Peltola!", but they needed to lie about how they felt about Sarah Palin to actually get the system to *respect* that preference. *That* is a strategyproofness violation.

In Approval, we can say that if you are already approving Begich and not approving Peltola, but Peltola is winning, then no matter how you change your ballot, you will not be able to get Begich to win instead of Peltola. You are already doing the best you can for Begich, and the system hears you loud and clear on that preference. There is no need to exaggerate or misrepresent that specific preference to get the system to respect it.

In RCV, Begich *already* had the numbers to beat Peltola, but the system was just too convoluted and dumb to acknowledge that fact. Approval voting does not have that problem. This is where simplicity can be an advantage.

Even Condorcet methods, which try to interpret your ranked ballot faithfully, are still open to failures like this [as seen in this post](../iia/){:target="_blank"}. That post also includes an example in SCORE voting where the exact same thing occurs. And [this post](../approval-only/){:target="_blank"} shows an example in STAR voting where participation leads to your worst outcome. Approval's strict monotonicity prevents such pathologies.

However, it could still be that you could get a *better* outcome in Approval by extending or reducing your approval threshold, as we saw in Example \ref{strategy-not-proof}. This can be articulated as a "failure to help" (**passive inefficiency**), versus **active betrayal**. So, again, Approval is not perfectly strategyproof, but still a nice little guarantee.

We can summarize this "ballot level strategyproofness" property as the system taking your preferences at face value. In any other system, you may need to exaggerate or misrepresent your preferences to get the system to listen to what you tell it. Or, perhaps, participating at all can lead to a strictly *worse* outcome. *Not* in Approval. In Approval, your ballot means *exactly* what it says. In these other systems, the more expressive ballot can backfire and be weaponized against you. Approval's simpler, more straightforward design protects you from such things. That's worth something, in my opinion.

It should be mentioned that Choose-one plurality voting also has ballot level strategyproofness. When you vote for a candidate, you are also doing the best you can for that candidate given the constraints of the system. However, the scope of this protection is limited to *one* candidate, making passive inefficiency more likely. Whereas in Approval, this ballot level strategyproofness extends to all of your approved candidates against all other candidates.

### An Axiomatic Digression

Brams and Fishburn proved Approval is strategyproof on dichotomous preferences in 1978 <d-cite key="bramsFishburn1978approval"></d-cite>, but the connection between Approval and strategyproofness actually goes much deeper. In 2007, Mark Vorsatz proved that Approval voting is *uniquely determined* axiomatically by strategyproofness on the dichotomous domain along with other properties like strict positive-responsiveness <d-cite key="vorsatz2007approvalDichotomous"></d-cite> as a canonical extension of May's theorem <d-cite key="may1952simpleMajority"></d-cite>. But we will discuss this in a future post.

I would argue it's probably more accurate to say that the dichotomous domain inherently allows for strategyproofness, and Approval is simply the natural language of that domain. As opposed to "Approval happens to be strategyproof as a happy coincidental loophole to Gibbard's theorem <d-cite key="gibbard1973manipulation"></d-cite>." This manifests in real world implementation of Approval voting as a genuine protection against explicit ballot backfiring which we have seen in RCV elections like Burlington and Alaska.
