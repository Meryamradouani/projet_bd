import streamlit as st
import requests

def fetch_trainers():
    url = 'https://apex.oracle.com/pls/apex/wksp_workspaceaya1/eeentraineur/?limit=10000'
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
    url = 'https://apex.oracle.com/pls/apex/wksp_workspaceaya1/ssseance/?limit=10000'
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
    url = f'https://apex.oracle.com/pls/apex/wksp_workspaceaya1/hhhoraire/?limit=10000&ssseance_id_s={session_id}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        schedule_data = response.json()
        return schedule_data['items']

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')

def insert_session_schedule(data):
    url = 'https://apex.oracle.com/pls/apex/wksp_workspaceaya1/hhhoraire/'
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
    st.title("Formulaire d'insertion de séance hebdomadaire")

    trainers = fetch_trainers()
    sessions = fetch_sessions()

    # Form inputs
    trainer_codee = st.selectbox("Sélectionner l'entraineur (CodeE)", [trainer['codee'] for trainer in trainers])
    session_id = st.selectbox("Sélectionner la séance (Id-S)", [session['id_s'] for session in sessions])
    day = st.selectbox("Sélectionner le jour de la semaine", ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI"])
    start_time = st.text_input("Heure de début")
    duration = st.slider("Durée de la séance (en minutes)", min_value=1, max_value=120, value=30)
    gym_salle = st.text_input("Salle de gym")

    if st.button("Insérer la séance"):
        # Data to be inserted
        data = {
            "codee": trainer_codee,
            "jour": day,
            "heure_de_debut": str(start_time),
            "duree":  f"{duration}min",
            "gymsalle": gym_salle,
            "ssseance_id_s": session_id,
        }

        # Perform validation and insertion
        if duration > 120:
            st.error("La durée de la séance ne peut pas dépasser 60 minutes.")
        elif day not in ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI"]:
            st.error("Le jour doit être compris entre le lundi et le vendredi.")
        else:
         
            insert_session_schedule(data)

if __name__ == "__main__":
    main()
