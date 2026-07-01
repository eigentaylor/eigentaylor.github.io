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
      name: Equal Vote Coalition (volunteer)
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
      - name: It Fits the Condorcet Ideal
      - name: You can vote intransitively
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

I have many problems with ranked methods <d-cite key="mit2023maineRcv"></d-cite>. But one that I've come to appreciate is that voters have no idea how their ranked ballot is going to be counted. If you place a bunch of ranked ballots in front of people and say "choose a winner", they're probably going to do one of the following:

1. A points system (Borda). Top rank gets a certain number of points, the second rank gets fewer points, and so on down the line. Most points wins.<d-footnote>I once tried to describe Condorcet to a friend (who is very intelligent) and they immediately invented Borda on the spot. Clay Shentrup has found the same thing, including from people who live in San Francisco, a location that actually uses RCV. People who use RCV think they know how it works, but usually are horrified when they are actually told the truth.</d-footnote> Or perhaps they'll invent a weighted average system!
2. Vote transferring (RCV). Eliminate candidates and transfer votes.
3. Pairwise comparison (Condorcet). Maybe a clever voter might ask "what if we just compare each candidate head-to-head against every other candidate and see who wins the most matchups?"

I think this is a *big problem with ranked ballots*. It should, in my view, be explicitly clear and obvious what the system is going to do with your vote, and how it's going to be counted and tallied to determine the winner.

This is one thing I like about Approval: it's not hard to guess that a bubble is a vote. That's how choose-one voting works, and Approval works the same way. Hence, Better Choices' system uses that *same* interface to its advantage. I think the idea of head-to-head matchups becomes much more obvious.

This is also nice because this should make it much easier to implement on existing voting machines, which is something I really like about Approval! Tallying becomes exceptionally simple: it's just three different matchups (six total tallies) instead of one. That's not absurdly overcomplicated.

The only question that remains is if the voters will understand how these head-to-head matchups translate to a winner. Will they be confused and expect the one who wins any matchup by the most is crowned the winner? Or will they understand the Condorcet principle at play?

I am someone who is very concerned about reforms with a hostile ballot. As far as ballots go, this is an extremely friendly ballot, especially relative to RCV and STAR. But it is objectively more complex than a choose-one or Approval ballot. Therefore, it's entirely possible that *even this* system could be too complex for voters to find palatable<d-footnote>My mother found it too confusing, and that's a bad sign because she is a smart lady.</d-footnote>. I want rigorous and unbiased/independent usability studies before I jump on board the bandwagon. But if there's *any* way to make Condorcet methods work, it's probably this or nothing.

### So Much Better Than RCV

I wish it didn't *need* to be said, but it does. Compared to this, RCV is legitimately awful. The practical drawbacks of RCV are not as blatant with only three candidates (you only effectively need to keep track of nine tallies with three candidates<d-footnote>The number of bullet voters, and the six possible transfers: $A\to B$, $A\to C$, $B\to A$, etc.</d-footnote>), but we have seen RCV fail utterly in elections with three viable candidates, such as [Alaska and Burlington](../ditch-rcv/){:target="_blank"}.

If they had used this system instead, a number of major issues would have been prevented. For those who aren't anti-RCV-pilled yet, Condorcet is what Fairvote *tells you RCV is, but actually isn't*.

In this system, you get to vote for your favorite, but you also get to support your second choice against your least favorite. This is what RCV fails to do. Most voters *assume* ranking a second choice fortifies against their least favorite, but that's not how RCV works. It is, however, exactly what this system does when you vote for your second choice against your least favorite in that matchup.

The major RCV failures stemmed from nonviable candidates *not* getting eliminated. Specifically, candidates with fervent but thin support, who would lose in every head-to-head matchup, got more first-choice votes than the broad consensus option--whose support was more widely distributed in second choices--and hence were not eliminated. This left voters who ranked that nonviable candidate first holding the bag when their honest support eliminated their backup candidate, and their first choice was unable to win against their least favorite.

RCV *ignored* the data voters were clearly communicated through their second choice rankings: that they preferred the consensus option as a second choice to their least favorite. The system was too shortsighted--it only looked at these voters' first-choices<d-footnote>This is why Later No Harm is a joke criterion that nobody who understands social choice takes as anything close to "desirable". By protecting your first choice from your later choices, the system can't <em>save</em> your second choice if your first is nonviable. That's what happened in Burlington and Alaska. <a href="https://electowiki.org/wiki/Later-no-harm_criterion">Later No Harm is incompatible with No Favorite Betrayal</a>. If you want to protect your first choice from your second choice, you will often have to betray your honest first choice or else risk electing your last choice directly as a result of your honesty.</d-footnote>. The system proposed by Better Choices *explicitly* asks for this information, and uses it faithfully.

Instead of looking at the first-choice votes--which say nothing about how broadly acceptable or unpalatable a candidate is--this system looks at the head-to-head matchups. A metric which is easier to count, and is far more indicative of a strong candidate.

### Cognitive Simplicity

The choice of three is a very good move, I think. A two-candidate runoff is very nice because the race is very cognitively simple. You just pick who you like better, and it means you get more time to decide who you think is genuinely better. It's fully strategyproof (in the runoff step) <d-cite key="may1952simpleMajority"></d-cite>, and your vote absolutely counts.

With three candidates, it's only *slightly* worse in that respect, in my opinion. Three is not *too many*. Four is kind of pushing it. Three also means that voting in each matchup is entirely tractable! Asking voters directly "who do you prefer out of these two" is still a simple question. There's still potential strategic considerations but, at the moment, it seems very minimal.

I've been skeptical of runoffs in the past, due to potential strategy concerns <d-cite key="fishburnBrams1981runoff"></d-cite>. However, in practice, I've been convinced that Approval with a runoff in particular is quite robust, since it lets voters feel safer being more generous with their approvals than they might otherwise be. The runoff step also allows for a real choice to distinguish between the options for all voters, even if they didn't distinguish previously.

I've also shared many issues with Condorcet methods in past posts. However, I believe the restriction of the Condorcet mechanism to the runoff step, among 3 candidates, essentially quells all of my concerns. I've always *liked* Condorcet in the abstract, and this feels like the *right way to do it*.

### System Agreement

Further, when restricted to three candidates, minimax agrees with Ranked Pairs and Schulze<d-cite key="brandt2025condorcet"></d-cite>, which are top-shelf Condorcet methods. Ranked Pairs and Schulze are robust, but harder to explain. The fact that the very simple "least bad loss" system agrees with them is very satisfying to me.

### Pass-Fail Criteria

Condorcet does not, in general, satisfy the participation criterion. That is, participating in an election might end up giving you a *worse* outcome than if you had abstained. However, this *generally* only occurs with four or more candidates.

With three candidates (or at least the system being considered here), there are no participation failures. No monotonicity violation like in RCV either<d-footnote>This is not that surprising. Monotonicity is actually really hard to violate. Some call it a "free" property, because you need to define an absurdly convoluted system to break it. The fact any seriously considered system fails it is a wonder. Condorcet does not fail monotonicit, but it's worth mentioning it here.</d-footnote>. You also get reversal-symmetry<d-cite key="brandt2025condorcet"></d-cite>. Further, when outside of a cycle, the system will satisfy [IIA](../iia/){:target="_blank"}!

Minimax also [does not generally satisfy the Condorcet loser criterion](https://en.wikipedia.org/wiki/Condorcet_loser_criterion#Minimax), but *does* with three candidates<d-footnote>This is easily seen by case analysis (if a Condorcet loser exists among three candidates, then a Condorcet winner must also exist and would be elected instead) or the equivalence with Ranked Pairs/Schulze, which do satisfy the Condorcet loser criterion for any number of candidates.</d-footnote>.

Condorcet, in general, can fail some desirable criteria. In fact, minimax, in general, often fails a number of nice properties. But minimax is actually quite robust in the three candidate case, because it's essentially a shortcut for more robust methods like Ranked Pairs and Schulze. This system essentially funnels down Condorcet into the scenario where it really shines.

### Strategy Is Minimal

(in the runoff step)

In practice, voting in this system is pretty straightforward. If you have a favorite, you vote for them in both their matchups. Then you can *also* vote for your second choice against your third choice. Easy-peasy.

No system is going to be strategyproof in general, but I think Condorcet methods like this are about as robust as you can get. I do not see any realistic case where a voter has serious incentive to lie on their ballot. Especially when there isn't a cycle. At worst, maybe the expected winner is your second choice, and so you "bury" them by voting for your least favorite over them in that matchup? But that requires helping your least favorite, which is risky.

The nice thing about minimax is that it's fairly robust to attempts to throw a cycle. If a Condorcet winner exists, then suppose a coalition purposefully buries them in their weakest matchup. If they are *somehow* able to do this in a way that creates a cycle, then most likely that weakest win of the Condorcet winner becomes the weakest loss of the whole election. Hence the winner is likely unchanged. The coalition would need to be coordinated and large enough to turn it into a strong loss.

I made [a simple model you can check out here](https://eigentaylor.github.io/weakest-link/graph.html) which shows how insincere deviations can affect the outcome of a Condorcet election if a coalition is able to coordinate and change the relative size of the margins. Out of a total 48 state nodes, only 6 of them had *some* path to a profitable change. Only 2 of them had an adjacent node with a profitable change, and they were both in a cycle. The amount of work, coordination, and *foresight* required would let me sleep soundly at night telling laypeople there's effectively no reason to ever lie in a system using this method.

{% proof Strategy details %}
My model is a bit tricky to explain, but the basic idea is that the election is decided entirely by the relative sizes of the margins in each matchup. For example, if Alice beats Bob by 10 votes, Bob beats Clark by 5 votes, and Clark beats Alice by 1 vote, then we can describe that via

$$(A>B) > (B>C) > (C>A)$$

where the ">" indicates the relative size of the margins. In this case, Alice's win over Bob is the largest margin, Bob's win over Clark is the second largest margin, and Clark's win over Alice is the smallest margin. Hence, Alice wins through the minimax tiebreaker.

My model is a graph of all $3!\cdot 2^3=48$ possible configurations of the relative margins, and edges between them represent deviations by a coalition of voters who sincerely vote for $A$ over $B$, $B$ over $C$, and $C$ over $A$, but then insincerely deviate in some say. For example, if the coalition insincerely votes for $C$ over $B$, then this scenario has an edge to the scenario

$$(A>B) > (C>A) > (B>C)$$

because a sufficient coalition of voters doing this deviation could only *possibly* change the outcome by changing the relative size of the margins. In this case, by voting for $C$ over $B$, the coalition has changed the least bad loss from Clark's win over Alice to Bob's win over Clark, and hence Clark now wins through the minimax tiebreaker. This is an *unprofitable* deviation, because the coalition has elected their worst candidate, Clark instead of their best candidate, Alice.

If you are interested, you can use the playground below to see the profitable strategies in action. Suppose you are a voter who most prefers Alice, then Bob, then Clark. Then insincere voting would involve moving any of the sliders to the left.

<iframe id="condorcet-election-frame" src="/assets/html/condorcet-election.html?strategy"
  width="100%" height="480" scrolling="yes"
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

The following two scenarios are the [only cases](https://eigentaylor.github.io/weakest-link/graph.html) where you might have an incentive to vote insincerely:

1. **Bob Burial**: If we have a cycle where Alice beats Clark by the largest margin, Bob beats Alice by the second largest margin, and Clark beats Bob by the smallest margin, then Bob wins through the tiebreaker. If you bury Bob in his matchup against Clark (move the bottom slider to the left, representing many voters insincerely changing their vote from Bob over Clark to Clark over Bob), until Alice's loss to Bob is the smallest margin, then Alice wins. This is a profitable deviation for you, but it requires a *very* specific cycle to occur.
2. **Alice Betrayal**: If we have a cycle where Clark beats Alice by the largest margin, Alice beats Bob by the second largest margin, and Bob beats Clark by the smallest margin, then Clark wins through the tiebreaker. If you bury Alice in her matchup against Bob (move the top slider to the left, representing many voters insincerely changing their vote from Alice over Bob to Bob over Alice), until Bob's loss to Alice is the smallest margin, then Bob wins.

These scenarios are absurdly unlikely to both occur and be predicted, since cycles are so empirically rare. Further, you would both need to be confident in the relative margins of the matchups, and be able to coordinate with other voters to actually *change* the order of the margins. This is a lot of work, and requires a lot of coordination and foresight. In practice, I do not see this as a realistic concern.
{% endproof %}

Condorcet methods, particularly minimax/ranked pairs, are just remarkably robust in practice, especially to coordinated manipulation. As far as voting systems go, this is probably the most honest system you can get, and that's genuinely nice.

### It Fits the Condorcet Ideal

I wrote in [a very cheeky past post](../condorcet-approval/){:target="_blank"} about how ranked Condorcet methods are a mere approximation of who would win in every matchup. *Runoff dominance* is what I see as the Condorcet ideal (though Condorcet himself may not necessarily agree). I actually mentioned in that post that you would need voters to vote in every matchup to truly claim you elected the Condorcet winner. Turns out there's now a system that does precisely this! I think that's cool.

### You Can Vote Intransitively

This is just funny. If you are feeling cheeky, you have full freedom to say "I prefer Alice to Bob, I prefer Bob to Clark, and I prefer Clark to Alice". You can't do this in a ranked method!

Why would you do this? If you have a favorite, why would you vote against them? Well, this is America. You can do whatever you gosh darn please. *Maybe* being intransitive floats your boat. I won't judge. Or maybe you're just being silly.

## Where I'm Skeptical

As I said before, my biggest issue is the choose-one primary. If this system uses the choose-one primary, we will still be plagued by vote-splitting and spoilers, with no [nursery effect for broadly acceptable candidates](../ca-top-2/){:target="_blank"} (see this post for more details on all my issues with a choose-one jungle).

Just increasing the number of candidates you take won't change the fundamental dynamics. Instead of the race being between *three* serious candidates and plagued by spoilers (as we have seen in the top 2 system), we will likely see the race expand to four serious candidates--split among the various internal factions of the two major parties--and likely even more spoilers <d-cite key="cox1994sntv"></d-cite>.

This is just what a choose-one multi-winner election with $M$ seats *does*. You get a Duvergerian abandonment of anyone outside of the top $M+1$ candidates, as strategic voters concentrate their support on the leading candidates to avoid wasting their votes. More candidates will run, there will be more spoilers and confusion, and the election will still be chaotic, strategic, and partisan, as voters rally behind the most established major party candidates who are perceived as the safest choices.

The only thing that will be fixed is the lockout problem. But, diversity does not necessarily equal a competitive election (in fact, it can cause the opposite). And I much prefer a competitive election with a real choice than a foregone conclusion full of diversity.

The issue with jungle primaries *is not that the runoff is between two candidates*. The issue is the vote splitting! Any proposal which does not fix this does not have my endorsement.

If, instead, Better Choices were to use Approval voting in the first round, then I think this could be one of (if not *the*) most robust systems currently in conversation. *Seriously*.

[Cursory VSE simulations](https://eigentaylor.github.io/satisficing-voter-sim/) in my model of epistemic noise and ballot fatigue have been very favorable to this system. I may have to correct this paragraph of the post later, but Approval Top-3 Condorcet (AT3C) is potentially the most robust system by far, if we assume no epistemic noise in the runoff election. Comparing Approval Top-2 (AT2) with Plurality Top-3 Condorcet (PT3C), they are quite competitive, and perform better in different situations. AT2 is much more robust to a crowded field, however. That said, I'm not yet confident enough in the code I have to make definitive claims, and further testing and validation are needed before drawing firm conclusions. But the evidence thus far seems to put the ranking of AT3C over AT2 over PT3C, in a holistic sense.

My other major concern is the Condorcet cycle. What happens when a cycle necessarily occurs. Unlike a top-2 election where the only tie is a literal split in the vote, a sort of "tie" in this method would involve all candidates winning and losing exactly one matchup. When the tiebreaker is used, will voters accept that result? Or will it undermine the legitimacy of the election? The empirical rarity of cycles does not fully reassure me that if such an event occurred, it wouldn't be as catastrophic to the system as [Burlington 2009 or Alaska 2022 were to RCV](../ditch-rcv/){:target="_blank"}.

## Conclusion

This system has potential, but only if it addresses the fundamental issue of vote splitting in the primary by using Approval voting. Without this change, I believe the system is going to be a downgrade from any system that uses Approval in the process. That is, going to Approval Top-2 instead would be a much stronger improvement than *only* changing the runoff step.<d-footnote>Is it a step in the right direction? I'm skeptical. I think if we do this and leave the primary as a choose-one election, the fundamental issue of vote splitting delivering poor outcomes will remain, one more slot or not. And, with more slots means more candidates running, which may exacerbate the issues with the primary even more. I firmly require the jungle primary to be held under Approval, or else I think the system will fail to address the core problem effectively (and potentially delay meaningful reform which could fix the fundamental issue of vote splitting). That is, my foremost concern is the opportunity cost of not patching the primary election when that seems like the most pressing issue.</d-footnote>

What remains to be seen for me is

1. Will Better Choices see the necessity of implementing Approval voting in the first round to address the vote-splitting issue?
2. Will this proposal actually *play* to voters. Will voters vote "yes" if it's on the ballot? Will they like it enough to keep it around if it passes? Will politicians support and push for it, without it becoming a partisan disaster like RCV has been? Are there unbiased usability studies that show voters can understand the ballot and the system?
3. Will this system be able to weather Condorcet cycles in a way that maintains voter confidence and legitimacy?

As I've said before, basically all "good" voting methods<d-footnote>Primarily, Approval, Condorcet, and STAR voting. RCV is a noticeable downgrade from these systems.</d-footnote> are going to agree most of the time, and will largely all defuse polarization and encourage more representative candidates. With that in mind, I think the most practical and voter-friendly system is very likely the best one. I think Approval Top-2 is tested, excellent, and one of the most voter-friendly systems. But I could see an argument that by taking in one more candidate from the Approval jungle (which would reduce the number of lockouts), this slightly more expressive--but still grounded and digestible--general election ballot could make a more *palatable* reform that people can get excited about.

At the moment, Approval Top-2 seems like a much safer system to back. The fact that it's *already* being used in St. Louis <d-cite key="sargent2025stlouis"></d-cite> is a fantastic thing to be able to point to, advocacy-wise.

However, I *do* genuinely like this system. I hope that Better Choices decides to go with Approval voting in the first round, and then I would consider this a top-tier method (should it prove politically viable). I am absolutely keeping my eye on this.
