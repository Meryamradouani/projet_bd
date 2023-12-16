# home.py
from PIL import Image
import streamlit as st

def app():
    st.title("Bienvenue dans notre application de gestion d'entraînement")

    # Présentation du projet en Markdown
    st.markdown("""
    Notre application a été créée pour simplifier la gestion des séances d'entraînement, des entraîneurs,
    et bien plus encore.

    ## Objectifs principaux du projet
    - Affichage et filtrage des séances disponibles.
    - Recherche et affichage des informations sur les entraîneurs.
    - Visualisation de graphiques sur les séances programmées.
    - Insertion de nouvelles séances via un formulaire.
    - Insertion de nouvelles séances hebdomadaires dans la table Horaire.
    """)

    # Charger l'image
    image = Image.open('WhatsApp Image 2023-12-15 at 23.05.48_e393b86e.jpg')  # Remplacez par le chemin de votre image

    # Redimensionner l'image
    new_size = (300, 300)  # Remplacez par la taille souhaitée (largeur, hauteur)
    resized_image = image.resize(new_size)

    # Afficher l'image redimensionnée
    st.image(resized_image, caption='salle de sport ', use_column_width=True)
