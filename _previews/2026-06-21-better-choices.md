---
layout: distill
title: Better Choices Has a Neat Idea
date: 2026-06-30
description: What I like about the system proposed by Better Choices, and my concerns.
importance: 3
tags: voting
category: polisci
featured: false
theorems: true
related_posts: true
pretty_table: true
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
    subsections:
      - name: Condorcet Methods
      - name: Jungle Primaries
  - name: The Better Choices System
  - name: Why This is Cool
    subsections:
      - name: Ballot Design
      - name: So Much Better Than RCV
      - name: Cognitive Simplicity
      - name: System Agreement
      - name: Pass-Fail Criteria
      - name: Strategy is Minimal
      - name: A Few Curiosities
  - name: Where I'm Skeptical
  - name: Conclusion
---

## Introduction

For a while now, Condorcet methods have gotten the short end of the stick in the reform space. The disaster known as [Ranked Choice Voting](../ditch-rcv/){:target="_blank"} has dominated the space as a whole, but particularly ranked ballots. Cardinal methods like Approval and STAR have been the main challengers, and while the Equal Vote Coalition "approves" of their flavor of Condorcet ("Ranked Robin"), Condorcet has not yet gained much traction.

Now, if you are reading this blog, you probably know I am an Approval die-hard. I think it is [the most practical and effective reform we should be supporting right now](../approval-only/){:target="_blank"}. However, I would like to share my positive thoughts here in this post.

I first heard about the system proposed by Better Choices through a bill in Ohio which would implement a "Top-3 Condorcet" system, where a jungle primary would be held and the top three candidates would advance to a final election conducted using a kind of Condorcet method. But before we start getting too lost into the jargon, let's ensure we are clear about what the hell I'm even talking about.

### Condorcet Methods

A Condorcet winner is a candidate who would win a head-to-head matchup against every other candidate. Simple, right? I have [my issues with the idea of the Condorcet winner as a measure of "consensus"](../why-condorcet/){:target="_blank"}, but *in practice* all "good" methods (Approval, STAR, Score, etc.) are going to agree on the best candidate, who is likely a Condorcet winner.

A Condorcet method is just a voting system (that usually takes in a ranked ballot) and then evaluates the head-to-head matchups between every pair of candidates to determine if there is a Condorcet winner. Some are complex, some are simple, some are a single method that is designed to pick the Condorcet winner if one exists, and some just say "elect the Condorcet winner if they exist, else do this other thing".

### Jungle Primaries

I just [published a post about California's Top-2 system](../ca-top-2/){:target="_blank"} in which I talk about the issues with jungle primaries and vote splitting. The fundamental idea is this:

> Put all candidates on a single primary ballot, from every party, let people vote, and then the top vote-getters advance to a final runoff.

This is technically a "nonpartisan blanket primary" but that's so wordy, let's just call it a "jungle".

The idea is to force candidates to be held accountable to all voters, rather than just those from their party<d-footnote>For example, in a state like California, the election would often be decided entirely in the Democratic primary, with Republicans getting effectively no say in the outcome.</d-footnote>. The *hope* is that this would elevate consensus candidates with low visibility and boost third parties. This has largely not materialized because voters can still only choose a single candidate.

When votes are a scarce resource, this leads to rallying behind the most viable candidate from your favorite major party, and rampant vote splitting from voters who are naive enough to support less popular candidates.

In my view, [any system that uses a choose-one jungle primary is a non-starter](../ca-top-2/){:target="_blank"}. It's simply *awful*. The issue with the jungle primary is *not* the runoff step, but the vote splitting. However, we will come back to this. First, we should discuss what Better Choices is actually advocating for.

## The Better Choices System

After the initial primary, the final election is between three candidates. Let's call them Alice, Bob, and Clark. Voters will walk into the booth and see three different races.

1. Alice versus Bob
2. Alice versus Clark
3. Bob versus Clark

Just like a choose-one or Approval system, there's a bubble next to each name. Voters then vote in each individual matchup, indicating their preference for one candidate over the other.

<iframe id="better-choices-frame" src="/assets/html/better-choices-ballot.html"
  width="100%" height="520" scrolling="no"
  frameborder="0"
  style="border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.18); display: block; margin-top: 1rem; overflow: hidden;"
  title="Interactive head-to-head ballot – Alice, Bob, and Clark">
</iframe>
<script>
window.addEventListener("message", function(e) {
  if (e.data && e.data.condorcetHeight) {
    var f = document.getElementById("better-choices-frame");
    if (f) f.style.height = e.data.condorcetHeight + "px";
  }
});
</script>

If a candidate wins both of their matchups, they are elected. If no candidate wins both matchups, the candidate with the "least bad loss" (the one who lost by the smallest margin) is elected<d-footnote>This is called "minimax".</d-footnote>.

<iframe id="condorcet-election-frame" src="/assets/html/condorcet-election.html"
  width="100%" height="480" scrolling="no"
  frameborder="0"
  style="border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.18); display: block; margin-top: 1rem; overflow: hidden;"
  title="Interactive Condorcet/minimax election visualization">
</iframe>
<script>
window.addEventListener("message", function(e) {
  if (e.data && e.data.condorcetElectionHeight) {
    var f = document.getElementById("condorcet-election-frame");
    if (f) f.style.height = e.data.condorcetElectionHeight + "px";
  }
});
</script>

## Why This Is Cool

Alright, I'm just gonna kind of nerd out here.

### Ballot Design

I have many problems with ranked methods <d-cite key="mit2023maineRcv"></d-cite>. But one that I've come to appreciate is that voters have no idea how their ranked ballot is going to be counted. Ask a voter if they understand how RCV works (even people who vote in RCV elections), or how their ballot is counted, and they will almost certainly say yes. But if you ask them to explain it, many I have talked to have experienced that the person then shows a fundamental misunderstanding (and are often horrified when they are told how it actually works)<d-footnote>I once tried to describe Condorcet to a friend (an intelligent guy) and they immediately invented Borda on the spot. Top rank gets 3 points, second rank gets 2, and last gets 1. I have heard similar stories from people like Clay Shentrup and Hayden Sasswood.</d-footnote>.

I think this is a *big problem with ranked ballots*. It should, in my view, be explicitly clear and obvious what the system is going to do with your vote, and how it's going to be counted and tallied to determine the winner.

This is one thing I like about Approval: it's not hard to understand that a bubble is a vote. That's how choose-one voting works, and Approval works the same way, using the same interface. Hence, the Better Choices system uses that *same* interface to its advantage. I think the idea of head-to-head matchups becomes much *more* obvious<d-footnote>A typical Condorcet method interprets a ranking like $A>B>C$ as one vote for $A$ over $B$, one vote for $A$ over $C$, and one vote for $B$ over $C$. Some voters might misunderstand and assume that $A$ gets "extra points" for being higher over $C$. By dropping the ranking interface, such misunderstandings can be reduced.</d-footnote>.

This is also nice because this should make it much easier to implement on existing voting machines, which is something I really like about Approval! Tallying becomes exceptionally simple: it's just three different matchups (six total tallies) instead of one. That's not absurdly overcomplicated.

The only question that remains is if the voters will understand how these head-to-head matchups translate to a winner. Will they be confused and expect the one who wins any matchup by the most is crowned the winner? Or will they understand the Condorcet principle at play?

I am someone who is very concerned about reforms with a hostile ballot. As far as ballots go, this is an extremely friendly ballot, especially relative to RCV and STAR. But it is objectively more complex than a choose-one or Approval ballot. Therefore, it's entirely possible that *even this* system could be too complex for voters to find palatable<d-footnote>My mother found it too confusing, and that's a bad sign because she is a smart lady.</d-footnote>. I want rigorous and unbiased/independent usability studies before I jump on board the bandwagon. But if there's *any* way to make Condorcet methods work, it's probably this or nothing.

### So Much Better Than RCV

I wish it didn't *need* to be said, but it does. Compared to this, RCV is legitimately awful. The practical drawbacks of RCV are not as blatant with only three candidates (you only effectively need to keep track of nine tallies with three candidates<d-footnote>The number of bullet voters, and the six possible transfers: $A\to B$, $A\to C$, $B\to A$, etc.</d-footnote>), but we have seen RCV fail utterly in elections with three viable candidates, such as [Alaska and Burlington](../ditch-rcv/){:target="_blank"}.

RCV utterly fails to deliver on its promises. Voters assume that ranking a second choice protects against their least favorite, but RCV only looks at first choices, ignoring the preference data it collected<d-footnote>This is why Later No Harm is a joke criterion that nobody who understands social choice takes as anything close to "desirable". By protecting your first choice from your later choices, the system can't <em>save</em> your second choice if your first is nonviable. That's what happened in Burlington and Alaska. <a href="https://electowiki.org/wiki/Later-no-harm_criterion">Later No Harm is incompatible with No Favorite Betrayal</a>. If you want to protect your first choice from your second choice, you will often have to betray your honest first choice or else risk electing your last choice directly as a result of your honesty.</d-footnote>. The result: candidates with fervent but thin support (who can't win the final round) stay in too long instead of being eliminated, voters who ranked them first end up handing the election to their least favorite, and the consensus candidate the partisans ranked second gets eliminated. This system fixes that by looking directly at head-to-head matchups--a better measure of who's broadly acceptable, not just who's most polarizing.

### Cognitive Simplicity

The choice of three is a very good move, I think. A two-candidate runoff is very nice because the race is very cognitively simple. You just pick who you like better, and it means you get more time to decide who you think is genuinely better. It's fully strategyproof (in the runoff step) <d-cite key="may1952simpleMajority"></d-cite>, and your vote absolutely counts.

With three candidates, it's only *slightly* worse in that respect, in my opinion. Three is arguably not *too many*, and means that voting in each matchup is entirely tractable! Asking voters directly "who do you prefer out of these two" is still a simple question. Four is kind of pushing it, and would require six matchups, requiring going back to the ranked ballot.

I've been skeptical of runoffs in the past, due to potential strategy concerns<d-cite key="fishburnBrams1981runoff"></d-cite>. However, in practice, I've been convinced that Approval with a runoff in particular is quite robust, since it lets voters feel safer being more generous with their approvals than they might otherwise be. The runoff step also allows for a real choice to distinguish between the options for all voters, even if they didn't distinguish previously.

I've also shared many issues with Condorcet methods in past posts. However, I believe the restriction of the Condorcet mechanism to the runoff step, among 3 candidates, essentially quells all of my concerns. I've always *liked* Condorcet in the abstract, and this feels like the *right way to do it*<d-footnote>Just because Approval is my favorite method does not make me a cardinalist. I've always leaned more towards Condorcet than something like SCORE or STAR.</d-footnote>.

### System Agreement

Further, when restricted to three candidates, minimax agrees with Ranked Pairs and Schulze<d-cite key="brandt2025condorcet"></d-cite>, which are top-shelf Condorcet methods. Ranked Pairs and Schulze are robust, but *much* harder to explain. The fact that the very simple "least bad loss" system agrees with them is very satisfying to me. This means the system is both robust *and* easy to explain, which are both very important properties for a voting system to have.

### Pass-Fail Criteria

Condorcet, in general, can fail some desirable criteria. For example, it can fail the participation criterion. That is, participating in an election might end up giving you a *worse* outcome than if you had abstained. However, this *generally* only occurs with four or more candidates.

With three candidates (or at least the system being considered here), there are no participation failures. No monotonicity violation like in RCV either<d-footnote>This is not that surprising. Monotonicity is actually really hard to violate. Some call it a "free" property, because you need to define an absurdly convoluted system to break it. The fact any seriously considered system fails it is a wonder. Condorcet does not fail monotonicity, but it's worth mentioning it here because of RCV.</d-footnote><d-cite key="brandt2025condorcet"></d-cite>. Minimax also [does not generally satisfy the Condorcet loser criterion](https://en.wikipedia.org/wiki/Condorcet_loser_criterion#Minimax), but *does* with three candidates<d-footnote>This is easily seen by case analysis (if a Condorcet loser exists among three candidates, then a Condorcet winner must also exist and would be elected instead) or the equivalence with Ranked Pairs/Schulze, which do satisfy the Condorcet loser criterion for any number of candidates.</d-footnote>. Further, when outside of a cycle, the system will satisfy [IIA](../iia/){:target="_blank"}!

This system essentially funnels down Condorcet into the perfect conditions where it really shines.

### Strategy Is Minimal

(in the runoff step)

In practice, voting in this system is pretty straightforward. If you have a favorite, you vote for them in both their matchups. Then you can *also* vote for your second choice against your third choice. Easy-peasy.

No system is going to be strategyproof in general, but I think Condorcet methods like this are about as robust as you can get. I do not see any realistic case where a voter has serious incentive to lie on their ballot. Especially when there isn't a cycle. As far as voting systems go, this is probably the most honest system you can get, and that's genuinely nice.

I made [a simple model you can check out here](https://eigentaylor.github.io/weakest-link/graph.html) which shows how insincere deviations can affect the outcome of a Condorcet election if a coalition is able to coordinate and change the relative size of the margins, and I'm going to write a whole post about this model and my findings. Look forward to that!

### A Few Curiosities

This system actually realizes what I'd call the "Condorcet ideal". Since voters participate in every matchup directly, you can genuinely claim the winner would beat everyone in a head-to-head runoff, not just by approximation by analyzing voter rankings. I wrote a cheeky post in the past about how ranked Condorcet methods are only approximations of this; turns out there's now a system that does it for real.

Oh, and if you're feeling mischievous: you can vote intransitively. Alice over Bob, Bob over Clark, Clark over Alice. You can't do that in a ranked method. I have no idea why you'd want to, but this is America. Be free of the shackles of transitivity!

## Where I'm Skeptical

As I said before, my biggest issue is the choose-one primary. If this system uses the choose-one primary, we will still be plagued by vote-splitting and spoilers, with no [nursery effect for broadly acceptable candidates](../ca-top-2/){:target="_blank"}.

Taking in more candidates does not fix vote splitting, it only expands the chaos. The Duvergerian abandonment dynamics will expand from three to four or five candidates<d-cite key="cox1994sntv"></d-cite>, and voters will still be pushed towards the safest established names of the major parties. The lockout problem will be fixed, but the spoiler problem doesn't. A diverse field is not the same as a competitive one. And, in my opinion, a competitive election between two similar candidates close to the median is far more preferable to a foregone conclusion with a diverse field of candidates.

If, instead, Better Choices were to use Approval voting in the first round, then I think this could be one of (if not *the*) most robust systems currently in conversation. *Seriously*.

I have been working on a number of [simulations](https://eigentaylor.github.io/satisficing-voter-sim/) which I will write dedicated posts about, but the short version is that Approval, even with just a top two, is overall more robust than any runoff system that uses a choose-one primary.

My other major concern is the Condorcet cycle. What happens when a cycle necessarily occurs? In the Better Choices system, it can easily run into a sort of "tie" where all candidates end up winning and losing exactly one matchup. When the tiebreaker is used, will voters accept that result? Or will it undermine the legitimacy of the election? The empirical rarity of cycles does not fully reassure me that if such an event occurred, it wouldn't be as catastrophic to the system as [Burlington 2009 or Alaska 2022 were to RCV](../ditch-rcv/){:target="_blank"}.

## Conclusion

This system has potential, but only if it addresses the fundamental issue of vote splitting in the primary by using Approval voting. Without this change, I believe the system is going to be a downgrade from any system that uses Approval in the process. That is, going to Approval Top-2 instead would be a much stronger improvement than *only* changing the runoff step.<d-footnote>Is it a step in the right direction? I'm skeptical. I think if we do this and leave the primary as a choose-one election, the fundamental issue of vote splitting delivering poor outcomes will remain, one more slot or not. As more candidates run, the choose-one mechanism will still be stressed to its limits and deliver worse outcomes than Approval taking in fewer candidates. In other words, my foremost concern is the opportunity cost of not patching the primary election when that seems like the most pressing issue.</d-footnote>

What remains to be seen for me is

1. Will Better Choices see the necessity of implementing Approval voting in the first round to address the vote-splitting issue?
2. Will this proposal actually *play* to voters. Will voters vote "yes" if it's on the ballot? Will they like it enough to keep it around if it passes? Will politicians support and push for it, without it becoming a partisan disaster like RCV has been? Are there unbiased usability studies that show voters can understand the ballot and the system?
3. Will this system be able to weather Condorcet cycles in a way that maintains voter confidence and legitimacy?

As I've said before, basically all "good" voting methods<d-footnote>Primarily, Approval, Condorcet, and STAR voting. RCV is a noticeable downgrade from these systems.</d-footnote> are going to agree most of the time, and will largely all defuse polarization and encourage more representative candidates. With that in mind, I think the most practical and voter-friendly system is very likely the best one.

Approval Top-2 is tested, excellent, and one of the most voter-friendly systems, and seems like a much safer system to back. The fact that it's *already* being used in St. Louis <d-cite key="sargent2025stlouis"></d-cite> is a fantastic thing to be able to point to, advocacy-wise.

That said, I could see an argument that by taking in one more candidate from the Approval jungle (which would reduce the number of lockouts), this slightly more expressive--but still grounded and digestible--general election ballot could make a more *palatable* reform that people can get excited about. But this remains to be seen.

I *do* genuinely like this system. I hope that Better Choices decides to go with Approval voting in the first round, and then I would consider this a top-tier method (should it prove politically viable). I am absolutely keeping my eye on this.
