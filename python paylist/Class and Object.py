#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Teach:
    def __init__(self,n,w):
        self.name=n
        self.work=w
        
    def do_work(self):
        if self.work=="teacher":
            print(self.name,"teaching java")
        elif self.work=="labasst":
            print(self.name," teaching you practical")
            
    def speaks(self):
        print(self.name,"how are you...")
        
chb=Teach("chirag bhatt","teacher")
chb.do_work()
chb.speaks()
    
dhb=Teach("Navin patel","labasst")
dhb.do_work()
dhb.speaks()
        
        


# In[ ]:




