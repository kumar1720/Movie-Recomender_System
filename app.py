import streamlit as st
import pickle

with open('movies.pkl', 'rb') as f:
    movies_list = pickle.load(f)

movies_list = movies_list['title'].values
st.title('Movie Recommender System')
select_movie_name = st.selectbox(
    movies_list['title'].values
)
