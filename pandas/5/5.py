#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd


# In[47]:


import numpy as np


# In[48]:


df=pd.read_csv("weather_data.csv")


# In[49]:


df


# In[50]:


df=df.replace(-99999,np.NaN)


# In[51]:


df


# In[52]:


newdf=df.replace({
    'temperature':-99999,
    'windspeed':-99999,
    'event':'0'
},np.NaN)
newdf


# In[53]:


newdf=df.replace({
    -99999:np.NaN,
    "0":'sunny'
})
newdf


# In[54]:


newdf=df.replace({
    'temperature':'[A-Za-z]',
    'windspeed':'[A-Za-z]',
    
}," ",regex=True)
newdf


# In[59]:


newd=pd.read_csv("feed.csv")


# In[60]:


newd


# In[62]:


nw=newd.replace(['poor','average','good','very good','best'],[0,1,2,3,4])
nw


# In[ ]:




