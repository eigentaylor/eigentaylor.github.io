---
layout: distill
title: Better Choices Has a Neat Idea
date: 2026-06-21
description: What I like about the system proposed by Better Choices, and my concerns.
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
toc:
  - name: Introduction
    subsections:
      - name: Condorcet Methods
      - name: Jungle Primaries
  - name: The Better Choices System
  - name: Why This is Cool
    subsections:
      - name: Ballot Design
      - name: Cognitive Simplicity
      - name: Pass-Fail Criteria
      - name: Strategy is Minimal
      - name: It Fits the Condorcet Ideal
      - name: You can vote intransitively
  - name: Where I'm Skeptical
  - name: Conclusion
---

## Introduction

For a while now, Condorcet methods have gotten the short end of the stick in the reform space. The distaster known as [Ranked Choice Voing](../ditch-rcv/){:target="_blank"} has dominated the space as a whole, but particularly ranked ballots. Cardinal methods like Approval and STAR have been the main challengers, and while the Equal Vote Coalition "approves" of their flavor of Condorcet ("Ranked Robin"), Condorcet has not gained much traction.

Now, if you are reading this blog, you probably know I am an Approval die-hard. I think it is [the most practical and effective reform we should be supporting right now](../approval-only/){:target="_blank"}. However, I would like to share my positive thoughts here in this post.

I first heard about the system proposed by Better Choices through a bill in Ohio which would implement a "Top 3 Condorcet" system, where a jungle primary would be held and the top three candidates would advance to a final election conducted using a kind of Condorcet method. But before we start flying into the jargon, let's ensure we are clear about what the hell I'm even talking about.

### Condorcet Methods

A Condorcet winner is a candidate who would win a head-to-head matchup against every other candidate. Simple, right? I have [my issues with the idea of the Condorcet winner as a measure of "consensus"](../why-condorcet/){:target="_blank"}, but *in practice* all "good" methods (Approval, STAR, Score, etc.) are going to agree on the best candidate, who is likely a Condorcet winner.

A Condorcet method is just a voting system that usually takes in a ranked ballot and then evaluates the head-to-head matchups between every pair of candidates to determine if there is a Condorcet winner. Some are complex, some are simple, some are a single method that is designed to pick the Condorcet winner if one exists, and some just say "elect the Condorcet winner if they exist, else do this other thing".

### Jungle Primaries

A jungle primary is a type of primary election in which all candidates for a given office compete in a single primary, regardless of party affiliation. The idea is to force candidates to be held accountable to all voters, rather than just those from their party. The *hope* is that this would moderate candidates and third parties. This has not happened in the slightest because voters can still only choose a single candidate.

When votes are a scarce resource, this leads to rallying behind the most viable candidate from your favorite major party, and rampant vote splitting from voters who are naive enough to support less popular candidates.

In my view, any system that uses a Choose-one Jungle primary is a non-starter. It's simply *awful*. The issue with the jungle primary is *not* the runoff step, but the vote splitting. However, we will come back to this. First, we should discuss what Better Choices is actually advocating for.

## The Better Choices System

After the initial primary, the final election is between three candidates. Let's call them Alice, Bob, and Clark. Voters will walk into the booth and see three different races.

1. Alice versus Bob
2. Alice versus Clark
3. Bob versus Clark

Just like a choose-one or Approval system, there's a bubble next to each name. Voters then vote in each individual matchup, indicating their preference for one candidate over the other.

If a candidate wins both of their matchups, they are elected. If no candidate wins both matchups, the candidate with the "least bad loss" (the one who lost by the smallest margin) is elected<d-footnote>This is called "minimax".</d-footnote>.

## Why This is Cool

Alright, I'm just gonna kind of nerd out here.

### Ballot Design

I have many problems with ranked methods. But one that I've come to appreciate is that voters have no idea how their ranked ballot is going to be counted. If you place a bunch of ranked ballots in front of people and say "choose a winner", they're probably going to do something of the following

1. A points system (Borda). Top rank gets a certain number of points, the second rank gets fewer points, and so on down the line. Most points wins.
2. Vote transferring (RCV). Eliminate candidates and transfer votes.
3. Pairwise comparison (Condorcet). Maybe a clever voter might ask "what if we just compare each candidate head-to-head against every other candidate and see who wins the most matchups?"

I think this is a *big problem with ranked ballots*. It should, in my view, be explicitly clear and obvious what the system is going to do with your vote, and how it's going to be counted and tallied to determine the winner.

This is one thing I like about Approval: it's not hard to guess that a bubble is a vote. That's how Choose-one voting works, and Approval works the same way. Hence, Better Choices' system uses that *same* interface to its advantage. I think the idea of head-to-head matchups becomes incredibly obvious.

This is also nice because this should make it much easier to implement on existing voting machines, which is something I really like about Approval! Tallying becomes exceptionally simple: it's just three different matchups (six total tallies) instead of one. That's not absurdly overcomplicated.

### Cognitive Simplicity

The choice of three is a very good move, I think. A two-candidate runoff is very nice because the race is very cognitively simple. You just pick who you like better, and it means you get more time to decide who you think is genuinely better. It's fully strategyproof, and your vote absolutely counts.

With three candidates, it's only *slightly* worse in that respect. Three is not *too many*. Four is kind of pushing it, in my view. Three also means that voting in each matchup is entirely tractable! Asking voters directly "who do you prefer out of these two" is still a simple question. There's still potential strategic considerations but, at the moment, it seems very minimal.

I've been skeptical of runoffs in the past, due to potential strategy concerns <d-cite key="fishburnBrams1981runoff"></d-cite>. However, in practice, I've been convinced that Approval with a runoff in particular is quite robust, since it lets voters feel safer being more generous with their approvals than they might otherwise be. The runoff step also allows for a real choice to distinguish between the options for all voters, even if they didn't distinguish previously. The same *somewhat* applies to Choose-one, since it's very possible most voters did not distinguish between the eventual top two winners of the first round.

### System Agreement

Further, when restricted to three candidates, minimax agrees with Ranked Pairs, Schulze, and other Condorcet methods. Ranked Pairs and Schulze are robust, but harder to explain. The fact the very simple "least bad loss" system agrees with them is very satisfying to me.

### Pass-Fail Criteria

Condorcet does not, in general, satisfy the participation criteron. That is, participating in an election might end up giving you a *worse* outcome than if you had abstained. However, this only occurs with four or more candidates.

With three candidates, there are no participation failures. No monotonicity violation like in RCV either. Further, when outside of a cycle, the system will satisfy [IIA](../iia/){:target="_blank"}!

### Strategy is Minimal

In practice, voting is pretty straightforward. If you have a favorite, you vote for them in both their matchups. Then you can *also* vote for your second choice against your third choice. Easy-peasy.

No system is going to be strategyproof in general, but I think Condorcet methods like this are about as robust as you can get. I do not see any realistic case where a voter has serious incentive to lie on their ballot. Especially when there isn't a cycle.

The nice thing about minimax is that it's fairly robust to attempts to throw a cycle. If a Condorcet winner exists, then suppose a coalition purposefully buries them in their weakest matchup. If they are *somehow* able to do this in a way that creates a cycle, then most likely that weakest win of the Condorcet winner becomes the weakest loss of the whole election. Hence the winner is likely unchanged. The coalition would need to be coordinated and large enough to turn it into a strong loss.

If, let's say instead, a coalition tries to manipulate the outcome to change the winner from the honest Condorcet winner Alice to Bob (who won his matchup against Clark), then such a voter would need to make Alice lose to Bob. But that means that voters who previously *honestly* voted for Alice over Bob, would need to lie and vote for Bob over Alice. Which would... give those voters a strictly worse outcome. Why would they do this?

Condorcet methods, particularly minimax, are just remarkably robust in practice. There's seriously no realistic incentive to lie in such a method. It's a genuine strength I appreciate, even as an Approval voting enthusiast.

### It Fits the Condorcet Ideal

I wrote in [a very cheeky past post](../condorcet-approval/){:target="_blank"} about how ranked Condorcet methods are a mere approximation of who would win in every matchup. *Runoff dominance* is what I see as the Condorcet ideal (though Condorcet may not necessarily agree). I actually mentioned in that post that you would need voters to vote in every matchup to truly claim you elected the Condorcet winner. Turns out there's now a system that does precisely this! I think that's cool.

### You can vote intransitively

This is just funny. If you are feeling cheeky, you have full freedom to say "I prefer Alice to Bob, I prefer Bob to Clark, and I prefer Clark to Alice". You can't do this in a ranked method!

Why would you do this? If you have a favorite, why would you vote against them? Well, this is America. You can do whatever you damn well please. Humans are messy, so *maybe* being intransitive floats your boat. I won't judge.

## Where I'm Skeptical

As I said before, my biggest issue is the choose-one primary. If this system uses the choose-one primary, we will still be plagued by vote-splitting, spoilers, and potential lockouts<d-footnote>This was a serious concern in the recent 2026 California Governor's race, where there was at one point a serious chance of the runoff being two Republicans. Regardless of your political stance, a Republican governor of California is an objectively unrepresentative choice in 2026.</d-footnote>.

There will be no nursery effect where moderates and third parties can gain enough support to ever make it into the runoff. Just increasing the number of candidates you take won't change the fundamental dynamics. Instead of the race being between *three* serious candidates and plagued by spoilers (as we have seen in the top 2 system), we will see the race expand to four serious candidates and likely even more spoilers <d-cite key="cox1994sntv"></d-cite>.

This is just what a choose-one multi-winner election with $M$ seats *does*. You get a Duvergerian abandonment of anyone outside of the top $M+1$ candidates, as strategic voters concentrate their support on the leading candidates to avoid wasting their votes.

In California, where Better Choices seems to want to implement their system, the 2026 Governor's race has 61 candidates on the ballot (many of which had dropped out). Are you trying to tell me there are going to be *fewer* candidates running if the number of potential winners *expands*?

More candidates will run, there will be more spoilers and confusion, and the election will still be chaotic, strategic, and partisan, as voters rally behind the most established major party candidates who are perceived as the safest choices.

The issue with jungle primaries *is not that the runoff is between two candidates*. The issue is the vote splitting! Any proposal which does not fix this does not have my endorsement.

If, instead, Better Choices were to use Approval voting in the first round, then I think this could be one of the most robust systems currently in conversation. *Seriously*.

Cursory VSE simulations have been somewhat favorable to this system. I may have to correct this paragraph of the post later, but it appears that Approval Top 2 outperforms Choose-one Top 3 Condorcet, but Approval Top 3 Condorcet potentially outperforms both. However, I'm not yet confident enough in the code I have to make definitive claims, and further testing and validation are needed before drawing firm conclusions.

## Conclusion

This system has potential, but only if it addresses the fundamental issue of vote splitting in the primary by using Approval voting. Without this change, the system is going to be a downgrade from any system that uses Approval in the process. That is, going to Approval Top 2 instead would be a much stronger improvement than *only* changing the runoff step.

What remains to be seen for me is

1. Will Better Choices see the necessity of implementing Approval voting in the first round to address the vote-splitting issue?
2. Will this proposal actually *play* to voters. Will voters vote "yes" if it's on the ballot? Will politicians support and push for it, without it becoming a partisan disaster like RCV has been?

At the moment, Approval Top 2 seems like a much better system to back. The fact it's *already* being used in St. Louis <d-cite key="sargent2025stlouis"></d-cite> is a fantastic thing to be able to point to, advocacy-wise. I feel like Approval is a safer bet, potentially just based on simplicity.

However, I *do* genuinely like this system. I hope that Better Choices decides to go with Approval voting in the first round, and then I would consider this a top-tier method (should it prove politically viable).
