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
    st.title("Créer une nouvelle séance")

    # Widgets pour saisir les données de la nouvelle séance
    nom = st.text_input("Nom de la séance")
    type_seance = st.text_input("Type de séance")
    niveau = st.number_input("Niveau de la séance", min_value=1, max_value=10)
    
    if st.button("Créer Séance"):
        new_session_data = {
            "nom": nom,
            "type": type_seance,
            "niveau": niveau
        }

        insert_session(new_session_data)

# Ajoutez d'autres fonctionnalités spécifiques à la page d'insertion de séance si nécessaire
