---
layout: distill
title: Approval is a Condorcet Method
date: 2026-04-01
description: Approval is the perfect Condorcet method, and I have permanently solved the Condorcet paradox. April Fools!
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
related_posts: true
theorems: true
pretty_table: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: Conclusion
  - name: References
---

## Introduction

Merry April Foolsmas, everyone! Fellow Condorcetists, I come bearing a gift: I have permanently solved the Condorcet paradox. There is in fact a *perfect* voting system: Approval voting, and it *is* indeed a Condorcet method.

[For an actually serious post on the fact that Approval is a practical Condorcet approximation, see this post.](../practicalapproval){:target="_blank"}

During the time of the French revolution, two titans battled out their ideas of what a good voting system were: Their names were Jean-Charles de Borda and the Marquis de Condorcet.

- Borda: Believed that we should give candidates points based on where they are ranked. My lowest ranked candidate gets zero. Next up gets one, and so on.
- Condorcet: Had a much better idea. If there is a Candidate who would defeat every other candidate in a one-on-one race, then they should be elected.

But it is impractical to hold an election for every $\frac{n(n-1)}{2}$ pair of candidates, so we need a voting system that can be used in a single election, but still satisfies the Condorcet criterion: if there is a Condorcet winner, they should win.

We compromise on the idea that we can simulate how voters would vote in each theoretical matchup by ranking candidates. If I rank Alice first, Bob and Clark second, and Dylan last, then I am saying that 

- I would vote for Alice over Bob, Alice over Clark, and Alice over Dylan.
- I would vote for Bob over Dylan, and Clark over Dylan.
- I am not as sure about Bob vs Clark, but I feel about the same about them, so I am ranking them equally.

The single ranked ballot thus allows us to simulate how voters would vote in each theoretical matchup, and thus determine if there is a Condorcet winner. If there is, then by golly, they should win!

If you do not elect such a candidate, then **what are you even** ***doing***? [Why ask for rankings if you aren't even going to use or respect them?](../ditch-rcv){:target="_blank"}. If you do not elect such a candidate, then you have elected someone else who has to serve their constituents knowing that a majority of voters wanted someone else more. That creates a [legitimacy problem](../consistentcardinal){:target="_blank"}.

Further, it's far more efficient to just count up the individual pairwise votes. This is precinct summable: It is realistic for the high school gymnasium to count up the approximately $n(n-1)$ number of pairwise votes, and just post them on the door. This can be added up across precincts, and it only requires simple addition to determine if such a candidate exists. This is much easier than doing something like a *ridiculously complex* algorithm where we count up first choices only, arbitrarily, eliminate the candidate with the least votes, and transfer votes around until someone gets a majority. This would require central tabulation, be more opaque, and have worse outcomes in simulations. That'd be a really stupid voting system, who would even want to use that? If we count rankings, we should use them! Condorcet only, baby!

The biggest question is, however, does such a candidate even exist? How likely is it that if we hold an election with hundreds, thousands, or even millions of voters, that there will be a single candidate who would be ranked above every other candidate by a majority of voters (when the results are not tied)? It turns out the answer can be 100%, or not 100%, depending on the system.

## Condorcet Methods

> **Definition**: A (Generalized) *Condorcet method* (GCM) is a voting system where voters can rank candidates, with ties allowed, among some number of tiers. If a voter ranks candidate X strictly over candidate Y, then that voter casts a vote for X in the X vs Y matchup. If there is a candidate who wins all of their matchups, then that candidate *must* win.

Simple enough. If 100 voters rank Alice above Bob, and 50 voters rank Bob above Alice, while 600 voters rank Alice and Bob equally, then Alice defeats Bob and Bob does not defeat Alice. If there is a candidate who defeats every other candidate, then they are the Condorcet winner, and they must win.

Generally, a Condorcet method uses the same number of tiers as there are candidates, so that voters could theoretically rank all candidates in a complete transitive order. 

> **Definition**: 

## Conclusion

## References