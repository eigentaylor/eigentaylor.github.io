---
layout: distill
title: Approval is a Condorcet Method
date: 2026-03-25
description: Approval is the perfect Condorcet method, and I have permanently solved the Condorcet paradox. April Fools!
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
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
    subsections:
      - name: Condorcet is an Approximation
  - name: Generalized Condorcet Methods
  - name: Limited Tiers and the Condorcet Paradox
    subsections:
      - name: A Remark on Precinct Summability
  - name: You can't prove it's not Condorcet
    slug: you-cant-prove-its-not-condorcet
    subsections:
      - name: A Remark on Legitimacy
  - name: You cannot be serious
    subsections:
      - name: What about the outcomes?
        slug: what-about-the-outcomes
      - name: Domain Restriction
  - name: Conclusion
  - name: Appendix
    subsections:
      - name: The Fine Print
  - name: References
---

## Introduction

Merry April Foolsmas, everyone! Fellow Condorcetists, I come bearing a gift: I have permanently solved the Condorcet paradox. There is in fact a *perfect* voting system! It is called Approval voting, and it *is* indeed a Condorcet method.

[For an actually serious argument on the fact that Approval is a practical Condorcet approximation, see this post.](../practicalapproval){:target="_blank"} However, I feel this is a fair argument that, in a practical sense, Approval is the "perfect" Condorcet method, so long as one is [aware of the fine print](#the-fine-print){:target="_blank"}.

During the time of the French revolution, two titans battled out their ideas of what a good voting system was: Their names were Jean-Charles de Borda and the Marquis de Condorcet.

- Borda: Believed that we should give candidates points based on where they are ranked. My lowest ranked candidate gets zero. Next up gets one, and so on. Equivalently, the candidate with the best average ranking wins.
- Condorcet: Had a much better idea. He believed that we should always elect a candidate which we now call a *Condorcet winner*: a candidate who would defeat every other candidate in a one-on-one election.

But it is impractical to hold an election for every $\frac{n(n-1)}{2}$ pair of candidates, or to put all possible one-on-one matchups for all candidates on the ballot given to each voter. Take the mayoral election in Portland from 2024, which had 19 candidates. That would require voters to consider $\frac{19 \cdot 18}{2} = 171$ different matchups just to elect a mayor. So we need a voting system that can be used in a single election, is not preposterously hostile to voters, and still satisfies the *spirit* of the Condorcet criterion: if there is a Condorcet winner, *and voters express this through their ballots*, then they should win.

> **Definition:** A *Condorcet winner* is a candidate who would defeat every other candidate in a one-on-one election, based purely on the ballot data of voters who express an explicit preference.\label{def:condorcet-winner}

We compromise on the idea that we can simulate how voters would vote in each theoretical matchup by ranking candidates. If I rank Alice first, Bob and Clark tied for second, and Dylan last, then a Condorcet method interprets this *only* as me saying that

- I would vote for Alice over Bob, Alice over Clark, and Alice over Dylan.
- I would vote for Bob over Dylan, and Clark over Dylan.

The single ranked ballot thus allows us to simulate how voters *might* vote in each theoretical matchup, and thus have an idea if there is a Condorcet winner. By ranking Bob and Clark equally, I am indicating that I have no preference between them in a head-to-head matchup. We make only a single assumption:

> **Axiom:** If a voter submits a ranked ballot, we assume only one thing about that voter's preferences: If a voter ranks candidate A above candidate B, then they would vote for A over B in a head-to-head matchup. If a voter ranks A and B equally, then they have no preference between A and B in a head-to-head matchup.\label{ax:ranked-ballot-assumption}

If there is a candidate who would defeat every other candidate in a head-to-head matchup based purely on the ballot data's indication of the above assumption, then we must assume they are the Condorcet winner, and by golly, they should win!

The value of this criterion is felt most strongly in the contrapositive. If the ballots indicate that a candidate would be defeated by any single other candidate in a runoff, then they would not have a strong claim of legitimacy if declared the winner.

The main drawback of a ranked method is that while it captures ordinal preferences, it cannot capture the distance between those choices. Borda explicitly exacerbates this problem to the extreme by assuming *exact* equidistance between ranks in the units of points. For example,

| Voters | 1st Rank | 2nd Rank | 3rd Rank |
|--------|----------|----------|----------|
| 3      | Alice    | Bob      | Clark    |
| 2      | Bob      | Clark    | Alice    |

Then Alice gets $3(2)+2(0)=6$ points. Bob earns $3(1)+2(2)=7$ points. Even though Alice was preferred over Bob by a majority (60%) of voters, Bob was elected instead. Personally, I wouldn't have a problem believing that Bob might be a more acceptable candidate, since they were not as polarizing as Alice, but the ranked ballot data is clear: If you don't elect Alice, then you are subverting the will of the majority. That's not a great way to maintain legitimacy in your elected leader.

### Condorcet is an Approximation

The use of rankings to infer one-on-one preferences is an approximation. Every Condorcetist must be honest about this. **So long as we do not directly ask how a voter would vote in every possible matchup, we cannot guarantee that there is a Condorcet winner, nor that we did, in fact, find them.**

That is precisely Axiom \ref{ax:ranked-ballot-assumption}: We go entirely off of what the majority of voters who explicitly expressed a preference between two candidates indicated.

This is a *huge* assumption. It is a *huge* compromise. But it makes the voting system *tractable*. Why can't a voter express that they would vote for Alice over Bob, they would vote for Bob over Clark, but they would vote for Clark over Alice? By restricting voters arbitrarily to a ranking, we are choosing to completely throw away all possible non-transitive preferences alongside all information about the distance and intensity of preferences. We Condorcetists are *all* about throwing away certain information so that preferences are easier to aggregate and treat faithfully!

> **Definition:** A voting system satisfies the *Condorcet criterion* if whenever there is a candidate who would defeat every other candidate in a head-to-head matchup **based on the ballot data of voters who expressed a preference between the two candidates**, then that candidate must win.

If you do not elect such a candidate, then **what are you even** ***doing***? [Why ask for rankings if you aren't even going to use or respect them?](../ditch-rcv){:target="_blank"} If you do not elect such a candidate, then you have elected someone else who has to serve their constituents knowing that a majority of voters wanted someone else more. That creates a [legitimacy problem](../consistentcardinal){:target="_blank"}.

We also cannot guarantee that even if we elect the Condorcet winner induced by the ballots, that this candidate would truly defeat every other candidate in a head-to-head matchup, because we are not asking all those direct head-to-head questions. Especially if we allow ties or ballot truncation.

Take the Alaska 2022 special election, for example. I have discussed that election extensively in recent posts. However, I will focus entirely on a single aspect relevant to Condorcet analysis.

Condorcetists, including myself, claim that Begich was the true Condorcet winner, who was eliminated by the ranked-choice voting tabulation that did not faithfully treat the expressed preferences of voters.

There were nearly 190,000 voters in this election, according to [ranked.vote](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}. Over 33,000 voters ranked Palin first and Begich second, while over 20,000 voters ranked Palin first and no other candidate second. If less than 3,000 of those Palin first and Begich second voters had instead ranked Begich first and Palin second, then Begich would have won the ranked-choice tabulation.

RCV was short-sighted, and interpreted the clear expressed preference of "I would take Palin *and* Begich over Peltola" in a way that ultimately led to the election of Peltola directly. This is *not* a faithful treatment of the voters' expressed preferences.

However, what Condorcetists often neglect to mention is that because so many voters who ranked Palin first did not rank a second choice, we have no idea how they would vote in a Begich vs. Peltola head-to-head matchup. While of those who did express a preference between Begich and Peltola, a majority preferred Begich, this was not a majority of all voters who cast a ballot, but rather approximately 46%. We report the number as 52.5% of voters who expressed a preference between Begich and Peltola preferred Begich, but it's *not* 52.5% of all voters.

Therefore, we cannot be certain that Begich was the true Condorcet winner, because if all of the unaccounted for votes had gone entirely to Peltola in a head-to-head matchup against Begich, then Begich would not have defeated Peltola. This is exceptionally unlikely, but because we did not collect that information, we cannot be 100% certain.

As Condorcetists, we have to rely exclusively on the expressed ballot data, and trust that of those who *did* express a preference between two candidates, the majority preference accurately reflects who would win in a head-to-head matchup. We value the expressed distinguished preferences over potential unexpressed preferences.

Now, hopefully we are on the same page about what it truly means, in practice, to be a Condorcet winner, given the limitations of the ballot data.

The biggest question is, however, does such a candidate even exist? How likely is it that if we hold an election with hundreds, thousands, or even millions of voters, that there will be a single candidate who would be ranked above every other candidate by a majority of voters in the ballot data? It turns out the answer can be 100%, or not 100%, depending on the system.

## Generalized Condorcet Methods

This is not a concept I have ever heard of anyone defining, but it's my post, so I get to make it up! At its core, a typical Condorcet method assumes the ability to be able to give a full ranking of all available candidates. Please excuse me for a moment while I move the goalpost.

> **Definition:** A *Generalized Condorcet method* (GCM) is a voting system where voters can rank all candidates, with ties allowed, among some predetermined number of tiers. If a voter ranks candidate X strictly over candidate Y, then that voter casts a vote for X in the X vs Y matchup. If there is a candidate who wins all of their matchups, then that candidate is declared the Condorcet winner and *must* win. We denote a GCM with $k\geq 2$ tiers as $C_k$. If there is no limit on the number of tiers, then we denote it as $C_\infty$.

If $k$ is smaller than the number of candidates, then a voter will necessarily express some number of ties, by the Pigeonhole principle.

$C_6$ is equivalent to voters assigning candidates 0 through 5 stars or points, but we do not treat this as a point system, necessarily. It is still a Condorcet method. We interpret that if a voter gives a candidate, say, three stars, then that voter casts a vote for that candidate over all candidates with two, one, or zero stars, as well as a vote for all candidates with four or five stars over them (but no assumption about other candidates who also get three stars). For $C_3$, this could be assigning candidates "good", "okay", and "bad". And for $C_2$ this is declaring candidates "acceptable" or "unacceptable". While it does not affect the math we discuss in this post, we generally assume that a truncated ballot (ex. a voter who does not rank a candidate) ranks all non-ranked candidates in the bottom tier.

If 100 voters rank Alice above Bob, and 50 voters rank Bob above Alice, while 600 voters rank Alice and Bob equally, then we choose to assume that Alice defeats Bob and Bob does not defeat Alice. If there is a candidate who defeats every other candidate, then we assume they are the Condorcet winner, and they must win. We would do this if this electorate of 750 voters had 100 possible ranks or fewer.

We treat the voting system as a function $C_k(P)$, for $k \geq 2$, including $k = \infty$, that takes in a profile $P$ of ballot preferences (compatible with $C_k$) and outputs a single winner. If there is a Condorcet winner, then that candidate must be the unique winner.

> **Axiom:** If no candidate wins all of their matchups, based on the ballot data $P$, then we make no assumption about which candidate is the Condorcet winner or should win. If $P$ induces no Condorcet winner, then we make no assumption about the outcome of $C_k(P)$, and allow that any candidate could potentially be the winner.

Essentially, $C_k$ can be an arbitrary function, so long as it agrees on the Condorcet winner when one exists. It could elect them alphabetically for all we care in the case of a cycle.

Generally, a Condorcet method always chooses the same number of tiers as there are candidates, so that voters could theoretically rank all candidates in a complete transitive order, which is effectively $C_\infty$. But we investigate what happens when we restrict the number of tiers.

## Limited Tiers and the Condorcet Paradox

We first establish a simple Axiom to make the following analysis clean.

> **Axiom:** (Unique winner) We assume that at most one candidate has no strict pairwise loss in any profile $P$. \label{ax:unique-winner}

This axiom allows us to disregard the possibility of a Condorcet method having to choose between multiple weak Condorcet winners in the absence of a cycle. We also define a compact notation for pairwise comparisons:

> **Definition:** For candidates $A$ and $B$, let $P(A>B)$ denote the number, or proportion, of voters who rank candidate $A$ strictly above candidate $B$ in their ballot. Similarly, let $P(B>A)$ denote the number, or proportion, of voters who rank candidate $B$ strictly above candidate $A$.

By our definition of a Condorcet winner, candidate $A$ is a Condorcet winner if and only if $P(A>B)>P(B>A)$ for all other candidates $B$.

> **Lemma:** A Condorcet winner can fail to exist in $C_k$ if $k>2$. \label{condorcet-paradox}

**Proof:** Consider the following profile of 3 voters:

| Voters | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 1      | Rock     | Scissors | Paper    |
| 1      | Scissors | Paper    | Rock     |
| 1      | Paper    | Rock     | Scissors |

In this profile, Rock defeats Scissors (a majority of voters rank Rock above Scissors), Scissors defeats Paper, and Paper defeats Rock. There is no Condorcet winner, and this only requires 3 or more tiers. $\square$

This is not an abstract result. While very rare, Condorcet cycles have occurred in real U.S. elections, such as a [Minnesota city council election in 2021](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}.

> **Definition:** For $C_2$, we denote $S(A)$ as the number of voters who put candidate $A$ in the upper tier, which we call the "approved tier". We denote $S(A>B)=P(A>B)$ as the number of "strict approvals" of $A$ over $B$--voters who put candidate $A$ in the approved tier and candidate $B$ in the not approved tier. And $S(A=B)$ as the number of voters who put both candidates in the approved tier. This does not include voters who put both candidates in the not approved tier.

Thus, $S(A)=S(A>B)+S(A=B)$, and $S(B)=S(B>A)+S(A=B)$.

> **Lemma:** Candidate $A$ defeats candidate $B$ pairwise in $C_2$ if and only if more voters put $A$ in the approved tier.

\begin{equation}
S(A>B)>S(B>A) \iff S(A)>S(B)
\end{equation}

**Proof:** If more voters put $A$ in the approved tier, then $S(A)>S(B)$. Thus, $S(A>B)+S(A=B)>S(B>A)+S(A=B)$, implies that $S(A>B)>S(B>A)$ by cancellation of $S(A=B)$, meaning $A$ defeats $B$. Conversely, if $A$ defeats $B$, then $S(A>B)>S(B>A)$, so $S(A)=S(A>B)+S(A=B)>S(B>A)+S(A=B)=S(B)$. $\square$

We now define Approval voting.

> **Definition:** Approval voting is a voting method in which each voter can approve any number of candidates. The candidate who is approved by the most voters wins.

We now land the crushing blow.

> **Theorem:**
>
> 1. $C_2$ induces a transitive majority relation
> 2. There can never be a Condorcet paradox in $C_2$.
> 3. To determine the winner in $C_2$, it suffices to count the number of first ranks (approvals) each candidate receives. The candidate who is in the upper tier of the most voters is the Condorcet winner and will win.
> 4. $C_2$ is the unique GCM that satisfies any of the first three properties. They do not hold for any $C_k$ where $k>2$.
> 5. Therefore, $C_2$ is exactly Approval voting, which is hence the unique Generalized Condorcet Method that never admits a Condorcet paradox.

**Proof:** This follows directly from the previous result.

**Claim 1:** By the previous lemma, $A$ defeats $B$ if and only if $S(A)>S(B)$. Thus, the ordinal ranking of candidates by $S(\cdot)$ is the same as the majority relation. Since the ordinal ranking of candidates by $S(\cdot)$ is a sequence of real numbers, it is totally ordered and thus transitive.

**Claim 2:** Claim 1 directly implies the absence of a Condorcet paradox in $C_2$. Suppose that $A$ defeats $B$, and $B$ defeats $C$. Then $S(A)>S(B)$ and $S(B)>S(C)$, so $S(A)>S(C)$ by transitivity of the real numbers, so $A$ defeats $C$.

**Claim 3:** As a Condorcet method, $C_2$ must elect the Condorcet winner whenever one exists. By the previous lemma, the candidate with the most first ranks (approvals) is the Condorcet winner. Therefore, $C_2$ always elects the candidate with the most approvals, and that candidate will always be the Condorcet winner.

**Claim 4:** We now show that any $C_k$ where $k>2$ cannot satisfy any of the previous three properties. Any $C_k$ where $k>2$ can admit a Condorcet paradox by Lemma \ref{condorcet-paradox}, so it cannot satisfy the first two properties. To conclude the proof, we show that if $k>2$ then a candidate with the most first ranks is not necessarily the Condorcet winner. Consider the following profile:

| Voter  | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 3      | A        | B        | C        |
| 2      | B        | C        | A        |
| 2      | C        | B        | A        |

In this profile, $A$ has the most first ranks, but $B$ defeats both $A$ and $C$, so $A$ is not the Condorcet winner.

Claims 1 through 3 establish that $C_2$ is precisely approval voting, proving that Approval is a Generalized Condorcet Method that never admits a Condorcet paradox. Claim 4 establishes that Approval voting is the unique Generalized Condorcet Method with this property. $\square$

This leads to the pièce de résistance:

> **Theorem:** Approval voting is perfectly Condorcet-consistent. It elects the Condorcet winner without fail in every single election with a unique winner, with no exceptions.\label{thm:approval-condorcet}

**Proof:** Claim 3 of the previous theorem states that the candidate with the most approvals is always the Condorcet winner. By Axiom \ref{ax:unique-winner}, that candidate is unique. Therefore Approval voting elects the Condorcet winner in every election, based on Definition \ref{def:condorcet-winner}. $\square$



Boom, Approval is the *only Condorcet method that can guarantee the existence of a Condorcet winner in every election*.

<img src="/assets/img/approvalcondorcetmeme1.jpg" alt="Approval is not two-tiered score, but two tiered Condorcet" style="width:100%; max-width:600px;">

Note: As I was writing this post, I was researching related arguments and I found out that [Charles Munger wrote a paper in 2023 proving that Approval is a two-tiered Condorcet method](https://bettervotingmethods.com/s/ApprovalRangeStarVoting030323.pdf){:target="_blank"}. Even hardcore Condorcetists know Approval is a Condorcet method! His conclusion is that Approval voting is a degenerate Condorcet method with worse outcomes. However, while I actually generally agree with his criticisms of Range and STAR voting, I think that in practice Approval really is just a more practical Condorcet method. [This is a pretty good argument in that regard](https://rangevoting.org/AppCW.html){:target="_blank"}.

### A Remark on Precinct Summability

Approval voting is very clearly precinct summable. We have proved that it is a Generalized Condorcet Method which only needs the total number of approvals each candidate receives to determine all pairwise matchups.

General Condorcet Methods, including $C_\infty$, are also technically precinct summable, unlike a method like RCV which absolutely requires [central tabulation](../ditch-rcv){:target="_blank"}. However, the practicality decreases as the number of candidates increases. For 19 candidates, a precinct would potentially need to report the number of voters who prefer each candidate over each other candidate, which is $19(18) = 342$ numbers, which is considerably more cumbersome than simply reporting 19 approval counts. However, it is technically fewer numbers than STAR voting, which would require reporting all of these numbers alongside the total scores for each candidate ($19^2=361$) for full summability that wouldn't require a later tabulation of the runoff numbers.

In fairness, optimizations could be made for both systems. It might be possible to reduce the number of reported numbers by considering $A>B$ rankings $+1$ and $B>A$ rankings a $-1$, and counting only the margins in each $\frac{n(n-1)}{2}$ pairwise matchup. But that's still over 170 numbers to put on the gymnasium door for a 19 candidate race. That's quadratic growth to Approvals linear.

## You can't prove it's not Condorcet

As we have proved, Approval voting is indeed a Condorcet method, just restricted to two tiers. This is a restriction to binary "acceptable" vs "unacceptable" preferences, just as a ranked method is a restriction of an arbitrary preference ordering to a transitive one. But as a Condorcet method, it always elects the candidate who would win all pairwise matchups against other candidates based on the preferences expressed in the ballot data.

As with *any* Condorcet method, all we have to go on is what voters express. Consider the following example in Approval voting between Alice, Bob, and Clark:

| Voters | True Preferences | Approvals |
|--------|------------------|-----------|
| 45     | A > B > C        | A         |
| 35     | B > A > C        | B, A      |
| 20     | C > B > A        | C         |

Then Alice wins the Approval voting election, since she has the most approvals. Based on the ballots, she appears to be the Condorcet winner. But a careful look at the true preferences shows that Bob is actually the Condorcet winner, as he would win all pairwise matchups against the other candidates based on the full preference rankings.

But if we want to play the "let's make up a profile where voters act stupidly", then we can play that game. Just because voters can rank beyond two tiers does not mean they will, and thus a general Condorcet method is susceptible to ridiculous outcomes. Let's suppose we instead give them a full ranked ballot, with ties allowed, and they vote in $C_\infty$ as follows:

| Voters | True Preferences | $C_\infty$ Ballot |
|--------|------------------|-------------------|
| 45     | A > B > C        | A > B > C         |
| 35     | B > A > C        | B > A > C         |
| 20     | C > B > A        | C                 |

Perhaps Clark, knowing he has no chance, told his supporters to rank him first and nobody else, in a misguided attempt to game the election. Out of voters who expressed a preference between Alice and Bob, still more preferred Alice over Bob (45 (56.25%) to 35 (43.75%)). Therefore, Alice would still be elected. And, based on that ballots, you still wouldn't be able to prove that Alice was not the Condorcet winner either, just like in Approval.

Whether it be Approval or $C_\infty$, the pathology of this scenario is that while Bob was the true Condorcet winner based on the full preferences, he was unable to convince the majority of voters who truly preferred him over Alice to express that preference on their ballots. Given that real voters truncate their ballots, this is a realistic concern.

I have my issues with utility arguments, and range voting methods, but let's pretend we magically know the utility that each candidate provides to each voter in this example (just as Condorcetists pretend to know the pairwise preferences that voters express in Approval voting).

| Voters | A Utility | B Utility | C Utility | Ranking   | Approvals |
|--------|-----------|-----------|-----------|-----------|-----------|
| 45     | 10        | 3         | 0         | A > B > C | A         |
| 35     | 9         | 10        | 0         | B > A > C | B, A      |
| 20     | 0         | 1         | 10        | C > B > A | C         |

In this scenario, Alice is a much higher utility option (765) for the electorate than the true Condorcet winner Bob (505). Perhaps Alice is a firebrand progressive candidate who excites her 45% base, who finds a milquetoast candidate like Bob unexciting. And perhaps, a substantial minority of moderate voters *slightly* prefers Bob over Alice, but would be genuinely happy with either one. The minority of Clark supporters hate both Alice and Bob, and preferring Bob is like preferring losing a kidney over losing a liver. Both awful, but if *forced* to pick one, they would pick Bob.

This is not to argue that utility maximization should be the goal of an election, especially because that's not the data we collect in a Condorcet method. But the utilities show the approvals are not necessarily irrational in this context. If this is genuinely how the voters feel, then I see no reason that Alice is an unreasonable winner. Under this dynamic, Alice is clearly a better compromise for the electorate as a whole than Bob, given that the Bob supporters seem to genuinely like Alice.

Most Condorcet winners are not like this, in my opinion. And when they are genuinely good, I have no doubt that Approval voting would likely elect them. But in cases like the one above, where the Condorcet winner is only marginally preferred by a lukewarm majority, Approval voting can reasonably elect a candidate who is actually acceptable to a larger portion of the electorate. The [1985 Institute of Management Sciences (TIMS) election](https://www.jstor.org/stable/2632078){:target="_blank"} is a good example that shows a narrow (and ambiguous) Condorcet winner can be defeated by a candidate who is more broadly acceptable to the electorate. See [this post](../practicalapproval){:target="_blank"} where I discuss it in more detail.

### A Remark on Legitimacy

However, unlike any ranked method, [or scoring method with three or more options](../consistentcardinal){:target="_blank"}, Approval never admits a case where another candidate has a legitimate claim to victory over the actual elected candidate, who is a Condorcet winner based on the ballot data.

Simply, any candidate loses an Approval voting election if and only if it was a skill issue. To be blunt, losing an Approval election is entirely the candidate's fault for not earning enough approvals from the voters. While the case could be made that this is true in plurality voting as well, it cannot be done quite as cleanly.

Unlike choose-one plurality voting, in Approval voting, the third party supporters can voter for the third party *and* for the viable alternative. If they have the pen in their hand, and look at your name, and say "no thanks", then that is entirely your fault for not being able to convince them to support you. *Skill issue*.

Similarly, if there was an underlying Condorcet winner who just couldn't convince their majority to approve them due to their majority preference being sufficiently lukewarm, then in that case, all I can say is, "cry about it".

Rather than wax poetic about utility maximization, I go the Condorcet route: If a voter ranks (or approves) Alice above Bob, then all we can say is that they would vote for Alice over Bob in a theoretical one-on-one matchup. As Condorcetists, we do not assume any information about how they would vote in matchups they did not express a preference for. We just take the ballot data at face value, and if Alice is ranked above Bob by more voters than Bob is ranked above Alice, then we say that Alice defeats Bob.

This does not, in my opinion, lose significant meaning when we restrict to two tiers. Under the conditions of the ballot, if more voters express they would vote for Alice over Bob than the other way around, then that does indeed show something meaningful about the relative popularity and acceptability of Alice and Bob.

In Approval there is no "but I got more first choice votes" argument to be made against a legitimate Condorcet winner, because the Condorcet winner is such *because* they convinced the most voters to approve them over any other candidate in a one-on-one comparison.

In Approval there is no "but I was ranked by more voters over the winner" argument, as in Ranked Choice Voting. And Condorcet can't escape this either, because when a Condorcet cycle inevitably occurs, there is no winner who doesn't lose to at least one other candidate in a one-on-one matchup. So much for "legitimacy" to the winner in those cases. Approval has no cycles, and therefore no ambiguity about who the legitimate winner is based on the ballot data.

My adherence and loyalty to the Condorcet criterion is not because I think the theoretical winner in all one-on-one plurality runoffs is actually the best candidate if there is potentially a better and less polarizing compromise. My loyalty is for the *legitimacy* of the criterion in the only data that truly matters: what the ballots collect.

<img src="/assets/img/approvalcondorcetmeme2.jpg" alt="Approval is the cool Condorcet method" style="width:100%; max-width:600px;">

## You cannot be serious

Oh, but I am. Mostly. Half-and-half.

Here's what is absolutely true: Because no Condorcet method asks voters to directly vote in every possible head-to-head matchup, we cannot assume that any ranked method can perfectly capture the Condorcet winner in all cases, because you simply cannot assume all voters have transitive preferences over all candidates, *and* you can't force voters to completely rank all candidates without ties unless you want to bottleneck turnout.

In reality, Approval voting is, in my opinion, "Condorcet-lite". It's not a Condorcet method *proper*, but I would absolutely say a "generalized" Condorcet method is an appropriate name. Condorcetists simplify messy preferences to a transitive ranking to make determining a Condorcet winner tractable and practical.

Approval just goes one step further with this logic and simplifies the ballot to make it completely consistent and ultimately practical. But it is still, at its core, fundamentally electing the candidate who is ranked strictly above any other candidate by a majority of voters who express a preference. And Approval inherits the base legitimacy of any system that does this reliably (Condorcet methods), along with the legitimacy that comes from simplified ballot data.

Here's the truth: At the time of writing, Condorcet would be my second choice over Approval. If Approval *didn't* show clear data that it was essentially *just* as good as a full Condorcet method in practice, and if I didn't feel that [simplicity is paramount in this era of distrust](../practicalapproval){:target="_blank"}, then I wouldn't be advocating for Approval voting so strongly over a full Condorcet method. But the fact that Approval is simple, transparent, and *practically as good* makes the choice for me quite clear.

### What about the outcomes?

We have established that Approval is a two-tiered Condorcet method. While those like Munger would argue that this simplification comes at the cost of outcomes, I would argue that the cost is minimal for the benefits we get in return.

Approval has been shown to have [essentially the same level of outcomes](https://electionscience.github.io/vse-sim/VSEbasic/){:target="_blank"} as more complex Condorcet methods. Whereas Condorcet get about 86%-98% VSE, Approval gets 89%-95%. So Approval can be better than full Condorcet! And what do we gain in return for that three percent drop in maximum VSE?

We have mentioned thus far the simplicity to count Approval votes compared to more complex ranked methods, which balloon in complexity as the number of candidates increases. So it's exceptionally simpler to actually use in practice, which has nontrivial importance.

There is the fact that, unlike any other Generalized Condorcet method, Approval never "breaks" due to a cycle, because Approval has no cycles. Sorry, but I'm not quite ready to take an extra 3% in maximum VSE for a system that's more complicated and has a tiny chance to completely collapse if voters are sufficiently messy. I'll take the sturdy simplicity of a 95% system, that can promise it will never break, any day.

We have shown that there are cases where a candidate other than the Condorcet winner can be elected to satisfy a much larger proportion of the electorate than the ordinal preferences would indicate. But even so, Approval voting elects the Condorcet winner so often that these pathological cases are essentially negligible.

[I recommend taking a look at some Yee diagrams](http://zesty.ca/voting/sim/){:target="_blank"}, and trying to tell me if you can truly tell the difference between the Approval and Condorcet diagrams without your reading glasses.

And even *if* Approval voting occasionally elects a candidate who is not the Condorcet winner, we would literally never even know! The only thing we would see is the candidate who earned approvals from the most voters, and all the others who couldn't manage to convince as many voters.

I may make a future post about some of the mathematical nuances of Approval versus full Condorcet. Approval does technically satisfy IIA (Independence of Irrelevant Alternatives), which is a property that no other Condorcet method (or ranked method, for that matter) satisfies. [Steven Brams](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy){:target="_blank"} (Chapter 2) proved that Approval guarantees that any strong Nash equilibrium can only elect a Condorcet winner. And as I have previously posted about, [Approval is technically strategyproof under the goal of electing any "acceptable" candidate](../avstratproof){:target="_blank"}.

### Domain Restriction

Plurality voting, as a matter of fact, also satisfies many of the same properties we have proved for Approval. It is also technically a Condorcet method (based on the ballot data) if you assume that voters can only like a single candidate and equally dislike all other candidates. However, this isn't the gotcha some might think, as this is only true because plurality is just an arbitrary restriction on Approval voting. Approval voting is precisely the minimal level of ballot restriction we can place on a Condorcet method to ensure that it works 100% of the time. Or, from another framing, dichotomous (two-tiered) preferences are the maximal domain where Condorcet methods can operate perfectly.

All Condorcetists choose to simplify the data through some sort of limitation on what ballots voters can cast, for the purpose of making the system tractable and practical. And we have a hierarchy of compromises that a Condorcet method can make.

1. $C_\infty$ simplifies the data by assuming voters have transitive preferences, but allows all possible rankings at the cost of not being able to guarantee a Condorcet winner.
2. $C_2$ simplifies the data by assuming voters can project their preferences into a partition of candidates into "acceptable" and "unacceptable" sets. This is a simplification and compromise that results in the complete elimination of all issues that arise from the Condorcet paradox, while still generally electing the best candidate almost all of the time,
3. Plurality voting restricts $C_2$ to a single choice for the top tier, which allows it to maintain the properties of $C_2$, but is an arbitrary restriction that does not simplify the data significantly and leads to significantly worse outcomes.

$C_2$ is the maximal level that maintains a "reasonable" level of preference expression while still allowing the Condorcet method to work "perfectly". 

The fact is, I am an ultra pure Condorcetist. Purer than those who scoff at Approval voting, because I do not just think the Condorcet winner *should* be elected if they exist (in the ballot data). Instead, I believe that if your system cannot guarantee that a Condorcet winner *will* exist, then it's a broken system with no practical potential. Approval is the purest Condorcet method because it always elects and induces a Condorcet winner!

However, to bring back in a little bit of seriousness to this April fools post, I accept that some believe there is value in a more expressive voting system. In particular, if Approval voting elects the Condorcet winner via sincere strategies, then that was done via voters likely choosing one of many sincere strategies. A full ranked method has only one sincere strategy, and there is value to that.

Approval is indeed a truly an "indeterminate" kind of system. It's impossible to tell who will win based purely on underlying ordinal preferences. The Condorcet winner *usually does*, but there is no guarantee, and it does rely on voters applying strategies. But Laslier, [and others](https://rangevoting.org/AppCW.html){:target="_blank"}, make a good case that these strategies end up being coordinations of selfish self-interest that act as a heat-seeking missile towards the Condorcet winner at equilibrium.

Unlike those who claim that Ranked Choice Voting is "good enough" because it only failed to elect the Condorcet winner a tiny percent of the time, as if that [excuses everything that makes that system a disaster](../ditch-rcv){:target="_blank"}, calling Approval a Condorcet approximation is I think entirely fair. In practice, Approval voting will generally elect the Condorcet winner (100% of the time for those induced by the ballots), and is basically a Condorcet method, all the while being a simpler, more cost-effective choice, which works excellently without a hitch.

## Conclusion

In conclusion, Approval voting is a Condorcet method that changes the question from asking voters for a ranking which may or may not accurately reflect their preferences in one-on-one elections into a simpler, and arguably more important, question: who do you consent to govern you?

The latter question is binary and well defined. And because it is binary, it is impossible to induce a Condorcet paradox. If you are a fellow Condorcetist who scoffs that this question is *too* restrictive, then I reject that your arbitrary restriction is any less arbitrary than mine. While yours certainly allows for more complex expression of preferences, it also allows for the possibility of cycles and paradoxes, which can lead to less legitimate outcomes. My choice to simplify things down to acceptability has the following benefits, however:

1. Making the system far more practical for voters and administrators
2. Always induces and elects a Condorcet winner
3. Ensures full legitimacy to the winner in every possible election scenario. No other candidate can claim to be more deserving of the winner than the candidate with the most approvals.
4. Eliminates the possibility of a Condorcet paradox, ensuring a clear and decisive outcome in every election.
5. Simplifies the voting process, reducing cognitive load on voters and minimizing the potential for errors in ballot completion.
6. Voters who don't have the time to rank 10 candidates for Comptroller can still participate meaningfully by simply approving the candidates they find acceptable.

We absolutely restrict the expression of voters to do this. And it's a normative choice to make that practicality should be prioritized over the ability to express more complex preferences. But here's why I think it's the right choice:

1. Approval, in practice and in simulations, elects the true Condorcet winner exceptionally often, depending on strategy. [Up to 90% or more](https://doi.org/10.1515/9781400859504.15){:target="_blank"}. And even when it doesn't, you literally can't prove it. Approval gets you the same or more legitimacy than a Condorcet method would, but 100% of the time instead of 100% of the time minus cycles.
2. Also in simulations, Approval has been shown to have [essentially the same level of outcomes](https://electionscience.github.io/vse-sim/VSEbasic/){:target="_blank"} as more complex Condorcet methods. Whereas Ranked Robin gets up to about 98% VSE, Approval gets up to about 95%. That's 95% *with other benefits* as listed above that are lost to get just a few percentage points more.
3. In an era of distrust in institutions and elections, I believe that simplicity and clarity are a prerequisite for trust. And I do not trust that a generic Condorcet method is sufficiently simple and transparent (particularly in the case of a cycle, rare as they may be) in all cases to be a permanent solution. Approval is the only system I think is simple enough to be that permanent solution, and I think it *has to be the first step*. Approval today, Condorcet tomorrow is something I might be willing to get behind.

Fellow Condorcetists, let us unite behind the best and most practical Condorcet method: Approval voting!

And if you are a true Condorcetist who read this far, I would like to extend a genuine thanks for getting through this complete mathematical abuse of the term "Condorcet". However, I hope that it at least convinced you that Approval is, in fact, a two-tiered Condorcet method. Whether or not that changes your opinion of Approval, I leave that up to you!

## Appendix

### The Fine Print

To be perfectly clear: Approval voting is strategyproof under the goal of electing any acceptable candidate, if you can cleanly partition the candidates into "acceptable" and "unacceptable" sets, then voting according to that preference is optimal *under that goal*. But in general, Approval voting is not strategyproof for any realistic sense of voter preferences beyond completely black-and-white acceptability judgments. There are [strategies like the Leader Rule](../avstrategy){:target="_blank"} that help draw a line of acceptability optimally to get the most preferable possible outcome, which [increase the Condorcet efficiency](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"} of Approval voting (under the Leader rule, the only equilibria is also one where the Condorcet winner is elected), but Approval is not generally strategyproof.

While [Brams does indeed prove](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy){:target="_blank"} that if a unique Condorcet winner exists, then there is a strong Nash equilibrium under Approval voting that elects them, and any strong Nash equilibrium elects a unique Condorcet winner, he also proves that there are other Nash equilibria. A Condorcet loser can be a Nash equilibria, but never a strong one (it is only a strong Nash if a unique Condorcet winner is elected). A Condorcet winner can be elected under a profile which is not a Nash equilibrium at all, just like Brams all other Condorcet methods can. However, Approval can guarantee any strong Nash elects a Condorcet winner, and I believe that absolutely has value.

Further, IIA is only satisfied by Approval voting at the ballot level. The introduction of a candidate, for example, can indeed change the decision of a voter about whether or not to approve other candidates, because the new candidate may alter the voter's perception of which candidates are acceptable. For example, maybe I'd vote for Bob and Dylan against Clark. But if Alice suddenly enters the race, then screw Bob and Dylan! I love Alice so much I will only approve of her.

Similar things can be said about plurality level if you decide that "at the ballot level" is an acceptable loophole. Then, as a domain restriction, plurality also satisfies IIA. However, I do believe there is something to be said that dichotomous preferences, which are relatively realistic enough to be worth defining a voting system around, are more realistic than the extreme restriction of single-peaked preferences that plurality relies on. And the dichotomous preference domain is maximal to guarantee that a Condorcet method can be "perfect".

It is not a surprise that Approval is "perfect" on the domain of Dichotomous preferences, since that is *precisely* the domain that the ballot data accepts. But I do think it is surprising that Approval voting is genuinely a *kind* of Condorcet method (if you squint a bit).

I maintain that any ranked method does rely on a domain restriction of transitive preferences. This is an extremely minimal restriction for tractability. But I do think it does add a level of uncertainty to the claim that any ranked system can reliably capture the Condorcet winner when voters truncate their ballots, or have incomplete information about their preferences, or have intransitive preferences.

In contrast, Approval voting is up front about its massive domain restriction, but treats and aggregates the signal it gets from voters faithfully. I posit that the binary Approval voting question of "who do you consent to govern you?" is a practical choice because

1. It elects the true Condorcet winner so often
2. It makes the system more practical and accessible to voters, which is crucial for legitimacy and turnout
3. It gives more legitimacy than any other Condorcet method can guarantee

For these reasons alone, I consider myself the purest kind of Condorcetist: an Approval voting Condorcetist!

## References

Brams, S. J. (2008). *Mathematics and Democracy: Designing Better Voting and Fair-Division Procedures*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy){:target="_blank"}

Brams, S. J., & Fishburn, P. C. (1978). Approval Voting. *The American Political Science Review*, 72(3), 831-847. [https://doi.org/10.2307/1955105](https://doi.org/10.2307/1955105){:target="_blank"}

Cox, G. W. (1987). Electoral Equilibrium under Alternative Voting Institutions. *American Journal of Political Science*, 31(1), 82-108. [https://doi.org/10.2307/2111325](https://doi.org/10.2307/2111325){:target="_blank"}

Laslier, J. F. (2009). The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate. *Journal of Theoretical Politics*, 21(1), 113-136. [https://journals.sagepub.com/doi/10.1177/0951629808097286](https://journals.sagepub.com/doi/10.1177/0951629808097286){:target="_blank"}

Merrill, S. (1988). Condorcet Efficiency. In *Making Multicandidate Elections More Democratic* (pp. 15-29). Princeton University Press. [https://doi.org/10.1515/9781400859504.15](https://doi.org/10.1515/9781400859504.15){:target="_blank"}

Quinn, J. (2017). *Voter Satisfaction Efficiency (VSE) summary*. Center for Election Science. [https://electionscience.github.io/vse-sim/VSEbasic/](https://electionscience.github.io/vse-sim/VSEbasic/){:target="_blank"}

Ranked.Vote. (2022). *Alaska At-large Congressional District*. [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd){:target="_blank"}

Ranked.Vote. (2021). *Minneapolis City Council Ward 2*. [https://ranked.vote/report/us/mn/2021/11/ward-2](https://ranked.vote/report/us/mn/2021/11/ward-2){:target="_blank"}
