#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


column_name=['user_id','item_id','rating','timestamp']


# In[3]:


df=pd.read_csv('u.data',sep='\t',names=column_name)


# In[4]:


df.head()


# In[5]:


movie_title=pd.read_csv("Movie_Id_Titles")
movie_title.head()


# In[6]:


df=pd.merge(df,movie_title,on="item_id")
df.head()


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("white")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


df.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[9]:


df.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[10]:


ratings=pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()


# In[11]:


ratings['no of ratings']=pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()


# In[12]:


plt.figure(figsize=(7,5))
ratings['no of ratings'].hist(bins=70)


# In[13]:


plt.figure(figsize=(7,5))
ratings['rating'].hist(bins=70)


# In[14]:


sns.jointplot(x='rating',y='no of ratings',data=ratings,alpha=0.7)


# In[15]:


moviemat=df.pivot_table(index='user_id',columns='title',values='rating')


# In[16]:


moviemat.head()


# In[17]:


ratings.sort_values('no of ratings',ascending=False).head(10)


# In[18]:


ratings.head()


# In[19]:


str_rating=moviemat['Star Wars (1977)']
lia_rating=moviemat['Liar Liar (1997)']
str_rating.head()


# In[20]:


same_str=moviemat.corrwith(str_rating)
same_liar=moviemat.corrwith(lia_rating)


# In[21]:


corr_starwars = pd.DataFrame(same_str,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()


# In[22]:


corr_starwars.sort_values('Correlation',ascending=False).head(10)


# In[25]:


corr_starwars = corr_starwars.join(ratings['no of ratings'])
corr_starwars.head()


# In[26]:


corr_starwars[corr_starwars['no of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[28]:


corr_liarliar = pd.DataFrame(same_liar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['no of ratings'])
corr_liarliar[corr_liarliar['no of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[ ]:




