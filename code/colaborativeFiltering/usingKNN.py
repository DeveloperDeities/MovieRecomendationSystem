
#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[15]:


movies=pd.read_csv("../../datasets/movies.csv",usecols=["movieId","title"])
movies.head()


# In[19]:


ratings=pd.read_csv("../../datasets/ratings.csv",usecols=["userId","movieId","rating"])
ratings.head()


# # nan values check
#

# In[20]:


ratings.shape


# In[21]:


movies.shape


# In[22]:


ratings.isnull().count()


# In[23]:


movies.isnull().count()


# # data Reshaping

# In[33]:


movies_users=ratings.pivot(index="movieId",columns="userId",values="rating")
movies_users.head()


# In[57]:


movies_users=movies_users.fillna(0)


# In[58]:


from scipy.sparse import csr_matrix


# In[59]:


mat_movies=csr_matrix(movies_users.values)


# In[ ]:





# In[60]:


from sklearn.neighbors import NearestNeighbors
model=NearestNeighbors(metric="cosine",algorithm="brute",n_neighbors=10)
model.fit(mat_movies)


# In[61]:


#used for searching
from  fuzzywuzzy import process


# In[63]:


def recomender(movies_name,data,n):
    idx=process.extractOne(movies_name,movies["title"])[2]
    print("movie_selected=",movies["title"][idx], "Index" ,idx)
    distance, indices=model.kneighbors(data[idx],n_neighbors=n)
    print(distance,indices)
    for i in indices:
        print(movies["title"][i].where(i != idx))


# In[64]:


recomender('toy story',mat_movies,10)


# In[ ]:



