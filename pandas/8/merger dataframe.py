#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


ind_weather1 = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    })
ind_weather1


# In[10]:


ind_weather2 = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "humidity": [80, 60, 78]
})
ind_weather2


# In[21]:


df2=pd.merge(ind_weather1,ind_weather2,on="city")


# In[22]:


df2


# In[23]:


df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})
df1


# In[24]:


df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})
df2


# In[27]:


df3=pd.merge(df1,df2,on="city",how="inner")


# In[28]:


df3


# In[29]:


df3=pd.merge(df1,df2,on="city",how="outer")
df3


# In[30]:


df3=pd.merge(df1,df2,on="city",how="left")
df3


# In[31]:


df3=pd.merge(df1,df2,on="city",how="right")
df3


# In[32]:


df3=pd.merge(df1,df2,on="city",how="outer",indicator=True)
df3


# In[33]:


ind_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
ind_weather


# In[34]:



us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
us_weather


# In[40]:


df7=pd.merge(ind_weather,us_weather,on="city",how="outer",suffixes=('_first','_second'))
df7


# In[ ]:




