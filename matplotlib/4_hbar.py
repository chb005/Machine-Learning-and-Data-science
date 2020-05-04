#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[10]:


company=['Infosys','TCS','L&T','SBI']
revenue=[90,130,110,100]
profit=[40,20,34,14]


# In[3]:


xpos=np.arange(len(company))


# In[4]:


xpos


# In[15]:


plt.yticks(xpos,company)

plt.title("Indian Company")
plt.barh(xpos-0.2,revenue,label="revenue")
plt.barh(xpos+0.2,profit,label="profit")
plt.legend()


# In[ ]:




