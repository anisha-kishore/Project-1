Results and Written Analysis

This projects attempts to uncover trends among NBA injuries over the past 18 years. 

To start, we looked at the distribution of injuries by body part and injury type. The analysis code for this data is contained in "Nicole_analysis.ipynb".

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

