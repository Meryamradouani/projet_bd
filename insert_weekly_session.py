# insert_weekly_session.py

import streamlit as st
import requests
from datetime import datetime

# Fonction pour insérer une nouvelle séance hebdomadaire
def insert_weekly_session(weekly_session_data):
    url = 'https://apex.oracle.com/pls/apex/mery/horaire/'
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

# Fonction pour l'application de création de séance hebdomadaire
def app():
    st.title("Insertion de Nouvelle Séance Hebdomadaire")

    # Widgets pour saisir les données de la nouvelle séance hebdomadaire
    coach_code = st.selectbox("Code de l'entraîneur", ["101", "102", "103"])  # Remplacez par les vrais codes d'entraîneurs
    session_id = st.selectbox("ID de la séance", ["1", "2", "3"])  # Remplacez par les vrais ID de séances
    day_of_week = st.selectbox("Jour de la semaine", ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"])
    start_time = st.time_input("Heure de début")
    duration = st.number_input("Durée (en minutes)", min_value=1, max_value=60, step=1)
    gym_room = st.text_input("Salle de gym")

    if st.button("Créer Séance Hebdomadaire"):
        start_datetime = datetime.combine(datetime.today(), start_time)

        # Vérifications
        if not all([coach_code, session_id, day_of_week, start_time, duration, gym_room]):
            st.error("Veuillez remplir tous les champs.")
        elif duration > 60:
            st.error("La durée ne peut pas dépasser 60 minutes.")
        elif day_of_week not in ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]:
            st.error("Le jour de la semaine doit être compris entre le lundi et le vendredi.")
        else:
            # Données valides, procéder à l'insertion
            new_weekly_session_data = {
                "CodeE": coach_code,
                "IdS": session_id,
                "Jour": day_of_week,
                "HeureDebut": start_datetime.isoformat(),
                "Duree": duration,
                "GymSalle": gym_room
            }
            # Appel à la fonction d'insertion
            insert_weekly_session(new_weekly_session_data)
