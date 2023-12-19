import streamlit as st
import pandas as pd
from datetime import date

# Création d'exemples de dataframes avec des données d'entraîneurs
data1 = {
            "codee":[1] ,
            "nom":["Dupont"] ,
            "prenom":["Jean"] ,
            "date_de_naissance":["1990-05-15T00:00:00Z"] ,
            "email":["jean.dupont@email.com"] ,
            "numero_de_tele": [123456789],
            "links": [
                {
                    "rel": "self",
                    "href": "https://apex.oracle.com/pls/apex/salma10/entraineur/1"
                }
            ]
}

data2 = {
           "codee":[2] ,
            "nom": ["Martin"],
            "prenom": ["Sophie"],
            "date_de_naissance":["1985-08-22T00:00:00Z"] ,
            "email": [ "sophie.martin@email.com"],
            "numero_de_tele":[987654321] ,
            "links": [
                {
                    "rel": "self",
                    "href": "https://apex.oracle.com/pls/apex/salma10/entraineur/2"
                }
            ]
}

data3 = {
           "codee":[3] ,
            "nom": ["Lefevre"],
            "prenom":["Pierre"] ,
            "date_de_naissance":["1988-12-10T00:00:00Z"] ,
            "email":["pierre.lefevre@email.com"] ,
            "numero_de_tele":[654321987] ,
            "links": [
                {
                    "rel": "self",
                    "href": "https://apex.oracle.com/pls/apex/salma10/entraineur/3"
                }
            ]
}

data4 = {
            "codee":[4],
            "nom":["Rousseau"] ,
            "prenom": ["Marie"],
            "date_de_naissance": ["1995-04-03T00:00:00Z"] ,
            "email":["marie.rousseau@email.com"] ,
            "numero_de_tele":[111223344] ,
            "links": [
                {
                    "rel": "self",
                    "href": "https://apex.oracle.com/pls/apex/salma10/entraineur/4"
                }
            ]
}

data_lengths = [len(data1["codee"]), len(data2["codee"]), len(data3["codee"]), len(data4["codee"])]

if len(set(data_lengths)) != 1:
    raise ValueError("Les listes dans les dictionnaires doivent avoir la même longueur.")

# Ajout d'une colonne d'index
index_values = range(1, max(map(len, [data1["codee"], data2["codee"], data3["codee"], data4["codee"]])) + 1)
data1["Index"] = index_values
data2["Index"] = index_values
data3["Index"] = index_values
data4["Index"] = index_values

df1 = pd.DataFrame(data1).set_index("Index")
df1["date_de_naissance"] = pd.to_datetime(df1["date_de_naissance"]).dt.date

df2 = pd.DataFrame(data2).set_index("Index")
df2["date_de_naissance"] = pd.to_datetime(df2["date_de_naissance"]).dt.date

df3 = pd.DataFrame(data3).set_index("Index")
df3["date_de_naissance"] = pd.to_datetime(df3["date_de_naissance"]).dt.date

df4 = pd.DataFrame(data4).set_index("Index")
df4["date_de_naissance"] = pd.to_datetime(df4["date_de_naissance"]).dt.date

# Concaténer les dataframes
all_dataframes = [df1, df2, df3, df4]
df = pd.concat(all_dataframes)

# Interface utilisateur Streamlit
st.title("Entraîneurs Disponibles")

# Filtres
nom_famille_input = st.text_input("Filtrer par nom de famille :")

# Ajuster la valeur par défaut pour être dans la plage spécifiée
default_date_value = date(1995, 1, 1)
date_naissance_input = st.date_input(
    "Filtrer par date de naissance :",
    min_value=df["date_de_naissance"].min(),
    max_value=df["date_de_naissance"].max(),
    value=default_date_value,
)

# Convertir la date en chaîne
date_naissance_input_str = date_naissance_input.strftime("%Y-%m-%d")

# Filtrage des données
filtered_df = df[
    df["nom"].str.contains(nom_famille_input, case=False)
    & (df["date_de_naissance"] == date_naissance_input)
]

# Affichage des résultats sous forme de tableau
if not filtered_df.empty:
    st.subheader("Résultats filtrés :")
    st.table(filtered_df)
else:
    st.warning("Aucun résultat trouvé.")