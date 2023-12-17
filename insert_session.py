# insert_session.py
import streamlit as st
import requests

def insert_session(session_data):
    url = 'https://apex.oracle.com/pls/apex/mery/seance/'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.post(url, headers=headers, json=session_data)
        response.raise_for_status()

        if response.status_code == 201:
            st.success('Nouvelle séance créée avec succès.')
        else:
            st.warning(f'La requête a réussi, mais le statut était {response.status_code}.')
            st.warning(response.text)

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')

def app():
    st.title("Insertion de Nouvelle Séance")

    # Ajout du style pour le formulaire
    st.markdown(
        """
        <style>
            body {
                background-color: #f5f5f5;
                font-family: 'Arial', sans-serif;
            }
            .stTextInput, .stNumberInput {
                width: 100%;
                padding: 10px;
                margin-bottom: 20px;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            .stButton {
                width: 100%;
                padding: 10px;
                background-color: #4caf50;
                color: black;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .stButton:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    session_id = st.text_input("ID de la séance", key="session_id")
    session_name = st.text_input("Nom de la séance", key="session_name")
    session_type = st.text_input("Type de la séance", key="session_type")
    session_level = st.number_input("Niveau de la séance (entre 1 et 4)", min_value=1, max_value=4, step=1, key="session_level")

    if st.button("Créer Séance"):
        if not all([session_id, session_name, session_type]):
            st.error("Veuillez remplir tous les champs.")
        elif not (1 <= session_level <= 4):
            st.error("Le niveau doit être un entier entre 1 et 4.")
        else:
            new_session_data = {
                "IdS": session_id,
                "Nom": session_name,
                "Type": session_type,
                "Niveau": session_level
            }
            insert_session(new_session_data)
