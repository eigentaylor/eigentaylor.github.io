---
layout: distill
title: Is the Condorcet Winner the True Compromise?
date: 2026-04-11
description: The Condorcet winner is not the true compromise candidate, but legitimacy is important.
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
published: false
related_posts: true
theorems: false
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
      - name: The State of the Reform Movement
  - name: The Bridge Criteria
  - name: Legitimacy
  - name: Practicality
  - name: Outcomes
    subsections:
      - name: Vote Splitting and Participation Failures
      - name: Voter Satisfaction Efficiency
      - name: Expressiveness
  - name: Conclusion
  - name: References
---

## Introduction

Three friends are trying to decide on a restaurant for dinner. Two of them really love pizza, but the third is a vegan. The full rankings of the three friends are as follows:

| Number | First Choice | Second Choice | Third Choice |
|--------|--------------|---------------|--------------|
| 2      | Pizza Palace | Veg n' Go     | Burger Barn  |
| 1      | Veg n' Go    | Burger Barn   | Pizza Palace |

The vegan obviously loves the vegan restaurant, and Burger Barn has some decent vegan options, particularly compared to Pizza Palace, so the vegan prefers Veg n' Go > Burger Barn > Pizza Palace. The two pizza lovers are really craving pizza, and they had burgers for lunch, so they prefer Pizza Palace > Veg n' Go > Burger Barn.

Marquis de Condorcet, would decree that the true consensus option is Pizza Palace, because a majority of voters have it as their first choice. Majority rule, after all, is the most fundamental principle of democracy, isn't it?

But is it really? I am not a vegan, but I absolutely *love* Veg n' Go. It may not be my *first* choice on any given day, but I would be perfectly happy to eat there.

If both pizza lovers find Veg n' Go to be 99% as good as Pizza Palace, then Veg n' Go is a choice that literally 100% of voters would be happy with, while Pizza Palace would make the minority vegan extremely unhappy.

This example highlights my major issue with the Condorcet criterion.

> The *Condorcet winner* is the candidate who would win a head-to-head matchup against every other candidate. A voting system satisfies the *Condorcet criterion* if it always elects the Condorcet winner when one exists.

Many Condorcetists will argue that if you don't elect the Condorcet winner, then you are not electing the true compromise of the electorate. But I think this is a complete fallacy and misunderstanding of what a compromise is.

The Condorcet winner is something defined by *ordinal* preferences. That is, it only looks at a comparison of orderings of candidates by the voters. Why should consensus be defined by ordinal preferences?

When we talk about compromise, or negotiation, or consensus, we don't evaluate things simply by how many people prefer one option to another, or even necessarily by majority rule. We tend to try to find agreements that make everyone happy, even if they aren't everyone's first choice.

In the example above, the Condorcet winner is Pizza Palace, but the true compromise is Veg n' Go. If we were to take a majority rule comparison between the two, Pizza Palace would win 2-1. But if we simply ask "who is okay with Pizza Palace?" the answer is "only 2 out of 3 people." If we ask "who is okay with Veg n' Go?" the answer is "all 3 people." How is that not the truest consensus option?

| Option        | Approval Count |
|---------------|----------------|
| Veg n' Go     | 3 (100%)       |
| Pizza Palace  | 2 (66.7%)      |
| Burger Barn   | 0 (0%)         |

It sure looks like we found the Compromise candidate, even if we know that underneath this data Pizza Palace would have defeated Veg n' Go in a head-to-head matchup. But everyone is happy with the outcome, and is that not the point of compromise?

Majority rule and ordinal preferences are a decent option when we have a very large group of voters, especially if no single option is going to make a majority of voters happy. But equating majority rule with compromise is a complete fallacy.

I have [previously argued](../condorcet-approval/){:target="_blank"} that if you collect ordinal data, then the Condorcet winner is the only candidate for which it makes sense to elect. Because without that intensity, all we can gather from ordinal preferences is that if we move from a non-Condorcet winner to the Condorcet winner, then a majority of voters will be happier. But that doesn't mean the entire electorate will be happier overall.

Moving from Veg n' Go to Pizza Palace would make 2 voters happier, objectively. And only one voter would be less happy. But the marginal increase in happiness for the two pizza lovers is extremely small, and the loss of happiness for the vegan is extremely large. And, I don't know about you, but watching my friend starve to death while two of us eat pizza is not going to make me feel like we found a compromise.

Electing candidates is not the same as picking a restaurant for dinner, but the logic is the same. Even if my preference is Pizza Palace over Veg n' Go, I want to be able to signal that I would be satisfied either way, and I'd rather more people be happy with the outcome than being forced to make a choice between which two options I prefer. Even if Veg n' Go is only 40% as good as Pizza Palace to me, I might still be willing to eat there if it means that everyone is happy with the outcome.

I am thus left with two propositions:

1. The Condorcet winner is not the true compromise candidate in all cases, and it is a fallacy to equate majority rule, or ordinal preferences, with compromise.
2. If we do not elect the Condorcet winner, when one exists in the ballot data, then we destroy the legitimacy of the election by electing a candidate that a majority of voters prefer less than another candidate.

Fortunately for me, there is a simple solution: Approval voting.

> Approval voting is a voting system where voters can approve of as many candidates as they like, and the candidate with the most approvals wins.

In Approval voting, I do not have to express that I *technically* prefer Pizza Palace to Veg n' Go, and I can instead express that I would be satisfied with either outcome. And if a consensus option like Veg n' Go racks up approvals from all voters, then it will win without anyone being any the wiser about the fact that there was a polarizing Condorcet winner that would have left the overall group less happy.

For you see, [approval is actually, provably, a two-tiered Condorcet method which never runs into a paradox where no Condorcet winner exists](../condorcet-approval/){:target="_blank"}. The Approval winner is always the Condorcet winner *induced by the ballot data*. But it is not beholden to pick the true ranked Condorcet winner if that candidate is less acceptable to the electorate than another candidate.

Approval, therefore, gives us the best of both worlds. It selects the true compromise candidate, while also giving the winner absolute legitimacy by being the Condorcet winner of the ballot data.

Let's scale up this example. Let's say that now we have to satisfy 100 friends instead of just 3. We have the following preferences:

| Number | Ranking       | Approvals |
|--------|---------------|-----------|
| 1      | V > B > P     | V         |
| 60     | P > V > B     | P,V       |
| 39     | B > P > V     | B         |

Unfortunately, now we can't satisfy 100% of voters with any one option. But we can still look at the approvals and the Condorcet winner to see how the two differ.

The Condorcet winner is still Pizza Palace, because 60% of voters put it as their first choice. Additionally, 99% of voters prefer Pizza Palace to Veg n' Go! However, the Approvals tell us a different story.

| Option        | Approval Count |
|---------------|----------------|
| Veg n' Go     | 61 (61%)       |
| Pizza Palace  | 60 (60%)       |
| Burger Barn   | 39 (39%)       |

Every single voter who said they would be happy with Pizza Palace also said they would be happy with Veg n' Go. Additionally, the 39 voters who really want a Burger technically prefer Pizza Palace to Veg n' Go, but did not feel that preference strongly enough to approve of Pizza Palace. Perhaps they hate pizza and vegan food about the same, even if they technically prefer pizza to vegan food. In any case, no voter who actually prefers Pizza Palace to Veg n' Go actually *expressed* that preference in their approvals.

We thus have to make a normative choice here.

1. If we pick Burger Barn, then a supermajority of voters will be unhappy with the outcome. They objectively *did not consent* to that option, *and* it loses via majority rule to both of the other options. This is a non-starter.
2. If we pick Pizza Palace, then we make a supermajority of voters the happiest they could be. However, 40% of voters would be very unhappy with the outcome.
3. If we pick Veg n' Go, then that same supermajority of voters would be just as happy as they would be with Pizza Palace, and one more voter would be extremely happy with the outcome. Only 39% of voters would be unhappy with the outcome, but they would be about equally unhappy with either Pizza Palace or Veg n' Go.

There is no single correct answer here. But objectively more voters would be happier with Veg n' Go than with Pizza Palace, even though if we asked voters to just choose between those two options, Pizza Palace would win by a landslide.

It doesn't feel great to give 39% of voters their least favorite option. And it doesn't feel great to pick an option that makes 99% of voters slightly less happy than if we picked the Condorcet winner. But between the two options, Veg n' Go makes the most voters "happy".
