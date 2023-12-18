import streamlit as st
import requests

# Fonction pour vérifier la validité des données saisies
def check_input(id_s, nom, tyype, niveau):
    if not (id_s and nom and tyype and niveau):
        return False, "Veuillez remplir tous les champs du formulaire."
    
    if niveau < 1 or niveau > 4:
        return False, "Le niveau doit être un entier entre 1 et 4."

    return True, ""

# Fonction pour insérer une nouvelle séance dans la base de données
def inserer_seance(ID_S, NOM, TYPE, NIVEAU):
    url = 'https://apex.oracle.com/pls/apex/salma10/seance/?limit=10000'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    data = {
        "ID_S": ID_S,
        "NOM": NOM,
        "TYPE": TYPE,
        "NIVEAU": NIVEAU
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        seance_data = response.json()

        if "ID_S" in seance_data:
            st.success("Séance insérée avec succès!")
        else:
            st.error("Séance insérée avec succès!")
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de requête : {e}")

# Page principale de l'application Streamlit
def main():

    # Personnalisation du style
    st.markdown(
        """
        <style>
        body {
        
            background-color: #fdf6fa; /* Couleur de fond douce */
            font-family: 'Arial', sans-serif; /* Police élégante */
            color: #a64ac9; /* Couleur principale */
        }
        .stButton { /* Style du bouton */
            border-radius: 20px;
            background-color: #ffc0cb;
            color: #a64ac9;
            padding: 10px 20px;
        }
        .stTextInput, .stNumberInput { /* Style des champs de saisie */
            border-radius: 10px;
            border-color: #a64ac9;
            padding: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Titre stylisé
    st.markdown(
        "<h1 style='text-align: center; color: #ff69b4;'>Formulaire d'Insertion de Séance</h1>",
        unsafe_allow_html=True
    )

    # Formulaire de saisie pour la nouvelle séance
    ID_S = st.number_input("ID de la séance", min_value=1)
    NOM = st.text_input("Nom de la séance")
    TYPE = st.text_input("Type de la séance")
    NIVEAU = st.number_input("Niveau de la séance" )
    
    # Bouton pour l'insertion de la séance
    if st.button("Insérer la Séance"):
        # Vérification des champs
        is_valid, message = check_input(ID_S, NOM, TYPE, NIVEAU)
        if is_valid:
            # Appel de la fonction d'insertion
            inserer_seance(ID_S, NOM, TYPE, NIVEAU)
        else:
            st.warning(message)

# Exécution de l'application principale
if __name__== "__main__":
    main()