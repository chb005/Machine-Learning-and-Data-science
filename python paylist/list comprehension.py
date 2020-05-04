#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst1=[]
def lst_sqre(lst):
    for i in lst:
        lst1.append(i*i)
    return lst1


# In[2]:


lst_sqre([1,3,5,7,8])


# In[4]:


lst=[1,2,3,4,5,6,7,8]


# In[5]:


lst1=[i*i for i in lst]
print(lst1)


# In[8]:


lst1=[i*i for i in lst if i%2!=0]

print(lst1)


# In[ ]:




