# home.py
from PIL import Image
import streamlit as st

def app():
    # Style CSS pour la mise en forme
    style = """
    <style>
        body {
            background-color: #f2f2f2;  /* Couleur de fond */
            font-family: 'Arial', sans-serif;  /* Police de caractères */
        }
        .container {
            max-width: 800px;  /* Largeur maximale du contenu */
            margin: auto;  /* Centrer le contenu */
            padding: 20px;  /* Espace intérieur */
            text-align: justify; /* Justification du texte */
        }
        img {
            max-width: 100%;  /* Image responsive */
            border-radius: 10px;  /* Coins arrondis pour l'image */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Ombre légère */
            margin-bottom: 20px;  /* Espace en bas de l'image */
        }
        h1 {
            color: #333;  /* Couleur du titre */
        }
        h2 {
            color: #333;  /* Couleur du sous-titre */
        }
        p {
            line-height: 1.5;  /* Hauteur de ligne agréable */
            color: #555;  /* Couleur du texte principal */
        }
    </style>
    """

    # Appliquer le style CSS
    st.markdown(style, unsafe_allow_html=True)

    # Présentation du projet en Markdown
    st.title("Bienvenue dans notre application de gestion d'entraînement")

    st.markdown("""
    Notre application a été créée pour simplifier la gestion des séances d'entraînement, des entraîneurs,
    et bien plus encore.
    """)

    # Charger l'image
    image = Image.open('WhatsApp Image 2023-12-15 at 23.05.48_e393b86e.jpg')  # Remplacez par le chemin de votre image

    # Redimensionner l'image
    new_size = (600, 400)  # Remplacez par la taille souhaitée (largeur, hauteur)
    resized_image = image.resize(new_size)

    # Afficher l'image redimensionnée
    st.image(resized_image, caption='Salle de sport', use_column_width=True)

    st.header("Objectifs principaux du projet")
    st.markdown("""
    - Affichage et filtrage des séances disponibles.
    - Recherche et affichage des informations sur les entraîneurs.
    - Visualisation de graphiques sur les séances programmées.
    - Insertion de nouvelles séances via un formulaire.
    - Insertion de nouvelles séances hebdomadaires dans la table Horaire.
    """)

# Exécutez l'application
if __name__ == "__main__":
    app()
