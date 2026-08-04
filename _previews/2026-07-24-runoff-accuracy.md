---
layout: distill
title: 'Coarse Correction: Is STAR Actually More Accurate than Approval?'
date: 2026-08-02
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
    subsections:
      - name: The Broader Context
  - name: Appendix
    subsections:
      - name: The Plurality Bump
      - name: Approval vs Plurality
      - name: The Ranked Methods Implosion
      - name: Condorcet Efficiency
      - name: SCORE vs STAR
      - name: The Jupyter Notebook
---

## Introduction

Voter Satisfaction Efficiency (VSE)<d-cite key="quinn2017vseSummary"></d-cite> is an incredible metric used for evaluating the performance of voting systems, primarily championed by the Equal Vote Coalition. It gives a numeric percentage to the "accuracy" of a voting system, with 0% being just a system that randomly chooses a winner, and 100% being a system that always elects the "best" (highest utility) candidate<d-footnote>VSE isn't the frequency of electing the single-best candidate. Rather, it's a linear rescaling of average voter utility normalized to the scale between random (average of all candidate utilities) and best. A VSE of 50% would, for example, mean that the candidate it tends to elect provides utility halfway between the average and the best, potentially without ever picking the single best candidate.</d-footnote>.

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

The Equal Vote Coalition supports three systems, which all have high VSE: STAR, Condorcet<d-footnote>Technically, they champion their particular flavor of Condorcet, "Ranked Robin", but the differences are minor and not relevant to this discussion. In what follows, we will focus on the Schulze method, which is a particularly robust Condorcet method used in a number of <a href="https://en.wikipedia.org/wiki/Schulze_method#Usage">organizations, societies, and even some local governments in Europe</a>.</d-footnote>, and Approval. My numbers are slightly lower than those reported by Jameson Quinn<d-cite key="quinn2017vseSummary"></d-cite>, but his report was nearly 10 years ago, so I will report the numbers I got by adapting the code as it is in the electionscience Github repository:

- Condorcet methods: Voters rank candidates and the candidate who defeats all others is the winner (with some tiebreaker in the rare case where one does not exist). We call the candidate who defeats all others the Condorcet winner. These usually get the highest VSE, but drop low due to strategy, despite the fact that strategic voting is just [not very effective in Condorcet methods](../better-choices-strategy/). The fact is, pairwise dominance ([while not a prerequisite for being the utility maximizer](../why-condorcet/)) is objectively a strong predictor of high utility.
- STAR voting (Score Then Automatic Runoff): Voters score candidates on a scale (usually 0-5), and the two highest-scoring candidates go to an automatic runoff where a candidate gets one vote for every voter who scored them higher than the other candidate. This system has arguably the best VSE range of the three.
- Approval voting: Voters can approve of as many candidates as they like, and the candidate with the most approvals wins. This is a system with surprisingly high VSE for its refreshing simplicity. With a top-2 runoff, Approval improves its VSE to be quite competitive with other more granular alternatives.

Missing from this list of endorsed systems is Ranked-Choice Voting (RCV). Although RCV is technically a serious contender in the reform space, it is not a serious consideration by organizations like the Equal Vote Coalition, Center for Election Science, and Better Choices for Democracy. [People who do the math don't support RCV](../ditch-rcv/). Its poor design and mechanism leads to a number of glaring issues<d-footnote>Including the spoiler effect, vote splitting, and center-squeezes. If your favorite can't win, your vote does not necessarily transfer, and this can lead to a compromise candidate getting eliminated early. Major RCV failures have already occurred in Burlington, VT, and Alaska. RCV does not deliver on its promises, plain and simple<d-cite key="wolk2023starVoting"></d-cite>.</d-footnote> including being absurdly impractical and expensive, just to deliver mediocre outcomes.

The following is the VSE range of the major reforms that are currently being considered in the United States.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="evc-vse" %}

In addition to measuring "aggregation competence," VSE can be used as advocacy evidence to demonstrate the robustness of a method to the public. In a recent [TEDx talk](https://youtu.be/xWQiy5VdwY0?si=ABEnMeAMKWSvMWjS), Sara Wolk, the Executive Director of the Equal Vote Coalition, introduces a version of the above chart and says:

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

Particularly when Ranked-Choice Voting has hogged the spotlight and attention (at the cost of better reforms), using VSE in this way is a powerful tool to demonstrate that there are far better alternatives to RCV. These simulations *do* show the shortcomings of RCV's blindness, due to its inability to see beyond the current active choice of a voter. The three systems supported by the Equal Vote Coalition all solve the issue of vote splitting by looking at each voter's *entire* ballot *immediately*, and that translates to strong VSE<d-footnote>There are other considerations as well that make these three systems the strongest choices, beyond excellent outcomes: They are logistically easy to implement and count, and are fairly resistant to strategic voting compared to some other methods.</d-footnote>.

And when we look at the actual numbers, they generally support their narrative that STAR does the overall best job at finding the highest utility candidate<d-footnote>Condorcet methods are also exceptionally strong performers in this regard, but there is a valid case that scoring requires less cognitive load and scales better than a ranked system with many candidates.</d-footnote>, while Approval is a simple and effective alternative that they also "approve of".

In Quinn's 2017 summary, he has this to say:

> [Approval is] not the best of the methods I tested, but it certainly is the best "bang for the buck"; a simple reform, with basically no downsides, which improves outcomes hugely. (Quinn, 2017<d-cite key="quinn2017vseSummary"></d-cite>)

And it is absolutely undeniable: single-round Approval voting, while simple and strong like a reliable sedan, absolutely underperforms the fancy Ferrari that is STAR, and the finely-tuned Formula 1 race car of Schulze, in VSE. If you want to win the Monaco Grand Prix, you don't drive the sedan you got from your uncle.

On the [Equal Vote page for Approval](https://www.equal.vote/approval), they make a fair case for Approval as something that "should be the default voting method". But they also call it a "stepping stone", say that "there's a good case to be made to upgrade further," and even though it's a "case for Approval", the text spends significant space pointing back to STAR:

> In many cases it may be quicker and easier to just switch directly from the traditional Choose-One voting method to something top of the line like STAR Voting, but we understand that there may be some cases where that's unrealistic. ([Source](https://www.equal.vote/approval), Accessed 7/30/2026)

The wording "top of the line" paints a vivid picture, to be sure. But how robust is that edge? If we are to describe VSE simulations as "like how engineers can test the plans for a new skyscraper before actually building it," then I would hope that the engineers test the skyscraper in weather other than a perfect 72-degree sunny day with a mild breeze. Perhaps we should see how the plans fare when there's a hurricane, or an earthquake, or a flood. If the skyscraper is only tested in perfect conditions, then that does not make me feel particularly safe if I have to live on the eightieth floor.

And though there has been a good effort to stress-test VSE under a variety of conditions and models<d-cite key="wolk2023starVoting"></d-cite>, the most unrealistic issue I take with VSE is in the assumptions of *voter information quality*.

> If the voter model, media model, and strategy model are realistic for a particular context, then VSE is probably a good metric for comparing voting methods. (Quinn, 2017<d-cite key="quinn2017vseSummary"></d-cite>)

I agree with this wholeheartedly. And in questioning the realism of the voter model, some questions that I would like to raise are:

1. Do voters *actually* know their true utilities for all the candidates on the ballot? Might some voters *think* they prefer $B$ over $A$, but would actually be happier if $A$ won? If they score $B$ higher than $A$, perhaps because of a convincing campaign ad, and the runoff is between $A$ and $B$, then this voter will accidentally vote *against* their interests in the automatic runoff step with no "undo" option.
2. What if voters have never heard of some of the candidates? If the utility maximizer is someone most voters are not aware of, then they are not likely to accumulate many stars, hurting that candidate's chance of winning. Similarly, if voters are fatigued and don't have time to thoughtfully score all the candidates, might that damage the accuracy of the election? How well do different systems handle such friction?

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

My concern is that an automatic runoff has a "garbage in, garbage out" problem: if the data collected from voters is poor, then the automatic runoff has no way to correct for that<d-footnote>This is a different pathology than the core problem with RCV. In RCV, even a perfectly filled out ballot can be weaponized against the voter due to the chaotic elimination order. The issue I am raising with STAR is based on inaccurately filled out ballots, which affects systems like Schulze and RCV just as much, if not more.</d-footnote>. In a delayed runoff, voters have a chance to familiarize themselves with the candidates in the narrowed field, and can make a more informed choice.

### A Tale of Two Cities

In 2024, a proposal in [Eugene, Oregon to eliminate primary elections for mayor, city council, and EWEB seats and replace them with STAR voting](https://ballotpedia.org/Eugene,_Oregon,_Measure_20-349,_STAR_Voting_for_Mayor_and_City_Council_Elections_Initiative_(May_2024)) was voted down by 64.49%. In 2020, [St. Louis, MO voters voted to adopt an all-candidate Approval voting primary election with a delayed top-2 runoff](https://ballotpedia.org/St._Louis,_Missouri,_Proposition_D,_Approval_Voting_Initiative_(November_2020)) by 68.15%. This system is still in place, and working excellently<d-cite key="sargent2025stlouis"></d-cite>. The comparison between these two proposals will be the focus of this post.

[The pitch](https://www.starvoting.org/eugene_faq) for a single-round STAR election was to save money by eliminating low-turnout primary elections<d-footnote>There was also a fair point that the primary elections generally have lower turnout which is disproportionately white, and that a single election might improve equity. The St. Louis proposition, however, was explicitly framed as <a href="https://www.stlamerican.com/election/prop-d-expected-to-protect-the-collective-power-of-black-voters/">protecting black voters from vote splitting with that primary election</a>. So there are real equity arguments on both sides, and "does X system help/hurt Y demographic" is an exceptionally complicated question that we won't focus on here.</d-footnote>, and just quickly elect the best candidate through an *automatic* runoff performed on an expressive and rich dataset collected in the high-turnout November election. And I assume they chose STAR over the existing Approval Top-2 system used in St. Louis because they see it as more accurate than Approval. Surely, a system with higher VSE is better than one with worse VSE, right?

> "STAR Voting is highly accurate with any number of candidates in the race, so there’s no need for an expensive primary for nonpartisan elections in most cases." ([Source](https://www.starvoting.org/eugene_faq))

I hypothesized that under noisy and truncated data, the edge that more granular systems like STAR and Condorcet have over more coarse systems would diminish, and that a delayed top-2 runoff is more effective at improving outcomes than an automatic runoff when there's a chance for voters to improve their information on the narrowed set of two candidates.

In this post, we evaluate the rejected single-round STAR system proposed in Eugene, Oregon against the currently in-place Approval Top-2 system in St. Louis, Missouri. My primary evidence is a [Jupyter notebook](#the-jupyter-notebook) that uses the original VSE simulation code with significant modifications to test these hypotheses. It was written with AI-assistance by Claude Code, but the full notebook is included for full transparency and reproducibility. I look forward to someone who is a more skilled coder than I am to improve upon it, and perhaps extend the model<d-footnote>I have no doubt someone is going to find a bug in my code, or an assumption that is not particularly realistic. I welcome that, and hope that this post can be a jumping-off point for further research into the robustness of voting systems to imperfect voter knowledge.</d-footnote>.

Spoiler alert: Under even mild friction, the gap between single-round Approval and STAR is basically negligible. And the delayed runoff, even with only *minimally* improved information, completely blew all single-round systems out of the water.

## The Friction Parameters

We define three parameters that we can adjust to simulate friction for voters:

### Epistemic Noise

Voters don't always know what they want. Whether that be a manipulative ad, an excellent social media presence, or a campaign blunder, sometimes a voter's feelings of a candidate don't match how they would actually feel if that candidate won. There is often an [unfortunate spike in "how to change my vote" web searches](https://appdevelopermagazine.com/change-my-vote-searches-soaring-up-during-2024-us-election/) shortly after an election, which means that we should not always assume that a voter's *perceived* utility of a candidate is the same as their *true* utility.

We simulate this by adding noise to the voter's perceived utility of each candidate, reflecting the fact that voters are often misinformed or otherwise unable to accurately evaluate the candidates. We adjust this with the $t$ parameter, which is the correlation between the voter's true utility and their perceived utility.

If $u_i(c)$ is the true utility of candidate $c$ for voter $i$, then we can define a voter's perceived utility as:

$$u'_i(c) = t\cdot u_i(c) + \sqrt{1-t^2}\cdot \sigma_i \cdot \epsilon_{ic}$$

Where $\epsilon_{ic} \sim N(0,1)$ and $\sigma_i$ is the standard deviation of voter $i$'s true utilities across the candidates, used to scale the injected noise to that voter's own utility range. Then $t$ is exactly the Pearson correlation coefficient between the true and perceived utilities. If $t=1$, then the voter is perfectly informed on their exact utilities, and if $t=0$, then the voter's perceived utilities are pure noise. We use one global $t$ for all voters.

### Unfamiliarity

When a voter receives their ballot, it is almost never the case that they recognize every single name on the ballot. Indeed, candidate quality is often divorced from the proportion of voters who recognize them. Whether that be a scandal-plagued incumbent or a dedicated and qualified civil servant with no name recognition, if a voter does not know a candidate, they cannot accurately evaluate them.

We draw an awareness/prominence ranking for each election, simulating that everyone knows the frontrunner, but as you go down the ranking, the number of voters who are aware of each candidate decreases. For the selected $\alpha$ "awareness" parameter, the probability that a voter is aware of candidate $c$ is given by:

$$P_{\text{aware}}(c) = \alpha^{\text{prominence_rank}(c)}$$

At $\alpha=1$, all voters are aware of all candidates, while at lower values, fewer voters are aware of the candidates lower in the awareness ranking.

### Fatigue

Even if a voter is vaguely aware of a candidate, if that candidate is number 40 on a list of 61, we cannot assume that voter will necessarily take the time to scan the whole list to find them. Perhaps if that candidate is first on the list, they would easily give them a solid 3 stars, but if that candidate is far lower down, the voter might forget about them and stop looking after evaluating the first few candidates.

While prominence is global to the election, fatigue is local to the voter. We draw a random fatigue ranking for each voter, as a stand-in for ballot-order rotation. As voters go down the ballot, they are more likely to be fatigued and simply skip a name. Maybe they need to pick up their kids from soccer practice, or their eyes are glazing over from tiredness, or they just came from a nine-hour nursing shift, or they just don't care enough about who their water commissioner is to fully evaluate every person they would recognize if they had read each name closely. For the "fatigue" parameter $\ell$, the probability that a voter is not fatigued enough to vote for candidate $c$ is given by:

$$P_{\text{not fatigued}}(voter, c) = \ell^{\text{fatigue_position}(voter, c)}$$

### How These Combine

Unfamiliarity and fatigue interact in an interesting way. To be able to vote for a candidate, a voter must be both aware of them and not fatigued. So the probability that a voter votes for candidate $c$ is given by:

$$P_{\text{genuine}} = P_{\text{aware}} \times P_{\text{not fatigued}}$$

If the check fails, then the utility for that candidate on the input ballot is set to be just below that of their least liked known candidate. This simulates voters basically saying "I don't know or remember them, so I'll leave them off my ballot".

This is how Schulze (Condorcet) would interpret a truncated ballot: all unranked candidates are tied below all ranked ones, and treated as the voter being indifferent between them. For cardinal systems, this functionally gives unknown candidates a 0 score (unapproved for Approval). In RCV, a voter's ballot cannot transfer to a candidate they did not vote for.

Originally, I ensured that the voter is always aware of the candidate with the highest $P_{\text{genuine}}$ probability, and always evaluates them. However, I decided a more realistic model is that a voter will always ensure that they evaluate their favorite *known* candidate. That is, of the candidates that voter is aware of, they always give that candidate a full evaluation (an approval, 5 stars, a first ranking, or a plurality vote). Changing to this assumption also improved the accuracy of a number of systems including STAR voting. 

## The Runoff Assumptions

This model essentially turns voters from robots, patient enough to thoughtfully evaluate and vote for all candidates, into messy humans who are often misinformed, fatigued, or otherwise unable to know which candidates would actually make them happiest. We would like to know how much of a difference a delayed runoff, with reduced cognitive load from there being just two finalists, can make in the overall accuracy of the election compared to a more granular system like STAR being used for a single-round election, taking in that poor data to perform an automatic runoff.

My hypothesis was that the runoff step can act as a corrective mechanism for misinformed voters in the primary step, whereas the more complex single-round mechanism suffers from the previously mentioned "garbage in, garbage out" issues.

However, there are a few ways that we could model improved voter information in the runoff step. We assume that in the primary election (say, in June) voters are tired and didn't have time to research all candidates in the crowded field. They vote imperfectly based on their limited knowledge (ex. vibes, not reading the candidate's website) and energy. But just how much more informed are voters in the runoff (say, in November<d-footnote>In California, the primary is in June with the general election top-2 runoff about five months later in November. In St. Louis, the general is only one month after the Approval primary. Either way, that is a fair amount of time to find out who the general election candidates are.</d-footnote>)?

We first assume that fatigue is entirely removed in a delayed runoff. With only two options, the voter is assumed to have the bandwidth to read two names and make a decision based on the direction of their preferences. The voter votes for the candidate who has a strictly higher perceived utility than the other candidate. If they are equal, then the voter is assumed to be indifferent and votes for neither (ex. if they are unaware of both).

### The Coma Model

Under the most pessimistic conditions, we could imagine that the voter has absolutely no time to update their beliefs. The voter essentially falls into a coma as soon as they submit their ballot, wakes up on election day in November, and then casts their runoff vote. We call this the "coma" runoff assumption, because I think that's kind of funny (and accurate). In Approval Top-2's coma variant, voters still have the opportunity to vote for their preferred finalist (according to their potentially misinformed preferences) *unless they were unaware of both candidates*.

The coma model is **not** how STAR functions (but it is close). The flawed understanding does indeed carry over to the runoff step, without a chance to be corrected. However, STAR is slightly worse here because if you gave both finalists an equal score, you have no chance to influence that final outcome (unlike in Approval where a voter with a strict preference who does not distinguish between the two finalists on their primary ballot is not precluded from casting a vote in the runoff).

For example, if you gave finalist $A$ one star because they're terrible, but the other finalist $B$ was at the bottom of your ballot so you forgot to give them their rightful three stars (perhaps they were okay, and not at the front of your mind, but you needed to pick up your kid from daycare and so you left them blank), then you have no opportunity to correct that mistake, and your ballot will be interpreted as being for your dispreferred candidate $A$ over your preferred candidate $B$.

### The Groggy Model

In contrast to the coma model, the remaining two models will simulate voters to have some extent of "wakefulness".

Under slightly more optimistic conditions, we can suppose that in the time between the primary and runoff, voters at least know who will be on the ballot. In the months since the primary election, maybe they were bombarded by television ads and social media posts, drove by a yard sign every day for work, or were pelted with mailers on the exciting options for water commissioner, and now they at least know who the two finalists are, though their preferences could still be noisy and in the wrong direction (because how many will actually *read* those mailers).

We'll call this the "groggy" runoff assumption, and it's how we define the baseline delayed runoff systems to work (Approval Top-2 and Plurality Top-2).

### The Clear-Eyed Model

The most optimistic assumption is that voters have had time to research the candidates in the runoff step, watching the debates, reading the websites, and generally becoming more informed about the candidates.

In this ideal case, we assume that the noise and unawareness have entirely evaporated, leaving the voters with the exact correct *direction* between the candidates, regardless of their previous ignorance in the primary election. We include "clear-eyed" alternates of each delayed runoff system which use this assumption.

It's likely that the reality of the situation is somewhere between these assumptions. We include an analysis that sweeps from the coma model to the clear-eyed model, and shows how much of a difference it makes in the overall accuracy of the election.

### Justification

I will not deny that the wakeful assumptions are particularly optimistic for a delayed runoff. Indeed, I might even call it "cheating"! However, it turns out that the groggy assumption is more than enough to make Approval Top-2 significantly more robust than STAR.

The proposal in Eugene *was* to eliminate the primary entirely, and have a one-shot expressive five-star score based election for seats as prestigious and of consequence as "Commissioner for Eugene Water and Electric Board, Wards 6 and 7" (no offense to the person who actually holds that office, I'm sure Eugene's EWEB is wonderful).

Any voter who fails to distinguish between the finalists (or accidentally submits a ballot with the order reversed) due to fatigue or lack of information would have absolutely no recourse to influence the outcome. In *any* top-2 system, all voters are guaranteed an opportunity to have final say in who is elected in a cognitively simple two-candidate race in November.

Further, in response to the previously mentioned California Gubernatorial primary (with 61 candidates), I did hear the suggestion of eliminating the primary in favor of a single-round STAR election (just as was proposed in Eugene). If replacing that 61-candidate choose-one primary with a single-round STAR general is an idea that is even being *considered* by STAR proponents, I feel entirely justified in rigorously testing that directly against the delayed runoff system that is already in place in St. Louis, Missouri. It is not wrong to compare apples and oranges if those are indeed the exact proposals that are competing for funding, attention, and implementation.

## Other Relevant Methodology

I tried to keep the default settings of the original vse-sim as much as possible. This includes simulating just six candidates, rather than 61, and 101 voters. I made an effort to change the code as little as possible, and included various sanity checks to see that the output was reasonable and matched expectations (before adding my friction parameters).

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="strategy-sweep-chart" %}<br>

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="vse-range-baseline" %}

{% proof Expand to see VSE tables %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="vse-tables" %}
{% endproof %}

Additionally, in the comparison, we used honest voting for all systems. This was the simplest choice, and is actually a potential disadvantage towards Approval and Plurality, since strategic voting is usually what makes the outcomes of these systems more accurate. STAR and especially Condorcet generally have their best VSE under honest voting, so this is a conservative choice that likely favors STAR and Condorcet in the comparison.

I also defined "joint scenarios" of various friction levels where I set the $t=\alpha=\ell$ parameters to the same values:

- 1.0: Ideal (Current VSE simulations)
- 0.9: Mild
- 0.8: Moderate
- 0.7: Heavy

The way some parameters compound is multiplicative, so while 0.7 may not seem as heavy as, say, 0.5 or 0.3, it is actually *quite* substantial (especially with only 6 candidates).

{% proof Expand to see the friction probability table %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="friction-table" %}
{% endproof %}

I chose not to tune the parameters too much, and to use the simplest settings possible to avoid overfitting the model. I look forward to seeing how others might improve upon this model with even more realistic assumptions, use different parameter combinations, and perhaps even incorporate real-world data.

## Findings

The code is included in [the Appendix](#the-jupyter-notebook), but we will summarize the results here as it pertains to our primary focus. However, a number of other fascinating findings will be discussed in the Appendix.

### The Approval-STAR Gap

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="approval-star-gap-scenarios" %}

Under perfect conditions, STAR is objectively more accurate than single-round Approval and Approval Top-2 (under honest ballots). For single-round Approval specifically, however, the VSE gap narrows under all friction scenarios. A 95% confidence interval on the VSE gap between single-round Approval and STAR voting, using a paired test, consistently contains 0 for all friction scenarios except heavy friction.

Approval Top-2, on the other hand, clearly wins out in simulations over STAR and Schulze except for the "coma model", which was significantly worse. Even under mild friction, Approval Top-2 is significantly more accurate than STAR so long as voters are "awake" to the runoff, and this grows as friction worsens. It's not even close. This is with and without removed noise in the runoff step. Misinformed voters who at least are aware of the candidates are enough to outperform the automatic runoff.

{% proof Expand to see significance tables %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="star-vse-gap-significant" %}
{% endproof %}

Perhaps the most sobering statistic is how solid groggy Plurality Top-2 was in VSE compared to STAR under the sweeps and scenarios (with the Clear-Eyed variant being even further ahead). Despite Plurality Top-2 having completely mediocre ~80% VSE in the ideal case, it stays robust compared to all other single-round systems<d-footnote>Technically, Plurality Top-2 is the exact system being used in California right now, including for that 61 candidate Gubernatorial race.</d-footnote>.

I would never advocate for Plurality Top-2<d-footnote>As previously mentioned, there are a number of things that VSE does not measure. For example, <em>who runs in the first place</em>. What a strong VSE for PT2 really shows is that "if the candidates are fixed and you run the election under different methods, PT2 would tend to elect a better candidate than a single-round STAR election". Plurality voting has a number of really nasty effects on the dynamics of elections beyond who wins.</d-footnote>, but this model seems to highlight that the potential corrective mechanism of a delayed runoff can somewhat salvage even the worst primary elections, when ignorance decimates the accuracy of the "more accurate" single-round system used.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="vse-joint" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-help-sweep" mode="images" %}

### How much does a delayed runoff actually help?

So far we have looked at fixed runoff awareness models (coma, groggy, clear-eyed). This gives a very binary change in how much the runoff helps. But we are interested to see what the "in-between" looks like.

We define a new parameter `p_learn`, which ranges from 0 to 1. This parameter is the probability that a voter can become aware of a candidate they were not aware of before (rolled against for one or both candidates the voter is unaware of). When a voter successfully rolls to learn of a candidate, we use their (potentially noisy) perceived utility.

When a voter learns about a candidate, they vote their real (potentially noisy) preference; otherwise, they fall back on their prior information, exactly as under the coma model. Under `p_learn=0`, the coma model, STAR is significantly better than Approval Top-2. Eyeballing the graph, the crossing point seems to be approximately at $p_{learn}=0.2$, where Approval Top-2 overtakes STAR in VSE (at this point, the gap is insignificant). By $p_{learn}=0.4$, Approval Top-2 is significantly better than STAR, and the gap continues to grow as `p_learn` increases.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-learn-sweep" mode="images" %}<br>

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="p-learn-ci-table" %}

As we sweep the runoff noise $t$, and keep the awareness fixed between the primary and runoff, the performance does not change much for the values of $t$ used for the scenarios, and the dropoff in quality seems to be primarily for $t < 0.4$. Further investigation on scenarios where the $t$ values are lower would be required to say more. So this analysis indicates that what we are measuring across the scenarios used in this post is a case where voters are unaware and fatigued, but are generally good at having the correct direction between the two finalists.

This could be more realistic than lowering the $t$ values further, but I won't make conclusions on that without running the data. Under the values tested, it seems that the main driver for the runoff dominance is the elimination of fatigue and reduction in the unawareness of the two finalists.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-t-sweep" mode="images" %}

### STAR Runoff Betrayal

We measure the difference between the actual automatic runoff and a hypothetical "perfect" clear-eyed runoff (i.e. 0-5 SCORE voting with a delayed runoff compared to STAR's automatic runoff), where voters are perfectly informed and vote for the candidate they truly prefer. This is a measure of how much the automatic runoff hurts voters who are misinformed in the primary step compared to a perfect clear-eyed runoff. We find that even under mild friction, STAR's automatic runoff is significantly worse than a perfect clear-eyed runoff, and this gap grows as friction worsens.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="star-betrayal-tables" mode="tables" %}

This is perhaps not too surprising given that we are modeling voters as not necessarily filling out the entire ballot. Of course a delayed runoff would improve the outcomes! But it's by *how much* that makes me really concerned about the automatic runoff in STAR. Rather than a "cost-saving" mechanism, it could instead "cost" outcomes, and give voters who have limited time to research candidates less of a voice in the outcomes.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="scoret2-vs-at2" %}

The evidence for my hypothesis that a more coarse ballot is more robust to friction seems to be mixed. There appears to be no (robust and persistent) significant gap, when comparing clear-eyed Approval Top-2 to a theoretical clear-eyed SCORE Top-2 delayed runoff: under ideal conditions SCORE appears significantly better, and under friction Approval is basically the same. Some runs show a significant difference where Approval is better in the 95% confidence interval, but it's so borderline that I'm not willing to make a strong claim about it.

At the very least, for this comparison of a theoretical SCORE Top-2 (that nobody is actually advocating for) with the St. Louis model, I would say that the SCORE ballot appears completely unjustified. That granularity does not seem to help outcomes under friction. The real difference, if not outcomes, is then how much more intimidating and easy to spoil the ballot is, and how politically viable proposing that change becomes. Approval is essentially the hardest ballot type to spoil, so I would conclude a SCORE ballot is strictly worse in this context.

The gulf between the *automatic* runoff of STAR and a delayed Approval runoff, however, is very, very large. There is no ambiguity there.

## Conclusion

It is absolutely undeniable that, with perfectly informed voters who fill out their ballots completely and accurately, STAR is an objectively more accurate mechanism than Approval. That granularity is a genuine strength when the data is high quality. However, that granularity becomes a liability when the data you collect is noisy or incomplete. Low quality data acts like sand in the gears, making the system no better than a simpler system like single-round Approval.

And based on my findings, I would say that for something like a City Council trying to decide between a few different options for the placement of a new library (where the voter assumptions for the original VSE model are very likely accurate), STAR would be an excellent choice. Highly informed voters, who will give full and thoughtful scores to all available options, match better with the assumptions that underlie the ideal VSE numbers commonly reported. It could be easily expected that there will be cases where STAR would produce higher quality outcomes than the council members simply approving of which options they like. This is the use case where STAR can really *shine*.

*Publicly electing that city council*, however, is a different story. I do not find it plausible that voters are going to be able to give thoughtful and accurate scores to all candidates for a local election. A simpler system like Approval, with a delayed runoff, seems more likely to produce better outcomes if the data collected from voters is likely low quality. Under such conditions, the gain from even just single-round Approval to STAR appears to be negligible.

Specifically, the proposal to eliminate the primary process in favor of a single-round STAR vote instead seems like the worst of both worlds for public political elections. If there is anything I have taken away from this project, it's that a delayed runoff is of **enormous benefit**. And given that the standard is already to have two elections, a winnowing primary process that feeds into a general election, the evidence that what we gain from eliminating the primary election would outweigh what we lose does not appear strong to me. I would, for example, vehemently oppose any proposition to replace the current California Plurality Top-2 system with any single-round method. [As bad as the current system is](../ca-top-2/), the narrowing process is a necessary evil, and the evidence that a single-round system would be better is not compelling to me.

A narrowing process seems absolutely necessary, and using the simple Approval system for that winnowing seems to be the most robust and politically viable option. It scales exceptionally well to crowded fields, compared to a ranking or scoring system, and eliminates the vote splitting we see in the Plurality Top-2 systems used in Washington and California. If 61 candidates on the ballot is a possibility, then Approval is the only system that can handle that without completely overbloating the ballot and overwhelming voters.

### The Broader Context

Independent of the results of these simulations is the fact that STAR is an objectively more complex system than Approval. And that seems exceptionally important for evaluation of political viability.

In a time when it's not even clear that the simplest voting system, Approval, is a slam dunk reform of our choose-one system, I see little evidence to assume that a more "expressive" (i.e. complicated and more difficult to explain) system like STAR would be *more* palatable to voters. Optimal accuracy or not, [trust in our elections is low](https://maristpoll.marist.edu/polls/election-security-march-2026/) and [often tied to partisan dynamics](https://statesunited.org/resources/confidence-poll/). I worry about how much trust voters would have for a pitch that involves an "accurate automatic runoff algorithm" more complex than "most votes wins".

Though the sample size for how Approval and STAR fare at the ballot box is small, the results are concerning:

STAR has been rejected three times by voters in Oregon. There is the Eugene situation that has framed this discussion, of course. But it was also rejected in [Lane County in 2018](https://ballotpedia.org/Lane_County,_Oregon,_Measure_20-290,_Score_Then_Automatic_Runoff_Voting_Method_(November_2018)) (52.4% opposed, also would have eliminated primaries) and [Oakridge in 2024](https://ballotpedia.org/Oakridge,_Oregon,_Measure_20-364,_STAR_Voting_for_Three_Election_Cycles_Amendment_(November_2024)) (53.56% opposed, and this was a reversible low-stakes three election pilot test).

Fundamentally, I have to ask: is scoring the options for Commissioner of the Eugene Water and Electric Board the way you rate a restaurant on Yelp actually something the average voter is clamoring to do? Perhaps this prospect is appealing to political junkies<d-footnote>No offense to you, dear reader, but if you are reading <em>this blog post</em> you may not be representative of the average voter. Thank you for reading this far, by the way!</d-footnote>, but I am skeptical that the number of voters who find this more expressive ballot enticing is particularly large, or outweighs the numbers who would vote "no" to it at the ballot box simply due to its complex nature.

This remains to be seen, and luck could simply have been against STAR in the three Oregon elections<d-footnote>Particularly the close ones. Though I have no earthly idea if Eugene would have accepted STAR if it had been integrated into the existing primary process somehow.</d-footnote>, but I am not optimistic. It seems concerning to me that the thing that gets supporters so excited and passionate about STAR *might be the very thing that hurts it at the ballot box*.

When a more granular ballot and system fails to justify itself in producing significantly better outcomes, you essentially just create more ways to disenfranchise people who don't have the time to treat politics like a hobby<d-footnote>Unlike the question of equity in primary election turnout, for which there is a strong case to be made on both sides, research on ballot-marking errors<d-cite key="neelyMcDaniel2015overvoting"></d-cite> is a more directly measurable effect that generally supports this when looking at RCV in San Francisco: Spoiled ballot rates were disproportionately higher for Black, Latino, elderly, and foreign born residents. "[The] evidence suggests it is not IRV per se but rather ballot complexity more generally that leads to such discrepancies in whose votes get counted." STAR is a significant improvement in how difficult it is to spoil a ballot over RCV, but when you suggest anything more complex than choose-one or Approval, I think we have to be incredibly mindful of what the cost of complexity could be, and if the theoretical benefits of granularity and complexity justify them. I think it is safe to say, however, that Approval is easily the hardest ballot type to spoil, which is a benefit to consider.</d-footnote>.

Eugene is a liberal city in a fairly progressive blue state. If STAR is 0-3 in *Oregon*, then I am really wondering about STAR's long-term potential to be the future of voting reform in the United States. When every *good* reform, like Approval and STAR, has the common enemy of [Ranked-Choice Voting](../ditch-rcv/), I worry about the potential waste of resources and energy that could be spent on a more politically viable reform like the St. Louis model of Approval Top-2.

I have said before that as RCV is dying a slow and agonizing death, we likely have one chance to pivot before we burn through all the good will and openness to try something new. I like our chances better if we all rally behind the system that has shown itself to be politically viable, and has a proven track record of success in St. Louis. I worry about flying too close to the sun trying to skip over Approval in favor of STAR. And I am deeply concerned with the potential effect of exhausting Oregonians with repeated STAR proposals to the point where they are unwilling to consider any other reform proposals in the future.

The evidence in favor of STAR thus far is primarily in simulations done *by STAR proponents themselves*. And though I find their methodology excellent and without obvious flaws or a hint of bias<d-footnote>In the paper by Wolk, Quinn, and Ogren, they mention that Quinn originally expected the model to find support for systems like Majority Judgment, but instead found that STAR had superior performance. They are also very up-front about their potential conflicts of interest regarding the fact that Wolk is the executive director for an organization advocating for the methods discussed in the paper. It is entirely above board, rigorous work by experts I have great respect for.</d-footnote>, the numbers so far have not swung me to becoming a STAR supporter. I do not find sufficient evidence that it is better suited for public elections than the St. Louis model of Approval Top-2. I do not approve of STAR.

If we suppose that expressiveness begets complexity which makes the system *less* politically viable, and *also* makes it less robust to real-world conditions, then Approval Top-2 seems to dominate STAR in every way that matters. However, that is just my opinion.

In a 1998 paper by Regenwetter and Grofman, they analyzed the outcomes of real Approval elections to see if they might match the theoretical outcomes under methods like Borda or Condorcet from reconstructed preferences. They reach the same conclusion I do, by a very different route:

> "We find no evidence here that approval voting should be replaced by a more elaborate voting scheme." (p. 532<d-cite key="regenwetterGrofman1998approvalBordaCondorcet"></d-cite>)

Perhaps we've been attempting to overcomplicate our elections chasing perfection. When we step beyond the idealized assumptions of perfect voters, we find that the "top of the line" systems like STAR and Condorcet perform far worse than the simpler system being used *right now* in St. Louis. Approval Top-2 may not be a compromise at all, but actually superior and more accurate than the more complex STAR that it has been overlooked in favor of. And when voters have actually been asked to choose STAR for themselves, they've said no every time. We need not fly high and melt our wings like Icarus, when the most robust solution might just be quietly working in Missouri as we speak.

## Appendix

### The Plurality Bump

Earlier, I mentioned the surprising robustness of Plurality Top-2 under friction. Related to this was a general trend where mild friction seemed to make plurality methods *better*. Upon reflection on the model, I believe I know why: the fact that a plurality vote is just choosing a single candidate.

Unlike every other voting system, choose-one voting is the only one where fatigue has a minimal effect on outcomes. In every other voting system, there's an attempt to extract *more* data from voters by allowing some sort of expression for other candidates. This makes plurality voting robust to fatigue and unawareness, which seems to *tighten* outcomes because voters are less likely to vote for a candidate who has no chance. The prominence model focuses votes on a smaller number of candidates, which appears to sort of accidentally simulate the strategic voting which makes plurality more effective. The VSE of single-round plurality is never *good*, but mild friction improves the outcomes. Plurality Top-2 under mild friction is actually on par with some of the *good* systems under ideal conditions.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="plurality-bump" %}<br>

This leads me to an uncomfortable conclusion that choose-one voting, for as flawed as its outcomes are, might actually be in some ways well-suited to our tired human brains. The mental shortcuts that we take might actually hone the outcomes of our terrible voting system to some extent. If nothing else, choose-one voting is simple to use and simple to count. Approval maintains that same simplicity, while improving a number of other aspects like candidate incentives.

### Approval vs Plurality

Despite the plurality bump, Approval still outperforms plurality voting at mild and moderate friction. The heavy friction gap is insignificant.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="plurality-vs-approval" %}<br>

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="plurality-approval-ci" %}

The Top-2 variants were less clear-cut. Approval Top-2 outperforms Plurality Top-2 under mild friction, but they are not significantly different under moderate or heavy friction.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="at2-pt2-ci" %}

I also did an analysis of the difference between Approval Top-2 and Plurality Top-2 when we vary the number of candidates. The idea is that for 6 candidates, the two may have similar performance, but vote splitting would become more of a problem for choose-one as the number of candidates increases. Under ideal conditions, AT2 stays fairly consistent, while PT2 declines rather quickly. This maintains in mild friction, but the gap is not as large.

Under moderate and heavy friction, however, the difference is less clear-cut. There does not seem to be a persistent difference between the two systems.


{% proof Expand to see the candidate sweep analysis %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="at2-pt2-candidate-sweep" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="at2-pt2-candidate-ci" %}
{% endproof %}

### The Ranked Methods Implosion

Perhaps the most shocking thing to me was the complete and utter collapse of the VSE of ranked methods like Schulze under friction. Going from the absolute best method to basically the worst method was not in any of my hypotheses; however, it's not exceptionally surprising in retrospect.

Schulze already has a massive drop-off in VSE under strategic voting. When you design a system to calculate the Condorcet winner explicitly, then you do indeed get the highest possible VSE under completely ideal honest voting (because the Condorcet winner is almost always that best candidate). But dishonest data just ends up electing someone else (who is almost surely *worse* than the Condorcet winner).

I expected friction to cause STAR to break, but I should have realized that Condorcet was the far more intricate machine that would truly seize up when sand got in its gears. It gets far worse for Schulze when voters are not even ranking candidates. It relies on all that nuanced preference data to do its thing, and otherwise it's just a mess. This is the Formula 1 race car spinning out when the track gets wet. You use a race car on a pristine track, but you don't drive it to Wendy's in the rain.

Ranked-Choice Voting (RCV) does not fare much better, and their gap is not significant at any friction level, which might be the most embarrassing thing to come out of this post. As someone relatively sympathetic to Condorcet methods, it does not fill me with relish to say that Schulze's massive outcome advantage over RCV basically completely vanishes. RCV is already very bad across the board, in essentially every respect (like practicality and logistical complexity), but even this is appalling.

I would not consider myself a cardinalist, but this has given me new appreciation for how sensitive ranked data can be to noise (the "garbage in, garbage out" problem seems to be far worse for ranked methods than STAR voting). The fact that cardinal voting deals with candidates *independently* (with the exception of STAR's automatic runoff) seems to cushion the blow of widespread noise and truncation. I may investigate the [Better Choices](../better-choices/) model of a delayed top-3 Condorcet runoff in a follow-up, to see if reducing Condorcet to three candidates, following a choose-one or Approval all-candidate primary, would be more robust than just doing Schulze on all 6 candidates in a single round.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="ranked-implosion" %}<br>

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="rcv-schulze-ci" %}

### Condorcet Efficiency

This is a little funnier. Under ideal conditions, Schulze has perfect 100% Condorcet efficiency, as expected. It's far beyond all other systems in doing this exact job:

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="ideal-honest-ce-table" %}

Surprisingly, Approval Top-2 is the best non-Condorcet method at electing the Condorcet winner, ahead of even STAR under ideal conditions.

However, under friction, the system designed specifically to elect the Condorcet winner becomes worse at electing the true Condorcet winner than basically every other method. It seems that cardinal and runoff systems, at least in this model, are actually better at electing the Condorcet winner than a system designed specifically to do that exact task.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="condorcet-joint" %}<br>

With only a few exceptions under mild friction, there is sufficient evidence to conclude that Schulze is worse at electing the Condorcet winner than basically all other methods (except RCV) under all levels of friction.

{% proof Expand to see the Condorcet efficiency significance tables %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="ce-ci-table" %}
{% endproof %}

It appears that if your desire is truly to elect the Condorcet winner no matter the cost, then a runoff method is the way to go if voters are not ideal.

### SCORE vs STAR

I also measured the difference between STAR voting and just plain 5-point scoring (SCORE, i.e. STAR's own ballots with the runoff step switched off) to isolate the runoff's own net effect from everything else STAR does. Overall, STAR seems to be better under these friction scenarios.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="score-vs-star" mode="images" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="score-vs-star-scenarios" %}

### The Jupyter Notebook

I am sure this post is going to be particularly controversial, so the full simulation is embedded below rather than just summarized. You can also [download it here](https://github.com/eigentaylor/eigentaylor.github.io/blob/main/assets/jupyter/vse_simulation.ipynb).

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
