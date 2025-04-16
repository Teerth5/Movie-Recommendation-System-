#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import pandas as pd 


import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[30]:


credits = pd.read_csv("archive/tmdb_5000_credits.csv")
movies =  pd.read_csv("archive/tmdb_5000_movies.csv")


# In[31]:


movies.head(2)


# In[4]:


movies.shape


# In[5]:


credits.head()


# In[32]:


movies = movies.merge(credits,on='title')


# In[ ]:


movies.head()
# budget
# homepage
# id
# original_language
# original_title
# popularity
# production_comapny
# production_countries
# release-date(not sure)


# In[33]:


movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]


# In[8]:


movies.head()


# In[12]:


import ast


# In[34]:


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L 


# In[35]:


movies.dropna(inplace=True)


# In[36]:


movies['genres'] = movies['genres'].apply(convert)
movies.head()


# In[37]:


movies['keywords'] = movies['keywords'].apply(convert)
movies.head()


# In[ ]:


import ast
ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')


# In[38]:


def convert3(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L 


# In[39]:


movies['cast'] = movies['cast'].apply(convert)
movies.head()


# In[40]:


movies['cast'] = movies['cast'].apply(lambda x:x[0:3])


# In[41]:


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L 


# In[42]:


movies['crew'] = movies['crew'].apply(fetch_director)


# In[22]:


#movies['overview'] = movies['overview'].apply(lambda x:x.split())
movies.sample(5)


# In[43]:


def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


# In[44]:


movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)


# In[26]:


movies.head()


# In[45]:


movies['overview'] = movies['overview'].apply(lambda x:x.split())


# In[46]:


movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']


# In[47]:


new = movies.drop(columns=['overview','genres','keywords','cast','crew'])
#new.head()


# In[48]:


new['tags'] = new['tags'].apply(lambda x: " ".join(x))
new.head()


# In[49]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
    


# In[50]:


vector = cv.fit_transform(new['tags']).toarray()


# In[ ]:


vector.shape


# In[51]:


from sklearn.metrics.pairwise import cosine_similarity


# In[52]:


similarity = cosine_similarity(vector)


# In[ ]:


similarity


# In[ ]:


new[new['title'] == 'The Lego Movie'].index[0]


# In[53]:
import streamlit as st
import pandas as pd
import pickle

# Load data from pickle files
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('🎬 Movie Recommender System')

# Create a dropdown (selectbox) using the 'title' column from movies DataFrame
selected_movie = st.selectbox('Select a movie you like:', movies['title'].values)

def recommend(movie):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]
    # Retrieve the similarity distances for the selected movie
    distances = similarity[movie_index]
    # Get top 5 recommendations (skipping the first one which is the same movie)
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    # Collect the recommended movie titles
    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommended_movies

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader('You might also like:')
    for rec in recommendations:
        st.write("🎥 " + rec)



        
    


# In[54]:

# if __name__ == "__main__":
#    user_input = input("Enter a movie name: ")
#    recommend(user_input)



# In[55]:







