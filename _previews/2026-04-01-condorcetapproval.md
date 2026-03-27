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
  - name: But wait, there's more!
    slug: but-wait-theres-more
    subsections:
      - name: Independence of Irrelevant Alternatives
      - name: Condorcet at Nash Equilibrium
      - name: Strategyproofness
  - name: You cannot be serious
  - name: Conclusion
  - name: Appendix
    subsections:
      - name: The Fine Print
  - name: References
---

## Introduction

Merry April Foolsmas, everyone! Fellow Condorcetists, I come bearing a gift: I have permanently solved the Condorcet paradox. There is in fact a *perfect* voting system: Approval voting, and it *is* indeed a Condorcet method.

> **Definition:** *Approval voting* is a voting system where voters can rank candidates among two tiers: approved and not approved. The candidate who is in the approved tier of the most voters wins.

[For an actually serious argument on the fact that Approval is a practical Condorcet approximation, see this post.](../practicalapproval){:target="_blank"} However, I feel this is a fair argument that, in a practical sense, Approval is the perfect Condorcet method.

During the time of the French revolution, two titans battled out their ideas of what a good voting system were: Their names were Jean-Charles de Borda and the Marquis de Condorcet.

- Borda: Believed that we should give candidates points based on where they are ranked. My lowest ranked candidate gets zero. Next up gets one, and so on. Equivalently, the candidate with the best average ranking wins.
- Condorcet: Had a much better idea:

> **Definition:** A *Condorcet winner* is a candidate who would defeat every other candidate in a one-on-one election.

But it is impractical to hold an election for every $\frac{n(n-1)}{2}$ pair of candidates, or to ask every voter to decide in 45 different one-on-one matchups for 10 candidates just to decide a Comptroller, so we need a voting system that can be used in a single election, is not preposterously hostile to voters, and still satisfies the Condorcet criterion: if there is a Condorcet winner, *and voters express this through their ballots*, then they should win.

We compromise on the idea that we can simulate how voters would vote in each theoretical matchup by ranking candidates. If I rank Alice first, Bob and Clark tied for second, and Dylan last, then I am saying that

- I would vote for Alice over Bob, Alice over Clark, and Alice over Dylan.
- I would vote for Bob over Dylan, and Clark over Dylan.

The single ranked ballot thus allows us to simulate how voters *might* vote in each theoretical matchup, and thus have an idea if there is a Condorcet winner. If there is a candidate who would defeat every other candidate in a head-to-head matchup based on the ballot data, then by golly, they should win!

Further, it's far more efficient to just count up the individual pairwise votes. This is precinct summable: It is realistic for the high school gymnasium to count up the approximately $n(n-1)$ number of pairwise votes, and just post them on the door. This can be added up across precincts, and it only requires simple addition to determine if such a candidate exists. This is much easier than doing something like a *ridiculously complex* algorithm where we count up first choices only, arbitrarily, eliminate the candidate with the least votes, and transfer votes around until someone gets a majority. This would require central tabulation, be more opaque, and have worse outcomes in simulations. [That'd be a really stupid voting system, who would even want to use that?](../ditch-rcv){:target="_blank"} If we count rankings, we should use them! Condorcet only, baby!

### Condorcet is an Approximation

However, the use of rankings to infer one-on-one preferences is an approximation. Every Condorcetist must be honest about this. **So long as we do not directly ask how a voter would vote in every possible matchup, we cannot guarantee that there is a Condorcet winner, nor that we can find them.** We *must* compromise:

> **Axiom:** We do not require voters to directly express their preferences in every possible matchup. Instead, we ask them for a simplified transitive ranking of candidates. We assume that if a voter ranks candidate $A$ above candidate $B$, then that voter would vote for $A$ over $B$ in a head-to-head matchup, and if a voter ranks $A$ and $B$ equally, then that voter would abstain in a head-to-head matchup between $A$ and $B$.

This is a *huge* assumption. It is a *huge* compromise. But it makes the voting system *tractable*. Why can't a voter express that they would vote for Alice over Bob, they would vote for Bob over Clark, but they would vote for Clark over Alice? By restricting voters arbitrarily to a ranking, we are choosing to completely throw away all possible non-transitive preferences alongside all information about the distance and intensity of preferences. We Condorcetists are *all* about throwing away certain information so that preferences are easier to aggregate and treat faithfully!

> **Definition:** A voting system satisfies the *Condorcet criterion* if whenever there is a candidate who would defeat every other candidate in a head-to-head matchup **based on the ballot data**, then that candidate must win.

If you do not elect such a candidate, then **what are you even** ***doing***? [Why ask for rankings if you aren't even going to use or respect them?](../ditch-rcv){:target="_blank"}. If you do not elect such a candidate, then you have elected someone else who has to serve their constituents knowing that a majority of voters wanted someone else more. That creates a [legitimacy problem](../consistentcardinal){:target="_blank"}.

We also cannot guarantee that even if we elect the Condorcet winner induced by the ballots, that this candidate would truly defeat every other candidate in a head-to-head matchup, because we are not asking all those direct head-to-head questions. Especially if we allow ties or ballot truncation. If 45% of voters say they prefer Alice over Bob, and 40% of voters say they prefer Bob over Alice, but 15% of voters did not express a preference between Alice and Bob, then we have no way to prove that Alice truly would defeat Bob in a head-to-head matchup, because those 15% of voters could be split in any way.

They *could* all prefer Bob over Alice, and would vote that way in a runoff, but were too tired to rank them, or didn't want to rank either differently because while they do prefer Alice, they really love or hate both candidates. Real voters truncate their ballots. Real voters do not always provide complete rankings. Real voters do not always have sufficient information to rank all candidates. Real voters are human, and hence messy and complex. Therefore, we must work purely with the data we are given, and trust that it is roughly accurate to the intention of the voters.

It only makes sense to assume that given that more voters expressed a direct preference of Alice over Bob in the ballots were we given, then Alice would indeed defeat Bob in a head-to-head matchup. To assume otherwise would be to completely spit in the face of the data. Alice sufficiently earned the victory by convincing more voters to rank her above Bob, regardless of the unknown underlying preferences of the remaining voters who chose not to express a preference between the two. Electing Alice in this scenario is the only reasonable choice, unless you want to incite a riot led by Alice's supporters.

The biggest question is, however, does such a candidate even exist? How likely is it that if we hold an election with hundreds, thousands, or even millions of voters, that there will be a single candidate who would be ranked above every other candidate by a majority of voters in the ballot data? It turns out the answer can be 100%, or not 100%, depending on the system.

## Generalized Condorcet Methods

> **Definition:** A *Generalized Condorcet method* (GCM) is a voting system where voters can rank candidates, with ties allowed, among some predetermined number of tiers. If a voter ranks candidate X strictly over candidate Y, then that voter casts a vote for X in the X vs Y matchup. If there is a candidate who wins all of their matchups, then that candidate is declared the Condorcet winner and *must* win. We denote a GCM with $k\geq 2$ tiers as $C_k$. If there is no limit on the number of tiers, then we denote it as $C_\infty$.

Simple enough. If 100 voters rank Alice above Bob, and 50 voters rank Bob above Alice, while 600 voters rank Alice and Bob equally, then we choose to assume that Alice defeats Bob and Bob does not defeat Alice. If there is a candidate who defeats every other candidate, then we assume they are the Condorcet winner, and they must win.

We treat the voting system as a function $C_k(P)$, for $k \geq 2$ or $k = \infty$, that takes in a profile $P$ of ballot preferences (compatible with $C_k$) and outputs a single winner. If there is a Condorcet winner, then that candidate must be the unique winner.

> **Axiom:** If no candidate wins all of their matchups, based on the ballot data $P$, then we make no assumption about which candidate is the Condorcet winner or should win. If $P$ induces no Condorcet winner, then we make no assumption about the outcome of $C_k(P)$, and allow that any candidate could potentially be the winner.

Generally, a Condorcet method always chooses the same number of tiers as there are candidates, so that voters could theoretically rank all candidates in a complete transitive order, which is effectively $C_\infty$. But we investigate what happens when we restrict the number of tiers.

## Limited Tiers and the Condorcet Paradox

> **Lemma:** A Condorcet winner can fail to exist if $k>2$. \label{condorcetparadox}

**Proof:** Consider the following profile:

| Voters | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 1      | A        | B        | C        |
| 1      | B        | C        | A        |
| 1      | C        | A        | B        |

In this profile, $A$ defeats $B$ (a majority of voters rank $A$ above $B$), $B$ defeats $C$, and $C$ defeats $A$. There is no Condorcet winner, and this only requires 3 tiers. $\square$

> **Definition:** For $C_2$, we denote $S(A)$ as the number of voters who put candidate $A$ in the approved tier. We denote $S(A>B)$ as the number of voters who put candidate $A$ in the approved tier and candidate $B$ in the not approved tier. And $S(A=B)$ as the number of voters who put both candidates in the approved tier.

Thus, $S(A)=S(A>B)+S(A=B)$, and $S(B)=S(B>A)+S(A=B)$.

> **Lemma:** Candidate $A$ defeats candidate $B$ in $C_2$ if and only if more voters put $A$ in the approved tier.

**Proof:** If more voters put $A$ in the approved tier, then $S(A)>S(B)$. Thus, $S(A>B)+S(A=B)>S(B>A)+S(A=B)$, so $S(A>B)>S(B>A)$, so $A$ defeats $B$. Conversely, if $A$ defeats $B$, then $S(A>B)>S(B>A)$, so $S(A)=S(A>B)+S(A=B)>S(B>A)+S(A=B)=S(B)$. $\square$

> **Theorem:**
>
> 1. $C_2$ induces a transitive majority relation
> 2. There can never be a Condorcet paradox in $C_2$.
> 3. To determine the winner in $C_2$, it suffices to count the number of approvals each candidate receives. The candidate with the most approvals is the Condorcet winner and will win.
> 4. Therefore, $C_2$ is exactly approval voting.
> 5. $C_2$ is the unique GCM that satisfies the first three properties. They do not hold for any $C_k$ where $k>2$.

**Proof:** This follows directly from the previous result.

**Claim 1:** By the previous lemma, $A$ defeats $B$ if and only if $S(A)>S(B)$. Thus, the ordinal ranking of candidates by $S(\cdot)$ is the same as the majority relation. Since the ordinal ranking of candidates by $S(\cdot)$ is a sequence of real numbers, it is totally ordered and thus transitive.

**Claim 2:** This directly implies the absence of a Condorcet paradox in $C_2$. Suppose that $A$ defeats $B$, and $B$ defeats $C$. Then $S(A)>S(B)$ and $S(B)>S(C)$, so $S(A)>S(C)$ by transitivity of the real numbers, so $A$ defeats $C$.

**Claim 3:** As a Condorcet method, $C_2$ must elect the Condorcet winner whenever one exists. By the previous lemma, the candidate with the most approvals is the Condorcet winner. Therefore, $C_2$ always elects the candidate with the most approvals, and that candidate will always be the Condorcet winner.

Therefore, $C_2$ is exactly approval voting. 

**Claim 5:** By Lemma \ref{condorcetparadox}, any $C_k$ where $k>2$ can admit a Condorcet paradox, so it cannot satisfy the first two properties. To conclude the proof, we show that if $k>3$ then a candidate with the most first ranks is not necessarily the Condorcet winner. Consider the following profile:

| Voters | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 3      | A        | B        | C        |
| 2      | B        | C        | A        |
| 2      | C        | B        | A        |

In this profile, $A$ has the most first ranks, but $B$ defeats both $A$ and $C$, so $A$ is not the Condorcet winner. $\square$

Boom, Approval is a Condorcet method! It is precisely Condorcet consistent based on the ballot data, which is really the only kind of Condorcet consistency that any Condorcetist seems to care about.

Not only that, it is also the *only Condorcet method that can guarantee the existence of a Condorcet winner*.

<img src="/assets/img/approvalcondorcetmeme1.jpg" alt="Approval is not two-tiered score, but two tiered Condorcet" style="width:100%; max-width:600px;">

Further, the last property of the theorem implies that we need only count the number of approvals each candidate receives to determine the winner and all the pairwise matchup data is perfectly captured by the approval scores. Therefore, practically, Approval only requires tallying up $n$ numbers, rather than approximately $n(n-1)$ numbers for precinct summability.

$n(n-1)$ is not very much, particularly for small $n$. But $n$ is even less and obviously grows more slowly. Further, if you wanted to do it really slickly, you could just have a single marginal pairwise tally for each candidates. So rather than $A>B$ being $+1$ for $A$ over $B$, and $B>A$ being $+1$ for $B$ over $A$, you could just have a single tally for $A$ where $A>B$ is $+1$ and $B>A$ is $-1$.

## You can't prove it's not Condorcet

As we have proved, Approval voting is indeed a Condorcet method, just restricted to two tiers. This is a restriction to binary "acceptable" vs "unacceptable" preferences, just as a ranked method is a restriction of an arbitrary preference ordering to a transitive one. But as a Condorcet method, it always elects the candidate who would win all pairwise matchups against other candidates based on the preferences expressed in the ballot data.

However, unlike any ranked method, [or scoring method with three or more options](../consistentcardinal){:target="_blank"}, Approval never admits a case where another candidate has a legitimate claim to victory over the actual elected candidate, who is a Condorcet winner.

As with any Condorcet method, all we have to go on is what voters express. Therefore, if there is, say, a true Condorcet winner if we theoretically held all pairwise matchups, and that candidate does not win, we can never know. But how *could* a candidate like that lose?

Simply, any candidate loses an Approval voting election if and only if it was a skill issue. To be blunt, losing an Approval election is entirely the candidate's fault for not earning enough approvals from the voters. While the case could be made that this is true in plurality voting as well, not quite as cleanly.

True, you lose plurality because not enough voters picked you. And if a third party sapped enough votes from you, well that is partially your fault. But under Approval, this isn't a proper excuse, because those third party voters can approve that third party *and* you. They had the pen in their hand, they looked at your name, and said "no thanks". Thus, if you get "spoiled", it's not because that third party candidate exists, it's because you couldn't convince their voters to also support you. In that case, all I can say is "cry about it".

### You can't prove it IS Condorcet

However, like we also said, for an arbitrary Condorcet method that allows full rankings, we can't prove the winner is actually the true Condorcet winner because we didn't actually hold all pairwise matchups. Unless you ask *every* single voter how they would vote in every possible pairwise matchup, I reject that you can prove the winner is the true Condorcet winner based on a ranked ballot election. You can probably have a very strong heuristic argument, but not a formal proof.

## But wait, there's more!

We have so far proved that Approval voting *is* a Condorcet method restricted to two tiers, and that it has a number of unique advantages over other Condorcet methods, but there's so much more!

### Independence of Irrelevant Alternatives

> **Definition:** A voting method satisfies independence of irrelevant alternatives (IIA) if the social preference between any two candidates depends only on the individual preferences between those two candidates, and not on the presence or absence of other candidates. That is, if we change the ballots from $P$ to $P'$ such that the relative ranking of candidates $A$ and $B$ is the same in both $P$ and $P'$, then the social preference between $A$ and $B$ should also remain the same.

To quote a humorous story from philosopher Sidney Morgenbesser:

> Morgenbesser, ordering dessert, is told by a waitress that he can choose between blueberry or apple pie. He orders apple. Soon the waitress comes back and explains cherry pie is also an option. Morgenbesser replies "In that case, I'll have blueberry."

Intuitively, changing how voters rank candidates that are not $A$ or $B$ should not affect the social preference between $A$ and $B$. Too bad no ranked voting method can satisfy IIA... Unless?

> **Theorem:** Approval voting is the unique GCM that satisfies independence of irrelevant alternatives.

**Proof:** First we show that if $k>2$, then $C_k$ cannot satisfy IIA. We have proven that $C_k$ can admit a cycle. Suppose that $P$ is one such profile of three candidates $X,Y,Z$ where candidate $X$ defeats candidate $Y$ who defeats candidate $Z$ who defeats candidate $X$. Now suppose without loss of generality that $C_k(P)=X$. Therefore, society ranks $X$ above $Y$ and $Z$.

Construct a profile $P'$ from $P$ by having every voter move $Y$ to the bottom of their ranking, without changing the relative ranking of $X$ and $Z$. Since there are at least three tiers available, this is always possible. In this new profile, $Z$ still defeats $X$, but now both $X$ and $Z$ defeat $Y$. This means that $Z$ is now the Condorcet winner in $P'$, so society ranks $Z$ above $X$. We therefore have a violation of IIA, because the social preference between $X$ and $Z$ has changed despite the relative ranking of $X$ and $Z$ remaining the same.

Finally, we show that Approval voting satisfies IIA. Suppose that $S_P(A) > S_P(B)$, implying $S_P(A>B) > S_P(B>A)$, under some profile $P$, where $S_P(X)$ denotes the approval score of candidate $X$ in profile $P$ and $S_P(X>Y)$ denotes the number of voters who strictly approve $X$ over $Y$. If we change the ballots from $P$ to $P'$ such that the relative ranking of candidates $A$ and $B$ is the same in both $P$ and $P'$, then we cannot change the approval of $A$ and $B$ for any voter who distinguishes between $A$ and $B$. Therefore, $S_P(A>B)=S_{P'}(A>B)$ and $S_P(B>A)=S_{P'}(B>A)$ represent the exact same set of voters in $P$ and $P'$, meaning

$$\begin{multline*}
S_P(A>B)-S_P(B>A)=S_{P'}(A>B)-S_{P'}(B>A)\\
\implies S_P(A)-S_P(B)=S_{P'}(A)-S_{P'}(B)\\
\implies S_P(A)>S_P(B) \iff S_{P'}(A)>S_{P'}(B)
\end{multline*}$$

Therefore, $A$ has more total approvals than $B$ in $P$ if and only if $A$ has more total approvals than $B$ in $P'$. $\square$

We can see that Approval voting actually satisfies a sort of "super-IIA" property, since the *exact* numerical distance between the approval scores of any two candidates remains unchanged when the relative ranking of those two candidates is preserved, regardless of changes in the approval of other candidates. That is, Approval is highly immutable with respect to the relative ranking of any two candidates. Voters *must* change how they express their relative preferences between two candidates in order to affect the social preference between them.

### Condorcet at Nash Equilibrium

For Approval voting, we need to define a crucial concept: a sincere strategy.

> **Definition:** A strategy or ballot in Approval voting is **sincere** if a voter also approves of all candidates strictly preferred to any candidate they approve. That is, a voter does not leave any "holes" in their approval ranking.

There are many "sincere" strategies in Approval voting, corresponding to different ways of drawing a line of acceptability in a voter's ranking.

> **Definition:** A Nash Equilibrium is a strategy profile in which no single voter can unilaterally deviate in a way that makes them strictly better off. A Strong Nash Equilibrium is a strategy profile in which no coalition of voters can jointly deviate in a way that makes every member of the coalition strictly better off.

The whole point of a Condorcet method is to elect the Condorcet winner whenever one exists, right? Then... shouldn't we hope that this happens at a Nash Equilibrium? The following results are from Steven Brams's 2008 book ["Mathematics and Democracy"](https://press.princeton.edu/books/paperback/9780691133218/mathematics-and-democracy){:target="_blank"} (Chapter 2).

> **Theorem:** When a Condorcet winner exists,
>
> 1. Approval voting has a strong Nash Equilibrium under sincere strategies in which the Condorcet winner is elected.
> 2. Any strong Nash Equilibrium under sincere strategies in Approval voting must elect a unique Condorcet winner.

We will not prove these theorems here, but they can be found in Brams's book. There are also some other important results I will mention in [the fine print](#the-fine-print){:target="_blank"}. I will, however, prove something that Brams alludes to but does not formally prove, as well as one of the other Theorems he includes.

> **Theorem:** Any strong Nash Equilibrium in Approval voting is a Strong Nash Equilibrium under both sincere and insincere strategies.

**Proof:** Suppose that we have a strong Nash Equilibrium in Approval voting under sincere strategies in a profile $P$, which Brams proves exists when a Condorcet winner exists. Suppose $W$ is the Condorcet winner, who must be currently winning, and let $X$ be any other candidate. We break the voters into five groups:

| Number of voters | Preference | Approves of $W$ | Approves of $X$ |
|------------------|------------|-----------------|-----------------|
| $G_1$            | $W>X$      | Yes             | No              |
| $G_2$            | $X>W$      | No              | Yes             |
| $G_3$            | $X>W$      | Yes             | Yes             |
| $G_4$            | $W>X$      | Yes             | Yes             |
| $G_5$            | $W>X$      | No              | No              |

We are assuming all voters are voting sincerely, so every voter is accounted for in one of the groups $G_1$ through $G_5$.

It suffices to prove that no coalition of voters who prefer $X$ to $W$ can deviate in a way that gives $X$ more approvals than $W$. By assumption, no coalition can do so with a sincere strategy. Particularly, $G_2$ and $G_3$ cannot form a coalition that would allow $X$ to surpass $W$ in approvals.

Since $W$ is the Condorcet winner, we know that the group who prefer $W$ to $X$ is larger than the group who prefer $X$ to $W$, so $G_1+G_4+G_5>G_2+G_3$.

Suppose that $G_3$ strategically omit $W$ from their approval set by adjusting to a new sincere strategy. Then the new $S(W)=G_1+G_4$ and $S(X)=G_2+G_3$. By the assumption that $P$ is a strong Nash Equilibrium under sincere strategies, no coalition can improve their outcome by deviating, so this deviation cannot result in $X$ winning over $W$. Thus, the strict approvals of $W$ must still be greater than the strict approvals of $X$: $G_1>G_2+G_3$.

The best possible case for $X$ is that all voters in $G_2$ and $G_3$ approve $X$ only--possibly insincerely--and no other candidate. But even then, $X$ only gets $G_2+G_3$ strict approvals, which we just showed is less than the strict approvals of $W$: $G_1$. Thus, $W$ still wins.

Therefore, no insincere strategy by any coalition of voters who prefer $X$ to $W$ can result in $X$ winning over $W$ from a strong Nash Equilibrium under sincere strategies. $\square$

And here's the kicker: While Approval voting has a strong Nash Equilibrium under both sincere and insincere strategies where the Condorcet winner is elected, and those are the only strong Nash Equilibria, no other Condorcet-consistent voting system can guarantee the election of a Condorcet winner in any kind of Nash equilibrium. The following is a proof by Brams in that same chapter.

> **Theorem:** If $k>2$, then $C_k$ is not strategyproof, nor can it ensure the election of a Condorcet winner as a Nash equilibrium. That is, if $P$ has a Condorcet winner $W$, then $P$ might not be a Nash equilibrium. Voters could benefit from misrepresenting their preferences and prevent the Condorcet winner from being elected.

**Proof:** Consider the following profile:

| Number of Voters | Preference Order $P$ |
|------------------|----------------------|
| 1                | $A > B > C$          |
| 1                | $B > C > A$          |
| 1                | $C > A > B$          |

Consider the following cases:

1. If $C_k(P)=A$, then suppose that the truthful preference of the first voter is actually $A>C>B$. If that was true, then the true Condorcet winner is $C$ in that honest profile $P_C$. Thus, moving from $P_C$ to $P$ by having the first vote bury $C$ to the bottom of their ranking results in a profitable deviation for the first voter, by changing the winner from their second favorite, $C$, to their first favorite, $A$.
2. If $C_k(P)=B$, then suppose that the truthful preference of the second voter is actually $B>A>C$. If that was true, then the true Condorcet winner is $A$ in that honest profile $P_A$. Thus, moving from $P_A$ to $P$ by having the second vote bury $A$ to the bottom of their ranking results in a profitable deviation for the second voter, by changing the winner from their second favorite, $A$, to their first favorite, $B$.
3. If $C_k(P)=C$, then suppose that the truthful preference of the third voter is actually $C>B>A$. If that was true, then the true Condorcet winner is $B$ in that honest profile $P_B$. Thus, moving from $P_B$ to $P$ by having the third vote bury $B$ to the bottom of their ranking results in a profitable deviation for the third voter, by changing the winner from their second favorite, $B$, to their first favorite, $C$.

In all cases, we have that a single voter can benefit by throwing the system into a cycle by burying the true Condorcet winner, so $C_k$ is not strategyproof, and the profiles $P_A$, $P_B$, and $P_C$ are not Nash equilibria. $\square$

This tells us that the more complex systems designed entirely to elect the Condorcet winner whenever detected by the more complex ballot cannot even boast that such election is a Nash equilibrium. Whereas the simpler system of Approval voting can guarantee that if there is a Condorcet winner, then there is a strong Nash equilibrium, and any strong Nash equilibrium must elect a Condorcet winner.

Sure, of course you can construct a pathological case where Approval elects the Condorcet loser by having voters vote stupidly. Just as the above proof constructs a pathological case where an election of just three voters can result in the system being thrown into a cycle by a single voter. However, the point is that Approval voting is still solidly good at electing the Condorcet winner, and more complex Condorcet methods still cannot even guarantee that they fulfill their main purpose as a Nash equilibrium.

### Strategyproofness

No... it can't be... No voting system can be strategyproof, can it? But... what of [Gibbard-Satterthwaite](../gibbard-satt){:target="_blank"}?

> **Definition:** A voting system is *strategyproof* if there exists a sincere dominant strategy for every voter, meaning that no voter can benefit from misrepresenting their preferences regardless of what the other voters do.

*Obviously*, any voter who participates in an election wants an acceptable candidate. And if you ask a voter if they find a candidate acceptable, and hold a gun to their head and refuse to take anything but "yes" or "no" as an answer, then of course the voter will be able to give you a truthful answer.

The following is a result from Brams and Fishburn which we will not prove.

> **Lemma:** Any optimal, non-dominated strategy for a voter in Approval voting involves voting for all candidates in a voter's highest tier and none in their lowest tier.

There is never any reason not to approve of your favorite(s) and to disapprove of your least favorite(s). This gives us the following result:

> **Theorem:** Approval voting is strategyproof under the goal of electing any acceptable candidate, with a dominant strategy for each voter being to approve all candidates they find acceptable and disapprove all candidates they find unacceptable.

We assume that if a voter ranks $A$ above $B$, then they prefer $A$ winning outright to $A$ tying with $B$ to $B$ winning outright. Under the goal of electing any acceptable candidate, we assume that a voter prefers any acceptable candidate winning to any unacceptable candidate winning, and [that is their entire preference ordering](#the-fine-print).

**Proof:** Consider a single voter with a particular honest preference that they find all candidates in a set $S$ acceptable and all candidates not in $S$ unacceptable. Under the goal of electing any acceptable candidate, all acceptable candidates comprise the voter's top tier, and all unacceptable candidates comprise the voter's bottom tier, so the voter's optimal strategy is to approve all candidates in $S$ and disapprove all candidates not in $S$. $\square$

Intuitively, consider any deviation from this strategy:

1. If the voter fails to vote for an acceptable candidate, then they may fail to break a tie between that candidate and an unacceptable candidate, resulting in a less preferred outcome. Therefore, having all acceptable candidates in the approval set strictly dominates any strategy that excludes acceptable candidates.
2. If the voter votes for an unacceptable candidate, then they may cause that candidate to tie with or surpass an acceptable candidate, resulting in a less preferred outcome. Therefore, having no unacceptable candidates in the approval set strictly dominates any strategy that includes unacceptable candidates.

Hence, voting sincerely for all acceptable candidates and against all unacceptable candidates is a unique dominant and sincere strategy for each voter. This proves that Approval voting is strategyproof under the goal of electing any acceptable candidate.

## You cannot be serious

Oh, but I am. Mostly. Half-and-half.

Here's what is absolutely true: Because no Condorcet method asks voters to directly vote in every possible head-to-head matchup, we cannot assume that any ranked method can perfectly capture the Condorcet winner in all cases, because you simply cannot assume all voters have transitive preferences over all candidates, *and* you can't force voters to completely rank all candidates without ties unless you want to bottleneck turnout.

There is one point (among many) that should be addressed, however. Plurality voting, as a matter of act, also satisfies many of the same properties we have proved for Approval. It is also technically a Condorcet method that satisfies IIA, and it is also strategyproof if you assume that voters can only like a single candidate and equally dislike all other candidates. However, this isn't the gotcha some might think, because this is so because plurality is just an arbitrary restriction on Approval voting. Approval voting is precisely the minimal level of ballot restriction we can place on a Condorcet method to ensure that it's "perfect".

All Condorcetists choose to simplify the data through some sort of limitation on what ballots voters can cast, for the purpose of making the system tractable and practical. And we have a hierarchy of compromises that a Condorcet method can make.

1. $C_\infty$ simplifies the data by assuming voters have transitive preferences, but allows all possible rankings at the cost of guaranteeing a Condorcet winner.
2. $C_k$ for $k>2$ simplifies the data by assuming voters have transitive preferences within some number of tiers. This still allows for paradoxes and does not really simplify the data much beyond unnecessarily restricting voters to a small number of tiers.
3. $C_2$ simplifies the data by assuming voters can project their preferences into a partition of candidates into "acceptable" and "unacceptable" sets. This is a simplification and compromise that results in the complete elimination of all issues that arise from the Condorcet paradox, and allows us to perfectly capture the Condorcet winner in all cases based on the ballot data.
4. Plurality voting restricts $C_2$ to a single choice for the top tier, which allows it to maintain the properties of $C_2$, but is an arbitrary restriction that does not simplify the data significantly.

$C_2$ is the maximal level that maintains a "reasonable" level of preference expression that allows the Condorcet method to work "perfectly". Here's the truth: I am an ultra pure Condorcetist. Purer than those who scoff at Approval voting, because I do not just think the Condorcet winner *should* be elected if they exist, I think if your system cannot guarantee that one will, then it's a broken system with no practical potential. Approval is the purest Condorcet method because it always elects and induces a Condorcet winner.

<img src="/assets/img/approvalcondorcetmeme2.jpg" alt="Approval is the cool Condorcet method" style="width:100%; max-width:600px;">

Another way to look at it is that Approval voting is a Condorcet method that changes the question from asking voters for a ranking which may or may not accurately reflect their preferences in one-on-one elections into a simpler question: who do you consent to govern you?

The latter question is binary and well defined. And because it is binary, it is impossible to induce a Condorcet paradox. If you are a fellow Condorcetist who scoffs that this question is *too* restrictive, then I reject that your arbitrary restriction is any less arbitrary than mine. Mine, however, has the following benefits:

1. Making the system far more practical for voters and administrators
2. Always defines and elects a Condorcet winner
3. Ensures full legitimacy to the winner in every possible election scenario. No other candidate can claim to be more deserving of the winner than the candidate with the most approvals.
4. Eliminates the possibility of a Condorcet paradox, ensuring a clear and decisive outcome in every election.
5. Simplifies the voting process, reducing cognitive load on voters and minimizing the potential for errors in ballot completion.
6. Voters who don't have the time to rank 10 candidates for Comptroller can still participate meaningfully by simply approving the candidates they find acceptable.

We absolutely restrict the expression of voters to do this. And it's a normative choice to make that practicality should be prioritized over the ability to express more complex preferences. But here's why I think it's the right choice:

1. Approval, in practice and in simulations, elects the true Condorcet winner exceptionally often, depending on strategy. Up to 90% or more. And even when it doesn't, you literally can't prove it. Approval gets you the same or more legitimacy than a Condorcet method would, but 100% of the time instead of 100% of the time minus cycles.
2. Also in simulations, Approval has been shown to have essentially the same level of outcomes as more complex Condorcet methods. Whereas Ranked Robin gets up to about 99% VSE, Approval gets up to about 95%. That's nearly 96% of the way there *with other benefits* as listed above.
3. In an era of distrust in institutions and elections, I believe that simplicity and clarity are a prerequisite for trust. And I do not trust that a generic Condorcet method is sufficiently simple and transparent (particularly in the case of a cycle, rare as they may be) in all cases to be a permanent solution. Approval is the only system I think is simple enough to be that permanent solution, and I think it *has to be the first step*. Approval tomorrow, Condorcet next week is something I might be willing to get behind.

## Conclusion

## Appendix

### The Fine Print

To be perfectly clear: Approval voting is strategyproof under the goal of electing an acceptable candidate, if you can cleanly partition the candidates into "acceptable" and "unacceptable" sets for each voter. But in general, Approval voting is not strategyproof for any realistic sense of voter preferences beyond completely black-and-white acceptability judgments.

Further, IIA is only satisfied by Approval voting at the ballot level. The introduction of a candidate, for example, can indeed change the decision of a voter about whether or not to approve other candidates, because the new candidate may alter the voter's perception of which candidates are acceptable. For example, maybe I'd vote for Bob and Dylan against Clark. But if Alice suddenly enters the race, then screw Bob and Dylan! I love Alice so much I will only approve of her.

## References
