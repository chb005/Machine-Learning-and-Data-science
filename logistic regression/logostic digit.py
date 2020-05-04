#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


from sklearn.datasets import load_digits
digits=load_digits()


# In[10]:


digits


# In[11]:


dir(digits)


# In[12]:


digits.images


# In[13]:


digits.images[0]


# In[14]:


plt.matshow(digits.images[0])


# In[15]:


plt.gray()


# In[20]:


for i in range(5):
    plt.matshow(digits.images[i])


# In[21]:


digits.target[:6]


# In[22]:


from sklearn.linear_model import LogisticRegression
model=LogisticRegression()


# In[23]:


from sklearn.model_selection import train_test_split
x_trian,x_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.2)


# In[24]:


len(x_trian)


# In[25]:


len(x_test)


# In[26]:


x_trian


# In[27]:


len(digits.data)


# In[28]:


model.fit(x_trian,y_train)


# In[29]:


model.predict(x_test)


# In[30]:


y_test


# In[31]:


model.score(x_test,y_test)


# In[32]:


y_pred=model.predict(x_test)


# In[33]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)


# In[34]:


cm


# In[36]:


import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm,annot=True)
plt.xlabel("PREDICTED")
plt.ylabel("Truth")


# In[ ]:




