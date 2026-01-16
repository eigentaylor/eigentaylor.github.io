---
layout: distill
title: A Practical Case for Approval Voting
date: 2026-01-15
description: It's not just mathematically elegant, it's the most practical voting system out there.
giscus_comments: true
importance: 1
tags: voting
category: polisci
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: The Logistical Case for Approval Voting
  - name: The Condorcet Criterion
  - name: Internal Consistency
  - name: Approval Voting and Internal Consistency
    subsections:
      - name: You can't prove it's not Condorcet
  - name: The Condorcet Approximation of Approval Voting
  - name: Conclusion
---

## Introduction

The focus of this post is less about *why* we need electoral reform, and more about *how* we should go about it in a practical manner. For one unconvinced of the issues with our current system, I recommend reading my [previous post on the theoretical case for Approval voting](../approval/){:target="_blank"}. This post assumes you are already convinced that plurality voting is deeply flawed, and that we need to adopt a better voting system.

I wanted to make this post because of [a video I saw, where Jason Snead testified before the Indiana Senate Elections Committee in favor of preemptively banning "Ranked Choice Voting" (AKA Instant Runoff Voting or IRV) in the state of Indiana](https://x.com/jasonwsnead/status/2011085198478266677).

> In IRV (Instant Runoff Voting), voters rank candidates in order of preference. If no candidate wins a majority of first-choice votes, the candidate with the fewest first-choice votes is eliminated, and their votes are redistributed to the remaining candidates based on the voters' next preferences. This process continues until a candidate wins a majority (of active ballots, which rank at least one remaining candidate).

Note: I refuse to call IRV "Ranked Choice Voting", since I believe that creates expectations that are not met by the method.

Now, while I don't necessarily believe this is truly a well-intentioned effort to protect "free and fair elections", the worst part about the video is that basically everything he says about IRV is, in my estimation, entirely correct. Here are some of his most convincing arguments:

- "Ranked choice voting makes every aspect of the election system more complicated"
- "It makes it harder to vote"
- "It makes it harder to count the votes"
- "It makes it harder to audit the elections"
- "It makes it harder for voters to have confidence in the results"
- "[An example in Oakland California] where mistakes were undetected that ultimately changed the outcome of an election... It took four months and a lawsuit just to see the actual winner in that particular Ranked-Choice voting election."
- "Because it is so hard to vote, it also takes voters longer"
- "One MIT study found that with just five people to rank, that adds an additional minute to the amount of time it takes to vote per race. And getting more candidates to run is an explicit goal of the Ranked-Choice voting lobby."
- "You're going to see voting times potentially double, on your ballot. That means longer lines at the polling place. That means people dropping off, possibly not even getting the opportunity to vote because they have to drop their kids off at soccer practice, or they simply can't stand that long in line."
- "There is simply no reason to put voters through that, only to wind up with a result they don't fully understand."

I cannot disagree with any of these critiques of IRV, and they are some of the primary reasons I do not consider it a serious candidate for electoral reform.

The simple fact is that ranked methods for a single-winner election are needlessly complicated, and they introduce a host of problems that make them impractical for real-world use.

Note: On the other hand, a ranked method for proportional representation (like Single Transferable Vote) makes a lot more sense, since a complicated method and ballot is more justified for a more complicated type of election.

Not to mention that the primary ranked method being pushed is IRV, which is a terrible voting system that has many well-documented flaws, and I would never recommend it for any serious use case (don't worry, we will get there). I plan to go into the serious problems with IRV in another post in the future.

In contrast, the Approval voting method has *none* of these problems. It is simple to understand, simple to vote with, simple to count, simple to audit, and simple to trust.

## The Logistical Case for Approval Voting

> Approval voting allows voters to approve of (vote for) as many candidates as they like.

It really is that simple.

In addition to its many theoretical benefits (which I have covered in [previous posts](../approval/){:target="_blank"}), Approval voting is *objectively* the most practical voting system for real-world use.

1. Ballots require minimal changes. Mere wording changes are sufficient to convert a plurality ballot into an Approval ballot. Instead of requiring voters to vote for only one, and throwing out the ballot if they vote for more than one, we simply change the wording to allow voters to vote for as many candidates as they like. Making it basically impossible to spoil or screw up filling out a ballot. Ranked ballots, on the other hand are a huge hassle to design, print, and explain to voters, and are much more prone to voter error.
2. It works on existing voting machines. Since Approval ballots are functionally identical to plurality ballots in terms of how they are marked, existing voting machines can be used, and only minor software changes are needed to change the counting logic. The cost of infrastructure to accommodate a ranked ballot is significant and expensive, often requiring entirely new voting machines to be purchased.
3. It is simple to understand. Voters simply vote for all the candidates they approve of. The paradox of choice, where too many options can lead to decision paralysis, a voter need not choose just one candidate, and can instead vote for all the candidates they like.
4. It is simple to count. Counting Approval votes is as simple as counting plurality votes. It is also "precinct summable": every precinct can count their own votes and report the totals, and then the overall winner can be determined by summing the totals from each precinct. This is NOT true for most ranked methods, which usually requires all ballots to be collected to know who to eliminate or who wins head-to-head match-ups.
5. It is simple to audit. Since counting is so simple, auditing is also simple. Approval voting elections can be audited using simple hand counts of random samples of ballots, just like plurality elections. Ranked methods, on the other hand, are much more difficult to audit due to their complexity.
6. It is simple to trust. Because the method is so simple and transparent, voters can easily understand how their votes are counted and how the winner is determined. This leads to greater trust in the election results.
7. It is "internally consistent". We will explain exactly what this means later, but in short, Approval voting always respects the expressed preferences of the electorate in a consistent manner, unlike IRV. There cannot be an outcome which contradicts the expressed approvals of the voters, which would compromise the legitimacy of the winner and trust in the system.
8. It allows for more expressive voting than plurality, while avoiding the complexity of ranked methods. Further, it has intense incentive for sincere voting. Voters also need not take advantage of the complexity and still vote for just one candidate if they wish.
9. It reduces negative campaigning and polarization. Since candidates want to be approved by as many voters as possible, they have an incentive to appeal to a broader audience, rather than just firing up a loud minority base. This can lead to more positive campaigning and less polarization.
10. It encourages more candidates to run, and more diverse options. Since voters can approve of multiple candidates, they can express honest preference to long-shot or niche candidates without fear of "wasting" their vote, by also voting for a front-runner they find acceptable. Minority candidates can get their full due, rather than being shut out due to vote-splitting and strategic betrayal.
11. It is insensitive to more candidates, vote-splitting, and the spoiler effect. Adding more candidates does not change the fundamental dynamics of the election, and requires only a binary choice (approve or not approve) for each added candidate for each voter.
12. It could increase voter turnout. By making voting simpler, more intuitive, and more sincere, Approval voting could encourage more people to participate in elections.
13. It would elect the strongest candidate broadly acceptable to the most voters, also increasing legitimacy of the winner.

If you want a simple reform, that is easy to implement and has massive positive ramifications, there is literally no better choice than Approval voting. This is inarguable.

But to really understand why Approval voting is truly the most practical and robust in practice and in theory, all the while maintaining the benefits of more robust ranked method with minimal complexity, we need to fully understand the problems with ranked methods like IRV.

The question then becomes: does a ranked method provide enough additional benefit to justify its added complexity and impracticality? Particularly if the method is opaque and difficult to audit, as IRV is. Further, does the method actually deliver on its promise to take into account the more nuanced and expressive preferences that the more complex ballot allows? I argue that IRV fails to do so in a significant way.

## The Condorcet Criterion

> The Condorcet criterion states that if there is a candidate who would win a head-to-head matchup against every other candidate, that candidate should be the overall winner of the election.

The ranked ballot inherently allows for this type of comparison: when a voter ranks candidate A over candidate B, that becomes a vote for A over B in a head-to-head matchup. A ranking is thus a vote in every possible head-to-head matchup between candidates (by assuming transitivity: if A is ranked over B, and B is ranked over C, then the voter prefers A over C as well).

If voters are allowed to rank candidates, then it seems reasonable to expect that the voting method should necessarily take advantage of that information to find a Condorcet winner if one exists. Particularly if the ranked method is being pushed with the promise of "majority rule".

The problem is that IRV does not satisfy the Condorcet criterion. This has occurred in real-world elections, such as the 2009 mayoral election in Burlington, Vermont and the 2022 Alaska U.S. House special election. In both cases, strong repeal efforts were taken as a result, succeeding in Burlington and barely failing in Alaska. These failures have **real** and **serious** consequences for public trust in the method. Not to mention, with ballot exhaustion, the winner might not even be ranked on a majority of ballots. The promise of majority rule in IRV is literally a blatant lie.

[Other reports](https://illinoislawreview.org/wp-content/uploads/2024/11/Atkinson-Foley-Ganz.pdf) have indicated that this problem would be far worse in bimodal swing states like Arizona and Pennsylvania, where the electorate is deeply divided.

> While it has been offered as a solution to polarization, our results show that IRV cannot be expected to effectively lead to representative outcomes relative to other election systems. Reformers concerned with polarization should look to other ranked-choice methods. As shown in our simulations, a Condorcet electoral method will tend to elect candidates much closer to the state’s median and mean voter, especially for highly polarized states with bimodal electorates. -(Atkinson, Foley, Ganz 2024)

Also in the report,

> As we will see, the center squeeze is generally more severe in the states with more polarized partisanship distributions. -(Atkinson, Foley, Ganz 2024)

IRV may actually *accelerate* polarization, rather than mitigate it, and Condorcet failures may be far more common in the most politically relevant swing states.

It seems only reasonable that *if* we must adopt a ranked method (which, in my estimation, does not have strong arguments in its favor), we should at least choose one that satisfies the Condorcet criterion.

The key reason for this is ***internal consistency***. If a ranked method fails to elect the Condorcet winner, then it both fails to deliver on its promise of majority rule, *and* erodes (if not destroys) public confidence and trust in the method, setting back the electoral reform movement as a whole. If the electorate becomes disillusioned with IRV, are they going to be willing to try another method?

If we wish to have trust in our elections, we **must** have a method that is internally consistent.

## Internal Consistency

But what does it truly mean to be "internally consistent"? Well, for a ranked method, for which the entire point is to obtain ordinal (ordered) preferences from voters, then the result should reflect those preferences in a consistent manner.

In Alaska 2022, we had a three way race between Mary Peltola (D), Sarah Palin (R), and Nick Begich III (R). We had in round 1:

- Peltola: ~40%
- Palin: ~32%
- Begich: ~28%

Clearly, approximately 60% of the electorate preferred a Republican over a Democrat. However, since no candidate had a majority, Begich (the last place candidate) was eliminated, and his votes were transferred to the second choice on those ballots. However, in the end, Peltola maintained her lead and won the election without even a majority of the ballots cast (only 47.5% over Palin's 44.8%, with 7.7% of ballots exhausted).

However, 52.5% of voters (who expressed a preference) preferred Begich over Peltola. Further, 61.4% of voters (who expressed a preference) preferred Begich over Palin as well. Begich was the Condorcet winner, and yet he lost. The system failed in both delivering majority rule, and also failed to honor the expressed preferences of the electorate.

All of the voters who ranked Palin first and Begich second (56.9% of Palin-first voters) had their preferences completely ignored. They clearly preferred both Republicans over Peltola, but because of the short-sightedness of IRV, their full ordered preferences were not honored or even considered. What is even the point of ranking candidates if your full preferences are not taken into account?

The potential fix is to employ a Condorcet method instead. There are many to choose from, such as Minimax, Schulze, or Ranked Pairs. All of these methods will always elect the Condorcet winner if one exists, thus satisfying internal consistency (at least when one exists).

If one is to use a ranked method, the only sane way to do so is to use a Condorcet method. If you *can* fail to elect the Condorcet winner, you *will* erode public trust in the method, and thus the entire reform effort.

However, Condorcet methods are not foolproof. There is not always a Condorcet winner (in the case of cycles), and we have seen this in real elections: for example, in [Minnesota](https://ranked.vote/report/us/mn/2021/11/ward-2). In such cases, we must have a reasonable and justifiable way to break the cycle. Different Condorcet methods have different ways of doing this, but all require some philosophical justification, which may not be universally agreed upon.

In that way, Condorcet methods are not perfectly internally consistent. However, they are far more consistent than IRV, which can fail to elect the Condorcet winner even when one clearly exists.

However, the issue with Condorcet methods, is less about potential cycles (non-existence of a Condorcet winner), and more fundamentally that they are often absurdly complex and difficult to understand, audit, and trust. So while they are more internally consistent than IRV, they still have significant practical drawbacks. They still face the complexity issues of ranked ballots, which would be particularly problematic in smaller local elections with low visibility.

Some [reports have indicated that Copeland](https://www.mathematica.org/api/sitecore/MediaLibrary/ActualDownload?fileId=%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileName=Mathematica_VotingSim_FINAL_Sep2025.pdf&fileData=Mathematica_VotingSim_FINAL_Sep2025.pdf%20-%20%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileMime=application%2Fpdf){:target="_blank"} (Mathematica) may be the most robust Condorcet method. However, I am partial to Minimax for its simplicity (if you haven't guessed, simplicity and practicality are my main priorities).

Approval voting, on the other hand, is both ultimately simple, ultimately logically practical, and ultimately internally consistent.

## Approval Voting and Internal Consistency

No matter what voting system you use, you must destroy some information. But, since it is simply impractical to ask every voter to write an essay about which candidates they like and should win, and aggregate that into a single coherent decision, we must settle for some compromise.

- Plurality requires the voter to pick only one candidate they (supposedly) want the most, throwing out all other information about alternatives they would have preferred or find acceptable.
- Ranked methods get the *ordinal* information about preferences, but fail to capture intensity or acceptability. A voter who ranked A > B > C cannot express if they would find B acceptable or not. We can only know that they prefer A more than B, and B more than C.
- Cardinal methods with more than two possible scores (like Score voting) are ambiguous about what the scores mean. Is a 3/5 candidate "acceptable" or not? Different voters may interpret the scores differently.
- Approval voting, requires the voter to split the candidates into exactly two tiers: which are "acceptable" (approved) and which are "not acceptable" (not approved). This collapses all the information of their potentially nuanced preferences into a binary choice for each candidate.

However, I believe that Approval asks the most practical and, arguably, *important* question: who do you actually want to win? This is a question that voters must give an unambiguous answer to for each candidate.

Out of all of these compromises, I think the most easy to justify are Approval voting and ranked methods (which are Condorcet consistent). Both are unambiguous about the expressed preferences of the voter. However, in addition to the objective greater simplicity of Approval over a ranked method, I also argue that Approval voting is *more* internally consistent than ranked methods, while also being "*good enough*".

### You can't prove it's not Condorcet

Both Approval voting and plurality voting, if the ballots are taken to be perfectly accurate expressions of voter preferences, are necessarily internally consistent.

- In plurality voting, if we assume that the candidate the voter votes for is the only acceptable candidate, and literally all others are not at all acceptable, then plurality voting will always elect the candidate that is most acceptable to the most voters, given that assumption.
- In Approval voting, if we assume that the candidates the voter approves of are all acceptable, and all others are not at all acceptable, then Approval voting will always elect the candidate that is most acceptable to the most voters, given that assumption. Further, the chosen candidate **will** always beat every other candidate in a head-to-head matchup based on the expressed "dichotomous" (two-tiered) preferences of the electorate.

In this way, both systems reduce the true preferences of all voters into simpler worlds where they always select the best candidate.

While both are internally consistent under these assumptions, it's hard to argue that the assumption for plurality voting--the simpler world it induces--is not far less reasonable or realistic than that of Approval voting. Voters can naturally like more than one alternative, and it's unreasonable to assume that they find literally all but one candidate completely unacceptable.

My favorite example is the 2000 U.S. Presidential election in Florida. George W. Bush got 537 more votes than Al Gore, giving Bush the presidency, despite losing the national popular vote. Out of the approximately 6 million votes cast in Florida, Ralph Nader got about 97,000 votes. As a more left-leaning alternative to Gore, it is reasonable to assume that most of Nader's voters would have preferred Gore over Bush if Nader were not on the ballot. In particular, it's very plausible that *at least* 538 of Nader's voters would have preferred Gore over Bush, which would have swung the election to Gore.

Further, the fact that voters must pick only one candidate forces them into strategic dilemmas. To have an impact on the election, a voter must pick only a viable candidate, even if they find other candidates more acceptable. This means that we can trust their expressed preference far less.

Approval, on the other hand, arguably captures the fact that if you force voters to say "yes" or "no" to each candidate, they will be able to answer that question. Further, the sincerity incentives under Approval voting are very strong, so we can trust that the expressed preferences are *at least* more accurate, and truer to the voter's actual preferences.

I cannot argue against the fact that this is still information destruction. It is not realistic to assume that voters feel equally about all those they approve, and all those they disapprove of. But it still asks, in my view, the most important question: who would you be okay with winning? And it does so in a way that is unambiguous and easy to understand. By simply finding the candidate that the most voters say "yes" to, this makes Approval voting a compromise that attempts to satisfy the most voters, while still being practical.

In my other [post on Approval voting](../approval/){:target="_blank"}, I showed that Approval is Condorcet-consistent with the expressed dichotomous preferences of the electorate. The proof is simple:

If W is the winner under Approval voting, then for any other candidate C, the difference in their total approvals is exactly equal to the difference of "strict" approvals. This is because if you subtract out all the ballots that approved both W and C, you are left with only the ballots that approved W but not C (strict approvals for W) and the ballots that approved C but not W (strict approvals for C), while preserving the difference in total approvals.

For example, if W got 100 approvals and C got 80 approvals, and there were 30 ballots that approved both W and C, then:

- W's strict approvals = 100 - 30 = 70
- C's strict approvals = 80 - 30 = 50
- Difference in total approvals = 100 - 80 = 20
- Difference in strict approvals = 70 - 50 = 20

Thus, if W has more total approvals than C, then W must also have more strict approvals than C.

That is, the Approval winner must necessarily have more strict approvals than any other candidate, and thus must win every head-to-head matchup based on the expressed dichotomous preferences of the electorate.

This is inherently more legitimate than the idea that the plurality winner is the candidate who had the most voters choose them than all others. Like, duh. This is because plurality necessarily takes voters hostage (particularly those who hate both major party candidates) and forces them to pick only one candidate (forcing them to be strategic about which candidate they should pick to have any impact on the results), with no way to express acceptability of alternatives. Approval allowed them to express an unambiguous signal of *some* level of acceptability for as many candidates as they wanted to.

That is, Approval voting is necessarily a compromise, yes, but the sacrifice makes the system far *more* practical than any ranked system. While being internally consistent, and reaping most of the benefits of the far more complicated Condorcet methods.

That's right, Approval is not just 100% Condorcet-consistent with the expressed preferences, but is also surprisingly effective at electing the ranked Condorcet winner in practice!

## The Condorcet Approximation of Approval Voting

In Calculus and Physics, and other STEM fields, there is a concept of a "linear approximation". This is where you take a complicated function, that is difficult to compute or evaluate, and approximate it locally, near a location, with a simpler linear function (a straight line) that is far easier to compute and evaluate. This line captures the local information with relatively high fidelity, while being far simpler to work with.

I claim that Approval voting is the "linear approximation" of Condorcet methods: simpler, easier to work with, far less expensive, more practical, and less opaque. It has high fidelity to the true Condorcet winner, without being beholden to them in every case. In my view, this makes it *better* than Condorcet methods in practice, because I am not convinced that the true Condorcet winner is always the best candidate to elect in every case.

Simulations put the true Condorcet-efficiency of Approval voting at around [67% to 84%](https://www.degruyterbrill.com/document/doi/10.1515/9781400859504.15/html), depending on the model and parameters used. Real world data is limited, but even more positive. With [certain strategic voting models](https://journals.sagepub.com/doi/10.1177/0951629808097286) paradoxically increasing the efficiency.

Brams proves in his 2008 book ["Mathematics and Democracy"](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy) (pg 39) that Approval voting outcomes are "strongly stable" if and only if the winner is a unique Condorcet winner. That is, if the Approval winner is not the Condorcet winner, then there exists some coalition of voters who could change their votes to elect a different winner, while no coalition can topple the actual Condorcet winner (through sincere strategies).

Other research has shown that Approval voting has a high likelihood of electing the Condorcet winner in practice, even if it does not do so every time. I argue this is a feature, not a bug.

Approval outcomes are inherently indeterminate with respect to the ranked preferences of the electorate. Even if you do not change the rankings that voters have, different approval thresholds can lead to different winners. This means that the Approval winner is not necessarily the "true" Condorcet winner, but rather the candidate who is most acceptable to the electorate given a certain level of acceptability.

If a Condorcet winner fails to be sufficiently acceptable to the electorate, then perhaps they should not win. There is a persistent myth that Approval voting elects the bland, milquetoast, inoffensive, "everyone's second choice" candidate who stands for nothing. This is simply not true. While having broad, widespread acceptability is important, you should also aim to have sufficient intensity of support, to excite that broad base to actually approve you on their ballots. The candidate who can inspire passionate support while also building bridges to a wide audience is the candidate who would ultimately win under Approval voting.

Like a bland Condorcet winner, a polarizing candidate A who is the Condorcet winner through first choice preferences of 51% of voters, but is found completely unacceptable by the other 49%, may not be the best candidate to elect. Does another candidate B, who is instead found acceptable by 60% of voters, not have a stronger claim to victory?

Not necessarily. This is ultimately a philosophical question about what we want from our elections. I cannot claim that B is a provably better candidate than A. However, here is the kicker: nobody can claim that A *is* a Condorcet winner in the first place, because Approval voting does not capture that information.

The internal consistency instead will show that 9% more voters found B acceptable, and A unacceptable than vice versa. "You can't prove B is not the Condorcet winner"! The internal consistency of Approval voting guarantees that B beats A in a head-to-head matchup based on the expressed dichotomous preferences of the electorate. This protects the method by ensuring legitimacy of the winner, even if the result might have differed under a ranked Condorcet method.

One might object that this is a weakness. That we have swindled the true Condorcet winner out of their rightful victory by destroying information. However, this cuts both ways. A Condorcet method might elect a candidate who is truly unacceptable to a large portion of the electorate, just because they are preferred by a slight majority in head-to-head match-ups. Ranked ballots destroy acceptability information, and thus cannot guarantee that the Condorcet winner is actually acceptable to the electorate. We must choose which information to preserve, and which to destroy.

I extend my hand to those who argue for Condorcet methods: even *if* you are not convinced that a non-Condorcet winner, who manages to be more broadly acceptable than the true ranked Condorcet winner, Approval still manages to elect the true Condorcet winner a majority of the time in practice, in return for the benefit of far greater simplicity, practicality, and trustworthiness. That is, I argue Approval voting is "good enough" of a "Condorcet approximation", while being far more practical.

A simpler method, more practical, Condorcet-efficient (a strong majority of the time), all the while maintaining that strong internal consistency, guaranteeing the legitimacy just as a Condorcet method would, while being simple enough that voters would *actually be able to TRUST it*. This is the ultimate compromise.

## Polarization Diffusion

[Cox 1987](https://www.jstor.org/stable/2111325){:target="_blank"} investigated the dynamics of various voting methods in a spatial model of voting. He found that a number of voting methods tend to encourage candidates to adopt more acceptable positions, rather than extreme positions, in order to win elections. He showed that Plurality voting encourages extremist outcomes, while systems like Approval, Borda, and Condorcet methods encourage outcomes where the Candidates converge towards the median voter. That is, both Approval and Condorcet methods will likely diffuse polarization over time, but Approval does this with far greater simplicity and practicality.

I have [spoken before](../approval/){:target="_blank"} on my worry about the intense polarization in modern politics. Approval voting, by encouraging candidates to seek broad acceptability, can help mitigate this polarization. I believe Condorcet methods can do this as well, but again, at the cost of practicality and trustworthiness. And, after the 2020 Presidential election "stop the steal" debacle, transparency and trust in our voting systems and election results is more important than ever.

## Conclusion

Approval voting is not just theoretically elegant, it is also the most practical voting system for real-world use. If you want a simple voting reform, which is easy to implement, and would be trusted by voters, there is literally no better choice than Approval voting.

The proposed ranked systems like IRV (which are not Condorcet-consistent) are needlessly complicated, difficult to understand, difficult to count, difficult to audit, difficult to trust, fail to deliver on their promises of majority rule, and fail to be internally consistent.

Condorcet methods, while more internally consistent, are still needlessly complicated and difficult to understand, audit, and trust.

Approval voting strikes the perfect balance between simplicity, practicality, internal consistency, and (sufficient in practice) Condorcet-efficiency. It is the best choice for real-world elections.

In summary, Approval voting is

- Practical: The acceptability question is **simple to ask and tally**. Approval voting is logistically practical and far simpler to understand, administrate, and interact with than any ranked system.
- Internally consistent and robust: Approval voting always respects the expressed preferences of the electorate in a consistent manner, guaranteeing legitimacy of the winner.
- Empirically Condorcet-efficient: Approval voting elects the ranked Condorcet winner a strong majority of the time in practice, while being far simpler and more practical than any ranked Condorcet method.

The choice is clear.

---

[hyperlink](https://www.youtube.com/watch?v=9bSxOhoM9pE){:target="_blank"}
