#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("weather_by_cities.csv")


# In[3]:


df


# In[4]:


g=df.groupby("city")


# In[5]:


g


# In[6]:


for city,city_df in g:
    print(city)
    print(city_df)


# In[7]:


g.get_group("mumbai")


# In[8]:


g.max()


# In[9]:


g.mean()


# In[10]:


g.describe()


# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
g.plot()


# In[ ]:




