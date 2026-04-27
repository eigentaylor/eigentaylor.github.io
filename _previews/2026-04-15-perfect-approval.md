---
layout: distill
title: The Perfection of Approval Voting
date: 2026-04-15
description: A mathematical dive into the fundamental nature of Approval voting on dichotomous preferences.
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
related_posts: true
theorems: true
pretty_table: true
chart:
  plotly: true
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: None
toc:
  - name: Introduction
    subsections:
      - name: May's Theorem
  - name: Dichotomous Preferences
  - name: The Natural Language of Dichotomous Preferences
    subsections:
      - name: The Significance of Strategyproofness
      - name: Uniqueness of Approval
      - name: The Extension of May's Theorem
  - name: Impossibilities Achieved
  - name: The Projection Perspective
  - name: The Canonical Voting System
  - name: Appendix
  - name: References
---

## Introduction

I've made plenty of [cases for Approval voting recently](../approval-only/){:target="_blank"}. I've talked about it in direct comparison with other methods and why I think it wins out for [various practical reasons](../practicalapproval/){:target="_blank"}. But that's not what I want to do in this post.

Here, I'm going back to my roots. I'm going to talk about the pure math underlying Approval voting, and why it's fundamental in a way that other voting systems just aren't. I will talk about the proofs that--under certain assumptions--Approval actually breaks famous impossibility theorems like [Gibbard-Satterthwaite](../gibbard-satt/){:target="_blank"} and [Arrow's Theorem](../arrows/){:target="_blank"}, and what that means.

This post is inspired and borrows heavily on an amazing paper by [Marc Vorsatz: "Approval voting on dichotomous preferences"](http://www.jstor.org/stable/41106808).

Many of the things I say here about Approval will not be true about Approval with a runoff. The runoff tends to really hamper the honesty incentives of Approval (in theory). In practice, there is evidence to suggest that the runoff might improve outcomes, but that's not what we're talking about here. We're talking about pure, single round, "vanilla" Approval voting.

### May's Theorem

In 1952, just a year after Kenneth Arrow published his impossibility theorem, another Kenneth in social choice theory, Kenneth May, published a theorem of his own.

> **Theorem:** (May's Theorem) Given a race between two candidates, the unique voting system that is anonymous, neutral, and strictly monotone is majority rule.

To put this in very simple terms:

- **Anonymous:** No voter bias. Everyone's vote is equal. Waldo doesn't contribute 100 votes just because he owns a hundred shares in the company.
- **Neutral:** No candidate bias. The system treats all candidates equally. No bias for Bob because his name starts with a B.
- **Strictly Monotone:** Your vote actually *matters*. If candidate $x$ is already winning or tied for first, then voting for $x$ makes them win outright.
- **Majority Rule:** (AKA [Condorcet](../condorcet-approval/){:target="_blank"}) You can either give one vote to either candidate, or abstain. The candidate with the most votes wins. If there is a tie, then we just say that both candidates win.

This is... painfully obvious. I mean, how else would you possibly pick between two people? Just choose the one with the most votes, right?

Well, for two candidates, this is obvious. But for decades, the extension of this theorem to more than two candidates was an open problem. The main problem was [the Condorcet paradox](../condorcet-approval/){:target="_blank"}, which throws a wrench into majority rule. For example, take the following electorate:

| Voters | 1st Tier | 2nd Tier | 3rd Tier |
|--------|----------|----------|----------|
| 5      | Rock     | Scissors | Paper    |
| 4      | Scissors | Paper    | Rock     |
| 3      | Paper    | Rock     | Scissors |

A majority of eight prefers Rock to Scissors, a majority of nine prefers Scissors to Paper, and a majority of seven prefers Paper to Rock. So who wins? Majority rule doesn't work here. There is no candidate for which it truly makes sense to elect.

But even before May, we already knew that [three candidates is a big problem, thanks to Arrow](../arrows/){:target="_blank"}. Arrow's theorem says that if you have three or more candidates, there is no voting system that can satisfy a certain set of (supposedly) "reasonable" criteria. You essentially have to pick one of the following:

- **Dictatorship:** One voter gets to decide everything. Waldo's ballot is the only one that counts.
- **Infinitely many voters:** If you allow for infinitely many voters, Peter Fishburn showed, hilariously, that you can get a "perfect" majority rule voting system using measure theory. See [this post](../arrows/){:target="_blank"} for more on that.
- **IIA Violation:** The voting system violates the "Independence of Irrelevant Alternatives" criterion, which *loosely* means that an irrelevant spoiler candidate can change the outcome of the election. For example, if Alice originally beats Bob, then the entrance of Clark into the race can cause Bob to win, even if a majority still prefers Alice to Bob.
- A secret fourth choice we will get to shortly...

The knife was twisted in the 70's when Gibbard went on to show that strategy is a fundamental part of voting systems, when you have three or more candidates. Essentially, either the system has to be completely unresponsive to your preferences, or you will always have opportunities to get a better outcome by lying to the system. While Gibbard's more general theorem in 1972 hits essentially every voting system (and many more types of things), the [Gibbard-Satterthwaite](../gibbard-satt/){:target="_blank"} theorem is a corollary that applies specifically to ranked voting systems.

The standard conclusion to take from these theorems is that there is no "perfect" voting system. You have to compromise somewhere. If you want something democratic and responsive to the voters, you won't be able to guarantee it works ideally in all scenarios. You'll always get a case where lying is profitable, or a spoiler candidate throws the system into chaos. But it turns out that this conclusion is not quite the full story.

## Dichotomous Preferences

It turns out that the true underlying key to May's theorem is not exactly that it's just two *candidates*. But, rather, that there are at most two *preference tiers* in the minds of the voters.

> **Definition:** A voter's preferences are *dichotomous* if they can be represented in a maximum of two tiers. In other words, the voter declares each candidate either "acceptable" or "unacceptable", with no further ranking or differentiation between candidates within those tiers. This can include complete indifference (where all candidates are in the same tier).

It may seem like we're basically lobotomizing the voters here. And critics of Approval often argue that this a serious problem. By squashing the voters' nuanced preferences into just two tiers, it becomes very easy to construct pathologies where voters use very strange Approval thresholds which elect candidates which seem "bad" [based on the ranked data](../why-condorcet/){:target="_blank"}.

But, from another perspective, when faced with many options, there's an argument that we often do simplify our preferences by just partitioning candidates into "good" and "bad" buckets. Particularly when information is scarce, or we haven't had time to develop more nuanced preferences.

Vorsatz proposes an example of a committee trying to hire a specialized contractor. At the early stages of the process, it may be easier to just label candidates as "qualified" or "unqualified", rather than trying to rank them in a more detailed way. But, more generally, there is an argument to make that even in high stakes elections, voters can identify a set of "acceptable" candidates that they would be happy to see win, and a set of "unacceptable" candidates that they would not want to see win, even if they have an underlying ranking of the candidates.

For example, suppose I love Alice, I think Bob is okay, and I hate Clark. While I technically have three-tiered preferences here, I might decide that Clark is so "unacceptable" that Alice and Bob are both "acceptable" to me. Sure, if it was a runoff between Alice and Bob, I would vote for Alice. But given this is a race between all three, I might decide to just express my preferences more simply as "please, Alice or Bob, just not Clark". If expressed in this way, my preferences have become dichotomous.

There is, in fact, genuine [psychological research](https://doi.org/10.1037/0278-7393.14.3.534) that indicates that people often use binary cutoffs and heuristics as mental shortcuts to make decisions, particularly under time pressure. In that way, Approval's binary cutoff ballot format may actually be more in line with how people naturally think about their preferences, rather than constructing a more complex ranking or rating system. Not everyone is a political junkie, and if you're reading this the probability is high you are not representative of the average voter.

However, we won't dwell too much more on this. Regardless of whether you think dichotomous preferences are realistic, it turns out that they are our fundamental ticket out of all the messiness of voting.

The question is: in this three candidate race, can we extend May's theorem to find a unique voting system to decide the winner(s) that satisfy basic fairness criteria? If we restrict ourselves to dichotomous preferences, the answer is yes!

## The Natural Language of Dichotomous Preferences

The most natural system we might devise for dichotomous preferences is to just count how many voters find each candidate acceptable, and then pick the candidate with the most "approvals". This is exactly what Approval voting does.

> **Definition:** In Approval voting, voters mark each candidate as either "approved" or "not approved". The candidate(s) with the most approvals wins.

We stated May's theorem above as satisfying three criteria: anonymity, neutrality, and strict monotonicity. For two candidates, this was sufficient. These three criteria are enough to prove that the system *has* to be majority rule. We can also see that Approval voting satisfies these three criteria.

- Nobody's vote counts more than anyone else's, so it's anonymous.
- The system treats all candidates equally, so it's neutral.
- If a candidate is tied for first, then voting for them makes them win outright, so it's strictly monotone. Your vote actually matters.

But to extend May's theorem to more than two candidates, we need a fourth criterion.

> **Definition:** A voting system is **strategyproof** if no voter can ever "manipulate" the outcome by misrepresenting their preferences.

To get a sense for what this means in practice, let's say that initially we have that Alice and Bob are currently tied for first. I prefer Alice over Clark, and so I voted accordingly (voting that Alice is good and Clark is bad). Strategyproofness means that I can't change my ballot to something else and get a better outcome, such as making Alice win.

Here's an example to show what that might look like. Suppose we have a voting system where you submit your "good" and "bad" candidates. If you say that $n$ candidates are good, then each gets $\frac{1}{n}$ points, and the candidate with the most points wins. This is anonymous, neutral, and monotone, but it's not strategyproof.

Consider the following scenario: Suppose that currently, Alice is behind Clark by half a point, while Bob and Dylan are behind both of them.

| Voters | Ballot | A | B  | C  | D  |
|--------|--------|---|----|----|----|
| 2      | B, C, D|0  |0.33|0.33|0.33|
| 2      | A, C   |0.5|0   |0.5 |0   |
| Total  |        |1  |0.66|1.66|0.66|

Let's assume my true preference is that Alice and Bob are both good, and both Clark and Dylan are bad. Let's compare my honest ballot for both Alice and Bob, versus a dishonest ballot for just Alice.

| My Ballot | A total  | B total  | C total  | D total  | Outcome    |
|-----------|----------|----------|----------|----------|------------|
| A, B      | 1.5      | 1.16     | 1.66     | 0.66     | C wins     |
| A         | 2        | 0.66     | 1.66     | 0.66     | A wins     |

If I say that only Alice is good, and lie about liking Bob, then my vote now gives Alice a *full* point, and Bob gets zero. This would give Alice a third of a point more than Clark, and make her win outright. If I'm honest, then my support is diluted between Alice and Bob, and Alice doesn't get enough support to win. I thus have an incentive to lie. This violates strategyproofness.

But Gibbard's theorem tells us that if we have three or more candidates, then it can't be strategyproof, right? Not on dichotomous preferences!

In [1978, Brams and Fishburn](https://doi.org/10.2307/1955105) prove that Approval voting is the unique "single ballot non-ranked" voting system (a system where you can give single votes to some number of candidates) which is strategyproof on dichotomous preferences.

The intuition being that

- If you vote for any "unacceptable" candidate, then you might make them win over an "acceptable" candidate, which is bad.
- If you don't vote for any "acceptable" candidate, then you might fail to break a tie between an "acceptable" candidate and an "unacceptable" candidate, which is also bad.

So voting exclusively for all good candidates and no bad candidates is *uniquely* undominated. There's no reason to submit any other ballot, and you'll never get anything but a potentially worse outcome by doing so.

### The Significance of Strategyproofness

This is worth emphasizing: strategyproofness is inherently achievable on dichotomous preferences. Essentially, each voter has two "blobs" of candidates: the good and the bad. Each voter just wants *any* candidate from the good blob to win, and *no* candidate from the bad blob to win. So there's nothing better to do than to fully support every option in the good blob and fully oppose every option in the bad blob. This is exactly what Approval voting does, and so Approval voting is strategyproof on dichotomous preferences.

Since Approval picks the candidate with the most approvals, it's simply "counting" voters or support. One person, one vote! So making sure you're counted fully for all the good, and not at all for the bad, is the best you can possibly do. Why would you ever do anything else?

However, it's also worth emphasizing that strategyproofness, when defined *mathematically* has a very specific meaning different from the natural intuition that we've been using. They're equivalent in a sense, but not exactly the same.

The math doesn't *know* what your true underlying preference is. It just knows the ballot you submitted. So strategyproofness is defined more in terms of how the outcome changes relative to the original ballot you submitted, or were planning to submit. For our example above, the ballot where I approved of both Alice and Bob clearly said "I prefer Alice to Clark", because I approved of Alice and not Clark. But changing my ballot, by pretending I didn't like Bob, made Alice win outright. I was already saying that I liked Alice more than Clark, but it took a lie or exaggeration for the system to *respect* that preference and give me Alice as the winner over Clark. My ballot had potential to be decisive, but *wasn't* without strategic manipulation.

Gibbard's theorem, and its [extension by Satterthwaite](../gibbard-satt/){:target="_blank"} says that if you have three or more candidates, then no voting system (including Approval!) can be strategyproof. Intuitively meaning that you can be clearly telling the voting system "I prefer Alice to Clark!", but you need to lie about your preferences in some other way to change the outcome from Clark winning to Alice winning.

Approval is not strategyproof when you have three or more tiers of preference. Then there can certainly be strategic consideration as to where to cut off your threshold of acceptability. *However*, based purely on the ballot data, Approval *does* hold a strategyproofness property. If you are already disapproving of Clark, you don't need to exaggerate to make sure your ballot fully counts against him. The ballot never betrays what you tell it. That is *not* a given in any other voting system.

This makes an Approval ballot incredibly "honest" in a way that other ballots aren't. Any other system, you might tell the system a preference, but need to lie or exaggerate in some other way to get the system to respect that preference. Voting for your favorite in STAR or RCV might give you your worst nightmare due to runoff rounds or vote transfers. Not in Approval!

### Uniqueness of Approval

Alright, so Approval is anonymous, neutral, strictly monotone, and strategyproof on dichotomous preferences. Big whoop, right? Why does that matter? It turns out this is a *huge* whoop.

> **Theorem:** (Vorsatz, 2007) Approval voting is the *unique* voting system that is anonymous, neutral, strictly monotone, and strategyproof on dichotomous preferences.\label{approval-unique}

It's not just that Approval happens to be so, it's that Approval is the *only* system that can satisfy these criteria. If you define a voting system that is anonymous, neutral, strictly monotone, and strategyproof on dichotomous preferences, then you can show it is *exactly* Approval voting. No other system can satisfy these criteria. And it gets even better...

> **Theorem:** (Vorsatz, 2007) The four criteria of anonymity, neutrality, strict monotonicity, and strategyproofness on dichotomous preferences are independent (Theorem \ref{approval-unique} is "tight"). That is, for each criterion, there exists a voting system that satisfies the other three criteria but violates that one.

Vorsatz shows that if you drop any single one of the four criteria, you can define some other voting system that satisfies the other three criteria but violates the one you dropped. So these four criteria are sufficient *and necessary* to define Approval voting on dichotomous preferences.

- Dropping strategyproof allows for scoring rules like the one in the example above.
- Dropping strict monotonicity allows for a system where everyone ties all the time and your vote is completely meaningless
- Dropping anonymity allows for Waldo to cast 5 votes instead of 1, because he's a generous donor.
- Dropping neutrality allows for candidate favoritism. For example, Bob is a friend of the CEO so if he ties for first, all ties are broken for him.

This, in a sense, makes Approval the "natural language" of dichotomous preferences. It satisfies the most basic fairness properties like neutrality and anonymity by holding no bias for voters or candidates. It's responsive to the voters' preferences by being strictly monotone. And it escapes manipulation by being strategyproof.

Intuitively, it might make sense that Approval is the most basic and intuitive possible voting system you might define if people are labeling candidates "good" and "bad". Just find the candidate(s) the most people think are "good". Done. But Vorsatz shows that it's more fundamental than that.

Rather than "Approval is intuitive and happens to satisfy xyz...", it's more that the dichotomous domain, though simple, still gives us a lot of room for weird and crazy voting systems. But as we take away more and more of the "weirdness" by imposing these basic criteria, we end up building a cage that can only contain one voting system: Approval. Approval becomes the lossless, perfect measure of the voters' preferences on this domain. It becomes the ultimate "honest" system. Your ballot means *exactly* what it says, and that eliminates all room for manipulation.

### The Extension of May's Theorem

One can verify that strategyproofness actually fits perfectly into majority rule on just two candidates. If you prefer one candidate over the other, then the only reasonable ballot is to vote for that candidate and not the other! And if you're indifferent, then expressing that honestly by abstaining is undominated. So strategyproofness is satisfied by majority rule with two candidates.

Further, notice that majority rule on two candidates is also equivalent to Approval voting. Voting for one candidate and not the other is exactly the same as approving of one candidate and not the other. Abstaining is the same as approving both candidates. Therefore, we can say that it's not exactly majority rule or Condorcet that May's theorem describes, but Approval voting! Which isn't a big surprise as [Approval is a two-tiered Condorcet method](../condorcet-approval/){:target="_blank"}--equivalently, Approval is equivalent to Condorcet rule on the dichotomous domain. Thus,

> **Theorem:** (Extension of May's Theorem) The unique voting system that is anonymous, neutral, strictly monotone, and strategyproof is Approval voting on dichotomous preferences.

And, of course, when you only have two candidates, you obviously have dichotomous preferences! So this is a true generalization of May's theorem.

Brams and Fishburn also proved in 1978 that, on dichotomous preferences, Approval voting is exactly the same as Condorcet. So the fact that May's original theorem is usually stated as majority rule or Condorcet means that this extension via dichotomous preferences through Approval voting is actually quite natural.

## Impossibilities Achieved

As mentioned in my [April Fools' post](../condorcet-approval/){:target="_blank"}, Approval voting is the only Condorcet method that escapes the Condorcet paradox. Approval voting determines the societal ranking, and pairwise defeats, of candidates via the number of approvals. If Alice gets more approvals than Bob, then Alice defeats Bob in a pairwise comparison. And since numbers don't cycle, neither does Approval. As a [two-tiered Condorcet method](../condorcet-approval/){:target="_blank"}, Approval is a Condorcet method that never has a paradox, so the Approval winner(s) are always at least weak Condorcet winners.

Therefore, Approval escapes the Condorcet paradox, and thus escapes the problems that come with it. Cycles are the source of many criterion failures in Condorcet methods, such as the failure of participation, strategyproofness, and IIA.

While I talked about IIA in my post on [Arrow's theorem](../arrows/){:target="_blank"}, I think it's worth emphasizing again here. I love to introduce it with the famous joke about Sidney Morgenbesser:

> Morgenbesser, ordering dessert, is told by a waitress that he can choose between blueberry or apple pie. He orders apple. Soon the waitress comes back and explains cherry pie is also an option. Morgenbesser replies "In that case, I'll have blueberry."

Intuitively, IIA basically just says that if you want to know if apple pie beats blueberry pie, then you only need to look at how people feel about apple versus blueberry. The presence or absence of cherry pie shouldn't change the outcome between apple and blueberry. The most shocking part of Arrow's theorem is that this seemingly reasonable criterion is actually utterly incompatible with the most basic fairness criteria we might want in a voting system. Approval voting is really the closest (reasonable) voting system that can be said to satisfy it.

There is a really cool lemma in the Vorsatz paper which I think is quite illuminating.

> **Lemma:** (Vorsatz Lemma 1) If a voting system is neutral and strategyproof, then it satisfies Independence of Irrelevant Alternatives (IIA).\label{stratproof-iia}

{% proof Click to expand proof %}
**Proof:** Suppose we have two profiles $P$ and $P'$ where every voter who strictly prefers candidate $x$ to candidate $y$ in $P$ also strictly prefers $x$ to $y$ in $P'$, and vice versa. Suppose for contradiction that this changes the outcome between $x$ and $y$. Without loss of generality we assume that in $P$ we have that $x$ wins and $y$ does not win, and in $P'$ we have that either $y$ wins (and not $x$) or $x$ and $y$ tie. We can call that "$y$ entering the winning set".

If every voter is indifferent between $x$ and $y$, then we would have a violation of neutrality, as we could just swap the names of $x$ and $y$ and get a different outcome without changing any of the ballots. So there must be at least one voter who strictly prefers one of the candidates to the other. We assume that voters who do not distinguish between $x$ and $y$ have no impact on the outcome between $x$ and $y$, so we can ignore them (this is called "consistency in individuals").

Let's look at a single concerned voter $v$. Because the strict preferences between $x$ and $y$ are the same in both profiles, $v$ votes with the same preference in both. Let's create an intermediate profile where just $v$ changes their ballot from $P$ to $P'$.

If $v$ strictly prefers $y$ to $x$, and we know that $x$ wins in $P$, then could the outcome change? If $v$ changes their ballot to their ballot in $P'$, and $y$ enters the winning set, then that would mean that $v$ has an incentive to lie. They prefer $y$ to $x$, but by changing their ballot to their ballot in $P'$, they can cause $y$ to enter the winning set, which is a better outcome for them. This would contradict strategyproofness. So $y$ cannot enter the winning set. Thus, the outcome cannot change if we change $v$'s ballot from $P$ to $P'$.

If $v$ strictly prefers $x$ to $y$, and $v$ changes their ballot to their ballot in $P'$, then suppose $y$ enters the winning set. This means that by changing from their $P'$ ballot to their $P$ ballot, they *remove* $y$ from the winning set, which is a better outcome for them. This would contradict strategyproofness. So $y$ cannot enter the winning set when moving $v$'s ballot from $P$ to $P'$.

We have hence shown that changing each concerned voter's ballot from their ballot in $P$ to their ballot in $P'$ cannot possibly change the outcome from $x$ winning and $y$ not winning, without contradicting strategyproofness. This contradicts the assumption that the outcome changes from $P$ to $P'$. Therefore, the outcome between $x$ and $y$ cannot change from $P$ to $P'$ if the relative preferences between $x$ and $y$ are the same in both profiles. Thus, the voting system satisfies IIA. $\square$
{% endproof %}

This is a really big deal. IIA is *the* criterion that causes so much trouble in Arrow's theorem. And, of course, strategyproofness is the big concern in Gibbard's theorem. So it turns out the fact that Approval *technically* breaks Gibbard's theorem (strategyproofness) and also Arrow's theorem (IIA) is not a coincidence at all. Rather, strategyproofness is an inherent fact of dichotomous preferences, so the natural language of dichotomous preferences (Approval) is strategyproof, so Approval has to satisfy IIA. It's all connected.

Arrow's theorem and Gibbard's theorem are often framed as saying that there is no "perfect" voting system. But what we see here is that, on dichotomous preferences, there is a perfect voting system: Approval. It satisfies all the basic fairness criteria we might want, and it also satisfies IIA and strategyproofness.

> **Corollary:** (The Perfect Voting System) A voting system is anonymous, neutral, strictly monotone, strategyproof, and satisfies IIA if and only if it is Approval voting on dichotomous preferences.

The way dichotomous preferences allows us to sidestep these theorems is actually because the number of preference levels is strictly less than three, even though we might have more than two candidates. The general theme with these impossibility theorems often comes from the fact that there are three or more candidates in the assumptions. But that's not really what causes the problems.

The real problem comes from the fact that, with three or more candidates, we can potentially have *three or more preference tiers*. If we restrict ourselves to keep the number of preference tiers to two, then we can have as many candidates as we want, and still have a perfect voting system that satisfies all the great properties that typical impossibility theorems say we can't have.

The magic number is two. Not two candidates, as May's theorem would imply. But two *preference tiers*. The number of candidates is irrelevant! Approval voting is robust enough to handle all the candidates you can throw at it without cracking under pressure.

## The Projection Perspective

All we have said thus far requires dichotomous preferences to be truly correct. And it's true: if voters have more complex preferences, then Approval voting won't be strategyproof. It won't satisfy IIA.

However, Approval *doesn't know that*. When you cast an approval ballot, it doesn't matter how complex or messy your preferences are. You still have to actually *choose* "who is acceptable". Who do you "approve" of? Whatever that means to you. It requires the voters to *project* their preferences down into the dichotomous domain.

Every voting system requires some sort of lossy projection. Ranked systems ask you to eliminate all distance between candidates and report [only the order](../why-condorcet/){:target="_blank"}, which can obscure all acceptability and intensity, and obscure compromise and consensus. Range methods like STAR require you to project each candidate onto a 0-5 star rating, which can lose order between some candidates and are prone to exaggeration and misrepresentation, and for which the scale is not well defined. Approval instead asks for an unambiguous signal of support: "Do you consent?" Consent to be governed. Consent to be supported by your vote. Consent to be elected.

If we assume that the ballots are a perfect reflection of reality, then Approval is perfect. It's nearly impossible to look at the Approval ballot data and point to a pathology.

- There are no issues where a majority preferred a candidate who was eliminated because of vote splitting, like in RCV.
- There are no clear spoiler candidates, because all the votes a nonviable candidate received were given by voters who were free to also vote for a viable candidate at no cost.
- There are no participation failures where, by voting for the candidates you like, you change the result to a *worse* outcome like in STAR, Condorcet, and especially RCV. Strict monotonicity means that your vote can only help a candidate you *actually vote for*. Which sounds absurdly trivial but is not a given in any other seriously proposed voting system, *except* Approval (and Choose-one plurality, which is just a special case of Approval).

That just *doesn't* happen in Approval, because it treats all the data it receives at face value. It doesn't have any weird quirks that cause it to misinterpret the data. An approval is an approval; an unambiguous signal of support. Impossible to exaggerate or misrepresent. The winner is simply the candidate who earned that unambiguous consent to govern from the largest number of voters. The candidate who earned the most consent.

But even though the ballot data *isn't* a perfect representation of reality, it still treats the data it gets with *full* fidelity. There are no *structural* issues with Approval voting. It does the best with the data it has. Any issue with Approval comes from the translation step. In that way, the issues with Approval are essentially "behavioral".

In this way, Approval asks voters to project their nuanced preferences into the dichotomous domain. It treats those preferences perfectly, and gives you a winner. We necessarily lose some information in the process. The question is how much that loss of information hurts the outcomes.

As I've also written about before, VSE (Voter Satisfaction Efficiency) is one measure of the outcomes of a system. [Approval gets a VSE range of 89-95%](https://electionscience.github.io/vse-sim/VSEbasic/). Meaning, it gets the "optimal" outcome about 90-95% of the time. That is *absurdly* good, especially in comparison to choose-one voting getting about 75%, and STAR voting clocking in around 91-98%. Approval is not perfect, but it's absurdly good for its simplicity and practicality. And that simplicity comes with the benefit of being particularly robust to insidious pathologies that can arise in more complex systems like RCV and STAR.

In a [1998 paper by Regenwetter and Grofman](http://www.jstor.org/stable/2634612), they found that Approval reliably picked the winners of Borda and Condorcet methods in experiments and real world elections when the ordinal preferences were reconstructed. In fact, they even say,

> "We find no evidence here that approval voting should be replaced by a more elaborate voting scheme." (p. 532)

And frankly, I agree. I think that those who are pushing more complex systems should really consider if the extra complexity is worth it, or if that system is just an overengineered solution to a problem that would be solved more simply by Approval. Particularly in a moment when [trust is low, RCV is imploding, and a failure to pass something more complicated than approval might ruin our chances and eliminate the public's appetite to get *anything* to replace Choose-one voting](../approval-only/){:target="_blank"}.

No participation failures, no vote splitting, no spoilers, no monotonicity failures, no favorite betrayal. Your vote can only help the candidates you vote for. Easy to count, easy to understand, easy to participate in. That's a pretty fantastic report card. Okay, that's enough, I can't help but make the case for Approval again. Let's wrap this up.

## The Canonical Voting System

The way I interpret May's theorem is that majority rule is the "canonical" voting system for two candidates. It's the unique system that satisfies the most fundamental idea of fairness in that context. It's the "natural language" of two candidates. If you want to be fair and responsive to voters in choosing between two options, then you have to use majority rule.

Vorsatz essentially generalizes this beyond two candidates to two preference tiers. The "canonical" voting system for dichotomous preferences is Approval. It's the unique system that satisfies the most fundamental idea of fairness in *that* context. It's the "natural language" of dichotomous preferences. If you want to be fair, responsive, and eliminate strategic incentives for dichotomous voters, then you have to use Approval.

But what does that really *say*? Is this just a fun mathematical exercise? Are we just skipping around the impossibility theorems by lobotomizing the voters? Yeah, sure, voting is easy if the world is black and white. But the world isn't black and white, so this is just a theoretical exercise, right?

I don't think so. I'm not ready to say Approval is the "perfect" voting system for the real world. It's certainly the [practical approximation of a perfect voting system](../practicalapproval/){:target="_blank"}. But rather than think of dichotomous preferences as a "get out of jail free" card, or a sneaky loophole, I think it's more accurate to say that Approval voting asks the *right* question.

We are conditioned to think that more data is always better. That more nuance gets us a better picture of reality. But, as a mathematician, I can tell you from personal experience that the more complicated you make your model, the *less* realistic it tends to be! You start collecting noise and overfitting. I'm not saying it's impossible to create a state of the art model which is both complex and accurate. But, in those cases, you usually need excellent data as an input.

In the context of a voting system, the "model" is the voting system itself, and the "data" is the ballot data you collect from the voters. The more complex your ballot, the worse the data quality tends to be. Voters have things to do, man. Many don't have time to rank 20 candidates, or give each of them a thoughtful 5-star rating. And when you rely on your system being "top of the line" through treating detailed preference data "well enough", you are more than likely going to be collecting *noise* rather than true signal.

[More data can often *obscure* the true compromise](../why-condorcet/){:target="_blank"}. Instead, why not just ask a simple, unambiguous question: "Who do you consent to govern you?" That's what Approval does. It asks a simpler, more fundamental question, and treats that data with full fidelity. It doesn't try to extrapolate more from you than what you give it. It's simple, but more honest. And by keeping it simple, it makes itself robust and practical, while still delivering excellent outcomes.

Approval is the canonical voting system for dichotomous preferences. But manages to stay an excellent voting system for all preferences. It just asks a different question than I think many in the electoral reform space *think* should be asked. It doesn't care about the order of your preferences, which obscures all sense of acceptability. It doesn't care about the intensity of your preferences, which are prone to exaggeration and misrepresentation. It just asks you who you want to support. Isn't that the most fundamental question we should be asking? Who do *you* actually want to win?

If democracy is ultimately about consent, then Approval is the ballot that captures consent most directly: not perfect information, but honest information. It asks each voter for one clear boundary between acceptable and unacceptable, then counts that boundary without distortion. That is why, mathematically, it becomes canonical on dichotomous preferences, and why, practically, it remains so compelling in the real world. We may never build a flawless voting system for every possible psychology, but we can choose one that is fair, transparent, strategy-resistant where it matters, and robust under real conditions. Approval does not promise utopia. It promises clarity, and in collective decision-making, clarity is power.

## References

Brams, S. J., & Fishburn, P. C. (1978). Approval Voting. *The American Political Science Review*, 72(3), 831-847. [https://doi.org/10.2307/1955105](https://doi.org/10.2307/1955105)

Payne, J. W., Bettman, J. R., & Johnson, E. J. (1988). Adaptive strategy selection in decision making. Journal of Experimental Psychology: Learning, Memory, and Cognition, 14(3), 534--552. [https://doi.org/10.1037/0278-7393.14.3.534](https://doi.org/10.1037/0278-7393.14.3.534)

Quinn, J. (2017). Voter Satisfaction Efficiency (VSE) summary. Center for Election Science. [https://electionscience.github.io/vse-sim/VSEbasic/](https://electionscience.github.io/vse-sim/VSEbasic/)

Regenwetter, M., & Grofman, B. (1998). Approval Voting, Borda Winners, and Condorcet Winners: Evidence from Seven Elections. Management Science, 44(4), 520--533. [http://www.jstor.org/stable/2634612](http://www.jstor.org/stable/2634612)

Vorsatz, M. (2007). Approval voting on dichotomous preferences. Social Choice and Welfare, 28(1), 127--141. [http://www.jstor.org/stable/41106808](http://www.jstor.org/stable/41106808)
