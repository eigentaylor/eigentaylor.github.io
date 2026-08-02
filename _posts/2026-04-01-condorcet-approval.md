---
layout: distill
title: Approval is the Perfect Condorcet Method
date: 2026-04-01
description: Approval is a perfect Condorcet method, and I have permanently solved the Condorcet paradox. April Fools!
thumbnail: /assets/img/approvalcondorcetmeme1.jpg
importance: 2
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
bibliography: voting.bib
---

## Introduction

{% proof EDIT (06/27/2026) %}
This post was extremely long and pedantic and I decided to significantly shorten, removing much of the detailed exposition and examples that made it cumbersome to read.
{% endproof %}

Merry April Foolsmas, everyone! I have seen the light of the math, and I am now a *true* Condorcet purist.

Fellow Condorcetists, I come bearing a gift: I have permanently solved the Condorcet paradox. There is in fact a *perfect* voting system! It is called *Approval voting*, and it *is* indeed a Condorcet method.

[For an actually serious argument on the fact that Approval is a practical Condorcet approximation, see this post.](../practicalapproval) However, the math I am about to present is *dead serious*, even if *I* am not.

## Condorcet and His Paradox

During the time of the French Revolution, a titan came up with an idea that changed the way we think about voting systems forever. This was Marie Jean Antoine Nicolas de Caritat, Marquis de Condorcet. While that is an *awesome* name, we will just call him Condorcet.

Condorcet believed that we should always elect what we now call a *Condorcet winner*--a candidate who would defeat every other candidate in a one-on-one election. This is often held as the *gold* standard for a voting system (by *cool* people).

But it is impractical to hold an election for every $\frac{n(n-1)}{2}$ pair of candidates, or to put all possible one-on-one matchups for all candidates on the ballot given to each voter<d-footnote>Since writing this post, I've learned that Better Choices is proposing <em>exactly this</em> for the general election of a Top-3 runoff. That is the exact number of candidates where this actually works. So that's really cool. But this stands for larger elections: a 19 candidate race, such as the 2024 Portland mayoral race would need 171 matchups.</d-footnote>. So we need a voting system that can be used in a single election, is not absurdly hostile to voters, and still satisfies the *spirit* of the Condorcet criterion: if there is a Condorcet winner, *and voters express this through their ballots*, then they should win.

> **Definition:** A *Condorcet winner* is a candidate who would defeat every other candidate in a one-on-one election, based purely on the ballot data of voters who express an explicit preference.\label{condorcet-winner}

We compromise on the idea that we can simulate how voters would vote in each theoretical matchup by ranking candidates and assuming a transitive order. If I rank Alice first, Bob and Clark tied for second, and Dylan last, then a Condorcet method interprets this *only* as me saying that

- I would vote for Alice over Bob, Alice over Clark, and Alice over Dylan.
- I would vote for Bob over Dylan, and Clark over Dylan.
- Bob and Clark are *about the same*, I don't have a strong preference between them. Maybe they're both just meh, while Alice is amazing, and Dylan is terrible.

The single ranked ballot thus allows us to simulate how voters *might* vote in each theoretical matchup, and thus have an idea if there is a Condorcet winner. By ranking Bob and Clark equally, I am indicating that I have no preference between them in a head-to-head matchup. We make only a single assumption:

> **Axiom:** (Ranked Ballot Assumption) If a voter submits a ranked ballot, we assume only one thing about that voter's preferences: If a voter ranks candidate $X$ above candidate $Y$, then they would vote for $X$ over $Y$ in a head-to-head matchup. That is, we assume the ranking implies transitive preferences. If a voter ranks $X$ and $Y$ equally, then they have no preference between $X$ and $Y$ in a head-to-head matchup. If more voters rank $X$ above $Y$ than the reverse, we assume $X$ defeats $Y$.\label{ranked-ballot-assumption}

If there is a candidate who would defeat every other candidate in a head-to-head matchup based purely on the ballot data, interpreted through the above assumption, then we must assume they are the Condorcet winner, and by golly, they should win!<d-footnote>The value of this criterion is felt most strongly in the contrapositive. If the ballots indicate that a candidate would be defeated by any single other candidate in a runoff, then they would not have a strong claim of legitimacy if declared the winner.</d-footnote>

### The Paradox

Condorcet's solution sounds perfect, theoretically. I mean, if we can tell voters "this is the candidate who would have won against *every* other", then that would be amazing!

As with all things in voting theory, there's a catch. While a Condorcet winner exists *quite* often, it's still less than 100% of the time.

**Example:** Consider the following profile of 3 voters:\label{cycle}

| Voters | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 1      | Rock     | Scissors | Paper    |
| 1      | Scissors | Paper    | Rock     |
| 1      | Paper    | Rock     | Scissors |

In this profile, Rock defeats Scissors (a majority of 2 voters rank Rock above Scissors). Similarly, Scissors defeats Paper. However, while we would expect that if Rock beats Scissors, and Scissors defeats Paper, then Rock must defeat Paper, another majority prefers Paper over Rock. Thus, there is no Condorcet winner. No matter who you elect, some other candidate can say, "but I would have defeated them!" There is no way to elect any candidate with full legitimacy based on these ballots.

### Condorcet is an Approximation

The use of rankings to infer one-on-one preferences is an approximation. Every Condorcetist must be honest about this. **So long as we do not directly ask how a voter would vote in every possible matchup, we cannot guarantee that there is a Condorcet winner, nor that we did, in fact, elect them** (this is precisely Axiom \ref{ranked-ballot-assumption}).

> **Definition:** A voting system satisfies the *Condorcet criterion* if whenever there is a candidate who would defeat every other candidate in a head-to-head matchup **based on the ballot data of voters who expressed a preference between the two candidates**, then that candidate must win.

