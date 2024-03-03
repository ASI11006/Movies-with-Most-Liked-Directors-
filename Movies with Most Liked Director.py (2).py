#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


#import dataset from a csv file saved in downloads extracted from sample data available online
Movies = pd.read_csv('Downloads/First-Project-main (2)/movie_metadata.csv')

#Run dataframe named Movies
Movies


# In[9]:


#Run .loc formula to display only two columns which are required for my work
Movies = Movies.loc[:,['director_name','director_facebook_likes']]


# In[10]:


#Showing the shape of the dataframe Movies which would only display the number of rows and columns available to display
Movies.shape


# In[7]:


#display information about the dataframe Movies
Movies.info()


# In[17]:


#Display 50 lines with the columns I've chosen to work on
Movies.head(50)


# In[13]:


#using numpy replace any nan or error values in the columns 

Movies['director_facebook_likes'] = Movies['director_facebook_likes'].replace(np.nan, '170')
Movies['director_name'] = Movies['director_name'].replace(np.nan, 'unknown')


# In[14]:


Movies.head(50)


# In[17]:


#Display any null values in the columns and show datatype
Movies.isnull().sum()


# In[15]:


#Create visual of line plot to show which director got the most Facebook likes. Clearly, the winner here is Christopher Nolan.
Movies.head().plot(x='director_name', y='director_facebook_likes', title= 'Director with most likes')

