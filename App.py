import streamlit as st
import pickle
import pandas as pd
import requests
import time
from streamlit_option_menu import option_menu

st.set_page_config(
     page_title="Recommender System",
     layout="wide",
     initial_sidebar_state="auto"
 )
with st.sidebar:
    selected = option_menu(
        menu_title="MainMenu",  # required
        options=['Home', 'REVIEW3', 'my info'],

        default_index=0,
        orientation="horizontal"
    )

    if selected == "Home":
        st.title(f"You have selected {selected}")
    if selected == "Projects":
        st.title(f"You have selected {selected}")
    if selected == "Contact":
        st.title(f"You have selected {selected}")


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e8d9abc9ca8f7736a15833fa564fa192&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster
movie_dict1 = pickle.load(open('movie_dict1.pkl', 'rb'))
movies = pd.DataFrame(movie_dict1)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('MOVIE RECOMMENDATION SYSTEM')

option = st.selectbox('Select a movie from below', movies['title'].values)

if st.button('RECOMMEND'):
    names, posters = recommend(option)
    with st.spinner('Wait for it...'):
        time.sleep(0)
    col1, col2, col3, col4, col5 = st.columns(5)
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

    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.text(names[5])
        st.image(posters[5])

    with col7:
        st.text(names[6])
        st.image(posters[6])

    with col8:
        st.text(names[7])
        st.image(posters[7])

    with col9:
        st.text(names[8])
        st.image(posters[8])

    with col10:
        st.text(names[9])
        st.image(posters[9])
