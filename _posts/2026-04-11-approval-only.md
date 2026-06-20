---
layout: distill
title: Why I Currently Only Support Approval
date: 2026-04-11
description: Why Approval voting is the only system I trust to push for right now.
giscus_comments: true
importance: 1
tags: voting
category: polisci
featured: true
preview_redirect: true
related_posts: true
theorems: false
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
      - name: The State of the Reform Movement
  - name: The Bridge Criteria
  - name: Legitimacy
  - name: Practicality
  - name: Outcomes
    subsections:
      - name: Vote Splitting and Participation Failures
      - name: Voter Satisfaction Efficiency
      - name: Expressiveness
  - name: Conclusion
---

## Introduction

EDIT (4/28/2026): Adjusted the STAR examples into a single example, and added a bit more explanation.

EDIT: (6/19/2026): Thank you to Clay Shentrup and Sarah Wolk for their detailed feedback, from which I have made some minor adjustments.

I would say I am still rather new to the electoral reform space. I've tried my best to catch up, read papers, and write about what I've found. When I first started writing about Approval voting, I initially said something along the lines of "anything is better than what we have now," which is a common sentiment among those new to the field. In particular, I also supported Ranked Choice Voting (RCV) alongside Approval at the time, because both seemed like a clear improvement over Choose-one. See [this post](../ditch-rcv){:target="_blank"} where I realized the error of my ways.

As a mathematician, I have a soft spot for theoretical perfection. But I also love exceptional approximations that are simple and practical. I have found that if a simple model can capture the vital essence of a complex phenomenon with high fidelity, then adding complexity does not often yield significantly more accurate results. In fact, it can often lead to worse results due to overfitting, noise, and the introduction of new failure modes. This is a common theme in many areas of mathematics and science, and I find it applies just as well to electoral systems.

Approval voting is the simplest possible electoral reform. It is a minimal extension of the existing system, where you can approve of as many candidates as you like instead of just one. That simplicity is deceptive, and led to me initially dismissing it entirely in favor of something more complex. How could such a complicated problem as Democracy be solved by just allowing people to check more boxes? My skepticism eventually gave way once I read the [seminal 1978 paper by Brams and Fishburn](https://doi.org/10.2307/1955105) on Approval voting <d-cite key="bramsFishburn1978approval"></d-cite>. I realized that sometimes, the simplest answer is genuinely the best one. By removing all restrictions on voters' ability to express support for multiple candidates, Approval voting is the only system that lets your ballot truly mean what it says, without putting the voter at risk.

At this point, I am fully convinced that Approval voting is the most practical fix for our democracy. In this post, I want to explain my personal philosophy and most important criteria for evaluating electoral systems, and why Approval voting is the only option that checks all the boxes. This is a snapshot in time of my current thoughts as of approximately April 2026. I am open to changing my mind, and will happily update this post if that happens (as I have done before). And if you aren't convinced by my reasons and the criteria that I value, that's fine. But my framework is grounded in pure practicality and in our common goal of permanently ending Choose-one voting.

### The State of the Reform Movement

We are in a critical moment right now. RCV is facing wide backlash and is now banned in [19 states](https://ballotpedia.org/Ranked-choice_voting_(RCV)) across the country (and has been rejected by voters in ballot propositions in red *and* blue states). The ["Make Elections Great Again Act"](https://ivn.us/posts/11-ways-mega-act-congress-tries-control-how-you-vote-2026-02-06) is currently accumulating sponsors and would ban *any voting system except Choose-one*, despite being framed specifically to target RCV. Other systems are being brought into the crossfire, and voters are increasingly skeptical of electoral reform. We might have *one* chance to pivot.

If we make the wrong move now and rally behind a system that is too complex, too new, or insufficiently tested, and the voters reject it, then we may lose the opportunity to make meaningful electoral reform progress in the near future. The political capital and public trust required to push through reform are finite and waning. Let's not squander them on a system that may fail to gain public trust when we have a tested, simple, and provably legitimate option right in front of us: Approval voting.

I am open to considering other systems in the future. If we get significant polarization diffusion and greater trust from voters to use a more complex system like STAR or Condorcet methods, then I would be glad to revisit those options as viable alternatives. But in this current moment, I can only say that I support "Approval today, [insert your preferred system] tomorrow." Approval voting, I think, truly needs to be the bridge--the new baseline from which we can *then* discuss whether we want or need something supposedly "better".

## The Bridge Criteria

The Equal Vote Coalition ~~champions~~ supports three systems: Approval, STAR, and Ranked Robin (AKA Condorcet)<d-footnote>Sarah Wolk specifically corrected me on this: Equal Vote only "champions" STAR, and merely "approves" of Approval and Condorcet. This is precisely the kind of thing that I worry about. Flying too close to the sun and pushing STAR when Approval could succeed would be disastrous.</d-footnote>. I, however, currently only champion one of those: Approval voting. This is not a decision I come to lightly, but rather based on what I've read in the literature, my assessment of the current political and social context in the United States, and the practical realities of what implementation involves. Based on the criteria that I feel are most important, only one system uniquely satisfies all of them.<d-footnote>Clay Shentrup has specifically highlighted that political viability should be a major consideration, which I largely agree with. There is not a lot of polling on how palatable these systems are to voters, unfortunately. However, I think the practical and logistical strengths of Approval make it unrivaled in some respects as a choice for administrators and politicians to consider.</d-footnote>

1. Legitimacy: The system must produce outcomes that the electorate can view as legitimate. If voters can point to the cast ballots and claim their losing candidate *should* have won for whatever reason, then I do not believe that system will stand up to scrutiny or maintain public trust in the democratic process when the stakes are high. And if voters cannot easily understand how their votes translate into outcomes, or why their candidate won or lost, then I believe that system is a non-starter in this political moment.
2. Practicality: The system must be simple enough that it can be implemented and understood by the general public in a transparent and trustworthy way. Voters must be able to easily understand how to fill out their ballots and how they will be counted, and election officials must be able to count them without introducing unnecessary complexity or opportunities for error.
3. Outcomes: We need a system that actually leads to *good* outcomes. Radical, I know. But the main issue that causes elections to fail is *vote splitting*. A good system allows voters to express support for multiple candidates, allowing strong consensus candidates to accumulate support and win, rather than polarizing and unrepresentative options that win because the majority was split.

One might wonder where "Expressiveness" fits into this framework. After all, don't we need to be able to tell the ballot all of our hopes and dreams? *Exactly* how much we like each of the candidates? Who is our 5th favorite and not our 6th? Well, I would argue... no.

At risk of sounding like I'm telling you to eat your vegetables before dessert, I value the outcomes of a system far more than the depth of the ballot. If a less expressive ballot leads to better outcomes that are more legitimate and more practical to count, as I think has been shown in the case of Approval versus RCV, then I am eager to sacrifice expressiveness in order to achieve those ends.

To steal a quote from a fellow [advocate of Approval voting](https://whelmedcitizen.substack.com),

> "Approval is not less expressive, it's more honest<d-footnote>By "honest", we mean that an approval means exactly what it says: if you approve a candidate, you are counted in their approval tally exactly as cast, with no reinterpretation or weighting. This contrasts with systems like RCV or STAR, where the meaning of your vote can be context-dependent and may be interpreted in a way that you did not intend. I intend to write a full post on this topic.</d-footnote>. RCV/STAR let you say more. Approval lets you mean what you say -- Approval is the only system where support is real. You don't have to choose like under Plurality. No rankings you don't mean. No scores you have to game." --Amanda Mahlendorf

Approval collects a simpler signal, but treats it with full fidelity: if a voter approves a candidate, that approval is counted exactly as cast, without any need for complex tabulation, weighting, or runoff logic. There is no ambiguity about what the voter meant, and no opportunity for the system to "reinterpret" the ballot in a way that could produce counterintuitive or seemingly unfair outcomes. The winner is the candidate who could convince the most voters to express that signal, from which there is no room for debate or reinterpretation: the ballots speak for themselves.

Additionally, I argue that expression comes at *direct cost* to legitimacy. The more data you have, the easier it is to spin it to show that some losing candidate *should* have won, based on a potentially flimsy but plausible-sounding excuse. And in an era of distrust in elections and institutions, I think legitimacy is the single most important attribute a system can have.

"Stop the steal" happened in a system as *simple and transparent* as Choose-one voting. But that movement is hard to really sustain on claims of "bamboo ballots" when we have precinct-level results that can be directly and easily audited and verified against the cast ballot records. *And yet*, there are a significant number of people who still believe the 2020 and 2024 presidential elections were stolen. Do we really think a more expressive ballot, or more preference data, is going to make people trust the system more? Or is it more likely that extra data is just going to give bad actors more ammunition to claim the election was stolen, and that the vote was rigged?

You cannot "spin" the fact that more people voted for one candidate than another without delving into the realm of pure fiction<d-footnote>One objection is that someone could claim that people secretly added bubbles in for a candidate after a voter submitted their vote. Most people I have talked to have said that strict chain of custody is sufficient to dispute this, but another solution is to have the ballot be "Yes/No" for each candidate. This makes it much harder to edit someone's ballot.</d-footnote>. You *can* explain to voters that their honest vote led to their worst outcome because of the complex tabulation rules of the system. You *can* explain to voters that their losing candidate was placed higher than the actual winner on more ballots than the reverse. You *can* explain that their losing candidate got more points than the eventual winner, but the runoff step gave them someone else. It's not too much further to convince them that the overcomplicated system is a ploy by the other party to steal the election.

Further, the more complex the system, the more susceptible it is to strange pathologies *such as* "you're telling me I would have gotten a better outcome if I had stayed home and *not* voted?" That's not a hypothetical edge case: that *has actually happened in real RCV elections*! And systems like STAR and Condorcet are susceptible to these kinds of counterintuitive outcomes as well, though less commonly. Evaluating systems strictly on pass/fail criteria is not the way to go. *But*, if a system fails a significant number of *basic* properties, then that should give us serious pause before we throw all of our eggs into the basket of that system, when there's a much simpler and more robust alternative available in Approval voting.

What I am not saying is that this must be true forever. But in an era where [RCV is currently imploding and losing public trust](../ditch-rcv/){:target="_blank"}, I think we who wish for electoral reform need to back our horse *carefully*. We might only get one chance, and if we back the wrong system *again*, I think it might set back the cause of electoral reform for a generation or more.

My argument is simple: let us begin with the sturdy, stable, boring bridge that Approval voting *can provide today* away from Choose-one plurality. When the house is *no longer on fire*, we can start having a serious conversation about whether we want to move to something more complex like STAR or Condorcet methods.

## Legitimacy

I think that legitimacy is one of the most important criteria for evaluating a voting system. I don't think it appeals that much to many others in the space, but I am fine standing alone (perhaps also with the Condorcetists). And this is where I break with a lot of reformers: Choose-one voting has one of the strongest guarantees of legitimacy of any system out there. We forgo that legitimacy and simplicity at our peril.

If a candidate wins a plurality of votes, then there is no way for a majority of voters to point to the ballots and say "we prefer someone else to the winner." This is done through data destruction, absolutely. But when we're trying to fix the perceived problems with Choose-one voting by moving to a more complex system like RCV, STAR, or Condorcet, we have to be aware of what we *lose*. Forgetting the objective strengths of Choose-one voting and being too ready to disregard them entirely is, I think, a mistake that many reformers make: in trying to "fix" the system, we can create new problems.

Choose-one has these strengths, however, only because it is an arbitrary restriction on Approval voting. Choose-one is just Approval voting where you can only approve one candidate and get objectively worse outcomes. Approval uncaps that lack of expressiveness, without sacrificing the legitimacy and simplicity that make Choose-one so robust.

But Choose-one has the spoiler problem: when a third party gets more votes than there is a difference between the frontrunners, that casts a shadow over the results. Approval actually sidesteps this problem because those third party votes were cast by voters who could have also cast votes for a major party candidate at no cost to themselves. This actually gives more legitimacy to the winner in Approval than Choose-one. Allowing voters to express more support makes winning all the more meaningful, because the winner is the candidate who could convince the most voters to cast that support--from which there is no room for debate or reinterpretation: the ballots speak for themselves.

However, when legitimacy comes into the conversation, you *have* to mention Condorcet methods--methods that attempt to elect [the candidate who would beat every other candidate in a head-to-head matchup](../condorcet-approval){:target="_blank"}. I find that its importance lies less in it *needing* to be satisfied, and more in how it *cannot be violated*.

I am in two minds about the Condorcet criterion. On the one hand, I find no reason that the underlying ranked Condorcet winner is truly the best consensus compromise. On the other hand, if you elect a candidate whom the ballots indicate would lose a head-to-head matchup against some other candidate, then that is a clear legitimacy problem: a pairwise majority of voters can point directly to the ballots and say "more of us preferred this other candidate to the one you elected," and that is a hard argument for the electorate to ignore. That's what happened in [Alaska](https://ranked.vote/report/us/ak/2022/08/cd) and [Burlington](https://ranked.vote/report/us/vt/btv/2009/03/mayor) under Ranked Choice. And that led to voter-led repeal efforts<d-footnote>It was not technically the Condorcet failure itself in Alaska, as much as voter confusion and the system being overly complicated and insufficiently transparent. The repeal effort was also very partisan in motivation. In Burlington, the center-squeeze was a serious reason that contributed to the repeal effort, however. I maintain that Condorcet failures generally lead to results that feel "wrong". For example, electing a Democrat when nearly 60% of voters ranked a Republican first.</d-footnote>

I have argued extensively [against RCV specifically](../ditch-rcv){:target="_blank"} and [in reference to the Condorcet criterion in general](../condorcet-approval){:target="_blank"} that if we do not elect the Condorcet winner when you give voters a ranked ballot, you are not respecting the data we were given by the voters, and blatantly ignoring the expressed preferences of the electorate.

For example, I think of the Republican voters in Burlington and Alaska, under RCV, who ranked the Republican first and a moderate compromise second. In both cases, the voters expressed that they wanted a Republican over the eventual left-wing winner, and that they were willing to compromise with the moderate over that left-wing candidate. But by doing so, they caused the moderate to be eliminated, and then their favorite lost to the left-wing candidate in the final round. That data expressing compromise was *completely ignored by the system*, and those voters *directly elected their worst option*. That is a complete betrayal of the voters. And I find it not at all surprising that Republicans are skeptical of electoral reform after getting burned *twice*.

Approval fixes this issue in the simplest possible way: voters are allowed to express support for their favorite *and* a backup compromise simultaneously.

And even when it's a [cardinal ballot](../consistentcardinal){:target="_blank"}, if the system can indicate that some candidate might beat the winner in a head-to-head matchup and yet still elect someone else, that is a legitimacy problem in the same sense: the electorate can point directly to the ballots and say "the data shows this other candidate would win head-to-head against the winner," and that is hard to ignore.

In those posts, I have been clear that Approval gives complete legitimacy to the winner in every election with a single winner. When a critic of Approval tries to create an Approval pathology, it's always based on information that would *not* be visible if it were to occur in real life. When bad actors will do *anything* to try to convince their supporters the election was stolen, I am willing to champion that Approval's inability to be "proven" to fail in practice is a meaningful safeguard.

I would even go so far as to say that the fact that a Condorcet method has cycles actually makes it *less legitimate* than Approval. Because when a Condorcet winner does not exist, you still have to make a choice about which candidate to elect, knowing that any choice will allow some (pairwise) majority of voters to say they wanted someone else more. Since Approval never admits a cycle, [always elects the Condorcet winner based on the ballot data](../condorcet-approval){:target="_blank"}, I argue it's more Condorcet than Condorcet (so long as you value the legitimacy of the Condorcet criterion more than the need to be able to express a full ranked preference, as I do).

Without [rehashing everything from those previous posts](../ditch-rcv){:target="_blank"}, I think RCV completely fails in giving its winners legitimacy. And I fear for a Condorcet method when it inevitably encounters a cycle: at which point you must choose an arbitrary tie-breaking rule which can't fix the fundamental legitimacy problem that a majority of voters can point to the ballots and say "we prefer someone else to the candidate you elected." You can't paper that over with "oh but cycles are rare". That was the argument for RCV Condorcet failures and the center squeeze too. I don't care if a failure mode is "rare" if it's *catastrophic when it does occur*. That is why I am skeptical of Condorcet, and why I absolutely *do not trust RCV*.

And let's not forget about STAR. STAR, I think, has the potential to be worse than Condorcet in this regard. In my [post about internal consistency](../consistentcardinal){:target="_blank"}, I showed that STAR can create a three-way legitimacy crisis where an apparent Condorcet winner, and the candidate with the most total stars, both lose.

If you have the Condorcet winner, candidate A, saying "I was preferred over everyone else by a majority, but the others exaggerated and their votes counted more!" and another candidate C saying "I got the most stars! The runoff is pointless and it was rigged against me!" and the actual winner B just shrugging because they won by the rules, then that's not exactly an outcome I would imagine everyone being particularly happy with.

However, I think a much more concerning legitimacy problem with STAR is the possibility of participation failures. Here's an example of how a simultaneous participation and Condorcet failure could occur in STAR:

| Voters | $A$ Score | $B$ Score | $C$ Score | Ranking      |
|--------|-----------|-----------|-----------|--------------|
| 2      | 0         | 5         | 3         | $B > C > A$  |
| 3      | 0         | 1         | 5         | $C > B > A$  |
| 3      | 5         | 1         | 0         | $A > B > C$  |
| You    | 5         | 3         | 0         | $A > B > C$  |
| Totals | 15 or 20  | 16 or 19  | 21        |              |

You can verify in this example that you would be better off staying home. If you abstain, $B$ defeats $C$ in the runoff. If you vote, $C$ defeats $A$ in the runoff. Your vote would change the result from your genuine compromise, $B$, to your worst nightmare, $C$.

Now suppose the election results are in, and you are following the tally on election night. Your website of choice displays the full matrix of scores and pairwise percentages:

On the diagonal, we put the total scores for each candidate. Off-diagonal entries give the percent of voters who prefer the candidate in the row to the candidate in the column.

|       | $A$ | $B$ | $C$ |
|-------|-----|-----|-----|
| $A$   | 20  |44.4%|44.4%|
| $B$   |55.6%| 19  |66.7%|
| $C$   |55.6%|33.3%| 21  |

Reading it, you realize with horror that $A$ was completely nonviable. They would have lost to *anyone* in the runoff. Whereas $B$ would have defeated *anyone else* in a runoff, as the Condorcet winner, including your least favorite $C$. But $B$ got a lower score than the nonviable $A$.

If you had just stayed home, $B$ would have won and you would have gotten a candidate you scored a genuine 3 out of 5. But your vote pushed $A$ over the top, and now you got a candidate you scored a 0 out of 5. Despite clearly signaling that you would still prefer $B$ over $C$, your ballot was weaponized against you to change the outcome from $B$ to $C$. If $A$ was completely nonviable, why were they put into the runoff at all, over your viable backup $B$?

This data also gives $B$ supporters good reason to be upset. The numbers show a clear majority preference for $B$ over any other option, but $B$ still lost. The result is philosophically defensible, since $B$ was not able to amass strong enough support, but it is also extremely worrying. It becomes obvious that the $A$ supporters who would have preferred $B$ over $C$ were screwed over by the system.

STAR is just too new, and the literature is too sparse to convince me that this *isn't* a problem. We need more empirical evidence from real-world elections to really stress test the system, and I do *not* believe we have the time for that. All it takes is a *single* election like this to cause a huge blow to the legitimacy of the system, and I don't believe we'd get a third chance to try again with something else if that happens.

Approval, on the other hand, *has* been tested. The literature is deep and extensive, spanning decades of theoretical work, simulations, and real-world applications in organizations and cities in the United States. And we can *prove* that Approval guarantees full legitimacy at the ballot level.<d-footnote>This is in contrast to the claim by RCV advocates that RCV is also "battle-tested." It has certainly been 'tested', but I would not say that it has passed with anything close to flying colors. RCV has been a disaster in the US, and the academic literature is not kind to it.</d-footnote>

Why, then, should we gamble our second chance on a system like STAR, while the house is on fire, when Approval is right there?

| System     | Legitimacy Guarantee |
|------------|----------------------|
| Approval   | Great                |
| Choose-one | Great                |
| Condorcet  | Usually great        |
| STAR       | Unproven             |
| RCV        | Awful                |

## Practicality

Now, I think it's hard to argue that Approval and Choose-one voting are not the most practical systems to use in terms of tabulation. There is simply no beating the fact that all you need to count is the total check marks each candidate gets. No need for pairwise tallies, no complicated elimination rounds, no runoff rounds, and no multi-stage tabulations. You literally just add up the marks and whoever has the most wins.

That is as simple as it gets, and that simplicity is a huge part of why I think Approval is the correct next step system for the current moment. The ballot is exactly, or almost exactly, the same as a Choose-one ballot, with the only difference being that instead of marking a single candidate, you can mark as many as you approve of. That minimal change keeps the system extremely practical while solving the vote-splitting problem that plagues Choose-one voting. It also works on our existing machines with only a minor code change. It's even harder to spoil a ballot. Approval wins here, hands down.

STAR and Condorcet are... fine. Better than RCV, certainly. There is no central tabulation, and both are precinct summable. But their tabulation complexity grows significantly as the number of candidates increases. With 19 candidates, as there were in [Portland's 2024 mayoral race](https://en.wikipedia.org/wiki/2024_Portland,_Oregon,_mayoral_election), here are the numbers each precinct would need to count (for FULL precinct decentralization, and no central aggregation) in order to fully tabulate the results:

| System     | Tally Complexity per Precinct | Number with 19 Candidates |
|------------|-------------------------------|---------------------------|
| Choose-one | $n$                           | 19                        |
| Approval   | $n$                           | 19                        |
| Condorcet  | $n \cdot (n-1)\sim O(n^2)$    | 342                       |
| STAR       | $n^2\sim O(n^2)$              | 361                       |
| RCV        | $O(n!)$                       | $2.09 \times 10^{17}$     |

Optimizations could be made to cut the numbers for STAR and Condorcet tabulations by about a half. For example, counting the *margins* of each matchup, rather than the raw count in each, but the numbers are still substantial<d-footnote>However, after speaking to knowledgeable STAR and Condorcet advocates directly, they told me it is more important for transparency and trustworthiness to report the full raw counts for each pairwise tally, not just the margins. I have accordingly removed that optimization from this post. Further, the Condorcet reform that is gaining popularity would restrict the Condorcet step to three candidates, as a runoff step after a simple Choose-one election, which would only require 6 numbers for that Condorcet step, which is quite reasonable, even if the primary would still be plagued by vote-splitting.</d-footnote>.

Still, these systems are not even close to approaching how absurdly impractical RCV is in this regard. In the actual Portland election, voters were restricted to ranking up to 6 candidates, which brings the number down to just... 21,029,599... Hard to post all of those possibilities on the high school gymnasium doors for independent verification of the tabulation.

$$21,029,599=\sum_{k=1}^{6} \frac{19!}{(19-k)!} $$

$$\sum_{k=1}^{19-1} \frac{19!}{(19-k)!} = \text{floor}((e-1) \cdot 19!)-1 $$

Which gives us that lovely astronomical number of functionally distinct rankings that the RCV tabulation would need to consider if voters were allowed to rank all 19 candidates. Indeed, the number of actual cast ballots would be a small subset of that number, but there is no way that a single precinct could realistically enumerate and tally all of those possibilities. Central tabulation is absolutely necessary under RCV.

And central tabulation has **[big problems](https://oaklandside.org/2023/01/05/recount-for-real-county-supervisor-calls-for-an-independent-recount-of-oaklands-ranked-choice-elections/)** <d-cite key="bondGraham2023oaklandRecount"></d-cite>. The Oakland RCV case shows just how important precinct summability is for the legitimacy of the results. A mistakenly checked box caused counting errors that yielded the wrong winner and took four months and a lawsuit to resolve.

When compared to RCV, Condorcet and STAR really do not look so bad. But both Approval and Plurality are the kings of the category.

| System     | Practicality |
|------------|--------------|
| Choose-one | Best         |
| Approval   | Best         |
| Condorcet  | Moderate     |
| STAR       | Moderate     |
| RCV        | Awful        |

We can also talk about practicality in terms of how easy it is for a voter to use. However, I would argue that this wouldn't really change my placement of these systems. STAR and Condorcet both use more complex ballots. While the ranked ballot has been studied for hundreds of years, and the literature on Approval is quite extensive, STAR is still quite young and untested. I am not convinced that STAR is simple enough, relative to a ranked ballot, to be meaningfully easier than Condorcet for voters.<d-footnote>The Condorcet proposal by Better Choices is actually exceptionally simple and straightforward. Voters vote in all three head-to-head matchups for the 3 candidates that have advanced to the runoff step.</d-footnote>

But there *are* serious logistical concerns with ranked ballots beyond just central tabulation. [MIT](https://electionlab.mit.edu/articles/effect-ranked-choice-voting-maine) <d-cite key="mit2023maineRcv"></d-cite> found that RCV led to significant increases in time to fill out ballots, significantly lower levels of overall satisfaction with the voting process, and a marked decrease in confidence regarding the integrity of the election results. The data also showed a heightened perception among voters that the process was "slanted" against their specific political party. This was about RCV and not Condorcet, but I am personally worried about logistical concerns with voting systems that require voters to rank candidates.

## Outcomes

We still must consider the outcomes of these systems, however. A system that is perfectly legitimate and practical but produces terrible outcomes is not a good system. While I still think that legitimacy and practicality are more important concerns in this climate, our reform of choice must still produce better outcomes than Choose-one voting. Otherwise, why bother?

### Vote Splitting and Participation Failures

Vote splitting is something we're all familiar with. In a Choose-one election, your vote will only truly matter if you vote for one of the top two candidates. If you vote for a third-party or less popular candidate, your vote is effectively "wasted" in the sense that it cannot help your preferred major candidate win without also helping elect the candidate you like least. This is the classic spoiler problem that leads to strategic voting and the need to vote not for your favorite, but for the "lesser evil" among the frontrunners.

All proposed systems *claim* to solve this problem. But one system stands out in particular for completely failing to address it: Ranked Choice Voting.

On the surface, RCV seems to be a solution. Maybe not as good as some others, but is it actively worse than Choose-one? I would argue that it is.

The most immediate way to see that RCV fails to address vote splitting is to realize that your vote only supports a single candidate at any given time. You cannot fix Choose-one voting by just iterating elections where you can still only support one candidate. But it gets much worse than that.

[As I have previously argued](../ditch-rcv){:target="_blank"}, RCV actually makes the spoiler problem *worse* in an insidious way. Because the promise is that it eliminates vote splitting, when it actually *does not*. By pure luck, Republicans have gotten the short end of the stick twice.

Consider this example that illustrates what happened in Alaska. Imagine we have a polarizing minority candidate Alice, and a majority coalition that is split among Bob and Clark. Bob is seen as more moderate and centrist and is the clear second choice for both Alice and Clark supporters, while Clark is extremely polarizing and seen as fringe. However, the RCV advocates in this town have told the majority coalition that they can safely run two candidates without fear of splitting the vote, because RCV will ensure that if one of them can't win, the votes will transfer to the other. Let's see about that...

| Voters | Ranking     |
|--------|-------------|
| 39     | $A > B > C$ |
| 12     | $B > A > C$ |
| 18     | $B > C > A$ |
| 31     | $C > B > A$ |

In this scenario, Bob would actually be eliminated in the first round of RCV despite being the Condorcet winner (defeating both other candidates by huge margins of 69-31 against Clark and 61-39 against Alice)--only getting 30 votes while Clark would advance with 31 and Alice with 39. If just a single Clark voter had lied and ranked Bob first instead of Clark, or just two of these Clark voters caught the flu and stayed home, then Bob would have advanced instead of Clark *and won*. By voting sincerely for $C>B>A$, these voters elected Alice, their least favorite. This is called a *participation failure* (where you would have been better off staying home), and this is also an example of a *center squeeze*, one of the biggest pathologies of RCV.

That is not a solution to vote splitting. The Clark voters, and Clark himself, were essentially lied to. Voters were told that they could safely rank their favorite first, and if that favorite couldn't win then their votes would transfer. What they *weren't* told was the truth: if their favorite can't win, then ranking them first can cause their viable back-up to *lose* and directly elect their worst nightmare.

The insidious part is not that RCV gives worse outcomes than Choose-one; it's that it promises to fix problems it objectively hasn't fixed, and that leads to voters and candidates behaving in ways that the system cannot sustain, leading to worse outcomes. RCV only really works well when there are two serious candidates. Once you have three or more viable candidates, the system starts to break down and sincere voting can actually elect your least favorite candidate.

Participation failures can happen in RCV, STAR, and even Condorcet methods. It is *not* always safe to vote sincerely in these systems, as seen in the example provided above.

These failures are generally assumed to be much rarer in STAR and Condorcet than RCV, but only Approval (and Choose-one) completely avoid them: in Approval, voting sincerely can never hurt your preferred outcome, and your single vote can only ever help elect someone you *actually vote for*. Which sounds so obvious that it shouldn't even need to be stated, but it's not true for RCV, STAR, or Condorcet. This is one way in which complexity and expressiveness in a voting system can actually make it less safe to vote.

For all of the faults and issues with Choose-one voting, we have gotten pretty good at dealing with them. Voters are now conditioned to vote only for viable candidates. We have primaries to narrow the field so similar candidates don't split the vote, and candidates (often) drop out when they realize they have no chance. Choose-one isn't *good*, but it doesn't pretend to be. We know what to expect from it, even if our expectations are low.

RCV, on the other hand, pretends to solve all these problems, gives voters and candidates false promises that lead to similar poor outcomes, and then leaves voters disillusioned and rightly upset when they realize they were lied to. At least with Condorcet, we know the main failure mode is a cycle, which are (so far) empirically rare. But with STAR, I fear that we have no idea what the main failure modes look like in practice.

### Voter Satisfaction Efficiency

Approval, Condorcet, and STAR voting mitigate the vote splitting problem because support for multiple candidates is counted simultaneously. All three systems are quite robust [in simulations](https://electionscience.github.io/vse-sim/VSEbasic/) <d-cite key="quinn2017vseSummary"></d-cite>, and from those simulations we can get a sense of how well they perform in terms of outcomes. One way to measure this is through Voter Satisfaction Efficiency (VSE), which measures how well a system tends to pick winners that reflect the preferences of the voters.

Before we reveal the numbers, we should be clear that a voting system changes all aspects of elections, including who runs, who comes out to vote, and who is perceived as viable. But VSE attempts to give us the best way to compare, approximately, how well the true will of the voters is reflected in the outcomes. This gives a range that we can't compare directly between systems, but it does give us a sense of how robust a system is at producing outcomes that reflect the will of the electorate.<d-footnote>I am specifically using the numbers reported by Jamison Quinn, but there are a number of alternative models where Approval actually outperforms these more complex methods.</d-footnote>

```plotly
{
  "data": [
    {
      "x": [71, 86],
      "y": ["Choose-one", "Choose-one"],
      "mode": "lines+markers",
      "name": "Choose-one",
      "line": { "width": 5 },
      "marker": { "size": 12 }
    },
    {
      "x": [79, 92],
      "y": ["RCV", "RCV"],
      "mode": "lines+markers",
      "name": "RCV",
      "line": { "width": 5 },
      "marker": { "size": 12 }
    },
    {
      "x": [89, 95],
      "y": ["Approval", "Approval"],
      "mode": "lines+markers",
      "name": "Approval",
      "line": { "width": 5 },
      "marker": { "size": 12 }
    },
    {
      "x": [86, 98],
      "y": ["Condorcet", "Condorcet"],
      "mode": "lines+markers",
      "name": "Condorcet",
      "line": { "width": 5 },
      "marker": { "size": 12 }
    },
    {
      "x": [91, 98],
      "y": ["STAR", "STAR"],
      "mode": "lines+markers",
      "name": "STAR",
      "line": { "width": 5 },
      "marker": { "size": 12 }
    }
  ],
  "layout": {
    "title": { "text": "Voter Satisfaction Efficiency (VSE) Range by Voting System" },
    "xaxis": {
      "title": { "text": "VSE (%)" },
      "range": [65, 100],
      "ticksuffix": "%"
    },
    "yaxis": { "autorange": true },
    "showlegend": false,
    "height": 350,
    "margin": { "l": 100 }
  }
}
```

[Source](https://electionscience.github.io/vse-sim/VSEbasic/).

These numbers should be taken with a grain of salt, and they depend on strategy assumptions. It's hard to directly compare the percentages, but the range gives us a rough heuristic for evaluating approximately how any two systems stack up in terms of pure outcomes when we vary strategic behavior.

And this is where Choose-one completely fails. It may be shocking that its range overlaps so much with RCV, but the upper range for Choose-one is primarily when voters are all being strategic. While it *is* practical, and it gives the winner a (relatively) strong level of legitimacy, it simply fails to provide solid outcomes. This is why I don't think that Choose-one is something we should settle for.

RCV is a bit better than Choose-one, ranging from 79-92%, but it still tends to underperform compared to the other systems, while also being more complex, less legitimate, and a practical nightmare. I would consider it an actively harmful choice, even compared to sticking with Choose-one, based on the combination of these factors.

This is also where the arguments for STAR and Condorcet are at their strongest, I think. But also where Approval finally wins out clearly. STAR and Condorcet give excellent outcomes. They allow for expression and then treat that data *well*. STAR attempts to mitigate some general issues of strategy in expressive SCORE systems with the runoff step, and the Condorcet winner is *usually* a strong candidate.

But here's the thing: Approval is basically comparable. The difference between the VSE ranges in Approval and both STAR and Condorcet is quite negligible--particularly when compared to the difference in the ranges of Approval, STAR, and Condorcet to Choose-one's poor 71-86%. Approval's 89-95% range is quite close to STAR's 91-98% and Condorcet's 86-98%.

Further, Approval also comes with significantly better legitimacy and practicality guarantees. So I have to ask: why go for marginal VSE improvements when Approval has all the other benefits we have discussed?

I am simply not convinced that the marginal gains in outcomes from these more complex systems are worth the *risk* that comes from trying to convince voters and election officials to adopt a more complicated system that is harder to explain, harder to implement, and more prone to misunderstandings and potential crises of legitimacy.

In a [1998 paper by Regenwetter and Grofman](http://www.jstor.org/stable/2634612) <d-cite key="regenwetterGrofman1998approvalBordaCondorcet"></d-cite>, they found that Approval reliably picked the winners of Borda and Condorcet methods in experiments and real-world elections when the ordinal preferences could be reconstructed. In fact, they even say,

> "We find no evidence here that approval voting should be replaced by a more elaborate voting scheme." (p. 532)

And in the present moment, I have to say I think that is still the case. Anytime I hear someone advocate for STAR voting in particular, I hear the pitch and wonder "but... why not just use Approval?" I have to wonder if these alternate systems are, perhaps, overengineered solutions to problems that Approval would solve just fine--without the added complexity, risk, and potential voter confusion in the pursuit of only a small potential gain in outcome quality.

### Expressiveness

I can only assume the reasoning is something along the lines of "expressiveness": that these more expressive systems *feel* better to (some) voters than treating the candidates you like and don't like equally, and that they collect "better" information to help deliver better outcomes.

However, it's arguably a lot easier to say "yes, I would support this candidate" or "no, I do not want to support them" than to decide if a candidate is a 3/5 or a 4/5, or to decide who is their 5th and 6th favorite. By forcing voters who aren't deeply engaged in politics to make fine-grained distinctions between candidates they may not feel they know well enough to evaluate, these systems risk collecting noise rather than meaningful data. And not every voter is going to find that expressiveness appealing. For some, it may even be a turn-off.

In a few recent posts, I have mathematically proven that Approval is the [maximal level of ballot expressiveness that can be achieved whilst maintaining full legitimacy to the winner](../condorcet-approval){:target="_blank"}. Approval is essentially a two-tiered Condorcet method that avoids cycles, while any [scoring method with more than two tiers](../consistentcardinal){:target="_blank"} necessarily introduces the possibility of a Condorcet failure<d-footnote>By being a "two-tiered" Condorcet method, I mean that it is Condorcet-consistent based on the ballot data, rather than potential underlying preferences. The actual Approval data is unimpeachable. This is a property unique to Approval, and not true for any other cardinal method which allows more expression than a binary 0 or 1. This is particularly detrimental to STAR, since the pairwise data must be reported, putting such failures on full display.</d-footnote>. And, given that Approval still performs extremely well in terms of outcome quality--producing results that are very close to what more expressive systems like STAR or Condorcet would produce--it seems difficult to justify the added complexity of those systems in exchange for expressiveness that opens the door to legitimacy concerns that Approval neatly avoids.

This is not to say STAR would be *bad*. I genuinely don't know because it has seen such limited use in real elections and the literature is so sparse. From my perspective, I just do not understand the appeal of STAR over Approval in a *practical* sense. I am simply not yet convinced, and I remain skeptical of the failure modes.

## Conclusion

Approval voting offers a compelling combination of simplicity, practicality, and strong performance in terms of election outcomes. While more expressive systems like STAR or Condorcet may offer marginally better results in simulations, the added complexity, potential for voter confusion, failure modes, and implementation challenges make them a riskier choice for widespread adoption at this time. Approval voting, by contrast, is easy to implement and explain to voters, and already delivers outcomes that are very close to those of the more complex systems. For these reasons, it seems like the most sensible place to start in reforming our elections.

Approval voting is the only system I trust at this moment. It strikes the right balance between delivering strong election outcomes and maintaining the simplicity and legitimacy that are crucial for broad adoption and public trust in our electoral process.

The final scoreboard is as follows:

| System      | Legitimacy | Practicality | Outcome Quality | Risk of Backlash     |
|-------------|------------|--------------|-----------------|----------------------|
| Choose-one  | ✅         | ✅           | ❌              | N/A                  |
| Approval    | ✅         | ✅           | ✅              | Low                  |
| Condorcet   | ✅⚠️       | ⚠️           | ✅              | Medium               |
| STAR        | ⚠️         | ⚠️           | ✅              | Medium               |
| RCV         | ❌         | ❌           | ⚠️              | Already in progress  |  

The choice seems clear to me. By making Approval voting the *bridge* to other, more expressive methods, we give ourselves the best chance to make electoral reform *stick*. Moving from Approval to something like STAR or Condorcet is much more feasible than jumping straight from Choose-one plurality to STAR or Condorcet, which would likely provoke significant resistance due to the perceived complexity and unfamiliarity of those systems.

[RCV has utterly failed, and needs to go](../ditch-rcv){:target="_blank"}, and I think we need to rally around Approval voting before attempting to push for more complex reforms like STAR or Condorcet. RCV sandbagged better methods like Approval, ignoring the warnings and evidence from experts, and in doing so has set back the Electoral Reform movement. We cannot repeat this mistake again by expecting another untested system to succeed where RCV failed without first building a foundation of public trust and understanding through a simpler, proven method like Approval voting.

I admire the Equal Vote Coalition for trying to be inclusive of multiple systems, and their choices of Approval, STAR, and Condorcet are the best available, in my opinion. But I worry that a clear favoritism towards STAR might tempt them to fly too close to the sun. If STAR fails when Approval could have succeeded, or are forced to compete directly, we may squander the last of our political capital and public trust in electoral reform. The solution in this moment seems quite obvious: let's start with Approval and go from there.

Adopting Approval does not exclude later adoption of other systems. Perhaps, after we whet the appetite for more expressive systems by showing voters that Approval voting can improve the outcomes and solve many of the problems we face as a nation, then we can start experimenting with more complex systems. But pushing for something too far outside of the Overton window, only for it to face backlash for being too new or complex, *does* make it harder to keep the reforms in place, or to try again later. It's a gamble, and I don't like the odds.

Approval voting is the *clear* first step we need to make in electoral reform. We should assume we have *one chance* to get this right, and stand together behind it before backlash leads to a successful ban on all systems besides Choose-one, as the existing ["Make Elections Great Again Act"](https://ivn.us/posts/11-ways-mega-act-congress-tries-control-how-you-vote-2026-02-06) threatens to do.
