#!/usr/bin/env python
# coding: utf-8

# In[1]:


1/0


# In[2]:


'ab'+3


# In[4]:


x=input("enter no1:")
y=input("enter no2:")

z=int(x)/int(y)
print("division:",z)


# In[2]:


x=input("enter no1:")
y=input("enter no2:")
try: 
    z=int(x)/int(y)
except Exception as e:
    print("Exception occured:",e)
    z=None
print("division:",z)    
    


# In[11]:


x=input("enter no1:")
y=input("enter no2:")
try: 
    z=(x)/int(y)
except ZeroDivisionError as e:
    print("Exception Type:",type(e).__name__)
    z=None
except Exception as e:
    print("Exception Type:",type(e).__name__)
    z=None    
print("division:",z)    
    


# In[ ]:




