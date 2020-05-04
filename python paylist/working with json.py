#!/usr/bin/env python
# coding: utf-8

# In[1]:


book={}
book['chb']={
    'name':'chirag',
    'address':'kadi',
    'mob':986745
    
}
book['dhb']={
    'name':'dipak',
    'address':'ahmedabad',
    'mob':386745
    
}


# In[2]:


import json


# In[3]:


s=json.dumps(book)


# In[4]:


print(s)


# In[5]:


with open("json_w.txt","w") as f:
    f.write(s)


# In[7]:


f=open("json_w.txt","r")
s=f.read()
s


# In[9]:


import json
book=json.loads(s)
book


# In[10]:


type(book)


# In[11]:


book['chb']


# In[12]:


book['chb']['mob']


# In[13]:


for person in book:
    print(book[person])


# In[ ]:




