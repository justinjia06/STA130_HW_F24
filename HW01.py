#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)


# In[3]:


num_rows, num_columns = df.shape
print(f"The dataset has {num_rows} rows and {num_columns} columns.")


# Observations vs Variables:
# 
# Observations - rows, they are individual entries in the dataset
# Variables - different characteristics for the data recorded for each observation

# In[4]:


print("Summary of Numerical Columns:")
print(df.describe())


# In[5]:


categorical_columns = ['species', 'gender', 'personality']

# Print value counts for each categorical column
for column in categorical_columns:
    print(f"\nValue Counts for '{column}':")
    print(df[column].value_counts())


# Discrepancies between size of the dataset given by df.shape and what is reported by df.describe() with respect to:
# 
# (a) the number of columns it analyzes
# 
# df.shape -> analyzes both categorical columns and numerical columns
# df.describe() -> only analyzes numerical columns, not categorical columns
# 
# (b) the values it reports in the "count" column
# 
# df.shape -> includes all entries
# df.describe() -> doesn't include null entries, so if a column has missing values, the count will be less than the total number of rows
# 

# The difference between an attribute and a method:
# 
# attribute -> They provide information about the object
# 
# method -> They perform operations and computations on the object and they often return some kind of result

# Summary of the session:
# 
# Dataset Analysis
# Checking for Missing Values:
# 
# To check for missing values in a dataset, use df.isna().sum() to see the number of missing values in each column.
# Understanding Dataset Size:
# 
# Use df.shape to get the dimensions of the dataset, which provides the number of rows and columns.
# Summary of Columns:
# 
# Use df.describe() to get statistical summaries for numerical columns, including count, mean, standard deviation, min, max, and percentiles.
# Use df['column'].value_counts() to get counts of unique values for categorical columns.
# Terminology
# Observations:
# 
# Rows in the dataset; each row represents an individual entry or data point.
# Variables:
# 
# Columns in the dataset; each column represents a different characteristic or attribute of the observations.
# Discrepancies Between df.shape and df.describe()
# Number of Columns Analyzed:
# 
# df.shape provides the total number of columns, including both numerical and categorical.
# df.describe() by default summarizes only numerical columns. Categorical columns are not included unless specified.
# Values in the "Count" Column:
# 
# df.shape gives the total number of rows in the dataset.
# df.describe() provides counts of non-null entries for each numerical column. If there are missing values, the count in df.describe() will be less than the total number of rows.
# Attributes vs. Methods
# Attributes:
# 
# Provide direct access to data or properties of an object.
# Syntax: Accessed without parentheses (e.g., df.shape).
# Methods:
# 
# Perform actions or computations and may modify the object or return results.
# Syntax: Called with parentheses (e.g., df.describe()).
# This summary covers how to analyze and interpret datasets, understand different types of dataset properties, and distinguish between attributes and methods in Python.

# Definitions of the summary statistics:
# 
# count -> number of non missing values in the dataset
# 
# mean -> the average of the data points in a column
# 
# std -> measures the amount of variation in the data
# 
# min -> smallest value in the dataset for each variable
# 
# 25% -> first quartile in a dataset (lower range)
# 
# 50% -> the median, half of the data points are below this value and half are above it
# 
# 75% -> the third quartile in the dataset
# 
# max -> the largest value in the dataset for each variable

# df.dropna() might be preferred when you only want to remove   missing values
# 
# del df['col'] might be preferred when you want to remove a whole column
# 
# using del df['col'] before df.dropna() ensures that you are only dealing with relevant columns when handling missing values.

# In[6]:


if 'unnecessary_col' in df.columns:
    del df['unnecessary_col']


# In[7]:


cleaned_df = df.dropna()

print("\nCleaned DataFrame:")
print(cleaned_df.head())
print("\nCleaned DataFrame Info:")
print(cleaned_df.info())


# In this session, we discussed various data cleaning techniques using pandas, particularly focusing on the use of del df['col'] and df.dropna(). Here's a concise summary of the key points covered:
# 
# Definitions of Summary Statistics:
# 
# count: Number of non-null entries.
# mean: Average of the values.
# std: Standard deviation, measuring the spread of values.
# min: Minimum value.
# 25%: First quartile (25th percentile).
# 50%: Median or second quartile (50th percentile).
# 75%: Third quartile (75th percentile).
# max: Maximum value.
# Use Case for df.dropna():
# 
# Scenario: When you want to remove rows with missing data to ensure that subsequent analyses are performed on complete records. For example, if you have a DataFrame with critical columns that should not contain missing values, using df.dropna() helps clean the data by removing any rows that have incomplete information.
# Opposite Use Case for del df['col']:
# 
# Scenario: When you have columns that are irrelevant or contain excessive missing values. For instance, if a column has mostly missing values and does not contribute to the analysis, removing it with del df['col'] prevents it from affecting the results of data cleaning operations like df.dropna().
# Combining del df['col'] with df.dropna():
# 
# Importance of Order:
# Efficiency: Removing irrelevant columns first reduces the DataFrame size, making the subsequent df.dropna() operation faster and more efficient.
# Data Integrity: Ensures that missing values are only dealt with in the context of relevant columns, avoiding unintended removal of rows due to irrelevant data.
# Clarity: Results in a cleaner DataFrame, simplifying further analysis by focusing only on the relevant data.
# Practical Example:
# 
# Dataset: Loaded a dataset from a URL and performed data cleaning.
# Steps Taken:
# Removed irrelevant columns using del df['col'].
# Used df.dropna() to drop rows with missing values.
# Justification: Improved efficiency, maintained data integrity, and provided a clearer, more manageable dataset for analysis.
# This session covered the rationale and methodology behind data cleaning techniques, emphasizing how to effectively use del df['col'] and df.dropna() to prepare data for analysis.

# df.groupby("col1")["col2"].describe() is used to perform group-wise summary statistics on a dataset

# df.describe() gives an overview of missing values for the whole dataset, while df.groupby("col1")["col2"].describe() gives a more detailed view by considering missing values within each specific group.

# I think that it is easier to work with ChatGPT because it can give corrections according to context. A google search will not be able to give answers to extremely specific questions, and a google search will only provide answers if your question has been asked before.

# Yes
