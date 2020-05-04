#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("weather.csv")
df


# In[4]:


df.pivot(index="date",columns="city",values="humidity")


# In[5]:


df=pd.read_csv("weather2.csv")
df


# In[14]:


df.pivot_table(index="city",columns="date",aggfunc="sum",margins=True)


# In[15]:


df=pd.read_csv("weather3.csv")


# In[16]:


df


# In[17]:


df['date']=pd.to_datetime(df['date'])


# In[18]:


df


# In[20]:


type(df['date'][1])


# In[21]:


df.pivot_table(index=pd.Grouper(freq="M",key='date'),columns='city')


# In[ ]:




