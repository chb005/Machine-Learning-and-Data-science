#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


x=[1,2,3,4,5,6,7]
y=[50,51,47,52,48,49,46]


# In[9]:


plt.plot(x,y,color="red",linewidth=5,linestyle="dotted")
plt.xlabel("Days")
plt.ylabel("Temp")
plt.title("WEATHER")


# In[ ]:




