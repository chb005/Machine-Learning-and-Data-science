#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd


# In[16]:


df=pd.read_csv("weather_data.csv")


# In[17]:


df


# In[18]:


type(df.day[0])


# In[19]:


df=pd.read_csv("weather_data.csv",parse_dates=['day'])


# In[20]:


df.set_index('day',inplace=True)


# In[21]:


df


# In[23]:


newdf=df.fillna(0)


# In[24]:


newdf


# In[25]:


newdf=df.fillna({
    'temperature':0,
    'windspeed':0,
    'event':'no event'
    
})
newdf


# In[27]:


newdf=df.fillna(method="ffill")


# In[28]:


newdf


# In[29]:


newdf=df.fillna(method="bfill")
newdf


# In[34]:


newdf=df.fillna(method="ffill",axis="columns",limit=3)
newdf


# In[36]:


newdf=df.interpolate(method="time")
newdf


# In[42]:


newdf=df.dropna(thresh=1)
newdf


# In[ ]:




