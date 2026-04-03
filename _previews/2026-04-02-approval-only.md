---
layout: distill
title: Why I Currently Only Support Approval
date: 2026-04-02
description: Opinion piece about my thoughts on other systems like STAR, RCV, and Condorcet.
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
published: false
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

I would say I am still rather new to the Electoral reform space. I've tried my best to catch up, read papers, and write about what I've found. When I first started writing about Approval voting, I initially said something along the lines that "anything is better than First-Past-The-Post," which is a common sentiment among those new to the field. In particular, I supported Ranked Choice Voting (RCV) at the time, because it seemed like a clear improvement over FPTP. See [this post](../ditch-rcv){:target="_blank"} where I realized the error of my ways.

At this point now, I am quite convinced that Approval voting is the most practical fix for our democracy. In this post, I want to explain my personal philosophy and most important criteria for evaluating electoral systems, and why Approval voting is the only option that checks all the boxes.

I am open to considering other systems in the future. If we get significant polarization diffusion, and greater trust from voters to use a more complex system like STAR or Condorcet methods, then I am open to revisiting those options as viable alternatives. But in this current moment, I can only say that I support "Approval today, [insert your preferred system for the future here] tomorrow." So long as that system is not RCV, however. Approval voting, I think, truly needs to be the bridge.

## The Taylor Criteria

These are the criteria that I personally see as the absolute most important when evaluating electoral systems in our current moment in the United States.

1. Practicality: The system must be simple enough that it can be implemented and understood by the general public in a transparent and trustworthy way. If voters cannot easily understand how their votes translate into outcomes, or why their candidate won or lost, then I believe that system is a non-starter.
2. Legitimacy: The system must produce outcomes that the electorate can view as legitimate. If voters can point to the cast ballots and claim their losing candidate *should* have won for whatever reason, then I do not believe that system will stand up to scrutiny or maintain public trust in the democratic process when the stakes are high.
3. Outcomes and the end of Vote Splitting: The main issue with Choose-one voting is vote splitting. This is what generally causes issues with voting system outcomes. We need a system that breaks that problem by allowing voters to simultaneously support multiple candidates, and leads to excellent outcomes.

One might wonder where "Expressiveness" fits into this framework. After all, don't we need to be able to tell the ballot all of our hopes and dreams about how much we like each of the candidates? Well, I would argue... no. Simply, no.

I value the outcomes of a system far more than the depth of the ballot. If a less expressive ballot leads to better outcomes which are more legitimate and more practical to count, then I am eager to sacrifice expressiveness in order to achieve those ends.

In particular, I argue that expression comes at *direct cost* to legitimacy in particular. And in an era of distrust in elections and institutions, I think legitimacy is the single most important attribute a system can have. "Stop the steal" happened in a system as *simple and transparent* as choose-one voting. But that movement is hard to really sustain on claims of "bamboo ballots" when we have precinct level results that can be directly audited and verified against the cast ballots.

When I think about the concrete reality of implementing a voting system, I try to think "How would bad faith actors try to subvert this system?" How much room is there for a skeptical voter to feel that they were truly robbed. If the answer is "a lot", then I will withhold my support for that system until I am sufficiently convinced that it is robust enough to withstand those attacks.

What I am not saying is that this must be true forever. But in an era where [RCV is currently imploding and losing public trust](../ditch-rcv/){:target="_blank"}, I think we who wish for electoral reform need to back our horses *carefully*. We might only get one chance, and if we back the wrong system *again*, I think it might set back the cause of electoral reform for a generation or more.

## Practicality

Now, I think both Approval and Choose-one voting are the ultimately practical systems. There is simply no beating the fact that all you need to count is the total check marks each candidate gets. No need for pairwise tallies, no complicated elimination rounds, no runoff rounds, no multi-stage tabulations. You literally just add up the marks and whoever has the most wins.

That is as simple as it gets, and that simplicity is a huge part of why I think Approval is the right bridge system for the current moment. The ballot is exactly, or almost exactly, the same as a Choose-one ballot, with the only difference being that instead of marking a single candidate, you can mark as many as you approve of. That minimal change keeps the system extremely practical while solving the vote-splitting problem that plagues Choose-one voting. It also works on our existent machines with only a minor code change. It's also even harder to spoil a ballot. Approval wins here, hands down.

STAR and Condorcet are... fine. Better than RCV, certainly. There is no central tabulation, and both are precinct summable. But their tabulation practicality grows significantly as the number of candidates increases. With 19 candidates, as there were in Portland's 2024 mayoral race, here are the numbers each precinct would need to count (for FULL precinct decentralization, and no central aggregation) in order to fully tabulate the results:

| System     | Tally Complexity per Precinct | Number with 19 Candidates |
|------------|-------------------------------|---------------------------|
| Choose-one | $n$                           | 19                        |
| Approval   | $n$                           | 19                        |
| Condorcet  | $n \cdot (n-1)\sim O(n^2)$    | 342                       |
| STAR       | $n^2\sim O(n^2)$              | 361                       |
| RCV        | $O(n!)$                       | 330,665,665,962,403,999   |

Optimizations could be made to cut the numbers for STAR and Condorcet tabulations by about a half. But RCV is absurdly impractical in this regard. In the actual Portland election, voters were restricted to ranking up to 6 candidates, which brings the number down to just... 21,029,599...

$$21,029,599=\sum_{k=1}^{6} \frac{19!}{(19-k)!} $$

$$\sum_{k=1}^{19} \frac{19!}{(19-k)!} = \text{floor}(e \cdot 19!) $$

Which gives us that lovely astronomical number of possible rankings that the RCV tabulation would need to consider if voters were allowed to rank all 19 candidates. Indeed, the number of actual cast ballots would be a small subset of that number, but there is no way that a single precinct could realistically enumerate and tally all of those possibilities. Central tabulation is vital under RCV.

When compared to RCV, Condorcet and STAR really do not look so bad. But both Approval and Plurality are the kings of the category.

| System     | Practicality |
|------------|--------------|
| Choose-one | Best         |
| Approval   | Best         |
| Condorcet  | Moderate     |
| STAR       | Moderate     |
| RCV        | Awful        |

We can also talk about practicality in terms of how easy it is for a voter to use. However, I would argue that wouldn't really change my placement of these systems. STAR an Condorcet both use more complex ballots. While the Ranked ballot has been studied for hundreds of years, and the literature on Approval is quite extensive, STAR is still quite young and untested. I am not convinced that STAR is so much simpler than a Ranked ballot to make it meaningfully better than Condorcet.

## Legitimacy

I think that legitimacy is one of the most important criteria for evaluating a voting system for me. I don't think it appeals that much to many others in the space, but I am fine standing alone (perhaps also with the Condorcetists).

Some recent posts by me have entered more into the Condorcet method space. I discussed seriously how [Approval is a "linear approximation of a Condorcet method"](../practicalapproval) more seriously, and then approached the topic with a more humorous tone in my [April Fools post where I explain that Approval is effectively the "perfect Condorcet method"](../approval-condorcet){:target="_blank"}.

My primary point is that I am in two minds about the Condorcet criterion. On the one hand, I find no reason that the underlying ranked Condorcet winner is truly the best candidate to govern. On the other hand, if you elect a candidate whom the ballots indicate would lose a head-to-head matchup against some other candidate, then that is a clear legitimacy problem: a majority of voters can point directly to the ballots and say "we prefer this other candidate to the one you elected," and that is a hard argument for the electorate to ignore. That's what happened in Alaska and Burlington under Ranked Choice.

I have argued extensively [against RCV specifically](../ditch-rcv){:target="_blank"} and [in reference to the Condorcet criterion in general](../condorcet-approval){:target="_blank"} that if you do not elect the Condorcet winner when you give voters a ranked ballot, you are not respecting the data you were given, and blatantly ignoring the expressed preferences of the electorate. And even when it's a [cardinal ballot](../consistentcardinal){:target="_blank"}, if the system can indicate that some candidate might beat the winner in a head-to-head matchup and yet still elect someone else, that is a legitimacy problem in the same sense: the electorate can point directly to the ballots and say "the data shows this other candidate would win head-to-head against the winner," and that is hard to ignore.

In those posts, I have been clear that Approval gives full and complete legitimacy to the winner in every election with a single winner. You can't prove it's *not* Condorcet.

I would even go as far to say that the fact that a Condorcet method has cycles actually makes it *less legitimate* than Approval. Because when a Condorcet winner does not exist, you still have to make a choice about which candidate to elect, knowing that any choice will allow some (simple) majority of voters to say they wanted someone else more.

Without rehashing everything from those previous posts, I think RCV completely fails in giving its winners legitimacy. And I fear for a Condorcet method when it inevitably encounters a cycle: at which point you must choose an arbitrary tie-breaking rule which can't fix the fundamental legitimacy problem that a majority of voters can point to the ballots and say "we prefer someone else to the candidate you elected," and that is impossible to paper over with any tie-breaking convention.

But you also get general problems with ranked ballots beyond cycles. "My candidate won the first place votes! If we were using the old system, they would have won!" is a common refrain from voters who see their top choice eliminated early in an RCV election. And regardless of whether or not that's *convincing*, the fact remains that the system has opened the door for those criticisms.

And let's not forget about STAR. STAR, I think, has the potential to be worse than Condorcet in this regard. In my [post about internal consistency](../consistentcardinal){:target="_blank"}, I showed that STAR can create a three-way legitimacy crisis where an apparent Condorcet winner, and the candidate with the most total stars, both lose. If you have a candidate saying "I was preferred over everyone else by a majority, but the others exaggerated and their votes counted more!" and another candidate saying "I got the most stars! The runoff is pointless and it was rigged against me!" and the actual winner just shrugging because they won by the rules, then that's not exactly an outcome I would imagine everyone being particularly happy with.

## The Condorcet Criterion

Some recent posts have entered more into the Condorcet method space. I discussed seriously how [Approval is a "linear approximation of a Condorcet method"](../practicalapproval) more seriously, and then approached the topic with a more humorous tone in my [April Fools post where I explain that Approval is effectively the "perfect Condorcet method"](../approval-condorcet){:target="_blank"}.

In short, I do think there's strong evidence that Approval voting is, for all intents and purposes, the idealized realization of a Condorcet method in essentially all ways except for one thing: expressiveness.

The Condorcet ideal inherently assumes full rankings, and then the system to satisfy the Condorcet criterion must treat that data faithfully and output the Condorcet winner, assuming one exists. The key phrase being "assuming one exists". I argue that a cycle is just as much a trust-breaking failure mode as an RCV Condorcet failure. Because no matter who you elect, if they are not a Condorcet winner, then a majority can point directly to the ballots and demonstrate that a majority prefers some other candidate to the winner, which undermines the legitimacy of the outcome.

Approval voting, by contrast, as I initially proved in [this post](../consistentcardinal){:target="_blank"}, gives an unassailable guarantee of legitimacy to the winner. By viewing Approval as a two-tiered Condorcet method, we can prove that Approval is basically a 100% Condorcet efficient method: it never admits a cycle, and the winner is always the Condorcet winner induced by the ballots. This is a powerful result, but comes with two big caveats.

First, this legitimacy guarantee comes at the cost of expression. While many, like myself, are entirely happy with a simple system that won't ever use my ballot to elect someone I didn't vote for, Approval does not allow voters to express nuanced preferences between candidates beyond a binary approve/disapprove. The Condorcet efficiency comes because the simplified ballots collapse all of the nuanced preference information into a binary signal, which trivially induces a Condorcet winner which Approval will elect. But the Condorcet winner, based on underlying preferences, can easily lose an Approval election [as I showed in this post](../condorcet-approval){:target="_blank"}.

I explained in that post that my loyalty to the Condorcet criterion is not the same way a true Condorcetist like the esteemed Robert Bristow Johnson would be. I don't believe the ranked Condorcet winner actually makes the electorate optimally happy. But if your system can indicate in the ballots that candidate $C$ *would* beat the candidate you elected in a head-to-head matchup, and *especially if they would beat ALL other candidates in head-to-head matchups*, then that is a serious legitimacy problem.

Approval works, then, because it's perfectly "ballot Condorcet consistent", even if it doesn't always elect the true Condorcet winner based on the full underlying rankings. And in that respect, it's perfect for me because it thus guarantees the Approval winner full legitimacy, without being beholden to a milquetoast Condorcet winner who only wins by the narrowest of margins based on very weak ordinal preferences. Take the example I provided in [the Condorcet vs Approval post](../condorcet-approval){:target="_blank"}:

| Voters | A Utility | B Utility | C Utility | True Ranking | Approvals |
|--------|-----------|-----------|-----------|--------------|-----------|
| 45     | 1         | 0.3       | 0         |  $A > B > C$ | $A$       |
| 35     | 0.9       | 1         | 0         |  $B > A > C$ | $B, A$    |
| 20     | 0         | 0.1       | 1         |  $C > B > A$ | $C$       |

In this example, candidate $A$, who we can call Alice, wins the election with an unprecedented 80% Approval share. She makes 80% of the electorate at least 90% happy. Compare this to the true Condorcet winner, $B$ob, who would make 65% of the electorate at *most* 30% happy. Alice is the utility maximizer here, and leaves the largest amount of voters "happy". The $C$lark supporters weren't really going to be happy with either of the viable candidates.

Like I said in that post, I don't generally find utility arguments particularly persuasive. But I think this illustrates the point. Outside of the 45% Alice loyalist group, the remaining 55% of voters feel extremely similar about both Alice and Bob, with only a slight 10% utility difference. For this reason, they chose not to distinguish between the two when casting their Approval ballots, approving both or neither of them.

This *looks* like a pathology because we know the underlying preferences. And I defend it by pretending we know the underlying honest utilities. But consider what each of these voters actually see on election night.

| Candidate | Approval Share |
|-----------|----------------|
| $A$       | 80%            |
| $B$       | 35%            |
| $C$       | 20%            |

And perhaps, maybe they'll see that 100% of the $B$ supporters also approved $A$. From an objective standpoint, this is an absurdly strong mandate for Alice: not only did she win a commanding 80% of the electorate's approval, but every voter who supported her closest competitor also found her acceptable enough to approve. This is the kind of cross-cutting support that gives a winner undeniable legitimacy in the eyes of the electorate, even if the underlying ordinal preferences suggest a different Condorcet winner. The "vibe" that a silent majority actually preferred a milquetoast candidate like Bob over Alice might be talked about on message boards or twitter, but could never be substantiated based on the election results.

Maybe the Clark supporters will think "maybe I should have approved my lesser-evil", but the 45% gap between Alice and Bob is so large that it's hard to really imagine that a few additional approvals from the $C$ bloc would have made any meaningful difference in the outcome. And given how similarly they view both candidates, would that seriously be a huge upgrade?

If the Clark and the Bob supporters had coordinated, and realized that they both preferred Bob to Alice, they *could* have strategically approved Bob and withheld approval from Alice in order to swing the election in Bob's favor. And since Bob was the Condorcet winner, that is absolutely possible. A true strong Nash equilibrium in Approval can only elect a Condorcet winner. But nobody *has* that data in real life.

