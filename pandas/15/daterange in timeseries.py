#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


df=pd.read_csv("aapl_no_dates.csv")
df


# In[12]:


df1=pd.date_range(start='6/1/2017',end='6/30/2017',freq='B')


# In[13]:


df1


# In[15]:


df.set_index(df1,inplace=True)
df


# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.plot()


# In[19]:


df["2017-06-01":"2017-06-10"].Close.mean()


# In[22]:


df.asfreq('H',method="pad")


# In[28]:


df1=pd.date_range(start='1/1/2017',periods=80,freq='B')
df1


# In[30]:


import numpy as np


# In[31]:


ts=np.random.randint(1,10,len(df1))


# In[33]:


ts


# In[35]:


df.head()


# In[ ]:




