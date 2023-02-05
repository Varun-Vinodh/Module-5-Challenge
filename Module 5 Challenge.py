#!/usr/bin/env python
# coding: utf-8

# In[42]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np

# Study data files
mouse_metadata_path = "/Users/varunvinodh/Downloads/module_5_starter_code/Pymaceuticals/data/Mouse_metadata.csv"
study_results_path = "/Users/varunvinodh/Downloads/module_5_starter_code/Pymaceuticals/data/Study_results.csv"

# Read the mouse data and the study results
mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)

# Combine the data into a single dataset
pharm_data_complete = pd.merge(mouse_metadata, study_results, how="left")

# Display the data table for preview
pharm_data_complete.head()


# In[43]:


# Checking the number of mice.
mice_count = len(pharm_data_complete["Mouse ID"].unique())
mice_count


# In[44]:


duplicates = pharm_data_complete(["Mouse ID"]).value_counts
duplicates = duplicates[duplicates > 1].index
print(duplicates)


# In[80]:


# Getting the duplicate mice by ID number that shows up for Mouse ID and Timepoint. 
pharm_data_complete.drop_duplicates(subset:=['Mouse ID','Timepoint'], keep=False, inplace = True)
pharm_data_complete


# In[81]:


mice_count = len(pharm_data_complete["Mouse ID"].unique())
mice_count


# In[82]:


# Generate a summary statistics table of mean, median, variance, standard deviation, and SEM of the tumor volume for each regimen

# Use groupby and summary statistical methods to calculate the following properties of each drug regimen: 
# mean, median, variance, standard deviation, and SEM of the tumor volume. 
# Assemble the resulting series into a single summary DataFrame.

mean_vol = pharm_data_complete.groupby('Drug Regimen').mean()["Tumor Volume (mm3)"]
median_vol = pharm_data_complete.groupby('Drug Regimen').median()["Tumor Volume (mm3)"]
var_vol = pharm_data_complete.groupby('Drug Regimen').var()["Tumor Volume (mm3)"]
std_vol = pharm_data_complete.groupby('Drug Regimen').std()["Tumor Volume (mm3)"]
ser_vol = pharm_data_complete.groupby('Drug Regimen').sem()["Tumor Volume (mm3)"]


summary_summary = pd.DataFrame({"Mean Tumor Volume": mean_vol,
                                   "Median Tumor Volume": median_vol,
                                   "Tumor Volume Variance": var_vol,
                                   "Volume Std Dev": std_vol,
                                   "Volume Std Err":ser_vol})

summary_summary


# In[83]:


# Generate a summary statistics table of mean, median, variance, standard deviation, 
# and SEM of the tumor volume for each regimen

# Using the aggregation method, produce the same summary statistics in a single line.

result = pharm_data_complete.groupby('Drug Regimen').agg({'Tumor Volume (mm3)': ['mean', 'median', 'std', 'var', lambda x: np.std(x) / np.sqrt(len(x))]})
result


# In[84]:


# group the data by 'Drug Regimen' and count the number of 'Timepoint' values
grouped_df1 =  pharm_data_complete.groupby(['Drug Regimen'])['Timepoint'].count()

# create the bar plot
grouped_df1.plot.bar(rot=0)


# In[85]:


# group the data by 'Drug Regimen' and count the number of 'Timepoint' values
grouped_df4 = pharm_data_complete.groupby(['Drug Regimen'])['Timepoint'].count().reset_index()

# create the bar plot
grouped_df4.plot.bar(x='Drug Regimen', y='Timepoint', rot=0)

# add title and labels
plt.title("Total number of timepoints for all mice tested for each drug regimen")
plt.xlabel("Drug Regimen")
plt.ylabel("Number of Timepoints")

# show the plot
plt.show()


# In[87]:


# Count the number of occurrences of each gender
gender_counts = pharm_data_complete['Sex'].value_counts()

# Plot the pie chart using the plot method
gender_counts.plot.pie(autopct='%1.1f%%', startangle=90)

# Add title to the plot
title = "Sex"
_ = plt.title(title)

# Display the plot
_ = plt.show()


# In[86]:


# Count the number of occurrences of each gender
female_mice = pharm_data_complete['Sex'].value_counts()['Female']
male_mice = pharm_data_complete['Sex'].value_counts()['Male']

# Pie chart
labels = ['Female', 'Male']
sizes = [female_mice, male_mice]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

# Add title and display the pie chart
ax.set_title("Sex")
plt.show()


# In[ ]:





# In[ ]:




