---
layout: distill
title: 'Coarse Correction: Is STAR Actually More Accurate than Approval?'
date: 2026-07-30
description: Why Approval with a delayed runoff might be far more robust than a more granular and expressive voting system like STAR when voters are misinformed and fatigued.
importance: 2
tags: voting
category: polisci
featured: false
theorems: false
bibliography: voting.bib
chart:
  plotly: true
images:
  photoswipe: true
jupyter_notebook_crawlable_text: false
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: Equal Vote Coalition (Volunteer)
toc:
  - name: Introduction
    subsections:
      - name: A Tale of Two Cities
  - name: The Friction Parameters
    subsections:
      - name: Epistemic Noise
      - name: Unfamiliarity
      - name: Fatigue
      - name: How These Combine
  - name: The Runoff Assumptions
    subsections:
      - name: The Coma Model
      - name: The Groggy Model
      - name: The Clear-Eyed Model
      - name: Justification
  - name: Other Relevant Methodology
  - name: Findings
    subsections:
      - name: The Approval-STAR Gap
      - name: How much does a delayed runoff actually help?
      - name: STAR Runoff Betrayal
  - name: Conclusion
  - name: Appendix
    subsections:
      - name: Condorcet Efficiency
      - name: SCORE vs STAR
      - name: The Jupyter Notebook
---

## Introduction

Voter Satisfaction Efficiency (VSE)<d-cite key="quinn2017vseSummary"></d-cite> is an incredible metric used for evaluating the performance of voting systems, primarily championed by the Equal Vote Coalition. It gives a numeric percentage to the "accuracy" of a voting system, with 0% being just a system that randomly chooses a winner, and 100% being a system that always elects the "best" (highest utility) candidate.

I interpret VSE as just a simple measure of "aggregation competence": how well a voting system can aggregate the preferences that are fed into it. If a system is *good*, then it almost surely has solid VSE. Choose-one voting, for example, has awful VSE (about 60%) when voters are simulated to just vote honestly. This is because the system is so blind that it cannot look beyond the top choice of each voter, and thus consensus candidates are often buried by vote-splitting. With strategic voting, it can rise to about 80%.

However, VSE on its own does not say anything about whether or not a system is "good" in the real world. If a voting method is so difficult to explain or fill out, then high VSE might not matter if it's so intimidating to voters that it reduces turnout or otherwise discourages participation (or is perhaps so exotic that voters reject adopting it outright). Practical considerations are exceptionally more important than "in simulations this voting system does great!" But VSE is still absolutely a useful metric for comparing the performance of different voting systems.

My status as a volunteer for the Equal Vote Coalition does not mean I speak for them. My views are often at odds with the official stances of the EVC, particularly with respect to STAR voting. My words in this post are my own. So when I call VSE excellent, that does not come lightly. Further, I will not pretend that I am not [partial to Approval voting over STAR voting](../approval-only/). In fact, one of the reasons is just how close the VSE of the simpler Approval is with STAR.

Additionally, while I was originally strongly against pairing Approval voting with a runoff, due to concerns of strategy<d-cite key="fishburnBrams1981runoff"></d-cite>, the results from this model have completely changed my mind. I now believe that Approval Top-2, rather than just being a far more practical alternative which is *almost* as good as STAR (see the image below), might actually be exceptionally *more* accurate at electing better candidates.

<div class="pswp-gallery mt-3" id="vse-accuracy-by-voting-method">
  <a href="/assets/img/vse-accuracy-by-voting-method.png"
     data-pswp-width="2500"
     data-pswp-height="1617"
     target="_blank">
    <img src="/assets/img/vse-accuracy-by-voting-method.png" class="img-fluid rounded z-depth-1" alt="Chart comparing election accuracy (VSE) by voting method" />
  </a>
</div>
<div class="caption mt-2">
  Election accuracy (VSE) by voting method. <a href="https://www.starvoting.org/faq">Source</a>.
</div>

I should make it clear that Ranked-Choice Voting has very poor VSE, which is consistent with its poor design and mechanism<d-footnote>Including the spoiler effect, vote splitting, and center-squeezes. If your favorite can't win, your vote does not necessarily transfer, and this can lead to a compromise candidate getting eliminated early. RCV does not deliver on its promises, plain and simple. (See p.314 of <d-cite key="wolk2023starVoting"></d-cite>)</d-footnote> (which, funnily enough, ends up achieving worse outcomes from its far greater logistical complexity and cost compared to Condorcet methods, which can be counted at the local precincts). Although RCV is technically a serious contender in the reform space, it is not a serious consideration by organizations like the Equal Vote Coalition, Center for Election Science, and Better Choices for Democracy. [People who do the math don't support RCV](../ditch-rcv/), so this post is focused more on STAR and Approval. It is included in the early cells of the notebook to show consistency with the original VSE code, but not focused on here.

The Equal Vote Coalition supports three systems, which all have high VSE: STAR, Condorcet<d-footnote>Technically, they champion their particular flavor of Condorcet, "Ranked Robin", but the differences are minor and not relevant to this discussion. In what follows, we will focus on the Schulze method, which is particularly robust and used in a number of organizations for their internal elections.</d-footnote>, and Approval. My numbers are slightly lower than those reported by Jameson Quinn<d-cite key="quinn2017vseSummary"></d-cite>, but his report was nearly 10 years ago, so I will report the approximate numbers I got by copying the code as it is in the electionscience Github repository:

- Condorcet methods: Voters rank candidates and the candidate who defeats all others is the winner (with some tiebreaker if no candidate is a Condorcet winner). These usually get the highest VSE, but drop low due to strategy, despite the fact that strategic voting is just [not very effective in Condorcet methods](../better-choices-strategy/). The fact is, pairwise dominance ([while not a prerequisite for being the utility maximizer](../why-condorcet/)) is objectively a strong predictor of high utility.
- STAR voting (Score Then Automatic Runoff): Voters score candidates on a scale (usually 0-5), and the two highest-scoring candidates go to an automatic runoff where a candidate gets one point for every voter who scored them higher than the other candidate. This system has arguably best VSE range of the three.
- Approval voting: Voters can approve of as many candidates as they like, and the candidate with the most approvals wins. This is a system with surprisingly high VSE for its refreshing simplicity. With a top-2 runoff, Approval improves its VSE to be quite competitive with other more granular alternatives.

The following is the VSE range of the three systems, including Approval Top-2 from my code, as well as Choose-one plurality, Plurality Top-2, and RCV for reference.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="evc-vse" %}

In addition to measuring "aggregation competence," VSE can be used as advocacy evidence to demonstrate the robustness of a method to the public. In a recent TEDx talk, [Sara Wolk](https://youtu.be/xWQiy5VdwY0?si=ABEnMeAMKWSvMWjS&t=483), the Executive Director of the Equal Vote Coalition, introduces a version of the above chart and says:

> "Today, experts can use computer models to see how different voting methods would actually perform. And it's pretty much just like how engineers can test the plans for a new skyscraper before actually building it." (Timestamp [7:10](https://youtu.be/xWQiy5VdwY0?si=9vzXt8aI6_beTKoi&t=430))

<div class="pswp-gallery mt-3" id="vse-accuracy-tedx-screenshot">
  <a href="/assets/img/vse-accuracy-tedx-screenshot.png"
     data-pswp-width="1280"
     data-pswp-height="720"
     target="_blank">
    <img src="/assets/img/vse-accuracy-tedx-screenshot.png" class="img-fluid rounded z-depth-1" alt="TEDx Mt. Hood talk slide showing the same Voting Method Accuracy chart" />
  </a>
</div>
<div class="caption mt-2">
  A similar chart presented in a <a href="https://youtu.be/xWQiy5VdwY0?si=ABEnMeAMKWSvMWjS&t=483">TEDx Mt. Hood talk on STAR Voting by Sara Wolk (2026)</a>, but only showing Choose One, Ranked Choice, Approval voting (no runoff), and STAR voting.
</div>

Particularly when Ranked-Choice Voting has hogged all the attention and oxygen (at the cost of better reforms), using VSE in this way is a powerful tool to demonstrate that there are far better alternatives to RCV. These simulations *do* show the shortcomings of RCV's blindness, due to its inability to see beyond the current active choice of a voter. The three systems supported by the Equal Vote Coalition all solve the issue of vote splitting by looking at each voter's *entire* ballot *immediately*, and that translates to strong VSE<d-footnote>There are other considerations as well that make these three systems the strongest choices, beyond excellent outcomes: They are logistically easy to implement and count, and are fairly resistant to strategic voting compared to some other methods.</d-footnote>.

And when we look at the actual numbers, it generally supports their narrative that STAR does the overall best job at finding the highest utility candidate (in simulations)<d-footnote>Condorcet methods are also exceptionally strong performers in this regard, but there is a valid case that scoring requires less cognitive load and scales better than a ranked system with many candidates.</d-footnote>, while Approval is a simple and effective alternative that they also "approve of"<d-footnote>On the <a href="https://bettervoting.com/">BetterVoting website</a> (a project of the Equal Vote Coalition), they list Approval as being "recommended for simplicity", and STAR as being "recommended for accuracy". With Condorcet being relegated as "recommended for ranking" (despite being exceptionally accurate). I do personally disagree with this framing, and I would rather use "recommended for scoring" for STAR.</d-footnote>.

In Quinn's 2017 summary, he has this to say:

> [Approval is] not the best of the methods I tested, but it certainly is the best "bang for the buck"; a simple reform, with basically no downsides, which improves outcomes hugely. (Quinn, 2017<d-cite key="quinn2017vseSummary"></d-cite>)

And it is absolutely undeniable: single-round Approval voting, while simple and strong like a reliable sedan, absolutely underperforms the fancy sports car of STAR voting in VSE, especially under the "honest" model of Approval voting used in the code (which functions like a SCORE system with two options).

On the [Equal Vote page for Approval](https://www.equal.vote/approval), they make a fair case for Approval as something that "should be the default voting method". But they also call it a "stepping stone", say that "there's a good case to be made to upgrade further," and even though it's a "case for Approval", the text spends significant space pointing back to STAR:

> In many cases it may be quicker and easier to just switch directly from the traditional Choose-One voting method to something top of the line like STAR Voting, but we understand that there may be some cases where that's unrealistic. ([Source](https://www.equal.vote/approval), Accessed 7/30/2026)

The wording "top of the line" paints a vivid picture, to be sure. But how robust is that edge? If we are to describe VSE simulations as "like how engineers can test the plans for a new skyscraper before actually building it," then I would hope that the engineers test the skyscraper in weather other than a perfect 72 degree sunny day. Perhaps we should see how the plans fare when there's a hurricane, or an earthquake, or a flood. If the skyscraper is only tested in perfect conditions, then that does not make me feel particularly safe if I have to live on the eightieth floor.

And though there has been a good effort to stress-test VSE under a variety of conditions and models<d-cite key="wolk2023starVoting"></d-cite>, the most unrealistic issue I take with VSE is in the assumptions of *voter information quality*.

> If the voter model, media model, and strategy model are realistic for a particular context, then VSE is probably a good metric for comparing voting methods. (Quinn, 2017<d-cite key="quinn2017vseSummary"></d-cite>)

I agree with this wholeheartedly. And in questioning the realism of the voter model, some questions that I would like to raise are:

1. Do voters *actually* know their true utilities for all the candidates on the ballot? Might some voters *think* they prefer $B$ over $A$, but would actually be happier if $A$ won? If they score $B$ higher than $A$, perhaps because of a convincing campaign ad, and the runoff is between $A$ and $B$, then this voter will accidentally vote *against* their interests in the automatic runoff step with no "undo" option.
2. What if voters have never heard of some of the candidates? If the utility maximizer is someone most voters are not aware of, then they are not likely to score them highly, hurting that candidate's chance of winning. Similarly, if voters are fatigued and don't have time to thoughtfully score all the candidates, might that damage the accuracy of the election? How well do different systems handle such friction?

The common thread here is that a complex, granular, and expressive system like STAR is designed to take in more information from voters to deliver better outcomes than a more coarse system like Approval. But what if the data it collects is truncated noise rather than signal?

One particular concern I have with this is that the runoff is *automatic*. A voter who is misinformed when they cast their initial score ballot cannot change their mind later if they realize that they were wrong. You don't know what you don't know. And many voters *are* tired and busy, and don't have time to read the campaign websites of all [61 candidates on the ballot, as we saw in the 2026 California Gubernatorial primary](../ca-top-2/). Even with 6 candidates, the default in the VSE simulations, I worry about the ability of voters to accurately evaluate all candidates.

<div class="pswp-gallery mt-3" id="ca-gov-2026-full-ballot">
  <a href="/assets/img/CAGovernorOpenPrimaryBallot2026.jpg"
     data-pswp-width="3472"
     data-pswp-height="4624"
     target="_blank">
    <img src="/assets/img/CAGovernorOpenPrimaryBallot2026.jpg" class="img-fluid rounded z-depth-1" alt="Official sample ballot showing all 61 candidates for California Governor, 2026 primary" />
  </a>
</div>
<div class="caption mt-2">
  The actual sample ballot for the 2026 gubernatorial primary, showing all 61 candidates for Governor. Thank you to <a href="https://electowiki.org/wiki/File:CAGovernorOpenPrimaryBallot2026.jpg">Rob Lanphier for the image</a>.
</div>

My concern is that an automatic runoff has a "garbage in, garbage out" problem: if the data collected from voters is poor, then the automatic runoff has no way to correct for that. In a delayed runoff, voters have a chance to familiarize themselves with the candidates in the narrowed field, and can make a more informed choice.

### A Tale of Two Cities

In 2024, a proposal in [Eugene, Oregon to eliminate primary elections for mayor, city council, and EWEB seats and replace them with STAR voting](https://ballotpedia.org/Eugene,_Oregon,_Measure_20-349,_STAR_Voting_for_Mayor_and_City_Council_Elections_Initiative_(May_2024)) was voted down by 64.49%. In 2020, [St. Louis, MO voters voted to adopt an all-candidate Approval voting primary election with a delayed top-2 runoff](https://ballotpedia.org/St._Louis,_Missouri,_Proposition_D,_Approval_Voting_Initiative_(November_2020)) by 68.15%. This system is still in place, and working excellently<d-cite key="sargent2025stlouis"></d-cite>. The comparison between these two proposals will be the focus of this post.

I assume that the pitch for a single-round STAR election over the proven Approval Top-2 system used in St. Louis was that STAR is more accurate than Approval. Surely, a system with better VSE is better than one with worse VSE, right? And if we can save money by eliminating primary elections, and just quickly elect the best candidate through an *automatic* runoff performed on an expressive and rich dataset, why not do that?

I hypothesized that under noisy and truncated data, that the edge that more granular systems like STAR and Condorcet have over more coarse systems would diminish, and that a delayed top-2 runoff is more effective at improving outcomes than an automatic runoff when there's a chance for voters to improve their information on the narrowed set of two candidates.

In this post, we evaluate the rejected single-round STAR system proposed in Eugene, Oregon to the currently in-place Approval Top-2 system in St. Louis, Missouri. My primary evidence is a [Jupyter notebook](#the-jupyter-notebook) that uses the original VSE simulation code with significant modifications to test these hypotheses. It was written with AI-assistance by Claude Code, but the full notebook is included for full transparency and reproducibility. I look forward to someone who is a more skilled coder than I am to improve upon it, and perhaps extend the model<d-footnote>I have no doubt someone is going to find a bug in my code, or an assumption that is not particularly realistic. I welcome that, and hope that this post can be a jumping-off point for further research into the robustness of voting systems to imperfect voter knowledge.</d-footnote>.

Spoiler alert: Under even mild friction, the gap between single-round Approval and STAR is basically negligible. And the delayed runoff, even with only *minimally* improved information completely blew all single-round systems out of the water.

## The Friction Parameters

We define three parameters that we can adjust to simulate friction for voters:

### Epistemic Noise

Voters don't always know what they want. Whether that be a manipulative ad, an excellent social media presence, or a campaign blunder, sometimes a voter's feelings of a candidate don't match how they would actually feel if that candidate won. There is often an [unfortunate spike in "how to change my vote" web searches](https://appdevelopermagazine.com/change-my-vote-searches-soaring-up-during-2024-us-election/) shortly after an election, which means that we should not always assume that a voter's *perceived* utility of a candidate is the same as their *true* utility.

We simulate this by adding noise to the voter's perceived utility of each candidate, simulating the fact that voters are often misinformed or otherwise unable to accurately evaluate the candidates. We adjust this with the $t$ parameter, which is the correlation between the voter's true utility and their perceived utility.

If $u_i(c)$ is the true utility of candidate $c$ for voter $i$, then we can define a voter's perceived utility as:

$$u'_i(c) = t\cdot u_i(c) + \sqrt{1-t^2}\cdot \sigma_i \cdot \epsilon_{ic}$$

Where $\epsilon_{ic} \sim N(0,1)$ and $\sigma_i$ is the standard deviation of voter $i$'s true utilities across the candidates, used to scale the injected noise to that voter's own utility range. Then $t$ is exactly the Pearson correlation coefficient between the true and perceived utilities. If $t=1$, then the voter is perfectly informed on their exact utilities, and if $t=0$, then the voter's perceived utilities are pure noise. We use one global $t$ for all voters.

### Unfamiliarity

When a voter receives their ballot, it is almost never the case that they recognize every single name on the ballot. Indeed, candidate quality is often divorced from the proportion of voters who recognize them. Whether that be a scandal-plagued incumbent or a dedicated and qualified civil servant with no name recognition, if a voter does not know a candidate, they cannot accurately evaluate them.

We draw an awareness/prominence ranking for each election, simulating that everyone knows the frontrunner, but as you go down the number of voters who are aware of each candidate decreases. For the selected $\alpha$ "awareness" parameter, the probability that a voter is aware of candidate $c$ is given by:

$$P_{\text{aware}}(c) = \alpha^{\text{prominence_rank}(c)}$$

At $\alpha=1$, all voters are aware of all candidates, while at lower values, fewer voters are aware of the candidates lower in the awareness ranking.

### Fatigue

Even if a voter is vaguely aware of a candidate, if that candidate is number 40 on a list of 61, we cannot assume that voter will necessarily take the time to scan the whole list to find them. Perhaps if that candidate was first on the list, they would easily give them a solid 3 stars, but if that candidate is far lower down, the voter might forget about them and stop looking after evaluating the first few candidates.

While prominence is global to the election, fatigue is local to the voter. We draw a random fatigue ranking for each voter, as a stand-in for ballot-order rotation. As voters go down the ballot, they are more likely to be fatigued and simply skip a name. Maybe they need to pick up their kids from soccer practice, or they came from a long day at work, or they just don't care enough about who their water commissioner is to fully evaluate every name they would recognize if they had read each name closely. For the "fatigue" parameter $\ell$, the probability that a voter is not fatigued enough to vote for candidate $c$ is given by:

$$P_{\text{not fatigued}}(voter, c) = \ell^{\text{fatigue_position}(voter, c)}$$

### How These Combine

Unfamiliarity and fatigue interact in an interesting way. To be able to vote for a candidate, a voter must be both aware of them and not fatigued. So the probability that a voter votes for candidate $c$ is given by:

$$P_{\text{genuine}} = P_{\text{aware}} \times P_{\text{not fatigued}}$$

If the check fails, then the utility for that candidate on the input ballot is set to be just below that of their least liked known candidate. This simulates the voters to basically say "I don't know or remember them, so I'll leave them off my ballot".

This is how Schulze (Condorcet) would interpret a truncated ballot: all unranked candidates are tied below all ranked ones, and treated as the voter being indifferent between them. For cardinal systems, this functionally gives unknown candidates a 0 score (unapproved for Approval).

## The Runoff Assumptions

This model essentially turns voters from robots, patient enough to thoughtfully evaluate and vote for all candidates, into messy humans who are often misinformed, fatigued, or otherwise unable to know which candidates would actually make them happiest. We would like to know how much of a difference a delayed runoff, with reduced cognitive load from there being just two finalists, can make in the overall accuracy of the election compared to a more granular system like STAR being used for a single-round election, taking in that poor data to perform an automatic runoff.

My hypothesis was that the runoff step can act as a corrective mechanism for misinformed voters in the primary step, whereas the more complex single-round mechanism suffers from the previously mentioned "garbage in, garbage out" issues.

However, there are a few ways that we could model improved voter information in the runoff step. We assume that in the primary election (say, in June) voters are tired and didn't have time to research all candidates in the crowded field. They vote imperfectly based on their limited knowledge (ex. vibes, not reading the candidate's website) and energy. But just how much more informed are voters in the runoff (say, in November<d-footnote>In California, the primary is in June with the general election top-2 runoff about five months later in November. In St. Louis, the general is only one month after the Approval primary. Either way, that is a fair amount of time to find out who the general election candidates are.</d-footnote>)?

We first assume that fatigue is entirely removed in a delayed runoff. With only two options, the voter is assumed to have the bandwidth to read two names and make a decision based on the direction of their preferences. The voter votes for the candidate who has a strictly higher perceived utility than the other candidate. If they are equal, then the voter is assumed to be indifferent and votes for neither.

### The Coma Model

Under the most pessimistic conditions, we could imagine that the voter has absolutely no time to update their beliefs. The voter essentially falls into a coma as soon as they submit their ballot, wakes up on election day in November, and then casts a vote. We call this the "coma" runoff assumption, because I think that's kind of funny. In Approval Top-2's coma variant, voters still have the opportunity to vote for their preferred finalist (according to their potentially misinformed preferences) *unless they were unaware of both candidates*.

The coma model is **not** how STAR functions (but it is close). The flawed understanding does indeed carry over to the runoff step, without a chance to be corrected. However, STAR is slightly worse here because if you gave both finalists an equal score (ex. say there was a 3.1/5 candidate and a 2.9/5 candidate and you rounded both to a 3/5), you have no chance to influence that final outcome (unlike in Approval where you may have approved both, or disapproved both, despite holding a strict underlying preference. With a runoff, you still get to express your preference between the two finalists).

For example, if you gave finalist $A$ one star because they're terrible, but the other finalist $B$ was at the bottom of your ballot so you forgot to give them their rightful three stars (perhaps needing to pick up your kid from daycare and so you left them blank), then you have no opportunity to correct that mistake, and your ballot will be interpreted as being for $A$ over $B$.

### The Groggy Model

In contrast to the coma model, the remaining two models will simulate voters to have some extent of "wakefulness". These are the "awake" models.

Under slightly more optimistic conditions, we can suppose that in the time between the primary and runoff, voters at least know who will be on the ballot. In the months since the primary election, maybe they were bombarded by television ads and social media posts, drove by a yard sign every day for work, or were pelted with mailers on the exciting options for Water commissioner, and now they at least know who the two finalists are, though their preferences could still be noisy and in the wrong direction (because how many will actually *read* those mailers).

We'll call this the "groggy" runoff assumption, and it's how we define the baseline delayed runoff systems to work (Approval Top-2 and Plurality Top-2).

### The Clear-Eyed Model

The most optimistic assumption is that voters have had time to research the candidates in the runoff step, watching the debates, reading the websites, and generally becoming more informed about the candidates.

In this ideal case, we assume that the noise has entirely evaporated, leaving the voters with the exact correct *direction* between the candidates. We include "clear-eyed" alternates of each delayed runoff system which uses this assumption.

It's likely that the reality of the situation is somewhere between the coma and clear-eyed assumptions. We include an analysis that sweeps from the coma model to the clear-eyed model, and shows how much of a difference it makes in the overall accuracy of the election.

### Justification

I will not deny that the awake assumptions are particularly optimistic for a delayed runoff. Indeed, I might even call it "cheating"! However, it turns out that the groggy assumption is more than enough to make Approval Top-2 significantly more robust than STAR.

The proposal in Eugene *was* to eliminate the primary entirely, and have a one-shot expressive five-star score based election for seats as prestigious and of consequence as "Commissioner for Eugene Water and Electric Board, Wards 6 and 7" (no offense to the person who actually holds that office, I'm sure Eugene's EWEB is wonderful).

Any voter who fails to distinguish between the finalists due to fatigue or lack of information would have absolutely no recourse to influence the outcome. In *any* top-2 system, all voters are guaranteed an opportunity to have final say in who is elected in a cognitively simple two-candidate race in November.

Further, in response to the previously mentioned California Gubernatorial primary (with 61 candidates), I did hear the suggestion of eliminating the primary in favor of a single-round STAR election (just as was proposed in Eugene). If replacing that 61 candidate Choose-one primary with single round STAR is an idea that is even being *considered* by STAR proponents, I feel entirely justified in rigorously testing that directly against the tried and true delayed runoff system that is already in place in St. Louis, Missouri. It is not wrong to compare apples and oranges if those are indeed the exact proposals that are competing for funding and implementation.

## Other Relevant Methodology

I tried to keep the default settings of the original vse-sim as much as possible. This includes simulating just six candidates, rather than 61. I made an effort to change the code as little as possible, and included various sanity checks to see that the output was reasonable and matched with expectation (before adding my friction parameters).

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="strategy-sweep-chart" %}<br>

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="vse-range-baseline" %}

{% proof Expand to see VSE tables %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="vse-tables" %}
{% endproof %}

Additionally, in the comparison, we used honest voting for all systems. This is actually a disadvantage towards Approval and Plurality, since strategic voting is usually what makes the outcomes of these systems more accurate. And honest voting is where STAR and Condorcet have their absolute best outcomes. This makes what I found all the more troubling.

I also defined "joint scenarios" of various friction levels where I set the $t=\alpha=\ell$ parameters to the same values:

- 1.0: Ideal
- 0.9: Mild
- 0.8: Moderate
- 0.7: Heavy

The way some parameters compound is multiplicative, so while 0.7 may not seem as heavy as, say, 0.5 or 0.3, it is actually *quite* substantial (especially with only 6 candidates). I chose not to tune the parameter too much, and use the simplest settings possible to avoid overfitting the model. I look forward to seeing how others might improve upon this model with even more realistic assumptions, and perhaps even real-world data.

## Findings

The code is included in [the Appendix](#the-jupyter-notebook), but we will summarize the results here.

### The Approval-STAR Gap

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="approval-star-gap-scenarios" %}

Under perfect conditions, STAR is objectively more accurate than single-round Approval and Approval Top-2 (under honest ballots). For single-round Approval specifically, however, the VSE gap narrows under all friction scenarios. A 95% confidence interval on the VSE gap between single-round Approval and STAR voting, using a paired test, consistently contains 0 for all friction scenarios. From this, I conclude that there is no evidence or justification that STAR is more effective than single round Approval in this simulation under any friction scenario. I find it unlikely that STAR, in the real world with real voters in public elections, would actually elect better candidates than Approval.

Approval Top-2, on the other hand, clearly wins out in simulations over STAR and Schulze except for the "coma model" (for which its edge over STAR is less clear cut). It's not even close. Even under mild friction, Approval Top-2 is significantly more accurate than STAR so long as voters are "awake" to the runoff, and this grows as friction worsens. This is with and without removed noise in the runoff step. Misinformed voters who at least are aware of the candidates are enough to outperform the automatic runoff.

The coma model was also quite strong. The only scenario where a gap of 0 was contained in the 95% confidence interval was under *moderate* friction (and it was extremely borderline). It seems relatively safe to say that under friction, even the coma model is likely an improvement over STAR.

Perhaps the most sobering statistic is how solid groggy Plurality Top-2 was in VSE compared to STAR under the sweeps and scenarios (with the Clear-eyed variant being even further). Despite Plurality Top-2 having completely mediocre ~80% VSE in the ideal case, it stays robust compared to all other single-round systems<d-footnote>Technically, Plurality Top-2 is the exact system being used in California right now, including for that 61 candidate Gubernatorial race.</d-footnote>.

I would never advocate for Plurality Top-2, but this model seems to highlight that the potential corrective mechanism of a delayed runoff can somewhat salvage even the worst primary elections, when ignorance decimates the accuracy of the "more accurate" single-round system used.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="vse-joint" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-help-sweep" mode="images" %}

### How much does a delayed runoff actually help?

So far we have looked at fixed runoff awareness models (coma, groggy, clear-eyed). This gives a very binary change in how much the runoff helps. But we are interested to see what the "in-between" looks like.

We define a new parameter `p_learn`, which ranges from 0 to 1. This parameter is the probability that a voter can become aware of a candidate they were not aware of before (rolled against for one or both candidates the voter is unaware of). When a voter successfully rolls to learn of a candidate, we use their (potentially noisy) perceived utility.

If a voter was unaware of exactly one candidate in the runoff, they have a chance to learn about the other and vote for them if they realize they think they have higher utility. Otherwise they vote for the one they were already aware of. If a voter was unaware of both, and becomes aware of one or both of the runoff candidates, then they vote for whichever has higher utility (if they are still unaware of one, they vote for the one they are aware of).

At 0, we effectively have the coma model when we maintain noise from the primary. We see that a coma runoff is essentially as good or better than STAR (depending on noise), but even for extremely small learning rates, the gap between STAR and Approval Top-2 grows significantly. As long as a small number of voters have a chance to learn about candidates (by osmosis) even if their opinions between them are wrong, the delayed runoff is significantly more accurate than STAR's automatic runoff.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-learn-sweep" mode="images" %}<br>

As we sweep the runoff noise $t$, and keep the awareness fixed between the primary and runoff, the performance does not change much. Awareness appears to be the entire driver of improved outcomes.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-t-sweep" mode="images" %}

### STAR Runoff Betrayal

We measure the difference between the actual automatic runoff versus a hypothetical "perfect" clear-eyed runoff (i.e. 0-5 SCORE voting with a delayed runoff compared to STAR's automatic runoff), where voters are perfectly informed and vote for the candidate they truly prefer. This is a measure of how much the automatic runoff hurts voters who are misinformed in the primary step compared to a perfect clear-eyed runoff. We find that even under mild friction, STAR's automatic runoff is significantly worse than a perfect clear-eyed runoff, and this gap grows as friction worsens.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="star-betrayal-tables" mode="tables" %}

This second table measures the VSE of the actual STAR runoff, the theoretic SCORE delayed runoff, and clear-eyed Approval Top-2 as we sweep just the epistemic noise. Once again, actual STAR is significantly worse than the other two, which are very close.

This is perhaps not too surprising given that we are modeling voters as not necessarily filling out the entire ballot. Of course a delayed runoff would improve the outcomes! But it's by *how much* that makes me really concerned about the automatic runoff in STAR. Rather than a "cost-saving" mechanism, it could instead "cost" outcomes, and give voters who have less time to research candidates less of a voice in the outcomes.

The evidence for my hypothesis that a more coarse ballot is more robust to friction is mixed. Under high friction scenarios with an assumed perfectly informed corrective primary, clear-eyed Approval Top-2 has a slight edge over a theoretical SCORE primary followed by a clear-eyed delayed runoff. But this gap does not seem large enough for me to declare it a decisive advantage. When we sweep epistemic noise exclusively, the performance is for all intents and purposes identical. I find insufficient evidence to conclude that there's likely to be a difference between the two systems under the friction levels I find realistic.

At the very least, for this comparison between a theoretical SCORE Top-2 (that nobody is actually advocating for) with the St. Louis model, I would say that the SCORE ballot appears unjustified. The gulf between the *automatic* runoff of STAR and a delayed Approval runoff, however, is very, very large.

## Conclusion

It is absolutely undeniable that, with perfectly informed voters who fill out their ballots completely and accurately, STAR is an objectively more accurate mechanism than Approval. That granularity is a genuine strength when the data is high quality. However, that granularity becomes a liability when the data you collect is noisy or incomplete. Low quality data acts like sand in the gears, making the system no better than a simpler system like single-round Approval.

And based on my findings, I would say that for something like a City Council trying to decide between a few different options for the placement of a new library (where the voter assumptions for the original VSE model are very likely accurate), STAR would be an excellent choice. Highly informed voters, who will give full and thoughtful scores to all available options, match better with the assumptions that underlie the ideal VSE numbers commonly reported. It could be easily expected that there will be cases where STAR would produce higher quality outcomes than the council members simply approving of which options they like. This is the use case where STAR can really *shine*.

*Publicly electing that city council*, however, is a different story. I do not find it plausible that voters are going to be able to give thoughtful and accurate scores to all candidates for a local election. A simpler system like Approval, with a delayed runoff, seems more likely to produce better outcomes if the data collected from voters is likely low quality. Under such conditions, the gain from even just single-round Approval to STAR appears to be negligible.

Specifically, the proposal to eliminate the primary process in favor of a single round STAR vote instead seems like the worst of both worlds for public political elections. If there is anything I have taken away from this project, it's that a delayed runoff is of **enormous benefit**. And given that the standard is already to have two elections, a winnowing primary process that feeds into a general election, I see no *serious* downside to a second election (ex. cost, turnout, etc.).

A narrowing process seems absolutely necessary, and using the simple Approval system for that winnowing seems to be the most robust and politically viable option. It scales exceptionally well to crowded fields, compared to a ranking or scoring system, and eliminates the vote splitting we see in the Plurality Top-2 systems used in Washington and California. If 61 candidates on the ballot is a possibility, then Approval is the only system that can handle that without completely overbloating the ballot and overwhelming voters.

Independent of the results of these simulations is the fact that STAR is an objectively more complex system than Approval. And that seems exceptionally important for evaluation of political viability.

In a time when it's not even clear that the simplest voting system, Approval, is a slam dunk reform of our choose-one system, I see little evidence to assume that a more "expressive" (i.e. complicated and more difficult to explain) system like STAR would be *more* palatable to voters (optimal accuracy or not).

Though the sample size for how Approval and STAR fare at the ballot box is small, the results are concerning:

STAR has been rejected three times by voters in Oregon. There is the Eugene situation that has framed this discussion, of course. But it was also rejected in [Lane County in 2018](https://ballotpedia.org/Lane_County,_Oregon,_Measure_20-290,_Score_Then_Automatic_Runoff_Voting_Method_(November_2018)) (52.4% opposed) and [Oakridge in 2024](https://ballotpedia.org/Oakridge,_Oregon,_Measure_20-364,_STAR_Voting_for_Three_Election_Cycles_Amendment_(November_2024)) (53.56% opposed, and this was a reversible low-stakes three election pilot test).

Fundamentally, I have to ask: is scoring the options for Commissioner of the Water and Electric Board the way you rate a restaurant on Yelp actually something the average voter is clambering to do? Perhaps this prospect is appealing to political junkies<d-footnote>No offense to you, dear reader, but if you are reading <em>this blog post</em> you may not be representative of the average voter. Thank you for reading this far, by the way!</d-footnote>, but I am skeptical that the number of voters who find this more expressive ballot enticing is particularly large. This remains to be seen, and luck could simply have been against STAR in the three Oregon elections<d-footnote>Particularly the close ones. Though I have no earthly idea if Eugene would have accepted STAR if it had been integrated into the existing primary process somehow.</d-footnote>, but I am not optimistic. It seems concerning to me that the thing that gets supporters so excited and passionate about STAR *might be the very thing that hurts it at the ballot box*.

When a more granular ballot and system fails to justify itself in producing significantly better outcomes, you essentially just create more ways to disenfranchise<d-footnote>Research on ballot-marking errors<d-cite key="neelyMcDaniel2015overvoting"></d-cite> generally supports this when looking at RCV in San Francisco: Spoiled ballot rates were disproportionately higher for Black, Latino, elderly, and foreign born residents. "[The] evidence suggests it is not IRV per se but rather ballot complexity more generally that leads to such discrepancies in whose votes get counted." STAR is a significant improvement in how difficult it is to spoil a ballot, but when you suggest anything more complex than Choose-one, I think we have to be incredibly mindful of what the cost of complexity could be, and if the theoretical benefits of granularity and complexity justify them. I think it is safe to say, however, that Approval is easily the hardest ballot type to spoil, which is a benefit to consider.</d-footnote> people who don't have the time to treat politics like a hobby.

Eugene is a liberal city in a fairly progressive blue state. If STAR is 0-3 in *Oregon*, then I am really wondering about STAR's long-term potential to be the future of voting reform in the United States. When every *good* reform, like Approval and STAR, has the common enemy of [Ranked-Choice Voting](../ditch-rcv/), I worry about the potential waste of resources and energy that could be spent on a more politically viable reform like the St. Louis model of Approval Top-2.

I have said before that as RCV is dying a slow and agonizing death, we likely have one chance to pivot before we burn through all the good will and willingness to try something new. I like our chances better if we all rally behind the system that has shown itself to be politically viable, and has a proven track record of success in St. Louis. I worry about flying too close to the sun trying to skip over Approval in favor of STAR. And I am deeply concerned with the potential effect of exhausting Oregonians with repeated STAR proposals to the point where they are unwilling to consider any other reform proposals in the future.

The evidence in favor of STAR thus far is primarily in simulations done *by STAR proponents themselves*. And though I find their methodology excellent and without obvious flaws or a hint of bias, the numbers so far have not swung me to becoming a STAR supporter. I do not find sufficient evidence that it is better suited for public elections than the St. Louis model of Approval Top-2.

If we suppose that expressiveness begets complexity which makes the system *less* politically viable, and *also* makes it less robust to real-world conditions, then Approval Top-2 seems to dominate STAR in every way that matters. However, that is just my opinion.

## Appendix

### Condorcet Efficiency

This is a little funnier. Under ideal conditions, Schulze has perfect 100% Condorcet efficiency, as expected. However, under friction, the system designed specifically to elect the Condorcet winner becomes worse at electing the true Condorcet winner than STAR, Approval Top-2, *and* even base Approval (though the gap is very small except for Approval Top-2). It seems that Cardinal systems, at least in this model, are actually better at electing the Condorcet winner than a system designed specifically to do so. Even Plurality Top-2 did exceptionally well, by the runoff alone.

It appears that if your desire is truly to elect the Condorcet winner no matter the cost, then a runoff method is the way to go if voters are not ideal.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="condorcet-joint" %}

### SCORE vs STAR

I also measured the difference between STAR voting and just plain 5-point scoring (SCORE, i.e. STAR's own ballots with the runoff step switched off) to isolate the runoff's own net effect from everything else STAR does. The difference is fairly negligible in aggregate.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="score-vs-star" mode="images" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="score-vs-star-scenarios" %}

## The Jupyter Notebook

I am sure this post is going to be particularly controversial, so the full simulation is embedded below rather than just summarized. Before any of the findings above are computed, Sections 11-12 of the notebook sanity-check the simulation itself against externally published VSE values (from the original `vse-sim` project). It seems to be working correctly, though the floor of the ranges appears lower than the ranges generally reported by advocates.

I encourage anyone who is interested to run the notebook themselves and scrutinize my methodology!

{% proof Click to open Jupyter Notebook %}
{::nomarkdown}
{% assign verification_jupyter_path = 'assets/jupyter/vse_simulation.ipynb' | relative_url %}
{% capture verification_notebook_exists %}{% file_exists assets/jupyter/vse_simulation.ipynb %}{% endcapture %}
{% if verification_notebook_exists == 'true' %}
  {% jupyter_notebook verification_jupyter_path %}
{% else %}
  <p>Sorry, the notebook you are looking for does not exist.</p>
{% endif %}
{:/nomarkdown}
{% endproof %}
