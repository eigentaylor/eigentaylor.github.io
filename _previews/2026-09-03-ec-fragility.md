---
layout: distill
title: 'How Close? A History of Fragile Presidential Elections'
date: 2026-09-03
description: Analyzing the most fragile presidential elections since 1864, and how consistently close to breaking the electoral college has truly been.
importance: 2
tags: presidents
category: polisci
featured: false
theorems: false
bibliography: voting.bib
chart:
  plotly: true
images:
  photoswipe: true
jupyter_notebook_crawlable_text: false
authors:  
  - name: Taylor Eigen Fisher
    url: ""
    affiliations:
      name: Equal Vote Coalition (Volunteer)
toc:
  - name: Introduction
    subsections:
      - name: "2000 and 2004"
      - name: Methodology
  - name: "1876"
  - name: The 1880s
  - name: "1916"
  - name: "1948"
  - name: "1960"
  - name: "1976"
  - name: "2016"
  - name: "2020"
  - name: An Honorable Mention of 2024
  - name: Conclusion
---

## Introduction

I have long been a nerd for presidential elections. I just find them super interesting! The Electoral College is one of the most fascinating terrible things we have.

I know, it's a brave opinion to stand up and say, "we should just elect the winner of the national popular vote". Especially when people have elections like 2000 and 2016 at the front of their minds. But I don't know if many people appreciate just how close the Electoral College has been to breaking beyond the times it actually *did*.

For those who do not know how the Electoral College actually works, let's go through it quickly. Voters do not vote directly for president, but rather for who their state will give its electoral votes to. With two exceptions, the candidate who gets the most votes in a state gets every single electoral college vote that state has. Even though George Bush only won Florida by 537 votes in 2000, he received all 25 electoral votes from the state, which resulted in his election.

Nebraska and Maine are two exceptions, who give the overall winner in the state two votes, but give the winner in each district one electoral vote each. Thus, even though Republicans have recently won Nebraska by a landslide, it's second district is a blue dot that often somewhat narrowly votes for Democrats. That means that Nebraska's five electoral votes often split with four going to Republicans and one going for Democrats. Maine similarly has a maverick second district which has recently been giving its electoral vote to Donald Trump in the last three elections.

The candidate who wins a majority of all electoral votes is elected president. Today, that is 270 of the total 538. Each state gets one electoral vote per congressional district, plus two from its senate seats, which makes the electoral power of states fairly unproportional. If no candidate receives a majority, which has happened once in 1824, it goes to the House of Representatives, which is a mess that everyone would rather avoid.

### 2000 and 2004

When people think "close election", I would wager that the first election that most often comes to mind is the 2000 election. This race was decided entirely by a highly contested Florida recount. The final certified results had Bush winning by 537 votes, though many have argued that Gore was the rightful winner due to "hanging chads" and the confusing "butterfly ballots", as well as the fact that Ralph Nader may have siphoned off crucial votes. The final result was Bush winning the election, despite the fact that Gore had won the popular vote by over 500,000 votes! This was an exceptionally narrow popular vote margin of roughly 0.5%. I give this election a 5/5 closeness rating!

<div class="pswp-gallery mt-3" id="2000-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/2000Bush.jpg"
     data-pswp-width="1425"
     data-pswp-height="1900"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2000Bush.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="George W. Bush portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/2000Gore.png"
     data-pswp-width="1200"
     data-pswp-height="1600"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2000Gore.png" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Al Gore portrait" />
  </a>
</div>
<div class="caption mt-2">
  George W. Bush (R), the 43rd President of the United States, who served from 2001 to 2009, and Al Gore (D), the 45th Vice President of the United States, who was the Democratic candidate in the 2000 presidential election.
</div>

<div class="pswp-gallery mt-3" id="2000-animation">
  <a href="/assets/img/pres_flips/2000_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/2000_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 2000 election classic votes" />
  </a>
</div>
<div class="caption mt-2">
  Animation of the 2000 election flip.
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="2000" %}

The 2004 election, by contrast, was not nearly as close in the popular vote, with George W. Bush defeating John Kerry by about 3 million votes, or roughly 2.5%. But that is misleading because it would not actually be that hard to destroy Bush's majority by flipping roughly 19,000 votes across three states: Nevada, New Mexico, and Iowa. This would leave the election as a 269-269 split, sending the decision to the House of Representatives once again. However, Bush would have likely won this anyway. To get Kerry across the finish line, you either have to flip about 60,000 votes in Ohio, or also flip Nebraska's second district, which Bush won by over 20 points. This election gets a 2/5 closeness rating from me.

<div class="pswp-gallery mt-3" id="2004-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/2004Bush.jpg"
     data-pswp-width="1968"
     data-pswp-height="2489"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2004Bush.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="George W. Bush portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/2004Kerry.jpg"
     data-pswp-width="1859"
     data-pswp-height="2649"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2004Kerry.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="John Kerry portrait" />
  </a>
</div>
<div class="caption mt-2">
  George W. Bush (R), the 43rd President of the United States, who served from 2001 to 2009, and John Kerry (D), the junior U.S. Senator from Massachusetts, who was the Democratic candidate in the 2004 presidential election.
</div>

<style>
.flip-swipe-gallery {
  display: flex;
  gap: 0.75rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
  padding-bottom: 0.25rem;
  scrollbar-width: thin;
}
.flip-swipe-gallery a {
  flex: 0 0 100%;
  scroll-snap-align: start;
  scroll-snap-stop: always;
}
.flip-swipe-gallery img {
  width: 100%;
  display: block;
}
</style>

<div class="pswp-gallery flip-swipe-gallery mt-3" id="2004-animation">
  <a href="/assets/img/pres_flips/2004_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/2004_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 2004 election classic votes: the minimum flip needed to hand Kerry the win outright" />
  </a>
  <a href="/assets/img/pres_flips/2004_no_majority_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/2004_no_majority_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 2004 election no-majority votes: the minimum flip needed to strip Bush of a majority" />
  </a>
</div>
<div class="caption mt-2">
  Swipe to compare: the minimum flip needed to hand Kerry the win outright (left) vs. the minimum votes needed to strip Bush of a majority and send the election to the House (right).
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="2004" %}

These two elections provide an interesting contrast. 2000 was very clearly close, while 2004 was not particularly close in the popular vote, but still "fragile" in terms of the Electoral College. I would not call this election "close", however. But just looking at the Wikipedia page for the 2004 election, would not make it obvious how precarious Bush's victory actually was. The question we have to ask is "how many other elections were similarly fragile despite not necessarily appearing close in the popular vote?"

We will look back at the elections since the Civil war 1864, partially because that's when the modern two-party system began to solidify, and also because that's where my data set ends. I may do a follow up analysis for earlier elections some other time.

### Methodology

I ran a knapsack algorithm to determine the minimum number of votes that would need to be flipped across states to change the outcome of the Electoral College, effectively identifying the "fragility" of each election. For example, Florida went to Bush by 537 votes, so flipping 269 votes from Bush to Gore would result in Gore winning by a single vote. This approach allows us to quantify how "fragile" an election was, even if the popular vote margin was relatively large. You can imagine fragility as how difficult it would be to dig into the ballots, change one name to another, and thereby alter the outcome of the election.

## 1876

<div class="pswp-gallery mt-3" id="1876-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/1876Hayes.jpg"
     data-pswp-width="1980"
     data-pswp-height="2636"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1876Hayes.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Rutherford B. Hayes portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/1876Tilden.jpg"
     data-pswp-width="275"
     data-pswp-height="366"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1876Tilden.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Samuel Tilden portrait" />
  </a>
</div>
<div class="caption mt-2">
  Rutherford B. Hayes (R), the 19th President of the United States, who served from 1877 to 1881 and Samuel Tilden (D), the 25th Governor of New York, who was the Democratic candidate in the 1876 presidential election.
</div>

The 1876 election was one of the most disputed and controversial elections in American history. Rutherford B. Hayes, was only elected by overcoming all of the contested electoral votes in several states. Four states were involved in the dispute, including South Carolina. In the end, Hayes win with the exact number of electoral votes needed to secure the presidency, 185 out of 369, and Samuel Tilden, his opponent, received 184 electoral votes. Even though Tilden won the national popular vote by 3% he still lost the election due to the distribution of electoral votes.

