import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd


tfidf = TfidfVectorizer(stop_words="english")

url = "https://drive.google.com/file/d/1xkKDLfYydan6g7G2du9mEX2PwJy8Kq-7/view?usp=share_link"
df = pd.read_csv(url)

df["description"] = df["description"].fillna("")

tfidf_matriz = tfidf.fit_transform(df["description"])
coseno_sim = linear_kernel(tfidf_matriz, tfidf_matriz)
indices = pd.Series(df.index, index=df["title"]).drop_duplicates()


def get_recom(title, coseno_sim=coseno_sim):
    idx = indices[title]

    # Obtenga la puntuacion de similitud de esa pelicula con todas las peliculas
    simil = list(enumerate(coseno_sim[idx]))

    # Ordenar las peliculas segun puntuacion
    simil = sorted(simil, key=lambda x: x[1], reverse=True)

    # Obtener las puntuaciones de las 10 primeras
    simil = simil[1:11]

    # Obtener los indices
    movie_index = [i[0] for i in simil]

    # Devuelve el top 10
    return df["title"].iloc[movie_index].to_list()[:5]


def main():
    st.title("Recomendacion de peliculas")
    # st.sidebar.header('User input parameters')
    # user_input = str(st.sidebar.text_input("Ingrese el title de la pelicula", 'the grand seduction'))
    # get_recom(user_input)
    lista = ["kadaram kondan", "the mystic river", "the grand seduction"]
    option = st.selectbox("Seleccione una pelicula", (lista))

    st.write("Tu seleccionaste:", option)
    st.write("Te recomendamos: ", get_recom(option))


if __name__ == "__main__":
    main()
