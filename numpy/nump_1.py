#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([1,2,3])


# In[2]:


a


# In[3]:


a[0]


# In[4]:


a[2]


# In[10]:


import sys


# In[11]:


x=range(500)


# In[12]:


array=np.arange(500)


# In[13]:


print(sys.getsizeof(5)*len(x))
print(array.size*array.itemsize)


# In[14]:


a1=np.array([1,2,3])
a2=np.array([4,5,6])


# In[15]:


a1+a2


# In[16]:


a1-a2


# In[17]:


a1*a2


# In[18]:


a1/a2


# In[ ]:




