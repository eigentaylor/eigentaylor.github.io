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
  - name: Conclusion
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

We treat the voting system as a (possibly non-deterministic) function $C_k(P)$, for $k \geq 2$ or $k = \infty$, that takes in a profile $P$ of ballot preferences (compatible with $C_k$) and outputs a single winner. If there is a Condorcet winner, then that candidate must be the unique winner.

> **Axiom:** If no candidate wins all of their matchups, based on the ballot data $P$, then we make no assumption about which candidate is the Condorcet winner or should win. If $P$ induces no Condorcet winner, then we make no assumption about the outcome of $C_k(P)$, and allow that any candidate could potentially be the winner.

Generally, a Condorcet method uses the same number of tiers as there are candidates, so that voters could theoretically rank all candidates in a complete transitive order, which is effectively $C_\infty$. But what if we only allow voters to rank candidates in a limited number of tiers?

## Limited Tiers and the Condorcet Paradox

> **Lemma:** A Condorcet winner can fail to exist if $k>2$.

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

> **Corollary:** To determine the winner in $C_2$, it suffices to count the number of approvals each candidate receives. The candidate with the most approvals is the Condorcet winner and will win. That is, $C_2$ is exactly approval voting.

**Proof:** This follows directly from the previous result. Two tier rankings with ties is exactly equivalent to bubbling multiple names to indicate approval, and treating non-approved candidates as disapproved. Therefore, counting the number of approvals each candidate receives is sufficient to determine the Condorcet winner in $C_2$, which is exactly the same as approval voting. $\square$

Boom, Approval is a Condorcet method! It is precisely Condorcet consistent based on the ballot data, which is really the only kind of Condorcet consistency that any Condorcetist seems to care about. But wait, there's more!

> **Proposition:** $C_2$ induces a transitive majority relation, and thus there can never be a Condorcet paradox in $C_2$.

**Proof:** By the previous lemma, $A$ defeats $B$ if and only if $S(A)>S(B)$. Thus, the ordinal ranking of candidates by $S(\cdot)$ is the same as the majority relation. Since the ordinal ranking of candidates by $S(\cdot)$ is a sequence of real numbers, it is totally ordered and thus transitive.

This directly implies the absence of a Condorcet paradox in $C_2$. Suppose that $A$ defeats $B$, and $B$ defeats $C$. Then $S(A)>S(B)$ and $S(B)>S(C)$, so $S(A)>S(C)$ by transitivity of the real numbers, so $A$ defeats $C$. $\square$

> **Theorem:** A Condorcet winner always exists for $C_k$ if and only if $k=2$. Further, as a GCM, that Condorcet winner will win without fail.

**Proof:** If $k=2$, then by the previous results, the candidate with the most approvals must defeat every other candidate, so there is a Condorcet winner. Conversely, if $k>2$, then by the first lemma, there can be a profile with no Condorcet winner. As a GCM, the Condorcet winner must win by definition. $\square$

Not only is Approval a Condorcet method, it is also the *only Condorcet method that can guarantee the existence of a Condorcet winner* when restricted to two tiers.

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

Finally, we show that Approval voting satisfies IIA. Suppose that $S(A) > S(B)$ under some profile $P$, where $S(X)$ denotes the approval score of candidate $X$. If we change the ballots from $P$ to $P'$ such that the relative ranking of candidates $A$ and $B$ is the same in both $P$ and $P'$, then we can only make the following changes:

- For a voter who ranks $A>B$ in $P$: They must still rank $A>B$ in $P'$, so their approval of $A$ and $B$ remains consistent. They may change their approval of other candidates, but this does not affect the relative approval scores of $A$ and $B$.
- For a voter who ranks $B>A$ in $P$: They similarly must still rank $B>A$ in $P'$, so their approval of $A$ and $B$ remains consistent.
- For a voter who ranks $A=B$ in $P$: They must still rank $A=B$ in $P'$, but they can choose to collectively move them both up or down between approval and disapproval. They may also change the approval of other candidates.

In all cases, no voter who distinguished between $A$ and $B$ in $P$ changes their approval of $A$ or $B$ in $P'$. Therefore, $S(A>B)$ and $S(B>A)$ remain the same in $P'$, though $S(A)$ and $S(B)$ may change due to changes in approval of other candidates. However,

$$S(A)-S(B)=S(A>B)-S(B>A)$$

which are the same in $P'$ as they were in $P$. Therefore, while the raw approval scores of $A$ and $B$ may change due to changes in approval of other candidates, the exact difference $S(A)-S(B)$ remains the same. Therefore, $A$ has more total approvals than $B$ in $P$ if and only if $A$ has more total approvals than $B$ in $P'$. Since societal ranking is determined by the order of approval scores, Approval voting satisfies IIA, and is thus the only GCM that does so. $\square$

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

> **Theorem:** If $k>2$, then $C_k$ cannot ensure the election of a Condorcet winner as a Nash equilibrium. That is, if $P$ has a Condorcet winner, and all voters are voting sincerely, then $P$ isn't necessarily a Nash equilibrium. Voters could benefit from misrepresenting their preferences and prevent the Condorcet winner from being elected.

**Proof:** Consider the following profile:

| Number of Voters | Preference Order $P$ |
|------------------|----------------------|
| $2$              | $A > B > B > C$      |
| $2$              | $B > D > C > A$      |
| $1$              | $C > A > B > D$      |

TODO: finish this proof

### Strategyproofness

No... it can't be... No voting system can be strategyproof, can it? But... what of [Gibbard-Satterthwaite](../gibbard-satt){:target="_blank"}?

> **Definition:** A voting system is *strategyproof* if there exists a sincere dominant strategy for every voter, meaning that no voter can benefit from misrepresenting their preferences regardless of what the other voters do.

*Obviously*, any voter who participates in an election wants an acceptable candidate. And if you ask a voter if they find a candidate acceptable, and hold a gun to their head and refuse to take anything but "yes" or "no" as an answer, then of course the voter will be able to give you a truthful answer.

> **Theorem:** Approval voting is strategyproof under the goal of electing an acceptable candidate, with a dominant strategy for each voter being to approve all candidates they find acceptable and disapprove all candidates they find unacceptable.

We assume that if a voter ranks $A$ above $B$, then they prefer $A$ winning outright to $A$ tying with $B$ to $B$ winning outright.

**Proof:** Consider a single voter with a particular honest preference that they find all candidates in a set $S$ acceptable and all candidates not in $S$ unacceptable. Consider any deviation from this strategy:

1. If the voter fails to vote for an acceptable candidate, then they may fail to break a tie between that candidate and an unacceptable candidate, resulting in a less preferred outcome. The outcome for any election with this ballot is identical to the outcome if the voter adds the acceptable candidate to their approval set, except that the acceptable candidate may now tie with or surpass the unacceptable candidate. Therefore, having all acceptable candidates in the approval set strictly dominates any strategy that excludes acceptable candidates.
2. If the voter votes for an unacceptable candidate, then they may cause that candidate to tie with or surpass an acceptable candidate, resulting in a less preferred outcome. The outcome for any election with this ballot is identical to the outcome if the voter drops the unacceptable candidate from their approval set, except that the unacceptable candidate may no longer tie with or surpass the acceptable candidate. Therefore, having no unacceptable candidates in the approval set strictly dominates any strategy that includes unacceptable candidates.

Therefore, voting sincerely for all acceptable candidates and against all unacceptable candidates is a unique dominant and sincere strategy for each voter. This proves that Approval voting is strategyproof under the goal of electing an acceptable candidate. $\square$

## You cannot be serious

Oh, but I am. Mostly. Half-and-half.

Here's what is absolutely true: Because no Condorcet method asks voters to directly vote in every possible head-to-head matchup, we cannot assume that any ranked method can perfectly capture the Condorcet winner in all cases, because you simply cannot assume all voters have transitive preferences over all candidates, *and* you can't force voters to completely rank all candidates without ties unless you want to bottleneck turnout.

Approval voting is a Condorcet method that changes the question from asking voters for a ranking which may or may not accurately reflect their preferences into a simpler question: who do you consent to govern you?

The latter question is binary and well defined. And because it is binary, it is impossible to induce a Condorcet paradox. If you are a fellow Condorcetist who scoffs that this question is *too* restrictive, then I reject that your arbitrary restriction is any less arbitrary than mine. Mine, however, has the following benefits:

1. Making the system far more practical for voters and administrators
2. Always defines and elects a Condorcet winner
3. Ensures full legitimacy to the winner in every possible election scenario. No other candidate can claim to be more deserving of the winner than the candidate with the most approvals.
4. Eliminates the possibility of a Condorcet paradox, ensuring a clear and decisive outcome in every election.
5. Simplifies the voting process, reducing cognitive load on voters and minimizing the potential for errors in ballot completion.
6. Voters who don't have the time to rank 10 candidates for Comptroller can still participate meaningfully by simply approving the candidates they find acceptable.

## Conclusion

## Appendix

### The Fine Print

To be perfectly clear: Approval voting is strategyproof under the goal of electing an acceptable candidate, if you can cleanly partition the candidates into "acceptable" and "unacceptable" sets for each voter. But in general, Approval voting is not strategyproof for any realistic sense of voter preferences beyond completely black-and-white acceptability judgments.

Further, IIA is only satisfied by Approval voting at the ballot level. The introduction of a candidate, for example, can indeed change the decision of a voter about whether or not to approve other candidates, because the new candidate may alter the voter's perception of which candidates are acceptable. For example, maybe I'd vote for Bob and Dylan against Clark. But if Alice suddenly enters the race, then screw Bob and Dylan! I love Alice so much I will only approve of her.

## References
