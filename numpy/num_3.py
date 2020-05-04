#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


n=[6,7,8]


# In[3]:


n


# In[4]:


n[0:2]


# In[5]:


n[-1]


# In[6]:


a=np.array([6,7,8])


# In[7]:


a[0:2]


# In[9]:


a[-1]


# In[10]:


a=np.array([[6,7,8],[1,2,3],[9,3,2]])


# In[11]:


a


# In[12]:


a[1,2]


# In[13]:


a[0:2,2]


# In[14]:


a[-1]


# In[15]:


a[-1,0:2]


# In[17]:


a[:,1:3]


# In[18]:


a=np.array([[6,7,8],[1,2,3],[9,3,2]])


# In[19]:


a


# In[20]:


for row in a:
    print(row)


# In[21]:


for cell in a.flat:
    print(cell)


# In[22]:


a=np.arange(6).reshape(3,2)
b=np.arange(6,12).reshape(3,2)


# In[23]:


a


# In[24]:


b


# In[25]:


np.vstack((a,b))


# In[26]:


np.hstack((a,b))


# In[27]:


a=np.arange(30).reshape(2,15)


# In[28]:


a


# In[29]:


np.hsplit(a,3)


# In[30]:


result=np.hsplit(a,3)


# In[32]:


result[0]


# In[33]:


result[1]


# In[34]:


result[2]


# In[38]:


result=np.vsplit(a,2)


# In[39]:


result[0]


# In[40]:


result[1]


# In[41]:


a=np.arange(12).reshape(3,4)


# In[42]:


a


# In[43]:


b=a>4


# In[44]:


b


# In[45]:


a[b]


# In[46]:


a[b]=1


# In[47]:


a


# In[ ]:




