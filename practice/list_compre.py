#!/usr/bin/env python
# coding: utf-8

# In[10]:


list1=[]
def lst_sqre(lst):
    for i in lst:
        list1.append(i*i)
    return list1


# In[11]:


lst_sqre([1,2,3,4,5,6,7])


# In[12]:


lst=[1,2,3,4,5,6,7]


# In[13]:


lst1=[i*i for i in lst]
print(lst1)


# In[16]:


lst1=[i*i for i in lst if i%2!=0]
print(lst1)


# In[ ]:




