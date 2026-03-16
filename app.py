import streamlit as st
import pickle
import pandas as pd

# Load files
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Title
st.title("🎬 Movie Recommendation System")

# Movie list
movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)),
                        reverse=True,
                        key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Button
if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write(movie)
