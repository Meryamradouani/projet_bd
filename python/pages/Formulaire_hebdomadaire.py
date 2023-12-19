import streamlit as st
import requests
import json

def fetch_trainers():
    url = 'https://apex.oracle.com/pls/apex/salma10/entraineur/?limit=10000'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        trainers_data = response.json()
        return trainers_data['items']

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP pour récupérer les entraineurs : {e}')

def fetch_sessions():
    url = 'https://apex.oracle.com/pls/apex/salma10/seance/?limit=10000'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        sessions_data = response.json()
        return sessions_data['items']

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP pour récupérer les séances : {e}')

def fetch_session_schedule(session_id):
    url = f'https://apex.oracle.com/pls/apex/salma10/horaire/?limit=10000&seance_id_s={session_id}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        schedule_data = response.json()
        return schedule_data['items']

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')

def insert_session_schedule(data):
    url = 'https://apex.oracle.com/pls/apex/salma10/horaire/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        st.success('Insertion réussie!')
    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP pour insérer la séance : {e}')

def main():

    trainers = fetch_trainers()
    sessions = fetch_sessions()

<<<<<<< HEAD
    # Configuration du style
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
        "<h1 style='text-align: center; color: #ff69b4;'>Formulaire d'insertion de séance hebdomadaire</h1>",
=======

# Titre stylisé
    st.markdown(
        "<h1 style='text-align: center; '>Formulaire d'insertion de séance hebdomadaire</h1>",
>>>>>>> a56eb95b8a339edb5eedde4c21a649ab1a591cfe
        unsafe_allow_html=True
    )


    # Form inputs
    trainer_codee = st.selectbox("Sélectionner l'entraineur (CodeE)", [trainer['codee'] for trainer in trainers])
    session_id = st.selectbox("Sélectionner la séance (Id-S)", [session['id_s'] for session in sessions])
    day = st.selectbox("Sélectionner le jour de la semaine", ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI"])
    start_time = st.text_input("Heure de début")
    duration = st.text_input("Durée de la séance (en minutes ne dépasser pas 60 minutes)")
    gym_salle = st.text_input("Salle de gym")

    if st.button("Insérer la séance"):
        # Data to be inserted
        data = {
            "entraineur_codee": trainer_codee,
            "jour": day,
            "h_debut": start_time,
            "duree":  duration,
            "gymsalle": gym_salle,
            "seance_id_s": session_id,
        }

        # Perform validation and insertion
       
        insert_session_schedule(data)

if __name__ == "__main__":
    main()

