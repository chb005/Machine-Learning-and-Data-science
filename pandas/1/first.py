#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[7]:


df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=["Column1","Column2","Column3","Coumn4"])


# In[8]:


df


# In[9]:


df.loc['Row1'] 


# In[10]:


df=pd.read_csv("weather_data.csv")


# In[11]:


df


# In[12]:


df.shape


# In[13]:


rows,columns=df.shape


# In[14]:


columns


# In[15]:


rows


# In[17]:


df.head()


# In[19]:


df.tail(2)


# In[20]:


df[2:4]


# In[21]:


df.iloc[:,:]


# In[22]:


df.iloc[2:4,1:3]


# In[29]:


df.iloc[0:2,0]


# In[30]:


df.to_csv("chb.csv")


# In[31]:


df.day


# In[32]:


df.temperature


# In[38]:


type(df['day'])


# In[34]:


df['day']


# In[39]:


type(df['temperature'])


# In[42]:


df.iloc[:,1:].values


# In[45]:


df[['day','temperature']]


# In[46]:


df.temperature.max()


# In[47]:


df.temperature.min()


# In[48]:


df.temperature.mean()


# In[49]:


df.describe()


# In[52]:


df[df.temperature==df.temperature.max()]


# In[53]:


df[['day','temperature']][df.temperature==df.temperature.max()]


# In[54]:


df.index


# In[ ]:




