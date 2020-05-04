#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("spam.csv")
df.head()


# In[3]:


df.groupby('Category').describe()


# In[4]:


df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df.head()


# In[5]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.Message,df.spam)


# In[6]:


from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
X_train_count = v.fit_transform(X_train.values)
X_train_count.toarray()[:2]


# In[20]:





# In[21]:


emails = [
    'Hey mohan, can we get together to watch footbal game tomorrow?',
    'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!'
]
emails_count = v.transform(emails)
model.predict(emails_count)


# In[22]:


X_test_count = v.transform(X_test)
model.score(X_test_count, y_test)


# In[32]:


from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])


# In[33]:


clf.fit(X_train, y_train)


# In[34]:


clf.score(X_test,y_test)


# In[35]:


clf.predict(emails)


# In[36]:


from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])


# In[37]:


clf.fit(X_train, y_train)


# In[46]:


emails = [
    'my name is chirag,',
    'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!'
]


# In[47]:


clf.predict(emails)


# In[ ]:




