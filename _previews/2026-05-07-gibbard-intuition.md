---
layout: distill
title: The Intuition Behind Gibbard's Theorem
date: 2026-05-07
description: An intuitive breakdown of Gibbard's more general 1973 theorem on the manipulation of voting schemes.
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

I made a post a few months ago about a proof of the [Gibbard-Satterthwaite theorem](../gibbard-satt){:target="_blank"}, which shows that deterministic ranked voting systems, where voters cannot express indifference, are manipulable. However, [Gibbard's original 1973 paper](https://www.jstor.org/stable/1914083) actually proves something *much* more general.

I will say, I highly recommend giving the paper a read yourself. The first half of the paper is a very intuitive and accessible breakdown of the intuition behind the proof, and the second half is the formal proof itself. The paper is only 15 pages long, and I had a great time reading it.

I think the fact that people are content to prove just the corollary, the Gibbard-Satterthwaite theorem, rather than the more general result, is a real shame. Especially when systems like STAR and Approval voting, which do not fit neatly into the Gibbard-Satterthwaite framework, are becoming more popular.

It's no secret that I am a [huge fan of Approval voting](../approval-only){:target="_blank"}, and I love to mention that (under certain strict conditions) [Approval voting is strategyproof](https://doi.org/10.2307/1955105). But the *way* that Gibbard proves that more general systems are manipulable is absolutely fascinating, and I'd like to give my attempt to break down the precise mechanism that Gibbard uses.

This won't be a formal proof, as my post on the Gibbard-Satterthwaite theorem did, and I might write a post in the future that goes deeper into the formal proof. But I think it's a bit more enlightening to just talk through the intuition of the definitions and steps of the proof, rather than the exact details. I think the *way* that Gibbard proves his theorem is perhaps more interesting than the proof itself!

## The Starting Point

In an age of quality production videos and resources explaining how [Arrow's theorem](../arrows){:target="_blank"} makes [democracy "mathematically impossible:"](https://www.youtube.com/watch?v=qf7ws2DF-zk), and breaking down strategy in voting systems in a [fun and intuitive way](https://youtu.be/rbVoEjS6Q1Q?si=BqaGjgs62WumgMA7), it's easy to forget that *axiomatic* social choice theory is a relatively young field. That is, in the sense that many of these theorems were proved in the 50's and 70's, despite democracy being thousands of years old, and many voting systems that are still talked about frequently being invented in the 1700's.

Many of the things we take for granted now, such as the *obvious* general susceptibility of voting systems to strategy were mere conjectures before Gibbard proved his theorem. People could come up with examples of scenarios where voters could manipulate the result of voting systems, and there was a *sense* that this was just a fact of the nature of voting, but nobody had proved it formally.

> "It seems unlikely that there is any voting procedure in which it can never be advantageous for any voter to vote 'strategically,' i.e., non-sincerely"
> -- Dummett and Farquharson (1961)

There were proofs for specific types of systems, but the level of abstraction that Gibbard used was unprecedented.

**Example:** Consider the example given in Gibbard's paper in the Borda count.

| Voter   | True Preference | Borda Ballot |
|---------|-----------------|--------------|
| Voter 1 | $a>b>c>d$       | $a>b>c>d$    |
| Voter 2 | $d>a>b>c$       | $d>a>b>c$    |
| Voter 3 | $d>a>b>c$       | $d>b>c>a$    |

In the Borda count, we can say that the last ranked candidate gets 0 points, the second to last gets 1 point, the second to first gets 2 points, and the first ranked candidate gets 3 points. In this example, the Borda count would give us:

| Candidate | Borda Score (Honest Ballots) | Borda Score (Actual) |
|-----------|------------------------------|----------------------|
| $a$       | 7 (Winner)                   | 5                    |
| $b$       | 4                            | 5                    |
| $c$       | 1                            | 2                    |
| $d$       | 6                            | 6 (Winner)           |

Voter 3 thus has an incentive to vote strategically, by burying $a$ to the bottom of their ballot, they starve $a$ of points enough to make their favorite, $d$, the winner instead of $a$.

This exemplifies the way that I think of manipulability in a voting system. Voter 3 had a sincere preference order that said "$d$ is my favorite! I prefer $d$ over $a$," but they had to lie about how they felt about $a$ relative to $b$ and $c$ in order for that preference to actually be "respected". Which, when articulated that way, might remind you of [the Independent of Irrelevant Alternatives (IIA) criterion](../iia){:target="_blank"}, which is a key part of Arrow's theorem. And that is no coincidence! A major step of the proof is to show, loosely, that from strategyproofness we must have IIA.

This was also something conjectured before Gibbard's paper by Vickrey in 1960. Gibbard proved this conjecture correct by using Arrow's theorem to prove his own theorem.

**Example:** A more modern flavored STAR example can be seen below:

{% proof Click to expand proof %}
| Voter   | True Ranking | Honest STAR Ballot | Actual STAR Ballot |
|---------|--------------|--------------------|--------------------|
| Voter 1 | $a>b>c$      | $a=5, b=2, c=0$    | $a=5, b=0, c=2$    |
| Voter 2 | $c>b>a$      | $c=5, b=1, a=0$    | $c=5, b=1, a=0$    |
| Voter 3 | $b>a>c$      | $b=5, a=2, c=0$    | $b=5, a=2, c=0$    |

The honest scores would be:

| Candidate | STAR Score (Honest Ballots) | STAR Score (Actual)   |
|-----------|-----------------------------|-----------------------|
| $a$       | 7 (In Runoff, Loser)        | 7 (In Runoff, Winner) |
| $b$       | 8 (In Runoff, Winner)       | 6                     |
| $c$       | 5                           | 7  (In Runoff, Loser) |

Two voters prefer $b$ to $a$, so in the honest profile, $a$ and $b$ advance to the runoff, and $b$ wins. However, Voter 1 has an incentive to strategically bury $b$ and boost $c$, which causes $c$ to tie with $a$ for the most points, and thus $a$ and $c$ advance to the runoff. Two voters prefer $a$ to $c$, so $a$ wins the runoff, changing the winner from $b$ to $a$. Voter 1 thus has an incentive to lie about their preferences in order to get a more preferred outcome.
{% endproof %}

## Game Forms

Rather than focus in on a voting system, where voters submit their rankings of candidates, Gibbard focuses on a much more general idea of a "game".

Essentially, we have some set of players, and each player has a set of strategies. The players choose a strategy, and out pops an "outcome".

> **Definition:** A "game form" is a function $g$, that takes in strategies from each player, and outputs an outcome. Formally, if we have $n$ players, and the set of strategies for player $i$ is $S_i$, then the game form is a function $g: \times_{i=1}^n S_i \to X$, where $X$ is the set of outcomes.

This is incredibly general, so we might have a game of the following form:

- Player 1: Gets a ballot where they can select a single name from a list of candidates.
- Player 2: Gets a ballot where they can rank the candidates from best to worst, no ties allowed!
- Player 3: Gets a ballot where they can rank the candidates, but ties are totally fine.
- Player 4: Scores the candidates from 0 to 5.
- Player 5: Gets a ballot where they can approve of as many candidates as they like.
- Player 6: Grades each candidate with a letter grade from A+ to F.
- Player 7: Must write a 10 page essay about what they think of all the candidates, which must include the word "bodacious" at least 50 times.
- Player 8: Must plan an elaborate dance routine to express their feelings about the candidates.
- Player 9: Must write a heartfelt opera about the election, and perform it in front of the other voters.

This is the level of abstraction we're working at. This allows Gibbard to hit any voting system, even if it doesn't involve ranked ballots. Each player would have some set of strategies $S_i$. Player 7, for example, would have the set of all possible 10 page essays that include the word "bodacious" at least 50 times.

Each player selects a strategy for their "ballot", and from all of these strategies, we *somehow* decide on a winner. Don't ask me how! One entirely valid way could be to just elect whoever Player 1 votes for, and ignore literally everyone else. Is that fair? Well, not really. But it is an entirely valid game form, and it is also technically strategyproof. Nobody has any incentive to lie about their preferences, because only Player 1's ballot matters. This is an example of a dictatorship, which is strategyproof but not at all desirable.

However, the way I explained it is not quite accurate. Because there is no true rigorous sense of "preference" or "honesty" in this game. If Player 4 has a preference of Alice over Bob over Clark, then is it more honest to score Alice a 5, Bob a 4, and Clark a 3 than it is to score Alice a 5, Bob a 1, and Clark a 0? If Player 5 has the same preference, then surely they should approve of Alice and not Clark, but is it more honest to approve of Bob than it is to not approve of him? Does the Carlton mean you prefer a candidate more than one you did the Gangnam Style dance for?

We start with what we formally define a "voting system" to really mean.

> **Definition:** A "voting scheme" is a deterministic function $v$ that takes in a list of preferences for each player, and outputs a single outcome. Formally, if we have $n$ players, and the set of preferences for player $i$ is $P_i$, then $v$ is a deterministic function $v(P_1, P_2, ..., P_n) \to X$, where $X$ is the set of outcomes.

Notions of "honesty" and "sincerity" and "manipulation" are notions for a "voting scheme", and not a game form.

> **Definition:** A voting scheme is "strategyproof" if there is never a scenario where a player can change their stated preference $P_k$ to some other preference $P_k'$, such that the outcome is strictly preferred, according to $P_k$. If we denote $\vec{P} = (P_1,\ldots, P_k,\ldots, P_n)$ and $\vec{P}' = (P_1, P_2, \ldots, P_k', \ldots, P_n)$, then strategyproofness means that there is never a scenario where:
> $$v(\vec{P}) \succ_{P_k} v(\vec{P}')$$
> where $\succ_{P_k}$ means "is strictly preferred to according to $P_k$".

This happened in our Borda example, where Voter 3 had a preference of $d > a > b > c$ ($P_3$), but they had an incentive to change their stated preference to $d > b > c > a$ ($P_3'$) in order to get a more preferred outcome. The outcome of $P_3$ was $a$, and the outcome of $P_3'$ was $d$, and we have that

$$d \succ_{P_3} a$$

As I explained it before, the voter was *already* saying "I prefer $d$ to $a$," but they had to change their strategy in order to change the winner from $a$ to $d$. This is the essence of manipulability. See [this post](../iia){:target="_blank"} for more examples of this in existing voting systems like RCV and Condorcet.

Compared to preference lists $P_i$, strategies are far more abstract. Gibbard defines "strategyproofness" for a game form as "straightforwardness" as follows:

> **Definition:** A game form is "straightforward" (strategyproof) if for every possible preference $P_k$ a player might have, there is a best response for that preference that works regardless of what everyone else does. We denote $\sigma_k(P_k)$ as the strategy for player $k$ that is the best response for preference $P_k$, and $\sigma(P)$ as the list of best response strategies for all players given the list of preferences $P$.

For example, maybe for Approval, the best response for a preference of Alice > Bob > Clark is to approve of Alice and Bob, regardless of what everyone else does. Intuitively, this seems sketchy. I mean... can't there be a scenario where I might want to betray Bob and not approve of him, in order to boost Alice's chances of winning? Yes, absolutely.

However, rather than focusing on the idea that Gibbard's theorem is trying to prove that the systems you are familiar with are manipulable, I think it's better to think of this proof as showing that if there *was* a strategyproof voting system that could handle three or more outcomes, it would have to be a dictatorship.

We basically construct a voting scheme from a game form as follows:

$$v(P) = g(\sigma(P))$$

That is, given some underlying preferences $P$, we ask each voter to use their best response strategy $\sigma_k(P_k)$ in the game $g$. Whoever the game selects as the winner is who we define as the winner of the voting scheme $v$ for that profile of preferences $P$.

I just think this is really neat. To generalize beyond ranked voting systems, we create a game. We suppose we have some straightforward game form $g$, with best response strategies $\sigma$. We then define a strategyproof "voting system" $v$ (which isn't necessarily a traditional ranked voting system) based on this straightforward game form.

### Pure Determinism

One thing that we should be clear about is that this theorem from this 1973 paper is about *deterministic* game forms. That is, absolutely no ties allowed. When the players/voters go out to vote, and do their dances or whatever, a *single* name as an outcome must be chosen.

In most *real* systems that we use, we often have some chance-based tie breaking mechanism. A coin flip, for example. This creates a "lottery" of outcomes, rather than a single outcome. To explain how chance can weaken strategy, Gibbard explains the system which I like to call "Random Dictatorship". Everyone casts their vote, and then a single ballot is drawn, and that decides the entire election.

Gibbard calls this system "unattractive", for very obvious reasons. If some joker writes down "Mickey Mouse" on his ballot, then what the heck are we supposed to do if his ballot is chosen? Gibbard tackles this in a later paper, but we're going to stick with purely deterministic games/"voting schemes" in this post.

Something a bit unintuitive that Gibbard uses is a sort of "tie-breaking" preference $Q$, which is a strict ranking. This is not a preference that any voter has, but rather a preference that the voting scheme itself has. For example, perhaps $Q$ lists the candidates alphabetically. This is a little weird, but it's absolutely necessary to ensure that our voting scheme and game form are purely deterministic. We often "defer" to $Q$ when we need to sort of rank things arbitrarily or break ties.

### The Approval Voting Exception

As usual, Approval voting is a technical exception. Brams and Fishburn ([1978](https://doi.org/10.2307/1955105)) proved that Approval voting is strategyproof on dichotomous preferences, where voters only have two levels of preference: "acceptable" and "not acceptable". In the framework of Gibbard's 1973 paper, we basically restrict $P_i$ to only have two levels of preference.

Then, we have strategies $S_i=2^X$ (subsets of the outcomes $X$), and dominant strategies $\sigma_i(P_i)$ that say "approve of all the candidates that are acceptable in $P_i$, and don't approve of any of the candidates that are not acceptable". Then, we have a game $g$ that says "choose the candidate(s) with the most approvals, and if there is a tie, defer to $Q$". Meaning that, among the candidates in the tied set, elect the one that is ranked highest in $Q$.

This game form can be shown to be straightforward, and thus the voting scheme of Approval voting $v(P) = g(\sigma(P))$ is strategyproof. It's not necessarily trivial that a $Q$ tie-breaker maintains the strategyproofness. However, if we view it from the perspective of a voter voting for their "acceptable" candidates, and pushing them into the tied set, then $Q$ either selects the same candidate as before, or must choose one of the new candidates introduced to the tied set (why?). In the latter case, the voter is strictly better off, and in the former case, they are just as well off. Thus, voting for all acceptable candidates is a best response regardless of what everyone else does, and thus Approval voting is strategyproof on dichotomous preferences.

This does not break Gibbard's proof, however, since he assumed unrestricted domain on the preferences $P$ that voters can hold. Since we have three or more possible outcomes, we can't assume that $P$ is dichotomous. But, it is nice to know that if a voter's preferences are dichotomous, they do, in fact, have a best response: perfect honesty.

This is also technically true of non-Approval score voting systems which only aggregate points (i.e. not STAR), due to the min/max strategy which makes it equivalent to approval voting.

## The Proof Structure

Okay, so we assume we have some straightforward game, $g$. We have that each player has a best response strategy $\sigma_k(P_k)$ for whatever their underlying preference $P_k$ is. We then define a voting scheme from this game form as $v(P) = g(\sigma(P))$. We assume that there are at least three possible outcomes in the outcome set $X$. We must show that $g$ is dictatorial:

> **Definition:** A game form $g$ is dictatorial if there is some player $k$ such that for each outcome $x \in X$, that player has some strategy $s(x)$ such that if they play that strategy, then $g(s)=x$ whenever $s_k = s(x)$. That is, player $k$ is a dictator if they make any candidate in $X$ win by playing some strategy, no matter what everyone else does.

The basic structure of the proof is to use [Arrow's theorem](../arrows){:target="_blank"}:

> **Theorem:** (Arrow's Impossibility Theorem) A social welfare function (a function on a preference profiles that outputs a societal preference), defined on a set of finite voters, cannot satisfy all of the following criteria simultaneously:
>
> - Scope: There are at least three candidates in the set of outcomes $X$.
> - Unanimity: If every voter prefers candidate $x$ to candidate $y$, then the societal preference must also prefer $x$ to $y$.
> - Independence of Irrelevant Alternatives (IIA): If every voter in profile $P$ and $P'$ have the same relative preference between candidates $x$ and $y$, then the societal preference must also have the same relative preference between $x$ and $y$ in both profiles.
> - Non-Dictatorship: There is no single voter whose preferences always determine the societal preference between any two candidates.

Gibbard shows that if a game form $g$ is straightforward, and there are at least three possible outcomes, then from the voting scheme $v(P) = g(\sigma(P))$, we can define a social welfare function $f$ that satisfies all of the criteria of Arrow's theorem except for non-dictatorship, and thus must be dictatorial. Then, he shows that if $f$ is dictatorial, then the game form $g$ must also be dictatorial.

## Inducing a Social Welfare Function

It's one thing to have a (social choice) function $v$ that just outputs a candidate. That's not *too* hard. But inducing a social welfare function from a social choice function is non-trivial. How do you create a societal ordering from a function that just outputs a single winner?

Gibbard's idea is to compare two (distinct) candidates $x$ and $y$ by looking at a very specific profile:

Given the voter's ranking $P_i$, we create a new ranking $P_i^*$ as follows:

- $x$ and $y$ are ranked at the top of the voter's
- If the voter prefers $x>y$, then they rank $x$ first and $y$ second. Likewise, if they prefer $y>x$, then they rank $y$ first and $x$ second.
- If the voter is indifferent between $x$ and $y$, then they defer to $Q$, and rank $x$ and $y$ according to $Q$.
- For every other candidate besides $x$ and $y$, we rank them according to $Q$, below $x$ and $y$.

We take a profile $P$ and then construct an alternate profile which we can call $P^*_{xy}$. A nice thing about this profile is that there is absolutely no indifference, every voter in the profile has a strict preference between all candidates. This is because we defer to $Q$ whenever there is indifference, and $Q$ is a strict ranking.

> **Definition:** Given a profile $P$, we can construct a new profile $$P^*_{xy}$$ by taking each voter's ranking $P_i$ and creating a new ranking $$P_i^*$$ as described above. We define a relation on $X$ as follows: $f(P)$ ranks $x>y$ if $$v(P^*_{xy}) = x$$, and ranks $y>x$ if $$v(P^*_{xy}) = y$$. If $$v(P^*_{xy}) \neq x$$, then we say that $f(P)$ ranks $y\geq x$.

It's nontrivial that $f(P)$ is actually a "ranking" so to speak. So, I am using the phrase "$f(P)$ ranks ..." loosely, in a way that's not properly correct. As an example, we might have a majority relation, which would not be transitive in the case of a cycle. My favorite example being

**Example:**\label{rock-paper-scissors}

| Voters | Preferences                 |
|--------|-----------------------------|
| 1      | Rock $>$ Scissors $>$ Paper |
| 1      | Scissors $>$ Paper $>$ Rock |
| 1      | Paper $>$ Rock $>$ Scissors |

Here the majority relation $R$ would say

- $R$ ranks Rock $>$ Scissors, because 2 voters prefer Rock to Scissors, and 1 voter prefers Scissors to Rock.
- $R$ ranks Scissors $>$ Paper, because 2 voters prefer Scissors to Paper, and 1 voter prefers Paper to Scissors.
- $R$ ranks Paper $>$ Rock, because 2 voters prefer Paper to Rock, and 1 voter prefers Rock to Paper.

Thus, $R$ would not be transitive, and so we can't really say that $R$ is a proper "ranking". The burden of proof lies on us to show that our $f(P)$ cannot have such inconsistencies.

However, the construction of $f$ automatically gives us IIA, because the $P^*$ profile will always be the same, so long as the voters have the same relative preference between $x$ and $y$. This is because every other candidate will be ranked the exact same way, because we defer them to $Q$.

We still have to answer a few questions, though.

1. Does $f(P)$ always produce a transitive ranking? That is, is $f$ actually a social welfare function?
2. Does $f$ satisfy unanimity?
3. If $f$ is dictatorial, how does that imply that $g$ is dictatorial?

Gibbard uses a very clever "assertion" or lemma, which I think is worth breaking down. But I want to motivate the necessity of specifying "no voter is indifferent" in the coming results: we are going to be applying these results to $P^*$ profiles, which all have strict rankings, with no indifference.

> **Lemma:** Let $s=\sigma(P)$ (the best response strategies for the profile $P$), and let $s'$ be another set of strategies. Suppose that, for distinct $x$ and $y$, we have that
>
> 1. No voter is indifferent between $x$ and $y$
> 2. If a voter prefers $y>x$, then they play the same strategy in $s$ and $s'$
> 3. $f(P)$ ranks $y\geq x$
>
> Then, $g(s') \neq x$.

This is a whole lot of gobbledygook, but this is saying something *extremely* basic that matches our intuition of what it means for the system to be strategyproof. If $x$ is currently not winning over $y$, then the people who prefer $x$ can't deviate and do something else which would suddenly make $x$ win. That's it. But we do need that no voter is indifferent to apply this.

If $g(s')=x$, then, changing one strategy at a time, we would have to have *some* point where one direction gives a voter a beneficial strategy. Meaning that their $s$ strategy (which is *supposed* to be a best response) would give them an outcome that they prefer less than the outcome of $s'$. This would contradict the fact that $s$ is a best response strategy, and thus we must have that $g(s') \neq x$ (this is a very, very loose explanation of the proof).

> **Corollary:** If every voter in $P$ ranks $x>y$, then $f(P)$ ranks $x>y$.\label{unanimity}

Suppose we have a profile $P$ where every voter ranks $x>y$, and $f(P)$ ranks $y\geq x$. Then, since $x$ is an outcome, we can have $s'$ be such that $g(s')=x$. But then, by the lemma, moving from $s=\sigma(P)$ to $s'$, we should have that $g(s') \neq x$, which is a contradiction. Thus, $f(P)$ must rank $x>y$.

This also trivially tells us

> **Corollary:** If $f(P)$ ranks $y\geq x$, and no voter is indifferent between $x$ and $y$ in $P$, then $v(P) \neq x$.\label{f-geq-implies-not-v}

We can just use $s=s'$ and apply the lemma, which is pretty nice. Similarly, if $v(P)=x$, and no voters are indifferent between $x$ and $y$, then we must have that $f(P)$ ranks $x>y$. The contrapositive of this statement tells us

> **Corollary:** If $v(P)=x$, and no voter is indifferent between $x$ and $y$ in $P$, then $f(P)$ ranks $x>y$.\label{v-implies-f}

Like the proof of the lemma, the proof that $f$ actually is a social welfare function (in that it produces a transitive order) is a bit... "in the weeds". So, I will defer to the original paper for that. However, I will leave a short explanation below for the curious.

> **Theorem:** $f(P)$ is a transitive ranking of the candidates in $X$, and thus $f$ is a social welfare function.

{% proof Proof sketch %}
Suppose we have three candidates $x$, $y$, and $z$, and suppose that $f(P)$ ranks $x>y$ and $y>z$. We want to show that $f(P)$ ranks $x>z$.

Knowing that $f(P)$ ranks $x>y$ and $y>z$ tells us, exactly, that $v(P^*_{xy})=x$ and $v(P^*_{yz})=y$. We want to show that $v(P^*_{xz})=x$. If we construct a profile $P'=P^*_{xyz}$ using the same type of construction as $P^*_{xy}$:

- Every voter with a strict preference between any two of $x$, $y$, and $z$ ranks them according to that preference.
- Every voter puts $x$, $y$, and $z$ at the top of their ballot.
- We defer to $Q$ for the ranking of any candidates other than $x$, $y$, and $z$
- We also defer to $Q$ when a voter is indifferent between any two of $x$, $y$, and $z$.

We can show that the profiles $P^*_{xy}$, $P^*_{yz}$, and $P^*_{xz}$ are all the same as $P'^*_{xy}$, $P'^*_{yz}$, and $P'^*_{xz}$, respectively. This is because the construction of $P^*$ only depends on the relative preference between the two candidates in question, and thus relative preference between any two candidates of $x$, $y$, and $z$ in $f(P)$ is the same as in $f(P')$. Thus, we have that $v(P'^*_{xy})=x$ and $v(P'^*_{yz})=y$.

This tells us that $v(P')$ cannot be $y$ or $z$, because $x$ beats $y$ in $P'^*_{xy}$, and $y$ beats $z$ in $P'^*_{yz}$. Thus, we must have that $v(P')=x$, and thus $f(P)$ ranks $x>z$ by Corollary \ref{v-implies-f}.
{% endproof %}

We thus, have successfully turned $v$ into a social welfare function $f$ that satisfies all of Arrow's criteria except for non-dictatorship. Therefore, by Arrow's theorem, $f$ must be dictatorial.

## Dictatorship Implies Dictatorial Game Form

We now know that $f$ is dictatorial. That is, we must have some voter $k$ such that $f(P)=P_k$. Let's suppose we have some profile $P_k^y$ where voter $k$ ranks $y$ at the top of their ranking. From this, we have, very straightforwardly, that if $P_k=P_k^y$ in $P$, then $f(P)=P_k$ ranks $y>x$ for all other $x$, so no $x\neq y$ can win by Corollary \ref{f-geq-implies-not-v}. Thus, $y=v(P)=g(\sigma(P))$, whenever $P_k=P_k^y$. However, we must show that $y=g(s')$ for any $s'$ where $s_k=s(y)$, for some $s(y)$ (which we will show can be $\sigma_k(P_k^y)$).

And suppose that in profile $P$ we have that voter $k$, the dictator, uses $P_k^y$, and every other voter ranks $x>y$. This is the "everybody hates $y$" profile (except the dictator).

Define $s(y)=\sigma_k(P_k^y)$, the best response strategy for voter $k$ when they have the preference $P_k^y$, and let $s=\sigma(P)$ be the list of best response strategies for all voters given the profile $P$. Thus, $k$ must use $\sigma_k(P_k^y)$.

Let's create a set of strategies $s'$, where voter $k$ plays $s(y)$, with no other restrictions on $s'$. The lemma tells us that $x$ can't win in $s'$ ($g(s') \neq x$), because the only voter who prefers $y$ to $x$, kept their strategy constant, and no voter was indifferent between $x$ and $y$.

Since this is true for any candidate $y$, we have that voter $k$ is a dictator for the game form $g$.

## Conclusion

What does this tell us? Well, the completely abstract game form Gibbard uses means that we can actually say quite a bit. If there are three options to choose from, and we have some finite group of people submitting "something" to influence that choice in a purely deterministic way, then we must choose between

- only one person's submission actually matters, and we ignore everyone else (dictatorship)
- there is not one best response that each player can use based on their underlying preference on the outcomes, that works regardless of what everyone else does

Therefore, there might be cases where you need to adjust your strategy to get a better outcome.

This idea doesn't perfectly apply to all of our typical voting systems, which may need chance to break a tie, but it does tell us that the pursuit of a strategyproof voting system is in vain. We can't just design a better, more complicated game form that will finally make it so that no one ever has to lie again when they go out to vote.

Gibbard says something very poignant.

> "Every voting scheme is dictatorial, limited to one or two possible outcomes, or subject to manipulation. Why should that matter? It means that no system of decision making but a trivial one can depend on informed self-interest to make outcomes a function of true preferences. If a system does make outcomes a function of preferences, it is in virtue of individual integrity, ignorance, or stupidity, or because preferences are sufficiently predictable that the system does not have to accommodate all possible patterns of preferences... The way [a voter] acts, then, must depend on something other than informed self-interest-perhaps ignorance, integrity, or stupidity."

In practice, it's basically impossible to figure out what the best response strategy is for your preferences, since you don't know what everyone else is doing. Polls are often wrong, and the result is unexpected. Some will vote on principle even if that vote is not at all optimal. Some will vote completely against their interests because they don't understand the system, or because they just don't care. etc. etc. etc.

But the Approval exception* is still interesting. If your preferences are dichotomous, then you do, in fact, have a best response. That is, if the preference you are choosing to apply, $P_i$, is dichotomous--for example, if you decide some subset of candidate are all "acceptable" and you only care that any one of them wins the election--then you can safely vote for all of them without worrying that you're failing to use some better strategy. In other words, $\sigma(P_i)$ is perfectly well defined if $P_i$ is dichotomous.

Voting systems like [STAR voting and Condorcet methods](../approval-only/){:target="_blank"} like to tout that they have strong honesty incentives, which is somewhat true. But they do, in fact, have potential for completely sincere and honest strategies to fully and completely backfire on you. Approval voting, relatively speaking, is one of the safest systems to vote in.

## References

Brams, S. J., & Fishburn, P. C. (1978). Approval Voting. The American Political Science Review, 72(3), 831--847. [https://doi.org/10.2307/1955105](https://doi.org/10.2307/1955105)

Gibbard, A. (1973). Manipulation of Voting Schemes: A General Result. Econometrica, 41(4), 587--601. [https://doi.org/10.2307/1914083](https://doi.org/10.2307/1914083)