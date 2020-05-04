#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits = load_digits()


# In[2]:



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.3)


# Logistic Regression

# In[3]:


lr = LogisticRegression(solver='liblinear',multi_class='ovr')
lr.fit(X_train, y_train)
lr.score(X_test, y_test)


# 
# SVM

# In[4]:


svm = SVC(gamma='auto')
svm.fit(X_train, y_train)
svm.score(X_test, y_test)


# Random Forest

# In[5]:


rf = RandomForestClassifier(n_estimators=40)
rf.fit(X_train, y_train)
rf.score(X_test, y_test)


# # KFold cross validation

# In[6]:


from sklearn.model_selection import KFold
kf = KFold(n_splits=3)
kf


# In[7]:


for train_index, test_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(train_index, test_index)


# In[8]:


def get_score(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)


# In[10]:


from sklearn.model_selection import StratifiedKFold
folds = StratifiedKFold(n_splits=3)

scores_logistic = []
scores_svm = []
scores_rf = []

for train_index, test_index in folds.split(digits.data,digits.target):
    X_train, X_test, y_train, y_test = digits.data[train_index], digits.data[test_index],                                        digits.target[train_index], digits.target[test_index]
    scores_logistic.append(get_score(LogisticRegression(solver='liblinear',multi_class='ovr'), X_train, X_test, y_train, y_test))  
    scores_svm.append(get_score(SVC(gamma='auto'), X_train, X_test, y_train, y_test))
    scores_rf.append(get_score(RandomForestClassifier(n_estimators=40), X_train, X_test, y_train, y_test))


# In[11]:


scores_logistic


# In[12]:


scores_svm


# In[13]:


scores_rf


# In[14]:


from sklearn.model_selection import cross_val_score


# In[15]:


digits.data


# In[16]:


digits.target


# In[17]:


cross_val_score(LogisticRegression(solver='liblinear',multi_class='ovr'), digits.data, digits.target,cv=3)


# In[18]:


cross_val_score(SVC(gamma='auto'), digits.data, digits.target,cv=3)


# In[19]:


cross_val_score(RandomForestClassifier(n_estimators=40),digits.data, digits.target,cv=3)


# In[20]:


scores1 = cross_val_score(RandomForestClassifier(n_estimators=5),digits.data, digits.target, cv=10)
np.average(scores1)


# In[21]:


scores1 = cross_val_score(RandomForestClassifier(n_estimators=10),digits.data, digits.target, cv=10)
np.average(scores1)


# In[22]:


scores1 = cross_val_score(RandomForestClassifier(n_estimators=20),digits.data, digits.target, cv=10)
np.average(scores1)


# In[23]:


scores1 = cross_val_score(RandomForestClassifier(n_estimators=40),digits.data, digits.target, cv=10)
np.average(scores1)


# In[ ]:




