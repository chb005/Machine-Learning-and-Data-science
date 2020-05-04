#!/usr/bin/env python
# coding: utf-8

# In[3]:


class father:
    def playing(self):
        print("father playing")

class mother:
    def cooking(self):
        print("mother is cooking")
        
class rahul(father,mother):
    def sport(self):
        print("enjoy sport")
        


# In[6]:


c=rahul()
c.playing()
c.cooking()
c.sport()


# In[ ]:




