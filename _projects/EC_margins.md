---
layout: distill
title: Just how chaotic is the electoral college?
date: 2025-08-13
description: An analysis of how close US elections really are
giscus_comments: true
importance: 3
category:
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: c1
  - name: c2
    subsections:
      - name: c22
---

Let's get POLITICAL! Okay, not really. But sort of. I am actually extremely fascinated by voting systems, elections, and presidents! And lately, I've been quite interested in the science behind elections. One of the primary gripes people have with US elections is the Electoral College. 

Whether or not the electoral college is *good* or *bad* is beyond the scope of this post. But the question I'm here to ask is

# Just how close was a particular election?

How do we define close? Well, we don't pick a president by the popular vote margin, but that's a good place to start! We define 

$$
m_{PV}=\frac{\abs{D_{votes}-R_{votes}}}{D_{votes}+R_{votes}}
$$

This measures the percentage difference in votes that the winning candiate got over the other. The format we will use in this post is D+$x$ or R+$x$ depending on the winner. For example, in 2020, Joseph Biden received 81,283,501 votes to Donald Trump's 74,223,975. 

$$
\frac{\abs{81,283,501-74,223,975}}{81,283,501+74,223,975}
\approx D+4.5
$$

Biden won by over 7 million votes, and over $4.5\%$. This is, in fact, the largest popular vote margin since Obama's 2008 landslide. Unlike the latter, however, Biden was frighteningly close to losing the election to the electoral college. How close? Well, unlike the popular vote, which would have required over 3.5 million Biden voters to have chosen Donald Trump instead, merely 32 thousand would have needed to change their vote to give Donald Trump a second electoral college victory, and about 22 thousand to achieve an electoral college tie.

Specifically, 5,229 votes in Arizona (0.157% of the vote in that state), 5,890 in Georgia (0.119% of the vote in that state), 10,342 in Wisconsin (0.319% of the vote in that state) and the electoral college total would be 269-269. If 10,819 votes in Nebraska's second district (3.366% of the total) had flipped from Biden to Trump, then the latter would have also won outright with exactly 270 electoral votes. For those keeping track at home that's a mere 32,280 votes across 3 states and one district. In total, that's 0.458% of the popular vote margin and only 0.021% of all votes cast in the whole election. 

To be clear, our formula for how many votes needed to be flipped is

$$
\operatorname{floor}\left(\frac{\abs{D_{statevotes}-R_{statevotes}}}2\right)+1
$$

The most famous example where this is smallest is the election of 2000. George W. Bush won Florida by 537 votes, which means that if 269 of those voters had put Gore instead of Bush, then Gore would have won the electoral college by a single vote. That's 0.05181% of the popular vote margin (about D+$0.5$), and a mere 0.00027% of the total votes cast that year.

Flipped states: {'ARIZONA': {'EC': 11, 'flipped votes': 5229, '% flipped': 0.157}, 'GEORGIA': {'EC': 16, 'flipped votes': 5890, '% flipped': 0.119}, 'WISCONSIN': {'EC': 10, 'flipped votes': 10342, '% flipped': 0.319}, 'NE-02': {'EC': 1, 'flipped votes': 10819, '% flipped': 3.366}}
Total number of flipped votes: 32280 across 4 states, Ratio to Popular Vote Margin: 0.45769%, Ratio to Total Votes in Year: 0.02076%
New Winner: Donald J. Trump (R) with 270 electoral votes vs Joseph R. Biden (D) with 268 electoral votes




[hyperlink](../eigentricks/){:target="_blank"}
