# coaches.py
import streamlit as st
import requests

def fetch_coaches():
    url = 'https://apex.oracle.com/pls/apex/mery/entraineur/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP
        data = response.json()

        if response.status_code == 200:
            # Affichage des données sous forme de tableau
            if data['items']:
                st.markdown("### Voici tous les entraîneurs :") 
                table_data = []

                # Ajouter les en-têtes du tableau
                table_data.append(['Nom', 'Prénom', 'Date de Naissance', 'Email', 'Numéro de téléphone'])

                # Ajouter les données de chaque entraîneur à la liste
                for item in data['items']:
                    table_data.append([item.get('nom'), item.get('prenom'), item.get('datenaissance'), item.get('email'), item.get('numerotelephone')])

                # Ajout du style au tableau
                st.markdown(
                    """
                    <style>
                        table {
                            width: 100%;
                            border-collapse: collapse;
                            margin: 1em 0;
                            font-size: 16px;
                        }
                        th, td {
                            padding: 10px;
                            text-align: left;
                            border-bottom: 1px solid #ddd;
                        }
                        th {
                            background-color: #f2f2f2;
                        }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                # Afficher le tableau dans Streamlit
                st.table(table_data)
            else:
                st.info("Aucune donnée disponible pour les entraîneurs.")

            st.success('Données des entraîneurs récupérées avec succès.')

        else:
            st.warning(f'La requête a réussi, mais le statut était {response.status_code}.')

    except requests.exceptions.RequestException as e:
        st.error(f'Erreur lors de la requête HTTP : {e}')

def app():
    st.title("Entraîneurs disponibles")

    # Utilisation de la fonction fetch_coaches pour récupérer les données de la table 'entraineur'
    fetch_coaches()

# Ajoutez d'autres fonctionnalités spécifiques à la page des entraîneurs si nécessaire
