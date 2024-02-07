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

