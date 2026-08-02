---
layout: distill
title: Approval voting is the Only Condorcet-Consistent SCORE Method
date: 2026-01-25
description: A proof that Approval voting is the unique score aggregation voting method that always elects the Condorcet winner induced by the ballot data.
importance: 2
tags: voting
category: polisci
featured: false
related_posts: true
pretty_table: true
theorems: true
exclude_appendix_from_word_count: true
exclude_footnotes_from_word_count: true
exclude_proof_blocks_from_word_count: true
citation: true
bibliography: voting.bib
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
  - name: Score-Condorcet-Consistency
    subsections:
      - name: Approval Is SCC
      - name: Uniqueness of Approval Voting
  - name: On the Existence of Condorcet Cycles
  - name: STAR Is Not SCC
  - name: How Bad It Can Get
  - name: Caveats
  - name: Uniquely Strong Legitimacy
    subsections:
      - name: The Skill Issue Defense
---

## Introduction

{% proof EDIT (06/27/2026) %}
This post was extremely long and pedantic and I decided to significantly shorten it down to the essential arguments and proofs, removing much of the detailed exposition and examples that made it cumbersome to read. I have also corrected some claims that I previously made which were inaccurate or misleading. The post title and description have also been changed to be more precise and reflective of the streamlined content.
{% endproof %}

I am personally a stickler for legitimacy in a voting system. I do not like it when the results select one winner, but the results can be legitimately challenged by another candidate who has a strong claim to victory based on the preferences expressed by the voters. I believe this undermines trust in the system and its outcomes, but is a tall order and ask from a system.

If a system gives its selected winner an unassailable claim to victory, then I would describe it as "internally consistent". However, this is a very subjective notion. In this post, I focus on a particular nicety of "single-ballot nonranked voting systems"<d-cite key="bramsFishburn1978approval"></d-cite> which proves them to be uniquely Condorcet-consistent with their ballot data.

> **Definition:** A single-ballot nonranked voting system is a voting system where voters can cast one vote for some number of candidates. For example, **Choose-one** plurality voting, where each voter can cast one vote for one candidate, or **Approval voting**, where each voter can cast one vote for as many candidates as they approve of. But this can include systems where, say, voters could cast either exactly one, or exactly three votes.

In 1978, Brams and Fishburn published a seminal paper on Approval voting<d-cite key="bramsFishburn1978approval"></d-cite>, where they prove that Approval voting is the unique single-ballot nonranked voting system that is Condorcet-consistent on the Dichotomous domain. However, if we define Condorcet-consistency based purely on the ballot data, then this property extends to all single-ballot nonranked voting systems, not just Approval voting.<d-footnote>For example, in Choose-one voting, there is no possibility for a candidate to be preferred over another candidate (in the ballot data) without getting more votes than that other candidate.</d-footnote>

Approval voting is often called a "two-tiered SCORE method" because, like a cardinal voting system, it allows voters to express numerical values independently for all candidates (just within the range of 0 to 1, where 0 represents disapproval and 1 represents approval). We will show that no other SCORE method, with a range more expressive than a binary 0 or 1, can be Condorcet-consistent based on its ballot data.

## Score-Condorcet-Consistency

We define some important notions we will be using throughout the post.

> **Definition:** A SCORE voting system is a voting system where each voter can assign a numerical score to each candidate, and the candidate with the highest total score wins. We define a SCORE voting method via a subset of $[0,1]$ that includes $0$ and $1$, representing the possible scores that a voter can assign to a candidate.

For example, the typical 0-5 scoring system would be denoted as $$\{0,0.2,0.4,0.6,0.8,1\}$$. By normalizing to $[0,1]$, we make proofs involving all SCORE voting systems more uniform and comparable. Approval voting would be simply $$\{0,1\}$$, representing disapproval and approval respectively, and we can say that a non-Approval score system contains some $0<s<1$, representing a score that is neither disapproval nor approval.

> **Definition:** We define the following notational shorthands:
>
> - Let $T(X>Y)$ be the number of voters who give candidate $X$ a strictly higher score than candidate $Y$. This is the number of voters who prefer $X$ over $Y$ based on their provided ballot data.
> - Let $S(X)$ be the total score given to candidate $X$ by all voters.
>
> Then, we say a SCORE voting system is **Score-Condorcet-Consistent** (SCC) if, whenever $T(X>Y) > T(Y>X)$, then $S(X) > S(Y)$. That is, if more voters give $X$ a higher score than $Y$ than vice versa, then the total score given to $X$ must be greater than the total score given to $Y$.

This is a pseudo-generalization of the Condorcet criterion of ordinal voting systems which states that if some candidate is preferred over every other candidate in head-to-head comparisons, then that candidate should be the winner.

In the context of SCORE voting, SCC is defined based on the ordinal preferences revealed when one voter scores one candidate above another. We wish that the pairwise dominance of a candidate be tied to their score<d-footnote>This is not the only way to generalize Condorcet-consistency. Methods like Smith // Score attempt to directly elect the Condorcet winner based on the ballot data.</d-footnote>. If candidate $X$ were to get a lower score than candidate $Y$ despite being preferred by more voters in head-to-head comparisons, that could be argued to be damaging to the legitimacy and perceived fairness of the election outcome.

### Approval Is SCC

> **Theorem:** Approval voting is Score-Condorcet-Consistent.

We will prove this via a surprising Lemma.

> **Lemma:** Every single-ballot nonranked voting system is Condorcet-consistent with its ballot data.\label{single-ballot-nonranked}

{% proof Click to expand proof %}
**Proof:** Observe that the only way for a voter to give $X$ a higher score than $Y$ in a single-ballot nonranked voting system is for the voter to vote for $X$ and not vote for $Y$. Let $T(X=Y)$ be the number of voters who vote for both $X$ and $Y$.

By abuse of notation, we can let $S(X)$ denote the total number of votes received by candidate $X$ in the single-ballot nonranked voting system. Then we can say that

$$\begin{equation}
S(X) = T(X>Y) + T(X=Y)
\end{equation}$$

It follows immediately that

$$\begin{equation}
S(X) - S(Y) = T(X>Y) - T(Y>X)
\end{equation}$$

Hence, we have that $$S(X) > S(Y)$$ if and only if $$T(X>Y) > T(Y>X)$$. We can therefore conclude that to get a higher number of votes than another candidate in a single-ballot nonranked voting system is to be preferred pairwise in a direct comparison according to the ballot data. Thus, every single-ballot nonranked voting system is Condorcet-consistent with its ballot data.
{% endproof %}

The Theorem for Approval voting follows directly from the Lemma, since Approval voting is both a single-ballot nonranked voting system and a SCORE voting method.

> **Corollary:** There can be no Condorcet cycles induced by the ballots in Approval voting.

**Proof:** Since Approval voting is SCC, if $$T(A>B) > T(B>A)$$, and $$T(B>C) > T(C>B)$$, then we have that $$S(A) > S(B)$$ and $$S(B) > S(C)$$, implying that $$S(A) > S(C)$$, and thus $$T(A>C) > T(C>A)$$. Therefore, there can be no cycles of the form $$A>B>C>A$$. **QED**

### Uniqueness of Approval Voting

The binary nature of votes and revealed preferences in single-ballot nonranked voting systems, such as Approval voting, lets the SCC property hold in a straightforward manner. We will show that adding any "in-between" scores, i.e., fractional approvals, disrupts this property.

> **Theorem:** The only SCORE voting system that is Score-Condorcet-Consistent is Approval voting. That is, if there exists a score $s$ with $$0 < s < 1$$ that voters can give to candidates, then candidates $X$ and $Y$ can be constructed such that $X$ beats $Y$ in head-to-head match-ups, but $Y$ has a higher total score than $X$.

{% proof Click to expand proof %}
**Proof:** Suppose that we have a non-Approval SCORE voting system. That is, there is some possible score $s$ with $$0 < s < 1$$ that a voter can give to a candidate.

Let $$t=\text{ceil}\left(\frac1s\right)$$. Note that this means that $$st=\text{ceil}\left(\frac1s\right)s\geq 1$$.

It suffices to show one counterexample where more voters prefer candidate A over candidate B, but B has a higher total score than A. Consider the following profile of voters:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| $$t+1$$          | 1           | $$s$$       | A > B      |
| $$t$$            | 0           | 1           | B > A      |

It is clear that more voters prefer A over B, since $$T(A>B)=t+1$$ and $$T(B>A)=t$$. However, the total scores are as follows:

$$
S(A) = t\cdot0 + (t+1)\cdot1 = t+1
$$

$$\begin{multline*}
S(B) = t\cdot1 + (t+1)\cdot s \\
= t + (t+1)s=t + ts + s
\end{multline*}$$

However, since $$ts\geq 1$$, we have that $$S(B)\geq t+1+s > S(A)$$. Thus, B has a higher total score than A, despite more voters preferring A over B. This violates the SCC condition, so any non-Approval voting system is not SCC. **QED**
{% endproof %}

The key insight is that by allowing fractional approvals (anything between the minimum and maximum score), we can create situations where a minority-preferred candidate snakes ahead in total score by accumulating many small fractional approvals from voters who prefer the other candidate. This is impossible in Approval voting, where each voter can only give a full approval or disapproval.

{% proof A 0-5 Example %}
**Example:** Consider the general SCORE system where voters can rate a candidate 0-5. But let's just focus on 0, 1, and 5. We can normalize this to scores 0, 0.2, and 1, giving us $$s=0.2$$.

We focus on the points of the two frontrunner candidates, A and B. Let us assume that there is an unpopular third candidate C, that both A and B voters dislike strongly, and that is why they give B a nonzero score. In a two candidate race, there is no rational reason for A voters to give B any score other than 0. Using the construction from the proof above, we have the following profile when we un-normalize:

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| 6 | 5 | 1 | A > B |
| 5 | 0 | 5 | B > A |

We still have more voters preferring A over B (6 to 5), but the total scores are:

| Candidate | Total Score |
|-----------|-------------|
| A | $$6\cdot5 + 5\cdot0 = 30$$ |
| B | $$6\cdot1 + 5\cdot5 = 31$$ |

Thus, B has a higher total score than A, despite more voters preferring A over B. This violates the SCC condition, so this non-Approval voting system is not SCC.
{% endproof %}

{% proof A more absurd example %}
**Example:** Consider a system where voters can give scores 0, 1, or 100. We can normalize this to scores 0, 0.01, and 1, giving us $$s=0.01$$. Then, we have $$t=\text{ceil}(100)=100$$. This gives the profile

| Number of Voters | Score for A | Score for B | Preference |
|------------------|-------------|-------------|------------|
| 101              | 100         | 1           | A > B      |
| 100              | 0           | 100         | B > A      |

We still have more voters preferring A over B (101 to 100), but the total scores are:

| Candidate | Total Score                            |
|-----------|----------------------------------------|
| A         | $$100\cdot 0 + 101\cdot 100 = 10,100$$ |
| B         | $$100\cdot 100 + 101\cdot 1 = 10,101$$ |

Once again B wins by one point despite a majority preferring A.
{% endproof %}

## On the Existence of Condorcet Cycles

> **Theorem:** Every non-Approval cardinal voting system can produce a Condorcet cycle induced by the ballots.

{% proof Click to expand proof %}
**Proof:** As per the above construction, suppose voters can give a score $s$ with $$0 < s < 1$$. Then, consider three candidates $A$, $B$, and $C$, and the following profile of voters:

| Number of Voters | Score for $A$ | Score for $B$ | Score for $C$ | Preference |
|------------------|-------------|-------------|-------------|------------|
| 1 | 1 | s | 0 | $A > B > C$ |
| 1 | 0 | 1 | s | $B > C > A$ |
| 1 | s | 0 | 1 | $C > A > B$ |

In this profile, we have that:

| Match-up | Winner | Vote Count |
|---------|--------|------------|
| $A$ vs $B$ | $A$ | 2 to 1 |
| $B$ vs $C$ | $B$ | 2 to 1 |
| $C$ vs $A$ | $C$ | 2 to 1 |

Thus, we have a Condorcet cycle $A > B > C > A$ induced by the ballots. **QED**
{% endproof %}

This is quite straightforward: by allowing just a third level of preference intensity, we can create a rock-paper-scissors style cycle among three candidates. By contrast, SCC guarantees a transitive pairwise ordering because the pairwise matchups are directly tied to the numerical scores. The transitive order of the real numbers ensures a transitive ordering of the candidates based on their pairwise scores, preventing cycles.

## STAR Is Not SCC

STAR voting is a popular cardinal-esque voting system that seems to attempt to fix this issue with score methods, by injecting in some majority rule. It is a 0 to 5 score system, where the winner is chosen by adding an additional runoff step: take the top two candidates by total score and then choose the winner by majority runoff between them (based on voters who gave them different scores). This protects it from some particularly damning examples, but it does not fix the underlying problem.

Since STAR voting is a 0 to 5 score system, by the above theorem, it is not SCC in the score aggregation step. However, we can show that the runoff still does not guarantee that the Condorcet winner induced by the ballots will win.

**Example:** Take this particular example with three candidates $A$, $B$, and $C$, and 11 voters:

| Number of Voters | Score for $A$ | Score for $B$ | Score for $C$ | Ranking   |
|------------------|-------------|-------------|-------------|-----------|
| 5                | 1           | 0           | 5           | $C > A > B$ |
| 4                | 1           | 5           | 0           | $B > A > C$ |
| 2                | 5           | 1           | 0           | $A > B > C$ |

If we look at the head-to-head match-ups:

| Match-up | Winner | Vote Count |
|----------|--------|------------|
| $A$ vs $B$ | $A$ | 7 to 4 |
| $A$ vs $C$ | $A$ | 6 to 5 |
| $B$ vs $C$ | $B$ | 6 to 5 |

Therefore, $A$ is the Condorcet winner and $C$ is the Condorcet loser.

When we add up the scores, however, something odd happens:

| Candidate | Total Score |
|-----------|-------------|
| $A$         | $$5\cdot1 + 4\cdot1 + 2\cdot5 = 19$$ |
| $B$         | $$5\cdot0 + 4\cdot5 + 2\cdot1 = 22$$ |
| $C$         | $$5\cdot5 + 4\cdot0 + 2\cdot0 = 25$$ |

We get that the Condorcet loser $C$ has the highest total score, while the Condorcet winner $A$ has the lowest total score. Thus, in a regular cardinal system, $C$ would be declared the winner, despite being the Condorcet loser induced by the ballots.

In STAR voting, however, we take the top two candidates by total score ($B$ and $C$) and have a runoff. In the runoff, $B$ beats $C$ by a vote of 6 to 5, so $B$ is declared the winner. While this prevents the Condorcet loser from ever winning, we still have two major problems:

1. The Condorcet winner $A$ still loses, despite having a legitimate claim to victory over both $B$ and $C$.
2. $C$ got the highest total score, but lost in the runoff. This gives them a legitimate claim to victory over $A$ and $B$, since they got the highest total score, despite fewer voters preferring them over the other two alternatives.

This could create a legitimacy-crisis where every candidate has a legitimate claim to victory. $A$ is the majority's favorite, $C$ got the highest total score, but $B$ won by the system's rules. This could create serious trust issues with the system, since it can't guarantee the winner a bulletproof claim to victory based on the preferences expressed by the voters.

## How Bad It Can Get

As it turns out, the closer the fractional score s is to 1, the worse the SCC violation can get. We can make the head-to-head win of $A$ over $B$ arbitrarily large, while $B$'s total score over $A$ is still greater.

**Example:** Let $s=0.9999$. Similar to the above proof, let us assume we have some nonviable third candidate $C$ that both $A$ and $B$ voters dislike strongly, and that is why $A$ voters give $B$ a nonzero score.

Consider the following profile (after un-normalizing):

| Number of Voters | Score for $A$ | Score for $B$ | Preference |
|------------------|-------------|-------------|------------|
| 9,999            | 10,000      | 9,999       | $A > B$      |
| 1                | 0           | 10,000      | $B > A$      |

Here, $A$ beats $B$ by 9,999 to 1 (99.99% of voters prefer $A$ over $B$), but $B$ has a higher total score:

| Candidate | Total Score                                     |
|-----------|-------------------------------------------------|
| A         | $$1\cdot0 + 9,999\cdot10,000 = 99,990,000$$     |
| B         | $$1\cdot10,000 + 9,999\cdot9,999 = 99,990,001$$ |

giving B a higher total score than A by 1 point, despite nearly all voters preferring A over B. The greater the granularity of the scoring system (the closer $s$ is to 1), the worse majority rule can be violated.

The issue with these examples is not that a clear consensus choice like B, who was rated at least 99.99% of the maximum score by every voter, has no legitimate claim to victory themselves. In fact, it seems very likely that, under Approval voting, all voters would approve of B. The problem that arises, however, is that the ballot data leaves evidence of an absurd violation of majority rule, that the losing candidate A could use to fuel distrust in the system.

> **Theorem:** For any rational number $$r\in(0.5,1)$$, there exists a SCORE system that allows a candidate $B$ to have a higher total score than candidate $A$, despite more voters giving $A$ a higher score than $B$ by a head-to-head ratio of $$r$$. That is, the head-to-head ratio of $A$ over $B$ in the ballot data can get arbitrarily close to 100% of voters declaring a preference for $A$ over $B$, while $B$ still has a higher total score than $A$.

{% proof Click to expand proof %}
**Proof:** Suppose we have a rational number $$r\in(0.5,1)$$, and let $$\frac{r}{1-r}=\frac{p}{q}$$ for some positive integers $p$ and $q$. Then, consider the following profile of voters:

| Number of Voters | Score for $A$ | Score for $B$ | Preference |
|------------------|-------------|-------------|------------|
| $p$ | 1 | $$s$$ | $A > B$ |
| $q$ | 0 | 1 | $B > A$ |

Note that $$f(x)=\frac{x}{1-x}$$ is a continuous increasing function on $(0,1)$. Since $$f(0.5)=1$$, we have that for any $$r\in(0.5,1)$$, we have that $$f(r)$$ is a rational number greater than 1. Therefore, if $$\frac{r}{1-r}=\frac{p}{q}$$, then $$p>q>0$$. This guarantees that $$T(A>B)=p$$ and $$T(B>A)=q$$ are positive integers with $$p>q$$, so more voters prefer A over B.

The precise head-to-head ratio for A over B, further, is

$$\begin{align*}
\frac{T(A>B)}{T(A>B)+T(B>A)} &= \frac{p}{p+q} \\
&= \frac{p/q}{1+p/q} \\
&= \frac{\frac{r}{1-r}}{1+\frac{r}{1-r}} \\
&= \frac{r}{(1-r) + r} \\
&= r
\end{align*}$$

This gives us the desired head-to-head win of size r for A over B.

We now show that B has a higher total score than A whenever $$2-\frac1r < s < 1$$. That is, we want to show that $$S(A)=p<q +ps=S(B)$$.

We prove this using a chain of equivalent inequalities:

$$\begin{align*}
s > 2-\frac1r & \iff rs>2r-1  \\
&\iff 1 - r + rs > r \\
&\iff 1 + \frac{rs}{1-r} > \frac{r}{1-r} \\
&\iff 1 + \frac{sp}{q} > \frac{p}{q} \\
&\iff q + sp > p\\
&\iff S(B) > S(A)
\end{align*}$$

Therefore, $B$ has a higher total score than $A$ and more voters prefer $A$ over $B$, completing the proof. **QED**
{% endproof %}

In general, to achieve a head-to-head win of size $$r=\frac{T(A>B)}{T(A>B)+T(B>A)}\in(0.5,1)$$ (where $r$ is rational), while having B get a higher total score than A, we need:

$$
2-\frac{1}{r} < s < 1
$$

If $$\frac{r}{1-r}=\frac{p}{q}$$ then the following profile will do the trick:

| Number of Voters | Score for $A$ | Score for $B$ | Preference |
|------------------|-------------|-------------|------------|
| $p$ | 1 | $$s$$ | $A > B$ |
| $q$ | 0 | 1 | $B > A$ |

One might ask the maximum head-to-head win size r achievable for a given score s. Rearranging the above inequality, we have that:

$$
r < \frac{1}{2 - s}
$$

Which gives us one upper bound on the head-to-head win size achievable for a given score $s$, in this structure of profile. As $s$ approaches 1, this upper bound approaches 1 as well, allowing for arbitrarily large head-to-head wins.

## Caveats

There are [systems](https://electowiki.org/wiki/Smith//Score) that attempt to make cardinal systems Condorcet-consistent by electing Condorcet winners when they exist based on the ballot data, or eliminating candidates outside the Smith set (which we will not get into here). In [this post](../condorcet-approval/) I define them as "Generalized Condorcet Methods". However, they are not SCC, as the above proof shows that no non-Approval SCORE system can be. That is, they cannot encode the head-to-head preferences of voters into the scores.

One can rightly argue this property is absurdly restrictive, and a ridiculous constraint to stubbornly impose on a voting system, limiting its flexibility and the ways in which it can aggregate voter preferences.

Rather, I would argue that instead of being a "necessary" property, it is instead just a positive of Approval voting. There are a number of reformers who find it abhorrent to elect a candidate $B$ when more voters rank $A$ over $B$ on their ballot than the reverse. As it turns out, you can only achieve this with a single-ballot nonranked voting system, like Choose-one or Approval.

In other words, more [expressivity restricts the amount of legitimacy you can guarantee to your voting system](../approval-only/). The fact that Approval's empirical outcomes in simulations are so close to that of more expressive systems like SCORE, STAR, or Condorcet<d-cite key="quinn2017vseSummary"></d-cite>, in my view, implies that expressiveness is not what makes a voting system good.

For most SCORE systems (i.e. not STAR voting), there is no need for the system to report the head-to-head preferences of voters. Instead, precincts might report only the numerical scores, and it might be difficult to get ahold of the preference data which might show the winner to not be the Condorcet winner, if such a discrepancy exists.

Given Approval's simplicity, logistical ease of implementation, the bulletproof legitimacy it yields the winner, and strong performance in electing representative candidates, the burden of proof lies on the more complex systems to show that their added complexity, and loss of internal consistency, is worth the trade-off. So far, I have not seen convincing evidence that it is. In the words of [Regenwetter and Grofman](http://www.jstor.org/stable/2634612)

> "We find no evidence here that approval voting should be replaced by a more elaborate voting scheme." (p. 532)<d-cite key="regenwetterGrofman1998approvalBordaCondorcet"></d-cite>

## Uniquely Strong Legitimacy

I would like to briefly note that, of the systems commonly being proposed right now, I have concerns about the legitimacy of their ballot data.

We have already discussed STAR in-depth, which can fail to elect both the Condorcet winner *and* the highest scoring candidate simultaneously.
In past posts, I've discussed [RCV](../ditch-rcv/)'s real-life failures in Burlington, Alaska, and Oakland. Further, we have touched on the notion of a Condorcet cycle. In any cyclic election, some candidate can point to the ballot data and rightly claim they were preferred by a pairwise majority over the actual winner.

In Lemma \ref{single-ballot-nonranked}, we established that every single-ballot nonranked voting system is Condorcet-consistent with its ballot data, including Choose-one voting. But I think it's quite apparent that our Choose-one system is not exactly the holy grail of legitimacy. Cases like the 2000 US Presidential election had spoiler candidates who almost surely changed the outcome. So while there are no Condorcet-failures in Choose-one, there's still the issue that we can infer that had the restriction of one vote been lifted--with voters freed to express their preferences more fully--the result could have changed.

### The Skill Issue Defense

Even though other non-Approval single-ballot nonranked voting systems like Choose-one voting also have the ballot-level Condorcet-consistency, Approval has other aspects that make its outcomes more legitimate and unassailable.

There is no spoiler effect. No Condorcet cycles. No case where the winner didn't get the most first-choice votes or five-star ratings. The winner always has the highest total approvals, so no other candidate can have a legitimate claim to victory. If Alice wins with 600 approvals, and Bob has 550 approvals, then Bob can't convincingly claim that he was somehow robbed of victory.

There's no ranked data to pour through, to see if maybe those who approved both or neither actually preferred Bob to Alice. The 100 votes a third candidate Clark got weren't votes that "could have gone to Bob *instead*", as could be claimed under Choose-one voting. Exactly 50 more voters approved Alice-and-not-Bob than Bob-and-not-Alice. 50 more voters had the choice to approve Bob alongside Alice. They had the pen in their hand, looked at the box, and they chose not to. Alice can rightly say, "Skill issue, Bob. Try being more acceptable next time."

## Conclusion

Perhaps I'm just a worrywart. But I think minimizing opportunities for bad actors to rile up voters and convince them that the system elected the wrong candidate, and their favorite candidate had the election stolen from them, is crucial. Because despite the legitimacy guarantees proven for Choose-one voting here, we still had Stop the Steal in 2020, and doubts of Trump's victory in 2024. Thus, I think there are great arguments that the SCC property, and Condorcet-consistency in general, is overrated. But I'm concerned about transitioning to a system with *less* legitimacy rather than *more*.<d-footnote>In fairness, there is opportunity that bad actors would claim that the election was stolen by adding bubbles after voters have cast their ballot. Changing the ballot to Yes/No could mitigate this concern.</d-footnote>

That said, in an age where trust in our institutions and elections are at an all-time low, having a voting system that can provide such a guarantee is invaluable, in my view. Approval voting is not just mathematically elegant, it's not just [the most practical and cost-effective solution for our electoral problems](../practicalapproval/), it is the only voting reform (cardinal or otherwise) in conversation that can guarantee an unassailable claim to victory for its winners in *all* non-tied elections.
