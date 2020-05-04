#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()


# In[2]:


iris


# In[3]:


dir(iris)


# In[4]:


iris.feature_names


# In[5]:


iris.target_names


# In[6]:


len(iris.data)


# In[7]:


df=pd.DataFrame(iris.data,columns=iris.feature_names)
df.head()


# In[9]:


df['target']=iris.target
df.head()


# In[10]:


iris.target


# In[14]:


df[df.target==2].head()


# In[16]:


df['flower_name']=df.target.apply(lambda x:iris.target_names[x])
df.head()


# In[17]:


df[45:55]


# In[18]:


df0=df[:50]
df1=df[50:100]
df2=df[100:]


# In[19]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


plt.xlabel("Sepal Length")
plt.ylabel("Sepal width")
plt.scatter(df0['sepal length (cm)'],df0['sepal width (cm)'],color="green",marker="+")
plt.scatter(df1['sepal length (cm)'],df1['sepal width (cm)'],color="blue",marker=".")


# In[23]:


plt.xlabel("Petal Length")
plt.ylabel("Petal width")
plt.scatter(df0['petal length (cm)'],df0['petal width (cm)'],color="green",marker="+")
plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'],color="blue",marker=".")


# In[24]:


from sklearn.model_selection import train_test_split


# In[26]:


x=df.drop(['target','flower_name'],axis="columns")
y=df.target


# In[27]:


xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)


# In[28]:


len(xtrain)


# In[29]:


len(ytrain)


# In[30]:


xtrain


# In[31]:


ytrain


# In[32]:


len(xtest)


# In[33]:


xtest


# In[34]:


from sklearn.svm import SVC
model=SVC()


# In[35]:


model.fit(xtrain,ytrain)


# In[36]:


model.score(xtest,ytest)


# In[38]:


model.predict([[4.4,3.0,1.4,0.3]])


# In[46]:


model_c=SVC(C=4)
model_c.fit(xtrain,ytrain)
model_c.score(xtest,ytest)


# In[49]:


model_c=SVC(gamma=10)
model_c.fit(xtrain,ytrain)
model_c.score(xtest,ytest)


# In[51]:


model_liear_keral=SVC(kernel="linear")
model_liear_keral.fit(xtrain,ytrain)


# In[52]:


model_liear_keral.score(xtest,ytest)


# In[ ]:




