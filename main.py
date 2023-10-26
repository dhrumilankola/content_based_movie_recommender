import streamlit as st
import pickle
import pandas as pd
import numpy as nppui
import requests

def fetch_poster(movie_idp):
     response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a267ee914f4f70e10a3ee429e6c6d550&language=en-US'.format(movie_idp))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
     movie_index = new_df[new_df['title'] == movie].index[0]
     distances = similarity[movie_index]
     movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movie = []
     recommended_movie_poster = []
     for i in movie_list:
          movies_id = new_df.iloc[i[0]].movie_id
          recommended_movie.append(new_df.iloc[i[0]].title)
          recommended_movie_poster.append(fetch_poster(movies_id))
     return recommended_movie,recommended_movie_poster


new_df = pickle.load(open('movies.pkl','rb'))
movies = new_df['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
     'How would you like to be contacted?',movies)

if st.button('Recommend'):
     names,posters = recommend(selected_movie_name)

     col1,col2,col3,col4,col5 = st.columns(5)
     with col1:
          st.text(names[0])
          st.image(posters[0])
     with col2:
          st.text(names[1])
          st.image(posters[1])
     with col3:
          st.text(names[2])
          st.image(posters[2])
     with col4:
          st.text(names[3])
          st.image(posters[3])
     with col5:
          st.text(names[4])
          st.image(posters[4])
