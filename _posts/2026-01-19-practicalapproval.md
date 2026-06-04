---
layout: distill
title: A Practical Case for Approval Voting
date: 2026-01-19
description: It's not just mathematically elegant, it's the most practical solution for our electoral problems.
giscus_comments: true
importance: 1
tags: voting
category: polisci
featured: false
related_posts: true
exclude_appendix_from_word_count: true
collapse_appendix: false
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: The Logistical Case for Approval Voting
    subsections:
      - name: Implementation
      - name: Voter Experience
      - name: Administration and Auditing
      - name: Democratic Quality
  - name: The Condorcet Criterion
    subsections:
      - name: The Alaska Failure
      - name: A sign of things to come
      - name: Why not Condorcet?
  - name: The Information Problem
  - name: Approval Voting and Internal Consistency
    subsections:
      - name: You can't prove it's not Condorcet
        slug: you-cant-prove-its-not-condorcet
  - name: The Condorcet Approximation of Approval Voting
  - name: Conclusion
  - name: Appendix
bibliography: voting.bib
---

## Introduction

The focus of this post is less about *why* we need electoral reform, and more about *how* we should go about it in a practical manner. This post assumes you are already convinced that plurality voting is deeply flawed, and that we need to adopt a better voting system.

For one unconvinced of the issues with our current system, I recommend reading this [fantastic post](https://substack.com/@whelmedcitizen/p-180772748) by Amanda Mahlendorf <d-cite key="mahlendorf2025pluralityAlternatives"></d-cite>. Rather than focus on the mathematically cute aspects of Approval voting, or the [nuances of the benefits for sincerity](../av-stratproof){:target="_blank"}, this post will focus on the strong practical logistical case for Approval voting, and why it is the most sensible choice for real-world use.

I wanted to make this post because of [testimony by Jason Snead to the Indiana Senate Elections Committee in favor of preemptively banning "Ranked Choice Voting" (AKA Instant Runoff Voting or IRV) in the state of Indiana](https://x.com/jasonwsnead/status/2011085198478266677).

> In **IRV (Instant Runoff Voting)**, voters rank candidates in order of preference. If no candidate wins a majority of first-choice votes, the candidate with the fewest first-choice votes is eliminated, and their votes are redistributed to the remaining candidates based on the voters' next preferences. This process continues until a candidate wins a majority (of active ballots, which rank at least one remaining candidate).

Note: I am not going to call IRV "Ranked Choice Voting", since I believe that creates expectations that are not met by the method. Since we are talking about multiple ranked methods, I prefer to use the more specific term "IRV" to avoid confusion.

Now, while I don't necessarily believe this is truly a well-intentioned effort to protect "free and fair elections", the worst part about the video is that basically everything he says about IRV is, in my estimation, entirely correct. And ironically, his reasons against IRV work simultaneously as reasons *for* Approval voting. His points include: ranked ballots makes every aspect more complicated (voting, counting, auditing), takes longer ([MIT](https://electionlab.mit.edu/articles/effect-ranked-choice-voting-maine) <d-cite key="mit2023maineRcv"></d-cite> found an extra minute per race with 5 candidates), creates longer lines (indirect disenfranchisement) and lower confidence. Further, the need for a blackbox algorithm to get the results allows for situations like [Oakland, California](https://oaklandside.org/2023/01/05/recount-for-real-county-supervisor-calls-for-an-independent-recount-of-oaklands-ranked-choice-elections/) <d-cite key="bondGraham2023oaklandRecount"></d-cite>, where a mistakenly checked box resulted in counting errors that yielded the wrong winner, and took four months and a lawsuit to resolve. Imagine if this happened in a federal senate or a presidential election in a swing state. It would be absolute chaos. "There is simply no reason to put voters through that." [(Source: Jason Snead, 2026)](https://x.com/jasonwsnead/status/2011085198478266677)

That MIT study also indicated that respondents reported significantly lower levels of overall satisfaction with the voting process and a marked decrease in confidence regarding the integrity of the election results. The data also showed a heightened perception among voters that the process was "slanted" against their specific political party.

As a strong proponent of electoral reform, and someone who believes that plurality voting is deeply flawed, and a threat to the stability of our democracy, I was not expecting to listen to testimony against reform and realize that it's almost completely on point. The conclusion, however, is wrong. It's not that reform is bad, it's that if we want reform, we *must* choose reform which preserves the practicality, simplicity, and transparency of our current system, while fixing its major, structural flaws that cause the rot that permeates through our political and electoral institutions. Approval voting does *exactly* that.

> **Approval voting** allows voters to approve of (vote for) as many candidates as they like. Simply put a check mark next to each candidate you approve of. The candidate with the most votes wins.

In short, it's our current system, but you can cast multiple votes. It really is that simple. But that simplicity is its greatest strength. It also asks the most important question for a democracy: who do you consent to govern you?

The simple fact is that ranked methods for a single-winner election, rather than a more complicated (but representative) goal like proportional representation, are needlessly complicated, and they introduce a host of problems that make them impractical for real-world use. **Simplicity is a prerequisite for trust.** If we want electoral reform to be widely adopted and trusted, we must choose a method that is simple enough for everyone to understand, audit, and trust.

Not to mention that the primary ranked method being pushed is IRV, which is inconsistent and has many well-documented flaws (don't worry, we will get there).

In contrast, the Approval voting method has *none* of these problems. It is simple to understand, simple to vote with, simple to count, simple to audit, and simple to trust. And the benefits for adopting Approval voting are substantial.

What we will see in this post is that the promises that IRV makes about "majority rule" and "honoring the complex granular preferences of voters" are simply not delivered in practice; those issues would likely exacerbate if adopted more widely in the US. Further, the methods which can guarantee those promises (called Condorcet methods) are far too complex and opaque to be practical or trustworthy for real-world use *in all cases*, particularly in the United States, where public trust in elections is already tenuous at best.

In your mind, I want you to picture the ideal ranked voting system like a complex curve, which is hard to work with, and Approval voting as a simple straight line that approximates that curve. Approval is essentially the engineering solution: the simple and practical, but still robust straight line "approximation" of the most robust ranked methods, while avoiding all the complexity.

## The Logistical Case for Approval Voting

In addition to its *many* theoretical benefits, Approval voting is *objectively* the most practical voting system for real-world use.

### Implementation

The beauty of Approval voting lies in its seamless integration with existing electoral infrastructure. Ballots require only minimal changes: mere wording adjustments convert a plurality ballot into an Approval ballot. Instead of instructing voters to "vote for only one" and invalidating overvotes, we simply allow voters to approve as many candidates as they like. An overvote in our current system (accidentally bubbling in too many candidates, causing the ballot to be thrown out entirely) becomes a valid vote under Approval voting. It's essentially impossible to spoil a ballot.

This simplicity extends to the machinery itself: Approval voting works on existing voting machines. Since Approval ballots are functionally identical to plurality ballots in how they're marked, existing hardware can be repurposed with only minor software changes to the counting logic. In contrast, ranked ballot systems require significant, expensive infrastructure investments, often demanding entirely new (and expensive) voting machines.

If you want simple reform that's easy to implement with massive positive ramifications, there is literally no simpler choice than Approval voting.

### Voter Experience

For voters, Approval voting strikes an ideal balance between simplicity and expressiveness. The system is trivially simple to understand: voters approve all candidates they find acceptable. Listing acceptable options from a set is far more intuitive than ranking preferences, a task that can confuse less-educated voters and lead to mistakes or spoiled ballots.

Yet this simplicity doesn't sacrifice expressiveness. Approval voting allows more expressive voting than plurality while promoting sincerity. Voters can approve all candidates they find acceptable without strategic anguish about "wasting" votes on long-shots. The strategic calculation reduces to [a simple threshold decision](../av-stratproof){:target="_blank"}: "where to draw the line" between acceptable and unacceptable candidates. And voters who prefer the traditional approach can still approve just one candidate if they wish. Choosing to approve an additional candidate can never hurt a voter's preferred candidate, at worst preserving an existing outcome.

This design encourages more candidates to run, giving voters more diverse options. Since voters can approve multiple candidates, they can express honest preference for niche or long-shot candidates while also supporting acceptable frontrunners. Adding candidates doesn't fundamentally alter the election dynamics: each new candidate requires only a binary choice (approve or not) from each voter. The system is thus insensitive to vote-splitting and the spoiler effect, allowing minority candidates their full due rather than being shut out by strategic concerns.

### Administration and Auditing

From an administrative perspective, Approval voting is a dream. Counting is simple and fast, essentially identical to counting plurality votes. Crucially, Approval voting is "precinct summable": each precinct counts its own votes and reports totals, then the overall winner emerges from simple summation across precincts. You get election results quickly, leveraging the optimized infrastructure we've developed for plurality elections. This stands in stark contrast to ranked methods like IRV, which require centralized tallying. [In Venezuela](https://havanatimes.org/news/final-report-on-the-stolen-venezuelan-presidential-election/) <d-cite key="cocuyo2024venezuelaReport"></d-cite>, the absence of officially published precinct results became central to the claim that the Presidential election was stolen.

This simplicity makes auditing straightforward. Approval elections can be audited using simple hand counts of random ballot samples, just like plurality elections. The same statistical methods apply with no additional complexity. Ranked methods, conversely, are often far more difficult to audit due to conditional eliminations or vote transfers. The smart ranked systems (Condorcet methods) are generally simpler, but still much more complex than Approval. If a ballot ranks Alice over Bob, then that can be counted as just $+1$ vote for Alice in the Alice vs Bob race. Rather than just one score per candidate ($n$), you need to tally all head-to-head matchups (at minimum, $\frac{1}{2}n(n-1)$). In many cases, one can simply know the winner by seeing who has a higher tally against all other candidates. But when that does not exist, you often need a complex or opaque algorithm.

Perhaps most importantly, Approval voting is simple to trust. The method's transparency allows voters to easily understand how votes are counted and how winners are determined, fostering confidence in results. There's no need to collect all ballots centrally and run a complex black-box algorithm algorithms that have demonstrably failed in real-world use, like in [Oakland](https://oaklandside.org/2023/01/05/recount-for-real-county-supervisor-calls-for-an-independent-recount-of-oaklands-ranked-choice-elections/) <d-cite key="bondGraham2023oaklandRecount"></d-cite>, where a mistakenly checked box caused counting errors that yielded the wrong winner and took four months and a lawsuit to resolve. "Stop the steal" happened under a system as simple and transparent as plurality voting. We cannot afford to make our elections more opaque or difficult to understand.

### Democratic Quality

Beyond logistics, Approval voting delivers superior democratic outcomes. The system is internally consistent, always respecting expressed preferences in a coherent manner — unlike IRV. For example, Nick Begich III lost the [Alaska 2022 House Special election](#the-alaska-failure) to Mary Peltola despite more voters ranking Begich over Peltola than vice versa. Approval voting avoids such contradictions entirely. We'll dive deep into this concept of internal consistency later.

The incentive structure of Approval voting reduces negative campaigning and polarization. Since candidates want approval from as many voters as possible, they're incentivized to appeal to broader audiences rather than merely firing up loud minority bases. This promotes more positive campaigning and less polarization.

Ultimately, Approval voting elects the strongest candidate broadly acceptable to the most voters, enhancing winner legitimacy. The candidate who wins is one who successfully convinced the largest portion of the electorate that they were acceptable, a more robust mandate than plurality's "most intense plurality support" or IRV's complex elimination dynamics.

---

The myth that voters don't or wouldn't take advantage of the ability to approve multiple candidates is just that: a myth. In the most [recent approval election in Utah's Senate District 11](https://approval.vote/report/us/ut/senate_district_11/2025/12/utah-senate-district-11) <d-cite key="approvalVote2025utahSd11"></d-cite>, the average approvals per ballot was 1.7 in a field of five candidates. We have consistently seen in Fargo and St. Louis that voters are very willing to approve multiple candidates when given the opportunity, while not being forced to do so.

The question then becomes: does a ranked method offer enough additional benefits, that Approval does not, to justify its added complexity and impracticality? Particularly if the method is opaque and difficult to audit. The primary promise is greater granularity of expression. But does the method actually deliver on its promise to take into account the more nuanced and expressive preferences that the more complex ballot allows? I argue that IRV, in particular, fails to do so in a significant way.

## The Condorcet Criterion

While sounding very technical, the Condorcet criterion is, intuitively, the concept of "internal consistency" for ranked voting methods.

> The Condorcet criterion states that if there is a candidate who would win a head-to-head matchup against every other candidate, that candidate should be the overall winner of the election.

The ranked ballot inherently allows for this type of comparison: when a voter ranks candidate A over candidate B, that becomes a vote for A over B in a head-to-head matchup. A ranking is thus a vote in every possible head-to-head matchup between candidates.

If voters are allowed to rank candidates, then it seems reasonable to expect that the voting method should necessarily take advantage of that information to find a Condorcet winner if one exists. Particularly if the ranked method is being pushed with the promise of "majority rule". If candidate A wins the election, but more voters ranked B over A than A over B, then this is a failure of both majority rule and honoring the expressed preferences of the electorate. This is what we will call "**internal consistency**" for a ranked method.

The problem is that IRV does not satisfy the Condorcet criterion. This has occurred in real-world elections, such as the 2009 mayoral election in Burlington, Vermont and the 2022 Alaska U.S. House special election (which we will dissect in the [next section](#the-alaska-failure)). In both cases, strong repeal efforts were taken as a result, succeeding in Burlington and barely failing in Alaska (160,230 (49.88%) to 160,973 (50.11%), failing by just 743 votes). These failures have **real** and **serious** consequences for public trust in the method. And when you fail to elect the Condorcet winner, you necessarily fail to deliver on majority rule.

### The Alaska Failure

In [Alaska 2022](https://ranked.vote/report/us/ak/2022/08/cd) <d-cite key="rankedVote2022alaskaCd"></d-cite>, we had a three way race between Mary Peltola (D), Sarah Palin (R), and Nick Begich III (R). We had in round 1:

- Peltola: ~40%
- Palin: ~31%
- Begich: ~28%

Clearly, approximately 60% of the electorate preferred a Republican over a Democrat in their first choice preferences. Highly plausible, given this election was to replace the late Don Young, the longest-serving Republican in House history, who represented Alaska for nearly 49 years. Fun fact: Don Young was elected in his own Special Election in 1973 after Nick Begich Sr. (D) (Nick Begich III's grandfather) disappeared in a plane crash and was declared dead. Sorry, the history is just too good to not mention.

However, since no single candidate had a majority, Begich (the last place candidate) was eliminated, and his votes were transferred to the second choice on those ballots. However, in the end, Peltola maintained her lead and won the election without even a majority of the ballots cast (only 47.5% over Palin's 44.8%, with 7.7% of ballots exhausted).

However, 52.5% of voters who expressed a preference between Peltola and Begich preferred Begich over Peltola (that is, only 41.3% of all ballots cast preferred Peltola to Begich). Further, 61.4% of voters (who expressed a preference) preferred Begich over Palin as well. Begich was the Condorcet winner, and yet he lost. This is not majority rule. And the system left evidence of its own failure in the results, for all to see.

Palin thus loses head-to-head match-ups against both other candidates (making her a "Condorcet loser"), but the system failed to eliminate her first, allowing her to spoil the race for the other Republican. The system failed in both delivering majority rule, and also failed to honor the expressed preferences of the electorate.

All of the voters who ranked Palin first and Begich second (56.9% of Palin-first voters) had their preferences completely ignored. They clearly preferred both Republicans over Peltola, but because of the short-sightedness of IRV, their full ordered preferences were not honored or even considered. The system eliminated the only Republican who could have won the second round, simply because they had slightly more first-choice votes.

33,308 voters ranked Palin-first and Begich-second. If just 2,893 (8.67%) of those voters changed their vote to Begich-first and Palin-second, it would have changed the eliminated candidate to Palin, and elected a Republican instead of a Democrat (see [the Appendix](#appendix) for how we arrive at that number). That is, 2,893 Republican voters, could insincerely lie, and switch the order of the Republican candidates they like, without changing their ranking of the Democrat, and change the outcome from a Democrat to a Republican. That isn't solving the spoiler problem. That's not honoring majority rule. What is even the point of ranking candidates if your full preferences are not taken into account?

In approval, the Palin-first and Begich-second voters could have simply approved both Republicans, expressing their sincere preferences simultaneously and not conditionally. No need to worry that ranking the less electable candidate *first* might eliminate your viable second choice. Since a large majority of the Peltola-first voters preferred Begich to Palin, as well, it's very likely that Begich would have won in Approval voting, earning second-choice support from both Palin-first voters and Peltola-first voters.

### A sign of things to come

It's often claimed that Condorcet failures are rare in IRV elections. Little blips that should be ignored. But this is actually a much more fundamental issue with the basic structure of IRV itself.

The primary mechanism by which this happens is called the "Center Squeeze". When a moderate and acceptable candidate (like Begich) is sandwiched between two more extreme option, the more extreme options can "squeeze out" the moderate option in first place votes, leading to an early elimination of the moderate candidate, even if that moderate would beat both extremes in head-to-head match-ups. The system is too short-sighted and does not properly utilize the information it's actually collecting from voters.

It should also be mentioned that, with ballot exhaustion, the winner might not even be ranked on a majority of ballots (as Peltola was not). This is how IRV achieves its so-called "majority". If all candidates a voter ranked are eliminated, their ballot is thrown out and has no say in the rest of the process. The promise of majority rule in IRV is at best a misleading claim made from ignorance, and at worst a blatant lie. Take [this San Francisco IRV election](https://ranked.vote/report/us/ca/sfo/2024/11/supervisor-d11) <d-cite key="rankedVote2024sfD11"></d-cite> where the winner won the final round by being ranked higher on just 37.2% of the total ballots cast. That is not majority rule in any meaningful sense. It is entirely artificial.

But [a report by Atkinson, Foley, and Ganz](https://illinoislawreview.org/wp-content/uploads/2024/11/Atkinson-Foley-Ganz.pdf) <d-cite key="atkinsonFoleyGanz2024polarization"></d-cite> suggests that this problem would be far worse in bimodal swing states like Arizona, Nevada, and Georgia, where the electorate is deeply divided. But also in states like South Carolina, Mississippi, Alabama, and Delaware. The distance between where the IRV winners and Condorcet winners lie is significantly larger in these states. In the report, Alaska actually appears to be, relatively speaking, one of the better states (near the middle of the distribution). If Alaska has already had a Condorcet failure with IRV, then it seems like this may be a sign of what could happen far more frequently if IRV is adopted in more places, rather than an isolated, rare event.

> "While it has been offered as a solution to polarization, our results show that IRV cannot be expected to effectively lead to representative outcomes relative to other election systems. Reformers concerned with polarization should look to other ranked-choice methods. As shown in our simulations, a Condorcet electoral method will tend to elect candidates much closer to the state’s median and mean voter, especially for highly polarized states with bimodal electorates." -(Atkinson, Foley, Ganz 2024)

Also in the report,

> "As we will see, the center squeeze is generally more severe in the states with more polarized partisanship distributions." -(Atkinson, Foley, Ganz 2024)

IRV may actually *exacerbate* polarized outcomes, rather than mitigate them, and Condorcet failures may be far more common in the most politically relevant swing states. But it was bad across the board: simulations done in the report had Condorcet failures in approximately **40% of all elections across all states**.

It seems only reasonable that *if* we must adopt a ranked method (which I am not convinced that we should), we should at least choose one that satisfies the Condorcet criterion. Otherwise, the system is not internally consistent, which erodes (if not destroys) public confidence and trust in the method, setting back the electoral reform movement as a whole. If the electorate becomes disillusioned with IRV, are they going to be willing to try another method?

This makes choosing a robust method *imperative*. The idea that we can pick a "transitional", flawed method like IRV, and then "fix it later" is a dangerous gamble that may backfire spectacularly. If we wish to have trust in our elections and democracy, and have the reform method stick, we **must** have a method that is internally consistent.

### Why not Condorcet?

The clear fix if we want to keep ranking candidates is to employ a Condorcet method instead. There are many to choose from, such as Minimax, Schulze, or Copeland. All of these methods will always elect the Condorcet winner if one exists, thus satisfying internal consistency (at least when one exists).

If one is to use a ranked method, the only sane way to do so is to use a Condorcet method. If you *can* fail to elect the Condorcet winner, you *will* erode public trust in the method, and thus the entire reform effort.

In complete fairness, Condorcet methods, if implemented optimally, would not likely be completely unweildy in all cases. If you use a sane method, like Ranked Robin, where voters can rank candidates equally and simply count how many ballots rank A over B, you can likely get the winner faster than STAR voting, which needs the scores in *addition* to the head-to-head talies for full precinct summability. But when a candidate who wins all their head-to-head match-ups does not exist, then it starts to get extremely tricky.

A running theme of the post is that expressiveness often comes at a cost of consistency and practicality. One issue with Condorcet methods is that the more complex ranked ballot can fail to create a Condorcet winner, due to cycles in preferences (e.g., A beats B, B beats C, and C beats A). We have seen this in real elections: for example, in [Minnesota](https://ranked.vote/report/us/mn/2021/11/ward-2) <d-cite key="rankedVote2021minneapolisWard2"></d-cite>. In such cases, we must have a reasonable and justifiable way to break the cycle. In that way, we still lose guaranteed internal consistency. In the case of a cycle, no matter who you pick, another candidate was preferred by more voters in a head-to-head matchup.

Without a Condorcet cycle, a Condorcet method will be generally quite good. Apart from the general complexity of ranked voting, requiring much more new infrastructure to count and audit things optimally, etc. But when a Condorcet cycle does exist, the method can become very complex and opaque. And it can be very difficult to explain to voters how that tie was broken fairly. Can a rushed voter in line open the [Wikipedia page for the Schulze method](https://en.wikipedia.org/wiki/Schulze_method) and understand how their ballot will be counted? Can you explain it simply to your grandmother who worries the election will be stolen? What about to a legislator who needs to be able to write it into law in a way that is understandable and unambiguous?

I know someone who tried to explain Schulze to the board members of Mensa, and they rejected it for being too complex. If Mensa *leaders*, certified *geniuses*, find it too complex for practical use, how can we expect the average voter to trust it in a high stakes political election? **Simplicity is a prerequisite for trust.** We cannot rely on a blackbox, theoretically perfect but opaque method, to run our elections. Not in the era of "stop the steal" and rampant election conspiracy theories.

If you cannot explain how the winner was chosen to your grandmother, who sends you articles about how the election was stolen, then that method is not practical for real-world use in the United States. What happens when the Condorcet winner is one who wins head-to-head with only a minority of ballot ranking them above her favorite? Will voters accept that outcome? You still have to take all the numbers and explain why the winner is legitimate. "But my candidate won by more first-choice votes!" "But my candidate won against your candidate by more head-to-head votes!" This is particularly glaring in the case of a cycle, but this applies to the existence of a Condorcet winner as well. If the Condorcet winner would have gotten last place, when looking just at first-choice votes, that's still a little iffy. The idea that the candidate won a majority over every other candidate is surely the strongest possible claim to legitimacy, especially if we want to claim the ranked data was used faithfully, but it may not be convincing to every voter. Condorcet-conistency is the most robust way to define internal consistency for ranked methods, but it still may not be sufficient to convince everyone of legitimacy.

So while Condorcet methods are more internally consistent than IRV, they still have significant practical drawbacks. They still face the complexity issues of ranked ballots, which would be particularly problematic in smaller local elections with low visibility. In our current system, it is often hard enough to pick a single comptroller or school board member, if you don't know any of the candidates. Asking voters to rank all of them is a big ask, and asking them to understand a complex counting method is even more so if no candidate wins all their head-to-head matchups.

Condorcet methods like Copeland or Minimax are probably the least difficult to legislate and explain. A [report by Mathematica indicates that one of the simplest methods, Copeland may be the most robust Condorcet method](https://www.mathematica.org/api/sitecore/MediaLibrary/ActualDownload?fileId=%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileName=Mathematica_VotingSim_FINAL_Sep2025.pdf&fileData=Mathematica_VotingSim_FINAL_Sep2025.pdf%20-%20%7BE313E9D5-F43B-4B45-B774-790034A48935%7D&fileMime=application%2Fpdf) <d-cite key="mathematica2025altVotingRules"></d-cite>, but one must also specify with it a tie-breaking procedure to put it into law, since it very often produces ties when a cycle exists.

A Condorcet method is at least slightly more precinct-summable than IRV, since each precinct can report the head-to-head tallies between each pair of candidates: the ballots with A > B, the ballots with B > A, and ballots indifferent ($$N^2(N-1)$$ numbers for $$N$$ candidates, though just $$N(N-1)+1$$ is needed), and then the overall winner can be determined from those tallies. However, this is still significantly more complex than Approval voting, which only requires $$N$$ numbers to be reported from each precinct. Also losing the benefits of utilizing existing plurality infrastructure for quick counts and audits.

If your goal is to have a practical and cost-effective reform that can be widely adopted and trusted, then Condorcet methods are still far too complex and expensive to be practical for widespread real-world use in the United States.

The primary benefit of a ranked method is that greater expressiveness. The only case to be made that a ranked Condorcet method would be better than Approval voting is if that expressiveness is worth the costs by actually delivering superior outcomes. But do they?

## The Information Problem

No matter what voting system you use, you must destroy some information. But, since it is simply impractical to ask every voter to write an essay about which candidates they like and should win, and aggregate that into a single coherent decision, we must settle for some compromise, such as ranking, scoring, or approving candidates. Remember, we are taking potentially millions of ballots and trying to aggregate them into a single winner. This is *inherently* lossy.

Every system has its trade-offs, and destroys some information about voter preferences. On one hand, we want to maximize expressiveness of what the voter can express, but we also need to balance that with practicality. In that end, we have to decide which information is most important to preserve, and what information we are willing to destroy.

- Plurality requires the voter to pick exactly one candidate to provide support, throwing out all other information about alternatives they would have preferred, find acceptable, or even *like*.
- Ranked methods get the *ordinal* information about preferences, but fail to capture intensity or acceptability. A voter who ranked A > B > C cannot express if they would find B acceptable or not. We can only know that they prefer A more than B, and B more than C.
- Cardinal methods with more than two possible scores (like Score voting) are ambiguous about what the scores mean. Is a 3/5 candidate "acceptable" or not? Different voters may interpret the scores differently.
- Approval voting requires the voter to split the candidates into exactly two tiers: which are "acceptable" (approved) and which are "not acceptable" (not approved). This collapses all the information of their potentially nuanced preferences into a binary choice for each candidate.

I believe that Approval asks the most practical and, arguably, *important* question: which candidates would you find acceptable as the winner? Who do you consent to govern you? This is a binary question that voters must give an unambiguous answer to for each candidate, and cannot be limited to a single choice. That excludes plurality from being able to capture the answer to this question, and it also cannot unamibiguously be captured by any ranked or non-binary cardinal method.

Out of all of these compromises, I think the easiest to justify are Approval voting and ranked methods (but only if the way the rankings are aggregated is Condorcet consistent). Both are unambiguous about the expressed preferences of the voter.

However, in addition to the objective greater simplicity of Approval over a ranked Condorcet method, and the fact that it asks the more important question, Approval voting maintains greater internal consistency than a Condorcet method, while also being "*good enough*".

## Approval Voting and Internal Consistency

Both Approval voting and plurality voting, if the ballots are taken to be perfectly accurate expressions of voter preferences, are necessarily internally consistent. Both create and assume a world where only the candidates that are voted for are acceptable, and all others are not acceptable. Whoever gets the most votes is thus the best candidate in that simplified world.

However, the plausibility and legitimacy of each of these simplified worlds is very different. For it is far more reasonable to assume that voters can find multiple candidates acceptable, than to assume that they find literally all but one candidate completely unacceptable.

Further, the fact that voters must pick only one candidate forces them into strategic dilemmas. To have an impact on the election, a voter must pick only a viable candidate, even if they find other candidates more acceptable. This means that we can trust their expressed plurality preference (as sincere) far less.

It is undeniably true that the plurality winner got the most votes. But that is only when voters were taken hostage, and forced to pick only one candidate. In a tight presidential election, we often run into cases where the difference between the top two candidates is far less than the number of votes that third-party candidates received. This weakens the legitimacy and "internal consistency" of plurality voting.

Whereas, such a race under Approval voting would allow voters who strongly prefer third-party candidates to also approve of a viable major party candidate, allowing them to express their sincere preferences without fear of "wasting" their vote, and adding legitimacy to the ultimate winner. No more "Al Gore would have won if Ralph Nader hadn't run" scenarios, or cries of "spoiler!". The winner got more votes when voters had the option to approve of *multiple candidates*. That is a much stronger claim to victory. More people consented to be governed by the winner than any loser, end of story.

Further, the sincerity incentives under Approval voting are very strong, so we can trust that the expressed preferences are *at least* more accurate, and truer to the actual preferences of the voters. We can reasonably assume that the candidates they approve of are at least preferable to those they do not approve of. This is a strong compromise between the overly lossy plurality world, and an ideal ranked world.

### You can't prove it's not Condorcet

When discussing the technical Condorcet consistency of Approval voting, based on assumed dichotomous preferences, someone said it's a "You can't prove it's not Condorcet" method, and I found that hilarious and apt.

In my other post on Approval voting, I showed that Approval is Condorcet-consistent with the expressed dichotomous preferences of the electorate. The proof is simple, but best illustrated with an example (though, a general proof is given in the [Appendix](#appendix)).:

For example, if W got 100 approvals and C got 80 approvals, and there were 70 ballots that approved both W and C, then:

- W's strict approvals = 100 - 70 = 30
- C's strict approvals = 80 - 70 = 10
- Difference in total approvals = 100 - 80 = 20
- Difference in strict approvals = 30 - 10 = 20. It's exactly the same!

Thus, if W has more total approvals than C, then W must also have more strict approvals than C.

That is, the Approval winner must necessarily have more strict approvals than any other candidate, and thus must win every head-to-head matchup based on the data it actually collected on the ballots. Therefore, Approval voting is Condorcet-consistent with the expressed preferences of the electorate.

Despite being far more expressive than plurality, its ability to express ordinal ranking is limited. But it still asks, in my view, the most important question: Who do you consent to govern you? And it does so in a way that is unambiguous and easy to understand. By simply finding the candidate that the most voters say "yes" to, this makes Approval voting a compromise that attempts to satisfy the most voters, while still being ultimately practical, and reaping most of the benefits of the far more complicated Condorcet methods.

Despite technically being a cardinal SCORE or RANGE system (where voters rate a candidate out of either 0 or 1), Approval is actually the only SCORE system that *is* always internally consistent. See the [Appendix](#appendix) for a detailed proof and example of this for both SCORE and STAR voting.

Now, I would never say that absurd pathological examples mean SCORE or STAR would not be fine in practice. But, again, in a "stop the steal" era, I do not believe we can afford to allow any such internal inconsistencies that could erode public trust in the method. Not to mention, these systems would fail to have all the logistical benefits of Approval voting, since they require more complex ballots and counting, and can't be run on existing infrastructure as easily. But, I feel I must at least address these systems, as they are often in the conversation of electoral reform.

In this way, Approval voting is uniquely positioned at the nexus of Ranked and Cardinal methods. It avoids the complexity of ranked methods, by being a cardinal method. But it's also the uniquely internally consistent cardinal method through its simplicity. **Simplicity begets internal consistency**. And, while it does achieve simplicity through reduced expressiveness, it still manages to capture the most important information about voter preferences: acceptability, while also being ultimately practical.

You see, Approval is not just 100% Condorcet-consistent with the expressed preferences, but is also surprisingly effective at electing the ranked Condorcet winner in practice!

So, what does a ranked system have above Approval voting? Well, the obvious answer is that it allows for a specific type of granularity of expression: the ordinal ranking of candidates. We have already seen that only a Condorcet method can properly use that information in an internally consistent manner, at the cost of complexity. Is that extra information worth the cost?

## The Condorcet Approximation of Approval Voting

At the start of this post, I pitched Approval voting as the engineering solution: the "good enough" straight line approximation of the most robust ranked methods. Strictly better than plurality, while avoiding all the complexity.

I claim that Approval voting is the "line of best fit" of Condorcet methods: simpler, easier to work with, far less expensive, more practical, and less opaque.

Simulations put the true Condorcet-efficiency of Approval voting at around [67% to 84%](https://www.degruyterbrill.com/document/doi/10.1515/9781400859504.15/html) <d-cite key="merrill1988condorcetEfficiency"></d-cite>, depending on the model and parameters used. Real world data is limited because there are not many real-world elections that collect both approval and ranked data. But a [1985 Institute of Management Sciences (TIMS) election](https://www.jstor.org/stable/2632078) <d-cite key="fishburnLittle1988approvalExperiment"></d-cite> where both approval and ranking data were collected showed approval voting elected a candidate with substantially broader support than the plurality winner, despite a near-tie in pairwise comparisons.

Critically, the plurality winner C, won by 8 first-place votes over candidate B. However, in inferred pairwise matchups of those who expressed preference, C ended up winning over B by only 1 vote (B > C: 900, C > B: 901) with 27 indifferent votes (see the [Appendix](#appendix) for how these numbers were arrived at). This makes C the technical Condorcet winner by a single vote, but without solid confidence. However, B won strongly over C in Approval voting with 1,038 for B to 908 for C (based on actual ballots cast).

This highlights the contrast between an approval winner and a ranked Condorcet winner. It's possible more people said they preferred C over B, but far more people found B acceptable than C.

Approval voting has high fidelity to the true Condorcet winner, without being beholden to them in every case. In my view, this makes it *better* than Condorcet methods in practice, because I am not convinced that the true Condorcet winner is always the best candidate to elect in every case.

Brams proves in his 2008 book ["Mathematics and Democracy"](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy) <d-cite key="brams2008mathDemocracy"></d-cite> (pg 39) that Approval voting outcomes are "strongly stable" if and only if the winner is a unique Condorcet winner. Stability here refers to the ability for coalitions or groups of voters to manipulate the outcome in a favorable way by changing their strategies.

Further, [certain intuitive strategies (Laslier)](https://journals.sagepub.com/doi/10.1177/0951629808097286) <d-cite key="laslier2009leaderRule"></d-cite> paradoxically increase the efficiency (potentially up to 100%), only requiring knowledge of the top two viable candidates.

This means that Condorcet winners have a sort of stability and gravitational pull in Approval voting, but only if they manage to be acceptable enough to be voted for by the electorate. An inoffensive Condorcet winner, who is such only because they are everyone's second choice, may not be able to win if they cannot inspire sufficient approval.

Approval outcomes are inherently indeterminate with respect to the ranked preferences of the electorate. Even if you do not change the rankings that voters have, different approval thresholds can lead to different winners. This means that the Approval winner is not necessarily the "true" Condorcet winner, but rather the candidate who is most acceptable to the electorate given a certain level of acceptability.

If a Condorcet winner fails to be sufficiently acceptable to the electorate, then perhaps they should not win. There is a persistent myth that Approval voting elects the bland, milquetoast, inoffensive, beige wall, "everyone's second choice" candidate who stands for nothing. This is simply not true. While having broad, widespread acceptability is important, you should also aim to have sufficient intensity of support, to excite that broad base to actually approve you on their ballots. The candidate who can inspire passionate support while also building bridges to be appealing to a broad audience is the candidate who would ultimately win under Approval voting. [Steven Brams suggests that Ronald Reagan would likely do very well under Approval voting](https://www.youtube.com/watch?v=BZiS3U7EG0M), and is not at all a bland candidate. I think Eisenhower, FDR, Theodore Roosevelt, and Obama would also do very well in an Approval system by being both exciting and widely appealing.

A polarizing Condorcet winner may not be the best candidate to elect either. Consider the following example, where the Condorcet winner has only minority support:

- 45% of voters rank A > B, and approve both A and B.
- 35% of voters rank B > A, and approve only B.
- 20% of voters rank only C, and approve only C.

In this case, A is technically the Condorcet (and IRV) winner, since we can't know how the C voters would rank A vs B. We only see that at least 45% prefer A over B, and at least 35% prefer B over A. We have an asymmetry where A and C are very polarizing and B is broadly acceptable. The A voters find B an acceptable compromise, while the B voters find A an unacceptable lesser evil to the extremely unpopular C. Due to the truncated rankings, we had no way of knowing who the true Condorcet winner is, but a Condorcet method would have to pick A, despite only minority support.

Approval on the other hand, would elect B with 80% approval (45% + 35%), over A with only 45% approval, and C with only 20% approval. Contrived as it may be, this example illustrates a key point: the "majority" Condorcet winner does not necessarily hold more legitimacy than a non-Condorcet winner who is far more broadly acceptable.

Who should win is ultimately a values judgement. However, here is the kicker: with only the Approval data, nobody can claim that B is *not* a Condorcet winner in the first place, because Approval voting does not capture that information.

The internal consistency instead will show that 35% more voters found B acceptable, and A unacceptable than vice versa. "You can't prove B is not the Condorcet winner"! Because there's no ranked data to consult, voters see a clear winner based on the only information available: who earned the most approval. This transparency preserves trust, even if the outcome might differ from a hypothetical Condorcet method. In short, the question the system asks is simply different from a Condorcet method, but both consistently pick the most legitimate candidate based on the question the ballot asks.

One might object that this is a weakness. That we have swindled the true Condorcet winner out of their rightful victory by destroying information. However, this cuts both ways. If nearly twice as many voters find B acceptable over A, then a Condorcet method would swindle the electorate out of a consensus candidate in favor of a polarizing candidate who only has minority support.

Ranked ballots destroy acceptability information, and thus cannot guarantee that the "Condorcet winner" is actually acceptable to the electorate. We must choose which information to preserve, and which to destroy.

Regardless, however, Approval voting still manages to elect the ranked Condorcet winner a strong majority of the time in practice, while being far simpler and more practical than any ranked method, all the while maintaining that strong internal consistency, guaranteeing the legitimacy just as a Condorcet method would, while being simple enough that voters would *actually be able to TRUST it*. This is the ultimate compromise.

## Conclusion

Approval voting is not just theoretically elegant, it is also the most practical voting system for real-world use. If you want a simple voting reform, which is easy to implement, and would be trusted by voters, there is literally no simpler choice than Approval voting.

The proposed ranked systems like IRV (which are not Condorcet-consistent) are needlessly complicated, difficult to understand, difficult to count, difficult to audit, difficult to trust, fail to deliver on their promises of majority rule, and fail to be internally consistent.

Condorcet methods, while more internally consistent, will eventually hit a cycle, and then become needlessly complicated and difficult to understand, legislate, count, audit, and trust.

Any ranked method necessarily falls into at least one of the following categories:

1. Too complicated for the average voter to understand or verify the results in all cases.
2. A conspiracy-breeding blackbox that is necessarily less trustworthy than our existing dead-simple plurality system (which is already distrusted enough as is).
3. Fails to be internally consistent with the expressed preferences of the electorate (ex. any non-Condorcet method)
4. Too logistically impractical and expensive to implement and efficiently audit in large scale elections.

Any one of these reasons is, in my view, disqualifying for real-world use. And, it appears that people are catching on. In Snead's testimony, he mentions the $100 million dollar effort to put IRV on the ballot in six states in 2024, and all failed by "overwhelming bipartisan margins". [Alaska is going to attempt to repeal it in 2026. Again.](https://ballotpedia.org/Alaska_Repeal_Top-Four_Ranked-Choice_Voting_Initiative_(2026)) If it's repealed, that may signal the death knell for IRV in the United States. And those pushing for Approval voting or STAR voting are going to be saying "We told you this would happen". If IRV fails, we must learn from its mistakes and pick a robust, practical, and trustworthy method next time.

Approval voting strikes the perfect balance between simplicity, practicality, internal consistency, and (sufficient in practice) Condorcet-efficiency. It is the best choice for real-world elections.

[Cox 1987](https://www.jstor.org/stable/2111325) <d-cite key="cox1987electoralEquilibrium"></d-cite> also indicates that Approval voting would encourage candidates to seek broad acceptability, potentially diffussing polarization over time, while plurality encourages extremism.

In summary, Approval voting is

- Practical: The acceptability question is **simple to ask and tally**. Approval voting is logistically practical, working on existing machines and infrastructure, and far simpler to understand, administrate, legislate, **trust**, and interact with than any ranked system.
- Internally consistent and robust: Approval voting always respects the expressed preferences of the electorate in a consistent manner, guaranteeing legitimacy of the winner.
- Empirically Condorcet-efficient: Approval voting elects the ranked Condorcet winner a strong majority of the time, while being far simpler and more practical than any ranked method. Regardless, even when it does not, it still, without fail, elects the most broadly acceptable candidate.

---

## Appendix

The post is over, but here I wish to include some mathematical proofs and examples for some of the claims made in this post, for interested readers.

**Approval Condorcet Consistency Proof**: Suppose candidate W is the Approval winner, and candidate C is any other candidate. If $$\gamma$$ is the number of ballots that approve both W and C, and $$x_W$$ and $$x_C$$ are the total approvals for W and C respectively, then $$x_W - \gamma$$ is the number of strict approvals for W (ballots that approve W but not C), and $$x_C - \gamma$$ is the number of strict approvals for C (ballots that approve C but not W).

The difference in strict approvals is:

$$(x_W - \gamma) - (x_C - \gamma) = x_W - x_C$$

Therefore, the difference in strict approvals is exactly that of total approvals. If W has more total approvals than C ($$x_W > x_C$$), then W must also have more strict approvals than C. Thus, W wins the head-to-head matchup against C based on the expressed dichotomous preferences of the electorate. Since this holds for any candidate C, W is the Condorcet winner based on the expressed dichotomous preferences.

---

**Score internal inconsistency example**: If you allow just one more tier than Approval in a SCORE system (like being able to rate candidates 0, 1, or 2), then you immediately lose internal consistency and ballot-based Condorcet consistency. Suppose we have two candidates, A and B, and 101 voters, and assume that we are using a SCORE voting system with more than 2 levels. If there were only two levels, this would be Approval voting which is consistent, as proven above. Without loss of generality, let's assume we have just three levels. The following example works regardless of how many levels there are. If the 101 voters have the following scores:

- 48 voters scored candidate A as 2, and candidate B as 0.
- 3 voters scored candidate A as 2, and candidate B as 1.
- 50 voters scored candidate A as 0, and candidate B as 2.
  
We then have that 51 voters prefer A over B (the first two groups), while only 50 voters prefer B over A (the last group). Thus, A is the Condorcet winner. But candidate A would lose with 102 points to B's 103 points, despite being preferred over B by a majority of voters. To avoid this, the second bloc of voters might strategically lower B's score to 0, and now it's just Approval voting again. A SCORE system with more than two levels is actually just Approval voting, but voters can give fractional approvals.

This is something STAR voting tries to solve by adding a runoff at the end, but doesn't manage to fix completely (while also adding complexity).

**STAR internal inconsistency example**: STAR voting uses a score ballot (0-5), but then has a runoff between the top two scoring candidates, where each ballot counts as one vote for whichever of the two runoff candidates was scored higher.
Take this example:

- 11 voters score A:5, B:4, C:3
- 10 voters score A:0, B:3, C:5

In total, A has 55 points, B has 74 points, and C has 83 points. So C and B go to the runoff, and B wins the runoff by one vote (11 to 10). But A was preferred over B and C by a majority of voters. This is a particularly nefarious example, since not only did the Condorcet winner not win, but the candidate with the highest total score didn't win either. Both losing candidates have a valid claim to victory.

The purpose of this example is that by allowing voters to be *more* expressive than just "approve" (1) or "disapprove" (0), we lose both:

1. Simplicity and the ability to run on existing infrastructure
2. Guaranteed internal consistency with the expressed preferences of the electorate.

In that the purpose of this post is to argue that Approval voting is uniquely positioned as the simultaneously simplest, most practical, and most robust method we could adopt, I do believe potential for such pathologies, and the lack of the major logistical advantages that Approval voting offers, is disqualifying.

**Alaska Failure Numbers**: In the [2022 Alaska special election for US House](https://ranked.vote/report/us/ak/2022/08/cd), the candidates had the following first choice votes:

- Mary Peltola (D): 74,840
- Sarah Palin (R): 58,582
- Nick Begich (R): 52,798

The difference between Palin and Begich is 5,784 votes. To flip the result, we need

$$ \frac{5,784}{2} + 1 = 2,893 \text{ votes} $$

to go from Palin-first ballots to Begich-first ballots. This would change the totals to:

- Sarah Palin (R): 58,582 - 2,893 = 55,689
- Nick Begich (R): 52,798 + 2,893 = 55,691

Since 33,308 ballots ranked Palin-first and Begich-second, that makes it just 8.69% of those voters to change the result (and [4.94% of Palin's 58,582 first-choice total](https://substack.com/home/post/p-182659376) <d-cite key="mahlendorf2026fearVoteSplitting"></d-cite>). Since swapping Palin and Begich at the top of the ballot does not change the head-to-head matchups with Peltola, the final rounds would still be identical: Begich would beat Peltola, but Palin would have lost to Peltola.

This highlights the path-dependence of IRV, due to its Condorcet-inconsistency. These swaps would only weaken the head-to-head of Palin vs Begich. It doesn't change that Palin is a Condorcet loser, or that Begich is the Condorcet winner. Nor does it change the head-to-head results of Peltola against either candidate. At least with a Condorcet method we could just count the head-to-head tallies directly, and Begich's victory would be very clear and obvious, and robust to small changes in voter preferences. Therefore, IRV is less robust than a Condorcet method, while being harder to administer. It's the worst of both worlds.

**1985 Professional Society Election Example**: Candidate A was not at all competitive, so we focus on candidates B and C.

In first choice votes, B received 827 votes, and C received 835 votes, a difference of 8 votes in favor of C. When examining the expressed ranked preferences, we find:

- 70 voters ranked ABC (B > C)
- 66 voters ranked ACB (C > B)

This results in a net difference of 4 votes in favor of B (70 - 66 = 4), which closes the lead of C to just 4 votes (B > C: 897, B > C: 901). However, there were 3 voters who approved both A and B, which naturally implies a preference of B > C. Adding these 3 votes to B's total gives us B > C: 900, C > B: 901. With 27 voters not expressing a preference between B and C (voting only for A, and neglecting to provide any further information), we arrive at a dead heat based on expressed preferences.

It gets even closer if we assume that the 27 voters who only voted for A match the proportion of preferences expressed by the other 139 (70+66+3) voters:

$$ \frac{70+3}{139}\cdot 27 =14.2\approx 14 \text{ voters for }B>C $$

$$ \frac{66}{139}\cdot 27 =12.8\approx 13 \text{ voters for }C>B $$

This gives both B and C 914 votes in the inferred pairwise matchup, a perfect tie. This makes it really difficult to determine who the true Condorcet winner is based on the expressed preferences.
