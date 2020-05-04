#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([5,6,7])


# In[2]:


a


# In[3]:


a.ndim


# In[4]:


a[0]


# In[5]:


a[2]


# In[7]:


a=np.array([[1,2],[3,4],[5,6]])


# In[8]:


a.ndim


# In[9]:


a.itemsize


# In[18]:


a.dtype


# In[19]:


a=np.array([[1,2],[3,4],[5,6]],dtype=np.float64)


# In[21]:


a


# In[22]:


a.size


# In[23]:


a.shape


# In[24]:


a=np.array([[1,2],[3,4],[5,6]],dtype=np.complex)


# In[25]:


a


# In[26]:


a.dtype


# In[27]:


a=np.zeros((3,4))


# In[28]:


a


# In[29]:


a=np.ones((3,4))


# In[30]:


a


# In[31]:


l=range(5)


# In[32]:


l


# In[33]:


l[0]


# In[34]:


l[3]


# In[35]:


a=np.arange(1,5)


# In[36]:


a


# In[37]:


np.arange(1,9,2)


# In[38]:


np.linspace(1,5,10)


# In[39]:


a=np.array([[1,2],[3,4],[5,6]])


# In[40]:


a


# In[41]:


a.shape


# In[42]:


a.reshape(2,3)


# In[43]:


a.reshape(6,1)


# In[44]:


a.ravel()


# In[45]:


a.min()


# In[46]:


a.max()


# In[47]:


a.sum()


# In[48]:


a.sum(axis=0)


# In[49]:


a.sum(axis=1)


# In[51]:


np.sqrt(a)


# In[52]:


np.std(a)


# In[53]:


a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])


# In[54]:


a


# In[55]:


b


# In[56]:


a+b


# In[57]:


a-b


# In[58]:


a*b


# In[59]:


a/b


# In[60]:


a.dot(b)


# In[ ]:




