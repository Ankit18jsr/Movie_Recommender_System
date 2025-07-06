import streamlit as st
import pickle
import pandas as pd
import requests
import base64


#  Base64 image function
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

#  Load your background image
image_base64 = get_base64_of_bin_file("background.jpg")  # Your image name

# Inject CSS into Streamlit
st.markdown(
    f"""
    <style>
    .stApp {{
        width: 100%;
        height: 100%;
        background-image: url("data:image/jpg;base64,{image_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(0, 0, 0, 0.5); /* Optional: Add a semi-transparent overlay */
    }}

    </style>
    """,
    unsafe_allow_html=True
)

def fetch_poster(movie_id):
  response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e015a2185bd15cb0808022de7e49ff3f'.format(movie_id))
  data = response.json()  # fetch data from API response

  return "https://image.tmdb.org/t/p/w500/" + data['poster_path']




def recommend(movie):
    movie_index =  movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse = True, key= lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters
        

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies= pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb')) 


st.markdown("<h1 style='text-align: center;'>Movie Recommender System</h1>", unsafe_allow_html=True)

selected_movie_name= st.selectbox("",movies['title'].values)



if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

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






