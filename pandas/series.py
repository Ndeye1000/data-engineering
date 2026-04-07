import pandas as pd

print("Exo 1 :\n")

fruits = ["Fraise","Pomme","Ananas","Banane"]

series = pd.Series(fruits, index=["a","b","c","d"])

series.iloc[1] = "Fruit de la passion"

print(series,"\n")
print(len(series) > 2,"\n")

print("Exo 2 :\n")

prix = {"Pomme" : 300, "Banane": 150}

series = pd.Series(prix)

series.loc["Banane"] += 50

print(series.loc["Pomme"] > 200)
