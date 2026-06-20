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

I made a post recently about why I do not believe [that the Condorcet winner is necessarily the true compromise choice](../why-condorcet/){:target="_blank"}. The Condorcet winner being the candidate who would defeat all others in a head-to-head matchup, based on preference rankings. To summarize it in one sentence: ordinal preference says nothing about "acceptability".

Consent, acceptability, consensus, compromise--I believe these are all independent of ordinal preference. If I tell you that I prefer candidate A over candidate B over candidate C, you have no idea how I feel about any candidate. Is candidate B, for all intents and purposes, *almost* as good as candidate A? Or is candidate B a lesser evil that I only hate marginally less than candidate C? Or are all three largely acceptable, and my preferences between them are merely subtle distinctions?

I think I made my point when it comes to ordinal preferences in that previous post. However, I'd like to tackle the distinction between approval and "scores" and "utility".

From one perspective, sure, Approval is just a "degenerate" score system where the range of possible scores is limited to two values: 0 and 1. However, I think that's an oversimplification. Because *where* do you draw the line?

Compare this to a 0-5 score system, that you might see on a STAR voting ballot. Which score is an "approval"? Well, 5/5 is surely an approval, right? 0/5 is surely a disapproval. 4/5, though? Probably an approval, I suppose. But what about 3/5? Or 2/5? The line becomes increasingly blurry, and different voters might draw it in different places. *This is precisely the problem, which shows the lack of a direct correspondence between utility and approval.*

Based on a conversation with Clay Shentrup, he said something that really stuck with me. He is very strongly in favor of the idea of "utility". He essentially argued that to truly compare voting systems, you have to use a utility model. We will never be able to extract utilities from real voters, so a simulation is as close as you can get to compare apples to apples. Hence, he is a big proponent of VSE simulations<d-cite key="quinn2017vseSummary"></d-cite>.

A claim I have heard often is that there is no such thing as "acceptability"; only utility.

Utility, in the context of voting, refers to a numerical representation of a voter's satisfaction or preference for a particular candidate. The higher the utility, the more a voter prefers that candidate. For simplicity, we will represent utilities as scores in $[0,1]$, in the form of scores out of 5, to match SCORE voting ballots. We can denote the utility of a candidate as $u(c)$.

We can imagine that we can translate between different granularities of scoring systems. For example, a 4/5 is the same as an 8/10. But how do you compress things down? If we want to go down below to the binary scale of Approval, then we need some sort of map or function. The only map to $$\{0,1\}$$ that makes sense to me is a threshold:

$$\phi(c)=\mathbf{1}[u(c)\geq \tau]$$

where $\tau$ is the threshold utility above which a candidate is considered "approved" and $\mathbf{1}[{\{...\}}]$ is the indicator function, which is 1 if the condition inside the braces is true and 0 otherwise.

My problem with the idea that acceptability is determined by utility is that I do not believe there is a single canonical $\tau$. Is a 3/5 acceptable or not?

[Laslier's leader rule](../leader-rule/){:target="_blank"} <d-cite key="laslier2009leaderRule"></d-cite> proves the best response to a particular probability model is to define your threshold $\tau$ to be equal to the utility of the expected winner, or right above it.

Consider a voter who rates candidate A as a 5/5, candidate B has a 4/5, candidate C as a 1/5, and candidate D as a 0/5.

If Candidate A is the expected winner, then the leader rule says there's no reason to compromise and approve anyone else. The voter has leverage, and no need to compromise. The threshold in this scenario is very high, because their expected outcome is very positive.

If, instead, candidate D is the expected winner, then the leader rule suggests that the voter should approve of candidates A, B, and C. In such a scenario, the voter has no leverage, and even though they are very unenthusiastic about C, it's certainly a compromise over their worst nightmare outcome, D.

What a voter finds "acceptable" is relative and exogenous to their pure utilities. For that reason alone, I claim that the Approval ballot does, in fact, contain information that cannot be found in a score ballot alone. That is, a 0-5 star score is insufficient to determine whether that option is acceptable or not. Correlated? Sure, but I reject the premise that utilities can tell you everything that an Approval ballot can.

I call this threshold a "line of acceptability". It represents the point at which a voter considers a candidate to be acceptable--who they consent to give their support to through their ballot.

I like to think of a ballot as a projection of a voter's nuanced and complex human experience down to some domain the voting system can easily aggregate. Rankings eliminate the distance and intensity, reducing the rich spectrum of preferences to a simple order. Score ballots retain some sense of intensity but still compress the full experience into numerical values. Approval ballots, on the other hand, capture a binary notion of acceptability, which is information that neither rankings nor scores fully convey.

The binary land of 0 or 1 is called the "dichotomous domain", on which [Approval is strategyproof](../av-stratproof/){:target="_blank"}<d-footnote>Soon I will write a blog post about Approvals wonderful mathematical perfection on this domain. <d-cite key="vorsatz2007approvalDichotomous"></d-cite> <d-cite key="maniquetMongin2015approvalArrow"></d-cite></d-footnote>. To put it simply, Approval voting takes what you tell it at face value and treats that simple signal with full fidelity.

The kicker? Despite this coarser, seemingly less expressive ballot, the outcomes under Approval are often as good as, or even better than, those under more expressive systems<d-cite key="quinn2017vseSummary"></d-cite>. See [this model, which is a work in progress](https://eigentaylor.github.io/satisficing-voter-sim/). In this model, the slight edge that systems like STAR have over Approval begin to disappear when voters are misinformed by epistemic noise and easily fatigued by the ballot.

The crux of my argument is this: **Acceptability is not derivable from utility alone.** It is a fundamentally different dimension of information--one that depends on context, expectations, and the voter's strategic position. A score ballot tells you how much a voter likes a candidate in isolation. An approval ballot tells you something more: whether that candidate crosses the threshold of being someone the voter is willing to help win.

This is not a limitation of Approval voting; it is precisely why Approval voting works so well. By focusing on this single, clear question--"Do you consent to this candidate?"--rather than trying to squeeze out numerical precision from voters' nebulous utilities<d-footnote>Particularly if voters are not engaged enough to give these meaningful numerical distinctions, a more expressive system risks collecting noise rather than signal. There is also the question of if more granular scores actually encourage honest expression or exaggeration, which I will not be addressing here.</d-footnote>, Approval voting captures something real and meaningful that scoring systems obscure.

The utility model assumes that voters have well-defined preferences that exist independently of circumstance. But real democracy is not conducted in a vacuum. Voters care about their relative power, their strategic position, and what futures are actually plausible.

The acceptability threshold embodies this lived reality. A voter in a close election genuinely does consider their fourth-choice candidate differently than they would in a blowout--not because their utility changed, but because the decision of whether to consent to that candidate changed. Approval voting respects this truth. And in doing so, it reveals something that the pursuit of utility-based perfection often misses: that democracy is fundamentally about consent, not optimization.
