#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


days=[1,2,3,4,5,6,7]
t_max=[32,51,52,47,48,50,46]
t_min=[43,42,40,44,33,35,37]
t_avg=[45,48,47,46,40,42,41]


# In[26]:


plt.xlabel("Days")
plt.ylabel("Temp")
plt.title("Weather")
plt.plot(days,t_max,label="MAX")
plt.plot(days,t_min,label="MIN")
plt.plot(days,t_avg,label="AVG")
plt.legend(loc="best",shadow=True,fontsize="small")
plt.grid()


# In[ ]:




