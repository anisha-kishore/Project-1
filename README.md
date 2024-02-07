Results and Written Analysis

This projects attempts to uncover trends among NBA injuries over the past 18 years. 

To start, we looked at the distribution of injuries by body part and injury type. The analysis and clean up code for this data is contained in "Nicole_analysis.ipynb".

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/93694a7f-5b67-425f-af83-aeceb9908667)

As seen on the graph, the most common body parts injured are the ankle, leg, and 
knee, respectively, before a sharp drop off to the third most common injury location. 
Injuries in the lower limbs are by far the most common.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/91874070-96c8-414d-8034-7c2291560c61)

As seen in this graph, the most common injury types are sprains, soreness, and
ilnesses, respectively. The most common injury type seem to be more minor and broad.

Next, we looked at NBA injuries over time. The clean up code for this data is contained in “cpl_data_cleanup.ipynb”. The analysis code is contained in "cpl_analysis.ipynb". As part of the cleanup to ensure that injuries between seasons were independent for the Chi Square analysis, all injuries marked as being from the previous season were removed.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/ce422464-25b0-43a2-ada1-e209c66fea55)

The graph shows the most common injuries per season. Strains start off common before dropping off and being replaced by soreness.
Sprain injuries showed to be a consistent source of injuries across all NBA seasons since 2005 and has trended upward in the recent seasons. This relationship was shown using a Chi-Square analysis between the two variables.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/5ace8d53-b4d4-4e0c-8e44-141046f2f113)

This graph shows the ratio of ilnesses to other injuries by season. There is a definite spike in the 2021-2022 season. 
This could potentially be due to COVID as the restrictions lifted and the "bubble" was no more. A Chi Square analysis was also done here to show evidence of a relationship between the two variables. 

Next, we look at injury location by height and weight. The analysis and clean up code for this data is contained in "analysisfinal-HG.ipynb".

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/6aba0782-9286-4cb7-af62-b6e0955d5109)

This graph shows the most common injuries among players with heights in the middle quartile.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/c73069e2-aea2-46e3-a6ca-422fb608186d)

This graph shows the most common injuries among players with heights in the lower quartile.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/044662a3-27cb-49fd-9c9d-7dbff910d759)

This graph shows the most common injuries among players with heights in the upper quartile.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/cd2b3f6e-eabc-4fed-aba3-a17e9e5ddd61)

This graph shows the most common injuries among players with weights in the middle quartile.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/89d937b4-8827-435a-b598-a7128d3f8fe3)

This graph shows the most common injuries among players with weights in the lower quartile.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/64a17535-d36d-42de-9070-3c731e4a5e6a)

This graph shows the most common injuries among players with weights in the upper quartile. As seen in these graphs and using Pearson correlation tests, the correlation for height with the most common injury (sprain) is very low and not statistically significant. There is no evidence to suggest that a player's height has a noticeable impact on the likelihood of sustaining the most common injury. However, the correlation between weight and sprain injuries, while statistically significant, is very weak.

Next, we examine the relationship between injury and severity, specifically with number of games missed and whether the injury required surgery or not. The analysis and clean up code for this data is contained in "ak_clean_dataset (2).ipynb". 

In this specific dataset, there were two columns that indicated where on the body the injury occurred- a ‘Body Part’ column and a ‘Part Specific’ column. I chose to use the ‘Body Part’ column provided by the dataset in order to group the injuries by on general area (knee, hip, back, etc.). However, these are broad strokes- for example, head injuries can include anything from tooth to eardrum- and do not paint the full picture or breakdown of each injury. Additionally, there is a miscellaneous category where the ‘Body Part’ column was empty. I chose not to change this or group them on my own in order to keep the groups that the data owner provided. Of these empty entries, 4067 entries out of the 4098 total were marked as an illness, and 4059 of those entries had nothing marked in the ‘Part Specific’ column either. However, it is important to note that there were 8 entries that were considered miscellaneous because of the empty ‘Body Part’ column, but did have a body part indicated in the ‘Part Specific’ column. As I chose not to regroup this data, these entries are still grouped into the miscellaneous data row, but it is important to note that it has the potential to change the analysis by body part (ie. 1 entry was attributed to the heart, and 7 entries were considered eye illnesses).

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/a5d5bdc3-cae9-4ee6-bfc1-f1adc10c8f77)

This box shows the number of games missed by body part injured. 

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/bd15dde2-3811-4bd7-91ed-e29103e3acef)

Overall dataset was fairly condensed- when looking at the median days missed (chose median because of the potential for large outliers), skin had the highest median, with an overall median of 4 days missed. However, the injuries attributed to skin were abnormal from the rest of the data because there were only two entries and both had caused at least 3 missed days, which caused the skin median and minimum to be higher than other body parts. This can be seen by the fact that every other body parts’ minimum number of days missed was 0, and the median number of days missed for their entries were either 0 or 1. Without knowing the whole story and therefore being unable to make a definite conclusion, it is fair to assume that overall, most injuries reported do not cause players to miss many games. However, besides six body parts- ear, heel, muscle, side,trunk, and undisclosed which all had both a median and mean of 0 days missed, the average was always higher than the median, which indicates to me that there are some injuries that are forcing players to sit out for a significant portion of the season, which is skewing the average number of missed days. Overall, though, the causes for missed games are fairly condensed. The maximum combined number of days missed (4601) was because ankle injuries, to be followed with miscellaneous, knee, and leg injuries which all caused more than 4,000 missed days. Back, foot, hand, and head injuries also attributed to more than 1,000 missed days each, but besides these 8 categories, every other category had caused less than 1,000 combined days missed since 2005.

![image](https://github.com/anisha-kishore/Project-1/assets/154575922/8a54bd0e-3698-4db7-88a7-718af84fb3c1)

This graph the number of injuries that needed surgery by body part. Although similar body parts were affected with both high days missed and number of surgeries (ankle, leg, knee, hand, foot and head all had at least 60 surgeries required), the proportion of days off by number of surgeries was different, and the spread of the data was very different.  For example, ankle injuries caused the most days missed with 4,601 days, but was not the injury type that required the most number of surgeries- in fact, in came in fifth. However, knee injuries which took the fourth most amount of days off required more surgeries than any other body part, accounting for more than a third of the surgeries since 2005/2006 season (385 surgeries out of the 1,111 overall surgeries). This shows that the number of surgeries and days missed do not necessarily correlate with each other, but, despite the specific order, overall, the same body part injuries are leading to both high numbers of days off and high numbers of surgeries. However, it is important to note that unlike days missed, the surgery count is very skewed towards certain body parts. As mentioned before, knee injuries accounted for 385 surgeries, which is more than triple the number of hand surgeries (123 surgeries), which was the second highest surgery count. These two body parts were the only two that required more than 100 cumulative surgeries, and only ankle, foot, head, leg, shoulder, and wrist (60, 97, 70, 82, 57, and 52 surgeries respectively) required more than 50 cumulative surgeries amongst all NBA injuries. This means that although these players have had bodily injuries everywhere, only some spots have been frequently injured in such a way that surgery is required.

Finally, we take a look at the most common recurring injuries. 

The most common recurring injury among NBA players is an ankle sprain. 
