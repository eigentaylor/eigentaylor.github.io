---
layout: distill
title: 'Coarse Correction: Is STAR Actually More Accurate than Approval?'
date: 2026-07-25
description: Why Approval with a delayed runoff might be far more robust than a more granular and expressive voting system like STAR when voters are misinformed and fatigued.
importance: 2
tags: voting
category: polisci
featured: false
theorems: true
bibliography: voting.bib
chart:
  plotly: true
images:
  photoswipe: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: Equal Vote Coalition (Volunteer)
toc:
  - name: Introduction
  - name: The Friction Parameters
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

Voter Satisfaction Efficiency (VSE) <d-cite key="quinn2017vseSummary"></d-cite> is an incredible metric used for evaluating the performance of voting systems. It gives a numeric percentage to the "accuracy" of a voting system, with 0% being just a system that randomly chooses a winner, and 100% being a system that always elects the "best" (highest utility) candidate.

These are, of course, just simulations, however. VSE does not say anything about candidate entry, voter turnout, or other real-world factors that can shape the dynamics of the government that uses a given voting system to elect their leaders.

I interpret VSE as just a simple measure of "aggregation competence": how well a voting system can aggregate the preferences that are fed into it. If a system is *good*, then it almost surely has solid VSE. Choose-one voting, for example, has awful VSE (about 60%) when voters are simulated to just vote honestly. This is because the system is so blind that it cannot look beyond the top choice of each voter, and thus consensus candidates are often buried by vote-splitting. With strategic voting, it can rise to about 80%.

However, VSE on its own does not say anything about whether or not a system is "good" in the real world. If a voting method is so difficult to explain or fill out, then high VSE might not matter if it's so intimidating to voters that it reduces turnout or otherwise discourages participation. Practical considerations are exceptionally more important than "in simulations this voting system does great!". But VSE is still a useful metric for comparing the performance of different voting systems.

I should make it clear that RCV has very poor VSE, which is consistent with its poor design and mechanism (which, funny enough, ends up achieving worse outcomes from its greater complexity compared to Condorcet<d-footnote>I find it especially humorous that RCV tends to consistently underperform Approval voting, which is exceptionally simpler.</d-footnote>). Although RCV is technically a serious contender in the reform space, it is not a serious consideration by organizations like the Equal Vote Coalition, Center for Election Science, and Better Choices for Democracy. [People who do the math don't support RCV](../ditch-rcv/), so this post is focused entirely on the STAR, Condorcet, and Approval systems. It is included in the early cells of the notebook to show consistency with the original VSE code, but not focused on here.

The Equal Vote Coalition pushes three systems, which all have high VSE<d-footnote>My status as a volunteer for the Equal Vote Coalition does not mean I speak for them. My views are often at odds with the official stances of EVC, particularly with respect to STAR voting. My words are my own.</d-footnote>: STAR, Condorcet<d-footnote>Technically, they champion their particular flavor of Condorcet, "Ranked Robin", but the differences are minor and not relevant to this discussion. In what follows, we will focus on the Schulze method, which is particularly robust and used in a number of organizations for their internal elections.</d-footnote>, and Approval. My numbers are slightly lower than those reported by Jamison Quinn<d-cite key="quinn2017vseSummary"></d-cite>, but his report was nearly 10 years ago, so I will report the approximate numbers I got by copying the code as it is in the electionscience Github repository:

- STAR voting (Score Then Automatic Runoff): Voters score candidates on a scale (usually 0-5), and the two highest-scoring candidates go to an automatic runoff where a candidate gets one point for every voter who scored them higher than the other candidate. This system has arguably best VSE range of the three (reported to be about 87%-97%).
- Condorcet methods: Voters rank candidates and the candidate who defeats all others is the winner (with some tiebreaker if no candidate is a Condorcet winner). This system is right alongside STAR in the maximum 98% VSE, though its lower bound is fairly low under strategic voting (84%), despite the fact that strategic voting is just [not very effective in Condorcet methods](../better-choices-strategy/). The fact is, pairwise dominance ([while not a prerequisite for being the utility maximizer](../why-condorcet/)) is objectively a strong predictor of high utility.
- Approval voting: Voters can approve of as many candidates as they like, and the candidate with the most approvals wins. This is a system with surprisingly high VSE (84-95%, strengthened by strategic voting) for its simplicity.

I will not pretend that I am not [partial to Approval voting over STAR voting](../approval-only/). In fact, one of the reasons is just how close the VSE of the simpler Approval, and especially its Top-2 variant, is nearly competitive with the far more complex and expressive STAR.

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

But, alas, I cannot ignore the fact that STAR simply has better VSE than Approval. And STAR proponents are not shy about pointing this out. On the [Better Voting website](https://bettervoting.com/), they list Approval as being "recommended for simplicity", and STAR as being "recommended for accuracy". There's a subtle implication that choosing Approval is simplicity *at the cost of accuracy*. As if my theoretical Approval poll on which Salsa flavor is best will be wrong, and *if only* I had selected the STAR option<d-footnote>I will also object to Condorcet being just "recommended for ranking" when it's basically as accurate as STAR, particularly for honest voters. Sure, it doesn't scale up well with many options, but I digress.</d-footnote>...

<div class="pswp-gallery mt-3" id="bettervoting-approval-vs-star">
  <a href="/assets/img/bettervoting-approval-vs-star.png"
     data-pswp-width="1163"
     data-pswp-height="675"
     target="_blank">
    <img src="/assets/img/bettervoting-approval-vs-star.png" class="img-fluid rounded z-depth-1" alt="Better Voting website comparison listing Approval as recommended for simplicity and STAR as recommended for accuracy" />
  </a>
</div>
<div class="caption mt-2">
  Source: <a href="https://bettervoting.com/">Better Voting</a>.
</div>

But what if that's not actually true? I have been somewhat skeptical about some of the assumptions that go into VSE simulations, that I don't believe are particularly realistic. Perhaps we need to put an *asterisk* on STAR's high VSE<d-footnote>This is actually an epic pun because asterisk derives from the Greek word "asteriskos," meaning "little star." I'll be here all week.</d-footnote>. Some questions that I would like to raise are:

1. Do voters *actually* know their true utilities for all the candidates on the ballot? Might some voters *think* they prefer $B$ over $A$, but would actually be happier if $A$ won than $B$? If they score $B$ higher than $A$, perhaps because they've never *heard* of $A$, and the runoff is between $A$ and $B$, then this voter will accidentally vote *against* their interests in the runoff step.
2. What if voters have never heard of some of the candidates? If the utility maximizer is someone most voters are not aware of, then they are not likely to score them highly, hurting that candidate's chance of winning. Compared to Approval, where a single ignorant voter only contributes one approval to all known approved candidates versus all unknown candidates they *would* approve, ignorant STAR voters can increase the margin of a poor known candidate over a better unknown candidate by up to 5 points. This can similarly happen if a voter gets fatigued by the ballot and simply gives up before even seeing that "best" candidate (even if they have vaguely heard of them).

The common thread here is that a complex and expressive system like STAR is designed to take in more information from voters to deliver better outcomes than a more coarse system like Approval. But what if the data it collects is truncated noise rather than signal?

One particular concern I have with this is that the runoff is *automatic*. A voter who is misinformed when they cast their initial score ballot cannot change their mind later if they realize that they were wrong. You don't know what you don't know. And many voters *are* tired and busy, and don't have time to read the campaign websites of all [61 candidates on the ballot, as we saw in the 2026 California Gubernatorial primary](./ca-top-2/). Even with 6 candidates, the default in the VSE simulations, I worry about the ability of voters to accurately evaluate all candidates.

In 2024, a proposal in [Eugene, Oregon to eliminate primary elections for mayor, city council, and EWEB seats and replace them with STAR voting](https://ballotpedia.org/Eugene,_Oregon,_Measure_20-349,_STAR_Voting_for_Mayor_and_City_Council_Elections_Initiative_(May_2024)) was voted down by 64.49%. In 2020, [St. Louis, MO voters voted to adopt an all-candidate Approval voting primary election with a delayed top-2 runoff](https://ballotpedia.org/St._Louis,_Missouri,_Proposition_D,_Approval_Voting_Initiative_(November_2020)) by 68.15%. This system is still in place, and working excellently<d-cite key="sargent2025stlouis"></d-cite>.

I assume that the pitch for a single-round STAR election over the proven Approval Top-2 system used in St. Louis was that STAR is more accurate than Approval. Surely, a system with better VSE is better than one with worse VSE, right? And if we can save money by eliminating primary elections, and just quickly elect the best candidate through an *automatic* runoff performed on expressive and rich data, why not do that?

My concern is that an automatic runoff has a "garbage in, garbage out" problem: if the data collected from voters is poor, then the runoff will be poor as well. In a delayed runoff, voters have a chance to familiarize themselves with the candidates in the narrowed field, and can make a more informed choice.

This led me to the following hypotheses:

1. If the preferences and data that voters provide are noisy or incomplete, a more coarse system like Approval will actually be more robust than a more expressive system like STAR to that degradation in voter information. In other words, STAR's advantage over Approval is not robust to friction.
2. A delayed runoff is more robust than an automatic runoff if the voters in the primary step are misinformed, unaware, or fatigued, and that ignorance is reduced in the runoff step.

In this post, we evaluate the rejected single-round STAR system proposed in Eugene, Oregon to the currently in-place Approval Top-2 system in St. Louis, Missouri. My primary evidence is a Jupyter notebook that uses the original VSE simulation code with significant modifications to test these hypotheses. It was written with AI-assisted with Claude Code, but the code is included for full transparency and reproducibility. I look forward to someone who is a more skilled coder than I am to improve upon it, and perhaps extend the model<d-footnote>I have no doubt someone is going to find a bug in my code, or an assumption that is not particularly realistic. I welcome that, and hope that this post can be a jumping-off point for further research into the robustness of voting systems to realistic conditions.</d-footnote>.

Spoiler alert: STAR's advantage over Approval narrows or even reverses under even mild friction, and Approval Top-2 is significantly more robust than STAR even when the runoff conditions are only mildly improved.

## The Friction Parameters

We define three parameters that we can adjust to simulate friction for voters:

### Epistemic Noise

We add noise to the voter's perceived utility of each candidate, simulating the fact that voters are often misinformed or otherwise unable to accurately evaluate the candidates. We adjust this with the $t$ parameter, which is the correlation between the voter's true utility and their perceived utility.

If $u_i(c)$ is the true utility of candidate $c$ for voter $i$, then we can define a voter's perceived utility as:

$$u'_i(c) = t\cdot u_i(c) + \sqrt{1-t^2}\cdot \sigma_i \cdot \epsilon_{ic}$$

Where $\epsilon_{ic} \sim N(0,1)$. Then $t$ is exactly the Pearson correlation coefficient between the true and perceived utilities, scaled by the voter's utility variance $\sigma_i$. If $t=1$, then the voter is perfectly informed, and if $t=0$, then the voter's perceived utilities are pure noise. We use one global $t$ for all voters.

### Unfamiliarity

We draw an awareness/prominence ranking for each election, simulating that everyone knows the frontrunner, but as you go down the number of voters who are aware of each candidate decreases. For the selected $\alpha$ "awareness" parameter, the probability that a voter is aware of candidate $c$ is given by:

$$P_{\text{aware}}(c) = \alpha^{\text{prominence_rank}(c)}$$

This ranking is independent of candidate quality, representing how a terrible candidate can have excellent name recognition, and a great candidate can be a complete unknown. At $\alpha=1$, all voters are aware of all candidates, while at lower values, fewer voters are aware of the candidates lower in the awareness ranking.

### Fatigue

While prominence is global to the election, fatigue is local to the voter. We draw a random fatigue ranking for each voter, as a stand-in for ballot-order rotation. As voters go down the ballot, they are more likely to be fatigued and simply stop looking at names. Maybe they need to pick up their kids from soccer practice, or they came from a long day at work, or they just don't care who their water commissioner is. For the "fatigue" parameter $\ell$, the probability that a voter is not fatigued enough to vote for candidate $c$ is given by:

$$P_{\text{not fatigued}}(voter, c) = \ell^{\text{fatigue_position}(voter, c)}$$

### How These Combine

Unfamiliarity and fatigue interact in an interesting way. To be able to vote for a candidate, a voter must be both aware of them and not fatigued. So the probability that a voter votes for candidate $c$ is given by:

$$P_{\text{genuine}} = P_{\text{aware}} \times P_{\text{not fatigued}}$$

If the check fails, then the utility for that candidate on the input ballot is set to be just below that of their least liked known candidate. This simulates the voters to basically say "I don't know them, so I'll leave them off my ballot". This simulates how Schulze (Condorcet) would interpret a truncated ballot: all unranked candidates are below all ranked ones, and treated as the voter being indifferent between them. For cardinal systems, this functionally gives unknown candidates a 0 score (unapproved for Approval).

## The Runoff Assumptions

This model essentially turns voters from robots, patient enough to thoughtfully evaluate and vote for all candidates, into messy humans who are often misinformed, fatigued, or otherwise unable to know which candidates would actually make them happiest. We would like to know how much of a difference a lower noise delayed runoff, with finalists selected with a more coarse system like Approval, can make in the overall accuracy of the election compared to a more granular system like STAR, taking in poor data.

My hypothesis was that the runoff step can act as a corrective mechanism for misinformed voters in the primary step, whereas the more complex single-round mechanism suffers from the previously mentioned "garbage in, garbage out" issues.

However, there are a few ways that we could model improved voter information in the runoff step. We assume that in the primary election (say, in June) voters are tired and didn't have time to research all candidates in the crowded field. They vote imperfectly based on their limited knowledge (ex. vibes, not reading the candidate's website). But just how much more informed are voters in the runoff (say, in November<d-footnote>In California, the primary is in June with the general election top-2 runoff about five months later in November. In St. Louis, the general is only one month after the Approval primary. Either way, that is a fair amount of time to find out who the general election candidates are.</d-footnote>)?

Under the most pessimistic conditions, we could imagine that the voter has absolutely no time to update their beliefs. The voter essentially falls into a coma as soon as they submit their ballot, wakes up in November, and then casts a vote. We call this the "frozen" runoff assumption in the code, but we'll call it the "coma" assumption here, because I think that's kind of funny.

The coma model is how STAR functions *almost exactly* (but slightly worse). The flawed understanding carries over to the runoff step, without a chance to be corrected. However, STAR is slightly worse here because if you gave both finalists an equal score, you have no chance to influence the outcome. For example, if you gave finalist $A$ two stars, but were too tired to give the other finalist $B$ their rightful four stars, then you have no opportunity to correct that mistake, and your ballot will be interpreted as being for $A$ over $B$. Similarly, if you were too tired to give $A$ or $B$ any stars at all, your ballot would effectively be ignored in the runoff, even if you *did* know who they were and had a preference. In Approval Top-2's coma variant, voters still have the opportunity to vote for their preferred finalist (according to their misinformed preferences) *unless they were unaware of both candidates*.

Under slightly more optimistic conditions, we can suppose that in the time between the primary and runoff, voters at least know who everyone in the runoff step actually are, though their preferences could still be noisy and in the wrong direction. We'll call this the "groggy" runoff assumption, and it's how we define the baseline delayed runoff systems to work (Approval Top-2 and Plurality Top-2).

The most optimistic assumption is that voters have had time to research the candidates in the runoff step, watching the debates, reading the websites, and generally becoming more informed about the candidates. In this ideal case, we assume that the noise has entirely evaporated, leaving the voters with their true utilities. However, since it the runoff is entirely just a pairwise check, this ideal case *only* assumes that voters know the correct *direction* (the fact that the utilities are perfectly accurate is inconsequential, since only the direction matters). We include "clear-eyed" alternates of each delayed runoff system which uses this assumption. It's likely that the reality of the situation is somewhere between the groggy and clear-eyed assumptions.

### Justification

I will not pretend that these assumptions are not particularly optimistic for a delayed runoff. Indeed, I might even call it "cheating"! However, the proposal in Eugene *was* to eliminate the primary entirely, and have a one-shot expressive five-star score based election for seats as prestigious and of consequence as "Commissioner for Eugene Water and Electric Board, Wards 6 and 7".

Any voter who fails to distinguish between the finalists due to fatigue or lack of information would have absolutely no recourse to influence the outcome. In *any* top-2 system, all voters are guaranteed an opportunity to have final say in who is elected in the runoff step.

## Other Relevant Methodology

I tried to keep the default settings of the original vse-sim as much as possible. I made an effort to change the code as little as possible, and included various sanity checks to see that the output was reasonable and matched with expectation (before adding my friction parameters).

(TODO: Insert the strategy sweep plot in the santity check section)

I also defined "joint scenarios" of various friction levels where I set the $t=\alpha=\ell$ parameters to the same values:

- 1.0: Ideal
- 0.85: Mild
- 0.7: Moderate
- 0.5: Heavy

The way some parameters compound is multiplicative, so while 0.5 may not seem as heavy as, say, 0.3 or 0, it is actually *quite* substantial (especially with only 6 candidates).

## Findings

Before we get into the code, I'd like to summarize some of the things I found.

### The Approval-STAR Gap

Under perfect conditions, STAR is objectively more accurate than Approval. However, the VSE gaps narrows under all friction scenarios. The systems calculate very close VSE. The gap is too small to strongly conclude that one system is actually stronger than the other (which I interpret as that greater complexity being entirely unjustified), but it appears certainly suggestive that STAR's advantage over Approval is not robust to friction.

Approval Top-2, on the other hand, clearly wins out in simulations over STAR and Schulze except for the "coma model" (which is competitive with STAR). It's not even close. Even under mild friction, Approval Top-2 is significantly more accurate than STAR so long as awareness is granted to the runoff, and this grows as friction worsens. This is with and without removed noise in the runoff step.

As long as voters at the very least *are* or *become aware* of both candidates in the runoff step, even if they are misinformed about their true utilities, Approval Top-2 still manages to outperform STAR by a mile. This gap widens further if voters are assumed to be perfectly informed in the runoff step.

Perhaps the most sobering statistic is how solid Plurality Top-2 was in VSE compared to STAR under the sweeps and scenarios. Despite Plurality Top-2 having completely mediocre VSE in the ideal case, it stays robust compared to all other single-round systems. I would never advocate for Plurality Top-2, but this model seems to highlight that the potential corrective mechanism of a delayed runoff can salvage even the worst of the single-round systems, when ignorance decimates the accuracy of the primary election<d-footnote>As the friction increases, the more common bullet voting becomes. This leads to both Approval Top-2 and Plurality Top-2 functioning more and more similarly as friction increases. One further reason that VSE alone is insufficient to declare a system dominant. Approval Top-2 does indeed dominate the plurality variant. But the fact that the worst top-2 system does so much better than any single round system under friction has given me exceptional appreciation for the value of a winnowing primary process.</d-footnote>.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="vse-joint" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-help-sweep" mode="images" %}

### How much does a delayed runoff actually help?

I also looked at what happens to Approval Top-2 when we vary the parameter improvements of the runoff step. That is, looking at how the VSE as a function of how much we improve the reduced noise and awareness in the runoff step.

What we find is that when we fix awareness (either eliminate it entirely or make it exactly equal to that of the primary, as per the coma model) and vary how much we reduce the noise itself, the outcomes improve only slightly. This is consistent with the relatively small difference in our Approval Top-2 groggy variant vs the clear-eyed variant.

The real driver in what makes a delayed runoff so dominant is when we improve the awareness of the candidates in the runoff step. Even if voters are still highly misinformed about the direction between the two candidates, the improvement alone of making sure the voters who were not aware of one or both of the finalists in the primary actually have some idea of who they are is sufficient to give Approval Top-2 a significant advantage over STAR. This is the "you don't know what you don't know" problem. This might have been a serious issue for Eugene, had the primary been eliminated.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-alpha-sweep" mode="images" %}

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="runoff-t-sweep" mode="images" %}

### STAR Runoff Betrayal

We measure the difference between the actual automatic runoff versus a hypothetical "perfect" runoff (i.e. 0-5 SCORE voting with a delayed runoff compared to STAR's automatic runoff), where voters are perfectly informed and vote for the candidate they truly prefer. This is a measure of how much the automatic runoff hurts voters who are misinformed in the primary step. We find that even under mild friction, STAR's automatic runoff is significantly worse than a perfect runoff, and this gap grows as friction worsens.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="star-betrayal-tables" mode="tables" %}

This is perhaps not too surprising given that we are modeling voters as not necessarily filling out the entire ballot. Of course a delayed runoff would improve the outcomes! But it's by *how much* that makes me really concerned about the automatic runoff in STAR. Rather than a "cost-saving" mechanism, it could instead "cost" outcomes, and give voters who have less time to research candidates less of a voice in the outcomes.

The evidence for my hypothesis that a more coarse ballot is more robust to friction is mixed. Under high friction scenarios with an assumed perfectly informed corrective primary, Approval Top-2 has a slight edge over a theoretical SCORE primary followed by voters getting to vote for their true preference in a delayed runoff. But under mild friction, STAR has a slight edge over Approval. When we sweep epistemic noise exclusively, the performance is for all intents and purposes identical. I find insufficient evidence to conclude that there's a difference between the two systems under these conditions.

At the very least, for this comparison between a theoretical SCORE Top-2 (that nobody is actually advocating for) with the St. Louis model, I would say that the SCORE ballot appears unjustified. The gulf between the *automatic* runoff of STAR and a delayed Approval runoff, however, is very, very large.

## Conclusion

It is absolutely undeniable that, with perfectly informed voters who fill out their ballots completely and accurately, STAR is an objectively more accurate mechanism than Approval. That granularity is a genuine strength when the data is high quality. However, that granularity becomes a liability when the data you collect is noisy or incomplete.

Based on this, I would say that for something like a City Council trying to decide between a few different options for a new park, STAR would be an excellent choice. Highly informed voters who will give full and thoughtful scores to all available options could be easily expected to produce higher quality outcomes than the council members simply approving of which options they like.

*Electing that city council*, however, is a different story. I do not find it plausible that voters are going to be able to give thoughtful and accurate scores to all candidates for a local election. A simpler system like Approval, with a delayed runoff, seems more likely to produce better outcomes if the data collected from voters is likely low quality. Under such conditions, the gain from even just single-round Approval to STAR appears to be negligible.

Specifically, the proposal to eliminate primary elections and have a single round STAR election instead seems like the worst of both worlds. Instead, an all-candidate primary under Approval with a delayed runoff, as we see in St. Louis, seems to be the most robust system for electing candidates. Given that the standard is already to have two elections, a winnowing primary process and a general election, I see no *serious* downside to a second election (ex. cost, turnout, etc.).

[A narrowing process seems absolutely necessary](https://robla.blog/2026/01/17/should-approval-voting-have-a-primary/), and using the simple Approval system for that winnowing seems to be the most robust and politically viable option. It scales exceptionally well to crowded fields, compared to a ranking or scoring system, and eliminates the vote splitting we see in the Plurality Top-2 systems used in Washington and California.

Independent of the results of these simulations is the fact that STAR is an objectively more complex system than Approval. And that seems exceptionally important for evaluation of political viability.

In a time when it's not even clear that the simplest voting system, Approval, is a slam dunk reform of our choose-one system, I see little evidence to assume that a more "expressive" (i.e. complicated and more difficult to explain) system like STAR would be *more* palatable to voters (optimal accuracy or not).

Though the sample size for how Approval and STAR fare at the ballot box is small, the results are concerning:

STAR has been rejected three times by voters in Oregon. There is the Eugene situation that has framed this discussion, of course. But it was also rejected in [Lane County in 2018](https://ballotpedia.org/Lane_County,_Oregon,_Measure_20-290,_Score_Then_Automatic_Runoff_Voting_Method_(November_2018)) (52.4% opposed) and [Oakridge in 2024](https://www.klcc.org/politics-government/2024-11-07/oakridge-voters-reject-star-voting-proposal) (54% opposed, and this was a reversible low-stakes three election pilot test).

I cannot help but wonder if the expressiveness, which makes STAR so appealing to its supporters and proponents, is exactly what is hurting it at the ballot box (at least, based on the evidence we have seen so far). Although, if I may say, the decision to attempt to eliminate the primary appears to have been a poor judgment call (I have no earthly idea if Eugene would have accepted STAR if it had been integrated into the existing primary process somehow).

But more fundamentally, I have to ask: is scoring the options for Commissioner of the Water and Electric Board the way you rate a restaurant on Yelp actually something the average voter is clambering to do? Perhaps this prospect is appealing to political junkies, but I am skeptical that the number of voters who actually like or care about politics (or, at least, their utilities commissioners and comptrollers) enough that this more expressive ballot is enticing, is particularly large. This remains to be seen, and luck could simply have been against STAR in the three Oregon elections (particularly the close ones), but I am not optimistic. It seems concerning to me that the thing that gets supporters so excited and passionate about STAR *might be the very thing that hurts it at the ballot box*.

Eugene is a *very* liberal city in a fairly progressive blue state. If STAR is 0-3 in *Oregon*, then I am really wondering about STAR's long-term potential to be the future of voting reform in the United States. When every *good* reform, like Approval and STAR, has the common enemy of [Ranked-Choice Voting](../ditch-rcv/), I worry about the potential waste of resources and energy that could be spent on a more politically viable reform like the St. Louis model of Approval Top-2.

I have said before that as RCV is dying a slow an agonizing death, we likely have one chance to pivot before we burn through all the good will and willingness to try something new. I like our chances better if we all rally behind the system that has shown itself to be politically viable, and has a proven track record of success in St. Louis. I worry about flying too close to the sun trying to skip over Approval in favor of STAR. And I am deeply concerned with the potential effect of exhausting Oregonians with repeated STAR proposals to the point where they are unwilling to consider any other reform proposals in the future.

The fact that my simulations show that STAR's more complex process becomes indistinguishable from single-round Approval under stress, and significantly worse than Approval Top-2 with a clear-eyed runoff election, makes me exceptionally concerned about STAR voting. Is a complex machine that cannot handle sand in its gears really a good idea for something as important as electing our leaders? I am not so sure.

The evidence in favor of STAR thus far is primarily in simulations done *by STAR proponents themselves*. And though I find their methodology excellent and without obvious flaws or evidence of bias, the numbers so far have not swung me to becoming a STAR supporter<d-footnote>Is it a good system? Probably. But I see insufficient evidence that we should skip over the more simpler and nearly as affective Approval voting in favor of STAR. The simpler and tested solution seems better from where I'm standing.</d-footnote>.

It is impossible to know for sure how actual real world conditions map onto the parameters I have defined in this simulation. Even mild friction could be pessimistic for a high profile election (especially if the field is not particularly crowded). However, I do believe that the narrowing of the gap between STAR and Approval, with Approval Top-2 surpassing it easily, under even mild friction is remarkable.

If we suppose that expressiveness begets complexity which makes the system *less* politically viable, and *also* makes it less robust to real-world conditions, then Approval Top-2 seems to dominate STAR in every way that matters. However, that is just my opinion.

## Appendix

### Condorcet Efficiency

This is a little funnier. Under ideal conditions, Schulze has 100% Condorcet efficiency, as expected. However, under friction, the system designed specifically to elect the Condorcet winner becomes worse at electing the true Condorcet winner than STAR, Approval Top-2, *and* even base Approval (though the gap is very small except for Approval Top-2). It seems that Cardinal systems, at least in this model, are actually better at electing the Condorcet winner than a system designed specifically to do so.

Even Plurality Top-2 did exceptionally well, by the runoff alone.

It appears that if your desire is truly to elect the Condorcet winner no matter the cost, then a runoff method is the way to go if voters are not ideal.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="condorcet-joint" %}

### SCORE vs STAR

I also measured the difference between STAR voting and just plain 5-point scoring (SCORE, i.e. STAR's own ballots with the runoff step switched off) to isolate the runoff's own net effect from everything else STAR does. The difference is fairly negligible in aggregate, but STAR appears to gain a slight edge as friction decreases towards ideal conditions. With low friction, it's very hard to tell. If I had to pick a side, the general benefits of the runoff seem to outweigh the costs (even for just the strategic incentives).

I had wondered if friction might damage outcomes significantly because voters would accidentally vote against their interest in the runoff step. In aggregate, this seemed to have a small effect, but not particularly significant. See the Findings section above for the sharper, per-election version of this same question.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="score-vs-star" mode="images" %}

## The Jupyter Notebook

I am sure this post is going to be particularly controversial, so the full simulation is embedded below rather than just summarized. Before any of the findings above are computed, Sections 12-13 of the notebook sanity-check the simulation itself against externally published VSE values (from the original `vse-sim` project). It seems to be working correctly, though the floor of the ranges appears lower than the ranges generally reported by advocates.

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
