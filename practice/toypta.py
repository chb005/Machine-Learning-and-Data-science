#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


car1=pd.read_csv("toyota EDA/ToyotaCorolla.csv",index_col=0,na_values=["??","????"])


# In[7]:


car1


# In[9]:


car2=car1.copy()


# In[20]:


pd.crosstab(index=car2['Fuel_Type'],columns='count',dropna=True)


# In[22]:


pd.crosstab(index=car2['Automatic'],columns=car2['Fuel_Type'],dropna=True)


# In[23]:


pd.crosstab(index=car2['Automatic'],columns=car2['Fuel_Type'],dropna=True,normalize=True)


# In[24]:


pd.crosstab(index=car2['Automatic'],columns=car2['Fuel_Type'],dropna=True,normalize=True,margins=True)


# In[27]:


pd.crosstab(index=car2['Automatic'],columns=car2['Fuel_Type'],dropna=True,normalize='index',margins=True)


# In[28]:


pd.crosstab(index=car2['Automatic'],columns=car2['Fuel_Type'],dropna=True,normalize='columns',margins=True)


# In[29]:


car2.shape


# In[30]:


num_data=car2.select_dtypes(exclude=[object])


# In[33]:


print(num_data.shape)


# In[32]:


num_data.shape


# In[34]:


coor_matx=num_data.corr()


# In[35]:


coor_matx


# In[ ]:




