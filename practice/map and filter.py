#!/usr/bin/env python
# coding: utf-8

# In[1]:


def odd_even(num):
    if num%2==0:
        return "the number {} is even".format(num)
    else:
         return "the number {} is odd".format(num)


# In[2]:


odd_even(32)


# In[3]:


list1=[2,4,6,8,34,57,32,11,45,39]


# In[4]:


map(odd_even,list1)


# In[5]:


list(map(odd_even,list1))


# In[6]:


def even(num):
    if num%2==0:
        return True


# In[7]:


list1=[1,2,3,4,5,6,7,8,9]


# In[9]:


list(map(even,list1))


# In[10]:


list(filter(even,list1))


# In[12]:


list(filter(lambda num:num%2==0,list1))


# In[13]:


list(map(lambda num:num%2==0,list1))


# In[ ]:




