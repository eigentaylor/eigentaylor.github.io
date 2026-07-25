---
layout: distill
title: 'Coarse Correction: Is STAR Actually More Accurate than Approval?'
date: 2026-07-24
description: How adverse conditions might make Approval, and delayed runoffs, more robust than a more granular and expressive voting system like STAR.
importance: 2
tags: voting
category: polisci
featured: false
theorems: true
bibliography: voting.bib
chart:
  plotly: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: Equal Vote Coalition (Volunteer)
toc:
  - name: Introduction
  - name: The Adverse Parameters
    subsections:
      - name: Epistemic Noise
      - name: Unfamiliarity
      - name: Fatigue
      - name: How These Combine
  - name: The Runoff Assumptions
    subsections:
      - name: Justification
  - name: Findings
    subsections:
      - name: The Approval-STAR Gap
      - name: Condorcet Efficiency
      - name: SCORE vs STAR
      - name: Better Choices Proposals
  - name: The Jupyter Notebook
  - name: Conclusion
---

## Introduction

Voter Satisfaction Efficiency (VSE) <d-cite key="quinn2017vseSummary"></d-cite> is an incredible metric used for evaluating the performance of voting systems. It gives a numeric percentage to the "accuracy" of a voting system, with 0% being just a system that randomly chooses a winner, and 100% being a system that always elects the "best" (highest utility) candidate.

These are, of course, just simulations, however. VSE does not say anything about candidate entry, voter turnout, or other real-world factors that can shape the dynamics of the government that uses a given voting system to elect their leaders.

I interpret VSE as just a simple measure of "aggregation competence": how well a voting system can aggregate the preferences that are fed into it. If a system is *good*, then it almost surely has solid VSE. Choose-one voting, for example, has awful VSE when voters are simulated to just vote honestly. This is because the system is so coarse that it cannot look beyond the top choice of each voter, and thus consensus candidates are often buried by vote-splitting.

The Equal Vote Coalition pushes three systems, which all have high VSE: STAR, Approval, and Condorcet<d-footnote>Technically, they champion their particular flavor of Condorcet, "Ranked Robin", but the differences are minor and not relevant to this discussion. In what follows, we will focus on the Schulze method, which is particularly robust and used in a number of organizations for their internal elections.</d-footnote>:

- Approval voting: Voters can approve of as many candidates as they like, and the candidate with the most approvals wins. This is a system with surprisingly high VSE (up to about 95%) for its simplicity.
- Condorcet methods: Voters rank candidates and the candidate who defeats all others is the winner (with some tiebreaker if no candidate is a Condorcet winner). This system gets up to about 98% VSE, though its lower bound is fairly low under strategic voting, despite the fact that strategic voting is just [not very effective in Condorcet methods](./better-choices-strategy/). The fact is, pairwise dominance (while not a prerequisite for being the utility maximizer) is objectively a strong predictor of high utility.
- STAR voting: Voters score candidates on a scale (usually 0-5), and the two highest-scoring candidates go to an automatic runoff where a candidate gets one point for every voter who scored them higher than the other candidate. This system has the best VSE range of the three (reported to be about 91%-98%).

I will not pretend that I am not [partial to Approval voting over STAR voting](./approval-only/). In fact, one of the reasons is just how close the VSE of the simpler Approval is nearly competitive with the far more complex and expressive STAR.But, alas, I cannot ignore the fact that STAR simply has better VSE than Approval. And STAR proponents are not shy about pointing this out. On the [Better Voting website](https://bettervoting.com/), they list Approval as being "recommended for simplicity", and STAR as being "recommended for accuracy".

But what if that's not actually true? I have been somewhat skeptical about some of the assumptions that go into VSE simulations, that I don't believe are particularly realistic. Perhaps we need to put an asterisk on STAR's high VSE<d-footnote>This is actually an epic pun because asterisk derives from the Greek word "asteriskos," meaning "little star."</d-footnote>. Some questions that I would like to raise are:

1. Do voters *actually* know their true utilities for all the candidates on the ballot? Might some voters *think* they prefer $B$ over $A$, but would actually be happier if $A$ won than $B$? If they score $B$ higher than $A$, and the runoff is between $A$ and $B$, then this voter will accidentally vote *against* their interests in the runoff step.
2. What if voters have never heard of some of the candidates? If the utility maximizer is someone a voter is not aware of, then they are not likely to score them highly, hurting their chance of winning.
3. What of voters who get fatigued by the more complex ballot? As easy as "score the candidates 0-5 like your Uber driver" might sound, voters often do not have the patience to seriously consider every candidate. Once we go beyond just selecting a single name, we have to consider that some voters are going to give up and not fill out the entire ballot, regardless of the method we use.

The common thread here is that a complex and expressive system like STAR is designed to take in more information from voters to deliver better outcomes than a more coarse system like Approval. But what if the data it collects is noise rather than signal?

One particular concern I have with this is that the runoff is *automatic*. A voter who is misinformed when they cast their initial score ballot cannot change their mind later if they realize that they were wrong. You don't know what you don't know. And many voters *are* tired and busy, and don't have time to read the campaign websites of all [61 candidates on the ballot](./ca-top-2/). In a delayed runoff, voters have a chance to familiarize themselves with the candidates in the narrowed field, and can make a more informed choice.

This led me to the following hypotheses:

1. If the preferences and data that voters provide are noisy or incomplete, a more coarse system like Approval will actually be more robust than a more expressive system like STAR to that degradation in voter information. In other words, STAR's advantage over Approval is not robust to adverse conditions.
2. A delayed runoff is more robust than an automatic runoff if the voters in the primary step are misinformed or fatigued, and that noise is reduced in the runoff step.

In this post, my primary evidence is a Jupyter notebook that uses the original VSE simulation code with significant modifications to test these hypotheses. It was written with AI-assisted with Claude Code, but the code is included for full transparency and reproducibility. I look forward to someone who is a more skilled coder than I am to improve upon it, and perhaps extend the model. I have no doubt someone is going to find a bug in my code, or an assumption that is not particularly realistic. I welcome that, and hope that this post can be a jumping-off point for further research into the robustness of these systems.

Spoiler alert: STAR's advantage over Approval narrows or even reverses under even mildly adverse conditions, and Approval Top-2 is significantly more robust than STAR even when the runoff conditions are only mildly improved.

## The Adverse Parameters

We define three parameters that we can adjust to simulate adverse conditions for voters:

### Epistemic Noise

We add noise to the voter's perceived utility of each candidate, simulating the fact that voters are often misinformed or otherwise unable to accurately evaluate the candidates.

If $u_i(c)$ is the true utility of candidate $c$ for voter $i$, then we can define a voter's perceived utility as:

$$u'_i(c) = t\cdot u_i(c) + \sqrt{1-t^2}\cdot \sigma_i \cdot \epsilon_{ic}$$

$$\text{perceived}{ij} = t \cdot \text{true}{ij} + \sqrt{1 - t^2} \cdot \sigma_i \cdot \text{noise}_{ij}$$

Where $\epsilon_{ic} \sim N(0,1)$. Then $t$ is exactly the Pearson correlation coefficient between the true and perceived utilities, scaled by the voter's utility variance $\sigma_i$. If $t=1$, then the voter is perfectly informed, and if $t=0$, then the voter's perceived utilities are pure noise. We use one global $t$ for all voters.

### Unfamiliarity

We draw an awareness/prominence ranking for each election, simulating that everyone knows the frontrunner, but as you go down the number of voters who are aware of each candidate decreases. The probability that a voter is aware of candidate $c$ is given by:

$$P_{\text{aware}}(c) = \texttt{AWARENESS_L}^{\text{prominence_rank}(c)}$$

This ranking is independent of candidate quality, representing how a terrible candidate can have excellent name recognition, and a great candidate can be a complete unknown. At $\text{AWARENESS}_L=1$, all voters are aware of all candidates, while at lower values, fewer voters are aware of the candidates lower in the awareness ranking.

### Fatigue

While prominence is global to the election, fatigue is local to the voter. We draw a random fatigue ranking for each voter, as a stand-in for ballot-order rotation. As voters go down the ballot, they are more likely to be fatigued and simply stop looking at names. Maybe they need to pick up their kids from soccer practice, or they came from a long day at work, or they just don't care. The probability that a voter is not fatigued enough to vote for candidate $c$ is given by:

$$P_{\text{not fatigued}}(voter, c) = \texttt{FATIGUE_L}^{\text{fatigue_position}(voter, c)}$$

### How These Combine

Unfamiliarity and fatigue interact in an interesting way. To be able to vote for a candidate, a voter must be both aware of them and not fatigued. So the probability that a voter votes for candidate $c$ is given by:

$$P_{\text{genuine}} = P_{\text{aware}} \times P_{\text{not fatigued}}$$

If the check fails, then the utility for that candidate is set to be equal to that of their least liked known candidate. This simulates the voters to basically say "I don't know them, so I'll leave them off my ballot".

## The Runoff Assumptions

This model essentially turns voters from robots, patient enough to thoughtfully evaluate and vote for all candidates, into messy humans who are often misinformed, fatigued, or otherwise unable to know which candidates would actually make them happiest. We would like to know how much of a difference a lower noise delayed runoff, with finalists selected with a more coarse system like Approval, can make in the overall accuracy of the election compared to a more granular system like STAR, taking in poor data.

My hypothesis is that the runoff step can act as a corrective mechanism for misinformed voters in the primary step, whereas the more complex single-round mechanism suffers from "garbage in, garbage out" issues.

However, there are a few ways that we could model improved voter information in the runoff step.

We assume that in the primary election (say, in June) has tired voters who didn't have time to research all candidates in the crowded field. They vote imperfectly based on their limited knowledge (ex. vibes, not reading the candidate's website). But just how much more informed are voters in the runoff (say, in November)?

Under the most pessimistic conditions, we could imagine that the voter has absolutely no time to update their beliefs. Almost like the runoff step is that same day, or done right after casting their primary ballot (or perhaps, they fell into a brief coma). We do not assume this, but do measure it later on.

Under slightly more optimistic conditions, we can suppose that in the time between the primary and runoff, voters at least know who everyone in the runoff step actually are, though their preferences could still be noisy and in the wrong direction. This is how we define the basic runoff systems.

The most optimistic assumption is that voters have had time to research the candidates in the runoff step, watching the debates, reading the websites, and generally becoming more informed about the candidates. This is how we define the "noiseless" runoff systems.

### Justification

I will not pretend that these assumptions are not particularly optimistic for a delayed runoff (especially for Approval Top-2). Indeed, I might even call it "cheating"! However, I think seeing what the simulations actually say when we suppose that a runoff step could genuinely act as a corrective mechanism for the misinformed voters in the primary step is important.

We can at least see how *much* of a difference it makes. Further, we do, in fact, measure the range of conditions between the pessimistic and optimistic assumptions, compared to a STAR baseline. We will see that even under exceptionally minimal improvements in the runoff step, Approval Top-2 gains an advantage over STAR.

## Findings

Before we get into the code, I'd like to summarize some of the things I found.

### The Approval-STAR Gap

Under perfect conditions, STAR is objectively more accurate than Approval. However, the VSE gaps narrows under all friction scenarios. The systems calculate essentially have equivalent VSE. The gap is too small to strongly conclude that it fully narrows, but it is certainly suggestive that STAR's advantage is not robust to adverse conditions.

Approval Top-2, on the other hand, clearly wins out in simulations. It's not even close. Even under mild adverse conditions, Approval Top-2 is more accurate than STAR, and this grows as the adverse conditions worsen. This is with and without removed noise in the runoff step. As long as voters at the very least *are* or *become aware* of both candidates in the runoff step, even if they are misinformed about their true utilities, Approval Top-2 still manages to outperform STAR by a mile. This gap widens if voters are assumed to be perfectly informed in the runoff step.

### Condorcet Efficiency

This is a little funnier. Under ideal conditions, Schulze has 100% Condorcet efficiency, as expected. However, under adverse conditions, the system designed specifically to elect the Condorcet winner becomes worse at electing the true Condorcet winner than STAR, Approval Top-2, *and* even base Approval (though the gap is very small except for Approval Top-2). It seems that Cardinal systems, at least in this model, are actually better at electing the Condorcet winner than a system designed specifically to do so.

Even Plurality Top-2 did exceptionally well, by the runoff alone. I also implemented Plurality Top-3 Condorcet (and Approval Top-3 Condorcet) [as per the Better Choices system](../better-choices), and these did even better than the Top-2 versions (unsurprisingly, particularly for a race with only 6 candidates, advancing half the candidates is bound to greatly increase the chance of the Condorcet winner being in the runoff).

It appears that if your desire is truly to elect the Condorcet winner no matter the cost, then a runoff method is the way to go if voters are not ideal.

### SCORE vs STAR

I also measured the difference between STAR voting and just plain 5-point scoring (SCORE). The difference is negligible, but SCORE appears to have a slight edge under high friction. STAR gains its edge back as conditions become more ideal.

I had wondered if the adverse conditions might damage outcomes significantly because voters would accidentally vote against their interest in the runoff step. This seemed to have a small effect, but not particularly significant. In evaluating STAR versus SCORE, I found that the difference in VSE was negligible.

### Better Choices Proposals

I also implemented the Better Choices proposals for Top-3 Condorcet under both a Plurality and Approval primary. These did exceptionally well, particularly the Approval Top-3 Condorcet. However, with three candidates the idealized perfect runoff seems even more of a stretch. If we suppose that noise and awareness are less improved with three candidates than two, then it's not immediately obvious if Approval Top-2 would actually perform worse than the Top-3 methods (though I suspect it would).

The surprise is how much better Plurality Top-3 Condorcet does than Approval Top-2. It seems that for a small number of candidates (like 6, the default of the simulations) means that taking in an extra candidate has a greater impact than Approval in the primary.

This ambiguous advantage disappeared immediately as the number of candidates increased. Taking in one more candidate does not offset the issues of vote-splitting that Approval remedies.

However, Approval Top-3 Condorcet may be the most robust system overall considered here. If Better Choices chooses to use Approval rather than Plurality in the primary of their Condorcet Top-3, they may have the best of both worlds. However, Approval Top-2 is also exceptionally robust, far simpler, and already in use in St. Louis <d-cite key="sargent2025stlouis"></d-cite>.

## The Jupyter Notebook

{::nomarkdown}
{% assign verification_jupyter_path = 'assets/jupyter/vse_simulation.ipynb' | relative_url %}
{% capture verification_notebook_exists %}{% file_exists assets/jupyter/vse_simulation.ipynb %}{% endcapture %}
{% if verification_notebook_exists == 'true' %}
  {% jupyter_notebook verification_jupyter_path %}
{% else %}
  <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}

## Conclusion

It is absolutely undeniable that, with perfectly informed voters who fill out their ballots completely and accurately, STAR is an objectively more accurate mechanism than Approval. That granularity is a genuine strength when the data is high quality. However, that granularity becomes a liability when the data you collect is noisy or incomplete.

Based on this, I would say that for something like a committee trying to decide between options, STAR would be an excellent choice. Perhaps, a City Council trying to decide between a few different options for a new park. Highly informed voters who will give full and thoughtful scores to all available options could be easily expected to produce higher quality outcomes than the council members simply approving of which options they like.

Electing a city council, however, is a different story. I do not find it plausible that voters are going to be able to give thoughtful and accurate scores to all candidates for a local election. A simpler system like Approval, with a delayed runoff, seems more likely to produce better outcomes if the data collected from voters is likely low quality. Under such conditions, the gain from Approval to STAR appears to be negligible.

Specifically, the proposal to eliminate primary elections and have a single round STAR election instead seems like the worst of both worlds. Instead, an all-candidate primary under Approval with a delayed runoff seems to be the most robust system for electing candidates. It is likely some sort of all-candidate primary to a delayed STAR election could outperform Approval with a runoff, but that complexity appears unnecessary to me, particularly once we start to consider political viability.

Independent of the results of these simulations is the fact that STAR is an objectively more complex system than Approval. And that seems exceptionally important for evaluation of political viability.

In a time when it's not even clear that the simplest voting system, Approval, is a slam dunk reform of our choose-one system, I see little evidence to assume that a more "expressive" (i.e. complicated and more difficult to explain) system like STAR would be *more* palatable to voters (optimal accuracy or not).

Though the sample size for how these two systems fare at the ballot box is small, the results are concerning:

- Approval was voted in by overwhelming numbers (over 60%) of voters in Fargo, ND, and St. Louis, MO. Its ban in Fargo was a partisan move by the North Dakota State Legislature, *not* the voters. Further, both that ban and the ban in Missouri (for which St Louis was grandfathered in) were framed as RCV bans. That is, Approval has simply been in the crossfire of ([justifiable](../ditch-rcv/)) RCV rejections<d-footnote>Further on the RCV issue, Approval failed in Seattle because it was pitted directly against RCV. Seattle was the home turf of RCV.</d-footnote>.
- STAR has been rejected three times by voters in Oregon. In 2024, a ballot measure for its implementation in [Eugene was voted down by about 67%](https://www.opb.org/article/2024/05/22/eugene-rejects-star-voting-rating-based-system/). It was also rejected in Oakridge in 2024 and Lane County in 2018.

I cannot help but wonder if the expressiveness, which makes STAR so appealing to its supporters and proponents, is exactly what makes it so unappealing to the silent majority of voters (at least, based on the evidence we have seen so far).

Is scoring comptrollers and city council members, the way you rate a restaurant, actually something the average voter is clambering to do? Perhaps this prospect is appealing to political junkies, but I somehow doubt that *most* voters actually like or care about politics enough that this more expressive ballot is enticing. This remains to be seen, and luck could simply have been against STAR in the three Oregon elections, but I am not optimistic.

The fact that my simulations show that this more complex process is actually *less robust* to adversarial conditions than simpler options like Approval makes me exceptionally concerned about STAR voting. Is a complex machine that cannot handle sand in its gears really a good idea for something as important as electing our leaders? I am not so sure. The evidence in favor of STAR thus far is primarily in simulations done *by STAR proponents themselves*. And though I find their methodology excellent and without obvious flaws or clear evidence of bias, the number so far have not swung me to becoming a STAR supporter<d-footnote>Is it a good system? Probably. But I see insufficient evidence that we should skip over the more simpler and nearly as affective Approval voting in favor of STAR. The simpler solution seems better from where I'm sitting.</d-footnote>.

It is impossible to know for sure how actual real world conditions map onto the parameters I have defined in this simulation. Even mild friction could be pessimistic for a high profile election (especially if the field is not particularly crowded). However, I do believe that the narrowing of the gap between STAR and Approval, with Approval Top-2 surpassing it easily, under even mild adverse conditions is remarkable.

If we suppose that expressiveness begets complexity which makes the system *less* politically viable, and *also* makes it less robust to real-world conditions, then Approval voting (particularly with a runoff) seems to dominate STAR in every way that matters. However, that is just my opinion.
