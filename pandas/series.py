# import pandas as pd

# print("Exo 1 :\n")

# fruits = ["Fraise","Pomme","Ananas","Banane"]

# series = pd.Series(fruits, index=["a","b","c","d"])

# series.iloc[1] = "Fruit de la passion"

# print(series,"\n")
# print(len(series) > 2,"\n")

# print("Exo 2 :\n")

# prix = {"Pomme" : 300, "Banane": 150}

# series = pd.Series(prix)

# series.loc["Banane"] += 50

# print(series.loc["Pomme"] > 200)

import pandas as pd
import streamlit as st # type: ignore

st.title("Exercices Pandas 🐼")

# Exo 1
st.header("Exo 1 :")

st.write("Tableau contenant des fruits")

fruits = ["Fraise", "Pomme", "Ananas", "Banane"]
series = pd.Series(fruits, index=["a", "b", "c", "d"])
series.iloc[1] = "Fruit de la passion"

st.write(series)
st.write("Le tableau contient plus de 2 elements :", len(series) > 2)

# Exo 2
st.header("Exo 2 :")

prix = {"Pomme": 300, "Banane": 150}
series = pd.Series(prix)
series.loc["Banane"] += 50

st.write("Pomme > 200 FCFA :", series.loc["Pomme"] > 200)
st.write("Prix mis a jour")
st.write(series)