South Carolina was the closest of the states, being flippable by roughly 500 votes. Hayes likely won this state, despite being the home of the Confederacy because of votes by newly freed slaves who were largely supportive of the Republican Party at the time, and had their right to vote protected by federal troops. This election resulted in the end of Reconstruction, which marked the withdrawal of federal troops from the South and the beginning of the Jim Crow era. This was thus the last time that South Carolina voted for a Republican for **88 years**, until it voted against Lyndon B. Johnson in 1964 because of the national Democratic Party's support for civil rights legislation.

The most shocking fact about this election I found is that even if you give Hayes all of the contested electoral votes, Tilden would have **still won** if the apportionment of electoral votes had been **done correctly by the legislated rules at the time** <d-cite key="neubauer2012unpopular"></d-cite>.

This is an easy 5/5 closeness rating. Tilden was so absurdly close to winning, just like Al Gore.

<div class="pswp-gallery mt-3" id="1876-animation">
  <a href="/assets/img/pres_flips/1876_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1876_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1876 election classic votes" />
  </a>
</div>
<div class="caption mt-2">
  Animation of the 1876 election flip.
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="1876" %}

## The 1880s

1876 wasn't the end of highly close elections in the later decades of the 19th century. In fact, all three subsequent presidential elections in the 1880s were also absurdly close and fraught with controversy. The most interesting aspect of these elections is that all three were decided by New York. New York was the largest state, and also frighteningly a swing state.

1880 had potentially the closest national popular vote in American history up to that point. Sources give the margin as between roughly 2,000 and 10,000 votes (approximately 0.1%).

I give this a 3/5 closeness rating. It's close, but you need to either flip a lot of states, or flip a significant number of votes in New York.

<div class="pswp-gallery mt-3" id="1880-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/1880Garfield.jpg"
     data-pswp-width="2250"
     data-pswp-height="2999"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1880Garfield.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="James A. Garfield portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/1880Hancock.jpg"
     data-pswp-width="2537"
     data-pswp-height="3333"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1880Hancock.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Winfield Scott Hancock portrait" />
  </a>
</div>
<div class="caption mt-2">
  James A. Garfield (R), the 20th President of the United States, who served from March to September 1881, and Winfield Scott Hancock (D), the Democratic candidate in the 1880 presidential election.
</div>

<div class="pswp-gallery mt-3" id="1880-animation">
  <a href="/assets/img/pres_flips/1880_classic_margin.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1880_classic_margin.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1880 election classic margin" />
  </a>
</div>
<div class="caption mt-2">
  Animation of the 1880 election flip.
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="1880" %}

Most think of the 1888 election as the most controversial because Grover Cleveland won the popular vote but lost the electoral vote to Benjamin Harrison, being the last time this would happen until 2000. However, 1884 was *significantly* closer electorally. Cleveland won New York by only about 1,000 votes. Flipping under 600 votes from Cleveland to Blaine and Cleveland would not have been elected. I give 1884 a 4.5/5 closeness rating.

<div class="pswp-gallery mt-3" id="1884-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/1884Cleveland.jpg"
     data-pswp-width="542"
     data-pswp-height="723"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1884Cleveland.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Grover Cleveland portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/1884Blaine.jpg"
     data-pswp-width="2026"
     data-pswp-height="2538"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1884Blaine.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="James G. Blaine portrait" />
  </a>
</div>
<div class="caption mt-2">
  Grover Cleveland (D), the 22nd and 24th President of the United States, who served from 1885 to 1889 and 1893 to 1897, and James G. Blaine (R), the Republican candidate in the 1884 presidential election.
</div>

<div class="pswp-gallery mt-3" id="1884-animation">
  <a href="/assets/img/pres_flips/1884_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1884_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1884 election classic votes" />
  </a>
</div>
<div class="caption mt-2">
  Animation of the 1884 election flip.
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="1884" %}

New York gave Cleveland the presidency, but then it took it away in 1888. Funny enough, the percent of votes you need to flip this election is actually relatively high, especially compared to 1884. 1888 gets a 3/5 closeness rating.

<div class="pswp-gallery mt-3" id="1888-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/1888Harrison.jpg"
     data-pswp-width="1509"
     data-pswp-height="2012"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1888Harrison.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Benjamin Harrison portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/1884Cleveland.jpg"
     data-pswp-width="542"
     data-pswp-height="723"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1884Cleveland.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Grover Cleveland portrait" />
  </a>
</div>
<div class="caption mt-2">
  Benjamin Harrison (R), the 23rd President of the United States, who served from 1889 to 1893, and Grover Cleveland (D), the incumbent president who narrowly lost his re-election bid in the 1888 presidential election.
</div>

<div class="pswp-gallery mt-3" id="1888-animation">
  <a href="/assets/img/pres_flips/1888_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1888_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1888 election classic votes" />
  </a>
</div>
<div class="caption mt-2">
  Animation of the 1888 election flip.
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="1888" %}

## 1916

<div class="pswp-gallery mt-3" id="1916-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
 <a href="/assets/img/pres_flips/portraits/1916Wilson.jpg"
     data-pswp-width="2166"
     data-pswp-height="2887"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1916Wilson.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Woodrow Wilson portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/1916Hughes.jpg"
     data-pswp-width="4567"
     data-pswp-height="6395"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1916Hughes.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Charles Evans Hughes portrait" />
  </a>
</div>
<div class="caption mt-2">
  Woodrow Wilson (D), the 28th President of the United States, who served from 1913 to 1921 and Charles Evans Hughes (R), the losing candidate in the 1916 presidential election.
</div>

A common theme of this post is that we'll have a sort of cluster of close elections with long gaps of relatively uncontroversial ones in between. After Cleveland won back the presidency in 1892, Republicans dominated the electoral college for nearly the next two decades, until Woodrow Wilson "squeaked" in a landslide victory in 1912 when Teddy Roosevelt's third-party run split the Republican vote.

Wilson then was only narrowly reelected in 1916, defeating Charles Evans Hughes by a very slim margin in both the popular and electoral votes. The election was decided entirely by California, which went to Wilson by under 4,000 votes. Flipping under 2,000 votes from Wilson to Hughes in California would have given Hughes the presidency. I give the 1916 election a 4.5/5 closeness rating.

Fun fact: While some complain about the Electoral College because of its lack of proportionally, there is actually some evidence that the senate seat bump actually *helps* national popular vote winners because winning the NPV usually involves winning many states <d-cite key="neubauer2012unpopular"></d-cite><d-footnote>How much this applies to modern times, compared to the simulations run in 2012 is debatable. States have become so solidified that a fairly strong NPV victory is not necessarily predictive of winning so many states anymore. Not counting DC, Biden only won 25 states in 2020, and Clinton only 20 states in 2016, despite having strong national popular vote showings.</d-footnote>. Indeed, even if Wilson wins California, removing the two extra electoral votes each state gets from their Senate representation would have caused him to lose! Wilson won 30 states, and if you subtract the 60 extra electoral votes from his total, he would have lost the election despite winning the popular vote with 216 electoral votes out of the now 218 needed.

<div class="pswp-gallery mt-3" id="1916-animation">
  <a href="/assets/img/pres_flips/1916_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1916_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1916 election classic votes" />
  </a>
</div>
<div class="caption mt-2">
  Animation of the 1916 election flip.
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="1916" %}

## 1948

<div class="pswp-gallery mt-3" id="1948-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/1948Truman.jpg"
     data-pswp-width="1947"
     data-pswp-height="2597"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1948Truman.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Harry S. Truman portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/1948Dewey.jpg"
     data-pswp-width="2664"
     data-pswp-height="3550"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1948Dewey.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Thomas E. Dewey portrait" />
  </a>
</div>
<div class="caption mt-2">
  Harry S. Truman (D), the 33rd President of the United States, who served from 1945 to 1953 and Thomas E. Dewey (R), the Republican candidate in the 1948 presidential election.
</div>

1916 was a blip between major landslides. It wasn't until 32 years later in 1948 that we saw another extremely close election. From 1920 to 1944, we had consecutive landslides. Republicans dominated the 1920's, and then FDR won by large margins in 1932, 1936, 1940, and 1944. It wasn't until Truman ran for reelection in 1948 that we found ourselves with another nail-biter.

The 1948 election is a classic and iconic election to discuss. Thomas E. Dewey was running a second time, after losing the 1944 election to Franklin D. Roosevelt. Everyone expected Dewey to win easily, including Truman himself! He went to bed expecting to lose, just as the newspapers had predicted. However, Truman pulled off one of the greatest election upsets in American history, winning both the popular and electoral votes against all expectations. His popular vote victory wasn't narrow either, it was about 4.5% over Dewey. But the electoral college was a different story. California, and Ohio were both extremely close, and flipping both would have destroyed Truman's majority, due to the protesting southern states that had withheld their support from him. Flipping Illinois as well would have given Dewey the win outright.

However, relative to these other close elections, the 1948 election might be considered slightly less fragile. I give it a solid 3/5 closeness rating. It would be exceptionally easy to break the majority here, but giving the win to Dewey could be hard.

<div class="pswp-gallery flip-swipe-gallery mt-3" id="1948-animation">
  <a href="/assets/img/pres_flips/1948_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1948_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1948 election classic votes: the minimum flip needed to hand Dewey the win outright" />
  </a>
  <a href="/assets/img/pres_flips/1948_no_majority_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1948_no_majority_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1948 election no-majority votes: the minimum flip needed to strip Truman of a majority" />
  </a>
</div>
<div class="caption mt-2">
  Swipe to compare: the minimum flip needed to hand Dewey the win outright (left) vs. the minimum votes needed to strip Truman of a majority and send the election to the House (right).
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="1948" %}

## 1960

<div class="pswp-gallery mt-3" id="1960-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/1960Kennedy.jpg"
     data-pswp-width="937"
     data-pswp-height="1317"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1960Kennedy.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="John F. Kennedy portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/1960Nixon.png"
     data-pswp-width="433"
     data-pswp-height="578"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1960Nixon.png" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Richard Nixon portrait" />
  </a>
</div>
<div class="caption mt-2">
  John F. Kennedy (D), the 35th President of the United States, who served from 1961 to 1963 and Richard Nixon (R), the 37th Vice President of the United States, who was the Republican candidate in the 1960 presidential election.
</div>

Eisenhower won his elections in the 50s comfortably, defeating Adlai Stevenson in both 1952 and 1956. However, the 1960 election between John F. Kennedy and Richard Nixon was much closer. We still have no idea who won the popular vote due to the absolutely convoluted insanity of Alabama. The common interpretation of the results gives Kennedy the win by about 0.2%, but it's entirely possible Richard Nixon could be the third candidate, after Andrew Jackson and Grover Cleveland, to win the popular vote three times, but only serve two terms as president due to Electoral College shenanigans.

Relatively speaking, this is a harder election to flip. Hawaii, newly a state, went to Kennedy by just 115 votes, making it the closest state in the election. Flipping Hawaii alone would not have changed the outcome, but flipping Nevada, New Mexico, and Illinois would have potentially broken Kennedy's majority, depending on what Alabama would do in response (Alabama could have easily given Kennedy three of its unpledged electors which would have maintained his majority). But flipping Missouri as well gives Nixon a clear path to victory, assuming the other states remain as they were. Due to this ambiguity, and Kennedy's relatively spread out support across the country, I would rate the closeness of the 1960 election as 3/5.

<div class="pswp-gallery flip-swipe-gallery mt-3" id="1960-animation">
  <a href="/assets/img/pres_flips/1960_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1960_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1960 election classic votes: the minimum flip needed to hand Nixon the win outright" />
  </a>
  <a href="/assets/img/pres_flips/1960_no_majority_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1960_no_majority_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1960 election no-majority votes: the minimum flip needed to strip Kennedy of a majority" />
  </a>
</div>
<div class="caption mt-2">
  Swipe to compare: the minimum flip needed to hand Nixon the win outright (left) vs. the minimum votes needed to strip Kennedy of a majority and send the election to the House (right).
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="1960" %}

## 1976

<div class="pswp-gallery mt-3" id="1976-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/1976Carter.jpg"
     data-pswp-width="1805"
     data-pswp-height="2408"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1976Carter.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Jimmy Carter portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/1976Ford.jpg"
     data-pswp-width="1125"
     data-pswp-height="1501"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/1976Ford.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Gerald Ford portrait" />
  </a>
</div>
<div class="caption mt-2">
  Jimmy Carter (D), the 39th President of the United States, who served from 1977 to 1981 and Gerald Ford (R), the 38th President of the United States, who was the Republican candidate in the 1976 presidential election.
</div>

