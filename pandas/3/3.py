#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd


# In[13]:


df=pd.read_csv("stock_data.csv")
df


# In[14]:


df=pd.read_csv("stock_data.csv",skiprows=1)
df


# In[15]:


df=pd.read_csv("stock_data.csv",header=1)
df


# In[16]:


df=pd.read_csv("stock_data.csv",header=None)
df


# In[18]:


df=pd.read_csv("stock_data.csv",header=None,names=['tickers','eps','revenue','price','people'],skiprows=1)
df


# In[21]:


df=pd.read_csv("stock_data.csv",nrows=3,skiprows=1)
df


# In[22]:


df


# In[23]:


df.head(5)


# In[24]:


df


# In[26]:


df=pd.read_csv("stock_data.csv")
df


# In[27]:


df=pd.read_csv("stock_data.csv",na_values=['not available','n.a.'])
df


# In[30]:


df=pd.read_csv("stock_data.csv",na_values={
    'eps':['not available','n.a.'],
    'revenue':['not available','n.a.',-1],
    'price':['not available','n.a.'],
    'people':['not available','n.a.']
    })
df


# In[32]:


df.to_csv("chirag.csv",index=False)


# In[33]:


df.columns


# In[35]:


df.to_csv("chb.csv",columns=['tickers','price'],header=False)


# In[40]:


df=pd.read_excel("stock_data.xlsx",sheet_name="Sheet2")
df


# In[41]:


def convert_na(cell):
    if cell=="n.a.":
        return "chirag"
    return cell


# In[42]:


df=pd.read_excel("stock_data.xlsx","Sheet1",converters={
    'people':convert_na
})
df


# In[47]:


df.to_excel("chb2.xlsx",sheet_name="chirag1",index=False,startcol=1,startrow=2)


# In[ ]:




