---
layout: distill
title: A Proof of the Gibbard-Satterthwaite Theorem
date: 2026-02-25
description: A detailed proof of the Gibbard-Satterthwaite theorem, based on W.D. Wallis' work.
giscus_comments: true
importance: 2
tags: voting
category: polisci
featured: true
related_posts: true
theorems: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: Definitions and Monotonicity
  - name: Blocking Sets
  - name: Dictating Sets
  - name: The Gibbard-Satterthwaite Theorem
  - name: Conclusion
  - name: The Approval Voting Exception
  - name: References
---

## Introduction

Based primarily on the proof include in W.D. Wallis' [The Mathematics of Elections and Voting](https://link.springer.com/book/10.1007/978-3-319-09810-4){:target="_blank"}, with more detail. I also referenced [these lecture notes](https://web.stanford.edu/~ashishg/msande336/aut2021/handouts/lecture5_notes.pdf){:target="_blank"} from Ashish Goel's course at Stanford, and this ["simple proof" by Andrew C. Eggars](https://andy.egge.rs/papers/Eggers_GibbardSatterthwaite.pdf){:target="_blank"}.

The Gibbard-Satterthwaite theorem is a fundamental result in social choice theory, which loosely states that "reasonable" voting system can be strategyproof. That is, there can always be a situation where a voter can get a better result by voting dishonestly. The exception is a "dictatorship", where the whole election is decided by a single voter, and all other ballots are ignored.

Similar to Arrow's impossibility theorem, the intuition is "If we have a voting system that has this nice property, then it must be a dictatorship". That is, seemingly obvious or desirable properties of a voting system are actually extremely difficult to satisfy when you must aggregate the preferences of multiple voters. The Gibbard-Satterthwaite theorem is focused on the inevitability of strategic voting in ranked voting systems.

## Definitions and Monotonicity

A social choice function is a function that takes in a profile of votes (a list of voters' rankings of candidates) and outputs a single winner. We will be working with ranked voting systems, where voters must strictly rank candidates without ties.

We will start with two very limited assumptions about our social choice function, including the key strategyproofness property, and show that strategyproofness is so strict that it forces the existence of a dictator.

First, we assume the social choice function respects "citizen sovereignty".

> **Definition 1:** We say a social choice function respects *citizen sovereignty* if any candidate can win under some profile. For example, if every voter ranks that candidate first.

This may seem like an absurdly weak assumption that any voting system would satisfy, but there are (admittedly very absurd) examples. Take a voting system that chooses the winner based on alphabetical order of candidates. Then, no matter how voters vote, the same candidate will always win. This is a voting system that does not respect citizen sovereignty. Intuitively, this property can be interpreted as "reachability" of candidates. Any candidate can be the winner if voters rank them in the right way. This is one measure of "responsiveness" for a voting system.

We now define the key property of strategyproofness.

> **Definition 2:** We call $$f$$ *strategyproof* if the following is satisfied.
>
> Suppose that in a given profile $$P_1$$ we have $$f(P_1)=A$$, and suppose in $$P_1$$ we have a voter $$v$$ with their honest ranking $$R_1$$. If we obtain $$P_2$$ from changing $$P_1$$ only by adjusting the vote of $$v$$ (to a dishonest ranking), then one of the following two cases must occur:
>
> 1. $$f(P_1)=f(P_2)=A$$. The winner is preserved.
> 2. If $$f(P_2)=B\neq A$$, then $$A>_{R_1}B$$ in $$v$$'s honest $$P_1$$ ranking.

More concisely, the winner in the honest case is at least weakly preferred to the winner in the dishonest case:

$$f(P_1)\geq_{R_1}f(P_2)$$

Intuitively, if I change my vote, then the winner can't change to something I like better. Otherwise, I have a beneficial strategy, and the system is not strategyproof.

All we need is to assume strategyproofness alongside the absurdly minimal assumption of citizen sovereignty, and we will show that this forces the existence of a dictator.

However, first, it will be helpful to establish a very useful consequence of strategyproofness on what happens when a voter moves a candidate up or down in their ranking.

> **Lemma 1:** If $$f$$ is strategyproof, and we have a profile $$P_1$$ where $$f(P_1)=A$$, then if we move from $$P_1\to P_2$$ by moving a candidate $$X$$ up in the ranking of a single voter, then \label{monotonelemma}
>
> 1. If $$X>_{R_1}A$$, then $$f(P_2)=A$$.
> 2. If $$A>_{R_2}X$$, then $$f(P_2)=A$$.

**Proof:** Suppose that $$f(P_1)=A$$ and $$f(P_2)=B$$. Then, strategyproofness tells us that from moving from $$P_1\to P_2$$,

$$f(P_1)=A\geq_{R_1}B=f(P_2)$$

And moving from $$P_2\to P_1$$,

$$f(P_2)=B\geq_{R_2}A=f(P_1)$$

Now we suppose the first condition: that $$X>_{R_1}A$$. Then, we have $$X>_{R_1}A\geq_{R_1}B$$, so $$X>_{R_1}B$$. Therefore, $$X\neq B$$, so the relative ordering of $$A$$ and $$B$$ is unchanged, so $$B\geq_{R_2}A$$ implies that $$B\geq_{R_1}A\geq_{R_1}B$$, so $$f(P_2)=B=A=f(P_1)$$.

Suppose the second condition instead now: that $$A>_{R_2}X$$. Then, we have $$B\geq_{R_2}A>_{R_2}X$$, so $$B\neq X$$, again. So the relative ordering of $$A$$ and $$B$$ is unchanged, so $$B\geq_{R_1}A$$ implies that $$B\geq_{R_2}A\geq_{R_2}B$$, so $$f(P_2)=B=A=f(P_1)$$. QED.

Suppose that the voter prefers $$X$$ to $$A$$ in $$P_1$$. Then, if the voter tries to make $$X$$ win by moving $$X$$ up, then either $$A$$ still wins or $$X$$ wins by monotonicity. If $$X$$ wins, then the voter has a beneficial strategy, contradicting strategyproofness. Thus, $$A$$ must still win.

Suppose instead that the voter has $$A$$ above $$X$$ in $$P_2$$. Assume for contradiction that $$X$$ wins in $$P_2$$. Then, if the voter goes back to $$P_1$$, by moving $$X$$ down, they managed to get a more preferred candidate, $$A$$, to win by burying $$X$$. This is a beneficial strategy, contradicting strategyproofness. Thus, $$A$$ must still win in $$P_2$$. QED.

> **Lemma 2:** If $$f$$ is strategyproof and respects citizen sovereignty, then $$f$$ is monotonic. That is, if a voter moves a candidate $$X$$ strictly up in their ranking, keeping all else fixed, then either the winner is unchanged, or $$X$$ is the new winner.

**Proof:** Take a profile $$P_1$$ and suppose that $$f(P_1)=A$$. Consider a voter $$v$$ with honest ranking $$R_1$$. Suppose that $$v$$ moves $$X$$ strictly up in their ranking to get ranking $$R_2$$ that induces profile $$P_2$$, and suppose that $$f(P_2)=B$$. If $$A=B$$, then there is nothing to show. So we will show that if $$A\neq B$$, then $$B=X$$.

First, let's suppose that $$X$$ is distinct from both $$A$$ and $$B$$. Then, we know the relative ranking of $$A$$ and $$B$$ is unchanged, so we have two cases:

- If $$v$$ prefers $$B$$ to $$A$$ (ranks $$B>_{R_1}A$$ and $$B>_{R_2}A$$), then this would be a beneficial strategy, contradicting strategyproofness.
- If $$v$$ prefers $$A$$ to $$B$$ (ranks $$A>_{R_1}B$$ and $$A>_{R_2}B$$), then $$v$$ would have a beneficial strategy moving from $$P_2$$ to $$P_1$$, also contradicting strategyproofness.

Thus, we cannot have $$X$$ be distinct from both $$A$$ and $$B$$. Therefore, $$B\in\{A,X\}$$. That is, moving $$X$$ up can only either preserve the winner or make $$X$$ the new winner. So $$f$$ is monotonic. QED.

We now establish a very useful lemma that limits the effects of monotonicity.

> **Lemma 3:** If $$f$$ is strategyproof, and we have a profile $$P_1$$ where $$f(P_1)=A$$, then if we move from $$P_1\to P_2$$ by moving a candidate $$X$$ up in the ranking of a single voter, then \label{monotonelemma}
>
> 1. If $$X>_{R_1}A$$, then $$f(P_2)=A$$.
> 2. If $$A>_{R_2}X$$, then $$f(P_2)=A$$.

**Proof:** Suppose that the voter prefers $$X$$ to $$A$$ in $$P_1$$. Then, if the voter tries to make $$X$$ win by moving $$X$$ up, then either $$A$$ still wins or $$X$$ wins by monotonicity. If $$X$$ wins, then the voter has a beneficial strategy, contradicting strategyproofness. Thus, $$A$$ must still win.

Suppose instead that the voter has $$A$$ above $$X$$ in $$P_2$$. Assume for contradiction that $$X$$ wins in $$P_2$$. Then, if the voter goes back to $$P_1$$, by moving $$X$$ down, they managed to get a more preferred candidate, $$A$$, to win by burying $$X$$. This is a beneficial strategy, contradicting strategyproofness. Thus, $$A$$ must still win in $$P_2$$. QED.

It's worth emphasizing the intuition of this lemma, as it will be crucial to the proof. The first part of the lemma says that we can't get a better result by moving a candidate preferred to the winner up. That is, lying about how much you like a better candidate can't topple the current winner.

The second part of the lemma comes down, intuitively, from the fact that burial strategies can't work. On the surface, the second part of the lemma does not seem particularly useful. If $$A>_{R_2}X$$, then $$A>_{R_1}X$$ as well, since the voter moved $$X$$ up. So the voter is just moving someone worse than the current winner up but still below that current winner. It would be strange if this could topple the current winner, but it's not immediately obvious why this cannot occur. But the reverse framing where we move from $$R_2\to R_1$$ is more intuitive, where $$X$$ is below $$A$$ and then is moved further down.

If $$X$$ *was* the winner in $$P_2$$, and $$A$$ was the winner in $$P_1$$, then that would be a successful burial strategy. By moving the winner $$X$$ down, we managed to get a more preferred candidate $$A$$ to win. This essentially tells us that $$f(P_2)\neq A \implies f(P_2)\neq A$$, or equivalently, $$f(P_1)=A\implies f(P_2)=A$$.

Strategyproofness therefore strongly restricts the effects of moving a candidate up or down in a single voter's ranking. This lack of responsiveness is what will eventually lead us to the conclusion that the only way to satisfy strategyproofness is to have a dictatorship.

Finally, we show another useful consequence of monotonicity.

> **Definition 3:** We say that a voting system is *Pareto efficient* if whenever every voter ranks candidate $$A$$ above candidate $$B$$, then $$B$$ cannot win.

In particular, if every voter ranks $$A$$ first, then $$A$$ must win (which is a property called unanimity).

Citizen sovereignty, unanimity, and Pareto efficiency are all measures of "responsiveness" for a voting system, but are exceptionally minimal. A dictatorship satisfies all three! Each has its own intuitive interpretation. As mentioned previously, citizen sovereignty, the weakest assumption, is a property of "reachability" of candidates. Unanimity is a property of "consensus", which implies citizen sovereignty. And Pareto efficiency is a sort of "veto power" property, where every voter is able to reject a candidate by collectively ranking them below some other candidate. Pareto efficiency is the strongest of the three, and implies both citizen sovereignty and unanimity.

> **Lemma 4:** If $$f$$ is monotonic and respects citizen sovereignty, then $$f$$ is Pareto efficient. Therefore, by lemma 2, if $$f$$ is strategyproof and respects citizen sovereignty, then $$f$$ is Pareto efficient.

**Proof:** By citizen sovereignty, there exists a profile $$P$$ where $$A$$ wins. By monotonicity, if every voter moves $$A$$ to the top of their ranking, inducing profile $$P\to P'$$, then $$A$$ must still win. QED.

Essentially, we know any candidate *can* win by citizen sovereignty. By monotonicity, we can move that winning candidate above any other candidate, and preserve the winner. Thus, we very easily get Pareto efficiency.

## Blocking Sets

> **Definition 4:** We say that a set of voters "$$S$$ can block candidate $$B$$ with candidate $$A$$", denoted $$A\triangleright_SB$$, if whenever every voter in $$S$$ ranks $$A>B$$, then $$B$$ does not win.

$$A \triangleright_S B$$

For example, if $$S$$ is the set of all voters and every voter ranks $$A>B$$, then $$f$$ will prefer $$A>B$$. As another example, though it technically does not fall under the purview of our assumptions (but may benefit for intuition), under plurality voting, a strict majority (ex. 61 Senators out of 100) can block any bill by voting no.

The idea we are building up to is that under the strategyproof assumption, any blocking set must contain a dictator.

> **Remark 1:**
>
> - An empty set cannot block. That is, if $$S=\varnothing$$, then we cannot have $$A\triangleright_\varnothing B$$.
> - The set of all voters is a blocking set.

> **Lemma 5:** If $B$ loses for all profiles where
>
> 1. All voters in $S$ rank $A>B$
> 2. All voters outside of $S$ rank $B$ first
>
> then $$A\triangleright_SB$$. \label{weakblock}

**Proof:** Suppose $$B$$ loses whenever all voters in $$S$$ rank $$A>B$$ and all voters outside of $$S$$ rank $$B$$ first. Assume for contradiction that we have another profile $$P$$ where $$S$$ ranks $$A>B$$ but $$B$$ wins. Then, by monotonicity, if every voter outside of $$S$$ moves $$B$$ to the top, inducing profile $$P\to P'$$, then $$B$$ must still win in $$P'$$. This contradicts our assumption that $$B$$ loses whenever all voters outside of $$S$$ rank $$B$$ first and all voters in $$S$$ rank $$A>B$$. Thus, we must have that $$A\triangleright_SB$$. QED.

Again, since we aim to eventually show that $$S$$ contains a dictator, if every voter outside of $$S$$ ranks $$B$$ first, then that is almost the best possible case for $$B$$. The fact that $$B$$ is first outside of $$S$$ is crucial. For example, if $$S$$ didn't contain a dictator, but the complement of $$S$$ did, then if the dictator (outside of $$S$$) ranks, say, $$C>B>A$$, then $$B$$ will still lose. Thus, we would not have sufficiently shown that $$S$$ can *always* block $$B$$ using $$A$$.

The following lemma characterizes the actual best possible case for $$B$$. If satisfied, then we will be able to conclude that lemma 5 is true.

> **Lemma 6:** (The Blocking Criterion) If there exists a single profile $$P$$ where
>
> 1. Every voter in $$S$$ ranks $$A$$ first and $$B$$ second
> 2. Every voter outside of $$S$$ ranks $$B$$ first
> 3. $$B$$ loses
>
> then $$A\triangleright_SB$$. \label{blockcriterion}

**Proof:** We aim to show that if $$P$$ exist then it implies that Lemma 5 must be true.

Take any profile $$P'$$ satisfying Lemma \ref{weakblock}. That is, in $$P'$$ we have that $$S$$ ranks $$A>B$$ and every voter outside of $$S$$ ranks $$B$$ first. We will show that moving from $$P$$ to $$P'$$ must maintain $$B$$'s loss.

Since $$B$$ loses, then by monotonicity we can have all voters in $$S$$ move $$B$$ down to its place in $$P'$$, and $$B$$ will still lose.

We now rearrange the profile to get to  $$P'$$. Take the candidate right above $$B$$'s new place in the ranking of $$S$$, and move it to the top (which moves $$A$$ down to second place in the ranking of voters in $$S$$). By monotonicity, either that new candidate wins, or the previous non $$B$$ candidate wins (either way, $$B$$ still loses). Repeat until $$A$$ is in its place in $$P'$$, and $$B$$ will still lose. Thus, Lemma \ref{weakblock} is satisfied. QED.

The intuitive idea of this lemma is that profile in Lemma 6 is the absolute best case for $$B$$ while still satisfying that $$S$$ ranks $$A>B$$. If $$B$$ loses in this profile, then $$B$$ must lose in any other profile where $$S$$ ranks $$A>B$$.

We now come to the most important lemma in the proof, which will be the key to showing that blocking implies dictatorship. This is a tough proof, so I will try to give as much intuition as possible.

> **Lemma 7:** If $$A\triangleright_SB$$ and $$S=M\sqcup N$$ is a partition of $$S$$, and $$S'$$ is the complement of $$S$$, then either
>
> - $$A\triangleright_MC$$ or
> - $$C\triangleright_NB$$ \label{partitionblock}

**Proof:** Suppose that we have a profile $P_0$ where the reported rankings are

- $$M:A>B>C$$
- $$N:C>A>B$$
- $$S':B>C>A$$

with all other candidates ranked below $$A,B,C$$. By Pareto efficiency, the only possible winners are $$A,B,C$$.

By the assumption that $$A\triangleright_SB$$, since all voters in $$M\sqcup N=S$$ rank $$A>B$$, then $$B$$ must lose. We aim to construct profiles satisfying Lemma \ref{blockcriterion} to show that either $$A\triangleright_MC$$ or $$C\triangleright_NB$$. We will rely heavily on Lemma \ref{monotonelemma}.

We have two cases for $$P_2$$: $$A$$ wins or $$C$$ wins.

If $$A$$ wins, then we make the following adjustments to get to profile $$P_A$$:

- $$S'$$ moves $$C$$ to the top: $$S':C>B>A$$. By part 1 of Lemma \ref{monotonelemma}, since the moved candidate $$C$$ is above the original winner $$A$$ in the original ranking, then $$A$$ must still win.
- $$M$$ moves $$C$$ up to to second place: $$M:A>C>B$$. By part 2 of Lemma \ref{monotonelemma}, since the original winner $$A$$ is above the moved candidate $$C$$ in the adjusted ranking, then $$A$$ must still win.

This creates a profile $$P_A$$ where

- $$M:A>C>B$$
- $$N:C>A>B$$
- $$S':C>B>A$$

which has $$M$$ ranking $$A$$ first and $$C$$ second, every voter outside of $$M$$ ranking $$C$$ first, and $$C$$ losing. By Lemma \ref{blockcriterion}, we must have that $$A\triangleright_MC$$.

Next, if $$C$$ wins, then we make the following adjustments to profile $$P_0$$ get to profile $$P_C$$:

- $$M$$ moves $$B$$ to the top: $$M:B>A>C$$. By part 1 of Lemma \ref{monotonelemma}, since the moved candidate $$B$$ is above the original winner $$C$$ in the original ranking, then $$C$$ must still win.
- $$N$$ moves $$B$$ up to second place: $$N:C>B>A$$. By part 2 of Lemma \ref{monotonelemma}, since the moved candidate $$B$$ is still below the original winner $$C$$ in the adjusted ranking, then $$C$$ must still win.

This creates a profile $$P_C$$ where

- $$M:B>A>C$$
- $$N:C>B>A$$
- $$S':B>C>A$$

which has $$N$$ ranking $$C$$ first and $$B$$ second, every voter outside of $$N$$ ranking $$B$$ first, and $$B$$ losing. By Lemma \ref{blockcriterion}, we must have that $$C\triangleright_NB$$. QED.

The intuitive idea here is that if $$S$$ can block $$B$$ with $$A$$, then we can split $$S$$ into two parts which place $$A$$ over $$B$$: one part that has $$A$$ first, and the other part that has $$C$$ first. Keeping in mind that we are building up to a dictator in $$S$$, then the winner must be either $$A$$ or $$C$$, depending on if the dictator is in the first part or the second part, respectively.

Monotonicity and strategyproofness then allow us to adjust the profile to get the best possible case for whichever relevant candidate is not the winner, and show that they still lose.

> **Lemma 8:** If $$A\triangleright_SB$$ and $$C$$ is any other candidate, then $$A\triangleright_SC$$ or $$C\triangleright_SB$$. \label{thirdblock}

That is, if $$A\triangleright_SB$$, then $$S$$ can block any third candidate $$C$$ with $$A$$, and $$S$$ can block $$B$$ with any third candidate $$C$$.

**Proof:** Using Lemma \ref{partitionblock}:

- Suppose we take $$M=\varnothing$$, and thus $$N=S$$. Then we cannot have $$A\triangleright_MC$$ since an empty set cannot block. Thus, $$C\triangleright_SB$$.
- Similarly, if $$N=\varnothing$$ and $$M=S$$, then we must have $$A\triangleright_SC$$.

QED.

> **Lemma 9:** If $$A\triangleright_SB$$, then $$B\triangleright_SA$$. \label{flipblock}

**Proof:** By Lemma \ref{thirdblock},

$$A\triangleright_SB\implies A\triangleright_SC$$

By the same lemma, taking $B$ as the third candidate

$$A\triangleright_SC\implies B\triangleright_SC$$

And, again, taking $A$ as the third candidate now,

$$B\triangleright_SC\implies B\triangleright_SA$$

QED.

At this point, we have essentially shown that the ability to block a single candidate with another actually implies far more power. In fact, it can block any candidate with any other. In that sense, $$S$$ can make all candidates lose. Therefore, if $$S$$ ranks a candidate $$A$$ over all others, then all other candidates must lose, and so $$A$$ wins. That is, $$S$$ exactly chooses the result of the election, making it a sort of collection of voters who together act as a dictator.

However, Lemma \ref{partitionblock} will land the crushing blow: any partition of a blocking set contains a blocking set. Perhaps the reader can see where this is going!

## Dictating Sets

> **Definition 5:** We call $$S$$ a *dictating set* if $$A\triangleright_SB$$ for any pair of candidates $$A,B$$. That is, if $$S$$ can block any candidate from winning using any other.

> **Remark 2:** The set of all electors is a dictating set, by Pareto efficiency, and a dictating set with a single voter must have that voter as a dictator.

> **Lemma 10:** If $$A\triangleright_SB$$ for any single pair of two candidates, then $$S$$ is a dictating set.

**Proof:** We must show that given $$A\triangleright_SB$$, then $$C\triangleright_SD$$ for any other pair of candidates.

By lemma \ref{thirdblock}, if $$A\triangleright_SB$$, then $$S$$ can use $$A$$ to block any third candidate. Say, $$A\triangleright_SD$$.

Also by lemma \ref{thirdblock}, $$S$$ can block $$D$$ with any other candidate. Say, $$C\triangleright_SD$$. QED.

Therefore, we have made the connection to blocking and dictatorship. The particular specification of which candidates $$S$$ can block with which are mostly irrelevant. Being able to block once implies dictatorial power.

The final lemmas are as follows.

> **Lemma 11:** If $$S$$ is a dictating set, and $$S=M\sqcup N$$ is any partition of $$S$$, then either $$M$$ is a dictating set or $$N$$ is a dictating set. \label{dictatepartition}

**Proof:** Suppose $$S$$ is a dictating set and $$S=M\sqcup N$$ is a partition.  Then $$A\triangleright_SB$$ for any two candidates $$A,B$$. By lemma \ref{partitionblock}, we must have

- $$A\triangleright_MC \iff M$$ is a dictating set
- $$C\triangleright_N B \iff N$$ is a dictating set.

Thus, at least one must be a dictating set.

> **Lemma 12:** If $$S$$ is a dictating set, then it contains a dictator. \label{dictator}

**Proof:** Let $$S=\left\{v_1,\ldots,v_n\right\}$$ be a dictating set.

Take the partition $$S=\left\{v_1\right\}\sqcup S_{1}$$ (where $$S_1=S\setminus\left\{v_1\right\}$$). Then by Lemma \ref{dictatepartition}, either $$\{v_1\}$$ or $$S_1$$ is a dictating set with a strictly lower cardinality. If $$\{v_1\}$$ is a dictating set, $$v_1$$ is a dictator and we are done. Otherwise, let

$$S_i:= S_{i-1}\setminus\{v_i\}$$

Then, eventually we will reach $$S_{n-1}=\{v_{n-1}\}\sqcup \{v_n\}$$. If no $$v_i$$ was a dictator for $$i<n-1$$, then one of $$\{v_{n-1}\}, \{v_n\}$$ must be a dictating set, in which case $$v_{n-1}$$ or $$v_n$$ is a dictator. Therefore $$S$$ must contain a dictator. QED.

Therefore, we can equate the existence of a blocking set with that of a dictating set and therefore with that of a dictator.

We can finally prove the theorem.

## The Gibbard-Satterthwaite Theorem

> **Theorem 1 (Gibbard-Satterthwaite):** Suppose that we have a ranked voting system, where voters must strictly rank candidates without ties, which respects citizen sovereignty and is strategyproof. Then it must be a dictatorship.

**Proof:** We will show that there must exist a dictating set, and thus by Lemma \ref{dictator} there must be a dictator.

Trivially, we can see that a dictatorship does indeed satisfy both requirements.

By lemma 1, the voting system must satisfy Pareto efficiency, so the set of all voters $S$ is a dictating set. By lemma \ref{dictator}, $S$ contains a dictator. QED.

## Conclusion

The proof comes down to a few essential elements:

1. Strategyproofness is an *extremely* strict property.
2. Strategyproofness with citizen sovereignty implies monotonicity and Pareto efficiency.
3. Pareto efficiency implies the trivial existence of a blocking set.
4. Less trivially, any blocking set contains a strictly smaller blocking set. This relies heavily on the strategyproofness.
5. A blocking set doesn't just block a single candidate, but can block all candidates, making it dictatorial.
6. Since we can reduce any dictating (blocking) set into a strictly smaller dictating set, we can show the existence of a single dictator.

While most lemmas follow relatively straightforwardly from the intuitive idea of a blocking set, the real key to the proof is that any blocking set contains a strictly smaller blocking set. This heavily relied on the fact that strategyproofness is so strict.

Eggers puts it in an interesting way: "strategy-proofness implies preference-proofness". The way strategyproofness is often framed is that being dishonest can't get you a better result. But what does being "honest" or "dishonest" even mean? If you watch a debate between the candidates and decide to adjust your vote based on what you learn, then which vote is the honest one?

The initial desire for strategyproofness comes from the idea that the "original ballot" is the one inside the voter's heart, and a desire for that ballot to be optimal. But the only way to define strategyproofness mathematically is to essentially require that *any* change in the ballot cannot improve the outcome from the perspective of the original ballot, since there is no way to mathematically define the "heart ballot".

Strategyproofness therefore implies a strong lack of responsiveness to ballots in general, requiring the need for a dictator.

## The Approval Voting Exception

Now, Gibbard-Satterthwaite only applies to ranked voting systems. But there are other types of voting systems, such as approval voting, or SCORE voting, where voters can give independent scores to candidates. Approval voting in particular has been proven to be strategyproof under an extremely strict assumption about voter preferences, which is that voters have "dichotomous preferences". That is, voters have a set of candidates they approve of and a set of candidates they disapprove of, and they are indifferent between all candidates in the same set.

The key is that Approval is strictly monotonic. If a voter approves of a candidate, then that candidate is strictly better off than if the voter disapproves of that candidate. Voting for that candidate can break any tie in their favor, push them into a tie with first place, increase their winning margin, or fail to help them win. But it can never make them go from winning to losing. The optimal strategy, then, is to approve all acceptable candidates and disapprove of all unacceptable candidates. This is strategyproof under the dichotomous preferences assumption, but does not apply when voters have three or more levels of preference.

The proof for this is relatively straightforward. If a voter has dichotomous preferences, then

1. Not voting for an acceptable candidate can lead to them losing by one vote to an unacceptable candidate, which is a worse outcome. Therefore, the voter should approve of all acceptable candidates.
2. Voting for an unacceptable candidate can lead to them winning by one vote over an acceptable candidate, which is a worse outcome. Therefore, the voter should disapprove of all unacceptable candidates.

Therefore, there is only one optimal strategy, which is to approve of all acceptable candidates and disapprove of all unacceptable candidates, which is a sincere strategy. Thus, approval voting is strategyproof under the dichotomous preferences assumption.

This can be extended slightly further, however. If you [decide that, as a voter, your only goal is to elect **any** candidate you deem "acceptable", and no other candidates, then approval voting is strategyproof even if you have more than two levels of preference](../avstratproof){:target="_blank"}. That is, you essentially pretend you have dichotomous preferences by treating all candidates you deem "acceptable" as equally good, and all candidates you deem "unacceptable" as equally bad. This is an obviously very strong assumption about voter preferences, but it is a framing that any voter can choose to adopt.

## References

- W.D. Wallis, *The Mathematics of Elections and Voting* (2018). [https://link.springer.com/book/10.1007/978-3-319-09810-4](https://link.springer.com/book/10.1007/978-3-319-09810-4){:target="_blank"}
- Ashish Goel, *Lecture Notes on Gibbard-Satterthwaite* (2021). [https://web.stanford.edu/~ashishg/msande336/aut2021/handouts/lecture5_notes.pdf](https://web.stanford.edu/~ashishg/msande336/aut2021/handouts/lecture5_notes.pdf){:target="_blank"}
- Andrew C. Eggers, *A Simple Proof of the Gibbard-Satterthwaite Theorem* (2018). [https://andy.egge.rs/papers/Eggers_GibbardSatterthwaite.pdf](https://andy.egge.rs/papers/Eggers_GibbardSatterthwaite.pdf){:target="_blank"}
