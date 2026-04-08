import pandas as pd
import streamlit as st # type: ignore

st.title("Exercice Pandas 🐼")
st.header("Anime liste")

# dictionnaire 

data = {
    "Anime-nom" : ["Tokyo Revengers", "Hunter X Hunter", "Demon Slayer"],
    "Nombre d'episode" : [62, 148, 60],
    "Date de fin" : ["A venir", "A venir", "A venir"]
}

# creation dataFrame

df = pd.DataFrame(data, index=["A-1","A-2","A-3"]) 

# Ajout de 2 colonnes en plus

new_rows = {"Anime-nom" : ["Gachiakuta", "Oshi No Ko"], "Nombre d'episode" : [25, 48], "Date de fin" : ["A venir", "A venir"]}

df_update = pd.DataFrame(new_rows, index=["A-4", "A-5"])

df = pd.concat([df, df_update]) # Concatenation

st.write(df)