#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv("salaries.csv")
df.head()


# In[5]:


inp=df.drop("salary_more_then_100k",axis="columns")
inp


# In[6]:


target=df["salary_more_then_100k"]
target


# In[7]:


from sklearn.preprocessing import LabelEncoder
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()


# In[15]:


inp["company_n"]=le_company.fit_transform(inp["company"])
inp["job_n"]=le_job.fit_transform(inp["job"])
inp["degree_n"]=le_degree.fit_transform(inp["degree"])


# In[16]:


inp


# In[17]:


inp1=inp.drop(['company','job','degree'],axis="columns")
inp1


# In[18]:


from sklearn import tree
model=tree.DecisionTreeClassifier()


# In[19]:


model.fit(inp1,target)


# In[20]:


model.score(inp1,target)


# In[24]:


#google,computer programmer,b.e degree
model.predict([[2,1,0]])  


# In[25]:


model.predict([[1,2,1]])


# In[ ]:




