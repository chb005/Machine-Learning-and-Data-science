#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.datasets import load_digits
digits = load_digits()


# In[2]:


dir(digits)


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[4]:


plt.gray() 
for i in range(4):
    plt.matshow(digits.images[i])


# In[5]:


df = pd.DataFrame(digits.data)
df.head()


# In[6]:


df['target'] = digits.target


# In[7]:



df[0:12]


# In[8]:


X = df.drop('target',axis='columns')
y = df.target


# In[9]:



df[0:12]


# In[10]:


X = df.drop('target',axis='columns')
y = df.target


# In[11]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)


# In[12]:


from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
model.fit(X_train, y_train)


# In[13]:


model.score(X_test, y_test)


# In[14]:


y_predicted = model.predict(X_test)


# In[15]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm


# In[16]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')


# In[ ]:




