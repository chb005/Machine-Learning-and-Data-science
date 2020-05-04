#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("weather.csv")
df


# In[3]:


df1=pd.melt(df,id_vars=['day'])
df1


# In[4]:


df1[df1['variable']=='chicago']


# In[6]:


df1=pd.melt(df,id_vars=['day'],var_name="city",value_name="temperature")
df1


# In[ ]:




