#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


ind_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
ind_weather


# In[3]:


us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
us_weather


# In[9]:


df=pd.concat([ind_weather,us_weather],keys=["india","US"])
df


# In[10]:


df.loc["india"]


# In[11]:


df.loc["US"]


# In[16]:


ind_weather1 = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    },index=[0,1,2])
ind_weather1


# In[19]:


ind_weather2 = pd.DataFrame({
    "city": ["delhi","banglore","mumbai"],
    "wpeed": [23,43,19],
    },index=[1,2,0])
ind_weather2


# In[21]:


pd.concat([ind_weather1,ind_weather2],axis=1)


# In[22]:


s=pd.Series(['Rain','Dry','Humid'],name='event')
s


# In[23]:


df=pd.concat([ind_weather1,s],axis=1)


# In[24]:


df


# In[ ]:




