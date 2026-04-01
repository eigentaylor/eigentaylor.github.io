---
layout: distill
title: Approval is the Perfect Condorcet Method
date: 2026-04-01
description: Approval is a perfect Condorcet method, and I have permanently solved the Condorcet paradox. April Fools!
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
  - name: Condorcet and His Paradox
    subsections:
      - name: The Paradox
      - name: Condorcet is an Approximation
  - name: Generalized Condorcet Methods
  - name: Limited Tiers and the End of Paradoxes
  - name: You can't prove it's not Condorcet
    slug: you-cant-prove-its-not-condorcet
    subsections:
      - name: A Remark on Legitimacy
      - name: A Remark on Precinct Summability
  - name: You cannot be serious
    subsections:
      - name: What about the outcomes?
        slug: what-about-the-outcomes
      - name: Domain Restriction
  - name: Conclusion
  - name: References
---

## Introduction

Merry April Foolsmas, everyone! I have seen the light of the math, and I am now a *true* Condorcet purist.

Fellow Condorcetists, I come bearing a gift: I have permanently solved the Condorcet paradox. There is in fact a *perfect* voting system! It is called *Approval voting*, and it *is* indeed a Condorcet method.

[For an actually serious argument on the fact that Approval is a practical Condorcet approximation, see this post.](../practicalapproval){:target="_blank"} However, the math I am about to present is *dead serious*, even if *I* am not.

## Condorcet and His Paradox

During the time of the French Revolution, a titan came up with an idea that changed the way we think about voting systems forever. This was Marie Jean Antoine Nicolas de Caritat, Marquis de Condorcet. While that is an *awesome* name, we will just call him Condorcet.

Condorcet believed that we should always elect what we now call a *Condorcet winner*--a candidate who would defeat every other candidate in a one-on-one election. This is often held as the *gold* standard for a voting system (by *cool* people).

But it is impractical to hold an election for every $\frac{n(n-1)}{2}$ pair of candidates, or to put all possible one-on-one matchups for all candidates on the ballot given to each voter. Take [the mayoral election in Portland from 2024](https://en.wikipedia.org/wiki/2024_Portland,_Oregon,_mayoral_election), which had 19 candidates. That would require voters to consider $\frac{19 \cdot 18}{2} = 171$ different matchups just to elect a mayor. Would you vote for Candidate 1 or Candidate 2? Would you vote for Candidate 1 or Candidate 3? ... Would you vote for Candidate 18 or Candidate 19? That would be utterly *preposterous*.

So we need a voting system that can be used in a single election, is not absurdly hostile to voters, and still satisfies the *spirit* of the Condorcet criterion: if there is a Condorcet winner, *and voters express this through their ballots*, then they should win.

> **Definition:** A *Condorcet winner* is a candidate who would defeat every other candidate in a one-on-one election, based purely on the ballot data of voters who express an explicit preference.\label{def:condorcet-winner}

We compromise on the idea that we can simulate how voters would vote in each theoretical matchup by ranking candidates and assuming a transitive order. If I rank Alice first, Bob and Clark tied for second, and Dylan last, then a Condorcet method interprets this *only* as me saying that

- I would vote for Alice over Bob, Alice over Clark, and Alice over Dylan.
- I would vote for Bob over Dylan, and Clark over Dylan.
- Bob and Clark are *about the same*, I don't have a strong preference between them. Maybe they're both just meh, while Alice is amazing, and Dylan is terrible.

The single ranked ballot thus allows us to simulate how voters *might* vote in each theoretical matchup, and thus have an idea if there is a Condorcet winner. By ranking Bob and Clark equally, I am indicating that I have no preference between them in a head-to-head matchup. We make only a single assumption:

> **Axiom:** If a voter submits a ranked ballot, we assume only one thing about that voter's preferences: If a voter ranks candidate A above candidate B, then they would vote for A over B in a head-to-head matchup. That is, we assume the ranking implies transitive preferences. If a voter ranks A and B equally, then they have no preference between A and B in a head-to-head matchup. If more voters rank A above B than the reverse, we assume A defeats B.\label{ax:ranked-ballot-assumption}

If there is a candidate who would defeat every other candidate in a head-to-head matchup based purely on the ballot data, interpreted through the above assumption, then we must assume they are the Condorcet winner, and by golly, they should win!

The value of this criterion is felt most strongly in the contrapositive. If the ballots indicate that a candidate would be defeated by any single other candidate in a runoff, then they would not have a strong claim of legitimacy if declared the winner.

The main drawback of a ranked method is that while it captures ordinal preferences, it cannot capture the distance between those choices. The system proposed by Jean-Charles de Borda, who Condorcet criticized, explicitly exacerbates this problem to the extreme by assuming *exact* equidistance between ranks in the units of points. Out of $n$ candidates, Borda gives $n-r$ points for being rank $r$ on a ballot. So the worst gets 0 points, the next gets 1, and so on. Functionally, this is equivalent to electing the candidate with the best average ranking.

Condorcet claimed this system could rob a majority from their preferred candidate, even when the expressed ballots clearly show that majority preference.

**Example:**

| Voters | 1st Rank | 2nd Rank | 3rd Rank |
|--------|----------|----------|----------|
| 3      | Alice    | Bob      | Clark    |
| 2      | Bob      | Clark    | Alice    |

Using the Borda count, Alice gets $3-1=2$ points from each member of the majority for being ranked first, and $3-3=0$ points from the minority for being ranked third, adding up to 6 points. Bob earns $3-2=1$ point from each member of the majority, and $3-1=2$ points from each member of the minority, adding up to 7 points. Even though Alice was preferred over Bob by a majority (60%) of voters, Bob was elected instead.

Personally, I wouldn't have a problem believing that Bob might be a more acceptable compromise candidate, since he was not as polarizing as Alice. However, there are two possible issues.

Borda is exceptionally manipulable. What if the Bob supporters, knowing Alice has the majority, buried Alice at the bottom, just to game the system? But even so, the ranked ballot data is clear: If you don't elect Alice, then you are subverting the expressed will of the majority. That's not a great way to give legitimacy to your elected leader.

### The Paradox

Condorcet's solution sounds perfect, theoretically. I mean, if we can tell voters "this is the candidate who would have won against *every* other", then that would be amazing!

As with all things in voting theory, there's a catch. While a Condorcet winner exists *quite* often, it's still less than 100% of the time.

**Example:** Consider the following profile of 3 voters: \label{ex:cycle}

| Voters | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 1      | Rock     | Scissors | Paper    |
| 1      | Scissors | Paper    | Rock     |
| 1      | Paper    | Rock     | Scissors |

In this profile, Rock defeats Scissors (a majority of 2 voters rank Rock above Scissors). Similarly, Scissors defeats Paper. However, while we would expect that if Rock beats Scissors, and Scissors defeats Paper, then Rock must defeat Paper, another majority prefers Paper over Rock. Thus, there is no Condorcet winner. No matter who you elect, some other candidate can say, "but I would have defeated them!" There is no way to elect any candidate with full legitimacy based on these ballots.

### Condorcet is an Approximation

The use of rankings to infer one-on-one preferences is an approximation. Every Condorcetist must be honest about this. **So long as we do not directly ask how a voter would vote in every possible matchup, we cannot guarantee that there is a Condorcet winner, nor that we did, in fact, elect them.**

That is precisely Axiom \ref{ax:ranked-ballot-assumption}: We go entirely off of what the majority *of voters who explicitly expressed a preference* between two candidates indicated, rather than requiring a full majority to have expressed a preference.

This is a *huge* assumption and a *huge* compromise. But it makes the voting system *tractable*.

It is simply too impractical to expect every voter to strictly rank 19 candidates with no ties allowed, let alone vote in 171 choose-one matchups, particularly when considering the cognitive load and time required.

We are also implicitly assuming transitive preferences, which is a minor point. That is, we do not allow a voter to express that they would vote for Alice over Bob, they would vote for Bob over Clark, but they would vote for Clark over Alice.

The fact we are disregarding all information about the distance and intensity of preferences is its own can of worms, but I don't mind this quite as much. Going with a majoritarian framing of legitimacy via the question of who would win in a plurality runoff is a fair choice, I think.

All this to say, we Condorcetists are *all* about throwing away certain information so that preferences are easier to aggregate and treat faithfully!

> **Definition:** A voting system satisfies the *Condorcet criterion* if whenever there is a candidate who would defeat every other candidate in a head-to-head matchup **based on the ballot data of voters who expressed a preference between the two candidates**, then that candidate must win.

If you do not elect such a candidate in a ranked system, then **what are you even** ***doing***? [Why ask for rankings if you aren't even going to use or respect them?](../ditch-rcv){:target="_blank"} If you do not elect such a candidate, then you have elected someone else who has to serve their constituents knowing that a majority of voters wanted someone else more. That creates a [legitimacy problem](../consistentcardinal){:target="_blank"}.

We also cannot guarantee that even if we elect the Condorcet winner induced by the ballots, that candidate would truly defeat every other candidate in a head-to-head matchup, because we are not directly asking all of those head-to-head questions, especially when ties or ballot truncation are allowed.

Take the Alaska 2022 special election, for example. I have discussed that election extensively in recent posts. However, I will focus entirely on a single aspect relevant to Condorcet analysis.

Condorcetists, including myself, claim that Nick Begich was the true Condorcet winner, who was eliminated by the ranked-choice voting tabulation that did not faithfully treat the expressed preferences of voters.

There were approximately 190,000 voters in this election, according to [Electorama ABIF results](https://abif.electorama.com/id/2022-08-16_Alaska-U.S._Representative_(Special_General)#pairwise) and [ranked.vote](https://ranked.vote/report/us/ak/2022/08/cd). Over 33,000 voters ranked Sarah Palin first and Nick Begich second, while over 20,000 voters ranked Palin first and no other candidate second. If less than 3,000 of those Palin first and Begich second voters had instead ranked Begich first and Palin second, then Begich would have won the ranked-choice tabulation.

RCV was short-sighted, and interpreted the clear expressed preference of "I would take Palin over Peltola *and* Begich over Peltola" in a way that ultimately led to the election of Peltola directly. This is *not* a faithful treatment of the voters' expressed preferences. Particularly because a clear majority of *all ballots cast*--approximately 53%, over 60% of those who expressed a preference between Begich and Palin--had voters expressing a preference of Begich over Palin.

However, what Condorcetists often neglect to mention is that because so many voters who ranked Palin first did not rank a second choice, we *technically* have no idea how they would vote in a Begich vs. Peltola head-to-head matchup. While out of all voters *who did express a preference* between Begich and Peltola, a majority preferred Begich, this was not a majority *of all voters who cast a ballot*, but rather approximately 46% of all voters. We report this as 52.5% among voters who expressed a Begich-Peltola preference, but it's *not* 52.5% of all voters.

Therefore, we cannot be certain that Begich was the true Condorcet winner, because if all of the unaccounted for votes had gone entirely to Peltola in a head-to-head matchup against Begich, then Begich would not have defeated Peltola. This is exceptionally unlikely, but because we did not collect that information, we cannot be 100% certain.

As Condorcetists, we have to rely exclusively on the expressed ballot data, and trust that among those who *did* express a preference between two candidates, the majority preference accurately reflects who would win in a head-to-head matchup among the entire electorate. Just as Ranked Choice Voting exhausts ballots from voters who failed to rank any remaining candidates, Condorcetists also value expressed preferences over potential unexpressed preferences.

Now, hopefully we are on the same page about what it truly means, in practice, to be a Condorcet winner, given the limitations of the ballot data. The only sane way to implement a Condorcet method is to

1. Allow ties in a voter's ranking, and truncation, for the sake of the voter
2. Define a Condorcet winner purely based on the ballot data, and Condorcet efficiency based on electing a candidate who is a Condorcet winner (based on the ballot data) when one exists

We saw in example \ref{ex:cycle} that a Condorcet winner does not always exist. But can they be forced to exist in every election if we just... make the system *better*? The answer may surprise you.

## Generalized Condorcet Methods

This is not a concept I have ever heard of anyone defining, but it's my post, so I get to make it up! At its core, a typical Condorcet method assumes the ability to give a full ranking of all available candidates if the voter is able to. Please excuse me for a moment while I move the goalpost.

> **Definition:** A *Generalized Condorcet method* (GCM) is a voting system where voters can rank all candidates, with ties allowed, among some predetermined number of tiers, with no other restrictions. If a voter ranks candidate X strictly over candidate Y, then that voter casts a vote for X in the X vs Y matchup. If a voter ranks candidate X in the same tier as Y, they abstain in the matchup. If there is a candidate who wins all of their matchups, then that candidate is declared the Condorcet winner and *must* win. We denote a GCM with $k\geq 2$ tiers as $C_k$. If there is no limit on the number of tiers, then we denote it as $C_\infty$.

If $k$ is smaller than the number of candidates, then a voter will necessarily have to express some number of ties, by the Pigeonhole principle.

$C_3$ would be like assigning candidates "good", "okay", and "bad". In this system, the voter expresses that they would vote for all "good" candidates over all "okay" and "bad", and all "okay" over all "bad". And for $C_2$ this is declaring candidates "acceptable" or "unacceptable", only assuming all "acceptable" are preferable to all "unacceptable".

$C_1$ does not really make sense as a system--it would be a trivial system where ballots say nothing and every voter is assumed to be indifferent between all of them. Plurality/choose-one voting does not fit in as a GCM, as it's an arbitrary restriction on $C_2$ where voters can only put a single candidate in the upper tier.

If 100 voters rank Alice above Bob, and 50 voters rank Bob above Alice, while 600 voters rank Alice and Bob equally, then we choose to assume that Alice defeats Bob and Bob does not defeat Alice. If there is a candidate who defeats every other candidate, then we assume they are the Condorcet winner, and they must win. We would assume this whether voters had had 100 possible tiers or just 2.

We treat the voting system as a function $C_k(P)=W$, for $k \geq 2$, including $k = \infty$, that takes in a profile $P$ of ballot preferences (having at most $k$ tiers) and outputs a single winner $W$. If there is a Condorcet winner induced by $P$, based on our axioms and definitions, then that candidate must be the unique winner output by the function.

> **Axiom:** If no candidate wins all of their matchups, based on the ballot data $P$, then we make no assumption about which candidate is the Condorcet winner or should win. If $P$ induces no Condorcet winner, then we make no assumption about the outcome of $C_k(P)$, and allow that any candidate could potentially be the winner.

Essentially, $C_k$ can be an arbitrary function, so long as it agrees on the Condorcet winner when one exists. In the case of a cycle, it could elect them alphabetically for all we care.

Generally, a Condorcet method always chooses the same number of tiers as there are candidates, so that voters could theoretically rank all candidates in a complete transitive order. We consider this $C_\infty$. But we investigate what happens when we restrict the number of tiers.

## Limited Tiers and the End of Paradoxes

We first establish a simple Axiom to make the following analysis clean.

> **Axiom:** (Unique winner) We assume that at most one candidate has no strict pairwise loss in any profile $P$. \label{ax:unique-winner}

This axiom allows us to disregard the possibility of a Condorcet method having to choose between multiple weak Condorcet winners in the absence of a cycle. Say Alice defeats Clark, and Bob defeats Clark, but Alice and Bob tie. Neither Alice and Bob have a strict pairwise loss, so neither is a unique Condorcet winner. We don't consider such cases here.

> **Lemma:** A Condorcet winner can fail to exist in $C_k$ if $k>2$. \label{condorcet-paradox}

**Proof:** By example \ref{ex:cycle}, we can see that any GCM that allows three tiers can result in no Condorcet winner. This example works for any $k\geq 3$, so a Condorcet winner can fail to exist for any $k\geq 3$. $\square$

This is not an abstract result. While very rare, Condorcet cycles have occurred in real U.S. elections, such as a [Minneapolis city council election in 2021](https://ranked.vote/report/us/mn/2021/11/ward-2).

> **Definition:** For $C_2$, we use the following notation. The two tiers are called the "approved tier" and the "unapproved tier". For candidates $A$ and $B$:
>
> - $S(A)$: the number of voters who place $A$ in the approved tier ("approvals of $A$").
> - $S(A>B)$: the number of voters who approve $A$ but not $B$ ("strict approvals of $A$ over $B$").
> - $S(A=B)$: the number of voters who approve both $A$ and $B$.
> Note that voters who disapprove both candidates do not contribute to $S(A>B)$, $S(B>A)$, or $S(A=B)$, and are therefore irrelevant to the $A$ vs $B$ pairwise comparison. It follows that $S(A)=S(A>B)+S(A=B)$.

By Axiom \ref{ax:ranked-ballot-assumption}, we say $A$ defeats $B$ if and only if $S(A>B)>S(B>A)$, as these are precisely the voters who distinguish between $A$ and $B$ on their ballots.

> **Lemma:** Candidate $A$ defeats candidate $B$ pairwise in $C_2$ if and only if more voters put $A$ in the approved tier.\label{lem:c2-approval}

$$\begin{equation}
S(A>B)>S(B>A) \iff S(A)>S(B)
\end{equation}$$

**Proof:** If more voters put $A$ in the approved tier, then $S(A)>S(B)$. Thus, $S(A>B)+S(A=B)>S(B>A)+S(A=B)$, implies that $S(A>B)>S(B>A)$ by cancellation of $S(A=B)$, meaning $A$ defeats $B$. Conversely, if $A$ defeats $B$, then $S(A>B)>S(B>A)$. Adding $S(A=B)$ to both sides of the inequality retrieves the desired result

$$\begin{multline*}
S(A>B)+S(A=B)>S(B>A)+S(A=B) \\
\iff S(A)>S(B)
\end{multline*}$$

Thus, $A$ gets more total approvals than $B$ if and only if $A$ defeats $B$ pairwise. $\square$

Beyond the algebra, the key and intuition of this proof is extraordinarily simple. Voters who approve both or neither do not contribute to the difference between the total approvals of A and B. That difference is based purely on voters who distinguish between them, which we use to *define* who wins the pairwise matchup. If Alice gets 50 more approvals than Bob, then that means that 50 more voters approved Alice and not Bob than voters approved Bob and not Alice. Therefore, Alice beats Bob!

We now define Approval voting.

> **Definition:** Approval voting is a voting method in which each voter can approve any number of candidates. The candidate who is approved by the most voters wins.

And land the crushing blow.

> **Theorem:**
>
> 1. $C_2$ induces a transitive majority relation
> 2. There can never be a Condorcet paradox in $C_2$.
> 3. To determine the winner in $C_2$, it suffices to count the number of first ranks (approvals) each candidate receives. The candidate who is in the upper "approved" tier of the most voters is a Condorcet winner and will, thus, win.
> 4. $C_2$ is the unique GCM that satisfies any of the above three properties. They do not hold for any $C_k$ where $k>2$.
> 5. Therefore, $C_2$ is exactly Approval voting, which is hence the unique Generalized Condorcet Method that never admits a Condorcet paradox.

**Proof:** This follows directly from Lemma \ref{lem:c2-approval}.

**Claim 1:** By the previous lemma, $A$ defeats $B$ if and only if $S(A)>S(B)$. Thus, the ordinal ranking of candidates by $S(\cdot)$ is the same as the majority relation. Since the ordinal ranking of candidates by $S(\cdot)$ is a sequence of real numbers, it is totally ordered and thus transitive.

**Claim 2:** Claim 1 directly implies the absence of a Condorcet paradox in $C_2$. Suppose that $A$ defeats $B$, and $B$ defeats $C$. Then $S(A)>S(B)$ and $S(B)>S(C)$, so $S(A)>S(C)$ by transitivity of the real numbers, so $A$ defeats $C$.

**Claim 3:** As a Condorcet method, $C_2$ must elect the Condorcet winner whenever one exists. By the previous lemma, the candidate with the most first ranks (approvals) is the Condorcet winner. Axiom \ref{ax:unique-winner} tells us that there can be at most one such candidate, meaning there is at most one candidate with the most total approvals. Therefore, $C_2$ always elects the candidate with the most approvals, and that candidate will always be the Condorcet winner.

**Claim 4:** We now show that any $C_k$ where $k>2$ cannot satisfy any of the previous three properties. Any $C_k$ where $k>2$ can admit a Condorcet paradox by Lemma \ref{condorcet-paradox}, so it cannot satisfy the first two properties. To conclude the proof, we show that if $k>2$ then a candidate with the most first ranks is not necessarily the Condorcet winner. Consider the following profile:

| Voter  | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 3      | A        | B        | C        |
| 2      | B        | C        | A        |
| 2      | C        | B        | A        |

In this profile, $A$ has the most first ranks, but $B$ defeats both $A$ and $C$, so $A$ is not the Condorcet winner. We cannot, then, infer pairwise dominance by considering only the number of ballots in which a candidate is in the top tier, except in $C_2$.

Claims 1 through 3 establish that $C_2$ is precisely approval voting, proving that Approval is a Generalized Condorcet Method that never admits a Condorcet paradox. Claim 4 establishes that Approval voting is the unique Generalized Condorcet Method with property 1, 2, or 3. $\square$

This leads to the pièce de résistance:

> **Theorem:** Approval voting is perfectly Condorcet-consistent. It elects the Condorcet winner without fail in every single election with a unique winner, with no exceptions.\label{thm:approval-condorcet}

**Proof:** Claim 3 of the previous theorem states that the candidate with the most approvals is always the Condorcet winner. By Axiom \ref{ax:unique-winner}, that candidate is unique. Therefore Approval voting elects the Condorcet winner in every election, based on Definition \ref{def:condorcet-winner}. $\square$

If you concede that we can only define a Condorcet winner by the ballot data that voters actually cast, rather than the preferences they *might have had*, then Approval is necessarily perfectly Condorcet consistent, and *the only Condorcet method that can guarantee the existence of a Condorcet winner in every election*.

<img src="/assets/img/approvalcondorcetmeme1.jpg" alt="Drake: Approval is not two-tiered score, but two-tiered Condorcet" style="width:100%; max-width:600px;">

Note: As I was writing this post, I was researching related arguments and I found out that [Charles Munger wrote a paper in 2023 proving that Approval is a two-tiered Condorcet method](https://bettervotingmethods.com/s/ApprovalRangeStarVoting030323.pdf). Even hardcore Condorcetists know Approval is a Condorcet method! His conclusion is that Approval voting is a degenerate Condorcet method with worse outcomes. However, while I actually generally agree with his criticisms of Range and STAR voting, I think that in practice Approval really is just a more practical Condorcet method. [This is a pretty good argument in that regard](https://rangevoting.org/AppCW.html).

## You can't prove it's not Condorcet

As proved above, Approval voting is indeed a Condorcet method, just restricted to two tiers. This is a restriction to binary "acceptable" vs "unacceptable" preferences, just as a ranked method is a restriction of an arbitrary preference ordering to a transitive one. But as a Condorcet method, it always elects the candidate who would win all pairwise matchups against other candidates based on the preferences expressed in the ballot data.

As with *any* Condorcet method, all we have to go on is what voters express.

**Example:** Consider the following example in Approval voting between Alice, Bob, and Clark: \label{ex:approval}

| Voters | True Preferences | Approvals |
|--------|------------------|-----------|
| 45     | $A > B > C$      | $A$       |
| 35     | $B > A > C$      | $B, A$    |
| 20     | $C > B > A$      | $C$       |

Then Alice wins the Approval voting election with 80 votes, since she has the most approvals. Bob and Clark only get 35 and 20, respectively. Based on the ballots, Alice appears to be the Condorcet winner. But a careful look at the true preferences, assuming we could know them, shows that Bob is actually the Condorcet winner, as he would win all pairwise matchups against the other candidates based on the full preference rankings.

From another perspective, however, this is a blowout. Alice was approved by *80%* of all voters. That is an *absurd* mandate, and it would be very difficult to actually question her status as the Condorcet winner if this was a true election outcome. This is only a "pathology" because we are choosing to assume that 55% of the electorate prefer Bob over Alice, even though they did not express this on their ballots.

But if we want to play the "let's make up a profile where voters act stupidly" game, then let's play it. Just because voters *can* rank beyond two tiers does not mean they will, and thus a general Condorcet method is susceptible to ridiculous outcomes.

**Example:** Let's suppose we instead give the voters in Example \ref{ex:approval} a full ranked ballot, with ties allowed, and they vote in $C_\infty$ as follows:\label{ex:cinf}

| Voters | True Preferences | $C_\infty$ Ballot |
|--------|------------------|-------------------|
| 45     | $A > B > C$      | $A > B > C$       |
| 35     | $B > A > C$      | $B > A > C$       |
| 20     | $C > B > A$      | $C > B = A$       |

Perhaps Clark, knowing he has no chance, told his supporters to rank him first and nobody else, in a misguided attempt to game the election. Out of voters who expressed a preference between Alice and Bob, still more preferred Alice over Bob (45 (56.25%) to 35 (43.75%)). Therefore, Alice would still be elected. And, based on the ballots, you still wouldn't be able to prove that Alice was not the Condorcet winner either, just like in Approval. The difference? Alice has a weaker mandate. Expression has weakened the legitimacy without changing the outcome.

Whether it be Approval or $C_\infty$, the pathology of this scenario is that while Bob was the true Condorcet winner based on the full preferences, he was unable to convince the majority of voters who truly preferred him over Alice to express that preference on their ballots. Given that real voters truncate their ballots, this is a realistic concern.

I have my issues with utility arguments, and range voting methods, but let's pretend we magically know the *true*, internal utility that each candidate provides to each voter in this example (just as Condorcetists pretend to know the true pairwise preferences that voters *might* have in Approval voting).

| Voters | A Utility | B Utility | C Utility | True Ranking | Approvals | $C_\infty$ Ballot |
|--------|-----------|-----------|-----------|--------------|-----------|-------------------|
| 45     | 1         | 0.3       | 0         |  $A > B > C$ | $A$       | $A > B > C$       |
| 35     | 0.9       | 1         | 0         |  $B > A > C$ | $B, A$    | $B > A > C$       |
| 20     | 0         | 0.1       | 1         |  $C > B > A$ | $C$       | $C > B = A$       |

In this scenario, Alice is a much higher utility option (76.5) for the electorate than the true Condorcet winner Bob (50.5). Perhaps Alice is a firebrand candidate who excites her 45% base, who finds a milquetoast candidate like Bob unexciting. And perhaps, a substantial minority of moderate voters *slightly* prefers Bob over Alice (a 10/10 vs a 9/10), but would be genuinely happy with either one. The minority of Clark supporters hate both Alice and Bob, and preferring Bob is like preferring losing a kidney over losing a liver. Both awful, but if *forced* to pick one, they would pick Bob. However, the utility disparity is so large, it's not unbelievable they might just rank both Bob *and* Alice equally below Clark.

This is not to argue that utility maximization should be the goal of an election, especially because that's not the data we collect in a Condorcet method. But the utilities show the approvals are not necessarily irrational in this context. Each voter is approving only the candidates above the average utility of all candidates (this is a [standard modeling choice for the approval threshold under honest, zero-information assumptions](https://electionscience.github.io/vse-sim/VSEbasic/)). If this is genuinely how the voters feel, and if 80% of the electorate gives Alice a 9/10 or higher, then I see no reason that Alice is an unreasonable winner, or somehow a "fringe" candidate.

Bob, on the other hand, is only a 3/10 or 1/10 to 65% of the electorate. Under this dynamic, Alice is clearly a better compromise for the electorate as a whole than Bob, given that the Bob supporters seem to genuinely like Alice. I would argue 80% of the voters being at least 90% happy is more majoritarian than 65% of the voters being at most 30% happy.

Most Condorcet winners are not like Bob here, in my opinion. And when they are genuinely good, I have no doubt that Approval voting would likely elect them. But in cases like the one above, where the Condorcet winner is only marginally preferred by a lukewarm majority who barely sees a difference between him and Alice, Approval voting can reasonably elect a candidate who is actually acceptable to a larger portion of the electorate.

The [1985 Institute of Management Sciences (TIMS) election](https://www.jstor.org/stable/2632078) is a good example that shows a narrow (and ambiguous) Condorcet winner can be defeated by a candidate who is more broadly acceptable to the electorate. See [this post](../practicalapproval){:target="_blank"} where I discuss it in more detail. But, in short, the Approval winner won by over a hundred approvals. The Condorcet winner was strictly preferred over the Approval winner by a single vote (of those who expressed a preference), while 27 voters abstained. That's not exactly a strong legitimate claim. Approval broke that ambiguity and would have given a mandate, even though ordinal preferences were in a deadlock.

### A Remark on Legitimacy

However, unlike any ranked method, [or scoring method with three or more options](../consistentcardinal){:target="_blank"}, Approval never admits a case where another candidate has a legitimate claim to victory over the actual elected candidate, who is a Condorcet winner based on the ballot data.

Simply, any candidate loses an Approval voting election if and only if it was a "skill issue". To be blunt, losing an Approval election is entirely the candidate's fault for not earning enough approvals from the voters. While the case could be made that this is true in plurality voting as well, it cannot be done quite as cleanly.

Unlike choose-one plurality voting, in Approval voting, third-party supporters can vote for the third party *and* for the viable alternative. If they have the pen in their hand, and look at your name, and say "no thanks", then that is entirely your fault for not being able to convince them to support you. *Skill issue*.

Similarly, if there was an underlying Condorcet winner who just couldn't convince their majority to approve them due to their majority preference being sufficiently lukewarm, which is what happened to Bob in the example above, then in that case, all I can say is, "cry about it".

Rather than wax poetic about utility maximization, I go the Condorcet route: If a voter ranks (or approves) Alice above Bob, then all we can say is that they would vote for Alice over Bob in a theoretical one-on-one matchup. As Condorcetists, we do not assume any information about how they would vote in matchups they did not express a preference for. We just take the ballot data at face value, and if Alice is ranked above Bob by more voters than Bob is ranked above Alice, then we say that Alice defeats Bob.

This does not, in my opinion, lose significant meaning when we restrict to two tiers. Under the conditions of the ballot, if more voters express they would vote for Alice over Bob than the other way around, then that does indeed show something meaningful about the relative popularity and acceptability of Alice and Bob.

In Approval there is no "but I got more first choice votes" argument to be made against a legitimate Condorcet winner, because the Condorcet winner is such *because* they convinced the most voters to approve them over any other candidate in a one-on-one comparison.

Likewise, in Approval there is no "but I was ranked by more voters over the winner" argument, as in ranked-choice voting. And Condorcet can't escape this either, because when a Condorcet cycle inevitably occurs, there is no winner who doesn't lose to at least one other candidate in a one-on-one matchup. So much for "legitimacy" to the winner in those cases. Approval has no cycles, and therefore no ambiguity about who the legitimate winner is based on the ballot data.

My adherence and loyalty to the Condorcet criterion is not because I think the theoretical winner in all one-on-one plurality runoffs is actually the best candidate if there is potentially a better and less polarizing compromise. My loyalty is for the *legitimacy* of the criterion in the only data that truly matters: what the ballots collect.

<img src="/assets/img/approvalcondorcetmeme2.jpg" alt="Approval is the cool Condorcet method" style="width:100%; max-width:600px;">

### A Remark on Precinct Summability

Approval voting is very clearly precinct summable. We have proved that it is a Generalized Condorcet Method which only needs the total number of approvals each candidate receives to determine all pairwise matchups. It is as simple as our current choose-one voting system.

General Condorcet Methods, including $C_\infty$, are also technically precinct summable, unlike a method like RCV which absolutely requires [central tabulation](../ditch-rcv){:target="_blank"}. However, the practicality decreases as the number of candidates increases. For 19 candidates, a precinct would potentially need to report the number of voters who prefer each candidate over each other candidate, which is $19(18) = 342$ numbers, which is considerably more cumbersome than simply reporting 19 approval counts. However, it is technically fewer numbers than STAR voting, which would require reporting all of these numbers alongside the total scores for each candidate ($19^2=361$) for full summability that wouldn't require a later tabulation of the runoff numbers.

In fairness, optimizations could be made for both systems. It might be possible to reduce the number of reported numbers by considering $A>B$ rankings $+1$ and $B>A$ rankings a $-1$, and counting only the margins in each $\frac{n(n-1)}{2}$ pairwise matchup. But that's still over 170 numbers to put on the gymnasium door for a 19 candidate race. Better than ranked-choice voting, surely, but not exactly practical.

## You cannot be serious

Oh, but I am. Mostly. Half-and-half.

The sleight of hand that I used in this post was to emphasize the outcomes at the ballot level. I conveniently left out an axiom that any true Condorcetist would absolutely mandate: that voters should be able to rank all candidates if they want to. If that is ultimately important, then a "Generalized Condorcet Method" violates the innate spirit of the Condorcet ideal.

What $C_k$ (including $C_\infty$) *really* does, mathematically, is ask voters to project their arbitrary preferences into a transitive $k$-tiered ("$k$-chotomous") preference order. $C_\infty$ projects into arbitrary transitive preferences, while $k=2$ projects to two-tiered ("dichotomous") preferences. Two-tiered preferences is where Approval is the natural language, and works "perfectly".

Here's what is absolutely true: Because no Condorcet method asks voters to directly vote in every possible head-to-head matchup, we cannot assume that any ranked method can perfectly capture the Condorcet winner in all cases, because you simply cannot assume all voters have and will express full, complete preferences over all candidates, so long as you do not force voters to completely rank all candidates without ties. And if you *do* force a full ranking, then you will bottleneck turnout and get a bunch of noise from voters with no genuine opinion who are just guessing.

In reality, Approval voting is, in my opinion, "Condorcet-lite". It's not a Condorcet method *proper*, but I would absolutely say a "generalized" Condorcet method is an appropriate name. Condorcetists simplify messy incomplete preferences to a transitive ranking, with abstention allowed, to make determining a (possible) Condorcet winner tractable and practical.

Approval just goes one step further with this logic and simplifies the ballot to make it completely consistent and practical. But at its core, it is still electing the candidate ranked strictly above any other candidate by a majority of voters who express a preference. To me, *that* is the appeal of the Condorcet criterion--the legitimacy given to the winner. And in *that* respect, Approval is perfect. It inherits the base legitimacy of any system that does this reliably (Condorcet methods), along with the legitimacy that comes from simplified ballot data.

Here's the truth: At the time of writing, Condorcet would be my second choice over Approval. If Approval *didn't* show clear data that it was essentially *just* as good as a full Condorcet method in practice, and if I didn't feel that [simplicity is paramount in this era of distrust](../practicalapproval){:target="_blank"}, then I wouldn't be advocating for Approval voting so strongly over a full Condorcet method. But the fact that Approval is simple, transparent, and *practically as good* makes the choice for me quite clear.

### What about the outcomes?

We have established that Approval is a simplified, two-tiered Condorcet method. While those like Munger would argue that this simplification comes at the cost of outcomes, I would argue that the cost is minimal for the benefits we get in return.

Approval has been shown to have [essentially the same level of outcomes](https://electionscience.github.io/vse-sim/VSEbasic/) as more complex Condorcet methods in "Voter Satisfaction Efficiency" (VSE). Whereas Condorcet gets about 86%-98% VSE, Approval gets 89%-95%, depending on strategy. And what do we gain in return for that three percent drop in maximum VSE?

We have mentioned thus far the simplicity of counting Approval votes compared to more complex ranked methods, which balloon in complexity as the number of candidates increases. So it's much simpler to use in practice, which has nontrivial importance.

There is the fact that, unlike any other Generalized Condorcet method, Approval never "breaks" due to a cycle, because Approval has no cycles. Sorry, but I'm not quite ready to take an extra 3% in maximum VSE for a system that's more complicated and has a tiny chance to completely collapse, and be relegated to a seemingly arbitrary tie-breaker, if voters are sufficiently messy. I'll take the sturdy simplicity of a 95% system, that can promise it will never break, any day.

[I recommend taking a look at some Yee diagrams](http://zesty.ca/voting/sim/), and trying to tell me if you can truly tell the difference between the Approval and Condorcet diagrams without your reading glasses.

In the same vein, [Gary Cox](https://doi.org/10.2307/2111325) has a paper that shows both Approval and Condorcet have strong median pulls. Munger's criticisms that Approval elects "fringe" candidates, based purely on ordinal preferences that have no information about intensity, just do not hold up to scrutiny in my opinion. To treat a candidate who ranks Alice over Bob but only finds Alice acceptable exactly the same as a voter who slightly prefers Alice but also loves Bob is to completely ignore the concept of acceptability and distance between rankings.

And even *if* Approval voting occasionally elects a candidate who is not the Condorcet winner, we would literally never even know! You would never be able to *prove* it. The only thing we would see is the candidate who earned approvals from the most voters, and all the others who couldn't manage to convince as many voters.

I may make a future post about some of the mathematical nuances of Approval versus full Condorcet, including discussion of IIA, and Nash equilibria guarantees. There is also [the fact that Approval is *technically* strategyproof under the goal of electing any "acceptable" candidate](../avstratproof){:target="_blank"}. Additionally, when voters apply an intuitive strategy like [Laslier's Leader rule](https://journals.sagepub.com/doi/10.1177/0951629808097286), the only equilibrium is one that elects a unique Condorcet winner, when they exist.

### Domain Restriction

Plurality voting, as a matter of fact, also satisfies many of the same properties we have proved for Approval. It is also technically a Condorcet method (based on the ballot data), that satisfies IIA "at the ballot level", if you assume that voters can only like a single candidate and equally dislike all other candidates.

However, this isn't the gotcha some might think, as this is only true because plurality is just an arbitrary restriction on Approval voting. Approval voting is precisely the minimal level of ballot restriction we can place on a Condorcet method to ensure that it works 100% of the time. Or, from another framing, dichotomous (two-tiered) preferences are the maximal domain where Condorcet methods (or a voting system in general) can operate perfectly.

Since Approval is perfect for dichotomous preferences, as that is literally the data it collects, then it's no surprise Approval is "perfect" if we assume the ballot data is perfectly accurate to the feelings of the voter. But that does not mean we *should* assume such a thing. The purpose of this post is to show that if we take Condorcet logic to the extreme, then Approval is the ultimate Condorcet system (if you conveniently leave out the axiom of allowing full rankings, as I did).

We have a hierarchy of compromises that a Condorcet method can make.

1. $C_\infty$ simplifies the data by assuming voters have transitive preferences, and allows voters to truncate and express indifference, but allows all possible rankings at the cost of not being able to guarantee a Condorcet winner.
2. $C_2$ simplifies the data by assuming voters can project their preferences into a partition of candidates into "acceptable" and "unacceptable" sets. This is a simplification and compromise that results in the complete elimination of all issues that arise from the Condorcet paradox, while still generally electing the best candidate almost all of the time.
3. Plurality voting restricts $C_2$ to a single choice for the top tier, which allows it to maintain the properties of $C_2$, but is an arbitrary restriction that does not greatly simplify the data, *and* leads to significantly worse outcomes.

$C_2$ is the maximal level that maintains a "reasonable" level of preference expression, still gives excellent outcomes, while still allowing the Condorcet method to work "perfectly".

The fact is, I am an ultra pure Condorcetist. Purer than those who scoff at Approval voting, because I do not just think the Condorcet winner *should* be elected if they exist (in the ballot data). Instead, I believe that if your system cannot guarantee that a Condorcet winner *will* exist (in the ballot data), then it's a broken system with no practical potential. Approval is the purest Condorcet method because it always elects and induces a Condorcet winner!

However, to bring back in a little bit of seriousness to this April Fools' post, I accept that some believe there is value in a more expressive voting system. In particular, if Approval voting elects the Condorcet winner via sincere strategies, then that was done via voters likely choosing one of many sincere strategies. A full ranked method has only one sincere strategy, and there is value to that.

Further, the effective rarity of Condorcet cycles "in the wild" (at least, under RCV) means that the guarantee that a Condorcet winner will always exist in the ballot data has limited persuasiveness. I think such a guarantee is valuable in an era of distrust, but I do not claim this is the only thing that matters. Especially because it *does* come at the cost of limiting expression significantly.

## Conclusion

In conclusion, Approval voting is a Condorcet method that changes the question from asking voters for a ranking which may or may not accurately reflect their preferences in one-on-one elections into a simpler, and arguably more important, question: who do you consent to govern you?

The latter question is binary and well-defined. Because it is binary, it is impossible to induce a Condorcet paradox. We do limit expression, at minimal cost to outcomes. And my choice to simplify things down to acceptability has the following benefits:

1. Making the system far more practical for voters and administrators by simplifying the voting process, reducing cognitive load, and minimizing ballot-completion errors. Voters who don't have the time to rank 10 candidates for Comptroller can still participate meaningfully by simply approving the candidates they find acceptable.
2. Ensuring full legitimacy to the winner in every possible non-tied election scenario, as the ballot Condorcet winner. No paradoxes or cycles, and no other candidate can claim to be more deserving of victory than the candidate with the most approvals based on the ballots cast.
3. Maintaining full transparency and being far easier to explain to voters, particularly to skeptical voters who demand to know why *their* candidate lost.

All the while providing [essentially the same level of outcomes](https://electionscience.github.io/vse-sim/VSEbasic/) as more complex Condorcet methods.

In an era of distrust in institutions and elections, I believe that simplicity and clarity are a prerequisite for trust. And I do not trust that a generic Condorcet method is sufficiently simple and transparent (particularly in the case of a cycle, rare as they may be) in all cases to be a permanent solution. Approval is the only system I think is simple enough to be that permanent solution, and I think it *has to be the first step*. Approval today, Condorcet tomorrow is something I might be willing to get behind.

Fellow Condorcetists, let us unite behind the best and most practical Condorcet method: Approval voting!

And if you are a true Condorcetist who read this far, I would like to extend my genuine thanks for getting through this complete mathematical abuse of the term "Condorcet". However, I hope that it at least convinced you that Approval is, in fact, a two-tiered Condorcet method. Whether or not that changes your opinion of Approval, I leave that up to you!

## References

Brams, S. J. (2008). *Mathematics and Democracy: Designing Better Voting and Fair-Division Procedures*. Princeton University Press. [https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy)

Brams, S. J., & Fishburn, P. C. (1978). Approval Voting. *The American Political Science Review*, 72(3), 831-847. [https://doi.org/10.2307/1955105](https://doi.org/10.2307/1955105)

Cox, G. W. (1987). Electoral Equilibrium under Alternative Voting Institutions. *American Journal of Political Science*, 31(1), 82-108. [https://doi.org/10.2307/2111325](https://doi.org/10.2307/2111325)

Electorama. (2022). U.S. Representative (Special General), Alaska, August 16, 2022 -- ABIF results. [https://abif.electorama.com/id/2022-08-16-Alaska-U.S.Representative(Special_General)](https://abif.electorama.com/id/2022-08-16_Alaska-U.S._Representative_(Special_General)#pairwise)

Fishburn, P. C., & Little, J. D. C. (1988). An Experiment in Approval Voting. *Management Science*, 34(5), 555–568. [https://www.jstor.org/stable/2632078](https://www.jstor.org/stable/2632078)

Laslier, J. F. (2009). The Leader Rule: A Model of Strategic Approval Voting in a Large Electorate. *Journal of Theoretical Politics*, 21(1), 113-136. [https://journals.sagepub.com/doi/10.1177/0951629808097286](https://journals.sagepub.com/doi/10.1177/0951629808097286)

Merrill, S. (1988). Condorcet Efficiency. In *Making Multicandidate Elections More Democratic* (pp. 15-29). Princeton University Press. [https://doi.org/10.1515/9781400859504.15](https://doi.org/10.1515/9781400859504.15)

Munger, C. T., Jr. (2023). Approval voting is Condorcet-compatible voting under a constraint: A critique of Approval, and both Range and Star, voting. Better Voting Methods. [https://bettervotingmethods.com/s/ApprovalRangeStarVoting030323.pdf](https://bettervotingmethods.com/s/ApprovalRangeStarVoting030323.pdf)

Quinn, J. (2017). *Voter Satisfaction Efficiency (VSE) summary*. Center for Election Science. [https://electionscience.github.io/vse-sim/VSEbasic/](https://electionscience.github.io/vse-sim/VSEbasic/)

Ranked.Vote. (2022). *Alaska At-large Congressional District*. [https://ranked.vote/report/us/ak/2022/08/cd](https://ranked.vote/report/us/ak/2022/08/cd)

Ranked.Vote. (2021). *Minneapolis City Council Ward 2*. [https://ranked.vote/report/us/mn/2021/11/ward-2](https://ranked.vote/report/us/mn/2021/11/ward-2)

Smith, W. D. (n.d.). Approval yields Condorcet winners in practice. Center for Range Voting. [https://rangevoting.org/AppCW.html](https://rangevoting.org/AppCW.html)

Yee, K. P. (2005). Voting simulation visualizations. [http://zesty.ca/voting/sim/](http://zesty.ca/voting/sim/)
