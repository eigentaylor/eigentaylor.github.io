---
layout: distill
title: Is the Condorcet Winner the True Compromise?
date: 2026-04-12
description: A Condorcet winner may not be a true consensus candidate. Approval voting can find consensus with a simpler ballot.
giscus_comments: true
importance: 3
tags: voting
category: polisci
featured: false
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
---

Three friends are trying to decide on a restaurant for dinner. Two of them really love pizza, but the third is a vegan. The full rankings of the three friends are as follows:

| Number | First Choice | Second Choice | Third Choice |
|--------|--------------|---------------|--------------|
| 2      | Pizza Palace | Veg n' Go     | Burger Barn  |
| 1      | Veg n' Go    | Burger Barn   | Pizza Palace |

The vegan obviously loves the vegan restaurant, and Burger Barn at least *has* vegan options, unlike Pizza Palace, so the vegan prefers Veg n' Go > Burger Barn > Pizza Palace. The two pizza lovers are really craving pizza, and they had burgers for lunch, so they prefer Pizza Palace > Veg n' Go > Burger Barn.

Marquis de Condorcet would decree that the true consensus option is Pizza Palace, because a majority of voters have it as their first choice. Majority rule, after all, is the most fundamental principle of democracy. Or is it?

When I was in grad school, I had a friend who was vegan, and he convinced me to give Veg n' Go a try. I was skeptical at first, but I loved it! It may not be my *first* choice on any given day, but I was always perfectly happy to eat there, despite not being a vegan myself. Its proximity to our office combined with the fact my friend was a vegan made it a great compromise that we went to regularly.

If both pizza lovers find Veg n' Go to be 99% as good as Pizza Palace, then Veg n' Go is a choice that literally 100% of voters would be happy with, while Pizza Palace would make the minority vegan extremely unhappy.

This example highlights my major issue with the Condorcet criterion.

> The *Condorcet winner* is the candidate who would win a head-to-head matchup against every other candidate. A voting system satisfies the *Condorcet criterion* if it always elects the Condorcet winner when one exists.

Many Condorcetists will argue that if you don't elect the Condorcet winner, then you are not electing the true compromise of the electorate. But I think this is a complete fallacy and misunderstanding of what a compromise is.

The Condorcet winner is something defined by *ordinal* preferences. That is, it only looks at a comparison of orderings of candidates by the voters. Why should consensus be defined by ordinal preferences?

When we talk about compromise, or negotiation, or consensus, we don't evaluate things simply by how many people prefer one option to another, or even necessarily by majority rule. We tend to try to find an agreement that allows everyone to leave feeling like they got something out of the deal, even if it wasn't their first choice.

In the example above, the Condorcet winner is Pizza Palace, but the true compromise is Veg n' Go. If we were to take a majority rule comparison between the two, Pizza Palace would win 2-1. But if we simply ask "who is okay with Pizza Palace?" the answer is "only 2 out of 3 people." If we ask "who is okay with Veg n' Go?" the answer is "all 3 people." How is that not the truest consensus option?

| Option        | Approval Count |
|---------------|----------------|
| Veg n' Go     | 3 (100%)       |
| Pizza Palace  | 2 (66.7%)      |
| Burger Barn   | 0 (0%)         |

It sure looks like we found the compromise candidate, even if we know that underneath this data Pizza Palace would have defeated Veg n' Go in a head-to-head matchup. But everyone is happy with the outcome, and is that not the point of compromise?

Majority rule and ordinal preferences are a decent option when we have a very large group of voters, especially if no single option is going to make a majority of voters happy. But equating majority rule with compromise is a complete fallacy.

I have [previously argued](../condorcet-approval/){:target="_blank"} that if you collect ordinal data, then the Condorcet winner is the only candidate for which it makes sense to elect. Because without that intensity, all we can gather from ordinal preferences is that if we move from a non-Condorcet winner to the Condorcet winner, then a majority of voters will be happier. But that doesn't mean the entire electorate will be happier overall.

Moving from Veg n' Go to Pizza Palace would make 2 voters happier, objectively. And only one voter would be less happy. But the marginal increase in happiness for the two pizza lovers is extremely small, and the loss of happiness for the vegan is extremely large. And, I don't know about you, but watching my friend starve to death while two of us eat pizza is not going to make me feel like we found a compromise.

Electing candidates is not the same as picking a restaurant for dinner, but I see no reason to redefine what a "compromise" is. Even if my preference is Pizza Palace over Veg n' Go, I want to be able to signal that I would be satisfied either way. Further, I'd rather more people be happy with the outcome than to be forced to make a choice between which two options I prefer. Even if Veg n' Go is only 40% as good as Pizza Palace to me, I might still be willing to eat there if it means that all of my friends can eat together and be happy.

I am thus left with two propositions:

1. The Condorcet winner is not the true compromise candidate in all cases, and it is a fallacy to equate majority rule, or ordinal preferences, with compromise.
2. If we do not elect a Condorcet winner, then we destroy the legitimacy of the election by electing a candidate who would have lost to someone else in a head-to-head matchup.

Fortunately for me, there is a simple solution: Approval voting.

> Approval voting is a voting system where voters can approve of as many candidates as they like, and the candidate with the most approvals wins.

In Approval voting, I do not have to express that I *technically* prefer Pizza Palace to Veg n' Go. Instead, I can express that I would be satisfied with either outcome. And if a consensus option like Veg n' Go racks up approvals from all voters, then it will win without anyone being any the wiser about the fact that there was a polarizing Condorcet winner that would have left the overall group less happy.

For you see, [approval is actually, provably, a two-tiered Condorcet method which never runs into a paradox where no Condorcet winner exists](../condorcet-approval/){:target="_blank"}. The Approval winner is always the Condorcet winner *induced by the ballot data*. But it is not beholden to pick the true ranked Condorcet winner if that candidate is less acceptable to the electorate than another candidate. To explain why, let's look back the first example with just three voters.

The number of voters who approved of Veg n' Go but not Pizza Palace is 1. The number of voters who approved of Pizza Palace but not Veg n' Go is 0. Therefore, Veg n' Go actually defeats Pizza Palace in a head-to-head matchup of approvals, as two voters declared indifference. Similarly, Veg n' Go also defeats Burger Barn in a head-to-head matchup of approvals three to zero. Therefore, Veg n' Go is the Condorcet winner of the approval data, even though Pizza Palace is the Condorcet winner of the ranked data. This always happens in Approval: the Approval winner is the Condorcet winner of the approval data, but it may not be the Condorcet winner when you consider the ranked data underlying those approvals.

Approval, therefore, gives us the best of both worlds. It can select the true compromise candidate while also giving the winner absolute legitimacy, by being [the Condorcet winner of the ballot data](../consistentcardinal/){:target="_blank"}. It does this without being *beholden* to the ranked Condorcet winner, which may not be the ultimate compromise choice.

Let's scale up this example. Let's say that now we have to satisfy 100 friends instead of just 3. We have the following preferences:

| Number | Ranking       | Approvals |
|--------|---------------|-----------|
| 1      | V > B > P     | V         |
| 60     | P > V > B     | P,V       |
| 39     | B > P > V     | B         |

Unfortunately, now we can't satisfy 100% of voters with any one option. But we can still look at the approvals and the Condorcet winner to see how the two differ.

The Condorcet winner is still Pizza Palace. Because 60% of voters put it as their first choice, it necessarily wins in head-to-head matchups against the other options. Additionally, 99% of voters prefer Pizza Palace to Veg n' Go! However, the Approvals tell us a different story.

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

What breaks the tie for me, however, is [the practical consideration of how we run each election](../approval-only/){:target="_blank"}. It's far easier to run an Approval election than a Condorcet election. We simply ask each voter to raise their hand for each option they would be happy with, and the option with the most raised hands wins. We don't need to collect 100 ballots and then run pairwise comparisons between every candidate to find the Condorcet winner. We can just count approvals and be done with it.

The Condorcet winner and Approval winner generally coincide. However, the [1985 Institute of Management Sciences (TIMS) election](https://www.jstor.org/stable/2632078) is a good example where they potentially didn't. See [this post](../practicalapproval){:target="_blank"} where I discuss it in more detail. In this election, they collected both Approval and Ranked data. The Approval winner won by over a hundred approvals. The supposed Condorcet winner was *inferred* to be strictly preferred over the Approval winner by a single vote (901 to 900 of those who expressed some type of preference), while 27 voters abstained--leaving it very ambiguous. That's not exactly a strong legitimate claim. Approval broke that ambiguity: the Approval winner earned 1,038 approvals to the "Condorcet winner's" 908 approvals.

Would a 901 to 900 majority really give as much legitimacy to the Condorcet winner as the 1,038 to 908 majority that Approval voting gave to its winner? I don't think so. Instead, we can definitively conclude that many of the voters who said they preferred the Condorcet winner to the Approval winner explicitly approved of both candidates. You can have an ordinal preference but still be perfectly happy with either candidate. To pretend this is some sort of impossibility, and that tiny ordinal distances make a non-Condorcet winner somehow "fringe", is to completely misunderstand the nature of compromise and acceptability.

The lesson is simple: majority preference and broad consent are not the same thing, and a voting system should make room for both. Condorcet logic captures pairwise legitimacy, but it can still miss the candidate most people can genuinely live with. Approval voting closes that gap by letting voters signal acceptable outcomes directly, while still preserving a coherent notion of legitimacy in the ballot data. It is easier to run, easier to explain, and often yields the same winner when the Condorcet case is clear, yet it behaves better when preferences are close, ambiguous, or weakly held. If our goal is not just to crown a winner but to produce outcomes people can accept as fair, then [approval voting](../practicalapproval/){:target="_blank"} is the better compromise between mathematical rigor and democratic reality.
