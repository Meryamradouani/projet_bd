import streamlit as st
import requests

def fetch_session_data():
<<<<<<< HEAD
    url = 'https://apex.oracle.com/pls/apex/fatima_zahra/seance/?limit=10000'
=======
    url = 'https://apex.oracle.com/pls/apex/salma10/seance/?limit=10000'
>>>>>>> a56eb95b8a339edb5eedde4c21a649ab1a591cfe
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        session_data = response.json()
        return session_data['items']

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')

def filter_and_display_sessions(session_data):
    st.title("Sessions disponibles")

    if not session_data:
        st.warning("Aucune donnée de séance disponible.")
        return

<<<<<<< HEAD
    actual_type_column_name = 'TYPE'
    actual_level_column_name = 'NIVEAU'
    actual_name_column_name = 'NOM'
=======
    actual_type_column_name = 'type'
    actual_level_column_name = 'niveau'
    actual_name_column_name = 'nom'
>>>>>>> a56eb95b8a339edb5eedde4c21a649ab1a591cfe

    # Filter by session type
    session_types = st.multiselect("Filtrer par type de séance", list(set(session[actual_type_column_name] for session in session_data)))

    # Filter by session level range
    level_range = st.slider("Sélectionner la plage de niveaux", min_value=1, max_value=3, value=(1, 3))

    # Apply filters
    filtered_sessions = [session for session in session_data
                         if (session[actual_level_column_name] >= level_range[0]) and
                            (session[actual_level_column_name] <= level_range[1]) and
                            (session[actual_type_column_name] in session_types)]

    # Display metrics
    st.metric("Nombre de séances disponibles", len(filtered_sessions))
    st.metric("Types de séances distincts", len(set(session[actual_type_column_name] for session in filtered_sessions)))

    # Display filtered session data without unwanted columns
    st.write("Informations sur les séances filtrées :")
    formatted_sessions = []
    for session in filtered_sessions:
        formatted_sessions.append({
            "numero de seance": session['ID_S'],
            "Nom de l'entraineur": session[actual_name_column_name],
            "Type de séance": session[actual_type_column_name],
            "Niveau": session[actual_level_column_name],
        })
    st.table(formatted_sessions)

def show_selected_sessions_schedule(session_data):
    selected_sessions = st.multiselect("Sélectionner des séances pour afficher les horaires", [session['ID_S'] for session in session_data])

    for session_id in selected_sessions:
        schedule_data = fetch_session_schedule(session_id)
        if schedule_data:
            st.write(f"Horaire pour la séance {session_id}:")
            st.table(schedule_data)
        else:
            st.warning(f"Aucun horaire disponible pour la séance {session_id}.")

def fetch_session_schedule(session_id):
    url = f'https://apex.oracle.com/pls/apex/salma10/horaire/?limit=10000&ssseance_id_s={session_id}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        schedule_data = response.json()
        
        # Modify the schedule data to exclude unwanted columns
        formatted_schedule = []
        for session_schedule in schedule_data['items']:
            formatted_schedule.append({
                "jour": session_schedule["jour"],
                "h_debut": session_schedule["h_debut"],
                "duree": session_schedule["duree"],
                "gymsalle": session_schedule["gymsalle"],
                "numero de seance": session_schedule["seance_id_s"],  # Change to the desired column name
            })
        return formatted_schedule

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')



def main():
    session_data = fetch_session_data()

    # Filter and display sessions
    filter_and_display_sessions(session_data)

    # Show schedules for selected sessions in an expander
    with st.expander("Afficher les horaires des séances sélectionnées"):
        show_selected_sessions_schedule(session_data)

if __name__ == "__main__":
    main()






