If you do not elect such a candidate in a ranked system, then **what are you even** ***doing***? [Why ask for rankings if you aren't even going to use or respect them?](../ditch-rcv) If you do not elect such a candidate, then you have elected someone else who has to serve their constituents knowing that a majority of voters wanted someone else more. That creates a [legitimacy problem](../consistentcardinal).

We also cannot guarantee that even if we elect the Condorcet winner induced by the ballots, that candidate would truly defeat every other candidate in a head-to-head matchup, because we are not directly asking all of those head-to-head questions, especially when ties or ballot truncation are allowed.<d-footnote>A commonly cited example of a Condorcet failure is Alaska's 2022 House special election. But due to ballot truncation, it's not even 100% guaranteed that Nick Begich was actually the Condorcet winner.</d-footnote>

As Condorcetists, we have to rely exclusively on the expressed ballot data, and trust that among those who *did* express a preference between two candidates, the majority preference accurately reflects who would win in a head-to-head matchup among the entire electorate. Just as ranked-choice voting exhausts ballots from voters who failed to rank any remaining candidates, Condorcetists also value expressed preferences over potential unexpressed preferences. The only sane way to implement a Condorcet method is to

1. Allow ties in a voter's ranking, and truncation, for the sake of the voter
2. Define a Condorcet winner purely based on the ballot data, and Condorcet efficiency based on electing a candidate who is a Condorcet winner (based on the ballot data) when one exists

We saw in example \ref{cycle} that a Condorcet winner does not always exist. But can they be forced to exist in every election if we just... make the system *better*? The answer may surprise you.

## Generalized Condorcet Methods

This is not a concept I have ever heard of anyone defining, but it's my post, so I get to make it up! At its core, a typical Condorcet method assumes the ability to give a full ranking of all available candidates if the voter is able to. Please excuse me for a moment while I move the goalpost.

> **Definition:** A *Generalized Condorcet method* (GCM) is a voting system where voters can rank all candidates, with ties allowed, among some predetermined number of tiers, with no other restrictions<d-footnote>Note: If $k$ is smaller than the number of candidates, then a voter will necessarily have to express some number of ties, by the Pigeonhole principle.</d-footnote>. If a voter ranks candidate $X$ strictly over candidate $Y$, then that voter casts a vote for $X$ in the $X$ vs $Y$ matchup. If a voter ranks candidate $X$ in the same tier as $Y$, they abstain in the matchup. If there is a candidate who wins all of their matchups, then that candidate is declared the Condorcet winner and *must* win. We denote a GCM with $k\geq 2$<d-footnote>$C_1$ does not really make sense as a system--it would be a trivial system where ballots say nothing and every voter is assumed to be indifferent between all of them. Plurality/choose-one voting does not fit in as a GCM, as it's an arbitrary restriction on $C_2$ where voters can only put a single candidate in the upper tier. Further, the Better Choices system where voters actually vote in every pairwise matchups (allowing an intransitive preference) would not fit into this system either. A GCM does require transitivity of preference.</d-footnote> tiers as $C_k$. If there is no limit on the number of tiers, then we denote it as $C_\infty$.

An example of a $C_6$ system is [Smith//Score](https://electowiki.miraheze.org/wiki/Smith/Score), which collects 0-5 scores for each candidate, elects the Condorcet winner if one exists, and otherwise breaks a tie/cycle by electing the candidate with the highest score. One can imagine that a Generalized Condorcet method is actually just a generalization of the concept of Smith//Score, where we allow for any number of tiers, and an arbitrary function to break ties when there is no Condorcet winner.

We treat the voting system as a function $C_k(P)=W$, for $k \geq 2$, including $k = \infty$, that takes in a profile $P$ of ballot preferences (having at most $k$ tiers) and outputs a single winner $W$. If there is a Condorcet winner induced by $P$, based on our axioms and definitions, then that candidate must be the unique winner output by the function.<d-footnote>If there is no Condorcet winner, $C_k$ can be an arbitrary function. Thus, $C_k$ is essentially a family of functions that we only require to all agree on the Condorcet winner when one exists.</d-footnote>.

We investigate what happens when we restrict the number of tiers.

## Limited Tiers and the End of Paradoxes

We first establish a simple Axiom to make the following analysis clean.

> **Axiom:** (Unique winner) We assume that at most one candidate has no strict pairwise loss in any profile $P$. \label{unique-winner}

This axiom allows us to disregard the possibility of a Condorcet method having to choose between multiple weak Condorcet winners in the absence of a cycle<d-footnote>Say Alice defeats Clark, and Bob defeats Clark, but Alice and Bob tie. Neither Alice and Bob have a strict pairwise loss, so neither is a unique Condorcet winner. We don't consider such cases here.</d-footnote>.

> **Lemma:** A Condorcet winner can fail to exist in $C_k$ if $k>2$. \label{condorcet-paradox}

**Proof:** By example \ref{cycle}, we can see that any GCM that allows three tiers can result in no Condorcet winner. This example works for any $k\geq 3$, so a Condorcet winner can fail to exist for any $k\geq 3$. $\square$

This is not an abstract result. While very rare, Condorcet cycles have occurred in real U.S. elections, such as a [Minneapolis city council election in 2021](https://ranked.vote/report/us/mn/2021/11/ward-2) <d-cite key="rankedVote2021minneapolisWard2"></d-cite>.

> **Definition:** For $C_2$, we use the following notation. The two tiers are called the "approved tier" and the "unapproved tier". For candidates $X$ and $Y$:
>
> - $S(X)$: the number of voters who place $X$ in the approved tier ("approvals of $X$").
> - $S(X>Y)$: the number of voters who approve $X$ but not $Y$ ("strict approvals of $X$ over $Y$").
> - $S(X=Y)$: the number of voters who approve both $X$ and $Y$.
> Note that voters who disapprove both candidates do not contribute to $S(X>Y)$, $S(Y>X)$, or $S(X=Y)$, and are therefore irrelevant to the $X$ vs $Y$ pairwise comparison. It follows that $S(X)=S(X>Y)+S(X=Y)$.

By Axiom \ref{ranked-ballot-assumption}, we say $X$ defeats $Y$ if and only if $S(X>Y)>S(Y>X)$, as these are precisely the voters who distinguish between $X$ and $Y$ on their ballots.

> **Lemma:** Candidate $X$ defeats candidate $Y$ pairwise in $C_2$ if and only if more voters put $X$ in the approved tier.\label{c2-approval}

$$\begin{equation}
S(X>Y)>S(Y>X) \iff S(X)>S(Y)
\end{equation}$$

**Proof:** If more voters put $X$ in the approved tier than $Y$, then $S(X)>S(Y)$. Thus, $S(X>Y)+S(X=Y)>S(Y>X)+S(X=Y)$, implies that $S(X>Y)>S(Y>X)$ by cancellation of $S(X=Y)$, meaning $X$ defeats $Y$. Conversely, if $X$ defeats $Y$, then $S(X>Y)>S(Y>X)$. Adding $S(X=Y)$ to both sides of the inequality retrieves the desired result

$$\begin{multline}
S(X>Y)>S(Y>X) \\
\iff S(X>Y)+S(X=Y)>S(Y>X)+S(X=Y) \\
\iff S(X)>S(Y)
\end{multline}$$

Thus, $X$ gets more total approvals than $Y$ if and only if $X$ defeats $Y$ pairwise. $\square$

Beyond the algebra, the key and intuition of this proof is extraordinarily simple. Voters who approve both or neither do not contribute to the difference between the total approvals of $X$ and $Y$. That difference is based purely on voters who distinguish between them, which we use to *define* who wins the pairwise matchup. If Alice gets 50 more approvals than Bob, then that means that 50 more voters approved Alice and not Bob than voters approved Bob and not Alice. Therefore, Alice beats Bob!

We now define Approval voting.

> **Definition:** Approval voting is a voting method in which each voter can approve any number of candidates. The candidate who is approved by the most voters wins. <d-cite key="bramsFishburn1978approval"></d-cite>

And come to our main result.

> **Theorem:**
>
> 1. $C_2$ induces a transitive majority relation
> 2. There can never be a Condorcet paradox in $C_2$. A Condorcet winner always exists in $C_2$, meaning there is only one unique $C_2$ GCM.
> 3. To determine the winner in $C_2$, it suffices to count the number of first ranks (approvals) each candidate receives. The candidate who is in the upper "approved" tier of the most voters is a Condorcet winner and will thus win by definition.
> 4. $C_2$ is the unique GCM that satisfies any of the above three properties. They do not hold for any $C_k$ where $k>2$.
> 5. Therefore, $C_2$ is exactly Approval voting, which is hence the unique Generalized Condorcet Method that never admits a Condorcet paradox.

{% proof Click to expand proof %}
**Proof:** This follows directly from Lemma \ref{c2-approval}.

**Claim 1:** By Lemma \ref{c2-approval}, $X$ defeats $Y$ if and only if $S(X)>S(Y)$. Thus, the ordinal ranking of candidates by $S(\cdot)$ is the same as the majority relation. Since the ordinal ranking of candidates by $S(\cdot)$ is a sequence of real numbers, it is totally ordered and thus transitive.

**Claim 2:** Claim 1 directly implies the absence of a Condorcet paradox in $C_2$. Suppose that $X$ defeats $Y$, and $Y$ defeats $Z$. Then $S(X)>S(Y)$ and $S(Y)>S(Z)$, so $S(X)>S(Z)$ by transitivity of the real numbers, so $X$ defeats $Z$. Therefore, a Condorcet winner always exists in $C_2$, meaning there is only one unique $C_2$ GCM, so long as we assume that there is no tie for the most approvals, which would contradict Axiom \ref{unique-winner}.

**Claim 3:** As a Condorcet method, $C_2$ must elect the Condorcet winner whenever one exists. By the previous lemma, the candidate with the most first ranks (approvals) is the Condorcet winner. Axiom \ref{unique-winner} tells us that there can be at most one such candidate, meaning there is at most one candidate with the most total approvals. Therefore, $C_2$ always elects the candidate with the most approvals, and that candidate will always be the Condorcet winner.

**Claim 4:** We now show that any $C_k$ where $k>2$ cannot satisfy any of the previous three properties. Any $C_k$ where $k>2$ can admit a Condorcet paradox by Lemma \ref{condorcet-paradox}, so it cannot satisfy the first two properties. To conclude the proof, we show that if $k>2$ then a candidate with the most first ranks is not necessarily the Condorcet winner. Consider the following profile:

| Voter  | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 3      | $A$      | $B$      | $C$      |
| 2      | $B$      | $C$      | $A$      |
| 2      | $C$      | $B$      | $A$      |

In this profile, $A$ has the most first ranks, but $B$ defeats both $A$ and $C$, so $A$ is not the Condorcet winner. We cannot, then, infer pairwise dominance by considering only the number of ballots in which a candidate is in the top tier, except in $C_2$.

Claims 1 through 3 establish that $C_2$ is precisely approval voting, proving that Approval is a Generalized Condorcet Method that never admits a Condorcet paradox. Further, this actually implies that there is only one unique $C_2$ function--Approval voting. Claim 4 establishes that Approval voting is the unique Generalized Condorcet Method with property 1, 2, or 3. $\square$
{% endproof %}

This leads to the pièce de résistance:

> **Theorem:** Approval voting is perfectly Condorcet-consistent. It elects the Condorcet winner without fail in every single election with a unique winner, with no exceptions.\label{approval-condorcet}

**Proof:** Claim 3 of the previous theorem states that the candidate with the most approvals is always the Condorcet winner. By Axiom \ref{unique-winner}, that candidate is unique. Therefore Approval voting elects the Condorcet winner in every election, based on Definition \ref{condorcet-winner}. $\square$

If you concede that we can only define a Condorcet winner by the ballot data that voters actually cast, rather than the preferences they *might have had*, then Approval is necessarily perfectly Condorcet consistent, and *the only Condorcet method that can guarantee the existence of a Condorcet winner in every election*.

<img src="/assets/img/approvalcondorcetmeme1.jpg" alt="Drake: Approval is not two-tiered score, but two-tiered Condorcet" style="width:100%; max-width:600px;">

Note: As I was writing this post, I was researching related arguments and I found out that [Charles Munger wrote a paper in 2023 proving that Approval is a two-tiered Condorcet method](https://bettervotingmethods.com/s/ApprovalRangeStarVoting030323.pdf) <d-cite key="munger2023approvalCondorcet"></d-cite>. Even hardcore Condorcetists know Approval is a Condorcet method!<d-footnote>His conclusion is that Approval voting is a degenerate Condorcet method with worse outcomes. However, while I actually generally agree with his criticisms of Range and STAR voting, I think that in practice Approval really is just a more practical Condorcet method. <a href="https://rangevoting.org/AppCW.html">This is a pretty good argument in that regard</a> <d-cite key="smithNdaAppCW"></d-cite>. Older Condorcet-efficiency work points in the same direction <d-cite key="merrill1988condorcetEfficiency"></d-cite>.</d-footnote>

## You can't prove it's not Condorcet

As proved above, Approval voting is indeed a Condorcet method, just restricted to two tiers. As a Condorcet method, it always elects the candidate who would win all pairwise matchups against other candidates based on the preferences expressed in the ballot data.

As with *any* Condorcet method, all we have to go on is what voters express.

**Example:** Consider the following example in Approval voting between Alice, Bob, and Clark: \label{approval}

| Voters | True Preferences | Approvals | $C_\infty$ Ballot |
|--------|------------------|-----------|-----------------|
| 45     | $A > B > C$      | $A$       | $A > B > C$     |
| 35     | $B > A > C$      | $B, A$    | $B > A > C$     |
| 20     | $C > B > A$      | $C$       | $C > B = A$     |

Then Alice wins the Approval voting election with 80 votes, since she has the most approvals. Bob and Clark only get 35 and 20, respectively. Based on the ballots, Alice appears to be the Condorcet winner. But a careful look at the true preferences, assuming we could know them, shows that Bob is actually the Condorcet winner, as he would win all pairwise matchups against the other candidates based on the full preference rankings.

From another perspective, however, this is a blowout. Alice was approved by *80%* of all voters. That is an *absurd* mandate, and it would be very difficult to actually question her status as the Condorcet winner if this was a true election outcome. This is only a "pathology" because we are choosing to assume that 55% of the electorate prefer Bob over Alice, even though they did not express this on their ballots.

Running the election under $C_\infty$, perhaps Clark, knowing he has no chance, told his supporters to rank him first and everyone else last, in a misguided attempt to game the election. Out of voters who expressed a preference between Alice and Bob, still more preferred Alice over Bob (45 (56.25%) to 35 (43.75%)). Therefore, Alice would still be elected. And, based on the ballots, you still wouldn't be able to prove that Alice was not the Condorcet winner either, just like in Approval. The difference? Alice has a weaker mandate. Expression has weakened the legitimacy without changing the outcome.

The [1985 Institute of Management Sciences (TIMS) election](https://www.jstor.org/stable/2632078) <d-cite key="fishburnLittle1988approvalExperiment"></d-cite> is a good example that shows a narrow (and ambiguous) Condorcet winner can be defeated by a candidate who is more broadly acceptable to the electorate. See [this post](../practicalapproval) where I discuss it in more detail.<d-footnote>The Approval winner won by over a hundred approvals. The Condorcet winner was inferred to be strictly preferred over the Approval winner by a single vote (of those who expressed some type of preference), while 27 voters abstained. That's not exactly a strong legitimate claim. Approval broke that ambiguity and would have given a mandate, even though ordinal preferences were in a deadlock.</d-footnote>

### A Remark on Legitimacy

However, unlike any ranked method, [or scoring method with three or more options](../consistentcardinal), Approval never admits a case where another candidate has a legitimate claim to victory over the actual elected candidate, who is a Condorcet winner based on the ballot data.

Simply, any candidate loses an Approval voting election if and only if it was a "skill issue". To be blunt, losing an Approval election is entirely the candidate's fault for not earning enough approvals from the voters. While the case could be made that this is true in plurality voting as well, it cannot be done quite as cleanly.

Unlike choose-one plurality voting, in Approval voting, third-party supporters can vote for the third party *and* for the viable alternative. If they have the pen in their hand, and look at your name, and say "no thanks", then that is entirely your fault for not being able to convince them to support you at literally no cost. *Skill issue*.

Similarly, if there was an underlying Condorcet winner who just couldn't convince their majority to approve them due to their majority preference being sufficiently lukewarm, which is what happened to Bob in the example above, then in that case, all I can say is, "cry about it".

Rather than wax poetic about utility maximization, I go the Condorcet route: If a voter ranks (or approves) Alice above Bob, then all we can say is that they would vote for Alice over Bob in a theoretical one-on-one matchup. As Condorcetists, we do not assume any information about how they would vote in matchups they did not express a preference for. We just take the ballot data at face value, and if Alice is ranked above Bob by more voters than Bob is ranked above Alice, then we say that Alice defeats Bob. Therefore, if Alice gets more approvals than Bob, by Lemma \ref{c2-approval}, Alice defeats Bob in the pairwise matchup.

This does not, in my opinion, lose significant meaning when we restrict to two tiers. Under the conditions of the ballot, if more voters express they would vote for Alice over Bob than the other way around, then that does indeed show something meaningful about the electoral strength and acceptability of Alice and Bob.

In Approval there is no "but I got more first choice votes" argument to be made against a legitimate Condorcet winner, because the Condorcet winner is such *because* they convinced the most voters to approve them over any other candidate in a one-on-one comparison.

Likewise, in Approval there is no "but I was ranked by more voters over the winner" argument, as in ranked-choice voting. And Condorcet can't escape this either, because when a Condorcet cycle inevitably occurs, there is no winner who doesn't lose to at least one other candidate in a one-on-one matchup. So much for "legitimacy" to the winner in those cases. Approval has no cycles, and therefore no ambiguity about who the legitimate winner is based on the ballot data.

My adherence and loyalty to the Condorcet criterion is not because I think the theoretical winner in all one-on-one plurality runoffs is actually the best candidate if there is potentially a better and less polarizing compromise. My loyalty is for the *legitimacy* of the criterion in the only data that truly matters: what the ballots collect.

<img src="/assets/img/approvalcondorcetmeme2.jpg" alt="Approval is the cool Condorcet method" style="width:100%; max-width:600px;">

## You cannot be serious

Oh, but I am. Mostly. Half-and-half.

The sleight of hand that I used in this post was to emphasize the outcomes at the ballot level. I conveniently left out an axiom that any true Condorcetist would absolutely mandate: that voters should be able to rank all candidates if they want to. If that is ultimately important, then a "Generalized Condorcet Method" violates the innate spirit of the Condorcet ideal.

What $C_k$ (including $C_\infty$) *really* does, mathematically, is ask voters to project their arbitrary preferences into a transitive $k$-tiered ("$k$-chotomous") preference order<d-footnote>$C_\infty$ projects into arbitrary transitive preferences, while $k=2$ projects to two-tiered ("dichotomous") preferences. Two-tiered preferences is where Approval is the natural language, works perfectly, and "agrees" with Condorcet <d-cite key="bramsFishburn1978approval"></d-cite></d-footnote>.

### What about the outcomes?

We have established that Approval is a simplified, two-tiered Condorcet method. While those like Munger would argue that this simplification comes at the cost of outcomes, I would argue that the cost is minimal for the benefits we get in return.

The surprising thing is that Approval has been shown to have [essentially the same level of outcomes](https://electionscience.github.io/vse-sim/VSEbasic/) <d-cite key="quinn2017vseSummary"></d-cite> as more complex Condorcet methods in "Voter Satisfaction Efficiency" (VSE).

[I recommend taking a look at some Yee diagrams](http://zesty.ca/voting/sim/) <d-cite key="yee2005simulations"></d-cite>, and tell me if you can truly tell the difference between the Approval and Condorcet diagrams without your reading glasses<d-footnote>In the same vein, [Gary Cox](https://doi.org/10.2307/2111325) <d-cite key="cox1987electoralEquilibrium"></d-cite> has a paper that shows both Approval and Condorcet have strong median pulls. Munger's criticisms that Approval elects "fringe" candidates, based purely on ordinal preferences that have no information about intensity, just do not hold up to scrutiny in my opinion.</d-footnote>.

And even *if* Approval voting occasionally elects a candidate who is not the Condorcet winner, we would literally never even know! You would never be able to *prove* it. The only thing we would see is the candidate who earned approvals from the most voters, and all the others who couldn't manage to convince as many voters.

See this post on [Laslier's Leader rule](../leader-rule) <d-cite key="laslier2009leaderRule"></d-cite> where I discuss equilibrium guarantees<d-footnote>including that Approval elects the Condorcet winner at any strong-nash equilibrium, while no Condorcet method can guarantee election of a Condorcet winner at any nash equilibrium.</d-footnote>.

### Domain Restriction

We have a hierarchy of compromises that a Condorcet method can make.

1. $C_\infty$ simplifies the data by assuming voters have transitive preferences, and allows voters to truncate and express indifference, but allows all possible rankings at the cost of not being able to guarantee a Condorcet winner.
2. $C_2$ simplifies the data by assuming voters can project their preferences into a partition of candidates into "acceptable" and "unacceptable" sets. This is a simplification and compromise that results in the complete elimination of all issues that arise from the Condorcet paradox, while still generally electing the best candidate almost all of the time.
3. Plurality voting restricts $C_2$ to a single choice for the top tier, which allows it to maintain the properties of $C_2$, but is an arbitrary restriction that does not greatly simplify the data, *and* leads to significantly worse outcomes.<d-footnote>Plurality voting, as a matter of fact, also satisfies many of the same properties we have proved for Approval. It is also technically a Condorcet method (based on the ballot data), that satisfies IIA "at the ballot level", if you assume that voters can only like a single candidate and equally dislike all other candidates.</d-footnote>.

$C_2$ is the maximal level that maintains a "reasonable" level of preference expression, still gives excellent outcomes, while still allowing the Condorcet method to work "perfectly".

The fact is, I am an ultra pure Condorcetist. Purer than those who scoff at Approval voting, because I do not just think the Condorcet winner *should* be elected if they exist (in the ballot data). Instead, I believe that if your system cannot guarantee that a Condorcet winner *will* exist (in the ballot data), then it's a broken system with no practical potential. Approval is the purest Condorcet method because it always elects and induces a Condorcet winner!<d-footnote>However, to bring back in a little bit of seriousness to this April Fools' post, I accept that some believe there is value in a more expressive voting system. In particular, if Approval voting elects the Condorcet winner via sincere strategies, then that was done via voters likely choosing one of many sincere strategies. A full ranked method has only one sincere strategy, and there is value to that. Further, the effective rarity of Condorcet cycles "in the wild" (at least, under RCV) means that the guarantee that a Condorcet winner will always exist in the ballot data has limited persuasiveness.</d-footnote>

## Conclusion

In conclusion, Approval voting is a Condorcet method that simplifies the ballot such that it works perfectly every time, all the while providing [essentially the same level of outcomes](https://electionscience.github.io/vse-sim/VSEbasic/) <d-cite key="quinn2017vseSummary"></d-cite> as more complex Condorcet methods.

In an era of distrust in institutions and elections, I believe that simplicity and legitimacy are a prerequisite for trust. And Approval is the Condorcet method which maximizes both.

Fellow Condorcetists, let us unite behind the best and most practical Condorcet method: Approval voting!

And if you are a true Condorcetist who read this far, I would like to extend my genuine thanks for getting through this complete mathematical abuse of the term "Condorcet". However, I hope that it at least convinced you that Approval is, in fact, a two-tiered Condorcet method. Whether or not that changes your opinion of Approval, I leave that up to you!
