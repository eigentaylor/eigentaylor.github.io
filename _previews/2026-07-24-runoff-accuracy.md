---
layout: distill
title: 'Coarse Correction Part 1: Is STAR Actually More Accurate than Approval?'
date: 2026-08-14
description: Why Approval with a delayed runoff might be far more accurate than STAR voting when voters are misinformed and fatigued.
importance: 1
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
      - name: Voter Satisfaction Efficiency
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
      - name: How Much Does a Delayed Runoff Actually Help?
      - name: STAR Silent Lock-in
  - name: Conclusion
    subsections:
      - name: The Broader Context
  - name: Appendix
    subsections:
      - name: The Plurality Bump
      - name: Approval vs Plurality
      - name: A Stricter Confidence Interval
      - name: Jameson Quinn
      - name: The Jupyter Notebook
---

## Introduction

Welcome to the beginning of my most ambitious project yet: Coarse Correction, a multi-part series on the robustness of voting systems to imperfect voters based on a simulation model I developed as a modification of Jameson Quinn's Voter Satisfaction Efficiency (VSE) simulation code<d-cite key="quinn2017vseSummary"></d-cite>. In part 1, we will focus on comparing the automatic runoff of STAR voting to the delayed runoff of Approval Top-2. Does a more expressive ballot in one round really produce better outcomes than a simpler ballot with a second round? The answer may surprise you.

### A Tale of Two Cities

In 2020, [St. Louis, MO voters voted to adopt an all-candidate Approval voting primary election with a delayed top-2 runoff](https://ballotpedia.org/St._Louis,_Missouri,_Proposition_D,_Approval_Voting_Initiative_(November_2020)) by 68.15%. This system is still in place, and working excellently<d-cite key="sargent2025stlouis"></d-cite>. A few years later, in 2024, [a proposal in Eugene, Oregon to eliminate primary elections for mayor, city council, and EWEB seats and replace them with "STAR voting"](https://ballotpedia.org/Eugene,_Oregon,_Measure_20-349,_STAR_Voting_for_Mayor_and_City_Council_Elections_Initiative_(May_2024)) was voted down by 64.49%.

[The pitch](https://www.starvoting.org/eugene_faq) for a single-round STAR election was to save money by eliminating low-turnout primary elections, and just quickly elect the best candidate through an *automatic* runoff performed on an expressive and rich dataset of 0-5 scores for each candidate collected in the high-turnout November election<d-footnote>There was also a fair point that the primary elections generally have lower turnout which is disproportionately white, and that a single election might improve equity. The St. Louis proposition, however, was explicitly framed as <a href="https://www.stlamerican.com/election/prop-d-expected-to-protect-the-collective-power-of-black-voters/">protecting Black voters from vote splitting with that primary election</a>. So there are real equity arguments on both sides, and "does X system help/hurt Y demographic" is an exceptionally complicated question that we won't focus on here.</d-footnote>.

> "STAR Voting is highly accurate with any number of candidates in the race, so there’s no need for an expensive primary for nonpartisan elections in most cases." ([Source](https://www.starvoting.org/eugene_faq))

It appears that the voters in Eugene were not swayed by this argument, and rejected STAR voting in favor of the status quo.

The overwhelming defeat of STAR in Eugene was a shock to many, and a devastating blow to the STAR voting movement. But 2024 was a particularly bad year for expressive voting systems in general. [Ranked-Choice Voting (RCV)](../ditch-rcv/) also faced [a sound rejection at the ballot box in a number of states, including Oregon](https://ballotpedia.org/Results_for_ranked-choice_voting_(RCV)_and_electoral_system_ballot_measures,_2024). Was STAR the victim of a bad year for reform, or was this a wake-up call that complex voting systems like STAR, and their supposed "accuracy", are not as appealing to voters as their proponents claim?

### Voter Satisfaction Efficiency

We must first establish what "accuracy" means in the context of voting systems, beyond "the candidate I like did or didn't win".

Voter Satisfaction Efficiency (VSE)<d-cite key="quinn2017vseSummary"></d-cite> is an incredible metric used for evaluating the performance of voting systems, primarily championed by the Equal Vote Coalition. It gives a numeric percentage to the "accuracy" of a voting system, with 0% being just a system that randomly chooses a candidate as the winner, and 100% being a system that always elects the "best" (highest utility) candidate<d-footnote>VSE isn't the frequency of electing the single-best candidate. Rather, it's a linear rescaling of average voter utility normalized to the scale between random (average of all candidate utilities) and best. A VSE of 50% would, for example, mean that the candidate it tends to elect provides utility halfway between the average and the best, potentially without ever picking the single best candidate. An illustrative, if slightly oversimplified, example would be that if the average provided utility of all candidates was 100, and the utility maximizer provided 110, then a VSE of 50% means we would expect the candidate that the system elects to provide 105 utility. Any positive VSE is better than random.</d-footnote>.

I interpret VSE as just a simple measure of "aggregation competence": how well a voting system can aggregate the preferences that are fed into it<d-footnote>VSE does not measure a number of other important and practical considerations, but we will focus on what it says about strict "outcomes".</d-footnote>. If a system is *good*, then it almost surely has solid VSE. Choose-one voting, for example, has awful VSE (about 60%) when voters are simulated to just vote honestly. This is because the system is so blind that it cannot look beyond the top choice of each voter, and thus consensus candidates are often buried by vote splitting. With strategic voting, it can rise to about 80%.

My status as a volunteer for the Equal Vote Coalition does not mean I speak for them. My views are often at odds with the official stances of the EVC, particularly with respect to STAR voting. My words in this post are my own. So when I call VSE excellent, that does not come lightly. Further, I will not pretend that I am not [partial to Approval voting over STAR voting](../approval-only/). In fact, one of the reasons is just how close the VSE of the simpler Approval is with STAR.

While I was originally strongly against pairing Approval voting with a runoff, due to concerns of strategy<d-cite key="fishburnBrams1981runoff"></d-cite>, the results from this model have completely changed my mind. I now believe that Approval Top-2, rather than just being a far more practical alternative which is *almost* as good as STAR (see the image below), might actually be exceptionally *more* accurate at electing better candidates.

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

The Equal Vote Coalition supports three systems, which all have high VSE: the aforementioned STAR system that lost in Eugene, Approval voting which is currently being used with a top-2 runoff in St. Louis, and Condorcet methods (which will receive focus in part 2). The *stars* of this post are the first two:

- **STAR voting** (Score Then Automatic Runoff): Voters score candidates on a scale (usually 0-5), and the two highest-scoring candidates go to an automatic runoff where a candidate gets one vote for every voter who scored them higher than the other candidate. This system has excellent VSE.
- **Approval voting**: Voters can approve of as many candidates as they like, and the candidate with the most approvals wins. This is a system with surprisingly high VSE for its refreshing simplicity, which becomes much higher with strategic voting. With a top-2 runoff, which is what St. Louis uses, Approval improves its VSE to be quite competitive with more granular alternatives.

The following is the VSE range of the major reforms that are currently being considered in the United States.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="evc-vse" %}

Already at this point, Approval's Top-2 variant looks accurate enough. But single-round Approval alone still falls short; to close the gap from single-round Approval to STAR, a second election *is* required. Therefore, saying STAR is "better" in terms of outcomes is not an unfair reading of the data.

In addition to measuring "aggregation competence," VSE can be used as advocacy evidence to demonstrate the robustness of a method to the public. In a recent [TEDx talk](https://youtu.be/xWQiy5VdwY0?si=ABEnMeAMKWSvMWjS), Sara Wolk, the Executive Director of the Equal Vote Coalition, introduced a version of the above chart and says:

> "Today, experts can use computer models to see how different voting methods would actually perform. And it's pretty much just like how engineers can test the plans for a new skyscraper before actually building it." (Timestamp [7:10](https://youtu.be/xWQiy5VdwY0?si=9vzXt8aI6_beTKoi&t=430))

Particularly when Ranked-Choice Voting, which is missing from this list of endorsed systems, has hogged the spotlight and attention ([at the cost of better reforms](../ditch-rcv/)), using VSE in this way is a powerful tool to demonstrate that there are far better alternatives to RCV. RCV will also receive focus in part 2, which will show exactly how abysmal it really is.

And when we look at the actual numbers, it is absolutely undeniable: In VSE, single-round Approval voting, while simple and reliable like a sedan, absolutely underperforms the Formula 1 race cars that are STAR and Condorcet. If you want to win the Monaco Grand Prix, you don't drive the beat-up sedan you got from your uncle.

The narrative, which is generally supported by the data, seems to be that Approval is the best "bang for the buck" reform, "with basically no downsides, which improves outcomes hugely" (Quinn, <d-cite key="quinn2017vseSummary"></d-cite>), but is lacking in other ways (like expressiveness and "accuracy").

On the [Equal Vote page for Approval](https://www.equal.vote/approval), they make a fair case for Approval as something that "should be the default voting method". But they also call it a "stepping stone", and say that "there's a good case to be made to upgrade further." Even though it's a "case for Approval", the text spends significant space pointing back to STAR:

> In many cases it may be quicker and easier to just switch directly from the traditional Choose-One voting method to something top of the line like STAR Voting, but we understand that there may be some cases where that's unrealistic. ([Source](https://www.equal.vote/approval), Accessed 8/14/2026)

The wording "top of the line" paints a vivid picture, to be sure. But how robust is that edge? If we are to describe VSE simulations as "like how engineers can test the plans for a new skyscraper before actually building it," then I would hope that the engineers test the skyscraper in weather other than a perfect 72-degree sunny day with a mild breeze. Perhaps we should see how the plans fare when there's a hurricane, or an earthquake, or a flood. If the skyscraper is only tested in perfect conditions, then that does not make me feel particularly safe if I have to live on the eightieth floor. If I'm going to be sold on a Formula 1 race car as my new daily driver, I don't care how fast it is on a race track if it can't handle a little mud and rain on my way to the Wendy's drive-thru.

And though there has been a good effort to stress-test VSE under a variety of conditions, models, and strategy assumptions<d-cite key="wolk2023starVoting"></d-cite>, the most unrealistic issue I take with VSE is in the assumptions of *voter information quality*.

1. Do voters *actually* know their true utilities for all the candidates on the ballot? Might some voters *think* they prefer $B$ over $A$, but would actually be happier if $A$ won? If they score $B$ higher than $A$, perhaps because of a convincing campaign ad, and the runoff is between $A$ and $B$, then this voter will accidentally vote *against* their interests in the automatic runoff step with no "undo" option.
2. What if voters have never heard of some of the candidates? If the utility maximizer is someone most voters are not aware of, then they are not likely to accumulate many stars, hurting that candidate's chance of winning. Similarly, if voters are fatigued and don't have time to thoughtfully score all the candidates, might that damage the accuracy of the election? How well do different systems handle such friction?

The common thread here is that a complex, granular, and expressive system like STAR is designed to take in more information from voters to deliver better outcomes than a more coarse system like Approval. But what if the data it collects is truncated noise rather than signal?

One particular concern I have with this is that the system is done all at once. A voter who is misinformed when they cast their initial score ballot cannot change their mind later if they realize that they were wrong. You don't know what you don't know. And many voters *are* tired and busy, and don't have time to read the campaign websites of all [61 candidates on the ballot, as we saw in the 2026 California gubernatorial primary](../ca-top-2/). Even with 6 candidates, the default in the VSE simulations, I worry about the ability of voters to accurately evaluate all candidates.

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

It seems to me that any single-round system has a "garbage in, garbage out" problem: If the data STAR collects from voters is poor, then the automatic runoff has no way to correct for that. I hypothesized that under noisy and truncated data, the edge that more granular systems like STAR and Condorcet have over more coarse systems would diminish, and that a delayed top-2 runoff is more effective at improving outcomes than an automatic runoff when there's a chance for voters to improve their information on the narrowed set of two candidates. The average on a closed-notes exam will be much worse than if you had just let the students take it home and use their notes.

In this post, we evaluate the rejected single-round STAR system proposed in Eugene, Oregon against the currently in-place Approval Top-2 system in St. Louis, Missouri. My primary evidence is a [Jupyter notebook](#the-jupyter-notebook) that copies the original VSE simulation code with significant modifications to test these hypotheses. It was written with AI-assistance by Claude Code, but the full notebook is available for transparency and reproducibility. I look forward to someone who is a more skilled coder than I am to improve upon it, and perhaps extend the model<d-footnote>I have no doubt someone is going to find a bug in my code, or an assumption that is not particularly realistic. I welcome that, and hope that this post can be a jumping-off point for further research into the robustness of voting systems to imperfect voter knowledge.</d-footnote>.

Spoiler alert: Under even mild friction, the gap between single-round Approval and STAR is basically negligible. And the delayed runoff, even with only *modestly* improved information, completely blew all single-round systems out of the water.

## The Friction Parameters

We define three parameters that we can adjust to simulate friction for voters:

### Epistemic Noise

Voters don't always know what they want. Whether that be a manipulative ad, an excellent social media presence, or a campaign blunder, sometimes a voter's feelings about a candidate don't match how they would actually feel if that candidate won.

<div class="mt-3">
  <iframe src="https://www.youtube.com/embed/rRlgq_8LNAw" class="rounded z-depth-1" style="width: 100%; aspect-ratio: 16 / 9; height: auto; display: block;" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="A Campaign Ad from Parks and Rec portraying an animated Leslie Knope trying to kill cute animals."></iframe>
</div>
<div class="caption mt-2">
  A Campaign Ad from Parks and Rec portraying an animated Leslie Knope trying to kill cute animals.
</div>

There is often an [unfortunate spike in "how to change my vote" web searches](https://appdevelopermagazine.com/change-my-vote-searches-soaring-up-during-2024-us-election/) shortly after an election. We should not always assume that a voter's *perceived* utility of a candidate is the same as their *true* utility.

We simulate this by adding noise to the voter's perceived utility of each candidate, reflecting the fact that voters are often misinformed or otherwise unable to accurately evaluate the candidates. We adjust this with the $\rho$ parameter, which is the correlation between the voter's true utility and their perceived utility.

If $u_i(c)$ is the true utility of candidate $c$ for voter $i$, then we can define a voter's perceived utility as:

$$u'_i(c) = \rho\cdot u_i(c) + \sqrt{1-\rho^2}\cdot \sigma_i \cdot \epsilon_{ic}$$

Where $\epsilon_{ic} \sim N(0,1)$ and $\sigma_i$ is the standard deviation of voter $i$'s true utilities across the candidates, used to scale the injected noise to that voter's own utility range<d-footnote>$\rho$ is exactly the Pearson correlation coefficient between the true and perceived utilities.</d-footnote>. If $\rho=1$, then the voter is perfectly informed on their exact utilities, and if $\rho=0$, then the voter's perceived utilities are pure noise. We use one global $\rho$ for all voters.

### Unfamiliarity

When a voter looks at the list of candidates, it is almost never the case that they recognize every single name on the ballot. Indeed, candidate quality is often divorced from the proportion of voters who recognize them. Whether that be a scandal-plagued incumbent or a dedicated and qualified civil servant with no name recognition, if a voter does not know a candidate, they cannot give them a thoughtful score or rank.

<div class="mt-3">
  <iframe src="https://www.youtube.com/embed/XCvC8pUI4ZA" class="rounded z-depth-1" style="width: 100%; aspect-ratio: 16 / 9; height: auto; display: block;" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen title="Bobby Newport from Parks and Rec has the name recognition, but not the qualifications"></iframe>
</div>
<div class="caption mt-2">
  Bobby Newport from Parks and Rec is Leslie Knope's opponent for city council. He has the name recognition and charisma, but not the qualifications. Even so, people won't vote for Leslie Knope if they don't know who she is.
</div>

We draw an awareness/prominence ranking for each election, simulating that everyone knows the frontrunner, but as you go down the ranking, the number of voters who are aware of each candidate decreases. For the selected $\alpha$ "awareness" parameter, the probability that a voter is aware of candidate $c$ is given by:

$$P_{\text{aware}}(c) = \alpha^{\text{prominence_rank}(c)}$$

At $\alpha=1$, all voters are aware of all candidates, while at lower values, fewer voters are aware of the candidates lower in the awareness ranking.

### Fatigue

<div class="pswp-gallery mt-3 d-flex justify-content-center" id="fatigue-tired-office-gif">
  <a href="https://media1.tenor.com/m/s-OkcMKD9VQAAAAC/tired-office.gif"
     data-pswp-width="498"
     data-pswp-height="284"
     target="_blank">
    <img src="https://media1.tenor.com/m/s-OkcMKD9VQAAAAC/tired-office.gif" class="img-fluid rounded z-depth-1" alt="Jim from The Office falling asleep" />
  </a>
</div><br>

Even if a voter is vaguely aware of a candidate, if that candidate is number 40 on a list of 61, we cannot assume that voter will necessarily take the time to scan the whole list to find them. Perhaps if Leslie Knope is first on the list, they would easily give her a solid 3 stars, but if she is far lower down, the voter might forget about her and stop looking after evaluating the first few candidates.

While prominence is global to the election, fatigue is local to the voter. We draw a random fatigue ranking for each voter, as a stand-in for ballot-order rotation. As voters go down the ballot, they are more likely to be fatigued and simply skip a name. Maybe they need to pick up their kids from soccer practice, or their eyes are glazing over from tiredness, or they just came from a nine-hour nursing shift, or they just don't care enough about who their water commissioner is to fully evaluate every person they would recognize if they had read each name closely. For the "fatigue" parameter $\beta$, the probability that a voter is not fatigued enough to vote for candidate $c$ is given by:

$$P_{\text{not fatigued}}(voter, c) = \beta^{\text{fatigue_position}(voter, c)}$$

For $\beta=1$, all voters evaluate every candidate they know, while at lower values, voters start to skip candidates lower down on their ballot, even if they are aware of them.

### How These Combine

Unfamiliarity and fatigue interact in an interesting way. To be able to vote for a candidate, a voter must be both aware of them and not fatigued. So the probability that a voter votes for candidate $c$ is given by:

$$P_{\text{genuine}} = P_{\text{aware}} \times P_{\text{not fatigued}}$$

If the check fails, then the utility for that candidate on the input ballot is set to be just below that of their least liked known candidate. This simulates voters basically saying "I don't know or remember them, so I'll leave them off my ballot". For cardinal systems like STAR and Approval, this means giving them a score of 0.

In the simulation, we assume that a voter always votes for their most preferred candidate that they are aware of, and we skip the fatigue check for that candidate.<d-footnote>The original methodology was to always evaluate the candidate with the highest $P_{\text{genuine}}$ probability, but I found that unrealistic: I decided honest voters would scan the list for the one candidate they want to vote for before going back to the top of the list and scanning down. This change actually improved the accuracy of systems like STAR, and damaged the performance of systems like Plurality and flavors of Approval.</d-footnote>

## The Runoff Assumptions

This model essentially turns voters from robots, patient enough to thoughtfully evaluate and vote for all candidates, into messy, "[satisficing](https://en.wikipedia.org/wiki/Satisficing)" humans who are often misinformed, fatigued, or otherwise unable to know which candidates would actually make them happiest. We would like to know how much of a difference a delayed runoff, with reduced cognitive load from there being just two finalists, can make in the overall accuracy of the election compared to a more granular system like STAR being used for a single-round election, taking in that poor data to perform an automatic runoff.

My hypothesis was that the delayed runoff step can act as a corrective mechanism for misinformed and ignorant voters in the primary step, whereas the more complex single-round mechanism suffers from the previously mentioned "garbage in, garbage out" issues.

However, there are a few ways that we could model improved voter information in the runoff step. We assume that in the primary election (say, in June) voters are tired and didn't have time to research all candidates in the crowded field. They vote imperfectly based on their limited knowledge (ex. vibes, not reading the candidate's website) and energy. But just how much more informed are voters in the runoff (say, in November<d-footnote>In California, the primary is in June with the general election top-2 runoff about five months later in November. In St. Louis, the general is only one month after the Approval primary.</d-footnote>)?

We first assume that fatigue is entirely removed in all delayed runoffs. With only two options, the voter is assumed to have the bandwidth to read two names and make a decision based on the direction of their preferences. The voter votes for the candidate who has a strictly higher perceived utility than the other candidate. If they are equal, then the voter is assumed to be indifferent and votes for neither (ex. if they are unaware of both).

### The Coma Model

Under the most pessimistic conditions, we could imagine that the voter has absolutely no time to update their beliefs. The voter essentially falls into a coma as soon as they submit their ballot, wakes up on election day in November, and then casts their runoff vote. We call this the "coma" runoff assumption, because I think that's kind of funny (and accurate). In Approval Top-2's coma variant, voters still have the opportunity to vote for their preferred finalist (according to their potentially misinformed preferences) without fatigue, *unless they were unaware of both candidates*.

This does mean that in a coma runoff, a voter will vote for any candidate they are aware of over any candidate they are not. That is, they might vote for the devil they know. The realism of this assumption is certainly debatable<d-footnote>It would be interesting to see alternative assumptions, such as only voting for a known candidate if they have above-average utility. That is, thinking "there's no way this other candidate can be as bad as the one I know."</d-footnote>.

An automatic runoff is very different from the coma model, and it's not necessarily clear which is better. Both systems have the potential for voters to vote against their interests.

- In STAR, a voter might give a corrupt incumbent 1 star, but be too fatigued to give a boring candidate their rightful 3 stars (or be unaware they exist). Then in the runoff, this voter's ballot will be cast for the 1-star candidate over the interpreted 0 stars.
- In coma Approval Top-2, a voter might instead be unaware of that better candidate entirely, and vote for the corrupt incumbent they know (even though they didn't approve them in the primary).

Which turned out to be better was a real shock.

### The Groggy Model

In contrast to the coma model, the remaining two models will simulate voters to have some extent of "wakefulness".

Under slightly more optimistic conditions, we can suppose that in the time between the primary and runoff, voters at least know who will be on the ballot. Like the coma model, they have no fatigue, but they also obtain awareness.

In the months since the primary election, maybe they were bombarded by unskippable YouTube ads and social media posts, drove by a yard sign every day for work, or were pelted with mailers on the exciting options for water commissioner. Though their preferences could still be noisy and in the wrong direction (because how many will actually *read* those mailers), they at least know who the candidates are.

We'll call this the "groggy" runoff assumption, and it's how we define the baseline delayed runoff systems to work (Approval Top-2 and Plurality Top-2).

### The Clear-Eyed Model

The most optimistic assumption is that voters have had time to research the candidates in the runoff step, watching the debates, reading the websites, and generally becoming more informed about the candidates.

In this ideal case, we assume that the noise and unawareness have entirely evaporated, leaving the voters with the exact correct *direction* between the candidates, regardless of their previous ignorance in the primary election. We include "clear-eyed" alternates of each delayed runoff system which use this (absurdly optimistic) assumption.

### Justification

I will not deny that the wakeful assumptions are particularly optimistic for a delayed runoff. Indeed, I might even call it "cheating"! However, it turns out that the groggy assumption is more than enough to make Approval Top-2 significantly more robust than STAR.

The proposal in Eugene *was* to eliminate the primary entirely, and have a one-shot expressive five-star score-based election for seats as prestigious and of consequence as "Commissioner for Eugene Water and Electric Board, Wards 6 and 7" (no offense to the person who actually holds that office, I'm sure Eugene's EWEB is wonderful).

On the Equal Vote Coalition's [STAR voting](https://www.equal.vote/star) page, they do present STAR as an alternative to primary elections. If replacing that [61-candidate choose-one primary we saw in California](../ca-top-2) with a single-round STAR general is an idea that is even being *considered* by STAR proponents, I feel entirely justified in rigorously testing that directly against the delayed runoff system that is already in place in St. Louis, Missouri. It is not wrong to compare apples and oranges if those are indeed the exact proposals that are competing for funding, attention, and implementation.

## Other Relevant Methodology

In the comparison, we used honest voting for all systems. This was the simplest choice, and is actually a potential disadvantage towards Approval and Plurality, since strategic voting is usually what makes the outcomes of these systems more accurate. STAR and especially Condorcet generally have their best VSE under honest voting, so this is a conservative choice that likely favors STAR and Condorcet in the comparison.

I also defined "joint scenarios" of various friction levels where I set the $\rho=\alpha=\beta$ parameters to the same values:

- 1.0: Ideal (Typical VSE simulations)
- 0.9: Mild
- 0.8: Moderate
- 0.7: Heavy

The way some parameters compound is multiplicative, so while 0.7 may not seem as heavy as, say, 0.5 or 0.3, it is actually *quite* substantial (especially with only 6 candidates).

{% proof Expand to see the friction probability table %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="friction-table" %}
{% endproof %}

I chose not to tune the parameters too much, and to use the simplest settings possible to avoid overfitting the model. I look forward to seeing how others might improve upon this model with even more realistic assumptions, use different parameter combinations, and perhaps even incorporate real-world data.

We do a number of significance tests under 95% confidence intervals (usually involving gaps in VSE). We use these to evaluate "significant" gaps, and distinguish between statistical and practical significance. For example, if a system has a gap that we can be confident is between 0.3% and 0.5%, then it is statistically significant (we can be confident the gap is non-zero), but not practically significant. It feels disingenuous and unfair to say that one system is "better" than another if the gap is so small that it would not be noticeable in practice. The terminology we use is as follows:

- Decisive: The gap is statistically significant and practically significant (greater than 1%). There is a clear and meaningful difference between the two systems.
- Narrow edge: The gap is statistically significant, but not practically significant (less than 1%). There is likely a slight difference between the two systems, but it is not meaningful in practice.
- Ambiguous edge: The gap is statistically significant, but the gap is not confidently within or outside the 1% practical significance threshold. There is a difference, but we cannot conclude whether it is meaningful in practice.
- Indistinguishable: The gap is not statistically significant (the confidence interval includes 0), but even so the gap is confidently within the 1% practical significance threshold. If a difference exists, it's not worth worrying about in practice.
- Inconclusive: The gap is not statistically significant, and the confidence interval includes both 0 and the 1% practical significance threshold. We cannot conclude anything about the gap.

I will also discuss any important statistically significant gaps that do not persist under a 99% confidence interval.

## Findings

The code is included in [the Appendix](#the-jupyter-notebook), but we will summarize the results here as it pertains to our primary focus. However, a number of other fascinating findings related to plurality voting will be discussed in the Appendix (and future parts of this series).

### The Approval-STAR Gap

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="star-vse-gap-significant" %}

Under perfect conditions, STAR is objectively more accurate than single-round Approval and Approval Top-2 (under honest ballots). For single-round Approval specifically, however, the VSE gap of about 8 points narrows under all friction scenarios. The gap is generally under about 1.5 points, and occasionally reaches significance at one friction level or another, but it's not particularly robust or consistent.

Approval Top-2, on the other hand, clearly wins out in simulations over STAR except for the "coma model", under which Approval Top-2 performed significantly worse than STAR (and single-round Approval). But even under mild friction, Approval Top-2 is significantly more accurate than STAR so long as voters are "awake" to the runoff, and this grows as friction worsens. It's not even close. This is with and without removed noise in the runoff step. Misinformed voters who at least are aware of the candidates are enough to outperform the automatic runoff.

{% proof Expand to see significance tables %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="approval-star-gap-scenarios" %}
{% endproof %}

Perhaps the most sobering statistic is how solid groggy Plurality Top-2 was in VSE compared to STAR under the sweeps and scenarios (with the clear-eyed variant being even further ahead). Despite Plurality Top-2 having completely mediocre ~80% VSE in the ideal case, it stays robust compared to all other single-round systems.

I would never advocate for Plurality Top-2<d-footnote>Technically, Plurality Top-2 is the exact system being used in California right now, including for that 61-candidate gubernatorial race. As previously mentioned, there are a number of things that VSE does not measure. For example, <em>who runs in the first place</em>. What a strong VSE for PT2 really shows is that "if the candidates are fixed and you run the election under different methods, PT2 would tend to elect a better candidate than a single-round STAR election". Plurality voting has a number of really nasty effects on the dynamics of elections beyond who wins.</d-footnote>, but this model seems to highlight that the potential corrective mechanism of a delayed runoff can somewhat salvage even the worst primary elections, whereas ignorance decimates the accuracy of all single-round systems.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="part-1-scenarios" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-help-sweep" mode="images" %}

### How Much Does a Delayed Runoff Actually Help?

First, I think we should highlight that the coma model actually ends up doing *significantly* worse than just single-round Approval and STAR. This is important because it shows that the runoff itself is not inherently a cheat to improve outcomes. Approval Top-2 is a strict improvement in the ideal case, but that's not a guarantee when voters lack awareness of candidates, and the runoff step gives them no way to correct that.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="coma-vs-approval" %}<br>

I believe the primary driver of the outcomes becoming so much worse in the coma model is the fact that we simulate that a voter always votes for the candidate they know, if they don't know the other. This can lead to voters casting votes for someone they hate because that candidate has better name recognition than a candidate they would actually prefer, whereas under single-round Approval, they would just never approve that candidate. The groggy model, on the other hand, performs far beyond STAR.

{% proof Expand to see the single-round vs runoff variants %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-vs-baseline" %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="coma-diagnostic" %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="coma-vs-groggy" %}
{% endproof %}

So far we have looked at fixed runoff awareness models (coma, groggy, clear-eyed). This gives a very binary change in how much the runoff helps. But we are interested to see what the "in-between" looks like. Particularly, at what level of improved awareness does the delayed runoff start to outperform STAR?

We define a new parameter $\kappa$, which ranges from 0 to 1. This parameter is the probability that a voter can become aware of a candidate they were not aware of before (rolled against for one or both candidates the voter is unaware of). When a voter successfully rolls to learn of a candidate, we use their (potentially noisy) perceived utility.

When a voter learns about a candidate, they vote their real (potentially noisy) preference; otherwise, they fall back on their prior information, exactly as under the coma model. Under $\kappa=0$, the coma model, STAR is significantly better than Approval Top-2. At $\kappa=1$, we have the groggy model. Eyeballing the graph, the crossing point seems to be approximately at $\kappa=0.1-0.2$ (depending on friction), where Approval Top-2 overtakes STAR in VSE.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-learn-sweep" mode="images" %}<br>

The values where the gap is significant depend on the level of friction and the level of confidence. However, it seems that you really just need at most about a one in three chance to learn about a candidate for the delayed runoff to have a significant advantage.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="p-learn-ci-table" %}

As we sweep the runoff noise $\rho$, and keep the awareness fixed between the primary and runoff, the performance does not change much for the values of $\rho$ used for the scenarios, and the dropoff in quality seems to be primarily for $\rho < 0.4$. Further investigation on scenarios where the $\rho$ values are lower would be required to say more.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-t-sweep" mode="images" %}

### STAR Silent Lock-in

I know a few "SCORE is better than STAR" fanatics, and so I did compare STAR with plain SCORE under friction. They were basically identical, but STAR generally had the edge.

{% proof Expand to see the STAR vs SCORE tables %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="score-vs-star" mode="images" %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="score-vs-star-scenarios" %}
{% endproof %}

Thus, it's not that STAR is losing VSE solely because of noise that is flipping which candidate wins in the runoff. Instead, it seems that the candidate who wins the runoff is generally still the one with the most stars.

{% proof Expand to see the STAR runoff betrayal breakdown %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="star-diagnostic" %}
{% endproof %}

The true culprit is not the automatic runoff itself, but the data fed into it. The times that STAR's automatic runoff "betrays" the voters in a way where SCORE would be better are very rare. Instead, it's the "silent lock-in" that drives the collapse of its VSE. The candidate who gets the most stars usually also wins the runoff, and this is often the worse of the two finalists under friction.

In fact, contrary to my hypothesis, the elections where the automatic runoff flips the winner from the candidate with the most stars actually appear to be *more good than bad* under the friction scenarios I tested.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="star-garbage" %}

We measure the difference between the actual automatic runoff and a hypothetical "perfect" clear-eyed runoff (i.e. 0-5 SCORE voting with a delayed runoff compared to STAR's automatic runoff), where voters are perfectly informed and vote for the candidate they truly prefer. This is a measure of how much the automatic runoff hurts voters who are misinformed in the primary step compared to a perfect clear-eyed runoff. We find that even under mild friction, STAR's automatic runoff is significantly worse than a clear-eyed runoff, and this gap grows as friction worsens.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="scoret2-vs-star" %}

This is perhaps not too surprising given that we are modeling voters as not necessarily filling out the entire ballot. Of course a delayed runoff would improve the outcomes! But it's by *how much* that makes me really concerned about STAR voting. Rather than a "cost-saving" mechanism, it could instead "cost" outcomes, and give voters who have limited time to research candidates less of a voice in the outcomes. The automatic runoff may just rubberstamp the candidate with the most stars, even if that candidate is not the one that voters would have chosen if they had more time to learn about the finalists.

Ultimately, I expected the automatic runoff to be the biggest factor in making STAR worse than Approval Top-2 under friction in a way that even a coma runoff would be able to fix. What I found instead is that the automatic runoff isn't the major problem, and a runoff on its own does not drive better outcomes (ex. the coma model). Rather, it's the chance to learn and focus on just two finalists that makes a delayed runoff so much more robust.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="scoret2-vs-at2" %}

The evidence for my hypothesis that a more coarse ballot is more robust to friction seems generally unsupported. There appears to be no (robust and persistent) significant gap, when comparing clear-eyed Approval Top-2 to a theoretical clear-eyed SCORE Top-2 delayed runoff: under ideal conditions SCORE appears significantly better, but under friction it is no more accurate than Approval Top-2<d-footnote>Under some runs, Approval Top-2 gets a significant (but narrow) edge under a 95% confidence interval in some friction scenario, but it hasn't yet persisted under a 99% confidence interval. I don't feel comfortable making any claims that Approval Top-2 is actually strictly better than SCORE Top-2 in the models I have tested.</d-footnote>.

At the very least, for this comparison of a theoretical SCORE Top-2 (that nobody is actually advocating for) with the St. Louis model, I would say that the SCORE ballot appears completely unjustified. That granularity does not seem to help outcomes under friction. The real difference, if not outcomes, is then how much more intimidating and easier to spoil the ballot is, and how politically viable proposing that change becomes. Approval is essentially the hardest ballot type to unintentionally spoil (there is no such thing as an overvote), so I would conclude a SCORE ballot is strictly worse in this context.

The gulf between the *automatic* runoff of STAR and a delayed Approval runoff, however, is very, very large. There is no ambiguity there.

<div class="pswp-gallery mt-3 d-flex justify-content-center" id="star-from-friction-meme">
  <a href="/assets/img/star_from_friction.jpg"
     data-pswp-width="889"
     data-pswp-height="500"
     target="_blank">
    <img src="/assets/img/star_from_friction.jpg" class="img-fluid rounded z-depth-1" alt="Parks and Rec meme of Ron Swanson and Ben Wyatt: STAR Voting has really bad VSE. It rubbed off. From friction." />
  </a>
</div>

## Conclusion

It is absolutely undeniable that, with perfectly informed voters who fill out their ballots completely and accurately, STAR is an objectively more accurate mechanism than Approval. That granularity is a genuine strength when the data is high quality. However, that granularity fails to deliver when the data you collect is noisy or incomplete, making the system no better than the simpler single-round Approval.

Based on my findings, I would say that for something like a city council trying to decide between a few different options for the placement of a new library (where the voter assumptions for the original VSE model are very likely accurate), STAR would be an excellent choice. Highly informed voters, who will give full and thoughtful scores to all available options, match better with the assumptions that underlie the ideal VSE numbers commonly reported. It could be easily expected that there will be cases where STAR would produce higher-quality outcomes than the council members simply approving of which options they find acceptable. This is the use case where STAR can really *shine*.

*Publicly electing that city council*, however, is a different story. I do not find it plausible that voters are going to be able to give thoughtful and accurate scores to all candidates for a local election. A simpler system like Approval, with a delayed runoff, seems more likely to produce better outcomes if the data collected from voters is likely low quality. Under such conditions, the gain from even just single-round Approval to STAR appears to be negligible.

If there is anything I have taken away from this project, it's that a delayed runoff is of **enormous benefit**. A narrowing process seems absolutely necessary, and using the simple Approval system for that winnowing seems to be the most robust and practical option. It scales exceptionally well to crowded fields, compared to a ranking or scoring system, and eliminates the vote splitting we see in the Plurality Top-2 systems used in Washington and California. If 61 candidates on the ballot is a possibility, then Approval is the only system that can handle that without completely overbloating the ballot and overwhelming voters.

### The Broader Context

Independent of the results of these simulations is the fact that STAR is an objectively more complex system than Approval. And that seems exceptionally important for consideration as our ticket away from choose-one voting.

STAR has been rejected three times by voters in Oregon. There is the Eugene situation that has framed this discussion, of course. But it was also rejected in [Lane County in 2018](https://ballotpedia.org/Lane_County,_Oregon,_Measure_20-290,_Score_Then_Automatic_Runoff_Voting_Method_(November_2018)) (52.4% opposed, also would have eliminated primaries) and [Oakridge in 2024](https://ballotpedia.org/Oakridge,_Oregon,_Measure_20-364,_STAR_Voting_for_Three_Election_Cycles_Amendment_(November_2024)) (53.56% opposed, and this was a reversible low-stakes three-election pilot test).

Fundamentally, I have to ask: is scoring the options for Commissioner of the Eugene Water and Electric Board the way you rate a restaurant on Yelp actually something the average voter is clamoring to do?

Unlike the question of equity in primary election turnout, for which there is a strong case to be made on both sides, research on ballot-marking errors<d-cite key="neelyMcDaniel2015overvoting"></d-cite> shows a more directly measurable effect. Well-intentioned "expressiveness" has a darker side-effect when looking at RCV in San Francisco: Spoiled ballot rates were disproportionately higher for Black, Latino, elderly, lower-income groups, and foreign born residents.

> "[The] evidence suggests it is not IRV per se but rather ballot complexity more generally that leads to such discrepancies in whose votes get counted."<d-cite key="neelyMcDaniel2015overvoting"></d-cite>

STAR is a significant improvement in how difficult it is to spoil a ballot over RCV, but when you suggest anything more complex than choose-one or Approval, I think we have to be incredibly mindful of what the cost of complexity could be, and if the theoretical benefits of granularity and complexity justify it. I think it is safe to say, however, that Approval is easily the hardest ballot type to spoil, which is a benefit to consider. When a more granular ballot and system fails to justify itself in producing significantly better outcomes, it essentially just creates more ways to disenfranchise people who don't have the time to treat politics like a hobby.

The evidence in favor of STAR thus far is primarily in simulations done *by STAR proponents themselves*. And though I find their methodology excellent and without obvious flaws or a hint of bias<d-footnote>In the paper by Wolk, Quinn, and Ogren<d-cite key="wolk2023starVoting"></d-cite>, they mention that Quinn originally expected the model to find support for systems like Majority Judgment, but instead found that STAR had superior performance. They are also very up-front about their potential conflicts of interest regarding the fact that Wolk is the executive director for an organization advocating for the methods discussed in the paper. It is entirely above board, rigorous work by experts I have great respect for.</d-footnote>, the numbers so far have not swung me to becoming a STAR supporter.

If we suppose that expressiveness begets complexity which makes the system *less* robust to real-world conditions, and risks disenfranchising marginalized groups, then Approval Top-2 seems better suited as a short-term practical reform than STAR voting. I do not find sufficient evidence that STAR is better suited for public elections than the St. Louis model of Approval Top-2. I do not yet approve of STAR.

In a 1998 paper by Regenwetter and Grofman, they analyzed the outcomes of real Approval elections to see if they might match the theoretical outcomes under ranked methods like Borda or Condorcet from reconstructed preferences. They reach the same conclusion I do, by a very different route:

> "We find no evidence here that approval voting should be replaced by a more elaborate voting scheme." (p. 532<d-cite key="regenwetterGrofman1998approvalBordaCondorcet"></d-cite>)

When we step beyond the idealized assumptions of perfect voters, we find that the "top of the line" systems like STAR perform far worse than the simpler two-round system being used *right now* in St. Louis. Approval Top-2 may not be a compromise at all, but actually superior and more accurate than the more complex STAR that it has been overlooked in favor of. And when voters have actually been asked to choose STAR for themselves, they've said no every time. Perhaps we've been attempting to overcomplicate our elections, flying too close to the sun chasing perfection. All the while, the most robust solution might just be quietly working in Missouri as we speak.

## Appendix

I would like to round off part 1 with a few surprising findings related to choose-one voting.

### The Plurality Bump

Earlier, I mentioned the surprising robustness of Plurality Top-2 under friction. Related to this was a general trend where mild friction seemed to make plurality methods *better*. I have a few ideas for why this might be.

Unlike every other voting system, choose-one voting is the only one where fatigue has no effect on outcomes. With the methodological adjustment that a voter always evaluates their favorite known candidate, plurality is functionally identical as fatigue is varied.

In every other voting system, there's an attempt to extract *more* data from voters by allowing some sort of expression for other candidates. This makes plurality voting robust to fatigue and unawareness, the latter of which might *tighten* outcomes because voters are less likely to vote for a candidate who has no chance. The prominence model focuses votes on a smaller number of candidates, which could sort of accidentally simulate the strategic voting which makes plurality more effective. The highest VSE for the unawareness sweep is indeed at 0.9, which is what we use for mild friction.

However, the most paradoxical effect is sweeping the noise parameter $\rho$ downwards. This, somehow, maximizes the VSE of single-round plurality around $\rho=0.5$, to a VSE of around 80%. I have no robust explanation for this. But this might somehow scramble voter preferences further into a more "strategic" vote. This requires further investigation. A cursory investigation shows that under mild friction, there are indeed elections where the noise produces a worse outcome, but there are just *more* where it seems to produce a better outcome.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="plurality-ideal-vs-friction" %}<br>

The VSE of single-round plurality is never *good* under the defined scenarios, but mild friction decently improves the outcomes. Plurality Top-2 under mild friction is actually on par with some of the *good* systems under ideal conditions.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="plurality-bump" %}<br>

This leads me to an uncomfortable conclusion that choose-one voting, for as flawed as its outcomes are, might actually be in some ways well-suited to our tired human brains. The mental shortcuts that we take might actually hone the outcomes of our terrible voting system to some extent. If nothing else, choose-one voting is simple to use and simple to count. But Approval maintains that same simplicity, while improving candidate incentives and reducing problems like the spoiler effect and vote splitting.

### Approval vs Plurality

Despite the plurality bump, Approval still strongly outperforms plurality voting under friction.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="plurality-vs-approval" %}<br>

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="plurality-approval-ci" %}

The Top-2 variants were less clear-cut. Approval Top-2 clearly outperforms Plurality Top-2 under mild friction. However, this edge does not remain robust or consistent under higher friction scenarios.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="at2-pt2-ci" %}

I also did an analysis of the difference between Approval Top-2 and Plurality Top-2 when we vary the number of candidates. The idea is that for 6 candidates, the two may have similar performance, but vote splitting would become more of a problem for choose-one as the number of candidates increases. Under ideal conditions, AT2 stays fairly consistent, while PT2 declines rather quickly, and Approval Top-2 is substantially better than Plurality Top-2.

This edge declines under friction and loses robustness. However, it seems that there is no evidence that Plurality Top-2 is better than Approval Top-2 under any scenario. The idea that Approval is a Pareto improvement over plurality seems reasonably supported: any flavor of Approval seems to be as good or better than that same flavor of Plurality.

{% proof Expand to see the candidate sweep analysis %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="at2-pt2-candidate-sweep" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="at2-pt2-candidate-ci" %}
{% endproof %}

### A Stricter Confidence Interval

These are the results which did not hold statistically significant under a 99% confidence interval. None change the major headlines of the post, and are generally quite borderline or inconsequential.

{% proof Click to expand %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="not-sig-at-99-part1" %}
{% endproof %}

### Jameson Quinn

This post obviously would not exist without the incredible work of Jameson Quinn, who died in March 2025. Dr. Quinn was a Harvard-trained statistician who contributed so much to the movement to improve our democracy with better voting systems, including his groundbreaking VSE methodology. I never met him, but I certainly owe him a debt of gratitude. I hope that this modification to his model does his amazing work justice. Please consider donating to the [Jameson Quinn Memorial Fund](https://www.equal.vote/jameson_quinn).

### The Jupyter Notebook

I am sure this post is going to be particularly controversial, so the full simulation can be [downloaded here](https://github.com/eigentaylor/eigentaylor.github.io/blob/main/assets/jupyter/vse_simulation.ipynb). It became too big to embed in the post, but the tables and charts are embedded directly from the notebook, and are generated automatically.

I encourage anyone who is interested to run the notebook themselves and scrutinize my methodology!
