#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a=np.arange(12).reshape(3,4)


# In[3]:


a


# In[4]:


for row in a:
    print(row)


# In[5]:


for x in np.nditer(a,order='C'):
    print(x)


# In[6]:


for x in np.nditer(a,order='F'):
    print(x)


# In[9]:


for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=x*x


# In[10]:


a


# In[12]:


b=np.arange(3,15,4).reshape(3,1)


# In[14]:


b


# In[15]:


for x,y in np.nditer([a,b]):
    print(x,y)


# In[ ]:




