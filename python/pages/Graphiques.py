import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# URL pour vos données d'entraîneurs et d'horaire
url_eeentraineur = 'https://apex.oracle.com/pls/apex/salma10/entraineur/'
url_hhhoraire = 'https://apex.oracle.com/pls/apex/salma10/horaire/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'  # Ajoutez votre User-Agent
}

# Récupération de vos données depuis les URLs
response_eeentraineur = requests.get(url_eeentraineur, headers=headers)
response_hhhoraire = requests.get(url_hhhoraire, headers=headers)

# Vérification que la requête a réussi avant de continuer
if response_eeentraineur.status_code == 200 and response_hhhoraire.status_code == 200:
    # Conversion des données JSON en DataFrames pandas
    df_eeentraineur = pd.DataFrame(response_eeentraineur.json()["items"])
    df_hhhoraire = pd.DataFrame(response_hhhoraire.json()["items"])

    # Vous pouvez procéder à votre traitement ou manipulation des données ici si nécessaire

    # Création des graphiques avec Plotly Express
    fig_bar = px.bar(df_hhhoraire, x="h_debut", title="Nombre de séances par plage horaire")
    fig_line = px.line(df_hhhoraire.groupby("jour").size().reset_index(name="nombre_seances"),
                       x="jour", y="nombre_seances", title="Nombre de séances par jour de la semaine")

    # Ordonner les jours de la semaine
    jours_ordre = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]
    fig_line.update_xaxes(categoryorder='array', categoryarray=jours_ordre)

    # Affichage des graphiques sur la page Streamlit
    st.title("Graphiques sur les séances programmées")
    st.plotly_chart(fig_bar)
    st.plotly_chart(fig_line)

    st.success("Les données ont été mises à jour avec succès.")
else:
    st.error("Échec de la récupération des données depuis les URLs.")