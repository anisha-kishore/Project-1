#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Websites I used to help clean up
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html
#https://www.statology.org/pandas-combine-two-columns/
#https://www.geeksforgeeks.org/replace-nan-with-blank-or-empty-string-in-pandas/
#https://www.geeksforgeeks.org/how-to-convert-integers-to-floats-in-pandas-dataframe/
#https://saturncloud.io/blog/how-to-sum-two-columns-in-a-pandas-dataframe/


# In[2]:


#import libraries
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#read file
injury_file = Path("injury_data.csv")
injury_df = pd.read_csv(injury_file)


# In[4]:


#make a copy 
ak_injury_df=injury_df.copy()


# In[5]:


#Adding relevant columns and removing non-relevant columns
ak_injury_df=ak_injury_df.drop(['Height', 'Weight'], axis=1)
ak_injury_df['Total Days Missed']= ak_injury_df['Total Playoff Games Missed']+ak_injury_df['Total  Regular Season Games Missed']
ak_injury_df['Total Regular Season Games Missed']= ak_injury_df['Total  Regular Season Games Missed']


# In[6]:


#cleaning up data frame for easy reading/easy analysis
ak_injury_df = ak_injury_df[['Playerid', 'Season', 'Part Specific', 'Injury Type', 'Surgery?', 'Time of Year', 'Total Regular Season Games Missed', 'Total Playoff Games Missed', 'Body Part', 'Side', 'Total Days Missed']].fillna('')
ak_injury_df=ak_injury_df[['Playerid', 'Season', 'Side', 'Body Part', 'Part Specific', 'Injury Type', 'Surgery?', 'Time of Year', 'Total Regular Season Games Missed', 'Total Playoff Games Missed', 'Total Days Missed']]
ak_injury_df['Total Playoff Games Missed'] = ak_injury_df['Total Playoff Games Missed'].astype(float) 
ak_injury_df['Total Regular Season Games Missed'] = pd.to_numeric(ak_injury_df['Total Regular Season Games Missed'], errors='coerce')
ak_injury_df['Total Days Missed']=pd.to_numeric(ak_injury_df['Total Days Missed'], errors= 'coerce')

#There is one spasm that was marked blank for if they got surgery- I replaced it with a No (DATA ASSUMPTION)
ak_injury_df['Surgery?'] = ak_injury_df['Surgery?'].replace({'No ': 'No'})

ak_injury_df.head()


# Injured Body Parts vs. Number of Days Missed

# In[7]:


#Days Missed Based on Body Part
ak_body_part_days_missed_counts=ak_injury_df.groupby('Body Part')['Total Days Missed'].count()
ak_body_part_days_missed_max=ak_injury_df.groupby('Body Part')['Total Days Missed'].max()
ak_body_part_days_missed_min=ak_injury_df.groupby('Body Part')['Total Days Missed'].min()
ak_body_part_days_missed_mean=ak_injury_df.groupby('Body Part')['Total Days Missed'].mean()
ak_body_part_days_missed_median=ak_injury_df.groupby('Body Part')['Total Days Missed'].median()

ak_body_part_summary=pd.DataFrame({"Count": ak_body_part_days_missed_counts,
                                   "Minimum": ak_body_part_days_missed_min,
                                   "Maximum": ak_body_part_days_missed_max,
                                   "Mean": ak_body_part_days_missed_mean,
                                   "Median": ak_body_part_days_missed_median
                                  })

ak_body_part_summary.style.highlight_max()


# In[8]:


###Injury Part by Number of Games Missed

#How to make multiple boxplots
fig, ax = plt.subplots(figsize=(25, 10))

sns.boxplot(x = 'Body Part', 
            y = 'Total Days Missed', 
            data = ak_injury_df)

ax.set_xlabel('Body Part')
ax.set_ylabel('Count')
ax.set_title('Boxplots of Games Missed by Body Part Injured')


# Injuried Body Part vs. Number of Surgeries

# In[9]:


#Days Missed Based on Body Part
ak_surgery_days_missed_counts=ak_injury_df.groupby('Body Part')['Surgery?'].value_counts()

#DataFrame from ChatGPT
ak_injury_df.pivot_table(index = 'Body Part', 
                   columns = 'Surgery?', 
                   values = 'Total Days Missed', 
                   aggfunc = ['count', 'max', 'min', 'median', 'mean']).style.highlight_max()


# In[10]:


fig, ax = plt.subplots(figsize=(10, 10))


sns.countplot(y = 'Body Part', 
              hue = 'Surgery?', 
              data = ak_injury_df)

sns.set_palette("bright")
ax.set_ylabel('Body Part')
ax.set_xlabel('Count')
ax.set_title('Number of Surgeries by Body Part')

