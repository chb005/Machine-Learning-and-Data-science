#!/usr/bin/env python
# coding: utf-8

# In[4]:


class vehicle:
    def general(self):
        print("general use: Transport")
        
class car(vehicle):
    def __init__(self):
        print("This is car")
        self.wheels=4
        self.roof=True
        
    def spec_use(self):
        #self.general()
        print("specific use: going to market")
        
class scotter(vehicle):
    def __init__(self):
        print("This is scotter")
        self.wheels=2
        self.roof=False
        
    def spec_use(self):
        #self.general()
        print("specific use: small trip")
        
c=car()
c.general()
c.spec_use()

s=scotter()
s.general()
s.spec_use()


# In[ ]:




