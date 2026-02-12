---
layout: distill
title: Deducing Possible Approval Outcomes from Ranked Ballots
date: 2026-01-29
description: A theoretical and practical exploration of cutting through the inherent indeterminacy of approval voting using ranked ballots. Exploring AK 2022 and a notable Minnesota election.
giscus_comments: true
importance: 2
tags: voting
category: polisci
featured: false
related_posts: true
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: The Indeterminacy of Approval Voting
  - name: The AV Critical Strategy Profile
  - name: Application to Ranked Ballots
  - name: What this can and cannot prove
    subsections:
      - name: You can't prove it's not Condorcet
  - name: References
---

## Introduction

> Approval voting (AV) is a voting method where each voter can "approve" of as many candidates as they like, and the candidate with the most approvals wins.

I have previously discussed the mathematical properties of AV, how a voter might be able to frame their vote as [sincere and strategyproof](../avstratproof){:target="_blank"}, given a [practical case](../practicalapproval){:target="_blank"} for its use in US elections, and also recently proven that [AV is the only internally consistent cardinal method](../consistentcardinal){:target="_blank"}.

In this post, I want to explore a particular and very fun exercise in deducing possible AV outcomes from ranked ballots. This is based on Chapter 2 of [Steven Brams' 2008 text *Mathematics and Democracy*](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy){:target="_blank"}.

## The Indeterminacy of Approval Voting

Something that is both a criticism and a feature of AV is that it captures something from a voter's preferences that a ranked ballot cannot: which candidates a voter would actually consent to govern them.

If a voter ranks candidates A > B > C, the ranked ballot can capture the *ordinal* preferences of the voter, but three different voters may submit the same ballot, while having very different *approval* preferences:

- Voter 1 only approves A. B and C are unacceptable, but B is the lesser of two evils.
- Voter 2 approves A and B. C is unacceptable. They prefer A *more* than B, but they would be okay with either.
- Voter 3 approves all three candidates. They prefer A > B > C, but they would be okay with any of them. Perhaps there is a fourth candidate D that they truly despise so much that they would be willing to accept any of A, B, or C over D.

Approval voting is often criticized for its lack of granularity in its ballot and ability to express preferences, but this is a values judgment. Voter 2 may strongly value that they can express that they find both A and B acceptable, and vote for them both equally *against* their least-preferred candidate C. They might fear that if they submit an honest ranked ballot, the system might elect C, which they find unacceptable, just because they ranked A first and B second.

If this sounds absurd, it has happened. In [Alaska's 2022 special election for US House](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}, voters who expressed an honest preference for Sarah Palin (R)-first and Nick Begich III (R)-second *did* in fact elect Mary Peltola (D) because of that sincerity. If 2,893 of voters who ranked Palin first and Begich second had simply switched the order of their first two rankings, the weaker candidate Palin would have been eliminated instead of the only Republican who could have beaten Peltola in the final round, Begich. Begich would have won because 52.5% of ballots expressing a preference between Begich and Peltola preferred Begich.

The issue is that a system like IRV (instant-runoff voting, AKA "ranked-choice voting") does not solve the [vote-splitting problem](https://substack.com/@akorky/p-182659376){:target="_blank"} since it does not properly consider the full rankings of voters. Who is eliminated first or second can entirely decide the winner, electing a candidate that a majority of voters would find someone else more preferable to.

Only a ranked Condorcet method can truly solve this vote-splitting problem, *generally* [at the cost of realistic practicality](../practicalapproval){:target="_blank"} (in the case of the particularly complicated methods, at least). But Approval voting also solves this problem because it counts all voters equally and simultaneously, rather than sequentially or conditionally, and does so while being eminently practical.

However, the cost of this practicality and simplicity is that AV does lose the granularity *within* the "approve" and "disapprove" buckets. And while this makes it very difficult to map an approval ballot into a ranked ballot, it also introduces a certain indeterminacy when considering how a ranked ballot might map into an approval ballot. Let's consider an example:

| Ballots | Count |
|---------|-------|
| Peltola > Begich > Palin | 25 |
| Peltola > Palin > Begich | 2 |
| Begich > Peltola > Palin | 8 |
| Begich > Palin > Peltola | 14 |
| Palin > Begich > Peltola | 18 |
| Palin > Peltola > Begich | 2 |
| Peltola only | 12 |
| Begich only | 6 |
| Palin only | 11 |

This a crude approximation of the Alaska 2022 special election results, with rounded numbers based on the percentages of such ballots reported. We have 98 total ballots here. This approximates the head-to-head preferences and first choice percentages quite well.

| Candidate | First Choice Votes |
|-----------|--------------------|
| Peltola   | 39 (39.8%) |
| Begich   | 28 (28.6%) |
| Palin     | 31 (31.6%) |

| Head-to-Head | Winner | Votes | Margin % |
|----------------------|--------|-------|--------|
| Peltola vs Begich    | Begich | Begich: 46, Peltola: 41 | 52.9% - 47.1% |
| Peltola vs Palin     | Peltola | Peltola: 47, Palin: 45 | 51.1% - 48.9% |
| Begich vs Palin      | Begich | Begich: 53, Palin: 33 | 61.6% - 38.4% |

Therefore, Begich is the Condorcet winner, beating both Peltola and Palin head-to-head. Peltola beats Palin head-to-head, and Palin is the Condorcet loser, losing to both other candidates head-to-head.

Consider the results of the election under AV if we assume different approval thresholds for each group of voters:

- If every voter only approves their first choice, Peltola wins with 39 approvals.
- If every voter approves their top two choices, Begich wins with 71 approvals.
- If we assume that anyone who ranks Palin first only approves Palin, anyone who ranks Palin second approves both Palin and their first choice, and anyone who ranks Palin last approves only their first choice, Palin wins with 47 approvals.

In this way, every candidate has a path to victory under Approval voting, depending on how we assume each group of voters sets their approval threshold. Even the Condorcet loser, Palin, who loses to Peltola 49-51 and to Begich 69-31.

## The AV Critical Strategy Profile

Steven Brams in *Mathematics and Democracy* describes a particular strategy profile for Approval voting that can be deduced from ranked ballots, called the "AV Critical Strategy Profile." This strategy profile is designed to essentially maximize the performance of a particular candidate assuming sincere strategies.

> Given a set of full candidate rankings, the **AV Critical Strategy Profile** (AVCSP) for candidate X is defined as follows:
> 1. If a voter ranks X last, then that voter only approves their top choice.
> 2. Otherwise, the voter approves X and all candidates they rank above x.

This gives an upper bound on the success of a candidate X under Approval voting, assuming all voters who don't rank X last find X acceptable enough to approve of them, and all voters who do rank X last minimize their approvals to only their top choice.

Brams proves the following results:

1. The AVCSP for candidate X maximizes the difference in the number of votes that candidate X receives over any other candidate y, assuming sincere strategies.
2. If a candidate X does not win under their AVCSP, then there is no way for X to win under Approval voting assuming sincere strategies.
3. If a candidate X is a unique Condorcet winner, then X also wins under their AVCSP. A Condorcet loser may also win under their AVCSP.

This gives us a way to analyze ranked ballots and deduce whether a particular candidate could possibly win under Approval voting, assuming sincere strategies.

## Application to Ranked Ballots

While the AVCSP is a theoretical tool used by Brams to pove properties of Approval voting, we can take the fundamental idea and apply it to analyze real-world elections that use ranked ballots.

> **Definition**: We say that a candidate X is **implicitly ranked** above candidate Y on a given voter's ranked ballot if either:
> 1. Both X and Y are ranked on the ballot, and X is ranked higher than Y.
> 2. X is ranked on the ballot, and Y is not ranked on the ballot.

This requires the assumption that unranked candidates are less preferred than any ranked candidate, which I believe is a reasonable assumption in most cases.

We define the "Ranked AV Upper Bound" (RAVUB) for candidate X based on the ballot data of an election as follows:

> Let M denote the set of major candidates in the election. The **Ranked AV Upper Bound** (RAVUB) for candidate X is defined as follows:
> 1. If candidate X is ranked on a voter's ballot, and X is implicitly ranked above some candidate Y in $$M\setminus\{X\}$$, then the voter approves X and all candidates they rank above X.
> 2. Otherwise, the voter only approves their top ranked candidate.

We specifically specify the requirements of "major candidates" to treat different ballots with the same implied preference structure the same. For example, if we were analyzing the Alaska 2022 special election, we would only consider Peltola, Begich, and Palin as major candidates. If we were looking at the RAVUB for Peltola, we would treat the following ballots equivalently:

- Palin > Begich
- Palin > Begich > Peltola
- Palin > Begich > Write-in
- Palin > Write-in > Begich
- Palin > Begich > Write-in > Peltola
- Palin > Begich > Peltola > Write-in
- Palin > Write-in > Begich > Peltola

They all imply the same preference structure of the major candidates: Palin > Begich > Peltola. Therefore, in all of these cases, the voter would only approve their top choice, Palin in the RAVUB for Peltola, since all voters clearly implicitly rank Peltola last among the major candidates.

This gives, in my estimation, the best balance we can hope for in studying real-world election data, since the reality is that many voters do not rank all candidates, and many places that use ranked ballots have direct ranking limits (for example, NYC 2025 only allows ranking up to five candidates). We choose not to make assumptions about unranked candidates beyond their relative ranking among the major candidates.

## What this can and cannot prove

Using the RAVUB, we can analyze ranked ballot data from real-world elections to deduce possible Approval voting outcomes. But the indeterminacy of Approval voting is something that must be kept in mind.

By calculating the RAVUBs for all the candidates, we should not rank the candidates by their RAVUB totals and assume that the highest RAVUB candidate is the "most likely" winner under Approval voting. Each RAVUB is an independent hypothetical election scenario, and the real insight comes from comparing things like "Does candidate X even win under their RAVUB?" or "By how much does candidate X win or lose under their RAVUB?"

## Case Studies

Let's take a look at two  real-world elections that used ranked ballots, and analyze them using the RAVUB. We won't go into excessive detail here, but I will link to the CSV files containing the ballot data I extracted for each election. Anyone can verify my results and tell me if I made any catastrophic errors in my calculations or in extracting the data. Feel free to reach out to me through Discord (eigentaylor) if you believe my data is miscounted. But take my results with a grain of salt.

You can view an interactive visualization of the RAVUB results for both elections [here](https://eigentaylor.github.io/AVCSP/){:target="_blank"}.

## Alaska 2022 Special Election for US House

I've spoken in-depth about this election in previous posts, so I won't rehash everything here. The key takeaway is that Nick Begich III was the Condorcet winner, beating both Mary Peltola and Sarah Palin head-to-head, but lost because he was eliminated first under IRV due to vote-splitting among Republican voters. However, his RAVUB shows an incredible performance:

| Candidate | First-Choice Votes | RAVUB Approvals |
|-----------|--------------------|-----------------|
| Begich    | 52,844 (27.48%)	| 135,457 (70.44%) |
| Peltola   | 74,867 (38.93%)	| 95,051 (49.43%) |
| Palin     | 58,620 (30.49%)	| 90,773 (47.21%) |

This being in their respective RAVUBs. I want to highlight the results for each RAVUB, because they are quite telling:

| Candidate | Begich RAVUB Approvals | Percentage |
|-----------|------------------------|------------|
| Begich    | 135,457                | 70.44%     |
| Peltola   | 75,500	               | 39.26%     |
| Palin     | 58,873	               | 30.62%     |

<img src="/assets/img/RAVUB/alaska_2022_Begich_Nick_ravub.png" alt="Alaska 2022 Begich RAVUB" style="width:100%; max-width:600px;">

| Candidate | Peltola RAVUB Approvals | Percentage |
|-----------|-------------------------|------------|
| Peltola   | 95,051                  | 49.43%     |
| Palin     | 58,690                  | 30.52%     |
| Begich    | 53,260                  | 27.70%     |

<img src="/assets/img/RAVUB/alaska_2022_Peltola_Mary_S_ravub.png" alt="Alaska 2022 Peltola RAVUB" style="width:100%; max-width:600px;">

| Candidate | Palin RAVUB Approvals | Percentage |
|-----------|-----------------------|------------|
| Palin     | 90,773                | 47.21%     |
| Peltola   | 74,997                | 39.00%     |
| Begich    | 53,253                | 27.69%     |

<img src="/assets/img/RAVUB/alaska_2022_Palin_Sarah_ravub.png" alt="Alaska 2022 Palin RAVUB" style="width:100%; max-width:600px;">

Begich wins handily under his RAVUB, with over 70% of approvals. Peltola wins under her RAVUB with just under 50% of approvals, and Palin wins under her RAVUB with just over 47% of approvals. This shows that Begich had the lowest floor, but also the highest ceiling under Approval voting, assuming sincere strategies.

Does this mean that had Alaska changed the method from IRV to Approval voting at the last second, Begich would have won? Not necessarily. While entirely possible that Begich could have won under Approval voting, it's impossible to guarantee that he would have actually gotten those second-choice approvals. Voters who ranked him between Peltola and Palin may not have found him sufficiently acceptable to approve of him.

I plan to make a post about the "Leader Rule" and its implications for Approval voting in the near future, which may shed more light on this question. Under that rule, if Begich was considered the "leader" or "challenger" (one of the top two candidates), the rule would put him in first place.

Keep in mind that this is an **upper bound** on Begich's performance under Approval voting, assuming sincere strategies. The fact that Begich's upper bound is over *70%* of ballots cast, however, compared to the under 50% upper bounds of both Peltola and Palin, is at least indicative that Begich was the most broadly acceptable candidate among the three, however.

## References

Brams, S. J. (2008). *Mathematics and Democracy: Designing Better Voting and Fair-Division Procedures*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy){:target="_blank"}

Mahlendorf, A. (2026). Fear of Vote Splitting. Substack. [https://substack.com/@akorky/p-182659376](https://substack.com/@akorky/p-182659376){:target="_blank"}

Ranked.Vote. (2022). *Alaska At-large Congressional District*. [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}