import pickle
import streamlit as st
import requests

st.header("Movie Recommendation System Using Machine Learning")
movies = pickle.load(open('artificats/movie_list.pkl','rb'))
similarity = pickle.load(open('artificats/similarity.pkl','rb'))

movie_list = movies['title'].values
st.selectbox(
    'Select a movie',
    movie_list
)