Fun fact, from 1960 to 1976, every presidential election had a national popular vote swing of over 20 percentage points. Carter's victory in 1976 is a blip in many ways. A single democratic victory amidst 5 Republican wins, sandwiched between Richard Nixon and Ronald Reagan, who had legendary reelection landslides. One may be surprised that the near-miss of 1968 is not being focused on, but Nixon actually won most of his states quite decisively, compared to the other elections, so I would only give it a 1/5 closeness.

Despite Watergate, Carter almost didn't win the election. Losing the entire western United States, and instead flipping the south back to the Democrats, Carter's modest 2.1% popular vote margin hides how close he was to losing the electoral college.

Flipping under 10,000 votes in Ohio and Hawaii would have given Ford exactly 270 electoral votes, securing a narrow victory in the 1976 presidential election. Hawaii wasn't particularly close by percentage, but the raw vote margin was small enough to make it the optimal flip alongside Ohio. Wisconsin was narrower in percentage terms than Hawaii, but the raw vote margin was larger, making it a less optimal flip.

This election gets a 4/5 closeness rating.

<div class="pswp-gallery mt-3" id="1976-animation">
  <a href="/assets/img/pres_flips/1976_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/1976_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 1976 election classic votes" />
  </a>
</div>
<div class="caption mt-2">
  Animation of the 1976 election flip.
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="1976" %}

## 2016

There wasn't a close election after 1976 until the previously discussed 2000 and 2004 elections. Barack Obama won both of his elections by comfortable margins, but the same cannot be said about the 2016 election, where Donald Trump won the Electoral College despite losing the popular vote.

<div class="pswp-gallery mt-3" id="2016-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/2016Clinton.jpg"
     data-pswp-width="704"
     data-pswp-height="976"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2016Clinton.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Hillary Clinton portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/2016Trump.jpg"
     data-pswp-width="1520"
     data-pswp-height="2096"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2016Trump.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Donald Trump portrait" />
  </a>
</div>
<div class="caption mt-2">
  Hillary Clinton (D), the Democratic candidate in the 2016 presidential election, and Donald Trump (R), the 45th and 47th President of the United States, who served from 2017 to 2021, and now 2025 to present.
</div>

This is another highly scrutinized election. Despite Clinton's 2.1% popular vote margin, Trump was able to secure a victory in the Electoral College by breaking the "blue wall". Wisconsin, Michigan, and Pennsylvania, which had reliably voted Democratic for over 20 years, flipped to the Republicans by under a percentage point each. Under 40,000 votes would need to be flipped across these states to give the victory to Clinton.

This election gets a 4/5 closeness rating.

<div class="pswp-gallery flip-swipe-gallery mt-3" id="2016-animation">
  <a href="/assets/img/pres_flips/2016_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/2016_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 2016 election classic votes: the minimum flip needed to hand Clinton the win outright" />
  </a>
  <a href="/assets/img/pres_flips/2016_no_majority_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/2016_no_majority_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 2016 election no-majority votes: the minimum flip needed to strip Trump of a majority" />
  </a>
</div>
<div class="caption mt-2">
  Swipe to compare: the minimum flip needed to hand Clinton the win outright (left) vs. the minimum votes needed to strip Trump of a majority and send the election to the House (right).
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="2016" %}

## 2020

<div class="pswp-gallery mt-3" id="2020-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/2020Biden.jpg"
     data-pswp-width="1491"
     data-pswp-height="1988"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2020Biden.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Joe Biden portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/2016Trump.jpg"
     data-pswp-width="1520"
     data-pswp-height="2096"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2016Trump.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Donald Trump portrait" />
  </a>
</div>
<div class="caption mt-2">
  Joe Biden (D), the Democratic candidate in the 2020 presidential election, and Donald Trump (R), the 45th and 47th President of the United States, who served from 2017 to 2021, and now 2025 to present.
</div>

Possibly the most controversial election in recent memory. The race was far closer than many anticipated, with Biden narrowly winning the electoral college despite his popular vote margin being the second largest in the 21st century.

Flipping roughly 22,000 votes across Arizona, Wisconsin, and Georgia would have resulted in an electoral college tie, that Trump potentially wins. Flipping about 10,000 more votes in Nebraska's 2nd congressional district would have given Trump an exact 270 electoral college vote victory.

This election also gets a 4/5 closeness rating.

<div class="pswp-gallery flip-swipe-gallery mt-3" id="2020-animation">
  <a href="/assets/img/pres_flips/2020_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/2020_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 2020 election classic votes: the minimum flip needed to hand Trump the win outright" />
  </a>
  <a href="/assets/img/pres_flips/2020_no_majority_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/2020_no_majority_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 2020 election no-majority votes: the minimum flip needed to strip Biden of a majority" />
  </a>
</div>
<div class="caption mt-2">
  Swipe to compare: the minimum flip needed to hand Trump the win outright (left) vs. the minimum votes needed to strip Biden of a majority and send the election to the House (right).
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="2020" %}

## An Honorable Mention of 2024

<div class="pswp-gallery mt-3" id="2024-election" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem;">
  <a href="/assets/img/pres_flips/portraits/2024Trump.jpg"
     data-pswp-width="1594"
     data-pswp-height="2048"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2024Trump.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Donald Trump portrait" />
  </a>
  <a href="/assets/img/pres_flips/portraits/2024Harris.jpg"
     data-pswp-width="1537"
     data-pswp-height="2051"
     target="_blank">
    <img src="/assets/img/pres_flips/portraits/2024Harris.jpg" class="img-fluid rounded z-depth-1" style="height: 400px; width: 100%; object-fit: cover; object-position: top;" alt="Kamala Harris portrait" />
  </a>
</div>
<div class="caption mt-2">
  Donald Trump (R), the 45th and 47th President of the United States, who served from 2017 to 2021, and now 2025 to present, and Kamala Harris (D), the former Vice President of the United States, who served from 2021 to 2025.
</div>

Relative to the absurdly close elections of 2016 and 2020, 2024 was relatively decisive in interesting ways. Since 1964, Trump's 1.5% popular vote margin is the third weakest, above Nixon's R+0.7 1968 and Gore's D+0.5 2000. A margin under 2% is exceptionally narrow in the context of modern presidential elections. And yet, only one state was within 1 percentage point: Wisconsin with an R+0.9 margin. To flip the election to Kamala Harris, you need over 100,000 votes, which is far above 2004, 2016, and 2020.

Similar to 1968, where a narrow popular vote margin masks fairly significant state-level swings, the 2024 election gets a 1/5 closeness rating from me.

<div class="pswp-gallery mt-3" id="2024-animation">
  <a href="/assets/img/pres_flips/2024_classic_votes.gif"
     data-pswp-width="1080"
     data-pswp-height="742"
     target="_blank">
    <img src="/assets/img/pres_flips/2024_classic_votes.gif" class="img-fluid rounded z-depth-1" alt="Animation of the 2024 election classic votes" />
  </a>
</div>
<div class="caption mt-2">
  Animation of the 2024 election flip.
</div>

{% jupyter_cell_embed "assets/jupyter/flip_scenarios.ipynb" tag="2024" %}

## Conclusion

Hopefully, this post gives a bit of a better perspective of how fragile the electoral college truly is. And maybe a fun perspective of some of these presidential elections, which live in *my* head rent free.

Overall, the fragility of these elections to very small shifts in the vote of just a handful of states highlights the precarious nature of the electoral college system. This post isn't really focused on the arguments of why or why not to keep the electoral college, but hopefully it exposes that it's not *just* the five elections that the electoral college has nearly defied the will of the voters. 

Further, it's not like the problems of the electoral college "went away" for the 112 years between 1888 and 2000. As we have seen, America had been cruisin' for a bruisin' for a number of elections throughout the 20th century. With states becoming more and more solidified in their partisan leanings, causing the utter collapse of the number of swing states down to just 7 states expected to be in play for 2028, we find that elections are now decided entirely by the voters in a very small number of states.

One thing I think is worth noting is that the system as it is today is not at all what the founding fathers envisioned. The original design was to intentionally subvert the direct will of the people, with the electors having the ultimate authority to choose the president, rather than being bound by the will of those in their states. Now, we have a zombie abomination where small vote changes have massive outcomes on the final result.

One aspect of these elections I did not talk about is electoral college "alignment", which I want to discuss in-depth in a future post. There are signs that the electoral college may be less of a problem in 2028 than it has been in recent years, but it is far too early to say that with any confidence. In general, there is really no robust justification to keep this antiquated system in place. Would it not be easier to just elect the president like *every other statewide office in the federal government*? Most votes wins.
