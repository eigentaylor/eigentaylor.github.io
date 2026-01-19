---
layout: distill
title: A Practical Case for Approval Voting
date: 2026-01-15
description: It's not just mathematically elegant, it's the most practical solution for solving our voting system's problems.
giscus_comments: true
importance: 1
tags: voting
category: polisci
featured: true
related_posts: true
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: The Logistical Case for Approval Voting
  - name: The Condorcet Criterion
  - name: The Information Problem
  - name: Internal Consistency
  - name: Approval Voting and Internal Consistency
    subsections:
      - name: You can't prove it's not Condorcet
  - name: The Condorcet Approximation of Approval Voting
  - name: Conclusion
  - name: Appendix
  - name: References
---

## Introduction

The focus of this post is less about *why* we need electoral reform, and more about *how* we should go about it in a practical manner. This post assumes you are already convinced that plurality voting is deeply flawed, and that we need to adopt a better voting system.

For one unconvinced of the issues with our current system, I recommend reading this [fantastic post](https://substack.com/@akorky/p-180772748) by Amanda Mahlendorf, or my [previous post on the theoretical case for Approval voting](../approval/){:target="_blank"} (which also explains the incredible mathematical elegance of Approval voting). Rather than focus on the theoretical benefits and mathematical properties of Approval voting (as that post did), or the [nuances of strategy](../avstratproof){:target="_blank"}, this post will focus on the practical logistical case for Approval voting, and why it is the most sensible choice for real-world use.

I wanted to make this post because of [a video I saw, where Jason Snead testified before the Indiana Senate Elections Committee in favor of preemptively banning "Ranked Choice Voting" (AKA Instant Runoff Voting or IRV) in the state of Indiana](https://x.com/jasonwsnead/status/2011085198478266677){:target="_blank"}.

> In IRV (Instant Runoff Voting), voters rank candidates in order of preference. If no candidate wins a majority of first-choice votes, the candidate with the fewest first-choice votes is eliminated, and their votes are redistributed to the remaining candidates based on the voters' next preferences. This process continues until a candidate wins a majority (of active ballots, which rank at least one remaining candidate).

Note: I am not going to call IRV "Ranked Choice Voting", since I believe that creates expectations that are not met by the method. Since we are talking about multiple ranked methods, I prefer to use the more specific term "IRV" to avoid confusion.

Now, while I don't necessarily believe this is truly a well-intentioned effort to protect "free and fair elections", the worst part about the video is that basically everything he says about IRV is, in my estimation, entirely correct. Here are some of his most convincing points:

>
- "Ranked choice voting makes every aspect of the election system more complicated"
- "It makes it harder to vote"
- "It makes it harder to count the votes"
- "It makes it harder to audit the elections"
- "It makes it harder for voters to have confidence in the results"
- "[[An example in Oakland California](https://oaklandside.org/2023/01/05/recount-for-real-county-supervisor-calls-for-an-independent-recount-of-oaklands-ranked-choice-elections/){:target="_blank"}] where mistakes were undetected that ultimately changed the outcome of an election... It took four months and a lawsuit just to see the actual winner in that particular Ranked-Choice voting election."
- "Because it is so hard to vote, it also takes voters longer"
- "[One MIT study](https://electionlab.mit.edu/articles/effect-ranked-choice-voting-maine){:target="_blank"} found that with just five people to rank, that adds an additional minute to the amount of time it takes to vote per race. And getting more candidates to run is an explicit goal of the Ranked-Choice voting lobby."
- "You're going to see voting times potentially double, on your ballot. That means longer lines at the polling place. That means people dropping off, possibly not even getting the opportunity to vote because they have to drop their kids off at soccer practice, or they simply can't stand that long in line."
- "There is simply no reason to put voters through that, only to wind up with a result they don't fully understand."

[(Source: Jason Snead, 2026)](https://x.com/jasonwsnead/status/2011085198478266677)

As a strong proponent of electoral reform, and someone who believes that plurality voting is deeply flawed, and a threat to the stability of our democracy, I was not expecting to listen to testimony against reform and realize that it's almost completely on point.

That MIT study also indicated that respondents reported significantly lower levels of overall satisfaction with the voting process and a marked decrease in confidence regarding the integrity of the election results. The data also showed a heightened perception among voters that the the process was "slanted" against their specific political party.

I cannot disagree with any of these critiques of IRV, and they are some of the primary reasons I do not consider it a serious candidate for electoral reform.

The simple fact is that ranked methods for a single-winner election are needlessly complicated, and they introduce a host of problems that make them impractical for real-world use.

Note: On the other hand, a ranked method for proportional representation (like Single Transferable Vote) makes a lot more sense, since a complicated method and ballot is more justified for a more complicated type of election.

Not to mention that the primary ranked method being pushed is IRV, which is a terrible voting system that has many well-documented flaws, and I would never recommend it for any serious use case (don't worry, we will get there). I plan to go into the serious problems with IRV in another post in the future.

In contrast, the Approval voting method has *none* of these problems. It is simple to understand, simple to vote with, simple to count, simple to audit, and simple to trust. And the benefits for adopting Approval voting are substantial.

What we will see in this post is that the promises that IRV makes about "majority rule" and "honoring voter's complex granular preferences" are simply not delivered in practice, those issues would likely exacerbate if adopted more widely in the US, and the methods which can guarantee those promises (called Condorcet methods) are far too complex and opaque to be practical or trustworthy for real-world use, particularly in the United States, where public trust in elections is already tenuous at best.

In your mind, I want you to picture the ideal ranked voting system like a complex curve, which is hard to work with, and Approval voting as a simple straight line that approximates that curve. Approval is essentially the engineering solution: the simple and practical, but still robust straight line "approximation" of the most robust ranked methods, while avoiding all the complexity.

## The Logistical Case for Approval Voting

> Approval voting allows voters to approve of (vote for) as many candidates as they like. Simply put a check mark next to each candidate you approve of. The candidate with the most approval votes wins.

It really is that simple. But that simplicity is its greatest strength.

In addition to its *many* theoretical benefits (which I have covered in [previous posts](../approval/){:target="_blank"}), Approval voting is *objectively* the most practical voting system for real-world use.

1. Ballots require minimal changes. Mere wording changes are sufficient to convert a plurality ballot into an Approval ballot. Instead of requiring voters to vote for only one, and throwing out the ballot if they vote for more than one, we simply change the wording to allow voters to vote for as many candidates as they like. Making it basically impossible to spoil or screw up filling out a ballot. Ranked ballots, on the other hand are a huge hassle to design, print, and explain to voters, and are much more prone to voter error.
2. It works on existing voting machines. Since Approval ballots are functionally identical to plurality ballots in terms of how they are marked, existing voting machines can be used, and only minor software changes are needed to change the counting logic. The cost of infrastructure to accommodate a ranked ballot is significant and expensive, often requiring entirely new voting machines to be purchased.
3. It is simple to understand. Voters simply vote for all the candidates they approve of. Listing all acceptable options from a list is a far simpler and more intuitive task than ranking options in order of preference. Ranked ballots can be confusing, particularly for less-educated voters, and can lead to mistakes and spoiled ballots.
4. It promotes sincerity and reduces the need for strategic voting. "Strategy" boils down to [a simple threshhold decision](../avstratproof){:target="_blank"} of "where to draw the line" between acceptable and not acceptable candidates. Voters can simply approve all candidates they find acceptable, without needing to worry about ranking or ordering them. Ranked ballots often require voters to make complex strategic decisions about how to rank candidates, or how to game the elimination order, which can lead to insincere voting and manipulation of the system. In particular, IRV does not eliminate the vote-splitting problem or spoiler effect (see the [Alaska 2022](#internal-consistency) example below).
5. It is simple and fast to count. Counting Approval votes is as simple as counting plurality votes. It is also "precinct summable": every precinct can count their own votes and report the totals, and then the overall winner can be determined by simply summing the totals from each precinct. You can actually get the election results *quickly*, using the optimized infrastructure we've been developing and improving for our current plurality elections. This is NOT true for most ranked methods, which usually requires all ballots to be collected to know who to eliminate or who wins head-to-head match-ups. For large-scale elections, a ranked method utilizing eliminations or head-to-head match-ups would require all ballots to be centrally collected and processed, which is logistically complex and expensive.
6. It is simple to audit. Since counting is so simple, auditing is also simple. Approval voting elections can be audited using simple hand counts of random samples of ballots, just like plurality elections. The same statistical methods apply with no additional complexity. Ranked methods, on the other hand, are generally much more difficult to audit due to conditional eliminations, vote transfers, or the need to compute all head-to-head matchups.
7. It is simple to trust. Because the method is so simple and transparent, voters can easily understand how their votes are counted and how the winner is determined. This leads to greater trust in the election results. Because of the need to collect all ballots centrally and run complex algorithms (which have been shown to have bugs and errors in real-world use, like in [Oakland](https://oaklandside.org/2023/01/05/recount-for-real-county-supervisor-calls-for-an-independent-recount-of-oaklands-ranked-choice-elections/){:target="_blank"}). "Stop the steal" happened in a system as simple and transparent as plurality voting. We cannot afford to make our elections any more opaque or difficult to understand.
8. It is "internally consistent". We will dive into this in-depth later, but in short, Approval voting always respects the expressed preferences of the electorate in a consistent manner, unlike IRV. For example, when Nick Begich III lost the [Alaska 2022 House Special election](#internal-consistency) (which we dive deep into later) to Mary Peltola, despite over 52% of voters who expressed a preference ranking Begich higher. This never happens in Approval voting. There cannot be an outcome which contradicts the expressed approvals of the voters, which would compromise the legitimacy of the winner and trust in the system.
9. It allows for more expressive voting than plurality, while avoiding the complexity of ranked methods. Further, it has intense incentive for sincere voting. Voters also need not take advantage of the complexity and still vote for just one candidate if they wish.
10. It reduces negative campaigning and polarization. Since candidates want to be approved by as many voters as possible, they have an incentive to appeal to a broader audience, rather than just firing up a loud minority base. This can lead to more positive campaigning and less polarization.
11. It encourages more candidates to run, giving voters more diverse options. Since voters can approve of multiple candidates, they can express honest preference to long-shot or niche candidates without fear of "wasting" their vote, by also voting for a front-runner they find acceptable. Minority candidates can get their full due, rather than being shut out due to vote-splitting and strategic betrayal.
12. It is insensitive to more candidates, vote-splitting, and the spoiler effect. Adding more candidates does not change the fundamental dynamics of the election, and requires only a binary choice (approve or not approve) for each added candidate for each voter.
13. It could increase voter turnout. By making voting simpler, more intuitive, and more sincere, Approval voting could encourage more people to participate in elections.
14. It would elect the strongest candidate broadly acceptable to the most voters, also increasing legitimacy of the winner.

If you want a simple reform, that is easy to implement and has massive positive ramifications, there is literally no simpler choice than Approval voting.

But to really understand why Approval voting is truly the most practical and robust in practice and in theory, all the while maintaining the benefits of more robust ranked method with minimal complexity, we need to fully understand the problems with ranked methods, like IRV.

The question then becomes: does a ranked method provide enough additional benefit to justify its added complexity and impracticality? Particularly if the method is opaque and difficult to audit, as IRV is. Further, does the method actually deliver on its promise to take into account the more nuanced and expressive preferences that the more complex ballot allows? I argue that IRV fails to do so in a significant way.

## The Condorcet Criterion

> The Condorcet criterion states that if there is a candidate who would win a head-to-head matchup against every other candidate, that candidate should be the overall winner of the election.

The ranked ballot inherently allows for this type of comparison: when a voter ranks candidate A over candidate B, that becomes a vote for A over B in a head-to-head matchup. A ranking is thus a vote in every possible head-to-head matchup between candidates (by assuming transitivity: if A is ranked over B, and B is ranked over C, then the voter prefers A over C as well).

If voters are allowed to rank candidates, then it seems reasonable to expect that the voting method should necessarily take advantage of that information to find a Condorcet winner if one exists. Particularly if the ranked method is being pushed with the promise of "majority rule".

The problem is that IRV does not satisfy the Condorcet criterion. This has occurred in real-world elections, such as the 2009 mayoral election in Burlington, Vermont and the 2022 Alaska U.S. House special election. In both cases, strong repeal efforts were taken as a result, succeeding in Burlington and barely failing in Alaska. These failures have **real** and **serious** consequences for public trust in the method. Not to mention, with ballot exhaustion, the winner might not even be ranked on a majority of ballots. The promise of majority rule in IRV is literally a blatant lie. Take [this IRV election](https://ranked.vote/report/us/ca/sfo/2024/11/supervisor-d11){:target="_blank"} where the winner got only 37.2% of the total ballots cast.

The primary mechanism for which this happens is called the "Center Squeeze". When a moderate and acceptable candidate is sandwiched between two more extreme option, the more extreme options can "squeeze out" the moderate option in first place votes, leading to an early elimination of the moderate candidate, even if that moderate would beat both extremes in head-to-head match-ups.

[Other reports (Atkinson, Foley, Ganz)](https://illinoislawreview.org/wp-content/uploads/2024/11/Atkinson-Foley-Ganz.pdf) have indicated that this problem would be far worse in bimodal swing states like Arizona, Nevada, and Georgia, where the electorate is deeply divided. But also in states like South Carolina, Mississippi, Alabama, and Delaware. The distance between where the IRV winners and Condorcet winners lie is significantly larger in these states. In the report, Alaska actually appears to be one of the better states (near the middle of the distribution), relatively speaking. If Alaska has already had a Condorcet failure with IRV, then it seems like this may be a sign of what could happen far more frequently if IRV is adopted in more places, rather than an isolated, rare event.

> "While it has been offered as a solution to polarization, our results show that IRV cannot be expected to effectively lead to representative outcomes relative to other election systems. Reformers concerned with polarization should look to other ranked-choice methods. As shown in our simulations, a Condorcet electoral method will tend to elect candidates much closer to the state’s median and mean voter, especially for highly polarized states with bimodal electorates." -(Atkinson, Foley, Ganz 2024)

Also in the report,

> "As we will see, the center squeeze is generally more severe in the states with more polarized partisanship distributions." -(Atkinson, Foley, Ganz 2024)

IRV may actually *exacerbate* polarized outcomes, rather than mitigate them, and Condorcet failures may be far more common in the most politically relevant swing states. The simulations done in the report had Condorcet failures in approximately **40% of all elections**.

It seems only reasonable that *if* we must adopt a ranked method (which I am not convinced that we should), we should at least choose one that satisfies the Condorcet criterion.

The key reason for this is ***internal consistency***. If a ranked method fails to elect the Condorcet winner, then it both fails to deliver on its promise of majority rule, *and* erodes (if not destroys) public confidence and trust in the method, setting back the electoral reform movement as a whole. If the electorate becomes disillusioned with IRV, are they going to be willing to try another method?

This makes choosing a robust method imperative. The idea that we can pick a "transitional", flawed method like IRV, and then "fix it later" is a dangerous gamble that may backfire spectacularly. If we wish to have trust in our elections and democracy, and have the reform method stick, we **must** have a method that is internally consistent.

## Internal Consistency

But what does it truly mean to be "internally consistent"? Well, for a ranked method, for which the entire point is to obtain ordinal (ordered) preferences from voters, then the result should reflect those preferences in a consistent manner.

In [Alaska 2022](https://ranked.vote/report/us/ak/2022/08/cd), we had a three way race between Mary Peltola (D), Sarah Palin (R), and Nick Begich III (R). We had in round 1:

- Peltola: ~40%
- Palin: ~31%
- Begich: ~28%

Clearly, approximately 60% of the electorate preferred a Republican over a Democrat. However, since no candidate had a majority, Begich (the last place candidate) was eliminated, and his votes were transferred to the second choice on those ballots. However, in the end, Peltola maintained her lead and won the election without even a majority of the ballots cast (only 47.5% over Palin's 44.8%, with 7.7% of ballots exhausted).

However, 52.5% of voters who expressed a preference preferred Begich over Peltola (that is, only 41.3% of all ballots cast preferred Peltola to Begich). Further, 61.4% of voters (who expressed a preference) preferred Begich over Palin as well. Begich was the Condorcet winner, and yet he lost. This is not majority rule. The system failed in both delivering majority rule, and also failed to honor the expressed preferences of the electorate.

All of the voters who ranked Palin first and Begich second (56.9% of Palin-first voters) had their preferences completely ignored. They clearly preferred both Republicans over Peltola, but because of the short-sightedness of IRV, their full ordered preferences were not honored or even considered. The system eliminated the only Republican who could have won the second round, and pushed the weaker Condorcet loser instead, simply because they had slightly more first-choice votes.

33,308 voters ranked Palin-first and Begich-second. If just 2,893 (8.67%) of those voters ([4.94% of Palin's first-choice total](https://substack.com/home/post/p-182659376){:target="_blank"}) changed their vote to Begich-first and Palin-second, it would have changed the eliminated candidate to Palin, and elected a Republican instead of a Democrat. That is, 2,893 Republican voters, who would just switch the order of the Republican candidates they like, without changing their ranking of the Democrat, would change the outcome from a Democrat to a Republican. That isn't solving the spoiler problem. That's not honoring majority rule. What is even the point of ranking candidates if your full preferences are not taken into account?

The potential fix is to employ a Condorcet method instead. There are many to choose from, such as Minimax, Schulze, or Copeland. All of these methods will always elect the Condorcet winner if one exists, thus satisfying internal consistency (at least when one exists).

If one is to use a ranked method, the only sane way to do so is to use a Condorcet method. If you *can* fail to elect the Condorcet winner, you *will* erode public trust in the method, and thus the entire reform effort.

However, Condorcet methods are not foolproof. There is not always a Condorcet winner (in the case of cycles), and we have seen this in real elections: for example, in [Minnesota](https://ranked.vote/report/us/mn/2021/11/ward-2). In such cases, we must have a reasonable and justifiable way to break the cycle. Different Condorcet methods have different ways of doing this, but all require some philosophical justification, which may not be universally agreed upon.

In that way, Condorcet methods are not perfectly internally consistent. However, they are far more consistent than IRV, which can fail to elect the Condorcet winner even when one clearly exists.

However, the issue with Condorcet methods, is less about potential cycles (non-existence of a Condorcet winner), and more fundamentally that they are often absurdly complex and difficult to understand, audit, and trust. I encourage you to open the [Wikipedia page for the Schulze method](https://en.wikipedia.org/wiki/Schulze_method) and explain it to a layperson or ballot worker. Or, more *importantly*, how are you going to explain it to a legislator, or write it into law in a way that is understandable and unambiguous? I, frankly, cannot see a law which mentions directed graphs and path strengths being passed in any state legislature anytime soon.

I know someone who tried to explain Schulze to the board members of Mensa, and they rejected it for being too complex. If Mensa *leaders*, certified *geniuses*, find it too complex for practical use, how can we expect the average voter to trust it in a high stakes political election? **Simplicity is a prerequisite for trust.** We cannot rely on a blackbox, theoretically perfect but opaque method, to run our elections. Not in the era of "stop the steal" and rampant election conspiracy theories.

If you cannot explain to the protester outside the polling place, the grandmother sending you an article about how the election was stolen, or the people frothing at the mouth when politicians are sowing doubt about the legitimacy of elections on twitter, why their candidate who got the most first-place votes didn't win, or how the winner was determined based on complex graph theory or vote transfers, then that method is not practical for real-world use in the United States. "When we shipped all the ballots to a central location to count them, and put them into a computer to run an algorithm, the other candidate got more vote transfers, so your candidate lost" is not going to cut it.

So while they are more internally consistent than IRV, they still have significant practical drawbacks. They still face the complexity issues of ranked ballots, which would be particularly problematic in smaller local elections with low visibility.

Some [reports have indicated that Copeland (Source: Mathematica)](https://www.mathematica.org/api/sitecore/MediaLibrary/ActualDownload?fileId=%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileName=Mathematica_VotingSim_FINAL_Sep2025.pdf&fileData=Mathematica_VotingSim_FINAL_Sep2025.pdf%20-%20%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileMime=application%2Fpdf){:target="_blank"} may be the most robust Condorcet method. However, I am partial to Minimax for its simplicity (if you haven't guessed, simplicity and practicality are my main priorities).

Approval voting, on the other hand, is both ultimately simple, ultimately logically practical, and ultimately internally consistent.

## The Information Problem

No matter what voting system you use, you must destroy some information. But, since it is simply impractical to ask every voter to write an essay about which candidates they like and should win, and aggregate that into a single coherent decision, we must settle for some compromise, such as ranking, scoring, or approving candidates. Remember, we are taking potentially millions of ballots and trying to aggregate them into a single winner. This is inherently lossy.

Every system has its trade-offs, and destroys some information about voter preferences. On one hand, we want to maximize expressiveness of what the voter can express, but we also need to balance that with practicality. In that end, we have to decide which information is most important to preserve, and what information we are willing to destroy.

- Plurality requires the voter to pick only one candidate they (supposedly) want the most, throwing out all other information about alternatives they would have preferred or find acceptable.
- Ranked methods get the *ordinal* information about preferences, but fail to capture intensity or acceptability. A voter who ranked A > B > C cannot express if they would find B acceptable or not. We can only know that they prefer A more than B, and B more than C.
- Cardinal methods with more than two possible scores (like Score voting) are ambiguous about what the scores mean. Is a 3/5 candidate "acceptable" or not? Different voters may interpret the scores differently.
- Approval voting, requires the voter to split the candidates into exactly two tiers: which are "acceptable" (approved) and which are "not acceptable" (not approved). This collapses all the information of their potentially nuanced preferences into a binary choice for each candidate.

I believe that Approval asks the most practical and, arguably, *important* question: which candidates would you find acceptable as the winner? Who do you consent to govern you? This is a question that voters must give an unambiguous answer to for each candidate.

Out of all of these compromises, I think the most easy to justify are Approval voting and ranked methods (but only if the way the rankings are aggregated is Condorcet consistent). Both are unambiguous about the expressed preferences of the voter.

However, in addition to the objective greater simplicity of Approval over a ranked Condorcet method, Approval voting maintains the internal consistency of a Condorcet method, while also being "*good enough*".

## Approval Voting and Internal Consistency

Both Approval voting and plurality voting, if the ballots are taken to be perfectly accurate expressions of voter preferences, are necessarily internally consistent.

- In plurality voting, if we assume that the candidate the voter votes for is the only acceptable candidate, and literally all others are not at all acceptable, then plurality voting will always elect the candidate that is most acceptable to the most voters, given that assumption.
- In Approval voting, if we assume that the candidates the voter approves of are all acceptable, and all others are not at all acceptable, then Approval voting will always elect the candidate that is most acceptable to the most voters, given that assumption. Further, the chosen candidate **will** always beat every other candidate in a head-to-head matchup based on the expressed "dichotomous" (two-tiered) preferences of the electorate.

In this way, both systems reduce the true preferences of all voters into simpler worlds where they always select the best candidate.

While both are internally consistent under these assumptions, it's hard to deny that the simpler world plurality pretends we live in is far less reasonable or realistic than that of Approval voting. Voters can naturally like more than one alternative, and it's unreasonable to assume that they find literally all but one candidate completely unacceptable.

Further, the fact that voters must pick only one candidate forces them into strategic dilemmas. To have an impact on the election, a voter must pick only a viable candidate, even if they find other candidates more acceptable. This means that we can trust their expressed plurality preference far less.

My favorite example is the 2000 U.S. Presidential election in Florida. George W. Bush got 537 more votes than Al Gore, giving Bush the presidency, despite losing the national popular vote. Out of the approximately 6 million votes cast in Florida, Ralph Nader got about 97,000 votes. As a more left-leaning alternative to Gore, it is reasonable to assume that most of Nader's voters would have preferred Gore over Bush if Nader were not on the ballot. In particular, it's very plausible that *at least* 538 of Nader's voters would have preferred Gore over Bush, which would have swung the election to Gore. All such voters chose sincerity, voting for the candidate they most preferred, and it gave them their least preferred outcome.

Under Approval voting, those Nader voters could have approved both Nader and Gore, expressing their sincere preferences while still contributing to the main contest between Gore and Bush. Not only is this a solution to the spoiler problem, but it also gives voters a powerful way to express their honest and sincere preferences without fear of "wasting" or "splitting" their vote.

Approval, on the other hand, arguably captures the fact that if you ask voters if they consent to be governed by a candidate, they will be able to answer that question. Further, the sincerity incentives under Approval voting are very strong, so we can trust that the expressed preferences are *at least* more accurate, and truer to the voter's actual preferences. We can reasonably assume that the candidates they approve of are at least preferable to those they do not approve of. This is a compromise between a lossy plurality world, and an ideal ranked world.

I cannot argue against the fact that this is still information destruction. It is not realistic to assume that voters feel equally about all those they approve, and equally dislike all those they disapprove of. But it still asks, in my view, the most important question: who would you be okay with winning? Who do you consent to govern you? And it does so in a way that is unambiguous and easy to understand. By simply finding the candidate that the most voters say "yes" to, this makes Approval voting a compromise that attempts to satisfy the most voters, while still being practical.

### You can't prove it's not Condorcet

When discussing the technical Condorcet consistency of Approval voting, based on assumed dichotomous preferences, someone said it's a "You can't prove it's not Condorcet" method, and I found that hilarious and apt.

In my other [post on Approval voting](../approval/){:target="_blank"}, I showed that Approval is Condorcet-consistent with the expressed dichotomous preferences of the electorate. The proof is simple, but best illustrated with an example (though, a general proof is given in the [Appendix](#appendix)).:

For example, if W got 100 approvals and C got 80 approvals, and there were 70 ballots that approved both W and C, then:

- W's strict approvals = 100 - 70 = 30
- C's strict approvals = 80 - 70 = 10
- Difference in total approvals = 100 - 80 = 20
- Difference in strict approvals = 30 - 10 = 20. It's exactly the same!

Thus, if W has more total approvals than C, then W must also have more strict approvals than C.

That is, the Approval winner must necessarily have more strict approvals than any other candidate, and thus must win every head-to-head matchup based on the expressed dichotomous preferences of the electorate.

This is inherently more legitimate than the idea that the plurality winner is the candidate who had the most voters choose them than all others. This is because plurality necessarily takes voters hostage (particularly those who hate both major party candidates) and forces them to pick only one candidate (forcing them to be strategic about which candidate they should pick to have any impact on the results), with no way to express acceptability of alternatives. Approval allows them to express an unambiguous signal of *some* level of acceptability for as many candidates as they want to.

That is, Approval voting is necessarily a compromise, yes, but the sacrifice makes the system far *more* practical than any ranked system. All the while being internally consistent, and reaping most of the benefits of the far more complicated Condorcet methods.

Despite technically being a cardinal SCORE system (where voters rate a candidate out of either 0 or 1), Approval is actually the only SCORE system that IS internally consistent. If you allow just one more tier (like being able to rate candidates 0, 1, or 2), then you lose internal consistency and ballot-based Condorcet consistency. This is something STAR tries to solve with a runoff, but it still fails to be internally (Condorcet) consistent in all cases. See the [Appendix](#appendix) for a detailed proof and example of this for both SCORE and STAR voting.

Now, I don't want to strawman, and argue that absurd pathological examples mean SCORE or STAR would not be fine in practice. But, again, in a "stop the steal" era, I do not believe we can afford to allow any such internal inconsistencies that could erode public trust in the method. Not to mention, these systems would fail to have all the logistical benefits of Approval voting, since they require more complex ballots and counting, and can't be run on existing infrastructure as easily. But, I feel I must at least address these systems, as they are often in the conversation of electoral reform.

In this way, Approval voting is uniquely positioned at the nexus of Ranked and Cardinal methods. It avoids the complexity of ranked methods, by being a cardinal method. But it's also the uniquely internally consistent cardinal method through its simplicity. Simplicity begets internal consistency. And, while it does achieve simplicity through reduced expressiveness, it still manages to capture the most important information about voter preferences: acceptability, while also being ultimately practical.

You see, Approval is not just 100% Condorcet-consistent with the expressed preferences, but is also surprisingly effective at electing the ranked Condorcet winner in practice!

## The Condorcet Approximation of Approval Voting

In Calculus and Physics, and other STEM fields, there is a concept of a "linear approximation". This is where you take a complicated function, that is difficult to compute or evaluate, and approximate it locally, near a location, with a simpler linear function (a straight line) that is far easier to compute and evaluate. This line captures the local information with relatively high fidelity, while being far simpler to work with.

I claim that Approval voting is the "linear approximation" of Condorcet methods: simpler, easier to work with, far less expensive, more practical, and less opaque. It has high fidelity to the true Condorcet winner, without being beholden to them in every case. In my view, this makes it *better* than Condorcet methods in practice, because I am not convinced that the true Condorcet winner is always the best candidate to elect in every case.

Simulations put the true Condorcet-efficiency of Approval voting at around [67% to 84%](https://www.degruyterbrill.com/document/doi/10.1515/9781400859504.15/html), depending on the model and parameters used. Real world data is limited because there are not many real-world elections that collect both approval and ranked data. But a [1985 professional society election](https://www.jstor.org/stable/2632078) where both approval and ranking data were collected showed approval voting elected a candidate with substantially broader support than the plurality winner, despite a near-tie in pairwise comparisons.

Critically, the plurality winner C, won by 8 first-place votes over candidate B. However, in inferred pairwise matchups of those who expressed preference, C ended up winning over B by only 1 vote (B > C: 900, C > B: 901), with 27 voters who expressed indifference and thus not counted in the pairwise comparison (see the [Appendix](#appendix) for how these numbers were arrived at). However, B won strongly over C in Approval voting with 1,038 for B to 908 for C (based on actual ballots cast; the lead expanded to almost 200 using extrapolated votes). This shows that Approval voting was able to capture the broader acceptability of B over C, despite the near-tie in pairwise matchups. Running this election with a Condorcet method (or plurality) would have produced bedlam, due to the absurdly close pairwise matchup based on incomplete expressed preferences, but Approval instead produced a clear and unambiguous winner with strong legitimacy. I argue this is a feature, not a bug.

Brams proves in his 2008 book ["Mathematics and Democracy"](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy) (pg 39) that Approval voting outcomes are "strongly stable" if and only if the winner is a unique Condorcet winner. That is, if the Approval winner is not the Condorcet winner, then there exists some coalition of voters who could coordinate to change their votes and elect a different winner while making all coalition members better off. However, when the winner IS the Condorcet winner, no such improving coalition exists. While coalitions could potentially topple the Condorcet winner through coordination, doing so would require some coalition members to accept a worse outcome, making such coordination unstable.

Further, [certain intuitive strategies (Laslier)](https://journals.sagepub.com/doi/10.1177/0951629808097286) paradoxically increase the efficiency (potentially up to 100%), only requiring knowledge of the top two viable candidates.

This means that Condorcet winners have a sort of stability and gravitational pull in Approval voting, if they can manage to be acceptable enough to be voted for by the electorate. An inoffensive Condorcet winner, who is such only because they are everyone's second choice, may not be able to win if they cannot inspire sufficient approval.

Approval outcomes are inherently indeterminate with respect to the ranked preferences of the electorate. Even if you do not change the rankings that voters have, different approval thresholds can lead to different winners. This means that the Approval winner is not necessarily the "true" Condorcet winner, but rather the candidate who is most acceptable to the electorate given a certain level of acceptability.

If a Condorcet winner fails to be sufficiently acceptable to the electorate, then perhaps they should not win. There is a persistent myth that Approval voting elects the bland, milquetoast, inoffensive, beige wall, "everyone's second choice" candidate who stands for nothing. This is simply not true. While having broad, widespread acceptability is important, you should also aim to have sufficient intensity of support, to excite that broad base to actually approve you on their ballots. The candidate who can inspire passionate support while also building bridges to be appealing to a broad audience is the candidate who would ultimately win under Approval voting.

I personally believe Zohran Mamdani is an excellent example of such a candidate, who managed to excite a passionate base of support, while also framing his campaign in terms of affordability, which made him broadly acceptable to a wide range of voters in New York City. In the three-way plurality general, he ended up winning the general election for Mayor in 2025 [with over 50% of the votes](https://en.wikipedia.org/wiki/2025_New_York_City_mayoral_election). Such a strong win would likely have been preserved under Approval voting, due to the polarizing nature of his main opponent, Andrew Cuomo.

Some claim Brad Lander, who was less exciting but not strongly disliked by anyone, would have won the primary under Approval voting. However, the ballot data makes this a possible but unlikely claim. [Mamdani's unexpected and strong first-round win (43.6%)](https://ranked.vote/report/us/ny/nyc/2025/07/mayor) over Cuomo's 35.9% gives Mamdani a very strong floor of support. In addition, the combination of Mamdani's astounding 69.6% head-to-head win over Lander (in ballots that expressed a preference) and Lander's weak 11.2% first choice votes suggests an insufficient intensity of support for Lander. To close the gap, Lander would have needed to excite enough of Mamdani's supporters to also approve Lander on their ballots, while enough of Lander's own supporters would have had to find Mamdani unacceptable enough to withhold approval. Given the 69.6% to 30.4% asymmetry in pairwise preferences, this outcome is highly unlikely.

A polarizing Condorcet winner may not be the best candidate to elect either. Suppose candidate A, who is the Condorcet winner through first choice preferences of 51% of voters, but is found completely unacceptable by the other 49%. Does another candidate B, who is instead found acceptable by 60% of voters, not have a stronger claim to victory?

Not necessarily. This is ultimately a philosophical question about what we want from our elections. I cannot claim that B is a provably better candidate than A. However, here is the kicker: nobody can claim that A *is* a Condorcet winner in the first place, because Approval voting does not capture that information.

The internal consistency instead will show that 9% more voters found B acceptable, and A unacceptable than vice versa. "You can't prove B is not the Condorcet winner"! The internal consistency of Approval voting guarantees that B beats A in a head-to-head matchup based on the expressed dichotomous preferences of the electorate. Because there's no ranked data to consult, voters see a clear winner based on the only information available: who earned the most approval. This transparency preserves trust, even if the outcome might differ from a hypothetical Condorcet method. In short, the question the system asks is simply different from a Condorcet method, but both consistently pick the most legitimate candidate based on the question the ballot asks.

One might object that this is a weakness. That we have swindled the true Condorcet winner out of their rightful victory by destroying information. However, this cuts both ways. A Condorcet method might elect a candidate who is truly unacceptable to a large portion of the electorate, just because they are preferred by a slight majority in head-to-head match-ups. Ranked ballots destroy acceptability information, and thus cannot guarantee that the Condorcet winner is actually acceptable to the electorate. We must choose which information to preserve, and which to destroy.

I extend my hand to those who argue for Condorcet methods: even *if* you are not convinced that a non-Condorcet winner, who manages to be more broadly acceptable than the true ranked Condorcet winner, should win, Approval still manages to elect the true Condorcet winner a majority of the time in practice, in return for the benefit of far greater simplicity, practicality, and trustworthiness. That is, I argue Approval voting is "good enough" of a "Condorcet approximation", while being far more practical.

A simpler method, more practical, Condorcet-efficient (a strong majority of the time), all the while maintaining that strong internal consistency, guaranteeing the legitimacy just as a Condorcet method would, while being simple enough that voters would *actually be able to TRUST it*. This is the ultimate compromise.

## Polarization Diffusion

I have [spoken before](../approval/){:target="_blank"} on my worry about the intense polarization in modern politics. Approval voting, by encouraging candidates to seek broad acceptability, can help mitigate this polarization. I believe Condorcet methods can do this as well, but again, at the cost of practicality and trustworthiness. And, after the 2020 Presidential election "stop the steal" debacle, transparency and trust in our voting systems and election results is more important than ever.

[Cox 1987](https://www.jstor.org/stable/2111325){:target="_blank"} investigated the dynamics of various voting methods in a spatial model of voting. He found that a number of voting methods tend to encourage candidates to adopt more acceptable positions, rather than extreme positions, in order to win elections. He showed that Plurality voting encourages extremist outcomes, while systems like Approval, Borda, and Condorcet methods encourage outcomes where the Candidates converge towards the median voter. That is, both Approval and Condorcet methods will likely diffuse polarization over time, but Approval does this with far greater simplicity and practicality.

## Conclusion

Approval voting is not just theoretically elegant, it is also the most practical voting system for real-world use. If you want a simple voting reform, which is easy to implement, and would be trusted by voters, there is literally no simpler choice than Approval voting.

The proposed ranked systems like IRV (which are not Condorcet-consistent) are needlessly complicated, difficult to understand, difficult to count, difficult to audit, difficult to trust, fail to deliver on their promises of majority rule, and fail to be internally consistent.

Condorcet methods, while more internally consistent, are still needlessly complicated and difficult to understand, count, audit, and trust.

Any ranked method necessarily falls into at least one of the following categories:

1. Too complicated for the average voter to understand or verify the results.
2. A conspiracy-breeding blackbox that is necessarily less trustworthy than our existing dead-simple plurality system (which is already distrusted enough as is).
3. Fails to be internally consistent with the expressed preferences of the electorate (ex. any non-Condorcet method)
4. Too logistically impractical and expensive to implement and **audit** in large scale elections.

Any one of these reasons is, in my view, disqualifying for real-world use.

Approval voting strikes the perfect balance between simplicity, practicality, internal consistency, and (sufficient in practice) Condorcet-efficiency. It is the best choice for real-world elections.

In summary, Approval voting is

- Practical: The acceptability question is **simple to ask and tally**. Approval voting is logistically practical, working on existing machines and infrastructure, and far simpler to understand, administrate, **trust**, and interact with than any ranked system.
- Internally consistent and robust: Approval voting always respects the expressed preferences of the electorate in a consistent manner, guaranteeing legitimacy of the winner.
- Empirically Condorcet-efficient: Approval voting elects the ranked Condorcet winner a strong majority of the time, while being far simpler and more practical than any ranked method. Regardless, even when it does not, it still, without fail, elects the most broadly acceptable candidate.

The choice is clear.

---

## Appendix

The post is over, but here I wish to include some mathematical proofs and examples for some of the claims made in this post, for interested readers.

**Approval Condorcet Consistency Proof**: Suppose candidate W is the Approval winner, and candidate C is any other candidate. If $$\gamma$$ is the number of ballots that approve both W and C, and $$x_W$$ and $$x_C$$ are the total approvals for W and C respectively, then $$x_W - \gamma$$ is the number of strict approvals for W (ballots that approve W but not C), and $$x_C - \gamma$$ is the number of strict approvals for C (ballots that approve C but not W).

The difference in strict approvals is:

$$(x_W - \gamma) - (x_C - \gamma) = x_W - x_C$$

Therefore, if W has more total approvals than C ($$x_W > x_C$$), then W must also have more strict approvals than C. Thus, W wins the head-to-head matchup against C based on the expressed dichotomous preferences of the electorate. Since this holds for any candidate C, W is the Condorcet winner based on the expressed dichotomous preferences.

**Score internal inconsistency example**: Suppose we have two candidates, A and B, and 101 voters, and assume that we are using a SCORE voting system with more than 2 levels. If there were only two levels, this would be Approval voting which is consistent, as proven above. Without loss of generality, let's assume we have just three levels. The following example works regardless of how many levels there are. If the 101 voters have the following scores:

- 51 voters scored candidate A as 1, and candidate B as 0.
- 50 voters scored candidate A as 0, and candidate B as 2.
  
Candidate A would lose with 51 points to B's 100 points, despite being preferred over B by a majority of voters. To avoid this, A voters might strategically score A as 2 instead of 1, and now it's just Approval voting again. A SCORE system with more than two levels is actually just Approval voting, but voters can give fractional approvals.

This is something STAR voting tries to solve by adding a runoff at the end, but doesn't fix (while also adding complexity).

**STAR internal inconsistency example**: STAR voting uses a score ballot (0-5), but then has a runoff between the top two scoring candidates, where each ballot counts as one vote for whichever of the two runoff candidates was scored higher.
Take this example:

- 30 voters score A:2, B:1, C:0
- 20 voters score A:0, B:2, C:5

In total, A has 60 points, B has 70 points, and C has 100 points. So C and B go to the runoff, and B wins the runoff 30 to 20. But A was preferred over B and C by a majority of voters. This is a particularly nefarious example, since not only did the Condorcet winner not win, but the candidate with the highest total score didn't win either. Both losing candidates have a valid claim to victory.

Is it realistic to assume that 60% of voters wouldn't rate anyone higher than a 2/5? I would never claim such a thing. The purpose of this example is that by allowing voters to be *more* expressive than just "approve" (1) or "disapprove" (0), we lose both:

1. Simplicity and the ability to run on existing infrastructure
2. Guaranteed internal consistency with the expressed preferences of the electorate.

In that the purpose of this post is to argue that Approval voting is uniquely positioned as the simultaneously simplest, most practical, and most robust method we could adopt, I do believe potential for such pathologies, and the lack of the major logistical advantages that Approval voting offers, is disqualifying.

**1985 Professional Society Election Example**: Candidate A was not at all competitive, so we focus on candidates B and C.

In first choice votes, B received 827 votes, and C received 835 votes, a difference of 8 votes in favor of C. When examining the expressed ranked preferences, we find:

- 70 voters ranked ABC (B > C)
- 66 voters ranked ACB (C > B)

This results in a net difference of 4 votes in favor of B (70 - 66 = 4), which closes the lead of C to just 4 votes (B > C: 897, B > C: 901). However, there were 3 voters who approved both A and B, which naturally implies a preference of B > C. Adding these 3 votes to B's total gives us B > C: 900, C > B: 901. With 27 voters not expressing a preference between B and C (voting only for A, and neglecting to provide any further information), we arrive at a dead heat based on expressed preferences.

It gets even closer if we assume that the 27 voters who only voted for A match the proportion of preferences expressed by the other 139 (70+66+3) voters:

$$ \frac{70+3}{139}\cdot 27 =14.2\approx 14 \text{ voters for }B>C $$

$$ \frac{66}{139}\cdot 27 =12.8\approx 13 \text{ voters for }C>B $$

Gives both B and C 914 votes in the inferred pairwise matchup, a perfect tie. This makes it really difficult to determine who the true Condorcet winner is based on the expressed preferences.

## References

Atkinson, M. L., Foley, E. B., & Ganz, S. M. (2024). *Beyond the Spoiler Effect: Can Ranked-Choice Voting Solve the Problem of Political Polarization*. Illinois Law Review. [https://illinoislawreview.org/wp-content/uploads/2024/11/Atkinson-Foley-Ganz.pdf](https://illinoislawreview.org/wp-content/uploads/2024/11/Atkinson-Foley-Ganz.pdf){:target="_blank"}

BondGraham, D. (2023). *Recount for real? County supervisor calls for an independent recount of Oakland’s ranked-choice elections*. [https://oaklandside.org/2023/01/05/recount-for-real-county-supervisor-calls-for-an-independent-recount-of-oaklands-ranked-choice-elections/](https://oaklandside.org/2023/01/05/recount-for-real-county-supervisor-calls-for-an-independent-recount-of-oaklands-ranked-choice-elections/){:target="_blank"}

Brams, S. J. (2008). *Mathematics and Democracy: Designing Better Voting and Fair-Division Procedures*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy){:target="_blank"}

Cox, G. W. (1987). Electoral Equilibrium under Alternative Voting Institutions. American Journal of Political Science, 31(1), 82–108. [https://doi.org/10.2307/2111325](https://doi.org/10.2307/2111325){:target="_blank"}

Fishburn, Peter C., and John D. C. Little. “An Experiment in Approval Voting.” Management Science, vol. 34, no. 5, 1988, pp. 555–68. JSTOR, [https://www.jstor.org/stable/2632078](https://www.jstor.org/stable/2632078){:target="_blank"}

Laslier, J. F. (2009). The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate. *Journal of Theoretical Politics*, 21(1), 113-136. [https://journals.sagepub.com/doi/10.1177/0951629808097286](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}

Mahlendorf, A. (2025). Why Some Voters Seek Alternatives to Plurality Voting. Substack. [https://substack.com/@akorky/p-180772748](https://substack.com/@akorky/p-180772748){:target="_blank"}

Mahlendorf, A. (2026). Fear of Vote Splitting. Substack. [https://substack.com/@akorky/p-182659376](https://substack.com/@akorky/p-182659376){:target="_blank"}

Mathematica Policy Research. (2025). *A Head-to-Head Comparison of Alternative Voting Rules*. [https://www.mathematica.org/api/sitecore/MediaLibrary/ActualDownload?fileId=%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileName=Mathematica_VotingSim_FINAL_Sep2025.pdf](https://www.mathematica.org/api/sitecore/MediaLibrary/ActualDownload?fileId=%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileName=Mathematica_VotingSim_FINAL_Sep2025.pdf&fileData=Mathematica_VotingSim_FINAL_Sep2025.pdf%20-%20%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileMime=application%2Fpdf){:target="_blank"}

Merrill, Samuel. "CHAPTER 2. Condorcet Efficiency". Making Multicandidate Elections More Democratic, Princeton: Princeton University Press, 1988, pp. 15-29. [https://doi.org/10.1515/9781400859504.15](https://doi.org/10.1515/9781400859504.15){:target="_blank"}

MIT Election Data and Science Lab. (2023). *The Effect of Ranked Choice Voting in Maine*. [https://electionlab.mit.edu/articles/effect-ranked-choice-voting-maine](https://electionlab.mit.edu/articles/effect-ranked-choice-voting-maine){:target="_blank"}

Ranked.Vote. (2022). *Alaska At-large Congressional District*. [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}

Ranked.Vote. (2021). *Minneapolis City Council Ward 2*. [https://ranked.vote/report/us/mn/2021/11/ward-2](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}

Ranked.Vote. (2025). *New York City DEM Mayor*. [https://ranked.vote/report/us/ny/nyc/2025/07/mayor](https://ranked.vote/report/us/ny/nyc/2025/07/mayor){:target="_blank"}

Ranked.Vote. (2024). *San Francisco Supervisor District 11 Election Results*. [https://ranked.vote/report/us/ca/sfo/2024/11/supervisor-d11](https://ranked.vote/report/us/ca/sfo/2024/11/supervisor-d11){:target="_blank"}

Snead, J. (2026). Testimony Before Indiana Senate Elections Committee on Ranked Choice Voting. [Video]. Twitter/X. [https://x.com/jasonwsnead/status/2011085198478266677](https://x.com/jasonwsnead/status/2011085198478266677){:target="_blank"}

Wikipeida Contributors. (2025). *2025 New York City mayoral election*. Wikipedia. [https://en.wikipedia.org/wiki/2025_New_York_City_mayoral_election](https://en.wikipedia.org/wiki/2025_New_York_City_mayoral_election){:target="_blank"}

Wikipedia Contributors. (2025). *Schulze method*. Wikipedia. [https://en.wikipedia.org/wiki/Schulze_method](https://en.wikipedia.org/wiki/Schulze_method){:target="_blank"}

---

[hyperlink](https://youtu.be/gvBYskU8zkU?si=A0Y_kPpYXt7nUUbW){:target="_blank"}
