#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"D:\python docouments\analytics_dataset\8. Netflix Dataset.csv")


# In[3]:


data.head(2)


# In[4]:


data.tail(2)


# In[5]:


data.shape


# In[6]:


data.columns


# In[7]:


data.dtypes


# In[8]:


data.info()


# In[9]:


data[data.duplicated()]


# In[10]:


data.drop_duplicates(inplace=True)


# In[11]:


data.isnull().sum()


# In[12]:


sns.heatmap(data.isnull())


# In[13]:


data.head(3)


# ## For 'House of Cards' what is the show id and who is the director of this show?

# In[14]:


data[data['Title']== 'House of Cards']


# In[15]:


data[data['Title'].isin(['House of Cards'])]


# In[16]:


data[data['Title'].str.contains('House of Cards')]


# ## In which year highest number of the TV shows and movies were released? show with bar graph

# In[17]:


data.head(2)


# In[18]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[19]:


data['Date_N'].dt.year.value_counts()


# ## How many movies and TV shows are in the datasets?

# In[20]:


data.head(2)


# In[23]:


data.groupby('Category').Category.count()


# ## Show all the movies that were released in year 2000?

# In[32]:


data.head(2)


# In[33]:


data['Year'] = data['Date_N'].dt.year


# In[35]:


data.head(2)


# In[38]:


data[(data['Category'] == 'Movie') & (data['Year'] == 2000)]


# ## Show only the title of all TV shows that were released in Inda only

# In[39]:


data.head(2)


# In[41]:


data[(data['Title'] == 'TV Show') & (data['Country'] == 'India')]


# ## Show Top 10 Director, who gave the highest number of TV shows and Movies to Netflix

# In[43]:


data['Director'].value_counts(10).head(10)


# ## Show all the records where Category is 'Movie' and Type is 'Comedies' or Country is 'United Kingdom'

# In[44]:


data.head(2)


# In[48]:


data[(data['Category']=='Movie') & (data['Type'] =='Comedies')|(data['Country'] == 'United Kingdom')]


# ## In how many movies/shows, Tom Cruise was cast

# In[49]:


data.head(2)


# In[58]:


data_new = data.dropna()


# In[59]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# ## What are the different ratings defined by netflix

# In[63]:


data['Rating'].unique()


# ## How many movies got the 'TV-14'  rating in Canada

# In[64]:


data.head(2)


# In[65]:


data[(data['Category'] == 'Movie') & (data['Rating'] == 'TV-14') & (data['Country'] == 'Canada')]


# ## how many TV shows got the 'R Rating' after year 2018?

# In[67]:


data.head(2)


# In[69]:


data[(data['Category']== 'TV Shows') & (data['Rating'] =='R') & (data['Year']> 2018)]


# ## what is the max duration of movie/shows on Netflix?
# 

# In[70]:


data.head(2)


# In[74]:


data[['Minutes', 'Units']] = data['Duration'].str.split(' ', expand = True)


# In[75]:


data.head(2)


# In[76]:


data['Minutes'].max()


# ## Which individual country has the highest no. of TV shows?

# In[77]:


data.head(2)


# In[78]:


data_tvshows = data[data['Category'] == 'TV Show']


# In[80]:


data_tvshows.Country.value_counts().head(1)


# ## How cans we sort the dataset by year?

# In[84]:


data.sort_values(by ='Year', ascending = False)


# ## Find all the instances where categoy is movie and Type is Drama or Category is TV Shows and type is KIDS TV

# In[90]:


data[(data['Category'] == 'Movie') & (data['Type'] == 'Drama')]


# In[89]:


data[(data['Category'] == 'TV Shows') & (data['Type'] == "Kids' TV")]


# In[ ]:




