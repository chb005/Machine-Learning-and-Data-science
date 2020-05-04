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


# In[13]:


plt.xticks(xpos,company)
plt.ylabel("Revenue in BLN")
plt.title("Indian Company")
plt.bar(xpos-0.2,revenue,label="revenue",width=0.4)
plt.bar(xpos+0.2,profit,label="profit",width=0.4)
plt.legend()


# In[ ]:




