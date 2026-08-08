---
layout: distill
title: 'Coarse Correction Part 2: The Ranked Implosion'
date: 2026-08-08
description: The complete collapse of ranked methods like Schulze under friction.
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
  - name: Findings
    subsections:
      - name: The Ranked Methods Implosion
      - name: Condorcet Efficiency
      - name: Robustness Rankings
      - name: The Shape of the Data
      - name: A Stricter Confidence Interval
  - name: Conclusion
  - name: Appendix
    subsections:
      - name: Further Research
      - name: The Jupyter Notebook
---

## Introduction

[part 1](../runoff-accuracy)...


## Findings

### The Ranked Methods Implosion

Perhaps the most shocking thing to me was the complete and utter collapse of the VSE of ranked methods like Schulze under friction. Going from the absolute best method to basically the worst method was not in any of my hypotheses; however, it's not exceptionally surprising in retrospect.

Schulze already has a massive drop-off in VSE under strategic voting. When you design a system to calculate the Condorcet winner explicitly, then you do indeed get the highest possible VSE under completely ideal honest voting (because the Condorcet winner is almost always that best candidate). But dishonest data just ends up electing someone else (who is almost surely *worse* than the Condorcet winner).

I expected friction to cause STAR to break, but I should have realized that Condorcet was the far more intricate machine that would truly seize up when sand got in its gears. It gets far worse for Schulze when voters are not even ranking candidates. It relies on all that nuanced preference data to do its thing, and otherwise it's just a mess. This is the Formula 1 race car spinning out when the track gets wet. You use a race car on a pristine track, but you don't drive it to Wendy's in the rain.

Ranked-Choice Voting (RCV) does not fare much better. The gap between it and Schulze is small and inconsistent in direction. They are overall the most negatively impacted by friction of all methods tested, becoming abysmal under heavy friction. As someone relatively sympathetic to Condorcet methods, it does not fill me with relish to say that Schulze's massive outcome advantage over RCV basically completely vanishes. Further, RCV is already very bad across the board, in essentially every respect (like practicality and logistical complexity), but even this is appalling. This is yet another way in which RCV is a poor choice for public elections, and I would not recommend it to anyone.

I would not consider myself a cardinalist, but this has given me new appreciation for how sensitive ranked data can be to noise (the "garbage in, garbage out" problem seems to be far worse for ranked methods than STAR voting). The fact that cardinal voting deals with candidates *independently* (with the exception of STAR's automatic runoff) seems to cushion the blow of widespread noise and truncation.

I may investigate the [Better Choices](../better-choices/) model of a delayed top-3 Condorcet runoff in a follow-up, to see if reducing Condorcet to three candidates, following a choose-one or Approval all-candidate primary, would be more robust than just doing Schulze on all 6 candidates in a single round<d-footnote>At the suggestion of Sass, I did a cursory test of Schulze with tied rankings for candidates with very close utilities. This seemed to cushion the major VSE drop that Schulze experiences due to friction, like flipped rankings from noise. That is, the true preference of a voter could be $A$ over $B$, but noise might flip it to $B$ over $A$. If the utilities are close, then ranking $A$ and $B$ equally does not cast a vote in the wrong direction, even if it doesn't cast a vote in the right direction. This was not tested rigorously, and requires further investigation. However, it seems to potentially put Schulze on par with STAR under friction, rather than significantly worse than both STAR and plurality.</d-footnote>.


{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="ranked-implosion" %}<br>

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="rcv-schulze-ci" %}

### Condorcet Efficiency

This is a little funnier. Under ideal conditions, Schulze has perfect 100% Condorcet efficiency, as expected. It's far beyond all other systems in doing this exact job:

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="ideal-honest-ce-table" %}

Surprisingly, Approval Top-2 is the best non-Condorcet method at electing the Condorcet winner, ahead of even STAR under ideal conditions.

However, under friction, the system designed specifically to elect the Condorcet winner becomes worse at electing the true Condorcet winner than basically every other method. It seems that cardinal and runoff systems, at least in this model, are actually better at electing the Condorcet winner than a system designed specifically to do that exact task.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="condorcet-joint" %}<br>

With only a few exceptions, there is sufficient evidence to conclude that Schulze is worse at electing the Condorcet winner than basically all other methods (except RCV) under all levels of friction.

{% proof Expand to see the Condorcet efficiency significance tables %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="ce-ci-table" %}
{% endproof %}

It appears that if your desire is truly to elect the Condorcet winner no matter the cost, then a runoff method is the way to go if voters are not ideal. In fact, it seems your *last* choice should be a Condorcet method like Schulze.

### Robustness Rankings

Just for fun, I decided to implement a few measures of robustness to evaluate the systems across several different dimensions.

1. Mean VSE
2. Worst-case VSE (by lower bound of the 95% confidence interval)
3. Avg. regret vs the best at that point
4. Avg. rank across the axis

Under ideal conditions, we measure robustness over strategy (ex. across the calculated VSE range). We also measure robustness across the friction scenarios (with and without ideal included).

Under ideal conditions, Approval Top-2 actually tops the ranks overall, with STAR in second place. This surprised me, but it makes sense. AT2 has a tighter and higher range, even if its honest VSE is a little lower.

When we looked at the robustness across friction scenarios, Approval Top-2 (Groggy and Clear-Eyed) is consistently the most robust. The flavors of Plurality Top-2 generally take up second place collectively.

{% proof Expand to see the robustness rankings tables %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="robustness-rankings" %}
{% endproof %}

### The Shape of the Data

This is also fun. VSE is generally reported as a point value, but it is actually an average of a distribution of outcomes of the form

$$\operatorname{VSE}(election)=\frac{u(winner)-\operatorname{avg}(u)}{\operatorname{max}(u)-\operatorname{avg}(u)}$$

for each election, where $u(winner)$ is the utility of the winner in that election, $\operatorname{avg}(u)$ is the average utility of all candidates in the election, and $\operatorname{max}(u)$ is the utility of the utility maximizer in that election. This is 1.0 if the winner is the utility maximizer, 0 if the winner has exactly average utility, and negative if the winner has below average utility. The VSE is the mean of this distribution, but the distribution itself is interesting to look at.

We look at the distribution of outcomes for each system under different levels of friction. We narrow our focus to six systems under the joint scenarios: STAR, Approval, Approval Top-2, Plurality, Plurality Top-2, and Schulze.

Under ideal conditions, the high VSE systems like STAR and Condorcet are tightly clustered around 100% with a very thin leftward tail. Lower VSE systems have more values near but not at 100%, and that clumpy tail gets fatter and fatter as the VSE drops when friction increases.

The most important thing to note is that the mode is 100% for all plots. Despite the friction, the most common outcome is the best candidate winning (terrible systems or not). What the "low" VSE values we have shown in this post really say is that, under friction, the commonality of these best outcomes decreases. The leftward tail of the distribution gets fatter.

Horrifically, exactly one of the six examined systems has negative values more common than the election of the utility maximizer when looking at the joint scenarios: Schulze under heavy friction. That is, Schulze elects someone worse than randomly choosing a candidate more often than it elects the best candidate.

{% proof Expand to see the histograms %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="histogram-data" %}
{% endproof %}

### A Stricter Confidence Interval

To evaluate the robustness of the results, I checked the results that were marked as significant under a 95% confidence interval, and re-evaluated them under a 99% confidence interval. Absence of evidence is not evidence of absence, so this does not mean that a difference or edge does not actually exist, it just shows which results are more robust and persistent.

{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="not-sig-at-99-part2" %}

{% proof Expand to see the results that hold under a 99% confidence interval %}
{% jupyter_cell_embed "assets/jupyter/vse_simulation.ipynb" tag="still-sig-at-99-part2" %}
{% endproof %}

## Conclusion

TODO

## Appendix

### Further Research

The following is a list of things that might be good to look at next, as logical extensions of this work:

1. How robust is a larger runoff system like Approval Top-3 Condorcet, or Plurality Top-4 RCV (the Alaska system)? How do Approval Top-2 and Plurality Top-3 Condorcet compare? How does the learning rate affect the outcomes of these larger runoff systems?
2. What happens to STAR's VSE when we use a "hard zero": where, in the runoff step, a voter's ballot would contribute a vote to a candidate left blank over a candidate who they gave an actual 0.
3. How much better does Schulze/Condorcet do when voters rank equally candidates that have similar utilities

### The Jupyter Notebook

