#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


df=pd.read_csv("insurance_data.csv")
df.head()


# In[9]:


plt.scatter(df.age,df.bought_insurance,marker="+",color="red")


# In[51]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(df[['age']],df[['bought_insurance']],test_size=0.1)


# In[52]:


len(X_train)


# In[53]:


len(X_test)


# In[54]:


X_train


# In[55]:


X_test


# In[56]:


from sklearn.linear_model import LogisticRegression
model1=LogisticRegression()


# In[ ]:





# In[57]:


model1.fit(X_train,y_train)


# In[58]:


X_test


# In[59]:


model1.predict(X_test)


# In[61]:


model1.predict([[78]])


# In[62]:


model1.predict([[35]])


# In[63]:


model.predict_proba(X_test)


# In[64]:


model1.fit(X_train,y_train)


# In[65]:


model1.predict_proba(X_test)


# In[68]:


model1.score(X_test,y_test)


# In[ ]:




