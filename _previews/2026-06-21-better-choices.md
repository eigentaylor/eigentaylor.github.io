---
layout: distill
title: Better Choices Has a Neat Idea
date: 2026-07-06
description: What I like about the system proposed by Better Choices, and my concerns.
importance: 3
tags: voting
category: polisci
featured: false
theorems: true
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
      - name: Strategy is Minimal (in the runoff step)
      - name: A Few Curiosities
  - name: Where I'm Skeptical
  - name: Conclusion
---

## Introduction

For a while now, Condorcet methods have gotten the short end of the stick in the reform space. The disaster known as [Ranked Choice Voting](../ditch-rcv/){:target="_blank"} has dominated the space as a whole, but particularly ranked ballots. Cardinal methods like Approval and STAR have been the main challengers, and while the Equal Vote Coalition "approves" of their flavor of Condorcet (["Ranked Robin"](https://www.equal.vote/ranked_robin)), Condorcet has not yet gained much traction.

Now, if you are reading this blog, you probably know I am a huge fan of Approval voting. I think it is [the most practical and effective reform we should be advocating for right now](../approval-only/){:target="_blank"}, and the only system that I currently support. However, I would like to share my positive thoughts on this neat new proposal by [Better Choices](https://www.betterchoices.vote/top3).

I first heard about this system through a bill in [Ohio](https://www.betterchoicesohio.org/) which would implement a "Top-3 Condorcet" system, where a jungle primary would be held and the top three candidates would advance to a final election conducted using a kind of Condorcet method. They call this system "Consensus Choice Voting". But before we start getting too lost in the jargon, let's ensure we are clear about what I'm even talking about.

### Condorcet Methods

A **Condorcet winner** is a candidate who would win a head-to-head matchup against every other candidate. Simple, right? It's just like a round-robin tournament, where every candidate faces off against every other candidate--and the one who wins every bout is the Condorcet winner.

I have [my issues with the idea of the Condorcet winner as a measure of "consensus"](../why-condorcet/){:target="_blank"}, but *in practice* all "good" methods (Approval, STAR, Score, etc.), even if they do not explicitly satisfy the Condorcet criterion, are going to agree on the best candidate, who is likely a Condorcet winner.

A Condorcet method is just a voting system (that usually takes in a ranked ballot) and then evaluates the head-to-head matchups between every pair of candidates to determine if there is a Condorcet winner, electing them if so. The many Condorcet methods differ only in how they handle the case where there is no Condorcet winner (a "Condorcet cycle").

### Jungle Primaries

I just [published a post about California's Top-2 system](../ca-top-2/){:target="_blank"} in which I talk about the issues with jungle primaries and vote splitting. The fundamental idea of a jungle primary is this:

> Put all candidates on a single primary ballot, from every party, let people vote, and then the top vote-getters advance to a final runoff<d-footnote>This is technically a "nonpartisan blanket primary" but that's so wordy, let's just call it a "jungle".</d-footnote>.

The idea is to force candidates to be held accountable to all voters, rather than just those from their party<d-footnote>For example, in a state like California, the election would often be decided entirely in the Democratic primary, with Republicans getting effectively no say in the outcome.</d-footnote>. The *hope* is that this would elevate consensus candidates with low visibility and boost third parties. These lofty aspirations have largely not materialized because voters can still only choose a single candidate--more on that shortly.

## The Better Choices System

Their proposal is as follows: after the initial primary, the final election is between three candidates. Let's call them Alice, Bob, and Clark. Voters will walk into the booth and see three different races.

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
<br>

If a candidate wins both of their matchups, they are elected. If no candidate wins both matchups, the candidate with the "least bad loss" (the one who lost by the smallest margin) is elected<d-footnote>This is called "minimax". Essentially, if everyone loses at least one race, then we pick the one who lost by the smallest amount.</d-footnote>.

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

I have many problems with ranked methods, and there are reports that RCV negatively impacts voter confidence and satisfaction with the election process<d-cite key="mit2021maineRcv"></d-cite>. But one issue that I've come to find especially serious is that voters have no idea how their ranked ballot is going to be counted. Ask a voter if they understand how RCV works (even people who vote in RCV elections), or how their ballot is counted, and they will almost certainly say yes. [But if you ask them to explain it, most reveal a fundamental misunderstanding](https://web.archive.org/web/20190219005105mp_/https://sites.google.com/a/electology.org/www/approval-score-sf#TOC-Intuitive-understanding)--and are often horrified when told how it actually works.

I think this is a *big problem with ranked ballots*. Each voter arrives with their own idea of how the ballot is going to be counted, and many of them will be understandably wrong<d-footnote>When I once tried to explain to a friend that a Condorcet winner was not elected in Alaska, they invented the Borda count on the spot, assuming that is the correct way to elect a pairwise winner. The fact that many voters seem to assume a weighted average (in the same vein as the Borda count) is how all Ranked voting methods work makes me think that ranked ballots are just inherently confusing.</d-footnote>. It should, in my view, be obvious to voters how their ballot is going to be counted.

This is one thing I like about Approval: it's not hard to understand that a bubble is a vote. That's how choose-one voting works, and Approval works the same way, using the same interface. Hence, Consensus Choice Voting uses that *same* interface to its advantage. I think the idea of head-to-head matchups becomes much *more* obvious in this format than using a ranked ballot<d-footnote>A typical Condorcet method interprets a ranking like $A>B>C$ as one vote for $A$ over $B$, one vote for $A$ over $C$, and one vote for $B$ over $C$. Some voters might misunderstand and assume that $A$ gets "extra points" for being higher over $C$. By dropping the ranking interface, such misunderstandings can be reduced.</d-footnote>.

This also simplifies implementation on existing voting machines, which is something I really like about Approval! Tallying becomes exceptionally simple: it's just three different matchups (six total tallies) instead of one. That's not absurdly overcomplicated.

One key question that remains is whether voters will understand how these head-to-head matchups translate to a winner. Will they be confused and expect that the candidate who wins any matchup by the most votes is crowned the winner? Or will they understand the Condorcet principle at play?

Ballot usability matters enormously to me. As far as design goes, this is an extremely friendly ballot, especially relative to RCV and STAR. But it is objectively more complex than a choose-one or Approval ballot. Therefore, it's entirely possible that *even this* system could be too complex for voters to find palatable<d-footnote>My mother found it too confusing, and that's a bad sign because she is a smart lady.</d-footnote>.

It's impossible for us voting nerds to say how regular voters will react to seeing each candidate on the ballot twice, and having to vote in three different matchups. I want rigorous, independent usability studies before I jump on the bandwagon. But if there's *any* way to make Condorcet work, it's probably this or nothing.

### So Much Better Than RCV

I wish it didn't *need* to be said, but it does. Compared to this, [RCV is legitimately awful](../ditch-rcv/). The practical drawbacks of RCV are not as blatant with only three candidates (you only effectively need to keep track of nine tallies with three candidates<d-footnote>The number of bullet voters, and the six possible transfers: $A\to B$, $A\to C$, $B\to A$, etc.</d-footnote>), but we have seen RCV fail utterly in elections with three viable candidates, such as [Alaska and Burlington](../ditch-rcv/){:target="_blank"}.

RCV utterly fails to deliver on its promises. Voters assume that ranking a second choice protects against their least favorite, but RCV only looks at first choices, ignoring the preference data it collected<d-footnote>This is why Later No Harm is a joke criterion that nobody who understands social choice takes as anything close to "desirable". By protecting your first choice from your later choices, the system can't <em>save</em> your second choice if your first is nonviable. That's what happened in Burlington and Alaska. <a href="https://electowiki.org/wiki/Later-no-harm_criterion">Later No Harm is incompatible with a number of other desirable properties like No Favorite Betrayal</a>. If you want to protect your first choice from your second choice, you will often have to betray your honest first choice or else risk electing your last choice directly as a result of your honesty.</d-footnote>. The result: candidates with fervent but thin support (who can't win the final round) can fail to be eliminated and spoil the election; voters who ranked them first end up handing the election to their least favorite, and the consensus candidate the partisans ranked second gets eliminated early. This system fixes that by looking directly at all head-to-head matchups simultaneously--a better measure of who's broadly acceptable, not just who's most polarizing.

### Cognitive Simplicity

The choice of three is a good move, I think. A two-candidate runoff is nice because the race is cognitively simple. You just pick who you like better, and the delayed second round means you get more time to decide who you think is genuinely better. It's fully strategyproof ([in the runoff step](https://en.wikipedia.org/wiki/Strategyproofness#Examples)), and your vote absolutely counts.

With three candidates, it's only *slightly* worse in that respect, in my opinion. Three is arguably not *too many*, and means that voting in each matchup is entirely tractable! Asking voters directly "who do you prefer out of these two?" is still a simple question. Four is kind of pushing it, and would require six matchups, effectively forcing a return to the ranked ballot<d-footnote>On <a href="https://www.betterchoices.vote/consensus-choice">the Better Choices website</a>, their proposal for Top 4 uses a ranked ballot. Voting in each matchup only really works with three candidates.</d-footnote>. Three candidates is a sweet spot.

I've been skeptical of runoffs in the past, due to potential strategy concerns<d-cite key="fishburnBrams1981runoff"></d-cite>. However, in practice, I've been convinced that the opportunity to distinguish between a final set of candidates, like the two who advance from a top-2 system, is ultimately a good thing. This system *attempts* to do the same thing, but with three candidates--like a theoretical top-2 for all three pairs of candidates.

### System Agreement

Further, when restricted to three candidates, minimax agrees with [Ranked Pairs](https://en.wikipedia.org/wiki/Ranked_pairs) and [Schulze](https://en.wikipedia.org/wiki/Schulze_method)<d-cite key="brandt2025condorcet"></d-cite>, which are top-shelf Condorcet methods. Ranked Pairs and Schulze are robust, but *much* harder to explain. The fact that the simple "least bad loss" system agrees with them is satisfying to me. This means the system is both robust *and* easy to explain, which are both seriously important properties for a voting system to have.

### Pass-Fail Criteria

Condorcet, in general, can fail some desirable criteria. For example, it can fail the [participation criterion](https://en.wikipedia.org/wiki/Participation_criterion). That is, participating in an election might end up giving you a *worse* outcome than if you had abstained. However, this *generally* only occurs with four or more candidates.

With three candidates (or at least the system being considered here), there are no participation failures. No [monotonicity](https://en.wikipedia.org/wiki/Non-negative_responsiveness) violations like in RCV either<d-footnote>This is not that surprising. Monotonicity is actually really hard to violate. Some call it a "free" property, because you need to define an absurdly convoluted system to break it. The fact any seriously considered system fails it is a wonder. Condorcet does not fail monotonicity, but it's worth mentioning it here because of RCV.</d-footnote><d-cite key="brandt2025condorcet"></d-cite>. Minimax also [does not generally satisfy the Condorcet loser criterion](https://en.wikipedia.org/wiki/Condorcet_loser_criterion#Minimax), but *does* with three candidates<d-footnote>This is easily seen by case analysis (if a Condorcet loser exists among three candidates, then a Condorcet winner must also exist and would be elected instead) or the equivalence with Ranked Pairs/Schulze, which do satisfy the Condorcet loser criterion for any number of candidates.</d-footnote>.

This system essentially funnels down Condorcet into the perfect conditions where it really shines.

### Strategy Is Minimal (in the runoff step)

In practice, voting in this system is pretty straightforward. If you have a favorite, you vote for them in both their matchups. Then you can *also* vote for your second choice against your third choice. Easy-peasy.

No system is going to be strategyproof in general, but I think Condorcet methods like this are about as robust as you can get. I do not see any realistic case where a voter has serious incentive to lie on their ballot. Especially when there isn't a cycle. As far as voting systems go, this is probably the most honest system you can get, and that's genuinely nice.

I made [a simple model you can check out here](https://eigentaylor.github.io/weakest-link/graph.html) which shows how insincere deviations can affect the outcome of a Condorcet election if a coalition is able to coordinate and change the relative size of the margins, and I'm going to write a whole post about this model and my findings<d-footnote>In short: the cases where lying is profitable are rare and specific. You'd need to start in a cycle with a very particular structure and/or have a massive coordinated effort to make a difference. Most lies lead to the same or a worse outcome.</d-footnote>. Look forward to that!

### A Few Curiosities

This system actually realizes what I'd call the "Condorcet ideal". Since voters participate in every matchup directly, you can more confidently claim the winner would beat everyone in a head-to-head runoff, rather than approximate head-to-head results from ranked data. I wrote [a cheeky post](../condorcet-approval/){:target="_blank"} in the past about how ranked Condorcet methods are only approximations of this; turns out there's now a system that does it for real.

Oh, and if you're feeling mischievous: you can vote intransitively. Rock over Scissors, Scissors over Paper, Paper over Rock. You can't do that in a ranked method. I have no idea why you'd want to, but in this system you are free of the shackles of transitivity!

## Where I'm Skeptical

As I said before, my biggest issue is the choose-one primary. If this system uses the choose-one primary, we will still be plagued by vote-splitting and spoilers, with no [nursery effect for broadly acceptable candidates](../ca-top-2/){:target="_blank"}.

Taking in more candidates does not fix vote splitting, it only expands the chaos. The Duvergerian abandonment dynamics will expand from three to four or more candidates<d-cite key="cox1994sntv"></d-cite>, and voters will still be pushed towards the safest established names of the major parties. The lockout problem might be fixed, but the spoiler problem won't. The broad "consensus choice", who would naturally be elevated by Approval voting, might not even make it into the "Consensus Choice" part of the election because voters are not free to support more than just their safest bet in the primary.

If, instead, Better Choices were to use Approval voting in the first round, then I think this could be one of (if not *the*) most robust systems currently in consideration. *Seriously*.

I have been working on a number of [simulations](https://eigentaylor.github.io/satisficing-voter-sim/) which I will write dedicated posts about, but the short version is that Approval, even with just a top two, is overall more robust than any runoff system that uses a choose-one primary, especially under crowded primary fields.

My other major concern is the Condorcet cycle. What happens when a cycle inevitably occurs? When the tiebreaker is used because every candidate loses a matchup, will voters accept that result? Or will it undermine the legitimacy of the election? The empirical rarity of cycles does not fully reassure me that if such an event occurred, it wouldn't be as catastrophic to the system as [Burlington 2009 or Alaska 2022 were to RCV](../ditch-rcv/){:target="_blank"}.

I've [written previously](../approval-only/){:target="_blank"} about how important legitimacy to the winner is to me. When comparing a general election under Approval to Condorcet, there's an argument to be made that Approval delivers a much more legitimate outcome, based on the ballot data<d-cite key="fishburnLittle1988approvalExperiment"></d-cite><d-footnote>In the experiment, voters submitted both approvals and rankings. The Approval winner won by over 130 votes, but the Condorcet winner was a different candidate who won the pairwise matchup against the Approval winner by a single vote, with 27 voters abstaining in that matchup. Had the rankings not been submitted, the election would have looked decisive, but that mandate was arguably muddied by the pairwise data.</d-footnote>. In a similar vein, a top-2 general election is always decisive and clear, with a majority mandate for the winner. A Condorcet cycle, on the other hand, is a mess. No matter who is elected, they will have to govern with everyone knowing a majority of voters preferred someone else to them.

## Conclusion

This system has potential, but only if it addresses the fundamental issue of vote splitting in the primary by using Approval voting. Without this change, I believe the system is going to be a downgrade from any system that uses Approval in the process. That is, switching to Approval Top-2 instead would be a much stronger improvement than *only* changing the runoff step<d-footnote>Is it a step in the right direction? I'm skeptical. I think if we do this and leave the primary as a choose-one election, the fundamental issue of vote splitting delivering poor outcomes will remain, one more slot or not. As more candidates run, the choose-one mechanism will still be stressed to its limits and deliver worse outcomes than if we had used Approval with fewer candidates in the general. In other words, my foremost concern is the opportunity cost of not patching the primary election when that seems like the most pressing issue.</d-footnote>.

What remains to be seen for me is:

1. Will Better Choices adopt Approval voting in the first round to address the vote-splitting issue?
2. Will this proposal actually *play* to voters? Will voters vote "yes" if it's on the ballot<d-footnote>Complex systems like <a href="https://ballotpedia.org/Eugene,_Oregon,_Measure_20-349,_STAR_Voting_for_Mayor_and_City_Council_Elections_Initiative_(May_2024)">STAR voting</a> and RCV have a tendency to be murdered at the ballot box. STAR lost in 2024 with over 64% voting "no". Can Better Choices succeed where others have failed?</d-footnote>? Will we see unbiased usability studies that show voters can understand the ballot and the system?
3. Will this system be able to weather Condorcet cycles in a way that maintains voter confidence and legitimacy?

As I've said before, virtually all "good" voting methods<d-footnote>Primarily, Approval, Condorcet, and STAR voting. RCV is a noticeable downgrade from these systems.</d-footnote> are going to agree most of the time, and will largely all defuse polarization and encourage more representative candidates. With that in mind, I think the most politically viable, practical, and voter-friendly system is very likely the best one.

Approval Top-2 is tested, excellent, and checks all the boxes. It seems like a much safer system to back. The fact that it's *already* being used in St. Louis<d-cite key="sargent2025stlouis"></d-cite> is a fantastic thing to be able to point to, advocacy-wise.

That said, I could see an argument that by taking in one more candidate from the Approval jungle (which would reduce the number of lockouts), this slightly more expressive--but still grounded and digestible--general election ballot could make a more *palatable* reform that people can get excited about. But this remains to be seen.

I *do* genuinely like this system. I hope that Better Choices decides to go with Approval voting in the first round, and then I would consider this a top-tier method (should it prove politically viable). I am absolutely keeping my eye on this.
