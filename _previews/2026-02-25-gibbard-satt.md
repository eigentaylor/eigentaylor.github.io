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
---

## Introduction

Based primarily on the proof include in W.D. Wallis' [*The Mathematics of Elections and Voting*](https://link.springer.com/book/10.1007/978-3-319-09810-4){:target="_blank"}, with more detail. I also referenced [these lecture notes](https://web.stanford.edu/~ashishg/msande336/aut2021/handouts/lecture5_notes.pdf){:target="_blank"} from Ashish Goel's course at Stanford.

The Gibbard-Satterthwaite theorem is a fundamental result in social choice theory, which loosely states that "reasonable" voting system can be strategyproof. That is, there can always be a situation where a voter can get a better result by voting dishonestly. The exception is a "dictatorship", where the whole election is decided by a single voter, and all other ballots are ignored.

Similar to Arrow's impossibility theorem, the intuition is "If we have a voting system that has this nice property, then it must be a dictatorship". That is, seemingly obvious or desirable properties of a voting system are actually extremely difficult to satisfy when you must aggregate the preferences of multiple voters. The Gibbard-Satterthwaite theorem is focused on the inevitability of strategic voting in ranked voting systems.

## Definitions and Monotonicity

A social choice function is a function that takes in a profile of votes (a list of voters' rankings of candidates) and outputs a single winner. We will be working with ranked voting systems, where voters must strictly rank candidates without ties.

Suppose that $$f$$ is a social choice function which is Pareto efficient (if every voter ranks $$A>B$$ then $$f$$ ranks $$A>B$$), unanimous (if every voter ranks $$A$$ first, then $$A$$ wins), and strategyproof (if we move from a profile $$P_1\to P_2$$ by changing the vote of a voter $v$ from their honest preference to a dishonest preference, then the winner of $$P_2$$ cannot be strictly preferred by $v$ to the winner of $$P_1$$).

The essential idea of the theorem is that strategyproofness is an extremely strict property only satisfied by a dictatorship.

**Definition 1:** We call $$f$$ *strategyproof* if the following is satisfied.

Suppose that in a given profile $$P_0$$ we have $$f(P_0)=A$$, and suppose in $$P_0$$ we have a voter $$v$$ with their honest ranking $$R_0$$. If we obtain $$P_1$$ from changing $$P_0$$ only by adjusting the vote of $$v$$ (to a dishonest ranking), then one of the following two cases must occur:

1. $$f(P_0)=f(P_1)=A$$. The winner is preserved.
2. If $$f(P_1)=B\neq A$$, then $$A>_{R_0}B$$ in $$v$$'s honest $$P_0$$ ranking.

More concisely, the winner in the honest case is at least weakly preferred to the winner in the dishonest case:

$$f(P_0)\geq_{R_0}f(P_1)$$

We give a more useful formulation via the contrapositive.

**Lemma 1:** Suppose we can move from one profile $$P_1\to P_2$$ via changing only a single voter $$v$$'s vote from $$R_1\to R_2$$ such that

- $$f(P_1)=A\neq f(P_2)=B$$: The winner changes from $$A\to B$$.
- $$v$$ originally ranked $$B>_{R_1}A$$

then $f$ is not strategyproof.

Intuitively, if I change my vote, then the winner can't change to something I like better. Otherwise, I have a beneficial strategy, and the system is not strategyproof.

**Lemma 2:** If $$f$$ is strategyproof, then $$f$$ is monotonic. That is, if a voter moves a candidate $$X$$ strictly up in their ranking, keeping all else fixed, then either the winner is unchanged, or $$X$$ is the new winner.

**Proof:** Take a profile $$P_1$$ and suppose that $$f(P_1)=A$$. Consider a voter $$v$$ with honest ranking $$R_1$$. Suppose that $$v$$ moves $$X$$ strictly up in their ranking to get ranking $$R_2$$ that induces profile $$P_2$$, and suppose that $$f(P_2)=B$$. If $$A=B$$, then there is nothing to show. So we will show that if $$A\neq B$$, then $$B=X$$.

First, let's suppose that $$X$$ is distinct from both $$A$$ and $$B$$. Then, we know the relative ranking of $$A$$ and $$B$$ is unchanged, so we have two cases:

- If $$v$$ prefers $$B$$ to $$A$$ (ranks $$B>_{R_1}A$$ and $$B>_{R_2}A$$), then this would be a beneficial strategy, contradicting strategyproofness.
- If $$v$$ prefers $$A$$ to $$B$$ (ranks $$A>_{R_1}B$$ and $$A>_{R_2}B$$), then $$v$$ would have a beneficial strategy moving from $$P_2$$ to $$P_1$$, also contradicting strategyproofness.

Thus, we cannot have $$X$$ be distinct from both $$A$$ and $$B$$. Therefore, $$B\in\{A,X\}$$. That is, moving $$X$$ up can only either preserve the winner or make $$X$$ the new winner. So $$f$$ is monotonic. QED.

## Blocking Sets

**Definition 2:** We say that a set of voters "$$S$$ can block candidate $$B$$ with candidate $$A$$", denoted $$A>_SB$$, if whenever every voter in $$S$$ ranks $$A>B$$, then $$B$$ does not win.

For example, if $$S$$ is the set of all voters and every voter ranks $$A>B$$, then $$f$$ will prefer $$A>B$$. As another example, though it technically does not fall under the purview of our assumptions (but may benefit for intuition), under plurality voting, a strict majority (ex. 51 Senators out of 100) can block a bill by voting no.

The idea we are building up to is that under the strategyproof assumption, any blocking set must contain a dictator.

**Remark 1:**

- An empty set cannot block. That is, if $$S=\varnothing$$, then we cannot have $$A>_\varnothing B$$.
- The set of all voters is a blocking set.

**Lemma 3:** If $B$ loses for all profiles where

1. All voters in $S$ rank $A>B$
2. All voters outside of $S$ rank $B$ first

then $$A>_SB$$. \label{weakblock}

**Proof:** Suppose the contents of the lemma. Suppose for contradiction that we have a profile $$P$$ where $$S$$ ranks $$A>B$$ but $$B$$ wins. Then, by monotonicity, if every voter outside of $$S$$ moves $$B$$ to the top, then $$B$$ must still win. This contradicts the contents of the lemma.
\end{proof}

Again, since we aim to eventually show that $$S$$ contains a dictator, if every voter outside of $$S$$ ranks $$B$$ first, then that is almost the best possible case for $$B$$. The fact that $$B$$ is first outside of $$S$$ is crucial. For example, if $$S$$ didn't contain a dictator, but the complement of $$S$$ did, then if the dictator (outside of $$S$$) ranks, say, $$C>B>A$$, then $$B$$ will still lose. Thus, we would not have sufficiently shown that $$S$$ can \textit{always} block $$B$$ using $$A$$.

The following lemma characterizes the actual best possible case for $$B$$. If satisfied, then we will be able to conclude that lemma 3 is true.

**Lemma 4:** (The Blocking Criterion) If there exists a single profile $$P$$ where

1. Every voter in $$S$$ ranks $$A$$ first and $$B$$ second
2. Every voter outside of $$S$$ ranks $$B$$ first
3. $$B$$ loses

then $$A>_SB$$. \label{blockcriterion}

**Proof:** We aim to show that if $$P$$ exist then it implies that Lemma 4 must be true.

Take any profile $$P'$$ satisfying Lemma 3 \ref{weakblock}. That is, in $$P'$$ we have that $$S$$ ranks $$A>B$$ and every voter outside of $$S$$ ranks $$B$$ first. We will show that moving from $$P$$ to $$P'$$ must maintain $$B$$'s loss.

Since $$B$$ loses, then by monotonicity we can have all voters in $$S$$ move $$B$$ down to its place in $$P'$$, and $$B$$ will still lose.

We now rearrange the profile to get to  $$P'$$. Take the candidate right above $$B$$'s new place in the ranking of $$S$$, and move it to the top (which moves $$A$$ down to second place in the ranking of voters in $$S$$). By monotonicity, either that new candidate wins, or the previous non $$B$$ candidate wins (either way, $$B$$ still loses). Repeat until $$A$$ is in its place in $$P'$$, and $$B$$ will still lose. Thus, Lemma 3 \ref{weakblock} is satisfied. QED.

The intuitive idea of this lemma is that profile in Lemma 4 is the absolute best case for $$B$$ while still satisfying that $$S$$ ranks $$A>B$$.

**Lemma 5:** If $$A>_SB$$ and $$S=M\sqcup N$$ is a partition of $$S$$, and $$S'$$ is the complement of $$S$$, then either

- $$A>_MC$$
- $$C>_NB$$ \label{partitionblock}

**Proof:** Suppose that we have a profile $P_0$ where the reported rankings are

- $$M:A>B>C$$
- $$N:C>B>A$$
- $$S':B>C>A$$

with all other candidates ranked below $$A,B,C$$. By Pareto efficiency, the only possible winners are $$A,B,C$$.

By the assumption that $$A>_SB$$, since all voters in $$M\sqcup N=S$$ rank $$A>B$$, then $$B$$ must lose. We aim to construct profiles satisfying Lemma 4 \ref{blockcriterion} where $$B$$ must still lose.

Since $$B$$ loses, we must have either $$A$$ win or $$C$$ win.

1. If $$C$$ wins, then suppose that $$M$$ moves $$B$$ above $$A$$: $$M:B>C>A$$, matching $$S'$$. By monotonicity, since we moved $$B$$ up, then either $$C$$ still wins or $$B$$ now wins. If voters in $$M$$ truly prefer $$A>B>C$$, then by strategyproofness the winner cannot be $$B$$ or else this would be a beneficial strategy. Thus, $$C$$ still wins. This create a profile

    - $$M:B>C>A$$
    - $$N:C>B>A$$
    - $$S':B>C>A$$

where $$B$$ loses, every voter in $$N$$ ranks $$C$$ first and $$B$$ second, and every voter not in $$N$$ ranks $$B$$ first. By Lemma 4 \ref{blockcriterion}, we must have that $$C>_NB$$

1. Suppose instead that $$A$$ wins. Similarly, we can have $$S'$$ move $$C$$ above $$B$$: $$S':C>B>A$$. By monotonicity, either $$C$$ wins or $$A$$ wins. As before, if voters in $$S'$$ truly preferred $$B>C>A$$, then $$C$$ winning would make this a beneficial strategy. Thus, $$A$$ must still win.

Suppose now that voters in $$M$$ raise $$C$$ above $$B$$: $$M:A>C>B$$. By monotonicity, we still must have that $$C$$ wins or $$A$$ wins. Suppose that $$C$$ now wins. Then, if $$M$$ voters truly preferred $$A>B>C$$, then moving backwards (moving $$C$$ below $$B$$) would make $$A$$ win and be a beneficial strategy. Contradiction. Thus, $$A$$ must still win after moving $$C$$ to second place. This create a profile

- $$M:A>C>B$$
- $$N:C>B>A$$
- $$S':C>B>A$$

and $$C$$ loses, satisfying Lemma \ref{blockcriterion} so we can conclude that $$A>_MC$$. QED.

**Lemma 6:** If $$A>_SB$$ and $$C$$ is any other candidate, then $$A>_SC$$ or $$C>_SB$$. \label{thirdblock}

That is, if $$A>_SB$$, then $$S$$ can block any third candidate $$C$$ with $$A$$, and $$S$$ can block $$B$$ with any third candidate $$C$$.

**Proof:** Using Lemma 5 \ref{partitionblock}:

- Suppose we take $$M=\varnothing$$, and thus $$N=S$$. Then we cannot have $$A>_MC$$ since an empty set cannot block. Thus, $$C>_SB$$.
- Similarly, if $$N=\varnothing$$ and $$M=S$$, then we must have $$A>_SC$$.

QED.

**Lemma 7:** If $$A>_SB$$, then $$B>_SA$$. \label{flipblock}

**Proof:** By Lemma 6 \ref{thirdblock},

$$A>_SB\implies A>_SC$$

By the same lemma, taking $B$ as the third candidate

$$A>_SC\implies B>_SC$$

And, again, taking $A$ as the third candidate now,

$$B>_SC\implies B>_SA$$

QED.

At this point, we have essentially shown that the ability to block a single candidate with another actually implies far more power. In fact, it can block any candidate with any other. In that sense, $$S$$ can make all candidates lose. Therefore, if $$S$$ ranks a candidate $$A$$ over all others, then all other candidates must lose, and so $$A$$ wins. That is, $$S$$ exactly chooses the result of the election, making it a sort of collection of voters who together act as a dictator.

However, lemma 6 \ref{partitionblock} will land the crushing blow: any partition of a blocking set contains a blocking set. Perhaps the reader can see where this is going!

## Dictating Sets

**Definition 3:** We call $$S$$ a *dictating set* if $$A>_SB$$ for any pair of candidates $$A,B$$. That is, if $$S$$ can block any candidate from winning using any other.

**Remark 2:** The set of all electors is a dictating set, and a dictating set with a single voter must have that voter as a dictator.

**Lemma 8:** If $$A>_SB$$ for any two candidates, then $$S$$ is a dictating set.

**Proof:** We must show that given $$A>_SB$$, then $$C>_SD$$ for any other pair of candidates.

By lemma \ref{thirdblock}, if $$A>_SB$$, then $$S$$ can use $$A$$ to block any third candidate. Say, $$A>_SD$$.

Also by lemma \ref{thirdblock}, $$S$$ can block $$D$$ with any other candidate. Say, $$C>_SD$$.

Therefore, we have made the connection to blocking and dictatorship. The particular specification of which candidates $$S$$ can block with which are not mostly irrelevant. Being able to block once implies dictatorial power.

The final lemmas are as follows.

**Lemma 9:** If $$S$$ is a dictating set, and $$S=M\sqcup N$$ is any partition of $$S$$, then either $$M$$ is a dictating set or $$N$$ is a dictating set. \label{dictatepartition}

**Proof:** Suppose $$S$$ is a dictating set and $$S=M\sqcup N$$ is a partition.  Then $$A>_SB$$ for any two candidates $$A,B$$. By lemma \ref{partitionblock}, we must have

- $$A>_MC \iff M$$ is a dictating set
- $$C>_N B \iff N$$ is a dictating set.

Thus, at least one must be a dictating set.

**Lemma 10:** If $$S$$ is a dictating set, then it contains a dictator. \label{dictator}

**Proof:** Let $$S=\bdef{v_1,\ldots,v_n}$$ be a dictating set.

Take the partition $$S=\bdef{v_1}\sqcup S_{1}$$ (where $$S_1=S\setminus\left\{v_1\right\}$$). Then by lemma 9 \ref{dictatepartition}, either $$\{v_1\}$$ or $$S_1$$ is a dictating set with a strictly lower cardinality. If $$\{v_1\}$$ is a dictating set, $$v_1$$ is a dictator and we are done. Otherwise, let

$$S_i\defeq S_{i-1}\setminus\{v_i\}$$

Then, eventually we will reach $$S_{n-1}=\{v_{n-1}\}\sqcup \{v_n\}$$. If no $$v_i$$ was a dictator for $$i<n-1$$, then one of $$\{v_{n-1}\}, \{v_n\}$$ must be a dictating set, in which case $$v_{n-1}$$ or $$v_n$$ is a dictator. Therefore $$S$$ must contain a dictator. QED.

Therefore, we can equate the existence of a blocking set with that of a dictating set and therefore with that of a dictator.

We can finally prove the theorem.

## The Gibbard-Satterthwaite Theorem

**Theorem 1 (Gibbard-Satterthwaite):** Suppose that we have a ranked voting system, where voters must strictly rank candidates without ties, which is unanimous, Pareto efficient, and strategyproof. Then it must be a dictatorship.

**Proof:** We will show that there must exist a dictating set, and thus by lemma 10 \ref{dictator} there must be a dictator.

Trivially, we can see that a dictatorship does indeed satisfy all three requirements.

By Pareto efficiency, the set of all voters $S$ is a dictating set. By lemma \ref{dictator}, $S$ contains a dictator. QED.

## Conclusion

The proof comes down to a few essential elements:

1. Strategyproofness is an \textit{extremely} strict property.
2. Strategyproofness implies monotonicity.
3. Pareto efficiency implies the trivial existence of a blocking set.
4. Less trivially, any blocking set contains a strictly smaller blocking set. This relies heavily on the strategyproofness.
5. A blocking set doesn't just block a single candidate, but can block all candidates, making it dictatorial.
6. Since we can reduce any dictating (blocking) set into a strictly smaller dictating set, we can show the existence of a single dictator.

While most lemmas follow relatively straightforwardly from the intuitive idea of a blocking set, the real key to the proof is that any blocking set contains a strictly smaller blocking set. This heavily relied on the fact that strategyproofness is so strict.
