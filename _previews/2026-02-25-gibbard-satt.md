---
layout: distill
title: The Gibbard-Satterthwaite Theorem
date: 2026-02-27
description: A walkthrough and proof of the theorem that proves ranked voting systems must be susceptible to strategic voting.
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
related_posts: true
theorems: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: Preliminaries
    subsections:
      - name: Strategyproofness
  - name: Monotonicity and Pareto Efficiency
  - name: Blocking Sets and Their Properties
    subsections:
      - name: Partitioning Blocking Sets
  - name: From Blocking to Dictatorship
  - name: The Gibbard-Satterthwaite Theorem
  - name: Conclusion
    subsections:
      - name: The Approval Voting Exception
  - name: References
---

## Introduction

Based primarily on the proof included in W.D. Wallis' [The Mathematics of Elections and Voting](https://link.springer.com/book/10.1007/978-3-319-09810-4){:target="_blank"}, with more detail. I also referenced [these lecture notes](https://web.stanford.edu/~ashishg/msande336/aut2021/handouts/lecture5_notes.pdf){:target="_blank"} from Ashish Goel's course at Stanford, and this ["simple proof" by Andrew C. Eggers](https://andy.egge.rs/papers/Eggers_GibbardSatterthwaite.pdf){:target="_blank"}.

The Gibbard-Satterthwaite theorem is a fundamental result in social choice theory, which loosely states that no "reasonable" ranked voting system can be strategyproof — there can always be a situation where a voter can get a better result by voting dishonestly. The exception is a "dictatorship", where the whole election is decided by a single voter, and all other ballots are ignored.

Similar to Arrow's impossibility theorem, the intuition is "If we have a voting system that has this nice property, then it's either absurdly undemocratic or must be a dictatorship". In other words, seemingly obvious or desirable properties of a voting system are actually extremely difficult to satisfy when you must aggregate the preferences of multiple voters. The Gibbard-Satterthwaite theorem is focused on the inevitability of strategic voting in ranked voting systems.

## Preliminaries

A social choice function is a function that takes in a profile of votes (a list of voters' rankings of candidates) and outputs a single winner. We will be working with ranked voting systems, where voters must strictly rank candidates without ties.

We will start with two very limited assumptions about our social choice function, including the key strategyproofness property, and show that strategyproofness is so strict that it forces the existence of a dictator.

First, we assume the social choice function respects "citizen sovereignty".

> **Definition:** We say a social choice function respects **citizen sovereignty** if any candidate can win under some profile. For example, if every voter ranks that candidate first.

This may seem like an absurdly weak assumption that any voting system would satisfy, but there are (admittedly very absurd) examples. Take a voting system that chooses the winner based on alphabetical order of candidates. Then, no matter how voters vote, the same candidate will always win. This is a voting system that does not respect citizen sovereignty. This property can be interpreted as "reachability" of candidates: any candidate can be the winner if voters rank them the right way. It is one measure of "responsiveness" for a voting system.

### Strategyproofness

We now define the key property of strategyproofness.

> **Definition:** We call $$f$$ **strategyproof** if the following is satisfied.
>
> Suppose that in a given profile $$P_1$$ we have $$f(P_1)=A$$, and suppose in $$P_1$$ we have a voter $$v$$ with their "honest" ranking $$R_1$$. If we obtain $$P_2$$ from changing $$P_1$$ only by adjusting the vote of $$v$$ (to a dishonest ranking), then one of the following two cases must occur:
>
> 1. $$f(P_1)=f(P_2)=A$$. The winner is preserved.
> 2. If $$f(P_2)=B\neq A$$, then $$A>_{R_1}B$$ in $$v$$'s honest $$P_1$$ ranking.

More concisely, the winner in the honest case is at least weakly preferred to the winner in the dishonest case:

$$f(P_1)\geq_{R_1}f(P_2)$$

The idea is simple: if I change my vote, the winner can't change to something I like better. Otherwise, I have a beneficial strategy, and the system is not strategyproof.

Take an example. If I love Alice, find Bob acceptable, but hate Clark, then my honest ballot would be Alice > Bob > Clark. Now, suppose that Bob is currently winning. If I strategically try to lower Bob, and submit Alice > Clark > Bob, then strategyproofness would mean that doing so could only result in Bob *still* winning, or Clark becoming the new winner. If Alice *could* win by doing that, then that would be a violation of strategyproofness. Any modification of my ballot can only result in a winner who is the same or worse.

All we need is to assume strategyproofness alongside the absurdly minimal assumption of citizen sovereignty, and we will show over the course of this post that this forces the existence of a dictator. To keep things in context, I'm going to be highlighting that fact *constantly*. And I suggest that to keep the motivations of the theorems strong, you should try to play "Where's Waldo" with the dictator. Every step of the proof narrows down where the dictator is hiding.

<img src="/assets/img/waldo_dictator.png" alt="Our glorious leader, Dictator Waldo, standing in line to vote" style="width:100%; max-width:600px;">

> **Lemma:** A dictatorship is strategyproof and respects citizen sovereignty.

**Proof:** If voter $$v$$ is a dictator, then the winner is always the candidate ranked first by the dictator, regardless of how other voters vote. Therefore, the dictator can place any candidate in their first ranking and that candidate will win. Therefore, dictatorship respects citizen sovereignty.

For all voters besides the dictator, ballot adjustments preserve the winner, making dictatorship strategyproof for all voters besides the dictator. The winner can only change if the dictator moves some candidate $$B$$ over their first choice, which we can call $$A$$. If $$R_1$$ has $$A$$ ranked first, and $$R_2$$ has $$B$$ ranked first, then we satisfy that $$f(P_1)=A\geq_{R_1}B=f(P_2)$$. Therefore, dictatorship is strategyproof. In other words, the dictator can only make a lower-ranked candidate win over their top choice. **QED**.

However, first, it will be helpful to establish a very useful consequence of strategyproofness on what happens when a voter moves a candidate up or down in their ranking.

> **Lemma:** If $$f$$ is strategyproof, and we have a profile $$P_1$$ where $$f(P_1)=A$$, and we move from $$P_1\to P_2$$ by changing the ranking of a single voter from $$R_1\to R_2$$ such that another candidate $$X$$ maintains the same relative position as $$A$$, then $$X$$ cannot win in $$P_2$$. \label{relativepositionlemma}

**Proof:** Suppose for contradiction that $$f(P_1)=A$$ and $$f(P_2)=X$$ for $$X\neq A$$. Then, strategyproofness tells us that from moving from $$P_1\to P_2$$,

$$f(P_1)=A\geq_{R_1}X=f(P_2)$$

And moving from $$P_2\to P_1$$,

$$f(P_2)=X\geq_{R_2}A=f(P_1)$$

But if the relative position of $$A$$ and $$X$$ is unchanged, then that precisely means that $$X\geq_{R_2}A$$ if and only if $$X\geq_{R_1}A$$. That is, $$X$$ is now ranked above $$A$$ in $$R_2$$ if and only if it was ranked above $$A$$ in $$R_1$$. Otherwise, $$A$$ is above $$X$$ in both. Thus, since moving from $$P_2$$ to $$P_1$$ implies $$X\geq_{R_2}A$$, and the relative position of $$A$$ and $$X$$ is unchanged, we also have $$X\geq_{R_1}A$$. Therefore, since we also know from moving from $$P_1$$ to $$P_2$$ that we have $$X\geq_{R_1}A$$, we have both

$$X\geq_{R_2}A\implies X\geq_{R_1}A\geq_{R_1}X$$

So $$A=X$$, contradicting our assumption that $$X\neq A$$. **QED**.

This tells us something crucial: when a voter adjusts their ranking, then they can only change the winner by changing the winner's relative position to some other candidate. Otherwise, there is some direction with which we can make that change where it would count as a beneficial strategy.

We can articulate this more precisely with this Corollary:

> **Corollary:** If $$f$$ is strategyproof, and we have a profile $$P_1$$ where $$f(P_1)=A$$, then if we move from $$P_1\to P_2$$ by moving a non-winning candidate $$X$$ up in the ranking of a single voter, then \label{monotonelemma}
>
> 1. If $$X>_{R_1}A$$, then $$f(P_2)=A$$.
> 2. If $$A>_{R_2}X$$, then $$f(P_2)=A$$.

**Proof:** We use Lemma \ref{relativepositionlemma} directly. If $$X>_{R_1}A$$, then moving $$X$$ up will not change the relative position of $$A$$ with $$X$$, and by extension any other candidate, so $$A$$ must still win. If $$A>_{R_2}X$$, then moving $$X$$ up did not change the relative position of $$A$$ and $$X$$, since we would need that $$A>_{R_1}X$$, so $$A$$ must still win. **QED**.

It's worth emphasizing the intuition of this Corollary, as it will be crucial to the proof. The first part of the Corollary says that we can't get a better result by moving a candidate preferred to the winner up. Concretely, lying about how much you like a better candidate can't topple the current winner. For example, if my least favorite candidate, Clark, is currently winning, then adjusting the general order of who I have above Clark can't get me anyone better than Clark. Even if Bob is my second choice, but the best chance I have to beat Clark, then strategically raising him above my favorite Alice, to try to get him some extra points to beat Clark, is not allowed to get me Bob or Alice.

The second part of the Corollary comes down, intuitively, from the fact that burial strategies can't work. On the surface, the second part of the Corollary does not seem particularly useful. If $$A>_{R_2}X$$, then $$A>_{R_1}X$$ as well, since the voter moved $$X$$ up. So the voter is just moving someone worse than the current winner up but still below that current winner. It would be strange if this could topple the current winner, but it's not immediately obvious why this cannot occur. But the reverse framing where we move from $$R_2\to R_1$$ is more intuitive, where $$X$$ is below $$A$$ and then $$X$$ is moved further down.

If $$X$$ *was* the winner in $$P_2$$, and $$A$$ was the winner in $$P_1$$, then that would be a successful burial strategy. By moving the winner $$X$$ down, we managed to get a more preferred candidate $$A$$ to win. This essentially tells us that $$f(P_2)\neq A \implies f(P_1)\neq A$$, or equivalently, $$f(P_1)=A\implies f(P_2)=A$$.

Strategyproofness therefore strongly restricts the effects of moving a candidate up or down in a single voter's ranking. This lack of responsiveness is what will eventually lead us to the conclusion that the only way to satisfy strategyproofness is to have a dictatorship.

## Monotonicity and Pareto Efficiency

> **Definition:** We say that a voting system is **monotonic** if whenever a voter moves a candidate up in their ranking, keeping all else fixed, then either the winner is unchanged, or that moved candidate is the new winner.

Note that this is technically "strong monotonicity", but we will simply call it "monotonicity".

This is a very natural property to expect from a voting system, which is not satisfied by many in common use. For example, Ranked Choice Voting or IRV is famously not monotonic. If a voter moves the current winner up to the top of their ranking, then that can change the elimination order, which can result in a previously eliminated candidate defeating the previous winner.

We will show that the relative positioning properties we have shown in the previous results imply that our strategyproof voting system *must* be monotonic.

> **Proposition:** If $$f$$ is strategyproof and respects citizen sovereignty, then $$f$$ is **monotonic**.

**Proof:** If $$X$$ is the only candidate moved, then the relative position of $$A$$ with all candidates, besides potentially $$X$$, is unchanged. Therefore, no candidate apart from $$X$$ or $$A$$ *can* be the new winner by Lemma \ref{relativepositionlemma}. That is, if $$B$$ is the new winner, then $$B\in\{X,A\}$$. **QED**

Monotonicity falls out quite directly from strategyproofness, driven by how tightly the relative position of the winner between candidates is constrained when moving between profiles.

Further, we can make the observation that moving $$X$$ up can only *possibly* make $$X$$ win if $$X$$ is moved from *under* the current winner to *above* that current winner.

> **Remark:** Monotonicity allows us to have multiple voters move the same candidate up in their rankings and the winner will either be preserved, or change to the moved candidate. This works by applying the monotonicity sequentially to each voter.

Finally, we show another useful consequence of monotonicity.

> **Definition:** We say that a voting system is **Pareto efficient** if whenever every voter ranks candidate $$A$$ above candidate $$B$$, then $$B$$ cannot win.

In particular, if every voter ranks $$A$$ first, then $$A$$ must win (which is a property called unanimity).

Citizen sovereignty, unanimity, and Pareto efficiency are all measures of "responsiveness" for a voting system, but are exceptionally minimal. A dictatorship satisfies all three!

Each has its own intuitive interpretation. As mentioned previously, citizen sovereignty, the weakest assumption, is a property of "reachability" of candidates. Unanimity is a property of "consensus", which implies citizen sovereignty. And Pareto efficiency is a sort of "veto power" property, where every voter is able to reject a candidate by collectively ranking them below some other candidate. Pareto efficiency is the strongest of the three, and implies both citizen sovereignty and unanimity.

> **Corollary:** If $$f$$ is monotonic and respects citizen sovereignty, then $$f$$ is Pareto efficient. Therefore, by the previous Proposition, if $$f$$ is strategyproof and respects citizen sovereignty, then $$f$$ is Pareto efficient. \label{paretolemma}

**Proof:** By citizen sovereignty, there exists a profile $$P$$ where $$A$$ wins. By monotonicity, if every voter moves $$A$$ to the top of their ranking, inducing profile $$P\to P'$$, then $$A$$ must still win. **QED**.

Essentially, we know any candidate *can* win by citizen sovereignty. By monotonicity, we can move that winning candidate above any other candidate, and preserve the winner. Thus, we very easily get Pareto efficiency.

## Blocking Sets and Their Properties

For this section, we assume that we are using a strategyproof voting system that respects citizen sovereignty.

> **Definition:** We say that a set of voters $$S$$ can block candidate $$B$$ with candidate $$A$$", denoted $$A\triangleright_SB$$, whenever every voter in $$S$$ ranks $$A>B$$, then $$B$$ does not win. We call such a set a **blocking set**.

In other words, the voters in $$S$$ can "veto" candidate $$B$$ by ranking some other candidate $$A$$ above $$B$$.

For example, if $$S$$ is the set of all voters and every voter ranks $$A>B$$, then $$f$$ will prefer $$A>B$$. As another example, though it technically does not fall under the purview of our assumptions (but may benefit for intuition), under plurality voting, a strict majority (ex. 61 Senators out of 100) can block any bill by voting no. While many voting systems have a notion of a blocking set, many of the results we prove will rely on the strategyproof assumptions, and results proved in the previous section, such as monotonicity and Pareto efficiency.

The idea we are building up to is that under the strategyproof assumption, any blocking set must contain a dictator. While many other systems allow a group of voters to veto an outcome, strategyproofness forces one of those voters to be the Waldo we're looking for: the dictator.

> **Remark:**
>
> - An empty set cannot block. That is, if $$S=\varnothing$$, then we cannot have $$A\triangleright_\varnothing B$$.
> - The set of all voters is a blocking set, by Pareto efficiency.

It will be extremely important to establish that a set of voters is a blocking set, so we establish the following Lemmas to characterize when we can conclude that a set of voters can block a candidate with another.

> **Lemma:** Suppose we are using a strategyproof voting system that respects citizen sovereignty. If $B$ loses for all profiles where
>
> 1. All voters in $S$ rank $A>B$
> 2. All voters outside of $S$ rank $B$ first
>
> then $A\triangleright_S B$. \label{weakblock}

**Proof:** Suppose $B$ loses whenever all voters in $S$ rank $A>B$ and all voters outside of $S$ rank $B$ first. Assume for contradiction that we have some profile $P$ where $S$ ranks $A>B$ but $B$ wins. Then, by monotonicity, if every voter outside of $S$ moves $B$ to the top, inducing profile $P\to P'$, then $B$ must still win in $P'$. This contradicts our assumption that $B$ loses whenever all voters outside of $S$ rank $B$ first and all voters in $S$ rank $A>B$. Thus, we must have that $A\triangleright_S B$. **QED**.

Again, since we aim to eventually show that $$S$$ contains a dictator, if every voter outside of $$S$$ ranks $$B$$ first, then that is almost the best possible case for $$B$$. The fact that $$B$$ is first outside of $$S$$ is crucial. For example, if $$S$$ didn't contain a dictator, but the complement of $$S$$ did, then if the dictator (outside of $$S$$) ranks, say, $$C>B>A$$, then $$B$$ will still lose. Thus, we would not have sufficiently shown that $$S$$ can *always* block $$B$$ using $$A$$.

The following Lemma characterizes the actual best possible case for $$B$$. If satisfied, then we will be able to conclude that Lemma \ref{weakblock} is satisfied and so $$S$$ is a blocking set.

> **Lemma:** (The Blocking Criterion) Suppose we are using a strategyproof voting system that respects citizen sovereignty. If there exists a single profile $$P$$ where
>
> 1. Every voter in $$S$$ ranks $$A$$ first and $$B$$ second
> 2. Every voter outside of $$S$$ ranks $$B$$ first
>
> and $$B$$ loses, then $$A\triangleright_S B$. \label{blockcriterion}

We remark that Pareto efficiency implies that, since $$B$$ is ranked over all candidates, except $$A$$, by every voter, then only $$B$$ or $$A$$ can possibly win in such a profile. Further, the difference between the conditions of this Lemma versus Lemma \ref{weakblock} is that voters in $$S$$ do not merely rank $$A>B$$, but have moved $$A$$ and $$B$$ to the top of their rankings. Intuitively, this is the best possible case for $$B$$ in a profile satisfying the conditions of Lemma \ref{weakblock}.

This proof is a bit more involved, so I'll preface it with a short roadmap.

**Roadmap:** We'll call the profile described in the conditions of Lemma \ref{blockcriterion} as the "best case" blocking profile for $$B$$: where every voter ranks $$B$$ as highly as they possibly can while $$S$$ still ranks $$A>B$$. We want to show that if $$B$$ loses in their "best case", then they have to lose in any profile satisfying Lemma \ref{weakblock}. It's easier to show that if $$B$$ wins in any profile satisfying Lemma \ref{weakblock}, then they also have to win in their "best case" profile. Since moving from a profile satisfying Lemma \ref{weakblock} to the "best case" profile either maintains relative positioning or involves monotonically increasing $$B$$'s standing, we can guarantee $$B$$ must still win.

**Proof:** We aim to show that if $$P$$ exists then it implies that Lemma \ref{weakblock} must be satisfied. We do this by contrapositive, showing that if $$B$$ can win in some profile $$P'$$ satisfying the conditions of Lemma \ref{weakblock}, then $$B$$ must win in any profile satisfying the conditions of Lemma \ref{blockcriterion}, our new blocking criterion.

Take a profile $$P'$$ satisfying Lemma \ref{weakblock} where $$B$$ wins, meaning $$S$$ ranks $$A>B$$ and every voter outside of $$S$$ ranks $$B$$ first. Let us denote $$S'$$ to be the set of all voters outside of $$S$$. We will show that moving from $$P'$$ to $$P$$ must maintain $$B$$'s win. It suffices to show that an arbitrary voter, in or outside of $$S$$, can change their ballot from that of $$P'$$ to that of $$P$$.

We create intermediate profiles.

$$P'\to P_1$$: Every voter in $$S$$ moves candidate $$A$$ to the top of their ranking. Since voters in $$S$$ already rank $$A$$ over $$B$$, then by Corollary \ref{monotonelemma}, we must preserve the winner.

$$P_1\to P_2$$: Every voter in $$S$$ moves candidate $$B$$ up to their second rank. Since voters in $$S$$ rank $$A>B$$, then the maximum rank of $$B$$ is second on the ballots of voters in $$S$$, so moving from $$P_1\to P_2$$ only potentially involves moving $$B$$ up. By monotonicity, this can only preserve $$B$$'s win.

$$P_2\to P_3$$: For every other candidate $$X$$ distinct from $$A$$ and $$B$$, every voter moves $$X$$ to their place in $$P$$. Since every voter in $$P_2$$ ranks $$B$$ over $$X$$, then by Lemma \ref{relativepositionlemma}, we must preserve the winner.

$$P_3\to P$$: Every voter outside of $$S$$ moves $$A$$ to their place in $$P$$. Since the relative position of $$A$$ and $$B$$ is preserved, as $$B$$ is still ranked first, then the winner must be preserved by Lemma \ref{relativepositionlemma}.

At every step, $$B$$ still wins, so $$B$$ must win in profile $$P$$. Therefore, if $$B$$ loses in any profile satisfying the conditions of Lemma \ref{blockcriterion}, then $$B$$ must lose in any profile satisfying the conditions of Lemma \ref{weakblock}, and thus $$A\triangleright_S B$$. **QED**.

### Partitioning Blocking Sets

We now come to the most important Lemma in the proof, which will be the key to showing that blocking implies dictatorship. This is a tough proof, so I will try to give as much intuition as possible. My suggestion is to keep in mind that we are building up to showing that if $$S$$ can block $$B$$ with $$A$$, then $$S$$ must contain a dictator. This section is, in essence, trying to narrow down where Waldo is.

> **Lemma:** Suppose we have a strategyproof social choice function respecting citizen sovereignty. If $$A\triangleright_S B$$ and $$S=M\sqcup N$$ is a partition of $$S$$, then either
>
> - $$A\triangleright_M C$$ or
> - $$C\triangleright_N B$$ \label{partitionblock}

In a normal voting system satisfying Pareto efficiency, the set of all voters can block any candidate from winning by ranking some other candidate above it. However, normally, we can weaken, dilute, or break this blocking power by splitting the group into sufficiently small subgroups. For example, 60% of Senators can block a bill, but if we split the Senate into two groups of 30% each, then neither group can block the bill on their own. However, under the strategyproof assumption, we find that blocking power is an unbreakable property that never dilutes or breaks, only transfers.

This is the most crucial step in proving the Gibbard-Satterthwaite theorem, so it's worth explaining the underlying mechanics, so that the proof doesn't seem so mysterious.

**Under the hood**: We split $$S$$ into two sets: $$M$$ and $$N$$. We tell the voters in $$M$$ to rank $$A$$ first, and those in $$N$$ to vote for $$C$$ first. We will eventually show that as a blocking set, $$S$$ contains Waldo, our dictator. Therefore, if we tell the voters in $$M$$ and $$N$$ to do this, then the winner tells us which set has Waldo. If $$A$$ wins, then we know $$M$$ has Waldo. We can then have all the voters outside of $$M$$ move $$C$$ up to their top spot and that won't change the fact that Waldo in $$M$$ still ranks $$A$$ first. We can also ask the $$M$$ voters to raise $$C$$ to second place, and that won't change $$A$$ winning either. The Blocking Criterion ensures that $$A$$ blocks $$C$$. Similarly, if $$C$$ wins, then we know $$N$$ has Waldo. We can repeat the same process, moving $$B$$ up, to show that $$C$$ blocks $$B$$ with $$N$$.

Obviously, this works for a dictatorship. But the reason it works more generally based on what we have established thus far is the rigidity of strategyproofness. By being careful about how we move things relative to the winner, we guarantee that the winner is preserved at every step, or else there exists a beneficial strategy from some perspective.

**Proof:** Suppose that $$S=M\sqcup N$$ is a partition of $$S$$, $$S'$$ is the complement of $$S$$, and we have a profile $P_0$ where the reported rankings are

- $$M:A>B>C$$
- $$N:C>A>B$$
- $$S':B>C>A$$

with all other candidates ranked below $$A,B,C$$. By Pareto efficiency, the only possible winners are $$A,B,C$$.

By the assumption that $$A\triangleright_S B$$, since all voters in $$M\sqcup N=S$$ rank $$A>B$$, then $$B$$ must lose. We aim to construct profiles satisfying Lemma \ref{blockcriterion} to show that either $$A\triangleright_M C$$ or $$C\triangleright_N B$$. We will rely heavily on Corollary \ref{monotonelemma}.

We have two cases for $$P_0$$: $$A$$ wins or $$C$$ wins.

If $$A$$ wins, then we make the following adjustments to get to profile $$P_A$$:

- $$S'$$ moves $$C$$ to the top: $$S':B>C>A\to C>B>A$$. By part 1 of Corollary \ref{monotonelemma}, since the moved candidate $$C$$ is already above the original winner $$A$$ in the original ranking, then $$A$$ must still win.
- $$M$$ moves $$C$$ up to second place: $$M:A>B>C\to A>C>B$$. By part 2 of Corollary \ref{monotonelemma}, since the original winner $$A$$ is still above the moved candidate $$C$$ in the adjusted ranking, then $$A$$ must still win.

This creates a profile $$P_A$$ where

- $$M:A>C>B$$
- $$N:C>A>B$$
- $$S':C>B>A$$

which has $$M$$ ranking $$A$$ first and $$C$$ second, every voter outside of $$M$$ ranking $$C$$ first, and $$C$$ losing. By Lemma \ref{blockcriterion}, we must have that $$A\triangleright_M C$$.

Next, if $$C$$ wins, then we make the following adjustments to profile $$P_0$$ to get to profile $$P_C$$:

- $$M$$ moves $$B$$ to the top: $$M:A>B>C\to B>A>C$$. By part 1 of Corollary \ref{monotonelemma}, since the moved candidate $$B$$ is above the original winner $$C$$ in the original ranking, then $$C$$ must still win.
- $$N$$ moves $$B$$ up to second place: $$N:C>A>B\to C>B>A$$. By part 2 of Corollary \ref{monotonelemma}, since the moved candidate $$B$$ is still below the original winner $$C$$ in the adjusted ranking, then $$C$$ must still win.

This creates a profile $$P_C$$ where

- $$M:B>A>C$$
- $$N:C>B>A$$
- $$S':B>C>A$$

which has $$N$$ ranking $$C$$ first and $$B$$ second, every voter outside of $$N$$ ranking $$B$$ first, and $$B$$ losing. By the Blocking Criterion, Lemma \ref{blockcriterion}, we must have that $$C\triangleright_N B$$. **QED**.

## From Blocking to Dictatorship

> **Definition:** We call $$S$$ a *dictating set* if $$A\triangleright_S B$$ for any pair of candidates $$A,B$$. Equivalently, $$S$$ can block any candidate from winning using any other.

By interpreting "blocking" as a sort of "veto power", we can see that a dictator has a similar sort of power. The ability to choose the winner by simply ranking them first is equivalent to making any candidate lose by ranking them below someone else. Our goal is to show that being able to block *one* candidate means the set can block *all* candidates.

> **Remark:** The set of all electors is a dictating set, by Pareto efficiency, and a dictating set with a single voter must have that voter as a dictator.

The power of Lemma \ref{partitionblock} is that we can choose *any* partition. Later we will use partitions where we remove a single voter, but for this next proof we will use the trivial partition $$S=\varnothing\sqcup S$$, and the inability for the empty set to block.

> **Corollary:** If $$A\triangleright_S B$$ and $$C$$ is any other candidate, then $$A\triangleright_S C$$ and $$C\triangleright_S B$$. \label{thirdblock}

More precisely, if $$A\triangleright_S B$$, then $$S$$ can block any third candidate $$C$$ with $$A$$, and $$S$$ can block $$B$$ with any third candidate $$C$$.

**Proof:** Using Lemma \ref{partitionblock}:

- Suppose we take $$M=\varnothing$$, and thus $$N=S$$. Then we cannot have $$A\triangleright_M C$$ since an empty set cannot block. Thus, $$C\triangleright_S B$$.
- Similarly, if $$N=\varnothing$$ and $$M=S$$, then we must have $$A\triangleright_S C$$.

Since both are acceptable partitions, we must have both conditions hold. **QED**.

Essentially, in Lemma \ref{partitionblock}, we said that at least one of the two conditions must hold. This Corollary says that actually *both* conditions must hold. The key is that Lemma \ref{partitionblock} is so powerful because it applies to *any* partition. We can choose the partition to be the trivial one where one side is empty, and since an empty set cannot block, then the other side must block.

Now, we bring it back around, and show that the "veto power" goes both ways.

> **Corollary:** If $$A\triangleright_S B$$, then $$B\triangleright_S A$$. \label{flipblock}

**Proof:** Corollary \ref{thirdblock} applies to any third candidate, so we can make this argument by relabeling candidates.

$$A\triangleright_S B\implies A\triangleright_S C$$

By the same Corollary, taking $B$ as the third candidate

$$A\triangleright_S C\implies B\triangleright_S C$$

And, again, taking $A$ as the third candidate now,

$$B\triangleright_S C\implies B\triangleright_S A$$

**QED**.

At this point, we have essentially shown that the ability to block a single candidate with another actually implies far more power, when we have strategyproofness. In fact, it can block any candidate with any other. In that sense, $$S$$ can make all candidates lose. Therefore, if $$S$$ ranks a candidate $$A$$ over all others, then all other candidates must lose, and so $$A$$ wins. In effect, $$S$$ completely determines the outcome of the election, acting as a coalition that collectively dictates the result.

However, Lemma \ref{partitionblock} will land the crushing blow: any partition of a blocking set contains a blocking set. Perhaps you can see where this is going!

> **Proposition:** If $$A\triangleright_S B$$ for any single pair of two candidates, then $$S$$ is a dictating set. Therefore, $$S$$ is a dictating set if and only if $$A\triangleright_S B$$ for any single pair of two candidates. In other words, being able to block one candidate with another is equivalent to being able to block any candidate with any other. \label{dictateiffsingleblock}

**Proof:** We must show that given $$A\triangleright_S B$$, then $$C\triangleright_S D$$ for any other pair of candidates.

By Corollary \ref{thirdblock}, if $$A\triangleright_S B$$, then $$S$$ can use $$A$$ to block any third candidate. Say, $$A\triangleright_S D$$.

Also by Corollary \ref{thirdblock}, $$S$$ can block $$D$$ with any other candidate. Say, $$C\triangleright_S D$$. **QED**.

Therefore, we have made the connection to blocking and dictatorship. The particular specification of which candidates $$S$$ can block with which are mostly irrelevant.

The final results are as follows.

> **Corollary:** If $$S$$ is a dictating set, and $$S=M\sqcup N$$ is any partition of $$S$$, then either $$M$$ is a dictating set or $$N$$ is a dictating set. \label{dictatepartition}

**Proof:** Suppose $$S$$ is a dictating set and $$S=M\sqcup N$$ is a partition.  Then $$A\triangleright_S B$$ for any two candidates $$A,B$$. By Lemma \ref{partitionblock}, we must have

- $$A\triangleright_M C \implies M$$ is a dictating set
- $$C\triangleright_N B \implies N$$ is a dictating set.

Thus, at least one must be a dictating set. **QED**.

> **Corollary:** If $$S$$ can be partitioned into $$S=S_1\sqcup\ldots\sqcup S_k$$, then at least one of the $$S_i$$ is a dictating set. \label{dictatepartitionk}

**Proof:** We prove this by induction. Corollary \ref{dictatepartition} gives us the base case for $k=2$. For the inductive step, we can take the partition $$S=S_1\sqcup (S_2\sqcup\ldots\sqcup S_k)$$. By Corollary \ref{dictatepartition}, either $$S_1$$ is a dictating set, or $$S_2\sqcup\ldots\sqcup S_k$$ is a dictating set. In the former case, we are done. In the latter case, we can apply the inductive hypothesis to conclude that at least one of the $$S_i$$ for $i>1$ is a dictating set. **QED**.

Waldo is cornered now. If $$S$$ is a dictating set, we can place each member in a separate room, and know that Waldo is in one of those rooms, and everyone in that room is a dictator. Since each room has only one person, that means Waldo is a dictator. The proof of the following theorem is a formalization of this idea.

> **Theorem:** If $$S$$ is a dictating set, then it contains a dictator. \label{dictator}

**Proof:** Let $$S=\left\{v_1,\ldots,v_n\right\}$$ be a dictating set.

Take the partition $$S=\{v_1\}\sqcup\{v_2\}\sqcup\ldots\sqcup\{v_n\}$$. By Corollary \ref{dictatepartitionk}, at least one of the $$\{v_i\}$$ is a dictating set, which means that $$v_i$$ is a dictator. Therefore, $$S$$ contains a dictator. **QED**.

This lets us equate the existence of a blocking set with that of a dictating set, and hence with the existence of a dictator.

We can finally prove the theorem.

## The Gibbard-Satterthwaite Theorem

> **Theorem:** (Gibbard-Satterthwaite) Suppose that we have a ranked voting system, where voters must strictly rank candidates without ties, which respects citizen sovereignty and is strategyproof. Then it must be a dictatorship.

**Proof:** By Corollary \ref{paretolemma}, the voting system must satisfy Pareto efficiency, so the set of all voters $$S$$ is a dictating set. By Theorem \ref{dictator}, $$S$$ contains a dictator. **QED**.

## Conclusion

The proof of the Gibbard-Satterthwaite theorem comes down to a few essential elements:

1. Strategyproofness is an *extremely* strict property.
2. Strategyproofness with citizen sovereignty implies monotonicity and Pareto efficiency.
3. Pareto efficiency implies the trivial existence of a blocking set.
4. Less trivially, any blocking set contains a strictly smaller blocking set when we have strategyproofness.
5. A blocking set doesn't just block a single candidate, but can block all candidates, making it dictatorial.
6. Since we can reduce any dictating (blocking) set into a strictly smaller dictating set, we can show the existence of a single dictator.

While most steps follow naturally from the notion of a blocking set, the real key to the proof is that any blocking set contains a strictly smaller blocking set under strategyproofness. This heavily relied on the fact that strategyproofness is so strict.

Eggers puts it in an interesting way: "strategy-proofness implies preference-proofness". The way strategyproofness is often framed is that being dishonest can't get you a better result. But what does being "honest" or "dishonest" even mean? If you watch a debate between the candidates and decide to adjust your vote based on what you learn, then which vote is the honest one?

The initial desire for strategyproofness comes from the idea that the "original ballot" is the one inside the voter's heart, and a desire for that ballot to be optimal. But the only way to define strategyproofness mathematically is to essentially require that *any* change in the ballot cannot improve the outcome from the perspective of the original ballot, since there is no way to mathematically define the "heart ballot".

Strategyproofness therefore implies a strong lack of responsiveness to ranked ballots in general, requiring the need for a dictator.

### The Approval Voting Exception

We conclude the post with an informal discussion of Approval voting. I have discussed [the nuances of "strategyproofness" in Approval voting](../avstratproof){:target="_blank"} in a previous post, but I think it warrants a discussion here as well, since it is an interesting exception to the Gibbard-Satterthwaite theorem.

Gibbard-Satterthwaite only applies to ranked voting systems. But there are other types of voting systems, such as approval voting, where voters can give independent votes to candidates. Although Gibbard's more general theorem still applies to Approval voting, [Approval in particular has been proven to be strategyproof under a strict assumption about voter preferences](https://www.jstor.org/stable/1955105){:target="_blank"}, which is that voters have "dichotomous preferences": they have a set of candidates they approve of and a set they disapprove of, and are indifferent between all candidates within each group.

The key is that Approval is also strictly monotonic. If a voter approves of a candidate, then that candidate is strictly better off than if the voter disapproves of that candidate. Voting for that candidate can break any tie in their favor, push them into a tie with first place, increase their winning margin, or fail to help them win. But it can never make them go from winning to losing. The optimal strategy, then, is to approve all acceptable candidates and disapprove of all unacceptable candidates. This is strategyproof under the dichotomous preferences assumption, but does not apply when voters have three or more levels of preference.

The intuition for the proof of this is relatively straightforward. If a voter has dichotomous preferences, then

1. Not voting for an acceptable candidate can lead to them losing by one vote to an unacceptable candidate, which is a worse outcome. Therefore, the voter should approve of all acceptable candidates.
2. Voting for an unacceptable candidate can lead to them winning by one vote over an acceptable candidate, which is a worse outcome. Therefore, the voter should disapprove of all unacceptable candidates.

Therefore, there is only one optimal strategy under the dichotomous assumption, which is to approve of all acceptable candidates and disapprove of all unacceptable candidates, which is a sincere strategy. Thus, approval voting is strategyproof under the dichotomous preferences assumption.

This can be extended slightly further, however. If you [decide that, as a voter, your only goal is to elect **any** candidate you deem "acceptable", and no other candidates, then approval voting is strategyproof even if you have more than two levels of preference](../avstratproof){:target="_blank"}. You essentially adopt dichotomous preferences by treating all candidates you deem "acceptable" as equally good and all candidates you deem "unacceptable" as equally bad. This is an obviously very strong assumption about voter preferences, but it is a framing that any voter can choose to adopt.

Calling Approval strategyproof in practice is a bit of a stretch. However, I find it endlessly fascinating that there is indeed a non-dictatorial voting system that is strategyproof, albeit under a very strong assumption about voter preferences.

A common theme of voting theory is that aggregating ranked preferences is extremely difficult to do so fairly and without potential for manipulation. Trying to impose stability, or make manipulation suboptimal collapses into needing to project onto the preferences of just one voter. By simply allowing voters to give independent votes, and restricting to a simple two-tiered preference, Approval voting makes expressing honest two-tiered preferences, like acceptable and unacceptable, the optimal strategy. But only for exactly that: two-tiered preferences. If voters have more complex preferences, then deciding where to draw the line between "acceptable" and "unacceptable" becomes a strategic question, and the strategyproofness of Approval voting breaks down. However, Approval is indeed one of the most sincere voting systems out there. In practice, it's never optimal to vote for one candidate, and not vote for all those candidates you strictly prefer to that candidate.

## References

- Andrew C. Eggers, *A Simple Proof of the Gibbard-Satterthwaite Theorem* (2015). [https://andy.egge.rs/papers/Eggers_GibbardSatterthwaite.pdf](https://andy.egge.rs/papers/Eggers_GibbardSatterthwaite.pdf){:target="_blank"}
- Ashish Goel, *Lecture Notes on Gibbard-Satterthwaite* (2021). [https://web.stanford.edu/~ashishg/msande336/aut2021/handouts/lecture5_notes.pdf](https://web.stanford.edu/~ashishg/msande336/aut2021/handouts/lecture5_notes.pdf){:target="_blank"}
- Brams, S. J., & Fishburn, P. C. (1978). Approval Voting. The American Political Science Review, 72(3), 831–847. [https://doi.org/10.2307/1955105](https://doi.org/10.2307/1955105){:target="_blank"}
- Wallis, W.D. (2014). Arrow’s Theorem and the Gibbard-Satterthwaite Theorem. In: The Mathematics of Elections and Voting. Springer, Cham. [https://doi.org/10.1007/978-3-319-09810-4_5](https://doi.org/10.1007/978-3-319-09810-4_5){:target="_blank"}
