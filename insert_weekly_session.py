# insert_weekly_session.py

import streamlit as st
import requests
from datetime import datetime

def insert_weekly_session(weekly_session_data):
    url = 'https://apex.oracle.com/pls/apex/mery/horaire/?limit=10000'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.post(url, headers=headers, json=weekly_session_data)
        response.raise_for_status()

        if response.status_code == 201:
            st.success('Nouvelle séance hebdomadaire créée avec succès.')
        else:
            st.warning(f'La requête a réussi, mais le statut était {response.status_code}.')
            st.warning(response.text)

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')

def app():
    st.title("Créer une nouvelle séance hebdomadaire")

    # Widgets pour saisir les données de la nouvelle séance hebdomadaire
    coach_code = st.text_input("Code de l'entraîneur")
    session_id = st.text_input("ID de la séance")
    day_of_week = st.selectbox("Jour de la semaine", ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"])
    start_time = st.time_input("Heure de début")
    duration = st.number_input("Durée (en minutes)", min_value=1, max_value=60, step=1)
    gym_room = st.text_input("Salle de gym")

    if st.button("Créer Séance Hebdomadaire"):
        start_datetime = datetime.combine(datetime.today(), start_time)

        new_weekly_session_data = {
            "CODEE": coach_code,
            "IDS": session_id,
            "JOUR": day_of_week,
            "HEUREDEBUT": start_datetime.isoformat(),
            "DDUREE": duration,
            "GYMSALLE": gym_room
        }

        insert_weekly_session(new_weekly_session_data)

# Ajoutez d'autres fonctionnalités spécifiques à la page d'insertion de séance hebdomadaire si nécessaire
