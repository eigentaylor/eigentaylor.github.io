---
layout: distill
title: Consent is Binary
date: 2026-06-19
description: What an Approval ballot captures that scores and rankings cannot.
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
theorems: true
related_posts: true
pretty_table: true
exclude_appendix_from_word_count: true
exclude_footnotes_from_word_count: true
exclude_proof_blocks_from_word_count: true
bibliography: voting.bib
chart:
  plotly: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
---

I made a post recently about why I do not believe [that the Condorcet winner is necessarily the true compromise choice](../why-condorcet/){:target="_blank"}. The Condorcet winner is the candidate who would defeat all others in a head-to-head matchup, based on preference rankings. To summarize it in one sentence: ordinal preference says nothing about "acceptability".

Consent, acceptability, consensus, compromise--I believe these are all independent of ordinal preference. If I tell you that I prefer candidate A over candidate B over candidate C, you have no idea how I truly feel about any candidate. Is candidate B a wonderful backup choice or a lesser evil?

I think I made my point when it comes to ordinal preferences in that previous post. However, I'd like to tackle the distinction between approval and "scores" and "utility".

Approval voting is a system where each voter can indicate approval or disapproval for each candidate independently. Voters can approve of as many candidates as they find acceptable, and the candidate who earns the approvals from the largest subset of voters is the winner.

From one perspective, sure, Approval is just a "degenerate" score system where the range of possible scores is limited to two values: 0 and 1. However, I think that's an oversimplification. Because *where* do you draw the line?

Compare this to a 0-5 score system that you might see on a STAR voting ballot. Which score is an "approval"? Well, 5/5 is surely an approval, right? 0/5 is surely a disapproval. 4/5 is probably an approval, I suppose. But what about 3/5? Or 2/5? The line becomes increasingly blurry, and different voters might draw it in different places. *This is precisely the problem, and shows the lack of a direct correspondence between utility and approval.*

Clay Shentrup said something that really stuck with me. He is very strongly in favor of the idea of "utility". He essentially argued that to truly compare voting systems, you have to use a utility model. We will never be able to extract utilities from real voters, so a simulation is as close as you can get to an apples-to-apples comparison. Hence, he is a big proponent of VSE simulations<d-cite key="quinn2017vseSummary"></d-cite>.

A claim I have heard often is that there is no such thing as "acceptability"; only utility.

Utility, in the context of voting, refers to a numerical representation of a voter's satisfaction or preference for a particular candidate. The higher the utility, the more a voter prefers that candidate. For simplicity, we will represent utilities as scores in $[0,1]$, in the form of scores out of 5, to match SCORE voting ballots. We can denote the utility of a candidate as $u(c)$.

Voters *somehow* translate their utilities to numerical scores on some scale <d-cite key="baujard2018how"></d-cite>. If we want to go down below to the binary scale of Approval, then we need some sort of map or function. The only map to $$\{0,1\}$$ that makes sense to me is a threshold:

$$\phi(c)=\mathbf{1}[u(c)\geq \tau]$$

where $\tau$ is the threshold utility above which a candidate is considered "approved" and $\mathbf{1}[{\{...\}}]$ is the indicator function, which is 1 if the condition inside the braces is true and 0 otherwise.

I call this threshold a "line of acceptability". It represents the point at which a voter considers a candidate to be acceptable--who they consent to give their support to through their ballot.

My problem with the idea that "there is no such thing as acceptability; only utility" is that I do not believe there is a single canonical $\tau$. Even if I gave you my *exact* utilities for every single candidate, that's still insufficient to know my line of acceptability--the threshold $\tau$ that determines which candidates I consider "acceptable" enough to consent to give my support to through my ballot.

[Laslier's leader rule](../leader-rule/){:target="_blank"} <d-cite key="laslier2009leaderRule"></d-cite> proves the best response to a particular probability model is to define your threshold $\tau$ to be equal to the utility of the expected winner, or right above it.

- If you prefer the leader $L$ to the challenger, your approval ballot is $$\{X:u(X)\geq u(L)\}$$
- If you prefer the challenger to the leader $L$, your approval ballot is $$\{X:u(X)>u(L)\}$$<d-footnote>This is the actual formulation of the leader rule in Laslier's paper, which I did not use in my post on the leader rule. But Laslier does indeed propose setting the infimum of your utility threshold to precisely the utility of the expected winner.</d-footnote>

Consider a voter who rates candidate A as a 5/5, candidate B as a 4/5, candidate C as a 1/5, and candidate D as a 0/5.

If their 5/5 Candidate A is the expected winner, then the leader rule says there's no reason to compromise and approve anyone else. The voter has leverage, and no need to compromise. The threshold in this scenario is very high, because their expected outcome is very positive.

If, instead, the 0/5 candidate D is the expected winner, then the leader rule suggests that the voter should approve of candidates A, B, and C (anyone better than a 0/5). In such a scenario, the voter has no leverage. And even though they are very unenthusiastic about C, it's certainly a compromise over their worst outcome, D. Approval becomes a relative measure. Compared to the expected 0/5 outcome, a 1/5 outcome becomes relatively more acceptable, and the voter is willing to approve it as a compromise.

What a voter finds "acceptable" is relative and exogenous to their pure utilities. For that reason alone, I claim that the Approval ballot does, in fact, contain information that cannot be found in a score ballot alone. That is, a 0-5 star score is insufficient to determine whether a candidate is acceptable or not. Correlated? Sure, but I reject the premise that utilities can tell you everything that an Approval ballot can.<d-footnote>Clay Shentrup made an interesting point that approvals are a function on utilities <em>and</em> beliefs. This is in agreement with my point that there is no canonical map from utilities to approval.</d-footnote>

I like to think of a ballot as a projection of a voter's nuanced and complex human experience down to some domain the voting system can easily aggregate. Rankings eliminate the distance and intensity, reducing the rich spectrum of preferences to a simple order. Score ballots retain some sense of intensity but still compress the full experience into numerical values.<d-footnote>There is also the matter of "exaggeration". The fact that STAR voting even exists at all is proof that there is arguable value to trying to correct for exaggeration in score ballots, where voters might inflate or deflate their scores strategically rather than expressing their true intensity of preference. The grade scale itself also influences how voters use the system <d-cite key="baujard2018how"></d-cite>. Voters in an experiment by Baujard et al. graded candidates differently on a (-1,0,1) scale than a (0,1,2) scale. Hence, a more granular scoring system is not necessarily a more direct function on utilities, and instead can be warped and distorted by the strategic considerations and the psychological framing imposed by the voting system itself.</d-footnote>

Approval ballots, on the other hand, limit the expression of voter preferences to a binary choice and capture a binary notion of acceptability, which is information that neither rankings nor scores fully convey.

The binary land of 0 or 1 is called the "dichotomous domain", on which [Approval is strategyproof](../av-stratproof/){:target="_blank"} <d-cite key="bramsFishburn1978approval"></d-cite>. To put it simply, Approval voting takes what you tell it at face value and treats that simple signal with full fidelity. I do believe that in *some* ways this makes Approval a more "honest", or at least straightforward, system for the layperson.

The kicker? Despite this coarser, seemingly less expressive ballot, the outcomes under Approval are often as good as, or even better than, those under more expressive systems<d-cite key="quinn2017vseSummary"></d-cite>. See [this model, which is a work in progress](https://eigentaylor.github.io/satisficing-voter-sim/), where the slight edge that systems like STAR have over Approval begins to disappear when voters are misinformed by epistemic noise and easily fatigued by the ballot.

The crux of my argument is this: **Acceptability is not derivable from utility alone.** It is a fundamentally different dimension of information--one that depends on context, expectations, and the voter's strategic position. A score ballot tells you how much a voter likes a candidate in isolation. An approval ballot tells you something more: whether that candidate crosses the threshold of being someone the voter is willing to help win.

This is not a limitation of Approval voting; it is precisely why Approval voting works so well. By focusing on this single, clear question:

> "Do you consent to this candidate?"

rather than trying to squeeze out numerical precision from voters' nebulous utilities<d-footnote>Particularly if voters are not engaged enough to give meaningful numerical distinctions, a more expressive system risks collecting noise rather than signal.</d-footnote>, Approval voting captures something real and meaningful that scoring systems obscure.

The utility model assumes that voters have well-defined preferences that exist independently of circumstance. But real democracy is not conducted in a vacuum. Voters care about their relative power, their strategic position, and what futures are actually plausible.

The acceptability threshold embodies this lived reality. A voter in a close election between their top two choices genuinely does consider their second-choice candidate differently than they would in an expected blowout for their third-choice--not because their utility changed, but because the decision of whether to consent to that candidate changed. Approval voting respects this truth. And in doing so, it reveals something that the pursuit of utility-based perfection often misses: that democracy is fundamentally about consent, rather than optimization.
